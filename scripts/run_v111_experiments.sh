#!/bin/bash
# v111 clean data combination experiments.
# Run AFTER v110_cf_gnn_3x95_s42 finishes (waits for its PID if passed as $1).
set -e

cd /home/dkord/code/twilight-struggle-ai

BLUE='\033[0;34m'; GREEN='\033[0;32m'; NC='\033[0m'
log_start() { echo -e "${BLUE}=== $1 ===${NC}"; date '+%Y-%m-%d %H:%M:%S'; }
log_done()  { echo -e "${GREEN}✓ $1${NC}";   date '+%Y-%m-%d %H:%M:%S'; }

export PYTHONPATH=/home/dkord/code/twilight-struggle-ai/build-ninja/bindings

RESULTS_FILE=results/v111_experiments.txt
mkdir -p results

# Wait for v110_3x95 to finish if PID passed
if [ -n "$1" ]; then
    echo "Waiting for PID $1 to finish..."
    tail --pid="$1" -f /dev/null 2>/dev/null || true
    echo "PID $1 done."
fi

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
ur  = tscore.benchmark_batched(model, tscore.Side.USSR, 500, pool_size=32, seed=50000, nash_temperatures=True)
usr = tscore.benchmark_batched(model, tscore.Side.US,   500, pool_size=32, seed=50500, nash_temperatures=True)
ussr_w = sum(1 for r in ur  if r.winner == tscore.Side.USSR)
us_w   = sum(1 for r in usr if r.winner == tscore.Side.US)
ussr_pct = ussr_w/5; us_pct = us_w/5
comb = (ussr_pct+us_pct)/2
se = math.sqrt(comb/100*(1-comb/100)/1000)*100
print(f'$name | Nash USSR {ussr_pct:5.1f}% | US {us_pct:5.1f}% | Combined {comb:5.1f}% +/-{se:.1f}')
" | tee -a "$RESULTS_FILE"
    log_done "Benchmark $name"
}

COMMON_ARGS="--model-type control_feat_gnn --hidden-dim 256 --batch-size 8192 \
             --lr 0.0024 --dropout 0.1 --weight-decay 1e-4 --label-smoothing 0.05 \
             --one-cycle --deterministic-split --value-target final_vp --seed 42"

# --- v111a: nash_c + nash_d, 2.74M rows, 47 epochs (clean 2x) ---
log_start "v111_cd_47ep_s42: clean 2x (nash_c + nash_d, 47ep)"
nice -n 10 uv run python scripts/train_baseline.py \
    --data-dir data/nash_cd_combined \
    --out-dir data/checkpoints/v111_cd_47ep_s42 \
    $COMMON_ARGS --epochs 47 --patience 15
log_done "v111_cd_47ep_s42 training"
benchmark_model "v111_cd_47ep_s42" "data/checkpoints/v111_cd_47ep_s42"

# --- v111b: nash_c + nash_d, 2.74M rows, 95 epochs (overtraining check) ---
log_start "v111_cd_95ep_s42: clean 2x overtraining check (nash_c + nash_d, 95ep)"
nice -n 10 uv run python scripts/train_baseline.py \
    --data-dir data/nash_cd_combined \
    --out-dir data/checkpoints/v111_cd_95ep_s42 \
    $COMMON_ARGS --epochs 95 --patience 20
log_done "v111_cd_95ep_s42 training"
benchmark_model "v111_cd_95ep_s42" "data/checkpoints/v111_cd_95ep_s42"

# --- v111c: nash_c only, 47 epochs (epoch-matched 1x control) ---
log_start "v111_c_only_47ep_s42: 1x control (nash_c only, 47ep)"
nice -n 10 uv run python scripts/train_baseline.py \
    --data-dir data/selfplay/heuristic_10k_setup_bid2_nash_c.parquet \
    --out-dir data/checkpoints/v111_c_only_47ep_s42 \
    $COMMON_ARGS --epochs 47 --patience 15
log_done "v111_c_only_47ep_s42 training"
benchmark_model "v111_c_only_47ep_s42" "data/checkpoints/v111_c_only_47ep_s42"

# --- v111d: nash_b only, 95 epochs (isolate nash_b quality) ---
log_start "v111_b_only_95ep_s42: nash_b quality check (nash_b only, 95ep)"
nice -n 10 uv run python scripts/train_baseline.py \
    --data-dir data/selfplay/heuristic_10k_setup_bid2_nash_b.parquet \
    --out-dir data/checkpoints/v111_b_only_95ep_s42 \
    $COMMON_ARGS --epochs 95 --patience 20
log_done "v111_b_only_95ep_s42 training"
benchmark_model "v111_b_only_95ep_s42" "data/checkpoints/v111_b_only_95ep_s42"

# --- Summary ---
log_start "v111 FINAL SUMMARY"
echo "v111 CLEAN DATA COMBINATION RESULTS (Nash temps, 500g/side, seed=50000/50500):"
echo "Baseline: v106_cf_gnn_s42 = Nash Combined 34.9%"
echo ""
cat "$RESULTS_FILE"
