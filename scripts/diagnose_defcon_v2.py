"""Attribute DEFCON-1 losses to the exact decision that caused 2 -> 1.

Usage:
    nice -n 10 uv run python scripts/diagnose_defcon_v2.py --n-games 400 --workers 6
"""
from __future__ import annotations

import argparse
import multiprocessing as mp
import random
from collections import Counter


def _format_action(action) -> str:
    mode_name = action.mode.name if hasattr(action.mode, "name") else str(action.mode)
    targets = ",".join(str(t) for t in action.targets) if action.targets else "-"
    return f"card={action.card_id} mode={mode_name} targets={targets}"


def _classify_trigger(action, pub_before) -> str:
    from tsrl.etl.game_data import load_cards, load_countries
    from tsrl.schemas import ActionMode

    cards = load_cards()
    countries = load_countries()
    card = cards.get(action.card_id)

    if action.mode == ActionMode.COUP and action.targets:
        country = countries.get(action.targets[0])
        if country is not None and country.is_battleground:
            return "ops_bg_coup"
        return "ops_nonbg_coup"

    if action.mode == ActionMode.EVENT:
        return "event"

    if card is not None and card.side not in (pub_before.phasing, type(pub_before.phasing).NEUTRAL):
        return "opponent_event_via_ops"

    return "other"


def _run_game(seed: int) -> dict:
    from tsrl.engine.game_loop import _run_game_gen
    from tsrl.engine.game_state import reset
    from tsrl.policies.minimal_hybrid import MinimalHybridParams, choose_minimal_hybrid

    rng = random.Random(seed)
    gs = reset(seed=rng.randint(0, 2**32))
    gen = _run_game_gen(gs, rng, 10)
    params = MinimalHybridParams()

    trigger = None

    try:
        req = next(gen)
        while True:
            action = choose_minimal_hybrid(req.pub, req.hand, req.holds_china, params=params)
            pre_defcon = gs.pub.defcon
            pre_turn = gs.pub.turn
            pre_ar = gs.pub.ar
            pre_side = req.side
            pre_phase = gs.phase.name if hasattr(gs.phase, "name") else str(gs.phase)
            pre_pub = gs.pub
            try:
                req = gen.send(action)
            except StopIteration as e:
                result = e.value
                if pre_defcon == 2 and gs.pub.defcon == 1 and action is not None:
                    trigger = {
                        "side": pre_side.name,
                        "turn": pre_turn,
                        "ar": pre_ar,
                        "phase": pre_phase,
                        "action": _format_action(action),
                        "kind": _classify_trigger(action, pre_pub),
                    }
                return {
                    "end_reason": result.end_reason,
                    "trigger": trigger,
                }

            if pre_defcon == 2 and gs.pub.defcon == 1 and action is not None:
                trigger = {
                    "side": pre_side.name,
                    "turn": pre_turn,
                    "ar": pre_ar,
                    "phase": pre_phase,
                    "action": _format_action(action),
                    "kind": _classify_trigger(action, pre_pub),
                }
    finally:
        gen.close()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-games", type=int, default=400)
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    seeds = list(range(args.seed, args.seed + args.n_games))
    print(f"Running {args.n_games} games on {args.workers} workers...")

    ctx = mp.get_context("spawn")
    with ctx.Pool(processes=args.workers) as pool:
        results = pool.map(_run_game, seeds)

    nuclear_wars = sum(1 for r in results if r["end_reason"] == "defcon1")
    trigger_counts: Counter[str] = Counter()
    kind_counts: Counter[str] = Counter()
    missing_triggers = 0

    for result in results:
        trigger = result["trigger"]
        if result["end_reason"] != "defcon1":
            continue
        if trigger is None:
            missing_triggers += 1
            continue
        trigger_counts[
            f'{trigger["side"]}: {trigger["action"]} turn={trigger["turn"]} ar={trigger["ar"]} phase={trigger["phase"]}'
        ] += 1
        kind_counts[trigger["kind"]] += 1

    print(f"\nNuclear wars: {nuclear_wars}/{args.n_games} = {nuclear_wars/args.n_games:.1%}")
    print("\nTrigger kinds:")
    for kind, count in kind_counts.most_common():
        print(f"  {count:3d}x  {kind}")
    if missing_triggers:
        print(f"  {missing_triggers:3d}x  missing_trigger")

    print("\nExact 2->1 triggers:")
    for trigger, count in trigger_counts.most_common(25):
        print(f"  {count:3d}x  {trigger}")


if __name__ == "__main__":
    main()
