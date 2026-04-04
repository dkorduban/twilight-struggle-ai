#!/bin/bash
# Follow-up sweep based on saturation analysis findings.
# All experiments use 1x clean data (nash_b, combined_v99_clean_b) for consistency.
#
# Priority 1: control_feat h256 @ 1x95ep x3 seeds
#   Tests if architecture + saturation compound (expected ~30-32% if so)
#   Requires ≥3 seeds to distinguish from luck (4.1pp seed variance in arch sweep)
#
# Priority 2: baseline @ 120ep (epoch ceiling test — cheap)
#   Tests if more epochs continue to improve past the 29.5% @ 95ep result
#
# Priority 3: 2x @ 95ep (disambiguate LR schedule vs data effect)
#   Tests if the saturation_1x win is about data arrangement or just training duration
#
# All runs: lr=0.0024, batch=8192, dropout=0.1, wd=1e-4, one-cycle, deterministic-split
# Queue file: results/pipeline_queue.txt (bench_pipeline watches this)

cd "$(dirname "$0")/.."

DATA_1X="data/combined_v99_clean_b"    # nash_b, 1.28M rows
DATA_2X="data/combined_v99_clean"      # nash_b+c, 2.58M rows
QUEUE_FILE="results/pipeline_queue.txt"
EPOCHS_1X_95=95;  PATIENCE_95=20
EPOCHS_1X_120=120; PATIENCE_120=25
EPOCHS_2X_95=95;  PATIENCE_2X_95=25

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

log "=== Follow-up sweep (saturation analysis recommendations) ==="

# ── Priority 1: control_feat h256 @ 1x95ep × 3 seeds ───────────────────────
# Key test: does architecture + saturation compound?
# Baseline (s42) @ 1x95ep = 29.5%. If control_feat consistently > 30%, it's real.
log "--- Group 1: control_feat h256 @ 1x95ep × 3 seeds ---"
train_and_queue v99_cf_1x95_s42  control_feat 256 42  --data-dir "$DATA_1X" --epochs $EPOCHS_1X_95 --patience $PATIENCE_95
train_and_queue v99_cf_1x95_s7   control_feat 256 7   --data-dir "$DATA_1X" --epochs $EPOCHS_1X_95 --patience $PATIENCE_95
train_and_queue v99_cf_1x95_s123 control_feat 256 123 --data-dir "$DATA_1X" --epochs $EPOCHS_1X_95 --patience $PATIENCE_95

# ── Priority 2: baseline @ 120ep (epoch ceiling test) ───────────────────────
# Cheap: tests if 120ep > 95ep. If still improving, try 150ep.
log "--- Group 2: baseline h256 @ 1x120ep (epoch ceiling) ---"
train_and_queue v99_baseline_120ep baseline 256 42 --data-dir "$DATA_1X" --epochs $EPOCHS_1X_120 --patience $PATIENCE_120

# ── Priority 3: 2x @ 95ep (LR schedule disambiguator) ──────────────────────
# If 2x@95ep ≈ 1x@95ep, the saturation_1x win is about LR schedule, not data.
# If 2x@95ep < 1x@95ep, it's genuinely about data arrangement (policy saturation).
log "--- Group 3: baseline h256 @ 2x95ep (disambiguator) ---"
train_and_queue v99_baseline_2x95ep baseline 256 42 --data-dir "$DATA_2X" --epochs $EPOCHS_2X_95 --patience $PATIENCE_2X_95

echo "DONE" >> "$QUEUE_FILE"
log "=== Follow-up sweep complete ==="
