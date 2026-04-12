#!/usr/bin/env python3
"""Run one traced self-play game and print a human-readable action log.

Usage:
    PYTHONPATH=build-ninja/bindings uv run python scripts/run_traced_game.py [--model PATH] [--seed N]
"""
from __future__ import annotations

import argparse
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import torch

# Ensure package is importable when run from repo root.
sys.path.insert(0, str(Path(__file__).parents[1] / "python"))

from tsrl.engine.game_loop import (  # noqa: E402
    _MAX_TURNS,
    _ars_for_turn,
    _end_of_turn,
    _run_action_rounds,
    _run_extra_ar,
    _run_headline_phase,
    GameResult,
    Policy,
)
from tsrl.engine.game_state import advance_to_late_war, advance_to_mid_war, deal_cards, reset  # noqa: E402
from tsrl.engine.legal_actions import enumerate_actions  # noqa: E402
from tsrl.engine.rng import make_rng  # noqa: E402
from tsrl.engine.step import _copy_pub  # noqa: E402
from tsrl.etl.game_data import load_cards, load_countries  # noqa: E402
from tsrl.policies.minimal_hybrid import make_minimal_hybrid_policy  # noqa: E402
from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Side  # noqa: E402

_DEFAULT_MODEL = Path("data/checkpoints/scripted_for_elo/v55_scripted.pt")
_EARLY_SCALAR_DIM = 11
_COUNTRY_COUNT = 86
_CARD_MASK_SLOTS = 112


@dataclass
class TracedStep:
    turn: int
    ar: int
    side: Side
    holds_china: bool
    pub_snapshot: PublicState
    post_pub: PublicState | None
    action: ActionEncoding
    ussr_hand: tuple[int, ...]
    us_hand: tuple[int, ...]


# ---------------------------------------------------------------------------
# Formatting helpers copied from scripts/run_mcts_game.py
# ---------------------------------------------------------------------------

def _card_name(card_id: int, cards: dict) -> str:
    spec = cards.get(card_id)
    return spec.name if spec else f"card#{card_id}"


def _country_name(cid: int, countries: dict) -> str:
    spec = countries.get(cid)
    return spec.name if spec else f"country#{cid}"


def _side_str(side: Side) -> str:
    return "USSR" if side == Side.USSR else "US"


def _mode_str(mode: ActionMode) -> str:
    return {
        ActionMode.INFLUENCE: "Place Influence",
        ActionMode.COUP:      "Coup",
        ActionMode.REALIGN:   "Realignment",
        ActionMode.SPACE:     "Space Race",
        ActionMode.EVENT:     "Event",
    }.get(mode, str(mode))


def _inf(pub: PublicState, side: Side, cid: int) -> int:
    return pub.influence.get((side, cid), 0)


def _score_str(vp: int) -> str:
    if vp > 0:
        return f"USSR {vp}"
    elif vp < 0:
        return f"US {-vp}"
    return "Tied 0"


def _influence_diff_lines(
    pre: PublicState,
    post: PublicState,
    countries: dict,
) -> list[str]:
    """Return raw-log-style lines for every influence change."""
    all_cids: set[int] = set()
    for (_, cid) in list(pre.influence.keys()) + list(post.influence.keys()):
        all_cids.add(cid)

    lines = []
    for cid in sorted(all_cids):
        pre_ussr = _inf(pre, Side.USSR, cid)
        post_ussr = _inf(post, Side.USSR, cid)
        pre_us = _inf(pre, Side.US, cid)
        post_us = _inf(post, Side.US, cid)
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


