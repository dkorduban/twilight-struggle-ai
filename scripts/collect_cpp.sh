#!/bin/bash
# collect_cpp.sh — C++ self-play collection + JSONL-to-Parquet conversion.
#
# Runs the native C++ ts_collect_selfplay_rows_jsonl binary (via chunked
# run_native_collection.py) and converts the resulting JSONL to a Parquet
# file compatible with train_baseline.py.
#
# For heuristic-vs-heuristic (no model):
#   bash scripts/collect_cpp.sh \
#       --games 1000 --seed 42 \
#       --ussr-policy minimal_hybrid --us-policy minimal_hybrid \
#       --out data/selfplay/heuristic_1000g.parquet
#
# For learned-vs-heuristic (requires a TorchScript model):
#   bash scripts/collect_cpp.sh \
#       --games 2000 --seed 99 \
#       --checkpoint data/checkpoints/retrain_v53/baseline_best.pt \
#       --learned-side ussr \
#       --out data/selfplay/learned_v53_vs_heuristic_2000g.parquet
#
# For learned-vs-learned (two models; provide pre-exported TorchScript files):
#   bash scripts/collect_cpp.sh \
#       --games 1000 --seed 42 \
#       --ussr-model data/checkpoints/retrain_v57/baseline_best_scripted.pt \
#       --us-model   data/checkpoints/retrain_v56/baseline_best_scripted.pt \
#       --out data/selfplay/learned_v57_vs_v56_1000g.parquet
#
# The TorchScript export step runs automatically if needed.
# Intermediate JSONL chunks are written to --chunk-dir (default: /tmp/cpp_chunks_$$)
# and cleaned up on success.
#
# Speed (single C++ thread, WSL2):
#   heuristic-vs-heuristic:      ~45 games/sec
#   learned-vs-heuristic (v53):  ~9 games/sec
#
# Compare: Python 16-worker learned-vs-heuristic: ~8 games/sec total
# (C++ single-thread is already on par; add parallelism by running multiple
# instances with different --seed values if more throughput is needed.)

set -euo pipefail

cd /home/dkord/code/twilight-struggle-ai

# ── Defaults ──────────────────────────────────────────────────────────────────
GAMES=1000
SEED=12345
CHUNK_SIZE=256
USSR_POLICY="minimal_hybrid"
US_POLICY="minimal_hybrid"
CHECKPOINT=""
LEARNED_SIDE="ussr"
USSR_MODEL=""
US_MODEL=""
OUT=""
CHUNK_DIR=""
ROWS_TOOL="build-ninja/cpp/tools/ts_collect_selfplay_rows_jsonl"
EXPORT_SCRIPT="cpp/tools/export_baseline_to_torchscript.py"
KEEP_CHUNKS=0
TEMPERATURE=""
EPSILON=""
EXPLORATION_RATE=""

# ── Parse args ────────────────────────────────────────────────────────────────
while [[ $# -gt 0 ]]; do
    case $1 in
        --games)            GAMES=$2;            shift 2 ;;
        --seed)             SEED=$2;             shift 2 ;;
        --chunk-size)       CHUNK_SIZE=$2;       shift 2 ;;
        --ussr-policy)      USSR_POLICY=$2;      shift 2 ;;
        --us-policy)        US_POLICY=$2;        shift 2 ;;
        --checkpoint)       CHECKPOINT=$2;       shift 2 ;;
        --learned-side)     LEARNED_SIDE=$2;     shift 2 ;;
        --ussr-model)       USSR_MODEL=$2;       shift 2 ;;
        --us-model)         US_MODEL=$2;         shift 2 ;;
        --out)              OUT=$2;              shift 2 ;;
        --chunk-dir)        CHUNK_DIR=$2;        shift 2 ;;
        --rows-tool)        ROWS_TOOL=$2;        shift 2 ;;
        --temperature)      TEMPERATURE=$2;      shift 2 ;;
        --epsilon)          EPSILON=$2;          shift 2 ;;
        --exploration-rate) EXPLORATION_RATE=$2;  shift 2 ;;
        --keep-chunks)
            if [[ $# -gt 1 && ! "$2" =~ ^-- ]]; then
                KEEP_CHUNKS=$2
                shift 2
            else
                KEEP_CHUNKS=1
                shift
            fi
            ;;
        -h|--help)
            sed -n '2,50p' "$0"
            exit 0
            ;;
        *)
            echo "Unknown arg: $1" >&2
            exit 1
            ;;
    esac
done

if [ -z "$OUT" ]; then
    echo "ERROR: --out is required" >&2
    exit 1
fi

# ── TorchScript export (only if a checkpoint was provided) ────────────────────
# In two-model mode (--ussr-model / --us-model), the caller provides pre-exported
# TorchScript files directly; no export step is needed.
LEARNED_MODEL_ARG=""
if [ -n "$USSR_MODEL" ] || [ -n "$US_MODEL" ]; then
    : # Two-model mode: use --ussr-model / --us-model args directly
