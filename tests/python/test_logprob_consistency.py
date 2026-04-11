"""Integration tests for log-probability computation consistency.

These tests verify that:
  1. Legal masking correctly zeroes illegal actions
  2. Log-probs are finite and negative (valid log-probabilities)
  3. Country log-prob accumulation with repeats works correctly
  4. Mode=SPACE/EVENT produces zero country log-prob (no country targets)
  5. Softmax + log_softmax identity holds after masking
  6. Log-prob is invariant to eval/train mode (no dropout noise in eval)
"""

from __future__ import annotations

from typing import Optional

import pytest
import torch
import torch.nn.functional as F
from tsrl.policies.model import (
    NUM_COUNTRIES,
    NUM_MODES,
    NUM_PLAYABLE_CARDS,
    TSBaselineModel,
    SCALAR_DIM,
    INFLUENCE_DIM,
    CARD_DIM,
)


def compute_log_prob(
    card_logits: torch.Tensor,
    mode_logits: torch.Tensor,
    country_logits: torch.Tensor,
    card_mask: torch.Tensor,
    mode_mask: torch.Tensor,
    country_mask: Optional[torch.Tensor],
    card_idx: int,
    mode_idx: int,
    country_targets: list[int],
) -> torch.Tensor:
    """Reimplementation of train_ppo._compute_log_prob for testing.

    This is a standalone copy so tests don't depend on importing the full
    train_ppo module (which has complex dataclass/import dependencies).
    Any divergence between this and train_ppo._compute_log_prob IS a bug
    to investigate.
    """
    masked_card = card_logits.clone()
    masked_card[~card_mask] = float("-inf")
    log_prob_card = F.log_softmax(masked_card, dim=0)[card_idx]

    masked_mode = mode_logits.clone()
    masked_mode[~mode_mask] = float("-inf")
    log_prob_mode = F.log_softmax(masked_mode, dim=0)[mode_idx]

    log_prob_country = torch.tensor(0.0, device=card_logits.device)
    if country_targets and country_mask is not None:
        probs = country_logits.clone()
        probs[~country_mask] = 0.0
        probs = probs / (probs.sum() + 1e-10)
        for c in country_targets:
            log_prob_country = log_prob_country + torch.log(probs[c] + 1e-10)

    return log_prob_card + log_prob_mode + log_prob_country


@pytest.fixture(scope="module")
def model():
    m = TSBaselineModel()
    m.eval()
    return m


def _random_masks(seed=42):
    """Generate random but valid masks."""
    g = torch.Generator().manual_seed(seed)
    card_mask = torch.rand(NUM_PLAYABLE_CARDS, generator=g) > 0.7  # ~30% legal
    card_mask[0] = True  # ensure at least one legal
    mode_mask = torch.zeros(NUM_MODES, dtype=torch.bool)
    mode_mask[0] = True  # at least influence mode legal
    mode_mask[torch.randint(0, NUM_MODES, (1,), generator=g).item()] = True
    country_mask = torch.rand(NUM_COUNTRIES, generator=g) > 0.5
    country_mask[0] = True  # at least one legal
    return card_mask, mode_mask, country_mask


# ---------------------------------------------------------------------------
# Basic log-prob properties
# ---------------------------------------------------------------------------


def test_log_prob_is_finite_and_negative(model):
    """Log-probabilities should be finite and non-positive."""
    batch = (
        torch.randn(1, INFLUENCE_DIM),
        torch.randint(0, 2, (1, CARD_DIM)).float(),
        torch.rand(1, SCALAR_DIM),
    )
    with torch.no_grad():
        out = model(*batch)

    card_mask, mode_mask, country_mask = _random_masks()
    # Pick a legal card and mode
    legal_cards = card_mask.nonzero(as_tuple=True)[0]
    legal_modes = mode_mask.nonzero(as_tuple=True)[0]
    legal_countries = country_mask.nonzero(as_tuple=True)[0]

    lp = compute_log_prob(
        out["card_logits"][0],
        out["mode_logits"][0],
        out["country_logits"][0],
        card_mask,
        mode_mask,
        country_mask,
        card_idx=legal_cards[0].item(),
        mode_idx=legal_modes[0].item(),
        country_targets=[legal_countries[0].item()],
    )

    assert torch.isfinite(lp), f"log_prob is not finite: {lp}"
    assert lp.item() <= 0.0 + 1e-6, f"log_prob should be <= 0, got {lp.item()}"


