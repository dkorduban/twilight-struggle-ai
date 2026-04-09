#!/usr/bin/env bash
# ppo_loop_step.sh — called after each PPO run finishes.
# Usage: bash scripts/ppo_loop_step.sh <finished_version> <next_version>
# Example: bash scripts/ppo_loop_step.sh v14 v15
#
# Plateau rule: arch sweep if v(N).elo - v(N-3).elo < 15
# (3-run cumulative window, not per-run delta)
set -euo pipefail
cd /home/dkord/code/twilight-struggle-ai

FINISHED=$1   # e.g. v14
NEXT=$2       # e.g. v15

FINISHED_DIR="data/checkpoints/ppo_${FINISHED}_league"
NEXT_DIR="data/checkpoints/ppo_${NEXT}_league"
LADDER="results/elo_full_ladder.json"
ELO_LOG="results/elo_${FINISHED}_update.log"
NEXT_LOG="results/ppo_${NEXT}.log"

# Fixtures updated 2026-04-09: v8/v14/v19 span the current Elo range better than v4/v8/v12.
# Original v4/v8/v12 were 50-90 Elo below frontier by v22 era. Update when frontier moves 50+ above v19.
FINISHED_SCRIPTED="data/checkpoints/scripted_for_elo/${FINISHED}_scripted.pt"
WEAKEST_FIXTURE="data/checkpoints/scripted_for_elo/v8_scripted.pt"
MID_FIXTURE="data/checkpoints/scripted_for_elo/v14_scripted.pt"
FRONTIER_FIXTURE="data/checkpoints/scripted_for_elo/v19_scripted.pt"

# --- Copy finished model's scripted file to scripted_for_elo/ ---
if [ -f "${FINISHED_DIR}/ppo_final_scripted.pt" ] && [ ! -f "${FINISHED_SCRIPTED}" ]; then
  cp "${FINISHED_DIR}/ppo_final_scripted.pt" "${FINISHED_SCRIPTED}"
  echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Copied ${FINISHED_DIR}/ppo_final_scripted.pt -> ${FINISHED_SCRIPTED}" \
    >> results/autonomous_decisions.log
fi

# --- Build model list dynamically from scripted_for_elo dir ---
MODELS="heuristic"
# Include all existing scripted models (excluding the FINISHED one, handled separately)
for scripted_path in data/checkpoints/scripted_for_elo/*_scripted.pt; do
  [ -f "$scripted_path" ] || continue
  fname=$(basename "$scripted_path")
  name="${fname%_scripted.pt}"
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
  --games 400 --anchor v12 --anchor-elo 2001 \
  --schedule round_robin \
  --resume-from "$LADDER" \
  --out "$LADDER" \
  --script-dir data/checkpoints/scripted_for_elo \
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

# --- Launch next PPO run ---
echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] LAUNCH: $NEXT from ${FINISHED} ppo_final.pt" \
  >> results/autonomous_decisions.log

mkdir -p "$NEXT_DIR"
nohup nice -n 10 uv run python scripts/train_ppo.py \
  --checkpoint "${FINISHED_DIR}/ppo_final.pt" \
  --out-dir "$NEXT_DIR" \
  --n-iterations 200 --games-per-iter 200 \
  --lr 2e-5 --clip-eps 0.12 \
  --ent-coef 0.03 --ent-coef-final 0.005 \
  --max-kl 0.3 \
  --league "$NEXT_DIR" \
  --league-save-every 10 \
  --league-mix-k 4 \
  --league-fixtures \
    "$WEAKEST_FIXTURE" \
    "$MID_FIXTURE" \
    "$FRONTIER_FIXTURE" \
  --eval-every 20 \
  --eval-opponent "$FINISHED_SCRIPTED" \
  --rollout-workers 1 \
  --rollout-temp 1.2 \
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
    bash scripts/ppo_loop_step.sh $NEXT v\${AFTER_NUM} >> results/ppo_loop_watcher.log 2>&1
  else
    echo \"[\$(date -u +%Y-%m-%dT%H:%M:%SZ)] watcher: $NEXT ended without ppo_final.pt — no auto-launch\" >> results/autonomous_decisions.log
  fi
" > /dev/null 2>&1 &

echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] watcher for $NEXT launched (PID $!)" \
  >> results/autonomous_decisions.log

echo "Done. $NEXT running (PID=$NEXT_PID), ELO=$ELO_FINISHED for $FINISHED. $PLATEAU_NOTE"
