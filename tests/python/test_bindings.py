"""Python-side smoke tests for the native ``tscore`` bindings."""

from __future__ import annotations

import importlib
import os
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
for _bindings_dir in (_REPO / "build-ninja" / "bindings", _REPO / "build" / "bindings"):
    if _bindings_dir.exists() and str(_bindings_dir) not in sys.path:
        sys.path.insert(0, str(_bindings_dir))
        break

# Use v66_sc — 32-scalar compatible scripted model, doesn't need to be strong.
MODEL_PATH = _REPO / "data" / "checkpoints" / "scripted_for_elo" / "v66_sc_scripted.pt"


@pytest.fixture(scope="module")
def tscore_module():
    return importlib.import_module("tscore")


def _assert_game_result_shape(result, tscore) -> None:
    assert isinstance(result, tscore.GameResult)
    assert hasattr(result, "winner")
    assert hasattr(result, "final_vp")
    assert hasattr(result, "end_turn")
    assert hasattr(result, "end_reason")
    assert result.winner in (tscore.Side.USSR, tscore.Side.US, tscore.Side.Neutral, None)
    assert isinstance(result.final_vp, int)
    assert isinstance(result.end_turn, int)
    assert isinstance(result.end_reason, str)


def _normalize_results(results) -> list[tuple[str, int, int, str]]:
    return [
        (str(result.winner), result.final_vp, result.end_turn, result.end_reason)
        for result in results
    ]


def test_import_tscore(tscore_module) -> None:
    assert tscore_module is not None
    assert hasattr(tscore_module, "Side")


def test_side_enum(tscore_module) -> None:
    assert tscore_module.Side.USSR != tscore_module.Side.US


def test_game_result_attrs(tscore_module) -> None:
    for attr in ("winner", "final_vp", "end_turn", "end_reason"):
        assert hasattr(tscore_module.GameResult, attr)

    result = tscore_module.play_random_game(seed=123)
    _assert_game_result_shape(result, tscore_module)


@pytest.mark.skipif(not os.path.exists(MODEL_PATH), reason="model not found")
def test_benchmark_batched_smoke(tscore_module) -> None:
    if not hasattr(tscore_module, "benchmark_batched"):
        pytest.skip("benchmark_batched not available in this build")

    results = tscore_module.benchmark_batched(
        str(MODEL_PATH),
        tscore_module.Side.USSR,
        2,
        pool_size=2,
        seed=7,
    )

    assert isinstance(results, list)
    assert len(results) == 2
    for result in results:
        _assert_game_result_shape(result, tscore_module)


@pytest.mark.skipif(not os.path.exists(MODEL_PATH), reason="model not found")
def test_benchmark_batched_deterministic(tscore_module) -> None:
    if not hasattr(tscore_module, "benchmark_batched"):
        pytest.skip("benchmark_batched not available in this build")

    first = tscore_module.benchmark_batched(
        str(MODEL_PATH),
        tscore_module.Side.USSR,
        2,
        pool_size=2,
        seed=19,
    )
    second = tscore_module.benchmark_batched(
        str(MODEL_PATH),
        tscore_module.Side.USSR,
        2,
        pool_size=2,
        seed=19,
    )

    assert _normalize_results(first) == _normalize_results(second)


@pytest.mark.skipif(not os.path.exists(MODEL_PATH), reason="model not found")
def test_benchmark_ismcts_smoke(tscore_module) -> None:
    if not hasattr(tscore_module, "benchmark_ismcts"):
        pytest.skip("benchmark_ismcts not available in this build")

    results = tscore_module.benchmark_ismcts(
        str(MODEL_PATH),
        tscore_module.Side.USSR,
        1,
        n_determinizations=4,
        n_simulations=5,
        seed=23,
    )

    assert isinstance(results, list)
    assert len(results) == 1
    _assert_game_result_shape(results[0], tscore_module)


@pytest.mark.skipif(not os.path.exists(MODEL_PATH), reason="model not found")
def test_benchmark_ismcts_different_det_counts(tscore_module) -> None:
    """Verify ISMCTS works with different determinization counts."""
    if not hasattr(tscore_module, "benchmark_ismcts"):
        pytest.skip("benchmark_ismcts not available in this build")

    for n_det in (2, 4, 8):
        results = tscore_module.benchmark_ismcts(
            str(MODEL_PATH),
            tscore_module.Side.USSR,
            1,
            n_determinizations=n_det,
            n_simulations=5,
            seed=29,
        )
        assert len(results) == 1
        _assert_game_result_shape(results[0], tscore_module)


@pytest.mark.skipif(not os.path.exists(MODEL_PATH), reason="model not found")
def test_benchmark_ismcts_single_det(tscore_module) -> None:
    """n_determinizations=1 should produce valid results (may draw at VP=0)."""
    if not hasattr(tscore_module, "benchmark_ismcts"):
        pytest.skip("benchmark_ismcts not available in this build")

    results = tscore_module.benchmark_ismcts(
        str(MODEL_PATH),
        tscore_module.Side.USSR,
        1,
        n_determinizations=1,
        n_simulations=5,
        seed=42,  # seed=29 produces a VP=0 draw (winner=None), which is valid
    )
    assert len(results) == 1
    _assert_game_result_shape(results[0], tscore_module)
