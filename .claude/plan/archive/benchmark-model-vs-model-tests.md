## Comprehensive Test Plan for `benchmark_model_vs_model_batched`

### Overview

This plan covers correctness, edge cases, performance, and statistical validity for the `benchmark_model_vs_model_batched` function. All tests use the Python `tscore` binding unless stated otherwise. Tests belong in `/home/dkord/code/twilight-struggle-ai/tests/python/test_benchmark_model_vs_model.py`.

**Key implementation details from source review:**
- `n_games` is rounded down to even: `half = n_games / 2; total = half * 2` (C++ integer division)
- For `n_games=1`, `half=0, total=0` -- returns empty vector
- For `n_games=0`, returns empty vector (early return)
- Game index `[0, half)` assigns model_a=USSR; `[half, total)` assigns model_a=US
- Seeds are per-game: `seed = base_seed + game_index`
- VP convention: positive VP = USSR wins, negative VP = US wins, zero = draw
- `GameResult` has: `winner` (Side.USSR, Side.US, or None), `final_vp` (int), `end_turn` (int), `end_reason` (str)

**Model paths for tests** (both confirmed to exist on disk):
- `MODEL_A = "data/checkpoints/v99_nash_c_95ep_s42/baseline_best_scripted.pt"` (same as existing test_bindings.py)
- `MODEL_B = "data/checkpoints/ppo_v1_from_v106/ppo_iter0080_scripted.pt"` (different model for asymmetric tests)

**Run command:**
```bash
cd /home/dkord/code/twilight-struggle-ai
uv run pytest tests/python/test_benchmark_model_vs_model.py -v -n 0 --timeout=600
```
Use `-n 0` (no parallelism) for determinism and performance measurement tests. For the full suite including slow tests:
```bash
uv run pytest tests/python/test_benchmark_model_vs_model.py -v -n 0 --timeout=1200 -m "not slow"
```

---

### File structure

Create: `/home/dkord/code/twilight-struggle-ai/tests/python/test_benchmark_model_vs_model.py`

```python
"""Tests for benchmark_model_vs_model_batched."""

from __future__ import annotations

import importlib
import math
import os
import time
from pathlib import Path

import pytest

# Model paths relative to repo root
_REPO = Path(__file__).resolve().parents[2]
MODEL_A = str(_REPO / "data/checkpoints/v99_nash_c_95ep_s42/baseline_best_scripted.pt")
MODEL_B = str(_REPO / "data/checkpoints/ppo_v1_from_v106/ppo_iter0080_scripted.pt")

_MODELS_EXIST = os.path.exists(MODEL_A) and os.path.exists(MODEL_B)
_SINGLE_MODEL_EXISTS = os.path.exists(MODEL_A)

skip_no_models = pytest.mark.skipif(not _MODELS_EXIST, reason="model checkpoints not found")
skip_no_single_model = pytest.mark.skipif(not _SINGLE_MODEL_EXISTS, reason="model A not found")


@pytest.fixture(scope="module")
def ts():
    return importlib.import_module("tscore")
```

---

### 1. Correctness Tests

#### 1.1 Result count test
```python
@skip_no_single_model
def test_result_count_even(ts):
    """n_games=10 returns exactly 10 results (10 is even, half*2 == 10)."""
    results = ts.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_A, n_games=10, pool_size=4, seed=42,
        temperature=0.0, nash_temperatures=False,
    )
    assert len(results) == 10
```

**Location:** `tests/python/test_benchmark_model_vs_model.py`
**Assertion:** `len(results) == 10`

