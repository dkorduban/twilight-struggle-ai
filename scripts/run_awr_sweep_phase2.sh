#!/bin/bash
# AWR architecture sweep Phase 2:
# Validate top-3 from Phase 1 with full tau sweep + 3 seeds
# Also test the new card cross-attention model
# Usage: bash scripts/run_awr_sweep_phase2.sh arch1 arch2 arch3

set -e
DATA="data/awr_eval/awr_panel_v5.parquet"
OUT="results/awr_sweep/panel_v5_phase2.json"
LOG="results/awr_sweep/panel_v5_sweep.log"

# Read top-3 from Phase 1 results (or use defaults)
ARCH1="${1:-control_feat_gnn_film}"
ARCH2="${2:-country_attn_film}"
ARCH3="${3:-control_feat_gnn_side}"

echo "[$(date -u)] Starting AWR sweep Phase 2: $ARCH1 $ARCH2 $ARCH3 + card_attn" | tee -a "$LOG"

PYTHONPATH=python nice -n 15 uv run python scripts/arch_sweep_awr.py \
  --data "$DATA" \
  --archs \
    "$ARCH1" \
    "$ARCH2" \
    "$ARCH3" \
    control_feat_gnn_card_attn \
  --hidden-dims 256 \
  --taus 0.5 1.0 2.0 1000.0 \
  --seeds 42 43 44 \
  --epochs 5 \
  --device cuda \
  --out "$OUT" \
  2>&1 | tee -a "$LOG"

echo "[$(date -u)] Phase 2 complete. Results at $OUT" | tee -a "$LOG"

# Test top-1 arch with hidden_dim=384
echo "[$(date -u)] Phase 2b: hidden_dim=384 for best arch ($ARCH1)" | tee -a "$LOG"
PYTHONPATH=python nice -n 15 uv run python scripts/arch_sweep_awr.py \
  --data "$DATA" \
  --archs "$ARCH1" \
  --hidden-dims 256 384 \
  --taus 1.0 \
  --seeds 42 43 44 \
  --epochs 5 \
  --device cuda \
  --out "results/awr_sweep/panel_v5_hidden_dim.json" \
  2>&1 | tee -a "$LOG"

echo "[$(date -u)] Phase 2b complete." | tee -a "$LOG"
