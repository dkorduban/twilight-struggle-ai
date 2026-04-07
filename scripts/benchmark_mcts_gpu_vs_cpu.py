#!/usr/bin/env python3
"""
GPU vs CPU MCTS inference benchmarks under training load.

Protocol:
- 6 configs: CPU(2,4 threads), GPU(1,2 threads), CPU+GPU with larger pool
- Each config: warmup run + measured run (32 games, 200 sims, seed=77700)
- Parse stderr for MCTS profile (sims/s breakdown)
- Record wall-clock time and outcome
- Write results to results/mcts_gpu_vs_cpu.md
"""

import sys
import time
import re
from pathlib import Path
from io import StringIO
import traceback

# Add bindings to path
sys.path.insert(0, str(Path(__file__).parent.parent / "build-ninja" / "bindings"))

try:
    import tscore
except ImportError as e:
    print(f"ERROR: Could not import tscore bindings: {e}")
    print("Make sure build-ninja/bindings exists and is built.")
    sys.exit(1)

# Find a checkpoint to use
CHECKPOINT_ROOT = Path(__file__).parent.parent / "data" / "checkpoints"
MODEL_PATH = None

# Try to find v106_cf_gnn_s42 first, then fallback to any v106
candidates = [
    CHECKPOINT_ROOT / "v106_cf_gnn_s42" / "baseline_best_scripted.pt",
    CHECKPOINT_ROOT / "v106_cf_gnn_s999" / "baseline_best_scripted.pt",
    CHECKPOINT_ROOT / "v106_cf_gnn_s123" / "baseline_best_scripted.pt",
]

for cand in candidates:
    if cand.exists():
        MODEL_PATH = str(cand)
        print(f"Using checkpoint: {cand.name}")
        break

if not MODEL_PATH:
    print(f"ERROR: No checkpoint found. Candidates checked: {[str(c) for c in candidates]}")
    sys.exit(1)

# Benchmark configs: (device, torch_intra_threads, pool_size, n_mcts_threads)
CONFIGS = [
    ("cpu", 2, 32, 4),
    ("cpu", 4, 32, 4),
    ("cuda", 1, 32, 4),
    ("cuda", 2, 32, 4),
    ("cpu", 4, 64, 4),
    ("cuda", 1, 64, 4),
]

BENCHMARK_PARAMS = {
    "n_games": 32,
    "n_simulations": 200,
    "seed": 77700,
    "greedy_nn_opponent": False,
    "nash_temperatures": True,
    "torch_interop_threads": 1,
}

results = []

print("Starting MCTS GPU vs CPU benchmarks under training load...")
print(f"Model: {MODEL_PATH}")
print(f"Params: {BENCHMARK_PARAMS}")
print()

for device, torch_intra, pool_size, n_mcts_threads in CONFIGS:
    config_name = f"{device}(intra={torch_intra}, pool={pool_size}, mcts={n_mcts_threads})"
    print(f"\n{'='*70}")
    print(f"Config: {config_name}")
    print(f"{'='*70}")

    try:
        # Warmup run
        print("Warmup run...")
        warmup_start = time.time()
        warmup_results = tscore.benchmark_mcts(
            MODEL_PATH,
            tscore.Side.US,
            BENCHMARK_PARAMS["n_games"],
            n_simulations=BENCHMARK_PARAMS["n_simulations"],
            pool_size=pool_size,
            seed=BENCHMARK_PARAMS["seed"],
            device=device,
            greedy_nn_opponent=BENCHMARK_PARAMS["greedy_nn_opponent"],
            nash_temperatures=BENCHMARK_PARAMS["nash_temperatures"],
            n_mcts_threads=n_mcts_threads,
            torch_intra_threads=torch_intra,
            torch_interop_threads=BENCHMARK_PARAMS["torch_interop_threads"],
        )
        warmup_time = time.time() - warmup_start
        print(f"Warmup completed in {warmup_time:.2f}s")

        # Measured run
        print("Measured run...")
        measured_start = time.time()
        measured_results = tscore.benchmark_mcts(
            MODEL_PATH,
            tscore.Side.US,
            BENCHMARK_PARAMS["n_games"],
            n_simulations=BENCHMARK_PARAMS["n_simulations"],
            pool_size=pool_size,
            seed=BENCHMARK_PARAMS["seed"],
            device=device,
            greedy_nn_opponent=BENCHMARK_PARAMS["greedy_nn_opponent"],
            nash_temperatures=BENCHMARK_PARAMS["nash_temperatures"],
            n_mcts_threads=n_mcts_threads,
            torch_intra_threads=torch_intra,
            torch_interop_threads=BENCHMARK_PARAMS["torch_interop_threads"],
        )
        measured_time = time.time() - measured_start
        print(f"Measured run completed in {measured_time:.2f}s")

        # Estimate sims/s (200 sims * 32 games)
        total_sims = BENCHMARK_PARAMS["n_simulations"] * BENCHMARK_PARAMS["n_games"]
        sims_per_sec = total_sims / measured_time if measured_time > 0 else 0

        results.append({
            "device": device,
            "torch_intra_threads": torch_intra,
            "pool_size": pool_size,
            "n_mcts_threads": n_mcts_threads,
            "wall_time_sec": measured_time,
            "sims_per_sec": sims_per_sec,
            "status": "OK",
            "note": f"{sims_per_sec:.0f} sims/s",
        })

        print(f"Result: {measured_time:.2f}s, {sims_per_sec:.0f} sims/s")

    except Exception as e:
        error_msg = str(e)
        is_oom = "OOM" in error_msg or "CUDA" in error_msg or "out of memory" in error_msg
        status = "OOM/CRASH" if is_oom else "ERROR"

        results.append({
            "device": device,
            "torch_intra_threads": torch_intra,
            "pool_size": pool_size,
            "n_mcts_threads": n_mcts_threads,
            "wall_time_sec": None,
            "sims_per_sec": None,
            "status": status,
            "note": error_msg[:100],
        })

        print(f"FAILED: {status}")
        print(f"Error: {error_msg}")
        traceback.print_exc()

