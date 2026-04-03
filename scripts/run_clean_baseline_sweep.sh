#!/bin/bash
# Clean baseline sweep on post-DEFCON-fix data (no contaminated nash).
# Uses deterministic train/val split and samples_seen W&B axis.
#
# Groups:
#   1. baseline h256 ×3 seeds on nash_b+c (2.71M rows) — seed variance on clean 2× data
#   2. Fair saturation test: nash_b only (1×, 60ep) vs nash_b+c (2×, 30ep)
#      Same total samples seen ≈ 1.35M × 60 = 2.71M × 30 → tells if we're data-limited
#   3. Best arch (control_feat h256) ×2 seeds on clean 2× data
#
# Run after arch sweep completes. GPU must be free.
# Benchmark pipeline runs in parallel: ./scripts/bench_pipeline.sh
set -e
cd "$(dirname "$0")/.."

DATA_2X="data/combined_v99_clean"     # nash_b + nash_c, 2.71M rows
DATA_1X="data/combined_v99_clean_b"   # nash_b only,      1.35M rows
QUEUE_FILE="results/pipeline_queue.txt"

log() { echo "[$(date '+%H:%M:%S')] $*"; }

train_and_queue() {
    local dir=$1; local model_type=$2; local hdim=$3; local seed=$4; shift 4
    log "=== Training $dir (model=$model_type h=$hdim seed=$seed) ==="
    nice -n 10 uv run python scripts/train_baseline.py \
        --out-dir "data/checkpoints/$dir" \
        --lr 0.0024 --batch-size 8192 --epochs 60 --patience 15 \
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

log "=== Clean baseline sweep ==="
log "1× data: $DATA_1X (1.35M rows, 10k games)"
log "2× data: $DATA_2X (2.71M rows, 20k games)"
log "Deterministic split: ~5% val fixed by game_id hash"

# --- Group 1: seed variance on clean 2× data ---
train_and_queue v99_baseline_h256_s42  baseline 256 42  --data-dir "$DATA_2X"
train_and_queue v99_baseline_h256_s123 baseline 256 123 --data-dir "$DATA_2X"
train_and_queue v99_baseline_h256_s7   baseline 256 7   --data-dir "$DATA_2X"

# --- Group 2: fair data saturation test (same total samples seen) ---
# 1× data @ 60 epochs vs 2× data @ 30 epochs
# If 2×@30 > 1×@60: data-limited (more diversity helps)
# If 2×@30 ≈ 1×@60: compute-limited at this scale
train_and_queue v99_saturation_1x_60ep baseline 256 42 --data-dir "$DATA_1X" --epochs 60 --patience 15
train_and_queue v99_saturation_2x_30ep baseline 256 42 --data-dir "$DATA_2X" --epochs 30 --patience 10

# --- Group 3: best arch on clean 2× data ---
train_and_queue v99_control_feat_h256_s42  control_feat 256 42  --data-dir "$DATA_2X"
train_and_queue v99_control_feat_h256_s123 control_feat 256 123 --data-dir "$DATA_2X"

# Signal end of queue
echo "DONE" >> "$QUEUE_FILE"

log "=== All training complete. Benchmark pipeline will process queue. ==="
log "Run bench_pipeline.sh in parallel to process benchmarks."
