#!/bin/bash
# Collect AWR panel v6: {ussr_only_v5, us_only_v5, v44, v55, v56, v54, v20} + heuristic + round-robin.
# Uses distinct model names to fix the ppo_best_scripted naming collision from panel v5.
# Output: data/awr_eval/awr_panel_v6.parquet (Parquet zstd)
set -e

OUT="data/awr_eval/awr_panel_v6.parquet"
GAMES_VS_HEURISTIC=200   # per model (split 50/50 USSR/US)
GAMES_PER_PAIR=100        # per ordered pair in round-robin
POOL=64
SEED=62000

echo "[$(date -u)] Collecting panel v6 → $OUT"
echo "Models: ussr_only_v5, us_only_v5, v44, v55, v56, v54, v20"
echo "Heuristic games: $GAMES_VS_HEURISTIC per model"
echo "Round-robin pairs: $GAMES_PER_PAIR per pair"
echo ""

PYTHONUNBUFFERED=1 PYTHONPATH=python:build-ninja/bindings nice -n 15 uv run python scripts/collect_awr_data.py \
    --models \
        results/capacity_test/ppo_ussr_only_v5/ppo_best_scripted.pt \
        results/capacity_test/ppo_us_only_v5/ppo_best_scripted.pt \
        data/checkpoints/scripted_for_elo/v44_scripted.pt \
        data/checkpoints/scripted_for_elo/v55_scripted.pt \
        data/checkpoints/scripted_for_elo/v56_scripted.pt \
        data/checkpoints/scripted_for_elo/v54_scripted.pt \
        data/checkpoints/scripted_for_elo/v20_scripted.pt \
    --model-names \
        ussr_only_v5 \
        us_only_v5 \
        v44 \
        v55 \
        v56 \
        v54 \
        v20 \
    --games-per-model "$GAMES_VS_HEURISTIC" \
    --games-per-pair "$GAMES_PER_PAIR" \
    --round-robin \
    --pool-size "$POOL" \
    --seed "$SEED" \
    --out "$OUT" \
    2>&1 | tee results/capacity_test/collect_panel_v6.log

echo ""
echo "[$(date -u)] Done. Written to $OUT"
