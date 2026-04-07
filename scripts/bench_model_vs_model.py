#!/usr/bin/env python3
"""Benchmark throughput of benchmark_model_vs_model_batched vs pool_size.

Measures games/second at various pool sizes and compares against
the single-model benchmark_batched (model vs heuristic).

Usage:
    cd /home/dkord/code/twilight-struggle-ai
    PYTHONPATH=build-ninja/bindings uv run python scripts/bench_model_vs_model.py

    # Or with custom model paths:
    PYTHONPATH=build-ninja/bindings uv run python scripts/bench_model_vs_model.py \
        --model-a data/checkpoints/ppo_v2_selfplay/ppo_best_scripted.pt \
        --model-b data/checkpoints/v99_nash_c_95ep_s42/baseline_best_scripted.pt
"""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

_REPO = Path(__file__).resolve().parents[1]
for _p in (_REPO / "build-ninja" / "bindings", _REPO / "build" / "bindings"):
    if _p.exists():
        sys.path.insert(0, str(_p))
        break

import tscore  # noqa: E402


def measure(fn, n_reps: int = 3) -> float:
    """Return average wall-clock seconds over n_reps calls."""
    times = []
    for _ in range(n_reps):
        t0 = time.perf_counter()
        fn()
        times.append(time.perf_counter() - t0)
    return sum(times) / n_reps


