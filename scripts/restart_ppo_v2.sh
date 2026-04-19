#!/bin/bash
# PPO chain v2 — resumes from ppo_gnn_card_attn_v1 best checkpoint.
# Improvements over v1:
#   - dense_reward_alpha=0.1 (delta_vp shaped rewards, annealed over 200k steps)
#   - heuristic_floor=0.25 (25% vs 15%: stronger regression prevention, helps US side)
#   - dense_reward_anneal_steps=150000 (80% of expected 300-iter training)
#   - wandb-run-name distinguishes v2 clearly
#
# Usage: bash scripts/restart_ppo_v2.sh [checkpoint_path] [n_iterations]
#   checkpoint_path: defaults to results/ppo_gnn_card_attn_v1/ppo_best.pt
#   n_iterations: defaults to 200
set -e

CKPT="${1:-results/ppo_gnn_card_attn_v1/ppo_best.pt}"
N_ITER="${2:-200}"
OUTDIR="results/ppo_gnn_card_attn_v2"
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

if [ ! -f "$CKPT" ]; then
    echo "ERROR: checkpoint not found: $CKPT"
    exit 1
fi

mkdir -p "$OUTDIR"
echo "[$(date -u)] Starting PPO v2 chain: $N_ITER iters from $CKPT" | tee "$LOG"

PYTHONPATH=build-ninja/bindings nice -n 10 uv run python scripts/train_ppo.py \
    --checkpoint "$CKPT" \
    --out-dir "$OUTDIR" \
    --n-iterations "$N_ITER" \
    --games-per-iter 200 \
    --lr 5e-5 \
    --clip-eps 0.10 \
    --ent-coef 0.005 --ent-coef-final 0.001 \
    --global-ent-decay-start 0 --global-ent-decay-end 200 \
    --max-kl 0.02 \
    --val-calib-coef 0.1 \
    --ema-decay 0.995 \
    --upgo \
    --reset-optimizer \
    --dense-reward-alpha 0.1 \
    --dense-reward-anneal-steps 150000 \
    --league "$OUTDIR" \
    --league-save-every 10 \
    --league-mix-k 6 \
    --league-fixtures $PANEL_FIX \
    --league-recency-tau 50 \
    --league-fixture-fadeout 999 \
    --pfsp-exponent 1.5 \
    --heuristic-floor 0.25 \
    --self-play-heuristic-mix 0.6 \
    --device cuda \
    --eval-every 10 \
    --eval-panel $PANEL_FIX \
    --jsd-probe-path data/probe_positions.parquet \
    --jsd-probe-interval 10 \
    --jsd-probe-bc-checkpoint results/awr_sweep/ppo_warmstart_control_feat_gnn_card_attn/ppo_warmstart_scripted.pt \
    --wandb \
    --wandb-run-name "ppo_gnn_card_attn_v2" \
    --skip-smoke-test \
    2>&1 | tee -a "$LOG"

echo "[$(date -u)] Done." | tee -a "$LOG"
