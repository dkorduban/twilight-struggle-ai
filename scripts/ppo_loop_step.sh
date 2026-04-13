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

# Corrupted-era models: trained with T=1.2 + log_prob bugs (v27-v41). Excluded permanently.
EXCLUDED_VERSIONS="27 28 29 30 31 32 33 34 35 36 37 38 39 40 41"
MIN_SCRIPTED_VERSION=8

FINISHED_DIR="data/checkpoints/ppo_${FINISHED}_league"
NEXT_DIR="data/checkpoints/ppo_${NEXT}_league"
LADDER="results/elo/elo_full_ladder.json"
ELO_LOG="results/logs/elo/elo_${FINISHED}_update.log"
NEXT_LOG="results/logs/ppo/ppo_${NEXT}.log"

# Fixtures: read from JSD-deduplicated fixture list (results/selected_fixtures.json).
# To regenerate: uv run python scripts/select_league_fixtures.py
# The JSON fixture_paths field lists scripted .pt paths + __heuristic__.
FINISHED_SCRIPTED="data/checkpoints/scripted_for_elo/${FINISHED}_scripted.pt"
# Panel eval and candidate tournament: same 5-opponent pool.
# Upgraded 2026-04-13: old-engine panel (v55/v54/v44/v45/v14) saturated at 0.878 WR
# (those models play suboptimally in the new engine). New panel = sc-lineage models
# spanning ELO 2017-2097. Expected WR at current model (~1800 ELO): ~18-25% avg.
# As model reaches 2000+ ELO, avg WR will reach 50% — good discrimination range.
# v67_sc=2017 | v136_sc=2022 | v77_sc=2092 | v78_sc=2097 | v132_sc=2092
PANEL_V55="data/checkpoints/scripted_for_elo/v67_sc_scripted.pt"
PANEL_V54="data/checkpoints/scripted_for_elo/v136_sc_scripted.pt"
PANEL_V44="data/checkpoints/scripted_for_elo/v77_sc_scripted.pt"
PANEL_V45="data/checkpoints/scripted_for_elo/v78_sc_scripted.pt"
PANEL_V14="data/checkpoints/scripted_for_elo/v132_sc_scripted.pt"

FIXTURES_JSON="results/selected_fixtures.json"

# --- Singleton guard: abort if another train_ppo.py is already running ---
# The lockfile (results/train_ppo.lock) is held exclusively by train_ppo.py
# for its entire lifetime. flock -n returns non-zero if the lock is taken.
if flock -n results/train_ppo.lock true 2>/dev/null; then
  : # lock was free, good to proceed (flock released immediately — we just tested)
else
  EXISTING_PIDS=$(pgrep -f "train_ppo.py" 2>/dev/null | tr '\n' ' ' || true)
  echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] ABORT: train_ppo.py already running (PIDs: $EXISTING_PIDS) — refusing to launch $NEXT" \
    >> results/autonomous_decisions.log
  echo "ERROR: train_ppo.py already running (PIDs: $EXISTING_PIDS). Kill it first." >&2
  exit 1
fi

# Load per-side fixture paths from JSON; skip the model about to be trained.
# ussr_fixture_paths: ranked by elo_ussr (best USSR opponents).
# us_fixture_paths:   ranked by elo_us  (best US opponents).
# LEAGUE_FIXTURES = union of both sets (train_ppo.py handles per-side PFSP internally).
# NOTE: Do NOT use `read a b c <<< $(...)` — bash word-splits the output, so only the
# first path goes to $a and the second path to $b. Each pool is read separately instead.
_FIXTURES_PYTHON=$(python3 -c "
import json
d = json.load(open('$FIXTURES_JSON'))
skip_pat = '/${NEXT}_scripted.pt'
ussr = [p for p in d['ussr_fixture_paths'] if skip_pat not in p]
us   = [p for p in d['us_fixture_paths']   if skip_pat not in p]
seen = set(); union = []
for p in ussr + us:
    if p not in seen:
        seen.add(p); union.append(p)
print('USSR=' + ' '.join(ussr))
print('US='   + ' '.join(us))
print('UNION='+ ' '.join(union))
" 2>/dev/null)
USSR_FIXTURES=$(echo "$_FIXTURES_PYTHON"  | grep '^USSR='  | cut -d= -f2-)
US_FIXTURES=$(echo "$_FIXTURES_PYTHON"    | grep '^US='    | cut -d= -f2-)
LEAGUE_FIXTURES=$(echo "$_FIXTURES_PYTHON"| grep '^UNION=' | cut -d= -f2-)

if [ -z "$LEAGUE_FIXTURES" ]; then
  echo "ERROR: Could not load fixtures from $FIXTURES_JSON" >&2
  exit 1
fi
FIXTURE_COUNT=$(echo $LEAGUE_FIXTURES | wc -w)
USSR_COUNT=$(echo $USSR_FIXTURES | wc -w)
US_COUNT=$(echo $US_FIXTURES | wc -w)
echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] League fixtures: $FIXTURE_COUNT unique (ussr=$USSR_COUNT us=$US_COUNT) from $FIXTURES_JSON" \
  >> results/autonomous_decisions.log

