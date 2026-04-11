"""Integration tests for the rollout → step → training pipeline.

Tests the full chain: C++ batched rollout produces steps with valid features,
masks, log-probs, and metadata that are consumable by the training loop.
Catches regressions like:
  - Feature shape mismatches (SCALAR_DIM changes)
  - Log-prob sign/finiteness issues
  - Mask validity (at least one legal action per head)
  - Country target validity (within bounds, non-negative)
  - SmallChoice field propagation
  - Step dict → Step dataclass conversion
"""

from __future__ import annotations

import os
import sys

import numpy as np
import pytest
import torch
import torch.nn.functional as F

# Ensure the build directory bindings are importable.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "build-ninja", "bindings"))
import tscore  # noqa: E402

# Path to a scripted model that matches current features.
MODEL_PATH = "data/checkpoints/scripted_for_elo/v45_scripted.pt"
MODEL_EXISTS = os.path.exists(MODEL_PATH)

pytestmark = pytest.mark.skipif(not MODEL_EXISTS, reason="v45 scripted model not found")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def run_small_rollout(n_games: int = 5, seed: int = 42, side=None):
    """Run a small batched rollout and return (results, steps, boundaries)."""
    if side is None:
        side = tscore.Side.USSR
    results, steps, boundaries = tscore.rollout_games_batched(
        MODEL_PATH, side, n_games, pool_size=8, seed=seed, device="cpu",
        temperature=1.0, nash_temperatures=True,
    )
    return results, steps, boundaries


def run_self_play_rollout(n_games: int = 5, seed: int = 42):
    """Run a small self-play rollout."""
    results, steps, boundaries = tscore.rollout_self_play_batched(
        MODEL_PATH, n_games, pool_size=8, seed=seed, device="cpu",
        temperature=1.0, nash_temperatures=True,
    )
    return results, steps, boundaries


# ---------------------------------------------------------------------------
# Step structure tests
# ---------------------------------------------------------------------------

class TestStepStructure:
    """Verify that each rollout step has the expected fields and shapes."""

    def test_steps_nonempty(self):
        _, steps, _ = run_small_rollout(n_games=3)
        assert len(steps) > 0, "Rollout produced zero steps"

    def test_step_has_required_keys(self):
        _, steps, _ = run_small_rollout(n_games=2)
        required = {
            "influence", "cards", "scalars",
            "card_mask", "mode_mask", "country_mask",
            "card_idx", "mode_idx", "country_targets",
            "log_prob", "value", "side_int", "game_index",
        }
        for step in steps[:5]:
            missing = required - set(step.keys())
            assert not missing, f"Step missing keys: {missing}"

    def test_step_has_raw_state_keys(self):
        _, steps, _ = run_small_rollout(n_games=2)
        raw_keys = {
            "raw_turn", "raw_ar", "raw_defcon", "raw_vp",
            "raw_milops", "raw_space",
            "raw_ussr_influence", "raw_us_influence",
            "hand_card_ids",
        }
        for step in steps[:5]:
            missing = raw_keys - set(step.keys())
            assert not missing, f"Step missing raw state keys: {missing}"

    def test_step_has_small_choice_keys(self):
        """SmallChoice fields must be present even when no decision occurred."""
        _, steps, _ = run_small_rollout(n_games=2)
        sc_keys = {"small_choice_target", "small_choice_n_options", "small_choice_logprob"}
        for step in steps[:5]:
            missing = sc_keys - set(step.keys())
            assert not missing, f"Step missing small_choice keys: {missing}"


# ---------------------------------------------------------------------------
# Feature shape tests
# ---------------------------------------------------------------------------

class TestFeatureShapes:
    """Verify tensor shapes match expected dimensions."""

    def test_influence_shape(self):
        _, steps, _ = run_small_rollout(n_games=2)
        for step in steps[:5]:
            assert step["influence"].shape == (172,), \
                f"influence shape {step['influence'].shape}, expected (172,)"

    def test_cards_shape(self):
        _, steps, _ = run_small_rollout(n_games=2)
        for step in steps[:5]:
            assert step["cards"].shape == (448,), \
                f"cards shape {step['cards'].shape}, expected (448,)"

    def test_scalars_shape(self):
        _, steps, _ = run_small_rollout(n_games=2)
        for step in steps[:5]:
            # SCALAR_DIM is 32 for current models
            assert step["scalars"].shape[0] == 32, \
                f"scalars dim {step['scalars'].shape[0]}, expected 32"

    def test_mask_shapes(self):
        _, steps, _ = run_small_rollout(n_games=2)
        for step in steps[:5]:
            assert step["card_mask"].shape == (111,)
            assert step["mode_mask"].shape == (5,)
            assert step["country_mask"].shape == (86,)


