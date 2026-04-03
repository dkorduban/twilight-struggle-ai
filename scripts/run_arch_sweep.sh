#!/bin/bash
set -e

cd /home/dkord/code/twilight-struggle-ai

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

log_start() {
  echo -e "${BLUE}=== $1 ===${NC}"
  date '+%Y-%m-%d %H:%M:%S'
}

log_done() {
  echo -e "${GREEN}✓ $1${NC}"
  date '+%Y-%m-%d %H:%M:%S'
}

wait_for_completion() {
  local pattern="$1"
  local label="$2"
  while ps aux | grep "$pattern" | grep -v grep | grep -q .; do
    sleep 30
  done
  log_done "$label"
}

export PYTHONPATH=/home/dkord/code/twilight-struggle-ai/build-ninja/bindings

# Run 1: country_attn h128
log_start "RUN 1: country_attn h128"
nice -n 10 uv run python scripts/train_baseline.py \
    --data-dir data/combined_v89 \
    --out-dir data/checkpoints/arch_country_attn_h128_v2 \
    --lr 0.0024 --batch-size 8192 --epochs 60 --patience 15 \
    --label-smoothing 0.05 --weight-decay 1e-4 --one-cycle \
    --hidden-dim 128 --value-target final_vp --dropout 0.1 \
    --model-type country_attn
log_done "Training Run 1"

wait_for_completion "train_baseline.*h128_v2" "Run 1 training fully completed"

log_start "Exporting Run 1"
nice -n 10 uv run python cpp/tools/export_baseline_to_torchscript.py \
    --checkpoint data/checkpoints/arch_country_attn_h128_v2/baseline_best.pt \
    --out data/checkpoints/arch_country_attn_h128_v2/baseline_best_scripted.pt
log_done "Export Run 1"

log_start "Benchmarking Run 1"
nice -n 19 uv run python -c "
import tscore, math
model = 'data/checkpoints/arch_country_attn_h128_v2/baseline_best_scripted.pt'
ussr_total = us_total = 0
for seed_base in [50000, 60000, 70000, 80000]:
    ur = tscore.benchmark_batched(model, tscore.Side.USSR, 500, pool_size=32, seed=seed_base)
    usr = tscore.benchmark_batched(model, tscore.Side.US, 500, pool_size=32, seed=seed_base+500)
    ussr_total += sum(1 for r in ur if r.winner == tscore.Side.USSR)
    us_total += sum(1 for r in usr if r.winner == tscore.Side.US)
n = 2000
ussr_pct = ussr_total/n*100; us_pct = us_total/n*100
comb = (ussr_total+us_total)/(n*2)*100
se = math.sqrt(comb/100*(1-comb/100)/(n*2))*100
print(f'country_attn h128 | USSR {ussr_pct:5.1f}% ±{se:.1f} | US {us_pct:5.1f}% | Combined {comb:5.1f}% ±{se:.1f}')
" | tee -a /tmp/arch_sweep_results.txt
log_done "Benchmark Run 1"

# Run 2: control_feat h128
log_start "RUN 2: control_feat h128"
nice -n 10 uv run python scripts/train_baseline.py \
    --data-dir data/combined_v89 \
    --out-dir data/checkpoints/arch_control_feat_h128 \
    --lr 0.0024 --batch-size 8192 --epochs 60 --patience 15 \
    --label-smoothing 0.05 --weight-decay 1e-4 --one-cycle \
    --hidden-dim 128 --value-target final_vp --dropout 0.1 \
    --model-type control_feat
log_done "Training Run 2"

log_start "Exporting Run 2"
nice -n 10 uv run python cpp/tools/export_baseline_to_torchscript.py \
    --checkpoint data/checkpoints/arch_control_feat_h128/baseline_best.pt \
    --out data/checkpoints/arch_control_feat_h128/baseline_best_scripted.pt
log_done "Export Run 2"

log_start "Benchmarking Run 2"
nice -n 19 uv run python -c "
import tscore, math
model = 'data/checkpoints/arch_control_feat_h128/baseline_best_scripted.pt'
ussr_total = us_total = 0
for seed_base in [50000, 60000, 70000, 80000]:
    ur = tscore.benchmark_batched(model, tscore.Side.USSR, 500, pool_size=32, seed=seed_base)
    usr = tscore.benchmark_batched(model, tscore.Side.US, 500, pool_size=32, seed=seed_base+500)
    ussr_total += sum(1 for r in ur if r.winner == tscore.Side.USSR)
    us_total += sum(1 for r in usr if r.winner == tscore.Side.US)
