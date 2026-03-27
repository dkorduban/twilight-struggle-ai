"""
Tests for python/tsrl/selfplay/collector.py.

All tests use n_sim=1 and n_games=1 (or 2 for multi-game checks) to keep
the suite fast.  The MCTS functions are exercised but with minimal budget.
"""
from __future__ import annotations

import pytest

from tsrl.selfplay.collector import (
    REQUIRED_COLUMNS,
    collect_games,
)
from tsrl.schemas import Side


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _fast_rows(n_games: int = 1, seed: int = 0, use_uct: bool = False) -> list[dict]:
    """Collect rows with the cheapest possible settings."""
    return collect_games(n_games=n_games, n_sim=1, base_seed=seed, use_uct=use_uct)


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_collect_single_game_returns_rows():
    """One game must produce at least one decision-point row."""
    rows = _fast_rows(n_games=1, seed=7)
    assert len(rows) > 0, "Expected at least one row from a single self-play game"


def test_row_schema_has_required_columns():
    """Every required column must be present in every row."""
    rows = _fast_rows(n_games=1, seed=8)
    assert rows, "No rows returned"
    for col in REQUIRED_COLUMNS:
        for i, row in enumerate(rows):
            assert col in row, f"Row {i} missing required column '{col}'"


def test_game_id_unique_per_game():
    """Two games with different game_idx must have different game_id values."""
    rows = _fast_rows(n_games=2, seed=9)
    assert rows, "No rows returned"
    game_ids = {row["game_id"] for row in rows}
    assert len(game_ids) == 2, (
        f"Expected 2 distinct game_ids from 2 games, got {game_ids}"
    )


def test_winner_side_consistent():
    """winner_side must match game_result string."""
    rows = _fast_rows(n_games=2, seed=10)
    assert rows, "No rows returned"
    mapping = {"ussr_win": 1, "us_win": -1, "draw": 0}
    for i, row in enumerate(rows):
        expected = mapping[row["game_result"]]
        assert row["winner_side"] == expected, (
            f"Row {i}: game_result={row['game_result']} "
            f"but winner_side={row['winner_side']} (expected {expected})"
        )


def test_deterministic_with_seed():
    """Same seed must produce identical row sequences."""
    rows_a = _fast_rows(n_games=1, seed=42)
    rows_b = _fast_rows(n_games=1, seed=42)
    assert len(rows_a) == len(rows_b), "Different row counts with same seed"
    for i, (a, b) in enumerate(zip(rows_a, rows_b)):
        # Compare scalar columns that must be identical.
        for col in ("game_id", "step_idx", "turn", "ar", "phasing",
                    "vp", "defcon", "winner_side", "final_vp", "end_turn",
                    "action_card_id", "action_mode", "action_targets"):
            assert a[col] == b[col], (
                f"Row {i} column '{col}' differs between identical seeds: "
                f"{a[col]!r} vs {b[col]!r}"
            )


def test_value_target_range():
    """winner_side must be in {-1, 0, 1}."""
    rows = _fast_rows(n_games=2, seed=11)
    assert rows, "No rows returned"
    for i, row in enumerate(rows):
        assert row["winner_side"] in (-1, 0, 1), (
            f"Row {i}: winner_side={row['winner_side']} outside valid range"
        )


def test_hand_features_present():
    """Hand feature columns must be non-null and have the right list length."""
    from tsrl.etl.dataset import _CARD_MASK_LEN

    rows = _fast_rows(n_games=1, seed=12)
    assert rows, "No rows returned"
    list_cols = ("actor_known_in", "actor_possible", "lbl_actor_hand", "lbl_card_quality")
    for i, row in enumerate(rows):
        for col in list_cols:
            assert col in row, f"Row {i} missing column '{col}'"
            assert row[col] is not None, f"Row {i} column '{col}' is None"
            assert len(row[col]) == _CARD_MASK_LEN, (
                f"Row {i} column '{col}' has length {len(row[col])}, "
                f"expected {_CARD_MASK_LEN}"
            )
        # actor_hand_size must be non-negative.
        assert row["actor_hand_size"] >= 0, (
            f"Row {i}: actor_hand_size={row['actor_hand_size']} is negative"
        )
        # lbl_step_quality must be 0 (EXACT) for self-play.
        assert row["lbl_step_quality"] == 0, (
            f"Row {i}: lbl_step_quality={row['lbl_step_quality']} "
            f"(expected 0 = EXACT for self-play)"
        )


def test_action_fields_valid():
    """action_card_id must be a positive int; action_mode must be in [0,4]."""
    rows = _fast_rows(n_games=1, seed=13)
    assert rows, "No rows returned"
    for i, row in enumerate(rows):
        assert isinstance(row["action_card_id"], int) and row["action_card_id"] > 0, (
            f"Row {i}: invalid action_card_id={row['action_card_id']}"
        )
        assert 0 <= row["action_mode"] <= 4, (
            f"Row {i}: action_mode={row['action_mode']} out of range [0,4]"
        )
        # action_targets must be a string (possibly empty).
        assert isinstance(row["action_targets"], str), (
            f"Row {i}: action_targets type={type(row['action_targets'])}"
        )


def test_phasing_is_ussr_or_us():
    """phasing must be 0 (USSR) or 1 (US) in every row."""
    rows = _fast_rows(n_games=2, seed=14)
    assert rows, "No rows returned"
    for i, row in enumerate(rows):
        assert row["phasing"] in (int(Side.USSR), int(Side.US)), (
            f"Row {i}: phasing={row['phasing']} not in {{0, 1}}"
        )
