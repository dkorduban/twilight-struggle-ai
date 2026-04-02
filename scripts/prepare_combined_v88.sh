#!/bin/bash
# prepare_combined_v88.sh — Create combined_v88 dataset for training.
#
# Combines:
# 1. Golden-era data (v23-v30 vsh_filtered)
# 2. Both heuristic anchors (v3 old + v4 fixed)
# 3. Fresh v88 data collected with setup influence active (v87 model)
#
# No self-play data — golden era showed pure vs-heuristic is strongest.
#
# Usage:
#   bash scripts/prepare_combined_v88.sh
set -euo pipefail
cd /home/dkord/code/twilight-struggle-ai

OUT_DIR="data/combined_v88"
mkdir -p "$OUT_DIR"

echo "[prepare_combined_v88] Creating $OUT_DIR"

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
for ANCHOR in data/selfplay/heuristic_3000games_v3_seed20000.parquet \
              data/selfplay/heuristic_3000games_v4_fixed_seed30000.parquet; do
    if [ -f "$ANCHOR" ]; then
        BASENAME=$(basename "$ANCHOR")
        ln -sf "$(realpath "$ANCHOR")" "$OUT_DIR/${BASENAME}"
        echo "  + anchor: $(basename "$ANCHOR")"
    fi
done

# ── Fresh v88 data (setup influence active, from v87 model) ─────────────────
for SIDE in ussr us; do
    SRC="data/combined_v88/learned_${SIDE}.parquet"
    if [ -f "$SRC" ]; then
        echo "  + v88 learned_${SIDE}: $(basename "$SRC")"
    else
        echo "  SKIP v88 learned_${SIDE} (not yet collected)"
    fi
done

echo ""
echo "[prepare_combined_v88] Contents:"
ls -lh "$OUT_DIR/"*.parquet 2>/dev/null || echo "  (no parquet files yet)"

echo ""
echo "[prepare_combined_v88] Row counts:"
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
