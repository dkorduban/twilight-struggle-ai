#!/usr/bin/env python3
"""Collect BC training data from strong model play.

Uses Python-side inference (11-dim scalars for old checkpoints) with
play_callback_matchup (one game at a time for correct game-boundary tracking).
Records each decision step with full game state including all active-effect
booleans from the callback state dict.

Output: Parquet files in --out-dir with all columns needed by TS_SelfPlayDataset.

Usage:
    # 0.5M tier: 4000 games of v3 vs heuristic
    uv run python scripts/collect_bc_dataset.py \\
        --model data/checkpoints/ppo_v3_league/ppo_best.pt \\
        --n-games 4000 --out-dir data/v3_selfplay --seed 90000 --tag v3

    # Collect from a league pool member
    uv run python scripts/collect_bc_dataset.py \\
        --model data/checkpoints/league_v3/iter_0100.pt \\
        --n-games 2000 --out-dir data/v3_selfplay --seed 92000 --tag v3_iter100
"""
from __future__ import annotations

import argparse
import os
import sys
import time
import uuid
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq
import torch

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT / "build-ninja" / "bindings") not in sys.path:
    sys.path.insert(0, str(_ROOT / "build-ninja" / "bindings"))
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import tscore  # noqa: E402

_EFFECT_BOOL_COLS = [
    "bear_trap_active", "quagmire_active", "cuban_missile_crisis_active",
    "iran_hostage_crisis_active", "norad_active", "shuttle_diplomacy_active",
    "salt_active", "flower_power_active", "flower_power_cancelled",
    "vietnam_revolts_active", "north_sea_oil_extra_ar",
    "glasnost_extra_ar", "nato_active", "de_gaulle_active",
    "nuclear_subs_active", "formosan_active", "awacs_active",
]

CARD_SLOTS = 112
COUNTRY_SLOTS = 86
DEFCON_LOWERING_CARDS = frozenset({
    4, 11, 13, 20, 24, 39, 48, 49, 50, 53, 83, 92, 105,
})


def load_model(checkpoint_path: str, device: str = "cpu"):
    from python.tsrl.policies.model import (
        TSBaselineModel, TSControlFeatGNNModel, TSControlFeatGNNSideModel,
        TSCardEmbedModel, TSCountryAttnModel, TSCountryAttnSideModel,
    )
    import python.tsrl.policies.model as model_module
    MODEL_REGISTRY = {
        "baseline": TSBaselineModel,
        "card_embed": TSCardEmbedModel,
        "country_attn": TSCountryAttnModel,
        "country_attn_side": TSCountryAttnSideModel,
        "control_feat_gnn": TSControlFeatGNNModel,
        "control_feat_gnn_side": TSControlFeatGNNSideModel,
    }
    ckpt = torch.load(checkpoint_path, map_location="cpu", weights_only=False)

    # TorchScript models (league checkpoints) don't have a dict interface.
    # Use them directly for inference; detect scalar_dim from their state_dict().
    if hasattr(ckpt, "graph"):  # TorchScript models have a .graph attribute
        _REGION_SCALAR_DIM = 28
        detected_dim = 11  # default for pre-kScalarDim=32 TorchScript models
        for k, v in ckpt.state_dict().items():
            if "scalar_encoder" in k and "weight" in k and len(v.shape) == 2:
                raw = v.shape[1]
                detected_dim = raw - _REGION_SCALAR_DIM if raw > _REGION_SCALAR_DIM else raw
                break
        ckpt.eval()
        ckpt.to(device)
        print(f"[collect_bc_dataset] TorchScript model detected, scalar_dim={detected_dim}")
        return ckpt, detected_dim

    state_dict = ckpt.get("model_state_dict", ckpt)
    args_d = ckpt.get("args", {})
    hidden_dim = args_d.get("hidden_dim", 256)
    model_type = args_d.get("model_type", "baseline")
    dropout = args_d.get("dropout", 0.1)
    cls = MODEL_REGISTRY.get(model_type, TSControlFeatGNNSideModel)

    # Detect actual scalar dim from checkpoint to handle 11-dim old models.
    # GNN-side models: scalar_encoder input = SCALAR_DIM + 28 (region scalars).
    # Non-GNN models: scalar_encoder input = SCALAR_DIM directly.
    orig_scalar_dim = model_module.SCALAR_DIM
    detected_dim = orig_scalar_dim
    _REGION_SCALAR_DIM = 28  # constant in TSControlFeatGNNSideModel
    for k, v in state_dict.items():
        if "scalar_encoder" in k and "weight" in k and len(v.shape) == 2:
            raw = v.shape[1]
            # Try GNN-side variant first (SCALAR_DIM + 28)
            if raw > _REGION_SCALAR_DIM:
                detected_dim = raw - _REGION_SCALAR_DIM
            else:
                detected_dim = raw
            model_module.SCALAR_DIM = detected_dim
            break

    model = cls(hidden_dim=hidden_dim, dropout=dropout)
    model.load_state_dict(state_dict, strict=False)
    model.eval()
    model.to(device)
    model_module.SCALAR_DIM = orig_scalar_dim
    return model, detected_dim


