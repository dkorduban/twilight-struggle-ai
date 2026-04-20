#!/bin/bash
# GNN PPO v15: control_feat_gnn_side architecture warm-started from BC v2
# BC v2 trained on 3M rows: 334K v13_iter20 games + 2.7M heuristic nash
# Prerequisites: results/bc_gnn_side_v2/baseline_best.pt must exist

set -euo pipefail
cd "$(dirname "$0")/.."

BC_CHECKPOINT="results/bc_gnn_side_v2/baseline_best.pt"
if [ ! -f "$BC_CHECKPOINT" ]; then
    echo "ERROR: BC checkpoint not found: $BC_CHECKPOINT"
    exit 1
fi

mkdir -p results/ppo_gnn_side_v15

echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] Launching GNN PPO v15 from BC v2 checkpoint" | tee -a results/autonomous_decisions.log
echo "Checkpoint: $BC_CHECKPOINT" | tee -a results/autonomous_decisions.log

OMP_NUM_THREADS=6 KMP_BLOCKTIME=0 nohup uv run python scripts/train_ppo.py \
  --checkpoint "$BC_CHECKPOINT" \
  --reset-optimizer \
  --out-dir results/ppo_gnn_side_v15 \
  --version gnn_side_v15 \
  --n-iterations 80 \
  --games-per-iter 200 \
  --ppo-epochs 4 \
  --clip-eps 0.12 \
  --lr 5e-5 \
  --lr-schedule constant \
  --lr-warmup-iters 0 \
  --gamma 0.99 --gae-lambda 0.95 \
  --ent-coef 0.01 --ent-coef-final 0.003 \
  --global-ent-decay-start 0 --global-ent-decay-end 300 \
  --vf-coef 0.5 \
  --minibatch-size 2048 \
  --eval-panel \
    data/checkpoints/scripted_for_elo/v56_scripted.pt \
    __heuristic__ \
  --eval-every 10 \
  --side both \
  --seed 42000 --device cuda \
  --wandb --wandb-project twilight-struggle-ai \
  --wandb-run-name ppo_gnn_side_v15_seed42000 \
  --league results/ppo_gnn_side_v15 \
  --league-save-every 10 \
  --league-fixtures \
    data/checkpoints/scripted_for_elo/v56_scripted.pt \
    data/checkpoints/scripted_for_elo/v55_scripted.pt \
    data/checkpoints/scripted_for_elo/v54_scripted.pt \
    data/checkpoints/scripted_for_elo/v44_scripted.pt \
    data/checkpoints/scripted_for_elo/v20_scripted.pt \
    results/capacity_test/ppo_ussr_only_v5/ppo_best_scripted.pt \
    results/capacity_test/ppo_us_only_v5/ppo_best_scripted.pt \
    __heuristic__ \
  --heuristic-floor 0.15 \
  --league-fixture-fadeout 999 \
  --upgo \
  --jsd-probe-path data/probe_positions.parquet \
  --jsd-probe-interval 10 \
  --jsd-probe-bc-checkpoint data/checkpoints/ppo_v56_league/ppo_best_6mode_scripted.pt \
  --rollout-temp 1.0 \
  --max-kl 0.1 \
  --skip-smoke-test \
  > results/ppo_gnn_side_v15/train.log 2>&1 &

GNN_PID=$!
echo "GNN PPO v15 PID: $GNN_PID" | tee -a results/autonomous_decisions.log
echo "$GNN_PID" > results/ppo_gnn_side_v15/pid.txt
