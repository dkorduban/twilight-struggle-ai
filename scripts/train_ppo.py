#!/usr/bin/env python3
"""PPO fine-tuning of BC checkpoint for Twilight Struggle AI.

Warms up from a BC checkpoint and runs PPO via league self-play.
Uses batched C++ rollout collection and PyTorch for updates.

Factorized log π(a|s) = log π_card(c|s) + log π_mode(m|s,c) + Σ log π_country(t_i|s,c,m)
Each head receives the same advantage signal (standard factorized PG).

Usage:
    uv run python scripts/train_ppo.py \\
        --checkpoint data/checkpoints/v106_cf_gnn_s42/baseline_best.pt \\
        --out-dir data/checkpoints/ppo_v1 \\
        --n-iterations 200 --games-per-iter 200 --seed 99000
"""
from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import math
import os
import random
import shutil
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Tracking imports (optional — never crash training if unavailable)
# ---------------------------------------------------------------------------
try:
    from tsrl.checkpoint_db import log_checkpoint as _log_checkpoint
    from tsrl.experiment_log import (
        log_experiment_start as _log_exp_start,
        log_experiment_end as _log_exp_end,
    )
    from tsrl.smoke_test import run_smoke_test as _run_smoke_test
    _TRACKING_AVAILABLE = True
except ImportError:
    _TRACKING_AVAILABLE = False

import torch
import torch.nn as nn
import torch.nn.functional as F

# Bindings
_repo_root = Path(__file__).resolve().parent.parent
for _bindings_path in (
    _repo_root / "build-ninja" / "bindings",  # preferred (ninja build)
    _repo_root / "build" / "bindings",
):
    # Check for actual .so file, not just directory existence (empty dir would break path).
    # Always break on first match so old build/ doesn't shadow build-ninja/ on PYTHONPATH.
    _bindings_dir = str(_bindings_path)
    if any(_bindings_path.glob("tscore*.so")):
        if _bindings_dir not in sys.path:
            sys.path.insert(0, _bindings_dir)
        break
_py_dir = str(Path(__file__).resolve().parent.parent / "python")
if _py_dir not in sys.path:
    sys.path.insert(0, _py_dir)

if not _TRACKING_AVAILABLE:
    try:
        from tsrl.checkpoint_db import log_checkpoint as _log_checkpoint
        from tsrl.experiment_log import (
            log_experiment_start as _log_exp_start,
            log_experiment_end as _log_exp_end,
        )
        from tsrl.smoke_test import run_smoke_test as _run_smoke_test
        _TRACKING_AVAILABLE = True
    except ImportError:
        _TRACKING_AVAILABLE = False

import tscore  # noqa: E402
from tsrl.constants import (
    MODEL_REGISTRY,
    NUM_CARDS,
    NUM_COUNTRIES,
    SCALAR_DIM,
)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------


def _load_country_region_map() -> dict[int, str]:
    """Load country_id -> region string from data/spec/countries.csv."""
    import csv as _csv

    csv_path = Path(__file__).parent.parent / "data" / "spec" / "countries.csv"
    mapping: dict[int, str] = {}
    try:
        with open(csv_path) as f:
            for row in _csv.DictReader(r for r in f if not r.startswith("#")):
                mapping[int(row["country_id"])] = row["region"]
    except Exception:
        pass
    return mapping


def _load_country_meta() -> tuple[dict[int, int], dict[int, float]]:
    """Load stability and BG weight per country_id from data/spec/countries.csv.

    BG weight: 1.0 for battlegrounds, 0.2 for non-battlegrounds.
    Returns (stability_map, bg_weight_map).
    """
    import csv as _csv

    csv_path = Path(__file__).parent.parent / "data" / "spec" / "countries.csv"
    stability_map: dict[int, int] = {}
    bg_weight_map: dict[int, float] = {}
    try:
        with open(csv_path) as f:
            for row in _csv.DictReader(r for r in f if not r.startswith("#")):
                cid = int(row["country_id"])
                stability_map[cid] = int(row["stability"])
                bg_weight_map[cid] = 1.0 if row["is_battleground"].strip().lower() == "true" else 0.2
    except Exception:
        pass
    return stability_map, bg_weight_map


_REGION_NAMES = [
    "Europe",
    "Asia",
    "MiddleEast",
    "Africa",
    "CentralAmerica",
    "SouthAmerica",
    "SoutheastAsia",
]
_REGION_KEY = {
    "Europe": "europe",
    "Asia": "asia",
    "MiddleEast": "middle_east",
    "Africa": "africa",
    "CentralAmerica": "central_america",
    "SouthAmerica": "south_america",
    "SoutheastAsia": "southeast_asia",
}
_COUNTRY_REGION: dict[int, str] = _load_country_region_map()
_COUNTRY_STABILITY: dict[int, int]
_COUNTRY_BG_WEIGHT: dict[int, float]
_COUNTRY_STABILITY, _COUNTRY_BG_WEIGHT = _load_country_meta()
_REGION_COUNTRY_IDS: dict[str, tuple[int, ...]] = {
    region: tuple(
        country_id
        for country_id, country_region in sorted(_COUNTRY_REGION.items())
        if country_region == region
    )
    for region in _REGION_NAMES
}
# SE Asia is a scoring subset of Asia — include SEA countries in the Asia bucket too.
_REGION_COUNTRY_IDS["Asia"] = tuple(sorted(
    set(_REGION_COUNTRY_IDS["Asia"]) | set(_REGION_COUNTRY_IDS["SoutheastAsia"])
))

CARD_SLOTS = NUM_CARDS
COUNTRY_SLOTS = NUM_COUNTRIES

# DEFCON-lowering cards (kept in sync with C++ learned_policy.cpp / mcts_batched.cpp)
# Mirror of cpp/tscore/card_properties.hpp kDefconLoweringCards.
# Keep in sync if that header changes.
DEFCON_LOWERING_CARDS = frozenset({
    4, 11, 13, 20, 24, 39, 48, 49, 50, 52, 53, 68, 83, 92, 105,
})

# Action mode indices
MODE_INFLUENCE = 0
MODE_COUP = 1
MODE_REALIGN = 2
MODE_SPACE = 3
MODE_EVENT = 4

# Valid country IDs: all IDs in 0..85 except 64 (which has no entry in countries.csv).
# IDs not in this set have no country spec and throw IndexError in play_callback_matchup.
VALID_COUNTRY_IDS: frozenset[int] = frozenset(set(range(COUNTRY_SLOTS)) - {64})
# Boolean mask tensor (CPU, device-agnostic) — True = valid country slot
_VALID_COUNTRY_MASK_CPU: torch.Tensor = torch.zeros(COUNTRY_SLOTS, dtype=torch.bool)
for _cid in VALID_COUNTRY_IDS:
    _VALID_COUNTRY_MASK_CPU[_cid] = True


# ---------------------------------------------------------------------------
# Feature extraction from C++ state dict
# ---------------------------------------------------------------------------

def _card_mask(card_ids: list[int] | set[int]) -> list[float]:
    mask = [0.0] * CARD_SLOTS
    for cid in card_ids:
        if 0 < cid < CARD_SLOTS:
            mask[cid] = 1.0
    return mask


