#!/usr/bin/env bash
# ppo_restart.sh — safely restart a crashed/killed PPO run.
# Usage: bash scripts/ppo_restart.sh <version>
# Example: bash scripts/ppo_restart.sh v27
#
# Reads latest_checkpoint.txt (written atomically after each successful checkpoint save)
# to find the correct resume point without guessing iteration numbers.
set -euo pipefail
cd /home/dkord/code/twilight-struggle-ai

VERSION=$1
DIR="data/checkpoints/ppo_${VERSION}_league"
POINTER="$DIR/latest_checkpoint.txt"
LOG="results/logs/ppo/ppo_${VERSION}.log"

if [ ! -f "$POINTER" ]; then
  echo "ERROR: $POINTER not found. Cannot determine latest checkpoint." >&2
  echo "Available checkpoints:" >&2
  ls "$DIR"/ppo_iter*.pt 2>/dev/null | sort -V | tail -5 >&2
  exit 1
fi

LATEST=$(cat "$POINTER" | tr -d '[:space:]')
if [ ! -f "$LATEST" ]; then
  echo "ERROR: pointer points to $LATEST which does not exist." >&2
  exit 1
fi

# Extract iteration number from filename (ppo_iter0173.pt → 173)
ITER=$(basename "$LATEST" | sed 's/ppo_iter0*\([0-9]*\)\.pt/\1/')
START_ITER=$((ITER + 1))

echo "Resuming $VERSION from $LATEST (iter $ITER → restart at $START_ITER)"
echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] ppo_restart: $VERSION from $LATEST start_iter=$START_ITER" \
  >> results/autonomous_decisions.log

# Read original launch args from saved ppo_args.json (written at start of each run)
ARGS_FILE="$DIR/ppo_args.json"
if [ ! -f "$ARGS_FILE" ]; then
  echo "ERROR: $ARGS_FILE not found — cannot reconstruct args." >&2
  exit 1
fi

# Extract key args from saved JSON
LR=$(python3 -c "import json; d=json.load(open('$ARGS_FILE')); print(d['lr'])")
CLIP_EPS=$(python3 -c "import json; d=json.load(open('$ARGS_FILE')); print(d['clip_eps'])")
ENT_COEF=$(python3 -c "import json; d=json.load(open('$ARGS_FILE')); print(d['ent_coef'])")
ENT_COEF_FINAL=$(python3 -c "import json; d=json.load(open('$ARGS_FILE')); print(d.get('ent_coef_final', d['ent_coef']))")
MAX_KL=$(python3 -c "import json; d=json.load(open('$ARGS_FILE')); print(d['max_kl'])")
N_ITER=$(python3 -c "import json; d=json.load(open('$ARGS_FILE')); print(d['n_iterations'])")
MIX_K=$(python3 -c "import json; d=json.load(open('$ARGS_FILE')); print(d['league_mix_k'])")
RECENCY_TAU=$(python3 -c "import json; d=json.load(open('$ARGS_FILE')); print(d['league_recency_tau'])")
FIXTURE_FADEOUT=$(python3 -c "import json; d=json.load(open('$ARGS_FILE')); print(d['league_fixture_fadeout'])")
PFSP_EXP=$(python3 -c "import json; d=json.load(open('$ARGS_FILE')); print(d['pfsp_exponent'])")
DIR_ALPHA=$(python3 -c "import json; d=json.load(open('$ARGS_FILE')); print(d['dir_alpha'])")
DIR_EPS=$(python3 -c "import json; d=json.load(open('$ARGS_FILE')); print(d['dir_epsilon'])")
EVAL_EVERY=$(python3 -c "import json; d=json.load(open('$ARGS_FILE')); print(d['eval_every'])")
ROLLOUT_TEMP=$(python3 -c "import json; d=json.load(open('$ARGS_FILE')); print(d['rollout_temp'])")
UPGO=$(python3 -c "import json; d=json.load(open('$ARGS_FILE')); print('--upgo' if d.get('upgo') else '')")
EVAL_PANEL=$(python3 -c "
import json; d=json.load(open('$ARGS_FILE'))
panel = d.get('eval_panel', [])
if panel: print('--eval-panel ' + ' '.join(panel))
")
FIXTURES=$(python3 -c "
import json; d=json.load(open('$ARGS_FILE'))
f = d.get('league_fixtures', [])
if f: print('--league-fixtures ' + ' '.join(f))
")

nohup nice -n 10 uv run python scripts/train_ppo.py \
  --checkpoint "$LATEST" \
  --start-iteration "$START_ITER" \
  --out-dir "$DIR" \
  --n-iterations "$N_ITER" --games-per-iter 200 \
  --lr "$LR" --clip-eps "$CLIP_EPS" \
  --ent-coef "$ENT_COEF" --ent-coef-final "$ENT_COEF_FINAL" \
  --max-kl "$MAX_KL" \
  --league "$DIR" \
  --league-save-every 10 \
  --league-mix-k "$MIX_K" \
  $FIXTURES \
  --league-recency-tau "$RECENCY_TAU" \
  --league-fixture-fadeout "$FIXTURE_FADEOUT" \
  --league-heuristic-pct 0.0 \
  --pfsp-exponent "$PFSP_EXP" \
  --dir-alpha "$DIR_ALPHA" \
  --dir-epsilon "$DIR_EPS" \
  $UPGO \
  --eval-every "$EVAL_EVERY" \
  $EVAL_PANEL \
  --rollout-workers 1 \
  --rollout-temp "$ROLLOUT_TEMP" \
  --device cuda --wandb --wandb-run-name "ppo_${VERSION}" \
  >> "$LOG" 2>&1 &

PID=$!
echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] ppo_restart: $VERSION PID=$PID start_iter=$START_ITER from $LATEST" \
  >> results/autonomous_decisions.log
echo "Launched PID=$PID"