# --- Candidate tournament: pick ppo_best.pt from panel eval history ---
# Runs non-blocking in background so the next training run starts immediately.
# ppo_confirm_best.py selects the top-N panel-eval checkpoints by Elo-weighted
# panel WR, runs a round-robin among them; winner is written to ppo_best.pt.
# Note: Option F (train_ppo.py) already saves ppo_running_best.pt on each panel
# high-water mark, so ppo_best.pt should reflect the running best even before
# this candidate tournament completes.
CONFIRM_LOG="results/logs/elo/confirm_${FINISHED}.log"
if [ -f "${FINISHED_DIR}/panel_eval_history.json" ]; then
  echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Launching candidate tournament for $FINISHED (non-blocking) ..." \
    >> results/autonomous_decisions.log
  nohup nice -n 10 uv run python scripts/ppo_confirm_best.py \
    --run-dir "$FINISHED_DIR" \
    --fixtures \
      "v55:${PANEL_V55}" \
      "v54:${PANEL_V54}" \
      "v44:${PANEL_V44}" \
      "v45:${PANEL_V45}" \
      "v14:${PANEL_V14}" \
    --n-top 8 \
    --n-games 150 \
    --anchor v14 --anchor-elo 2015 \
    --script-dir data/checkpoints/scripted_for_elo \
    >> "$CONFIRM_LOG" 2>&1 &
  echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Candidate tournament launched in background (PID $!) for $FINISHED" \
    >> results/autonomous_decisions.log
else
  echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] No panel_eval_history.json for $FINISHED — skipping candidate tournament" \
    >> results/autonomous_decisions.log
fi

# ppo_best.pt set by Option F (train_ppo.py running_best) or candidate tournament above;
# fall back to ppo_final.pt if missing.
FINISHED_CHECKPOINT="${FINISHED_DIR}/ppo_final.pt"
if [ -f "${FINISHED_DIR}/ppo_best.pt" ]; then
  FINISHED_CHECKPOINT="${FINISHED_DIR}/ppo_best.pt"
  echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Using ppo_best.pt for $FINISHED (Option F / candidate tournament)" \
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
  # Extract numeric prefix from version (v12 -> 12, v65_sc -> 65)
  ver="${name#v}"
  ver_num="${ver%%[^0-9]*}"
  if [ -z "$ver_num" ]; then continue; fi
  if [ "$ver_num" -lt "$MIN_SCRIPTED_VERSION" ]; then continue; fi
  # Skip corrupted-era models (only exact numeric matches)
  if echo "$EXCLUDED_VERSIONS" | grep -qw "$ver_num"; then continue; fi
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

echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] ppo_loop_step: $FINISHED finished, launching $NEXT then running ELO update in background" \
  >> results/autonomous_decisions.log

# --- Capture 3rd-place Elo BEFORE adding the new candidate (fast, just reads JSON) ---
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

# --- UPGO: always enabled (analysis 2026-04-11: reduces variance on US-side sparse reward) ---
UPGO_FLAG="--upgo"
echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] UPGO always enabled for $NEXT" \
  >> results/autonomous_decisions.log

# --- League pool safety: guard against stale iter_*.pt from a crashed/restarted lineage ---
if [ -d "$NEXT_DIR" ]; then
  STALE_COUNT=$(find "${NEXT_DIR}" -maxdepth 1 -name "iter_*.pt" 2>/dev/null | wc -l)
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
DECAY = 0.5
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
print(f'Carried over {len(out)} fixture WR entries (0.5x decay for discounted UCB)')
"
  echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Copied WR table from $FINISHED to $NEXT (0.5x decay, fixtures only)" \
    >> results/autonomous_decisions.log