#### 1.2 Winner correctness and VP sign agreement
```python
@skip_no_single_model
def test_winner_and_vp_consistency(ts):
    """Every result has valid winner and VP sign matches winner."""
    results = ts.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_A, n_games=20, pool_size=8, seed=100,
        temperature=0.0, nash_temperatures=False,
    )
    for i, r in enumerate(results):
        assert r.winner in (ts.Side.USSR, ts.Side.US, None), (
            f"Game {i}: invalid winner {r.winner}"
        )
        assert isinstance(r.final_vp, int)
        assert isinstance(r.end_turn, int)
        assert isinstance(r.end_reason, str)
        assert 1 <= r.end_turn <= 10

        if r.winner == ts.Side.USSR:
            assert r.final_vp > 0 or r.end_reason in ("defcon1", "europe_control", "asia_control", "scoring_card_held"), (
                f"Game {i}: USSR won but final_vp={r.final_vp}, reason={r.end_reason}"
            )
        elif r.winner == ts.Side.US:
            assert r.final_vp < 0 or r.end_reason in ("defcon1", "europe_control", "asia_control", "scoring_card_held"), (
                f"Game {i}: US won but final_vp={r.final_vp}, reason={r.end_reason}"
            )
        elif r.winner is None:
            assert r.final_vp == 0, f"Game {i}: draw but final_vp={r.final_vp}"
```

**Note on VP/winner**: For `defcon1` and `europe_control` end reasons, the winner is determined by who *triggered* the condition, not by VP sign. The test allows these exceptions. For `turn_limit` and `vp_threshold`, VP sign must match winner.

#### 1.3 Determinism test
```python
@skip_no_single_model
def test_determinism_same_seed(ts):
    """Same seed produces identical results across two runs."""
    kwargs = dict(
        model_a_path=MODEL_A, model_b_path=MODEL_A,
        n_games=10, pool_size=4, seed=777,
        temperature=0.0, nash_temperatures=False,
    )
    r1 = ts.benchmark_model_vs_model_batched(**kwargs)
    r2 = ts.benchmark_model_vs_model_batched(**kwargs)

    assert len(r1) == len(r2)
    for i, (a, b) in enumerate(zip(r1, r2)):
        assert str(a.winner) == str(b.winner), f"Game {i}: winner mismatch"
        assert a.final_vp == b.final_vp, f"Game {i}: VP mismatch"
        assert a.end_turn == b.end_turn, f"Game {i}: end_turn mismatch"
        assert a.end_reason == b.end_reason, f"Game {i}: end_reason mismatch"
```

**Assertion:** Bitwise-identical results for same (model, seed, pool_size, temperature, n_games).

#### 1.4 Independence test (different seeds differ)
```python
@skip_no_single_model
def test_different_seeds_differ(ts):
    """Results with different seeds should not be identical."""
    kwargs = dict(
        model_a_path=MODEL_A, model_b_path=MODEL_A,
        n_games=20, pool_size=8, temperature=0.0, nash_temperatures=False,
    )
    r1 = ts.benchmark_model_vs_model_batched(seed=1000, **kwargs)
    r2 = ts.benchmark_model_vs_model_batched(seed=2000, **kwargs)

    # At least one game must differ in VP or winner
    any_differ = any(
        a.final_vp != b.final_vp or str(a.winner) != str(b.winner)
        for a, b in zip(r1, r2)
    )
    assert any_differ, "All 20 games identical with different seeds -- RNG not functioning"
```

#### 1.5 Symmetry test (same model, expect ~50% WR)
```python
@skip_no_single_model
@pytest.mark.slow
def test_symmetry_same_model(ts):
    """When model_a == model_b, model_a win rate should be near 50%.

    With 200 games at T=0 and same model, expected WR is ~50%.
    Twilight Struggle has a slight USSR advantage (~+2 VP bid), so
    model_a WR may deviate slightly. Use wide tolerance: 35-65%.
    For 200 games, sigma = sqrt(0.5*0.5/200) = 3.5%, so 3-sigma = 10.5%.
    """
    n_games = 200
    results = ts.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_A, n_games=n_games, pool_size=32, seed=50000,
        temperature=0.0, nash_temperatures=False,
    )
    half = n_games // 2
    a_wins = 0
    for i, r in enumerate(results):
        if r.winner is None:
            continue
        if i < half:
            a_wins += 1 if r.winner == ts.Side.USSR else 0
        else:
            a_wins += 1 if r.winner == ts.Side.US else 0

    a_wr = a_wins / len(results)
    assert 0.35 <= a_wr <= 0.65, (
        f"Same-model WR = {a_wr:.1%}, expected ~50% (±15%)"
    )
```

