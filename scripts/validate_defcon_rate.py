"""Fast parallel DEFCON-1 rate validator for minimal_hybrid heuristic.

Usage:
    uv run python scripts/validate_defcon_rate.py [--n-games 400] [--workers 8] [--seed 0]
"""
from __future__ import annotations

import argparse
import multiprocessing as mp
import random
import sys
from collections import Counter


def _run_game_worker(args: tuple[int, int]) -> tuple[str, int]:
    """Run a single game and return (end_reason, end_turn). Runs in subprocess."""
    seed, game_idx = args
    # Import inside worker to avoid forked-process issues with torch
    from tsrl.policies.minimal_hybrid import choose_minimal_hybrid, MinimalHybridParams
    from tsrl.engine.game_loop import run_game_cb

    params = MinimalHybridParams()
    try:
        result = run_game_cb(
            ussr_policy=lambda pub, hand, holds_china: choose_minimal_hybrid(
                pub, hand, holds_china, params
            ),
            us_policy=lambda pub, hand, holds_china: choose_minimal_hybrid(
                pub, hand, holds_china, params
            ),
            seed=seed,
        )
        return result.end_reason, result.end_turn
    except Exception as e:
        return f"error:{e}", 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate heuristic DEFCON-1 rate.")
    parser.add_argument("--n-games", type=int, default=400)
    parser.add_argument("--workers", type=int, default=min(8, mp.cpu_count()))
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    seeds = [(args.seed + i, i) for i in range(args.n_games)]

    print(
        f"Running {args.n_games} games with {args.workers} workers (seed base={args.seed})..."
    )

    with mp.Pool(processes=args.workers) as pool:
        results = pool.map(_run_game_worker, seeds)

    end_reasons = Counter(r[0] for r in results)
    end_turns = [r[1] for r in results if r[0] != "error"]

    total = len(results)
    defcon1 = end_reasons.get("defcon1", 0)
    errors = sum(1 for r in results if r[0].startswith("error"))

    print(f"\nResults ({total} games):")
    print(f"  DEFCON-1 rate:   {defcon1}/{total} = {defcon1/total:.1%}")
    if end_turns:
        print(f"  Mean end_turn:   {sum(end_turns)/len(end_turns):.1f}")
        t8plus = sum(1 for t in end_turns if t >= 8)
        print(f"  Turn 8+ games:   {t8plus}/{len(end_turns)} = {t8plus/len(end_turns):.1%}")
    print(f"\nEnd reason breakdown:")
    for reason, count in sorted(end_reasons.items(), key=lambda x: -x[1]):
        print(f"  {reason:20s}: {count:4d} ({count/total:.1%})")
    if errors:
        print(f"\n  WARNING: {errors} games errored")


if __name__ == "__main__":
    main()
