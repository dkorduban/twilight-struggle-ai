#!/usr/bin/env python3
"""Diagnose DEFCON-1 failures: identify which cards/modes cause nuclear war."""

from __future__ import annotations

import argparse
import multiprocessing as mp
import random
import sys
from collections import Counter, defaultdict

sys.path.insert(0, "python")


def _run_game(seed: int) -> list[tuple[int, str, int]]:
    from tsrl.engine.game_loop import _MAX_TURNS, _run_game_gen
    from tsrl.engine.game_state import reset
    from tsrl.engine.legal_actions import sample_action
    from tsrl.policies.minimal_hybrid import choose_minimal_hybrid

    rng = random.Random(seed)
    gs = reset(seed=rng.randint(0, 2**32))
    gen = _run_game_gen(gs, rng, _MAX_TURNS)
    failures: list[tuple[int, str, int]] = []
    last_action = None
    prev_defcon = gs.pub.defcon

    try:
        req = next(gen)
        while True:
            action = choose_minimal_hybrid(req.pub, req.hand, req.holds_china)
            if action is None:
                action = sample_action(
                    req.hand,
                    req.pub,
                    req.pub.phasing,
                    holds_china=req.holds_china,
                    rng=rng,
                )
            last_action = action
            req = gen.send(action)
            if prev_defcon > 1 and req.pub.defcon <= 1:
                failures.append((action.card_id, action.mode.name, req.pub.turn))
            prev_defcon = req.pub.defcon
    except StopIteration:
        if last_action is not None and prev_defcon > 1 and gs.pub.defcon <= 1:
            failures.append((last_action.card_id, last_action.mode.name, gs.pub.turn))
    finally:
        gen.close()

    return failures


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-games", type=int, default=500)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--workers", type=int, default=min(8, mp.cpu_count()))
    args = parser.parse_args()

    failures: dict[tuple[int, str], Counter[int]] = defaultdict(Counter)
    seeds = [args.seed + i for i in range(args.n_games)]

    with mp.get_context("spawn").Pool(processes=args.workers) as pool:
        for game_failures in pool.map(_run_game, seeds):
            for card_id, mode_name, turn in game_failures:
                failures[(card_id, mode_name)][turn] += 1

    print(f"\nTop 5 DEFCON-1 failure modes (out of {args.n_games} games):")
    ranked = sorted(
        failures.items(),
        key=lambda item: (-sum(item[1].values()), item[0][0], item[0][1]),
    )[:5]
    for (card_id, mode_name), turn_counts in ranked:
        total = sum(turn_counts.values())
        turns = ", ".join(
            f"T{turn}:{count}"
            for turn, count in sorted(turn_counts.items(), key=lambda item: (-item[1], item[0]))
        )
        print(
            f"  Card {card_id:3d}, mode={mode_name:8s} : {total:3d} failures | turns {turns}"
        )


if __name__ == "__main__":
    main()
