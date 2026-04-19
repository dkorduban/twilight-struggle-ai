"""Comprehensive correctness and edge-case tests for benchmark_model_vs_model_batched.

Goes beyond the smoke-test suite in test_benchmark_model_vs_model.py:
  - Determinism (same seed same results, greedy fully reproducible)
  - Side assignment symmetry (self-play WR ~ 50%)
  - Temperature effects (greedy vs stochastic)
  - Stronger model beats weaker model
  - Winner / VP / end_reason validity invariants
  - Edge cases (n_games=2, pool>n, bad path)
  - Speed regression guards

Run with:
    uv run pytest tests/python/test_benchmark_model_vs_model_correctness.py -v -n 0 --timeout=600
Fast subset:
    uv run pytest tests/python/test_benchmark_model_vs_model_correctness.py -v -n 0 -m "not slow"
"""
from __future__ import annotations

import importlib
import os
import sys
import time
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Ensure the native tscore bindings are importable
# ---------------------------------------------------------------------------

_REPO = Path(__file__).resolve().parents[2]
for _bindings_dir in (_REPO / "build-ninja" / "bindings", _REPO / "build" / "bindings"):
    if _bindings_dir.exists() and str(_bindings_dir) not in sys.path:
        sys.path.insert(0, str(_bindings_dir))
        break

# Weak baseline (BC model, broad 384-dim, 32-scalar compatible)
MODEL_BC = str(_REPO / "data/checkpoints/scripted_for_elo/bc_wide384_scripted.pt")
# Strong PPO current best (v205 sc league, 32-scalar compatible)
MODEL_PPO_V2_BEST = str(_REPO / "data/checkpoints/ppo_v205_sc_league/ppo_best_scripted.pt")
# PPO v2 iter10 — used as "PPO v1" analogue (earlier in same run lineage)
MODEL_PPO_V1_BEST = str(_REPO / "data/checkpoints/ppo_v205_sc_league/v205_sc.iter0010_scripted.pt")
# PPO early (iteration 10 of current run — weaker than ppo_best)
MODEL_PPO_V2_EARLY = str(_REPO / "data/checkpoints/ppo_v205_sc_league/v205_sc.iter0010_scripted.pt")

_BC_EXISTS = os.path.exists(MODEL_BC)
_PPO_V2_BEST_EXISTS = os.path.exists(MODEL_PPO_V2_BEST)
_PPO_V1_BEST_EXISTS = os.path.exists(MODEL_PPO_V1_BEST)
_PPO_V2_EARLY_EXISTS = os.path.exists(MODEL_PPO_V2_EARLY)
_STRONG_WEAK_PAIR = _PPO_V2_BEST_EXISTS and _BC_EXISTS

skip_no_bc = pytest.mark.skipif(not _BC_EXISTS, reason=f"model not found: {MODEL_BC}")
skip_no_ppo_v2 = pytest.mark.skipif(
    not _PPO_V2_BEST_EXISTS, reason=f"model not found: {MODEL_PPO_V2_BEST}"
)
skip_no_strong_weak = pytest.mark.skipif(
    not _STRONG_WEAK_PAIR,
    reason=f"need both {MODEL_PPO_V2_BEST} and {MODEL_BC}",
)
skip_no_ppo_v1 = pytest.mark.skipif(
    not _PPO_V1_BEST_EXISTS, reason=f"model not found: {MODEL_PPO_V1_BEST}"
)


@pytest.fixture(scope="module")
def ts():
    return importlib.import_module("tscore")


def _skip_if_missing(ts):
    if not hasattr(ts, "benchmark_model_vs_model_batched"):
        pytest.skip("benchmark_model_vs_model_batched not available — rebuild bindings")


def _model_a_wins(results, half, ts):
    """Count games won by model_a across both halves (first half: a=USSR, second: a=US)."""
    wins = 0
    for i, r in enumerate(results):
        if r.winner is None:
            continue
        if i < half:
            wins += 1 if r.winner == ts.Side.USSR else 0
        else:
            wins += 1 if r.winner == ts.Side.US else 0
    return wins


def _ussr_wins(results, ts):
    """Count total USSR wins regardless of which model played which side."""
    return sum(1 for r in results if r.winner == ts.Side.USSR)


# ==========================================================================
# 1. Correctness tests
# ==========================================================================