**Tolerance:** 35-65% is approximately a 4-sigma window for n=200, p=0.5. This keeps flaky test risk below 0.01%.

#### 1.6 Side assignment test
```python
@skip_no_models
@pytest.mark.slow
def test_side_assignment(ts):
    """First half should have model_a=USSR, second half model_a=US.

    Use two different models. If model_a is stronger, it should win
    most games in BOTH halves (as USSR in first half, as US in second).
    """
    n_games = 100
    results = ts.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_B, n_games=n_games, pool_size=32, seed=60000,
        temperature=0.0, nash_temperatures=False,
    )
    half = n_games // 2

    # First half: model_a is USSR
    a_wins_first_half = sum(
        1 for r in results[:half] if r.winner == ts.Side.USSR
    )
    # Second half: model_a is US
    a_wins_second_half = sum(
        1 for r in results[half:] if r.winner == ts.Side.US
    )

    # We cannot assert which model is stronger without knowing,
    # but we CAN assert that both halves produce valid games
    # and that the total makes sense.
    total_games = len(results)
    assert total_games == n_games

    # Weaker test: just verify results are well-formed in both halves
    for r in results[:half]:
        assert r.winner in (ts.Side.USSR, ts.Side.US, None)
    for r in results[half:]:
        assert r.winner in (ts.Side.USSR, ts.Side.US, None)

    # If we know A > B, we can add stronger assertions.
    # For now, print diagnostics:
    a_total = a_wins_first_half + a_wins_second_half
    print(f"Model A WR: {a_total}/{total_games} = {a_total/total_games:.1%}")
    print(f"  As USSR (1st half): {a_wins_first_half}/{half}")
    print(f"  As US (2nd half): {a_wins_second_half}/{half}")
```

#### 1.7 WR inversion test
```python
@skip_no_models
@pytest.mark.slow
def test_wr_inversion(ts):
    """If A vs B gives WR=X, then B vs A with same seed should give WR ~= 1-X.

    Due to the half-split structure and same seeds, swapping model_a and model_b
    simply relabels who is "model_a". The games themselves should be identical
    (same seeds -> same game states), just with swapped side assignments.
    """
    n_games = 100
    seed = 70000

    r_ab = ts.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_B, n_games=n_games, pool_size=32, seed=seed,
        temperature=0.0, nash_temperatures=False,
    )
    r_ba = ts.benchmark_model_vs_model_batched(
        MODEL_B, MODEL_A, n_games=n_games, pool_size=32, seed=seed,
        temperature=0.0, nash_temperatures=False,
    )

    half = n_games // 2

    def model_a_wins(results, half):
        wins = 0
        for i, r in enumerate(results):
            if r.winner is None:
                continue
            if i < half:
                wins += 1 if r.winner == ts.Side.USSR else 0
            else:
                wins += 1 if r.winner == ts.Side.US else 0
        return wins

    a_wins_ab = model_a_wins(r_ab, half)
    a_wins_ba = model_a_wins(r_ba, half)  # "A" in r_ba is actually MODEL_B

    # In r_ab, model_A wins a_wins_ab games.
    # In r_ba, model_B is "model_a" and wins a_wins_ba games.
    # Since same seeds produce same game trajectories with swapped roles,
    # a_wins_ab + a_wins_ba should equal n_games (minus draws).
    # More precisely: A's WR in AB + B's WR in BA should ~= 1.0

    total = len(r_ab)
    wr_a_in_ab = a_wins_ab / total
    wr_b_as_a_in_ba = a_wins_ba / total  # this is B's WR

    # wr_a_in_ab + wr_b_as_a_in_ba ~ 1.0 (minus draw fraction)
    draws_ab = sum(1 for r in r_ab if r.winner is None)
    draws_ba = sum(1 for r in r_ba if r.winner is None)

    # With same seeds, the games should be identical just relabeled,
    # so a_wins_ab + a_wins_ba == total - draws (if draws are same)
    # Allow tolerance for numerical differences
    assert abs(draws_ab - draws_ba) <= 2, (
        f"Draw count mismatch: {draws_ab} vs {draws_ba}"
    )
    # The sum should be close to total minus average draws
    expected_sum = total - (draws_ab + draws_ba) / 2
    actual_sum = a_wins_ab + a_wins_ba
    assert abs(actual_sum - expected_sum) <= 3, (
        f"WR inversion failed: A_wins={a_wins_ab}, B_wins_as_A={a_wins_ba}, "
        f"draws_ab={draws_ab}, draws_ba={draws_ba}"
    )
```