# Write results
output_path = Path(__file__).parent.parent / "results" / "mcts_gpu_vs_cpu.md"
output_path.parent.mkdir(parents=True, exist_ok=True)

report = "# GPU vs CPU MCTS Inference Benchmarks\n\n"
report += f"**Date**: {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
report += f"**Model**: {MODEL_PATH}\n"
report += f"**Setup**: RTX 3050 4GB, training running (~88% util), 32 games, 200 sims/game\n\n"

report += "## Results Table\n\n"
report += "| Device | Intra Threads | Pool Size | MCTS Threads | Wall Time (s) | Sims/sec | Status | Note |\n"
report += "|--------|---------------|-----------|--------------|---------------|----------|--------|------|\n"

for r in results:
    wall_time = f"{r['wall_time_sec']:.2f}" if r['wall_time_sec'] is not None else "N/A"
    sims_sec = f"{r['sims_per_sec']:.0f}" if r['sims_per_sec'] is not None else "N/A"
    report += f"| {r['device']} | {r['torch_intra_threads']} | {r['pool_size']} | {r['n_mcts_threads']} | {wall_time} | {sims_sec} | {r['status']} | {r['note']} |\n"

report += "\n## Analysis\n\n"

# Find successful runs and compare
successful = [r for r in results if r['status'] == 'OK']

if successful:
    cpu_runs = [r for r in successful if r['device'] == 'cpu']
    gpu_runs = [r for r in successful if r['device'] == 'cuda']

    if cpu_runs and gpu_runs:
        best_cpu = max(cpu_runs, key=lambda x: x['sims_per_sec'])
        best_gpu = max(gpu_runs, key=lambda x: x['sims_per_sec'])
        speedup = best_gpu['sims_per_sec'] / best_cpu['sims_per_sec']

        report += f"**Best CPU config**: {best_cpu['torch_intra_threads']} intra threads, pool={best_cpu['pool_size']} → {best_cpu['sims_per_sec']:.0f} sims/s\n"
        report += f"**Best GPU config**: {best_gpu['torch_intra_threads']} intra threads, pool={best_gpu['pool_size']} → {best_gpu['sims_per_sec']:.0f} sims/s\n"
        report += f"**Speedup**: {speedup:.2f}x\n\n"

        if speedup > 1.1:
            report += "### Recommendation\n"
            report += "**GPU inference helps under training load.** Use GPU for MCTS inference in production.\n"
        elif speedup < 0.9:
            report += "### Recommendation\n"
            report += "**GPU inference does not help under training load.** Use CPU for MCTS inference to avoid contention.\n"
        else:
            report += "### Recommendation\n"
            report += "**GPU and CPU are comparable.** Either works; prefer CPU to avoid training contention.\n"
    else:
        report += "Could not compare GPU vs CPU (one or both failed).\n"

else:
    report += "No successful runs to analyze.\n"

report += "\n## Detailed Results\n\n"
for r in results:
    report += f"### {r['device'].upper()} (intra={r['torch_intra_threads']}, pool={r['pool_size']})\n"
    if r['status'] == 'OK':
        report += f"- Wall time: {r['wall_time_sec']:.2f}s\n"
        report += f"- Sims/sec: {r['sims_per_sec']:.0f}\n"
    else:
        report += f"- Status: {r['status']}\n"
        report += f"- Error: {r['note']}\n"
    report += "\n"

with open(output_path, 'w') as f:
    f.write(report)

print("\n" + "="*70)
print(f"Results written to: {output_path}")
print("="*70)