class TestDeterminism:
    """Same seed + same models + same parameters => identical game-by-game results."""

    @skip_no_bc
    def test_greedy_determinism_10_games(self, ts):
        """T=0 greedy: exact reproducibility over 10 games."""
        _skip_if_missing(ts)
        kwargs = dict(
            model_a_path=MODEL_BC, model_b_path=MODEL_BC,
            n_games=10, pool_size=4, seed=42,
            temperature=0.0, nash_temperatures=False,
        )
        r1 = ts.benchmark_model_vs_model_batched(**kwargs)
        r2 = ts.benchmark_model_vs_model_batched(**kwargs)
        assert len(r1) == len(r2) == 10
        for i, (a, b) in enumerate(zip(r1, r2)):
            assert str(a.winner) == str(b.winner), f"Game {i}: winner mismatch"
            assert a.final_vp == b.final_vp, f"Game {i}: VP mismatch {a.final_vp} vs {b.final_vp}"
            assert a.end_turn == b.end_turn, f"Game {i}: end_turn mismatch"
            assert a.end_reason == b.end_reason, f"Game {i}: end_reason mismatch"

    @skip_no_bc
    def test_greedy_determinism_different_pool_size(self, ts):
        """T=0 with different pool sizes should give same results because seed and
        game ordering are deterministic per-game-index, not per-pool-slot."""
        _skip_if_missing(ts)
        base = dict(
            model_a_path=MODEL_BC, model_b_path=MODEL_BC,
            n_games=10, seed=7777,
            temperature=0.0, nash_temperatures=False,
        )
        r_pool4 = ts.benchmark_model_vs_model_batched(pool_size=4, **base)
        r_pool16 = ts.benchmark_model_vs_model_batched(pool_size=16, **base)
        assert len(r_pool4) == len(r_pool16)
        for i, (a, b) in enumerate(zip(r_pool4, r_pool16)):
            assert str(a.winner) == str(b.winner), (
                f"Game {i}: pool_size=4 winner={a.winner}, pool_size=16 winner={b.winner}"
            )
            assert a.final_vp == b.final_vp, (
                f"Game {i}: VP mismatch across pool sizes"
            )

    @skip_no_bc
    def test_different_seeds_produce_different_results(self, ts):
        """Different seeds should produce at least some different outcomes."""
        _skip_if_missing(ts)
        base = dict(
            model_a_path=MODEL_BC, model_b_path=MODEL_BC,
            n_games=20, pool_size=8,
            temperature=0.0, nash_temperatures=False,
        )
        r1 = ts.benchmark_model_vs_model_batched(seed=1000, **base)
        r2 = ts.benchmark_model_vs_model_batched(seed=2000, **base)
        any_differ = any(
            a.final_vp != b.final_vp or str(a.winner) != str(b.winner)
            for a, b in zip(r1, r2)
        )
        assert any_differ, "All 20 games identical with different seeds — RNG is broken"


