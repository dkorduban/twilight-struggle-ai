#!/usr/bin/env bash
# post_train_confirm.sh — candidate tournament + Elo placement after PPO training.
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
# Policy: post-training placement MUST use --incremental. >20 new matches = stop and investigate.
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
# Step 1: Candidate tournament (pick best checkpoint within run)
# ---------------------------------------------------------------------------
if [ -f "${RUN_DIR}/panel_eval_history.json" ]; then
  # Pre-sc panel (switched 2026-04-16): ALL SC models (v55_sc-v295_sc) degenerate
  # due to scoring card exploit (commit 5f8f4ea). Pre-sc models are true strongest:
  # v56=45.1%, v54=44.1%, v44=43.9%, v20=42.4%, v55=41.1% (500 games/side vs heuristic)
  PANEL_V56="${SCRIPT_DIR}/v56_scripted.pt"
  PANEL_V54="${SCRIPT_DIR}/v54_scripted.pt"
  PANEL_V44="${SCRIPT_DIR}/v44_scripted.pt"
  PANEL_V20="${SCRIPT_DIR}/v20_scripted.pt"
  PANEL_V55="${SCRIPT_DIR}/v55_scripted.pt"
  if [ "$DRY_RUN" = "1" ]; then
    echo "Step 1: Would run ppo_confirm_best.py vs v56, v54, v44, v20, v55 (150 games each)"
  else
    log_decision "Running candidate tournament for $VERSION ..."
    uv run python scripts/ppo_confirm_best.py \
      --run-dir "$RUN_DIR" \
      --fixtures \
        "v56:${PANEL_V56}" \
        "v54:${PANEL_V54}" \
        "v44:${PANEL_V44}" \
        "v20:${PANEL_V20}" \
        "v55:${PANEL_V55}" \
      --n-top 8 \
      --n-games 150 \
      --anchor v56 --anchor-elo 1900 \
      --script-dir "$SCRIPT_DIR" \
      2>&1 | tee "$CONFIRM_LOG"
    log_decision "Candidate tournament done for $VERSION"
  fi