fi

# --- Read total_iters from parent checkpoint for per-run entropy decay ---
# Ensures each chained run gets fresh entropy annealing (global iter offset > 80 otherwise)
PREV_TOTAL_ITERS=$(python3 -c "
import torch, sys
try:
    ckpt = torch.load('${FINISHED_CHECKPOINT}', map_location='cpu', weights_only=False)
    print(int(ckpt.get('args', {}).get('total_iters', 0)))
except Exception as e:
    print(0)
" 2>/dev/null)
PREV_TOTAL_ITERS="${PREV_TOTAL_ITERS:-0}"

# --- Launch next PPO run ---
echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] LAUNCH: $NEXT from ${FINISHED} $(basename $FINISHED_CHECKPOINT)" \
  >> results/autonomous_decisions.log
echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Config: k=6, pfsp_exp=1.5, fixtures=$FIXTURE_COUNT, fadeout=999, tau=50, ent=0.01->0.003 heuristic=0.15 n_iters=30 global_decay=[${PREV_TOTAL_ITERS},$((PREV_TOTAL_ITERS+30))]" \
  >> results/autonomous_decisions.log

mkdir -p "$NEXT_DIR" results/logs/ppo

cat > "$NEXT_DIR/snakemake_train_config.yaml" <<YAML
out_dir: "$NEXT_DIR"
checkpoint: "$FINISHED_CHECKPOINT"
next_version: "$NEXT"
prev_total_iters: $PREV_TOTAL_ITERS
elo_log: "$NEXT_LOG"
probe_set: "data/probe_positions.parquet"
upgo_flag: "$UPGO_FLAG"
ussr_fixtures: "$USSR_FIXTURES __heuristic__"
us_fixtures: "$US_FIXTURES __heuristic__"
league_fixtures: "$LEAGUE_FIXTURES __heuristic__"
panel_v55: "$PANEL_V55"
panel_v54: "$PANEL_V54"
panel_v44: "$PANEL_V44"
panel_v45: "$PANEL_V45"
panel_v14: "$PANEL_V14"
YAML

nohup nice -n 10 uv run snakemake \
  --snakefile /home/dkord/code/twilight-struggle-ai/Snakefile.ppo \
  --config train_config="$NEXT_DIR/snakemake_train_config.yaml" \
  --resources gpu=1 \
  --cores all \
  -j 1 \
  ppo_train_dynamic \
  >> "$ELO_LOG" 2>&1 &

NEXT_PID=$!
echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] $NEXT launched PID=$NEXT_PID" \
  >> results/autonomous_decisions.log

# --- Chain the watcher for the next run ---
# Version name increment: supports both plain vN (v65->v66) and suffixed vN_foo (v65_sc->v66_sc).
# Extract numeric prefix and optional suffix, then increment the number.
nohup bash -c "
  cd /home/dkord/code/twilight-struggle-ai
  echo \"[\$(date -u +%Y-%m-%dT%H:%M:%SZ)] watcher: polling $NEXT (PID $NEXT_PID)\" >> results/autonomous_decisions.log
  while kill -0 $NEXT_PID 2>/dev/null; do sleep 15; done
  if [ -f data/checkpoints/ppo_${NEXT}_league/ppo_final.pt ] || [ -f data/checkpoints/ppo_${NEXT}_league/ppo_running_best.pt ]; then
    # Parse version: v65 -> num=65 suffix=''; v65_sc -> num=65 suffix='_sc'
    VSTR='$NEXT'
    VBODY=\"\${VSTR#v}\"
    VNUM=\"\${VBODY%%[^0-9]*}\"
    VSUFFIX=\"\${VBODY#\$VNUM}\"
    AFTER_NUM=\$((VNUM + 1))
    AFTER=\"v\${AFTER_NUM}\${VSUFFIX}\"
    echo \"[\$(date -u +%Y-%m-%dT%H:%M:%SZ)] watcher: $NEXT done, running loop step -> \$AFTER\" >> results/autonomous_decisions.log
    bash scripts/ppo_loop_step.sh $NEXT \$AFTER >> results/logs/ppo/ppo_loop_watcher.log 2>&1
  else
    echo \"[\$(date -u +%Y-%m-%dT%H:%M:%SZ)] watcher: $NEXT ended without ppo_final.pt — no auto-launch\" >> results/autonomous_decisions.log
  fi
