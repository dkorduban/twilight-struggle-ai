#!/bin/bash
# Round-robin model-vs-model collection for AWR eval.
# Run AFTER the vs-heuristic collection completes.
set -e

PYTHONPATH=build-ninja/bindings nice -n 15 uv run python scripts/collect_awr_data.py \
  --models \
    data/checkpoints/scripted_for_elo/v56_scripted.pt \
    data/checkpoints/scripted_for_elo/v54_scripted.pt \
    data/checkpoints/scripted_for_elo/v44_scripted.pt \
    data/checkpoints/scripted_for_elo/v20_scripted.pt \
    data/checkpoints/scripted_for_elo/v55_scripted.pt \
    results/capacity_test/ppo_ussr_only_v5/ppo_best_scripted.pt \
    results/capacity_test/ppo_us_only_v5/ppo_best_scripted.pt \
  --games-per-model 0 \
  --round-robin \
  --games-per-pair 300 \
  --out data/awr_eval/awr_panel_v5.parquet \
  --append \
  --seed 55000 \
  --pool-size 64
