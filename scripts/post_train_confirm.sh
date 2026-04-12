#!/usr/bin/env bash
# post_train_confirm.sh — confirmation tournament + Elo placement after PPO training.
#
# Designed to be called from train_ppo.py --post-train-hook or manually.
# Handles arbitrary version names (v65, v66_sc, etc.) — no numeric-only assumption.
#
# Modes:
#   --incremental (DEFAULT): place new model vs previous best + 2 fixtures + heuristic.
#                            ~4-5 matches, <5 minutes. Use for post-training automation.
#   --full:                  full round-robin across ALL models in scripted_for_elo/.
#                            Can be 100+ matches. Explicit user request ONLY.
#   --dry-run:               print match schedule without executing. Always check this first.
#
# Usage:
#   bash scripts/post_train_confirm.sh <run_dir>                    # incremental (default)
#   bash scripts/post_train_confirm.sh <run_dir> --dry-run          # preview scope
#   bash scripts/post_train_confirm.sh <run_dir> --full             # full ladder update
#
# Policy: post-training confirmation MUST use --incremental. >20 new matches = stop and investigate.
set -euo pipefail
cd /home/dkord/code/twilight-struggle-ai

RUN_DIR="${1:?Usage: post_train_confirm.sh <run_dir> [--incremental|--full] [--dry-run]}"
shift

MODE="incremental"
DRY_RUN=0
for arg in "$@"; do
  case "$arg" in
    --full)        MODE="full" ;;
    --incremental) MODE="incremental" ;;
    --dry-run)     DRY_RUN=1 ;;
  esac
done

# Derive version name from run dir: ppo_v66_sc_league -> v66_sc
VERSION=$(basename "$RUN_DIR" | sed 's/^ppo_//; s/_league$//')
LADDER="results/elo/elo_full_ladder.json"
SCRIPT_DIR="data/checkpoints/scripted_for_elo"
LOG_PREFIX="results/logs/elo"
CONFIRM_LOG="${LOG_PREFIX}/confirm_${VERSION}.log"
ELO_LOG="${LOG_PREFIX}/elo_${VERSION}_update.log"

# Corrupted-era models: trained with T=1.2 + log_prob bugs (v27-v41). Excluded permanently.
EXCLUDED_VERSIONS="27 28 29 30 31 32 33 34 35 36 37 38 39 40 41"
MIN_SCRIPTED_VERSION=8

mkdir -p "$LOG_PREFIX"

timestamp() { date -u '+%Y-%m-%dT%H:%M:%SZ'; }

log_decision() {
  echo "[$(timestamp)] $1" >> results/autonomous_decisions.log
}

if [ "$DRY_RUN" = "1" ]; then
  echo "=== DRY RUN: post_train_confirm.sh for $VERSION (mode=$MODE) ==="
fi

# ---------------------------------------------------------------------------
# Step 1: Confirmation tournament (pick best checkpoint within run)
# ---------------------------------------------------------------------------
if [ -f "${RUN_DIR}/panel_eval_history.json" ]; then
  PANEL_WEAKEST="${SCRIPT_DIR}/v8_scripted.pt"
  PANEL_MID="${SCRIPT_DIR}/v14_scripted.pt"
  PANEL_FRONTIER="${SCRIPT_DIR}/v22_scripted.pt"
  if [ "$DRY_RUN" = "1" ]; then
    echo "Step 1: Would run ppo_confirm_best.py vs v8, v14, v22, heuristic (200 games each)"
  else
    log_decision "Running confirmation tournament for $VERSION ..."
    uv run python scripts/ppo_confirm_best.py \
      --run-dir "$RUN_DIR" \
      --fixtures \
        "v8:${PANEL_WEAKEST}" \
        "v14:${PANEL_MID}" \
        "v22:${PANEL_FRONTIER}" \
        "heuristic" \
      --n-top 8 \
      --n-games 200 \
      --anchor v14 --anchor-elo 2015 \
      --script-dir "$SCRIPT_DIR" \
      2>&1 | tee "$CONFIRM_LOG"
    log_decision "Confirmation tournament done for $VERSION"
  fi
else
  echo "No panel_eval_history.json for $VERSION — skipping confirmation tournament"
fi

# ---------------------------------------------------------------------------
# Step 2: Copy scripted checkpoint to scripted_for_elo/
# ---------------------------------------------------------------------------
FINISHED_SCRIPTED="${SCRIPT_DIR}/${VERSION}_scripted.pt"
FINISHED_SCRIPTED_SRC="${RUN_DIR}/ppo_final_scripted.pt"
if [ -f "${RUN_DIR}/ppo_best_scripted.pt" ]; then
  FINISHED_SCRIPTED_SRC="${RUN_DIR}/ppo_best_scripted.pt"
fi
if [ "$DRY_RUN" = "1" ]; then
  echo "Step 2: Would copy ${FINISHED_SCRIPTED_SRC} -> ${FINISHED_SCRIPTED}"
elif [ -f "${FINISHED_SCRIPTED_SRC}" ] && [ ! -f "${FINISHED_SCRIPTED}" ]; then
  mkdir -p "$SCRIPT_DIR"
  cp "${FINISHED_SCRIPTED_SRC}" "${FINISHED_SCRIPTED}"
  log_decision "Copied ${FINISHED_SCRIPTED_SRC} -> ${FINISHED_SCRIPTED}"
fi

