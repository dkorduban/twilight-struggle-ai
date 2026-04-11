#!/usr/bin/env bash
# ppo_loop_step.sh — called after each PPO run finishes.
# Usage: bash scripts/ppo_loop_step.sh <finished_version> <next_version>
# Example: bash scripts/ppo_loop_step.sh v14 v15
#
# Plateau rule: 3 consecutive runs with delta < 15 Elo vs pre-tournament rank-3
# Config (2026-04-11): 80 iters, ent 0.01->0.003, UPGO, all-version fixtures, UCB-PFSP c=2.0, k=6
set -euo pipefail
cd /home/dkord/code/twilight-struggle-ai

FINISHED=$1   # e.g. v14
NEXT=$2       # e.g. v15

FINISHED_DIR="data/checkpoints/ppo_${FINISHED}_league"
NEXT_DIR="data/checkpoints/ppo_${NEXT}_league"
LADDER="results/elo/elo_full_ladder.json"
ELO_LOG="results/logs/elo/elo_${FINISHED}_update.log"
NEXT_LOG="results/logs/ppo/ppo_${NEXT}.log"

# Fixtures updated 2026-04-11: use ALL good scripted versions as league fixtures.
# Broader opponent diversity provides harder training signal (Opus analysis:
# v45 paradox — lowest rollout_wr = highest Elo because of harder opponents).
FINISHED_SCRIPTED="data/checkpoints/scripted_for_elo/${FINISHED}_scripted.pt"
# Panel eval still uses 3 fixed references for comparability
PANEL_WEAKEST="data/checkpoints/scripted_for_elo/v8_scripted.pt"
PANEL_MID="data/checkpoints/scripted_for_elo/v14_scripted.pt"
PANEL_FRONTIER="data/checkpoints/scripted_for_elo/v22_scripted.pt"

# Corrupted-era models: trained with T=1.2 + log_prob bugs (v27-v41). Excluded permanently.
EXCLUDED_VERSIONS="27 28 29 30 31 32 33 34 35 36 37 38 39 40 41"
MIN_SCRIPTED_VERSION=8

