#!/bin/bash
# BC-on-fixed-engine (#109): retrain v32-architecture on heuristic-vs-heuristic
# data collected against post-Plan-B engine (abe69f3 + fb9e814 Camp David).
#
# Rationale: v32 combined dropped 0.650 -> 0.483 on fixed engine, asymmetric
# (US: -0.228, USSR: -0.105). PPO-continue at lr=3e-6 (#110) didn't move policy.
# BC from fresh heuristic data teaches the policy the new engine dynamics.
#
# Usage: bash scripts/bc_v32_fixed_engine.sh
set -e

DATA_DIR="data/heuristic_postplanb"
OUT_DIR="results/bc_v32_fixed_engine"
WARMSTART_CKPT="results/ppo_v32_continue/ppo_best.pt"

# Wait for collection to finish if still running
while pgrep -f collect_heuristic_selfplay > /dev/null; do
    echo "[$(date -u)] waiting for collection to finish..."
    sleep 60
done

if [ ! -f "$DATA_DIR/heuristic_5k.parquet" ]; then
    echo "ERROR: $DATA_DIR/heuristic_5k.parquet not found"
    exit 1
fi

mkdir -p "$OUT_DIR"

echo "[$(date -u)] Launching BC-on-fixed-engine from v32 warmstart"

PYTHONPATH=build-ninja/bindings nice -n 10 uv run python scripts/train_baseline.py \
    --data-dir "$DATA_DIR" \
    --out-dir "$OUT_DIR" \
    --init-from "$WARMSTART_CKPT" \
    --model-type country_attn_side \
    --num-strategies 4 \
    --epochs 30 \
    --batch-size 1024 \
    --lr 1e-4 \
    --weight-decay 1e-4 \
    --label-smoothing 0.05 \
    --one-cycle \
    --hidden-dim 256 \
    --deterministic-split \
    --val-fraction 0.1 \
    --num-workers 4 \
    --seed 20260421 \
    2>&1 | tee "$OUT_DIR/train.log"

echo "[$(date -u)] BC done. Bench next."
