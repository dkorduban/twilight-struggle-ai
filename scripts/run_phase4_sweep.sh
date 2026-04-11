#!/usr/bin/env bash
# Phase 4 Architecture Sweep: GNN-side vs Attn-side with data scaling.
# Usage: bash scripts/run_phase4_sweep.sh [tier]
# tier: 05M (default), 1M, 2M, 4M, 8M
#
# Round 1: 0.5M (v3 self-play only: 4 parquet files from v3_best 4000 games)
# Round 2: 1M  (+ v3 vs league iter_0100 4000 games)
# Round 3+: conditional on Round 2 gap

set -euo pipefail

TIER="${1:-05M}"
BASE_DATA="data/v3_selfplay"
OUT_DIR="data/checkpoints/phase4"
LOG_DIR="results/phase4_logs"
mkdir -p "$OUT_DIR" "$LOG_DIR"

# Common hyperparams (plan §Phase 4)
EPOCHS=60
PATIENCE=15
BS=8192
LR=0.0024
HIDDEN=256
DROPOUT=0.1
WD=1e-4
LABEL_SM=0.05

# Data files per tier
case "$TIER" in
  05M)
    # ~520k rows from v3_best 4000 games (both sides)
    DATA_DIR="$BASE_DATA"
    DATA_GLOB="v3_*g_s*.parquet"
    TIER_LABEL="0.5M"
    ;;
  1M)
    # ~1.04M rows: v3_best + league_iter100
    DATA_DIR="$BASE_DATA"
    DATA_GLOB="*.parquet"
    TIER_LABEL="1M"
    ;;
  *)
    echo "Unknown tier: $TIER (supported: 05M, 1M)"
    exit 1
    ;;
esac

echo "=== Phase 4 Architecture Sweep: $TIER_LABEL tier ==="
echo "Data: $DATA_DIR/$DATA_GLOB"
echo "Out: $OUT_DIR"
echo ""

run_one() {
  local MODEL_TYPE=$1
  local SEED=$2
  local TAG="${MODEL_TYPE}_s${SEED}_${TIER}"
  local CKPT_DIR="$OUT_DIR/$TAG"
  mkdir -p "$CKPT_DIR"
  local LOG="$LOG_DIR/${TAG}.log"

  echo "  Training $TAG..."
  uv run python scripts/train_baseline.py \
    --data-dir "$DATA_DIR" \
    --out-dir "$CKPT_DIR" \
    --model-type "$MODEL_TYPE" \
    --epochs $EPOCHS \
    --patience $PATIENCE \
    --batch-size $BS \
    --lr $LR \
    --hidden-dim $HIDDEN \
    --dropout $DROPOUT \
    --weight-decay $WD \
    --label-smoothing $LABEL_SM \
    --one-cycle \
    --seed $SEED \
    --value-target final_vp \
    --deterministic-split \
    --num-workers 4 \
    2>&1 | tee "$LOG"

  echo "  Done: $TAG → $CKPT_DIR/best.pt"
}

# GNN-side × 3 seeds, then Attn-side × 3 seeds
for SEED in 7 42 123; do
  run_one "control_feat_gnn_side" $SEED
done

for SEED in 7 42 123; do
  run_one "country_attn_side" $SEED
done

echo ""
echo "=== Summary ==="
echo "Checkpoints written to: $OUT_DIR"
echo "Logs written to: $LOG_DIR"
echo ""
echo "To compare val_loss and card_top1, run:"
echo "  grep -h 'best val\|card_top1' $LOG_DIR/*_${TIER}.log"
