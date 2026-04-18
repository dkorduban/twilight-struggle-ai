#!/usr/bin/env python3
"""ISMCTS failure-mode diagnostic.

For v55:
  A) ISMCTS(4x50) vs greedy NN self (100 games: 50 ISMCTS-USSR + 50 ISMCTS-US)
  B) ISMCTS(4x50) vs heuristic      (same split)
  C) Greedy NN vs heuristic         (control, same split)

Reports per-bucket:
  - win rate
  - end_reason distribution (vp_threshold, defcon1, final_scoring, wargames, ...)
  - end_turn mean / distribution

Takes one turn-length snapshot per game via GameResult.end_turn/end_reason.
"""
import collections
import sys
import time

sys.path.insert(0, "build-ninja/bindings")
import torch
import tscore

MODEL = "data/checkpoints/scripted_for_elo/v55_scripted.pt"
N_PER_SIDE = 10
POOL  = 16
PEND  = 8
INTRA = 4
DEV   = "cpu"

SEED_U = 80000
SEED_S = 80500
SEED_SELF = 81000

torch.set_num_threads(INTRA)


def summarize(results, ismcts_side_label):
    """Compact summary per bucket."""
    n = len(results)
    if n == 0:
        return "(no games)"
    reasons = collections.Counter(r.end_reason for r in results)
    turns = [r.end_turn for r in results]
    mean_t = sum(turns) / n
    winners = collections.Counter("USSR" if r.winner == tscore.Side.USSR
                                  else "US"   if r.winner == tscore.Side.US
                                  else "draw" for r in results)
    reason_str = ", ".join(f"{k}={v}" for k, v in reasons.most_common())
    winner_str = ", ".join(f"{k}={v}" for k, v in winners.most_common())
    return (f"  n={n}  mean_end_turn={mean_t:.2f}  winners[{winner_str}]\n"
            f"  reasons: {reason_str}")


def ismcts_vs_self():
    print("\n=== A) v55 ISMCTS(4x50) vs v55 greedy NN ===", flush=True)
    t0 = time.perf_counter()
    results = tscore.benchmark_ismcts_vs_model_both_sides(
        MODEL, MODEL,
        n_games=2 * N_PER_SIDE,
        n_determinizations=4, n_simulations=50,
        seed=SEED_SELF, pool_size=POOL, max_pending_per_det=PEND, device=DEV,
    )
    elapsed = time.perf_counter() - t0
    ussr_half = results[:N_PER_SIDE]
    us_half   = results[N_PER_SIDE:]
    print(f"elapsed={elapsed:.1f}s", flush=True)
    print("ISMCTS as USSR (opponent = greedy v55 US):", flush=True)
    print(summarize(ussr_half, "USSR"), flush=True)
    print("ISMCTS as US (opponent = greedy v55 USSR):", flush=True)
    print(summarize(us_half, "US"), flush=True)


def ismcts_vs_heuristic():
    print("\n=== B) v55 ISMCTS(4x50) vs heuristic ===", flush=True)
    t0 = time.perf_counter()
    r_ussr = tscore.benchmark_ismcts(
        MODEL, tscore.Side.USSR, N_PER_SIDE,
        n_determinizations=4, n_simulations=50,
        seed=SEED_U, pool_size=POOL, max_pending_per_det=PEND, device=DEV,
    )
    r_us = tscore.benchmark_ismcts(
        MODEL, tscore.Side.US, N_PER_SIDE,
        n_determinizations=4, n_simulations=50,
        seed=SEED_S, pool_size=POOL, max_pending_per_det=PEND, device=DEV,
    )
    elapsed = time.perf_counter() - t0
    print(f"elapsed={elapsed:.1f}s", flush=True)
    print("ISMCTS as USSR (opponent = greedy heuristic US):", flush=True)
    print(summarize(r_ussr, "USSR"), flush=True)
    print("ISMCTS as US (opponent = greedy heuristic USSR):", flush=True)
    print(summarize(r_us, "US"), flush=True)


def greedy_vs_heuristic():
    print("\n=== C) v55 greedy NN vs heuristic (control) ===", flush=True)
    t0 = time.perf_counter()
    # Match config with ISMCTS heuristic — greedy_opponent=False, nash_temperatures=FALSE
    # so heuristic is greedy (apples-to-apples with benchmark_ismcts).
    r_ussr_nash = tscore.benchmark_batched(
        MODEL, tscore.Side.USSR, N_PER_SIDE,
        pool_size=POOL, seed=SEED_U, device=DEV,
        greedy_opponent=False, temperature=0.0, nash_temperatures=False,
    )
    r_us_nash = tscore.benchmark_batched(
        MODEL, tscore.Side.US, N_PER_SIDE,
        pool_size=POOL, seed=SEED_S, device=DEV,
        greedy_opponent=False, temperature=0.0, nash_temperatures=False,
    )
    elapsed = time.perf_counter() - t0
    print(f"elapsed={elapsed:.1f}s (greedy heuristic — matches ISMCTS opponent config)", flush=True)
    print("greedy v55 as USSR (opponent = greedy heuristic US):", flush=True)
    print(summarize(r_ussr_nash, "USSR"), flush=True)
    print("greedy v55 as US (opponent = greedy heuristic USSR):", flush=True)
    print(summarize(r_us_nash, "US"), flush=True)


def main():
    print(f"Diagnostic: {N_PER_SIDE} games/side · pool={POOL} pend={PEND} intra={INTRA}", flush=True)
    greedy_vs_heuristic()
    ismcts_vs_heuristic()
    ismcts_vs_self()


if __name__ == "__main__":
    main()
