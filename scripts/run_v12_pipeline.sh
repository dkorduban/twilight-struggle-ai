#!/bin/bash
# v12 pipeline: wait for training, benchmark, collect v10-vs-heuristic, build combined_v13, train v13
# Runs at low priority. Logs to /tmp/pipeline_v12.log

set -euo pipefail
LOG=/tmp/pipeline_v12.log
exec >> "$LOG" 2>&1

cd /home/dkord/code/twilight-struggle-ai

echo "=== v12 pipeline started at $(date) ==="

# ── Step 1: wait for v12 training to finish ──────────────────────────────────
echo "[$(date)] Waiting for v12 training to finish (PID 17666)..."
TRAIN_PID=17666
while kill -0 "$TRAIN_PID" 2>/dev/null; do
    sleep 60
done
echo "[$(date)] v12 training done."

# Check best checkpoint exists
if [ ! -f data/checkpoints/retrain_v12/baseline_best.pt ]; then
    echo "ERROR: v12 checkpoint not found, aborting."
    exit 1
fi

# ── Step 2: benchmark v12 ────────────────────────────────────────────────────
echo "[$(date)] Running v12 benchmark..."
nice -n 10 uv run python scripts/benchmark_vf_mcts.py \
    --checkpoint data/checkpoints/retrain_v12/baseline_best.pt \
    --n-games 30 \
    --n-sim 50 \
    --seed 9999 \
    2>&1 | tee /tmp/benchmark_v12.log
echo "[$(date)] v12 benchmark done."

# ── Step 3: collect v10-vs-heuristic games (2000 games, if script exists) ────
V10_CKPT=data/checkpoints/retrain_v10/baseline_best.pt
VS_HEURISTIC_OUT=data/selfplay/learned_v10_vs_heuristic_2k_seed15000.parquet
VS_HEURISTIC_SCRIPT=scripts/collect_learned_vs_heuristic.py

if [ -f "$V10_CKPT" ] && [ -f "$VS_HEURISTIC_SCRIPT" ] && [ ! -f "$VS_HEURISTIC_OUT" ]; then
    echo "[$(date)] Starting v10-vs-heuristic collection..."
    nice -n 10 uv run python "$VS_HEURISTIC_SCRIPT" \
        --checkpoint "$V10_CKPT" \
        --n-games 2000 \
        --workers 14 \
        --batch-size 8 \
        --seed 15000 \
        --out "$VS_HEURISTIC_OUT" \
        2>&1 | tee /tmp/collect_v10_vs_heuristic.log
    echo "[$(date)] v10-vs-heuristic collection done."
else
    echo "[$(date)] Skipping v10-vs-heuristic (missing checkpoint or script or already done)."
fi

# Also try v12-vs-heuristic
V12_CKPT=data/checkpoints/retrain_v12/baseline_best.pt
V12_VS_HEURISTIC_OUT=data/selfplay/learned_v12_vs_heuristic_2k_seed16000.parquet

if [ -f "$V12_CKPT" ] && [ -f "$VS_HEURISTIC_SCRIPT" ] && [ ! -f "$V12_VS_HEURISTIC_OUT" ]; then
    echo "[$(date)] Starting v12-vs-heuristic collection..."
    nice -n 10 uv run python "$VS_HEURISTIC_SCRIPT" \
        --checkpoint "$V12_CKPT" \
        --n-games 2000 \
        --workers 14 \
        --batch-size 8 \
        --seed 16000 \
        --out "$V12_VS_HEURISTIC_OUT" \
        2>&1 | tee /tmp/collect_v12_vs_heuristic.log
    echo "[$(date)] v12-vs-heuristic collection done."
fi

# ── Step 4: build combined_v13 and train v13 ────────────────────────────────
COMBINED_V13=data/combined_v13
mkdir -p "$COMBINED_V13"

# Symlink all of combined_v12
for f in data/combined_v12/*.parquet; do
    fname=$(basename "$f")
    target=$(readlink -f "$f")
    ln -sf "$target" "$COMBINED_V13/$fname"
done

# Add vs-heuristic data if collected
for vs_file in "$VS_HEURISTIC_OUT" "$V12_VS_HEURISTIC_OUT"; do
    if [ -f "$vs_file" ]; then
        fname=$(basename "$vs_file")
        ln -sf "$(readlink -f "$vs_file")" "$COMBINED_V13/$fname"
        echo "[$(date)] Added to combined_v13: $fname"
    fi
done

FILE_COUNT=$(ls "$COMBINED_V13"/*.parquet 2>/dev/null | wc -l)
echo "[$(date)] combined_v13 assembled: $FILE_COUNT parquet files"

if [ "$FILE_COUNT" -gt 0 ]; then
    echo "[$(date)] Starting v13 training on combined_v13..."
    nice -n 10 uv run python scripts/train_baseline.py \
        --data-dir "$COMBINED_V13" \
        --out-dir data/checkpoints/retrain_v13 \
        --epochs 60 \
        --batch-size 256 \
        --lr 3e-4 \
        --weight-decay 1e-4 \
        --dropout 0.1 \
        --label-smoothing 0.05 \
        --value-target final_vp \
        --num-workers 2 \
        2>&1 | tee /tmp/train_v13.log
    echo "[$(date)] v13 training done."

    # Benchmark v13
    echo "[$(date)] Running v13 benchmark..."
    nice -n 10 uv run python scripts/benchmark_vf_mcts.py \
        --checkpoint data/checkpoints/retrain_v13/baseline_best.pt \
        --n-games 30 \
        --n-sim 50 \
        --seed 9999 \
        2>&1 | tee /tmp/benchmark_v13.log
    echo "[$(date)] v13 benchmark done."
fi

echo "=== v12 pipeline finished at $(date) ==="