# ---------------------------------------------------------------------------
# Step 3: Elo placement
# ---------------------------------------------------------------------------
if [ "$MODE" = "incremental" ]; then
  # INCREMENTAL: new model vs previous best + 2 nearest fixtures + heuristic only.
  # Reads the current ladder to find the top-rated model as "previous best".
  PREV_BEST=$(python3 -c "
import json, sys
try:
    d = json.load(open('$LADDER'))
    ratings = d.get('ratings', {})
    # Exclude the new version itself
    others = {k: v for k, v in ratings.items() if k != '$VERSION'}
    if others:
        best = max(others.items(), key=lambda x: x[1].get('elo', 0))
        print(best[0])
    else:
        print('v55')
except Exception:
    print('v55')
" 2>/dev/null)

  # Fixed fixture set: prev_best + v55 (frontier) + v14 (anchor) + heuristic (deduplicated)
  INCREMENTAL_FIXTURES="${PREV_BEST} v55 v14 heuristic"

  # Resolve to paths (deduplicate fixture names)
  MODELS="heuristic"
  SEEN=""
  for fixture in $PREV_BEST v55 v14; do
    echo "$SEEN" | grep -qw "$fixture" && continue  # skip duplicate
    SEEN="$SEEN $fixture"
    pt="${SCRIPT_DIR}/${fixture}_scripted.pt"
    [ -f "$pt" ] && MODELS="$MODELS ${fixture}:${pt}"
  done
  # Add new version
  NEW_PT="${RUN_DIR}/ppo_best_scripted.pt"
  [ -f "$NEW_PT" ] || NEW_PT="${RUN_DIR}/ppo_final_scripted.pt"
  [ -f "$NEW_PT" ] || NEW_PT="${FINISHED_SCRIPTED}"
  MODELS="$MODELS ${VERSION}:${NEW_PT}"

  MODEL_COUNT=$(echo $MODELS | wc -w)
  NEW_MATCHES=$((MODEL_COUNT * (MODEL_COUNT - 1) / 2))

  if [ "$DRY_RUN" = "1" ]; then
    echo "Step 3 (incremental): Would run round_robin on: $MODELS"
    echo "  ~$NEW_MATCHES total pairs (most will be cached), ~$((NEW_MATCHES < 5 ? NEW_MATCHES : MODEL_COUNT - 1)) new matches"
    echo "  Estimated runtime: <5 minutes"
    exit 0
  fi

  log_decision "Elo incremental placement: $VERSION vs $INCREMENTAL_FIXTURES"
  echo "=== ELO incremental placement: $VERSION ===" | tee "$ELO_LOG"
  uv run python scripts/run_elo_tournament.py \
    --models $MODELS \
    --games 200 --anchor v14 --anchor-elo 2015 \
    --schedule round_robin \
    ${LADDER:+--resume-from "$LADDER"} \
    --out "$LADDER" \
    --script-dir "$SCRIPT_DIR" \
    --match-cache-dir results/matches \
    2>&1 | tee -a "$ELO_LOG"

else
  # FULL: round-robin across all models (explicit user request only)
  echo "WARNING: full mode — this may schedule 100+ matches and take >1 hour" | tee "$ELO_LOG"
  log_decision "Elo FULL ladder update requested for $VERSION"

  MODELS="heuristic"
  for scripted_path in "${SCRIPT_DIR}"/*_scripted.pt; do
    [ -f "$scripted_path" ] || continue
    fname=$(basename "$scripted_path")
    name="${fname%_scripted.pt}"
    ver="${name#v}"
    fix_num="${ver%%[^0-9]*}"
    if [ -n "$fix_num" ]; then
      if [ "$fix_num" -lt "$MIN_SCRIPTED_VERSION" ] 2>/dev/null; then continue; fi
      if echo "$EXCLUDED_VERSIONS" | grep -qw "$fix_num"; then continue; fi
    fi
    if [ "$name" = "$VERSION" ]; then
      BEST_PATH="${RUN_DIR}/ppo_best.pt"
      [ -f "$BEST_PATH" ] || BEST_PATH="${RUN_DIR}/ppo_final.pt"
      [ -f "$BEST_PATH" ] && MODELS="$MODELS ${name}:${BEST_PATH}" || true
    else
      MODELS="$MODELS ${name}:${scripted_path}"
    fi
  done

  if [ "$DRY_RUN" = "1" ]; then
    N=$(echo $MODELS | wc -w)
    echo "Step 3 (full): Would run round_robin on $N models"
    echo "  ~$((N * (N-1) / 2)) total pairs"
    echo "  Models: $MODELS"
    exit 0
  fi

  log_decision "Elo full update: $(echo $MODELS | wc -w) models"
  echo "=== ELO full update ===" | tee -a "$ELO_LOG"
  uv run python scripts/run_elo_tournament.py \
    --models $MODELS \
    --games 400 --anchor v14 --anchor-elo 2015 \
    --schedule round_robin \
    ${LADDER:+--resume-from "$LADDER"} \
    --out "$LADDER" \
    --script-dir "$SCRIPT_DIR" \
    --match-cache-dir results/matches \
    2>&1 | tee -a "$ELO_LOG"
fi

# ---------------------------------------------------------------------------
# Report result
# ---------------------------------------------------------------------------
ELO_RESULT=$(python3 -c "
import json
try:
    d = json.load(open('$LADDER'))
    r = d['ratings'].get('$VERSION', {})
    print(f\"elo={r.get('elo','?'):.0f} elo_ussr={r.get('elo_ussr','?'):.0f} elo_us={r.get('elo_us','?'):.0f}\")
except Exception as e:
    print(f'error: {e}')
" 2>/dev/null)

log_decision "Elo done: $VERSION $ELO_RESULT"
echo "Done. $VERSION: $ELO_RESULT"