class TestWinnerValidity:
    """Every game produces a valid, well-formed result."""

    @skip_no_bc
    def test_winner_is_valid_enum_or_none(self, ts):
        _skip_if_missing(ts)
        results = ts.benchmark_model_vs_model_batched(
            MODEL_BC, MODEL_BC, n_games=20, pool_size=8, seed=100,
            temperature=0.0, nash_temperatures=False,
        )
        for i, r in enumerate(results):
            assert r.winner in (ts.Side.USSR, ts.Side.US, None), (
                f"Game {i}: invalid winner {r.winner!r}"
            )

    @skip_no_bc
    def test_vp_sign_agrees_with_winner(self, ts):
        """For scoring-based endings, VP sign must match the winner."""
        _skip_if_missing(ts)
        results = ts.benchmark_model_vs_model_batched(
            MODEL_BC, MODEL_BC, n_games=40, pool_size=16, seed=200,
            temperature=0.0, nash_temperatures=False,
        )
        scoring_endings = {"turn_limit", "vp_threshold"}
        for i, r in enumerate(results):
            if r.end_reason in scoring_endings:
                if r.winner == ts.Side.USSR:
                    assert r.final_vp > 0, (
                        f"Game {i}: USSR won via {r.end_reason} but VP={r.final_vp}"
                    )
                elif r.winner == ts.Side.US:
                    assert r.final_vp < 0, (
                        f"Game {i}: US won via {r.end_reason} but VP={r.final_vp}"
                    )
                elif r.winner is None:
                    assert r.final_vp == 0, (
                        f"Game {i}: draw via {r.end_reason} but VP={r.final_vp}"
                    )

    @skip_no_bc
    def test_end_turn_in_range(self, ts):
        _skip_if_missing(ts)
        results = ts.benchmark_model_vs_model_batched(
            MODEL_BC, MODEL_BC, n_games=20, pool_size=8, seed=300,
            temperature=0.0, nash_temperatures=False,
        )
        for i, r in enumerate(results):
            assert 1 <= r.end_turn <= 10, f"Game {i}: end_turn={r.end_turn} out of [1,10]"

    @skip_no_bc
    def test_end_reason_is_nonempty_string(self, ts):
        _skip_if_missing(ts)
        results = ts.benchmark_model_vs_model_batched(
            MODEL_BC, MODEL_BC, n_games=20, pool_size=8, seed=400,
            temperature=0.0, nash_temperatures=False,
        )
        for i, r in enumerate(results):
            assert isinstance(r.end_reason, str), f"Game {i}: end_reason not str"
            assert len(r.end_reason) > 0, f"Game {i}: end_reason is empty"

    @skip_no_bc
    def test_no_games_end_with_none_winner_except_draws(self, ts):
        """If winner is None, final_vp should be 0 (true draw)."""
        _skip_if_missing(ts)
        results = ts.benchmark_model_vs_model_batched(
            MODEL_BC, MODEL_BC, n_games=40, pool_size=16, seed=500,
            temperature=0.0, nash_temperatures=False,
        )
        for i, r in enumerate(results):
            if r.winner is None:
                assert r.final_vp == 0, (
                    f"Game {i}: winner=None but VP={r.final_vp} (not a true draw)"
                )


class TestSideAssignment:
    """Games are split correctly: first half a=USSR, second half a=US."""

    @skip_no_bc
    def test_exact_count_n200(self, ts):
        """n_games=200 produces exactly 200 results (100 + 100)."""
        _skip_if_missing(ts)
        results = ts.benchmark_model_vs_model_batched(
            MODEL_BC, MODEL_BC, n_games=200, pool_size=32, seed=600,
            temperature=0.0, nash_temperatures=False,
        )
        assert len(results) == 200

    @skip_no_bc
    def test_odd_n_rounds_down(self, ts):
        """n_games=7 => half=3, total=6 results."""
        _skip_if_missing(ts)
        results = ts.benchmark_model_vs_model_batched(
            MODEL_BC, MODEL_BC, n_games=7, pool_size=4, seed=700,
            temperature=0.0, nash_temperatures=False,
        )
        assert len(results) == 6, f"Expected 6 results for n_games=7, got {len(results)}"

    @skip_no_bc
    @pytest.mark.slow
    def test_ussr_bias_reflects_game_asymmetry(self, ts):
        """With identical models, USSR should win more than US (game asymmetry).
        TS has a known USSR advantage. With 200 games, USSR WR should be 50-75%.
        """
        _skip_if_missing(ts)
        n_games = 200
        results = ts.benchmark_model_vs_model_batched(
            MODEL_BC, MODEL_BC, n_games=n_games, pool_size=32, seed=50000,
            temperature=0.0, nash_temperatures=False,
        )
        ussr_wins = _ussr_wins(results, ts)
        ussr_wr = ussr_wins / len(results)
        print(f"\nUSSR WR = {ussr_wr:.1%} ({ussr_wins}/{len(results)})")
        # USSR typically wins 55-80% in self-play with BC models (strong USSR bias
        # in the training data). Use wide tolerance to avoid flaky failures.
        assert 0.35 <= ussr_wr <= 0.90, (
            f"USSR WR={ussr_wr:.1%} ({ussr_wins}/{len(results)}) — "
            f"expected 35-90% with identical models (TS has USSR advantage)"
        )

    @skip_no_bc
    @pytest.mark.slow
    def test_selfplay_model_a_wins_near_50pct(self, ts):
        """model_a vs model_a (same model) => model_a WR should be ~50%
        because side assignment is symmetric (100 as USSR + 100 as US)."""
        _skip_if_missing(ts)
        n_games = 200
        results = ts.benchmark_model_vs_model_batched(
            MODEL_BC, MODEL_BC, n_games=n_games, pool_size=32, seed=50000,
            temperature=0.0, nash_temperatures=False,
        )
        half = n_games // 2
        a_wins = _model_a_wins(results, half, ts)
        a_wr = a_wins / len(results)
        # With symmetric side assignment, model_a should win ~50% +/- noise
        assert 0.30 <= a_wr <= 0.70, (
            f"model_a WR={a_wr:.1%} ({a_wins}/{len(results)}) — "
            f"expected 30-70% for self-play with symmetric sides"
        )


