#!/bin/bash
# AWR architecture sweep on awr_panel_v5 dataset
# Phase 1: 9 archs x 2 taus x 1 seed = 18 runs (fast ranking)
# Phase 2: top-3 archs x 4 taus x 3 seeds = up to 36 runs (validation)
# Dataset loaded ONCE for all experiments (10x speedup)

set -e
DATA="data/awr_eval/awr_panel_v5.parquet"
OUT="results/awr_sweep/panel_v5_full.json"
LOG="results/awr_sweep/panel_v5_sweep.log"

mkdir -p results/awr_sweep

echo "[$(date -u)] Starting AWR sweep (Phase 1: 18 runs) on $DATA" | tee -a "$LOG"

PYTHONPATH=python nice -n 15 uv run python scripts/arch_sweep_awr.py \
  --data "$DATA" \
  --archs \
    baseline \
    control_feat_gnn_side \
    control_feat_gnn_film \
    country_attn_side \
    country_attn_side_policy \
    country_attn_film \
    direct_country \
    control_feat \
    full_embed \
  --hidden-dims 256 \
  --taus 0.5 1.0 \
  --seeds 42 \
  --epochs 5 \
  --device cuda \
  --out "$OUT" \
  2>&1 | tee -a "$LOG"

echo "[$(date -u)] Phase 1 complete. Results at $OUT" | tee -a "$LOG"
