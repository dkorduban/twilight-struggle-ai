"""Tests for tscore.benchmark_model_vs_model_batched.

Covers: correctness, edge cases, determinism, statistical validity.
Run with:
    uv run pytest tests/python/test_benchmark_model_vs_model.py -v -n 0 --timeout=600
Exclude slow tests:
    uv run pytest tests/python/test_benchmark_model_vs_model.py -v -n 0 -m "not slow"
"""
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

# ---------------------------------------------------------------------------
# Model paths
# ---------------------------------------------------------------------------

# Fast BC checkpoint — used as "same model" for symmetry / determinism tests
MODEL_A = str(_REPO / "data/checkpoints/scripted_for_elo/bc_wide384_scripted.pt")
# Different model — PPO current best (32-scalar compatible)
MODEL_B = str(_REPO / "data/checkpoints/ppo_v205_sc_league/ppo_best_scripted.pt")

_SINGLE_MODEL_EXISTS = os.path.exists(MODEL_A)
_MODELS_EXIST = _SINGLE_MODEL_EXISTS and os.path.exists(MODEL_B)

skip_no_single_model = pytest.mark.skipif(
    not _SINGLE_MODEL_EXISTS, reason=f"model not found: {MODEL_A}"
)
skip_no_models = pytest.mark.skipif(
    not _MODELS_EXIST,
    reason=f"models not found: {MODEL_A} and/or {MODEL_B}",
)


@pytest.fixture(scope="module")
def ts():
    return importlib.import_module("tscore")


def _has_bmvmb(ts) -> bool:
    return hasattr(ts, "benchmark_model_vs_model_batched")


def _model_a_wins(results, half, ts):
    wins = 0
    for i, r in enumerate(results):
        if r.winner is None:
            continue
        if i < half:
            wins += 1 if r.winner == ts.Side.USSR else 0
        else:
            wins += 1 if r.winner == ts.Side.US else 0
    return wins


# ---------------------------------------------------------------------------
# 1. Correctness tests
# ---------------------------------------------------------------------------


@skip_no_single_model
def test_result_count_even(ts):
    """n_games=10 returns exactly 10 results."""
    if not _has_bmvmb(ts):
        pytest.skip("benchmark_model_vs_model_batched not available")
    results = ts.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_A, n_games=10, pool_size=4, seed=42,
        temperature=0.0, nash_temperatures=False,
    )
    assert len(results) == 10


@skip_no_single_model
def test_winner_and_vp_consistency(ts):
    """Every result has a valid winner; VP sign must agree with winner for
    turn-limit and vp-threshold end reasons."""
    if not _has_bmvmb(ts):
        pytest.skip("benchmark_model_vs_model_batched not available")
    results = ts.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_A, n_games=20, pool_size=8, seed=100,
        temperature=0.0, nash_temperatures=False,
    )
    for i, r in enumerate(results):
        assert r.winner in (ts.Side.USSR, ts.Side.US, None), (
            f"Game {i}: invalid winner {r.winner!r}"
        )
        assert isinstance(r.final_vp, int), f"Game {i}: final_vp not int"
        assert isinstance(r.end_turn, int), f"Game {i}: end_turn not int"
        assert isinstance(r.end_reason, str), f"Game {i}: end_reason not str"
        assert 1 <= r.end_turn <= 10, (
            f"Game {i}: end_turn={r.end_turn} out of range [1, 10]"
        )
        # VP sign must match winner for scoring-based endings
        SCORING_ENDINGS = {"turn_limit", "vp_threshold"}
        if r.end_reason in SCORING_ENDINGS:
            if r.winner == ts.Side.USSR:
                assert r.final_vp > 0, (
                    f"Game {i}: USSR won via {r.end_reason} but final_vp={r.final_vp}"
                )
            elif r.winner == ts.Side.US:
                assert r.final_vp < 0, (
                    f"Game {i}: US won via {r.end_reason} but final_vp={r.final_vp}"
                )
            elif r.winner is None:
                assert r.final_vp == 0, (
                    f"Game {i}: draw via {r.end_reason} but final_vp={r.final_vp}"
                )


