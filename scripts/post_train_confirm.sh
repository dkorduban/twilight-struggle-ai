#!/usr/bin/env bash
# post_train_confirm.sh — confirmation tournament + Elo ladder update after PPO training.
#
# Designed to be called from train_ppo.py --post-train-hook or manually.
# Handles arbitrary version names (v65, v66_sc, etc.) — no numeric-only assumption.
#
# Usage:
#   bash scripts/post_train_confirm.sh <run_dir>
#   # e.g. bash scripts/post_train_confirm.sh data/checkpoints/ppo_v66_sc_league
#
# What it does:
#   1. Runs confirmation tournament (ppo_confirm_best.py) to pick best checkpoint
#   2. Copies scripted best to scripted_for_elo/
#   3. Updates the full Elo ladder (run_elo_tournament.py)
#   4. Logs all actions to results/autonomous_decisions.log
set -euo pipefail
cd /home/dkord/code/twilight-struggle-ai

RUN_DIR="${1:?Usage: post_train_confirm.sh <run_dir>}"

# Derive version name from run dir: ppo_v66_sc_league -> v66_sc
VERSION=$(basename "$RUN_DIR" | sed 's/^ppo_//; s/_league$//')
LADDER="results/elo/elo_full_ladder.json"
SCRIPT_DIR="data/checkpoints/scripted_for_elo"
LOG_PREFIX="results/logs/elo"
CONFIRM_LOG="${LOG_PREFIX}/confirm_${VERSION}.log"
ELO_LOG="${LOG_PREFIX}/elo_${VERSION}_update.log"

# Panel references for confirmation tournament
PANEL_WEAKEST="${SCRIPT_DIR}/v8_scripted.pt"
PANEL_MID="${SCRIPT_DIR}/v14_scripted.pt"
PANEL_FRONTIER="${SCRIPT_DIR}/v22_scripted.pt"

# Corrupted-era models: trained with T=1.2 + log_prob bugs (v27-v41). Excluded permanently.
EXCLUDED_VERSIONS="27 28 29 30 31 32 33 34 35 36 37 38 39 40 41"
MIN_SCRIPTED_VERSION=8

mkdir -p "$LOG_PREFIX"

timestamp() { date -u '+%Y-%m-%dT%H:%M:%SZ'; }

log_decision() {
  echo "[$(timestamp)] $1" >> results/autonomous_decisions.log
}

# ---------------------------------------------------------------------------
# Step 1: Confirmation tournament
# ---------------------------------------------------------------------------
if [ -f "${RUN_DIR}/panel_eval_history.json" ]; then
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
else
  log_decision "No panel_eval_history.json for $VERSION — skipping confirmation tournament"
fi

# ---------------------------------------------------------------------------
# Step 2: Copy scripted checkpoint to scripted_for_elo/
# ---------------------------------------------------------------------------
FINISHED_SCRIPTED="${SCRIPT_DIR}/${VERSION}_scripted.pt"
FINISHED_SCRIPTED_SRC="${RUN_DIR}/ppo_final_scripted.pt"
if [ -f "${RUN_DIR}/ppo_best_scripted.pt" ]; then
  FINISHED_SCRIPTED_SRC="${RUN_DIR}/ppo_best_scripted.pt"
fi
if [ -f "${FINISHED_SCRIPTED_SRC}" ] && [ ! -f "${FINISHED_SCRIPTED}" ]; then
  mkdir -p "$SCRIPT_DIR"
  cp "${FINISHED_SCRIPTED_SRC}" "${FINISHED_SCRIPTED}"
  log_decision "Copied ${FINISHED_SCRIPTED_SRC} -> ${FINISHED_SCRIPTED}"
fi

# ---------------------------------------------------------------------------
# Step 3: Full Elo ladder update
# ---------------------------------------------------------------------------
# Build model list dynamically from scripted_for_elo dir
MODELS="heuristic"
for scripted_path in "${SCRIPT_DIR}"/*_scripted.pt; do
  [ -f "$scripted_path" ] || continue
  fname=$(basename "$scripted_path")
  name="${fname%_scripted.pt}"
  # Extract version number for filtering (v12 -> 12, v66_sc -> skip filter)
  ver="${name#v}"
  # Only apply numeric filters to pure numeric versions
  if [[ "$ver" =~ ^[0-9]+$ ]]; then
    if [ "$ver" -lt "$MIN_SCRIPTED_VERSION" ]; then continue; fi
    # Skip corrupted-era models
    if echo "$EXCLUDED_VERSIONS" | grep -qw "$ver"; then continue; fi
  fi
  if [ "$name" = "$VERSION" ]; then
    # Use ppo_best.pt for the just-finished model (fresher than the scripted copy)
    BEST_PATH="${RUN_DIR}/ppo_best.pt"
    if [ -f "$BEST_PATH" ]; then
      MODELS="$MODELS ${name}:${BEST_PATH}"
    elif [ -f "${RUN_DIR}/ppo_final.pt" ]; then
      MODELS="$MODELS ${name}:${RUN_DIR}/ppo_final.pt"
    fi
  else
    MODELS="$MODELS ${name}:${scripted_path}"
  fi
done
# If VERSION not yet in scripted_for_elo and ppo_final.pt exists, add it
if [ -f "${RUN_DIR}/ppo_final.pt" ] && ! echo "$MODELS" | grep -q " ${VERSION}:"; then
  MODELS="$MODELS ${VERSION}:${RUN_DIR}/ppo_final.pt"
fi

if [ ! -f "$LADDER" ]; then
  log_decision "No existing ladder at $LADDER — creating fresh"
fi

log_decision "Elo ladder update: adding $VERSION (model count: $(echo $MODELS | wc -w))"

echo "=== ELO update: adding $VERSION ===" | tee "$ELO_LOG"
uv run python scripts/run_elo_tournament.py \
  --models $MODELS \
  --games 400 --anchor v14 --anchor-elo 2015 \
  --schedule round_robin \
  ${LADDER:+--resume-from "$LADDER"} \
  --out "$LADDER" \
  --script-dir "$SCRIPT_DIR" \
  --match-cache-dir results/matches \
  2>&1 | tee -a "$ELO_LOG"

ELO_FINISHED=$(python3 -c "
import json
with open('$LADDER') as f: d=json.load(f)
print(d['ratings'].get('$VERSION', {}).get('elo', 'N/A'))
")

log_decision "Elo update done: $VERSION = $ELO_FINISHED"
echo "Done. Elo($VERSION) = $ELO_FINISHED"
