from __future__ import annotations

import math
import subprocess
import sys
from pathlib import Path

import polars as pl
import pytest
import torch
import torch.nn as nn

from tsrl.policies.jsd_probe import ProbeEvaluator


class TinyProbeModel(nn.Module):
    def __init__(self, seed: int) -> None:
        super().__init__()
        torch.manual_seed(seed)
        self.influence_encoder = nn.Linear(172, 32)
        self.card_encoder = nn.Linear(448, 32)
        self.scalar_encoder = nn.Linear(32, 32)
        self.card_head = nn.Linear(32, 111)
        self.mode_head = nn.Linear(32, 5)
        self.country_head = nn.Linear(32, 86)
        self.value_head = nn.Linear(32, 1)

    def forward(
        self,
        influence: torch.Tensor,
        cards: torch.Tensor,
        scalars: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        hidden = torch.tanh(
            self.influence_encoder(influence)
            + self.card_encoder(cards)
            + self.scalar_encoder(scalars)
        )
        return {
            "card_logits": self.card_head(hidden),
            "mode_logits": self.mode_head(hidden),
            "country_logits": self.country_head(hidden),
            "value": torch.tanh(self.value_head(hidden)),
        }


def _make_probe_rows(
    turns: list[int],
    *,
    hand_card_ids: list[list[int]] | None = None,
    mode_ids: list[int] | None = None,
) -> list[dict]:
    rows: list[dict] = []
    hand_card_ids = hand_card_ids or [[1, 2, 3] for _ in turns]
    mode_ids = mode_ids or [0 for _ in turns]
    for idx, turn in enumerate(turns):
        defcon = (idx % 5) + 1
        side_int = idx % 2
        vp = idx - 3
        influence = [float((idx + j) % 7) for j in range(172)]
        cards = [0.0] * 448
        for card_id in hand_card_ids[idx]:
            if 1 <= card_id <= 111:
                cards[card_id - 1] = 1.0
                cards[111 + card_id - 1] = 1.0
        scalars = [0.0] * 32
        scalars[0] = vp / 20.0
        scalars[1] = (defcon - 1) / 4.0
        scalars[8] = turn / 10.0
        scalars[10] = float(side_int)
        rows.append(
            {
                "influence": influence,
                "cards": cards,
                "scalars": scalars,
                "raw_turn": turn,
                "side_int": side_int,
                "raw_defcon": defcon,
                "raw_vp": vp,
                "hand_card_ids": hand_card_ids[idx],
                "mode_id": mode_ids[idx],
            }
        )
    return rows


def _write_probe_parquet(tmp_path: Path, rows: list[dict], name: str = "probe.parquet") -> Path:
    path = tmp_path / name
    pl.DataFrame(rows).write_parquet(path)
    return path


def _make_rollout_input(tmp_path: Path) -> Path:
    data_dir = tmp_path / "rollouts"
    data_dir.mkdir()

    rows: list[dict] = []
    turn_buckets = [2, 5, 9]
    side_values = [0, 1]
    defcon_values = [2, 3, 5]
    idx = 0
    for turn in turn_buckets:
        for side_int in side_values:
            for defcon in defcon_values:
                rows.extend(
                    _make_probe_rows(
                        [turn, turn],
                        hand_card_ids=[[1 + (idx % 5), 7], [2 + (idx % 5), 8]],
                        mode_ids=[0, 2],
                    )
                )
                rows[-2]["side_int"] = side_int
                rows[-1]["side_int"] = side_int
                rows[-2]["raw_defcon"] = defcon
                rows[-1]["raw_defcon"] = defcon
                idx += 1

    frame = pl.DataFrame(rows)
    midpoint = len(frame) // 2
    frame[:midpoint].write_parquet(data_dir / "part_a.parquet")
    frame[midpoint:].write_parquet(data_dir / "part_b.parquet")
    return data_dir


def test_jsd_identical_models(tmp_path: Path) -> None:
    probe_path = _write_probe_parquet(tmp_path, _make_probe_rows([1, 4, 8, 10], mode_ids=[0, 2, 3, 0]))
    evaluator = ProbeEvaluator(probe_path)
    model_a = TinyProbeModel(seed=7)
    model_b = TinyProbeModel(seed=11)
    model_b.load_state_dict(model_a.state_dict())

    metrics = evaluator.compare(model_a, model_b)

    assert metrics.card_jsd == pytest.approx(0.0, abs=1e-7)
    assert metrics.mode_jsd == pytest.approx(0.0, abs=1e-7)
    assert metrics.country_jsd == pytest.approx(0.0, abs=1e-7)
    assert metrics.value_mae == pytest.approx(0.0, abs=1e-7)
    assert metrics.top1_card_agree == pytest.approx(1.0, abs=1e-7)
    assert metrics.top1_mode_agree == pytest.approx(1.0, abs=1e-7)


def test_jsd_random_models(tmp_path: Path) -> None:
    probe_path = _write_probe_parquet(tmp_path, _make_probe_rows([1, 3, 5, 7, 9], mode_ids=[0, 2, 3, 0, 2]))
    evaluator = ProbeEvaluator(probe_path)
    model_a = TinyProbeModel(seed=1)
    model_b = TinyProbeModel(seed=2)

    metrics = evaluator.compare(model_a, model_b)

    assert 0.0 < metrics.card_jsd <= 1.0
    assert 0.0 < metrics.mode_jsd <= 1.0
    assert 0.0 < metrics.country_jsd <= 1.0


def test_jsd_masking(tmp_path: Path) -> None:
    probe_path = _write_probe_parquet(
        tmp_path,
        _make_probe_rows([1, 2, 3], hand_card_ids=[[17], [17], [17]], mode_ids=[0, 0, 0]),
    )
    evaluator = ProbeEvaluator(probe_path)
    model_a = TinyProbeModel(seed=3)
    model_b = TinyProbeModel(seed=4)

    metrics = evaluator.compare(model_a, model_b)

    assert metrics.card_jsd == pytest.approx(0.0, abs=1e-7)


def test_probe_metrics_phases(tmp_path: Path) -> None:
    probe_path = _write_probe_parquet(tmp_path, _make_probe_rows(list(range(1, 11)), mode_ids=[0] * 10))
    evaluator = ProbeEvaluator(probe_path)
    metrics = evaluator.compare(TinyProbeModel(seed=5), TinyProbeModel(seed=6))

    assert not math.isnan(metrics.card_jsd_early)
    assert not math.isnan(metrics.card_jsd_mid)
    assert not math.isnan(metrics.card_jsd_late)


def test_build_probe_set_runs(tmp_path: Path) -> None:
    data_dir = _make_rollout_input(tmp_path)
    out_path = tmp_path / "probe_positions.parquet"
    repo_root = Path(__file__).resolve().parents[2]

    subprocess.run(
        [
            sys.executable,
            str(repo_root / "scripts" / "build_probe_set.py"),
            "--data-dir",
            str(data_dir),
            "--out",
            str(out_path),
            "--n",
            "8",
            "--seed",
            "13",
            "--force",
        ],
        cwd=repo_root,
        check=True,
        capture_output=True,
        text=True,
    )

    result = pl.read_parquet(out_path)
    assert len(result) <= 8
    assert {
        "influence",
        "cards",
        "scalars",
        "raw_turn",
        "side_int",
        "raw_defcon",
        "raw_vp",
        "hand_card_ids",
        "mode_id",
        "card_mask",
        "mode_mask",
    }.issubset(result.columns)


def test_probe_evaluator_load(tmp_path: Path) -> None:
    probe_path = _write_probe_parquet(tmp_path, _make_probe_rows([2, 6, 9], mode_ids=[0, 2, 3]))
    evaluator = ProbeEvaluator(probe_path)

    assert evaluator.n_positions > 0
    assert evaluator.influence.shape == (3, 172)
    assert evaluator.cards.shape == (3, 448)
    assert evaluator.scalars.shape == (3, 32)
    assert evaluator.card_mask.shape == (3, 111)
    assert evaluator.mode_mask.shape == (3, 5)
