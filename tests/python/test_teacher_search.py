from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import polars as pl
import pytest


def _load_script_module():
    script_path = Path(__file__).resolve().parents[2] / "scripts" / "teacher_search.py"
    spec = importlib.util.spec_from_file_location("teacher_search", script_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _target(size: int, hot_idx: int) -> list[float]:
    values = [0.0] * size
    values[hot_idx] = 1.0
    return values


def test_build_teacher_targets_accumulates_root_visits():
    mod = _load_script_module()

    teacher_card, teacher_mode = mod.build_teacher_targets(
        [
            {"card_id": 3, "mode": 1, "visits": 6},
            {"card_id": 3, "mode": 4, "visits": 2},
            {"card_id": 5, "mode": 1, "visits": 2},
        ]
    )

    assert sum(teacher_card) == pytest.approx(1.0)
    assert sum(teacher_mode) == pytest.approx(1.0)
    assert teacher_card[2] == pytest.approx(0.8)
    assert teacher_card[4] == pytest.approx(0.2)
    assert teacher_mode[1] == pytest.approx(0.8)
    assert teacher_mode[4] == pytest.approx(0.2)


def test_run_teacher_search_rejects_partial_state(tmp_path):
    mod = _load_script_module()
    positions_path = tmp_path / "hard_positions.jsonl"
    positions_path.write_text(
        json.dumps(
            {
                "game_id": "g1",
                "step_index": 7,
                "turn": 4,
                "ar": 2,
                "side": 1,
                "state_dict_complete": False,
                "state_dict": {"_partial": True},
            }
        )
        + "\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="partial state_dict"):
        mod.run_teacher_search(
            positions_path,
            "model.pt",
            tmp_path / "teacher.parquet",
            n_sim=32,
            c_puct=1.5,
            progress_interval=0,
        )


def test_run_teacher_search_resume_merges_existing_cache(tmp_path, monkeypatch):
    mod = _load_script_module()

    class FakeTscore:
        def __init__(self) -> None:
            self.calls: list[dict[str, object]] = []

        def mcts_search_from_state(
            self, *, state_dict, model_path, n_sim, c_puct, calib_a, calib_b, seed
        ):
            self.calls.append(
                {
                    "state_dict": state_dict,
                    "model_path": model_path,
                    "n_sim": n_sim,
                    "c_puct": c_puct,
                    "calib_a": calib_a,
                    "calib_b": calib_b,
                    "seed": seed,
                }
            )
            return {
                "root_value": -0.25,
                "edges": [
                    {"card_id": 2, "mode": 0, "visits": 3},
                    {"card_id": 5, "mode": 4, "visits": 1},
                ],
            }

    fake = FakeTscore()
    monkeypatch.setattr(mod, "_get_tscore", lambda: fake)

    positions_path = tmp_path / "hard_positions.jsonl"
    positions = [
        {
            "game_id": "g0",
            "step_index": 1,
            "turn": 3,
            "ar": 1,
            "side": 0,
            "state_dict_complete": True,
            "state_dict": {"turn": 3, "ar": 1, "phasing": 0},
        },
        {
            "game_id": "g1",
            "step_index": 2,
            "turn": 4,
            "ar": 2,
            "side": 1,
            "state_dict_complete": True,
            "state_dict": {"turn": 4, "ar": 2, "phasing": 1},
        },
    ]
    with positions_path.open("w", encoding="utf-8") as handle:
        for position in positions:
            handle.write(json.dumps(position))
            handle.write("\n")

    out_path = tmp_path / "teacher.parquet"
    existing_df = mod._rows_to_frame(
        [
            {
                "game_id": "g0",
                "step_index": 1,
                "turn": 3,
                "ar": 1,
                "side": 0,
                "teacher_n_sim": 16,
                "teacher_c_puct": 1.0,
                "teacher_root_value": 0.1,
                "teacher_value_target": 0.1,
                "teacher_card_target": _target(mod.CARD_TARGET_SIZE, 0),
                "teacher_mode_target": _target(mod.MODE_TARGET_SIZE, 0),
                "search_elapsed_s": 0.01,
            }
        ]
    )
    existing_df.write_parquet(out_path)

    processed = mod.run_teacher_search(
        positions_path,
        "model.pt",
        out_path,
        n_sim=64,
        c_puct=1.5,
        seed=11,
        resume=True,
        progress_interval=0,
    )

    assert processed == 1
    assert fake.calls == [
        {
            "state_dict": {"turn": 4, "ar": 2, "phasing": 1},
            "model_path": "model.pt",
            "n_sim": 64,
            "c_puct": 1.5,
            "calib_a": 1.0,
            "calib_b": 0.0,
            "seed": 11,
        }
    ]

    df = pl.read_parquet(out_path).sort(["game_id", "step_index"])
    assert df["game_id"].to_list() == ["g0", "g1"]
    assert df["step_index"].to_list() == [1, 2]

    new_row = df.filter((pl.col("game_id") == "g1") & (pl.col("step_index") == 2)).row(
        0, named=True
    )
    assert sum(new_row["teacher_card_target"]) == pytest.approx(1.0)
    assert sum(new_row["teacher_mode_target"]) == pytest.approx(1.0)
    assert new_row["teacher_card_target"][1] == pytest.approx(0.75)
    assert new_row["teacher_card_target"][4] == pytest.approx(0.25)
    assert new_row["teacher_mode_target"][0] == pytest.approx(0.75)
    assert new_row["teacher_mode_target"][4] == pytest.approx(0.25)


def test_load_calibration_reads_platt_params(tmp_path):
    mod = _load_script_module()
    path = tmp_path / "calibration.json"
    path.write_text(json.dumps({"a": 1.25, "b": -0.5}), encoding="utf-8")

    assert mod._load_calibration(path) == pytest.approx((1.25, -0.5))
    assert mod._load_calibration(None) == pytest.approx((1.0, 0.0))
