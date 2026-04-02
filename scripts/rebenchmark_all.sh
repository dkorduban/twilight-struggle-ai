#!/bin/bash
# rebenchmark_all.sh — rebenchmark all historical checkpoints against
# the current (DEFCON-fixed) heuristic opponent.
#
# Runs one benchmark at a time to avoid memory pressure.
# Each benchmark: 500 games, seed 9999, learned side ussr.

set -euo pipefail
cd /home/dkord/code/twilight-struggle-ai

GAMES=500
SEED=9999
RESULTS_DIR="results"

# Versions from benchmark_history.json (v23-v85), in order
VERSIONS=(
    23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40
    41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58
    59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76
    77 78 79 80 81 82 83 84 85
)

TOTAL=${#VERSIONS[@]}
DONE=0
FAILED=()

echo "=== Rebenchmark ALL checkpoints against DEFCON-fixed heuristic ==="
echo "    Total versions: $TOTAL"
echo "    Games per version: $GAMES"
echo "    Seed: $SEED"
echo ""

for V in "${VERSIONS[@]}"; do
    DONE=$((DONE + 1))
    CKPT="data/checkpoints/retrain_v${V}/baseline_best.pt"
    OUT="${RESULTS_DIR}/rebench_v${V}.json"

    if [ ! -f "$CKPT" ]; then
        echo "[$DONE/$TOTAL] SKIP v${V}: checkpoint not found ($CKPT)"
        FAILED+=("v${V}:missing")
        continue
    fi

    # Skip if already completed (allows resuming)
    if [ -f "$OUT" ]; then
        echo "[$DONE/$TOTAL] SKIP v${V}: already done ($OUT)"
        continue
    fi

    echo "[$DONE/$TOTAL] Benchmarking v${V}..."
    START=$(date +%s)

    if nice -n 10 bash scripts/bench_cpp.sh \
        --checkpoint "$CKPT" \
        --n-games "$GAMES" \
        --seed "$SEED" \
        --out "$OUT" 2>&1; then
        END=$(date +%s)
        echo "[$DONE/$TOTAL] v${V} completed in $((END - START))s"
    else
        echo "[$DONE/$TOTAL] FAILED v${V}"
        FAILED+=("v${V}:error")
    fi
    echo ""
done

echo "=== Rebenchmark complete ==="
echo "Completed: $((DONE - ${#FAILED[@]})) / $TOTAL"
if [ ${#FAILED[@]} -gt 0 ]; then
    echo "Failed/skipped: ${FAILED[*]}"
fi
