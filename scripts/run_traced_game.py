#!/usr/bin/env python3
"""Run one traced self-play game and print a human-readable action log.

Usage:
    PYTHONPATH=build-ninja/bindings uv run python scripts/run_traced_game.py [--model PATH] [--seed N] [--heuristic]
"""
from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

import torch

sys.path.insert(0, "build-ninja/bindings")

_REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO_ROOT / "python"))

import tscore  # noqa: E402
from tsrl.etl.game_data import load_cards, load_countries  # noqa: E402

_DEFAULT_MODEL = Path("data/checkpoints/scripted_for_elo/v55_scripted.pt")
_COUNTRY_COUNT = 86
_CARD_MASK_SLOTS = 112

_MODE_INFLUENCE = 0
_MODE_COUP = 1
_MODE_REALIGN = 2
_MODE_SPACE = 3
_MODE_EVENT = 4


# ---------------------------------------------------------------------------
# Formatting helpers copied from scripts/run_mcts_game.py
# ---------------------------------------------------------------------------

def _card_name(card_id: int, cards: dict) -> str:
    spec = cards.get(card_id)
    return spec.name if spec else f"card#{card_id}"


def _country_name(cid: int, countries: dict) -> str:
    spec = countries.get(cid)
    return spec.name if spec else f"country#{cid}"


def _side_str(side: tscore.Side) -> str:
    return "USSR" if side == tscore.Side.USSR else "US"


def _mode_value(mode: object) -> int:
    return int(mode)


def _mode_str(mode: object) -> str:
    return {
        _MODE_INFLUENCE: "Place Influence",
        _MODE_COUP: "Coup",
        _MODE_REALIGN: "Realignment",
        _MODE_SPACE: "Space Race",
        _MODE_EVENT: "Event",
    }.get(_mode_value(mode), str(mode))


def _score_str(vp: int) -> str:
    if vp > 0:
        return f"USSR {vp}"
    if vp < 0:
        return f"US {-vp}"
    return "Tied 0"


def _copy_state_dict(state: dict) -> dict:
    return {
        "turn": state["turn"],
        "ar": state["ar"],
        "phasing": state["phasing"],
        "vp": state["vp"],
        "defcon": state["defcon"],
        "milops": tuple(state["milops"]),
        "space": tuple(state["space"]),
        "china_held_by": state["china_held_by"],
        "ussr_influence": list(state["ussr_influence"]),
        "us_influence": list(state["us_influence"]),
        "discard": list(state["discard"]),
        "removed": list(state["removed"]),
    }


def _influence_diff_lines(
    pre: dict,
    post: dict,
    countries: dict,
) -> list[str]:
    """Return raw-log-style lines for every influence change."""
    lines: list[str] = []
    for cid in range(_COUNTRY_COUNT):
        pre_ussr = pre["ussr_influence"][cid]
        post_ussr = post["ussr_influence"][cid]
        pre_us = pre["us_influence"][cid]
        post_us = post["us_influence"][cid]
        d_ussr = post_ussr - pre_ussr
        d_us = post_us - pre_us
        cname = _country_name(cid, countries)
        if d_ussr != 0:
            sign = "+" if d_ussr > 0 else ""
            lines.append(f"    USSR {sign}{d_ussr} in {cname} [{post_us}][{post_ussr}]")
        if d_us != 0:
            sign = "+" if d_us > 0 else ""
            lines.append(f"    US   {sign}{d_us} in {cname} [{post_us}][{post_ussr}]")
    return lines


def _make_terminal_post_snapshot(step, result) -> dict:
    post = _copy_state_dict(step.pub_snapshot)
    post["vp"] = step.vp_after
    post["defcon"] = step.defcon_after
    if result is not None:
        post["vp"] = result.final_vp
    return post


def _post_snapshot_for_step(steps: list, idx: int, result) -> dict:
    if idx + 1 < len(steps):
        return _copy_state_dict(steps[idx + 1].pub_snapshot)
    return _make_terminal_post_snapshot(steps[idx], result)


