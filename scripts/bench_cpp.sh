#!/bin/bash
# bench_cpp.sh — benchmark learned vs heuristic using the native C++ collector.
#
# Usage:
#   bash scripts/bench_cpp.sh \
#       --checkpoint data/checkpoints/retrain_vN/baseline_best.pt \
#       --n-games 500 \
#       --seed 9999 \
#       --out results/bench_vN.json

set -euo pipefail

cd /home/dkord/code/twilight-struggle-ai

CHECKPOINT=""
N_GAMES=500
SEED=9999
OUT="results/bench_cpp.json"
LEARNED_SIDE="ussr"  # US-side C++ collection has high variance at low win rates; use ussr for stable tracking
COLLECT_SCRIPT="scripts/collect_cpp.sh"
EXPORT_SCRIPT="cpp/tools/export_baseline_to_torchscript.py"

usage() {
    sed -n '2,12p' "$0"
}

while [[ $# -gt 0 ]]; do
    case $1 in
        --checkpoint)   CHECKPOINT=$2;   shift 2 ;;
        --n-games)      N_GAMES=$2;      shift 2 ;;
        --seed)         SEED=$2;         shift 2 ;;
        --out)          OUT=$2;          shift 2 ;;
        --learned-side) LEARNED_SIDE=$2; shift 2 ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            echo "Unknown arg: $1" >&2
            exit 1
            ;;
    esac
done

if [ -z "$CHECKPOINT" ]; then
    echo "ERROR: --checkpoint is required" >&2
    exit 1
fi

case "$LEARNED_SIDE" in
    both|ussr|us) ;;
    *)
        echo "ERROR: --learned-side must be one of: both, ussr, us" >&2
        exit 1
        ;;
esac

mkdir -p "$(dirname "$OUT")"
mkdir -p results

# ── Provenance tracking ─────────────────────────────────────────────────────
PROV_OUT="${OUT%.json}_provenance.json"
python3 -c "
from tsrl.provenance import capture_provenance, save_provenance
prov = capture_provenance(
    input_files=['$CHECKPOINT'],
    binaries=['build-ninja/cpp/tools/ts_collect_selfplay_rows_jsonl'],
    extra={'n_games': $N_GAMES, 'seed': $SEED, 'learned_side': '$LEARNED_SIDE'},
)
save_provenance(prov, '$PROV_OUT')
print(f'[provenance] git={prov[\"git_sha\"][:8]} dirty={prov[\"git_dirty\"]}')
" 2>/dev/null || echo "[provenance] Skipped (non-fatal)"

TS_PATH="${CHECKPOINT%.pt}_scripted.pt"
if [ ! -f "$TS_PATH" ] || [ "$CHECKPOINT" -nt "$TS_PATH" ]; then
    echo "[bench_cpp] Exporting TorchScript: $CHECKPOINT -> $TS_PATH"
    nice -n 10 uv run python "$EXPORT_SCRIPT" \
        --checkpoint "$CHECKPOINT" \
        --out "$TS_PATH"
else
    echo "[bench_cpp] TorchScript already up to date: $TS_PATH"
fi

GAMES_USSR=0
GAMES_US=0
case "$LEARNED_SIDE" in
    both)
        GAMES_USSR=$(( (N_GAMES + 1) / 2 ))
        GAMES_US=$(( N_GAMES / 2 ))
        ;;
    ussr)
        GAMES_USSR=$N_GAMES
        ;;
    us)
        GAMES_US=$N_GAMES
        ;;
esac

TMP_DIR=$(mktemp -d /tmp/bench_cpp.XXXXXX)
cleanup() {
    rm -rf "$TMP_DIR"
}
trap cleanup EXIT

USSR_OUT="$TMP_DIR/learned_ussr.parquet"
US_OUT="$TMP_DIR/learned_us.parquet"
START_TIME=$(date +%s)

if [ "$GAMES_USSR" -gt 0 ]; then
    bash "$COLLECT_SCRIPT" \
        --checkpoint "$CHECKPOINT" \
        --learned-side ussr \
        --games "$GAMES_USSR" \
        --seed "$SEED" \
        --out "$USSR_OUT" \
        --keep-chunks 0
fi

if [ "$GAMES_US" -gt 0 ]; then
    bash "$COLLECT_SCRIPT" \
        --checkpoint "$CHECKPOINT" \
        --learned-side us \
        --games "$GAMES_US" \
        --seed $(( SEED + GAMES_USSR )) \
        --out "$US_OUT" \
        --keep-chunks 0