elif [ -n "$CHECKPOINT" ]; then
    # Single-model mode: export checkpoint to TorchScript.
    CKPT_STEM="${CHECKPOINT%.pt}"
    TS_PATH="${CKPT_STEM}_scripted.pt"
    if [ ! -f "$TS_PATH" ]; then
        echo "[collect_cpp] Exporting TorchScript: $CHECKPOINT -> $TS_PATH"
        nice -n 10 uv run python "$EXPORT_SCRIPT" \
            --checkpoint "$CHECKPOINT" \
            --out "$TS_PATH"
    else
        echo "[collect_cpp] TorchScript already exists: $TS_PATH"
    fi
    LEARNED_MODEL_ARG="$TS_PATH"
fi

# ── Chunk directory ───────────────────────────────────────────────────────────
if [ -z "$CHUNK_DIR" ]; then
    CHUNK_DIR="/tmp/cpp_chunks_$$"
fi
mkdir -p "$CHUNK_DIR"

echo "[collect_cpp] Collecting $GAMES games  seed=$SEED  out=$OUT"
echo "[collect_cpp] Policies: ussr=$USSR_POLICY  us=$US_POLICY"
if [ -n "$USSR_MODEL" ]; then
    echo "[collect_cpp] USSR model: $USSR_MODEL"
fi
if [ -n "$US_MODEL" ]; then
    echo "[collect_cpp] US model: $US_MODEL"
fi
if [ -n "$LEARNED_MODEL_ARG" ]; then
    echo "[collect_cpp] Learned model: $LEARNED_MODEL_ARG  side=$LEARNED_SIDE"
fi

START_TIME=$(date +%s)

# ── Provenance tracking ─────────────────────────────────────────────────────
PROV_OUT="${OUT%.parquet}_provenance.json"
python3 -c "
from tsrl.provenance import capture_provenance, save_provenance
prov = capture_provenance(
    binaries=['$ROWS_TOOL'],
    extra={
        'games': $GAMES, 'seed': $SEED,
        'ussr_policy': '$USSR_POLICY', 'us_policy': '$US_POLICY',
        'checkpoint': '${CHECKPOINT:-none}',
        'ussr_model': '${USSR_MODEL:-none}', 'us_model': '${US_MODEL:-none}',
        'temperature': '${TEMPERATURE:-none}',
    },
)
save_provenance(prov, '$PROV_OUT')
print(f'[provenance] git={prov[\"git_sha\"][:8]} dirty={prov[\"git_dirty\"]}')
" 2>/dev/null || echo "[provenance] Skipped (non-fatal)"

# ── Run native collection (chunked via run_native_collection.py) ──────────────
NATIVE_ARGS=(
    --out-dir "$CHUNK_DIR"
    --games "$GAMES"
    --chunk-size "$CHUNK_SIZE"
    --seed "$SEED"
    --rows-tool "$ROWS_TOOL"
    --ussr-policy "$USSR_POLICY"
    --us-policy "$US_POLICY"
)
if [ -n "$USSR_MODEL" ]; then
    NATIVE_ARGS+=(--ussr-model "$USSR_MODEL")
fi
if [ -n "$US_MODEL" ]; then
    NATIVE_ARGS+=(--us-model "$US_MODEL")
fi
if [ -n "$LEARNED_MODEL_ARG" ]; then
    NATIVE_ARGS+=(
        --learned-model "$LEARNED_MODEL_ARG"
        --learned-side "$LEARNED_SIDE"
    )
fi
if [ -n "$TEMPERATURE" ]; then
    NATIVE_ARGS+=(--temperature "$TEMPERATURE")
fi
if [ -n "$EPSILON" ]; then
    NATIVE_ARGS+=(--epsilon "$EPSILON")
fi
if [ -n "$EXPLORATION_RATE" ]; then
    NATIVE_ARGS+=(--exploration-rate "$EXPLORATION_RATE")
fi

nice -n 10 uv run python cpp/tools/run_native_collection.py "${NATIVE_ARGS[@]}"

# ── Convert JSONL chunks to Parquet ──────────────────────────────────────────
echo "[collect_cpp] Converting JSONL to Parquet -> $OUT"
nice -n 10 uv run python scripts/jsonl_to_parquet.py \
    --input-dir "$CHUNK_DIR" \
    --out "$OUT"

# ── Cleanup ───────────────────────────────────────────────────────────────────
if [ "$KEEP_CHUNKS" -eq 0 ]; then
    rm -rf "$CHUNK_DIR"
fi

END_TIME=$(date +%s)
ELAPSED=$(( END_TIME - START_TIME ))
GPS=$(echo "scale=1; $GAMES / $ELAPSED" | bc 2>/dev/null || echo "?")

echo "[collect_cpp] Done: $GAMES games in ${ELAPSED}s (~${GPS} games/sec)"
echo "[collect_cpp] Output: $OUT"
