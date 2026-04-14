"""Integration tests for --heuristic-teacher-mode in ts_collect_mcts_games_jsonl.

All tests skip if the binary or scripted model is missing. Use pytest -n 0
(serial) since the tests shell out to the C++ binary.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

import pyarrow.parquet as pq
import pytest

# ---------------------------------------------------------------------------
# Fixtures / constants
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[2]
BINARY = REPO_ROOT / "build-ninja" / "cpp" / "tools" / "ts_collect_mcts_games_jsonl"
# Use v66_sc model — 32-scalar compatible scripted model, doesn't need to be strong.
MODEL_PATH = (
    REPO_ROOT / "data" / "checkpoints" / "scripted_for_elo" / "v66_sc_scripted.pt"
)
SCRIPT = REPO_ROOT / "scripts" / "collect_mcts_targets.py"

BINARY_AVAILABLE = BINARY.exists()
MODEL_AVAILABLE = MODEL_PATH.exists()
DEPS_OK = BINARY_AVAILABLE and MODEL_AVAILABLE

SKIP_REASON = (
    f"binary={BINARY_AVAILABLE} model={MODEL_AVAILABLE} — "
    "requires built ts_collect_mcts_games_jsonl and v99 scripted model"
)


def _run_teacher_mode(
    tmp_dir: Path,
    *,
    seed: int = 1000,
    games: int = 2,
    n_sim: int = 5,
    game_id_prefix: str | None = None,
    extra_args: list[str] | None = None,
) -> list[dict]:
    """Run binary in heuristic_teacher_mode and return parsed JSONL rows."""
    out_jsonl = tmp_dir / "out.jsonl"
    cmd = [
        str(BINARY),
        "--model", str(MODEL_PATH),
        "--games", str(games),
        "--n-sim", str(n_sim),
        "--seed", str(seed),
        "--out", str(out_jsonl),
        "--heuristic-teacher-mode",
        "--torch-intra-threads", "1",
    ]
    if game_id_prefix is not None:
        cmd += ["--game-id-prefix", game_id_prefix]
    if extra_args:
        cmd += extra_args
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    assert proc.returncode == 0, f"binary failed:\n{proc.stderr[-2000:]}"
    rows = []
    with open(out_jsonl) as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def _run_normal_mode(
    tmp_dir: Path,
    *,
    seed: int = 1000,
    games: int = 2,
    n_sim: int = 5,
) -> list[dict]:
    """Run binary in normal mode (no teacher mode) and return parsed JSONL rows."""
    out_jsonl = tmp_dir / "normal_out.jsonl"
    cmd = [
        str(BINARY),
        "--model", str(MODEL_PATH),
        "--games", str(games),
        "--n-sim", str(n_sim),
        "--seed", str(seed),
        "--out", str(out_jsonl),
        "--torch-intra-threads", "1",
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    assert proc.returncode == 0, f"binary failed:\n{proc.stderr[-2000:]}"
    rows = []
    with open(out_jsonl) as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


@pytest.mark.serial
@pytest.mark.skipif(not DEPS_OK, reason=SKIP_REASON)
def test_heuristic_teacher_mode_game_id_prefix(tmp_path):
    """game_ids in heuristic_teacher_mode should start with 'selfplay_<seed>_'."""
    rows = _run_teacher_mode(tmp_path, seed=1000, games=2, n_sim=5)
    assert rows, "Expected at least one row"
    for row in rows:
        gid = row.get("game_id", "")
        assert gid.startswith("selfplay_1000_"), (
            f"Expected game_id to start with 'selfplay_1000_', got '{gid}'"
        )


@pytest.mark.serial
@pytest.mark.skipif(not DEPS_OK, reason=SKIP_REASON)
def test_heuristic_teacher_mode_deterministic(tmp_path):
    """Same seed in heuristic_teacher_mode must produce identical rows."""
    (tmp_path / "a").mkdir()
    (tmp_path / "b").mkdir()
    rows_a = _run_teacher_mode(tmp_path / "a", seed=1001, games=2, n_sim=5)
    rows_b = _run_teacher_mode(tmp_path / "b", seed=1001, games=2, n_sim=5)
    assert len(rows_a) == len(rows_b), (
        f"Row count differs: {len(rows_a)} vs {len(rows_b)}"
    )
    for i, (a, b) in enumerate(zip(rows_a, rows_b)):
        for col in ("game_id", "step_idx", "action_card_id", "action_mode"):
            assert a.get(col) == b.get(col), (
                f"Row {i} col '{col}' differs: {a.get(col)} vs {b.get(col)}"
            )


@pytest.mark.serial
@pytest.mark.skipif(not DEPS_OK, reason=SKIP_REASON)
def test_heuristic_teacher_mode_has_visit_counts(tmp_path):
    """Every row in heuristic_teacher_mode must have mcts_visit_counts and mcts_root_value."""
    rows = _run_teacher_mode(tmp_path, seed=1002, games=2, n_sim=5)
    assert rows, "Expected at least one row"
    for i, row in enumerate(rows):
        vc = row.get("mcts_visit_counts")
        rv = row.get("mcts_root_value")
        assert vc is not None and len(vc) > 0, (
            f"Row {i}: missing or empty mcts_visit_counts"
        )
        assert rv is not None and isinstance(rv, (int, float)), (
            f"Row {i}: missing or non-numeric mcts_root_value"
        )
        import math
        assert math.isfinite(rv), f"Row {i}: mcts_root_value={rv} is not finite"


@pytest.mark.serial
@pytest.mark.skipif(not DEPS_OK, reason=SKIP_REASON)
def test_normal_mode_unaffected(tmp_path):
    """Without --heuristic-teacher-mode, game_ids should start with 'mcts_'."""
    rows = _run_normal_mode(tmp_path, seed=1003, games=2, n_sim=5)
    assert rows, "Expected at least one row"
    for row in rows:
        gid = row.get("game_id", "")
        assert gid.startswith("mcts_"), (
            f"Expected game_id to start with 'mcts_', got '{gid}'"
        )


@pytest.mark.serial
@pytest.mark.skipif(not DEPS_OK, reason=SKIP_REASON)
def test_custom_game_id_prefix(tmp_path):
    """--game-id-prefix should override the default prefix."""
    rows = _run_teacher_mode(tmp_path, seed=1004, games=2, n_sim=5, game_id_prefix="myprefix")
    assert rows, "Expected at least one row"
    for row in rows:
        gid = row.get("game_id", "")
        assert gid.startswith("myprefix_1004_"), (
            f"Expected game_id to start with 'myprefix_1004_', got '{gid}'"
        )


@pytest.mark.serial
@pytest.mark.skipif(not DEPS_OK or not SCRIPT.exists(), reason=SKIP_REASON)
def test_collect_mcts_targets_script_output_schema(tmp_path):
    """collect_mcts_targets.py must produce Parquet with the expected schema."""
    out_parquet = tmp_path / "teacher_targets.parquet"
    cmd = [
        sys.executable, str(SCRIPT),
        "--model", str(MODEL_PATH),
        "--games", "2",
        "--n-sim", "5",
        "--seed", "77700",
        "--output", str(out_parquet),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120,
                          cwd=str(REPO_ROOT),
                          env={**__import__("os").environ,
                               "PYTHONPATH": str(REPO_ROOT / "build-ninja" / "bindings")})
    assert proc.returncode == 0, f"script failed:\n{proc.stderr[-2000:]}"
    assert out_parquet.exists(), "Output Parquet not created"
    table = pq.read_table(out_parquet)
    schema = table.schema
    expected_cols = {
        "game_id", "step_idx",
        "teacher_card_target", "teacher_mode_target", "teacher_value_target",
    }
    actual_cols = set(schema.names)
    assert expected_cols.issubset(actual_cols), (
        f"Missing columns: {expected_cols - actual_cols}"
    )
    # Check teacher_card_target has 111 entries per row
    if len(table) > 0:
        card_col = table.column("teacher_card_target")
        first_row = card_col[0].as_py()
        assert len(first_row) == 111, (
            f"teacher_card_target length={len(first_row)}, expected 111"
        )
