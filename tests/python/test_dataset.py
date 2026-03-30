"""Tests for the Parquet dataset builder."""
import tempfile
from pathlib import Path

import polars as pl
import pytest

from tsrl.etl.dataset import (
    MAX_CARD_ID,
    MAX_COUNTRY_ID,
    _CARD_MASK_LEN,
    _COUNTRY_MASK_LEN,
    _card_mask,
    _influence_array,
    _rows_to_dataframe,
    build_dataset,
    process_game,
)
from tsrl.etl.game_data import load_cards
from tsrl.schemas import PublicState, Side


ALL_CARD_IDS = frozenset(cid for cid in load_cards() if cid != 6)

# ---------------------------------------------------------------------------
# Helpers / fixtures
# ---------------------------------------------------------------------------

_MINIMAL_LOG = "\n".join([
    "Turn 1, USSR AR1: East European Unrest: Place Influence (3 Ops):",
    "USSR +3 in Thailand [0][3]",
    "Turn 1, US AR1: NORAD*: Coup (3 Ops):",
    "US +2 in Iran [2][0]",
])

_MULTI_TURN_LOG = "\n".join([
    "Turn 1, USSR AR1: Marshall Plan: Place Influence (6 Ops):",
    "USSR +2 in France [0][2]",
    "Turn 1, US AR1: NORAD*: Coup (3 Ops):",
    "US +2 in Iran [2][0]",
    "Turn 2, USSR AR1: Decolonization: Place Influence (3 Ops):",
    "USSR +2 in Angola [0][2]",
])


# ---------------------------------------------------------------------------
# Unit tests for helpers
# ---------------------------------------------------------------------------


def test_card_mask_empty():
    assert _card_mask(frozenset()) == [0] * _CARD_MASK_LEN


def test_card_mask_sets_correct_positions():
    m = _card_mask(frozenset({1, 10, 111}))
    assert m[1] == 1
    assert m[10] == 1
    assert m[111] == 1
    assert m[0] == 0
    assert sum(m) == 3


def test_card_mask_ignores_out_of_range():
    m = _card_mask(frozenset({0, 200}))
    assert sum(m) == 0


def test_card_mask_length():
    assert len(_card_mask(frozenset())) == _CARD_MASK_LEN


def test_influence_array_length():
    pub = PublicState()
    arr = _influence_array(pub, Side.USSR)
    assert len(arr) == _COUNTRY_MASK_LEN


def test_influence_array_reflects_state():
    pub = PublicState()
    pub.influence[(Side.USSR, 18)] = 3  # West Germany (country_id=18 → index 18)
    arr = _influence_array(pub, Side.USSR)
    assert arr[18] == 3  # array is indexed directly by country_id (0..85)
    arr_us = _influence_array(pub, Side.US)
    assert arr_us[18] == 0


# ---------------------------------------------------------------------------
# process_game
# ---------------------------------------------------------------------------


def test_process_game_returns_rows():
    rows = process_game(_MINIMAL_LOG, "test_game", ALL_CARD_IDS)
    assert len(rows) > 0


def test_process_game_row_count_equals_decision_events():
    """Each PLAY / HEADLINE / SPACE_RACE event → one row."""
    rows = process_game(_MINIMAL_LOG, "test_game", ALL_CARD_IDS)
    # Two action round headers → two PLAY events
    assert len(rows) == 2


def test_process_game_empty_log():
    rows = process_game("", "empty", ALL_CARD_IDS)
    assert rows == []


def test_process_game_row_fields():
    rows = process_game(_MINIMAL_LOG, "abc123", ALL_CARD_IDS)
    row = rows[0]
    assert row.game_id == "abc123"
    assert row.step_idx == 0
    assert row.turn == 1
    assert row.ar == 1
    assert row.phasing == int(Side.USSR)


def test_process_game_mask_lengths():
    rows = process_game(_MINIMAL_LOG, "g", ALL_CARD_IDS)
    row = rows[0]
    assert len(row.ussr_influence) == _COUNTRY_MASK_LEN
    assert len(row.us_influence) == _COUNTRY_MASK_LEN
    assert len(row.discard_mask) == _CARD_MASK_LEN
    assert len(row.actor_known_in) == _CARD_MASK_LEN
    assert len(row.lbl_actor_hand) == _CARD_MASK_LEN
    assert len(row.lbl_card_quality) == _CARD_MASK_LEN
    assert len(row.lbl_opponent_possible) == _CARD_MASK_LEN


