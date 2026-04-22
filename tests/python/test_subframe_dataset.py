from __future__ import annotations

import pytest
import polars as pl

from tsrl.policies.dataset import (
    TARGET_HEAD_AR,
    TARGET_HEAD_COUNTRY_PICK,
    TS_SelfPlayDataset,
)


def _base_row(**overrides):
    zeros86 = [0] * 86
    zeros112 = [0] * 112
    row = {
        "ussr_influence": zeros86,
        "us_influence": zeros86,
        "actor_known_in": [1] + [0] * 111,
        "actor_possible": [1] + [0] * 111,
        "discard_mask": zeros112,
        "removed_mask": zeros112,
        "vp": 0,
        "defcon": 5,
        "milops_ussr": 0,
        "milops_us": 0,
        "space_ussr": 0,
        "space_us": 0,
        "china_held_by": 0,
        "actor_holds_china": 0,
        "turn": 1,
        "ar": 1,
        "phasing": 0,
        "action_card_id": 1,
        "action_mode": 4,
        "action_targets": "",
        "winner_side": 1,
        "final_vp": 10,
        "end_reason": "vp",
        "game_id": "g1",
        "step_idx": 0,
    }
    row.update(overrides)
    return row


def _write_parquet(path, rows):
    pl.DataFrame(rows).write_parquet(path)


def test_subframe_defaults_for_old_parquet(tmp_path):
    path = tmp_path / "old.parquet"
    _write_parquet(path, [_base_row()])

    ds = TS_SelfPlayDataset(str(path))
    item = ds[0]

    assert int(item["row_kind"]) == 0
    assert int(item["frame_kind"]) == 0
    assert int(item["target_head"]) == TARGET_HEAD_AR
    assert item["eligible_cards_mask"].shape == (112,)
    assert item["eligible_countries_mask"].shape == (86,)
    assert int(item["eligible_cards_mask"].sum()) == 0
    assert int(item["eligible_countries_mask"].sum()) == 0
    assert item["scalars"][32].item() == pytest.approx(0.0)
    assert item["scalars"][34].item() == pytest.approx(1.0 / 16.0)
    assert item["scalars"][39].item() == pytest.approx(1.0)


def test_subframe_columns_and_frame_context(tmp_path):
    path = tmp_path / "new.parquet"
    _write_parquet(
        path,
        [
            _base_row(
                row_kind="subframe",
                frame_kind=2,
                source_card=17,
                parent_card=9,
                step_index=1,
                total_steps=4,
                budget_remaining=2,
                stack_depth=2,
                criteria_bits=255,
                eligible_cards=[17, 42],
                eligible_countries=[5, 6],
                eligible_n=2,
                chosen_option_index=1,
                chosen_card=42,
                chosen_country=6,
            )
        ],
    )

    ds = TS_SelfPlayDataset(str(path))
    item = ds[0]
    frame_ctx = item["scalars"][32:40]

    assert int(item["row_kind"]) == 1
    assert int(item["frame_kind"]) == 2
    assert int(item["target_head"]) == TARGET_HEAD_COUNTRY_PICK
    assert int(item["eligible_cards_mask"][16]) == 1
    assert int(item["eligible_cards_mask"][41]) == 1
    assert int(item["eligible_countries_mask"][5]) == 1
    assert int(item["eligible_countries_mask"][6]) == 1
    assert frame_ctx[0].item() == pytest.approx(0.2)
    assert frame_ctx[1].item() == pytest.approx(0.25)
    assert frame_ctx[2].item() == pytest.approx(0.25)
    assert frame_ctx[3].item() == pytest.approx(0.5)
    assert frame_ctx[4].item() == pytest.approx(0.5)
    assert frame_ctx[5].item() == pytest.approx(17.0 / 112.0)
    assert frame_ctx[6].item() == pytest.approx(1.0)
    assert frame_ctx[7].item() == pytest.approx(0.0)
