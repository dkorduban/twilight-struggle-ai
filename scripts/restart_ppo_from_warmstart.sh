#!/bin/bash
# Main PPO chain restart from AWR+warmstart checkpoint (control_feat_gnn_card_attn).
# Requires user authorization before running.
#
# Starting point: results/awr_sweep/ppo_warmstart_control_feat_gnn_card_attn/ppo_best.pt
# Validation: 45.0% vs heuristic after 15-iter warmstart (at v56 level already).
# rollout_wr at iter 15: 0.409 (still increasing — not converged).
#
# Usage: bash scripts/restart_ppo_from_warmstart.sh [n_iterations]
set -e

N_ITER="${1:-300}"
WARMSTART_CKPT="results/awr_sweep/ppo_warmstart_control_feat_gnn_card_attn/ppo_best.pt"
OUTDIR="results/ppo_gnn_card_attn_v1"
LOG="$OUTDIR/train.log"

PANEL_FIX="\
results/capacity_test/ppo_ussr_only_v5/ppo_best_scripted.pt \
results/capacity_test/ppo_us_only_v5/ppo_best_scripted.pt \
data/checkpoints/scripted_for_elo/v44_scripted.pt \
data/checkpoints/scripted_for_elo/v55_scripted.pt \
data/checkpoints/scripted_for_elo/v56_scripted.pt \
data/checkpoints/scripted_for_elo/v54_scripted.pt \
data/checkpoints/scripted_for_elo/v20_scripted.pt \
__heuristic__"

if [ ! -f "$WARMSTART_CKPT" ]; then
    echo "ERROR: warmstart checkpoint not found: $WARMSTART_CKPT"
    exit 1
fi

mkdir -p "$OUTDIR"
echo "[$(date -u)] Starting main PPO chain: arch=control_feat_gnn_card_attn, $N_ITER iters" | tee "$LOG"
echo "[$(date -u)] Checkpoint: $WARMSTART_CKPT" | tee -a "$LOG"

PYTHONPATH=build-ninja/bindings nice -n 10 uv run python scripts/train_ppo.py \
    --checkpoint "$WARMSTART_CKPT" \
    --out-dir "$OUTDIR" \
    --n-iterations "$N_ITER" \
    --games-per-iter 200 \
    --lr 1e-4 \
    --clip-eps 0.12 \
    --ent-coef 0.01 --ent-coef-final 0.003 \
    --global-ent-decay-start 0 --global-ent-decay-end 300 \
    --max-kl 0.03 \
    --ema-decay 0.995 \
    --upgo \
    --reset-optimizer \
    --league "$OUTDIR" \
    --league-save-every 10 \
    --league-mix-k 6 \
    --league-fixtures $PANEL_FIX \
    --league-recency-tau 50 \
    --league-fixture-fadeout 999 \
    --pfsp-exponent 1.5 \
    --heuristic-floor 0.15 \
    --self-play-heuristic-mix 0.5 \
    --device cuda \
    --eval-every 10 \
    --eval-panel __heuristic__ \
    --wandb \
    --wandb-run-name "ppo_gnn_card_attn_v1" \
    --skip-smoke-test \
    2>&1 | tee -a "$LOG"

echo "[$(date -u)] Done." | tee -a "$LOG"
