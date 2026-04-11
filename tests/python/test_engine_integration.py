"""Integration tests for C++ engine via Python bindings.

These tests exercise complete game paths through the C++ engine, catching
regressions like DEFCON-1 rate anomalies, card bug regressions, and
determinism violations. They are meant to run fast (few games) but catch
real issues that unit tests miss.

Covers:
  - Deterministic replay: same seed → same results
  - Random game completion: 100 games finish without crash
  - DEFCON-1 rate sanity: not 100% of games should end in DEFCON-1
  - VP distribution: games should produce varied VP outcomes
  - End reasons: all expected end reasons should appear in a large enough sample
  - Game length distribution: games shouldn't all end on turn 1
  - Model vs heuristic: model checkpoint (if available) wins more than random
"""

from __future__ import annotations

import importlib
import os
from collections import Counter
from pathlib import Path

import pytest

MODEL_PATH = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "checkpoints"
    / "scripted_for_elo"
    / "v45_scripted.pt"
)


@pytest.fixture(scope="module")
def ts():
    return importlib.import_module("tscore")


# ---------------------------------------------------------------------------
# Determinism
# ---------------------------------------------------------------------------


def test_random_game_deterministic(ts):
    """Same seed produces identical game result."""
    r1 = ts.play_random_game(seed=12345)
    r2 = ts.play_random_game(seed=12345)
    assert r1.final_vp == r2.final_vp
    assert r1.end_turn == r2.end_turn
    assert r1.end_reason == r2.end_reason
    assert str(r1.winner) == str(r2.winner)


def test_random_game_different_seeds_differ(ts):
    """Different seeds should (almost certainly) produce different results."""
    results = set()
    for seed in range(100, 110):
        r = ts.play_random_game(seed=seed)
        results.add((r.final_vp, r.end_turn, r.end_reason))
    # At least 5 distinct outcomes from 10 games
    assert len(results) >= 5, f"Only {len(results)} distinct outcomes from 10 different seeds"


# ---------------------------------------------------------------------------
# Game completion
# ---------------------------------------------------------------------------


def test_100_random_games_complete(ts):
    """100 random games should all complete without crashing."""
    results = []
    for seed in range(1000, 1100):
        r = ts.play_random_game(seed=seed)
        results.append(r)
        assert r.end_turn >= 1, f"Game ended on turn {r.end_turn} (seed={seed})"
        assert r.end_turn <= 10, f"Game ended on turn {r.end_turn} > 10 (seed={seed})"
        assert isinstance(r.final_vp, int)
        assert r.end_reason in ("defcon1", "turn_limit", "vp_threshold", "europe_control", "vp"), (
            f"Unknown end_reason: {r.end_reason} (seed={seed})"
        )
    assert len(results) == 100


# ---------------------------------------------------------------------------
# Statistical sanity
# ---------------------------------------------------------------------------


def test_defcon1_rate_bounded(ts):
    """DEFCON-1 rate in random games should be bounded — not 100%."""
    n = 200
    defcon1_count = 0
    for seed in range(2000, 2000 + n):
        r = ts.play_random_game(seed=seed)
        if r.end_reason == "defcon1":
            defcon1_count += 1
    rate = defcon1_count / n
    # Random play has high DEFCON-1 rate (~75%) because random players
    # coup battlegrounds without considering DEFCON. But not 100%.
    assert rate < 0.95, f"DEFCON-1 rate too high: {rate:.1%} ({defcon1_count}/{n})"
    # Should have at least some DEFCON-1 endings
    assert rate > 0.10, f"DEFCON-1 rate suspiciously low: {rate:.1%}"


def test_vp_distribution_has_variance(ts):
    """VP distribution across games should have reasonable variance."""
    vps = []
    for seed in range(3000, 3100):
        r = ts.play_random_game(seed=seed)
        vps.append(r.final_vp)
    mean_vp = sum(vps) / len(vps)
    variance = sum((v - mean_vp) ** 2 for v in vps) / len(vps)
    # VP should have meaningful variance (not all 0 or all same value)
    assert variance > 1.0, f"VP variance too low: {variance:.2f}"
    assert min(vps) != max(vps), "All games had same VP"


