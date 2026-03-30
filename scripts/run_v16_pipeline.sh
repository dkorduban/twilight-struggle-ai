#!/bin/bash
# v16 pipeline — clean slate, no poisoned data, default trunk size.
#
# Key decisions:
#   - Data: ONLY fresh heuristic games from the DEFCON-safe policy (seed=20000).
#           No old heuristic/learned data (high DEFCON-rate era, 12.5% suicide).
#   - Architecture: default hidden_dim=256 (no wide trunk until vs-heuristic perf confirmed).
#   - Shape: 86 countries / 172-dim influence (Austria + Taiwan now included).
#
# Steps:
#   1. Collect 3000 fresh heuristic games (seed=20000)
#   2. Build combined_v16 from that single clean batch
#   3. Train v16 (256-dim trunk, 60 epochs)
#   4. Benchmark v16 vs heuristic
#   5. Collect v16-vs-heuristic (seed=21000) if v16 scores >=35%
set -euo pipefail
LOG=/tmp/pipeline_v16.log
exec >> "$LOG" 2>&1

cd /home/dkord/code/twilight-struggle-ai

echo "=== v16 pipeline started at $(date) ==="

# ── Collect 3000 fresh heuristic games ───────────────────────────────────────
FRESH_HEU=data/selfplay/heuristic_3000games_v3_seed20000.parquet
if [ ! -f "$FRESH_HEU" ]; then
    echo "[$(date)] Collecting 3000 fresh heuristic games (seed=20000)..."
    nice -n 10 uv run python scripts/collect_heuristic_selfplay.py \
        --n-games 3000 --workers 8 --seed 20000 \
        --out "$FRESH_HEU" \
        2>&1 | tee /tmp/collect_heuristic_v3.log
    echo "[$(date)] Fresh heuristic collection done."
else
    echo "[$(date)] Fresh heuristic data already exists, skipping."
fi

# ── Build combined_v16 (fresh data only, no poisoned legacy files) ────────────
COMBINED_V16=data/combined_v16
mkdir -p "$COMBINED_V16"
# Clear any legacy links that may exist from a prior attempt
rm -f "$COMBINED_V16"/*.parquet
ln -sf "$(readlink -f "$FRESH_HEU")" "$COMBINED_V16/$(basename "$FRESH_HEU")"

FILE_COUNT=$(ls "$COMBINED_V16"/*.parquet 2>/dev/null | wc -l)
echo "[$(date)] combined_v16 assembled: $FILE_COUNT files (fresh heuristic only)"

# ── Train v16 (default hidden_dim=256, 86-country features) ──────────────────
echo "[$(date)] Starting v16 training on combined_v16 (hidden_dim=256)..."
nice -n 10 uv run python scripts/train_baseline.py \
    --data-dir "$COMBINED_V16" \
    --out-dir data/checkpoints/retrain_v16 \
    --epochs 60 --batch-size 1024 --lr 1.2e-3 \
    --weight-decay 1e-4 --dropout 0.1 --label-smoothing 0.05 \
    --value-target final_vp --num-workers 4 --one-cycle --pin-memory \
    2>&1 | tee /tmp/train_v16.log
echo "[$(date)] v16 training done."

# ── Benchmark v16 ────────────────────────────────────────────────────────────
V16_CKPT=data/checkpoints/retrain_v16/baseline_best.pt
if [ ! -f "$V16_CKPT" ]; then echo "ERROR: v16 checkpoint not found"; exit 1; fi

echo "[$(date)] Running v16 benchmark..."
nice -n 10 uv run python scripts/benchmark_vf_mcts.py \
    --checkpoint "$V16_CKPT" \
    --n-games 30 --n-sim 50 --n-candidates 8 --seed 9999 --pool-size 30 \
    2>&1 | tee /tmp/benchmark_v16.log
echo "[$(date)] v16 benchmark done."

# ── Collect v16-vs-heuristic (seed=21000) — always collect for gen 1 ─────────
# Rationale: even a weak gen-1 model provides useful training data when playing
# vs heuristic, since the heuristic's responses to diverse game states are
# high-quality labels. Threshold applies only to later generations (v18+).
V16_VS_HEU=data/selfplay/learned_v16_vs_heuristic_2k_seed21000.parquet
V16_PCT=$(grep "learned vs heuristic" /tmp/benchmark_v16_new.log | grep -oP '\(\K[0-9.]+(?=%)' | head -1)
if [ -z "$V16_PCT" ]; then
    V16_PCT=$(grep "vf_mcts.*vs heuristic" /tmp/benchmark_v16_new.log | grep -oP '\(\K[0-9.]+(?=%)' | head -1)
fi
echo "[$(date)] v16 vs heuristic: ${V16_PCT:-unknown}%"

if [ ! -f "$V16_VS_HEU" ]; then
    echo "[$(date)] Collecting v16-vs-heuristic (gen-1 always-collect, ${V16_PCT:-?}% vs heuristic)..."
    nice -n 10 uv run python scripts/collect_learned_vs_heuristic.py \
        --checkpoint "$V16_CKPT" --n-games 2000 --workers 8 \
        --seed 21000 --out "$V16_VS_HEU" \
        2>&1 | tee /tmp/collect_v16_vs_heuristic.log
    echo "[$(date)] v16-vs-heuristic collection done."
    echo "[$(date)] Launching v17 pipeline..."
    bash scripts/run_v17_pipeline.sh
fi

echo "=== v16 pipeline finished at $(date) ==="
