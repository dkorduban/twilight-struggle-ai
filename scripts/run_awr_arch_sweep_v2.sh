#!/bin/bash
# AWR arch sweep v2: 60 epochs, PYTHONUNBUFFERED, benchmark vs panel after each arch.
# Run after panel v6 collection completes.
#
# Archs tested:
#   country_attn_side          — baseline (best from phase 2)
#   country_attn_film_gated    — FiLM with gate (avoids cold-start, grad from step 0)
#   country_attn_film_normal_init — FiLM with N(0,1e-2) init (cold-start fix)
#   control_feat_gnn_card_attn — GNN + card attention (competitive with baseline)
#   country_attn_film_normal_init_zero_beta — FiLM combine A+B
#
# After each arch: export best checkpoint → benchmark vs v56 + specialists (N=100/side).
set -e

DATA="${1:-data/awr_eval/awr_panel_v6.parquet}"
OUTDIR="results/awr_sweep/v2"
LOG="$OUTDIR/sweep.log"
RESULTS="$OUTDIR/results.txt"

# Full panel opponents (same models used for data collection)
OPP_USSR_V5="results/capacity_test/ppo_ussr_only_v5/ppo_best_scripted.pt"
OPP_US_V5="results/capacity_test/ppo_us_only_v5/ppo_best_scripted.pt"
OPP_V44="data/checkpoints/scripted_for_elo/v44_scripted.pt"
OPP_V55="data/checkpoints/scripted_for_elo/v55_scripted.pt"
OPP_V56="data/checkpoints/scripted_for_elo/v56_scripted.pt"
OPP_V54="data/checkpoints/scripted_for_elo/v54_scripted.pt"
OPP_V20="data/checkpoints/scripted_for_elo/v20_scripted.pt"

BENCH_GAMES=100
BENCH_POOL=32
BENCH_SEED=80000

mkdir -p "$OUTDIR"
echo "[$(date -u)] AWR arch sweep v2: 60 epochs, benchmark included" | tee "$LOG"
echo "Data: $DATA" | tee -a "$LOG"
echo "" | tee -a "$LOG"

printf "%-45s %8s %8s %8s %8s %8s %8s %8s %8s %8s\n" \
    "Architecture" "val_adv" "ep" "vs_heur" "vs_ussr5" "vs_us5" "vs_v44" "vs_v55" "vs_v56" "vs_v54" \
    | tee "$RESULTS"
printf "%-45s %8s %8s %8s %8s %8s %8s %8s %8s %8s\n" \
    "---------------------------------------------" "-------" "--" "-------" "--------" "------" "------" "------" "------" "------" \
    | tee -a "$RESULTS"

ARCHS=(
    "country_attn_side"
    "country_attn_film_gated"
    "country_attn_film_normal_init"
    "control_feat_gnn_card_attn"
    "country_attn_film_normal_init_zero_beta"
)

for ARCH in "${ARCHS[@]}"; do
    CKPT_DIR="$OUTDIR/$ARCH"
    mkdir -p "$CKPT_DIR"
    echo "" | tee -a "$LOG"
    echo "[$(date -u)] Training $ARCH (60 epochs)..." | tee -a "$LOG"

    PYTHONUNBUFFERED=1 PYTHONPATH=python nice -n 15 uv run python scripts/train_awr.py \
        --data "$DATA" \
        --model-type "$ARCH" \
        --hidden-dim 256 \
        --tau 1.0 \
        --epochs 60 \
        --seed 42 \
        --device cuda \
        --out-dir "$CKPT_DIR" \
        2>&1 | tee "$CKPT_DIR/train.log"

    # Extract best val metrics from checkpoint
    BEST_CKPT="$CKPT_DIR/awr_best.pt"
    if [ ! -f "$BEST_CKPT" ]; then
        echo "[$(date -u)] WARNING: no checkpoint found for $ARCH, skipping benchmark" | tee -a "$LOG"
        continue
    fi

    # Read metrics from checkpoint
    METRICS=$(PYTHONPATH=python uv run python -c "
import torch, json
ckpt = torch.load('$BEST_CKPT', map_location='cpu', weights_only=False)
m = ckpt.get('metrics', {})
print(f\"{m.get('val_adv_card_acc', 0):.4f} {m.get('best_epoch', '?')}\")
" 2>/dev/null)
    VAL_ADV=$(echo "$METRICS" | awk '{print $1}')
    BEST_EP=$(echo "$METRICS" | awk '{print $2}')

    echo "[$(date -u)] $ARCH: val_adv=$VAL_ADV best_epoch=$BEST_EP" | tee -a "$LOG"
    echo "[$(date -u)] Benchmarking $ARCH vs panel..." | tee -a "$LOG"

    # Export and benchmark
    SCRIPTED="$CKPT_DIR/awr_best_scripted.pt"
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

    # Parse benchmark results (grep by model name suffix)
    VS_HEUR=$(echo "$BENCH_OUT" | grep "heuristic" | grep -oP "combined=\K[0-9.]+")
    VS_USSR5=$(echo "$BENCH_OUT" | grep "ussr_only_v5" | grep -oP "combined=\K[0-9.]+")
    VS_US5=$(echo "$BENCH_OUT" | grep "us_only_v5" | grep -oP "combined=\K[0-9.]+")
    VS_V44=$(echo "$BENCH_OUT" | grep "v44_scripted" | grep -oP "combined=\K[0-9.]+")
    VS_V55=$(echo "$BENCH_OUT" | grep "v55_scripted" | grep -oP "combined=\K[0-9.]+")
    VS_V56=$(echo "$BENCH_OUT" | grep "v56_scripted" | grep -oP "combined=\K[0-9.]+")
    VS_V54=$(echo "$BENCH_OUT" | grep "v54_scripted" | grep -oP "combined=\K[0-9.]+")

    printf "%-45s %8s %8s %8s %8s %8s %8s %8s %8s %8s\n" \
        "$ARCH" "$VAL_ADV" "$BEST_EP" \
        "${VS_HEUR:-N/A}" "${VS_USSR5:-N/A}" "${VS_US5:-N/A}" \
        "${VS_V44:-N/A}" "${VS_V55:-N/A}" "${VS_V56:-N/A}" "${VS_V54:-N/A}" \
        | tee -a "$RESULTS"
done

echo "" | tee -a "$LOG"
echo "[$(date -u)] Sweep complete. Results:" | tee -a "$LOG"
cat "$RESULTS" | tee -a "$LOG"