**Important caveat from source review:** The WR inversion is NOT exact because the seed-to-game-index mapping is the same (`seed = base_seed + game_index`), but the side assignment flips. In r_ab, game 0 has A=USSR with seed `base_seed+0`. In r_ba, game 0 has B=USSR with same seed. The game states will differ because different models make different decisions. So exact inversion only holds statistically with large N. The tolerance `<=3` may need adjustment; alternatively, set tolerance to `0.1 * total`.

---

### 2. Edge Cases

#### 2.1 n_games=2 (minimum even)
```python
@skip_no_single_model
def test_n_games_2(ts):
    """Minimum meaningful run: 1 game each side."""
    results = ts.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_A, n_games=2, pool_size=2, seed=111,
        temperature=0.0, nash_temperatures=False,
    )
    assert len(results) == 2
    for r in results:
        assert r.winner in (ts.Side.USSR, ts.Side.US, None)
```

#### 2.2 n_games=1 (odd, rounds to 0)
```python
@skip_no_single_model
def test_n_games_1_returns_empty(ts):
    """n_games=1 -> half=0, total=0 -> empty results.

    This is a known limitation: odd n_games rounds down to even.
    """
    results = ts.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_A, n_games=1, pool_size=1, seed=222,
        temperature=0.0, nash_temperatures=False,
    )
    assert len(results) == 0
```

#### 2.3 n_games=0
```python
@skip_no_single_model
def test_n_games_0(ts):
    results = ts.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_A, n_games=0, pool_size=1, seed=333,
        temperature=0.0, nash_temperatures=False,
    )
    assert len(results) == 0
```

#### 2.4 Odd n_games rounds down
```python
@skip_no_single_model
def test_odd_n_games_rounds_down(ts):
    """n_games=7 -> half=3, total=6 -> returns 6 results."""
    results = ts.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_A, n_games=7, pool_size=4, seed=444,
        temperature=0.0, nash_temperatures=False,
    )
    assert len(results) == 6  # 7 // 2 * 2 = 6
```

#### 2.5 Same model path for both
```python
@skip_no_single_model
def test_same_model_both_sides(ts):
    """Same model path for A and B should work (loads two separate copies)."""
    results = ts.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_A, n_games=4, pool_size=2, seed=555,
        temperature=0.0, nash_temperatures=False,
    )
    assert len(results) == 4
```

#### 2.6 temperature=0.0 (greedy/argmax)
```python
@skip_no_single_model
def test_temperature_zero_deterministic(ts):
    """T=0 (argmax) should be fully deterministic."""
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
```

#### 2.7 temperature=1.0 (sampled) with fixed seed
```python
@skip_no_single_model
def test_temperature_nonzero_deterministic(ts):
    """T=1.0 with same seed should still be deterministic (seed controls sampling)."""
    kwargs = dict(
        model_a_path=MODEL_A, model_b_path=MODEL_A,
        n_games=6, pool_size=4, seed=667,
        temperature=1.0, nash_temperatures=False,
    )
    r1 = ts.benchmark_model_vs_model_batched(**kwargs)
    r2 = ts.benchmark_model_vs_model_batched(**kwargs)
    for a, b in zip(r1, r2):
        assert a.final_vp == b.final_vp
        assert str(a.winner) == str(b.winner)
```