@skip_no_single_model
def test_determinism_same_seed(ts):
    """Same inputs produce identical results."""
    if not _has_bmvmb(ts):
        pytest.skip("benchmark_model_vs_model_batched not available")
    kwargs = dict(
        model_a_path=MODEL_A,
        model_b_path=MODEL_A,
        n_games=10,
        pool_size=4,
        seed=777,
        temperature=0.0,
        nash_temperatures=False,
    )
    r1 = ts.benchmark_model_vs_model_batched(**kwargs)
    r2 = ts.benchmark_model_vs_model_batched(**kwargs)
    assert len(r1) == len(r2)
    for i, (a, b) in enumerate(zip(r1, r2)):
        assert str(a.winner) == str(b.winner), f"Game {i}: winner mismatch"
        assert a.final_vp == b.final_vp, f"Game {i}: VP mismatch"
        assert a.end_turn == b.end_turn, f"Game {i}: end_turn mismatch"
        assert a.end_reason == b.end_reason, f"Game {i}: end_reason mismatch"


@skip_no_single_model
def test_different_seeds_differ(ts):
    """Results with different seeds are not all identical."""
    if not _has_bmvmb(ts):
        pytest.skip("benchmark_model_vs_model_batched not available")
    kwargs = dict(
        model_a_path=MODEL_A,
        model_b_path=MODEL_A,
        n_games=20,
        pool_size=8,
        temperature=0.0,
        nash_temperatures=False,
    )
    r1 = ts.benchmark_model_vs_model_batched(seed=1000, **kwargs)
    r2 = ts.benchmark_model_vs_model_batched(seed=2000, **kwargs)
    any_differ = any(
        a.final_vp != b.final_vp or str(a.winner) != str(b.winner)
        for a, b in zip(r1, r2)
    )
    assert any_differ, "All 20 games identical with different seeds — RNG not working"


@skip_no_single_model
@pytest.mark.slow
def test_symmetry_same_model(ts):
    """Same model vs itself → WR near 50% (within ±15%, ~4-sigma tolerance)."""
    if not _has_bmvmb(ts):
        pytest.skip("benchmark_model_vs_model_batched not available")
    n_games = 200
    results = ts.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_A, n_games=n_games, pool_size=32, seed=50000,
        temperature=0.0, nash_temperatures=False,
    )
    a_wins = _model_a_wins(results, n_games // 2, ts)
    a_wr = a_wins / len(results)
    assert 0.35 <= a_wr <= 0.65, (
        f"Same-model WR={a_wr:.1%}, expected 35-65% (model may be degenerate)"
    )


@skip_no_models
@pytest.mark.slow
def test_side_assignment_valid_results(ts):
    """Both halves produce valid game results with correct side assignments."""
    if not _has_bmvmb(ts):
        pytest.skip("benchmark_model_vs_model_batched not available")
    n_games = 100
    results = ts.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_B, n_games=n_games, pool_size=32, seed=60000,
        temperature=0.0, nash_temperatures=False,
    )
    assert len(results) == n_games
    for r in results:
        assert r.winner in (ts.Side.USSR, ts.Side.US, None)

    half = n_games // 2
    a_wins = _model_a_wins(results, half, ts)
    print(f"\nSide assignment: Model A WR={a_wins}/{n_games}={a_wins/n_games:.1%}")
    print(f"  As USSR (games 0-{half-1}): "
          f"{sum(1 for r in results[:half] if r.winner == ts.Side.USSR)}/{half}")
    print(f"  As US (games {half}-{n_games-1}): "
          f"{sum(1 for r in results[half:] if r.winner == ts.Side.US)}/{half}")


# ---------------------------------------------------------------------------
# 2. Edge cases
# ---------------------------------------------------------------------------


@skip_no_single_model
def test_n_games_2_minimum_even(ts):
    """n_games=2 → 1 game each side."""
    if not _has_bmvmb(ts):
        pytest.skip("benchmark_model_vs_model_batched not available")
    results = ts.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_A, n_games=2, pool_size=2, seed=111,
        temperature=0.0, nash_temperatures=False,
    )
    assert len(results) == 2
    for r in results:
        assert r.winner in (ts.Side.USSR, ts.Side.US, None)


