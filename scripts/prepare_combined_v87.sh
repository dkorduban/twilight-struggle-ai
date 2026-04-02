#!/bin/bash
# prepare_combined_v87.sh — Create combined_v87 dataset for next-gen training.
#
# Combines:
# 1. Golden-era data (v23-v30 vsh_filtered, same as v86 training base)
# 2. Both heuristic anchors (v3 old + v4 fixed)
# 3. Self-play data from v86 both-sides model (must be collected first)
#
# Usage:
#   bash scripts/prepare_combined_v87.sh [--selfplay-path PATH]
set -euo pipefail
cd /home/dkord/code/twilight-struggle-ai

SELFPLAY_PATH=""
OUT_DIR="data/combined_v87"

while [[ $# -gt 0 ]]; do
    case $1 in
        --selfplay-path) SELFPLAY_PATH=$2; shift 2 ;;
        --out-dir) OUT_DIR=$2; shift 2 ;;
        *) echo "Unknown arg: $1"; exit 1 ;;
    esac
done

mkdir -p "$OUT_DIR"

echo "[prepare_combined_v87] Creating $OUT_DIR"

# ── Golden-era filtered data (v23-v30) ───────────────────────────────────────
for V in 23 24 25 26 27 28 29 30; do
    SRC="data/combined_v${V}_vsh_filtered/filtered.parquet"
    if [ -f "$SRC" ]; then
        ln -sf "$(realpath "$SRC")" "$OUT_DIR/learned_v${V}_vs_heuristic_filtered.parquet"
        echo "  + v${V} vsh_filtered"
    else
        echo "  SKIP v${V} (not found: $SRC)"
    fi
done

# ── Heuristic anchors ────────────────────────────────────────────────────────
for ANCHOR in data/selfplay/heuristic_3000games_v3_seed30000.parquet \
              data/selfplay/heuristic_3000games_v4_fixed_seed30000.parquet; do
    if [ -f "$ANCHOR" ]; then
        BASENAME=$(basename "$ANCHOR")
        ln -sf "$(realpath "$ANCHOR")" "$OUT_DIR/heuristic_anchor_${BASENAME#heuristic_3000games_}"
        echo "  + anchor: $(basename "$ANCHOR")"
    fi
done

# ── Self-play data from v86 both-sides model ────────────────────────────────
if [ -n "$SELFPLAY_PATH" ] && [ -f "$SELFPLAY_PATH" ]; then
    ln -sf "$(realpath "$SELFPLAY_PATH")" "$OUT_DIR/v86_both_selfplay.parquet"
    echo "  + selfplay: $SELFPLAY_PATH"
elif [ -n "$SELFPLAY_PATH" ]; then
    echo "  WARNING: selfplay not found: $SELFPLAY_PATH"
fi

echo ""
echo "[prepare_combined_v87] Contents:"
ls -lh "$OUT_DIR/"*.parquet 2>/dev/null

echo ""
echo "[prepare_combined_v87] Row counts:"
python3 -c "
import pyarrow.parquet as pq
from pathlib import Path
total = 0
for f in sorted(Path('$OUT_DIR').glob('*.parquet')):
    n = pq.read_metadata(str(f)).num_rows
    total += n
    print(f'  {f.name}: {n:,} rows')
print(f'  TOTAL: {total:,} rows')
"
