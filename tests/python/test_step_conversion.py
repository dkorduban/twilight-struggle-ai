"""Tests for Step conversion from C++ rollout dicts.

The _steps_from_native function is the boundary between C++ rollout output
and Python training. Bugs here silently corrupt training data. These tests
verify:
  - All required fields are mapped correctly
  - Tensor shapes match expected dimensions
  - Mask dtypes are bool
  - Country mask None-handling for SPACE/EVENT modes
  - SmallChoice fields default correctly when absent
  - Type conversions don't lose precision
  - Edge cases: empty country targets, maximum card IDs
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pytest
import torch

# Ensure train_ppo is importable
_repo_root = Path(__file__).resolve().parent.parent.parent
_scripts_dir = str(_repo_root / "scripts")
if _scripts_dir not in sys.path:
    sys.path.insert(0, _scripts_dir)

from tsrl.policies.model import (
    CARD_DIM,
    INFLUENCE_DIM,
    NUM_COUNTRIES,
    NUM_MODES,
    NUM_PLAYABLE_CARDS,
    SCALAR_DIM,
)

from train_ppo import Step, _steps_from_native


# ---------------------------------------------------------------------------
# Synthetic rollout dict factory
# ---------------------------------------------------------------------------

def _make_native_dict(
    card_idx: int = 5,
    mode_idx: int = 0,
    country_targets: list[int] | None = None,
    side_int: int = 0,
    log_prob: float = -1.5,
    value: float = 0.1,
    country_mask_all_false: bool = False,
    small_choice_target: int = -1,
    small_choice_n_options: int = 0,
    small_choice_logprob: float = 0.0,
    seed: int = 42,
) -> dict:
    """Create a dict mimicking C++ rollout_step_to_dict output."""
    rng = np.random.RandomState(seed)

    if country_targets is None:
        country_targets = [10, 20]

    card_mask = np.zeros(NUM_PLAYABLE_CARDS, dtype=bool)
    card_mask[card_idx] = True
    card_mask[min(card_idx + 1, NUM_PLAYABLE_CARDS - 1)] = True

    mode_mask = np.zeros(NUM_MODES, dtype=bool)
    mode_mask[mode_idx] = True

    if country_mask_all_false:
        country_mask = np.zeros(NUM_COUNTRIES, dtype=bool)
    else:
        country_mask = np.zeros(NUM_COUNTRIES, dtype=bool)
        for c in country_targets:
            if 0 <= c < NUM_COUNTRIES:
                country_mask[c] = True
        country_mask[30] = True  # extra legal country

    return {
        "influence": rng.randn(2 * 86).astype(np.float32),
        "cards": rng.randn(4 * 112).astype(np.float32),
        "scalars": rng.randn(SCALAR_DIM).astype(np.float32),
        "card_mask": card_mask,
        "mode_mask": mode_mask,
        "country_mask": country_mask,
        "card_idx": card_idx,
        "mode_idx": mode_idx,
        "country_targets": np.array(country_targets, dtype=np.int64),
        "log_prob": log_prob,
        "value": value,
        "side_int": side_int,
        "game_index": 0,
        "raw_turn": 3,
        "raw_ar": 1,
        "raw_defcon": 4,
        "raw_vp": 0,
        "raw_milops": np.array([0, 0], dtype=np.int32),
        "raw_space": np.array([0, 0], dtype=np.int32),
        "raw_ussr_influence": np.zeros(86, dtype=np.int16),
        "raw_us_influence": np.zeros(86, dtype=np.int16),
        "hand_card_ids": np.array([card_idx + 1, card_idx + 2], dtype=np.int32),
        "small_choice_target": small_choice_target,
        "small_choice_n_options": small_choice_n_options,
        "small_choice_logprob": small_choice_logprob,
    }


# ---------------------------------------------------------------------------
# Basic conversion tests
# ---------------------------------------------------------------------------

class TestBasicConversion:
    """Test that _steps_from_native produces correct Step objects."""

    def test_single_step_conversion(self):
        """Convert a single native dict to Step."""
        d = _make_native_dict()
        steps = _steps_from_native([d])
        assert len(steps) == 1
        assert isinstance(steps[0], Step)

    def test_batch_conversion(self):
        """Convert multiple native dicts."""
        dicts = [_make_native_dict(seed=i) for i in range(5)]
        steps = _steps_from_native(dicts)
        assert len(steps) == 5

    def test_empty_list(self):
        """Empty input should return empty list."""
        steps = _steps_from_native([])
        assert steps == []


# ---------------------------------------------------------------------------
# Field mapping tests
# ---------------------------------------------------------------------------

class TestFieldMapping:
    """Test that each field is correctly mapped."""

    def test_card_idx_preserved(self):
        d = _make_native_dict(card_idx=42)
        step = _steps_from_native([d])[0]
        assert step.card_idx == 42

    def test_mode_idx_preserved(self):
        d = _make_native_dict(mode_idx=3)
        step = _steps_from_native([d])[0]
        assert step.mode_idx == 3

    def test_country_targets_preserved(self):
        d = _make_native_dict(country_targets=[15, 42, 7])
        step = _steps_from_native([d])[0]
        assert step.country_targets == [15, 42, 7]

    def test_side_int_preserved(self):
        for side in (0, 1):
            d = _make_native_dict(side_int=side)
            step = _steps_from_native([d])[0]
            assert step.side_int == side

    def test_log_prob_preserved(self):
        d = _make_native_dict(log_prob=-2.345)
        step = _steps_from_native([d])[0]
        assert abs(step.old_log_prob - (-2.345)) < 1e-6

    def test_value_preserved(self):
        d = _make_native_dict(value=0.789)
        step = _steps_from_native([d])[0]
        assert abs(step.value - 0.789) < 1e-6

    def test_raw_turn_preserved(self):
        d = _make_native_dict()
        d["raw_turn"] = 7
        step = _steps_from_native([d])[0]
        assert step.raw_turn == 7

    def test_raw_defcon_preserved(self):
        d = _make_native_dict()
        d["raw_defcon"] = 2
        step = _steps_from_native([d])[0]
        assert step.raw_defcon == 2

    def test_raw_vp_preserved(self):
        d = _make_native_dict()
        d["raw_vp"] = -5
        step = _steps_from_native([d])[0]
        assert step.raw_vp == -5

    def test_hand_card_ids_preserved(self):
        d = _make_native_dict(card_idx=10)
        step = _steps_from_native([d])[0]
        assert step.hand_card_ids == [11, 12]


# ---------------------------------------------------------------------------
# Tensor shape tests
# ---------------------------------------------------------------------------

class TestTensorShapes:
    """Test that tensor fields have correct shapes."""

    def test_influence_shape(self):
        d = _make_native_dict()
        step = _steps_from_native([d])[0]
        assert step.influence.shape == (1, INFLUENCE_DIM)

    def test_cards_shape(self):
        d = _make_native_dict()
        step = _steps_from_native([d])[0]
        assert step.cards.shape == (1, CARD_DIM)

    def test_scalars_shape(self):
        d = _make_native_dict()
        step = _steps_from_native([d])[0]
        assert step.scalars.shape == (1, SCALAR_DIM)

    def test_card_mask_shape_and_dtype(self):
        d = _make_native_dict()
        step = _steps_from_native([d])[0]
        assert step.card_mask.shape == (NUM_PLAYABLE_CARDS,)
        assert step.card_mask.dtype == torch.bool

    def test_mode_mask_shape_and_dtype(self):
        d = _make_native_dict()
        step = _steps_from_native([d])[0]
        assert step.mode_mask.shape == (NUM_MODES,)
        assert step.mode_mask.dtype == torch.bool

    def test_country_mask_shape_and_dtype(self):
        d = _make_native_dict()
        step = _steps_from_native([d])[0]
        assert step.country_mask is not None
        assert step.country_mask.shape == (NUM_COUNTRIES,)
        assert step.country_mask.dtype == torch.bool


# ---------------------------------------------------------------------------
# Country mask None-handling
# ---------------------------------------------------------------------------

class TestCountryMaskNone:
    """Country mask should be None when all entries are False (SPACE/EVENT)."""

    def test_all_false_country_mask_becomes_none(self):
        d = _make_native_dict(country_mask_all_false=True)
        step = _steps_from_native([d])[0]
        assert step.country_mask is None

    def test_some_true_country_mask_preserved(self):
        d = _make_native_dict(country_targets=[10])
        step = _steps_from_native([d])[0]
        assert step.country_mask is not None
        assert step.country_mask[10].item() is True


# ---------------------------------------------------------------------------
# SmallChoice field tests
# ---------------------------------------------------------------------------

class TestSmallChoiceFields:
    """Test SmallChoice field conversion."""

    def test_sc_fields_present_when_in_dict(self):
        d = _make_native_dict(
            small_choice_target=2,
            small_choice_n_options=4,
            small_choice_logprob=-0.5,
        )
        step = _steps_from_native([d])[0]
        assert step.small_choice_target == 2
        assert step.small_choice_n_options == 4
        assert abs(step.small_choice_logprob - (-0.5)) < 1e-6

    def test_sc_defaults_when_absent(self):
        """If SmallChoice keys are missing, defaults should apply."""
        d = _make_native_dict()
        del d["small_choice_target"]
        del d["small_choice_n_options"]
        del d["small_choice_logprob"]

        step = _steps_from_native([d])[0]
        assert step.small_choice_target == -1
        assert step.small_choice_n_options == 0
        assert step.small_choice_logprob == 0.0

    def test_sc_no_decision_values(self):
        d = _make_native_dict(
            small_choice_target=-1,
            small_choice_n_options=0,
            small_choice_logprob=0.0,
        )
        step = _steps_from_native([d])[0]
        assert step.small_choice_target == -1


# ---------------------------------------------------------------------------
# Edge cases
# ---------------------------------------------------------------------------

class TestEdgeCases:
    """Edge cases in step conversion."""

    def test_empty_country_targets(self):
        d = _make_native_dict(country_targets=[])
        step = _steps_from_native([d])[0]
        assert step.country_targets == []

    def test_max_card_idx(self):
        d = _make_native_dict(card_idx=110)  # last valid index (111 cards, 0-indexed)
        step = _steps_from_native([d])[0]
        assert step.card_idx == 110

    def test_card_mask_has_correct_card_set(self):
        d = _make_native_dict(card_idx=5)
        step = _steps_from_native([d])[0]
        assert step.card_mask[5].item() is True

    def test_mode_mask_has_correct_mode(self):
        d = _make_native_dict(mode_idx=2)
        step = _steps_from_native([d])[0]
        assert step.mode_mask[2].item() is True

    def test_influence_dtype_float32(self):
        d = _make_native_dict()
        step = _steps_from_native([d])[0]
        assert step.influence.dtype == torch.float32

    def test_country_mask_matches_legal_countries(self):
        d = _make_native_dict(country_targets=[15, 42])
        step = _steps_from_native([d])[0]
        assert step.country_mask is not None
        assert step.country_mask[15].item() is True
        assert step.country_mask[42].item() is True
        assert step.country_mask[30].item() is True  # extra legal country from factory

    def test_raw_influence_preserved(self):
        d = _make_native_dict()
        d["raw_ussr_influence"] = np.arange(86, dtype=np.int16)
        d["raw_us_influence"] = np.arange(86, dtype=np.int16) * 2

        step = _steps_from_native([d])[0]
        assert step.raw_ussr_influence is not None
        assert step.raw_ussr_influence[0] == 0
        assert step.raw_ussr_influence[85] == 85
        assert step.raw_us_influence[1] == 2
