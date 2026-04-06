#!/usr/bin/env python3
"""GPU-accelerated benchmark: learned policy vs heuristic.

Uses the C++ game engine via play_callback_matchup, with a Python callback
that does GPU inference. The C++ side handles the game loop and heuristic
opponent; the Python side provides the learned policy via neural network.

Usage:
    uv run python scripts/bench_gpu.py \
        --checkpoint data/checkpoints/retrain_v65/baseline_best.pt \
        --n-games 500 --seed 9999

This is ~2-3x faster than bench_cpp.sh because:
  - GPU inference (even single-sample) avoids CPU TorchScript overhead
  - No subprocess spawning or TorchScript export step
  - Direct Python→C++ call via pybind11
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

import torch

# Ensure the build-ninja bindings are importable
_bindings_dir = str(Path(__file__).resolve().parent.parent / "build-ninja" / "bindings")
if _bindings_dir not in sys.path:
    sys.path.insert(0, _bindings_dir)

import tscore  # noqa: E402

# ── Constants matching C++ nn_features.cpp ──────────────────────────────────
CARD_SLOTS = 112    # kMaxCardId(111) + 1; index 0 unused
COUNTRY_SLOTS = 86  # kMaxCountryId(85) + 1; IDs 0..85
SCALAR_DIM = 11

# DEFCON-lowering cards (must stay in sync with C++ learned_policy.cpp)
DEFCON_LOWERING_CARDS = frozenset({
    4, 11, 13, 20, 24, 39, 48, 49, 50, 53, 83, 92, 105,
})


def load_model(checkpoint_path: str, device: str = "cuda"):
    """Load a TSBaselineModel checkpoint onto the given device."""
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

    cls = MODEL_REGISTRY.get(model_type, TSBaselineModel)
    model = cls(hidden_dim=hidden_dim, dropout=dropout)
    model.load_state_dict(state_dict, strict=False)
    model.eval()
    model.to(device)
    return model


def _card_mask(card_ids: list[int]) -> list[float]:
    """Binary mask of length CARD_SLOTS."""
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
    """Build (influence, cards, scalars) tensors from C++ state dict + hand.

    Matches the C++ nn_features.cpp feature extraction exactly.
    Returns CPU tensors of shape (1, D) for each.
    """
    ussr_inf = state["ussr_influence"]  # list[int], len 86
    us_inf = state["us_influence"]      # list[int], len 86

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


def make_gpu_policy(model: torch.nn.Module, device: str = "cuda"):
    """Return a callback function for play_callback_matchup.

    The callback:
    1. Extracts features from the C++ state dict
    2. Runs GPU inference
    3. Decodes action (argmax card from hand, argmax mode, country allocation)
    """
    from tsrl.etl.game_data import load_cards
    card_specs = load_cards()

    def policy_callback(state: dict, hand: list[int], holds_china: bool, side_int: int):
        if not hand:
            return None

        side_enum = tscore.Side.USSR if side_int == 0 else tscore.Side.US

        # Extract features and move to GPU
        influence, cards, scalars = extract_features(state, hand, holds_china, side_int)
        influence = influence.to(device)
        cards = cards.to(device)
        scalars = scalars.to(device)

        with torch.no_grad():
            outputs = model(influence, cards, scalars)

        card_logits = outputs["card_logits"][0].cpu()  # (CARD_SLOTS-1,) or (CARD_SLOTS,)
        mode_logits = outputs["mode_logits"][0].cpu()   # (5,)

        # Country logits for target allocation
        country_logits = outputs.get("country_logits")
        if country_logits is not None:
            country_logits = country_logits[0].cpu()  # (86,)

        # ── Card selection with DEFCON safety ───────────────────────────
        defcon = state["defcon"]
        ar = state["ar"]
        playable = set(hand)

        masked_card = torch.full((card_logits.shape[0],), float("-inf"))
        for card_id in playable:
            idx = card_id - 1
            if idx < 0 or idx >= masked_card.shape[0]:
                continue

            # DEFCON safety
            if card_id in DEFCON_LOWERING_CARDS:
                spec = card_specs.get(card_id)
                if spec is not None:
                    card_side = spec.side
                    from tsrl.schemas import Side as PySide
                    is_opp = card_side != PySide(side_int) and card_side != PySide.NEUTRAL
                    is_neutral = card_side == PySide.NEUTRAL
                    if is_opp and defcon <= 2:
                        continue
                    if is_opp and defcon == 3 and ar == 0:
                        continue
                    if is_neutral and ar == 0 and defcon <= 3:
                        continue

            masked_card[idx] = card_logits[idx]

        # If all masked, allow all hand cards (fallback)
        if masked_card.max().item() == float("-inf"):
            for card_id in playable:
                idx = card_id - 1
                if 0 <= idx < masked_card.shape[0]:
                    masked_card[idx] = card_logits[idx]

        if masked_card.max().item() == float("-inf"):
            return None

        card_id = int(masked_card.argmax().item()) + 1

        # ── Mode selection ──────────────────────────────────────────────
        # Simple argmax over all 5 modes. Not perfectly legal-aware, but
        # the model strongly prefers legal modes from training.
        mode = int(mode_logits.argmax().item())

        # DEFCON safety: no coup at DEFCON <= 2
        if mode == 1 and defcon <= 2:  # 1 = Coup
            mode_logits_safe = mode_logits.clone()
            mode_logits_safe[1] = float("-inf")
            mode = int(mode_logits_safe.argmax().item())

        # DEFCON safety: no event for DEFCON-lowering cards at DEFCON <= 2
        if mode == 4 and defcon <= 2 and card_id in DEFCON_LOWERING_CARDS:  # 4 = Event
            mode_logits_safe = mode_logits.clone()
            mode_logits_safe[4] = float("-inf")
            mode = int(mode_logits_safe.argmax().item())

        # ── Target allocation ───────────────────────────────────────────
        # Space (3) and Event (4) have no targets
        if mode in (3, 4):
            return {"card_id": card_id, "mode": mode, "targets": []}

        # For Influence (0), Coup (1), Realign (2): use country logits
        if mode in (1, 2):
            # Coup/Realign: pick top accessible country
            if country_logits is not None:
                target = int(country_logits.argmax().item())
            else:
                target = 0  # fallback
            return {"card_id": card_id, "mode": mode, "targets": [target]}

        # Influence: allocate ops proportionally
        if country_logits is not None:
            # Estimate ops (simplified: use card's ops value)
            ops = _estimate_ops(card_id, card_specs)
            probs = torch.softmax(country_logits, dim=0)
            alloc = probs * ops
            floor_alloc = torch.floor(alloc).long()
            remainder = ops - int(floor_alloc.sum().item())

            if remainder > 0:
                fractional = alloc - floor_alloc.float()
                _, top_indices = fractional.topk(min(remainder, len(fractional)))
                for idx in top_indices:
                    floor_alloc[idx] += 1

            targets = []
            for country_id in range(COUNTRY_SLOTS):
                count = int(floor_alloc[country_id].item())
                targets.extend([country_id] * count)
            return {"card_id": card_id, "mode": mode, "targets": targets}

        # Fallback: no country logits, just place everything on country 0
        return {"card_id": card_id, "mode": mode, "targets": [0]}

    return policy_callback


def _estimate_ops(card_id: int, card_specs: dict) -> int:
    """Get ops value for a card."""
    spec = card_specs.get(card_id)
    if spec is None:
        return 1
    return max(1, getattr(spec, "ops", 1) or 1)


def run_benchmark(
    checkpoint: str,
    n_games: int,
    seed: int,
    learned_side: str,
    device: str,
) -> dict:
    """Run benchmark and return results dict."""
    model = load_model(checkpoint, device)
    callback = make_gpu_policy(model, device)

    results = {}

    if learned_side in ("ussr", "both"):
        n_ussr = n_games if learned_side == "ussr" else (n_games + 1) // 2
        t0 = time.time()
        ussr_results = tscore.play_callback_matchup(
            callback,
            tscore.Side.USSR,
            tscore.PolicyKind.MinimalHybrid,
            n_ussr,
            seed=seed,
        )
        t_ussr = time.time() - t0
        summary = tscore.summarize_results(ussr_results)
        results["ussr"] = {
            "games": summary.games,
            "learned_wins": summary.ussr_wins,
            "opponent_wins": summary.us_wins,
            "draws": summary.draws,
            "elapsed_s": round(t_ussr, 1),
            "games_per_sec": round(summary.games / t_ussr, 1) if t_ussr > 0 else 0,
        }

    if learned_side in ("us", "both"):
        n_us = n_games if learned_side == "us" else n_games // 2
        seed_us = seed + (n_games if learned_side == "both" else 0)
        t0 = time.time()
        us_results = tscore.play_callback_matchup(
            callback,
            tscore.Side.US,
            tscore.PolicyKind.MinimalHybrid,
            n_us,
            seed=seed_us,
        )
        t_us = time.time() - t0
        summary = tscore.summarize_results(us_results)
        results["us"] = {
            "games": summary.games,
            "learned_wins": summary.us_wins,
            "opponent_wins": summary.ussr_wins,
            "draws": summary.draws,
            "elapsed_s": round(t_us, 1),
            "games_per_sec": round(summary.games / t_us, 1) if t_us > 0 else 0,
        }

    return results


def print_results(results: dict):
    """Pretty-print benchmark results."""
    for side_name, data in results.items():
        total = data["games"]
        wins = data["learned_wins"]
        losses = data["opponent_wins"]
        draws = data["draws"]
        decisive = total - draws
        wr = wins / decisive * 100 if decisive > 0 else 0
        speed = data["games_per_sec"]
        print(
            f"  learned ({side_name.upper()}) vs heuristic: "
            f"{wins}/{decisive} ({wr:.1f}%)  "
            f"Draw {draws}/{total}  "
            f"[{data['elapsed_s']}s, {speed} games/s]"
        )


def main():
    parser = argparse.ArgumentParser(description="GPU-accelerated benchmark")
    parser.add_argument("--checkpoint", required=True, help="Path to .pt checkpoint")
    parser.add_argument("--n-games", type=int, default=500)
    parser.add_argument("--seed", type=int, default=9999)
    parser.add_argument("--learned-side", default="both", choices=["ussr", "us", "both"])
    parser.add_argument("--device", default="cuda", choices=["cuda", "cpu"])
    parser.add_argument("--out", default=None, help="Optional JSON output path")
    args = parser.parse_args()

    if args.device == "cuda" and not torch.cuda.is_available():
        print("CUDA not available, falling back to CPU")
        args.device = "cpu"

    print(f"[bench_gpu] checkpoint: {args.checkpoint}")
    print(f"[bench_gpu] device: {args.device}, n_games: {args.n_games}, seed: {args.seed}")

    t_start = time.time()
    results = run_benchmark(
        args.checkpoint,
        args.n_games,
        args.seed,
        args.learned_side,
        args.device,
    )
    t_total = time.time() - t_start

    print(f"\n[bench_gpu] Results ({t_total:.1f}s total):")
    print_results(results)

    if args.out:
        os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
        with open(args.out, "w") as f:
            json.dump(results, f, indent=2)
        print(f"\n[bench_gpu] Saved to {args.out}")


if __name__ == "__main__":
    main()