n = 2000
ussr_pct = ussr_total/n*100; us_pct = us_total/n*100
comb = (ussr_total+us_total)/(n*2)*100
se = math.sqrt(comb/100*(1-comb/100)/(n*2))*100
print(f'control_feat h128  | USSR {ussr_pct:5.1f}% ±{se:.1f} | US {us_pct:5.1f}% | Combined {comb:5.1f}% ±{se:.1f}')
" | tee -a /tmp/arch_sweep_results.txt
log_done "Benchmark Run 2"

# Run 3: country_attn h256
log_start "RUN 3: country_attn h256"
nice -n 10 uv run python scripts/train_baseline.py \
    --data-dir data/combined_v89 \
    --out-dir data/checkpoints/arch_country_attn_h256_v2 \
    --lr 0.0024 --batch-size 8192 --epochs 60 --patience 15 \
    --label-smoothing 0.05 --weight-decay 1e-4 --one-cycle \
    --hidden-dim 256 --value-target final_vp --dropout 0.1 \
    --model-type country_attn
log_done "Training Run 3"

log_start "Exporting Run 3"
nice -n 10 uv run python cpp/tools/export_baseline_to_torchscript.py \
    --checkpoint data/checkpoints/arch_country_attn_h256_v2/baseline_best.pt \
    --out data/checkpoints/arch_country_attn_h256_v2/baseline_best_scripted.pt
log_done "Export Run 3"

log_start "Benchmarking Run 3"
nice -n 19 uv run python -c "
import tscore, math
model = 'data/checkpoints/arch_country_attn_h256_v2/baseline_best_scripted.pt'
ussr_total = us_total = 0
for seed_base in [50000, 60000, 70000, 80000]:
    ur = tscore.benchmark_batched(model, tscore.Side.USSR, 500, pool_size=32, seed=seed_base)
    usr = tscore.benchmark_batched(model, tscore.Side.US, 500, pool_size=32, seed=seed_base+500)
    ussr_total += sum(1 for r in ur if r.winner == tscore.Side.USSR)
    us_total += sum(1 for r in usr if r.winner == tscore.Side.US)
n = 2000
ussr_pct = ussr_total/n*100; us_pct = us_total/n*100
comb = (ussr_total+us_total)/(n*2)*100
se = math.sqrt(comb/100*(1-comb/100)/(n*2))*100
print(f'country_attn h256 | USSR {ussr_pct:5.1f}% ±{se:.1f} | US {us_pct:5.1f}% | Combined {comb:5.1f}% ±{se:.1f}')
" | tee -a /tmp/arch_sweep_results.txt
log_done "Benchmark Run 3"

# Run 4: control_feat h256
log_start "RUN 4: control_feat h256"
nice -n 10 uv run python scripts/train_baseline.py \
    --data-dir data/combined_v89 \
    --out-dir data/checkpoints/arch_control_feat_h256 \
    --lr 0.0024 --batch-size 8192 --epochs 60 --patience 15 \
    --label-smoothing 0.05 --weight-decay 1e-4 --one-cycle \
    --hidden-dim 256 --value-target final_vp --dropout 0.1 \
    --model-type control_feat
log_done "Training Run 4"

log_start "Exporting Run 4"
nice -n 10 uv run python cpp/tools/export_baseline_to_torchscript.py \
    --checkpoint data/checkpoints/arch_control_feat_h256/baseline_best.pt \
    --out data/checkpoints/arch_control_feat_h256/baseline_best_scripted.pt
log_done "Export Run 4"

log_start "Benchmarking Run 4"
nice -n 19 uv run python -c "
import tscore, math
model = 'data/checkpoints/arch_control_feat_h256/baseline_best_scripted.pt'
ussr_total = us_total = 0
for seed_base in [50000, 60000, 70000, 80000]:
    ur = tscore.benchmark_batched(model, tscore.Side.USSR, 500, pool_size=32, seed=seed_base)
    usr = tscore.benchmark_batched(model, tscore.Side.US, 500, pool_size=32, seed=seed_base+500)
    ussr_total += sum(1 for r in ur if r.winner == tscore.Side.USSR)
    us_total += sum(1 for r in usr if r.winner == tscore.Side.US)
n = 2000
ussr_pct = ussr_total/n*100; us_pct = us_total/n*100
comb = (ussr_total+us_total)/(n*2)*100
se = math.sqrt(comb/100*(1-comb/100)/(n*2))*100
print(f'control_feat h256  | USSR {ussr_pct:5.1f}% ±{se:.1f} | US {us_pct:5.1f}% | Combined {comb:5.1f}% ±{se:.1f}')
" | tee -a /tmp/arch_sweep_results.txt
log_done "Benchmark Run 4"

# Final summary
echo ""
log_start "FINAL SUMMARY"
echo "ARCHITECTURE SWEEP RESULTS (2000 games/side):"
cat /tmp/arch_sweep_results.txt || echo "No results collected"