def _rich_detail(
    steps: list,
    idx: int,
    cards: dict,
    countries: dict,
    result,
) -> list[str]:
    """Generate raw-log-style sub-detail lines for a step."""
    step = steps[idx]
    pre = step.pub_snapshot
    post = _post_snapshot_for_step(steps, idx, result)
    action = step.action
    side = step.side
    opp = tscore.Side.US if side == tscore.Side.USSR else tscore.Side.USSR
    lines: list[str] = []

    mode = _mode_value(action.mode)

    card_spec = cards.get(action.card_id)
    ops = card_spec.ops if card_spec else 1

    if mode == _MODE_INFLUENCE:
        lines.append(f"  Place Influence ({ops} Ops):")
        lines.extend(_influence_diff_lines(pre, post, countries))

    elif mode == _MODE_COUP:
        target_cid = action.targets[0] if action.targets else None
        cspec = countries.get(target_cid) if target_cid is not None else None
        stab = cspec.stability if cspec else 1
        cname = _country_name(target_cid, countries) if target_cid is not None else "?"

        lines.append(f"  Coup ({ops} Ops):")
        lines.append(f"    Target: {cname}")

        if target_cid is not None:
            side_idx = 0 if side == tscore.Side.USSR else 1
            opp_idx = 1 - side_idx
            pre_opp = pre["ussr_influence"][target_cid] if opp_idx == 0 else pre["us_influence"][target_cid]
            post_opp = post["ussr_influence"][target_cid] if opp_idx == 0 else post["us_influence"][target_cid]
            pre_own = pre["ussr_influence"][target_cid] if side_idx == 0 else pre["us_influence"][target_cid]
            post_own = post["ussr_influence"][target_cid] if side_idx == 0 else post["us_influence"][target_cid]
            opp_removed = pre_opp - post_opp
            own_gained = post_own - pre_own
            net = opp_removed + own_gained

            if net > 0:
                implied_roll = net - ops + 2 * stab
                lines.append(
                    f"    SUCCESS: ~{implied_roll} "
                    f"[ +{ops} ops - 2x{stab} stab = {net} net ]"
                )
            else:
                lines.append(f"    FAILURE: [ +{ops} ops - 2x{stab} stab <= 0 ]")

        lines.extend(_influence_diff_lines(pre, post, countries))

        side_idx = 0 if side == tscore.Side.USSR else 1
        d_milops = post["milops"][side_idx] - pre["milops"][side_idx]
        if d_milops != 0:
            lines.append(f"    {_side_str(side)} Military Ops to {post['milops'][side_idx]}")

        if post["defcon"] < pre["defcon"]:
            lines.append(f"    DEFCON degrades to {post['defcon']}")

    elif mode == _MODE_REALIGN:
        lines.append(f"  Realignment ({ops} Ops):")
        lines.extend(_influence_diff_lines(pre, post, countries))
        if post["defcon"] < pre["defcon"]:
            lines.append(f"    DEFCON degrades to {post['defcon']}")

    elif mode == _MODE_SPACE:
        lines.append(f"  Space Race ({ops} Ops):")
        side_idx = 0 if side == tscore.Side.USSR else 1
        pre_level = pre["space"][side_idx]
        post_level = post["space"][side_idx]
        if post_level > pre_level:
            lines.append(f"    Success! {_side_str(side)} advances to level {post_level}.")
        else:
            lines.append("    Failed.")

    elif mode == _MODE_EVENT:
        lines.append(f"  Event: {_card_name(action.card_id, cards)}")
        lines.extend(_influence_diff_lines(pre, post, countries))
        if post["defcon"] < pre["defcon"]:
            lines.append(f"    DEFCON degrades to {post['defcon']}")
        elif post["defcon"] > pre["defcon"]:
            lines.append(f"    DEFCON improves to {post['defcon']}")

    if mode != _MODE_COUP:
        for trace_side in (tscore.Side.USSR, tscore.Side.US):
            side_idx = 0 if trace_side == tscore.Side.USSR else 1
            d = post["milops"][side_idx] - pre["milops"][side_idx]
            if d != 0:
                lines.append(f"    {_side_str(trace_side)} Military Ops to {post['milops'][side_idx]}")

    d_vp = post["vp"] - pre["vp"]
    if d_vp != 0:
        if d_vp > 0:
            lines.append(f"    USSR gains {d_vp} VP. Score is {_score_str(post['vp'])}.")
        else:
            lines.append(f"    US gains {-d_vp} VP. Score is {_score_str(post['vp'])}.")

    if mode == _MODE_EVENT:
        for trace_side in (tscore.Side.USSR, tscore.Side.US):
            side_idx = 0 if trace_side == tscore.Side.USSR else 1
            if post["space"][side_idx] > pre["space"][side_idx]:
                lines.append(
                    f"    {_side_str(trace_side)} advances to {post['space'][side_idx]} in the Space Race."
                )

    return lines


# ---------------------------------------------------------------------------
# Model policy
# ---------------------------------------------------------------------------