else
  echo "No panel_eval_history.json for $VERSION — skipping candidate tournament"
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
  # INCREMENTAL — fast Elo placement with zero redundant games.
  #
  # Strategy:
  #   - The candidate tournament (Step 1) already played VERSION vs PANEL
  #     {v56, v54, v44, v20, v55} — those 5 pairs are in the SQL match cache.
  #   - We add 3 DIVERSE opponents chosen to span the full Elo range:
  #     bottom-quartile, median, and top (excluding panel models).
  #     This anchors the rating across the full distribution, not just the top.
  #   - Run round-robin among (panel + diverse + VERSION).
  #     The 5 panel pairs are loaded from cache (0 new games).
  #     Only the 3 diverse pairs are played (~600 games, ~3-5 min).
  #   - Merge only VERSION's updated rating into elo_full_ladder.json.

  # Panel fixtures used in ppo_confirm_best.py (Step 1) — results already cached.
  PANEL="v56 v54 v44 v20 v55"

  # Pick 3 diverse opponents from the full ladder, spanning the Elo range.
  # Exclude panel members, heuristic, and the new version itself.
  DIVERSE_FIXTURES=$(python3 - "$VERSION" "$LADDER" "$SCRIPT_DIR" "$PANEL" << 'PYEOF'
import json, os, sys
version = sys.argv[1]
ladder_path = sys.argv[2]
script_dir = sys.argv[3]
panel = set(sys.argv[4].split())

try:
    d = json.load(open(ladder_path))
except Exception:
    d = {}
ratings = d.get("ratings", {})

import re
def is_6mode_sc(name):
    # Only 6-mode _sc models (v205_sc+) for meaningful diverse games.
    # Old 5-mode _sc (v55_sc-v204_sc) and non-_sc models have inflated Elo
    # from the 5-mode pool and don't provide useful Elo anchoring.
    m = re.match(r"v(\d+)_sc$", name)
    return bool(m and int(m.group(1)) >= 205)

# Build candidate list: 6-mode _sc models with a scripted checkpoint on disk,
# not in panel, not heuristic, not the new version.
candidates = []
for name, info in ratings.items():
    if name in panel or name == version or name == "heuristic":
        continue
    if not is_6mode_sc(name):
        continue
    pt = os.path.join(script_dir, f"{name}_scripted.pt")
    if not os.path.exists(pt):
        continue
    candidates.append((name, info.get("elo", 1500)))

if not candidates:
    sys.exit(0)

candidates.sort(key=lambda x: x[1])
n = len(candidates)

picks = []
# Bottom quartile
picks.append(candidates[n // 4][0])
# Median
picks.append(candidates[n // 2][0])
# Top (strongest not in panel)
picks.append(candidates[-1][0])

# Deduplicate (possible if n is small)
seen = set()
out = []
for p in picks:
    if p not in seen:
        seen.add(p)
        out.append(p)

print(" ".join(out))
PYEOF
)

  # Resolve new version's checkpoint path
  NEW_PT="${RUN_DIR}/ppo_best_scripted.pt"
  [ -f "$NEW_PT" ] || NEW_PT="${RUN_DIR}/ppo_final_scripted.pt"
  # Mid-training incremental check: use latest per-iter scripted checkpoint
  [ -f "$NEW_PT" ] || NEW_PT=$(ls -t "${RUN_DIR}/ppo_iter"*"_scripted.pt" 2>/dev/null | head -1)
  [ -f "$NEW_PT" ] || NEW_PT="${FINISHED_SCRIPTED}"

  # Build --models arg: panel + diverse + new version
  MODELS=""
  SEEN=""
  for fixture in $PANEL ${DIVERSE_FIXTURES:-}; do
    echo "$SEEN" | grep -qw "$fixture" && continue
    SEEN="$SEEN $fixture"
    pt="${SCRIPT_DIR}/${fixture}_scripted.pt"
    [ -f "$pt" ] && MODELS="$MODELS ${fixture}:${pt}"
  done
  MODELS="${MODELS# } ${VERSION}:${NEW_PT}"

  # Count: how many pairs involve VERSION (= new games to play)
  TOTAL_OPPONENTS=$(echo "$PANEL ${DIVERSE_FIXTURES:-}" | wc -w)
  PANEL_CACHED=5
  NEW_GAME_PAIRS=$((TOTAL_OPPONENTS - PANEL_CACHED))
  NEW_GAME_PAIRS=$((NEW_GAME_PAIRS < 0 ? 0 : NEW_GAME_PAIRS))

  if [ "$DRY_RUN" = "1" ]; then
    echo "Step 3 (incremental):"
    echo "  Panel (cached, 0 new games): $PANEL"
    echo "  Diverse (new games):         ${DIVERSE_FIXTURES:-(none found)}"
    echo "  New pairs to play:           ~$NEW_GAME_PAIRS × 200 games = $((NEW_GAME_PAIRS * 200)) games"
    echo "  Estimated runtime:           ~$((NEW_GAME_PAIRS * 2 + 1)) minutes"
    echo "  Models in pool:              $MODELS"
    exit 0
  fi

  log_decision "Elo incremental placement: $VERSION | panel(cached)=$PANEL | diverse=$DIVERSE_FIXTURES"
  echo "=== ELO incremental placement: $VERSION ===" | tee "$ELO_LOG"

  # Write to scratch file; merge only VERSION's rating into the full ladder.
  # Never overwrite elo_full_ladder.json with only the incremental subset.
  INCREMENTAL_OUT="${LOG_PREFIX}/elo_${VERSION}_incremental.json"

  uv run python scripts/run_elo_tournament.py \
    --models $MODELS \
    --games 200 --anchor v56 --anchor-elo 1900 \
    --schedule round_robin \
    --mode incremental --new-model "$VERSION" \
    ${LADDER:+--resume-from "$LADDER"} \
    --out "$INCREMENTAL_OUT" \
    --script-dir "$SCRIPT_DIR" \
    --match-cache-dir results/matches \
    2>&1 | tee -a "$ELO_LOG"

  # Merge VERSION's rating into the full ladder (atomic-ish via read-modify-write)
  python3 -c "
import json, sys, os
try:
    incremental = json.load(open('$INCREMENTAL_OUT'))
    ladder_path = '$LADDER'
    ladder = json.load(open(ladder_path)) if os.path.exists(ladder_path) else {'ratings': {}}
    new_rating = incremental['ratings'].get('$VERSION')
    if new_rating:
        ladder['ratings']['$VERSION'] = new_rating
        with open(ladder_path, 'w') as f:
            json.dump(ladder, f, indent=2)
        print(f'[confirm] Merged \$VERSION into {ladder_path}: elo={new_rating[\"elo\"]:.0f}')
    else:
        print('[confirm] WARNING: \$VERSION not found in incremental results', file=sys.stderr)
        sys.exit(1)
except Exception as e:
    print(f'[confirm] ERROR: {e}', file=sys.stderr)
    sys.exit(1)
" 2>&1 | tee -a "$ELO_LOG"

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
    --mode full --new-model "$VERSION" \
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
