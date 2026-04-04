#!/bin/bash
# Clean baseline sweep on post-DEFCON-fix data (no contaminated nash).
# Uses deterministic train/val split and samples_seen W&B axis.
#
# All runs target ~121M total samples seen (= arch sweep reference):
#   - 2× data (2.58M train): 47 epochs → 121.1M samples
#   - 1× data (1.28M train): 95 epochs → 121.4M samples
#
# Groups:
#   1. baseline h256 ×3 seeds on 2× data
#   2. Saturation test: 1×@95ep vs 2×@47ep (same ~121M samples)
#   3. control_feat h256 ×2 seeds on 2× data
#
# Benchmark pipeline runs in parallel: ./scripts/bench_pipeline.sh
cd "$(dirname "$0")/.."

DATA_2X="data/combined_v99_clean"
DATA_1X="data/combined_v99_clean_b"
QUEUE_FILE="results/pipeline_queue.txt"
EPOCHS_2X=47; PATIENCE_2X=12
EPOCHS_1X=95; PATIENCE_1X=20

log() { echo "[$(date '+%H:%M:%S')] $*"; }

train_and_queue() {
    local dir=$1; local model_type=$2; local hdim=$3; local seed=$4; shift 4
    log "=== Training $dir ==="
    if nice -n 10 uv run python scripts/train_baseline.py \
        --out-dir "data/checkpoints/$dir" \
        --lr 0.0024 --batch-size 8192 \
        --label-smoothing 0.05 --weight-decay 1e-4 --one-cycle \
        --hidden-dim "$hdim" --value-target final_vp --dropout 0.1 \
        --model-type "$model_type" --seed "$seed" --deterministic-split \
        "$@"; then
        log "Training done: $dir — exporting..."
        if nice -n 10 uv run python cpp/tools/export_baseline_to_torchscript.py \
            --checkpoint "data/checkpoints/$dir/baseline_best.pt" \
            --out "data/checkpoints/$dir/baseline_best_scripted.pt"; then
            echo "data/checkpoints/$dir/baseline_best_scripted.pt" >> "$QUEUE_FILE"
            log "Queued: $dir"
        else
            log "WARNING: export failed for $dir"
        fi
    else
        log "WARNING: training failed for $dir — skipping"
    fi
}

mkdir -p results
# Append to existing queue (don't wipe — s42 result already there)

log "=== Clean baseline sweep (resuming from s7) ==="
log "2× data: $DATA_2X ($EPOCHS_2X epochs), 1× data: $DATA_1X ($EPOCHS_1X epochs)"

# Queue s123 scripted model (already trained)
if [ -f "data/checkpoints/v99_baseline_h256_s123/baseline_best_scripted.pt" ]; then
    echo "data/checkpoints/v99_baseline_h256_s123/baseline_best_scripted.pt" >> "$QUEUE_FILE"
    log "Re-queued s123 (already trained)"
fi

# --- Group 1 continued ---
train_and_queue v99_baseline_h256_s7 baseline 256 7 --data-dir "$DATA_2X" --epochs $EPOCHS_2X --patience $PATIENCE_2X

# --- Group 2: saturation test ---
train_and_queue v99_saturation_1x_95ep baseline 256 42 --data-dir "$DATA_1X" --epochs $EPOCHS_1X --patience $PATIENCE_1X
train_and_queue v99_saturation_2x_47ep baseline 256 42 --data-dir "$DATA_2X" --epochs $EPOCHS_2X --patience $PATIENCE_2X

# --- Group 3: best arch ---
train_and_queue v99_control_feat_h256_s42  control_feat 256 42  --data-dir "$DATA_2X" --epochs $EPOCHS_2X --patience $PATIENCE_2X
train_and_queue v99_control_feat_h256_s123 control_feat 256 123 --data-dir "$DATA_2X" --epochs $EPOCHS_2X --patience $PATIENCE_2X

echo "DONE" >> "$QUEUE_FILE"
log "=== All training complete ==="
