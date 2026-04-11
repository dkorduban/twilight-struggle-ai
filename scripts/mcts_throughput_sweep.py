#!/usr/bin/env python3
"""
MCTS throughput matrix benchmark sweep.
Runs Phase 1 (thread sweep) and Phase 2 (max-pending sweep).
Parses stderr for MCTS profiling data and computes sims/s.
"""

import subprocess
import re
import json
from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class BenchmarkResult:
    mcts_threads: int
    torch_intra_threads: int
    torch_interop_threads: int
    pool_size: int
    max_pending: int
    sims_per_sec: float
    total_time_sec: float
    total_items: int
    avg_batch_size: float
    select_time_sec: float
    nn_time_sec: float
    expand_time_sec: float
    advance_time_sec: float
    stderr: str

def parse_mcts_profile(stderr: str) -> Optional[dict]:
    """Extract [MCTS profile] line from stderr."""
    match = re.search(
        r'\[MCTS profile\].*?threads=(\d+).*?advance=([\d.]+)s.*?select=([\d.]+)s.*?nn=([\d.]+)s.*?expand=([\d.]+)s.*?total=([\d.]+)s',
        stderr,
        re.DOTALL
    )
    if match:
        return {
            'threads': int(match.group(1)),
            'advance_time': float(match.group(2)),
            'select_time': float(match.group(3)),
            'nn_time': float(match.group(4)),
            'expand_time': float(match.group(5)),
            'total_time': float(match.group(6)),
        }
    return None

def parse_batch_info(stderr: str) -> Optional[dict]:
    """Extract batches=N items=N avg_batch=F from stderr."""
    match = re.search(r'batches=(\d+)\s+items=(\d+)\s+avg_batch=([\d.]+)', stderr)
    if match:
        return {
            'batches': int(match.group(1)),
            'items': int(match.group(2)),
            'avg_batch': float(match.group(3)),
        }
    return None

def run_benchmark(
    mcts_threads: int,
    torch_intra_threads: int,
    torch_interop_threads: int,
    pool_size: int = 32,
    max_pending: int = 32,
) -> Optional[BenchmarkResult]:
    """Run a single benchmark configuration."""

    cmd = [
        './build-ninja/cpp/tools/ts_collect_mcts_games_jsonl',
        '--games', '32',
        '--n-sim', '200',
        '--seed', '77700',
        '--temperature', '1.0',
        '--dir-alpha', '0.3',
        '--dir-epsilon', '0.25',
        '--model', 'data/checkpoints/v106_cf_gnn_s42/baseline_best_scripted.pt',
        '--mcts-threads', str(mcts_threads),
        '--torch-intra-threads', str(torch_intra_threads),
        '--torch-interop-threads', str(torch_interop_threads),
        '--pool-size', str(pool_size),
        '--max-pending', str(max_pending),
        '--out', '/dev/null',
    ]

    try:
        result = subprocess.run(
            cmd,
            cwd='/home/dkord/code/twilight-struggle-ai',
            capture_output=True,
            text=True,
            timeout=120,
        )
        stderr = result.stderr

        profile = parse_mcts_profile(stderr)
        batch_info = parse_batch_info(stderr)

        if not profile or not batch_info:
            print(f"  [PARSE FAIL] threads={mcts_threads}, intra={torch_intra_threads}, interop={torch_interop_threads}")
            print(f"    Profile: {profile}")
            print(f"    Batch: {batch_info}")
            return None

        total_items = batch_info['items']
        total_time = profile['total_time']
        sims_per_sec = total_items / total_time if total_time > 0 else 0

        return BenchmarkResult(
            mcts_threads=mcts_threads,
            torch_intra_threads=torch_intra_threads,
            torch_interop_threads=torch_interop_threads,
            pool_size=pool_size,
            max_pending=max_pending,
            sims_per_sec=sims_per_sec,
            total_time_sec=total_time,
            total_items=total_items,
            avg_batch_size=batch_info['avg_batch'],
            select_time_sec=profile['select_time'],
            nn_time_sec=profile['nn_time'],
            expand_time_sec=profile['expand_time'],
            advance_time_sec=profile['advance_time'],
            stderr=stderr,
        )
    except subprocess.TimeoutExpired:
        print(f"  [TIMEOUT] threads={mcts_threads}, intra={torch_intra_threads}, interop={torch_interop_threads}")
        return None
    except Exception as e:
        print(f"  [ERROR] threads={mcts_threads}, intra={torch_intra_threads}, interop={torch_interop_threads}: {e}")
        return None

