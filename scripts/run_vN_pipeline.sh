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
QUICK_BENCH_GAMES=200
FULL_BENCH_EVERY=5

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
PREV_TEACHER_IN_COMBINED="${COMBINED}/teacher_targets/teacher_targets_v$(( N - 1 )).parquet"
PREV_TEACHER="data/teacher_targets/v$(( N - 1 ))/targets.parquet"
BENCH_LOG=logs/benchmark_v${N}.log
MONITOR_LOG=logs/monitor_v${N}.log
VSH_SEED=$(( SEED_BASE + N * 1000 + 500 ))
VSH_OUT=data/selfplay/learned_v${N}_vs_heuristic_${GAMES_VSH}g_seed${VSH_SEED}.parquet
VSH_US_SEED=$(( SEED_BASE + N * 1000 + 600 ))
VSH_US_OUT=data/selfplay/learned_v${N}_us_vs_heuristic_${GAMES_VSH}g_seed${VSH_US_SEED}.parquet
TEACHER_DIR="data/teacher_targets/v${N}"
TEACHER_POSITIONS="${TEACHER_DIR}/hard_positions_top1000.jsonl"
TEACHER_TARGETS="${TEACHER_DIR}/targets.parquet"
TEACHER_TARGETS_TS="${TEACHER_DIR}/model.scripted.pt"

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

    # Cold start every generation: warm-start caused epoch-1 early-stopping
    # and gradual win% degradation (v69-v80). Full 120-epoch cold start
    # produces stronger models even though it's slower.
    echo "[$(date)] Training v${N} COLD START (120 epochs, patience=12)..."
    TRAIN_ARGS=(
        --data-dir "$COMBINED"
        --out-dir "$CKPT_DIR"
        --epochs 120 --batch-size 8192 --lr 2.4e-3
        --weight-decay 1e-4 --dropout 0.1 --label-smoothing 0.05
        --value-target final_vp --num-workers 0 --pin-memory --amp --one-cycle
        --patience 12 --advantage-weight 0.5
    )
    if [ -f "$PREV_TEACHER_IN_COMBINED" ]; then
        echo "[$(date)] Using teacher targets for v${N}: $PREV_TEACHER_IN_COMBINED"
        TRAIN_ARGS+=(--teacher-targets "$PREV_TEACHER_IN_COMBINED" --teacher-weight 0.3)
    elif [ -f "$PREV_TEACHER" ]; then
        echo "[$(date)] Using teacher targets for v${N}: $PREV_TEACHER"
        TRAIN_ARGS+=(--teacher-targets "$PREV_TEACHER" --teacher-weight 0.3)
    fi
    nice -n 10 uv run python scripts/train_baseline.py \
        "${TRAIN_ARGS[@]}" \
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
    if (( N % FULL_BENCH_EVERY == 0 )); then
        N_BENCH=500
    else
        N_BENCH=$QUICK_BENCH_GAMES
    fi

    uv run python scripts/resource_monitor.py --tag "benchmark" --out "$MONITOR_LOG"
    echo "[$(date)] Benchmarking v${N} (${N_BENCH} games)..."
    if [ -f "build-ninja/cpp/tools/ts_collect_selfplay_rows_jsonl" ]; then
        bash scripts/bench_cpp.sh \
            --checkpoint "$CKPT" \
            --n-games "$N_BENCH" \
            --seed 9999 \
            --out "results/bench_v${N}.json" \
            2>&1 | tee "$BENCH_LOG"
    else
        nice -n 10 uv run python scripts/benchmark_vf_mcts.py \
            --checkpoint "$CKPT" \
            --n-games "$N_BENCH" --n-sim 0 --n-candidates 8 --seed 9999 --pool-size 30 \
            2>&1 | tee "$BENCH_LOG"

        # ── Persist benchmark result to durable JSON (survives /tmp wipe) ─────
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
    # Publish bench results to W&B (best-effort, don't fail pipeline)
    if [ -f "results/bench_v${N}.json" ]; then
        uv run python scripts/publish_bench_to_wandb.py "results/bench_v${N}.json" --generation "v${N}" 2>/dev/null || true
    fi
    echo "[$(date)] v${N} benchmark done."
fi

# ── Collect vs-heuristic if above threshold ───────────────────────────────────
# Benchmark summary format: "learned vs heuristic  learned  3/ 30 ( 10.0%)  heuristic ..."
# Pattern allows optional space after '(' e.g. "( 10.0%)" or "(10.0%)".
PCT=$(grep "learned vs heuristic" "$BENCH_LOG" | grep -v "^\s*\[" | grep -oP '\( *\K[0-9.]+(?=%)' | head -1 || true)
if [ -z "$PCT" ]; then
    PCT=$(grep "vf_mcts.*vs heuristic" "$BENCH_LOG" | grep -v "^\s*\[" | grep -oP '\( *\K[0-9.]+(?=%)' | head -1 || true)