def test_log_prob_zero_for_only_legal_action(model):
    """When only one action is legal, its log-prob should be 0 (probability 1)."""
    batch = (
        torch.randn(1, INFLUENCE_DIM),
        torch.randint(0, 2, (1, CARD_DIM)).float(),
        torch.rand(1, SCALAR_DIM),
    )
    with torch.no_grad():
        out = model(*batch)

    # Only one card legal
    card_mask = torch.zeros(NUM_PLAYABLE_CARDS, dtype=torch.bool)
    card_mask[5] = True
    # Only one mode legal
    mode_mask = torch.zeros(NUM_MODES, dtype=torch.bool)
    mode_mask[3] = True  # SPACE
    # No country targets for SPACE mode
    lp = compute_log_prob(
        out["card_logits"][0],
        out["mode_logits"][0],
        out["country_logits"][0],
        card_mask,
        mode_mask,
        None,  # no country mask for SPACE
        card_idx=5,
        mode_idx=3,
        country_targets=[],
    )

    assert abs(lp.item()) < 1e-5, (
        f"Only one legal action: log_prob should be ~0, got {lp.item()}"
    )


# ---------------------------------------------------------------------------
# Masking correctness
# ---------------------------------------------------------------------------


def test_illegal_card_gets_neg_inf_probability(model):
    """An illegal card should have -inf log-probability via masking."""
    batch = (
        torch.randn(1, INFLUENCE_DIM),
        torch.randint(0, 2, (1, CARD_DIM)).float(),
        torch.rand(1, SCALAR_DIM),
    )
    with torch.no_grad():
        out = model(*batch)

    card_mask = torch.ones(NUM_PLAYABLE_CARDS, dtype=torch.bool)
    card_mask[10] = False  # card 10 is illegal
    mode_mask = torch.ones(NUM_MODES, dtype=torch.bool)

    # Compute log_prob for the illegal card
    lp = compute_log_prob(
        out["card_logits"][0],
        out["mode_logits"][0],
        out["country_logits"][0],
        card_mask,
        mode_mask,
        None,
        card_idx=10,
        mode_idx=0,
        country_targets=[],
    )
    assert lp.item() == float("-inf"), (
        f"Illegal card should have -inf log_prob, got {lp.item()}"
    )


def test_illegal_mode_gets_neg_inf_probability(model):
    """An illegal mode should have -inf log-probability via masking."""
    batch = (
        torch.randn(1, INFLUENCE_DIM),
        torch.randint(0, 2, (1, CARD_DIM)).float(),
        torch.rand(1, SCALAR_DIM),
    )
    with torch.no_grad():
        out = model(*batch)

    card_mask = torch.ones(NUM_PLAYABLE_CARDS, dtype=torch.bool)
    mode_mask = torch.zeros(NUM_MODES, dtype=torch.bool)
    mode_mask[0] = True  # only INFLUENCE legal
    mode_mask[2] = False  # COUP is illegal

    lp = compute_log_prob(
        out["card_logits"][0],
        out["mode_logits"][0],
        out["country_logits"][0],
        card_mask,
        mode_mask,
        None,
        card_idx=0,
        mode_idx=2,  # COUP, which is illegal
        country_targets=[],
    )
    assert lp.item() == float("-inf"), (
        f"Illegal mode should have -inf log_prob, got {lp.item()}"
    )


# ---------------------------------------------------------------------------
# Country target accumulation
# ---------------------------------------------------------------------------


def test_country_log_prob_accumulates_for_repeats(model):
    """Multi-ops into same country should multiply (add log-probs)."""
    batch = (
        torch.randn(1, INFLUENCE_DIM),
        torch.randint(0, 2, (1, CARD_DIM)).float(),
        torch.rand(1, SCALAR_DIM),
    )
    with torch.no_grad():
        out = model(*batch)

    card_mask = torch.ones(NUM_PLAYABLE_CARDS, dtype=torch.bool)
    mode_mask = torch.ones(NUM_MODES, dtype=torch.bool)
    country_mask = torch.ones(NUM_COUNTRIES, dtype=torch.bool)

    # Single country target
    lp1 = compute_log_prob(
        out["card_logits"][0], out["mode_logits"][0], out["country_logits"][0],
        card_mask, mode_mask, country_mask,
        card_idx=0, mode_idx=0, country_targets=[5],
    )
    # Same country twice (2 ops into country 5)
    lp2 = compute_log_prob(
        out["card_logits"][0], out["mode_logits"][0], out["country_logits"][0],
        card_mask, mode_mask, country_mask,
        card_idx=0, mode_idx=0, country_targets=[5, 5],
    )

    # log_prob for [5,5] should be card+mode + 2*log(p_country[5])
    # log_prob for [5] should be card+mode + 1*log(p_country[5])
    # Difference should be approximately log(p_country[5])
    diff = lp2.item() - lp1.item()
    assert diff < 0, "Adding more country targets should decrease log-prob"