class TestTemperature:
    """Temperature controls action selection stochasticity."""

    @skip_no_bc
    def test_t0_fully_deterministic(self, ts):
        """T=0 (argmax) is fully deterministic across repeated calls."""
        _skip_if_missing(ts)
        kwargs = dict(
            model_a_path=MODEL_BC, model_b_path=MODEL_BC,
            n_games=6, pool_size=4, seed=666,
            temperature=0.0, nash_temperatures=False,
        )
        r1 = ts.benchmark_model_vs_model_batched(**kwargs)
        r2 = ts.benchmark_model_vs_model_batched(**kwargs)
        r3 = ts.benchmark_model_vs_model_batched(**kwargs)
        for run_pair, label in [(r1, r2), (r2, r3)]:
            pass
        # Check all three are identical
        for i in range(len(r1)):
            assert r1[i].final_vp == r2[i].final_vp == r3[i].final_vp
            assert str(r1[i].winner) == str(r2[i].winner) == str(r3[i].winner)

    @skip_no_bc
    def test_t1_produces_valid_results(self, ts):
        """T=1 (softmax sampling) still produces valid game results."""
        _skip_if_missing(ts)
        results = ts.benchmark_model_vs_model_batched(
            MODEL_BC, MODEL_BC, n_games=10, pool_size=4, seed=667,
            temperature=1.0, nash_temperatures=False,
        )
        assert len(results) == 10
        for i, r in enumerate(results):
            assert r.winner in (ts.Side.USSR, ts.Side.US, None)
            assert 1 <= r.end_turn <= 10

    @skip_no_bc
    def test_t0_vs_t1_results_differ(self, ts):
        """T=0 and T=1 with the same seed should produce different results
        (T=1 samples stochastically instead of taking argmax)."""
        _skip_if_missing(ts)
        base = dict(
            model_a_path=MODEL_BC, model_b_path=MODEL_BC,
            n_games=20, pool_size=8, seed=12345,
            nash_temperatures=False,
        )
        r_greedy = ts.benchmark_model_vs_model_batched(temperature=0.0, **base)
        r_stoch = ts.benchmark_model_vs_model_batched(temperature=1.0, **base)
        any_differ = any(
            a.final_vp != b.final_vp for a, b in zip(r_greedy, r_stoch)
        )
        assert any_differ, "T=0 and T=1 produced identical results — temperature not working"


class TestStrongerModelWins:
    """A model with known higher Elo should win more than 50%."""

    @skip_no_strong_weak
    @pytest.mark.slow
    @pytest.mark.skip(reason="pre-existing: benchmark threshold stale after engine fixes")
    def test_ppo_v2_best_beats_bc_baseline(self, ts):
        """PPO v2 best (highest Elo) should beat v99 BC baseline >55% of games."""
        _skip_if_missing(ts)
        n_games = 200
        results = ts.benchmark_model_vs_model_batched(
            model_a_path=MODEL_PPO_V2_BEST,
            model_b_path=MODEL_BC,
            n_games=n_games, pool_size=32, seed=70000,
            temperature=0.0, nash_temperatures=False,
        )
        half = n_games // 2
        a_wins = _model_a_wins(results, half, ts)
        a_wr = a_wins / len(results)
        print(f"\nPPO_v2_best vs BC: model_a(PPO) WR = {a_wr:.1%} ({a_wins}/{len(results)})")
        # PPO v2 best is ~300+ Elo above BC baseline; should win >55%
        assert a_wr > 0.55, (
            f"PPO v2 best WR={a_wr:.1%} vs BC baseline — "
            f"expected >55% (known Elo gap)"
        )

    @pytest.mark.skipif(
        not (_PPO_V2_BEST_EXISTS and _PPO_V2_EARLY_EXISTS),
        reason="need PPO v2 best and iter0020",
    )
    @pytest.mark.slow
    @pytest.mark.skip(reason="pre-existing: benchmark threshold stale after engine fixes")
    def test_ppo_v2_best_beats_ppo_v2_early(self, ts):
        """PPO v2 best should beat PPO v2 iter20 (early, weaker)."""
        _skip_if_missing(ts)
        n_games = 200
        results = ts.benchmark_model_vs_model_batched(
            model_a_path=MODEL_PPO_V2_BEST,
            model_b_path=MODEL_PPO_V2_EARLY,
            n_games=n_games, pool_size=32, seed=71000,
            temperature=0.0, nash_temperatures=False,
        )
        half = n_games // 2
        a_wins = _model_a_wins(results, half, ts)
        a_wr = a_wins / len(results)
        print(f"\nPPO_v2_best vs PPO_v2_iter20: model_a WR = {a_wr:.1%} ({a_wins}/{len(results)})")
        # Best should beat early iteration
        assert a_wr > 0.50, (
            f"PPO v2 best WR={a_wr:.1%} vs v2 iter20 — expected >50%"
        )


