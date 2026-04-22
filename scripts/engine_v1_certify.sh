#!/usr/bin/env bash
#
# Engine v1.0 certification + golden regression gate.
#
# Asserts:
#   1. C++ ctest suite passes clean.
#   2. Python pytest suite passes clean (use -n 0 per pytest-Python3.14 workaround).
#   3. Replay validator violation count is at or below the documented ceiling.
#
# Violation ceiling is set at 74 as of 2026-04-21 post-#125 Shuttle fix.
# Shuttle Diplomacy (engine card 74 / print card #73) now correctly subtracts
# the top-stability USSR-controlled BG from the USSR total only, per verbatim
# card text (twilightstrategy.com/card-list/).  Cleared 4 violations
# (tsreplayer_29 T7, tsreplayer_44 T9, tsreplayer_47 T5, tsreplayer_54 T7).
# Remaining 74 are corpus-convention / log-truncation edge cases; further
# reductions come from #121 corpus expansion and #120 rules-lawyer oracle.
#
# Any future regression that pushes count above 74 indicates an engine-side
# change introduced real mismatches.
#
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

ENGINE_V1_VIOLATION_CEILING="${ENGINE_V1_VIOLATION_CEILING:-74}"
BUILD_DIR="${BUILD_DIR:-build-ninja}"
LOG_DIR="${LOG_DIR:-data/raw_logs}"
OUT_DIR="${OUT_DIR:-results/engine_cert}"
mkdir -p "$OUT_DIR"

# Pretty-print helper.
step() { printf "\n\033[1;36m==> %s\033[0m\n" "$*"; }
fail() { printf "\n\033[1;31m!! %s\033[0m\n" "$*" >&2; exit 1; }
ok()   { printf "\033[1;32m   %s\033[0m\n" "$*"; }

# --- 1. ctest ---------------------------------------------------------------
step "C++ ctest ($BUILD_DIR)"
if [[ ! -d "$BUILD_DIR" ]]; then
  fail "build directory $BUILD_DIR not found — run cmake configure+build first"
fi
# Exclude shelved ISMCTS tests (tests 26-28). ISMCTS is disabled per
# project memory note "feedback_ismcts_verdict" — value head is miscalibrated
# for determinized states; tests stay in the suite for eventual re-enable.
ISMCTS_EXCLUDE="${ISMCTS_EXCLUDE:-^(play_ismcts_matchup_pooled|ismcts determinization|ismcts_search returns)}"
ctest --test-dir "$BUILD_DIR" --output-on-failure \
      --exclude-regex "$ISMCTS_EXCLUDE" \
  > "$OUT_DIR/ctest.log" 2>&1 || {
    tail -50 "$OUT_DIR/ctest.log" >&2
    fail "ctest failed — see $OUT_DIR/ctest.log"
  }
ok "ctest passed ($(grep -cE '^[[:space:]]*[0-9]+/[0-9]+ Test' "$OUT_DIR/ctest.log" || echo '?') tests; ISMCTS shelved tests excluded)"

# --- 2. pytest --------------------------------------------------------------
step "Python pytest (-n 0)"
uv run pytest tests/python/ -q -n 0 \
  > "$OUT_DIR/pytest.log" 2>&1 || {
    tail -80 "$OUT_DIR/pytest.log" >&2
    fail "pytest failed — see $OUT_DIR/pytest.log"
  }
ok "pytest passed ($(grep -oE '[0-9]+ passed' "$OUT_DIR/pytest.log" | head -1))"

# --- 3. replay validator ----------------------------------------------------
step "Replay validator ($LOG_DIR)"
uv run python scripts/validate_replays.py \
  --log-dir "$LOG_DIR" \
  --out "$OUT_DIR/validator.json" \
  --violations-jsonl "$OUT_DIR/violations.jsonl" \
  > "$OUT_DIR/validator.log" 2>&1 || {
    tail -80 "$OUT_DIR/validator.log" >&2
    fail "validator run failed — see $OUT_DIR/validator.log"
  }

violation_count=$(wc -l < "$OUT_DIR/violations.jsonl" | tr -d ' ')
if (( violation_count > ENGINE_V1_VIOLATION_CEILING )); then
  echo "violation count: $violation_count (ceiling: $ENGINE_V1_VIOLATION_CEILING)" >&2
  echo "recent deltas:" >&2
  diff <(sort "$OUT_DIR/violations.jsonl") \
       <(sort results/validator_violations_post127.jsonl 2>/dev/null || true) \
       | head -40 >&2 || true
  fail "validator violation regression: $violation_count > $ENGINE_V1_VIOLATION_CEILING"
fi
ok "validator: $violation_count violations (≤ $ENGINE_V1_VIOLATION_CEILING ceiling)"

# --- Summary ----------------------------------------------------------------
step "Engine v1.0 certification PASSED"
cat <<EOF
  ctest:     $OUT_DIR/ctest.log
  pytest:    $OUT_DIR/pytest.log
  validator: $OUT_DIR/violations.jsonl ($violation_count violations)
  ceiling:   $ENGINE_V1_VIOLATION_CEILING (env: ENGINE_V1_VIOLATION_CEILING)
EOF
