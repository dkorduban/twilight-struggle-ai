#!/bin/bash
# v15 pipeline:
#   1. Filter combined_v13 → combined_v13_filtered (min_end_turn=4)
#   2. Train v15 on combined_v13_filtered with hidden_dim=512
#   3. Benchmark v15
#   4. Collect v15-vs-heuristic (seed18000)
#
# Key changes vs v14:
#   - Data: combined_v13_filtered (no early DEFCON-suicide games) instead of
#     combined_v14 (which added weak v13-vs-heuristic data and regressed)
#   - Architecture: --hidden-dim 512 (trunk capacity was v13/v14 bottleneck)
#   - No v13-vs-heuristic or v14-vs-heuristic in training mix (both from
#     models scoring < 40% vs heuristic)
set -euo pipefail
LOG=/tmp/pipeline_v15.log
exec >> "$LOG" 2>&1

cd /home/dkord/code/twilight-struggle-ai

echo "=== v15 pipeline started at $(date) ==="

# ── Filter combined_v13 → combined_v13_filtered ──────────────────────────────
COMBINED_V13=data/combined_v13
COMBINED_V13_FILTERED=data/combined_v13_filtered

if [ ! -d "$COMBINED_V13_FILTERED" ] || [ -z "$(ls "$COMBINED_V13_FILTERED"/*.parquet 2>/dev/null)" ]; then
    echo "[$(date)] Building combined_v13_filtered (min_end_turn=4)..."
    nice -n 10 uv run python scripts/filter_dataset.py \
        --src "$COMBINED_V13" \
        --dst "$COMBINED_V13_FILTERED" \
        --min-end-turn 4 \
        2>&1 | tee /tmp/filter_v13.log
    echo "[$(date)] combined_v13_filtered done."
else
    echo "[$(date)] combined_v13_filtered already exists, skipping filter step."
fi

FILE_COUNT=$(ls "$COMBINED_V13_FILTERED"/*.parquet 2>/dev/null | wc -l)
echo "[$(date)] combined_v13_filtered: $FILE_COUNT files"

# ── Train v15 ────────────────────────────────────────────────────────────────
echo "[$(date)] Starting v15 training on combined_v13_filtered (hidden_dim=512)..."
nice -n 10 uv run python scripts/train_baseline.py \
    --data-dir "$COMBINED_V13_FILTERED" \
    --out-dir data/checkpoints/retrain_v15 \
    --epochs 60 --batch-size 1024 --lr 1.2e-3 \
    --weight-decay 1e-4 --dropout 0.1 --label-smoothing 0.05 \
    --value-target final_vp --num-workers 4 --one-cycle --pin-memory \
    --hidden-dim 512 \
    2>&1 | tee /tmp/train_v15.log
echo "[$(date)] v15 training done."

# ── Benchmark v15 ────────────────────────────────────────────────────────────
V15_CKPT=data/checkpoints/retrain_v15/baseline_best.pt
if [ ! -f "$V15_CKPT" ]; then echo "ERROR: v15 checkpoint not found"; exit 1; fi

echo "[$(date)] Running v15 benchmark..."
nice -n 10 uv run python scripts/benchmark_vf_mcts.py \
    --checkpoint "$V15_CKPT" \
    --n-games 30 --n-sim 50 --n-candidates 8 --seed 9999 --pool-size 30 \
    2>&1 | tee /tmp/benchmark_v15.log
echo "[$(date)] v15 benchmark done."

# ── Collect v15-vs-heuristic (seed18000) ─────────────────────────────────────
# Only collect if v15 scores > 40% vs heuristic (anti-collapse guard).
# Check benchmark result:
V15_VS_HEU_PCT=$(grep "learned vs heuristic" /tmp/benchmark_v15.log | grep -oP '\(\K[0-9.]+(?=%)' | head -1)
echo "[$(date)] v15 vs heuristic: ${V15_VS_HEU_PCT:-unknown}%"

V15_VS_HEU_OUT=data/selfplay/learned_v15_vs_heuristic_2k_seed18000.parquet

if [ ! -f "$V15_VS_HEU_OUT" ]; then
    # Only collect if >= 35% (relaxed threshold vs strict 40% since we're still improving)
    PCT_INT=${V15_VS_HEU_PCT%.*}
    if [ "${PCT_INT:-0}" -ge 35 ]; then
        echo "[$(date)] Collecting v15-vs-heuristic (v15 scored ${V15_VS_HEU_PCT}% >= 35%)..."
        nice -n 10 uv run python scripts/collect_learned_vs_heuristic.py \
            --checkpoint "$V15_CKPT" --n-games 2000 --workers 8 \
            --seed 18000 --out "$V15_VS_HEU_OUT" \
            2>&1 | tee /tmp/collect_v15_vs_heuristic.log
        echo "[$(date)] v15-vs-heuristic collection done."
    else
        echo "[$(date)] SKIP collection: v15 only scored ${V15_VS_HEU_PCT}% vs heuristic (< 35%). Not worth collecting."
    fi
fi

echo "=== v15 pipeline finished at $(date) ==="
