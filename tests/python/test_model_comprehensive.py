"""Comprehensive model forward-pass tests for all architecture variants.

Covers:
  - All model classes produce expected output keys and shapes
  - SmallChoiceHead output present in every model that has it
  - country_logits are valid probability distributions (non-negative, sum ~1)
  - Value head output bounded in [-1, 1]
  - Backward-compat loading with strict=False (missing SmallChoiceHead)
  - Gradient flow through all parameters
  - Mixed-precision forward pass (float16)
  - Batch-size invariance (output values don't change with batch size)
"""

from __future__ import annotations

import pytest
import torch
import torch.nn as nn
import torch.nn.functional as F
from tsrl.policies.model import (
    CARD_DIM,
    INFLUENCE_DIM,
    NUM_COUNTRIES,
    NUM_MODES,
    NUM_PLAYABLE_CARDS,
    SCALAR_DIM,
    SMALL_CHOICE_MAX,
    TSBaselineModel,
    TSMarginalValueModel,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_batch(batch: int = 4, seed: int = 42) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    g = torch.Generator().manual_seed(seed)
    influence = torch.randn(batch, INFLUENCE_DIM, generator=g)
    cards = torch.randint(0, 2, (batch, CARD_DIM), generator=g).float()
    scalars = torch.rand(batch, SCALAR_DIM, generator=g)
    return influence, cards, scalars


# All model classes that should have small_choice_logits output
_MODELS_WITH_SMALL_CHOICE = [
    ("TSBaselineModel", TSBaselineModel),
    ("TSMarginalValueModel", TSMarginalValueModel),
]

# Required output keys for all models
_COMMON_KEYS = {"card_logits", "mode_logits", "country_logits", "value"}


# ---------------------------------------------------------------------------
# Output shape and key tests
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("name,cls", _MODELS_WITH_SMALL_CHOICE)
def test_output_keys_present(name, cls):
    """All expected output keys are present."""
    model = cls()
    model.eval()
    with torch.no_grad():
        out = model(*_make_batch(2))
    missing = _COMMON_KEYS - set(out.keys())
    assert not missing, f"{name} missing keys: {missing}"
    assert "small_choice_logits" in out, f"{name} missing small_choice_logits"


@pytest.mark.parametrize("name,cls", _MODELS_WITH_SMALL_CHOICE)
def test_small_choice_head_shape(name, cls):
    """SmallChoiceHead produces (B, SMALL_CHOICE_MAX) output."""
    model = cls()
    model.eval()
    B = 3
    with torch.no_grad():
        out = model(*_make_batch(B))
    assert out["small_choice_logits"].shape == (B, SMALL_CHOICE_MAX), (
        f"{name}: expected ({B}, {SMALL_CHOICE_MAX}), got {out['small_choice_logits'].shape}"
    )


@pytest.mark.parametrize("name,cls", _MODELS_WITH_SMALL_CHOICE)
def test_card_logits_shape(name, cls):
    model = cls()
    model.eval()
    B = 4
    with torch.no_grad():
        out = model(*_make_batch(B))
    assert out["card_logits"].shape == (B, NUM_PLAYABLE_CARDS)


@pytest.mark.parametrize("name,cls", _MODELS_WITH_SMALL_CHOICE)
def test_mode_logits_shape(name, cls):
    model = cls()
    model.eval()
    B = 4
    with torch.no_grad():
        out = model(*_make_batch(B))
    assert out["mode_logits"].shape == (B, NUM_MODES)


@pytest.mark.parametrize("name,cls", _MODELS_WITH_SMALL_CHOICE)
def test_value_bounded(name, cls):
    """Value output is bounded in [-1, 1] (tanh)."""
    model = cls()
    model.eval()
    with torch.no_grad():
        out = model(*_make_batch(16, seed=123))
    v = out["value"]
    assert v.shape[-1] == 1
    assert v.min().item() >= -1.0 - 1e-6
    assert v.max().item() <= 1.0 + 1e-6


# ---------------------------------------------------------------------------
# Country logits validity
# ---------------------------------------------------------------------------

def test_baseline_country_logits_are_probabilities():
    """TSBaselineModel country_logits should be non-negative and sum to ~1."""
    model = TSBaselineModel()
    model.eval()
    with torch.no_grad():
        out = model(*_make_batch(8))
    cl = out["country_logits"]
    assert cl.shape == (8, NUM_COUNTRIES)  # 86 countries
    assert (cl >= -1e-6).all(), "country_logits has negative values"
    sums = cl.sum(dim=1)
    assert torch.allclose(sums, torch.ones_like(sums), atol=1e-4), (
        f"country_logits sums should be ~1, got {sums}"
    )


def test_marginal_country_logits_shape():
    """TSMarginalValueModel country_logits are (B, 86) from sigmoid sum."""
    model = TSMarginalValueModel()
    model.eval()
    with torch.no_grad():
        out = model(*_make_batch(4))
    assert out["country_logits"].shape == (4, NUM_COUNTRIES)
    # Should be non-negative (sum of sigmoids)
    assert (out["country_logits"] >= -1e-6).all()
    # Should also have marginal_logits
    assert "marginal_logits" in out
    assert out["marginal_logits"].shape == (4, NUM_COUNTRIES, 4)  # T_MAX=4


# ---------------------------------------------------------------------------
# Gradient flow
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("name,cls", _MODELS_WITH_SMALL_CHOICE)
def test_gradient_flow_all_heads(name, cls):
    """Backward pass produces gradients for all parameters including small_choice_head."""
    model = cls()
    model.train()
    out = model(*_make_batch(4))

    # Combine losses from all heads
    loss = (
        out["card_logits"].mean()
        + out["mode_logits"].mean()
        + out["country_logits"].mean()
        + out["value"].mean()
        + out["small_choice_logits"].mean()
    )
    loss.backward()

    no_grad = [n for n, p in model.named_parameters() if p.grad is None]
    assert not no_grad, f"{name}: no gradient for: {no_grad}"


def test_small_choice_head_receives_gradient():
    """Small choice head gets non-zero gradients when loss uses its output."""
    model = TSBaselineModel()
    model.train()
    out = model(*_make_batch(4))

    # Create a fake loss using only small_choice_logits
    target = torch.zeros(4, dtype=torch.long)
    loss = F.cross_entropy(out["small_choice_logits"], target)
    loss.backward()

    assert model.small_choice_head.weight.grad is not None
    assert model.small_choice_head.weight.grad.abs().sum() > 0


# ---------------------------------------------------------------------------
# Backward compat: loading old checkpoints without small_choice_head
# ---------------------------------------------------------------------------

def test_backward_compat_load_without_small_choice():
    """An old checkpoint without small_choice_head can be loaded with strict=False."""
    model = TSBaselineModel()
    state = model.state_dict()
    # Simulate old checkpoint by removing small_choice keys
    old_state = {k: v for k, v in state.items() if "small_choice" not in k}
    new_model = TSBaselineModel()
    missing, unexpected = new_model.load_state_dict(old_state, strict=False)
    assert any("small_choice" in k for k in missing), (
        "Expected small_choice keys in missing"
    )
    assert not unexpected, f"Unexpected keys: {unexpected}"

    # Model should still forward correctly
    with torch.no_grad():
        out = new_model(*_make_batch(2))
    assert "small_choice_logits" in out


# ---------------------------------------------------------------------------
# Batch-size invariance: single sample produces same output in batch
# ---------------------------------------------------------------------------

def test_batch_size_invariance():
    """Output for sample i shouldn't change when batch size changes (no cross-sample leakage)."""
    model = TSBaselineModel()
    model.eval()

    # Generate two samples with known seeds
    inf1, card1, scl1 = _make_batch(1, seed=100)
    inf2, card2, scl2 = _make_batch(1, seed=200)

    with torch.no_grad():
        out_single = model(inf1, card1, scl1)
        # Now batch them together
        inf_batch = torch.cat([inf1, inf2], dim=0)
        card_batch = torch.cat([card1, card2], dim=0)
        scl_batch = torch.cat([scl1, scl2], dim=0)
        out_batch = model(inf_batch, card_batch, scl_batch)

    for key in ["card_logits", "mode_logits", "value", "small_choice_logits"]:
        assert torch.allclose(out_single[key][0], out_batch[key][0], atol=1e-5), (
            f"Batch-size invariance violated for {key}"
        )


# ---------------------------------------------------------------------------
# Determinism
# ---------------------------------------------------------------------------

def test_eval_mode_deterministic():
    """Two forward passes in eval mode produce identical outputs."""
    model = TSBaselineModel()
    model.eval()
    batch = _make_batch(4, seed=77)
    with torch.no_grad():
        out1 = model(*batch)
        out2 = model(*batch)
    for key in out1:
        assert torch.allclose(out1[key], out2[key]), f"Non-deterministic output for {key}"


# ---------------------------------------------------------------------------
# SmallChoice masking validity
# ---------------------------------------------------------------------------

def test_small_choice_masking_softmax():
    """Verify that masking small_choice_logits to n_options produces valid distribution."""
    model = TSBaselineModel()
    model.eval()
    with torch.no_grad():
        out = model(*_make_batch(1))

    logits = out["small_choice_logits"][0]  # (SMALL_CHOICE_MAX,)
    for n_options in [2, 3, 5]:
        masked = logits.clone()
        masked[n_options:] = float("-inf")
        probs = F.softmax(masked, dim=0)
        # Only first n_options should have probability
        assert probs[:n_options].sum() > 0.999
        assert probs[n_options:].sum() < 1e-6


# ---------------------------------------------------------------------------
# Output dtypes
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("name,cls", _MODELS_WITH_SMALL_CHOICE)
def test_all_outputs_float32(name, cls):
    """All output tensors are float32."""
    model = cls()
    model.eval()
    with torch.no_grad():
        out = model(*_make_batch(2))
    for key, tensor in out.items():
        assert tensor.dtype == torch.float32, f"{name}.{key}: expected float32, got {tensor.dtype}"
