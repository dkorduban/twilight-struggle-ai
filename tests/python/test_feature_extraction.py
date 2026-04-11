"""Tests for feature extraction consistency.

Catches regressions when SCALAR_DIM, INFLUENCE_DIM, or CARD_DIM change
without corresponding model/training updates. Also verifies that feature
scaling is within expected ranges (no unbounded values that cause NaN).
"""

from __future__ import annotations

import os
import sys

import numpy as np
import pytest
import torch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "build-ninja", "bindings"))

from tsrl.policies.model import (
    INFLUENCE_DIM,
    CARD_DIM,
    SCALAR_DIM,
    NUM_PLAYABLE_CARDS,
    NUM_MODES,
    NUM_COUNTRIES,
)


# ---------------------------------------------------------------------------
# Dimension consistency
# ---------------------------------------------------------------------------

class TestDimensionConstants:
    """Verify feature dimension constants are consistent across the system."""

    def test_influence_dim_is_2x_countries(self):
        """Influence = USSR + US per country = 2 * 86."""
        assert INFLUENCE_DIM == 2 * 86, f"INFLUENCE_DIM={INFLUENCE_DIM}, expected {2*86}"

    def test_card_dim_is_4x_card_slots(self):
        """Cards = hand + hand_copy + discard + removed = 4 * 112."""
        CARD_SLOTS = 112  # kCardSlots in C++
        assert CARD_DIM == 4 * CARD_SLOTS, f"CARD_DIM={CARD_DIM}, expected {4*CARD_SLOTS}"

    def test_scalar_dim_matches_current(self):
        """SCALAR_DIM should be 32 (11 core + 21 effects)."""
        assert SCALAR_DIM == 32, f"SCALAR_DIM={SCALAR_DIM}, expected 32"

    def test_num_playable_cards(self):
        """NUM_PLAYABLE_CARDS should be 111 (card IDs 1-111 map to indices 0-110)."""
        assert NUM_PLAYABLE_CARDS == 111, f"NUM_PLAYABLE_CARDS={NUM_PLAYABLE_CARDS}"

    def test_num_modes(self):
        """NUM_MODES should be 5 (influence, realign, coup, event, space)."""
        assert NUM_MODES == 5, f"NUM_MODES={NUM_MODES}"

    def test_num_countries(self):
        """NUM_COUNTRIES should be 86."""
        assert NUM_COUNTRIES == 86, f"NUM_COUNTRIES={NUM_COUNTRIES}"


# ---------------------------------------------------------------------------
# Feature range tests (from rollout data)
# ---------------------------------------------------------------------------

try:
    import tscore
    HAS_TSCORE = True
except ImportError:
    HAS_TSCORE = False

MODEL_PATH = "data/checkpoints/scripted_for_elo/v45_scripted.pt"
MODEL_EXISTS = os.path.exists(MODEL_PATH) if HAS_TSCORE else False


@pytest.mark.skipif(not (HAS_TSCORE and MODEL_EXISTS), reason="tscore or model not available")
class TestFeatureRanges:
    """Verify that extracted features are within expected ranges."""

    @pytest.fixture(scope="class")
    def rollout_steps(self):
        results, steps, _ = tscore.rollout_games_batched(
            MODEL_PATH, tscore.Side.USSR, 3, pool_size=4, seed=42,
            device="cpu", temperature=1.0, nash_temperatures=True,
        )
        return steps

    def test_influence_nonnegative(self, rollout_steps):
        """Influence features should be non-negative (raw counts)."""
        for i, step in enumerate(rollout_steps[:20]):
            inf = step["influence"]
            assert (inf >= -0.01).all(), f"Step {i}: negative influence: min={inf.min()}"

    def test_influence_bounded(self, rollout_steps):
        """Influence should be bounded (no country has >30 influence)."""
        for i, step in enumerate(rollout_steps[:20]):
            inf = step["influence"]
            assert inf.max() < 50, f"Step {i}: extreme influence: max={inf.max()}"

    def test_card_features_binary(self, rollout_steps):
        """Card features should be 0 or 1 (mask values)."""
        for i, step in enumerate(rollout_steps[:10]):
            cards = step["cards"]
            unique = np.unique(cards)
            assert set(unique).issubset({0.0, 1.0}), \
                f"Step {i}: non-binary card features: {sorted(set(unique) - {0.0, 1.0})}"

    def test_scalars_bounded(self, rollout_steps):
        """Scalar features should be normalized to roughly [0, 1] or [-1, 1]."""
        for i, step in enumerate(rollout_steps[:20]):
            scalars = step["scalars"]
            assert scalars.max() <= 2.0, f"Step {i}: scalar too large: max={scalars.max()}"
            assert scalars.min() >= -2.0, f"Step {i}: scalar too small: min={scalars.min()}"

    def test_scalars_no_nan(self, rollout_steps):
        """No NaN values in scalar features."""
        for i, step in enumerate(rollout_steps[:20]):
            scalars = step["scalars"]
            assert not np.isnan(scalars).any(), f"Step {i}: NaN in scalars"

    def test_influence_no_nan(self, rollout_steps):
        """No NaN values in influence features."""
        for i, step in enumerate(rollout_steps[:20]):
            inf = step["influence"]
            assert not np.isnan(inf).any(), f"Step {i}: NaN in influence"

    def test_card_features_no_nan(self, rollout_steps):
        """No NaN values in card features."""
        for i, step in enumerate(rollout_steps[:20]):
            cards = step["cards"]
            assert not np.isnan(cards).any(), f"Step {i}: NaN in cards"