def main():
    parser = argparse.ArgumentParser(description="Benchmark model-vs-model throughput")
    parser.add_argument(
        "--model-a",
        default=str(_REPO / "data/checkpoints/v99_nash_c_95ep_s42/baseline_best_scripted.pt"),
        help="Path to scripted model A",
    )
    parser.add_argument(
        "--model-b",
        default=str(_REPO / "data/checkpoints/ppo_v1_from_v106/ppo_best_scripted.pt"),
        help="Path to scripted model B",
    )
    parser.add_argument("--n-reps", type=int, default=3, help="Repetitions per measurement")
    args = parser.parse_args()

    model_a = args.model_a
    model_b = args.model_b

    if not hasattr(tscore, "benchmark_model_vs_model_batched"):
        print("ERROR: benchmark_model_vs_model_batched not available. Rebuild bindings.")
        sys.exit(1)

    for p, name in [(model_a, "model_a"), (model_b, "model_b")]:
        if not Path(p).exists():
            print(f"ERROR: {name} not found: {p}")
            sys.exit(1)

    # ------------------------------------------------------------------
    # Warmup
    # ------------------------------------------------------------------
    print("Warming up...")
    tscore.benchmark_model_vs_model_batched(
        model_a, model_a, n_games=4, pool_size=2, seed=1,
        temperature=0.0, nash_temperatures=False,
    )
    if hasattr(tscore, "benchmark_batched"):
        tscore.benchmark_batched(
            model_a, tscore.Side.USSR, 4, pool_size=2, seed=1,
            temperature=0.0, nash_temperatures=True,
        )

    # ------------------------------------------------------------------
    # Section 1: Throughput vs pool_size
    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("Section 1: model_vs_model throughput vs pool_size")
    print(f"  model_a: {Path(model_a).name}")
    print("  model_b: same as model_a (self-play)")
    print(f"  n_reps: {args.n_reps}")
    print("=" * 70)

    pool_sizes = [1, 4, 8, 16, 32, 64]
    n_games_for_pool = 100

    print(f"\n{'pool_size':>10} {'n_games':>8} {'time(s)':>10} {'games/s':>10} {'speedup':>10}")
    print("-" * 52)

    baseline_gps = None
    for ps in pool_sizes:
        t = measure(
            lambda _ps=ps: tscore.benchmark_model_vs_model_batched(
                model_a, model_a, n_games=n_games_for_pool, pool_size=_ps,
                seed=50000, temperature=0.0, nash_temperatures=False,
            ),
            n_reps=args.n_reps,
        )
        gps = n_games_for_pool / t
        if baseline_gps is None:
            baseline_gps = gps
        speedup = gps / baseline_gps
        print(f"{ps:>10} {n_games_for_pool:>8} {t:>10.2f} {gps:>10.1f} {speedup:>10.2f}x")

    # ------------------------------------------------------------------
    # Section 2: Same model vs different model throughput
    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("Section 2: same model vs different models throughput")
    print("=" * 70)

    n_games = 100
    ps = 32

    t_same = measure(
        lambda: tscore.benchmark_model_vs_model_batched(
            model_a, model_a, n_games=n_games, pool_size=ps,
            seed=60000, temperature=0.0, nash_temperatures=False,
        ),
        n_reps=args.n_reps,
    )
    t_diff = measure(
        lambda: tscore.benchmark_model_vs_model_batched(
            model_a, model_b, n_games=n_games, pool_size=ps,
            seed=60000, temperature=0.0, nash_temperatures=False,
        ),
        n_reps=args.n_reps,
    )

    print(f"\n{'Config':<40} {'time(s)':>10} {'games/s':>10}")
    print("-" * 62)
    print(f"{'model_vs_model (same model, ps=32)':<40} {t_same:>10.2f} {n_games/t_same:>10.1f}")
    print(f"{'model_vs_model (diff models, ps=32)':<40} {t_diff:>10.2f} {n_games/t_diff:>10.1f}")

    # ------------------------------------------------------------------
    # Section 3: vs benchmark_batched (model vs heuristic)
    # ------------------------------------------------------------------
    if hasattr(tscore, "benchmark_batched"):
        print("\n" + "=" * 70)
        print("Section 3: model_vs_model vs benchmark_batched (model vs heuristic)")
        print("=" * 70)

        t_heur_ussr = measure(
            lambda: tscore.benchmark_batched(
                model_a, tscore.Side.USSR, n_games, pool_size=ps, seed=70000,
                temperature=0.0, nash_temperatures=True,
            ),
            n_reps=args.n_reps,
        )
        t_heur_us = measure(
            lambda: tscore.benchmark_batched(
                model_a, tscore.Side.US, n_games, pool_size=ps, seed=70000,
                temperature=0.0, nash_temperatures=True,
            ),
            n_reps=args.n_reps,
        )

        print(f"\n{'Config':<42} {'time(s)':>8} {'games/s':>8}")
        print("-" * 60)
        ussr_gps = n_games / t_heur_ussr
        us_gps = n_games / t_heur_us
        same_gps = n_games / t_same
        diff_gps = n_games / t_diff
        print(f"{'bench_batched (USSR vs heur, ps=32)':<42} {t_heur_ussr:>8.2f} {ussr_gps:>8.1f}")
        print(f"{'bench_batched (US vs heur, ps=32)':<42} {t_heur_us:>8.2f} {us_gps:>8.1f}")
        print(f"{'model_vs_model (same model, ps=32)':<42} {t_same:>8.2f} {same_gps:>8.1f}")
        print(f"{'model_vs_model (diff models, ps=32)':<42} {t_diff:>8.2f} {diff_gps:>8.1f}")

        avg_heur = (t_heur_ussr + t_heur_us) / 2
        avg_mvm = (t_same + t_diff) / 2
        ratio = avg_mvm / avg_heur if avg_heur > 0 else float("inf")
        print(f"\nSlowdown ratio (model_vs_model / vs_heuristic): {ratio:.2f}x")
        print("Expected: ~1.5-3x (two NN forward passes per step vs one NN + fast heuristic)")

    # ------------------------------------------------------------------
    # Section 4: Consistency across n_games
    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("Section 4: games/s stability across n_games")
    print("=" * 70)

    ps = 32
    print(f"\n{'n_games':>10} {'time(s)':>10} {'games/s':>10}")
    print("-" * 32)
    for ng in [10, 50, 100, 200]:
        t = measure(
            lambda _ng=ng: tscore.benchmark_model_vs_model_batched(
                model_a, model_a, n_games=_ng, pool_size=ps,
                seed=80000, temperature=0.0, nash_temperatures=False,
            ),
            n_reps=max(1, args.n_reps // (ng // 50 + 1)),  # fewer reps for large n
        )
        gps = ng / t
        print(f"{ng:>10} {t:>10.2f} {gps:>10.1f}")

    print("\nDone.")


if __name__ == "__main__":
    main()
