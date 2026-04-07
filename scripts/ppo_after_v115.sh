#!/usr/bin/env bash
# Wait for v115 training to finish, then:
#   1. Export + benchmark v115 via Snakemake
#   2. Start PPO training on v106 checkpoint
# Run in background: nohup bash scripts/ppo_after_v115.sh > results/ppo_pipeline.log 2>&1 &

set -e
REPO=$(cd "$(dirname "$0")/.." && pwd)
cd "$REPO"

LOG="results/ppo_pipeline.log"
V115_CKPT="data/checkpoints/v115_gnn_k1_s42/baseline_best.pt"
PPO_OUT="data/checkpoints/ppo_v1_from_v106"
PPO_CHECKPOINT="data/checkpoints/v106_cf_gnn_s42/baseline_best.pt"
SEED=99000

echo "[$(date '+%H:%M:%S')] PPO pipeline starting" | tee -a "$LOG"

# ── Step 1: Wait for v115 training to finish ─────────────────────────────────
echo "[$(date '+%H:%M:%S')] Waiting for v115 training to finish..." | tee -a "$LOG"
while true; do
    # Check if v115 training process is still running
    if ! pgrep -f "v115_gnn_k1_s42" > /dev/null 2>&1; then
        break
    fi
    sleep 30
done

# Verify checkpoint exists
if [ ! -f "$V115_CKPT" ]; then
    echo "[$(date '+%H:%M:%S')] ERROR: v115 checkpoint not found at $V115_CKPT" | tee -a "$LOG"
    exit 1
fi
echo "[$(date '+%H:%M:%S')] v115 training complete. Checkpoint: $V115_CKPT" | tee -a "$LOG"

# ── Step 2: Export + benchmark v115 ──────────────────────────────────────────
echo "[$(date '+%H:%M:%S')] Running Snakemake export+benchmark for v115_gnn_k1_s42..." | tee -a "$LOG"
uv run snakemake results/bench/v115_gnn_k1_s42.txt \
    -j4 --resources gpu=1 bench=1 \
    >> "$LOG" 2>&1 || {
    echo "[$(date '+%H:%M:%S')] WARNING: Snakemake failed, trying manual benchmark..." | tee -a "$LOG"
    # Manual fallback
    V115_SCRIPTED="data/checkpoints/v115_gnn_k1_s42/baseline_best_scripted.pt"
    if [ ! -f "$V115_SCRIPTED" ]; then
        uv run python cpp/tools/export_baseline_to_torchscript.py \
            --checkpoint "$V115_CKPT" --out "$V115_SCRIPTED" >> "$LOG" 2>&1
    fi
    BENCH_OUT="results/bench/v115_gnn_k1_s42.txt"
    mkdir -p results/bench
    uv run python -c "
import sys; sys.path.insert(0, 'build-ninja/bindings')
import tscore
model = '$V115_SCRIPTED'
n = 500
ur = tscore.benchmark_batched(model, tscore.Side.USSR, n, pool_size=32, seed=50000, nash_temperatures=True)
usr = tscore.benchmark_batched(model, tscore.Side.US, n, pool_size=32, seed=50500, nash_temperatures=True)
ussr_wr = sum(1 for r in ur if r.winner == tscore.Side.USSR) / n
us_wr = sum(1 for r in usr if r.winner == tscore.Side.US) / n
combined = (sum(1 for r in ur if r.winner == tscore.Side.USSR) + sum(1 for r in usr if r.winner == tscore.Side.US)) / (2*n)
print(f'USSR={ussr_wr:.3f} US={us_wr:.3f} combined={combined:.3f}')
" | tee "$BENCH_OUT" | tee -a "$LOG"
}

echo "[$(date '+%H:%M:%S')] v115 benchmark complete." | tee -a "$LOG"
cat results/bench/v115_gnn_k1_s42.txt >> "$LOG" 2>/dev/null || true

# ── Step 3: Check GPU is free before starting PPO ────────────────────────────
echo "[$(date '+%H:%M:%S')] Waiting for GPU to be free..." | tee -a "$LOG"
while true; do
    GPU_UTIL=$(nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader 2>/dev/null | tr -d ' %')
    if [ "${GPU_UTIL:-100}" -lt 20 ]; then
        break
    fi
    echo "[$(date '+%H:%M:%S')] GPU at ${GPU_UTIL}%, waiting..." | tee -a "$LOG"
    sleep 30
done

# ── Step 4: Start PPO training ────────────────────────────────────────────────
echo "[$(date '+%H:%M:%S')] Starting PPO training from $PPO_CHECKPOINT..." | tee -a "$LOG"
echo "[$(date '+%H:%M:%S')] Output: $PPO_OUT" | tee -a "$LOG"

mkdir -p "$PPO_OUT"

uv run python scripts/train_ppo.py \
    --checkpoint "$PPO_CHECKPOINT" \
    --out-dir "$PPO_OUT" \
    --n-iterations 200 \
    --games-per-iter 200 \
    --ppo-epochs 4 \
    --clip-eps 0.2 \
    --lr 1e-4 \
    --gamma 0.99 \
    --gae-lambda 0.95 \
    --ent-coef 0.01 \
    --vf-coef 0.5 \
    --minibatch-size 2048 \
    --benchmark-every 20 \
    --side both \
    --seed "$SEED" \
    --device cuda \
    --wandb \
    2>&1 | tee -a "$LOG"

echo "[$(date '+%H:%M:%S')] PPO pipeline complete." | tee -a "$LOG"
