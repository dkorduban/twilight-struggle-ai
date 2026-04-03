#!/bin/bash
# GPU pipeline: train → export → signal → repeat
# Writes model paths to QUEUE_FILE for the benchmark pipeline to pick up.
set -e
cd "$(dirname "$0")/.."

QUEUE_FILE="${QUEUE_FILE:-$(dirname "$0")/../results/pipeline_queue.txt}"
touch "$QUEUE_FILE"

export_model() {
    local dir=$1
    nice -n 10 uv run python cpp/tools/export_baseline_to_torchscript.py \
        --checkpoint "data/checkpoints/$dir/baseline_best.pt" \
        --out "data/checkpoints/$dir/baseline_best_scripted.pt" 2>&1
    echo "data/checkpoints/$dir/baseline_best_scripted.pt" >> "$QUEUE_FILE"
    echo "[train_pipeline] Queued $dir for benchmarking"
}

train_model() {
    local dir=$1 model_type=$2 hdim=$3
    shift 3
    echo "[train_pipeline] $(date '+%H:%M:%S') Training $model_type h$hdim => $dir"
    nice -n 10 uv run python scripts/train_baseline.py \
        --data-dir "${DATA_DIR:-data/combined_v89}" \
        --out-dir "data/checkpoints/$dir" \
        --lr 0.0024 --batch-size 8192 --epochs 60 --patience 15 \
        --label-smoothing 0.05 --weight-decay 1e-4 --one-cycle \
        --hidden-dim "$hdim" --value-target final_vp --dropout 0.1 \
        --model-type "$model_type" "$@" 2>&1 | tail -5
    export_model "$dir"
}

# Process arguments: each arg is "dir:model_type:hdim[:extra_flags]"
# Example: ./scripts/train_pipeline.sh arch_baseline_h256:baseline:256 arch_attn_h256:country_attn:256
for spec in "$@"; do
    IFS=':' read -r dir model_type hdim extra <<< "$spec"
    train_model "$dir" "$model_type" "$hdim" $extra
done

echo "DONE" >> "$QUEUE_FILE"
echo "[train_pipeline] All training complete"
