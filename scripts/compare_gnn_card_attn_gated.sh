#!/bin/bash
# AWR comparison: gnn_card_attn_gated vs parent control_feat_gnn_card_attn.
# Run on v7 data (1.48M rows) with same hyperparams as v2b sweep.
# Queue this after PPO chain finishes or GPU is free.
#
# Usage: bash scripts/compare_gnn_card_attn_gated.sh [out_dir]
set -e

OUTDIR="${1:-results/awr_sweep/gated_vs_parent}"
DATA="data/awr_eval/awr_panel_v7.parquet"
ARCHS=("control_feat_gnn_card_attn" "gnn_card_attn_gated")
SEED=42
EPOCHS=30
TAU=1.0
N_BENCH=200
BENCH_SEED=90000

mkdir -p "$OUTDIR"
LOG="$OUTDIR/compare.log"

echo "[$(date -u)] Comparing gnn_card_attn_gated vs parent on v7 data" | tee "$LOG"
echo "  data=$DATA n=$EPOCHS epochs, tau=$TAU, seed=$SEED" | tee -a "$LOG"

RESULTS_FILE="$OUTDIR/results.txt"
printf "%-42s  %s  %s  %s  %s\n" "Architecture" "val_adv" "ep" "vs_heur" "avg_8panel" > "$RESULTS_FILE"
printf "%s\n" "------------------------------------------------------------" >> "$RESULTS_FILE"

for ARCH in "${ARCHS[@]}"; do
    ARCH_DIR="$OUTDIR/$ARCH"
    mkdir -p "$ARCH_DIR"
    echo "" | tee -a "$LOG"
    echo "[$(date -u)] Training $ARCH ..." | tee -a "$LOG"

    PYTHONUNBUFFERED=1 nice -n 15 uv run python scripts/train_awr.py \
        --data "$DATA" \
        --model-type "$ARCH" \
        --out-dir "$ARCH_DIR" \
        --epochs "$EPOCHS" \
        --seed "$SEED" \
        --tau "$TAU" \
        --batch-size 4096 \
        2>&1 | tee "$ARCH_DIR/train.log"

    # Export to TorchScript
    BEST_CKPT=$(ls -t "$ARCH_DIR"/*.pt 2>/dev/null | grep -v scripted | head -1)
    if [ -z "$BEST_CKPT" ]; then
        echo "  [warn] no checkpoint found for $ARCH" | tee -a "$LOG"
        continue
    fi

    SCRIPTED="$ARCH_DIR/best_scripted.pt"
    PYTHONPATH=build-ninja/bindings uv run python -c "
import torch, sys
m = torch.load('$BEST_CKPT', map_location='cpu', weights_only=False)
m.eval()
sc = torch.jit.script(m)
sc.save('$SCRIPTED')
print('Scripted:', '$SCRIPTED')
" 2>&1 | tee -a "$LOG"

    # Get val_adv from training log
    VAL_ADV=$(grep "val_adv_card_acc" "$ARCH_DIR/train.log" | tail -1 | grep -oE "[0-9]\.[0-9]+" | head -1 || echo "?")
    BEST_EP=$(grep "val_adv_card_acc" "$ARCH_DIR/train.log" | tail -1 | grep -oE "ep=[0-9]+" | grep -oE "[0-9]+" || echo "?")

    # Benchmark vs heuristic + panel
    echo "[$(date -u)] Benchmarking $ARCH ..." | tee -a "$LOG"

    PANEL_OPPS="data/checkpoints/scripted_for_elo/v44_scripted.pt \
data/checkpoints/scripted_for_elo/v55_scripted.pt \
data/checkpoints/scripted_for_elo/v56_scripted.pt \
data/checkpoints/scripted_for_elo/v54_scripted.pt \
data/checkpoints/scripted_for_elo/v20_scripted.pt \
results/capacity_test/ppo_ussr_only_v5/ppo_best_scripted.pt \
results/capacity_test/ppo_us_only_v5/ppo_best_scripted.pt"

    # vs heuristic (uses benchmark_batched both sides)
    VS_HEUR=$(PYTHONPATH=build-ninja/bindings uv run python -c "
import tscore
r_u = tscore.benchmark_batched('$SCRIPTED', tscore.Side.USSR, $N_BENCH, seed=$BENCH_SEED)
r_s = tscore.benchmark_batched('$SCRIPTED', tscore.Side.US, $N_BENCH, seed=$(( BENCH_SEED + 500 )))
wr_u = sum(1 for x in r_u if x.winner == tscore.Side.USSR) / len(r_u) * 100
wr_s = sum(1 for x in r_s if x.winner == tscore.Side.US) / len(r_s) * 100
print(f'{(wr_u+wr_s)/2:.1f}')
" 2>/dev/null) || VS_HEUR="err"

    BENCH_OUT=""
    for OPP in $PANEL_OPPS; do
        WR=$(PYTHONPATH=build-ninja/bindings uv run python -c "
import tscore
results = tscore.benchmark_model_vs_model_batched('$SCRIPTED', '$OPP', n_games=$N_BENCH, seed=$BENCH_SEED)
n = len(results)
# First half: scripted=USSR (model_a=USSR). Second half: scripted=US (model_a=US)
half = n // 2
wr_u = sum(1 for x in results[:half] if x.winner == tscore.Side.USSR) / half * 100
wr_s = sum(1 for x in results[half:] if x.winner == tscore.Side.US) / (n-half) * 100
print(f'{(wr_u+wr_s)/2:.1f}')
" 2>/dev/null) || WR="err"
        BENCH_OUT="$BENCH_OUT $WR"
    done

    # Compute avg_8panel
    AVG=$(python3 -c "
vals = [v for v in '$BENCH_OUT $VS_HEUR'.split() if v not in ('err','')]
print(f'{sum(float(v) for v in vals)/len(vals):.2f}' if vals else '?')
" 2>/dev/null)

    printf "%-42s  %s  %s  %s  %s\n" "$ARCH" "$VAL_ADV" "$BEST_EP" "$VS_HEUR" "$AVG" | tee -a "$RESULTS_FILE"
    echo "[$(date -u)] $ARCH done: val_adv=$VAL_ADV vs_heur=$VS_HEUR avg=$AVG" | tee -a "$LOG"
done

echo "" | tee -a "$LOG"
echo "=== RESULTS ===" | tee -a "$LOG"
cat "$RESULTS_FILE" | tee -a "$LOG"
echo "[$(date -u)] Done." | tee -a "$LOG"
