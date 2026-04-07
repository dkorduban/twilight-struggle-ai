#!/bin/bash
set -e

cd /home/dkord/code/twilight-struggle-ai

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

log_start() { echo -e "${BLUE}=== $1 ===${NC}"; date '+%Y-%m-%d %H:%M:%S'; }
log_done() { echo -e "${GREEN}✓ $1${NC}"; date '+%Y-%m-%d %H:%M:%S'; }

export PYTHONPATH=/home/dkord/code/twilight-struggle-ai/build-ninja/bindings

RESULTS_FILE=results/v110_data_sweep.txt
mkdir -p results

benchmark_model() {
  local name="$1"
  local ckpt_dir="$2"

  log_start "Exporting $name"
  nice -n 10 uv run python cpp/tools/export_baseline_to_torchscript.py \
      --checkpoint "$ckpt_dir/baseline_best.pt" \
      --out "$ckpt_dir/baseline_best_scripted.pt"
  log_done "Export $name"

  log_start "Benchmarking $name (Nash temps, 500g/side)"
  nice -n 10 uv run python -c "
import tscore, math
model = '$ckpt_dir/baseline_best_scripted.pt'
ur = tscore.benchmark_batched(model, tscore.Side.USSR, 500, pool_size=32, seed=50000, nash_temperatures=True)
usr = tscore.benchmark_batched(model, tscore.Side.US, 500, pool_size=32, seed=50500, nash_temperatures=True)
ussr_w = sum(1 for r in ur if r.winner == tscore.Side.USSR)
us_w = sum(1 for r in usr if r.winner == tscore.Side.US)
ussr_pct = ussr_w/5; us_pct = us_w/5
comb = (ussr_pct+us_pct)/2
se = math.sqrt(comb/100*(1-comb/100)/1000)*100
print(f'$name | Nash USSR {ussr_pct:5.1f}% | US {us_pct:5.1f}% | Combined {comb:5.1f}% ±{se:.1f}')
" | tee -a "$RESULTS_FILE"
  log_done "Benchmark $name"
}

# --- Run 3: GNN 2x data 95ep (resume from epoch 17) ---
log_start "RUN 3: GNN 2x95 s42 (resume)"
nice -n 10 uv run python scripts/train_baseline.py \
    --data-dir data/nash_bc_combined \
    --out-dir data/checkpoints/v110_cf_gnn_2x95_s42 \
    --model-type control_feat_gnn --hidden-dim 256 \
    --batch-size 8192 --lr 0.0024 --epochs 95 --patience 20 \
    --dropout 0.1 --weight-decay 1e-4 --label-smoothing 0.05 \
    --one-cycle --deterministic-split --value-target final_vp --seed 42 \
    --resume
log_done "Training Run 3"
benchmark_model "v110_gnn_2x95_s42" "data/checkpoints/v110_cf_gnn_2x95_s42"

# --- Run 4: GNN 3x data 95ep (resume from epoch 11) ---
log_start "RUN 4: GNN 3x95 s42 (resume)"
nice -n 10 uv run python scripts/train_baseline.py \
    --data-dir data/nash_bcd_combined \
    --out-dir data/checkpoints/v110_cf_gnn_3x95_s42 \
    --model-type control_feat_gnn --hidden-dim 256 \
    --batch-size 8192 --lr 0.0024 --epochs 95 --patience 20 \
    --dropout 0.1 --weight-decay 1e-4 --label-smoothing 0.05 \
    --one-cycle --deterministic-split --value-target final_vp --seed 42 \
    --resume
log_done "Training Run 4"
benchmark_model "v110_gnn_3x95_s42" "data/checkpoints/v110_cf_gnn_3x95_s42"

# --- Summary ---
echo ""
log_start "FINAL SUMMARY"
echo "v110 DATA SWEEP RESULTS (Nash temps, 500g/side, seed=50000/50500):"
echo "Baseline: v106_cf_gnn_s42 = Nash Combined 34.9%"
echo ""
cat "$RESULTS_FILE"
