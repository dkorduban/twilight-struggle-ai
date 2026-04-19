#!/bin/bash
# Launch PPO v3: waits for PPO v2 to complete, then starts from best fixed-engine AWR warmstart.
# Usage: bash scripts/launch_ppo_v3.sh [--arch <arch>] [--no-wait]
# Run in background: nohup bash scripts/launch_ppo_v3.sh &
set -e

ARCH="${ARCH:-control_feat_gnn_card_attn}"
NO_WAIT="${NO_WAIT:-0}"
N_ITER="${N_ITER:-200}"

OUTDIR="results/ppo_gnn_card_attn_v3"
LOG="$OUTDIR/train_v3_launch.log"
PPO_V2_LOCK="results/train_ppo.lock"

# AWR warmstart candidates (in preference order)
AWR_CANDIDATES=(
  "results/awr_sweep/fixed_engine_full.json"          # from fixed-engine pipeline
  "results/awr_sweep/ppo_warmstart_control_feat_gnn_card_attn/ppo_warmstart_scripted.pt"  # old warmstart
)

mkdir -p "$OUTDIR"
echo "[$(date -u)] launch_ppo_v3.sh started (arch=$ARCH, n_iter=$N_ITER)" | tee "$LOG"

# Wait for PPO v2 to finish (release lock)
if [ "$NO_WAIT" = "0" ] && [ -f "$PPO_V2_LOCK" ]; then
  echo "[$(date -u)] Waiting for PPO v2 to complete (lock: $PPO_V2_LOCK)..." | tee -a "$LOG"
  until [ ! -f "$PPO_V2_LOCK" ]; do sleep 60; done
  echo "[$(date -u)] PPO v2 completed. Starting PPO v3..." | tee -a "$LOG"
else
  echo "[$(date -u)] Skipping wait (no-wait or no lock file)." | tee -a "$LOG"
fi

# Find best AWR checkpoint
WARMSTART_CKPT=""
FULL_JSON="results/awr_sweep/fixed_engine_full.json"
if [ -f "$FULL_JSON" ]; then
  WARMSTART_CKPT=$(python3 -c "
import json
d = json.load(open('$FULL_JSON'))
runs = d.get('runs', [])
if runs:
    best = max(runs, key=lambda x: x.get('val_adv_card_acc', 0))
    print(best.get('checkpoint_path', ''))
" 2>/dev/null)
fi

# Fallback: use existing PPO v2 best as warmstart
if [ -z "$WARMSTART_CKPT" ] || [ ! -f "$WARMSTART_CKPT" ]; then
  echo "[$(date -u)] WARNING: fixed-engine AWR checkpoint not found. Using PPO v2 best as warmstart." | tee -a "$LOG"
  WARMSTART_CKPT="results/ppo_gnn_card_attn_v2/ppo_best.pt"
fi

if [ ! -f "$WARMSTART_CKPT" ]; then
  echo "[$(date -u)] ERROR: No warmstart checkpoint found." | tee -a "$LOG"
  exit 1
fi

echo "[$(date -u)] Warmstart checkpoint: $WARMSTART_CKPT" | tee -a "$LOG"

# Panel fixtures (same as v2)
PANEL_FIX="
    results/capacity_test/ppo_ussr_only_v5/ppo_best_scripted.pt
    results/capacity_test/ppo_us_only_v5/ppo_best_scripted.pt
    data/checkpoints/scripted_for_elo/v44_scripted.pt
    data/checkpoints/scripted_for_elo/v55_scripted.pt
    data/checkpoints/scripted_for_elo/v56_scripted.pt
    data/checkpoints/scripted_for_elo/v54_scripted.pt
    data/checkpoints/scripted_for_elo/v20_scripted.pt
    __heuristic__
"

# If warmstart is a .pt AWR checkpoint (not scripted), load via --checkpoint
# If it's a scripted model, use it directly (train_ppo.py handles both)
echo "[$(date -u)] Launching PPO v3 ($N_ITER iters, arch=$ARCH)..." | tee -a "$LOG"
echo "[$(date -u)] CMD: uv run python scripts/train_ppo.py --checkpoint $WARMSTART_CKPT --out-dir $OUTDIR --n-iterations $N_ITER ..." | tee -a "$LOG"

PYTHONUNBUFFERED=1 PYTHONPATH=build-ninja/bindings nice -n 15 uv run python scripts/train_ppo.py \
    --checkpoint "$WARMSTART_CKPT" \
    --out-dir "$OUTDIR" \
    --n-iterations "$N_ITER" \
    --games-per-iter 200 \
    --lr 5e-5 \
    --clip-eps 0.10 \
    --ent-coef 0.005 --ent-coef-final 0.001 \
    --global-ent-decay-start 0 --global-ent-decay-end "$N_ITER" \
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
    --wandb-run-name ppo_gnn_card_attn_v3 \
    --skip-smoke-test \
    2>&1 | tee -a "$OUTDIR/train.log"

echo "[$(date -u)] PPO v3 training complete." | tee -a "$LOG"