def _card_mask(card_ids: list[int]) -> list[float]:
    mask = [0.0] * _CARD_MASK_SLOTS
    for cid in card_ids:
        if 0 < cid < _CARD_MASK_SLOTS:
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
    # Slot 2: opponent support mask — cards not known to be in own hand, discard, or removed
    _excluded = set(hand) | set(state["discard"]) | set(state["removed"])
    opponent_support_mask = [
        0.0 if cid in _excluded else 1.0 for cid in range(_CARD_MASK_SLOTS)
    ]
    cards = hand_mask + opponent_support_mask + discard_mask + removed_mask

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


def _load_model(model_path: Path):
    """Load a TorchScript model or a regular PyTorch checkpoint."""
    try:
        model = torch.jit.load(str(model_path), map_location="cpu")
        model.eval()
        return model
    except RuntimeError:
        pass

    from tsrl.policies.model import (  # noqa: E402
        TSBaselineModel,
        TSCardEmbedModel,
        TSControlFeatGNNModel,
        TSControlFeatGNNSideModel,
        TSControlFeatModel,
        TSCountryAttnModel,
        TSCountryAttnSideModel,
        TSCountryEmbedModel,
        TSDirectCountryModel,
        TSFullEmbedModel,
        TSMarginalValueModel,
    )

    model_registry = {
        "baseline": TSBaselineModel,
        "card_embed": TSCardEmbedModel,
        "country_embed": TSCountryEmbedModel,
        "full_embed": TSFullEmbedModel,
        "country_attn": TSCountryAttnModel,
        "country_attn_side": TSCountryAttnSideModel,
        "direct_country": TSDirectCountryModel,
        "marginal_value": TSMarginalValueModel,
        "control_feat": TSControlFeatModel,
        "control_feat_gnn": TSControlFeatGNNModel,
        "control_feat_gnn_side": TSControlFeatGNNSideModel,
    }

    ckpt = torch.load(str(model_path), map_location="cpu", weights_only=False)
    args = ckpt.get("args", {})
    hidden_dim = args.get("hidden_dim", 256)
    dropout = args.get("dropout", 0.1)
    model_type = args.get("model_type", "baseline")
    cls = model_registry.get(model_type, TSBaselineModel)
    model = cls(hidden_dim=hidden_dim, dropout=dropout)
    state = ckpt.get("model_state_dict") or ckpt
    model.load_state_dict(state, strict=False)
    model.eval()
    return model


def _infer_expected_scalar_dim(model) -> int:
    state = model.state_dict()
    scalar_weight = state.get("scalar_encoder.weight")
    if scalar_weight is None:
        return 11
    input_dim = int(scalar_weight.shape[1])
    has_region_encoder = any(key.startswith("region_encoder.") for key in state)
    region_dim = 42 if has_region_encoder else 0
    scalar_dim = input_dim - region_dim
    return scalar_dim if scalar_dim > 0 else 11


def _adapt_scalars(scalars: torch.Tensor, expected_dim: int) -> torch.Tensor:
    current_dim = int(scalars.shape[1])
    if current_dim == expected_dim:
        return scalars
    if current_dim > expected_dim:
        return scalars[:, :expected_dim]
    pad = torch.zeros((scalars.shape[0], expected_dim - current_dim), dtype=scalars.dtype)
    return torch.cat([scalars, pad], dim=1)


def _candidate_country_ids(country_scores: torch.Tensor | None) -> list[int]:
    if country_scores is None:
        return list(range(_COUNTRY_COUNT))
    n = int(country_scores.numel())
    if n == _COUNTRY_COUNT:
        return list(range(_COUNTRY_COUNT))
    if n == 84:
        return list(range(1, 85))
    return list(range(min(n, _COUNTRY_COUNT)))


def _country_score(country_scores: torch.Tensor | None, country_id: int) -> float:
    if country_scores is None:
        return 0.0
    n = int(country_scores.numel())
    if n == _COUNTRY_COUNT and 0 <= country_id < _COUNTRY_COUNT:
        return float(country_scores[country_id].item())
    if n == 84 and 1 <= country_id <= 84:
        return float(country_scores[country_id - 1].item())
    if 0 <= country_id < n:
        return float(country_scores[country_id].item())
    return float("-inf")


