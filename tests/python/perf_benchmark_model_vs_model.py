"""Performance comparison: benchmark_batched vs benchmark_model_vs_model_batched.

Not a pytest test — run directly:
    cd /home/dkord/code/twilight-struggle-ai
    PYTHONPATH=build-ninja/bindings uv run python tests/python/perf_benchmark_model_vs_model.py
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
for _p in (_REPO / "build-ninja" / "bindings", _REPO / "build" / "bindings"):
    if _p.exists():
        sys.path.insert(0, str(_p))
        break

import tscore  # noqa: E402

MODEL_A = str(_REPO / "data/checkpoints/v99_nash_c_95ep_s42/baseline_best_scripted.pt")
MODEL_B = str(_REPO / "data/checkpoints/ppo_v1_from_v106/ppo_best_scripted.pt")
N_GAMES = 100
POOL_SIZE = 32
SEED = 80000


def measure(label: str, fn, n_reps: int = 3):
    times = []
    for _ in range(n_reps):
        t0 = time.perf_counter()
        fn()
        times.append(time.perf_counter() - t0)
    avg = sum(times) / n_reps
    return avg


def main():
    if not hasattr(tscore, "benchmark_model_vs_model_batched"):
        print("ERROR: tscore.benchmark_model_vs_model_batched not available — rebuild.")
        sys.exit(1)

    print("Warmup...")
    tscore.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_A, n_games=4, pool_size=2, seed=1, temperature=0.0,
    )
    tscore.benchmark_batched(
        MODEL_A, tscore.Side.USSR, 4, pool_size=2, seed=1, temperature=0.0,
        nash_temperatures=True,
    )

    print(f"\nBenchmark: {N_GAMES} games, pool_size={POOL_SIZE} (avg of 3 runs)\n")
    print(f"{'Method':<40} {'Time (s)':>10} {'Games/s':>10}")
    print("-" * 62)

    t_old_ussr = measure("vs-heuristic USSR", lambda: tscore.benchmark_batched(
        MODEL_A, tscore.Side.USSR, N_GAMES, pool_size=POOL_SIZE, seed=SEED,
        temperature=0.0, nash_temperatures=True,
    ))
    print(f"{'benchmark_batched (USSR, nash-temp)':<40} {t_old_ussr:>10.2f} {N_GAMES/t_old_ussr:>10.1f}")

    t_old_us = measure("vs-heuristic US", lambda: tscore.benchmark_batched(
        MODEL_A, tscore.Side.US, N_GAMES, pool_size=POOL_SIZE, seed=SEED,
        temperature=0.0, nash_temperatures=True,
    ))
    print(f"{'benchmark_batched (US, nash-temp)':<40} {t_old_us:>10.2f} {N_GAMES/t_old_us:>10.1f}")

    t_new_same = measure("model-vs-model same", lambda: tscore.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_A, n_games=N_GAMES, pool_size=POOL_SIZE, seed=SEED, temperature=0.0,
    ))
    print(f"{'model_vs_model (same model)':<40} {t_new_same:>10.2f} {N_GAMES/t_new_same:>10.1f}")

    t_new_diff = measure("model-vs-model diff", lambda: tscore.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_B, n_games=N_GAMES, pool_size=POOL_SIZE, seed=SEED, temperature=0.0,
    ))
    print(f"{'model_vs_model (diff models)':<40} {t_new_diff:>10.2f} {N_GAMES/t_new_diff:>10.1f}")

    avg_old = (t_old_ussr + t_old_us) / 2
    avg_new = (t_new_same + t_new_diff) / 2
    ratio = avg_new / avg_old
    print(f"\nSlowdown (model-vs-model / model-vs-heuristic): {ratio:.2f}x")
    print(f"Expected: ~1.5-2.5x (two NN passes vs one NN + fast heuristic)")


if __name__ == "__main__":
    main()
