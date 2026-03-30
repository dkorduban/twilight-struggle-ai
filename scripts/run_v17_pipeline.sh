#!/bin/bash
# v17 pipeline — first generation with vs-heuristic data mixed in.
#
# Key decisions:
#   - Data: combined_v17 = v16 heuristic (3k games) + v16-vs-heuristic (2k games)
#           This is the first vs-heuristic generation; the anchor data prevents collapse.
#   - Architecture: default hidden_dim=256 (same as v16)
#   - Seeds: heuristic=20000 (reused from v16), vs-heuristic=21000 (collected by v16 pipeline)
#
# Steps:
#   1. Build combined_v17 from v16 heuristic + v16-vs-heuristic data
#   2. Train v17 (256-dim trunk, 60 epochs)
#   3. Benchmark v17 (learned vs random/heuristic first, then MCTS)
#   4. Collect v17-vs-heuristic (seed=22000) if v17 scores >=35%
set -euo pipefail
LOG=/tmp/pipeline_v17.log
exec >> "$LOG" 2>&1

cd /home/dkord/code/twilight-struggle-ai

echo "=== v17 pipeline started at $(date) ==="

# ── Prerequisites ─────────────────────────────────────────────────────────────
FRESH_HEU=data/selfplay/heuristic_3000games_v3_seed20000.parquet
V16_VS_HEU=data/selfplay/learned_v16_vs_heuristic_2k_seed21000.parquet

if [ ! -f "$FRESH_HEU" ]; then
    echo "ERROR: v16 heuristic data not found: $FRESH_HEU"
    exit 1
fi
if [ ! -f "$V16_VS_HEU" ]; then
    echo "ERROR: v16-vs-heuristic data not found: $V16_VS_HEU"
    echo "       Run run_v16_pipeline.sh first and ensure v16 scored >=35%."
    exit 1
fi

# ── Build combined_v17 ────────────────────────────────────────────────────────
COMBINED_V17=data/combined_v17
mkdir -p "$COMBINED_V17"
rm -f "$COMBINED_V17"/*.parquet
ln -sf "$(readlink -f "$FRESH_HEU")" "$COMBINED_V17/$(basename "$FRESH_HEU")"
ln -sf "$(readlink -f "$V16_VS_HEU")" "$COMBINED_V17/$(basename "$V16_VS_HEU")"

FILE_COUNT=$(ls "$COMBINED_V17"/*.parquet 2>/dev/null | wc -l)
echo "[$(date)] combined_v17 assembled: $FILE_COUNT files (heuristic + v16-vs-heuristic)"

# ── Train v17 ─────────────────────────────────────────────────────────────────
echo "[$(date)] Starting v17 training on combined_v17 (hidden_dim=256)..."
nice -n 10 uv run python scripts/train_baseline.py \
    --data-dir "$COMBINED_V17" \
    --out-dir data/checkpoints/retrain_v17 \
    --epochs 60 --batch-size 1024 --lr 1.2e-3 \
    --weight-decay 1e-4 --dropout 0.1 --label-smoothing 0.05 \
    --value-target final_vp --num-workers 2 --one-cycle --pin-memory \
    2>&1 | tee /tmp/train_v17.log
echo "[$(date)] v17 training done."

# ── Benchmark v17 ─────────────────────────────────────────────────────────────
V17_CKPT=data/checkpoints/retrain_v17/baseline_best.pt
if [ ! -f "$V17_CKPT" ]; then echo "ERROR: v17 checkpoint not found"; exit 1; fi

echo "[$(date)] Running v17 benchmark..."
nice -n 10 uv run python scripts/benchmark_vf_mcts.py \
    --checkpoint "$V17_CKPT" \
    --n-games 30 --n-sim 50 --n-candidates 8 --seed 9999 --pool-size 30 \
    2>&1 | tee /tmp/benchmark_v17.log
echo "[$(date)] v17 benchmark done."

# ── Collect v17-vs-heuristic (seed=22000) if v17 scores >=35% ────────────────
V17_VS_HEU=data/selfplay/learned_v17_vs_heuristic_2k_seed22000.parquet
V17_PCT=$(grep "learned vs heuristic" /tmp/benchmark_v17.log | grep -oP '\(\K[0-9.]+(?=%)' | head -1)
if [ -z "$V17_PCT" ]; then
    V17_PCT=$(grep "vf_mcts.*vs heuristic" /tmp/benchmark_v17.log | grep -oP '\(\K[0-9.]+(?=%)' | head -1)
fi
echo "[$(date)] v17 vs heuristic: ${V17_PCT:-unknown}%"

if [ ! -f "$V17_VS_HEU" ]; then
    PCT_INT=${V17_PCT%.*}
    if [ "${PCT_INT:-0}" -ge 35 ]; then
        echo "[$(date)] Collecting v17-vs-heuristic (scored ${V17_PCT}% >= 35%)..."
        nice -n 10 uv run python scripts/collect_learned_vs_heuristic.py \
            --checkpoint "$V17_CKPT" --n-games 2000 --workers 8 \
            --seed 22000 --out "$V17_VS_HEU" \
            2>&1 | tee /tmp/collect_v17_vs_heuristic.log
        echo "[$(date)] v17-vs-heuristic collection done."

        # ── Build combined_v18 and chain to generic pipeline ─────────────────
        mkdir -p data/combined_v18
        rm -f data/combined_v18/*.parquet
        ln -sf "$(readlink -f "$FRESH_HEU")"   data/combined_v18/$(basename "$FRESH_HEU")
        ln -sf "$(readlink -f "$V16_VS_HEU")"  data/combined_v18/$(basename "$V16_VS_HEU")
        ln -sf "$(readlink -f "$V17_VS_HEU")"  data/combined_v18/$(basename "$V17_VS_HEU")
        echo "[$(date)] combined_v18 assembled: 3 files"
        echo "[$(date)] Launching v18+ via generic pipeline..."
        bash scripts/run_vN_pipeline.sh 18
    else
        echo "[$(date)] SKIP: v17 scored ${V17_PCT:-?}% vs heuristic (< 35%). Collect more heuristic data before retraining."
    fi
fi

echo "=== v17 pipeline finished at $(date) ==="
