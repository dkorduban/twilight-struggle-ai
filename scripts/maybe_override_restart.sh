#!/usr/bin/env bash
# maybe_override_restart.sh: After a run finishes, check its Elo.
# If below the restart_elo_threshold, set checkpoint_override_<next_next>.txt
# to restart from the anchor checkpoint.
# Usage: bash scripts/maybe_override_restart.sh <finished_version> <next_version> <anchor_checkpoint> <restart_elo_threshold>
# Example: bash scripts/maybe_override_restart.sh v222_sc v223_sc data/checkpoints/ppo_v217_sc_league/ppo_best.pt 1800

set -euo pipefail
cd /home/dkord/code/twilight-struggle-ai

FINISHED=$1
NEXT=$2
ANCHOR=$3
THRESHOLD=${4:-1800}
LADDER="results/elo/elo_full_ladder.json"

# Compute version after NEXT (for the override)
VSTR="$NEXT"
VBODY="${VSTR#v}"
VNUM="${VBODY%%[^0-9]*}"
VSUFFIX="${VBODY#$VNUM}"
AFTER_NUM=$((VNUM + 1))
AFTER="v${AFTER_NUM}${VSUFFIX}"

# Check finished Elo
FINISHED_ELO=$(python3 -c "
import json
with open('$LADDER') as f: d=json.load(f)
r = d.get('ratings', {})
for name in ['$FINISHED', '${FINISHED}_scripted']:
    v = r.get(name, {}).get('elo')
    if v: print(v); exit()
print('N/A')
" 2>/dev/null)

echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] maybe_override: $FINISHED Elo=$FINISHED_ELO, threshold=$THRESHOLD, anchor=$ANCHOR" \
  >> results/autonomous_decisions.log

if [ "$FINISHED_ELO" = "N/A" ]; then
  echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] maybe_override: $FINISHED has no Elo yet — skipping override decision" \
    >> results/autonomous_decisions.log
  exit 0
fi

# Compare (bash doesn't handle floats; use python)
SHOULD_RESTART=$(python3 -c "print('yes' if float('$FINISHED_ELO') < $THRESHOLD else 'no')" 2>/dev/null)

if [ "$SHOULD_RESTART" = "yes" ]; then
  echo "$ANCHOR" > "results/checkpoint_override_${AFTER}.txt"
  echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] maybe_override: $FINISHED Elo=$FINISHED_ELO < $THRESHOLD — set override for $AFTER to $ANCHOR" \
    >> results/autonomous_decisions.log
  # Pre-seed WR table if anchor's wr_table.json exists
  ANCHOR_DIR=$(dirname "$ANCHOR")
  if [ -f "${ANCHOR_DIR}/wr_table.json" ]; then
    mkdir -p "data/checkpoints/ppo_${AFTER}_league"
    python3 -c "
import json
with open('${ANCHOR_DIR}/wr_table.json') as f:
    data = json.load(f)
DECAY = 0.7
out = {}
for key, val in data.items():
    if key.startswith('iter_') or key == '__self__':
        continue
    out[key] = {k: int(round(v * DECAY)) for k, v in val.items()}
with open('data/checkpoints/ppo_${AFTER}_league/wr_table.json', 'w') as f:
    json.dump(out, f, indent=2, sort_keys=True)
print(f'Pre-seeded {len(out)} WR entries (0.7x decay) for ${AFTER}')
"
    echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] maybe_override: pre-seeded WR table for $AFTER from anchor" \
      >> results/autonomous_decisions.log
  fi
else
  echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] maybe_override: $FINISHED Elo=$FINISHED_ELO >= $THRESHOLD — no restart needed for $AFTER" \
    >> results/autonomous_decisions.log
fi
