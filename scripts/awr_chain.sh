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

# Analyze and get top-3 architectures
TOP3=$(PYTHONPATH=python uv run python scripts/analyze_awr_results.py "$P1_JSON" --top 3 --emit-phase2-cmd 2>&1)
echo "$TOP3" | tee -a "$LOG"

# Extract top-3 arch names from the analysis output
ARCH1=$(echo "$TOP3" | grep "^  1\." | grep -oP 'control_feat_gnn_\S+|country_attn_\S+|baseline|full_embed|direct_country|control_feat\b')
ARCH2=$(echo "$TOP3" | grep "^  2\." | grep -oP 'control_feat_gnn_\S+|country_attn_\S+|baseline|full_embed|direct_country|control_feat\b')
ARCH3=$(echo "$TOP3" | grep "^  3\." | grep -oP 'control_feat_gnn_\S+|country_attn_\S+|baseline|full_embed|direct_country|control_feat\b')

# Fallback defaults
ARCH1="${ARCH1:-control_feat_gnn_film}"
ARCH2="${ARCH2:-country_attn_film}"
ARCH3="${ARCH3:-control_feat_gnn_side}"

echo "[$(date -u)] Top-3: $ARCH1, $ARCH2, $ARCH3" | tee -a "$LOG"

# Check if Phase 2 fits in time (estimate 2 seeds x 4 archs x 2 taus x 146s = ~23 min)
echo "[$(date -u)] Launching Phase 2: top-3 + card_attn (2 seeds, 2 taus)" | tee -a "$LOG"

PYTHONPATH=python nice -n 15 uv run python scripts/arch_sweep_awr.py \
  --data data/awr_eval/awr_panel_v5.parquet \
  --archs "$ARCH1" "$ARCH2" "$ARCH3" control_feat_gnn_card_attn \
  --hidden-dims 256 \
  --taus 0.5 1.0 \
  --seeds 42 43 \
  --epochs 5 \
  --device cuda \
  --out results/awr_sweep/panel_v5_phase2.json \
  2>&1 | tee -a "$LOG"

echo "[$(date -u)] Phase 2 complete." | tee -a "$LOG"

# Final analysis
echo "[$(date -u)] Final results comparison:" | tee -a "$LOG"
PYTHONPATH=python uv run python scripts/analyze_awr_results.py \
  results/awr_sweep/panel_v5_phase2.json \
  --top 3 2>&1 | tee -a "$LOG"

echo "[$(date -u)] AWR evaluation chain complete. Check results for best architecture." | tee -a "$LOG"