def _rich_detail(
    step: TracedStep,
    cards: dict,
    countries: dict,
) -> list[str]:
    """Generate raw-log-style sub-detail lines for a step."""
    if step.post_pub is None:
        return []

    pre = step.pub_snapshot
    post = step.post_pub
    action = step.action
    side = step.side
    opp = Side.US if side == Side.USSR else Side.USSR
    lines: list[str] = []

    mode = action.mode

    card_spec = cards.get(action.card_id)
    ops = card_spec.ops if card_spec else 1

    if mode == ActionMode.INFLUENCE:
        lines.append(f"  Place Influence ({ops} Ops):")
        lines.extend(_influence_diff_lines(pre, post, countries))

    elif mode == ActionMode.COUP:
        target_cid = action.targets[0] if action.targets else None
        cspec = countries.get(target_cid) if target_cid is not None else None
        stab = cspec.stability if cspec else 1
        cname = _country_name(target_cid, countries) if target_cid is not None else "?"

        lines.append(f"  Coup ({ops} Ops):")
        lines.append(f"    Target: {cname}")

        if target_cid is not None:
            pre_opp = _inf(pre, opp, target_cid)
            post_opp = _inf(post, opp, target_cid)
            pre_own = _inf(pre, side, target_cid)
            post_own = _inf(post, side, target_cid)
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

        d_milops = post.milops[int(side)] - pre.milops[int(side)]
        if d_milops != 0:
            lines.append(f"    {_side_str(side)} Military Ops to {post.milops[int(side)]}")

        if post.defcon < pre.defcon:
            lines.append(f"    DEFCON degrades to {post.defcon}")

    elif mode == ActionMode.REALIGN:
        lines.append(f"  Realignment ({ops} Ops):")
        lines.extend(_influence_diff_lines(pre, post, countries))
        if post.defcon < pre.defcon:
            lines.append(f"    DEFCON degrades to {post.defcon}")

    elif mode == ActionMode.SPACE:
        lines.append(f"  Space Race ({ops} Ops):")
        pre_level = pre.space[int(side)]
        post_level = post.space[int(side)]
        if post_level > pre_level:
            lines.append(f"    Success! {_side_str(side)} advances to level {post_level}.")
        else:
            lines.append("    Failed.")

    elif mode == ActionMode.EVENT:
        lines.append(f"  Event: {_card_name(action.card_id, cards)}")
        lines.extend(_influence_diff_lines(pre, post, countries))
        if post.defcon < pre.defcon:
            lines.append(f"    DEFCON degrades to {post.defcon}")
        elif post.defcon > pre.defcon:
            lines.append(f"    DEFCON improves to {post.defcon}")

    if mode != ActionMode.COUP:
        for s in (Side.USSR, Side.US):
            d = post.milops[int(s)] - pre.milops[int(s)]
            if d != 0:
                lines.append(f"    {_side_str(s)} Military Ops to {post.milops[int(s)]}")

    d_vp = post.vp - pre.vp
    if d_vp != 0:
        if d_vp > 0:
            lines.append(f"    USSR gains {d_vp} VP. Score is {_score_str(post.vp)}.")
        else:
            lines.append(f"    US gains {-d_vp} VP. Score is {_score_str(post.vp)}.")

    if mode == ActionMode.EVENT:
        for s in (Side.USSR, Side.US):
            if post.space[int(s)] > pre.space[int(s)]:
                lines.append(
                    f"    {_side_str(s)} advances to {post.space[int(s)]} in the Space Race."
                )

    return lines


# ---------------------------------------------------------------------------
# Model policy
# ---------------------------------------------------------------------------

def _card_mask(card_ids: list[int] | tuple[int, ...] | frozenset[int]) -> list[float]:
    mask = [0.0] * _CARD_MASK_SLOTS
    for cid in card_ids:
        if 0 < cid < _CARD_MASK_SLOTS:
            mask[cid] = 1.0
    return mask


def _public_state_to_state_dict(pub: PublicState) -> dict:
    return {
        "turn": pub.turn,
        "ar": pub.ar,
        "vp": pub.vp,
        "defcon": pub.defcon,
        "milops": list(pub.milops),
        "space": list(pub.space),
        "china_held_by": int(pub.china_held_by),
        "ussr_influence": [_inf(pub, Side.USSR, cid) for cid in range(_COUNTRY_COUNT)],
        "us_influence": [_inf(pub, Side.US, cid) for cid in range(_COUNTRY_COUNT)],
        "discard": list(pub.discard),
        "removed": list(pub.removed),
    }


def _extract_features(
    pub: PublicState,
    hand: frozenset[int],
    holds_china: bool,
    side: Side,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    state = _public_state_to_state_dict(pub)
    influence = [float(x) for x in state["ussr_influence"]] + [float(x) for x in state["us_influence"]]

    hand_mask = _card_mask(sorted(hand))
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
        float(int(side)),
    ]

    return (
        torch.tensor([influence], dtype=torch.float32),
        torch.tensor([cards], dtype=torch.float32),
        torch.tensor([scalars], dtype=torch.float32),
    )


