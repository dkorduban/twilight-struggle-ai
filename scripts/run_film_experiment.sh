#!/bin/bash
# FiLM variant comparison: train all 5 FiLM variants for 20 epochs on frozen AWR data.
# Outputs AWR offline metrics only (val_adv_card_acc) — no rollout benchmark.
# Run after model.py changes are live.
set -e

DATA="data/awr_eval/awr_panel_v5.parquet"
OUTDIR="results/awr_sweep/film_exp"
LOG="$OUTDIR/film_experiment.log"

mkdir -p "$OUTDIR"
echo "[$(date -u)] FiLM variant experiment: 5 archs x 20 epochs x tau=1.0" | tee "$LOG"

ARCHS=(
    "country_attn_film"
    "country_attn_film_normal_init"
    "country_attn_film_zero_beta_bias"
    "country_attn_film_gated"
    "country_attn_film_normal_init_zero_beta"
)

printf "\n%-45s %10s %10s %10s\n" "Architecture" "AdvCard%" "CardAcc%" "PolicyL" | tee "$OUTDIR/results.txt"
printf "%-45s %10s %10s %10s\n" "---------------------------------------------" "--------" "--------" "-------" | tee -a "$OUTDIR/results.txt"

for ARCH in "${ARCHS[@]}"; do
    CKPT_DIR="$OUTDIR/$ARCH"
    mkdir -p "$CKPT_DIR"
    echo "" | tee -a "$LOG"
    echo "[$(date -u)] Training $ARCH (20 epochs) ..." | tee -a "$LOG"

    PYTHONPATH=python nice -n 15 uv run python scripts/train_awr.py \
        --data "$DATA" \
        --model-type "$ARCH" \
        --hidden-dim 256 \
        --tau 1.0 \
        --epochs 20 \
        --seed 42 \
        --device cuda \
        --out-dir "$CKPT_DIR" \
        2>&1 | tee "$CKPT_DIR/train.log"

    # Extract best val metrics from training log (actual format: "val_adv=0.XXX val_card=0.XXX")
    ADV=$(grep -oP "val_adv=\K[0-9.]+" "$CKPT_DIR/train.log" | tail -1 || echo "N/A")
    CARD=$(grep -oP "val_card=\K[0-9.]+" "$CKPT_DIR/train.log" | tail -1 || echo "N/A")
    PL=$(grep -oP "val_pl=\K[0-9.]+" "$CKPT_DIR/train.log" | tail -1 || echo "N/A")

    echo "[$(date -u)] $ARCH: adv_card=$ADV card=$CARD policy_loss=$PL" | tee -a "$LOG"
    printf "%-45s %10s %10s %10s\n" "$ARCH" "$ADV" "$CARD" "$PL" | tee -a "$OUTDIR/results.txt"
done

echo "" | tee -a "$LOG"
echo "[$(date -u)] Done. Results:" | tee -a "$LOG"
cat "$OUTDIR/results.txt" | tee -a "$LOG"