def _allocate_influence_targets(country_scores: torch.Tensor | None, ops: int) -> list[int]:
    if ops <= 0:
        return []

    country_ids = _candidate_country_ids(country_scores)
    if not country_ids:
        return []

    weights: list[tuple[int, float]] = []
    for cid in country_ids:
        score = _country_score(country_scores, cid)
        if not math.isfinite(score):
            continue
        weights.append((cid, max(score, 0.0)))

    if not weights:
        return []

    total = sum(weight for _, weight in weights)
    if total <= 0.0:
        weights = [(cid, 1.0) for cid, _ in weights]
        total = float(len(weights))

    base_alloc: dict[int, int] = {}
    remainders: list[tuple[float, int]] = []
    allocated = 0
    for cid, weight in weights:
        raw = ops * weight / total
        count = int(math.floor(raw))
        base_alloc[cid] = count
        allocated += count
        remainders.append((raw - count, cid))

    for _, cid in sorted(remainders, key=lambda item: (-item[0], item[1]))[: max(0, ops - allocated)]:
        base_alloc[cid] = base_alloc.get(cid, 0) + 1

    targets: list[int] = []
    for cid, count in sorted(base_alloc.items()):
        targets.extend([cid] * count)
    return targets


def _make_model_callback(model_path: Path, temperature: float = 0.0, seed: int = 0):
    model = _load_model(model_path)
    cards = load_cards()
    expected_scalar_dim = _infer_expected_scalar_dim(model)
    rng = torch.Generator()
    rng.manual_seed(seed ^ 0xDEADBEEF)

    def _callback(state_dict, hand_list, holds_china: bool, side_int: int):
        if not hand_list:
            return None

        influence, cards_tensor, scalars = extract_features(state_dict, hand_list, holds_china, side_int)
        scalars = _adapt_scalars(scalars, expected_scalar_dim)
        with torch.no_grad():
            outputs = model(influence, cards_tensor, scalars)

        card_logits = outputs["card_logits"][0].cpu()
        mode_logits = outputs["mode_logits"][0].cpu()
        country_logits = outputs.get("country_logits")
        if country_logits is not None:
            country_logits = country_logits[0].cpu()

        legal_hand = sorted(cid for cid in hand_list if 1 <= cid <= 111)
        if not legal_hand:
            return None

        if temperature > 0.0:
            # Sampled card selection
            legal_logits = torch.tensor([float(card_logits[cid - 1].item()) for cid in legal_hand])
            probs = torch.softmax(legal_logits / temperature, dim=0)
            idx = int(torch.multinomial(probs, 1, generator=rng).item())
            best_card_id = legal_hand[idx]
            # Sampled mode
            mode_probs = torch.softmax(mode_logits / temperature, dim=0)
            best_mode = int(torch.multinomial(mode_probs, 1, generator=rng).item())
        else:
            best_card_id = max(legal_hand, key=lambda cid: (float(card_logits[cid - 1].item()), -cid))
            best_mode = int(mode_logits.argmax().item())

        if best_mode == _MODE_INFLUENCE:
            card_spec = cards.get(best_card_id)
            ops = card_spec.ops if card_spec else 1
            targets = _allocate_influence_targets(country_logits, ops)
        elif best_mode in (_MODE_COUP, _MODE_REALIGN):
            country_ids = _candidate_country_ids(country_logits)
            best_target = max(
                country_ids,
                key=lambda cid: (_country_score(country_logits, cid), -cid),
                default=None,
            )
            targets = [] if best_target is None else [best_target]
        else:
            targets = []

        return {
            "card_id": int(best_card_id),
            "mode": int(best_mode),
            "targets": [int(cid) for cid in targets],
        }

    return _callback


# ---------------------------------------------------------------------------
# Trace collection
# ---------------------------------------------------------------------------

def collect_traced_game(model_path: Path, seed: int, heuristic: bool, temperature: float = 0.0):
    if heuristic:
        traced_game = tscore.play_traced_game(
            tscore.PolicyKind.MinimalHybrid,
            tscore.PolicyKind.MinimalHybrid,
            seed=seed,
        )
        return traced_game.steps, traced_game.result, "Using MinimalHybrid heuristics for both sides."

    if model_path.exists():
        callback = _make_model_callback(model_path, temperature=temperature, seed=seed)
        traced_game = tscore.play_traced_game_with_callback(callback, seed=seed)
        mode_str = "greedy" if temperature == 0.0 else f"T={temperature}"
        return traced_game.steps, traced_game.result, f"Using scripted model: {model_path} ({mode_str})"

    traced_game = tscore.play_traced_game(
        tscore.PolicyKind.MinimalHybrid,
        tscore.PolicyKind.MinimalHybrid,
        seed=seed,
    )
    return (
        traced_game.steps,
        traced_game.result,
        f"Model not found at {model_path}; falling back to MinimalHybrid for this run.",
    )


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def _sorted_hand(hand: list[int] | tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sorted(int(cid) for cid in hand))


