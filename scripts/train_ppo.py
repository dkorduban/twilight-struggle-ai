#!/usr/bin/env python3
"""PPO fine-tuning of BC checkpoint for Twilight Struggle AI.

Warms up from a BC checkpoint and runs PPO against the MinimalHybrid heuristic.
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
import json
import math
import os
import sys
import tempfile
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import torch
import torch.nn as nn
import torch.nn.functional as F

# Bindings
_repo_root = Path(__file__).resolve().parent.parent
for _bindings_path in (
    _repo_root / "build" / "bindings",
    _repo_root / "build-ninja" / "bindings",
):
    _bindings_dir = str(_bindings_path)
    if _bindings_path.exists() and _bindings_dir not in sys.path:
        sys.path.insert(0, _bindings_dir)
        break
_py_dir = str(Path(__file__).resolve().parent.parent / "python")
if _py_dir not in sys.path:
    sys.path.insert(0, _py_dir)

import tscore  # noqa: E402

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


_COUNTRY_REGION: dict[int, str] = {}  # lazy-loaded once

CARD_SLOTS = 112      # kMaxCardId(111) + 1; index 0 unused
COUNTRY_SLOTS = 86    # country IDs 0..85
SCALAR_DIM = 11
CARD_DIM = CARD_SLOTS * 4   # 448
INFLUENCE_DIM = COUNTRY_SLOTS * 2  # 172

# DEFCON-lowering cards (kept in sync with C++ learned_policy.cpp / mcts_batched.cpp)
DEFCON_LOWERING_CARDS = frozenset({
    4, 11, 13, 20, 24, 39, 48, 49, 50, 53, 83, 92, 105,
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
    scalars: torch.Tensor        # (1, 11) CPU
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
    returns: float = 0.0


# ---------------------------------------------------------------------------
# Model loading
# ---------------------------------------------------------------------------

def load_model(checkpoint_path: str, device: str = "cuda") -> nn.Module:
    """Load a checkpoint and return the model in training mode on device."""
    from tsrl.policies.model import (
        TSBaselineModel,
        TSCardEmbedModel,
        TSControlFeatGNNModel,
        TSControlFeatGNNSideModel,
        TSControlFeatModel,
        TSCountryAttnModel,
        TSCountryEmbedModel,
        TSDirectCountryModel,
        TSFullEmbedModel,
        TSMarginalValueModel,
    )
    MODEL_REGISTRY = {
        "baseline": TSBaselineModel,
        "card_embed": TSCardEmbedModel,
        "country_embed": TSCountryEmbedModel,
        "full_embed": TSFullEmbedModel,
        "country_attn": TSCountryAttnModel,
        "direct_country": TSDirectCountryModel,
        "marginal_value": TSMarginalValueModel,
        "control_feat": TSControlFeatModel,
        "control_feat_gnn": TSControlFeatGNNModel,
        "control_feat_gnn_side": TSControlFeatGNNSideModel,
    }

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
    model.load_state_dict(state_dict, strict=False)
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

    # Sample card from masked distribution
    masked_card_logits = card_logits.clone()
    masked_card_logits[~card_mask] = float("-inf")
    card_probs = torch.softmax(masked_card_logits, dim=0)
    card_idx = int(torch.multinomial(card_probs, 1).item())
    card_id = card_idx + 1

    # ── Mode mask ───────────────────────────────────────────────────────────
    # All 5 modes start as potentially legal; apply DEFCON safety overrides.
    # We don't have full legal_modes() here, so use the model's distribution
    # with DEFCON safety constraints. The model strongly prefers legal modes.
    mode_mask = torch.ones(5, dtype=torch.bool, device=device)

    # DEFCON safety: no coup at DEFCON <= 2
    if defcon <= 2:
        mode_mask[MODE_COUP] = False

    # DEFCON safety: no event for DEFCON-lowering cards at DEFCON <= 2
    if defcon <= 2 and card_id in DEFCON_LOWERING_CARDS:
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
        # INFLUENCE: proportional allocation using card ops
        spec = card_specs.get(card_id)
        ops = max(1, getattr(spec, "ops", 1) or 1) if spec else 1
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
    )
    return {"card_id": card_id, "mode": mode, "targets": country_targets}, step


# ---------------------------------------------------------------------------
# Reward computation
# ---------------------------------------------------------------------------

def _compute_reward(result: "tscore.GameResult", side_int: int, vp_coef: float = 0.0) -> float:
    """Terminal reward. side_int 0=USSR, 1=US. Optional VP-magnitude component."""
    is_ussr = side_int == 0
    won = result.winner == (tscore.Side.USSR if is_ussr else tscore.Side.US)
    base = 1.0 if won else -1.0
    if vp_coef <= 0.0:
        return base
    # final_vp is from USSR perspective: positive = USSR ahead
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
        reward = _compute_reward(result, side_int, vp_reward_coef)

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
            temperature=1.0,
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
        )
        all_steps.append(step)

    side_int = 0 if learned_side == tscore.Side.USSR else 1
    for i, result in enumerate(results):
        start = boundaries[i]
        end = boundaries[i + 1] if i + 1 < len(boundaries) else len(all_steps)
        if start >= end:
            continue
        all_steps[end - 1].reward = _compute_reward(result, side_int, vp_reward_coef)
        all_steps[end - 1].done = True

    return all_steps


def collect_rollout_self_play_batched(
    model: nn.Module,
    n_games: int,
    base_seed: int,
    device: str,
    vp_reward_coef: float = 0.0,
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
            temperature=1.0,
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
        )
        all_steps.append(step)

    for i, result in enumerate(results):
        start = boundaries[i]
        end = boundaries[i + 1] if i + 1 < len(boundaries) else len(all_steps)
        if start >= end:
            continue
        last = all_steps[end - 1]
        last.reward = _compute_reward(result, last.side_int, vp_reward_coef)
        last.done = True

    return all_steps


# ---------------------------------------------------------------------------
# League training helpers
# ---------------------------------------------------------------------------

def sample_league_opponent(league_dir: str) -> Optional[str]:
    """Sample an opponent from the league pool.

    Returns None → use heuristic opponent.
    Distribution: 20% heuristic (always anchor), 50% latest checkpoint,
    30% uniformly random from all checkpoints.
    """
    import random

    pts = sorted(Path(league_dir).glob("iter_*.pt"))
    if not pts:
        return None  # empty pool → heuristic
    r = random.random()
    if r < 0.20:
        return None           # 20%: heuristic anchor
    elif r < 0.70:
        return str(pts[-1])   # 50%: most recent checkpoint
    else:
        return str(random.choice(pts))  # 30%: random past checkpoint


def collect_rollout_league_batched(
    model: nn.Module,
    league_dir: str,
    n_games: int,
    base_seed: int,
    device: str,
    vp_reward_coef: float = 0.0,
) -> list[Step]:
    """Collect rollout steps against a league-sampled opponent.

    When a model opponent is sampled, uses rollout_model_vs_model_batched:
    steps are recorded only for model_a (the learning model). When the heuristic
    is sampled, falls back to collect_rollout_batched for both sides.
    """
    opponent_path = sample_league_opponent(league_dir)

    if opponent_path is None or not hasattr(tscore, "rollout_model_vs_model_batched"):
        # Heuristic fallback (also used when rollout_model_vs_model_batched unavailable)
        n_half = n_games // 2
        steps_ussr = collect_rollout_batched(
            model, n_half, tscore.Side.USSR, base_seed, device, {}, vp_reward_coef
        )
        steps_us = collect_rollout_batched(
            model, n_half, tscore.Side.US, base_seed + n_half, device, {}, vp_reward_coef
        )
        return steps_ussr + steps_us

    script_path = _export_temp_model(model)
    try:
        results, steps, boundaries = tscore.rollout_model_vs_model_batched(
            model_a_path=script_path,
            model_b_path=opponent_path,
            n_games=n_games,
            pool_size=min(n_games, 64),
            seed=base_seed,
            device="cpu",
            temperature=1.0,
            nash_temperatures=False,
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
        )
        all_steps.append(step)

    # Assign terminal rewards for model_a steps only.
    # Game assignments: first n_games//2 → model_a=USSR; second half → model_a=US.
    half = n_games // 2
    for i, result in enumerate(results):
        start = boundaries[i]
        end = boundaries[i + 1] if i + 1 < len(boundaries) else len(all_steps)
        if start >= end:
            continue
        model_a_side_int = 0 if i < half else 1  # 0=USSR, 1=US
        last = all_steps[end - 1]
        last.reward = _compute_reward(result, model_a_side_int, vp_reward_coef)
        last.done = True

    return all_steps


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

    metrics = {"policy_loss": 0.0, "value_loss": 0.0, "entropy": 0.0,
               "clip_fraction": 0.0, "approx_kl": 0.0}
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

            loss = policy_loss + vf_coef * value_loss + ent_coef * entropy_loss

            # Skip update if loss is NaN to prevent weight corruption
            if torch.isnan(loss):
                print(f"  [NaN] loss components: pl={policy_loss.item():.4f} "
                      f"vl={value_loss.item():.4f} ent={entropy_loss.item():.4f} — skipping", flush=True)
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
            metrics["entropy"] += entropies.mean().item()
            metrics["clip_fraction"] += clip_frac
            metrics["approx_kl"] += approx_kl
            n_updates += 1

    if n_updates > 0:
        for k in metrics:
            metrics[k] /= n_updates

    return metrics


# ---------------------------------------------------------------------------
# Benchmark via benchmark_batched (fast)
# ---------------------------------------------------------------------------

def collect_policy_stats(
    script_path: str,
    n_games: int = 100,
    seed_base: int = 51000,
) -> dict:
    """
    Run a small rollout batch and compute per-phase policy statistics.
    Returns a flat dict of W&B-loggable scalars.

    Phase labels: early=turns 1-3, mid=turns 4-7, late=turns 8-10.
    Mode names: Influence, Event, Space, Coup, Realign.
    """
    global _COUNTRY_REGION
    if not _COUNTRY_REGION:
        _COUNTRY_REGION = _load_country_region_map()

    MODE_NAMES = ["Influence", "Event", "Space", "Coup", "Realign"]
    REGIONS = ["Europe", "Asia", "Middle East", "Africa", "Central America", "South America"]
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

    # Collect steps for both sides
    all_step_dicts: list[dict] = []
    for side in [tscore.Side.USSR, tscore.Side.US]:
        try:
            _, steps, _ = tscore.rollout_games_batched(
                model_path=script_path,
                learned_side=side,
                n_games=n_games,
                pool_size=min(n_games, 32),
                seed=seed_base + (0 if side == tscore.Side.USSR else n_games),
                device="cpu",
                temperature=1.0,   # training-representative stats
                nash_temperatures=True,
            )
            for s in steps:
                s["_side_name"] = "ussr" if side == tscore.Side.USSR else "us"
            all_step_dicts.extend(steps)
        except Exception as e:
            print(f"  [stats] rollout failed for {side}: {e}", flush=True)
            return {}

    # Aggregate
    from collections import defaultdict

    mode_counts: dict[tuple, int] = defaultdict(int)       # (phase, side, mode_name)
    region_counts: dict[tuple, int] = defaultdict(int)     # (phase, side, region)
    split_counts: dict[tuple, int] = defaultdict(int)      # (phase, side, split_label)
    total_counts: dict[tuple, int] = defaultdict(int)      # (phase, side)
    inf_counts: dict[tuple, int] = defaultdict(int)        # (phase, side) influence-only total
    defcon_sum: dict[tuple, float] = defaultdict(float)
    vp_sum: dict[tuple, float] = defaultdict(float)

    for s in all_step_dicts:
        scalars = s["scalars"]           # numpy (11,)
        turn = round(float(scalars[8]) * 10)
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
            # Region of first (top) target
            region = _COUNTRY_REGION.get(targets[0], "Unknown")
            region_counts[(ph, side_name, region)] += 1
            split_counts[(ph, side_name, influence_split_label(targets))] += 1
            inf_counts[key] += 1

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
            n_inf = inf_counts[key]
            if n_inf > 0:
                for r in REGIONS:
                    stats[f"{prefix}/region_{r.lower().replace(' ', '_')}_frac"] = (
                        region_counts[(ph, side_name, r)] / n_inf
                    )
                for label in ["concentrated", "split", "dispersed"]:
                    stats[f"{prefix}/split_{label}_frac"] = split_counts[(ph, side_name, label)] / n_inf
    return stats


def _save_rollout_parquet(steps: list[Step], out_dir: str, iteration: int) -> None:
    """Save rollout steps to Parquet for BC bootstrapping.

    Each row contains the raw feature tensors and action labels from a PPO step,
    in the same format as the BC dataset (influence, cards, scalars, card_id, mode_id,
    country_targets, side_int, reward). Saved to out_dir/rollout_iter_{N:04d}.parquet.

    These files can be used to warm-start BC training from PPO data without
    re-running games.
    """
    try:
        import pyarrow as pa
        import pyarrow.parquet as pq
    except ImportError:
        print("  [rollout-save] pyarrow not available, skipping Parquet save", flush=True)
        return

    Path(out_dir).mkdir(parents=True, exist_ok=True)
    out_path = Path(out_dir) / f"rollout_iter_{iteration:04d}.parquet"

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

    table = pa.table({
        "influence": pa.array(inf_list, type=pa.list_(pa.float32())),
        "cards": pa.array(cards_list, type=pa.list_(pa.float32())),
        "scalars": pa.array(scalars_list, type=pa.list_(pa.float32())),
        "card_id": pa.array(card_ids, type=pa.int32()),
        "mode_id": pa.array(mode_ids, type=pa.int32()),
        "country_targets": pa.array(country_targets, type=pa.list_(pa.int32())),
        "side_int": pa.array(side_ints, type=pa.int8()),
        "reward": pa.array(rewards, type=pa.float32()),
        "value": pa.array(values, type=pa.float32()),
        "iteration": pa.array([iteration] * len(steps), type=pa.int32()),
    })
    pq.write_table(table, out_path, compression="zstd", compression_level=9)
    print(f"  [rollout-save] {len(steps):,} steps → {out_path}", flush=True)


def run_benchmark(
    checkpoint_path: str,
    n_games: int = 500,
    seed_base: int = 50000,
    collect_stats: bool = False,
    stats_n_games: int = 100,
) -> dict[str, float]:
    """Export current checkpoint and benchmark via tscore.benchmark_batched."""
    script_path = checkpoint_path
    if not script_path.endswith("_scripted.pt"):
        script_path = checkpoint_path.replace(".pt", "_scripted.pt")
    ussr_results = tscore.benchmark_batched(
        script_path, tscore.Side.USSR, n_games,
        pool_size=32, seed=seed_base, nash_temperatures=True,
    )
    us_results = tscore.benchmark_batched(
        script_path, tscore.Side.US, n_games,
        pool_size=32, seed=seed_base + n_games, nash_temperatures=True,
    )
    ussr_wins = sum(1 for r in ussr_results if r.winner == tscore.Side.USSR)
    us_wins = sum(1 for r in us_results if r.winner == tscore.Side.US)
    ussr_wr = ussr_wins / len(ussr_results) if ussr_results else 0.0
    us_wr = us_wins / len(us_results) if us_results else 0.0
    combined = (ussr_wins + us_wins) / (len(ussr_results) + len(us_results)) if (ussr_results and us_results) else 0.0
    result = {"ussr_wr": ussr_wr, "us_wr": us_wr, "combined_wr": combined}
    if collect_stats:
        try:
            if os.path.exists(script_path):
                result["policy_stats"] = collect_policy_stats(
                    script_path, n_games=stats_n_games, seed_base=seed_base + 10000
                )
        except Exception as e:
            print(f"  [stats] policy stats failed: {e}", flush=True)
    return result


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
            example_inputs = (
                torch.zeros((1, 172), dtype=torch.float32),
                torch.zeros((1, 448), dtype=torch.float32),
                torch.zeros((1, 11), dtype=torch.float32),
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


def export_checkpoint(model: nn.Module, checkpoint_path: str, ckpt_meta: dict) -> None:
    """Save model checkpoint in format compatible with benchmark_batched."""
    payload = {"model_state_dict": model.state_dict(), "args": ckpt_meta}
    torch.save(payload, checkpoint_path)
    script_path = checkpoint_path.replace(".pt", "_scripted.pt")
    _export_torchscript_model(model, script_path, warn_only=True)


# ---------------------------------------------------------------------------
# Main training loop
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="PPO fine-tuning for Twilight Struggle AI")
    p.add_argument("--checkpoint", required=True, help="BC checkpoint to warm-start from")
    p.add_argument("--out-dir", required=True, help="Directory for PPO checkpoints")
    p.add_argument("--n-iterations", type=int, default=200, help="PPO iterations")
    p.add_argument("--games-per-iter", type=int, default=200, help="Games per rollout batch")
    p.add_argument("--ppo-epochs", type=int, default=4, help="PPO update epochs per batch")
    p.add_argument("--clip-eps", type=float, default=0.2, help="PPO clip epsilon")
    p.add_argument("--lr", type=float, default=1e-4, help="Learning rate")
    p.add_argument("--gamma", type=float, default=0.99, help="Discount factor")
    p.add_argument("--gae-lambda", type=float, default=0.95, help="GAE lambda")
    p.add_argument("--ent-coef", type=float, default=0.01, help="Initial entropy coefficient")
    p.add_argument("--ent-coef-final", type=float, default=None,
                   help="Final entropy coefficient (linear decay). None = constant")
    p.add_argument("--vf-coef", type=float, default=0.5, help="Value function coefficient")
    p.add_argument("--minibatch-size", type=int, default=2048, help="PPO minibatch size")
    p.add_argument("--benchmark-every", type=int, default=20, help="Benchmark every N iterations")
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
    p.add_argument("--max-kl", type=float, default=0.1, help="Early stop if KL > this")
    p.add_argument("--vp-reward-coef", type=float, default=0.0,
                   help="VP delta reward shaping coefficient (0 = disabled)")
    p.add_argument("--league", type=str, default=None,
                   help="League directory for checkpoint pool self-play (enables league training)")
    p.add_argument("--league-save-every", type=int, default=20,
                   help="Save model to league pool every N iterations (default: 20)")
    p.add_argument("--start-iteration", type=int, default=1,
                   help="Resume: start loop from this iteration (seeds offset accordingly)")
    p.add_argument("--best-combined", type=float, default=0.0,
                   help="Resume: best combined WR achieved so far (for checkpoint tracking)")
    p.add_argument("--save-rollout-parquet", type=str, default=None,
                   help="If set, save each iteration's rollout steps as Parquet to this directory "
                        "(for BC bootstrapping from PPO data). One file per iteration.")
    return p.parse_args()


def main() -> None:
    args = parse_args()

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
            wandb_run = wandb.init(
                project=args.wandb_project,
                name=args.wandb_run_name or f"ppo_{Path(args.out_dir).name}",
                config=vars(args),
            )
        except Exception as e:
            print(f"W&B init failed: {e}, continuing without logging")
            wandb_run = None

    device = args.device
    if device == "cuda" and not torch.cuda.is_available():
        print("CUDA not available, falling back to CPU")
        device = "cpu"

    print(f"Loading checkpoint: {args.checkpoint}")
    model, model_type, ckpt_args = load_model(args.checkpoint, device)

    # Keep a copy of BC checkpoint args for saving
    ckpt_meta = dict(ckpt_args)
    ckpt_meta["model_type"] = model_type

    # Card specs for DEFCON safety and ops values
    from tsrl.etl.game_data import load_cards
    card_specs = load_cards()

    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr)

    # Determine training sides
    if args.side == "ussr":
        sides = [tscore.Side.USSR]
    elif args.side == "us":
        sides = [tscore.Side.US]
    else:
        sides = [tscore.Side.USSR, tscore.Side.US]

    games_per_side = args.games_per_iter // len(sides)

    best_combined = args.best_combined
    best_ckpt_path = os.path.join(args.out_dir, "ppo_best.pt")

    # Track the last rolling checkpoint path so we can delete it after the next
    # successful save.  Milestone checkpoints (benchmark_every multiples and the
    # final iteration) are never deleted.
    last_rolling_ckpt: str | None = None

    def _is_milestone(it: int) -> bool:
        return it % args.benchmark_every == 0 or it == args.n_iterations

    print(f"\nStarting PPO training: {args.n_iterations} iterations × "
          f"{args.games_per_iter} games/iter, side={args.side}", flush=True)
    print(f"Device: {device}, lr={args.lr}, clip={args.clip_eps}, "
          f"ent={args.ent_coef}, vf={args.vf_coef}", flush=True)
    if args.league:
        print(f"League training enabled (pool: {args.league}, save-every={args.league_save_every})", flush=True)
    elif args.self_play:
        print(f"Self-play enabled (heuristic mix={args.self_play_heuristic_mix:.3f})", flush=True)
    if args.start_iteration > 1:
        print(f"Resuming from iteration {args.start_iteration} "
              f"(best_combined={best_combined:.3f})", flush=True)

    t_start = time.time()

    for iteration in range(args.start_iteration, args.n_iterations + 1):
        t_iter_start = time.time()

        # ── Rollout phase ────────────────────────────────────────────────────
        all_steps: list[Step] = []
        self_play_steps: list[Step] = []
        if args.league:
            seed = args.seed + (iteration - 1) * args.games_per_iter
            # Save current checkpoint to league pool before rollout.
            # Add at iteration 1 (so iter 2+ has at least one checkpoint to play against)
            # and every league_save_every iterations.
            if iteration == 1 or iteration % args.league_save_every == 0:
                Path(args.league).mkdir(parents=True, exist_ok=True)
                pool_path = str(Path(args.league) / f"iter_{iteration:04d}.pt")
                _export_torchscript_model(model, pool_path, warn_only=True)
                print(f"  Saved to league pool: {pool_path}", flush=True)
            all_steps = collect_rollout_league_batched(
                model, args.league, args.games_per_iter, seed, device,
                vp_reward_coef=args.vp_reward_coef,
            )
        elif args.self_play:
            seed = args.seed + (iteration - 1) * args.games_per_iter
            self_play_steps = collect_rollout_self_play_batched(
                model, args.games_per_iter, seed, device, vp_reward_coef=args.vp_reward_coef
            )
            all_steps = list(self_play_steps)
            if args.self_play_heuristic_mix > 0:
                n_heur = max(1, int(args.games_per_iter * args.self_play_heuristic_mix))
                heur_steps_ussr = collect_rollout_batched(
                    model, n_heur // 2, tscore.Side.USSR, seed + 1000000, device, card_specs,
                    vp_reward_coef=args.vp_reward_coef,
                )
                heur_steps_us = collect_rollout_batched(
                    model, n_heur // 2, tscore.Side.US, seed + 2000000, device, card_specs,
                    vp_reward_coef=args.vp_reward_coef,
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
                )
                all_steps.extend(steps)

        n_steps = len(all_steps)
        if n_steps == 0:
            print(f"[iter {iteration}] No steps collected, skipping")
            continue

        # Optionally save rollout steps as Parquet for BC bootstrapping
        if args.save_rollout_parquet and all_steps:
            _save_rollout_parquet(all_steps, args.save_rollout_parquet, iteration)

        # Compute GAE advantages
        compute_gae_batch(all_steps, gamma=args.gamma, lam=args.gae_lambda)

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
        # Entropy scheduling: linear decay from ent_coef to ent_coef_final
        if args.ent_coef_final is not None:
            t_frac = (iteration - 1) / max(1, args.n_iterations - 1)
            current_ent_coef = args.ent_coef + t_frac * (args.ent_coef_final - args.ent_coef)
        else:
            current_ent_coef = args.ent_coef

        t_update_start = time.time()
        metrics = ppo_update(
            all_steps, model, optimizer, device,
            ppo_epochs=args.ppo_epochs,
            clip_eps=args.clip_eps,
            vf_coef=args.vf_coef,
            ent_coef=current_ent_coef,
            minibatch_size=args.minibatch_size,
        )
        t_update = time.time() - t_update_start
        t_iter = time.time() - t_iter_start

        # Early stopping on KL divergence
        if metrics.get("approx_kl", 0) > args.max_kl:
            print(f"[iter {iteration}] KL divergence {metrics['approx_kl']:.4f} > "
                  f"{args.max_kl:.4f}, stopping early")
            break

        print(
            f"[iter {iteration:3d}/{args.n_iterations}] "
            f"steps={n_steps:5d} "
            f"rollout_wr={rollout_wr:.3f} (ussr={rollout_wr_ussr:.3f} us={rollout_wr_us:.3f}) "
            f"pl={metrics.get('policy_loss', 0):.4f} "
            f"vl={metrics.get('value_loss', 0):.4f} "
            f"ent={metrics.get('entropy', 0):.3f} "
            f"clip={metrics.get('clip_fraction', 0):.3f} "
            f"kl={metrics.get('approx_kl', 0):.4f} "
            f"t={t_iter:.1f}s (rollout={t_rollout:.1f}s update={t_update:.1f}s)",
            flush=True,
        )

        # ── Rolling checkpoint (every iteration) ─────────────────────────────
        # Write new checkpoint first, then delete the previous non-milestone one.
        # This ensures we always have the latest weights even after a crash.
        new_ckpt_path = os.path.join(args.out_dir, f"ppo_iter{iteration:04d}.pt")
        export_checkpoint(model, new_ckpt_path, ckpt_meta)
        # Delete previous rolling checkpoint if it was not a milestone.
        if last_rolling_ckpt is not None and not _is_milestone(
            int(os.path.basename(last_rolling_ckpt).removeprefix("ppo_iter").split(".")[0])
        ):
            try:
                os.remove(last_rolling_ckpt)
                scripted = last_rolling_ckpt.replace(".pt", "_scripted.pt")
                if os.path.exists(scripted):
                    os.remove(scripted)
            except OSError:
                pass
        last_rolling_ckpt = new_ckpt_path

        # ── Periodic benchmark ────────────────────────────────────────────────
        if _is_milestone(iteration):
            ckpt_path = new_ckpt_path

            print(f"  Running benchmark (500 games each side)...")
            t_bench_start = time.time()
            bench = run_benchmark(
                ckpt_path.replace(".pt", "_scripted.pt"),
                n_games=500, seed_base=50000,
                collect_stats=True, stats_n_games=100,
            )
            t_bench = time.time() - t_bench_start
            print(
                f"  Benchmark: USSR={bench['ussr_wr']:.3f} "
                f"US={bench['us_wr']:.3f} "
                f"combined={bench['combined_wr']:.3f} "
                f"({t_bench:.0f}s)"
            )

            if bench["combined_wr"] > best_combined:
                best_combined = bench["combined_wr"]
                export_checkpoint(model, best_ckpt_path, ckpt_meta)
                print(f"  New best: combined={best_combined:.3f}")

            if wandb_run is not None:
                metrics.update({
                    "ussr_wr": bench["ussr_wr"],
                    "us_wr": bench["us_wr"],
                    "combined_wr": bench["combined_wr"],
                    "rollout_wr": rollout_wr,
                    "rollout_wr_ussr": rollout_wr_ussr,
                    "rollout_wr_us": rollout_wr_us,
                    "n_steps": n_steps,
                    "iter_time_s": t_iter,
                })
                if args.self_play:
                    metrics["sp_rollout_wr_ussr"] = sp_rollout_wr_ussr
                    metrics["sp_rollout_wr_us"] = sp_rollout_wr_us
                wandb_run.log(metrics, step=iteration)
                if "policy_stats" in bench and wandb_run and bench["policy_stats"]:
                    wandb_run.log(bench["policy_stats"], step=iteration)
        else:
            if wandb_run is not None:
                log_dict = dict(metrics)
                log_dict["rollout_wr"] = rollout_wr
                log_dict["rollout_wr_ussr"] = rollout_wr_ussr
                log_dict["rollout_wr_us"] = rollout_wr_us
                log_dict["n_steps"] = n_steps
                log_dict["iter_time_s"] = t_iter
                log_dict["ent_coef"] = current_ent_coef
                if args.self_play:
                    log_dict["sp_rollout_wr_ussr"] = sp_rollout_wr_ussr
                    log_dict["sp_rollout_wr_us"] = sp_rollout_wr_us
                wandb_run.log(log_dict, step=iteration)

    # ── Final checkpoint + summary ────────────────────────────────────────────
    final_path = os.path.join(args.out_dir, "ppo_final.pt")
    export_checkpoint(model, final_path, ckpt_meta)

    t_total = time.time() - t_start
    print(f"\nTraining complete in {t_total/60:.1f} minutes")
    print(f"Best combined WR: {best_combined:.3f}")
    print(f"Checkpoints in: {args.out_dir}")

    if wandb_run is not None:
        wandb_run.finish()


if __name__ == "__main__":
    main()
