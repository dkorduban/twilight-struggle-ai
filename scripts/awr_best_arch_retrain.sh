#!/bin/bash
# After sweep v2 completes: retrain best arch on panel v6b (correct tags), then benchmark.
# Usage: bash scripts/awr_best_arch_retrain.sh [best_arch_name]
# If no arch specified, reads from results/awr_sweep/v2/results.txt (best by vs_v56 col).
set -e

SWEEP_RESULTS="results/awr_sweep/v2/results.txt"
DATA="data/awr_eval/awr_panel_v6b.parquet"
OUTDIR="results/awr_sweep/v2b"
LOG="$OUTDIR/retrain.log"

OPP_USSR_V5="results/capacity_test/ppo_ussr_only_v5/ppo_best_scripted.pt"
OPP_US_V5="results/capacity_test/ppo_us_only_v5/ppo_best_scripted.pt"
OPP_V44="data/checkpoints/scripted_for_elo/v44_scripted.pt"
OPP_V55="data/checkpoints/scripted_for_elo/v55_scripted.pt"
OPP_V56="data/checkpoints/scripted_for_elo/v56_scripted.pt"
OPP_V54="data/checkpoints/scripted_for_elo/v54_scripted.pt"
OPP_V20="data/checkpoints/scripted_for_elo/v20_scripted.pt"
BENCH_GAMES=200
BENCH_POOL=32
BENCH_SEED=82000

mkdir -p "$OUTDIR"

if [ -n "$1" ]; then
    BEST_ARCH="$1"
else
    # Pick arch with best combined benchmark (vs_v56 column = col 8 in results.txt)
    BEST_ARCH=$(tail -n +3 "$SWEEP_RESULTS" | awk 'NF>=8 && $8+0>0 {print $8, $1}' | sort -rn | head -1 | awk '{print $2}')
fi

if [ -z "$BEST_ARCH" ]; then
    echo "ERROR: could not determine best arch from $SWEEP_RESULTS" | tee -a "$LOG"
    echo "Pass arch name explicitly: bash $0 country_attn_side"
    exit 1
fi

echo "[$(date -u)] Retraining best arch: $BEST_ARCH on $DATA" | tee "$LOG"
CKPT_DIR="$OUTDIR/$BEST_ARCH"
mkdir -p "$CKPT_DIR"

PYTHONUNBUFFERED=1 PYTHONPATH=python nice -n 15 uv run python scripts/train_awr.py \
    --data "$DATA" \
    --model-type "$BEST_ARCH" \
    --hidden-dim 256 \
    --tau 1.0 \
    --epochs 60 \
    --seed 42 \
    --device cuda \
    --out-dir "$CKPT_DIR" \
    2>&1 | tee "$CKPT_DIR/train.log"

BEST_CKPT="$CKPT_DIR/awr_best.pt"
if [ ! -f "$BEST_CKPT" ]; then
    echo "[$(date -u)] ERROR: no checkpoint found" | tee -a "$LOG"
    exit 1
fi

METRICS=$(PYTHONPATH=python uv run python -c "
import torch
ckpt = torch.load('$BEST_CKPT', map_location='cpu', weights_only=False)
m = ckpt.get('metrics', {})
print(f\"{m.get('val_adv_card_acc', 0):.4f} {m.get('best_epoch', '?')}\")
" 2>/dev/null)
VAL_ADV=$(echo "$METRICS" | awk '{print $1}')
BEST_EP=$(echo "$METRICS" | awk '{print $2}')

echo "[$(date -u)] $BEST_ARCH on v6b: val_adv=$VAL_ADV best_epoch=$BEST_EP" | tee -a "$LOG"

SCRIPTED="$CKPT_DIR/awr_best_scripted.pt"
echo "[$(date -u)] Benchmarking vs full panel (N=$BENCH_GAMES)..." | tee -a "$LOG"

BENCH_OUT=$(PYTHONUNBUFFERED=1 PYTHONPATH=python:build-ninja/bindings nice -n 15 uv run python \
    scripts/benchmark_awr_checkpoint.py \
    --checkpoint "$BEST_CKPT" \
    --scripted-out "$SCRIPTED" \
    --vs "$OPP_USSR_V5" "$OPP_US_V5" "$OPP_V44" "$OPP_V55" "$OPP_V56" "$OPP_V54" "$OPP_V20" \
    --vs-heuristic \
    --n-games "$BENCH_GAMES" \
    --pool "$BENCH_POOL" \
    --seed "$BENCH_SEED" \
    2>&1)
echo "$BENCH_OUT" | tee -a "$LOG"

echo "" | tee -a "$LOG"
echo "[$(date -u)] Done. Best arch: $BEST_ARCH, val_adv=$VAL_ADV, epoch=$BEST_EP" | tee -a "$LOG"
echo "Scripted checkpoint: $SCRIPTED" | tee -a "$LOG"
echo ""
echo "Next step (mini-PPO warm-start):"
echo "  bash scripts/awr_chain.sh $SCRIPTED"