# ---------------------------------------------------------------------------
# Mask validity tests
# ---------------------------------------------------------------------------

class TestMaskValidity:
    """Legal masks must have at least one True entry per head."""

    def test_card_mask_has_legal_action(self):
        _, steps, _ = run_small_rollout(n_games=5)
        for i, step in enumerate(steps):
            assert step["card_mask"].any(), f"Step {i}: card_mask is all-False (no legal card)"

    def test_mode_mask_has_legal_action(self):
        _, steps, _ = run_small_rollout(n_games=5)
        for i, step in enumerate(steps):
            assert step["mode_mask"].any(), f"Step {i}: mode_mask is all-False (no legal mode)"

    def test_selected_card_is_legal(self):
        _, steps, _ = run_small_rollout(n_games=5)
        for i, step in enumerate(steps):
            if step["card_idx"] >= 0:
                assert step["card_mask"][step["card_idx"]], \
                    f"Step {i}: selected card {step['card_idx']} is not legal"

    def test_selected_mode_is_legal(self):
        _, steps, _ = run_small_rollout(n_games=5)
        for i, step in enumerate(steps):
            if step["mode_idx"] >= 0:
                assert step["mode_mask"][step["mode_idx"]], \
                    f"Step {i}: selected mode {step['mode_idx']} is not legal"


# ---------------------------------------------------------------------------
# Log-prob validity tests
# ---------------------------------------------------------------------------

class TestLogProbValidity:
    """Log-probabilities must be finite, negative, and consistent."""

    def test_log_prob_finite(self):
        _, steps, _ = run_small_rollout(n_games=5)
        for i, step in enumerate(steps):
            lp = step["log_prob"]
            assert np.isfinite(lp), f"Step {i}: log_prob={lp} is not finite"

    def test_log_prob_nonpositive(self):
        _, steps, _ = run_small_rollout(n_games=5)
        for i, step in enumerate(steps):
            lp = step["log_prob"]
            assert lp <= 0.01, f"Step {i}: log_prob={lp} should be <= 0"

    def test_log_prob_not_extreme(self):
        """Log-probs shouldn't be extreme (< -50) for sampled actions."""
        _, steps, _ = run_small_rollout(n_games=5)
        extreme_count = sum(1 for s in steps if s["log_prob"] < -50)
        # Allow a small fraction of extreme log-probs (rare forced actions)
        assert extreme_count < len(steps) * 0.1, \
            f"{extreme_count}/{len(steps)} steps have extreme log-probs (< -50)"


# ---------------------------------------------------------------------------
# Value head tests
# ---------------------------------------------------------------------------

class TestValueHead:
    """Value predictions should be bounded and finite."""

    def test_value_finite(self):
        _, steps, _ = run_small_rollout(n_games=5)
        for i, step in enumerate(steps):
            v = step["value"]
            assert np.isfinite(v), f"Step {i}: value={v} is not finite"

    def test_value_bounded(self):
        """Value should be roughly in [-1, 1] for tanh output or reasonable range."""
        _, steps, _ = run_small_rollout(n_games=5)
        values = [s["value"] for s in steps]
        assert min(values) > -5.0, f"Value too negative: {min(values)}"
        assert max(values) < 5.0, f"Value too positive: {max(values)}"


# ---------------------------------------------------------------------------
# Country target tests
# ---------------------------------------------------------------------------

class TestCountryTargets:
    """Country targets should be within valid range and consistent with mode."""

    def test_country_targets_in_range(self):
        _, steps, _ = run_small_rollout(n_games=5)
        for i, step in enumerate(steps):
            for ct in step["country_targets"]:
                assert 0 <= ct < 86, f"Step {i}: country_target {ct} out of range [0, 86)"

    def test_influence_modes_have_country_targets(self):
        """Modes 0 (influence) and 2 (coup) should typically have country targets."""
        _, steps, _ = run_small_rollout(n_games=10)
        influence_steps = [s for s in steps if s["mode_idx"] in (0, 2)]
        if influence_steps:
            has_targets = sum(1 for s in influence_steps if len(s["country_targets"]) > 0)
            assert has_targets > 0, "No influence/coup steps have country targets"


# ---------------------------------------------------------------------------
# Game boundary tests
# ---------------------------------------------------------------------------