def _card_mask(cards) -> list[float]:
    mask = [0.0] * CARD_SLOTS
    for cid in cards:
        if 0 < cid < CARD_SLOTS:
            mask[cid] = 1.0
    return mask


def _build_scalars_11(state, hand, holds_china, side_int) -> list[float]:
    return [
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


def _infer(model, scalar_dim, state, hand, holds_china, side_int, device, card_specs):
    """Run model inference and return (card_id, mode, targets) or None."""
    if not hand:
        return None

    ussr = [float(x) for x in state["ussr_influence"]]
    us_inf = [float(x) for x in state["us_influence"]]
    influence = torch.tensor([ussr + us_inf], dtype=torch.float32, device=device)

    hand_mask = _card_mask(hand)
    cards_feat = torch.tensor(
        [hand_mask + hand_mask + _card_mask(state["discard"]) + _card_mask(state["removed"])],
        dtype=torch.float32, device=device
    )

    sc = _build_scalars_11(state, hand, holds_china, side_int)
    scalars = torch.tensor([sc], dtype=torch.float32, device=device)

    with torch.no_grad():
        outputs = model(influence, cards_feat, scalars)

    card_logits = outputs["card_logits"][0].cpu()
    mode_logits = outputs["mode_logits"][0].cpu()
    country_logits = outputs.get("country_logits")
    if country_logits is not None:
        country_logits = country_logits[0].cpu()

    defcon = state["defcon"]
    ar = state["ar"]

    masked = torch.full((card_logits.shape[0],), float("-inf"))
    for cid in hand:
        idx = cid - 1
        if not (0 <= idx < masked.shape[0]):
            continue
        if cid in DEFCON_LOWERING_CARDS:
            from python.tsrl.schemas import Side as PySide
            spec = card_specs.get(cid)
            if spec is not None:
                cs = spec.side
                is_opp = cs != PySide(side_int) and cs != PySide.NEUTRAL
                is_neutral = cs == PySide.NEUTRAL
                if is_opp and defcon <= 2:
                    continue
                if is_opp and defcon == 3 and ar == 0:
                    continue
                if is_neutral and ar == 0 and defcon <= 3:
                    continue
        masked[idx] = card_logits[idx]

    if masked.max().item() == float("-inf"):
        for cid in hand:
            idx = cid - 1
            if 0 <= idx < masked.shape[0]:
                masked[idx] = card_logits[idx]

    if masked.max().item() == float("-inf"):
        return None

    card_id = int(masked.argmax().item()) + 1
    mode = int(mode_logits.argmax().item())

    if mode == 1 and defcon <= 2:
        ml = mode_logits.clone()
        ml[1] = float("-inf")
        mode = int(ml.argmax().item())

    if mode in (3, 4):
        return card_id, mode, []

    if country_logits is not None:
        if mode in (1, 2):
            return card_id, mode, [int(country_logits.argmax().item())]
        spec = card_specs.get(card_id)
        ops = max(1, getattr(spec, "ops", 1) or 1) if spec else 1
        probs = torch.softmax(country_logits, dim=0)
        alloc = probs * ops
        floor_alloc = torch.floor(alloc).long()
        rem = ops - int(floor_alloc.sum().item())
        if rem > 0:
            frac = alloc - floor_alloc.float()
            _, top_idx = frac.topk(min(rem, len(frac)))
            for i in top_idx:
                floor_alloc[i] += 1
        targets = [c for c in range(COUNTRY_SLOTS) for _ in range(int(floor_alloc[c].item()))]
        return card_id, mode, targets

    return card_id, mode, [0]


def collect_one_game(model, scalar_dim, card_specs, device, side: tscore.Side, seed: int) -> tuple[list[dict], dict]:
    """Collect one game. Returns (steps, game_result)."""
    steps: list[dict] = []

    def cb(state, hand, holds_china, side_int):
        result = _infer(model, scalar_dim, state, hand, holds_china, side_int, device, card_specs)
        if result is None:
            return None
        card_id, mode, targets = result
        step = {
            "step_idx": len(steps),
            "ussr_influence": list(state["ussr_influence"]),
            "us_influence": list(state["us_influence"]),
            "actor_known_in": _card_mask(hand),
            "actor_possible": _card_mask(hand),
            "discard_mask": _card_mask(state["discard"]),
            "removed_mask": _card_mask(state["removed"]),
            "vp": int(state["vp"]),
            "defcon": int(state["defcon"]),
            "milops_ussr": int(state["milops"][0]),
            "milops_us": int(state["milops"][1]),
            "space_ussr": int(state["space"][0]),
            "space_us": int(state["space"][1]),
            "china_held_by": int(state["china_held_by"]),
            "actor_holds_china": int(holds_china),
            "turn": int(state["turn"]),
            "ar": int(state["ar"]),
            "phasing": int(side_int),
            "action_card_id": card_id,
            "action_mode": mode,
            "action_targets": ",".join(str(t) for t in targets),
            **{col: int(bool(state.get(col, False))) for col in _EFFECT_BOOL_COLS},
            "ops_modifier": list(state.get("ops_modifier", (0, 0))),
        }
        steps.append(step)
        return {"card_id": card_id, "mode": mode, "targets": targets}

    results = tscore.play_callback_matchup(
        cb, side, tscore.PolicyKind.MinimalHybrid, 1, seed=seed
    )
    r = results[0]
    winner = r.winner
    winner_side = 0.0 if winner == tscore.Side.USSR else (1.0 if winner == tscore.Side.US else 0.0)
    final_vp = getattr(r, "final_vp", 0)
    end_reason = getattr(r, "end_reason", "")
    game_meta = {"winner_side": winner_side, "final_vp": int(final_vp), "end_reason": end_reason}
    return steps, game_meta


def collect_selfplay(model, scalar_dim, card_specs, device, n_games: int, seed: int, verbose_every: int = 100) -> list[dict]:
    """Collect n_games of model-vs-self using dual callback — records BOTH sides per game.
    Yields ~2× rows vs collect_side for the same number of games.
    """
    all_steps = []
    t0 = time.time()
    ussr_wins = us_wins = draws = 0

    for i in range(n_games):
        game_id = str(uuid.uuid4())
        steps: list[dict] = []

        def cb(state, hand, holds_china, side_int, _steps=steps):
            result = _infer(model, scalar_dim, state, hand, holds_china, side_int, device, card_specs)
            if result is None:
                return None
            card_id, mode, targets = result
            step = {
                "step_idx": len(_steps),
                "ussr_influence": list(state["ussr_influence"]),
                "us_influence": list(state["us_influence"]),
                "actor_known_in": _card_mask(hand),
                "actor_possible": _card_mask(hand),
                "discard_mask": _card_mask(state["discard"]),
                "removed_mask": _card_mask(state["removed"]),
                "vp": int(state["vp"]),
                "defcon": int(state["defcon"]),
                "milops_ussr": int(state["milops"][0]),
                "milops_us": int(state["milops"][1]),
                "space_ussr": int(state["space"][0]),
                "space_us": int(state["space"][1]),
                "china_held_by": int(state["china_held_by"]),
                "actor_holds_china": int(holds_china),
                "turn": int(state["turn"]),
                "ar": int(state["ar"]),
                "phasing": int(side_int),
                "action_card_id": card_id,
                "action_mode": mode,
                "action_targets": ",".join(str(t) for t in targets),
                **{col: int(bool(state.get(col, False))) for col in _EFFECT_BOOL_COLS},
                "ops_modifier": list(state.get("ops_modifier", (0, 0))),
            }
            _steps.append(step)
            return {"card_id": card_id, "mode": mode, "targets": targets}

        results = tscore.play_dual_callback_matchup(cb, game_count=1, seed=seed + i)
        r = results[0]
        winner = r.winner
        winner_side = 0.0 if winner == tscore.Side.USSR else (1.0 if winner == tscore.Side.US else 0.0)
        final_vp = getattr(r, "final_vp", 0)
        end_reason = getattr(r, "end_reason", "")

        if winner == tscore.Side.USSR:
            ussr_wins += 1
        elif winner == tscore.Side.US:
            us_wins += 1
        else:
            draws += 1

        for step in steps:
            step["game_id"] = game_id
            step["winner_side"] = winner_side
            step["final_vp"] = int(final_vp)
            step["end_reason"] = end_reason
        all_steps.extend(steps)

        if (i + 1) % verbose_every == 0:
            elapsed = time.time() - t0
            gps = (i + 1) / elapsed
            print(f"    game {i+1}/{n_games}  steps={len(all_steps):,}  {gps:.1f} games/s  "
                  f"ussr={ussr_wins} us={us_wins} draws={draws}")

    elapsed = time.time() - t0
    print(f"  selfplay: {len(all_steps):,} steps in {elapsed:.1f}s ({n_games/elapsed:.1f} games/s, "
          f"{len(all_steps)/n_games:.1f} steps/game)")
    return all_steps


def collect_side(model, scalar_dim, card_specs, device, side: tscore.Side, n_games: int, seed: int, verbose_every: int = 100) -> list[dict]:
    all_steps = []
    t0 = time.time()
    ussr_wins = us_wins = draws = 0

    for i in range(n_games):
        game_id = str(uuid.uuid4())
        steps, meta = collect_one_game(model, scalar_dim, card_specs, device, side, seed + i)
        ws = meta["winner_side"]
        if ws == 0.0:
            ussr_wins += 1
        elif ws == 1.0:
            us_wins += 1
        else:
            draws += 1
        for step in steps:
            step["game_id"] = game_id
            step["winner_side"] = meta["winner_side"]
            step["final_vp"] = meta["final_vp"]
            step["end_reason"] = meta["end_reason"]
        all_steps.extend(steps)

        if (i + 1) % verbose_every == 0:
            elapsed = time.time() - t0
            gps = (i + 1) / elapsed
            print(f"    game {i+1}/{n_games}  steps={len(all_steps):,}  {gps:.1f} games/s  "
                  f"ussr={ussr_wins} us={us_wins} draws={draws}")

    elapsed = time.time() - t0
    side_name = "USSR" if side == tscore.Side.USSR else "US"
    print(f"  {side_name}: {len(all_steps):,} steps in {elapsed:.1f}s ({n_games/elapsed:.1f} games/s)")
    return all_steps


def write_parquet(steps: list[dict], out_path: str) -> int:
    if not steps:
        return 0
    N = len(steps)

    def col(k, t=None):
        v = [s[k] for s in steps]
        return pa.array(v, type=t) if t else pa.array(v)

    arrays = {
        "game_id":         col("game_id"),
        "step_idx":        col("step_idx", pa.int64()),
        "ussr_influence":  pa.array([s["ussr_influence"] for s in steps], pa.list_(pa.int32())),
        "us_influence":    pa.array([s["us_influence"] for s in steps],   pa.list_(pa.int32())),
        "actor_known_in":  pa.array([s["actor_known_in"] for s in steps], pa.list_(pa.float32())),
        "actor_possible":  pa.array([s["actor_possible"] for s in steps], pa.list_(pa.float32())),
        "discard_mask":    pa.array([s["discard_mask"] for s in steps],   pa.list_(pa.float32())),
        "removed_mask":    pa.array([s["removed_mask"] for s in steps],   pa.list_(pa.float32())),
        "vp":              col("vp",           pa.int32()),
        "defcon":          col("defcon",       pa.int32()),
        "milops_ussr":     col("milops_ussr",  pa.int32()),
        "milops_us":       col("milops_us",    pa.int32()),
        "space_ussr":      col("space_ussr",   pa.int32()),
        "space_us":        col("space_us",     pa.int32()),
        "china_held_by":   col("china_held_by",    pa.int32()),
        "actor_holds_china": col("actor_holds_china", pa.int32()),
        "turn":            col("turn",   pa.int32()),
        "ar":              col("ar",     pa.int32()),
        "phasing":         col("phasing", pa.int32()),
        "action_card_id":  col("action_card_id", pa.int32()),
        "action_mode":     col("action_mode",    pa.int32()),
        "action_targets":  col("action_targets"),
        "winner_side":     col("winner_side",  pa.float32()),
        "final_vp":        col("final_vp",     pa.int32()),
        "end_reason":      col("end_reason"),
        "ops_modifier":    pa.array([s["ops_modifier"] for s in steps], pa.list_(pa.int32())),
    }
    for eff_col in _EFFECT_BOOL_COLS:
        arrays[eff_col] = col(eff_col, pa.int8())

    pq.write_table(pa.table(arrays), out_path, compression="snappy")
    print(f"  Wrote {N:,} rows → {out_path}")
    return N


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--n-games", type=int, default=4000)
    parser.add_argument("--out-dir", default="data/v3_selfplay")
    parser.add_argument("--seed", type=int, default=90000)
    parser.add_argument("--tag", default="v3")
    parser.add_argument("--device", default="cpu", choices=["cpu", "cuda"])
    parser.add_argument(
        "--mode", default="onesided", choices=["onesided", "selfplay"],
        help="onesided: collect N/2 USSR + N/2 US games vs heuristic (default). "
             "selfplay: collect N games model-vs-self, recording BOTH sides (~2× rows/game)."
    )
    args = parser.parse_args()

    print(f"[collect_bc_dataset] model: {args.model}")
    print(f"[collect_bc_dataset] n_games={args.n_games}, seed={args.seed}, out={args.out_dir}, mode={args.mode}")

    model, scalar_dim = load_model(args.model, args.device)
    print(f"[collect_bc_dataset] detected scalar_dim={scalar_dim}, device={args.device}")

    from python.tsrl.etl.game_data import load_cards
    card_specs = load_cards()

    os.makedirs(args.out_dir, exist_ok=True)

    if args.mode == "selfplay":
        print(f"\nSelf-play (dual callback): {args.n_games} games (seed={args.seed})...")
        steps = collect_selfplay(model, scalar_dim, card_specs, args.device,
                                 args.n_games, args.seed)
        out_path = os.path.join(args.out_dir, f"{args.tag}_selfplay_{args.n_games}g_s{args.seed}.parquet")
        total = write_parquet(steps, out_path)
    else:
        n_half = args.n_games // 2

        print(f"\nUSSR side: {n_half} games (seed={args.seed})...")
        steps_ussr = collect_side(model, scalar_dim, card_specs, args.device,
                                   tscore.Side.USSR, n_half, args.seed)
        write_parquet(steps_ussr, os.path.join(args.out_dir, f"{args.tag}_ussr_{n_half}g_s{args.seed}.parquet"))

        seed_us = args.seed + n_half
        print(f"\nUS side: {n_half} games (seed={seed_us})...")
        steps_us = collect_side(model, scalar_dim, card_specs, args.device,
                                 tscore.Side.US, n_half, seed_us)
        write_parquet(steps_us, os.path.join(args.out_dir, f"{args.tag}_us_{n_half}g_s{seed_us}.parquet"))

        total = len(steps_ussr) + len(steps_us)

    print(f"\n[collect_bc_dataset] Done. Total: {total:,} steps")


if __name__ == "__main__":
    main()
