#!/usr/bin/env python3
"""Sweep n_determinizations × n_simulations for ISMCTS vs heuristic.

Small sweep (N=10 games/side) to find a setting where ISMCTS beats greedy control.
"""
import sys
import time

sys.path.insert(0, "build-ninja/bindings")
import torch
import tscore

MODEL = "data/checkpoints/scripted_for_elo/v55_scripted.pt"
N = 10
POOL = 16
PEND = 8
DEV = "cpu"
SEED_U = 80000
SEED_S = 80500

torch.set_num_threads(4)


def wins(results, side):
    return sum(1 for g in results if g.winner == side)


def run(n_det, n_sim):
    t0 = time.perf_counter()
    r_ussr = tscore.benchmark_ismcts(
        MODEL, tscore.Side.USSR, N,
        n_determinizations=n_det, n_simulations=n_sim,
        seed=SEED_U, pool_size=POOL, max_pending_per_det=PEND, device=DEV,
    )
    r_us = tscore.benchmark_ismcts(
        MODEL, tscore.Side.US, N,
        n_determinizations=n_det, n_simulations=n_sim,
        seed=SEED_S, pool_size=POOL, max_pending_per_det=PEND, device=DEV,
    )
    elapsed = time.perf_counter() - t0
    return wins(r_ussr, tscore.Side.USSR), wins(r_us, tscore.Side.US), elapsed


def main():
    print(f"ISMCTS sweep: N={N} games/side, pool={POOL} pend={PEND}", flush=True)
    print(f"{'n_det':>6} {'n_sim':>6} {'rollouts':>9} {'USSR_wr':>8} {'US_wr':>7} {'combined':>9} {'secs':>6}")
    configs = [
        (2, 25), (2, 50), (2, 100),
        (4, 25), (4, 50), (4, 100),
        (8, 25), (8, 50), (8, 100),
    ]
    for n_det, n_sim in configs:
        u, s, t = run(n_det, n_sim)
        combined = (u + s) / (2 * N)
        print(
            f"{n_det:>6} {n_sim:>6} {n_det*n_sim:>9} "
            f"{u/N:>8.1%} {s/N:>7.1%} {combined:>9.1%} {t:>6.1f}",
            flush=True,
        )


if __name__ == "__main__":
    main()
