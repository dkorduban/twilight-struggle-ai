#!/usr/bin/env bash
# Run Phase 4 architecture sweep sequentially (one run at a time, full GPU).
# Avoids GPU contention between runs.
set -euo pipefail

DATA_05M="data/v3_selfplay_05M_v2"   # dual-callback data; 516k rows, 4500 games
DATA_1M="data/v3_selfplay_1M_v2"    # not yet collected
EXCLUDE_05M="$DATA_05M/EXCLUDE_GAME_IDS.txt"  # proxy-eval game_ids — never in train/val
OUT_BASE="data/checkpoints/phase4"
LOG_BASE="results/logs/phase4"
mkdir -p "$OUT_BASE" "$LOG_BASE"

EPOCHS=60
PATIENCE=15
BS=8192
LR=0.0024
HIDDEN=256
DROPOUT=0.1
WD=1e-4
LABEL_SM=0.05

run_one() {
  local MODEL_TYPE=$1
  local SEED=$2
  local DATA_DIR=$3
  local TIER_LABEL=$4
  local EXCLUDE_FILE=$5
  local TAG="${MODEL_TYPE}_s${SEED}_${TIER_LABEL}"
  local CKPT_DIR="$OUT_BASE/$TAG"
  local LOG="$LOG_BASE/${TAG}.log"
  mkdir -p "$CKPT_DIR"

  # Skip if already done
  if [ -f "$CKPT_DIR/baseline_best.pt" ] && grep -q "Training complete" "$LOG" 2>/dev/null; then
    echo "  [SKIP] $TAG already done"
    return 0
  fi

  echo "  Training $TAG..."
  local EXCLUDE_ARG=""
  if [ -f "$EXCLUDE_FILE" ]; then
    EXCLUDE_ARG="--exclude-game-ids $EXCLUDE_FILE"
  fi

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
    $EXCLUDE_ARG \
    --num-workers 4 \
    2>&1 | tee "$LOG"

  echo "  Done: $TAG"
}

echo "=== Phase 4 Sequential Sweep ==="
echo ""

# Round 1: 0.5M tier — GNN first (fast: ~15 min each)
echo "--- GNN-side 0.5M tier ---"
run_one "control_feat_gnn_side" 7   "$DATA_05M" "05M" "$EXCLUDE_05M"
run_one "control_feat_gnn_side" 123 "$DATA_05M" "05M" "$EXCLUDE_05M"

# Round 1: 0.5M tier — Attn (slower: ~60 min each)
echo "--- Attn-side 0.5M tier ---"
run_one "country_attn_side" 7   "$DATA_05M" "05M" "$EXCLUDE_05M"
run_one "country_attn_side" 42  "$DATA_05M" "05M" "$EXCLUDE_05M"
run_one "country_attn_side" 123 "$DATA_05M" "05M" "$EXCLUDE_05M"

echo ""
echo "=== Phase 4 Round 1 complete ==="
echo "Results in: $LOG_BASE"

# Print summary
echo ""
echo "Best val_loss per run:"
for log in "$LOG_BASE"/*_05M.log; do
  tag=$(basename "$log" .log)
  best=$(grep "Training complete" "$log" 2>/dev/null | grep -oP "val_loss=\K[\d.]+" | tail -1)
  card=$(grep "\[BEST\]" "$log" 2>/dev/null | grep -oP "val_card_top1=\K[\d.]+" | tail -1)
  echo "  $tag: best_val_loss=${best:-?} card_top1=${card:-?}"
done
