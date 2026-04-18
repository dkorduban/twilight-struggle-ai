#!/bin/bash
# AWR evaluation chain: Phase 1 → analyze → Phase 2 (if needed) → log results
# Designed to run in background after Phase 1 completes.
# Usage: bash scripts/awr_chain.sh  (assumes Phase 1 already running)

set -e
LOG="results/awr_sweep/panel_v5_sweep.log"
P1_JSON="results/awr_sweep/panel_v5_full.json"

echo "[$(date -u)] awr_chain.sh: waiting for Phase 1 JSON..." | tee -a "$LOG"

# Wait for Phase 1 JSON
until [ -f "$P1_JSON" ]; do sleep 30; done

echo "[$(date -u)] Phase 1 complete. Analyzing results..." | tee -a "$LOG"

# Print Phase 1 analysis for reference
echo "[$(date -u)] Phase 1 analysis:" | tee -a "$LOG"
PYTHONPATH=python uv run python scripts/analyze_awr_results.py "$P1_JSON" --top 5 2>&1 | tee -a "$LOG"

# Phase 2 fixed architecture list (per Opus analysis 2026-04-17):
# - GNN models are 2.5x faster than attn for statistically identical accuracy
# - FiLM adds nothing measurable over side conditioning
# - card_attn is the new model to validate
# - country_attn_side kept as 1 attn slot for comparison to current PPO baseline
echo "[$(date -u)] Launching Phase 2: fixed archs [gnn_side, card_attn, country_attn_side, baseline] (3 seeds, 2 taus)" | tee -a "$LOG"

PYTHONPATH=python nice -n 15 uv run python scripts/arch_sweep_awr.py \
  --data data/awr_eval/awr_panel_v5.parquet \
  --archs control_feat_gnn_side control_feat_gnn_card_attn country_attn_side baseline \
  --hidden-dims 256 \
  --taus 0.5 1.0 \
  --seeds 42 43 44 \
  --epochs 5 \
  --device cuda \
  --out results/awr_sweep/panel_v5_phase2.json \
  2>&1 | tee -a "$LOG"

echo "[$(date -u)] Phase 2 complete." | tee -a "$LOG"

# Phase 2 analysis — identify winner
echo "[$(date -u)] Phase 2 analysis:" | tee -a "$LOG"
PYTHONPATH=python uv run python scripts/analyze_awr_results.py \
  results/awr_sweep/panel_v5_phase2.json \
  --top 3 2>&1 | tee -a "$LOG"

# Phase 2b: hidden_dim=384 for best GNN arch
# Test control_feat_gnn_side and control_feat_gnn_card_attn at 384 to check capacity
echo "[$(date -u)] Phase 2b: hidden_dim=384 capacity test for top GNN archs (3 seeds, tau=1.0)" | tee -a "$LOG"
PYTHONPATH=python nice -n 15 uv run python scripts/arch_sweep_awr.py \
  --data data/awr_eval/awr_panel_v5.parquet \
  --archs control_feat_gnn_side control_feat_gnn_card_attn \
  --hidden-dims 256 384 \
  --taus 1.0 \
  --seeds 42 43 44 \
  --epochs 5 \
  --device cuda \
  --out results/awr_sweep/panel_v5_hidden_dim.json \
  2>&1 | tee -a "$LOG"

echo "[$(date -u)] Phase 2b complete." | tee -a "$LOG"
echo "[$(date -u)] hidden_dim comparison:" | tee -a "$LOG"
PYTHONPATH=python uv run python scripts/analyze_awr_results.py \
  results/awr_sweep/panel_v5_hidden_dim.json \
  --top 4 2>&1 | tee -a "$LOG"

echo "[$(date -u)] AWR evaluation chain complete. Check results for best architecture." | tee -a "$LOG"