def _country_term_is_probabilities(country_scores: torch.Tensor) -> bool:
    if country_scores.numel() == 0:
        return False
    min_v = float(country_scores.min().item())
    max_v = float(country_scores.max().item())
    total = float(country_scores.sum().item())
    return min_v >= 0.0 and max_v <= 1.0 + 1e-6 and abs(total - 1.0) <= 1e-3


def _country_score(country_scores: torch.Tensor | None, country_id: int) -> float:
    if country_scores is None:
        return 0.0
    n = int(country_scores.numel())
    if n == 86 and 0 <= country_id < 86:
        return float(country_scores[country_id].item())
    if n == 84 and 1 <= country_id <= 84:
        return float(country_scores[country_id - 1].item())
    return float("-inf")


def _action_score(
    action: ActionEncoding,
    card_logits: torch.Tensor,
    mode_logits: torch.Tensor,
    country_scores: torch.Tensor | None,
    country_is_probs: bool,
) -> float:
    score = float(card_logits[action.card_id - 1].item()) + float(mode_logits[int(action.mode)].item())
    if not action.targets or country_scores is None:
        return score

    for target in action.targets:
        target_score = _country_score(country_scores, target)
        if target_score == float("-inf"):
            return float("-inf")
        if country_is_probs:
            score += math.log(max(target_score, 1e-12))
        else:
            score += target_score
    return score


def _action_sort_key(action: ActionEncoding) -> tuple[int, int, tuple[int, ...]]:
    return (action.card_id, int(action.mode), tuple(action.targets))


def _make_model_policy(model_path: Path) -> Policy:
    model = torch.jit.load(str(model_path), map_location="cpu")
    model.eval()

    def _policy(pub: PublicState, hand: frozenset[int], holds_china: bool) -> ActionEncoding | None:
        legal_actions = enumerate_actions(hand, pub, pub.phasing, holds_china=holds_china)
        if not legal_actions:
            return None

        influence, cards, scalars = _extract_features(pub, hand, holds_china, pub.phasing)
        with torch.no_grad():
            outputs = model(influence, cards, scalars)

        card_logits = outputs["card_logits"][0].cpu()
        mode_logits = outputs["mode_logits"][0].cpu()
        country_scores = outputs.get("country_logits")
        if country_scores is not None:
            country_scores = country_scores[0].cpu()
        country_is_probs = country_scores is not None and _country_term_is_probabilities(country_scores)

        best_action: ActionEncoding | None = None
        best_score = float("-inf")
        for action in legal_actions:
            score = _action_score(action, card_logits, mode_logits, country_scores, country_is_probs)
            if best_action is None or score > best_score or (
                score == best_score and _action_sort_key(action) < _action_sort_key(best_action)
            ):
                best_action = action
                best_score = score
        return best_action

    return _policy


# ---------------------------------------------------------------------------
# Trace collection
# ---------------------------------------------------------------------------

def _sorted_hand(hand: frozenset[int]) -> tuple[int, ...]:
    return tuple(sorted(hand))


