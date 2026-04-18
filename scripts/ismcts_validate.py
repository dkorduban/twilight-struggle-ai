#!/usr/bin/env python3
"""Post-fix ISMCTS validation: larger N, both buckets.

  B_heur) ISMCTS vs heuristic (50/side)  -- the bucket that was 9.5%
  A_self) ISMCTS vs greedy NN self (50/side)  -- was 77.5% pre-fix
  C_ctrl) greedy NN vs heuristic (50/side)  -- sanity ceiling

Reports per-bucket: USSR WR, US WR, combined, end_reason breakdown.
"""
import collections
import sys
import time

sys.path.insert(0, "build-ninja/bindings")
import torch
import tscore

MODEL = "data/checkpoints/scripted_for_elo/v55_scripted.pt"
N = 50
POOL = 16
PEND = 8
DEV = "cpu"

# Seeds chosen distinct from ismcts_failure_diag.py to avoid cherry-pick.
SEED_HU = 70000  # heuristic bucket USSR
SEED_HS = 70500  # heuristic bucket US
SEED_SE = 71000  # self bucket


torch.set_num_threads(4)


def fmt(results, target_side):
    n = len(results)
    if n == 0:
        return "(empty)"
    wins = sum(1 for g in results if g.winner == target_side)
    reasons = collections.Counter(g.end_reason for g in results)
    mean_turn = sum(g.end_turn for g in results) / n
    reason_str = ", ".join(f"{k}={v}" for k, v in reasons.most_common(4))
    return f"wr={wins}/{n}={wins/n:.1%} mean_end_turn={mean_turn:.1f} reasons[{reason_str}]"


def main():
    print(f"POST-FIX VALIDATION: N={N}/side, n_det=4 n_sim=50", flush=True)
    print(f"model={MODEL}", flush=True)

    # C) greedy NN vs heuristic - ceiling
    print("\n=== C) greedy NN vs heuristic (control) ===", flush=True)
    t0 = time.perf_counter()
    c_u = tscore.benchmark_batched(
        MODEL, tscore.Side.USSR, N,
        pool_size=POOL, seed=SEED_HU, device=DEV,
        greedy_opponent=False, temperature=0.0, nash_temperatures=False,
    )
    c_s = tscore.benchmark_batched(
        MODEL, tscore.Side.US, N,
        pool_size=POOL, seed=SEED_HS, device=DEV,
        greedy_opponent=False, temperature=0.0, nash_temperatures=False,
    )
    print(f"elapsed={time.perf_counter()-t0:.1f}s")
    print(f"  USSR : {fmt(c_u, tscore.Side.USSR)}")
    print(f"  US   : {fmt(c_s, tscore.Side.US)}")
    c_wins = sum(1 for g in c_u if g.winner == tscore.Side.USSR) + \
             sum(1 for g in c_s if g.winner == tscore.Side.US)
    print(f"  COMBINED: {c_wins}/{2*N}={c_wins/(2*N):.1%}")

    # B) ISMCTS vs heuristic
    print("\n=== B) ISMCTS vs heuristic ===", flush=True)
    t0 = time.perf_counter()
    b_u = tscore.benchmark_ismcts(
        MODEL, tscore.Side.USSR, N,
        n_determinizations=4, n_simulations=50,
        seed=SEED_HU, pool_size=POOL, max_pending_per_det=PEND, device=DEV,
    )
    b_s = tscore.benchmark_ismcts(
        MODEL, tscore.Side.US, N,
        n_determinizations=4, n_simulations=50,
        seed=SEED_HS, pool_size=POOL, max_pending_per_det=PEND, device=DEV,
    )
    print(f"elapsed={time.perf_counter()-t0:.1f}s")
    print(f"  USSR : {fmt(b_u, tscore.Side.USSR)}")
    print(f"  US   : {fmt(b_s, tscore.Side.US)}")
    b_wins = sum(1 for g in b_u if g.winner == tscore.Side.USSR) + \
             sum(1 for g in b_s if g.winner == tscore.Side.US)
    print(f"  COMBINED: {b_wins}/{2*N}={b_wins/(2*N):.1%}")

    # A) ISMCTS vs greedy v55 self
    print("\n=== A) ISMCTS vs greedy v55 self ===", flush=True)
    t0 = time.perf_counter()
    a_all = tscore.benchmark_ismcts_vs_model_both_sides(
        MODEL, MODEL,
        n_games=2 * N,
        n_determinizations=4, n_simulations=50,
        seed=SEED_SE, pool_size=POOL, max_pending_per_det=PEND, device=DEV,
    )
    a_u = a_all[:N]
    a_s = a_all[N:]
    print(f"elapsed={time.perf_counter()-t0:.1f}s")
    print(f"  ISMCTS-USSR vs greedy-US  : {fmt(a_u, tscore.Side.USSR)}")
    print(f"  ISMCTS-US   vs greedy-USSR: {fmt(a_s, tscore.Side.US)}")
    a_wins = sum(1 for g in a_u if g.winner == tscore.Side.USSR) + \
             sum(1 for g in a_s if g.winner == tscore.Side.US)
    print(f"  COMBINED: {a_wins}/{2*N}={a_wins/(2*N):.1%}")

    print("\n=== SUMMARY ===")
    print(f"greedy  vs heuristic : {c_wins/(2*N):.1%}  <- ceiling")
    print(f"ISMCTS  vs heuristic : {b_wins/(2*N):.1%}  <- target: match or beat greedy")
    print(f"ISMCTS  vs greedy-self: {a_wins/(2*N):.1%}  <- search-vs-no-search check")


if __name__ == "__main__":
    main()
