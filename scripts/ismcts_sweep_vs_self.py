#!/usr/bin/env python3
"""Sweep n_determinizations × n_simulations for ISMCTS vs greedy v55 self.

Test whether search budget correlates with WR. If more rollouts → more wins, the
fix is fine and low budgets are just search-weak. If search budget has no effect
or is negatively correlated, there's a bug in the search itself.
"""
import sys
import time

sys.path.insert(0, "build-ninja/bindings")
import torch
import tscore

MODEL = "data/checkpoints/scripted_for_elo/v55_scripted.pt"
N_PER_SIDE = 20
POOL = 16
PEND = 8
DEV = "cpu"
SEED = 91000

torch.set_num_threads(4)


def run(n_det, n_sim):
    t0 = time.perf_counter()
    results = tscore.benchmark_ismcts_vs_model_both_sides(
        MODEL, MODEL,
        n_games=2 * N_PER_SIDE,
        n_determinizations=n_det, n_simulations=n_sim,
        seed=SEED, pool_size=POOL, max_pending_per_det=PEND, device=DEV,
    )
    elapsed = time.perf_counter() - t0
    r_ussr = results[:N_PER_SIDE]
    r_us = results[N_PER_SIDE:]
    u = sum(1 for g in r_ussr if g.winner == tscore.Side.USSR)
    s = sum(1 for g in r_us if g.winner == tscore.Side.US)
    return u, s, elapsed


def main():
    print(f"ISMCTS vs greedy v55 self sweep: N={N_PER_SIDE} games/side, seed={SEED}", flush=True)
    print(f"{'n_det':>6} {'n_sim':>6} {'rollouts':>9} {'USSR_wr':>8} {'US_wr':>7} {'combined':>9} {'secs':>6}")
    configs = [
        (2, 25),
        (2, 50),
        (4, 50),
        (4, 100),
        (8, 100),
        (16, 100),
    ]
    for n_det, n_sim in configs:
        u, s, t = run(n_det, n_sim)
        combined = (u + s) / (2 * N_PER_SIDE)
        print(
            f"{n_det:>6} {n_sim:>6} {n_det*n_sim:>9} "
            f"{u/N_PER_SIDE:>8.1%} {s/N_PER_SIDE:>7.1%} {combined:>9.1%} {t:>6.1f}",
            flush=True,
        )


if __name__ == "__main__":
    main()