def extract_features(
    state: dict,
    hand: list[int],
    holds_china: bool,
    side_int: int,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    """Build (influence, cards, scalars) CPU tensors of shape (1, D).

    Matches C++ nn_features.cpp exactly.
    """
    ussr_inf = state["ussr_influence"]
    us_inf = state["us_influence"]
    influence = [float(x) for x in ussr_inf] + [float(x) for x in us_inf]

    hand_mask = _card_mask(hand)
    discard_mask = _card_mask(state["discard"])
    removed_mask = _card_mask(state["removed"])
    cards = hand_mask + hand_mask + discard_mask + removed_mask

    scalars = [
        state["vp"] / 20.0,
        (state["defcon"] - 1) / 4.0,
        state["milops"][0] / 6.0,
        state["milops"][1] / 6.0,
        state["space"][0] / 9.0,
        state["space"][1] / 9.0,
        float(state["china_held_by"]),
        float(holds_china),
        state["turn"] / 10.0,
        state["ar"] / 8.0,
        float(side_int),
    ]
    return (
        torch.tensor([influence], dtype=torch.float32),
        torch.tensor([cards], dtype=torch.float32),
        torch.tensor([scalars], dtype=torch.float32),
    )


# ---------------------------------------------------------------------------
# Step: one decision point in a rollout
# ---------------------------------------------------------------------------

@dataclass
class Step:
    influence: torch.Tensor      # (1, 172) CPU
    cards: torch.Tensor          # (1, 448) CPU
    scalars: torch.Tensor        # (1, SCALAR_DIM) CPU — 32-dim base + 28 region = 60 for GNN-side
    card_mask: torch.Tensor      # (111,) bool - True = legal
    mode_mask: torch.Tensor      # (5,) bool
    country_mask: Optional[torch.Tensor]  # (86,) bool or None for SPACE/EVENT
    card_idx: int                # 0-indexed (card_id - 1)
    mode_idx: int                # 0..4
    country_targets: list[int]   # 0-indexed country IDs, with repeats for multi-ops
    old_log_prob: float
    value: float
    side_int: int = 0            # 0=USSR, 1=US (for per-side advantage normalization)
    reward: float = 0.0
    done: bool = False
    advantage: float = 0.0
    returns: float = 0.0         # GAE return target (filled after rollout by _compute_gae_per_side)
    # Raw game state for future re-encoding (added 2026-04-07).
    # All fields are None when the step was not collected via rollout_self_play_batched.
    raw_ussr_influence: Optional[list] = None  # list of 86 int16 values
    raw_us_influence: Optional[list] = None    # list of 86 int16 values
    raw_turn: Optional[int] = None
    raw_ar: Optional[int] = None
    raw_defcon: Optional[int] = None
    raw_vp: Optional[int] = None
    raw_milops: Optional[list] = None    # [USSR, US]
    raw_space: Optional[list] = None     # [USSR, US]
    hand_card_ids: Optional[list] = None  # 1-indexed card IDs in deciding side's hand
    # Policy logits for KL-distillation in arch sweep (added 2026-04-08).
    # Stored as plain Python lists (CPU) to avoid holding GPU tensors across iterations.
    # None when collected via C++ batched rollout (logits not returned by tscore).
    card_logits: Optional[list] = None    # (111,) raw pre-mask logits
    mode_logits: Optional[list] = None    # (5,) raw pre-mask logits
    country_logits: Optional[list] = None # (86,) probability mixture from model
    # SmallChoice event decision captured during rollout (Phase 1e).
    small_choice_target: int = -1         # -1 means no decision this step
    small_choice_n_options: int = 0       # number of legal options
    small_choice_logprob: float = 0.0     # log-prob of chosen option under rollout policy


# ---------------------------------------------------------------------------
# Model loading
# ---------------------------------------------------------------------------

def load_model(checkpoint_path: str, device: str = "cuda") -> nn.Module:
    """Load a checkpoint and return the model in training mode on device."""
    from tsrl.policies.model import TSBaselineModel, TSControlFeatGNNModel

    ckpt = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
    state_dict = ckpt.get("model_state_dict", ckpt)
    args = ckpt.get("args", {})
    hidden_dim = args.get("hidden_dim", 256)
    model_type = args.get("model_type", "baseline")
    dropout = args.get("dropout", 0.1)
    num_strategies = args.get("num_strategies", 4)

    cls = MODEL_REGISTRY.get(model_type, TSBaselineModel)
    if cls in (TSControlFeatGNNModel,) and num_strategies != 4:
        model = cls(hidden_dim=hidden_dim, dropout=dropout, num_strategies=num_strategies)
    else:
        model = cls(hidden_dim=hidden_dim, dropout=dropout)
    # Load compatible weights; for size-mismatched keys (e.g. scalar_encoder after
    # region scalar dim expansion) copy the old columns and leave new cols at init values.
    model_state = model.state_dict()
    filtered = {}
    for k, v in state_dict.items():
        if k not in model_state:
            continue
        if v.shape == model_state[k].shape:
            filtered[k] = v
        elif v.dim() == 2 and model_state[k].dim() == 2 and v.shape[0] == model_state[k].shape[0]:
            # Weight matrix: old has fewer input cols — copy old cols, keep new cols at init
            new_w = model_state[k].clone()
            old_cols = v.shape[1]
            new_w[:, :old_cols] = v
            filtered[k] = new_w
            print(f"  [load_model] partial warm-start {k}: {v.shape} → {model_state[k].shape}", flush=True)
        else:
            print(f"  [load_model] skipped incompatible {k}: {v.shape} vs {model_state[k].shape}", flush=True)
    model.load_state_dict(filtered, strict=False)
    model.train()
    model.to(device)
    return model, model_type, args


# ---------------------------------------------------------------------------
# Action log-prob computation
# ---------------------------------------------------------------------------

def _compute_log_prob(
    card_logits: torch.Tensor,    # (111,) on device
    mode_logits: torch.Tensor,    # (5,) on device
    country_logits: torch.Tensor, # (86,) on device, mixed probs ∈ [0,1]
    card_mask: torch.Tensor,      # (111,) bool on device
    mode_mask: torch.Tensor,      # (5,) bool on device
    country_mask: Optional[torch.Tensor],  # (86,) bool on device or None
    card_idx: int,
    mode_idx: int,
    country_targets: list[int],
) -> torch.Tensor:
    """Compute log π(a|s) = log π_card + log π_mode + Σ log π_country.

    Returns a scalar tensor (with grad).
    """
    # Card log-prob
    masked_card = card_logits.clone()
    masked_card[~card_mask] = float("-inf")
    log_prob_card = F.log_softmax(masked_card, dim=0)[card_idx]

    # Mode log-prob
    masked_mode = mode_logits.clone()
    masked_mode[~mode_mask] = float("-inf")
    log_prob_mode = F.log_softmax(masked_mode, dim=0)[mode_idx]

    # Country log-prob (for INFLUENCE/COUP/REALIGN)
    log_prob_country = torch.tensor(0.0, device=card_logits.device)
    if country_targets and country_mask is not None:
        # country_logits is a probability mixture from the model (sums to ~1).
        # Mask illegal countries, renormalize, then compute log.
        probs = country_logits.clone()
        probs[~country_mask] = 0.0
        probs = probs / (probs.sum() + 1e-10)
        # log_prob for each target (with repeats for multi-ops influence)
        for c in country_targets:
            log_prob_country = log_prob_country + torch.log(probs[c] + 1e-10)

    return log_prob_card + log_prob_mode + log_prob_country


# ---------------------------------------------------------------------------
# Rollout: collect steps for one game
# ---------------------------------------------------------------------------

def _sample_action_and_step(
    model: nn.Module,
    state: dict,
    hand: list[int],
    holds_china: bool,
    side_int: int,
    device: str,
    card_specs: dict,
    explore_alpha: float = 0.0,
    explore_eps: float = 0.0,
) -> tuple[dict, Step]:
    """Run model inference, sample action, return (action_dict, Step)."""
    if not hand:
        return None, None

    influence, cards, scalars = extract_features(state, hand, holds_china, side_int)
    inf_d = influence.to(device)
    cards_d = cards.to(device)
    scalars_d = scalars.to(device)

    model.eval()
    with torch.no_grad():
        outputs = model(inf_d, cards_d, scalars_d)

    card_logits = outputs["card_logits"][0]       # (111,)
    mode_logits = outputs["mode_logits"][0]       # (5,)
    country_logits = outputs.get("country_logits")
    if country_logits is not None:
        country_logits = country_logits[0]        # (86,)
    marginal_logits = outputs.get("marginal_logits")
    if marginal_logits is not None:
        marginal_logits = marginal_logits[0]      # (86, T_MAX)
    value = float(outputs["value"][0, 0].item())

    defcon = state["defcon"]
    ar = state["ar"]

    # ── Card mask with DEFCON safety ────────────────────────────────────────
    from tsrl.schemas import Side as PySide
    side_enum = PySide(side_int)
    card_mask = torch.zeros(111, dtype=torch.bool, device=device)
    for card_id in hand:
        idx = card_id - 1
        if idx < 0 or idx >= 111:
            continue
        if card_id in DEFCON_LOWERING_CARDS:
            spec = card_specs.get(card_id)
            if spec is not None:
                is_opp = spec.side != side_enum and spec.side != PySide.NEUTRAL
                is_neutral = spec.side == PySide.NEUTRAL
                if is_opp and defcon <= 2:
                    continue
                if is_opp and defcon == 3 and ar == 0:
                    continue
                if is_neutral and ar == 0 and defcon <= 3:
                    continue
        card_mask[idx] = True

    # Fallback: if all cards masked, allow all hand cards
    if not card_mask.any():
        for card_id in hand:
            idx = card_id - 1
            if 0 <= idx < 111:
                card_mask[idx] = True

    if not card_mask.any():
        return None, None

    # Sample card from masked distribution (with optional Dirichlet exploration noise)
    masked_card_logits = card_logits.clone()
    masked_card_logits[~card_mask] = float("-inf")
    card_probs = torch.softmax(masked_card_logits, dim=0)
    if explore_alpha > 0.0 and explore_eps > 0.0:
        n_legal = int(card_mask.sum().item())
        if n_legal > 1:
            concentration = torch.full((n_legal,), explore_alpha, device=device)
            noise = torch._standard_gamma(concentration)
            noise = noise / (noise.sum() + 1e-10)
            noise_full = torch.zeros(111, device=device)
            noise_full[card_mask] = noise
            card_probs = (1.0 - explore_eps) * card_probs + explore_eps * noise_full
    card_idx = int(torch.multinomial(card_probs, 1).item())
    card_id = card_idx + 1

    # ── Mode mask ───────────────────────────────────────────────────────────
    # All 5 modes start as potentially legal; apply DEFCON safety overrides.
    # We don't have full legal_modes() here, so use the model's distribution
    # with DEFCON safety constraints. The model strongly prefers legal modes.
    mode_mask = torch.ones(5, dtype=torch.bool, device=device)

    # DEFCON safety: no coup at DEFCON <= 2
    # Exception: US with Nuclear Subs active — coups don't lower DEFCON (mirrors C++ game_loop.cpp:238)
    nuclear_subs_safe = (side_int == 1 and bool(state.get("nuclear_subs_active", False)))
    if defcon <= 2 and not nuclear_subs_safe:
        mode_mask[MODE_COUP] = False

    # DEFCON safety: no event for DEFCON-lowering cards at DEFCON <= 2
    # Exceptions: cards whose events cannot reach DEFCON 1 even when played as event.
    #   #49 How I Learned to Stop Worrying: phasing player sets DEFCON to 2-5 (min=2, never 1)
    #   #48 Summit: winner chooses +1/-1; a rational model never chooses -1 at DEFCON 2
    DEFCON2_EVENT_SAFE = {49, 48}
    if defcon <= 2 and card_id in DEFCON_LOWERING_CARDS and card_id not in DEFCON2_EVENT_SAFE:
        mode_mask[MODE_EVENT] = False

    # Sample mode from masked distribution
    masked_mode_logits = mode_logits.clone()
    masked_mode_logits[~mode_mask] = float("-inf")
    mode_probs = torch.softmax(masked_mode_logits, dim=0)
    mode_idx = int(torch.multinomial(mode_probs, 1).item())
    mode = mode_idx

    # ── SPACE / EVENT: no targets ────────────────────────────────────────────
    if mode in (MODE_SPACE, MODE_EVENT):
        log_prob = _compute_log_prob(
            card_logits, mode_logits,
            country_logits if country_logits is not None else torch.zeros(86, device=device),
            card_mask, mode_mask,
            None, card_idx, mode_idx, [],
        )
        step = Step(
            influence=influence, cards=cards, scalars=scalars,
            card_mask=card_mask.cpu(), mode_mask=mode_mask.cpu(),
            country_mask=None,
            card_idx=card_idx, mode_idx=mode_idx, country_targets=[],
            old_log_prob=float(log_prob.item()), value=value, side_int=side_int,
            card_logits=card_logits.cpu().tolist(),
            mode_logits=mode_logits.cpu().tolist(),
            country_logits=(country_logits.cpu().tolist() if country_logits is not None else None),
        )
        return {"card_id": card_id, "mode": mode, "targets": []}, step

    # ── Country selection (INFLUENCE / COUP / REALIGN) ──────────────────────
    if country_logits is None:
        country_logits = torch.zeros(COUNTRY_SLOTS, device=device)

    # Build legal country mask (all non-zero-stability countries, simplified).
    # Exact legality computed by C++ engine; this mask just enables gradient flow.
    # Use all countries as potentially legal (C++ enforces actual legality).
    country_mask = torch.ones(COUNTRY_SLOTS, dtype=torch.bool, device=device)

    # Mask to accessible: probs = 0 for countries with both influence = 0
    # and no adjacency. For now, use all countries; C++ will re-validate.
    # NOTE: using all countries inflates entropy but allows gradient flow.
    # In practice the model already puts near-zero mass on illegal targets.

    # Restrict to valid country IDs only (invalid IDs have no C++ country spec
    # and throw IndexError when passed to play_callback_matchup).
    valid_mask = _VALID_COUNTRY_MASK_CPU.to(device)
    country_mask = country_mask & valid_mask

    country_probs = country_logits.clone()
    country_probs[~country_mask] = 0.0
    country_probs = country_probs / (country_probs.sum() + 1e-10)

    country_targets: list[int] = []

    if mode in (MODE_COUP, MODE_REALIGN):
        # Single country sample
        target = int(torch.multinomial(country_probs, 1).item())
        country_targets = [target]
    else:
        # INFLUENCE: DP allocation when marginal_logits available, else proportional
        spec = card_specs.get(card_id)
        ops = max(1, getattr(spec, "ops", 1) or 1) if spec else 1
        if marginal_logits is not None:
            from tsrl.policies.dp_decoder import dp_decode_allocation
            budget_t = torch.tensor([ops], dtype=torch.long, device=device)
            alloc_t = dp_decode_allocation(
                marginal_logits.unsqueeze(0),   # (1, 86, T_MAX)
                budget_t,
                country_mask.unsqueeze(0),      # (1, 86)
            )
            floor_alloc = alloc_t[0]            # (86,) int
        else:
            alloc = country_probs * ops
            floor_alloc = torch.floor(alloc).long()
            remainder = ops - int(floor_alloc.sum().item())
            if remainder > 0:
                fractional = alloc - floor_alloc.float()
                _, top_idx = fractional.topk(min(remainder, len(fractional)))
                for i in top_idx:
                    floor_alloc[i] += 1
        for cid in range(COUNTRY_SLOTS):
            country_targets.extend([cid] * int(floor_alloc[cid].item()))

    # Compute log_prob
    log_prob = _compute_log_prob(
        card_logits, mode_logits, country_logits,
        card_mask, mode_mask, country_mask,
        card_idx, mode_idx, country_targets,
    )

    step = Step(
        influence=influence, cards=cards, scalars=scalars,
        card_mask=card_mask.cpu(), mode_mask=mode_mask.cpu(),
        country_mask=country_mask.cpu(),
        card_idx=card_idx, mode_idx=mode_idx, country_targets=country_targets,
        old_log_prob=float(log_prob.item()), value=value, side_int=side_int,
        card_logits=card_logits.cpu().tolist(),
        mode_logits=mode_logits.cpu().tolist(),
        country_logits=country_logits.cpu().tolist(),
    )
    return {"card_id": card_id, "mode": mode, "targets": country_targets}, step


# ---------------------------------------------------------------------------
# Reward computation
# ---------------------------------------------------------------------------

def _compute_reward(
    result: "tscore.GameResult",
    side_int: int,
    vp_coef: float = 0.0,
    reward_shaping: bool = False,
    reward_alpha: float = 0.5,
) -> float:
    """Terminal reward. side_int 0=USSR, 1=US. Optional VP-magnitude component.

    VP shaping uses the pre-transfer VP for Wargames (card 103 gives +6 to opponent
    before checking winner, so final_vp understates the actual margin) and uses
    max-margin for Europe control (instant win regardless of VP board).

    When reward_shaping=True, uses compute_shaped_reward() from tsrl.rewards for
    VP trajectory + turn length bonuses on top of the base win/loss reward.
    """
    is_ussr = side_int == 0
    won = result.winner == (tscore.Side.USSR if is_ussr else tscore.Side.US)
    end_reason = getattr(result, "end_reason", "")

    # DEFCON-1 suicide penalty: extra signal beyond -1.0 normal loss.
    if end_reason == "defcon1" and not won:
        return -1.2

    if reward_shaping:
        from tsrl.rewards import compute_shaped_reward
        winner_int = None
        if result.winner == tscore.Side.USSR:
            winner_int = 0
        elif result.winner == tscore.Side.US:
            winner_int = 1
        return compute_shaped_reward(
            winner=winner_int,
            side=side_int,
            final_vp=result.final_vp,
            end_turn=getattr(result, "end_turn", 10),
            end_reason=end_reason,
            alpha=reward_alpha,
        )

    base = 1.0 if won else -1.0
    if vp_coef <= 0.0:
        return base
    if end_reason == "europe_control":
        vp_scaled = 1.0 if won else -1.0
    elif end_reason == "wargames":
        pre_vp = result.final_vp + (6 if result.final_vp > 0 else -6)
        vp_scaled = max(-1.0, min(1.0, pre_vp / 20.0))
        if not is_ussr:
            vp_scaled = -vp_scaled
    else:
        vp_scaled = max(-1.0, min(1.0, result.final_vp / 20.0))
        if not is_ussr:
            vp_scaled = -vp_scaled
    return (1.0 - vp_coef) * base + vp_coef * vp_scaled


# ---------------------------------------------------------------------------
# Rollout: collect N games
# ---------------------------------------------------------------------------

def collect_rollout_sequential(
    model: nn.Module,
    n_games: int,
    learned_side: tscore.Side,
    base_seed: int,
    device: str,
    card_specs: dict,
    vp_reward_coef: float = 0.0,
    reward_shaping: bool = False,
    reward_alpha: float = 0.5,
) -> list[Step]:
    """Play n_games and return all collected steps with rewards assigned."""
    all_steps: list[Step] = []
    side_int = 0 if learned_side == tscore.Side.USSR else 1

    for game_i in range(n_games):
        game_steps: list[Step] = []

        def make_callback(steps_list: list[Step]):
            def callback(state: dict, hand: list[int], holds_china: bool, si: int) -> dict | None:
                action_dict, step = _sample_action_and_step(
                    model, state, hand, holds_china, si, device, card_specs
                )
                if step is not None:
                    steps_list.append(step)
                return action_dict
            return callback

        results = tscore.play_callback_matchup(
            make_callback(game_steps),
            learned_side,
            tscore.PolicyKind.MinimalHybrid,
            1,
            seed=base_seed + game_i,
        )

        if not results or not game_steps:
            continue

        result = results[0]
        side_int = 0 if learned_side == tscore.Side.USSR else 1
        reward = _compute_reward(result, side_int, vp_reward_coef, reward_shaping=reward_shaping, reward_alpha=reward_alpha)

        if game_steps:
            game_steps[-1].reward = reward
            game_steps[-1].done = True

        all_steps.extend(game_steps)

    return all_steps


def _recompute_log_probs_and_values(
    steps: list[Step],
    model: nn.Module,
    device: str,
    batch_size: int = 2048,
) -> None:
    """Fallback utility to recompute old_log_prob and value from the PyTorch model."""
    if not steps:
        return
    model.eval()
    with torch.no_grad():
        for start in range(0, len(steps), batch_size):
            batch = steps[start:start + batch_size]
            inf_b = torch.cat([s.influence for s in batch], dim=0).to(device)
            cards_b = torch.cat([s.cards for s in batch], dim=0).to(device)
            scalars_b = torch.cat([s.scalars for s in batch], dim=0).to(device)
            outputs = model(inf_b, cards_b, scalars_b)
            card_logits_b = outputs["card_logits"]
            mode_logits_b = outputs["mode_logits"]
            country_logits_b = outputs.get("country_logits")
            values_b = outputs["value"]
            for i, step in enumerate(batch):
                lp = _compute_log_prob(
                    card_logits_b[i],
                    mode_logits_b[i],
                    country_logits_b[i] if country_logits_b is not None else torch.zeros(COUNTRY_SLOTS, device=device),
                    step.card_mask.to(device),
                    step.mode_mask.to(device),
                    step.country_mask.to(device) if step.country_mask is not None else None,
                    step.card_idx,
                    step.mode_idx,
                    step.country_targets,
                )
                step.old_log_prob = float(lp.item())
                step.value = float(values_b[i, 0].item())
    model.train()


def collect_rollout_batched(
    model: nn.Module,
    n_games: int,
    learned_side: tscore.Side,
    base_seed: int,
    device: str,
    card_specs: dict,
    vp_reward_coef: float = 0.0,
    rollout_temp: float = 1.0,
    reward_shaping: bool = False,
    reward_alpha: float = 0.5,
) -> list[Step]:
    """Collect PPO rollout steps through the native batched C++ game pool."""
    if not hasattr(tscore, "rollout_games_batched"):
        return collect_rollout_sequential(
            model, n_games, learned_side, base_seed, device, card_specs
        )

    script_path = _export_temp_model(model)
    try:
        results, steps, boundaries = tscore.rollout_games_batched(
            model_path=script_path,
            learned_side=learned_side,
            n_games=n_games,
            pool_size=min(n_games, 64),
            seed=base_seed,
            device="cpu",
            temperature=rollout_temp,
            nash_temperatures=True,
        )
    finally:
        try:
            os.remove(script_path)
        except OSError:
            pass

    all_steps: list[Step] = []
    for s in steps:
        country_mask = torch.from_numpy(s["country_mask"])
        step = Step(
            influence=torch.from_numpy(s["influence"]).unsqueeze(0),
            cards=torch.from_numpy(s["cards"]).unsqueeze(0),
            scalars=torch.from_numpy(s["scalars"]).unsqueeze(0),
            card_mask=torch.from_numpy(s["card_mask"]),
            mode_mask=torch.from_numpy(s["mode_mask"]),
            country_mask=country_mask if bool(country_mask.any()) else None,
            card_idx=s["card_idx"],
            mode_idx=s["mode_idx"],
            country_targets=list(s["country_targets"]),
            old_log_prob=float(s["log_prob"]),
            value=float(s["value"]),
            side_int=int(s["side_int"]),
            raw_ussr_influence=s["raw_ussr_influence"].tolist() if "raw_ussr_influence" in s else None,
            raw_us_influence=s["raw_us_influence"].tolist() if "raw_us_influence" in s else None,
            raw_turn=int(s["raw_turn"]) if "raw_turn" in s else None,
            raw_ar=int(s["raw_ar"]) if "raw_ar" in s else None,
            raw_defcon=int(s["raw_defcon"]) if "raw_defcon" in s else None,
            raw_vp=int(s["raw_vp"]) if "raw_vp" in s else None,
            raw_milops=list(s["raw_milops"]) if "raw_milops" in s else None,
            raw_space=list(s["raw_space"]) if "raw_space" in s else None,
            hand_card_ids=list(s["hand_card_ids"]) if "hand_card_ids" in s else None,
            small_choice_target=int(s["small_choice_target"]) if "small_choice_target" in s else -1,
            small_choice_n_options=int(s["small_choice_n_options"]) if "small_choice_n_options" in s else 0,
            small_choice_logprob=float(s["small_choice_logprob"]) if "small_choice_logprob" in s else 0.0,
        )
        all_steps.append(step)

    side_int = 0 if learned_side == tscore.Side.USSR else 1
    for i, result in enumerate(results):
        start = boundaries[i]
        end = boundaries[i + 1] if i + 1 < len(boundaries) else len(all_steps)
        if start >= end:
            continue
        all_steps[end - 1].reward = _compute_reward(result, side_int, vp_reward_coef, reward_shaping=reward_shaping, reward_alpha=reward_alpha)
        all_steps[end - 1].done = True

    return all_steps


def collect_rollout_self_play_batched(
    model: nn.Module,
    n_games: int,
    base_seed: int,
    device: str,
    vp_reward_coef: float = 0.0,
    rollout_temp: float = 1.0,
    reward_shaping: bool = False,
    reward_alpha: float = 0.5,
) -> list[Step]:
    """Collect PPO rollout steps from self-play (both sides use learned model)."""
    if not hasattr(tscore, "rollout_self_play_batched"):
        raise RuntimeError("tscore.rollout_self_play_batched is not available")

    script_path = _export_temp_model(model)
    try:
        results, steps, boundaries = tscore.rollout_self_play_batched(
            model_path=script_path,
            n_games=n_games,
            pool_size=min(n_games, 64),
            seed=base_seed,
            device="cpu",
            temperature=rollout_temp,
            nash_temperatures=True,
        )
    finally:
        try:
            os.remove(script_path)
        except OSError:
            pass

    all_steps: list[Step] = []
    for s in steps:
        country_mask = torch.from_numpy(s["country_mask"])
        step = Step(
            influence=torch.from_numpy(s["influence"]).unsqueeze(0),
            cards=torch.from_numpy(s["cards"]).unsqueeze(0),
            scalars=torch.from_numpy(s["scalars"]).unsqueeze(0),
            card_mask=torch.from_numpy(s["card_mask"]),
            mode_mask=torch.from_numpy(s["mode_mask"]),
            country_mask=country_mask if bool(country_mask.any()) else None,
            card_idx=s["card_idx"],
            mode_idx=s["mode_idx"],
            country_targets=list(s["country_targets"]),
            old_log_prob=float(s["log_prob"]),
            value=float(s["value"]),
            side_int=int(s["side_int"]),
            raw_ussr_influence=s["raw_ussr_influence"].tolist() if "raw_ussr_influence" in s else None,
            raw_us_influence=s["raw_us_influence"].tolist() if "raw_us_influence" in s else None,
            raw_turn=int(s["raw_turn"]) if "raw_turn" in s else None,
            raw_ar=int(s["raw_ar"]) if "raw_ar" in s else None,
            raw_defcon=int(s["raw_defcon"]) if "raw_defcon" in s else None,
            raw_vp=int(s["raw_vp"]) if "raw_vp" in s else None,
            raw_milops=list(s["raw_milops"]) if "raw_milops" in s else None,
            raw_space=list(s["raw_space"]) if "raw_space" in s else None,
            hand_card_ids=list(s["hand_card_ids"]) if "hand_card_ids" in s else None,
            small_choice_target=int(s["small_choice_target"]) if "small_choice_target" in s else -1,
            small_choice_n_options=int(s["small_choice_n_options"]) if "small_choice_n_options" in s else 0,
            small_choice_logprob=float(s["small_choice_logprob"]) if "small_choice_logprob" in s else 0.0,
        )
        all_steps.append(step)

    for i, result in enumerate(results):
        start = boundaries[i]
        end = boundaries[i + 1] if i + 1 < len(boundaries) else len(all_steps)
        if start >= end:
            continue
        last = all_steps[end - 1]
        last.reward = _compute_reward(result, last.side_int, vp_reward_coef, reward_shaping=reward_shaping, reward_alpha=reward_alpha)
        last.done = True

    return all_steps


# ---------------------------------------------------------------------------
# League training helpers
# ---------------------------------------------------------------------------

def _load_wr_table(wr_table_path: str | None) -> dict[str, dict]:
    """Load per-opponent, per-side WR table from JSON. Returns empty dict on miss/error.

    Schema: {opponent_key: {wins_ussr, total_ussr, wins_us, total_us}}
    Migrates old flat format {wins, total} by splitting evenly across both sides.
    """
    if not wr_table_path:
        return {}
    try:
        with open(wr_table_path) as f:
            data = json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as e:
        print(f"  [league] WR table decode failed at {wr_table_path}: {e}; starting empty", flush=True)
        return {}
    if not isinstance(data, dict):
        return {}
    # Migrate old flat schema (wins/total) → per-side schema
    migrated: dict[str, dict] = {}
    needs_migration = False
    for key, val in data.items():
        if "wins_ussr" in val:
            migrated[key] = val
        else:
            # Old format: split evenly (best-effort; data will refine over time)
            old_wins = int(val.get("wins", 0))
            old_total = int(val.get("total", 0))
            migrated[key] = {
                "wins_ussr": old_wins // 2,
                "total_ussr": old_total // 2,
                "wins_us": old_wins - old_wins // 2,
                "total_us": old_total - old_total // 2,
            }
            needs_migration = True
    if needs_migration:
        print(f"  [league] WR table migrated to per-side schema at {wr_table_path}", flush=True)
    return migrated


def _save_json_atomic(path: str, payload: dict) -> None:
    """Write JSON atomically via temp file + rename."""
    parent = os.path.dirname(path) or "."
    os.makedirs(parent, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(prefix=f".{Path(path).name}.", suffix=".tmp", dir=parent)
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(payload, f, indent=2, sort_keys=True)
            f.write("\n")
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_path, path)
    except Exception:
        try:
            os.remove(tmp_path)
        except OSError:
            pass
        raise


# Sentinel path for heuristic when used as a league fixture.
# Allows heuristic to participate in PFSP weighting (tracked under key "heuristic" in wr_table)
# instead of the separate coin-flip mechanism.
HEURISTIC_FIXTURE = "__heuristic__"


def _pfsp_weight(
    opponent_key: str,
    wr_table: dict[str, dict],
    pfsp_exponent: float,
    total_games_all: int = 0,
    side: str = "ussr",
) -> float:
    """Symmetric PFSP + additive UCB opponent selection weight for one side.

    Uses: weight = 4*WR*(1-WR) + c * sqrt(ln(N)/n_i)
    where c = pfsp_exponent, N = total games across all opponents, n_i = games vs this one.
    - Symmetric base: peaks at WR=0.5 (learning sweet spot), drops at extremes.
    - Additive UCB: independent of WR, ensures under-explored opponents get sampled
      even when dominated (WR→1) — allowing re-testing for regression detection.
    - Multiplicative UCB was rejected: near-zero symmetric base at WR→1 kills
      the exploration bonus, preventing re-testing of weak opponents.

    side: "ussr" → use USSR WR   "us" → use US WR
    Always call with an explicit side; the two pools use this independently.
    """
    wr_info = wr_table.get(opponent_key, {})
    MIN_GAMES = 10

    wins_key, total_key = ("wins_ussr", "total_ussr") if side == "ussr" else ("wins_us", "total_us")
    wins = int(wr_info.get(wins_key, 0))
    total = int(wr_info.get(total_key, 0))
    if total < MIN_GAMES:
        return 1.0
    wr = wins / total

    # Symmetric base: parabola peaking at 1.0 when WR=0.5, zero at extremes
    symmetric = 4.0 * wr * (1.0 - wr)

    # Additive UCB exploration bonus — independent of WR so weak opponents get re-tested
    if total_games_all > 0 and total > 0:
        ucb = pfsp_exponent * math.sqrt(math.log(total_games_all) / total)
    else:
        ucb = 0.0

    return max(0.01, symmetric + ucb)


def _update_wr_table_from_steps(
    wr_table: dict[str, dict],
    opponent_path: str | None,
    steps: list,
) -> None:
    """Update per-side WR table in-place from terminal steps of one rollout batch.

    Schema: {wins_ussr, total_ussr, wins_us, total_us}
    side_int=0 → model played USSR; side_int=1 → model played US.
    """
    terminal_steps = [s for s in steps if s.done]
    if not terminal_steps:
        return
    if opponent_path is None:
        key = "heuristic"
    elif opponent_path == "__self__":
        key = "__self__"
    else:
        key = Path(opponent_path).stem
    entry = wr_table.setdefault(key, {
        "wins_ussr": 0, "total_ussr": 0,
        "wins_us": 0, "total_us": 0,
    })
    for s in terminal_steps:
        if s.side_int == 0:  # model played USSR
            entry["wins_ussr"] = int(entry.get("wins_ussr", 0)) + (1 if s.reward > 0 else 0)
            entry["total_ussr"] = int(entry.get("total_ussr", 0)) + 1
        else:  # model played US
            entry["wins_us"] = int(entry.get("wins_us", 0)) + (1 if s.reward > 0 else 0)
            entry["total_us"] = int(entry.get("total_us", 0)) + 1


def sample_K_league_opponents(
    league_dir: str,
    k: int,
    fixtures: list[str],
    recency_tau: float = 20.0,
    heuristic_pct: float = 0.10,
    fixture_fadeout: int = 50,
    current_iter: int = 0,
    self_slot: bool = False,
    current_script: Optional[str] = None,
    wr_table: dict[str, dict] | None = None,
    pfsp_exponent: float = 1.0,
    side: str = "ussr",
    heuristic_floor: float = 0.0,
) -> list[Optional[str]]:
    """Sample k opponents for one side's pool. None = heuristic.

    Call twice — once with side="ussr", once with side="us" — to get independent
    pools each weighted by the relevant per-side PFSP UCB score.

    - Recency-weighted past-self: weight = exp(rank / tau).
    - Fixture fadeout: fixtures removed at current_iter >= fixture_fadeout.
    - UCB-PFSP: (1-WR_side) + c*sqrt(ln(N)/n_i) using the specified side's WR.
    - self_slot: if True, prepend current_script as slot 0 (legacy; prefer False and
      handle self-play separately in the caller).
    - heuristic_floor: minimum selection probability for __heuristic__ fixture.
      If heuristic's normalized PFSP weight falls below this, it's boosted to the
      floor and other weights are reduced proportionally. Prevents PFSP from starving
      heuristic when model WR→1 (sym term→0). 0.0 = no floor (legacy behavior).
    """
    import random
    import re

    # Parse iter_*.pt sorted by iteration number
    iter_pts: list[tuple[int, str]] = []
    for p in sorted(Path(league_dir).glob("iter_*.pt")):
        m = re.search(r"iter_(\d+)\.pt$", str(p))
        if m:
            iter_pts.append((int(m.group(1)), str(p)))
    iter_pts.sort(key=lambda x: x[0])

    # Compute total games for THIS SIDE only (UCB exploration denominator N).
    # Must be per-side to avoid cross-contamination between USSR and US pools.
    _wr = wr_table or {}
    _total_key = "total_ussr" if side == "ussr" else "total_us"
    total_games_all = sum(int(v.get(_total_key, 0)) for v in _wr.values())

    # Recency-weighted past-self pool, multiplied by UCB-PFSP factor
    past_self_paths: list[str] = []
    past_self_weights: list[float] = []
    for rank, (_, path) in enumerate(iter_pts):
        recency_w = math.exp(rank / max(recency_tau, 1.0))
        pfsp_w = _pfsp_weight(Path(path).stem, _wr, pfsp_exponent, total_games_all, side=side)
        past_self_paths.append(path)
        past_self_weights.append(recency_w * pfsp_w)
    if past_self_weights:
        total = sum(past_self_weights)
        past_self_weights = [w / total for w in past_self_weights]

    # Active fixtures (hard-removed after fixture_fadeout iterations)
    active_fixtures = [] if current_iter >= fixture_fadeout else list(fixtures)

    # Combined pool: past-self (recency*pfsp weighted) + fixtures (pfsp weighted).
    # Fixture mass ratio: 2.0x during warm-up (iter<5) for diversity before self-play
    # history builds, 1.0x at steady state (fixtures get 67% → 50% of combined weight).
    # This ensures external opponents are sampled early and often.
    combined_pool: list[str] = past_self_paths + active_fixtures
    if combined_pool:
        past_total = sum(past_self_weights) if past_self_weights else 0.0
        fixture_pfsp_weights = [
            _pfsp_weight("heuristic" if f == HEURISTIC_FIXTURE else Path(f).stem,
                         _wr, pfsp_exponent, total_games_all, side=side) for f in active_fixtures
        ]
        fixture_total = sum(fixture_pfsp_weights) or 1.0
        # Early-iteration boost: 2.0x fixture mass for iter<5 to counter self-play dominance
        # at warm-up when only iter_0001 exists in past-self pool. At steady state: 1.0x.
        fixture_mass_mult = 2.0 if current_iter < 5 else 1.0
        fixture_each = [
            past_total * fixture_mass_mult * (w / fixture_total)
            for w in fixture_pfsp_weights
        ] if active_fixtures else []
        combined_weights = past_self_weights + fixture_each
        total_w = sum(combined_weights)
        if total_w <= 0:
            # Past-self pool is empty (early iters before first iter_*.pt).
            # Fall back to uniform weights over fixtures so random.choices doesn't crash.
            combined_weights = [0.0] * len(past_self_paths) + [1.0 / max(len(active_fixtures), 1)] * len(active_fixtures)
        else:
            combined_weights = [w / total_w for w in combined_weights]
    else:
        combined_weights = []

    # Heuristic floor: if __heuristic__ is a fixture and its normalized weight < floor,
    # boost it to the floor. This prevents PFSP from starving heuristic when WR→1
    # (symmetric term 4*WR*(1-WR) → 0, leaving only tiny UCB bonus).
    # The v299-v305 regression showed that without a floor, heuristic gets <2% of
    # samples, allowing the model to forget general play while optimizing model-vs-model.
    if heuristic_floor > 0 and HEURISTIC_FIXTURE in active_fixtures and combined_pool:
        heur_idx = combined_pool.index(HEURISTIC_FIXTURE)
        heur_w = combined_weights[heur_idx]
        if heur_w < heuristic_floor:
            # Redistribute: scale non-heuristic weights down to make room
            deficit = heuristic_floor - heur_w
            non_heur_total = 1.0 - heur_w
            if non_heur_total > 0:
                scale = (non_heur_total - deficit) / non_heur_total
                combined_weights = [
                    heuristic_floor if i == heur_idx else w * scale
                    for i, w in enumerate(combined_weights)
                ]

    # Don't double-count heuristic: if __heuristic__ is an explicit fixture, its PFSP
    # weight handles allocation. The coin-flip mechanism would oversample it.
    _heuristic_pct = 0.0 if HEURISTIC_FIXTURE in fixtures else heuristic_pct

    opponents: list[Optional[str]] = []

    # Slot 0: always current model (true self-play signal)
    if self_slot and current_script is not None:
        opponents.append(current_script)

    # Remaining slots: recency*pfsp-weighted pool (includes heuristic as a fixture if set).
    # heuristic_pct fallback still applies when pool is empty.
    for _ in range(k - len(opponents)):
        if not combined_pool or random.random() < _heuristic_pct:
            opponents.append(None)  # heuristic
        else:
            chosen = random.choices(combined_pool, weights=combined_weights, k=1)[0]
            opponents.append(chosen)

    return opponents


def _steps_from_native(raw_steps: list) -> list[Step]:
    """Convert a list of native rollout dicts into Step objects."""
    out: list[Step] = []
    for s in raw_steps:
        country_mask = torch.from_numpy(s["country_mask"])
        out.append(Step(
            influence=torch.from_numpy(s["influence"]).unsqueeze(0),
            cards=torch.from_numpy(s["cards"]).unsqueeze(0),
            scalars=torch.from_numpy(s["scalars"]).unsqueeze(0),
            card_mask=torch.from_numpy(s["card_mask"]),
            mode_mask=torch.from_numpy(s["mode_mask"]),
            country_mask=country_mask if bool(country_mask.any()) else None,
            card_idx=s["card_idx"],
            mode_idx=s["mode_idx"],
            country_targets=list(s["country_targets"]),
            old_log_prob=float(s["log_prob"]),
            value=float(s["value"]),
            side_int=int(s["side_int"]),
            raw_ussr_influence=s["raw_ussr_influence"].tolist() if "raw_ussr_influence" in s else None,
            raw_us_influence=s["raw_us_influence"].tolist() if "raw_us_influence" in s else None,
            raw_turn=int(s["raw_turn"]) if "raw_turn" in s else None,
            raw_ar=int(s["raw_ar"]) if "raw_ar" in s else None,
            raw_defcon=int(s["raw_defcon"]) if "raw_defcon" in s else None,
            raw_vp=int(s["raw_vp"]) if "raw_vp" in s else None,
            raw_milops=list(s["raw_milops"]) if "raw_milops" in s else None,
            raw_space=list(s["raw_space"]) if "raw_space" in s else None,
            hand_card_ids=list(s["hand_card_ids"]) if "hand_card_ids" in s else None,
            small_choice_target=int(s["small_choice_target"]) if "small_choice_target" in s else -1,
            small_choice_n_options=int(s["small_choice_n_options"]) if "small_choice_n_options" in s else 0,
            small_choice_logprob=float(s["small_choice_logprob"]) if "small_choice_logprob" in s else 0.0,
        ))
    return out


_ROLLOUT_DIRICHLET_SUPPORT: dict[str, bool] = {}


def _call_rollout_with_optional_dirichlet(fn_name: str, *, dir_alpha: float = 0.0, dir_epsilon: float = 0.0, **kwargs):
    """Call a tscore rollout function, optionally adding Dirichlet noise kwargs.

    Probes on first call whether the C++ binding accepts dir_alpha/dir_epsilon.
    Falls back silently if not supported (bindings predate the feature).
    """
    fn = getattr(tscore, fn_name)
    if dir_alpha <= 0.0 or dir_epsilon <= 0.0:
        return fn(**kwargs)

    cached = _ROLLOUT_DIRICHLET_SUPPORT.get(fn_name)
    call_kwargs = dict(kwargs, dir_alpha=dir_alpha, dir_epsilon=dir_epsilon)
    if cached is not False:
        try:
            result = fn(**call_kwargs)
            _ROLLOUT_DIRICHLET_SUPPORT[fn_name] = True
            return result
        except TypeError as e:
            msg = str(e)
            if "dir_alpha" in msg or "dir_epsilon" in msg or "incompatible function arguments" in msg:
                _ROLLOUT_DIRICHLET_SUPPORT[fn_name] = False
                print(f"  [rollout] {fn_name}: dir noise not supported by bindings, continuing without", flush=True)
            else:
                raise
    return fn(**kwargs)


def _collect_heuristic_from_script(
    script_path: str,
    n_games: int,
    base_seed: int,
    vp_reward_coef: float,
    rollout_temp: float = 1.0,
    dir_alpha: float = 0.0,
    dir_epsilon: float = 0.0,
    side: str = "both",
    reward_shaping: bool = False,
    reward_alpha: float = 0.5,
) -> list[Step]:
    """Collect n_games vs heuristic using an already-exported script.

    side: "ussr" → only USSR games, "us" → only US games, "both" → half each.
    n_games is per side when side!="both", total otherwise.
    """
    if side == "ussr":
        collect_sides = [(tscore.Side.USSR, 0)]
        n_half = n_games
    elif side == "us":
        collect_sides = [(tscore.Side.US, 0)]
        n_half = n_games
    else:
        collect_sides = [(tscore.Side.USSR, 0), (tscore.Side.US, n_games // 2)]
        n_half = n_games // 2
    all_steps: list[Step] = []
    for side_enum, seed_offset in collect_sides:
        results, raw_steps, boundaries = _call_rollout_with_optional_dirichlet(
            "rollout_games_batched",
            dir_alpha=dir_alpha,
            dir_epsilon=dir_epsilon,
            model_path=script_path,
            learned_side=side_enum,
            n_games=n_half,
            pool_size=min(n_half, 64),
            seed=base_seed + seed_offset,
            device="cpu",
            temperature=rollout_temp,
            nash_temperatures=True,
        )
        steps = _steps_from_native(raw_steps)
        side_int = 0 if side_enum == tscore.Side.USSR else 1
        for i, result in enumerate(results):
            start = boundaries[i]
            end = boundaries[i + 1] if i + 1 < len(boundaries) else len(steps)
            if start < end:
                steps[end - 1].reward = _compute_reward(result, side_int, vp_reward_coef, reward_shaping=reward_shaping, reward_alpha=reward_alpha)
                steps[end - 1].done = True
        all_steps.extend(steps)
    return all_steps


def _collect_vs_model_from_script(
    our_script: str,
    opp_script: str,
    n_games: int,
    base_seed: int,
    vp_reward_coef: float,
    rollout_temp: float = 1.0,
    dir_alpha: float = 0.0,
    dir_epsilon: float = 0.0,
    side: str = "both",
    reward_shaping: bool = False,
    reward_alpha: float = 0.5,
) -> list[Step]:
    """Collect n_games vs a scripted model opponent.

    side="both": n_games total, alternating USSR/US (legacy behaviour).
    side="ussr": n_games with model_a as USSR only (no wasted games).
    side="us":   n_games with model_a as US only (no wasted games).
    """
    if side == "ussr":
        learned_side = tscore.Side.USSR
    elif side == "us":
        learned_side = tscore.Side.US
    else:
        learned_side = tscore.Side.Neutral  # alternating

    results, raw_steps, boundaries = _call_rollout_with_optional_dirichlet(
        "rollout_model_vs_model_batched",
        dir_alpha=dir_alpha,
        dir_epsilon=dir_epsilon,
        model_a_path=our_script,
        model_b_path=opp_script,
        n_games=n_games,
        pool_size=min(n_games, 64),
        seed=base_seed,
        device="cpu",
        temperature=rollout_temp,
        nash_temperatures=False,
        learned_side=learned_side,
    )
    steps = _steps_from_native(raw_steps)
    half = n_games // 2
    kept: list[Step] = []
    for i, result in enumerate(results):
        start = boundaries[i]
        end = boundaries[i + 1] if i + 1 < len(boundaries) else len(steps)
        if start >= end:
            continue
        if side == "ussr":
            model_a_side_int = 0
        elif side == "us":
            model_a_side_int = 1
        else:
            model_a_side_int = 0 if i < half else 1
        steps[end - 1].reward = _compute_reward(result, model_a_side_int, vp_reward_coef, reward_shaping=reward_shaping, reward_alpha=reward_alpha)
        steps[end - 1].done = True
        kept.extend(steps[start:end])
    return kept


def collect_rollout_league_batched(
    model: nn.Module,
    league_dir: str,
    n_games: int,
    base_seed: int,
    device: str,
    vp_reward_coef: float = 0.0,
    mix_k: int = 4,
    fixtures: Optional[list[str]] = None,
    ussr_fixtures: Optional[list[str]] = None,
    us_fixtures: Optional[list[str]] = None,
    n_workers: int = 4,
    rollout_temp: float = 1.0,
    recency_tau: float = 20.0,
    heuristic_pct: float = 0.10,
    fixture_fadeout: int = 50,
    current_iter: int = 0,
    self_slot: bool = True,
    wr_table_path: str | None = None,
    pfsp_exponent: float = 1.0,
    dir_alpha: float = 0.0,
    dir_epsilon: float = 0.0,
    reward_shaping: bool = False,
    reward_alpha: float = 0.5,
    heuristic_floor: float = 0.0,
) -> tuple[list[Step], dict[str, float]]:
    """Collect rollout steps against K opponents in parallel (ThreadPoolExecutor).

    Returns (steps, ucb_metrics) where ucb_metrics maps "ucb/{key}" to the UCB
    weight for each fixture/opponent in the WR table. Suitable for W&B logging.

    Exports the model once, splits n_games evenly across K opponents, and runs
    each opponent's batch in a separate thread. The C++ rollout functions release
    the GIL so threads run truly in parallel. Steps are concatenated in order
    (no shuffle — PPO minibatch permutation handles randomization).

    Opponent sampling (see sample_K_league_opponents):
    - Slot 0: always current model (self_slot=True); true self-play gradient signal.
    - Remaining slots: recency*PFSP-weighted past-self + fixtures (faded out after fixture_fadeout iters).
    - heuristic_pct chance per non-self slot of playing vs heuristic.
    - heuristic_floor: minimum selection probability for heuristic (prevents PFSP starvation).
    - PFSP: opponents the model currently struggles against get more training time.
    """
    from concurrent.futures import ThreadPoolExecutor

    if fixtures is None:
        fixtures = []
    # Per-side fixture pools: if provided, use them; otherwise fall back to combined list.
    _ussr_fixtures = ussr_fixtures if ussr_fixtures is not None else fixtures
    _us_fixtures   = us_fixtures   if us_fixtures   is not None else fixtures
    if mix_k < 1:
        mix_k = 1

    wr_table = _load_wr_table(wr_table_path)

    if not hasattr(tscore, "rollout_model_vs_model_batched"):
        # Fallback: single heuristic opponent
        n_half = n_games // 2
        steps_ussr = collect_rollout_batched(model, n_half, tscore.Side.USSR, base_seed, device, {}, vp_reward_coef, rollout_temp)
        steps_us = collect_rollout_batched(model, n_half, tscore.Side.US, base_seed + n_half, device, {}, vp_reward_coef, rollout_temp)
        all_steps = steps_ussr + steps_us
        if wr_table_path:
            _update_wr_table_from_steps(wr_table, None, all_steps)
            _save_json_atomic(wr_table_path, wr_table)
        return all_steps, {}, []

    script_path = _export_temp_model(model)

    # Two independent opponent pools — USSR and US — each weighted by per-side PFSP.
    # k_per_side opponents per pool; self-play slot is always added separately.
    k_per_side = max(1, (mix_k - (1 if self_slot else 0)) // 2)
    _common_kwargs = dict(
        recency_tau=recency_tau,
        heuristic_pct=heuristic_pct,
        fixture_fadeout=fixture_fadeout,
        current_iter=current_iter,
        self_slot=False,  # self handled below
        current_script=script_path,
        wr_table=wr_table,
        pfsp_exponent=pfsp_exponent,
        heuristic_floor=heuristic_floor,
    )
    ussr_opps = sample_K_league_opponents(league_dir, k_per_side, side="ussr", fixtures=_ussr_fixtures, **_common_kwargs)
    us_opps   = sample_K_league_opponents(league_dir, k_per_side, side="us",   fixtures=_us_fixtures,   **_common_kwargs)

    # Each slot gets an equal share of n_games; self gets both sides, pools get one side each.
    total_slots = (1 if self_slot else 0) + k_per_side * 2
    games_per_slot = max(2, n_games // max(total_slots, 1))
    games_per_slot = games_per_slot if games_per_slot % 2 == 0 else games_per_slot - 1

    def _label(opp: Optional[str]) -> str:
        if opp is None or opp == HEURISTIC_FIXTURE:
            return "heuristic"
        if opp == script_path:
            return "self"
        return Path(opp).stem

    try:
        # Log opponent selections
        if self_slot:
            print(f"  [league] self: self | ussr_pool: {[_label(o) for o in ussr_opps]} | us_pool: {[_label(o) for o in us_opps]}", flush=True)
        else:
            print(f"  [league] ussr_pool: {[_label(o) for o in ussr_opps]} | us_pool: {[_label(o) for o in us_opps]}", flush=True)

        # Print per-side PFSP weights with component breakdown
        if wr_table:
            # Per-side totals for correct UCB (no cross-side contamination)
            _log_total_ussr = sum(int(v.get("total_ussr", 0)) for v in wr_table.values())
            _log_total_us = sum(int(v.get("total_us", 0)) for v in wr_table.values())
            all_shown_keys: set[str] = set()
            pfsp_lines = []
            for pool_side, pool_opps in [("ussr", ussr_opps), ("us", us_opps)]:
                _side_total = _log_total_ussr if pool_side == "ussr" else _log_total_us
                seen: set[str] = set()
                for opp in pool_opps:
                    label = _label(opp)
                    if label in seen or label == "self":
                        continue
                    seen.add(label)
                    all_shown_keys.add(label)
                    wr_key = "heuristic" if (opp is None or opp == HEURISTIC_FIXTURE) else label
                    info = wr_table.get(wr_key, {})
                    wins_key = "wins_ussr" if pool_side == "ussr" else "wins_us"
                    total_key = "total_ussr" if pool_side == "ussr" else "total_us"
                    n_side = int(info.get(total_key, 0))
                    if n_side >= 10:
                        wr_side = int(info.get(wins_key, 0)) / n_side
                        sym = 4.0 * wr_side * (1.0 - wr_side)
                        ucb_val = pfsp_exponent * math.sqrt(math.log(_side_total) / n_side) if _side_total > 0 and n_side > 0 else 0.0
                        w = max(0.01, sym + ucb_val)
                        pfsp_lines.append(
                            f"    [{pool_side}] {label}: WR={wr_side:.2f}(n={n_side}) "
                            f"sym={sym:.3f} ucb={ucb_val:.3f} → pfsp={w:.3f}"
                        )
                    else:
                        pfsp_lines.append(f"    [{pool_side}] {label}: WR=?(n={n_side}) pfsp=1.000 (< MIN_GAMES)")
            if pfsp_lines:
                print("  [pfsp]", flush=True)
                for line in pfsp_lines:
                    print(line, flush=True)

        # Build task list: (slot_index, opp, collect_side)
        # collect_side: "ussr"/"us" for pool opponents (single-side); "both" for self-slot.
        tasks: list[tuple[int, Optional[str], str]] = []
        slot_idx = 0
        if self_slot:
            tasks.append((slot_idx, script_path, "both"))
            slot_idx += 1
        for opp in ussr_opps:
            tasks.append((slot_idx, opp, "ussr"))
            slot_idx += 1
        for opp in us_opps:
            tasks.append((slot_idx, opp, "us"))
            slot_idx += 1

        def _run_one(task_idx: int, opp: Optional[str], collect_side: str) -> list[Step]:
            seed = base_seed + task_idx * games_per_slot
            if opp is None or opp == HEURISTIC_FIXTURE:
                return _collect_heuristic_from_script(
                    script_path, games_per_slot, seed, vp_reward_coef,
                    rollout_temp, dir_alpha, dir_epsilon, side=collect_side,
                    reward_shaping=reward_shaping, reward_alpha=reward_alpha,
                )
            return _collect_vs_model_from_script(
                script_path, opp, games_per_slot, seed, vp_reward_coef, rollout_temp, dir_alpha, dir_epsilon,
                side=collect_side, reward_shaping=reward_shaping, reward_alpha=reward_alpha,
            )

        actual_workers = min(n_workers, len(tasks))
        # per_opp_results: [{opponent, side, wins, losses, draws, n_games}]
        # populated below for SQL logging; keyed by task index for ordering.
        per_opp_results: list[dict] = []

        with ThreadPoolExecutor(max_workers=actual_workers) as executor:
            futures_with_meta = [
                (executor.submit(_run_one, ti, opp, cs), opp, cs)
                for ti, opp, cs in tasks
            ]
            all_steps: list[Step] = []
            for f, opp, collect_side in futures_with_meta:
                batch = f.result()
                if wr_table_path:
                    wr_key = opp
                    if opp is not None and opp == script_path:
                        wr_key = "__self__"
                    elif opp == HEURISTIC_FIXTURE:
                        wr_key = None
                    _update_wr_table_from_steps(wr_table, wr_key, batch)
                # Compute per-batch W/L for SQL logging (terminal steps only)
                terminal = [s for s in batch if s.done]
                wins = sum(1 for s in terminal if s.reward > 0)
                losses = sum(1 for s in terminal if s.reward < 0)
                draws = len(terminal) - wins - losses
                per_opp_results.append({
                    "opponent": _label(opp),
                    "side": collect_side,
                    "wins": wins,
                    "losses": losses,
                    "draws": draws,
                    "n_games": len(terminal),
                })
                all_steps.extend(batch)

        if wr_table_path:
            _save_json_atomic(wr_table_path, wr_table)

        # Compute UCB metrics for all WR table entries → W&B logging
        ucb_metrics: dict[str, float] = {}
        if wr_table:
            # Per-side totals for correct UCB denominator (no cross-contamination)
            _total_ussr = sum(int(v.get("total_ussr", 0)) for v in wr_table.values())
            _total_us = sum(int(v.get("total_us", 0)) for v in wr_table.values())
            # Aggregate pool composition metrics
            _fixture_weight_ussr_sum = 0.0
            _fixture_weight_us_sum = 0.0
            _self_weight_ussr_sum = 0.0
            _self_weight_us_sum = 0.0
            for key, info in wr_table.items():
                if key == "__self__":
                    continue
                # Clean name for W&B: v8_scripted → v8
                clean = key.replace("_scripted", "")
                w_u = _pfsp_weight(key, wr_table, pfsp_exponent, _total_ussr, side="ussr")
                w_s = _pfsp_weight(key, wr_table, pfsp_exponent, _total_us, side="us")
                is_self_snap = key.startswith("iter_")
                if not is_self_snap:
                    ucb_metrics[f"ucb/{clean}_weight_ussr"] = w_u
                    ucb_metrics[f"ucb/{clean}_weight_us"] = w_s
                    _fixture_weight_ussr_sum += w_u
                    _fixture_weight_us_sum += w_s
                else:
                    _self_weight_ussr_sum += w_u
                    _self_weight_us_sum += w_s
                # Per-side WR for context
                t_u = int(info.get("total_ussr", 0))
                t_s = int(info.get("total_us", 0))
                if t_u >= 10:
                    ucb_metrics[f"ucb/{clean}_wr_ussr"] = int(info.get("wins_ussr", 0)) / t_u
                if t_s >= 10:
                    ucb_metrics[f"ucb/{clean}_wr_us"] = int(info.get("wins_us", 0)) / t_s
            # Pool composition: fixture vs past-self weight mass
            ucb_metrics["ucb/fixture_mass_ussr"] = _fixture_weight_ussr_sum
            ucb_metrics["ucb/fixture_mass_us"] = _fixture_weight_us_sum
            ucb_metrics["ucb/self_mass_ussr"] = _self_weight_ussr_sum
            ucb_metrics["ucb/self_mass_us"] = _self_weight_us_sum
            if (_fixture_weight_ussr_sum + _self_weight_ussr_sum) > 0:
                ucb_metrics["ucb/fixture_frac_ussr"] = _fixture_weight_ussr_sum / (_fixture_weight_ussr_sum + _self_weight_ussr_sum)
            if (_fixture_weight_us_sum + _self_weight_us_sum) > 0:
                ucb_metrics["ucb/fixture_frac_us"] = _fixture_weight_us_sum / (_fixture_weight_us_sum + _self_weight_us_sum)
            ucb_metrics["ucb/total_games_ussr"] = _total_ussr
            ucb_metrics["ucb/total_games_us"] = _total_us

        return all_steps, ucb_metrics, per_opp_results
    finally:
        try:
            os.remove(script_path)
        except OSError:
            pass


collect_rollout = collect_rollout_batched


# ---------------------------------------------------------------------------
# GAE advantage computation
# ---------------------------------------------------------------------------

def compute_gae(steps: list[Step], gamma: float = 0.99, lam: float = 0.95) -> None:
    """Compute GAE advantages and returns in-place for a single-side episode.

    Assumes all steps are from the same side (e.g., heuristic-mode training).
    Assumes steps[-1].done is True and steps[-1].reward is the terminal reward.
    """
    T = len(steps)
    gae = 0.0
    for t in reversed(range(T)):
        if t == T - 1:
            next_value = 0.0
            delta = steps[t].reward - steps[t].value
        else:
            next_value = steps[t + 1].value
            delta = steps[t].reward + gamma * next_value - steps[t].value
        gae = delta + gamma * lam * (0.0 if steps[t].done else gae)
        steps[t].advantage = gae
        steps[t].returns = gae + steps[t].value


def _compute_gae_per_side(seg: list[Step], gamma: float, lam: float) -> None:
    """GAE computed independently for each side's steps in a self-play game.

    In zero-sum self-play, steps alternate between USSR and US. Computing GAE on
    the interleaved sequence would mix perspectives (V_USSR and V_US). Instead,
    we compute GAE on each side's steps independently, bootstrapping only from
    same-side values.

    Terminal reward for each side is assigned from game outcome:
    - The side that took the last action gets the assigned reward (done=True step)
    - The other side gets the negation (zero-sum)
    """
    if not seg:
        return

    terminal = seg[-1]
    terminal_side = terminal.side_int
    terminal_reward = terminal.reward

    for target_side in [0, 1]:
        side_steps = [s for s in seg if s.side_int == target_side]
        if not side_steps:
            continue

        # Terminal reward from this side's perspective
        reward = terminal_reward if target_side == terminal_side else -terminal_reward

        T = len(side_steps)
        gae = 0.0
        for t in reversed(range(T)):
            if t == T - 1:
                # Last step for this side: bootstrap from terminal outcome
                delta = reward - side_steps[t].value
                next_value = 0.0
            else:
                # Bootstrap from next same-side step's value
                next_value = side_steps[t + 1].value
                delta = gamma * next_value - side_steps[t].value  # non-terminal r=0
            gae = delta + gamma * lam * gae
            side_steps[t].advantage = gae
            side_steps[t].returns = gae + side_steps[t].value


def compute_gae_batch(all_steps: list[Step], gamma: float = 0.99, lam: float = 0.95) -> None:
    """Compute GAE for all games in the flat steps list.

    Game boundaries are detected by the `done` flag. For self-play games (mixed
    side_ints), per-side GAE is used. For single-side games (heuristic mode),
    standard GAE is used.
    """
    # Split into per-game segments
    game_segments: list[list[Step]] = []
    current: list[Step] = []
    for step in all_steps:
        current.append(step)
        if step.done:
            game_segments.append(current)
            current = []
    if current:
        game_segments.append(current)

    for seg in game_segments:
        sides = {s.side_int for s in seg}
        if len(sides) > 1:
            # Self-play: compute GAE per side to avoid mixing perspectives
            _compute_gae_per_side(seg, gamma=gamma, lam=lam)
        else:
            # Heuristic mode: all steps same side, standard GAE
            compute_gae(seg, gamma=gamma, lam=lam)


# ---------------------------------------------------------------------------
# UPGO — Upgoing Policy Update (AlphaStar)
# ---------------------------------------------------------------------------

def apply_upgo_advantages(all_steps: list[Step], gamma: float = 0.99) -> None:
    """Override `advantage` field with UPGO estimates, in-place.

    UPGO return: G_t = r_t + γ * max(V(s_{t+1}), G_{t+1})
    Only propagates returns upward when they exceed the value estimate,
    filtering out bad-luck outcomes from the policy gradient signal.

    `returns` (used for value function training) is left unchanged — it
    keeps the GAE return so the critic stays well-calibrated. Only the
    policy gradient uses the UPGO advantage.

    Must be called AFTER compute_gae_batch (which populates `returns`).
    """
    # Split into per-game segments by `done` flag
    game_segments: list[list[Step]] = []
    current: list[Step] = []
    for step in all_steps:
        current.append(step)
        if step.done:
            game_segments.append(current)
            current = []
    if current:
        game_segments.append(current)

    for seg in game_segments:
        # Per-side UPGO for self-play; single-side for league/heuristic
        sides = {s.side_int for s in seg}
        if len(sides) > 1:
            for target_side in [0, 1]:
                side_steps = [s for s in seg if s.side_int == target_side]
                _apply_upgo_to_segment(side_steps, gamma)
        else:
            _apply_upgo_to_segment(seg, gamma)


def _apply_upgo_to_segment(seg: list[Step], gamma: float) -> None:
    """UPGO on a single-side segment."""
    if not seg:
        return
    T = len(seg)
    upgo_g = 0.0
    for t in reversed(range(T)):
        r = seg[t].reward
        v_next = seg[t + 1].value if t + 1 < T else 0.0
        upgo_g = r + gamma * max(v_next, upgo_g)
        seg[t].advantage = upgo_g - seg[t].value


# ---------------------------------------------------------------------------
# PPO update — vectorized (no per-step Python loop)
# ---------------------------------------------------------------------------

def ppo_update(
    steps: list[Step],
    model: nn.Module,
    optimizer: torch.optim.Optimizer,
    device: str,
    ppo_epochs: int = 4,
    clip_eps: float = 0.2,
    vf_coef: float = 0.5,
    ent_coef: float = 0.01,
    minibatch_size: int = 2048,
) -> dict[str, float]:
    """Run PPO updates over collected steps. Returns metric dict.

    P0 fixes vs initial version:
    - model.eval() during forward pass → consistent log_probs with rollout (no dropout noise)
    - Vectorized log_prob + entropy computation (no per-step Python loop)
    - Country entropy included
    - Per-side advantage normalization (USSR/US have different baselines)
    - Schulman approx_kl: E[(r-1) - log(r)]
    """
    N = len(steps)
    if N == 0:
        return {}

    # Per-side advantage normalization (USSR and US have different win-rate baselines)
    advs = torch.tensor([s.advantage for s in steps], dtype=torch.float32)
    returns = torch.tensor([s.returns for s in steps], dtype=torch.float32)

    # Diagnose NaN source before normalization
    n_nan_adv = torch.isnan(advs).sum().item()
    n_nan_ret = torch.isnan(returns).sum().item()
    if n_nan_adv > 0 or n_nan_ret > 0:
        nan_vals = [(i, s.value, s.advantage, s.returns)
                    for i, s in enumerate(steps)
                    if s.value != s.value or s.advantage != s.advantage]  # NaN check via !=
        print(f"  [NaN] adv={n_nan_adv}/{len(steps)}, ret={n_nan_ret}/{len(steps)}, "
              f"first NaN steps: {nan_vals[:3]}", flush=True)
    # Defensive: replace NaN with 0 to prevent gradient corruption
    advs = advs.nan_to_num(nan=0.0, posinf=10.0, neginf=-10.0)
    returns = returns.nan_to_num(nan=0.0, posinf=10.0, neginf=-10.0)

    for side_val in (0, 1):
        mask = torch.tensor([s.side_int == side_val for s in steps])
        if mask.sum() > 1:
            mu = advs[mask].mean()
            sigma = advs[mask].std()
            advs[mask] = (advs[mask] - mu) / (sigma + 1e-8)

    metrics = {"policy_loss": 0.0, "value_loss": 0.0, "sc_loss": 0.0,
               "entropy": 0.0, "clip_fraction": 0.0, "approx_kl": 0.0}
    n_updates = 0

    for _ in range(ppo_epochs):
        perm = torch.randperm(N)
        for start in range(0, N, minibatch_size):
            idx = perm[start:start + minibatch_size]
            batch_steps = [steps[i] for i in idx.tolist()]
            B = len(batch_steps)
            batch_advs = advs[idx].to(device)
            batch_returns = returns[idx].to(device)

            # Stack features
            inf_batch = torch.cat([s.influence for s in batch_steps]).to(device)
            card_batch = torch.cat([s.cards for s in batch_steps]).to(device)
            scalar_batch = torch.cat([s.scalars for s in batch_steps]).to(device)

            # Forward in eval mode to match rollout (no dropout noise on log_probs).
            # eval() still allows gradient flow for optimizer.step().
            model.eval()
            outputs = model(inf_batch, card_batch, scalar_batch)
            card_logits_b = outputs["card_logits"]        # (B, 111)
            mode_logits_b = outputs["mode_logits"]        # (B, 5)
            country_logits_b = outputs.get("country_logits")  # (B, 86) or None
            small_choice_logits_b = outputs.get("small_choice_logits")  # (B, 8) or None
            values_b = outputs["value"].squeeze(-1)       # (B,)

            # Diagnose NaN in inputs and model outputs (first minibatch only to avoid log spam)
            if n_updates == 0:
                print(f"  [diag] inf dtype={inf_batch.dtype} shape={inf_batch.shape} "
                      f"nan={torch.isnan(inf_batch).sum()} inf_vals={torch.isinf(inf_batch).sum()} "
                      f"range=[{inf_batch.min():.2f},{inf_batch.max():.2f}]", flush=True)
                print(f"  [diag] scalar dtype={scalar_batch.dtype} "
                      f"nan={torch.isnan(scalar_batch).sum()} "
                      f"range=[{scalar_batch.min():.3f},{scalar_batch.max():.3f}]", flush=True)
                print(f"  [diag] card_logits nan={torch.isnan(card_logits_b).sum()} "
                      f"range=[{card_logits_b.min():.2f},{card_logits_b.max():.2f}]", flush=True)
                print(f"  [diag] values nan={torch.isnan(values_b).sum()} "
                      f"range=[{values_b.min():.4f},{values_b.max():.4f}]", flush=True)
            if torch.isnan(card_logits_b).any() or torch.isnan(values_b).any():
                print(f"  [NaN] model outputs: card={torch.isnan(card_logits_b).sum().item()}, "
                      f"value={torch.isnan(values_b).sum().item()}", flush=True)
            # Defensive: replace NaN model outputs with 0
            card_logits_b = card_logits_b.nan_to_num(nan=0.0)
            mode_logits_b = mode_logits_b.nan_to_num(nan=0.0)
            values_b = values_b.nan_to_num(nan=0.0)
            if country_logits_b is not None:
                country_logits_b = country_logits_b.nan_to_num(nan=0.0)

            # ── Build batched masks and action indices ─────────────────────────
            card_masks_b = torch.stack([s.card_mask for s in batch_steps]).to(device)   # (B, 111)
            mode_masks_b = torch.stack([s.mode_mask for s in batch_steps]).to(device)   # (B, 5)
            # country_mask: None (SPACE/EVENT) → all-False → zero contribution
            country_masks_b = torch.stack([
                s.country_mask if s.country_mask is not None
                else torch.zeros(COUNTRY_SLOTS, dtype=torch.bool)
                for s in batch_steps
            ]).to(device)  # (B, 86)

            card_idxs_b = torch.tensor([s.card_idx for s in batch_steps], device=device)  # (B,)
            mode_idxs_b = torch.tensor([s.mode_idx for s in batch_steps], device=device)  # (B,)

            # ── Vectorized log-prob computation ────────────────────────────────
            # Card: masked log_softmax → gather at sampled index
            masked_card = card_logits_b.masked_fill(~card_masks_b, float("-inf"))
            log_prob_card = F.log_softmax(masked_card, dim=1).gather(
                1, card_idxs_b.unsqueeze(1)).squeeze(1)  # (B,)

            # Mode: masked log_softmax → gather at sampled index
            masked_mode = mode_logits_b.masked_fill(~mode_masks_b, float("-inf"))
            log_prob_mode = F.log_softmax(masked_mode, dim=1).gather(
                1, mode_idxs_b.unsqueeze(1)).squeeze(1)  # (B,)

            # Country: mixture probs masked + normalized → log → gather + sum over targets
            log_prob_country = torch.zeros(B, device=device)
            ent_country = torch.zeros(B, device=device)
            if country_logits_b is not None:
                country_probs_b = country_logits_b.clone()
                country_probs_b = country_probs_b.masked_fill(~country_masks_b, 0.0)
                country_probs_b = country_probs_b / (
                    country_probs_b.sum(dim=1, keepdim=True) + 1e-10)
                log_country_b = torch.log(country_probs_b + 1e-10)  # (B, 86)

                # Entropy over country distribution
                ent_country = -(country_probs_b * log_country_b).sum(dim=1)  # (B,)

                # Padded gather for per-step variable-length targets
                max_ct = max((len(s.country_targets) for s in batch_steps), default=0)
                if max_ct > 0:
                    ct_pad = torch.zeros(B, max_ct, dtype=torch.long, device=device)
                    ct_valid = torch.zeros(B, max_ct, dtype=torch.bool, device=device)
                    for i, step in enumerate(batch_steps):
                        if step.country_targets:
                            t = torch.tensor(step.country_targets, dtype=torch.long)
                            ct_pad[i, :len(t)] = t
                            ct_valid[i, :len(t)] = True
                    gathered = log_country_b.gather(1, ct_pad.clamp(0, COUNTRY_SLOTS - 1))
                    log_prob_country = (gathered * ct_valid.float()).sum(dim=1)  # (B,)

            new_log_probs = log_prob_card + log_prob_mode + log_prob_country

            # ── Vectorized entropy ─────────────────────────────────────────────
            # Clamp log_softmax to -20 before multiplying by softmax. This handles
            # masked entries (log_softmax=-inf, softmax=0): in the forward pass
            # exp(-20)≈0 so contribution≈0; in the backward pass, clamp's gradient
            # is 0 at -inf so NaN gradients never flow into model weights.
            # (nan_to_num only fixes forward; clamp also fixes backward.)
            log_p_card = F.log_softmax(masked_card, dim=1).clamp(min=-20)
            ent_card = -(log_p_card.exp() * log_p_card).sum(dim=1)
            log_p_mode = F.log_softmax(masked_mode, dim=1).clamp(min=-20)
            ent_mode = -(log_p_mode.exp() * log_p_mode).sum(dim=1)
            entropies = ent_card + ent_mode + ent_country

            # ── PPO objective ─────────────────────────────────────────────────
            old_log_probs = torch.tensor(
                [s.old_log_prob for s in batch_steps], device=device)

            ratio = torch.exp(new_log_probs - old_log_probs)
            clipped_ratio = torch.clamp(ratio, 1.0 - clip_eps, 1.0 + clip_eps)

            policy_loss = -torch.min(ratio * batch_advs, clipped_ratio * batch_advs).mean()
            value_loss = F.mse_loss(values_b, batch_returns)
            entropy_loss = -entropies.mean()

            # ── SmallChoice auxiliary cross-entropy loss ──────────────────────
            sc_loss = torch.tensor(0.0, device=device)
            if small_choice_logits_b is not None:
                sc_targets = torch.tensor(
                    [s.small_choice_target for s in batch_steps], device=device)
                sc_n_opts = torch.tensor(
                    [s.small_choice_n_options for s in batch_steps], device=device)
                sc_valid = (sc_targets >= 0) & (sc_n_opts > 1)
                if sc_valid.any():
                    sc_logits_valid = small_choice_logits_b[sc_valid]  # (V, 8)
                    sc_targets_valid = sc_targets[sc_valid].long()     # (V,)
                    sc_n_valid = sc_n_opts[sc_valid]                   # (V,)
                    # Mask logits beyond n_options to -inf
                    sc_mask = torch.arange(
                        sc_logits_valid.size(1), device=device
                    ).unsqueeze(0) < sc_n_valid.unsqueeze(1)  # (V, 8)
                    sc_logits_masked = sc_logits_valid.masked_fill(~sc_mask, float("-inf"))
                    sc_loss = F.cross_entropy(sc_logits_masked, sc_targets_valid)

            loss = (policy_loss + vf_coef * value_loss
                    + ent_coef * entropy_loss + sc_loss)

            # Skip update if loss is NaN to prevent weight corruption
            if torch.isnan(loss):
                print(f"  [NaN] loss components: pl={policy_loss.item():.4f} "
                      f"vl={value_loss.item():.4f} ent={entropy_loss.item():.4f} "
                      f"sc={sc_loss.item():.4f} — skipping", flush=True)
                continue

            optimizer.zero_grad()
            loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), max_norm=0.5)
            optimizer.step()

            with torch.no_grad():
                clip_frac = ((ratio - 1.0).abs() > clip_eps).float().mean().item()
                # Schulman's KL approximation: E[(r-1) - log(r)] — always ≥ 0
                approx_kl = ((ratio - 1.0) - torch.log(ratio + 1e-10)).mean().item()

            metrics["policy_loss"] += policy_loss.item()
            metrics["value_loss"] += value_loss.item()
            metrics["sc_loss"] += sc_loss.item()
            metrics["entropy"] += entropies.mean().item()
            metrics["clip_fraction"] += clip_frac
            metrics["approx_kl"] += approx_kl
            n_updates += 1

    if n_updates > 0:
        for k in metrics:
            metrics[k] /= n_updates

    return metrics


# ---------------------------------------------------------------------------
# Packed PPO update (ported from experimental/ppo/update.py)
# Packs all rollout steps once into dense tensors, moves to device once,
# then uses index_select for minibatches — ~12x faster than baseline update.
# ---------------------------------------------------------------------------

@dataclass
class PackedSteps:
    """Dense tensor representation of a rollout batch for fast PPO updates."""
    influence: torch.Tensor
    cards: torch.Tensor
    scalars: torch.Tensor
    card_masks: torch.Tensor
    mode_masks: torch.Tensor
    country_masks: torch.Tensor
    card_indices: torch.Tensor
    mode_indices: torch.Tensor
    country_targets: torch.Tensor   # (N, max_targets) padded
    country_valid: torch.Tensor     # (N, max_targets) bool validity mask
    old_log_probs: torch.Tensor
    advantages: torch.Tensor        # per-side normalized
    returns: torch.Tensor
    sc_targets: torch.Tensor        # (N,) SmallChoice target (-1 = no decision)
    sc_n_options: torch.Tensor      # (N,) number of options per SmallChoice

    def to(self, device: str) -> "PackedSteps":
        return PackedSteps(
            influence=self.influence.to(device),
            cards=self.cards.to(device),
            scalars=self.scalars.to(device),
            card_masks=self.card_masks.to(device),
            mode_masks=self.mode_masks.to(device),
            country_masks=self.country_masks.to(device),
            card_indices=self.card_indices.to(device),
            mode_indices=self.mode_indices.to(device),
            country_targets=self.country_targets.to(device),
            country_valid=self.country_valid.to(device),
            old_log_probs=self.old_log_probs.to(device),
            advantages=self.advantages.to(device),
            returns=self.returns.to(device),
            sc_targets=self.sc_targets.to(device),
            sc_n_options=self.sc_n_options.to(device),
        )


def pack_steps(steps: list[Step]) -> PackedSteps:
    """Pack rollout steps once. Performs per-side advantage normalization."""
    if not steps:
        raise ValueError("steps must be non-empty")

    advantages = torch.tensor([s.advantage for s in steps], dtype=torch.float32)
    returns = torch.tensor([s.returns for s in steps], dtype=torch.float32)

    # NaN diagnostics (mirror ppo_update)
    n_nan_adv = torch.isnan(advantages).sum().item()
    n_nan_ret = torch.isnan(returns).sum().item()
    if n_nan_adv > 0 or n_nan_ret > 0:
        nan_vals = [(i, s.value, s.advantage, s.returns)
                    for i, s in enumerate(steps)
                    if s.value != s.value or s.advantage != s.advantage]
        print(f"  [NaN] adv={n_nan_adv}/{len(steps)}, ret={n_nan_ret}/{len(steps)}, "
              f"first NaN steps: {nan_vals[:3]}", flush=True)
    advantages = advantages.nan_to_num(nan=0.0, posinf=10.0, neginf=-10.0)
    returns = returns.nan_to_num(nan=0.0, posinf=10.0, neginf=-10.0)

    side_ints = torch.tensor([s.side_int for s in steps], dtype=torch.long)
    for side_val in (0, 1):
        mask = side_ints == side_val
        if int(mask.sum().item()) > 1:
            mu = advantages[mask].mean()
            sigma = advantages[mask].std()
            advantages[mask] = (advantages[mask] - mu) / (sigma + 1e-8)

    max_targets = max((len(s.country_targets) for s in steps), default=0)
    target_pad = torch.zeros((len(steps), max(max_targets, 1)), dtype=torch.long)
    target_valid = torch.zeros((len(steps), max(max_targets, 1)), dtype=torch.bool)
    for row, step in enumerate(steps):
        if step.country_targets:
            t = torch.tensor(step.country_targets, dtype=torch.long)
            target_pad[row, :len(t)] = t
            target_valid[row, :len(t)] = True

    return PackedSteps(
        influence=torch.cat([s.influence for s in steps], dim=0),
        cards=torch.cat([s.cards for s in steps], dim=0),
        scalars=torch.cat([s.scalars for s in steps], dim=0),
        card_masks=torch.stack([s.card_mask for s in steps]),
        mode_masks=torch.stack([s.mode_mask for s in steps]),
        country_masks=torch.stack([
            s.country_mask if s.country_mask is not None
            else torch.zeros(COUNTRY_SLOTS, dtype=torch.bool)
            for s in steps
        ]),
        card_indices=torch.tensor([s.card_idx for s in steps], dtype=torch.long),
        mode_indices=torch.tensor([s.mode_idx for s in steps], dtype=torch.long),
        country_targets=target_pad,
        country_valid=target_valid,
        old_log_probs=torch.tensor([s.old_log_prob for s in steps], dtype=torch.float32),
        advantages=advantages,
        returns=returns,
        sc_targets=torch.tensor([s.small_choice_target for s in steps], dtype=torch.long),
        sc_n_options=torch.tensor([s.small_choice_n_options for s in steps], dtype=torch.long),
    )


def ppo_update_packed(
    packed_steps: PackedSteps,
    model: nn.Module,
    optimizer: torch.optim.Optimizer,
    device: str,
    ppo_epochs: int = 4,
    clip_eps: float = 0.2,
    vf_coef: float = 0.5,
    ent_coef: float = 0.01,
    minibatch_size: int = 2048,
    target_kl: float = 0.015,
) -> dict[str, float]:
    """PPO update with packed tensors — ~12x faster than baseline.

    Packs the batch to device once, uses index_select for minibatches,
    avoids per-minibatch Python tensor assembly. PPO math identical to ppo_update.

    target_kl: per-epoch KL early stopping. When the average KL over minibatches
    in an epoch exceeds this threshold, remaining epochs are skipped. This prevents
    the policy from drifting too far in a single update, smoothing training.
    Set to 0 to disable.
    """
    num_steps = packed_steps.influence.shape[0]
    if num_steps == 0:
        return {}

    packed = packed_steps.to(device)
    model.eval()

    metrics = {"policy_loss": 0.0, "value_loss": 0.0, "sc_loss": 0.0,
               "entropy": 0.0, "clip_fraction": 0.0, "approx_kl": 0.0}
    n_updates = 0

    _epochs_run = 0
    _kl_early_stopped = False
    for _epoch_i in range(ppo_epochs):
        _epoch_kl_sum = 0.0
        _epoch_kl_count = 0
        perm = torch.randperm(num_steps, device=device)
        for start in range(0, num_steps, minibatch_size):
            idx = perm[start:start + minibatch_size]

            outputs = model(
                packed.influence.index_select(0, idx),
                packed.cards.index_select(0, idx),
                packed.scalars.index_select(0, idx),
            )
            card_logits = outputs["card_logits"].nan_to_num(nan=0.0)
            mode_logits = outputs["mode_logits"].nan_to_num(nan=0.0)
            values = outputs["value"].squeeze(-1).nan_to_num(nan=0.0)
            country_logits = outputs.get("country_logits")
            small_choice_logits = outputs.get("small_choice_logits")

            # Diag on first minibatch
            if n_updates == 0:
                inf_b = packed.influence.index_select(0, idx)
                sc_b = packed.scalars.index_select(0, idx)
                print(f"  [diag] inf dtype={inf_b.dtype} shape={inf_b.shape} "
                      f"nan={torch.isnan(inf_b).sum()} inf_vals={torch.isinf(inf_b).sum()} "
                      f"range=[{inf_b.min():.2f},{inf_b.max():.2f}]", flush=True)
                print(f"  [diag] scalar dtype={sc_b.dtype} nan={torch.isnan(sc_b).sum()} "
                      f"range=[{sc_b.min():.3f},{sc_b.max():.3f}]", flush=True)
                print(f"  [diag] card_logits nan={torch.isnan(card_logits).sum()} "
                      f"range=[{card_logits.min():.2f},{card_logits.max():.2f}]", flush=True)
                print(f"  [diag] values nan={torch.isnan(values).sum()} "
                      f"range=[{values.min():.4f},{values.max():.4f}]", flush=True)

            if country_logits is not None:
                country_logits = country_logits.nan_to_num(nan=0.0)

            card_masks = packed.card_masks.index_select(0, idx)
            mode_masks = packed.mode_masks.index_select(0, idx)
            country_masks = packed.country_masks.index_select(0, idx)
            card_indices = packed.card_indices.index_select(0, idx)
            mode_indices = packed.mode_indices.index_select(0, idx)
            old_log_probs = packed.old_log_probs.index_select(0, idx)
            advantages = packed.advantages.index_select(0, idx)
            returns = packed.returns.index_select(0, idx)
            country_targets = packed.country_targets.index_select(0, idx)
            country_valid = packed.country_valid.index_select(0, idx)

            masked_card = card_logits.masked_fill(~card_masks, float("-inf"))
            masked_mode = mode_logits.masked_fill(~mode_masks, float("-inf"))

            log_prob_card = F.log_softmax(masked_card, dim=1).gather(
                1, card_indices.unsqueeze(1)).squeeze(1)
            log_prob_mode = F.log_softmax(masked_mode, dim=1).gather(
                1, mode_indices.unsqueeze(1)).squeeze(1)

            log_prob_country = torch.zeros_like(log_prob_card)
            ent_country = torch.zeros_like(log_prob_card)
            if country_logits is not None:
                country_probs = country_logits.masked_fill(~country_masks, 0.0)
                country_probs = country_probs / (country_probs.sum(dim=1, keepdim=True) + 1e-10)
                log_country = torch.log(country_probs + 1e-10)
                ent_country = -(country_probs * log_country).sum(dim=1)
                if country_targets.shape[1] > 0:
                    gathered = log_country.gather(1, country_targets.clamp_min(0))
                    log_prob_country = (gathered * country_valid.float()).sum(dim=1)

            new_log_probs = log_prob_card + log_prob_mode + log_prob_country

            log_p_card = F.log_softmax(masked_card, dim=1).clamp(min=-20)
            log_p_mode = F.log_softmax(masked_mode, dim=1).clamp(min=-20)
            ent_card = -(log_p_card.exp() * log_p_card).sum(dim=1)
            ent_mode = -(log_p_mode.exp() * log_p_mode).sum(dim=1)
            entropies = ent_card + ent_mode + ent_country

            ratio = torch.exp(new_log_probs - old_log_probs)
            clipped_ratio = torch.clamp(ratio, 1.0 - clip_eps, 1.0 + clip_eps)
            policy_loss = -torch.min(ratio * advantages, clipped_ratio * advantages).mean()
            value_loss = F.mse_loss(values, returns)
            entropy_loss = -entropies.mean()

            # SmallChoice auxiliary cross-entropy loss
            sc_loss = torch.tensor(0.0, device=device)
            if small_choice_logits is not None:
                sc_tgt = packed.sc_targets.index_select(0, idx)
                sc_nopt = packed.sc_n_options.index_select(0, idx)
                sc_valid = (sc_tgt >= 0) & (sc_nopt > 1)
                if sc_valid.any():
                    sc_logits_v = small_choice_logits[sc_valid]
                    sc_tgt_v = sc_tgt[sc_valid]
                    sc_nopt_v = sc_nopt[sc_valid]
                    sc_mask = torch.arange(
                        sc_logits_v.size(1), device=device
                    ).unsqueeze(0) < sc_nopt_v.unsqueeze(1)
                    sc_logits_v = sc_logits_v.masked_fill(~sc_mask, float("-inf"))
                    sc_loss = F.cross_entropy(sc_logits_v, sc_tgt_v)

            loss = policy_loss + vf_coef * value_loss + ent_coef * entropy_loss + sc_loss

            if torch.isnan(loss):
                continue

            optimizer.zero_grad(set_to_none=True)
            loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), max_norm=0.5)
            optimizer.step()

            with torch.no_grad():
                clip_frac = ((ratio - 1.0).abs() > clip_eps).float().mean().item()
                approx_kl = ((ratio - 1.0) - (new_log_probs - old_log_probs)).mean().item()

            metrics["policy_loss"] += float(policy_loss.item())
            metrics["value_loss"] += float(value_loss.item())
            metrics["sc_loss"] += float(sc_loss.item())
            metrics["entropy"] += float(entropies.mean().item())
            metrics["clip_fraction"] += clip_frac
            metrics["approx_kl"] += approx_kl
            n_updates += 1
            _epoch_kl_sum += approx_kl
            _epoch_kl_count += 1

        _epochs_run += 1
        # Per-epoch KL early stopping: if average KL this epoch exceeds target,
        # skip remaining epochs to prevent policy from drifting too far.
        if target_kl > 0 and _epoch_kl_count > 0:
            _epoch_avg_kl = _epoch_kl_sum / _epoch_kl_count
            if _epoch_avg_kl > target_kl:
                _kl_early_stopped = True
                break

    if n_updates > 0:
        for key in metrics:
            metrics[key] /= n_updates
    metrics["ppo_epochs_run"] = _epochs_run
    metrics["kl_early_stopped"] = 1.0 if _kl_early_stopped else 0.0
    return metrics


# ---------------------------------------------------------------------------
# Benchmark via benchmark_batched (fast)
# ---------------------------------------------------------------------------

def collect_policy_stats(
    script_path: str | None = None,
    n_games: int = 100,
    seed_base: int = 51000,
    steps: list | None = None,
) -> dict:
    """Compute per-phase policy statistics (mode/region/split fractions).

    Preferred: pass `steps` (Step objects from the current training rollout) to
    avoid a redundant 100-game heuristic rollout. The training rollout already
    covers league opponents which are more representative than heuristic.

    Fallback: if steps is None and script_path is provided, runs n_games vs
    the built-in heuristic (legacy behaviour, kept for standalone use).

    Returns a flat dict of W&B-loggable scalars.
    Phase labels: early=turns 1-3, mid=turns 4-7, late=turns 8-10.
    Mode names: Influence, Event, Space, Coup, Realign.
    """
    MODE_NAMES = ["Influence", "Event", "Space", "Coup", "Realign"]
    PHASES = ["early", "mid", "late"]

    def phase(turn: int) -> str:
        if turn <= 3:
            return "early"
        if turn <= 7:
            return "mid"
        return "late"

    def influence_split_label(targets: list[int]) -> str:
        """Classify allocation as concentrated / split / dispersed."""
        if not targets:
            return "none"
        from collections import Counter

        counts = sorted(Counter(targets).values(), reverse=True)
        total = sum(counts)
        if counts[0] == total:
            return "concentrated"   # all ops to one country
        if counts[0] == 1:
            return "dispersed"      # at most 1 op per country
        return "split"              # mixed

    # Build step dicts either from provided Step objects or fresh heuristic rollout
    all_step_dicts: list[dict] = []
    if steps is not None:
        # Use training rollout steps directly — more representative than heuristic
        for step in steps:
            d: dict = {
                "scalars": step.scalars.squeeze(0).numpy() if hasattr(step.scalars, "numpy") else step.scalars,
                "mode_idx": step.mode_idx,
                "country_targets": step.country_targets or [],
                "_side_name": "ussr" if step.side_int == 0 else "us",
            }
            # raw_turn from step if available, else decode from scalars
            if step.raw_turn is not None:
                d["_raw_turn"] = step.raw_turn
            all_step_dicts.append(d)
    else:
        # Legacy: run fresh games vs heuristic (only used for standalone calls)
        if script_path is None:
            return {}
        for side in [tscore.Side.USSR, tscore.Side.US]:
            try:
                _, raw_steps, _ = tscore.rollout_games_batched(
                    model_path=script_path,
                    learned_side=side,
                    n_games=n_games,
                    pool_size=min(n_games, 32),
                    seed=seed_base + (0 if side == tscore.Side.USSR else n_games),
                    device="cpu",
                    temperature=1.0,
                    nash_temperatures=True,
                )
                for s in raw_steps:
                    s["_side_name"] = "ussr" if side == tscore.Side.USSR else "us"
                all_step_dicts.extend(raw_steps)
            except Exception as e:
                print(f"  [stats] rollout failed for {side}: {e}", flush=True)
                return {}

    # Aggregate
    from collections import defaultdict

    mode_counts: dict[tuple, int] = defaultdict(int)       # (phase, side, mode_name)
    region_counts: dict[tuple, int] = defaultdict(int)     # (phase, side, region)
    split_counts: dict[tuple, int] = defaultdict(int)      # (phase, side, split_label)
    total_counts: dict[tuple, int] = defaultdict(int)      # (phase, side)
    inf_action_counts: dict[tuple, int] = defaultdict(int) # (phase, side) influence-only actions
    region_op_counts: dict[tuple, int] = defaultdict(int)  # (phase, side) influence ops
    defcon_sum: dict[tuple, float] = defaultdict(float)
    vp_sum: dict[tuple, float] = defaultdict(float)

    for s in all_step_dicts:
        scalars = s["scalars"]           # numpy (11,)
        # _raw_turn is set directly when building from Step objects; fallback decodes from scalar
        turn = int(s["_raw_turn"]) if "_raw_turn" in s else round(float(scalars[8]) * 10)
        defcon = round(float(scalars[1]) * 4 + 1)
        vp = round(float(scalars[0]) * 20)
        mode_idx = int(s["mode_idx"])
        targets = list(s["country_targets"])
        side_name = s["_side_name"]
        ph = phase(turn)
        key = (ph, side_name)

        mode_name = MODE_NAMES[mode_idx] if 0 <= mode_idx < len(MODE_NAMES) else "Unknown"
        mode_counts[(ph, side_name, mode_name)] += 1
        total_counts[key] += 1
        defcon_sum[key] += defcon
        vp_sum[key] += vp

        if mode_idx == 0 and targets:  # Influence
            for target in targets:
                region = _COUNTRY_REGION.get(target, "Unknown")
                region_counts[(ph, side_name, region)] += 1
            split_counts[(ph, side_name, influence_split_label(targets))] += 1
            inf_action_counts[key] += 1
            region_op_counts[key] += len(targets)

    # Build flat W&B dict
    stats: dict[str, float] = {}
    for ph in PHASES:
        for side_name in ["ussr", "us"]:
            key = (ph, side_name)
            n = total_counts[key]
            if n == 0:
                continue
            prefix = f"stats/{ph}/{side_name}"
            # Mode fractions
            for mn in MODE_NAMES:
                stats[f"{prefix}/mode_{mn.lower()}_frac"] = mode_counts[(ph, side_name, mn)] / n
            # Mean defcon and vp
            stats[f"{prefix}/mean_defcon"] = defcon_sum[key] / n
            stats[f"{prefix}/mean_vp"] = vp_sum[key] / n
            # Influence sub-stats
            n_region_ops = region_op_counts[key]
            if n_region_ops > 0:
                for r in _REGION_NAMES:
                    stats[f"{prefix}/region_{_REGION_KEY.get(r, r.lower())}_frac"] = (
                        region_counts[(ph, side_name, r)] / n_region_ops
                    )
            n_inf_actions = inf_action_counts[key]
            if n_inf_actions > 0:
                for label in ["concentrated", "split", "dispersed"]:
                    stats[f"{prefix}/split_{label}_frac"] = (
                        split_counts[(ph, side_name, label)] / n_inf_actions
                    )
    return stats


def _add_region_net_delta_stats(terminal_steps: list[Step], log_dict: dict) -> None:
    """Add mean terminal regional influence and control deltas to log_dict.

    Reported per side (ussr/us) × per phase (early t1-3 / mid t4-7 / late t8-10).
    Two metrics per region per slice, both BG-weighted (BG=1.0, non-BG=0.2):
      net_inf_delta   — weighted sum of (that_side_inf - opp_inf) per country
      net_ctrl_delta  — weighted sum of (that_side controls - opp controls) per country
                        where control = influence > stability

    SE Asia countries are counted in both SoutheastAsia AND Asia buckets (SE Asia is a
    scoring subset of Asia, not disjoint from it).
    BG-weighting prevents high-stability non-BG countries from dominating the delta.
    """
    if not _COUNTRY_REGION or not _COUNTRY_STABILITY:
        return

    _PHASES = {"early": (1, 3), "mid": (4, 7), "late": (8, 10)}
    _SIDES = {0: "ussr", 1: "us"}

    # Accumulators: (side_int, phase_name, region) -> float
    inf_totals: dict[tuple, float] = {}
    ctrl_totals: dict[tuple, float] = {}
    counts: dict[tuple, int] = {}
    for side_int in (0, 1):
        for phase in _PHASES:
            for region in _REGION_NAMES:
                k = (side_int, phase, region)
                inf_totals[k] = 0.0
                ctrl_totals[k] = 0.0
                counts[k] = 0

    for step in terminal_steps:
        if step.raw_ussr_influence is None or step.raw_us_influence is None:
            continue
        turn = step.raw_turn or 0
        phase = "early" if turn <= 3 else ("mid" if turn <= 7 else "late")

        for side_int, side_name in _SIDES.items():
            if side_int == 0:
                model_inf = step.raw_ussr_influence
                opp_inf = step.raw_us_influence
            else:
                model_inf = step.raw_us_influence
                opp_inf = step.raw_ussr_influence

            for region, country_ids in _REGION_COUNTRY_IDS.items():
                k = (side_int, phase, region)
                for cid in country_ids:
                    w = _COUNTRY_BG_WEIGHT.get(cid, 0.2)
                    stab = _COUNTRY_STABILITY.get(cid, 1)
                    inf_totals[k] += w * (model_inf[cid] - opp_inf[cid])
                    model_ctrl = 1 if model_inf[cid] > stab else 0
                    opp_ctrl = 1 if opp_inf[cid] > stab else 0
                    ctrl_totals[k] += w * (model_ctrl - opp_ctrl)
                counts[k] += 1

    for side_int, side_name in _SIDES.items():
        for phase in _PHASES:
            for region in _REGION_NAMES:
                k = (side_int, phase, region)
                n = counts[k]
                if n == 0:
                    continue
                rkey = _REGION_KEY[region]
                prefix = f"stats/{side_name}_{phase}"
                log_dict[f"{prefix}/region_{rkey}_net_inf_delta"] = inf_totals[k] / n
                log_dict[f"{prefix}/region_{rkey}_net_ctrl_delta"] = ctrl_totals[k] / n


def _add_scalar_weight_norms(model: nn.Module, log_dict: dict) -> None:
    """Add scalar_encoder weight norms to log_dict for W&B tracking.

    Tracks three slices of scalar_encoder.weight:
      new_scalar_weight_norm  — L2 norm of cols 11:32 (the 21 new active-effect features)
                                Should grow from ~0.05 (random init) as model learns to use them.
                                If stays near initial value after 50 iters → features not learned.
      core_scalar_weight_norm — L2 norm of cols 0:11 (original 11 features, should stay stable)
      region_scalar_weight_norm — L2 norm of cols 32:60 (region scalars, for GNN-side models)
    """
    if not hasattr(model, "scalar_encoder"):
        return
    w = model.scalar_encoder.weight.detach()  # (hidden_dim, input_dim)
    input_dim = w.shape[1]
    log_dict["core_scalar_weight_norm"] = float(w[:, :11].norm().item())
    if input_dim >= 32:
        log_dict["new_scalar_weight_norm"] = float(w[:, 11:32].norm().item())
    if input_dim >= 60:
        log_dict["region_scalar_weight_norm"] = float(w[:, 32:60].norm().item())


def _save_rollout_parquet(
    steps: list[Step],
    out_dir: str,
    iteration: int,
    base_seed: int = 0,
    checkpoint_path: str = "",
) -> None:
    """Save rollout steps to Parquet for BC bootstrapping.

    Each row contains the raw feature tensors and action labels from a PPO step,
    in the same format as the BC dataset (influence, cards, scalars, card_id, mode_id,
    country_targets, side_int, reward). Saved to out_dir/rollout_iter_{N:04d}.parquet.

    For future re-encoding with different features: game seeds are deterministic as
    base_seed + game_index. With the checkpoint and seeds, any game can be replayed
    using collect_selfplay_rows_jsonl to get full JSONL → re-encode to any feature format.
    The out_dir/rollout_iter_{N:04d}.meta.json file records base_seed and checkpoint_path
    for this purpose.

    These files can be used to warm-start BC training from PPO data without re-running games.
    """
    try:
        import pyarrow as pa
        import pyarrow.parquet as pq
    except ImportError:
        print("  [rollout-save] pyarrow not available, skipping Parquet save", flush=True)
        return

    Path(out_dir).mkdir(parents=True, exist_ok=True)
    out_path = Path(out_dir) / f"rollout_iter_{iteration:04d}.parquet"
    meta_path = Path(out_dir) / f"rollout_iter_{iteration:04d}.meta.json"

    inf_list = [s.influence[0].numpy().tolist() for s in steps]
    cards_list = [s.cards[0].numpy().tolist() for s in steps]
    scalars_list = [s.scalars[0].numpy().tolist() for s in steps]
    card_ids = [s.card_idx + 1 for s in steps]           # 1-indexed card_id
    mode_ids = [s.mode_idx for s in steps]
    # country_targets: list of int (0-indexed). Store as list<int32>.
    country_targets = [s.country_targets for s in steps]
    side_ints = [s.side_int for s in steps]
    rewards = [s.reward for s in steps]
    values = [s.value for s in steps]
    gae_returns = [s.returns for s in steps]   # GAE return target (value + TD-lambda advantage)

    # Policy logits — present when steps were collected via Python sequential callback.
    # None when collected via C++ batched rollout (tscore doesn't return logits).
    has_logits = steps[0].card_logits is not None if steps else False

    # Raw game state columns — present when steps were collected with raw state support.
    has_raw = steps[0].raw_ussr_influence is not None if steps else False

    table_dict: dict = {
        "influence": pa.array(inf_list, type=pa.list_(pa.float32())),
        "cards": pa.array(cards_list, type=pa.list_(pa.float32())),
        "scalars": pa.array(scalars_list, type=pa.list_(pa.float32())),
        "card_id": pa.array(card_ids, type=pa.int32()),
        "mode_id": pa.array(mode_ids, type=pa.int32()),
        "country_targets": pa.array(country_targets, type=pa.list_(pa.int32())),
        "side_int": pa.array(side_ints, type=pa.int8()),
        "reward": pa.array(rewards, type=pa.float32()),
        "value": pa.array(values, type=pa.float32()),
        "gae_return": pa.array(gae_returns, type=pa.float32()),  # GAE target for value training
        "iteration": pa.array([iteration] * len(steps), type=pa.int32()),
    }
    if has_logits:
        # card_logits: (111,) raw logits before masking — used for KL-distillation in arch sweep
        # mode_logits: (5,) raw logits before masking
        # country_logits: (86,) probability mixture from model (not raw logits — model output)
        table_dict["card_logits"] = pa.array(
            [s.card_logits for s in steps], type=pa.list_(pa.float32()))
        table_dict["mode_logits"] = pa.array(
            [s.mode_logits for s in steps], type=pa.list_(pa.float32()))
        table_dict["country_logits"] = pa.array(
            [s.country_logits if s.country_logits is not None else [0.0] * 86
             for s in steps], type=pa.list_(pa.float32()))
    if has_raw:
        table_dict["raw_ussr_influence"] = pa.array(
            [s.raw_ussr_influence for s in steps], type=pa.list_(pa.int16()))
        table_dict["raw_us_influence"] = pa.array(
            [s.raw_us_influence for s in steps], type=pa.list_(pa.int16()))
        table_dict["raw_turn"]   = pa.array([s.raw_turn for s in steps],   type=pa.int8())
        table_dict["raw_ar"]     = pa.array([s.raw_ar for s in steps],     type=pa.int8())
        table_dict["raw_defcon"] = pa.array([s.raw_defcon for s in steps], type=pa.int8())
        table_dict["raw_vp"]     = pa.array([s.raw_vp for s in steps],     type=pa.int16())
        table_dict["raw_milops"] = pa.array(
            [s.raw_milops for s in steps], type=pa.list_(pa.int8()))
        table_dict["raw_space"]  = pa.array(
            [s.raw_space for s in steps], type=pa.list_(pa.int8()))
        table_dict["hand_card_ids"] = pa.array(
            [s.hand_card_ids for s in steps], type=pa.list_(pa.int16()))
    table = pa.table(table_dict)
    pq.write_table(table, out_path, compression="zstd", compression_level=9)

    # Save replay metadata: checkpoint + seed allows exact game reconstruction
    # via: collect_selfplay_rows_jsonl --model checkpoint --seed base_seed+game_index
    meta = {
        "iteration": iteration,
        "n_steps": len(steps),
        "base_seed": base_seed,
        "checkpoint_path": checkpoint_path,
        "replay_note": (
            "To re-encode with new features: replay games using "
            "collect_selfplay_rows_jsonl with checkpoint_path and seeds "
            "[base_seed, base_seed+1, ..., base_seed+n_games-1]"
        ),
    }
    meta_path.write_text(json.dumps(meta, indent=2))
    print(f"  [rollout-save] {len(steps):,} steps → {out_path} (meta: {meta_path.name})", flush=True)



def run_h2h_eval(
    model: nn.Module,
    opponent_script: str,
    n_games: int = 200,
    seed: int = 70000,
) -> dict[str, float]:
    """Head-to-head eval: current model vs opponent scripted checkpoint.

    Runs n_games total (half as USSR, half as US) using benchmark_model_vs_model_batched.
    Returns win rates from the current model's perspective.
    """
    fd, our_script = tempfile.mkstemp(prefix="ppo_h2h_eval_", suffix="_scripted.pt")
    os.close(fd)
    try:
        _export_torchscript_model(model, our_script, warn_only=False)
        half = n_games // 2
        # First half: our model = USSR
        results_ussr = tscore.benchmark_model_vs_model_batched(
            model_a_path=our_script,
            model_b_path=opponent_script,
            n_games=half,
            pool_size=min(32, half),
            seed=seed,
            device="cpu",
            temperature=0.0,
        )
        # Second half: our model = US
        results_us = tscore.benchmark_model_vs_model_batched(
            model_a_path=opponent_script,
            model_b_path=our_script,
            n_games=half,
            pool_size=min(32, half),
            seed=seed + half,
            device="cpu",
            temperature=0.0,
        )
        ussr_wins = sum(1 for r in results_ussr if r.winner == tscore.Side.USSR)
        us_wins = sum(1 for r in results_us if r.winner == tscore.Side.US)
        ussr_wr = ussr_wins / max(1, len(results_ussr))
        us_wr = us_wins / max(1, len(results_us))
        combined = (ussr_wins + us_wins) / max(1, len(results_ussr) + len(results_us))
        return {"h2h_ussr_wr": ussr_wr, "h2h_us_wr": us_wr, "h2h_combined_wr": combined}
    finally:
        for p in (our_script, our_script.replace(".pt", "_scripted.pt")):
            try:
                os.remove(p)
            except OSError:
                pass


def _panel_eval_worker(
    our_script: str,
    panel: list,
    n_games_per_opp: int,
    seed: int,
    result_path: str,
) -> None:
    """Module-level function (required for multiprocessing fork/spawn).
    Runs panel eval entirely on CPU, writes JSON result file.
    """
    import json
    import sys
    from pathlib import Path as _Path

    try:
        import tscore as _tscore
    except ImportError:
        for bd in ["build-ninja/bindings", "build/bindings"]:
            bd_path = _Path(__file__).parent.parent / bd
            if bd_path.exists():
                sys.path.insert(0, str(bd_path))
                break
        import tscore as _tscore

    results = {}
    half = max(2, n_games_per_opp // 2)
    pool = min(32, half)

    for opp in panel:
        if opp == HEURISTIC_FIXTURE:
            opp_name = "heuristic"
            try:
                r_ussr = _tscore.benchmark_batched(our_script, _tscore.Side.USSR, half, pool_size=pool, seed=seed, nash_temperatures=False)
                r_us = _tscore.benchmark_batched(our_script, _tscore.Side.US, half, pool_size=pool, seed=seed + half, nash_temperatures=False)
                ussr_wins = sum(1 for r in r_ussr if r.winner == _tscore.Side.USSR)
                us_wins = sum(1 for r in r_us if r.winner == _tscore.Side.US)
            except Exception as e:
                results[opp_name] = {"error": str(e)}
                continue
        else:
            opp_name = _Path(opp).stem.replace("_scripted", "")
            try:
                # Single call: our_script=model_a plays both sides (first half as USSR,
                # second half as US). Count only our model's wins using result ordering.
                # Bug note: the old two-call approach counted total USSR/US wins across
                # both halves of each call, which always summed to ~n_games/2 regardless
                # of opponent strength (always ~0.5 combined WR).
                n_total = max(4, n_games_per_opp)
                # temperature=1.0 matches rollout conditions and keeps WR in the
                # 30-60% discriminating range. temperature=0.0 (greedy) inflates WR
                # to 85-90% even against 2092 ELO opponents (tiny logit differences
                # compound over 100+ moves), making the panel useless for tracking.
                r = _tscore.benchmark_model_vs_model_batched(
                    model_a_path=our_script, model_b_path=opp, n_games=n_total,
                    pool_size=pool, seed=seed, device="cpu", temperature=1.0,
                )
                half_c = len(r) // 2
                # Games 0..half_c-1: our_script=USSR, opponent=US
                ussr_wins = sum(1 for i, r_ in enumerate(r) if i < half_c and r_.winner == _tscore.Side.USSR)
                # Games half_c..end: our_script=US, opponent=USSR
                us_wins = sum(1 for i, r_ in enumerate(r) if i >= half_c and r_.winner == _tscore.Side.US)
            except Exception as e:
                results[opp_name] = {"error": str(e)}
                continue
        results[opp_name] = {
            "ussr_wr": ussr_wins / max(1, half),
            "us_wr": us_wins / max(1, half),
            "combined_wr": (ussr_wins + us_wins) / max(1, half * 2),
        }

    with open(result_path, "w") as f:
        json.dump(results, f, indent=2)


def _export_torchscript_model(model: nn.Module, script_path: str, *, warn_only: bool = False) -> None:
    """Export a device-agnostic TorchScript copy of the current model to disk."""
    orig_device = next(model.parameters()).device
    was_training = model.training
    model_cpu = model.cpu()
    model_cpu.eval()
    try:
        try:
            scripted = torch.jit.script(model_cpu)
        except Exception:
            # Use SCALAR_DIM (32) for trace — this is what C++ sends.
            # Models with region_encoder internally extend scalars before
            # scalar_encoder, so scalar_encoder.weight.shape[1] > SCALAR_DIM.
            example_inputs = (
                torch.zeros((1, 172), dtype=torch.float32),
                torch.zeros((1, 448), dtype=torch.float32),
                torch.zeros((1, SCALAR_DIM), dtype=torch.float32),
            )
            scripted = torch.jit.trace(model_cpu, example_inputs, strict=False)
        scripted.save(script_path)
    except Exception as e:
        if warn_only:
            print(f"  Warning: TorchScript save failed: {e}", flush=True)
        else:
            raise
    finally:
        model.to(orig_device)
        model.train(was_training)


def _export_temp_model(model: nn.Module) -> str:
    """Write a temporary TorchScript model file and return its path."""
    fd, script_path = tempfile.mkstemp(prefix="ppo_rollout_", suffix="_scripted.pt")
    os.close(fd)
    _export_torchscript_model(model, script_path)
    return script_path


def export_checkpoint(
    model: nn.Module,
    checkpoint_path: str,
    ckpt_meta: dict,
    optimizer: Optional[torch.optim.Optimizer] = None,
) -> None:
    """Save model checkpoint atomically (write to .tmp then rename).

    Direct torch.save to the target path is not atomic: a kill/crash mid-write
    leaves a corrupt file at the target path. After the rename the file is either
    fully present or absent — never corrupt. The previous checkpoint is only
    deleted AFTER this rename succeeds, so there is always at least one valid
    checkpoint on disk.
    """
    tmp_path = checkpoint_path + ".tmp"
    payload = {"model_state_dict": model.state_dict(), "args": ckpt_meta}
    if optimizer is not None:
        payload["optimizer_state_dict"] = optimizer.state_dict()
    torch.save(payload, tmp_path)
    os.replace(tmp_path, checkpoint_path)  # atomic on Linux (same filesystem)
    script_path = checkpoint_path.replace(".pt", "_scripted.pt")
    _export_torchscript_model(model, script_path, warn_only=True)

    # Update pointer file so restart scripts always know the latest valid checkpoint
    # without having to guess the iteration number.
    pointer_path = os.path.join(os.path.dirname(checkpoint_path), "latest_checkpoint.txt")
    tmp_ptr = pointer_path + ".tmp"
    with open(tmp_ptr, "w") as f:
        f.write(checkpoint_path)
    os.replace(tmp_ptr, pointer_path)


def _derive_version(out_dir: str) -> str:
    version = Path(out_dir).name
    if version.startswith("ppo_"):
        version = version.removeprefix("ppo_")
    if version.endswith("_league"):
        version = version.removesuffix("_league")
    return version or Path(out_dir).name


def _flat_checkpoint_path(out_dir: str, version: str, iteration: int) -> str:
    return os.path.join(out_dir, f"{version}.iter{iteration:04d}.pt")


def _legacy_checkpoint_path(out_dir: str, iteration: int) -> str:
    return os.path.join(out_dir, f"ppo_iter{iteration:04d}.pt")


def _remove_if_exists(path: str) -> None:
    try:
        os.remove(path)
    except FileNotFoundError:
        pass
    except OSError:
        pass


def _write_compat_alias(src_path: str, alias_path: str) -> None:
    _remove_if_exists(alias_path)
    try:
        os.symlink(os.path.basename(src_path), alias_path)
    except OSError:
        shutil.copy2(src_path, alias_path)


# ---------------------------------------------------------------------------
# Main training loop
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="PPO fine-tuning for Twilight Struggle AI")
    p.add_argument("--checkpoint", required=True, help="BC checkpoint to warm-start from")
    p.add_argument("--reset-optimizer", action="store_true",
                   help="Ignore optimizer state in checkpoint; start fresh Adam. "
                        "Use when restarting from a checkpoint trained under different code.")
    p.add_argument("--out-dir", required=True, help="Directory for PPO checkpoints")
    p.add_argument("--version", default=None,
                   help="Checkpoint version prefix. Defaults to deriving from --out-dir, "
                        "e.g. ppo_v79_sc_league -> v79_sc.")
    p.add_argument("--n-iterations", type=int, default=200, help="PPO iterations")
    p.add_argument("--games-per-iter", type=int, default=200, help="Games per rollout batch")
    p.add_argument("--ppo-epochs", type=int, default=4, help="PPO update epochs per batch")
    p.add_argument("--clip-eps", type=float, default=0.2, help="PPO clip epsilon")
    p.add_argument("--lr", type=float, default=1e-4, help="Learning rate (after warmup)")
    p.add_argument("--lr-warmup-iters", type=int, default=0,
                   help="Number of iterations to linearly warm up LR from lr/10 to lr. "
                        "Use 15 when resuming from a checkpoint with new input features "
                        "to prevent early noisy gradients from destabilizing learned weights.")
    p.add_argument("--gamma", type=float, default=0.99, help="Discount factor")
    p.add_argument("--gae-lambda", type=float, default=0.95, help="GAE lambda")
    p.add_argument("--ent-coef", type=float, default=0.01, help="Initial entropy coefficient")
    p.add_argument("--ent-coef-final", type=float, default=None,
                   help="Final entropy coefficient (linear decay). None = constant")
    p.add_argument("--global-ent-decay-start", type=int, default=400,
                   help="Global total iteration where entropy decay begins (across all chained runs)")
    p.add_argument("--global-ent-decay-end", type=int, default=2000,
                   help="Global total iteration where entropy reaches ent_coef_final")
    p.add_argument("--vf-coef", type=float, default=0.5, help="Value function coefficient")
    p.add_argument("--minibatch-size", type=int, default=2048, help="PPO minibatch size")
    p.add_argument("--eval-opponent", type=str, default=None,
                   help="[DEPRECATED] Use --eval-panel instead. Single scripted .pt to eval against.")
    p.add_argument("--eval-panel", nargs="*", default=[],
                   help="Fixed panel of opponents for async background eval. Accepts paths to scripted .pt files "
                        "or '__heuristic__'. Evals all opponents in parallel process so training is not blocked. "
                        "Results logged to W&B under panel/<opponent>_combined_wr. Does NOT affect checkpoint selection "
                        "(ppo_best.pt = ppo_final.pt).")
    p.add_argument("--eval-every", type=int, default=20,
                   help="Run panel eval every N iterations (default: 20)")
    p.add_argument("--side", choices=["ussr", "us", "both"], default="both",
                   help="Which side to train as")
    p.add_argument("--self-play", action="store_true",
                   help="Train via self-play (both sides use learned model) instead of vs heuristic")
    p.add_argument("--self-play-heuristic-mix", type=float, default=0.2,
                   help="Fraction of games to play vs heuristic when --self-play is active (collapse anchor)")
    p.add_argument("--seed", type=int, default=99000, help="Base random seed")
    p.add_argument("--device", default="cuda", help="torch device")
    p.add_argument("--wandb", action="store_true", help="Enable W&B logging")
    p.add_argument("--wandb-project", default="twilight-struggle-ai", help="W&B project")
    p.add_argument("--wandb-run-name", default=None, help="W&B run name")
    p.add_argument("--max-kl", type=float, default=0.1, help="Early stop entire run if KL > this")
    p.add_argument("--ema-decay", type=float, default=0.995,
                   help="EMA decay for model weights (0 to disable). EMA model is used for "
                        "panel eval and checkpoint export. Smooths out per-iteration noise.")
    p.add_argument("--target-kl", type=float, default=0.015,
                   help="Per-epoch KL early stopping threshold. When avg KL in a PPO epoch "
                        "exceeds this, remaining epochs are skipped. Smooths training by "
                        "preventing large policy updates. 0 to disable.")
    p.add_argument("--vp-reward-coef", type=float, default=0.0,
                   help="VP delta reward shaping coefficient (0 = disabled)")
    p.add_argument("--reward-shaping", action="store_true",
                   help="Enable shaped rewards (VP trajectory + turn length bonus)")
    p.add_argument("--reward-alpha", type=float, default=0.5,
                   help="Overall shaping weight (default: 0.5)")
    p.add_argument("--league", type=str, default=None,
                   help="League directory for checkpoint pool self-play (enables league training)")
    p.add_argument("--league-save-every", type=int, default=10,
                   help="Save model to league pool every N iterations (default: 10)")
    p.add_argument("--league-mix-k", type=int, default=4,
                   help="Number of distinct opponents to sample per iteration (default: 4)")
    p.add_argument("--rollout-workers", type=int, default=1,
                   help="Parallel threads for rollout collection (default: 1; >1 added overhead for vs-model rollout)")
    p.add_argument("--league-fixtures", nargs="*", default=[],
                   help="Permanent fixture scripted .pt paths for both sides (union fallback if "
                        "--ussr-league-fixtures/--us-league-fixtures not provided)")
    p.add_argument("--ussr-league-fixtures", nargs="*", default=None,
                   help="Fixture pool for USSR-side opponent sampling (JSD-deduped USSR pool). "
                        "If omitted, falls back to --league-fixtures.")
    p.add_argument("--us-league-fixtures", nargs="*", default=None,
                   help="Fixture pool for US-side opponent sampling (JSD-deduped US pool). "
                        "If omitted, falls back to --league-fixtures.")
    p.add_argument("--heuristic-floor", type=float, default=0.0,
                   help="Minimum selection probability for __heuristic__ in PFSP pool. "
                        "Prevents heuristic starvation when model WR→1 drives symmetric "
                        "PFSP weight to zero. 0.15 = heuristic gets ≥15%% of opponent slots. "
                        "0.0 = no floor (legacy). Recommended: 0.15 for stable general strength.")
    p.add_argument("--league-recency-tau", type=float, default=20.0,
                   help="Recency half-life for past-self checkpoint sampling. "
                        "weight=exp(rank/tau); higher=more uniform, lower=more recency bias (default: 20)")
    p.add_argument("--league-heuristic-pct", type=float, default=0.0,
                   help="[DEPRECATED] Fraction of non-self league slots assigned to heuristic opponent. "
                        "Default changed to 0.0. Pass '__heuristic__' in --league-fixtures instead for "
                        "proper PFSP tracking. Setting this >0 will print a deprecation warning.")
    p.add_argument("--league-fixture-fadeout", type=int, default=50,
                   help="Hard-remove fixtures from pool after this many iterations (default: 50)")
    p.add_argument("--league-self-slot", action=argparse.BooleanOptionalAction, default=True,
                   help="Reserve slot 0 for current model (true self-play). --no-league-self-slot to disable.")
    p.add_argument("--pfsp-exponent", type=float, default=1.0,
                   help="PFSP exponent: opponent sampling weight = (1-WR)^p. 1.0=linear, 2.0=squared. "
                        "Defaults to 0.5 WR until 20 games played vs that opponent.")
    p.add_argument("--dir-alpha", type=float, default=0.0,
                   help="Dirichlet noise alpha at C++ rollout root (0=disabled, 0.3=AlphaZero default). "
                        "Silently no-ops if C++ binding does not support it yet.")
    p.add_argument("--dir-epsilon", type=float, default=0.25,
                   help="Dirichlet noise mixing weight (default 0.25, only active when --dir-alpha > 0).")
    p.add_argument("--upgo", action="store_true", default=False,
                   help="Enable UPGO (Upgoing Policy Update): G_t = r_t + γ*max(V(s+1), G(t+1)). "
                        "Overrides GAE advantages; leaves `returns` unchanged for value function.")
    p.add_argument("--start-iteration", type=int, default=1,
                   help="Resume: start loop from this iteration (seeds offset accordingly)")
    p.add_argument("--best-combined", type=float, default=0.0,
                   help="(deprecated, ignored) best combined WR was used for heuristic-based selection")
    p.add_argument("--save-rollout-parquet", type=str, default=None,
                   help="If set, save each iteration's rollout steps as Parquet to this directory "
                        "(for BC bootstrapping from PPO data). One file per iteration.")
    p.add_argument("--jsd-probe-path", "--probe-set", dest="jsd_probe_path",
                   type=str, default="data/probe_positions.parquet",
                   help="Path to probe_positions.parquet for JSD evaluation")
    p.add_argument("--jsd-probe-interval", "--probe-every", dest="jsd_probe_interval",
                   type=int, default=10,
                   help="Compute JSD probe every K iterations (0=disabled)")
    p.add_argument("--jsd-probe-bc-checkpoint", "--probe-bc-checkpoint",
                   dest="jsd_probe_bc_checkpoint", type=str,
                   default="data/checkpoints/bc_wide384/scripted.pt",
                   help="BC baseline checkpoint for JSD comparison")
    p.add_argument("--rollout-temp", type=float, default=1.0,
                   help="Softmax temperature for C++ batched rollouts (>1.0 = more exploration). "
                        "Default 1.0. Recommended: 1.2 for exploration phase.")
    p.add_argument("--explore-alpha", type=float, default=0.0,
                   help="Dirichlet alpha for card-selection noise in sequential rollouts "
                        "(0=disabled, 0.3=standard AlphaZero setting).")
    p.add_argument("--explore-eps", type=float, default=0.0,
                   help="Epsilon weight for Dirichlet noise mixing (0=disabled, 0.25=standard). "
                        "Only active when --explore-alpha > 0.")
    p.add_argument("--skip-smoke-test", action="store_true", default=False,
                   help="Skip the pre-training smoke test (10 games) that validates the checkpoint.")
    p.add_argument("--post-train-hook", type=str, default=None,
                   help="Shell command to run after training completes (non-blocking, in background). "
                        "The placeholder {out_dir} is replaced with the actual out-dir path. "
                        "Example: 'bash scripts/post_train_confirm.sh {out_dir}'")
    p.add_argument("--experiment", type=str, default=None,
                   help="Experiment name for tracking (informational only)")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    if args.version is None:
        args.version = _derive_version(args.out_dir)

    # ── Singleton guard: prevent duplicate training runs ──────────────────────
    # Uses an exclusive flock so the lock auto-releases if the process crashes.
    # Any second invocation (health_check restart, stray autonomous loop, etc.)
    # will see the lock held and exit immediately with a clear error message.
    _lock_path = Path("results/train_ppo.lock")
    _lock_path.parent.mkdir(parents=True, exist_ok=True)
    _lock_fd = open(_lock_path, "w")
    try:
        fcntl.flock(_lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        # Read the PID from the lockfile to report it
        try:
            _lock_fd2 = open(_lock_path)
            _held_by = _lock_fd2.read().strip()
            _lock_fd2.close()
        except Exception:
            _held_by = "unknown"
        print(
            f"[train_ppo] ABORT: another instance is already running (lock held by PID {_held_by}).\n"
            "  Only one train_ppo.py may run at a time (GPU singleton).\n"
            "  Kill the existing process first, then retry.",
            file=sys.stderr,
        )
        sys.exit(1)
    _lock_fd.write(str(os.getpid()))
    _lock_fd.flush()
    # lock_fd intentionally kept open for process lifetime; closed on exit

    # Renice the whole process group to nice 10 so training doesn't starve
    # interactive work. os.setpriority covers the calling process; the rollout
    # worker children inherit the priority automatically.
    try:
        import signal as _signal
        _pgid = os.getpgid(0)
        os.setpriority(os.PRIO_PGRP, _pgid, 10)
    except Exception:
        pass  # non-fatal — Linux-only, ignore on other platforms
    # ─────────────────────────────────────────────────────────────────────────

    if args.league_heuristic_pct > 0:
        print(
            f"\n[DEPRECATED] --league-heuristic-pct={args.league_heuristic_pct} is deprecated and will be removed.\n"
            "  The coin-flip approach gives P(zero heuristic games) = (1-pct)^k per iteration.\n"
            "  Instead, add '__heuristic__' to --league-fixtures for proper PFSP tracking:\n"
            "    --league-fixtures <path1> <path2> __heuristic__\n"
            "  Setting to 0.0 for this run.\n",
            file=sys.stderr,
        )
        args.league_heuristic_pct = 0.0

    os.makedirs(args.out_dir, exist_ok=True)

    # Save args for reproducibility
    with open(os.path.join(args.out_dir, "ppo_args.json"), "w") as f:
        json.dump(vars(args), f, indent=2)

    # W&B setup
    wandb_run = None
    if args.wandb:
        try:
            import wandb
            api_key_path = Path(__file__).parent.parent / ".wandb-api-key.txt"
            if api_key_path.exists():
                os.environ["WANDB_API_KEY"] = api_key_path.read_text().strip()
            run_name = args.wandb_run_name or f"ppo_{Path(args.out_dir).name}"
            # Stable run_id derived from out_dir so restarts resume the same W&B run.
            # Stored in out_dir/wandb_run_id.txt to survive process restarts.
            run_id_file = Path(args.out_dir) / "wandb_run_id.txt"
            if run_id_file.exists():
                run_id = run_id_file.read_text().strip()
            else:
                import hashlib
                run_id = hashlib.md5(str(Path(args.out_dir).resolve()).encode()).hexdigest()[:8]
                run_id_file.write_text(run_id)
            wandb_run = wandb.init(
                project=args.wandb_project,
                name=run_name,
                id=run_id,
                resume="allow",
                config=vars(args),
            )
        except Exception as e:
            print(f"W&B init failed: {e}, continuing without logging")
            wandb_run = None

    if _TRACKING_AVAILABLE:
        try:
            _log_exp_start(
                name=str(args.out_dir) if hasattr(args, "out_dir") else "ppo_run",
                hypothesis="PPO self-play training run",
                command=" ".join(sys.argv),
                wandb_id=wandb_run.id if wandb_run is not None else None,
            )
        except Exception as _e:
            print(f"[tracking] log_experiment_start failed: {_e}")

    device = args.device
    if device == "cuda" and not torch.cuda.is_available():
        print("CUDA not available, falling back to CPU")
        device = "cpu"

    print(f"Loading checkpoint: {args.checkpoint}")
    model, model_type, ckpt_args = load_model(args.checkpoint, device)
    global_iter_offset = int(ckpt_args.get("total_iters", 0))

    if _TRACKING_AVAILABLE and not args.skip_smoke_test:
        try:
            _ok, _msg = _run_smoke_test(Path(args.checkpoint))
            if not _ok:
                print(f"[smoke test] FAILED: {_msg}")
                print("Use --skip-smoke-test to bypass.")
                raise SystemExit(1)
            print(f"[smoke test] {_msg}")
        except SystemExit:
            raise
        except Exception as _e:
            print(f"[smoke test] Error (non-fatal): {_e}")

    probe_eval = None
    probe_bc_model = None
    rolling_ckpt_keep = 1
    if args.jsd_probe_interval > 0:
        probe_path = Path(args.jsd_probe_path)
        if probe_path.exists():
            from tsrl.policies.jsd_probe import ProbeEvaluator, load_probe_model

            probe_eval = ProbeEvaluator(probe_path, device=device)
            rolling_ckpt_keep = max(1, args.jsd_probe_interval)
            probe_bc_path = Path(args.jsd_probe_bc_checkpoint)
            if probe_bc_path.exists():
                probe_bc_model = load_probe_model(probe_bc_path, device=device)
        else:
            print(f"  [jsd] probe set missing at {probe_path}; skipping JSD probe.", flush=True)

    # Keep a copy of BC checkpoint args for saving
    ckpt_meta = dict(ckpt_args)
    ckpt_meta["model_type"] = model_type
    ckpt_meta["version"] = args.version

    # Card specs for DEFCON safety and ops values
    from tsrl.etl.game_data import load_cards
    card_specs = load_cards()

    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr)
    # Restore optimizer state if checkpoint contains it (PPO resume, not BC warm-start).
    # Skip if --reset-optimizer is set (e.g. restarting from a checkpoint trained under different code).
    if getattr(args, "reset_optimizer", False):
        print("  --reset-optimizer: skipping optimizer state restore, starting fresh Adam.", flush=True)
    else:
        _opt_ckpt = torch.load(args.checkpoint, map_location="cpu", weights_only=False)
        if isinstance(_opt_ckpt, dict) and "optimizer_state_dict" in _opt_ckpt:
            try:
                optimizer.load_state_dict(_opt_ckpt["optimizer_state_dict"])
                # Move optimizer state tensors to the training device.
                for state in optimizer.state.values():
                    for k, v in state.items():
                        if isinstance(v, torch.Tensor):
                            state[k] = v.to(device)
                print("  Restored optimizer state from checkpoint.", flush=True)
            except Exception as e:
                print(f"  [warn] Could not restore optimizer state: {e}", flush=True)
        del _opt_ckpt

    # EMA (exponential moving average) model weights for smoother evaluation.
    # The live model trains normally; the EMA model is a smoothed version used for
    # panel eval, league pool export, and final checkpoint. This prevents the
    # oscillation pattern where single-iteration checkpoints regress.
    _ema_decay = args.ema_decay
    _ema_state: dict[str, torch.Tensor] | None = None
    if _ema_decay > 0:
        _ema_state = {k: v.clone().detach() for k, v in model.state_dict().items()}
        print(f"  EMA enabled: decay={_ema_decay}", flush=True)

    def _update_ema() -> None:
        """Update EMA weights: ema = decay * ema + (1 - decay) * current."""
        if _ema_state is None:
            return
        with torch.no_grad():
            for k, v in model.state_dict().items():
                if v.is_floating_point():
                    _ema_state[k].mul_(_ema_decay).add_(v, alpha=1.0 - _ema_decay)
                else:
                    _ema_state[k].copy_(v)  # bool/int params: just copy

    def _apply_ema() -> dict[str, torch.Tensor]:
        """Swap EMA weights into model, return original state for restore."""
        if _ema_state is None:
            return {}
        original = {k: v.clone() for k, v in model.state_dict().items()}
        model.load_state_dict(_ema_state)
        return original

    def _restore_from_ema(original: dict[str, torch.Tensor]) -> None:
        """Restore original (non-EMA) weights after eval/export."""
        if original:
            model.load_state_dict(original)

    # Determine training sides
    if args.side == "ussr":
        sides = [tscore.Side.USSR]
    elif args.side == "us":
        sides = [tscore.Side.US]
    else:
        sides = [tscore.Side.USSR, tscore.Side.US]

    games_per_side = args.games_per_iter // len(sides)

    # Keep enough rolling checkpoints on disk to compare against iteration-K
    # when the JSD probe is enabled. Milestone checkpoints are never deleted.

    def _is_milestone(it: int) -> bool:
        return it % args.eval_every == 0 or it == args.n_iterations

    def _find_rolling_checkpoint(it: int) -> str | None:
        candidates = (
            _flat_checkpoint_path(args.out_dir, args.version, it),
            _legacy_checkpoint_path(args.out_dir, it),
        )
        for candidate in candidates:
            if os.path.exists(candidate):
                return candidate
        return None

    # Async panel eval state (non-blocking: runs in background Process)
    import multiprocessing as _mp
    _panel_proc: "_mp.Process | None" = None
    _panel_result_path: "str | None" = None
    _panel_script_path: "str | None" = None
    _panel_trigger_iter: int = 0

    print(f"\nStarting PPO training: {args.n_iterations} iterations × "
          f"{args.games_per_iter} games/iter, side={args.side}", flush=True)
    print(f"Device: {device}, lr={args.lr}, clip={args.clip_eps}, "
          f"ent={args.ent_coef}, vf={args.vf_coef}", flush=True)
    if args.league:
        print(f"League training enabled (pool: {args.league}, save-every={args.league_save_every})", flush=True)
    elif args.self_play:
        print(f"Self-play enabled (heuristic mix={args.self_play_heuristic_mix:.3f})", flush=True)
    if args.start_iteration > 1:
        print(f"Resuming from iteration {args.start_iteration}", flush=True)

    t_start = time.time()
    best_ckpt_path = os.path.join(args.out_dir, "ppo_best.pt")
    # Option F: track panel high-water mark to avoid warm-starting next run from ppo_final.pt
    # (which is systematically the worst checkpoint ~83% of runs per Opus analysis 2026-04-12).
    _panel_best_wr: float = -1.0
    _running_best_path = os.path.join(args.out_dir, "ppo_running_best.pt")
    _running_best_provenance_path = os.path.join(args.out_dir, "ppo_running_best_provenance.json")
    _panel_launch_time: float = 0.0  # wall time when panel eval subprocess was launched

    # W&B chart history: accumulate per-iteration values for multi-line charts.
    _chart_iters: list[int] = []
    _chart_wr_ussr: list[float] = []
    _chart_wr_us: list[float] = []
    _chart_wr_combined: list[float] = []

    for iteration in range(args.start_iteration, args.n_iterations + 1):
        t_iter_start = time.time()

        # ── Rollout phase ────────────────────────────────────────────────────
        all_steps: list[Step] = []
        self_play_steps: list[Step] = []
        ucb_metrics: dict[str, float] = {}
        if args.league:
            seed = args.seed + (iteration - 1) * args.games_per_iter
            # Save current checkpoint to league pool before rollout.
            # Add at iteration 1 (so iter 2+ has at least one checkpoint to play against)
            # and every league_save_every iterations.
            if iteration == 1 or iteration % args.league_save_every == 0:
                Path(args.league).mkdir(parents=True, exist_ok=True)
                pool_path = str(Path(args.league) / f"iter_{iteration:04d}.pt")
                # Use EMA weights for league pool (smoother opponents)
                _ema_orig_pool = _apply_ema()
                _export_torchscript_model(model, pool_path, warn_only=True)
                _restore_from_ema(_ema_orig_pool)
                print(f"  Saved to league pool: {pool_path}", flush=True)
            all_steps, ucb_metrics, _rollout_opp_results = collect_rollout_league_batched(
                model, args.league, args.games_per_iter, seed, device,
                vp_reward_coef=args.vp_reward_coef,
                mix_k=args.league_mix_k,
                fixtures=args.league_fixtures,
                ussr_fixtures=args.ussr_league_fixtures,
                us_fixtures=args.us_league_fixtures,
                n_workers=args.rollout_workers,
                rollout_temp=args.rollout_temp,
                recency_tau=args.league_recency_tau,
                heuristic_pct=args.league_heuristic_pct,
                fixture_fadeout=args.league_fixture_fadeout,
                current_iter=iteration,
                self_slot=args.league_self_slot,
                wr_table_path=os.path.join(args.league, "wr_table.json"),
                pfsp_exponent=args.pfsp_exponent,
                dir_alpha=args.dir_alpha,
                dir_epsilon=args.dir_epsilon,
                reward_shaping=args.reward_shaping,
                reward_alpha=args.reward_alpha,
                heuristic_floor=args.heuristic_floor,
            )
            # Full PFSP pool weight dump at milestones for visibility
            if _is_milestone(iteration) and args.league:
                _wr_path = os.path.join(args.league, "wr_table.json")
                _wr_data = _load_wr_table(_wr_path) if os.path.exists(_wr_path) else {}
                if _wr_data:
                    _t_u = sum(int(v.get("total_ussr", 0)) for v in _wr_data.values())
                    _t_s = sum(int(v.get("total_us", 0)) for v in _wr_data.values())
                    print(f"  [pfsp pool dump iter={iteration}] N_ussr={_t_u} N_us={_t_s}", flush=True)
                    # Collect all candidates with weights
                    _pool_entries: list[tuple[str, str, float, float, float, int]] = []  # (key, type, wr, sym, ucb, n)
                    for _pk, _pv in sorted(_wr_data.items()):
                        if _pk == "__self__":
                            continue
                        _ptype = "self" if _pk.startswith("iter_") else "fix"
                        for _ps, _pt, _pn_total in [("ussr", _t_u, "total_ussr"), ("us", _t_s, "total_us")]:
                            _pn = int(_pv.get(_pn_total, 0))
                            _pw_key = "wins_ussr" if _ps == "ussr" else "wins_us"
                            if _pn >= 10:
                                _pwr = int(_pv.get(_pw_key, 0)) / _pn
                                _psym = 4.0 * _pwr * (1.0 - _pwr)
                                _pucb = args.pfsp_exponent * math.sqrt(math.log(_pt) / _pn) if _pt > 0 and _pn > 0 else 0.0
                                _pw = max(0.01, _psym + _pucb)
                                print(f"    [{_ps}] {_pk:20s} ({_ptype}) WR={_pwr:.3f} n={_pn:4d} sym={_psym:.3f} ucb={_pucb:.3f} → w={_pw:.3f}", flush=True)
                            else:
                                print(f"    [{_ps}] {_pk:20s} ({_ptype}) WR=?     n={_pn:4d} → w=1.000 (warmup)", flush=True)
        elif args.self_play:
            seed = args.seed + (iteration - 1) * args.games_per_iter
            self_play_steps = collect_rollout_self_play_batched(
                model, args.games_per_iter, seed, device, vp_reward_coef=args.vp_reward_coef,
                rollout_temp=args.rollout_temp,
                reward_shaping=args.reward_shaping, reward_alpha=args.reward_alpha,
            )
            all_steps = list(self_play_steps)
            if args.self_play_heuristic_mix > 0:
                n_heur = max(1, int(args.games_per_iter * args.self_play_heuristic_mix))
                heur_steps_ussr = collect_rollout_batched(
                    model, n_heur // 2, tscore.Side.USSR, seed + 1000000, device, card_specs,
                    vp_reward_coef=args.vp_reward_coef, rollout_temp=args.rollout_temp,
                    reward_shaping=args.reward_shaping, reward_alpha=args.reward_alpha,
                )
                heur_steps_us = collect_rollout_batched(
                    model, n_heur // 2, tscore.Side.US, seed + 2000000, device, card_specs,
                    vp_reward_coef=args.vp_reward_coef, rollout_temp=args.rollout_temp,
                    reward_shaping=args.reward_shaping, reward_alpha=args.reward_alpha,
                )
                all_steps = all_steps + heur_steps_ussr + heur_steps_us
        else:
            for side in sides:
                side_seed = args.seed + (iteration - 1) * args.games_per_iter
                if side == tscore.Side.US:
                    side_seed += games_per_side
                steps = collect_rollout_batched(
                    model, games_per_side, side, side_seed, device, card_specs,
                    vp_reward_coef=args.vp_reward_coef,
                    reward_shaping=args.reward_shaping, reward_alpha=args.reward_alpha,
                )
                all_steps.extend(steps)

        n_steps = len(all_steps)
        if n_steps == 0:
            print(f"[iter {iteration}] No steps collected, skipping")
            continue

        # ── n_steps regression check (after iter 1) ─────────────────────────
        # Healthy games average ~60 steps each (8-10 turns × ~7 decisions/turn).
        # Degenerate games (scoring card exploit, DEFCON safety removed) average
        # <15 steps. Check after iter 1 to catch engine regressions immediately.
        # Threshold: 30 steps/game (~4 turns). Below this = likely engine bug.
        MIN_STEPS_PER_GAME = 30
        steps_per_game = n_steps / max(1, args.games_per_iter)
        if iteration == 1 and steps_per_game < MIN_STEPS_PER_GAME:
            print(
                f"\n  *** WARNING: n_steps regression detected! ***\n"
                f"  steps_per_game = {steps_per_game:.1f} (threshold: {MIN_STEPS_PER_GAME})\n"
                f"  n_steps = {n_steps}, games = {args.games_per_iter}\n"
                f"  This usually means an engine bug (DEFCON safety removed, scoring\n"
                f"  card enforcement missing, etc.) is causing abnormally short games.\n"
                f"  Check: git log --oneline -5 -- cpp/tscore/\n"
                f"  Healthy baseline: ~60 steps/game (v55/v56 era)\n",
                flush=True,
            )

        # Compute GAE advantages — must come BEFORE saving parquet so s.returns is populated
        compute_gae_batch(all_steps, gamma=args.gamma, lam=args.gae_lambda)

        # Optionally override GAE advantages with UPGO (leaves `returns` for value fn)
        if args.upgo:
            apply_upgo_advantages(all_steps, gamma=args.gamma)

        # Optionally save rollout steps as Parquet for BC/KL-distillation
        # Saved after GAE so gae_return column is correct.
        if args.save_rollout_parquet and all_steps:
            # base_seed is deterministic: args.seed + (iteration - 1) * args.games_per_iter
            _rollout_base_seed = args.seed + (iteration - 1) * args.games_per_iter
            _save_rollout_parquet(
                all_steps, args.save_rollout_parquet, iteration,
                base_seed=_rollout_base_seed,
                checkpoint_path=args.checkpoint,
            )

        t_rollout = time.time() - t_iter_start

        # Compute win rates from rewards (fraction of games with +1 final reward)
        terminal_steps = [s for s in all_steps if s.done]
        terminal_rewards = [s.reward for s in terminal_steps]
        rollout_wr = sum(1 for r in terminal_rewards if r > 0) / max(1, len(terminal_rewards))
        ussr_done = [s for s in terminal_steps if s.side_int == 0]
        us_done = [s for s in terminal_steps if s.side_int == 1]
        rollout_wr_ussr = sum(1 for s in ussr_done if s.reward > 0) / max(1, len(ussr_done))
        rollout_wr_us = sum(1 for s in us_done if s.reward > 0) / max(1, len(us_done))
        sp_rollout_wr_ussr = 0.0
        sp_rollout_wr_us = 0.0
        if args.self_play:
            terminal_sp_steps = [s for s in self_play_steps if s.done]
            ussr_sp_steps = [s for s in terminal_sp_steps if s.side_int == 0]
            us_sp_steps = [s for s in terminal_sp_steps if s.side_int == 1]
            sp_rollout_wr_ussr = sum(1 for s in ussr_sp_steps if s.reward > 0) / max(1, len(ussr_sp_steps))
            sp_rollout_wr_us = sum(1 for s in us_sp_steps if s.reward > 0) / max(1, len(us_sp_steps))

        # ── PPO update phase ──────────────────────────────────────────────────
        # LR warmup: linearly ramp from lr/10 → lr over lr_warmup_iters iterations.
        # Use when resuming with new input features to prevent early gradients from
        # destabilizing already-learned weights.
        if args.lr_warmup_iters > 0 and iteration <= args.lr_warmup_iters:
            warmup_lr = args.lr * (0.1 + 0.9 * (iteration - 1) / args.lr_warmup_iters)
            for pg in optimizer.param_groups:
                pg["lr"] = warmup_lr
        elif args.lr_warmup_iters > 0 and iteration == args.lr_warmup_iters + 1:
            for pg in optimizer.param_groups:
                pg["lr"] = args.lr  # restore full LR after warmup

        # Global entropy schedule: decays based on total iterations across all chained runs,
        # not per-run iteration. Prevents entropy from resetting to high on each new run.
        if args.ent_coef_final is not None:
            global_iter = global_iter_offset + iteration
            if global_iter <= args.global_ent_decay_start:
                current_ent_coef = args.ent_coef
            elif global_iter >= args.global_ent_decay_end:
                current_ent_coef = args.ent_coef_final
            else:
                t_frac = (global_iter - args.global_ent_decay_start) / max(
                    1, args.global_ent_decay_end - args.global_ent_decay_start
                )
                current_ent_coef = args.ent_coef + t_frac * (args.ent_coef_final - args.ent_coef)
        else:
            current_ent_coef = args.ent_coef

        t_update_start = time.time()
        metrics = ppo_update_packed(
            pack_steps(all_steps), model, optimizer, device,
            ppo_epochs=args.ppo_epochs,
            clip_eps=args.clip_eps,
            vf_coef=args.vf_coef,
            ent_coef=current_ent_coef,
            minibatch_size=args.minibatch_size,
            target_kl=args.target_kl,
        )
        t_update = time.time() - t_update_start
        t_iter = time.time() - t_iter_start

        # Update EMA weights after each PPO step
        _update_ema()

        # Cosine LR decay: smoothly reduce LR from args.lr to args.lr * 0.1 over the run.
        # Applied after warmup phase. Prevents late-training overshooting.
        if args.lr_warmup_iters == 0 or iteration > args.lr_warmup_iters:
            cos_progress = (iteration - 1) / max(1, args.n_iterations - 1)
            cos_lr = args.lr * (0.1 + 0.9 * 0.5 * (1.0 + math.cos(math.pi * cos_progress)))
            for pg in optimizer.param_groups:
                pg["lr"] = cos_lr

        # Early stopping on KL divergence
        if metrics.get("approx_kl", 0) > args.max_kl:
            print(f"[iter {iteration}] KL divergence {metrics['approx_kl']:.4f} > "
                  f"{args.max_kl:.4f}, stopping early")
            break

        _epochs_info = f" ep={int(metrics.get('ppo_epochs_run', args.ppo_epochs))}/{args.ppo_epochs}" if metrics.get("kl_early_stopped", 0) > 0 else ""
        print(
            f"[iter {iteration:3d}/{args.n_iterations}] "
            f"steps={n_steps:5d} "
            f"rollout_wr={rollout_wr:.3f} (ussr={rollout_wr_ussr:.3f} us={rollout_wr_us:.3f}) "
            f"pl={metrics.get('policy_loss', 0):.4f} "
            f"vl={metrics.get('value_loss', 0):.4f} "
            f"ent={metrics.get('entropy', 0):.3f} "
            f"clip={metrics.get('clip_fraction', 0):.3f} "
            f"kl={metrics.get('approx_kl', 0):.4f}{_epochs_info} "
            f"t={t_iter:.1f}s (rollout={t_rollout:.1f}s update={t_update:.1f}s)",
            flush=True,
        )

        probe_metrics: dict[str, float] = {}
        if probe_eval is not None and iteration % args.jsd_probe_interval == 0:
            try:
                with torch.no_grad():
                    prev_iter = iteration - args.jsd_probe_interval
                    prev_ckpt = _find_rolling_checkpoint(prev_iter) if prev_iter >= args.start_iteration else None
                    if prev_ckpt is not None:
                        from tsrl.policies.jsd_probe import load_probe_model

                        prev_model = load_probe_model(prev_ckpt, device=device)
                        prev_model.eval()
                        m = probe_eval.compare(model, prev_model)
                        probe_metrics.update({
                            "jsd/card_vs_prev": m.card_jsd,
                            "jsd/mode_vs_prev": m.mode_jsd,
                            "jsd/country_vs_prev": m.country_jsd,
                            "jsd/value_mae_vs_prev": m.value_mae,
                            "jsd/top1_card_agreement_vs_prev": m.top1_card_agree,
                            "jsd/top1_mode_agreement_vs_prev": m.top1_mode_agree,
                            "jsd/card_early_vs_prev": m.card_jsd_early,
                            "jsd/card_mid_vs_prev": m.card_jsd_mid,
                            "jsd/card_late_vs_prev": m.card_jsd_late,
                        })
                        print(
                            f"  [jsd] iter={iteration} prev_iter={prev_iter} "
                            f"card_jsd={m.card_jsd:.4f} top1={m.top1_card_agree:.3f} "
                            f"val_mae={m.value_mae:.4f}",
                            flush=True,
                        )
                        del prev_model
                    if probe_bc_model is not None:
                        m_bc = probe_eval.compare(model, probe_bc_model)
                        probe_metrics.update({
                            "jsd/card_vs_bc": m_bc.card_jsd,
                            "jsd/mode_vs_bc": m_bc.mode_jsd,
                            "jsd/country_vs_bc": m_bc.country_jsd,
                            "jsd/value_mae_vs_bc": m_bc.value_mae,
                            "jsd/top1_card_agreement_vs_bc": m_bc.top1_card_agree,
                            "jsd/top1_mode_agreement_vs_bc": m_bc.top1_mode_agree,
                            "jsd/card_early_vs_bc": m_bc.card_jsd_early,
                            "jsd/card_mid_vs_bc": m_bc.card_jsd_mid,
                            "jsd/card_late_vs_bc": m_bc.card_jsd_late,
                        })
            except Exception as _probe_err:
                print(f"  [jsd] error (non-fatal): {_probe_err}", flush=True)

        # ── Rolling checkpoint (every iteration) ─────────────────────────────
        # Write new checkpoint first, then delete the previous non-milestone one.
        # This ensures we always have the latest weights even after a crash.
        new_ckpt_path = _flat_checkpoint_path(args.out_dir, args.version, iteration)
        export_checkpoint(model, new_ckpt_path, ckpt_meta)
        legacy_ckpt_path = _legacy_checkpoint_path(args.out_dir, iteration)
        _write_compat_alias(new_ckpt_path, legacy_ckpt_path)
        _write_compat_alias(
            new_ckpt_path.replace(".pt", "_scripted.pt"),
            legacy_ckpt_path.replace(".pt", "_scripted.pt"),
        )

        # Delete rolling checkpoints that have aged out of the retention window.
        delete_iteration = iteration - rolling_ckpt_keep
        if delete_iteration >= args.start_iteration and not _is_milestone(delete_iteration):
            old_flat = _flat_checkpoint_path(args.out_dir, args.version, delete_iteration)
            old_legacy = _legacy_checkpoint_path(args.out_dir, delete_iteration)
            for old_path in (old_flat, old_legacy):
                _remove_if_exists(old_path)
                _remove_if_exists(old_path.replace(".pt", "_scripted.pt"))

        # WS3: Log rollout win rates to metadata DB
        if _TRACKING_AVAILABLE:
            try:
                from tsrl.checkpoint_db import log_rollout_wr as _log_rollout_wr
                _log_rollout_wr(
                    checkpoint_name=Path(new_ckpt_path).stem,
                    iter_num=iteration,
                    ussr_wr=rollout_wr_ussr,
                    us_wr=rollout_wr_us,
                    combined_wr=(rollout_wr_ussr + rollout_wr_us) / 2.0,
                    n_games=len(terminal_rewards),
                )
            except Exception as _e:
                print(f"[tracking] log_rollout_wr failed: {_e}")
            # Per-opponent granular stats (league mode only)
            if args.league and "_rollout_opp_results" in dir():
                try:
                    from tsrl.checkpoint_db import log_rollout_opponent_stats as _log_ros
                    _log_ros(
                        run_id=Path(args.out_dir).name,
                        checkpoint_name=Path(new_ckpt_path).stem,
                        iter_num=iteration,
                        opponent_results=_rollout_opp_results,
                        rollout_temp=args.rollout_temp,
                        dir_alpha=getattr(args, "dir_alpha", 0.0),
                        dir_epsilon=getattr(args, "dir_epsilon", 0.0),
                    )
                except Exception as _e:
                    print(f"[tracking] log_rollout_opponent_stats failed: {_e}")

        # WS7: Launch incremental Elo confirmation non-blocking at milestones
        if _is_milestone(iteration) and os.path.exists("scripts/post_train_confirm.sh"):
            try:
                _confirm_log = open(
                    os.path.join(args.out_dir, f"confirm_iter{iteration:04d}.log"), "w"
                )
                subprocess.Popen(
                    ["nice", "-n", "15", "bash", "scripts/post_train_confirm.sh",
                     args.out_dir, "--incremental"],
                    stdout=_confirm_log,
                    stderr=subprocess.STDOUT,
                    cwd=os.getcwd(),
                )
                print(f"  [confirm] launched incremental Elo check for iter {iteration}", flush=True)
            except Exception as _e:
                print(f"  [confirm] launch failed: {_e}", flush=True)

        # ── Build log dict ────────────────────────────────────────────────────
        log_dict = dict(metrics)
        log_dict["rollout_wr"] = rollout_wr
        log_dict["rollout_wr_ussr"] = rollout_wr_ussr
        log_dict["rollout_wr_us"] = rollout_wr_us
        log_dict["n_steps"] = n_steps
        log_dict["steps_per_game"] = steps_per_game
        log_dict["iter_time_s"] = t_iter
        log_dict["ent_coef"] = current_ent_coef
        log_dict["lr"] = optimizer.param_groups[0]["lr"]
        log_dict["ppo_epochs_run"] = metrics.get("ppo_epochs_run", args.ppo_epochs)
        log_dict["kl_early_stopped"] = metrics.get("kl_early_stopped", 0.0)
        if args.self_play:
            log_dict["sp_rollout_wr_ussr"] = sp_rollout_wr_ussr
            log_dict["sp_rollout_wr_us"] = sp_rollout_wr_us
        _add_scalar_weight_norms(model, log_dict)
        _add_region_net_delta_stats(terminal_steps, log_dict)
        if args.league and ucb_metrics:
            log_dict.update(ucb_metrics)

        # ── Async panel eval: collect result from previous run ────────────────
        if _panel_proc is not None and not _panel_proc.is_alive():
            _panel_proc.join()
            _panel_proc = None
            if _panel_result_path and os.path.exists(_panel_result_path):
                try:
                    with open(_panel_result_path) as f:
                        panel_res = json.load(f)
                    os.remove(_panel_result_path)
                    panel_log: dict = {}
                    valid_opps = {k: v for k, v in panel_res.items() if "error" not in v}
                    for opp_name, stats in panel_res.items():
                        if "error" in stats:
                            print(f"  [panel eval] {opp_name}: ERROR {stats['error']}", flush=True)
                            continue
                        panel_log[f"panel/{opp_name}_ussr_wr"] = stats["ussr_wr"]
                        panel_log[f"panel/{opp_name}_us_wr"] = stats["us_wr"]
                        panel_log[f"panel/{opp_name}_combined_wr"] = stats["combined_wr"]
                    if valid_opps:
                        # Elo-weighted panel scoring: frontier opponents count more.
                        # Weights calibrated to 5-opponent pool (Opus rec 2026-04-12):
                        #   v55 (2124) > v54 (2108) > v44 (2106) > v45 (2102) > v14 (2015).
                        # Normalized over whichever opponents actually ran (some may error).
                        _PANEL_WEIGHTS: dict[str, float] = {"v55": 0.35, "v54": 0.25, "v44": 0.20, "v45": 0.15, "v14": 0.05}
                        # Heuristic is tracked for monitoring but excluded from weighted avg
                        # (checkpoint selection should optimize model-vs-model; heuristic WR
                        # is a regression detector, not a training target).
                        _scoring_opps = {k: v for k, v in valid_opps.items() if k != "heuristic"}
                        _wsum = sum(_PANEL_WEIGHTS.get(k, 0.25) for k in _scoring_opps) if _scoring_opps else 1.0
                        avg_combined = sum(
                            v["combined_wr"] * _PANEL_WEIGHTS.get(k, 0.25) for k, v in _scoring_opps.items()
                        ) / _wsum if _scoring_opps else 0.0
                        _panel_elapsed = time.time() - _panel_launch_time if _panel_launch_time > 0 else 0.0
                        panel_log["panel/avg_combined_wr"] = avg_combined
                        panel_log["panel/eval_time_sec"] = _panel_elapsed
                        print(
                            f"  [panel eval iter {_panel_trigger_iter}] avg={avg_combined:.3f} "
                            f"elapsed={_panel_elapsed:.0f}s: "
                            + " | ".join(f"{k}={v['combined_wr']:.3f}" for k, v in valid_opps.items()),
                            flush=True,
                        )
                    if wandb_run is not None and panel_log:
                        wandb_run.log(panel_log, step=_panel_trigger_iter)
                    # Persist to panel_eval_history.json for post-run checkpoint selection
                    history_path = os.path.join(args.out_dir, "panel_eval_history.json")
                    try:
                        history: dict = {}
                        if os.path.exists(history_path):
                            with open(history_path) as f:
                                history = json.load(f)
                        history[str(_panel_trigger_iter)] = panel_res
                        _save_json_atomic(history_path, history)
                    except Exception as he:
                        print(f"  [panel eval] history save failed: {he}", flush=True)
                    # Option F: save ppo_running_best.pt when panel avg is a new high-water mark.
                    # The evaluated checkpoint is ppo_iter{_panel_trigger_iter:04d}.pt
                    # (always retained since panel eval only fires at milestones).
                    if valid_opps and avg_combined > _panel_best_wr:
                        _panel_best_wr = avg_combined
                        _hwm_ckpt = os.path.join(
                            args.out_dir, f"ppo_iter{_panel_trigger_iter:04d}.pt"
                        )
                        if os.path.exists(_hwm_ckpt):
                            import shutil as _shutil
                            _shutil.copy2(_hwm_ckpt, _running_best_path)
                            _hwm_scripted = _hwm_ckpt.replace(".pt", "_scripted.pt")
                            if os.path.exists(_hwm_scripted):
                                _shutil.copy2(_hwm_scripted, _running_best_path.replace(".pt", "_scripted.pt"))
                            # Provenance sidecar: records which iter checkpoint became running_best.
                            _prov = {
                                "source_checkpoint": os.path.basename(_hwm_ckpt),
                                "source_path": _hwm_ckpt,
                                "panel_avg_wr": round(avg_combined, 6),
                                "panel_trigger_iter": _panel_trigger_iter,
                                "run_dir": args.out_dir,
                                "saved_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                                "panel_opponents": list(valid_opps.keys()),
                            }
                            _save_json_atomic(_running_best_provenance_path, _prov)
                            print(
                                f"  [panel eval] NEW HIGH-WATER MARK iter={_panel_trigger_iter} "
                                f"avg_wr={avg_combined:.4f} → ppo_running_best.pt "
                                f"(provenance: {os.path.basename(_hwm_ckpt)})",
                                flush=True,
                            )
                except Exception as e:
                    print(f"  [panel eval] result read failed: {e}", flush=True)
            if _panel_script_path:
                try:
                    os.remove(_panel_script_path)
                except OSError:
                    pass

        # ── Async panel eval: trigger new run at milestone ────────────────────
        if _is_milestone(iteration) and args.eval_panel and _panel_proc is None:
            _panel_script_path = os.path.join(args.out_dir, f"panel_eval_{iteration:04d}.pt")
            _panel_result_path = os.path.join(args.out_dir, f"panel_eval_{iteration:04d}_result.json")
            _panel_trigger_iter = iteration
            _panel_launch_time = time.time()
            try:
                # Use EMA weights for panel eval (smoother, less noisy)
                _ema_orig = _apply_ema()
                _export_torchscript_model(model, _panel_script_path, warn_only=False)
                _restore_from_ema(_ema_orig)
                # Use "spawn" to avoid inheriting CUDA context from parent (fork + CUDA = deadlock).
                _panel_proc = _mp.get_context("spawn").Process(
                    target=_panel_eval_worker,
                    args=(_panel_script_path, args.eval_panel, 60, 70000 + iteration * 200, _panel_result_path),
                    daemon=True,
                )
                _panel_proc.start()
                panel_labels = [
                    "heuristic" if p == HEURISTIC_FIXTURE else Path(p).stem.replace("_scripted", "")
                    for p in args.eval_panel
                ]
                print(f"  [panel eval] launched pid={_panel_proc.pid} iter={iteration} panel={panel_labels}", flush=True)
            except Exception as e:
                print(f"  [panel eval] launch failed: {e}", flush=True)
                _panel_proc = None

        if wandb_run is not None:
            log_dict.update(probe_metrics)

            # ── Rename flat metrics to prefixed keys for W&B section grouping ──
            # W&B auto-groups metrics by prefix (e.g. "train/" → one section).
            # Old flat keys are kept alongside so existing saved charts still work.
            _prefix_map = {
                "policy_loss": "train/policy_loss",
                "value_loss": "train/value_loss",
                "sc_loss": "train/sc_loss",
                "entropy": "train/entropy",
                "clip_fraction": "train/clip_fraction",
                "approx_kl": "train/approx_kl",
                "ent_coef": "train/ent_coef",
                "rollout_wr": "rollout/wr_combined",
                "rollout_wr_ussr": "rollout/wr_ussr",
                "rollout_wr_us": "rollout/wr_us",
                "sp_rollout_wr_ussr": "rollout/sp_wr_ussr",
                "sp_rollout_wr_us": "rollout/sp_wr_us",
                "n_steps": "rollout/n_steps",
                "iter_time_s": "meta/iter_time_s",
                "core_scalar_weight_norm": "weights/core_scalar_norm",
                "new_scalar_weight_norm": "weights/new_scalar_norm",
                "region_scalar_weight_norm": "weights/region_scalar_norm",
            }
            for old_key, new_key in _prefix_map.items():
                if old_key in log_dict:
                    log_dict[new_key] = log_dict[old_key]

            # ── Named composite charts (same layout for every run) ─────────────
            # charts/rollout_wr: multi-line USSR/US/combined on one plot.
            _chart_iters.append(iteration)
            _chart_wr_ussr.append(rollout_wr_ussr)
            _chart_wr_us.append(rollout_wr_us)
            _chart_wr_combined.append((rollout_wr_ussr + rollout_wr_us) / 2.0)
            try:
                log_dict["charts/rollout_wr"] = wandb.plot.line_series(
                    xs=[list(_chart_iters)] * 3,
                    ys=[_chart_wr_ussr, _chart_wr_us, _chart_wr_combined],
                    keys=["USSR", "US", "combined"],
                    title="Rollout win rate",
                    xname="iteration",
                )
            except Exception:
                pass  # line_series may not be available in all wandb versions

            # charts/turn_dist, vp_dist, defcon_dist: histograms from terminal steps.
            if terminal_steps:
                _end_turns = [s.raw_turn for s in terminal_steps if s.raw_turn is not None]
                _end_vps = [s.raw_vp for s in terminal_steps if s.raw_vp is not None]
                _end_defcons = [s.raw_defcon for s in terminal_steps if s.raw_defcon is not None]
                if _end_turns:
                    log_dict["charts/turn_dist"] = wandb.Histogram(
                        _end_turns, num_bins=10
                    )
                if _end_vps:
                    log_dict["charts/vp_dist"] = wandb.Histogram(
                        _end_vps, num_bins=30
                    )
                if _end_defcons:
                    log_dict["charts/defcon_dist"] = wandb.Histogram(
                        _end_defcons, num_bins=5
                    )

            wandb_run.log(log_dict, step=iteration)

    # ── Final checkpoint + summary ────────────────────────────────────────────
    final_path = os.path.join(args.out_dir, "ppo_final.pt")
    ckpt_meta["total_iters"] = global_iter_offset + args.n_iterations
    # Use EMA weights for final checkpoint (smoother)
    _ema_orig_final = _apply_ema()
    export_checkpoint(model, final_path, ckpt_meta)
    _restore_from_ema(_ema_orig_final)
    # Verify ppo_final.pt was written; if missing, copy from last rolling checkpoint.
    # This guard catches a rare race condition where ppo_final.pt gets deleted after writing.
    if not os.path.exists(final_path):
        _last_flat = _flat_checkpoint_path(args.out_dir, args.version, global_iter_offset + args.n_iterations)
        _fallback = _last_flat if os.path.exists(_last_flat) else _running_best_path
        if os.path.exists(_fallback):
            shutil.copy2(_fallback, final_path)
            print(f"  Warning: ppo_final.pt was missing after export; copied from {_fallback}", flush=True)
        else:
            print(f"  Warning: ppo_final.pt missing and no fallback found; watcher may not auto-chain", flush=True)
    if _TRACKING_AVAILABLE:
        try:
            _hp = {k: v for k, v in vars(args).items() if isinstance(v, (int, float, str, bool, type(None)))}
            _log_checkpoint(
                name=Path(final_path).stem,
                file_path=Path(final_path),
                hyperparams=_hp,
                wandb_run_id=wandb_run.id if wandb_run is not None else None,
                parent_name=getattr(args, "checkpoint", None),
            )
        except Exception as _e:
            print(f"[tracking] log_checkpoint(final) failed: {_e}")

    # Promote ppo_running_best.pt → ppo_best.pt (Option F: panel high-water mark).
    # ppo_running_best is set during training when a new panel eval high-water mark is found.
    # ppo_loop_step.sh checks for ppo_best.pt first; if missing it falls back to ppo_final.pt
    # (the last iteration, usually worse). Always promote running_best so the next run warm-starts
    # from the best-evaluated checkpoint, not the last one.
    # NOTE: This block is wrapped in try/except because Snakemake deletes declared outputs
    # (ppo_final.pt) if the process exits non-zero. Any error here must not propagate.
    try:
        best_scripted_path = best_ckpt_path.replace(".pt", "_scripted.pt")
        if os.path.exists(_running_best_path) and not os.path.exists(best_ckpt_path):
            shutil.copy2(_running_best_path, best_ckpt_path)
            _rb_scripted = _running_best_path.replace(".pt", "_scripted.pt")
            if os.path.exists(_rb_scripted):
                shutil.copy2(_rb_scripted, best_scripted_path)
            print(
                "ppo_best.pt ← ppo_running_best.pt (Option F: panel high-water mark → next run warmstart)",
                flush=True,
            )
        elif not os.path.exists(best_ckpt_path):
            # No panel eval ran (or benchmark_every=0); use ppo_final.pt as best.
            shutil.copy2(final_path, best_ckpt_path)
            final_scripted = final_path.replace(".pt", "_scripted.pt")
            if os.path.exists(final_scripted):
                shutil.copy2(final_scripted, best_scripted_path)
            print(
                "ppo_best.pt ← ppo_final.pt (panel eval did not run; consider --eval-panel)",
                flush=True,
            )
    except Exception as _promote_err:
        print(f"  Warning: ppo_best.pt promotion failed (non-fatal): {_promote_err}", flush=True)

    # Wait for any still-running panel eval (e.g. final iteration) instead of
    # killing it — the result is valuable for checkpoint selection and W&B.
    if _panel_proc is not None and _panel_proc.is_alive():
        print("  [panel eval] waiting for final panel eval to complete (up to 120s)...", flush=True)
        _panel_proc.join(timeout=120)
        if _panel_proc.is_alive():
            print("  [panel eval] timed out — terminating", flush=True)
            _panel_proc.terminate()
            _panel_proc.join(timeout=5)
    if _panel_proc is not None:
        _panel_proc.join(timeout=1)
        _panel_proc = None
        # Process the result the same way the main loop does
        if _panel_result_path and os.path.exists(_panel_result_path):
            try:
                with open(_panel_result_path) as f:
                    panel_res = json.load(f)
                valid_opps = {k: v for k, v in panel_res.items() if "error" not in v}
                panel_log: dict = {}
                for opp_name, stats in panel_res.items():
                    if "error" in stats:
                        print(f"  [panel eval] {opp_name}: ERROR {stats['error']}", flush=True)
                        continue
                    panel_log[f"panel/{opp_name}_ussr_wr"] = stats["ussr_wr"]
                    panel_log[f"panel/{opp_name}_us_wr"] = stats["us_wr"]
                    panel_log[f"panel/{opp_name}_combined_wr"] = stats["combined_wr"]
                if valid_opps:
                    _PANEL_WEIGHTS: dict[str, float] = {"v55": 0.35, "v54": 0.25, "v44": 0.20, "v45": 0.15, "v14": 0.05}
                    _scoring_opps = {k: v for k, v in valid_opps.items() if k != "heuristic"}
                    _wsum = sum(_PANEL_WEIGHTS.get(k, 0.25) for k in _scoring_opps) if _scoring_opps else 1.0
                    avg_combined = sum(
                        v["combined_wr"] * _PANEL_WEIGHTS.get(k, 0.25) for k, v in _scoring_opps.items()
                    ) / _wsum if _scoring_opps else 0.0
                    _panel_elapsed = time.time() - _panel_launch_time if _panel_launch_time > 0 else 0.0
                    panel_log["panel/avg_combined_wr"] = avg_combined
                    panel_log["panel/eval_time_sec"] = _panel_elapsed
                    print(
                        f"  [panel eval iter {_panel_trigger_iter}] avg={avg_combined:.3f} "
                        f"elapsed={_panel_elapsed:.0f}s: "
                        + " | ".join(f"{k}={v['combined_wr']:.3f}" for k, v in valid_opps.items()),
                        flush=True,
                    )
                if wandb_run is not None and panel_log:
                    wandb_run.log(panel_log, step=_panel_trigger_iter)
                # Persist to panel_eval_history.json
                history_path = os.path.join(args.out_dir, "panel_eval_history.json")
                try:
                    history: dict = {}
                    if os.path.exists(history_path):
                        with open(history_path) as f:
                            history = json.load(f)
                    history[str(_panel_trigger_iter)] = panel_res
                    _save_json_atomic(history_path, history)
                except Exception as he:
                    print(f"  [panel eval] history save failed: {he}", flush=True)
                # Update running best if this is a new high-water mark
                if valid_opps and avg_combined > _panel_best_wr:
                    _panel_best_wr = avg_combined
                    _hwm_ckpt = os.path.join(
                        args.out_dir, f"ppo_iter{_panel_trigger_iter:04d}.pt"
                    )
                    if os.path.exists(_hwm_ckpt):
                        import shutil as _shutil
                        _shutil.copy2(_hwm_ckpt, _running_best_path)
                        _hwm_scripted = _hwm_ckpt.replace(".pt", "_scripted.pt")
                        if os.path.exists(_hwm_scripted):
                            _shutil.copy2(_hwm_scripted, _running_best_path.replace(".pt", "_scripted.pt"))
                        _prov = {
                            "source_checkpoint": os.path.basename(_hwm_ckpt),
                            "source_path": _hwm_ckpt,
                            "panel_avg_wr": round(avg_combined, 6),
                            "panel_trigger_iter": _panel_trigger_iter,
                            "run_dir": args.out_dir,
                            "saved_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                            "panel_opponents": list(valid_opps.keys()),
                        }
                        _save_json_atomic(_running_best_provenance_path, _prov)
                        print(
                            f"  [panel eval] NEW HIGH-WATER MARK iter={_panel_trigger_iter} "
                            f"avg_wr={avg_combined:.4f} → ppo_running_best.pt "
                            f"(provenance: {os.path.basename(_hwm_ckpt)})",
                            flush=True,
                        )
            except Exception as e:
                print(f"  [panel eval] final result read failed: {e}", flush=True)
    for leftover in [_panel_result_path, _panel_script_path]:
        if leftover:
            try:
                os.remove(leftover)
            except OSError:
                pass

    if _TRACKING_AVAILABLE:
        try:
            _log_exp_end(
                name=str(args.out_dir) if hasattr(args, "out_dir") else "ppo_run",
                result_summary=f"PPO training complete, {args.n_iterations} iterations",
            )
        except Exception as _e:
            print(f"[tracking] log_experiment_end failed: {_e}")

    t_total = time.time() - t_start
    print(f"\nTraining complete in {t_total/60:.1f} minutes")
    print(f"Checkpoints in: {args.out_dir}")

    if wandb_run is not None:
        wandb_run.finish()

    # ── Post-training hook (e.g. confirmation tournament) ──────────────────
    if args.post_train_hook:
        hook_cmd = args.post_train_hook.replace("{out_dir}", args.out_dir)
        print(f"\n[post-train-hook] Running: {hook_cmd}")
        try:
            hook_result = subprocess.run(
                hook_cmd, shell=True, timeout=3600,  # 1 hour max
                capture_output=False,  # let output flow to stdout/stderr
            )
            if hook_result.returncode != 0:
                print(f"[post-train-hook] WARNING: exited with code {hook_result.returncode}")
            else:
                print("[post-train-hook] completed successfully")
        except subprocess.TimeoutExpired:
            print("[post-train-hook] WARNING: timed out after 3600s")
        except Exception as e:
            print(f"[post-train-hook] ERROR: {e}")


if __name__ == "__main__":
    main()