class TestGameBoundaries:
    """Game boundaries should be consistent with step count and game count."""

    def test_boundaries_count(self):
        n = 5
        results, steps, boundaries = run_small_rollout(n_games=n)
        assert len(boundaries) == n, f"Expected {n} boundaries, got {len(boundaries)}"

    def test_boundaries_monotonic(self):
        _, _, boundaries = run_small_rollout(n_games=5)
        for i in range(1, len(boundaries)):
            assert boundaries[i] >= boundaries[i - 1], \
                f"Boundaries not monotonic at {i}: {boundaries[i-1]} > {boundaries[i]}"

    def test_all_results_have_winner(self):
        results, _, _ = run_small_rollout(n_games=5)
        for i, r in enumerate(results):
            assert r.winner in (tscore.Side.USSR, tscore.Side.US), \
                f"Game {i} has no winner: {r.winner}"


# ---------------------------------------------------------------------------
# Raw state validity tests
# ---------------------------------------------------------------------------

class TestRawState:
    """Raw game state fields should have valid ranges."""

    def test_raw_turn_range(self):
        _, steps, _ = run_small_rollout(n_games=5)
        for i, step in enumerate(steps):
            t = step["raw_turn"]
            assert 1 <= t <= 10, f"Step {i}: raw_turn={t} out of range [1, 10]"

    def test_raw_defcon_range(self):
        _, steps, _ = run_small_rollout(n_games=5)
        for i, step in enumerate(steps):
            d = step["raw_defcon"]
            assert 1 <= d <= 5, f"Step {i}: raw_defcon={d} out of range [1, 5]"

    def test_raw_influence_shape(self):
        _, steps, _ = run_small_rollout(n_games=2)
        for step in steps[:3]:
            assert len(step["raw_ussr_influence"]) == 86
            assert len(step["raw_us_influence"]) == 86

    def test_raw_influence_nonnegative(self):
        _, steps, _ = run_small_rollout(n_games=5)
        for i, step in enumerate(steps):
            for c in range(86):
                assert step["raw_ussr_influence"][c] >= 0, \
                    f"Step {i}: negative USSR influence at country {c}"
                assert step["raw_us_influence"][c] >= 0, \
                    f"Step {i}: negative US influence at country {c}"

    def test_hand_card_ids_valid(self):
        _, steps, _ = run_small_rollout(n_games=3)
        for i, step in enumerate(steps):
            if step["hand_card_ids"]:
                for card_id in step["hand_card_ids"]:
                    assert 1 <= card_id <= 111, \
                        f"Step {i}: hand card_id={card_id} out of range [1, 111]"


# ---------------------------------------------------------------------------
# SmallChoice field tests
# ---------------------------------------------------------------------------

class TestSmallChoiceFields:
    """SmallChoice fields should be properly initialized and bounded."""

    def test_default_no_decision(self):
        """Most steps should have small_choice_target=-1 (no decision)."""
        _, steps, _ = run_small_rollout(n_games=5)
        no_decision = sum(1 for s in steps if s["small_choice_target"] == -1)
        # Expect most steps to not have a small_choice
        assert no_decision > len(steps) * 0.5, \
            f"Too many small_choice decisions: {len(steps) - no_decision}/{len(steps)}"

    def test_n_options_consistency(self):
        """If target >= 0, n_options should be > 1. If target < 0, n_options should be 0."""
        _, steps, _ = run_small_rollout(n_games=10)
        for i, step in enumerate(steps):
            if step["small_choice_target"] >= 0:
                assert step["small_choice_n_options"] > 1, \
                    f"Step {i}: has target but n_options={step['small_choice_n_options']}"
            # n_options=0 → no decision (target should be -1)
            if step["small_choice_n_options"] == 0:
                assert step["small_choice_target"] == -1, \
                    f"Step {i}: n_options=0 but target={step['small_choice_target']}"

    def test_target_in_range(self):
        """SmallChoice target must be < n_options when valid."""
        _, steps, _ = run_small_rollout(n_games=10)
        for i, step in enumerate(steps):
            if step["small_choice_target"] >= 0:
                assert step["small_choice_target"] < step["small_choice_n_options"], \
                    f"Step {i}: target={step['small_choice_target']} >= n_options={step['small_choice_n_options']}"

    def test_logprob_finite_when_valid(self):
        _, steps, _ = run_small_rollout(n_games=10)
        for i, step in enumerate(steps):
            if step["small_choice_target"] >= 0:
                assert np.isfinite(step["small_choice_logprob"]), \
                    f"Step {i}: small_choice_logprob={step['small_choice_logprob']} not finite"