def test_turn_distribution_not_all_turn1(ts):
    """Games should not all end on turn 1 (would indicate a bug)."""
    turns = []
    for seed in range(4000, 4100):
        r = ts.play_random_game(seed=seed)
        turns.append(r.end_turn)
    mean_turn = sum(turns) / len(turns)
    assert mean_turn > 2.0, f"Mean turn {mean_turn:.1f} is too low — most games ending early"
    # Should have some late-game endings
    late_games = sum(1 for t in turns if t >= 8)
    assert late_games > 5, f"Only {late_games}/100 games reached turn 8+"


def test_end_reasons_diverse(ts):
    """Multiple end reasons should appear across 200 games."""
    reasons = Counter()
    for seed in range(5000, 5200):
        r = ts.play_random_game(seed=seed)
        reasons[r.end_reason] += 1
    # Should have at least 2 different end reasons
    assert len(reasons) >= 2, f"Only {len(reasons)} end reason(s): {dict(reasons)}"


def test_winner_distribution_both_sides_win(ts):
    """Both USSR and US should win some games."""
    ussr_wins = 0
    us_wins = 0
    for seed in range(6000, 6200):
        r = ts.play_random_game(seed=seed)
        if r.winner == ts.Side.USSR:
            ussr_wins += 1
        elif r.winner == ts.Side.US:
            us_wins += 1
    assert ussr_wins > 10, f"USSR won only {ussr_wins}/200 random games"
    assert us_wins > 10, f"US won only {us_wins}/200 random games"


# ---------------------------------------------------------------------------
# Matchup tests (requires model)
# ---------------------------------------------------------------------------


@pytest.mark.skipif(not os.path.exists(MODEL_PATH), reason="model checkpoint not found")
def test_model_vs_heuristic_not_zero_wins(ts):
    """Trained model should win at least some games vs heuristic."""
    if not hasattr(ts, "benchmark_batched"):
        pytest.skip("benchmark_batched not available")
    results = ts.benchmark_batched(
        str(MODEL_PATH), ts.Side.USSR, 10, pool_size=4, seed=50000
    )
    wins = sum(1 for r in results if r.winner == ts.Side.USSR)
    assert wins > 0, "Model won 0/10 games as USSR — possible regression"


@pytest.mark.skipif(not os.path.exists(MODEL_PATH), reason="model checkpoint not found")
def test_benchmark_batched_deterministic_extended(ts):
    """Benchmark with same seed produces bit-identical results across 10 games."""
    if not hasattr(ts, "benchmark_batched"):
        pytest.skip("benchmark_batched not available")
    r1 = ts.benchmark_batched(str(MODEL_PATH), ts.Side.USSR, 10, pool_size=4, seed=99999)
    r2 = ts.benchmark_batched(str(MODEL_PATH), ts.Side.USSR, 10, pool_size=4, seed=99999)
    for i, (a, b) in enumerate(zip(r1, r2)):
        assert a.final_vp == b.final_vp, f"Game {i}: VP mismatch {a.final_vp} vs {b.final_vp}"
        assert a.end_turn == b.end_turn, f"Game {i}: turn mismatch"
        assert a.end_reason == b.end_reason, f"Game {i}: reason mismatch"


# ---------------------------------------------------------------------------
# Specific card regression tests
# ---------------------------------------------------------------------------


def test_games_with_seed_range_no_crash(ts):
    """Run games across a wide seed range to catch rare card bugs."""
    # Use seeds that historically triggered edge cases
    seeds = list(range(10000, 10050)) + [42, 137, 271828, 314159]
    for seed in seeds:
        r = ts.play_random_game(seed=seed)
        assert r.end_turn >= 1
        assert r.end_turn <= 10


def test_matchup_hybrid_vs_hybrid_balanced(ts):
    """MinimalHybrid vs MinimalHybrid should be reasonably balanced."""
    results = ts.play_matchup(ts.PolicyKind.MinimalHybrid, ts.PolicyKind.MinimalHybrid, 50, seed=7777)
    ussr_wins = sum(1 for r in results if r.winner == ts.Side.USSR)
    us_wins = sum(1 for r in results if r.winner == ts.Side.US)
    # Neither side should win more than 80%
    assert ussr_wins < 40, f"USSR won {ussr_wins}/50 — hybrid imbalanced"
    assert us_wins < 40, f"US won {us_wins}/50 — hybrid imbalanced"