#### 2.8 pool_size=1 (sequential)
```python
@skip_no_single_model
def test_pool_size_1(ts):
    """pool_size=1 forces sequential processing, should still work."""
    results = ts.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_A, n_games=4, pool_size=1, seed=888,
        temperature=0.0, nash_temperatures=False,
    )
    assert len(results) == 4
```

#### 2.9 pool_size larger than n_games
```python
@skip_no_single_model
def test_pool_size_larger_than_n_games(ts):
    """pool_size=64 with n_games=4 should work (most slots unused)."""
    results = ts.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_A, n_games=4, pool_size=64, seed=999,
        temperature=0.0, nash_temperatures=False,
    )
    assert len(results) == 4
```

---

### 3. Performance / Speed Comparison

Create a separate file: `/home/dkord/code/twilight-struggle-ai/tests/python/test_benchmark_model_vs_model_perf.py`

This is a benchmark script, not a pytest test (no assertions on speed, just measurement). Run manually:

```bash
cd /home/dkord/code/twilight-struggle-ai
uv run python tests/python/test_benchmark_model_vs_model_perf.py
```

```python
"""Performance comparison: benchmark_batched (model vs heuristic) vs
benchmark_model_vs_model_batched (model vs model).

Not a pytest test -- run directly for measurements.
"""
import sys
import time

sys.path.insert(0, "build-ninja/bindings")
import tscore

MODEL_A = "data/checkpoints/v99_nash_c_95ep_s42/baseline_best_scripted.pt"
N_GAMES = 100
POOL_SIZE = 32
SEED = 80000


def measure_old_benchmark():
    """Model vs heuristic (single NN batch per step)."""
    t0 = time.perf_counter()
    results = tscore.benchmark_batched(
        MODEL_A, tscore.Side.USSR, N_GAMES,
        pool_size=POOL_SIZE, seed=SEED, temperature=0.0, nash_temperatures=True,
    )
    elapsed = time.perf_counter() - t0
    return results, elapsed


def measure_new_benchmark():
    """Model vs model (two NN batches per step)."""
    t0 = time.perf_counter()
    results = tscore.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_A, n_games=N_GAMES,
        pool_size=POOL_SIZE, seed=SEED, temperature=0.0, nash_temperatures=False,
    )
    elapsed = time.perf_counter() - t0
    return results, elapsed


if __name__ == "__main__":
    # Warmup (JIT compilation, cache warming)
    tscore.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_A, n_games=4, pool_size=2, seed=1, temperature=0.0, nash_temperatures=False,
    )
    tscore.benchmark_batched(
        MODEL_A, tscore.Side.USSR, 4, pool_size=2, seed=1, temperature=0.0, nash_temperatures=True,
    )

    print(f"{'Method':<35} {'Games':>6} {'Time (s)':>10} {'Games/s':>10}")
    print("-" * 65)

    _, t_old = measure_old_benchmark()
    print(f"{'benchmark_batched (vs heuristic)':<35} {N_GAMES:>6} {t_old:>10.2f} {N_GAMES/t_old:>10.1f}")

    _, t_new = measure_new_benchmark()
    print(f"{'model_vs_model_batched':<35} {N_GAMES:>6} {t_new:>10.2f} {N_GAMES/t_new:>10.1f}")

    ratio = t_new / t_old
    print(f"\nNew/Old time ratio: {ratio:.2f}x")
    print(f"Expected: ~1.5-2.5x slower (two NN forward passes vs one NN + heuristic)")
```

**Expected results:** The new function should be roughly 1.5-2.5x slower because it runs two separate neural net forward passes per game step (one for model_a decisions, one for model_b decisions), while the old function runs one NN forward pass + fast C++ heuristic lookup.

---

### 4. Statistical Validity

For Elo tracking, the key quantity is the confidence interval on win rate (WR).

**Formula:** For a binomial proportion p estimated from n games, the standard error is:

`sigma = sqrt(p * (1 - p) / n)`

At p = 0.5 (equal models):