# ---------------------------------------------------------------------------
# Scalar feature content tests
# ---------------------------------------------------------------------------

@pytest.mark.skipif(not (HAS_TSCORE and MODEL_EXISTS), reason="tscore or model not available")
class TestScalarContent:
    """Verify specific scalar feature slots have expected content."""

    @pytest.fixture(scope="class")
    def first_step(self):
        _, steps, _ = tscore.rollout_games_batched(
            MODEL_PATH, tscore.Side.USSR, 1, pool_size=2, seed=42,
            device="cpu", temperature=1.0, nash_temperatures=True,
        )
        return steps[0]

    def test_vp_normalized(self, first_step):
        """VP (index 0) should be in [-1, 1] (normalized by /20)."""
        vp = first_step["scalars"][0]
        assert -1.1 <= vp <= 1.1, f"VP scalar={vp}, expected [-1, 1]"

    def test_defcon_normalized(self, first_step):
        """DEFCON (index 1) should be in [0, 1] (normalized by (d-1)/4)."""
        defcon = first_step["scalars"][1]
        assert -0.1 <= defcon <= 1.1, f"DEFCON scalar={defcon}, expected [0, 1]"

    def test_turn_normalized(self, first_step):
        """Turn (index 8) should be in [0.1, 1.0] (normalized by /10)."""
        turn = first_step["scalars"][8]
        assert 0.05 <= turn <= 1.1, f"Turn scalar={turn}, expected [0.1, 1.0]"

    def test_side_indicator(self, first_step):
        """Side (index 10) should be 0 or 1."""
        side = first_step["scalars"][10]
        assert side in (0.0, 1.0), f"Side scalar={side}, expected 0 or 1"

    def test_active_effects_binary(self, first_step):
        """Active effect flags (indices 11-27) should be 0 or 1."""
        for idx in range(11, 28):
            val = first_step["scalars"][idx]
            assert val in (0.0, 1.0), f"Effect scalar[{idx}]={val}, expected 0 or 1"


# ---------------------------------------------------------------------------
# Cross-model dimension compatibility
# ---------------------------------------------------------------------------

class TestModelDimensionCompat:
    """Verify all model variants accept the same input dimensions."""

    @pytest.fixture(params=["TSBaselineModel"])
    def model_cls(self, request):
        from tsrl.policies import model as model_mod
        return getattr(model_mod, request.param)

    def test_forward_with_standard_dims(self, model_cls):
        """Model should accept standard (INFLUENCE_DIM, CARD_DIM, SCALAR_DIM) input."""
        model = model_cls(hidden_dim=64)
        B = 2
        out = model(
            torch.randn(B, INFLUENCE_DIM),
            torch.randn(B, CARD_DIM),
            torch.randn(B, SCALAR_DIM),
        )
        assert "card_logits" in out
        assert "value" in out
        assert out["card_logits"].shape[0] == B
        assert out["value"].shape[0] == B

    def test_single_batch(self, model_cls):
        """Model should handle batch_size=1."""
        model = model_cls(hidden_dim=64)
        out = model(
            torch.randn(1, INFLUENCE_DIM),
            torch.randn(1, CARD_DIM),
            torch.randn(1, SCALAR_DIM),
        )
        assert out["card_logits"].shape == (1, NUM_PLAYABLE_CARDS)
        assert out["value"].shape == (1, 1)