def test_no_country_targets_gives_zero_country_contribution(model):
    """When country_targets is empty, country log-prob should be 0."""
    batch = (
        torch.randn(1, INFLUENCE_DIM),
        torch.randint(0, 2, (1, CARD_DIM)).float(),
        torch.rand(1, SCALAR_DIM),
    )
    with torch.no_grad():
        out = model(*batch)

    card_mask = torch.ones(NUM_PLAYABLE_CARDS, dtype=torch.bool)
    mode_mask = torch.ones(NUM_MODES, dtype=torch.bool)

    lp_no_country = compute_log_prob(
        out["card_logits"][0], out["mode_logits"][0], out["country_logits"][0],
        card_mask, mode_mask, None,
        card_idx=0, mode_idx=0, country_targets=[],
    )
    lp_with_country = compute_log_prob(
        out["card_logits"][0], out["mode_logits"][0], out["country_logits"][0],
        card_mask, mode_mask, torch.ones(NUM_COUNTRIES, dtype=torch.bool),
        card_idx=0, mode_idx=0, country_targets=[0],
    )
    # With no country targets, lp = card_lp + mode_lp + 0
    # With country targets, lp = card_lp + mode_lp + country_lp
    assert lp_no_country.item() >= lp_with_country.item(), (
        "No country targets should give higher (less negative) log-prob"
    )


# ---------------------------------------------------------------------------
# Eval vs train mode consistency
# ---------------------------------------------------------------------------


def test_eval_mode_log_prob_deterministic():
    """Same inputs should give identical log-probs in eval mode (no dropout)."""
    model = TSBaselineModel()
    model.eval()

    g = torch.Generator().manual_seed(99)
    batch = (
        torch.randn(1, INFLUENCE_DIM, generator=g),
        torch.randint(0, 2, (1, CARD_DIM), generator=g).float(),
        torch.rand(1, SCALAR_DIM, generator=g),
    )
    card_mask, mode_mask, country_mask = _random_masks(seed=99)
    legal_cards = card_mask.nonzero(as_tuple=True)[0]
    legal_countries = country_mask.nonzero(as_tuple=True)[0]

    with torch.no_grad():
        out1 = model(*batch)
        out2 = model(*batch)

    lp1 = compute_log_prob(
        out1["card_logits"][0], out1["mode_logits"][0], out1["country_logits"][0],
        card_mask, mode_mask, country_mask,
        card_idx=legal_cards[0].item(), mode_idx=0,
        country_targets=[legal_countries[0].item()],
    )
    lp2 = compute_log_prob(
        out2["card_logits"][0], out2["mode_logits"][0], out2["country_logits"][0],
        card_mask, mode_mask, country_mask,
        card_idx=legal_cards[0].item(), mode_idx=0,
        country_targets=[legal_countries[0].item()],
    )
    assert abs(lp1.item() - lp2.item()) < 1e-6, (
        f"Eval mode should be deterministic: {lp1.item()} vs {lp2.item()}"
    )


# ---------------------------------------------------------------------------
# Masking + softmax identity
# ---------------------------------------------------------------------------


def test_masked_softmax_sums_to_one():
    """After masking and softmax, legal probabilities should sum to 1."""
    logits = torch.randn(NUM_PLAYABLE_CARDS)
    mask = torch.rand(NUM_PLAYABLE_CARDS) > 0.5
    mask[0] = True  # at least one legal

    masked = logits.clone()
    masked[~mask] = float("-inf")
    probs = F.softmax(masked, dim=0)

    assert abs(probs.sum().item() - 1.0) < 1e-5, (
        f"Masked softmax should sum to 1, got {probs.sum().item()}"
    )
    # Illegal positions should be exactly 0
    assert (probs[~mask] == 0).all(), "Illegal positions should have 0 probability"


def test_masked_log_softmax_consistency():
    """log_softmax after masking should equal log(softmax after masking)."""
    logits = torch.randn(NUM_PLAYABLE_CARDS)
    mask = torch.rand(NUM_PLAYABLE_CARDS) > 0.5
    mask[0] = True

    masked = logits.clone()
    masked[~mask] = float("-inf")
    log_probs = F.log_softmax(masked, dim=0)
    probs = F.softmax(masked, dim=0)

    # For legal positions, log_softmax should equal log(softmax)
    legal = mask.nonzero(as_tuple=True)[0]
    for i in legal:
        expected = torch.log(probs[i])
        assert abs(log_probs[i].item() - expected.item()) < 1e-5


# ---------------------------------------------------------------------------
# Country probability renormalization
# ---------------------------------------------------------------------------


def test_country_prob_renormalization():
    """Country probs after masking should renormalize correctly."""
    # Simulate what _compute_log_prob does for country
    probs = torch.rand(NUM_COUNTRIES)
    probs = probs / probs.sum()  # valid distribution

    mask = torch.rand(NUM_COUNTRIES) > 0.5
    mask[0] = True

    masked_probs = probs.clone()
    masked_probs[~mask] = 0.0
    renormed = masked_probs / (masked_probs.sum() + 1e-10)

    assert abs(renormed[mask].sum().item() - 1.0) < 1e-5
    assert (renormed[~mask] == 0).all()