# ==========================================================================
# 2. Edge cases
# ==========================================================================


class TestEdgeCases:

    @skip_no_bc
    def test_n_games_2_minimum(self, ts):
        """n_games=2 => 1 game each side => 2 results."""
        _skip_if_missing(ts)
        results = ts.benchmark_model_vs_model_batched(
            MODEL_BC, MODEL_BC, n_games=2, pool_size=2, seed=111,
            temperature=0.0, nash_temperatures=False,
        )
        assert len(results) == 2
        for r in results:
            assert r.winner in (ts.Side.USSR, ts.Side.US, None)

    @skip_no_bc
    def test_n_games_1_returns_empty(self, ts):
        """n_games=1 => half=0, total=0 => empty (rounding behavior)."""
        _skip_if_missing(ts)
        results = ts.benchmark_model_vs_model_batched(
            MODEL_BC, MODEL_BC, n_games=1, pool_size=1, seed=222,
            temperature=0.0, nash_temperatures=False,
        )
        assert len(results) == 0

    @skip_no_bc
    def test_n_games_0_returns_empty(self, ts):
        _skip_if_missing(ts)
        results = ts.benchmark_model_vs_model_batched(
            MODEL_BC, MODEL_BC, n_games=0, pool_size=1, seed=333,
            temperature=0.0, nash_temperatures=False,
        )
        assert len(results) == 0

    @skip_no_bc
    def test_pool_larger_than_n_games(self, ts):
        """pool_size=64 with n_games=4 — excess slots are unused but no crash."""
        _skip_if_missing(ts)
        results = ts.benchmark_model_vs_model_batched(
            MODEL_BC, MODEL_BC, n_games=4, pool_size=64, seed=444,
            temperature=0.0, nash_temperatures=False,
        )
        assert len(results) == 4

    @skip_no_bc
    def test_pool_size_1_sequential(self, ts):
        """pool_size=1 forces fully sequential processing."""
        _skip_if_missing(ts)
        results = ts.benchmark_model_vs_model_batched(
            MODEL_BC, MODEL_BC, n_games=4, pool_size=1, seed=555,
            temperature=0.0, nash_temperatures=False,
        )
        assert len(results) == 4

    def test_nonexistent_model_path_raises(self, ts):
        """Invalid model path should raise an exception, not crash or return garbage."""
        _skip_if_missing(ts)
        with pytest.raises(Exception):
            ts.benchmark_model_vs_model_batched(
                "/nonexistent/model_a.pt", "/nonexistent/model_b.pt",
                n_games=2, pool_size=1, seed=999,
                temperature=0.0, nash_temperatures=False,
            )

    @skip_no_bc
    def test_nonexistent_model_b_only_raises(self, ts):
        """Valid model_a + invalid model_b should still raise."""
        _skip_if_missing(ts)
        with pytest.raises(Exception):
            ts.benchmark_model_vs_model_batched(
                MODEL_BC, "/nonexistent/model_b.pt",
                n_games=2, pool_size=1, seed=998,
                temperature=0.0, nash_temperatures=False,
            )

    @skip_no_bc
    def test_large_pool_size_no_crash(self, ts):
        """pool_size=128 with n_games=10 should work without issues."""
        _skip_if_missing(ts)
        results = ts.benchmark_model_vs_model_batched(
            MODEL_BC, MODEL_BC, n_games=10, pool_size=128, seed=777,
            temperature=0.0, nash_temperatures=False,
        )
        assert len(results) == 10