@skip_no_single_model
def test_n_games_1_returns_empty(ts):
    """n_games=1 → half=0, total=0 → empty (known rounding behavior)."""
    if not _has_bmvmb(ts):
        pytest.skip("benchmark_model_vs_model_batched not available")
    results = ts.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_A, n_games=1, pool_size=1, seed=222,
        temperature=0.0, nash_temperatures=False,
    )
    assert len(results) == 0


@skip_no_single_model
def test_n_games_0_returns_empty(ts):
    """n_games=0 → empty results."""
    if not _has_bmvmb(ts):
        pytest.skip("benchmark_model_vs_model_batched not available")
    results = ts.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_A, n_games=0, pool_size=1, seed=333,
        temperature=0.0, nash_temperatures=False,
    )
    assert len(results) == 0


@skip_no_single_model
def test_odd_n_games_rounds_down(ts):
    """n_games=7 → half=3, total=6 → 6 results."""
    if not _has_bmvmb(ts):
        pytest.skip("benchmark_model_vs_model_batched not available")
    results = ts.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_A, n_games=7, pool_size=4, seed=444,
        temperature=0.0, nash_temperatures=False,
    )
    assert len(results) == 6  # 7 // 2 * 2 = 6


@skip_no_single_model
def test_temperature_zero_deterministic(ts):
    """T=0 (greedy/argmax) is fully deterministic."""
    if not _has_bmvmb(ts):
        pytest.skip("benchmark_model_vs_model_batched not available")
    kwargs = dict(
        model_a_path=MODEL_A, model_b_path=MODEL_A,
        n_games=6, pool_size=4, seed=666,
        temperature=0.0, nash_temperatures=False,
    )
    r1 = ts.benchmark_model_vs_model_batched(**kwargs)
    r2 = ts.benchmark_model_vs_model_batched(**kwargs)
    for a, b in zip(r1, r2):
        assert a.final_vp == b.final_vp
        assert str(a.winner) == str(b.winner)


@skip_no_single_model
def test_temperature_nonzero_valid_results(ts):
    """T=1.0 produces valid results (stochastic — exact determinism not guaranteed
    due to pool-based execution ordering; game completion order affects RNG state).
    """
    if not _has_bmvmb(ts):
        pytest.skip("benchmark_model_vs_model_batched not available")
    results = ts.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_A, n_games=6, pool_size=4, seed=667,
        temperature=1.0, nash_temperatures=False,
    )
    assert len(results) == 6
    for r in results:
        assert r.winner in (ts.Side.USSR, ts.Side.US, None)


@skip_no_single_model
def test_pool_size_1_sequential(ts):
    """pool_size=1 forces sequential processing — must still work."""
    if not _has_bmvmb(ts):
        pytest.skip("benchmark_model_vs_model_batched not available")
    results = ts.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_A, n_games=4, pool_size=1, seed=888,
        temperature=0.0, nash_temperatures=False,
    )
    assert len(results) == 4


@skip_no_single_model
def test_pool_size_larger_than_n_games(ts):
    """pool_size=64 with n_games=4 — most slots unused but must work."""
    if not _has_bmvmb(ts):
        pytest.skip("benchmark_model_vs_model_batched not available")
    results = ts.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_A, n_games=4, pool_size=64, seed=999,
        temperature=0.0, nash_temperatures=False,
    )
    assert len(results) == 4


# ---------------------------------------------------------------------------
# 3. Statistical validity (slow)
# ---------------------------------------------------------------------------


@skip_no_single_model
@pytest.mark.slow
def test_statistical_confidence_interval(ts):
    """Same-model WR stays within expected binomial CI.

    200 games, p=0.5. 99.9% CI = [0.384, 0.616]. Use [0.30, 0.70] for safety.
    """
    if not _has_bmvmb(ts):
        pytest.skip("benchmark_model_vs_model_batched not available")
    n_games = 200
    results = ts.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_A, n_games=n_games, pool_size=32, seed=90000,
        temperature=0.0, nash_temperatures=False,
    )
    half = n_games // 2
    a_wins = _model_a_wins(results, half, ts)
    a_wr = a_wins / len(results)
    # 99.9% CI for p=0.5, n=200 is [0.384, 0.616]; using wider [0.30, 0.70]
    assert 0.30 <= a_wr <= 0.70, (
        f"WR={a_wr:.1%} far outside expected CI — possible side assignment bug"
    )
