#!/bin/bash
# v13 pipeline: wait for training → benchmark → collect v13-vs-heuristic → build combined_v14 → train v14
set -euo pipefail
LOG=/tmp/pipeline_v13.log
exec >> "$LOG" 2>&1

cd /home/dkord/code/twilight-struggle-ai

echo "=== v13 pipeline started at $(date) ==="

TRAIN_PID="${1:-}"
if [ -n "$TRAIN_PID" ]; then
    echo "[$(date)] Waiting for v13 training to finish (PID $TRAIN_PID)..."
    while kill -0 "$TRAIN_PID" 2>/dev/null; do sleep 60; done
    echo "[$(date)] v13 training done."
fi

V13_CKPT=data/checkpoints/retrain_v13/baseline_best.pt
if [ ! -f "$V13_CKPT" ]; then echo "ERROR: v13 checkpoint not found"; exit 1; fi

# ── Benchmark v13 ────────────────────────────────────────────────────────────
echo "[$(date)] Running v13 benchmark..."
nice -n 10 uv run python scripts/benchmark_vf_mcts.py \
    --checkpoint "$V13_CKPT" \
    --n-games 30 --n-sim 50 --n-candidates 8 --seed 9999 \
    2>&1 | tee /tmp/benchmark_v13.log
echo "[$(date)] v13 benchmark done."

# ── Collect v13-vs-heuristic (seed17000) ─────────────────────────────────────
VS_HEURISTIC_SCRIPT=scripts/collect_learned_vs_heuristic.py
V13_VS_HEU_OUT=data/selfplay/learned_v13_vs_heuristic_2k_seed17000.parquet

if [ -f "$VS_HEURISTIC_SCRIPT" ] && [ ! -f "$V13_VS_HEU_OUT" ]; then
    echo "[$(date)] Collecting v13-vs-heuristic..."
    nice -n 10 uv run python "$VS_HEURISTIC_SCRIPT" \
        --checkpoint "$V13_CKPT" --n-games 2000 --pool-size 256 \
        --seed 17000 --out "$V13_VS_HEU_OUT" \
        2>&1 | tee /tmp/collect_v13_vs_heuristic.log
    echo "[$(date)] v13-vs-heuristic collection done."
fi

# ── Build combined_v14 ───────────────────────────────────────────────────────
COMBINED_V14=data/combined_v14
mkdir -p "$COMBINED_V14"
for f in data/combined_v13/*.parquet; do
    ln -sf "$(readlink -f "$f")" "$COMBINED_V14/$(basename "$f")"
done
if [ -f "$V13_VS_HEU_OUT" ]; then
    ln -sf "$(readlink -f "$V13_VS_HEU_OUT")" "$COMBINED_V14/$(basename "$V13_VS_HEU_OUT")"
fi
FILE_COUNT=$(ls "$COMBINED_V14"/*.parquet 2>/dev/null | wc -l)
echo "[$(date)] combined_v14 assembled: $FILE_COUNT files"

# ── Train v14 ────────────────────────────────────────────────────────────────
echo "[$(date)] Starting v14 training on combined_v14..."
nice -n 10 uv run python scripts/train_baseline.py \
    --data-dir "$COMBINED_V14" \
    --out-dir data/checkpoints/retrain_v14 \
    --epochs 60 --batch-size 1024 --lr 1.2e-3 \
    --weight-decay 1e-4 --dropout 0.1 --label-smoothing 0.05 \
    --value-target final_vp --num-workers 4 --one-cycle --pin-memory \
    2>&1 | tee /tmp/train_v14.log
echo "[$(date)] v14 training done."

# ── Benchmark v14 ────────────────────────────────────────────────────────────
V14_CKPT=data/checkpoints/retrain_v14/baseline_best.pt
if [ -f "$V14_CKPT" ]; then
    echo "[$(date)] Running v14 benchmark..."
    nice -n 10 uv run python scripts/benchmark_vf_mcts.py \
        --checkpoint "$V14_CKPT" \
        --n-games 30 --n-sim 50 --n-candidates 8 --seed 9999 --pool-size 30 \
        2>&1 | tee /tmp/benchmark_v14.log
    echo "[$(date)] v14 benchmark done."
fi

echo "=== v13 pipeline finished at $(date) ==="
