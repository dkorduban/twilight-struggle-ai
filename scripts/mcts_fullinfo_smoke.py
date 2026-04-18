"""Full-info MCTS smoke test: benchmark_mcts_vs_greedy at various sim budgets.

Compares:
  - MCTS (full information, both hands known) vs greedy NN (same model)
  - Same seeds as ISMCTS paired test for direct comparison

Hypothesis: if value head is calibrated, full-info MCTS should be net-positive
vs greedy at sufficient budget. If still net-negative, the PUCT/rollout itself
is the problem (not just determinization bias as with ISMCTS).

Reference: ISMCTS post-fix paired result was -21 net (5/50 wins, 27/50 losses).
"""

import argparse
import json
import os
import sys
import time

import tscore


def side_wr(results, side: tscore.Side) -> float:
    wins = sum(1 for r in results if r.winner == side)
    return wins / len(results) if results else 0.0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="data/checkpoints/scripted_for_elo/v55_scripted.pt")
    ap.add_argument("--n-games", type=int, default=20, help="games per side")
    ap.add_argument("--pool", type=int, default=16)
    ap.add_argument("--seed", type=int, default=91000, help="same as ISMCTS sweep")
    ap.add_argument(
        "--sims",
        default="50,100,200,400",
        help="comma-separated n_simulations to try",
    )
    ap.add_argument("--output", default="results/ismcts_fix/mcts_fullinfo_smoke.json")
    args = ap.parse_args()

    sim_values = [int(s) for s in args.sims.split(",") if s.strip()]
    model_path = args.model

    print(f"Model: {model_path}")
    print(f"N games/side: {args.n_games}  pool: {args.pool}  seed: {args.seed}")
    print()
    print(f"{'n_sim':>6}  {'USSR_wr':>8}  {'US_wr':>7}  {'combined':>9}  {'secs':>6}")
    print("-" * 50)

    all_results = []
    for n_sim in sim_values:
        t0 = time.time()
        # USSR side
        results_ussr = tscore.benchmark_mcts_vs_greedy(
            model_path,
            tscore.Side.USSR,
            n_games=args.n_games,
            n_simulations=n_sim,
            pool_size=args.pool,
            seed=args.seed,
        )
        # US side
        results_us = tscore.benchmark_mcts_vs_greedy(
            model_path,
            tscore.Side.US,
            n_games=args.n_games,
            n_simulations=n_sim,
            pool_size=args.pool,
            seed=args.seed + 500,
        )
        dt = time.time() - t0
        ussr_wr = side_wr(results_ussr, tscore.Side.USSR)
        us_wr = side_wr(results_us, tscore.Side.US)
        combined = (ussr_wr + us_wr) / 2
        print(
            f"{n_sim:>6}  {ussr_wr:>8.1%}  {us_wr:>7.1%}  {combined:>9.1%}  {dt:>6.1f}"
        )
        all_results.append(
            {
                "n_sim": n_sim,
                "ussr_wr": ussr_wr,
                "us_wr": us_wr,
                "combined": combined,
                "n_games_per_side": args.n_games,
                "secs": dt,
            }
        )

    out = {
        "model": model_path,
        "n_games_per_side": args.n_games,
        "seed": args.seed,
        "pool": args.pool,
        "sweep": all_results,
        "reference_ismcts_combined_postfix": 0.42,
        "reference_greedy_combined": 0.51,
    }
    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote: {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