fi

END_TIME=$(date +%s)

CHECKPOINT="$CHECKPOINT" \
N_GAMES="$N_GAMES" \
SEED="$SEED" \
OUT="$OUT" \
LEARNED_SIDE="$LEARNED_SIDE" \
USSR_OUT="$USSR_OUT" \
US_OUT="$US_OUT" \
ELAPSED_SECONDS=$(( END_TIME - START_TIME )) \
uv run python - <<'PY'
import json
import os
import re
from pathlib import Path

import pyarrow.parquet as pq


def summarize(path: str, learned_side: str) -> tuple[int, int, int]:
    """Count wins for the learned side using final_vp (unambiguous encoding).

    final_vp > 0 → USSR wins; final_vp < 0 → US wins; final_vp == 0 → draw.
    winner_side in the dataset is actor-relative (1=actor won, -1=actor lost),
    NOT side-absolute, so we use final_vp instead.
    """
    if not path or not Path(path).exists():
        return 0, 0, 0

    table = pq.read_table(path, columns=["game_id", "final_vp"])
    vp_by_game: dict = {}
    for game_id, vp in zip(table.column("game_id").to_pylist(), table.column("final_vp").to_pylist()):
        vp_by_game[game_id] = vp

    wins = 0
    decisive = 0
    draws = 0
    for vp in vp_by_game.values():
        if vp is None or vp == 0:
            draws += 1
            continue
        decisive += 1
        ussr_won = vp > 0
        if (learned_side == "ussr" and ussr_won) or (learned_side == "us" and not ussr_won):
            wins += 1
    return wins, decisive, draws


def infer_history_key(out_path: Path, checkpoint_path: Path) -> str:
    for candidate in (out_path.as_posix(), checkpoint_path.as_posix()):
        match = re.search(r"(v\d+)", candidate)
        if match:
            return match.group(1)
    return out_path.stem


checkpoint = Path(os.environ["CHECKPOINT"])
out_path = Path(os.environ["OUT"])
history_path = Path("results/benchmark_history.json")

ussr_wins, ussr_decisive, ussr_draws = summarize(os.environ["USSR_OUT"], learned_side="ussr")
us_wins, us_decisive, us_draws = summarize(os.environ["US_OUT"], learned_side="us")

learned_wins = ussr_wins + us_wins
decisive_games = ussr_decisive + us_decisive
draws = ussr_draws + us_draws
win_pct = 0.0 if decisive_games == 0 else 100.0 * learned_wins / decisive_games
heuristic_wins = decisive_games - learned_wins

summary_line = (
    f"{'learned vs heuristic':35s} "
    f"  {'learned':12s} {learned_wins:3d}/{decisive_games:3d} ({win_pct:5.1f}%)  "
    f"{'heuristic':12s} {heuristic_wins:3d}/{decisive_games:3d} ({100.0 - win_pct if decisive_games else 0.0:5.1f}%)  "
    f"Draw {draws:2d}/{int(os.environ['N_GAMES']):d}"
)

payload = {
    "checkpoint": str(checkpoint),
    "decisive_games": decisive_games,
    "draws": draws,
    "elapsed_seconds": int(os.environ["ELAPSED_SECONDS"]),
    "heuristic_wins": heuristic_wins,
    "learned_side": os.environ["LEARNED_SIDE"],
    "learned_wins": learned_wins,
    "learned_win_pct": round(win_pct, 1),
    "n_games": int(os.environ["N_GAMES"]),
    "seed": int(os.environ["SEED"]),
    "sides": {
        "us": {
            "decisive_games": us_decisive,
            "draws": us_draws,
            "games": us_decisive + us_draws,
            "learned_wins": us_wins,
        },
        "ussr": {
            "decisive_games": ussr_decisive,
            "draws": ussr_draws,
            "games": ussr_decisive + ussr_draws,
            "learned_wins": ussr_wins,
        },
    },
    "summary_line": summary_line,
}

out_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")

history = {}
if history_path.exists():
    history = json.loads(history_path.read_text())
history[infer_history_key(out_path, checkpoint)] = {"learned_vs_heuristic": round(win_pct, 1)}
history_path.write_text(json.dumps(history, indent=2, sort_keys=True) + "\n")

print(summary_line)
print(f"[bench_cpp] Wrote {out_path}")
print(f"[bench_cpp] Updated {history_path}")
PY