# Build full fixture list from all good scripted versions (excluding corrupted era + self)
LEAGUE_FIXTURES=""
for fix_path in data/checkpoints/scripted_for_elo/*_scripted.pt; do
  [ -f "$fix_path" ] || continue
  fix_name=$(basename "$fix_path" | sed 's/_scripted\.pt//')
  fix_ver="${fix_name#v}"
  if ! [[ "$fix_ver" =~ ^[0-9]+$ ]]; then continue; fi
  if [ "$fix_ver" -lt "$MIN_SCRIPTED_VERSION" ]; then continue; fi
  # Skip corrupted-era models
  if echo "$EXCLUDED_VERSIONS" | grep -qw "$fix_ver"; then continue; fi
  # Skip the model about to be trained (it'll be the starting checkpoint)
  if [ "$fix_name" = "$NEXT" ]; then continue; fi
  LEAGUE_FIXTURES="$LEAGUE_FIXTURES $fix_path"
done
# Always include heuristic
LEAGUE_FIXTURES="$LEAGUE_FIXTURES __heuristic__"
FIXTURE_COUNT=$(echo $LEAGUE_FIXTURES | wc -w)
echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] League fixtures: $FIXTURE_COUNT opponents (all good versions + heuristic)" \
  >> results/autonomous_decisions.log

# --- Confirmation tournament: pick ppo_best.pt from panel eval history ---
# Runs ~10 min on CPU; selects the top-3 panel-eval checkpoints by avg combined WR,
# runs a round-robin tournament among them + fixtures, copies winner to ppo_best.pt.
CONFIRM_LOG="results/logs/elo/confirm_${FINISHED}.log"
if [ -f "${FINISHED_DIR}/panel_eval_history.json" ]; then
  echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Running confirmation tournament for $FINISHED ..." \
    >> results/autonomous_decisions.log
  uv run python scripts/ppo_confirm_best.py \
    --run-dir "$FINISHED_DIR" \
    --fixtures \
      "v8:${PANEL_WEAKEST}" \
      "v14:${PANEL_MID}" \
      "v22:${PANEL_FRONTIER}" \
      "heuristic" \
    --n-top 8 \
    --n-games 200 \
    --anchor v14 --anchor-elo 2015 \
    --script-dir data/checkpoints/scripted_for_elo \
    2>&1 | tee "$CONFIRM_LOG"
  echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Confirmation tournament done for $FINISHED" \
    >> results/autonomous_decisions.log
else
  echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] No panel_eval_history.json for $FINISHED — skipping confirmation tournament" \
    >> results/autonomous_decisions.log
fi

# ppo_best.pt set by confirmation tournament above; fall back to ppo_final.pt if missing.
FINISHED_CHECKPOINT="${FINISHED_DIR}/ppo_final.pt"
if [ -f "${FINISHED_DIR}/ppo_best.pt" ]; then
  FINISHED_CHECKPOINT="${FINISHED_DIR}/ppo_best.pt"
  echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Using ppo_best.pt for $FINISHED (confirmation tournament winner)" \
    >> results/autonomous_decisions.log
fi

# --- One-time checkpoint override (e.g. restart lineage from a different base) ---
# Create results/checkpoint_override_${NEXT}.txt with the desired checkpoint path to override.
OVERRIDE_FILE="results/checkpoint_override_${NEXT}.txt"
if [ -f "$OVERRIDE_FILE" ]; then
  OVERRIDE_PATH=$(cat "$OVERRIDE_FILE" | tr -d '[:space:]')
  if [ -f "$OVERRIDE_PATH" ]; then
    echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] OVERRIDE: $NEXT will start from $OVERRIDE_PATH (not $FINISHED_CHECKPOINT)" \
      >> results/autonomous_decisions.log
    FINISHED_CHECKPOINT="$OVERRIDE_PATH"
    mv "$OVERRIDE_FILE" "${OVERRIDE_FILE}.used"
  else
    echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] WARNING: override file $OVERRIDE_FILE found but path $OVERRIDE_PATH does not exist — ignoring" \
      >> results/autonomous_decisions.log
  fi
fi

# --- Copy finished model's scripted file to scripted_for_elo/ ---
# Use best scripted if available, else final scripted
FINISHED_SCRIPTED_SRC="${FINISHED_DIR}/ppo_final_scripted.pt"
if [ -f "${FINISHED_DIR}/ppo_best_scripted.pt" ]; then
  FINISHED_SCRIPTED_SRC="${FINISHED_DIR}/ppo_best_scripted.pt"
fi
if [ -f "${FINISHED_SCRIPTED_SRC}" ] && [ ! -f "${FINISHED_SCRIPTED}" ]; then
  cp "${FINISHED_SCRIPTED_SRC}" "${FINISHED_SCRIPTED}"
  echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Copied ${FINISHED_SCRIPTED_SRC} -> ${FINISHED_SCRIPTED}" \
    >> results/autonomous_decisions.log
fi

# --- Build model list dynamically from scripted_for_elo dir ---
# Only include heuristic + v8 and later (v1-v7 are too weak to be informative anchors)
# EXCLUDED_VERSIONS and MIN_SCRIPTED_VERSION defined at top of script

MODELS="heuristic"
# Include scripted models v${MIN_SCRIPTED_VERSION}+ (excluding the FINISHED one, handled separately)
for scripted_path in data/checkpoints/scripted_for_elo/*_scripted.pt; do
  [ -f "$scripted_path" ] || continue
  fname=$(basename "$scripted_path")
  name="${fname%_scripted.pt}"
  # Extract version number (e.g. v12 -> 12)
  ver="${name#v}"
  if ! [[ "$ver" =~ ^[0-9]+$ ]]; then continue; fi
  if [ "$ver" -lt "$MIN_SCRIPTED_VERSION" ]; then continue; fi
  # Skip corrupted-era models
  if echo "$EXCLUDED_VERSIONS" | grep -qw "$ver"; then continue; fi
  if [ "$name" = "$FINISHED" ]; then
    # Use ppo_final.pt for the just-finished model (fresher than the scripted copy)
    if [ -f "${FINISHED_DIR}/ppo_final.pt" ]; then
      MODELS="$MODELS ${name}:${FINISHED_DIR}/ppo_final.pt"
    fi
  else
    MODELS="$MODELS ${name}:${scripted_path}"
  fi
done
# If FINISHED not yet in scripted_for_elo (first time) and ppo_final.pt exists, add it
if [ -f "${FINISHED_DIR}/ppo_final.pt" ] && ! echo "$MODELS" | grep -q " ${FINISHED}:"; then
  MODELS="$MODELS ${FINISHED}:${FINISHED_DIR}/ppo_final.pt"
fi

echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] ppo_loop_step: $FINISHED finished, running ELO update then launching $NEXT" \
  >> results/autonomous_decisions.log

# --- Capture 3rd-place Elo BEFORE adding the new candidate ---
# Plateau rule: new_model.elo - pre_tournament_rank3.elo < 15
PRE_THIRD=$(python3 -c "
import json
with open('$LADDER') as f: d=json.load(f)
ppo = {n: v['elo'] for n, v in d['ratings'].items() if n != 'heuristic'}
ranked = sorted(ppo.items(), key=lambda x: -x[1])
if len(ranked) >= 3:
    print(f\"{ranked[2][0]}:{ranked[2][1]:.1f}\")
else:
    print('NONE')
" 2>/dev/null)

# --- ELO update (CPU, overlaps safely with GPU training) ---
echo "=== ELO update: adding $FINISHED ===" | tee "$ELO_LOG"
uv run python scripts/run_elo_tournament.py \
  --models $MODELS \
  --games 400 --anchor v14 --anchor-elo 2015 \
  --schedule round_robin \
  --resume-from "$LADDER" \
  --out "$LADDER" \
  --script-dir data/checkpoints/scripted_for_elo \
  --match-cache-dir results/matches \
  2>&1 | tee -a "$ELO_LOG"

# --- Plateau check: new_model.elo vs 3rd-place from BEFORE it was added ---
PLATEAU_NOTE=$(python3 - "$FINISHED" "$LADDER" "$PRE_THIRD" << 'PYEOF'
import json, sys

finished = sys.argv[1]
ladder_path = sys.argv[2]
pre_third_str = sys.argv[3]  # "name:elo" or "NONE"

with open(ladder_path) as f:
    d = json.load(f)
ratings = d["ratings"]

elo_finished = ratings.get(finished, {}).get("elo")
if elo_finished is None:
    print(f"PLATEAU_NODATA ({finished} not in post-tournament ladder)")
    sys.exit(0)

if pre_third_str == "NONE":
    print("PLATEAU_NODATA (fewer than 3 models in pre-tournament ladder)")
    sys.exit(0)

third_name, third_elo = pre_third_str.split(":")
third_elo = float(third_elo)

# Also check new model is actually at the top (if it regressed, no plateau signal)
ppo_only = {n: v["elo"] for n, v in ratings.items() if n != "heuristic"}
ranked = sorted(ppo_only.items(), key=lambda x: -x[1])
if ranked[0][0] != finished:
    print(f"PLATEAU_SKIP: {finished}({elo_finished:.0f}) is not top model after tournament (top={ranked[0][0]})")
    sys.exit(0)

delta = elo_finished - third_elo
if delta < 15:
    print(f"PLATEAU_YES: {finished}({elo_finished:.0f}) - pre-3rd {third_name}({third_elo:.0f}) = {delta:+.0f} < 15")
else:
    print(f"PLATEAU_NO: {finished}({elo_finished:.0f}) - pre-3rd {third_name}({third_elo:.0f}) = {delta:+.0f} >= 15")
PYEOF
)

ELO_FINISHED=$(python3 -c "
import json
with open('$LADDER') as f: d=json.load(f)
print(d['ratings'].get('$FINISHED', {}).get('elo', 'N/A'))
")

# --- Track consecutive plateau count in a persistent file ---
PLATEAU_FILE="results/plateau_count.txt"
PLATEAU_COUNT=0
if [ -f "$PLATEAU_FILE" ]; then
  PLATEAU_COUNT=$(cat "$PLATEAU_FILE")
fi

if echo "$PLATEAU_NOTE" | grep -q "PLATEAU_YES"; then
  PLATEAU_COUNT=$((PLATEAU_COUNT + 1))
elif echo "$PLATEAU_NOTE" | grep -q "PLATEAU_NO"; then
  PLATEAU_COUNT=0  # reset on any non-plateau run
fi
echo "$PLATEAU_COUNT" > "$PLATEAU_FILE"

echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] ELO result: $FINISHED=$ELO_FINISHED  $PLATEAU_NOTE  consecutive_plateaus=$PLATEAU_COUNT" \
  >> results/autonomous_decisions.log

if [ "$PLATEAU_COUNT" -ge 3 ]; then
  echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] *** 3 CONSECUTIVE PLATEAUS — next run should try simple arch experiment (wider trunk, more strategies, etc.) ***" \
    >> results/autonomous_decisions.log
fi

# --- UPGO: always enabled (analysis 2026-04-11: reduces variance on US-side sparse reward) ---
UPGO_FLAG="--upgo"
echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] UPGO always enabled for $NEXT" \
  >> results/autonomous_decisions.log

# --- League pool safety: NEXT_DIR is fresh, so no stale iter files to worry about.
# But guard against accidental re-use: if NEXT_DIR already has iter_*.pt from a
# different checkpoint lineage (e.g. after a crash mid-run), remove them so the
# new run's league pool starts clean.
if [ -d "$NEXT_DIR" ]; then
  STALE_COUNT=$(ls "${NEXT_DIR}"/iter_*.pt 2>/dev/null | wc -l)
  if [ "$STALE_COUNT" -gt 0 ]; then
    echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] WARNING: $NEXT_DIR has $STALE_COUNT stale iter_*.pt files — removing to prevent league pool mismatch" \
      >> results/autonomous_decisions.log
    rm -f "${NEXT_DIR}"/iter_*.pt "${NEXT_DIR}"/iter_*_scripted.pt
  fi
fi

# --- Persist WR table across runs for UCB-PFSP warm-start ---
# IMPORTANT: Always carry over the WR table when starting any PPO run — including
# manual launches that bypass this script. Without a seeded WR table, all fixtures
# start at n=0 → pfsp=1.0 (max), but are individually diluted by the 50%-mass cap
# across all fixtures, so they effectively get almost no selection weight in early
# iters. The model then trains only against itself, defeating the league purpose.
#
# For manual launches, run this before starting the PPO process:
#   python3 scripts/seed_wr_table.py <source_wr_table.json> <new_out_dir>/wr_table.json
# Or copy ppo_loop_step.sh's WR-table block manually.
#
# Copy fixture WR data with 0.7× decay (discounted UCB for non-stationary bandits).
# Model changes each run, so old WR estimates go stale. Decay shrinks n_i, which
# increases UCB exploration bonus → stale matchups get re-tested. 0.7× is moderate:
#   After 1 run: 200→140, after 3: 200→69 (significant re-explore).
# Strip self-play iter_* entries (keys don't match across runs).
mkdir -p "$NEXT_DIR"
if [ -f "${FINISHED_DIR}/wr_table.json" ]; then
  python3 -c "
import json, math
with open('${FINISHED_DIR}/wr_table.json') as f:
    data = json.load(f)
DECAY = 0.7
out = {}
for key, val in data.items():
    if key.startswith('iter_') or key == '__self__':
        continue
    out[key] = {
        'wins_ussr': int(round(val.get('wins_ussr', 0) * DECAY)),
        'total_ussr': int(round(val.get('total_ussr', 0) * DECAY)),
        'wins_us': int(round(val.get('wins_us', 0) * DECAY)),
        'total_us': int(round(val.get('total_us', 0) * DECAY)),
    }
with open('${NEXT_DIR}/wr_table.json', 'w') as f:
    json.dump(out, f, indent=2, sort_keys=True)
print(f'Carried over {len(out)} fixture WR entries (0.7x decay for discounted UCB)')
"
  echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Copied WR table from $FINISHED to $NEXT (0.7x decay, fixtures only)" \
    >> results/autonomous_decisions.log
fi

# --- Launch next PPO run ---
echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] LAUNCH: $NEXT from ${FINISHED} $(basename $FINISHED_CHECKPOINT)" \
  >> results/autonomous_decisions.log
echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Config: k=6, pfsp_exp=2.0, fixtures=$FIXTURE_COUNT, fadeout=999, tau=50, ent=0.01->0.003" \
  >> results/autonomous_decisions.log

nohup nice -n 10 uv run python scripts/train_ppo.py \
  --checkpoint "${FINISHED_CHECKPOINT}" \
  --out-dir "$NEXT_DIR" \
  --n-iterations 80 --games-per-iter 200 \
  --lr 2e-5 --clip-eps 0.12 \
  --ent-coef 0.01 --ent-coef-final 0.003 \
  --global-ent-decay-start 1 --global-ent-decay-end 80 \
  --max-kl 0.3 \
  --reset-optimizer \
  --league "$NEXT_DIR" \
  --league-save-every 10 \
  --league-mix-k 6 \
  --league-fixtures \
    $LEAGUE_FIXTURES \
  --league-recency-tau 50 \
  --league-fixture-fadeout 999 \
  --league-heuristic-pct 0.0 \
  --pfsp-exponent 2.0 \
  $UPGO_FLAG \
  --eval-every 10 \
  --eval-panel \
    "$PANEL_WEAKEST" \
    "$PANEL_MID" \
    "$PANEL_FRONTIER" \
    "__heuristic__" \
  --rollout-workers 1 \
  --device cuda --wandb --wandb-run-name "ppo_${NEXT}" \
  >> "$NEXT_LOG" 2>&1 &

NEXT_PID=$!
echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] $NEXT launched PID=$NEXT_PID" \
  >> results/autonomous_decisions.log

# --- Chain the watcher for the next run ---
nohup bash -c "
  cd /home/dkord/code/twilight-struggle-ai
  echo \"[\$(date -u +%Y-%m-%dT%H:%M:%SZ)] watcher: polling $NEXT (PID $NEXT_PID)\" >> results/autonomous_decisions.log
  while kill -0 $NEXT_PID 2>/dev/null; do sleep 15; done
  if [ -f data/checkpoints/ppo_${NEXT}_league/ppo_final.pt ]; then
    NEXT_NUM=\$(echo '$NEXT' | sed 's/v//')
    AFTER_NUM=\$((NEXT_NUM + 1))
    echo \"[\$(date -u +%Y-%m-%dT%H:%M:%SZ)] watcher: $NEXT done, running loop step\" >> results/autonomous_decisions.log
    bash scripts/ppo_loop_step.sh $NEXT v\${AFTER_NUM} >> results/logs/ppo/ppo_loop_watcher.log 2>&1
  else
    echo \"[\$(date -u +%Y-%m-%dT%H:%M:%SZ)] watcher: $NEXT ended without ppo_final.pt — no auto-launch\" >> results/autonomous_decisions.log
  fi
" > /dev/null 2>&1 &

echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] watcher for $NEXT launched (PID $!)" \
  >> results/autonomous_decisions.log

echo "Done. $NEXT running (PID=$NEXT_PID), ELO=$ELO_FINISHED for $FINISHED. $PLATEAU_NOTE"
