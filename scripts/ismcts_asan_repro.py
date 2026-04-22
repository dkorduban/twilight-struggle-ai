#!/usr/bin/env python3
"""ASAN repro harness: run ISMCTS at the known crasher config and let ASAN
catch heap bugs long before glibc free() would.

Runs at escalating N/side until asan reports something (or we time out).
"""
import os
import sys
import time

# Must come BEFORE importing tscore — ASAN interposes malloc at dlopen
os.environ.setdefault(
    "ASAN_OPTIONS",
    "abort_on_error=1:halt_on_error=1:detect_leaks=0:"
    "alloc_dealloc_mismatch=0:print_stacktrace=1:symbolize=1",
)

sys.path.insert(0, "build-asan/bindings")
import torch
import tscore

MODEL = "data/checkpoints/scripted_for_elo/v55_scripted.pt"
POOL = 16
N_DET = 16
N_SIM = 100
MAX_PEND = 8
DEV = "cpu"
SEED = 91000

torch.set_num_threads(2)


def run(n_per_side):
    print(f"\n=== N={n_per_side}/side  n_det={N_DET} n_sim={N_SIM} pool={POOL} ===",
          flush=True)
    t0 = time.perf_counter()
    try:
        results = tscore.benchmark_ismcts_vs_model_both_sides(
            MODEL, MODEL,
            n_games=2 * n_per_side,
            n_determinizations=N_DET, n_simulations=N_SIM,
            seed=SEED, pool_size=POOL, max_pending_per_det=MAX_PEND, device=DEV,
        )
        elapsed = time.perf_counter() - t0
        u = sum(1 for g in results[:n_per_side] if g.winner == tscore.Side.USSR)
        s = sum(1 for g in results[n_per_side:] if g.winner == tscore.Side.US)
        print(f"OK: elapsed={elapsed:.1f}s USSR={u}/{n_per_side} US={s}/{n_per_side}",
              flush=True)
        return True
    except Exception as e:
        print(f"FAIL: {e!r}", flush=True)
        return False


def main():
    for n in (5, 10, 15, 20, 25):
        ok = run(n)
        if not ok:
            print(f"Error at N={n}, stopping", flush=True)
            break


if __name__ == "__main__":
    main()