def test_process_game_defcon_in_range():
    rows = process_game(_MINIMAL_LOG, "g", ALL_CARD_IDS)
    for row in rows:
        assert 1 <= row.defcon <= 5


def test_process_game_phasing_valid():
    rows = process_game(_MINIMAL_LOG, "g", ALL_CARD_IDS)
    for row in rows:
        assert row.phasing in (int(Side.USSR), int(Side.US))


def test_process_game_step_idx_sequential():
    rows = process_game(_MINIMAL_LOG, "g", ALL_CARD_IDS)
    for i, row in enumerate(rows):
        assert row.step_idx == i


def test_process_game_multi_turn():
    rows = process_game(_MULTI_TURN_LOG, "g", ALL_CARD_IDS)
    assert len(rows) == 3


# ---------------------------------------------------------------------------
# _rows_to_dataframe
# ---------------------------------------------------------------------------


def test_rows_to_dataframe_shape():
    rows = process_game(_MINIMAL_LOG, "g", ALL_CARD_IDS)
    df = _rows_to_dataframe(rows)
    assert df.shape[0] == len(rows)
    assert "game_id" in df.columns
    assert "turn" in df.columns
    assert "lbl_actor_hand" in df.columns


def test_rows_to_dataframe_empty():
    df = _rows_to_dataframe([])
    assert df.is_empty()


# ---------------------------------------------------------------------------
# build_dataset (integration)
# ---------------------------------------------------------------------------


def test_build_dataset_writes_parquet(tmp_path):
    log_dir = tmp_path / "logs"
    log_dir.mkdir()
    out_dir = tmp_path / "parquet"

    # Write 3 minimal log files so we get non-trivial splits.
    for i in range(3):
        (log_dir / f"game{i}.txt").write_text(_MINIMAL_LOG)

    counts = build_dataset(log_dir=log_dir, out_dir=out_dir, seed=0)
    assert counts["total"] > 0
    assert counts["train"] + counts["val"] + counts["test"] == counts["total"]


def test_build_dataset_parquet_files_readable(tmp_path):
    log_dir = tmp_path / "logs"
    log_dir.mkdir()
    out_dir = tmp_path / "parquet"

    for i in range(3):
        (log_dir / f"game{i}.txt").write_text(_MINIMAL_LOG)

    build_dataset(log_dir=log_dir, out_dir=out_dir, seed=0)

    parquet_files = list(out_dir.glob("*.parquet"))
    assert len(parquet_files) > 0
    for pf in parquet_files:
        df = pl.read_parquet(pf)
        assert df.shape[0] > 0
        assert "game_id" in df.columns


def test_build_dataset_no_leakage_same_game_in_one_split(tmp_path):
    """Rows from the same game_id should not appear in multiple splits."""
    log_dir = tmp_path / "logs"
    log_dir.mkdir()
    out_dir = tmp_path / "parquet"

    for i in range(5):
        (log_dir / f"game{i}.txt").write_text(_MINIMAL_LOG + f"\n# game {i}")

    build_dataset(log_dir=log_dir, out_dir=out_dir, seed=42)

    splits: dict[str, set[str]] = {}
    for split in ("train", "val", "test"):
        pf = out_dir / f"{split}.parquet"
        if pf.exists():
            df = pl.read_parquet(pf)
            splits[split] = set(df["game_id"].to_list())

    # No game_id should appear in more than one split
    all_ids = [gid for ids in splits.values() for gid in ids]
    assert len(all_ids) == len(set(all_ids)), "Same game_id in multiple splits!"


def test_build_dataset_empty_dir(tmp_path):
    log_dir = tmp_path / "logs"
    log_dir.mkdir()
    out_dir = tmp_path / "parquet"

    counts = build_dataset(log_dir=log_dir, out_dir=out_dir)
    assert counts["total"] == 0


def test_build_dataset_on_real_logs():
    """Smoke test: build dataset from real raw_logs and verify non-zero rows."""
    with tempfile.TemporaryDirectory() as tmpdir:
        counts = build_dataset(
            log_dir="data/raw_logs",
            out_dir=tmpdir,
            seed=0,
        )
    assert counts["total"] > 0
    # 7 games × ~100-200 decisions each ≈ 700-1400 rows
    assert counts["total"] > 100