| n_games | sigma  | 95% CI (p +/- 1.96*sigma) | 99% CI (p +/- 2.58*sigma) |
|---------|--------|---------------------------|---------------------------|
| 100     | 0.050  | 0.50 +/- 0.098            | 0.50 +/- 0.129            |
| 200     | 0.035  | 0.50 +/- 0.069            | 0.50 +/- 0.091            |
| 500     | 0.022  | 0.50 +/- 0.044            | 0.50 +/- 0.058            |
| 1000    | 0.016  | 0.50 +/- 0.031            | 0.50 +/- 0.041            |

**Elo sensitivity:** A WR difference of 5% (0.45 vs 0.50) corresponds to roughly 35 Elo points. To detect a 35-Elo difference at 95% confidence, you need the CI to be smaller than 5%, which requires n >= 400 games.

**Recommendation for the elo_tracker.py default of 200 games:** The 95% CI is +/-6.9% on WR, which corresponds to roughly +/-48 Elo points of uncertainty. This is adequate for tracking large improvements but insufficient for detecting <30 Elo differences.

Add a statistical validation test:

```python
@skip_no_single_model
@pytest.mark.slow
def test_statistical_confidence_interval(ts):
    """Verify that same-model matchup WR falls within expected binomial CI.

    200 games, p=0.5, 99.9% CI = p +/- 3.29*sigma = 0.50 +/- 0.116.
    So WR should be in [0.384, 0.616]. Use 0.30-0.70 for extra safety.
    """
    n_games = 200
    results = ts.benchmark_model_vs_model_batched(
        MODEL_A, MODEL_A, n_games=n_games, pool_size=32, seed=90000,
        temperature=0.0, nash_temperatures=False,
    )
    half = n_games // 2
    a_wins = 0
    for i, r in enumerate(results):
        if r.winner is None:
            continue
        if i < half:
            a_wins += 1 if r.winner == ts.Side.USSR else 0
        else:
            a_wins += 1 if r.winner == ts.Side.US else 0
    wr = a_wins / len(results)

    # 99.9% CI for binomial p=0.5, n=200 is [0.384, 0.616]
    # Use generous bounds to avoid flaky tests
    assert 0.30 <= wr <= 0.70, f"Same-model WR={wr:.3f} outside [0.30, 0.70]"
```

---

### 5. Summary of all tests and their locations

| Test name | File | Requires 2 models | Slow marker | Key assertion |
|---|---|---|---|---|
| test_result_count_even | test_benchmark_model_vs_model.py | No | No | len == n_games |
| test_winner_and_vp_consistency | " | No | No | VP sign matches winner |
| test_determinism_same_seed | " | No | No | Bitwise identical |
| test_different_seeds_differ | " | No | No | At least 1 game differs |
| test_symmetry_same_model | " | No | Yes | 35-65% WR |
| test_side_assignment | " | Yes | Yes | Both halves valid |
| test_wr_inversion | " | Yes | Yes | Sum of WRs ~= 1 |
| test_n_games_2 | " | No | No | len == 2 |
| test_n_games_1_returns_empty | " | No | No | len == 0 |
| test_n_games_0 | " | No | No | len == 0 |
| test_odd_n_games_rounds_down | " | No | No | len == 6 for n=7 |
| test_same_model_both_sides | " | No | No | len == 4 |
| test_temperature_zero_deterministic | " | No | No | Identical results |
| test_temperature_nonzero_deterministic | " | No | No | Identical results |
| test_pool_size_1 | " | No | No | len == 4 |
| test_pool_size_larger_than_n_games | " | No | No | len == 4 |
| test_statistical_confidence_interval | " | No | Yes | 30-70% WR |
| (perf script) | test_benchmark_model_vs_model_perf.py | No | N/A | Print measurements |

---

### 6. Notable implementation observations / potential issues

1. **n_games=1 returns empty**: The implementation does `half = n_games / 2; total = half * 2` with integer division, so any odd n_games loses 1 game. n_games=1 returns 0 results. This should be

---

> **Note:** The captured text above is truncated at ~22.6 KB (mid-sentence in section 6). The agent's
> output was cut off before completing the remaining observations. The content above is complete
> through section 5 (summary table) and begins section 6 (implementation observations).
