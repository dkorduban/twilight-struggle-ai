#!/usr/bin/env python3
"""Minimal repro: try to reproduce the free() crash at n_det=16 n_sim=100.

Test matrix:
  1. n_det=16 n_sim=100 pool=16 — known crasher
  2. n_det=16 n_sim=50  pool=16 — does n_sim matter?
  3. n_det=16 n_sim=100 pool=4  — does pool size matter?
  4. n_det=12 n_sim=100 pool=16 — does n_det matter?
"""
import sys
import time

sys.path.insert(0, "build-ninja/bindings")
import torch
import tscore

MODEL = "data/checkpoints/scripted_for_elo/v55_scripted.pt"
N_PER_SIDE = 10
DEV = "cpu"

torch.set_num_threads(4)


def run(n_det, n_sim, pool, label):
    print(f"\n=== {label}: n_det={n_det} n_sim={n_sim} pool={pool} ===", flush=True)
    t0 = time.perf_counter()
    try:
        results = tscore.benchmark_ismcts_vs_model_both_sides(
            MODEL, MODEL,
            n_games=2 * N_PER_SIDE,
            n_determinizations=n_det, n_simulations=n_sim,
            seed=91000, pool_size=pool, max_pending_per_det=8, device=DEV,
        )
        elapsed = time.perf_counter() - t0
        ussr_wins = sum(1 for g in results[:N_PER_SIDE] if g.winner == tscore.Side.USSR)
        us_wins = sum(1 for g in results[N_PER_SIDE:] if g.winner == tscore.Side.US)
        combined = (ussr_wins + us_wins) / (2 * N_PER_SIDE)
        print(f"OK: elapsed={elapsed:.1f}s combined={combined:.1%}", flush=True)
        return True
    except Exception as e:
        print(f"FAIL: {e!r}", flush=True)
        return False


def main():
    # Try the known crasher first to confirm repro
    run(16, 100, 16, "A (known crasher)")
    # Then variations
    run(16, 50, 16, "B (half sims)")
    run(16, 100, 4, "C (smaller pool)")
    run(12, 100, 16, "D (fewer dets)")


if __name__ == "__main__":
    main()
