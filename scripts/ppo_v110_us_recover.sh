#!/bin/bash
# PPO-continue cheap test: US-side recovery on post-Plan-B engine.
# Hypothesis (advisor 2026-04-21): v32's combined=0.464 drop is asymmetric
# (USSR 0.650→0.654 noise, US 0.512→0.274 collapse). US collapse == policy
# over-fit to buggy engine dynamics (Camp David, SALT, Yuri, etc). PPO is
# the native tool for dynamics adaptation.
#
# Cheap test: 10 iters, --side us, small LR, fixed engine.
# Kill: combined <0.55 → fall back to BC (task #109).
set -e

WARMSTART_CKPT="results/ppo_v32_continue/ppo_best.pt"
OUTDIR="results/ppo_v110_us_recover"
LOG="$OUTDIR/train.log"

PANEL="\
data/checkpoints/scripted_for_elo/v56_scripted.pt \
data/checkpoints/scripted_for_elo/v55_scripted.pt \
data/checkpoints/scripted_for_elo/v44_scripted.pt \
__heuristic__"

if [ ! -f "$WARMSTART_CKPT" ]; then
    echo "ERROR: warmstart checkpoint not found: $WARMSTART_CKPT"
    exit 1
fi

mkdir -p "$OUTDIR"
echo "[$(date -u)] Launching v110 US-recovery PPO continue from v32_continue" | tee "$LOG"
echo "[$(date -u)] Engine head: abe69f3 + fb9e814 (Plan B + Camp David)" | tee -a "$LOG"

PYTHONPATH=build-ninja/bindings nice -n 10 uv run python scripts/train_ppo.py \
    --checkpoint "$WARMSTART_CKPT" \
    --out-dir "$OUTDIR" \
    --version "v110_us_recover" \
    --n-iterations 10 \
    --games-per-iter 200 \
    --side us \
    --ppo-epochs 1 \
    --lr 3e-6 \
    --lr-schedule constant \
    --clip-eps 0.05 \
    --ent-coef 0.01 --ent-coef-final 0.003 \
    --max-kl 0.5 --target-kl 0.015 \
    --val-calib-coef 0.0 \
    --ema-decay 0.995 \
    --reset-optimizer \
    --league "$OUTDIR" \
    --league-save-every 10 \
    --league-mix-k 4 \
    --league-fixtures $PANEL \
    --league-recency-tau 20 \
    --league-fixture-fadeout 999 \
    --pfsp-exponent 1.0 \
    --heuristic-floor 0.5 \
    --self-play-heuristic-mix 0.2 \
    --device cuda \
    --eval-every 5 \
    --eval-panel $PANEL \
    --panel-heuristic-weight 3.0 \
    --skip-smoke-test \
    --seed 55555 \
    2>&1 | tee -a "$LOG"

echo "[$(date -u)] v110 PPO done; bench next." | tee -a "$LOG"
