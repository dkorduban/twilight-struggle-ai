#!/bin/bash
# bench_and_selfplay_v86.sh — Post-training: benchmark both sides, then collect self-play.
#
# Run after training completes:
#   nice -n 10 bash scripts/bench_and_selfplay_v86.sh
set -euo pipefail
cd /home/dkord/code/twilight-struggle-ai

CKPT="data/checkpoints/retrain_v86_both_sides/baseline_best.pt"
BENCH_GAMES=500
SELFPLAY_GAMES=2000
SEED=50000

if [ ! -f "$CKPT" ]; then
    echo "ERROR: checkpoint not found: $CKPT"
    exit 1
fi

echo "=== v86 both-sides benchmark + self-play ==="

# ── Step 1: Benchmark both sides ─────────────────────────────────────────────
echo "[$(date)] Benchmarking USSR side ($BENCH_GAMES games)..."
nice -n 10 bash scripts/bench_cpp.sh \
    --checkpoint "$CKPT" \
    --n-games "$BENCH_GAMES" \
    --seed 9999 \
    --learned-side ussr \
    --out results/bench_v86_both_ussr.json

echo "[$(date)] Benchmarking US side ($BENCH_GAMES games)..."
nice -n 10 bash scripts/bench_cpp.sh \
    --checkpoint "$CKPT" \
    --n-games "$BENCH_GAMES" \
    --seed 9998 \
    --learned-side us \
    --out results/bench_v86_both_us.json

# ── Step 2: Show results ─────────────────────────────────────────────────────
echo ""
echo "=== Benchmark results ==="
python3 -c "
import json
for side in ['ussr', 'us']:
    f = f'results/bench_v86_both_{side}.json'
    try:
        data = json.load(open(f))
        pct = data.get('learned_win_pct', 0) * 100
        print(f'  {side.upper()}: {pct:.1f}% win rate')
    except:
        print(f'  {side.upper()}: N/A')
"

# ── Step 3: Collect learned-vs-learned self-play with exploration noise ──────
echo ""
echo "[$(date)] Collecting learned-vs-learned self-play ($SELFPLAY_GAMES games)..."
echo "[$(date)] Using Dirichlet noise (alpha=0.2, eps=0.25) + temperature=1.0"

TS_MODEL="${CKPT%.pt}_scripted.pt"
# Export if needed (bench_cpp.sh already did this, but just in case)
if [ ! -f "$TS_MODEL" ]; then
    uv run python cpp/tools/export_baseline_to_torchscript.py \
        --checkpoint "$CKPT" --out "$TS_MODEL"
fi

nice -n 10 bash scripts/collect_cpp.sh \
    --ussr-model "$TS_MODEL" \
    --us-model "$TS_MODEL" \
    --games "$SELFPLAY_GAMES" \
    --seed "$SEED" \
    --temperature 1.0 \
    --out data/selfplay/v86_both_selfplay_${SELFPLAY_GAMES}g_seed${SEED}.parquet

echo "[$(date)] Done!"
echo "[$(date)] Output: data/selfplay/v86_both_selfplay_${SELFPLAY_GAMES}g_seed${SEED}.parquet"
