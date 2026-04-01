#!/bin/bash
# Generic vN pipeline — train on combined_vN, benchmark, collect vs-heuristic, chain to v(N+1).
#
# Usage:
#   bash scripts/run_vN_pipeline.sh <N> [--threshold PCT] [--games-per-gen N] [--seed-base S]
#
# Arguments:
#   N               Version number (e.g. 18)
#   --threshold PCT Win-rate threshold to proceed to vs-heuristic collection (default: 35)
#   --games-vsh N   Games to collect for vs-heuristic (default: 2000)
#   --seed-base S   Base seed; heuristic seed = S + N*1000, vs-heu seed = S + N*1000 + 500 (default: 20000)
#   --max-gens G    Rolling window: keep only the last G generations of parquet data (default: 6, 0=keep all)
#
# combined_vN must already exist (symlinks to parquet files).
# The script trains, benchmarks, conditionally collects, then launches run_vN_pipeline.sh N+1.
set -euo pipefail

N=${1:?Usage: $0 <version_number>}
THRESHOLD=0   # 0 = always collect; raise to 35+ once model can consistently beat heuristic
GAMES_VSH=2000
GAMES_VSL=1000  # Games to collect for learned-vs-learned self-play (0 = skip)
SEED_BASE=20000
MAX_GENS=6    # Rolling window: keep only last N generations of parquet data (0 = keep all)

shift
while [[ $# -gt 0 ]]; do
    case $1 in
        --threshold)  THRESHOLD=$2;  shift 2 ;;
        --games-vsh)  GAMES_VSH=$2;  shift 2 ;;
        --games-vsl)  GAMES_VSL=$2;  shift 2 ;;
        --seed-base)  SEED_BASE=$2;  shift 2 ;;
        --max-gens)   MAX_GENS=$2;   shift 2 ;;
        *) echo "Unknown arg: $1"; exit 1 ;;
    esac
done

cd /home/dkord/code/twilight-struggle-ai

LOG=logs/pipeline_v${N}.log
mkdir -p logs
exec >> "$LOG" 2>&1

echo "=== v${N} pipeline started at $(date) ==="

COMBINED=data/combined_v${N}
CKPT_DIR=data/checkpoints/retrain_v${N}
CKPT=${CKPT_DIR}/baseline_best.pt
BENCH_LOG=logs/benchmark_v${N}.log
MONITOR_LOG=logs/monitor_v${N}.log
VSH_SEED=$(( SEED_BASE + N * 1000 + 500 ))
VSH_OUT=data/selfplay/learned_v${N}_vs_heuristic_${GAMES_VSH}g_seed${VSH_SEED}.parquet