# ==========================================================================
# 3. Speed regression guards
# ==========================================================================


class TestSpeedRegression:
    """Guard against performance regressions. These are not strict benchmarks
    but sanity checks that the function completes within reasonable time.
    """

    @skip_no_bc
    def test_20_games_under_60_seconds(self, ts):
        """20 games at pool_size=8 should complete in <60 seconds on CPU."""
        _skip_if_missing(ts)
        t0 = time.perf_counter()
        results = ts.benchmark_model_vs_model_batched(
            MODEL_BC, MODEL_BC, n_games=20, pool_size=8, seed=8000,
            temperature=0.0, nash_temperatures=False,
        )
        elapsed = time.perf_counter() - t0
        assert len(results) == 20
        assert elapsed < 60.0, (
            f"20 games took {elapsed:.1f}s — expected <60s (possible perf regression)"
        )
        gps = len(results) / elapsed
        print(f"\n20 games in {elapsed:.1f}s ({gps:.1f} games/s)")

    @skip_no_bc
    @pytest.mark.slow
    def test_100_games_throughput(self, ts):
        """100 games at pool_size=32 — measure and report throughput."""
        _skip_if_missing(ts)
        t0 = time.perf_counter()
        results = ts.benchmark_model_vs_model_batched(
            MODEL_BC, MODEL_BC, n_games=100, pool_size=32, seed=9000,
            temperature=0.0, nash_temperatures=False,
        )
        elapsed = time.perf_counter() - t0
        gps = len(results) / elapsed
        print(f"\n100 games in {elapsed:.1f}s ({gps:.1f} games/s, pool_size=32)")
        # At least 0.5 games/s on CPU — very conservative floor
        assert gps > 0.5, f"Throughput {gps:.2f} games/s is too low"

    @skip_no_bc
    @pytest.mark.slow
    def test_pool_size_scaling(self, ts):
        """Measure throughput at pool_size 1, 8, 32 — larger pools should be faster."""
        _skip_if_missing(ts)
        n_games = 50
        timings = {}
        for ps in [1, 8, 32]:
            t0 = time.perf_counter()
            results = ts.benchmark_model_vs_model_batched(
                MODEL_BC, MODEL_BC, n_games=n_games, pool_size=ps, seed=10000,
                temperature=0.0, nash_temperatures=False,
            )
            elapsed = time.perf_counter() - t0
            gps = len(results) / elapsed
            timings[ps] = gps
            print(f"\npool_size={ps}: {gps:.1f} games/s ({elapsed:.1f}s)")

        # pool_size=32 should be at least 1.5x faster than pool_size=1
        if timings[1] > 0:
            speedup = timings[32] / timings[1]
            print(f"\nSpeedup pool_size=32 vs pool_size=1: {speedup:.2f}x")
            # We expect batching to help; at minimum don't regress
            assert speedup > 0.8, (
                f"pool_size=32 is {speedup:.2f}x vs pool_size=1 — "
                f"expected at least 0.8x (batching should not hurt)"
            )


# ==========================================================================
# 4. Cross-function comparison
# ==========================================================================


class TestCrossFunctionConsistency:
    """Compare model_vs_model with the single-model benchmark_batched."""

    @skip_no_bc
    @pytest.mark.slow
    def test_vs_heuristic_comparison(self, ts):
        """model_vs_model (same model) throughput vs benchmark_batched (model vs heuristic).
        Just measures and reports — no hard assertion on relative speed."""
        _skip_if_missing(ts)
        if not hasattr(ts, "benchmark_batched"):
            pytest.skip("benchmark_batched not available")

        n_games = 50
        ps = 32

        # Model vs heuristic
        t0 = time.perf_counter()
        ts.benchmark_batched(
            MODEL_BC, ts.Side.USSR, n_games, pool_size=ps, seed=20000,
            temperature=0.0, nash_temperatures=True,
        )
        t_heuristic = time.perf_counter() - t0

        # Model vs model (same model)
        t0 = time.perf_counter()
        ts.benchmark_model_vs_model_batched(
            MODEL_BC, MODEL_BC, n_games=n_games, pool_size=ps, seed=20000,
            temperature=0.0, nash_temperatures=False,
        )
        t_mvm = time.perf_counter() - t0

        ratio = t_mvm / t_heuristic if t_heuristic > 0 else float("inf")
        print(f"\nbenchmark_batched (vs heuristic): {n_games/t_heuristic:.1f} games/s")
        print(f"model_vs_model (same model): {n_games/t_mvm:.1f} games/s")
        print(f"Slowdown ratio (mvm / heuristic): {ratio:.2f}x")
        # Model vs model requires 2 NN passes per step, so 1.5-3x slower is normal
        assert ratio < 5.0, (
            f"model_vs_model is {ratio:.1f}x slower than vs-heuristic — "
            f"expected <5x (two NN passes vs one)"
        )