fi
echo "[$(date)] v${N} vs heuristic: ${PCT:-unknown}%"

# ── Regression circuit breaker ────────────────────────────────────────────────
# If win rate drops significantly from recent best, STOP the pipeline instead
# of collecting more contaminated data. This prevents echo-chamber cascades
# where a bad gen generates selfplay that makes the next gen even worse.
#
# Triggers: win% < SELFPLAY_MIN_WIN_PCT (absolute floor)
#        OR win% < recent_best * 0.65 (relative drop >35% from peak)
# When triggered: still collect vs-heuristic data (it has heuristic labels,
# useful for recovery), but SKIP selfplay (weak-vs-weak is toxic) and
# flag the gen as "regressed" so downstream gens skip its selfplay.
SELFPLAY_MIN_WIN_PCT=8
REGRESSION_DETECTED=false
if [ -n "$PCT" ]; then
    RECENT_BEST=$(python3 -c "
import json
h = json.load(open('results/benchmark_history.json'))
# Look at the last 10 gens for the rolling best
vals = []
for g in range(max(1, $N - 10), $N):
    v = h.get(f'v{g}', {}).get('learned_vs_heuristic', 0)
    if v > 0:
        vals.append(v)
print(max(vals) if vals else 0)
" 2>/dev/null || echo "0")
    echo "[$(date)] Recent best: ${RECENT_BEST}%, current: ${PCT}%"

    # Check absolute floor
    if python3 -c "exit(0 if float('${PCT}') < ${SELFPLAY_MIN_WIN_PCT} else 1)" 2>/dev/null; then
        REGRESSION_DETECTED=true
        echo "[$(date)] ⚠ REGRESSION: v${N}=${PCT}% below floor ${SELFPLAY_MIN_WIN_PCT}%"
    fi
    # Check relative drop from recent best
    if python3 -c "exit(0 if float('${RECENT_BEST}') > 0 and float('${PCT}') < float('${RECENT_BEST}') * 0.65 else 1)" 2>/dev/null; then
        REGRESSION_DETECTED=true
        echo "[$(date)] ⚠ REGRESSION: v${N}=${PCT}% is >35% drop from recent best ${RECENT_BEST}%"
    fi

    if $REGRESSION_DETECTED; then
        echo "[$(date)] Circuit breaker: will collect vs-heuristic (useful for recovery) but SKIP selfplay."
        echo "[$(date)] Future gens will auto-skip v${N} selfplay via dynamic win-rate filter."
    fi
fi

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
                --temperature 1.0 \
                2>&1 | tee logs/collect_v${N}_vs_heuristic.log
        else
            echo "[$(date)] WARNING: C++ binary missing — falling back to Python collector"
            nice -n 10 uv run python scripts/collect_learned_vs_heuristic.py \
                --checkpoint "$CKPT" --n-games "$GAMES_VSH" --workers 16 \
                --seed "$VSH_SEED" --out "$VSH_OUT" \
                --value-guided --value-guided-k 4 \
                2>&1 | tee logs/collect_v${N}_vs_heuristic.log
        fi
        echo "[$(date)] v${N}-vs-heuristic (USSR) collection done."

        # ── Collect learned-as-US vs heuristic ───────────────────────────────
        # Model must learn both sides. Without this, US-acting rows come from
        # the heuristic — the model can never surpass heuristic at US play.
        if [ ! -f "$VSH_US_OUT" ]; then
            echo "[$(date)] Collecting v${N}-as-US-vs-heuristic (${GAMES_VSH} games, seed=${VSH_US_SEED})..."
            if [ -f "build-ninja/cpp/tools/ts_collect_selfplay_rows_jsonl" ]; then
                bash scripts/collect_cpp.sh \
                    --checkpoint "$CKPT" \
                    --learned-side us \
                    --games "$GAMES_VSH" \
                    --seed "$VSH_US_SEED" \
                    --out "$VSH_US_OUT" \
                    --temperature 1.0 \
                    2>&1 | tee logs/collect_v${N}_us_vs_heuristic.log
            else
                echo "[$(date)] WARNING: C++ binary missing — skipping US-side collection"
            fi
            echo "[$(date)] v${N}-as-US-vs-heuristic collection done."
        fi

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

        if $REGRESSION_DETECTED; then
            echo "[$(date)] SKIP selfplay: circuit breaker active (v${N}=${PCT}%)"
        elif [ "$GAMES_VSL" -gt 0 ] && [ -f "$PREV_CKPT" ] && [ ! -f "$VSL_OUT" ]; then
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
                --temperature 1.0 \
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

        # ── Mine hard positions + sparse teacher search ───────────────────────
        TSCORE_SO=$(find build-ninja/bindings/ -name "tscore*.so" -print -quit 2>/dev/null || true)
        if [ -f "$TEACHER_TARGETS" ]; then
            echo "[$(date)] Teacher targets already exist, skipping search: $TEACHER_TARGETS"
        elif [ -z "$TSCORE_SO" ]; then
            echo "[$(date)] Skipping teacher search: no tscore binding found under build-ninja/bindings"
        else
            mkdir -p "$TEACHER_DIR"
            if [ ! -f "$TEACHER_TARGETS_TS" ]; then
                echo "[$(date)] Exporting v${N} TorchScript: $CKPT -> $TEACHER_TARGETS_TS"
                nice -n 10 uv run python cpp/tools/export_baseline_to_torchscript.py \
                    --checkpoint "$CKPT" \
                    --out "$TEACHER_TARGETS_TS" \
                    2>&1
            fi
            echo "[$(date)] Mining top-1000 hard positions from $VSH_OUT -> $TEACHER_POSITIONS"
            nice -n 10 uv run python scripts/mine_hard_positions.py \
                --data "$VSH_OUT" \
                --checkpoint "$CKPT" \
                --out "$TEACHER_POSITIONS" \
                --top-k 1000 \
                2>&1 | tee logs/mine_teacher_v${N}.log
            echo "[$(date)] Running sparse teacher search (n_sim=200) -> $TEACHER_TARGETS"
            nice -n 10 uv run python scripts/teacher_search.py \
                --positions "$TEACHER_POSITIONS" \
                --model "$TEACHER_TARGETS_TS" \
                --out "$TEACHER_TARGETS" \
                --n-sim 200 \
                2>&1 | tee logs/teacher_search_v${N}.log
            echo "[$(date)] Teacher search done."
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

        # ── Filter US-side vs-heuristic data ─────────────────────────────────
        # US-side data is only useful if the model actually wins a decent fraction
        # of games.  At <10% US win rate, including this data teaches the model to
        # make losing moves (96% of rows are from games the model lost).
        # Filter to US-winning games only; skip if fewer than 20 US wins.
        VSH_US_FILTERED=data/combined_v${N}_vsh_us_filtered/filtered.parquet
        if [ -f "$VSH_US_OUT" ]; then
            echo "[$(date)] Filtering $VSH_US_OUT (defcon1 cap + US-wins only)..."
            nice -n 10 uv run python scripts/filter_bad_games.py \
                --input "$VSH_US_OUT" \
                --output "${VSH_US_FILTERED}.tmp" \
                --max-defcon1-pct 15 \
                2>&1 | tee logs/filter_v${N}_us.log
            # Keep only games the learned US player won (winner_side == -1)
            nice -n 10 python3 -c "
import polars as pl, sys
df = pl.read_parquet('${VSH_US_FILTERED}.tmp')
if 'winner_side' not in df.columns:
    print('WARNING: no winner_side column, skipping US win filter')
    df.write_parquet('${VSH_US_FILTERED}')
    sys.exit(0)
wins = df.filter(pl.col('winner_side') == -1)
n_games = wins['game_id'].n_unique() if len(wins) > 0 else 0
print(f'US wins: {n_games} games, {len(wins)} rows (from {df[\"game_id\"].n_unique()} total games)')
if n_games < 20:
    print('Too few US wins (<20 games) — skipping US data for this generation')
    sys.exit(1)
wins.write_parquet('${VSH_US_FILTERED}')
print(f'Wrote {len(wins)} US-winning rows to ${VSH_US_FILTERED}')
" 2>&1 | tee -a logs/filter_v${N}_us.log
            US_FILTER_RC=$?
            rm -f "${VSH_US_FILTERED}.tmp"
            if [ "$US_FILTER_RC" -ne 0 ]; then
                rm -f "$VSH_US_FILTERED"
                echo "[$(date)] US-side data dropped (too few wins)."
            else
                echo "[$(date)] US-side filter done (wins only)."
            fi
        fi

        # ── Build combined_v(N+1) and launch next generation ─────────────────
        NP1=$(( N + 1 ))
        COMBINED_NP1=data/combined_v${NP1}
        mkdir -p "$COMBINED_NP1"
        rm -f "$COMBINED_NP1"/*.parquet
        mkdir -p "$COMBINED_NP1/teacher_targets"
        rm -f "$COMBINED_NP1/teacher_targets"/*.parquet

        # Rolling window: carry forward files from combined_vN, skipping those
        # whose embedded version number is older than (N+1 - MAX_GENS).
        # Files with no parseable version are always kept (seed/baseline data).
        # MAX_GENS=0 means keep everything.
        MIN_GEN=0
        if [ "$MAX_GENS" -gt 0 ]; then
            MIN_GEN=$(( NP1 - MAX_GENS ))
        fi
        # Dynamic selfplay quality gate: skip selfplay from gens with win rate
        # below threshold. VSH (vs-heuristic) data is always kept since the
        # heuristic provides a stronger label signal even when the learned side
        # is weak. The threshold prevents echo-chamber cascades where weak
        # models generate selfplay that makes the next gen even weaker.
        SELFPLAY_MIN_WIN_PCT=8
        DROPPED=0
        for f in "$COMBINED"/*.parquet; do
            fname=$(basename "$f")
            # Extract first _vNN_ or _vNN. version number from filename
            file_gen=$(echo "$fname" | grep -oP '(?<=_v)\d+' | head -1 || true)

            # Check if this is a selfplay file (learned_vN_vs_vM pattern)
            is_selfplay=false
            if [[ "$fname" =~ _vs_v[0-9]+ ]] && [[ ! "$fname" =~ _vs_heuristic ]]; then
                is_selfplay=true
            fi

            # For selfplay files, check the gen's benchmark win rate
            skip_weak_selfplay=false
            if $is_selfplay && [ -n "$file_gen" ] && [ -f results/benchmark_history.json ]; then
                gen_pct=$(python3 -c "
import json, sys
h = json.load(open('results/benchmark_history.json'))
pct = h.get('v${file_gen}', {}).get('learned_vs_heuristic', 100)
print(pct)
" 2>/dev/null || echo "100")
                if python3 -c "exit(0 if float('${gen_pct}') < ${SELFPLAY_MIN_WIN_PCT} else 1)" 2>/dev/null; then
                    skip_weak_selfplay=true
                fi
            fi

            # Anchor files (heuristic baseline, winning games) are always kept
            is_anchor=false
            if [[ "$fname" == *"anchor"* ]] || [[ "$fname" == "heuristic_"* ]]; then
                is_anchor=true
            fi

            if $is_anchor; then
                ln -sf "$(readlink -f "$f")" "$COMBINED_NP1/$fname"
            elif $skip_weak_selfplay; then
                DROPPED=$(( DROPPED + 1 ))
                echo "[$(date)] Rolling window: skipping weak selfplay (v${file_gen}=${gen_pct}% < ${SELFPLAY_MIN_WIN_PCT}%): $fname"
            elif [ -n "$file_gen" ] && [ "$MAX_GENS" -gt 0 ] && [ "$file_gen" -lt "$MIN_GEN" ]; then
                DROPPED=$(( DROPPED + 1 ))
                echo "[$(date)] Rolling window: dropping old gen v${file_gen} file: $fname"
            else
                ln -sf "$(readlink -f "$f")" "$COMBINED_NP1/$fname"
            fi
        done
        ln -sf "$(readlink -f "$VSH_FILTERED")" \
            "$COMBINED_NP1/learned_v${N}_vs_heuristic_filtered.parquet"
        # Include US-side vs-heuristic data
        if [ -f "$VSH_US_FILTERED" ]; then
            ln -sf "$(readlink -f "$VSH_US_FILTERED")" \
                "$COMBINED_NP1/learned_v${N}_us_vs_heuristic_filtered.parquet"
            echo "[$(date)] Added US-side vs-heuristic v${N} to combined_v${NP1}"
        fi
        if [ -f "$TEACHER_TARGETS" ]; then
            ln -sf "$(readlink -f "$TEACHER_TARGETS")" \
                "$COMBINED_NP1/teacher_targets/teacher_targets_v${N}.parquet"
            echo "[$(date)] Added teacher targets v${N} to combined_v${NP1}"
        fi

        # Include learned-vs-learned data if it was collected this generation
        if [ -f "$VSL_OUT" ]; then
            ln -sf "$(readlink -f "$VSL_OUT")" \
                "$COMBINED_NP1/learned_v${N}_vs_v${NM1}_selfplay.parquet"
            echo "[$(date)] Added self-play v${N}-vs-v${NM1} to combined_v${NP1}"
        fi

        # Include heuristic anchor (always present — provides baseline quality data)
        HEURISTIC_ANCHOR="data/selfplay/heuristic_3000games_v3_seed20000.parquet"
        if [ -f "$HEURISTIC_ANCHOR" ]; then
            ln -sf "$(readlink -f "$HEURISTIC_ANCHOR")" \
                "$COMBINED_NP1/heuristic_anchor_3000g.parquet"
            echo "[$(date)] Added heuristic anchor to combined_v${NP1}"
        fi

        # Include curated winning games anchor dataset (VP>5 or wargames wins)
        WINNING_GAMES="data/curated/winning_games_v55_v75.parquet"
        if [ -f "$WINNING_GAMES" ]; then
            ln -sf "$(readlink -f "$WINNING_GAMES")" \
                "$COMBINED_NP1/winning_games_anchor.parquet"
            echo "[$(date)] Added winning games anchor to combined_v${NP1}"
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
