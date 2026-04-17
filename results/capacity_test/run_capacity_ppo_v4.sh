#!/bin/bash
set -e

# Capacity test v4: 80 iters, matching main chain hyperparams EXACTLY including league.
# Key difference from v3: uses --league with per-side fixture pools (not just heuristic).
# The --side flag now works with league (collect_rollout_league_batched respects it).
# Previous v3 test (20 iters, heuristic-only) was inconclusive — both curves still trending up.

V56_CKPT="data/checkpoints/ppo_v56_league/ppo_best_6mode.pt"

# Fixture lists (same as main chain v309)
USSR_FIX="data/checkpoints/scripted_for_elo/v56_scripted.pt data/checkpoints/scripted_for_elo/v44_scripted.pt data/checkpoints/scripted_for_elo/v54_scripted.pt data/checkpoints/scripted_for_elo/v20_scripted.pt data/checkpoints/scripted_for_elo/v55_scripted.pt data/checkpoints/scripted_for_elo/v22_scripted.pt data/checkpoints/scripted_for_elo/v45_scripted.pt data/checkpoints/scripted_for_elo/v57_scripted.pt __heuristic__"
US_FIX="data/checkpoints/scripted_for_elo/v54_scripted.pt data/checkpoints/scripted_for_elo/v55_scripted.pt data/checkpoints/scripted_for_elo/v56_scripted.pt data/checkpoints/scripted_for_elo/v44_scripted.pt data/checkpoints/scripted_for_elo/v20_scripted.pt data/checkpoints/scripted_for_elo/v22_scripted.pt data/checkpoints/scripted_for_elo/v58_scripted.pt data/checkpoints/scripted_for_elo/v46_scripted.pt __heuristic__"
ALL_FIX="data/checkpoints/scripted_for_elo/v56_scripted.pt data/checkpoints/scripted_for_elo/v44_scripted.pt data/checkpoints/scripted_for_elo/v54_scripted.pt data/checkpoints/scripted_for_elo/v20_scripted.pt data/checkpoints/scripted_for_elo/v55_scripted.pt data/checkpoints/scripted_for_elo/v22_scripted.pt data/checkpoints/scripted_for_elo/v45_scripted.pt data/checkpoints/scripted_for_elo/v57_scripted.pt data/checkpoints/scripted_for_elo/v58_scripted.pt data/checkpoints/scripted_for_elo/v46_scripted.pt __heuristic__"

# Clean previous outputs
rm -f results/capacity_test/ppo_ussr_only_v4/*.pt results/capacity_test/ppo_ussr_only_v4/*.json results/capacity_test/ppo_ussr_only_v4/*.txt 2>/dev/null
rm -f results/capacity_test/ppo_us_only_v4/*.pt results/capacity_test/ppo_us_only_v4/*.json results/capacity_test/ppo_us_only_v4/*.txt 2>/dev/null
mkdir -p results/capacity_test/ppo_ussr_only_v4 results/capacity_test/ppo_us_only_v4

echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Starting capacity test v4: USSR-only PPO from v56, 80 iters, league with one-sided pools"

PYTHONPATH=build-ninja/bindings nice -n 10 uv run python scripts/train_ppo.py \
  --checkpoint "$V56_CKPT" \
  --out-dir results/capacity_test/ppo_ussr_only_v4 \
  --side ussr \
  --n-iterations 80 \
  --games-per-iter 200 \
  --lr 5e-5 --clip-eps 0.12 \
  --ent-coef 0.01 --ent-coef-final 0.003 \
  --global-ent-decay-start 0 --global-ent-decay-end 300 \
  --max-kl 0.03 \
  --ema-decay 0.995 \
  --upgo \
  --reset-optimizer \
  --league results/capacity_test/ppo_ussr_only_v4 \
  --league-save-every 10 \
  --league-mix-k 6 \
  --ussr-league-fixtures $USSR_FIX \
  --us-league-fixtures $US_FIX \
  --league-fixtures $ALL_FIX \
  --league-recency-tau 50 \
  --league-fixture-fadeout 999 \
  --pfsp-exponent 0.5 \
  --heuristic-floor 0.15 \
  --device cuda \
  --wandb \
  --wandb-run-name capacity_ussr_only_v4 \
  --skip-smoke-test

echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] USSR-only done. Starting US-only PPO from v56"

PYTHONPATH=build-ninja/bindings nice -n 10 uv run python scripts/train_ppo.py \
  --checkpoint "$V56_CKPT" \
  --out-dir results/capacity_test/ppo_us_only_v4 \
  --side us \
  --n-iterations 80 \
  --games-per-iter 200 \
  --lr 5e-5 --clip-eps 0.12 \
  --ent-coef 0.01 --ent-coef-final 0.003 \
  --global-ent-decay-start 0 --global-ent-decay-end 300 \
  --max-kl 0.03 \
  --ema-decay 0.995 \
  --upgo \
  --reset-optimizer \
  --league results/capacity_test/ppo_us_only_v4 \
  --league-save-every 10 \
  --league-mix-k 6 \
  --ussr-league-fixtures $USSR_FIX \
  --us-league-fixtures $US_FIX \
  --league-fixtures $ALL_FIX \
  --league-recency-tau 50 \
  --league-fixture-fadeout 999 \
  --pfsp-exponent 0.5 \
  --heuristic-floor 0.15 \
  --device cuda \
  --wandb \
  --wandb-run-name capacity_us_only_v4 \
  --skip-smoke-test

echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Both capacity test v4 runs complete"