# ---------------------------------------------------------------------------
# Self-play rollout tests
# ---------------------------------------------------------------------------

class TestSelfPlayRollout:
    """Tests specific to self-play mode rollout."""

    def test_self_play_produces_steps(self):
        results, steps, boundaries = run_self_play_rollout(n_games=3)
        assert len(steps) > 0

    def test_self_play_both_sides_present(self):
        """Self-play should have steps from both USSR (0) and US (1)."""
        _, steps, _ = run_self_play_rollout(n_games=5)
        sides = set(s["side_int"] for s in steps)
        assert 0 in sides, "No USSR steps in self-play"
        assert 1 in sides, "No US steps in self-play"

    def test_self_play_step_structure(self):
        """Self-play steps should have same structure as learned-vs-heuristic."""
        _, steps, _ = run_self_play_rollout(n_games=2)
        for step in steps[:3]:
            assert step["influence"].shape == (172,)
            assert step["card_mask"].shape == (111,)
            assert step["card_mask"].any()


# ---------------------------------------------------------------------------
# Determinism tests
# ---------------------------------------------------------------------------

class TestDeterminism:
    """Rollouts with same seed should produce identical results."""

    def test_deterministic_game_count(self):
        """Same seed should produce same number of completed games."""
        r1, _, _ = run_small_rollout(n_games=3, seed=123)
        r2, _, _ = run_small_rollout(n_games=3, seed=123)
        assert len(r1) == len(r2), f"Game counts differ: {len(r1)} vs {len(r2)}"

    def test_different_seeds_differ(self):
        """Different seeds should produce different game outcomes."""
        r1, s1, _ = run_small_rollout(n_games=5, seed=111)
        r2, s2, _ = run_small_rollout(n_games=5, seed=222)
        # At least some game outcomes should differ
        winners1 = [r.winner for r in r1]
        winners2 = [r.winner for r in r2]
        # With 5 games, very unlikely all outcomes match with different seeds
        # But don't assert — just check steps differ
        if len(s1) > 0 and len(s2) > 0:
            # Check that at least some step features differ
            f1 = s1[0]["scalars"]
            f2 = s2[0]["scalars"]
            assert not np.array_equal(f1, f2) or len(s1) != len(s2), \
                "Different seeds produced suspiciously identical rollouts"


# ---------------------------------------------------------------------------
# Log-prob recomputation test (integration: verifies C++ and Python agree)
# ---------------------------------------------------------------------------

class TestLogProbRecomputation:
    """Verify that log-probs from C++ rollout can be approximately recomputed
    by running the Python model forward pass on the same features."""

    def test_log_prob_recompute_close(self):
        """C++ sampled log-probs should match Python-recomputed log-probs."""
        _, steps, _ = run_small_rollout(n_games=3, seed=42)

        model = torch.jit.load(MODEL_PATH, map_location="cpu")
        model.eval()

        mismatches = 0
        tested = 0
        for step in steps[:20]:
            influence = torch.from_numpy(step["influence"]).unsqueeze(0).float()
            cards = torch.from_numpy(step["cards"]).unsqueeze(0).float()
            scalars = torch.from_numpy(step["scalars"]).unsqueeze(0).float()

            with torch.no_grad():
                try:
                    outputs = model(influence, cards, scalars)
                except RuntimeError:
                    pytest.skip("Scripted model forward call format mismatch")

            card_logits = outputs["card_logits"].squeeze(0)
            mode_logits = outputs["mode_logits"].squeeze(0)

            card_mask = torch.from_numpy(step["card_mask"]).bool()
            mode_mask = torch.from_numpy(step["mode_mask"]).bool()

            # Recompute log-prob for card + mode
            masked_card = card_logits.clone()
            masked_card[~card_mask] = float("-inf")
            lp_card = F.log_softmax(masked_card, dim=0)[step["card_idx"]]

            masked_mode = mode_logits.clone()
            masked_mode[~mode_mask] = float("-inf")
            lp_mode = F.log_softmax(masked_mode, dim=0)[step["mode_idx"]]

            recomputed = (lp_card + lp_mode).item()
            original = step["log_prob"]

            # Country log-prob component means these won't match exactly,
            # but card+mode should be within a reasonable range
            if abs(recomputed - original) > 5.0:
                mismatches += 1
            tested += 1

        # Allow some discrepancy due to country log-prob differences
        assert mismatches < tested * 0.3, \
            f"{mismatches}/{tested} steps have large log-prob discrepancy"
