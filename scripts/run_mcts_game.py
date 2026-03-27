"""
Run one MCTS self-play game and print a human-readable log.

Usage:
    uv run python scripts/run_mcts_game.py [--n-sim N] [--seed S] [--flat] [--verbose]

Options:
    --n-sim N    MCTS simulations per move (default: 20)
    --seed S     RNG seed (default: 42)
    --flat       Use flat Monte Carlo instead of UCT
    --verbose    Show event sub-effects, influence changes, dice outcomes
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Optional

# Ensure package is importable when run from repo root.
sys.path.insert(0, str(Path(__file__).parents[1] / "python"))

from tsrl.engine.mcts import collect_self_play_game, SelfPlayStep
from tsrl.engine.game_loop import GameResult
from tsrl.etl.game_data import load_cards, load_countries
from tsrl.schemas import ActionMode, PublicState, Side


# ---------------------------------------------------------------------------
# Formatting helpers
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


# ---------------------------------------------------------------------------
# Rich detail: compute what changed between pre and post pub
# ---------------------------------------------------------------------------

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
        pre_us   = _inf(pre, Side.US,   cid)
        post_us  = _inf(post, Side.US,   cid)
        d_ussr = post_ussr - pre_ussr
        d_us   = post_us   - pre_us
        cname = _country_name(cid, countries)
        if d_ussr != 0:
            sign = "+" if d_ussr > 0 else ""
            lines.append(f"    USSR {sign}{d_ussr} in {cname} [{post_us}][{post_ussr}]")
        if d_us != 0:
            sign = "+" if d_us > 0 else ""
            lines.append(f"    US   {sign}{d_us} in {cname} [{post_us}][{post_ussr}]")
    return lines


def _rich_detail(
    step: SelfPlayStep,
    cards: dict,
    countries: dict,
) -> list[str]:
    """Generate raw-log-style sub-detail lines for a step."""
    if step.post_pub is None:
        return []

    pre  = step.pub_snapshot
    post = step.post_pub
    action = step.action
    side = step.side
    opp  = Side.US if side == Side.USSR else Side.USSR
    lines: list[str] = []

    mode = action.mode

    # ---- Ops value header ----
    card_spec = cards.get(action.card_id)
    ops = card_spec.ops if card_spec else 1

    if mode == ActionMode.INFLUENCE:
        lines.append(f"  Place Influence ({ops} Ops):")
        lines.extend(_influence_diff_lines(pre, post, countries))

    elif mode == ActionMode.COUP:
        target_cid = action.targets[0] if action.targets else None
        cspec = countries.get(target_cid) if target_cid is not None else None
        stab = cspec.stability if cspec else 1
        is_bg = cspec.is_battleground if cspec else False
        cname = _country_name(target_cid, countries) if target_cid is not None else "?"

        lines.append(f"  Coup ({ops} Ops):")
        lines.append(f"    Target: {cname}")

        if target_cid is not None:
            pre_opp  = _inf(pre,  opp,  target_cid)
            post_opp = _inf(post, opp,  target_cid)
            pre_own  = _inf(pre,  side, target_cid)
            post_own = _inf(post, side, target_cid)
            opp_removed = pre_opp - post_opp
            own_gained  = post_own - pre_own
            net = opp_removed + own_gained

            if net > 0:
                # net = roll + ops - 2*stab  →  roll = net - ops + 2*stab
                implied_roll = net - ops + 2 * stab
                lines.append(
                    f"    SUCCESS: ~{implied_roll} "
                    f"[ +{ops} ops - 2x{stab} stab = {net} net ]"
                )
            else:
                lines.append(f"    FAILURE: [ +{ops} ops - 2x{stab} stab ≤ 0 ]")

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
        pre_level  = pre.space[int(side)]
        post_level = post.space[int(side)]
        if post_level > pre_level:
            lines.append(f"    Success! {_side_str(side)} advances to level {post_level}.")
        else:
            lines.append(f"    Failed.")

    elif mode == ActionMode.EVENT:
        lines.append(f"  Event: {_card_name(action.card_id, cards)}")
        inf_lines = _influence_diff_lines(pre, post, countries)
        lines.extend(inf_lines)
        if post.defcon < pre.defcon:
            lines.append(f"    DEFCON degrades to {post.defcon}")
        elif post.defcon > pre.defcon:
            lines.append(f"    DEFCON improves to {post.defcon}")

    # ---- Trailing VP / milops lines (all modes) ----
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

    # ---- Space advances (EVENT can trigger space, e.g. Captured Nazi Scientist) ----
    if mode == ActionMode.EVENT:
        for s in (Side.USSR, Side.US):
            if post.space[int(s)] > pre.space[int(s)]:
                lines.append(
                    f"    {_side_str(s)} advances to {post.space[int(s)]} in the Space Race."
                )

    return lines


# ---------------------------------------------------------------------------
# Log printers
# ---------------------------------------------------------------------------

def print_game_log(
    steps: list[SelfPlayStep],
    result: GameResult,
    cards: dict,
    countries: dict,
    *,
    verbose: bool = False,
) -> None:
    current_turn = 0
    current_ar = -1

    for step in steps:
        pub = step.pub_snapshot
        action = step.action

        # Turn header.
        if pub.turn != current_turn:
            current_turn = pub.turn
            current_ar = -1
            print(f"\n{'='*72}")
            print(f"  TURN {pub.turn:2d}   VP: {pub.vp:+4d}   DEFCON: {pub.defcon}"
                  f"   MilOps: USSR {pub.milops[0]} / US {pub.milops[1]}")
            print(f"{'='*72}")

        # AR header.
        if pub.ar != current_ar:
            current_ar = pub.ar
            label = "Headline Phase" if pub.ar == 0 else f"AR {pub.ar}"
            print(f"\nTurn {pub.turn}, {label}:")

        side_str  = _side_str(step.side)
        card_str  = _card_name(action.card_id, cards)
        mode_str  = _mode_str(action.mode)

        # Compact header line (always shown).
        if action.mode == ActionMode.EVENT:
            print(f"  {side_str} | {card_str}: {mode_str}")
        elif action.targets:
            target_strs = [_country_name(t, countries) for t in action.targets]
            print(f"  {side_str} | {card_str}: {mode_str} ({', '.join(target_strs)})")
        else:
            print(f"  {side_str} | {card_str}: {mode_str}")

        # Verbose sub-detail.
        if verbose:
            for line in _rich_detail(step, cards, countries):
                print(line)

    # Final banner.
    print(f"\n{'='*72}")
    print(f"  GAME OVER")
    if result.winner is not None:
        print(f"  Winner: {_side_str(result.winner)}")
    else:
        print(f"  Result: Draw / Mutual Destruction")
    print(f"  Final VP: {result.final_vp:+d}   End Turn: {result.end_turn}"
          f"   Reason: {result.end_reason}")
    print(f"  Total decision points: {len(steps)}")
    print(f"{'='*72}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Run one MCTS self-play game.")
    parser.add_argument("--n-sim",   type=int,  default=20,    help="MCTS sims per move (default: 20)")
    parser.add_argument("--seed",    type=int,  default=42,    help="RNG seed (default: 42)")
    parser.add_argument("--flat",    action="store_true",      help="Use flat Monte Carlo (default: UCT)")
    parser.add_argument("--verbose", action="store_true",      help="Show event effects, influence changes, dice outcomes")
    args = parser.parse_args()

    use_uct = not args.flat
    algo = "flat Monte Carlo" if args.flat else "UCT (c=1.41)"
    print(f"Running MCTS self-play game: {algo}, n_sim={args.n_sim}, seed={args.seed}"
          + (" [verbose]" if args.verbose else ""))
    print("(this may take a few seconds...)\n")

    steps, result = collect_self_play_game(
        n_sim=args.n_sim,
        use_uct=use_uct,
        seed=args.seed,
    )

    cards     = load_cards()
    countries = load_countries()

    print_game_log(steps, result, cards, countries, verbose=args.verbose)


if __name__ == "__main__":
    main()
