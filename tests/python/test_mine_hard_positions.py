from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np
import polars as pl
import pytest


def _load_script_module():
    script_path = Path(__file__).resolve().parents[2] / "scripts" / "mine_hard_positions.py"
    spec = importlib.util.spec_from_file_location("mine_hard_positions", script_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _mask(*ids: int) -> list[int]:
    mask = [0] * 112
    for cid in ids:
        mask[cid] = 1
    return mask


def _influence(seed: int) -> list[int]:
    return [int((seed + idx) % 4) for idx in range(86)]


def test_add_scores_and_top_k_records_rank_deterministically():
    mod = _load_script_module()

    df = pl.DataFrame(
        {
            "game_id": ["g2", "g1", "g1"],
            "step_idx": [2, 0, 1],
            "turn": [4, 3, 3],
            "ar": [2, 1, 2],
            "phasing": [1, 0, 1],
            "vp": [1, -2, 0],
            "defcon": [4, 5, 3],
            "milops_ussr": [1, 0, 2],
            "milops_us": [0, 1, 2],
            "space_ussr": [0, 1, 2],
            "space_us": [1, 2, 3],
            "china_held_by": [0, 1, 0],
            "china_playable": [True, False, True],
            "actor_hand_size": [7, 8, 6],
            "actor_holds_china": [False, True, False],
            "opp_hand_size": [8, 7, 6],
            "opp_holds_china": [True, False, True],
            "winner_side": [1, -1, 0],
            "final_vp": [-6, -10, 0],
            "end_reason": ["turn_limit", "turn_limit", "turn_limit"],
            "ussr_influence": [_influence(0), _influence(1), _influence(2)],
            "us_influence": [_influence(3), _influence(4), _influence(5)],
            "discard_mask": [_mask(1, 3), _mask(2), _mask()],
            "removed_mask": [_mask(4), _mask(5), _mask(6)],
            "actor_known_in": [_mask(7, 8), _mask(9), _mask(10, 11)],
            "actor_known_not_in": [_mask(12), _mask(13, 14), _mask(15)],
            "actor_possible": [_mask(7, 8, 16), _mask(9, 17), _mask(10, 11, 18)],
            "opp_known_in": [_mask(), _mask(19), _mask()],
            "opp_known_not_in": [_mask(20), _mask(21), _mask(22)],
            "opp_possible": [_mask(23), _mask(24, 25), _mask(26)],
        }
    )

    preds = np.array([0.1, 0.2, 0.0], dtype=np.float32)
    scored = mod.add_scores(df, preds, metric="both")
    records = mod.top_k_records(scored, top_k=2)

    assert [record["game_id"] for record in records] == ["g1", "g2"]
    assert [record["step_index"] for record in records] == [0, 2]

    first = records[0]
    assert first["value_target"] == -0.5
    assert first["surprise_score"] == pytest.approx(0.7)
    assert first["uncertainty_score"] == pytest.approx(0.8)
    assert first["difficulty_score"] == pytest.approx(1.5)
    assert first["state_dict_complete"] is False
    assert first["state_dict"]["_partial"] is True
    assert first["state_dict"]["discard"] == [2]
    assert first["state_dict"]["removed"] == [5]
    assert first["state_dict"]["actor_known_in"] == [9]
    assert "ussr_hand" in first["state_dict"]["_missing_keys"]