def collect_traced_game(model_path: Path, seed: int) -> tuple[list[TracedStep], GameResult, str]:
    if model_path.exists():
        policy = _make_model_policy(model_path)
        policy_note = f"Using scripted model: {model_path}"
    else:
        policy = make_minimal_hybrid_policy()
        policy_note = (
            f"Model not found at {model_path}; falling back to MinimalHybrid for this run."
        )

    rng = make_rng(seed)
    gs = reset(seed=int(rng.integers(0, 2**32)))
    steps: list[TracedStep] = []
    pending: list[TracedStep | None] = [None]

    def _flush_pending() -> None:
        if pending[0] is not None:
            pending[0].post_pub = _copy_pub(gs.pub)
            pending[0] = None

    def _trace_policy(pub: PublicState, hand: frozenset[int], holds_china: bool) -> ActionEncoding | None:
        _flush_pending()
        action = policy(pub, hand, holds_china)
        if action is None:
            return None
        step = TracedStep(
            turn=pub.turn,
            ar=pub.ar,
            side=pub.phasing,
            holds_china=holds_china,
            pub_snapshot=_copy_pub(pub),
            post_pub=None,
            action=action,
            ussr_hand=_sorted_hand(gs.hands[Side.USSR]),
            us_hand=_sorted_hand(gs.hands[Side.US]),
        )
        steps.append(step)
        pending[0] = step
        return action

    result: GameResult | None = None
    for turn in range(1, _MAX_TURNS + 1):
        gs.pub.turn = turn

        if turn == 4:
            advance_to_mid_war(gs, rng)
        elif turn == 8:
            advance_to_late_war(gs, rng)

        deal_cards(gs, Side.USSR, rng)
        deal_cards(gs, Side.US, rng)

        result = _run_headline_phase(gs, _trace_policy, _trace_policy, rng)
        _flush_pending()
        if result is not None:
            break

        result = _run_action_rounds(gs, _trace_policy, _trace_policy, rng, _ars_for_turn(turn))
        _flush_pending()
        if result is not None:
            break

        if gs.pub.north_sea_oil_extra_ar:
            gs.pub.north_sea_oil_extra_ar = False
            result = _run_extra_ar(gs, Side.US, _trace_policy, rng)
            _flush_pending()
            if result is not None:
                break

        if gs.pub.glasnost_extra_ar:
            gs.pub.glasnost_extra_ar = False
            result = _run_extra_ar(gs, Side.USSR, _trace_policy, rng)
            _flush_pending()
            if result is not None:
                break

        result = _end_of_turn(gs, rng, turn)
        if result is not None:
            break

    if result is None:
        winner = None
        if gs.pub.vp > 0:
            winner = Side.USSR
        elif gs.pub.vp < 0:
            winner = Side.US
        result = GameResult(
            winner=winner,
            final_vp=gs.pub.vp,
            end_turn=_MAX_TURNS,
            end_reason="turn_limit",
        )

    _flush_pending()
    return steps, result, policy_note


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def _format_hand(hand: tuple[int, ...], cards: dict) -> str:
    if not hand:
        return "(empty)"
    named = sorted((_card_name(cid, cards) for cid in hand), key=str.casefold)
    return ", ".join(named)


def _format_target_summary(action: ActionEncoding, countries: dict) -> str:
    if not action.targets:
        return ""

    counts: dict[int, int] = {}
    for cid in action.targets:
        counts[cid] = counts.get(cid, 0) + 1

    ordered = sorted(counts.items(), key=lambda item: (_country_name(item[0], countries), item[0]))
    parts = []
    for cid, count in ordered:
        suffix = f"(+{count})" if action.mode == ActionMode.INFLUENCE else ""
        parts.append(f"{_country_name(cid, countries)}{suffix}")
    return " -> " + ", ".join(parts)


def print_game_log(
    steps: list[TracedStep],
    result: GameResult,
    cards: dict,
    countries: dict,
) -> None:
    for step in steps:
        pub = step.pub_snapshot
        action = step.action
        target_summary = _format_target_summary(action, countries)

        print(
            f"=== Turn {pub.turn} AR {pub.ar} | {_side_str(step.side)} | "
            f"DEFCON {pub.defcon} | VP: {pub.vp:+d} ==="
        )
        print(f"USSR hand: {_format_hand(step.ussr_hand, cards)}")
        print(f"US hand: {_format_hand(step.us_hand, cards)}")
        print(
            f"Action: Play {_card_name(action.card_id, cards)} as {_mode_str(action.mode)}"
            f"{target_summary}"
        )
        for line in _rich_detail(step, cards, countries):
            print(line)
        print()

    print(f"{'=' * 72}")
    print("GAME OVER")
    if result.winner is None:
        print("Winner: Draw / Mutual Destruction")
    else:
        print(f"Winner: {_side_str(result.winner)}")
    print(f"Final VP: {result.final_vp:+d}")
    print(f"End Turn: {result.end_turn}")
    print(f"Reason: {result.end_reason}")
    print(f"Total decision points: {len(steps)}")
    print(f"{'=' * 72}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run one traced self-play game.")
    parser.add_argument("--model", type=Path, default=_DEFAULT_MODEL, help=f"Path to scripted model (default: {_DEFAULT_MODEL})")
    parser.add_argument("--seed", type=int, default=42, help="RNG seed (default: 42)")
    args = parser.parse_args()

    steps, result, policy_note = collect_traced_game(args.model, args.seed)
    if not args.model.exists():
        print(f"[run_traced_game] {policy_note}", file=sys.stderr)
    else:
        print(f"[run_traced_game] {policy_note}", file=sys.stderr)

    cards = load_cards()
    countries = load_countries()
    print_game_log(steps, result, cards, countries)


if __name__ == "__main__":
    main()
