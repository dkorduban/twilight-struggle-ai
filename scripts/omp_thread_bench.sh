#!/bin/bash
# OMP thread-count micro-benchmark for TS inference throughput.
# Runs benchmark_batched at N=2,4,6,8,10 threads and finds the knee.
# Must be run when CPU is otherwise idle (no PPO, no Elo tournament).
# Results written to results/analysis/omp_thread_bench_TIMESTAMP.txt

set -euo pipefail
cd "$(dirname "$0")/.."

OUTFILE="results/analysis/omp_thread_bench_$(date -u +%Y%m%d_%H%M%S).txt"
SCRIPT="data/checkpoints/scripted_for_elo/v56_scripted.pt"
N_GAMES=200   # enough for stable timing, not too long
SEED=12345

echo "OMP thread bench — $(date -u)" | tee "$OUTFILE"
echo "Model: $SCRIPT  n_games=$N_GAMES  seed=$SEED" | tee -a "$OUTFILE"
echo "" | tee -a "$OUTFILE"

for N in 1 2 4 6 8 10; do
    echo -n "threads=$N: " | tee -a "$OUTFILE"
    T_START=$(date +%s%3N)
    OMP_NUM_THREADS=$N MKL_NUM_THREADS=$N OMP_WAIT_POLICY=passive KMP_BLOCKTIME=0 \
        uv run python - <<PYEOF 2>/dev/null
import sys, time
sys.path.insert(0, "build-ninja/bindings")
import torch
torch.set_num_threads($N)
import tscore
model = torch.jit.load("$SCRIPT")
model.eval()
# Warmup
tscore.benchmark_batched(model, tscore.Side.USSR, 20, seed=0)
# Timed run
t0 = time.perf_counter()
r = tscore.benchmark_batched(model, tscore.Side.USSR, $N_GAMES, seed=$SEED)
t1 = time.perf_counter()
elapsed = t1 - t0
games_per_sec = $N_GAMES / elapsed
print(f"{games_per_sec:.1f} games/s  ({elapsed:.2f}s total)")
PYEOF
done | tee -a "$OUTFILE"

echo "" | tee -a "$OUTFILE"
echo "Saved to $OUTFILE"
