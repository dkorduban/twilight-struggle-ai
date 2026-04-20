#!/bin/bash
set -e

V56_CKPT="data/checkpoints/ppo_v56_league/ppo_best_6mode.pt"

echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Starting capacity test: USSR-only PPO from v56 (no league, no EMA)"

PYTHONPATH=build-ninja/bindings nice -n 10 uv run python scripts/train_ppo.py \
  --checkpoint "$V56_CKPT" \
  --out-dir results/capacity_test/ppo_ussr_only \
  --side ussr \
  --n-iterations 20 \
  --games-per-iter 200 \
  --lr 5e-5 --clip-eps 0.12 --ent-coef 0.01 --max-kl 0.03 \
  --ema-decay 0.0 \
  --reset-optimizer \
  --device cuda \
  --wandb \
  --wandb-run-name capacity_ussr_only_v3

echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] USSR-only done. Starting US-only PPO from v56"

PYTHONPATH=build-ninja/bindings nice -n 10 uv run python scripts/train_ppo.py \
  --checkpoint "$V56_CKPT" \
  --out-dir results/capacity_test/ppo_us_only \
  --side us \
  --n-iterations 20 \
  --games-per-iter 200 \
  --lr 5e-5 --clip-eps 0.12 --ent-coef 0.01 --max-kl 0.03 \
  --ema-decay 0.0 \
  --reset-optimizer \
  --device cuda \
  --wandb \
  --wandb-run-name capacity_us_only_v3

echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Both capacity test PPO runs complete"
