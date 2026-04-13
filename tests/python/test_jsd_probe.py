from __future__ import annotations

import importlib.util
import math
from pathlib import Path

import polars as pl
import pytest
import torch
from tsrl.policies.jsd_probe import ProbeEvaluator
from tsrl.policies.model import CARD_DIM, INFLUENCE_DIM, SCALAR_DIM, TSBaselineModel

_SCRIPT_PATH = Path(__file__).resolve().parents[2] / "scripts" / "build_probe_set.py"


def _load_build_probe_module():
    spec = importlib.util.spec_from_file_location("build_probe_set", _SCRIPT_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _feature_vec(length: int, offset: int) -> list[float]:
    return [float(((idx + offset) % 7) / 6.0) for idx in range(length)]


def _mask_vec(length: int, period: int, offset: int) -> list[bool]:
    return [((idx + offset) % period) == 0 for idx in range(length)]


def _write_probe_parquet(
    path: Path,
    turns: list[int],
    *,
    single_legal_card: bool = False,
) -> Path:
    rows = []
    for row_idx, turn in enumerate(turns):
        if single_legal_card:
            card_mask = [False] * 111
            card_mask[row_idx % 111] = True
        else:
            card_mask = _mask_vec(111, 5, row_idx)
            if not any(card_mask):
                card_mask[0] = True
        rows.append(
            {
                "influence": _feature_vec(INFLUENCE_DIM, row_idx),
                "cards": _feature_vec(CARD_DIM, row_idx + 1),
                "scalars": _feature_vec(SCALAR_DIM, row_idx + 2),
                "card_mask": card_mask,
                "mode_mask": [True] * 5,
                "raw_turn": turn,
                "side_int": row_idx % 2,
                "raw_defcon": (row_idx % 5) + 1,
                "raw_vp": (row_idx % 11) - 5,
                "mode_id": row_idx % 5,
            }
        )
    pl.DataFrame(rows).write_parquet(path)
    return path


def _write_rollout_source(dir_path: Path, n_rows: int = 18) -> Path:
    dir_path.mkdir(parents=True, exist_ok=True)
    rows = []
    turns = [1, 2, 3, 4, 5, 7, 8, 9, 10]
    for row_idx in range(n_rows):
        turn = turns[row_idx % len(turns)]
        side = row_idx % 2
        rows.append(
            {
                "influence": _feature_vec(INFLUENCE_DIM, row_idx),
                "cards": _feature_vec(CARD_DIM, row_idx + 1),
                "scalars": _feature_vec(SCALAR_DIM, row_idx + 2),
                "raw_turn": turn,
                "side_int": side,
                "raw_defcon": (row_idx % 5) + 1,
                "raw_vp": ((row_idx * 3) % 21) - 10,
                "hand_card_ids": [1 + (row_idx % 5), 6 + (row_idx % 7), 12 + (row_idx % 9)],
                "mode_id": row_idx % 5,
            }
        )
    out_path = dir_path / "rollout.parquet"
    pl.DataFrame(rows).write_parquet(out_path)
    return out_path


def test_jsd_identical_models(tmp_path: Path) -> None:
    probe_path = _write_probe_parquet(tmp_path / "probe.parquet", [1, 2, 5, 6, 8, 10])
    evaluator = ProbeEvaluator(probe_path, batch_size=2)

    torch.manual_seed(0)
    model_a = TSBaselineModel()
    model_b = TSBaselineModel()
    model_b.load_state_dict(model_a.state_dict())
    model_a.train()
    model_b.eval()

    metrics = evaluator.compare(model_a, model_b)

    assert metrics.card_jsd == pytest.approx(0.0, abs=1e-8)
    assert metrics.mode_jsd == pytest.approx(0.0, abs=1e-8)
    assert metrics.country_jsd == pytest.approx(0.0, abs=1e-8)
    assert metrics.value_mae == pytest.approx(0.0, abs=1e-8)
    assert metrics.top1_card_agree == pytest.approx(1.0, abs=1e-8)
    assert metrics.top1_mode_agree == pytest.approx(1.0, abs=1e-8)
    assert model_a.training is True
    assert model_b.training is False


def test_jsd_random_models(tmp_path: Path) -> None:
    probe_path = _write_probe_parquet(tmp_path / "probe.parquet", [1, 2, 5, 6, 8, 10])
    evaluator = ProbeEvaluator(probe_path, batch_size=3)

    torch.manual_seed(1)
    model_a = TSBaselineModel()
    torch.manual_seed(2)
    model_b = TSBaselineModel()

    metrics = evaluator.compare(model_a, model_b)

    assert 0.0 <= metrics.card_jsd <= 1.0
    assert 0.0 <= metrics.mode_jsd <= 1.0
    assert 0.0 <= metrics.country_jsd <= 1.0
    assert metrics.card_jsd > 0.0
    assert metrics.mode_jsd > 0.0
    assert metrics.value_mae > 0.0


def test_jsd_masking(tmp_path: Path) -> None:
    probe_path = _write_probe_parquet(
        tmp_path / "probe.parquet",
        [1, 5, 9],
        single_legal_card=True,
    )
    evaluator = ProbeEvaluator(probe_path)

    torch.manual_seed(3)
    model_a = TSBaselineModel()
    torch.manual_seed(4)
    model_b = TSBaselineModel()

    metrics = evaluator.compare(model_a, model_b)

    assert metrics.card_jsd == pytest.approx(0.0, abs=1e-8)


def test_probe_metrics_phases(tmp_path: Path) -> None:
    probe_path = _write_probe_parquet(tmp_path / "probe.parquet", [1, 2, 5, 6, 8, 10])
    evaluator = ProbeEvaluator(probe_path)

    torch.manual_seed(5)
    model_a = TSBaselineModel()
    torch.manual_seed(6)
    model_b = TSBaselineModel()

    metrics = evaluator.compare(model_a, model_b)

    assert not math.isnan(metrics.card_jsd_early)
    assert not math.isnan(metrics.card_jsd_mid)
    assert not math.isnan(metrics.card_jsd_late)


def test_build_probe_set_stratification(tmp_path: Path) -> None:
    build_probe = _load_build_probe_module()
    src_dir = tmp_path / "ppo_rollout_combined"
    _write_rollout_source(src_dir, n_rows=24)
    out_path = tmp_path / "probe_positions.parquet"

    build_probe.build_probe_set(src_dir, out_path, n=18, seed=42)
    frame = pl.read_parquet(out_path)

    assert len(frame) == 18
    seen = {
        ("early" if row["raw_turn"] <= 3 else "mid" if row["raw_turn"] <= 7 else "late", row["side_int"])
        for row in frame.select(["raw_turn", "side_int"]).to_dicts()
    }
    expected = {
        ("early", 0),
        ("early", 1),
        ("mid", 0),
        ("mid", 1),
        ("late", 0),
        ("late", 1),
    }
    assert expected.issubset(seen)


def test_probe_evaluator_load(tmp_path: Path) -> None:
    probe_path = _write_probe_parquet(tmp_path / "probe.parquet", [1, 5, 9, 10])
    evaluator = ProbeEvaluator(probe_path)

    assert evaluator.influence.shape == (4, INFLUENCE_DIM)
    assert evaluator.cards.shape == (4, CARD_DIM)
    assert evaluator.scalars.shape == (4, SCALAR_DIM)
    assert evaluator.card_mask.shape == (4, 111)
    assert evaluator.mode_mask.shape == (4, 5)
    assert evaluator.n_positions == 4
