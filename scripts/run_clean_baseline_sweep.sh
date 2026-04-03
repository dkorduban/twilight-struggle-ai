#!/bin/bash
# Clean baseline sweep on post-DEFCON-fix data (no contaminated nash).
# Uses deterministic train/val split and samples_seen W&B axis.
#
# IMPORTANT: All runs target ~121M total samples seen, matching the arch sweep
# (combined_v89 2.02M train × 60 epochs). This ensures fair comparison.
#   - 2× data (2.58M train): 47 epochs → 121.1M samples
#   - 1× data (1.28M train): 95 epochs → 121.4M samples
#
# Groups:
#   1. baseline h256 ×3 seeds on 2× data — seed variance on clean data
#   2. Fair saturation test: 1×@95ep vs 2×@47ep (same ~121M samples)
#   3. Best arch (control_feat h256) ×2 seeds on 2× data
#
# NOTE: v99_baseline_h256_s42 already ran at 60 epochs (162M samples).
#       It's a useful data point but not directly comparable to 47-epoch runs.
#       s123 and s7 start fresh at 47 epochs.
#
# Benchmark pipeline runs in parallel: ./scripts/bench_pipeline.sh
set -e
cd "$(dirname "$0")/.."

DATA_2X="data/combined_v99_clean"     # nash_b + nash_c, 2.71M rows, ~2.58M train
DATA_1X="data/combined_v99_clean_b"   # nash_b only,      1.35M rows, ~1.28M train
QUEUE_FILE="results/pipeline_queue.txt"

# Epoch counts matched to ~121M total samples seen (same as arch sweep)
EPOCHS_2X=47    # 2.58M × 47 = 121.1M
EPOCHS_1X=95    # 1.28M × 95 = 121.4M
PATIENCE_2X=12  # ~25% of epochs
PATIENCE_1X=20  # ~21% of epochs

log() { echo "[$(date '+%H:%M:%S')] $*"; }

train_and_queue() {
    local dir=$1; local model_type=$2; local hdim=$3; local seed=$4; shift 4
    log "=== Training $dir (model=$model_type h=$hdim seed=$seed) ==="
    nice -n 10 uv run python scripts/train_baseline.py \
        --out-dir "data/checkpoints/$dir" \
        --lr 0.0024 --batch-size 8192 \
        --label-smoothing 0.05 --weight-decay 1e-4 --one-cycle \
        --hidden-dim "$hdim" --value-target final_vp --dropout 0.1 \
        --model-type "$model_type" \
        --seed "$seed" \
        --deterministic-split \
        "$@"
    log "Training done: $dir"

    log "Exporting $dir..."
    nice -n 10 uv run python cpp/tools/export_baseline_to_torchscript.py \
        --checkpoint "data/checkpoints/$dir/baseline_best.pt" \
        --out "data/checkpoints/$dir/baseline_best_scripted.pt"

    echo "data/checkpoints/$dir/baseline_best_scripted.pt" >> "$QUEUE_FILE"
    log "Queued: $dir"
}

# Ensure queue file exists; start fresh each sweep run
mkdir -p results
> "$QUEUE_FILE"

log "=== Clean baseline sweep (~121M samples/run) ==="
log "1× data: $DATA_1X (1.35M rows), $EPOCHS_1X epochs"
log "2× data: $DATA_2X (2.71M rows), $EPOCHS_2X epochs"
log "Deterministic split: ~5% val fixed by game_id hash"

# --- Group 1: seed variance on clean 2× data ---
# NOTE: s42 already ran at 60ep (confounded); skip it, start from s123
train_and_queue v99_baseline_h256_s123 baseline 256 123 --data-dir "$DATA_2X" --epochs $EPOCHS_2X --patience $PATIENCE_2X
train_and_queue v99_baseline_h256_s7   baseline 256 7   --data-dir "$DATA_2X" --epochs $EPOCHS_2X --patience $PATIENCE_2X

# --- Group 2: fair saturation test (same ~121M total samples) ---
# If 2×@47ep > 1×@95ep: data-limited (diversity helps at fixed compute)
# If 2×@47ep ≈ 1×@95ep: compute-limited or data-saturated
train_and_queue v99_saturation_1x_95ep baseline 256 42 --data-dir "$DATA_1X" --epochs $EPOCHS_1X --patience $PATIENCE_1X
train_and_queue v99_saturation_2x_47ep baseline 256 42 --data-dir "$DATA_2X" --epochs $EPOCHS_2X --patience $PATIENCE_2X

# --- Group 3: best arch on clean 2× data ---
train_and_queue v99_control_feat_h256_s42  control_feat 256 42  --data-dir "$DATA_2X" --epochs $EPOCHS_2X --patience $PATIENCE_2X
train_and_queue v99_control_feat_h256_s123 control_feat 256 123 --data-dir "$DATA_2X" --epochs $EPOCHS_2X --patience $PATIENCE_2X

# Signal end of queue
echo "DONE" >> "$QUEUE_FILE"

log "=== All training complete. Benchmark pipeline will process queue. ==="