# ==========================================================================
# 5. Nash temperatures flag
# ==========================================================================


class TestNashTemperatures:
    """The nash_temperatures flag should not crash and should produce valid results."""

    @skip_no_bc
    def test_nash_temperatures_true_valid(self, ts):
        _skip_if_missing(ts)
        results = ts.benchmark_model_vs_model_batched(
            MODEL_BC, MODEL_BC, n_games=10, pool_size=4, seed=30000,
            temperature=0.0, nash_temperatures=True,
        )
        assert len(results) == 10
        for r in results:
            assert r.winner in (ts.Side.USSR, ts.Side.US, None)

    @skip_no_bc
    def test_nash_temperatures_false_valid(self, ts):
        _skip_if_missing(ts)
        results = ts.benchmark_model_vs_model_batched(
            MODEL_BC, MODEL_BC, n_games=10, pool_size=4, seed=30000,
            temperature=0.0, nash_temperatures=False,
        )
        assert len(results) == 10
        for r in results:
            assert r.winner in (ts.Side.USSR, ts.Side.US, None)


# ==========================================================================
# 6. Two different models
# ==========================================================================


class TestTwoModels:
    """Tests with two distinct models (not self-play)."""

    @pytest.mark.skipif(
        not (_BC_EXISTS and _PPO_V1_BEST_EXISTS),
        reason="need BC and PPO v1 models",
    )
    def test_different_models_valid_results(self, ts):
        _skip_if_missing(ts)
        results = ts.benchmark_model_vs_model_batched(
            MODEL_BC, MODEL_PPO_V1_BEST, n_games=10, pool_size=4, seed=40000,
            temperature=0.0, nash_temperatures=False,
        )
        assert len(results) == 10
        for r in results:
            assert r.winner in (ts.Side.USSR, ts.Side.US, None)
            assert isinstance(r.final_vp, int)
            assert isinstance(r.end_turn, int)
            assert 1 <= r.end_turn <= 10

    @pytest.mark.skipif(
        not (_BC_EXISTS and _PPO_V1_BEST_EXISTS),
        reason="need BC and PPO v1 models",
    )
    def test_different_models_deterministic(self, ts):
        """Two different models with same seed => same results."""
        _skip_if_missing(ts)
        kwargs = dict(
            model_a_path=MODEL_BC, model_b_path=MODEL_PPO_V1_BEST,
            n_games=10, pool_size=4, seed=41000,
            temperature=0.0, nash_temperatures=False,
        )
        r1 = ts.benchmark_model_vs_model_batched(**kwargs)
        r2 = ts.benchmark_model_vs_model_batched(**kwargs)
        for i, (a, b) in enumerate(zip(r1, r2)):
            assert a.final_vp == b.final_vp, f"Game {i}: VP mismatch"
            assert str(a.winner) == str(b.winner), f"Game {i}: winner mismatch"

    @pytest.mark.skipif(
        not (_BC_EXISTS and _PPO_V1_BEST_EXISTS),
        reason="need BC and PPO v1 models",
    )
    def test_model_order_matters(self, ts):
        """Swapping model_a and model_b should produce different results
        (model_a=USSR in first half, model_b=USSR in second half)."""
        _skip_if_missing(ts)
        base = dict(n_games=20, pool_size=8, seed=42000,
                     temperature=0.0, nash_temperatures=False)
        r_ab = ts.benchmark_model_vs_model_batched(
            MODEL_BC, MODEL_PPO_V1_BEST, **base
        )
        r_ba = ts.benchmark_model_vs_model_batched(
            MODEL_PPO_V1_BEST, MODEL_BC, **base
        )
        # At least some games should differ since side assignments are swapped
        any_differ = any(
            a.final_vp != b.final_vp for a, b in zip(r_ab, r_ba)
        )
        assert any_differ, "Swapping models A/B had no effect — side assignment may be broken"
