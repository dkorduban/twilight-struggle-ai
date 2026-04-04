#!/bin/bash
# Nash-C hypothesis test: does nash_c data alone perform like nash_b?
# If yes → 2x failure is from mixing. If no → nash_c data is inherently worse.
#
# Experiments:
#   1. nash_c_95ep_s42  — nash_c only, seed 42 (compare to v99_saturation_1x_95ep = nash_b s42)
#   2. nash_c_95ep_s7   — nash_c only, seed 7  (seed variance)
#   3. nash_b_95ep_s7   — nash_b only, seed 7  (matching seed for nash_b baseline)
#
# Expected runtime: ~15 min training + ~10 min benchmark per run = ~75 min total
set -e
cd "$(dirname "$0")/.."

# --- Memory check ---
FREE_MB=$(free -m | awk 'NR==2{print $4}')
if [ "$FREE_MB" -lt 4000 ]; then
    echo "ERROR: Only ${FREE_MB}MB free. Need 4GB minimum. Aborting."
    exit 1
fi

# --- Lock ---
LOCK_FILE="results/sweep.lock"
if [ -f "$LOCK_FILE" ]; then
    OLD_PID=$(grep -oP 'PID=\K\d+' "$LOCK_FILE" 2>/dev/null || true)
    if [ -n "$OLD_PID" ] && kill -0 "$OLD_PID" 2>/dev/null; then
        echo "ERROR: Another sweep is running (PID=$OLD_PID). Aborting."
        exit 1
    fi
    echo "WARN: Stale lock from PID=$OLD_PID, removing."
    rm -f "$LOCK_FILE"
fi
echo "PID=$$ started=$(date '+%Y-%m-%d %H:%M:%S')" > "$LOCK_FILE"
trap 'rm -f "$LOCK_FILE"' EXIT

COMMON_ARGS="--epochs 95 --batch-size 1024 --lr 0.0012 --weight-decay 1e-4 \
  --label-smoothing 0.05 --one-cycle --hidden-dim 256 \
  --value-target final_vp --patience 20"

echo "=== Nash-C Hypothesis Test ==="
echo "Started: $(date '+%Y-%m-%d %H:%M:%S')"

# --- Prepare single-file data dirs (symlinks) ---
mkdir -p data/nash_c_only data/nash_b_only
ln -sf "$(pwd)/data/combined_v99_clean/heuristic_nash_c.parquet" data/nash_c_only/heuristic_nash_c.parquet
ln -sf "$(pwd)/data/combined_v99_clean/heuristic_nash_b.parquet" data/nash_b_only/heuristic_nash_b.parquet

# --- Run 1: nash_c, seed 42 ---
echo ""
echo "=== [1/3] nash_c_95ep_s42 ==="
uv run python scripts/train_baseline.py \
  --data-dir data/nash_c_only \
  --out-dir data/checkpoints/v99_nash_c_95ep_s42 \
  --seed 42  \
  $COMMON_ARGS 2>&1 | tail -5

# --- Run 2: nash_c, seed 7 ---
echo ""
echo "=== [2/3] nash_c_95ep_s7 ==="
uv run python scripts/train_baseline.py \
  --data-dir data/nash_c_only \
  --out-dir data/checkpoints/v99_nash_c_95ep_s7 \
  --seed 7  \
  $COMMON_ARGS 2>&1 | tail -5

# --- Run 3: nash_b, seed 7 ---
echo ""
echo "=== [3/3] nash_b_95ep_s7 ==="
uv run python scripts/train_baseline.py \
  --data-dir data/nash_b_only \
  --out-dir data/checkpoints/v99_nash_b_95ep_s7 \
  --seed 7  \
  $COMMON_ARGS 2>&1 | tail -5

# --- Export all ---
echo ""
echo "=== Exporting ==="
for dir in v99_nash_c_95ep_s42 v99_nash_c_95ep_s7 v99_nash_b_95ep_s7; do
  uv run python cpp/tools/export_baseline_to_torchscript.py \
    --checkpoint "data/checkpoints/$dir/baseline_best.pt" \
    --out "data/checkpoints/$dir/baseline_best_scripted.pt" 2>&1
  echo "exported $dir"
done

# --- Benchmark all ---
echo ""
echo "=== Benchmarking ==="
PYTHONPATH=build-ninja/bindings uv run python -c "
import tscore, math

models = {
    'v99_nash_c_95ep_s42': 'data/checkpoints/v99_nash_c_95ep_s42/baseline_best_scripted.pt',
    'v99_nash_c_95ep_s7':  'data/checkpoints/v99_nash_c_95ep_s7/baseline_best_scripted.pt',
    'v99_nash_b_95ep_s7':  'data/checkpoints/v99_nash_b_95ep_s7/baseline_best_scripted.pt',
}

n = 2000
for name, path in models.items():
    ussr = tscore.benchmark_batched(path, tscore.Side.USSR, n, pool_size=32, seed=9000)
    us   = tscore.benchmark_batched(path, tscore.Side.US,   n, pool_size=32, seed=9000+n)
    uw = sum(1 for r in ussr if r.winner == tscore.Side.USSR)
    sw = sum(1 for r in us   if r.winner == tscore.Side.US)
    up = uw/n*100; sp = sw/n*100; cp = (uw+sw)/(2*n)*100
    use = math.sqrt(up/100*(1-up/100)/n)*100
    sse = math.sqrt(sp/100*(1-sp/100)/n)*100
    cse = math.sqrt((up/100*(1-up/100)+sp/100*(1-sp/100))/(4*n))*100
    print(f'{name} | USSR {up:.1f}% +/-{use:.1f} | US {sp:.1f}% +/-{sse:.1f} | Combined {cp:.1f}% +/-{cse:.1f}')
" 2>&1

echo ""
echo "=== Reference baselines ==="
echo "v99_saturation_1x_95ep (nash_b, s42) | USSR 46.2% +/-1.1 | US 13.0% +/-0.8 | Combined 29.5% +/-0.7"
echo "v99_saturation_2x_47ep (nash_b+c, s42) | USSR 42.1% +/-1.1 | US 11.6% +/-0.7 | Combined 26.9% +/-0.7"
echo "v99_baseline_2x95ep (nash_b+c, s42) | USSR 36.0% +/-1.1 | US 9.0% +/-0.6 | Combined 22.5% +/-0.6"

echo ""
echo "Finished: $(date '+%Y-%m-%d %H:%M:%S')"