def main():
    results: List[BenchmarkResult] = []

    # Phase 1: Thread sweep (pool=32, max-pending=32)
    phase1_configs = [
        (1, 1, 1),
        (1, 2, 1),
        (1, 4, 1),
        (2, 1, 1),
        (2, 2, 1),
        (2, 4, 1),
        (4, 1, 1),
        (4, 2, 1),
        (4, 4, 1),
        (8, 2, 1),
        (8, 4, 1),
    ]

    print("=" * 80)
    print("WARMUP RUN (discarding)")
    print("=" * 80)
    _ = run_benchmark(4, 2, 1, pool_size=32, max_pending=32)
    print()

    print("=" * 80)
    print("PHASE 1: Thread sweep (pool=32, max-pending=32)")
    print("=" * 80)
    for mcts_t, intra_t, interop_t in phase1_configs:
        print(f"threads={mcts_t}, intra={intra_t}, interop={interop_t}...", end=" ", flush=True)
        result = run_benchmark(mcts_t, intra_t, interop_t, pool_size=32, max_pending=32)
        if result:
            print(f"✓ {result.sims_per_sec:.1f} sims/s ({result.total_time_sec:.2f}s)")
            results.append(result)
        else:
            print("FAILED")
    print()

    # Find best config from Phase 1
    if results:
        best_phase1 = max(results, key=lambda r: r.sims_per_sec)
        print(f"Best Phase 1 config: threads={best_phase1.mcts_threads}, "
              f"intra={best_phase1.torch_intra_threads}, "
              f"interop={best_phase1.torch_interop_threads} "
              f"({best_phase1.sims_per_sec:.1f} sims/s)")
        print()

        # Phase 2: max-pending sweep using best config
        phase2_configs = [
            (32, 8),
            (32, 16),
            (32, 32),
            (32, 64),
            (64, 32),
            (64, 64),
        ]

        print("=" * 80)
        print("PHASE 2: max-pending sweep (using best Phase 1 thread config)")
        print("=" * 80)
        for pool, pending in phase2_configs:
            print(f"pool={pool}, max-pending={pending}...", end=" ", flush=True)
            result = run_benchmark(
                best_phase1.mcts_threads,
                best_phase1.torch_intra_threads,
                best_phase1.torch_interop_threads,
                pool_size=pool,
                max_pending=pending,
            )
            if result:
                print(f"✓ {result.sims_per_sec:.1f} sims/s ({result.total_time_sec:.2f}s)")
                results.append(result)
            else:
                print("FAILED")
        print()

    # Generate summary report
    if results:
        print("=" * 80)
        print("SUMMARY TABLE (sorted by sims/s)")
        print("=" * 80)

        sorted_results = sorted(results, key=lambda r: r.sims_per_sec, reverse=True)

        # Header
        print(f"{'MCTS':<5} {'Intra':<6} {'Interop':<8} {'Pool':<5} {'MaxPend':<8} "
              f"{'Sims/s':<10} {'Time':<8} {'AvgBatch':<10} {'Select':<8} {'NN':<8} {'Expand':<8}")
        print("-" * 95)

        for r in sorted_results:
            print(f"{r.mcts_threads:<5} {r.torch_intra_threads:<6} {r.torch_interop_threads:<8} "
                  f"{r.pool_size:<5} {r.max_pending:<8} "
                  f"{r.sims_per_sec:<10.1f} {r.total_time_sec:<8.3f} {r.avg_batch_size:<10.2f} "
                  f"{r.select_time_sec:<8.3f} {r.nn_time_sec:<8.3f} {r.expand_time_sec:<8.3f}")

        print()
        best = sorted_results[0]
        print(f"BEST OVERALL: threads={best.mcts_threads}, intra={best.torch_intra_threads}, "
              f"interop={best.torch_interop_threads}, pool={best.pool_size}, "
              f"max-pending={best.max_pending}")
        print(f"  → {best.sims_per_sec:.1f} sims/s")

        # Best config with ≤4 MCTS threads
        constrained = [r for r in sorted_results if r.mcts_threads <= 4]
        if constrained:
            best_constrained = constrained[0]
            print(f"\nBEST WITH ≤4 MCTS THREADS: threads={best_constrained.mcts_threads}, "
                  f"intra={best_constrained.torch_intra_threads}, interop={best_constrained.torch_interop_threads}")
            print(f"  → {best_constrained.sims_per_sec:.1f} sims/s")

        # Bottleneck analysis
        print("\nBOTTLENECK ANALYSIS (from best overall):")
        total = best.total_time_sec
        print(f"  Select:  {best.select_time_sec:.3f}s ({100*best.select_time_sec/total:.1f}%)")
        print(f"  NN:      {best.nn_time_sec:.3f}s ({100*best.nn_time_sec/total:.1f}%)")
        print(f"  Expand:  {best.expand_time_sec:.3f}s ({100*best.expand_time_sec/total:.1f}%)")
        print(f"  Advance: {best.advance_time_sec:.3f}s ({100*best.advance_time_sec/total:.1f}%)")

        # Write markdown report
        report_path = Path('/home/dkord/code/twilight-struggle-ai/results/analysis/mcts_throughput_matrix.md')
        report_path.parent.mkdir(parents=True, exist_ok=True)

        with open(report_path, 'w') as f:
            f.write("# MCTS Throughput Matrix Benchmark\n\n")
            f.write(f"**Timestamp**: {Path.cwd()}\n")
            f.write(f"**Model**: v106_cf_gnn_s42/baseline_best_scripted.pt\n")
            f.write(f"**Fixed params**: --games 32, --n-sim 200, --seed 77700, --temperature 1.0, --dir-alpha 0.3, --dir-epsilon 0.25\n\n")

            f.write("## Results (sorted by sims/s)\n\n")
            f.write("| MCTS Threads | Intra Threads | Interop Threads | Pool Size | Max Pending | Sims/s | Total Time (s) | Avg Batch | Select (s) | NN (s) | Expand (s) |\n")
            f.write("|---|---|---|---|---|---|---|---|---|---|---|\n")

            for r in sorted_results:
                f.write(f"| {r.mcts_threads} | {r.torch_intra_threads} | {r.torch_interop_threads} | "
                       f"{r.pool_size} | {r.max_pending} | {r.sims_per_sec:.1f} | {r.total_time_sec:.3f} | "
                       f"{r.avg_batch_size:.2f} | {r.select_time_sec:.3f} | {r.nn_time_sec:.3f} | {r.expand_time_sec:.3f} |\n")

            f.write("\n## Analysis\n\n")
            f.write(f"**Best Overall Config**: MCTS threads={best.mcts_threads}, Intra={best.torch_intra_threads}, "
                   f"Interop={best.torch_interop_threads}, Pool={best.pool_size}, Max-Pending={best.max_pending}\n")
            f.write(f"- **Throughput**: {best.sims_per_sec:.1f} sims/s\n")
            f.write(f"- **Latency**: {best.total_time_sec:.3f}s for {best.total_items} items\n")
            f.write(f"- **Avg Batch Size**: {best.avg_batch_size:.2f}\n\n")

            if constrained:
                f.write(f"**Best Config (≤4 MCTS threads)**: MCTS threads={best_constrained.mcts_threads}, "
                       f"Intra={best_constrained.torch_intra_threads}, Interop={best_constrained.torch_interop_threads}\n")
                f.write(f"- **Throughput**: {best_constrained.sims_per_sec:.1f} sims/s ({100*(best_constrained.sims_per_sec/best.sims_per_sec - 1):.1f}% vs best)\n\n")

            f.write("### Bottleneck Analysis\n\n")
            f.write("Breakdown of total time (from best overall config):\n\n")
            f.write(f"- **Select**: {best.select_time_sec:.3f}s ({100*best.select_time_sec/total:.1f}%)\n")
            f.write(f"- **NN**: {best.nn_time_sec:.3f}s ({100*best.nn_time_sec/total:.1f}%)\n")
            f.write(f"- **Expand**: {best.expand_time_sec:.3f}s ({100*best.expand_time_sec/total:.1f}%)\n")
            f.write(f"- **Advance**: {best.advance_time_sec:.3f}s ({100*best.advance_time_sec/total:.1f}%)\n\n")

            if best.nn_time_sec / total > 0.4:
                f.write("**Conclusion**: NN is the dominant bottleneck. Increase torch threads or batch size to hide latency.\n")
            elif best.select_time_sec / total > 0.3:
                f.write("**Conclusion**: Tree selection is dominant. Consider more MCTS threads or alternate traversal strategy.\n")
            else:
                f.write("**Conclusion**: Fairly balanced; no single bottleneck dominates.\n")

        print(f"\n✓ Report written to results/analysis/mcts_throughput_matrix.md")

if __name__ == '__main__':
    main()
