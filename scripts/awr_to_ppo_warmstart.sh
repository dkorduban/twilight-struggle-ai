#!/bin/bash
# Mini-PPO warm-start from best AWR checkpoint.
# Usage: bash scripts/awr_to_ppo_warmstart.sh <awr_best.pt> [n_iterations]
#
# Loads the AWR checkpoint (train_ppo.py supports awr_best.pt directly via
# model_state_dict key), runs short PPO to validate the arch produces
# real improvement over v56 baseline.
#
# Expected: combined WR improves vs heuristic + panel models after 10-15 iters.
set -e

AWR_CKPT="${1:?Usage: $0 <awr_best.pt> [n_iterations]}"
N_ITER="${2:-15}"

if [ ! -f "$AWR_CKPT" ]; then
    echo "ERROR: checkpoint not found: $AWR_CKPT"
    exit 1
fi

ARCH=$(PYTHONPATH=python uv run python -c "
import torch
ckpt = torch.load('$AWR_CKPT', map_location='cpu', weights_only=False)
args = ckpt.get('args', {})
print(args.get('model_type', 'unknown'))
" 2>/dev/null)

echo "[$(date -u)] AWR→PPO warm-start: arch=$ARCH, checkpoint=$AWR_CKPT, iterations=$N_ITER"

# Output directory: named after arch
OUTDIR="results/awr_sweep/ppo_warmstart_${ARCH}"
mkdir -p "$OUTDIR"
LOG="$OUTDIR/warmstart.log"

# Panel opponents for league fixtures (same as capacity test v5)
PANEL_FIX="
    results/capacity_test/ppo_ussr_only_v5/ppo_best_scripted.pt
    results/capacity_test/ppo_us_only_v5/ppo_best_scripted.pt
    data/checkpoints/scripted_for_elo/v56_scripted.pt
    data/checkpoints/scripted_for_elo/v55_scripted.pt
    data/checkpoints/scripted_for_elo/v54_scripted.pt
    data/checkpoints/scripted_for_elo/v44_scripted.pt
    data/checkpoints/scripted_for_elo/v20_scripted.pt
    __heuristic__
"

echo "[$(date -u)] Starting PPO warm-start: $N_ITER iterations" | tee "$LOG"

PYTHONUNBUFFERED=1 PYTHONPATH=build-ninja/bindings nice -n 15 uv run python scripts/train_ppo.py \
    --checkpoint "$AWR_CKPT" \
    --out-dir "$OUTDIR" \
    --n-iterations "$N_ITER" \
    --games-per-iter 200 \
    --lr 3e-5 \
    --clip-eps 0.12 \
    --ent-coef 0.01 --ent-coef-final 0.003 \
    --global-ent-decay-start 0 --global-ent-decay-end "$((N_ITER * 2))" \
    --max-kl 0.03 \
    --ema-decay 0.995 \
    --upgo \
    --reset-optimizer \
    --league "$OUTDIR" \
    --league-save-every 5 \
    --league-mix-k 4 \
    --league-fixtures $PANEL_FIX \
    --league-recency-tau 30 \
    --league-fixture-fadeout 999 \
    --pfsp-exponent 1.5 \
    --heuristic-floor 0.15 \
    --self-play-heuristic-mix 0.5 \
    --device cuda \
    --eval-every 5 \
    --skip-smoke-test \
    2>&1 | tee -a "$LOG"

echo "" | tee -a "$LOG"
echo "[$(date -u)] PPO warm-start done. Benchmarking best checkpoint..." | tee -a "$LOG"

# Find best checkpoint
BEST_PPO=$(ls -t "$OUTDIR"/*.pt 2>/dev/null | grep -v scripted | head -1)
if [ -z "$BEST_PPO" ]; then
    echo "WARNING: no checkpoint found in $OUTDIR"
    exit 0
fi

echo "[$(date -u)] Benchmarking $BEST_PPO" | tee -a "$LOG"

# Benchmark vs full panel
PYTHONUNBUFFERED=1 PYTHONPATH=python:build-ninja/bindings nice -n 15 uv run python \
    scripts/benchmark_awr_checkpoint.py \
    --checkpoint "$BEST_PPO" \
    --scripted-out "$OUTDIR/ppo_warmstart_scripted.pt" \
    --vs \
        results/capacity_test/ppo_ussr_only_v5/ppo_best_scripted.pt \
        results/capacity_test/ppo_us_only_v5/ppo_best_scripted.pt \
        data/checkpoints/scripted_for_elo/v44_scripted.pt \
        data/checkpoints/scripted_for_elo/v55_scripted.pt \
        data/checkpoints/scripted_for_elo/v56_scripted.pt \
        data/checkpoints/scripted_for_elo/v54_scripted.pt \
        data/checkpoints/scripted_for_elo/v20_scripted.pt \
    --vs-heuristic \
    --n-games 200 \
    --pool 32 \
    --seed 90000 \
    2>&1 | tee -a "$LOG"

echo "" | tee -a "$LOG"
echo "[$(date -u)] Done. Results in $LOG" | tee -a "$LOG"
echo "Scripted checkpoint: $OUTDIR/ppo_warmstart_scripted.pt" | tee -a "$LOG"