def _estimate_display_hands(steps: list) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    display_hands: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
    known = {
        tscore.Side.USSR: set(),
        tscore.Side.US: set(),
    }
    seen = {
        tscore.Side.USSR: False,
        tscore.Side.US: False,
    }

    for idx, step in enumerate(steps):
        side = step.side
        opp = tscore.Side.US if side == tscore.Side.USSR else tscore.Side.USSR
        actor_hand = _sorted_hand(step.hand_snapshot)
        known[side] = set(actor_hand)
        seen[side] = True

        opp_hand: tuple[int, ...]
        if seen[opp]:
            opp_hand = tuple(sorted(known[opp]))
        elif step.ar == 0 and idx + 1 < len(steps):
            next_step = steps[idx + 1]
            if next_step.turn == step.turn and next_step.ar == step.ar and next_step.side == opp:
                opp_hand = _sorted_hand(next_step.hand_snapshot)
            else:
                opp_hand = ()
        else:
            opp_hand = ()

        if side == tscore.Side.USSR:
            display_hands.append((actor_hand, opp_hand))
        else:
            display_hands.append((opp_hand, actor_hand))

        if step.action.card_id in known[side]:
            known[side].remove(step.action.card_id)

    return display_hands


def _format_hand(hand: tuple[int, ...], cards: dict) -> str:
    if not hand:
        return "(empty)"
    named = sorted((_card_name(cid, cards) for cid in hand), key=str.casefold)
    return ", ".join(named)


def _format_target_summary(action, countries: dict) -> str:
    if not action.targets:
        return ""

    counts: dict[int, int] = {}
    for cid in action.targets:
        counts[cid] = counts.get(cid, 0) + 1

    ordered = sorted(counts.items(), key=lambda item: (_country_name(item[0], countries), item[0]))
    parts = []
    for cid, count in ordered:
        suffix = f"(+{count})" if _mode_value(action.mode) == _MODE_INFLUENCE else ""
        parts.append(f"{_country_name(cid, countries)}{suffix}")
    return " -> " + ", ".join(parts)


def print_game_log(
    steps: list,
    result,
    cards: dict,
    countries: dict,
) -> None:
    display_hands = _estimate_display_hands(steps)

    for idx, step in enumerate(steps):
        pub = step.pub_snapshot
        action = step.action
        ussr_hand, us_hand = display_hands[idx]
        target_summary = _format_target_summary(action, countries)

        print(
            f"=== Turn {pub['turn']} AR {pub['ar']} | {_side_str(step.side)} | "
            f"DEFCON {pub['defcon']} | VP: {pub['vp']:+d} ==="
        )
        print(f"USSR hand: {_format_hand(ussr_hand, cards)}")
        print(f"US hand: {_format_hand(us_hand, cards)}")
        print(
            f"Action: Play {_card_name(action.card_id, cards)} as {_mode_str(action.mode)}"
            f"{target_summary}"
        )
        for line in _rich_detail(steps, idx, cards, countries, result):
            print(line)
        print()

    print(f"{'=' * 72}")
    print("GAME OVER")
    if result.winner == tscore.Side.USSR:
        winner = "USSR"
    elif result.winner == tscore.Side.US:
        winner = "US"
    else:
        winner = "Draw"
    print(f"Winner: {winner}" if winner != "Draw" else "Winner: Draw / Mutual Destruction")
    print(f"Final VP: {result.final_vp:+d}")
    print(f"End Turn: {result.end_turn}")
    print(f"Reason: {result.end_reason}")
    print(f"Total decision points: {len(steps)}")
    print(f"{'=' * 72}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run one traced self-play game.")
    parser.add_argument(
        "--model",
        type=Path,
        default=_DEFAULT_MODEL,
        help=f"Path to scripted model (default: {_DEFAULT_MODEL})",
    )
    parser.add_argument("--seed", type=int, default=42, help="RNG seed (default: 42)")
    parser.add_argument(
        "--heuristic",
        action="store_true",
        help="Use MinimalHybrid heuristics for both sides instead of a model callback.",
    )
    parser.add_argument(
        "--temperature", type=float, default=0.0,
        help="Sampling temperature (0=greedy, 1.0=full sampling; default: 0=greedy)",
    )
    args = parser.parse_args()

    steps, result, policy_note = collect_traced_game(args.model, args.seed, args.heuristic, args.temperature)
    print(f"[run_traced_game] {policy_note}", file=sys.stderr)

    cards = load_cards()
    countries = load_countries()
    print_game_log(steps, result, cards, countries)


if __name__ == "__main__":
    main()
