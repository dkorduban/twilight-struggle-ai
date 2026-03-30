"""Fast multiprocessed DEFCON-1 rate validation for the minimal_hybrid heuristic.

Usage:
    uv run python scripts/validate_heuristic_defcon.py [--games 200] [--workers 8] [--seed 0]
"""
import argparse
import multiprocessing as mp
import random
from collections import Counter


def _run_game(seed: int) -> dict:
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
        return {
            "end_reason": result.end_reason,
            "end_turn": result.end_turn,
            "ok": True,
        }
    except Exception as e:
        return {"end_reason": "error", "end_turn": 0, "ok": False, "err": str(e)}


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate heuristic DEFCON-1 rate.")
    parser.add_argument("--games", type=int, default=200)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    seeds = list(range(args.seed, args.seed + args.games))

    ctx = mp.get_context("spawn")
    with ctx.Pool(processes=args.workers) as pool:
        results = pool.map(_run_game, seeds)

    ok = [r for r in results if r["ok"]]
    reasons = Counter(r["end_reason"] for r in ok)
    lengths = [r["end_turn"] for r in ok]

    defcon1 = reasons.get("defcon1", 0)
    total = len(ok)
    mean_len = sum(lengths) / max(1, len(lengths))
    turn8plus = sum(1 for t in lengths if t >= 8)

    print(f"Games:        {total}/{args.games} succeeded")
    print(f"DEFCON-1:     {defcon1}/{total} = {defcon1/total:.1%}")
    print(f"Mean turn:    {mean_len:.1f}")
    print(f"Turn 8+:      {turn8plus}/{total} = {turn8plus/total:.1%}")
    print(f"End reasons:  {dict(sorted(reasons.items(), key=lambda x: -x[1]))}")


if __name__ == "__main__":
    main()