# ── Verify combined data exists ───────────────────────────────────────────────
FILE_COUNT=$(ls "$COMBINED"/*.parquet 2>/dev/null | wc -l)
if [ "$FILE_COUNT" -eq 0 ]; then
    echo "ERROR: No parquet files in $COMBINED — build combined_v${N} first."
    exit 1
fi
echo "[$(date)] combined_v${N}: $FILE_COUNT files"

# ── Start resource monitor (background) ──────────────────────────────────────
uv run python scripts/resource_monitor.py --out "$MONITOR_LOG" --interval 5 &
MONITOR_PID=$!
echo "[$(date)] Resource monitor started (PID=$MONITOR_PID) -> $MONITOR_LOG"
trap "kill $MONITOR_PID 2>/dev/null || true" EXIT

# ── Train ─────────────────────────────────────────────────────────────────────
if [ ! -f "$CKPT" ]; then
    uv run python scripts/resource_monitor.py --tag "train" --out "$MONITOR_LOG"
    echo "[$(date)] Training v${N} (hidden_dim=256, up to 120 epochs, patience=12)..."
    nice -n 10 uv run python scripts/train_baseline.py \
        --data-dir "$COMBINED" \
        --out-dir "$CKPT_DIR" \
        --epochs 120 --batch-size 8192 --lr 2.4e-3 \
        --weight-decay 1e-4 --dropout 0.1 --label-smoothing 0.05 \
        --value-target final_vp --num-workers 0 --pin-memory --amp --one-cycle \
        --patience 12 --advantage-weight 0.5 \
        2>&1 | tee logs/train_v${N}.log
    echo "[$(date)] v${N} training done."
else
    echo "[$(date)] Checkpoint already exists, skipping training."
fi

# ── Benchmark ─────────────────────────────────────────────────────────────────
# MCTS matchups skipped until learned vs heuristic win rate > 25% (too slow, ~0% anyway).
# Re-enable by adding --n-sim 50 --n-candidates 8 --pool-size 30 below.
# Skip if benchmark already completed (summary line present) — allows restart after failure.
if grep -q "learned vs heuristic" "$BENCH_LOG" 2>/dev/null && \
   grep -q "^\s*learned vs heuristic" "$BENCH_LOG" 2>/dev/null; then
    echo "[$(date)] Benchmark log exists with complete results, skipping re-run."
else
    uv run python scripts/resource_monitor.py --tag "benchmark" --out "$MONITOR_LOG"
    echo "[$(date)] Benchmarking v${N}..."
    nice -n 10 uv run python scripts/benchmark_vf_mcts.py \
        --checkpoint "$CKPT" \
        --n-games 500 --n-sim 0 --n-candidates 8 --seed 9999 --pool-size 30 \
        2>&1 | tee "$BENCH_LOG"
    echo "[$(date)] v${N} benchmark done."

    # ── Persist benchmark result to durable JSON (survives /tmp wipe) ─────────
    mkdir -p results
    uv run python -c "
import json, pathlib, re
log = pathlib.Path('$BENCH_LOG').read_text()
m = re.search(r'learned vs heuristic\s+learned\s+\d+/\d+\s+\(\s*([0-9.]+)%\)', log)
pct = float(m.group(1)) if m else None
hist_path = pathlib.Path('results/benchmark_history.json')
hist = json.loads(hist_path.read_text()) if hist_path.exists() else {}
hist['v${N}'] = {'learned_vs_heuristic': pct}
hist_path.write_text(json.dumps(hist, indent=2, sort_keys=True))
print(f'  Saved v${N} win%={pct} to results/benchmark_history.json')
" 2>/dev/null || true
fi

# ── Collect vs-heuristic if above threshold ───────────────────────────────────
# Benchmark summary format: "learned vs heuristic  learned  3/ 30 ( 10.0%)  heuristic ..."
# Pattern allows optional space after '(' e.g. "( 10.0%)" or "(10.0%)".
PCT=$(grep "learned vs heuristic" "$BENCH_LOG" | grep -v "^\s*\[" | grep -oP '\( *\K[0-9.]+(?=%)' | head -1 || true)
if [ -z "$PCT" ]; then
    PCT=$(grep "vf_mcts.*vs heuristic" "$BENCH_LOG" | grep -v "^\s*\[" | grep -oP '\( *\K[0-9.]+(?=%)' | head -1 || true)
fi
echo "[$(date)] v${N} vs heuristic: ${PCT:-unknown}%"

if [ ! -f "$VSH_OUT" ]; then
    PCT_INT=${PCT%.*}
    if [ "${PCT_INT:-0}" -ge "$THRESHOLD" ]; then
        uv run python scripts/resource_monitor.py --tag "collect" --out "$MONITOR_LOG"
        echo "[$(date)] Collecting v${N}-vs-heuristic (${PCT}% >= ${THRESHOLD}%, seed=${VSH_SEED})..."
        # Use C++ collection (single thread ~9 games/sec, avoids 16-process Python overhead).
        # Falls back to Python if the C++ binary or export script is missing.
        if [ -f "build-ninja/cpp/tools/ts_collect_selfplay_rows_jsonl" ]; then
            bash scripts/collect_cpp.sh \
                --checkpoint "$CKPT" \
                --learned-side ussr \
                --games "$GAMES_VSH" \
                --seed "$VSH_SEED" \
                --out "$VSH_OUT" \
                2>&1 | tee logs/collect_v${N}_vs_heuristic.log
        else
            echo "[$(date)] WARNING: C++ binary missing — falling back to Python collector"
            nice -n 10 uv run python scripts/collect_learned_vs_heuristic.py \
                --checkpoint "$CKPT" --n-games "$GAMES_VSH" --workers 16 \
                --seed "$VSH_SEED" --out "$VSH_OUT" \
                --value-guided --value-guided-k 4 \
                2>&1 | tee logs/collect_v${N}_vs_heuristic.log
        fi
        echo "[$(date)] v${N}-vs-heuristic collection done."

        # ── Collect learned-vs-learned self-play (vN vs vN-1) ────────────────
        # Uses vN as USSR, vN-1 as US. Skipped on gen 1 (no prior checkpoint).
        # Provides diverse value signal (wins and losses against a near-peer)
        # to supplement vs-heuristic BC data and break the BC ceiling.
        NM1=$(( N - 1 ))
        VSL_SEED=$(( SEED_BASE + N * 1000 + 750 ))
        VSL_OUT=data/selfplay/learned_v${N}_vs_v${NM1}_${GAMES_VSL}g_seed${VSL_SEED}.parquet
        PREV_CKPT="data/checkpoints/retrain_v${NM1}/baseline_best.pt"
        PREV_TS="data/checkpoints/retrain_v${NM1}/baseline_best_scripted.pt"
        CURR_TS="data/checkpoints/retrain_v${N}/baseline_best_scripted.pt"

        if [ "$GAMES_VSL" -gt 0 ] && [ -f "$PREV_CKPT" ] && [ ! -f "$VSL_OUT" ]; then
            # Export previous checkpoint to TorchScript if needed
            if [ ! -f "$PREV_TS" ]; then
                echo "[$(date)] Exporting v${NM1} TorchScript: $PREV_CKPT -> $PREV_TS"
                nice -n 10 uv run python cpp/tools/export_baseline_to_torchscript.py \
                    --checkpoint "$PREV_CKPT" --out "$PREV_TS" 2>&1
            fi
            echo "[$(date)] Collecting v${N}-vs-v${NM1} self-play (${GAMES_VSL} games, seed=${VSL_SEED})..."
            bash scripts/collect_cpp.sh \
                --ussr-model "$CURR_TS" \
                --us-model "$PREV_TS" \
                --games "$GAMES_VSL" \
                --seed "$VSL_SEED" \
                --out "$VSL_OUT" \
                2>&1 | tee logs/collect_v${N}_vs_v${NM1}.log
            echo "[$(date)] v${N}-vs-v${NM1} self-play collection done."
        else
            echo "[$(date)] Skipping learned-vs-learned: GAMES_VSL=${GAMES_VSL} prev_ckpt=${PREV_CKPT}"
        fi

        # ── Validate DEFCON-1 rate in collected data ──────────────────────────
        DEFCON1_RATE=$(uv run python -c "
import pyarrow.parquet as pq
from collections import Counter
tbl = pq.read_table('$VSH_OUT')
gids = tbl['game_id'].to_pylist()
reasons = tbl['end_reason'].to_pylist()
gr = {}
for g, r in zip(gids, reasons): gr[g] = r
total = len(gr)
defcon1 = sum(1 for r in gr.values() if r == 'defcon1')
print(f'{defcon1/total*100:.1f}')
" 2>/dev/null || echo "?")
        echo "[$(date)] v${N}-vs-heuristic DEFCON-1 rate: ${DEFCON1_RATE}%"
        # Warn if rate is much higher than heuristic baseline (~8%)
        DEFCON1_INT=${DEFCON1_RATE%.*}
        if [ "${DEFCON1_INT:-0}" -gt 25 ]; then
            echo "[$(date)] WARNING: DEFCON-1 rate ${DEFCON1_RATE}% > 25% — check inference safety guards"
        fi

        # ── Filter new vs-heuristic data ─────────────────────────────────────
        VSH_FILTERED=data/combined_v${N}_vsh_filtered/filtered.parquet
        echo "[$(date)] Filtering $VSH_OUT (cap defcon1 at 15%)..."
        nice -n 10 uv run python scripts/filter_bad_games.py \
            --input "$VSH_OUT" \
            --output "$VSH_FILTERED" \
            --max-defcon1-pct 15 \
            2>&1 | tee logs/filter_v${N}.log
        echo "[$(date)] Filter done."

        # ── Build combined_v(N+1) and launch next generation ─────────────────
        NP1=$(( N + 1 ))
        COMBINED_NP1=data/combined_v${NP1}
        mkdir -p "$COMBINED_NP1"
        rm -f "$COMBINED_NP1"/*.parquet

        # Rolling window: carry forward files from combined_vN, skipping those
        # whose embedded version number is older than (N+1 - MAX_GENS).
        # Files with no parseable version are always kept (seed/baseline data).
        # MAX_GENS=0 means keep everything.
        MIN_GEN=0
        if [ "$MAX_GENS" -gt 0 ]; then
            MIN_GEN=$(( NP1 - MAX_GENS ))
        fi
        DROPPED=0
        for f in "$COMBINED"/*.parquet; do
            fname=$(basename "$f")
            # Extract first _vNN_ or _vNN. version number from filename
            file_gen=$(echo "$fname" | grep -oP '(?<=_v)\d+' | head -1 || true)
            if [ -n "$file_gen" ] && [ "$MAX_GENS" -gt 0 ] && [ "$file_gen" -lt "$MIN_GEN" ]; then
                DROPPED=$(( DROPPED + 1 ))
                echo "[$(date)] Rolling window: dropping old gen v${file_gen} file: $fname"
            else
                ln -sf "$(readlink -f "$f")" "$COMBINED_NP1/$fname"
            fi
        done
        ln -sf "$(readlink -f "$VSH_FILTERED")" \
            "$COMBINED_NP1/learned_v${N}_vs_heuristic_filtered.parquet"

        # Include learned-vs-learned data if it was collected this generation
        if [ -f "$VSL_OUT" ]; then
            ln -sf "$(readlink -f "$VSL_OUT")" \
                "$COMBINED_NP1/learned_v${N}_vs_v${NM1}_selfplay.parquet"
            echo "[$(date)] Added self-play v${N}-vs-v${NM1} to combined_v${NP1}"
        fi

        NP1_COUNT=$(ls "$COMBINED_NP1"/*.parquet | wc -l)
        echo "[$(date)] combined_v${NP1} assembled: $NP1_COUNT files (dropped $DROPPED old, min_gen=v${MIN_GEN})"

        echo "[$(date)] Launching v${NP1} pipeline..."
        bash scripts/run_vN_pipeline.sh "$NP1" \
            --threshold "$THRESHOLD" --games-vsh "$GAMES_VSH" --games-vsl "$GAMES_VSL" \
            --seed-base "$SEED_BASE" --max-gens "$MAX_GENS"
    else
        echo "[$(date)] SKIP: v${N} scored ${PCT:-?}% (< ${THRESHOLD}%). Stopping chain."
        echo "[$(date)] Consider: collect more heuristic data or tune architecture before continuing."
    fi
else
    echo "[$(date)] vs-heuristic data already exists: $VSH_OUT"
fi

echo "=== v${N} pipeline finished at $(date) ==="