" > /dev/null 2>&1 &

echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] watcher for $NEXT launched (PID $!)" \
  >> results/autonomous_decisions.log

# --- ELO plateau check + targeted extension for promising models ---
# Incremental placement (5-6 matches) is done in post_train_confirm.sh --incremental.
# Here we only run additional matchups if the new model looks promising (within 50 Elo of top).
# Full round-robin of all models is NEVER run automatically — too slow (1081 pairs × 400 = 432k games).
# To trigger a full rebuild manually: bash scripts/post_train_confirm.sh <run_dir> --full

nohup bash -c "
  cd /home/dkord/code/twilight-struggle-ai
  echo \"[\$(date -u +%Y-%m-%dT%H:%M:%SZ)] ELO plateau check (incremental already placed $FINISHED)\" >> results/autonomous_decisions.log

  # Read Elo from ladder — already placed by post_train_confirm.sh --incremental
  ELO_FINISHED=\$(python3 -c \"
import json
with open('$LADDER') as f: d=json.load(f)
r = d.get('ratings', {})
for name in ['$FINISHED', '${FINISHED}_scripted']:
    v = r.get(name, {}).get('elo')
    if v: print(v); exit()
print('N/A')
\")

  # Promising-model extension: if new model is within 50 Elo of current top,
  # play it vs up to 5 more top models to narrow the Elo CI.
  # This is fast: 5 new pairs × 200 games = 1000 games, ~5 minutes.
  EXTENDED=\$(python3 - '$FINISHED' '$LADDER' '$FINISHED_SCRIPTED' << 'PYEOF'
import json, subprocess, sys, os
finished = sys.argv[1]
ladder_path = sys.argv[2]
finished_pt = sys.argv[3]

with open(ladder_path) as f:
    d = json.load(f)
ratings = d.get('ratings', {})
elo_finished = ratings.get(finished, {}).get('elo')
if elo_finished is None:
    print('SKIP_NOELO')
    sys.exit(0)

# Find models already played vs finished (from incremental placement)
played = set()
for k, v in ratings.get(finished, {}).get('opponents', {}).items():
    played.add(k)
# Also check match cache directory
cache_dir = 'results/matches'
for fn in os.listdir(cache_dir) if os.path.isdir(cache_dir) else []:
    if finished in fn and fn.endswith('.json'):
        other = fn.replace(finished, '').strip('_').replace('__vs__', '').replace('.json', '')
        played.add(other)

ppo_only = {n: v for n, v in ratings.items() if n != 'heuristic'}
ranked = sorted(ppo_only.items(), key=lambda x: -x[1].get('elo', 0))
top_elo = ranked[0][1].get('elo', 0) if ranked else 0

if elo_finished < top_elo - 50:
    print(f'SKIP_NOT_PROMISING: {finished}({elo_finished:.0f}) is {elo_finished - top_elo:.0f} below top')
    sys.exit(0)

# Pick top-5 opponents not yet played
script_dir = 'data/checkpoints/scripted_for_elo'
extension_models = []
for name, rating in ranked:
    if name == finished:
        continue
    if name in played:
        continue
    pt = os.path.join(script_dir, f'{name}_scripted.pt')
    if not os.path.exists(pt):
        continue
    extension_models.append(f'{name}:{pt}')
    if len(extension_models) >= 5:
        break

if not extension_models:
    print('SKIP_NO_NEW_OPPONENTS')
    sys.exit(0)

finished_pt_arg = f'{finished}:{finished_pt}' if os.path.exists(finished_pt) else ''
if not finished_pt_arg:
    print(f'SKIP_NO_FINISHED_PT: {finished_pt} missing')
    sys.exit(0)

models_arg = ' '.join([finished_pt_arg] + extension_models)
print(f'EXTEND: {finished}({elo_finished:.0f}) is promising, playing vs {len(extension_models)} more: {\" \".join(n.split(\":\")[0] for n in extension_models)}')
cmd = (
    f'nice -n 19 uv run python scripts/run_elo_tournament.py'
    f' --models {models_arg}'
    f' --games 200 --anchor v14 --anchor-elo 2015'
    f' --schedule round_robin'
    f' --mode incremental --new-model {finished}'
    f' --resume-from {ladder_path}'
    f' --out results/logs/elo/elo_{finished}_extension.json'
    f' --script-dir {script_dir}'
    f' --match-cache-dir results/matches'
)
os.system(cmd)

# Merge extension results into ladder
try:
    ext_data = json.load(open(f'results/logs/elo/elo_{finished}_extension.json'))
    ladder_data = json.load(open(ladder_path))
    new_r = ext_data['ratings'].get(finished)
    if new_r:
        ladder_data['ratings'][finished] = new_r
        with open(ladder_path, 'w') as f:
            json.dump(ladder_data, f, indent=2)
        print(f'EXTENDED_OK: merged updated {finished} rating elo={new_r[\"elo\"]:.0f}')
    else:
        print(f'EXTENDED_NORATING: {finished} not found in extension output')
except Exception as e:
    print(f'EXTENDED_ERR: {e}')
PYEOF
)
  echo \"[\$(date -u +%Y-%m-%dT%H:%M:%SZ)] Extension check: \$EXTENDED\" >> results/autonomous_decisions.log

  # Re-read Elo after potential extension
  ELO_FINISHED=\$(python3 -c \"
import json
with open('$LADDER') as f: d=json.load(f)
r = d.get('ratings', {})
for name in ['$FINISHED', '${FINISHED}_scripted']:
    v = r.get(name, {}).get('elo')
    if v: print(v); exit()
print('N/A')
\")

  # Plateau check
  PLATEAU_NOTE=\$(python3 - '$FINISHED' '$LADDER' '$PRE_THIRD' << 'PYEOF'
import json, sys
finished = sys.argv[1]
ladder_path = sys.argv[2]
pre_third_str = sys.argv[3]
with open(ladder_path) as f:
    d = json.load(f)
ratings = d['ratings']
elo_finished = ratings.get(finished, {}).get('elo')
if elo_finished is None:
    print(f'PLATEAU_NODATA ({finished} not in ladder)')
    sys.exit(0)
if pre_third_str == 'NONE':
    print('PLATEAU_NODATA (fewer than 3 models)')
    sys.exit(0)
third_name, third_elo = pre_third_str.split(':')
third_elo = float(third_elo)
ppo_only = {n: v['elo'] for n, v in ratings.items() if n != 'heuristic'}
ranked = sorted(ppo_only.items(), key=lambda x: -x[1])
if ranked[0][0] != finished:
    print(f'PLATEAU_SKIP: {finished}({elo_finished:.0f}) not top (top={ranked[0][0]})')
    sys.exit(0)
delta = elo_finished - third_elo
if delta < 15:
    print(f'PLATEAU_YES: {finished}({elo_finished:.0f}) - pre-3rd {third_name}({third_elo:.0f}) = {delta:+.0f} < 15')
else:
    print(f'PLATEAU_NO: {finished}({elo_finished:.0f}) - pre-3rd {third_name}({third_elo:.0f}) = {delta:+.0f} >= 15')
PYEOF
)

  PLATEAU_FILE='results/plateau_count.txt'
  PLATEAU_COUNT=0
  [ -f \"\$PLATEAU_FILE\" ] && PLATEAU_COUNT=\$(cat \"\$PLATEAU_FILE\")
  echo \"\$PLATEAU_NOTE\" | grep -q 'PLATEAU_YES' && PLATEAU_COUNT=\$((PLATEAU_COUNT + 1)) || true
  echo \"\$PLATEAU_NOTE\" | grep -q 'PLATEAU_NO'  && PLATEAU_COUNT=0 || true
  echo \"\$PLATEAU_COUNT\" > \"\$PLATEAU_FILE\"

  echo \"[\$(date -u +%Y-%m-%dT%H:%M:%SZ)] ELO result: $FINISHED=\$ELO_FINISHED  \$PLATEAU_NOTE  consecutive_plateaus=\$PLATEAU_COUNT\" \
    >> results/autonomous_decisions.log
  if [ \"\$PLATEAU_COUNT\" -ge 3 ]; then
    echo \"[\$(date -u +%Y-%m-%dT%H:%M:%SZ)] *** 3 CONSECUTIVE PLATEAUS — consider arch experiment ***\" \
      >> results/autonomous_decisions.log
  fi
" >> "$ELO_LOG" 2>&1 &

echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] ELO update for $FINISHED launched in background (PID $!)" \
  >> results/autonomous_decisions.log

echo "Done. $NEXT launched (PID=$NEXT_PID). ELO update for $FINISHED running in background."
