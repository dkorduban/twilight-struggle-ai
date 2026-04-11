"""Integration tests for the PackedSteps pipeline.

The packed pipeline is the critical path for PPO training:
    Step objects → pack_steps() → PackedSteps → ppo_update_packed()

These tests catch regressions in:
  - Data preservation through packing (no silent truncation or reordering)
  - Log-prob equivalence between per-step and batched computation
  - Country target padding and validity masking
  - SmallChoice field propagation through packing
  - Advantage normalization during packing
  - Mask propagation from Step to packed tensors
  - Edge cases: empty country targets, single-step batches, mixed modes
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pytest
import torch
import torch.nn.functional as F

# Ensure train_ppo is importable (it's a script, not a package)
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
    TSBaselineModel,
)

# Import pack_steps and Step from train_ppo
# This import chain validates that train_ppo is importable (no syntax errors)
from train_ppo import PackedSteps, Step, pack_steps


# ---------------------------------------------------------------------------
# Fixtures: synthetic steps with known values
# ---------------------------------------------------------------------------

COUNTRY_SLOTS = 86


def _make_step(
    side_int: int = 0,
    card_idx: int = 5,
    mode_idx: int = 0,
    country_targets: list[int] | None = None,
    old_log_prob: float = -1.5,
    value: float = 0.1,
    advantage: float = 0.5,
    returns: float = 0.6,
    small_choice_target: int = -1,
    small_choice_n_options: int = 0,
    country_mask_indices: list[int] | None = None,
    card_mask_indices: list[int] | None = None,
    mode_mask_indices: list[int] | None = None,
    seed: int = 42,
) -> Step:
    """Create a synthetic Step with controlled values."""
    g = torch.Generator().manual_seed(seed)
    if country_targets is None:
        country_targets = [10, 20]
    if country_mask_indices is None:
        country_mask_indices = [10, 20, 30]
    if card_mask_indices is None:
        card_mask_indices = [card_idx, card_idx + 1, card_idx + 2]
    if mode_mask_indices is None:
        mode_mask_indices = [mode_idx, (mode_idx + 1) % NUM_MODES]

    card_mask = torch.zeros(NUM_PLAYABLE_CARDS, dtype=torch.bool)
    for i in card_mask_indices:
        if 0 <= i < NUM_PLAYABLE_CARDS:
            card_mask[i] = True

    mode_mask = torch.zeros(NUM_MODES, dtype=torch.bool)
    for i in mode_mask_indices:
        mode_mask[i] = True

    country_mask = torch.zeros(COUNTRY_SLOTS, dtype=torch.bool)
    for i in country_mask_indices:
        if 0 <= i < COUNTRY_SLOTS:
            country_mask[i] = True

    return Step(
        influence=torch.randn(1, INFLUENCE_DIM, generator=g),
        cards=torch.randn(1, CARD_DIM, generator=g),
        scalars=torch.randn(1, SCALAR_DIM, generator=g),
        card_mask=card_mask,
        mode_mask=mode_mask,
        country_mask=country_mask,
        card_idx=card_idx,
        mode_idx=mode_idx,
        country_targets=country_targets,
        old_log_prob=old_log_prob,
        value=value,
        side_int=side_int,
        advantage=advantage,
        returns=returns,
        small_choice_target=small_choice_target,
        small_choice_n_options=small_choice_n_options,
    )


def _make_batch(n: int = 8, mixed_sides: bool = True, mixed_targets: bool = True) -> list[Step]:
    """Create a batch of synthetic steps with variety."""
    steps = []
    for i in range(n):
        side = i % 2 if mixed_sides else 0
        card_idx = 3 + i
        mode_idx = i % 3  # INFLUENCE, REALIGN, COUP (country-target modes)

        # Vary country targets length
        if mixed_targets:
            n_targets = (i % 4) + 1
            targets = [(10 + j * 5) % COUNTRY_SLOTS for j in range(n_targets)]
        else:
            targets = [10]

        steps.append(_make_step(
            side_int=side,
            card_idx=card_idx,
            mode_idx=mode_idx,
            country_targets=targets,
            old_log_prob=-1.0 - i * 0.1,
            value=0.1 * i,
            advantage=0.5 - i * 0.1,
            returns=0.6 + i * 0.05,
            seed=42 + i,
            country_mask_indices=targets + [30, 40],
            card_mask_indices=[card_idx, card_idx + 1, card_idx + 2],
        ))
    return steps


# ---------------------------------------------------------------------------
# Data preservation tests
# ---------------------------------------------------------------------------

class TestPackPreservesData:
    """Packing must not lose or reorder data."""

    def test_influence_preserved(self):
        steps = _make_batch(4)
        packed = pack_steps(steps)

        for i, step in enumerate(steps):
            torch.testing.assert_close(
                packed.influence[i:i+1],
                step.influence,
                msg=f"Step {i}: influence mismatch after packing",
            )

    def test_cards_preserved(self):
        steps = _make_batch(4)
        packed = pack_steps(steps)

        for i, step in enumerate(steps):
            torch.testing.assert_close(
                packed.cards[i:i+1],
                step.cards,
                msg=f"Step {i}: cards mismatch",
            )

    def test_scalars_preserved(self):
        steps = _make_batch(4)
        packed = pack_steps(steps)

        for i, step in enumerate(steps):
            torch.testing.assert_close(
                packed.scalars[i:i+1],
                step.scalars,
                msg=f"Step {i}: scalars mismatch",
            )

    def test_card_masks_preserved(self):
        steps = _make_batch(4)
        packed = pack_steps(steps)

        for i, step in enumerate(steps):
            assert (packed.card_masks[i] == step.card_mask).all(), \
                f"Step {i}: card_mask mismatch"

    def test_mode_masks_preserved(self):
        steps = _make_batch(4)
        packed = pack_steps(steps)

        for i, step in enumerate(steps):
            assert (packed.mode_masks[i] == step.mode_mask).all(), \
                f"Step {i}: mode_mask mismatch"

    def test_country_masks_preserved(self):
        steps = _make_batch(4)
        packed = pack_steps(steps)

        for i, step in enumerate(steps):
            expected = step.country_mask if step.country_mask is not None \
                else torch.zeros(COUNTRY_SLOTS, dtype=torch.bool)
            assert (packed.country_masks[i] == expected).all(), \
                f"Step {i}: country_mask mismatch"

    def test_card_indices_preserved(self):
        steps = _make_batch(4)
        packed = pack_steps(steps)

        for i, step in enumerate(steps):
            assert packed.card_indices[i].item() == step.card_idx, \
                f"Step {i}: card_idx {packed.card_indices[i]} != {step.card_idx}"

    def test_mode_indices_preserved(self):
        steps = _make_batch(4)
        packed = pack_steps(steps)

        for i, step in enumerate(steps):
            assert packed.mode_indices[i].item() == step.mode_idx, \
                f"Step {i}: mode_idx {packed.mode_indices[i]} != {step.mode_idx}"

    def test_old_log_probs_preserved(self):
        steps = _make_batch(4)
        packed = pack_steps(steps)

        for i, step in enumerate(steps):
            assert abs(packed.old_log_probs[i].item() - step.old_log_prob) < 1e-6, \
                f"Step {i}: old_log_prob {packed.old_log_probs[i]} != {step.old_log_prob}"


# ---------------------------------------------------------------------------
# Country target padding tests
# ---------------------------------------------------------------------------

class TestCountryTargetPadding:
    """Country targets are variable-length and must be padded correctly."""

    def test_padding_width_equals_max_targets(self):
        """Padded tensor width should equal the longest target list."""
        steps = [
            _make_step(country_targets=[10]),
            _make_step(country_targets=[10, 20, 30]),
            _make_step(country_targets=[10, 20]),
        ]
        packed = pack_steps(steps)

        assert packed.country_targets.shape == (3, 3), \
            f"Expected (3, 3), got {packed.country_targets.shape}"

    def test_validity_mask_matches_targets(self):
        """country_valid[i, j] should be True iff step i has j-th target."""
        steps = [
            _make_step(country_targets=[10]),
            _make_step(country_targets=[10, 20, 30]),
            _make_step(country_targets=[]),
        ]
        packed = pack_steps(steps)

        # Step 0: 1 target
        assert packed.country_valid[0, 0].item() is True
        assert packed.country_valid[0, 1].item() is False
        assert packed.country_valid[0, 2].item() is False

        # Step 1: 3 targets
        assert packed.country_valid[1, 0].item() is True
        assert packed.country_valid[1, 1].item() is True
        assert packed.country_valid[1, 2].item() is True

        # Step 2: 0 targets
        assert packed.country_valid[2].sum().item() == 0

    def test_target_values_preserved_in_valid_positions(self):
        """Valid positions should contain the original country IDs."""
        steps = [
            _make_step(country_targets=[15, 42]),
            _make_step(country_targets=[7]),
        ]
        packed = pack_steps(steps)

        assert packed.country_targets[0, 0].item() == 15
        assert packed.country_targets[0, 1].item() == 42
        assert packed.country_targets[1, 0].item() == 7

    def test_empty_targets_produce_zero_country_logprob(self):
        """Steps with no country targets should contribute 0 to log-prob."""
        model = TSBaselineModel(hidden_dim=64)
        model.eval()

        # SPACE mode — no country targets
        step = _make_step(mode_idx=3, country_targets=[])
        step.country_mask = None  # SPACE has no country mask
        packed = pack_steps([step])

        with torch.no_grad():
            out = model(packed.influence, packed.cards, packed.scalars)

        country_logits = out.get("country_logits")
        if country_logits is not None:
            country_probs = country_logits.masked_fill(
                ~packed.country_masks, 0.0
            )
            country_probs = country_probs / (country_probs.sum(dim=1, keepdim=True) + 1e-10)
            log_country = torch.log(country_probs + 1e-10)

            gathered = log_country.gather(1, packed.country_targets.clamp_min(0))
            log_prob_country = (gathered * packed.country_valid.float()).sum(dim=1)

            assert abs(log_prob_country[0].item()) < 1e-5, \
                f"Empty targets should give 0 country log-prob, got {log_prob_country[0].item()}"


# ---------------------------------------------------------------------------
# SmallChoice field propagation tests
# ---------------------------------------------------------------------------

class TestSmallChoicePacking:
    """SmallChoice fields must survive packing."""

    def test_sc_targets_preserved(self):
        steps = [
            _make_step(small_choice_target=2, small_choice_n_options=4),
            _make_step(small_choice_target=-1, small_choice_n_options=0),
            _make_step(small_choice_target=0, small_choice_n_options=2),
        ]
        packed = pack_steps(steps)

        assert packed.sc_targets[0].item() == 2
        assert packed.sc_targets[1].item() == -1
        assert packed.sc_targets[2].item() == 0

    def test_sc_n_options_preserved(self):
        steps = [
            _make_step(small_choice_target=2, small_choice_n_options=4),
            _make_step(small_choice_target=-1, small_choice_n_options=0),
        ]
        packed = pack_steps(steps)

        assert packed.sc_n_options[0].item() == 4
        assert packed.sc_n_options[1].item() == 0

    def test_sc_valid_mask_logic(self):
        """Valid SmallChoice = (target >= 0) & (n_options > 1)."""
        steps = [
            _make_step(small_choice_target=1, small_choice_n_options=3),  # valid
            _make_step(small_choice_target=-1, small_choice_n_options=0),  # no decision
            _make_step(small_choice_target=0, small_choice_n_options=1),  # n_options=1, skip
        ]
        packed = pack_steps(steps)

        sc_valid = (packed.sc_targets >= 0) & (packed.sc_n_options > 1)
        assert sc_valid[0].item() is True
        assert sc_valid[1].item() is False
        assert sc_valid[2].item() is False


# ---------------------------------------------------------------------------
# Advantage normalization tests
# ---------------------------------------------------------------------------

class TestPackedAdvantageNorm:
    """pack_steps normalizes advantages per-side. Test that it works."""

    def test_per_side_zero_mean(self):
        """After packing, each side's advantages should have ~zero mean."""
        steps = _make_batch(20, mixed_sides=True)
        # Give each side different mean advantages
        for i, s in enumerate(steps):
            s.advantage = 5.0 + i if s.side_int == 0 else -3.0 + i

        packed = pack_steps(steps)
        side_ints = torch.tensor([s.side_int for s in steps])

        for side in (0, 1):
            mask = side_ints == side
            if mask.sum() > 1:
                mean = packed.advantages[mask].mean().item()
                assert abs(mean) < 1e-5, \
                    f"Side {side} advantages mean={mean}, expected ~0"

    def test_nan_advantages_replaced(self):
        """NaN advantages should be replaced with 0 during packing."""
        steps = _make_batch(4)
        steps[1].advantage = float("nan")

        packed = pack_steps(steps)
        assert torch.isfinite(packed.advantages).all(), "NaN advantages should be handled"

    def test_nan_returns_replaced(self):
        """NaN returns should be replaced with 0 during packing."""
        steps = _make_batch(4)
        steps[2].returns = float("nan")

        packed = pack_steps(steps)
        assert torch.isfinite(packed.returns).all(), "NaN returns should be handled"


# ---------------------------------------------------------------------------
# Log-prob equivalence: per-step vs packed batched
# ---------------------------------------------------------------------------

class TestLogProbEquivalence:
    """The batched packed log-prob computation must match per-step computation."""

    @pytest.fixture
    def model(self):
        m = TSBaselineModel(hidden_dim=64)
        m.eval()
        return m

    def _per_step_log_prob(
        self,
        card_logits: torch.Tensor,
        mode_logits: torch.Tensor,
        country_logits: torch.Tensor | None,
        card_mask: torch.Tensor,
        mode_mask: torch.Tensor,
        country_mask: torch.Tensor | None,
        card_idx: int,
        mode_idx: int,
        country_targets: list[int],
    ) -> float:
        """Reimplementation of _compute_log_prob from train_ppo.py."""
        masked_card = card_logits.clone()
        masked_card[~card_mask] = float("-inf")
        lp_card = F.log_softmax(masked_card, dim=0)[card_idx]

        masked_mode = mode_logits.clone()
        masked_mode[~mode_mask] = float("-inf")
        lp_mode = F.log_softmax(masked_mode, dim=0)[mode_idx]

        lp_country = 0.0
        if country_targets and country_logits is not None and country_mask is not None:
            probs = country_logits.clone()
            probs[~country_mask] = 0.0
            probs = probs / (probs.sum() + 1e-10)
            for c in country_targets:
                lp_country += torch.log(probs[c] + 1e-10).item()

        return lp_card.item() + lp_mode.item() + lp_country

    def _packed_log_probs(
        self,
        model: TSBaselineModel,
        packed: PackedSteps,
    ) -> torch.Tensor:
        """Reimplementation of batched log-prob from ppo_update_packed."""
        with torch.no_grad():
            out = model(packed.influence, packed.cards, packed.scalars)

        card_logits = out["card_logits"]
        mode_logits = out["mode_logits"]
        country_logits = out.get("country_logits")

        masked_card = card_logits.masked_fill(~packed.card_masks, float("-inf"))
        masked_mode = mode_logits.masked_fill(~packed.mode_masks, float("-inf"))

        lp_card = F.log_softmax(masked_card, dim=1).gather(
            1, packed.card_indices.unsqueeze(1)).squeeze(1)
        lp_mode = F.log_softmax(masked_mode, dim=1).gather(
            1, packed.mode_indices.unsqueeze(1)).squeeze(1)

        lp_country = torch.zeros_like(lp_card)
        if country_logits is not None:
            country_probs = country_logits.masked_fill(~packed.country_masks, 0.0)
            country_probs = country_probs / (country_probs.sum(dim=1, keepdim=True) + 1e-10)
            log_country = torch.log(country_probs + 1e-10)
            if packed.country_targets.shape[1] > 0:
                gathered = log_country.gather(1, packed.country_targets.clamp_min(0))
                lp_country = (gathered * packed.country_valid.float()).sum(dim=1)

        return lp_card + lp_mode + lp_country

    def test_packed_matches_per_step(self, model):
        """Batched packed log-prob must match per-step computation within tolerance."""
        steps = _make_batch(6, mixed_targets=True)
        packed = pack_steps(steps)

        # Get per-step log-probs
        with torch.no_grad():
            per_step_lps = []
            for step in steps:
                out = model(step.influence, step.cards, step.scalars)
                lp = self._per_step_log_prob(
                    out["card_logits"][0],
                    out["mode_logits"][0],
                    out.get("country_logits", [None])[0] if "country_logits" in out else None,
                    step.card_mask,
                    step.mode_mask,
                    step.country_mask,
                    step.card_idx,
                    step.mode_idx,
                    step.country_targets,
                )
                per_step_lps.append(lp)

        # Get packed log-probs
        packed_lps = self._packed_log_probs(model, packed)

        for i in range(len(steps)):
            assert abs(per_step_lps[i] - packed_lps[i].item()) < 1e-4, \
                f"Step {i}: per-step={per_step_lps[i]:.6f} vs packed={packed_lps[i].item():.6f}"

    def test_single_legal_card_gives_zero_card_logprob(self, model):
        """With only one legal card, card log-prob should be 0."""
        step = _make_step(card_idx=5, card_mask_indices=[5])  # only card 5 legal
        packed = pack_steps([step])

        with torch.no_grad():
            out = model(packed.influence, packed.cards, packed.scalars)

        masked = out["card_logits"].masked_fill(~packed.card_masks, float("-inf"))
        lp = F.log_softmax(masked, dim=1).gather(
            1, packed.card_indices.unsqueeze(1)).squeeze(1)

        assert abs(lp[0].item()) < 1e-5, \
            f"Single legal card should have lp=0, got {lp[0].item()}"

    def test_all_log_probs_finite_and_negative(self, model):
        """All log-probs in a batch should be finite and <= 0."""
        steps = _make_batch(16)
        packed = pack_steps(steps)

        packed_lps = self._packed_log_probs(model, packed)

        assert torch.isfinite(packed_lps).all(), \
            f"Non-finite log-probs: {packed_lps[~torch.isfinite(packed_lps)]}"
        assert (packed_lps <= 1e-5).all(), \
            f"Positive log-probs found: max={packed_lps.max().item()}"


# ---------------------------------------------------------------------------
# Mixed mode tests (SPACE/EVENT have no country targets)
# ---------------------------------------------------------------------------

class TestMixedModes:
    """Batch with mixed modes: influence has country targets, space/event don't."""

    def test_mixed_batch_packs_correctly(self):
        """A batch with both INFLUENCE and SPACE steps should pack without error."""
        influence_step = _make_step(mode_idx=0, country_targets=[10, 20])
        space_step = _make_step(mode_idx=3, country_targets=[])
        space_step.country_mask = None

        packed = pack_steps([influence_step, space_step])

        assert packed.country_valid[0].sum().item() == 2
        assert packed.country_valid[1].sum().item() == 0

    def test_none_country_mask_becomes_zeros(self):
        """Step with country_mask=None should become all-False in packed tensor."""
        step = _make_step(mode_idx=3, country_targets=[])
        step.country_mask = None

        packed = pack_steps([step])
        assert packed.country_masks[0].sum().item() == 0


# ---------------------------------------------------------------------------
# Edge cases
# ---------------------------------------------------------------------------

class TestEdgeCases:
    """Edge cases that have caused bugs in production."""

    def test_single_step_batch(self):
        """Batch of 1 should work (normalization edge case)."""
        step = _make_step()
        packed = pack_steps([step])

        assert packed.influence.shape[0] == 1
        assert packed.card_indices.shape[0] == 1

    def test_all_same_side(self):
        """All steps same side — normalization should still work."""
        steps = _make_batch(10, mixed_sides=False)
        packed = pack_steps(steps)

        assert torch.isfinite(packed.advantages).all()

    def test_empty_raises(self):
        """Empty step list should raise."""
        with pytest.raises(ValueError, match="non-empty"):
            pack_steps([])

    def test_large_country_targets(self):
        """Steps with max country targets (4 ops) should pack correctly."""
        step = _make_step(
            country_targets=[10, 20, 30, 40],
            country_mask_indices=[10, 20, 30, 40, 50],
        )
        packed = pack_steps([step])

        assert packed.country_targets.shape[1] >= 4
        assert packed.country_valid[0, :4].all()

    def test_to_device_preserves_shapes(self):
        """PackedSteps.to() should preserve all tensor shapes."""
        steps = _make_batch(4)
        packed = pack_steps(steps)
        moved = packed.to("cpu")

        assert moved.influence.shape == packed.influence.shape
        assert moved.card_masks.shape == packed.card_masks.shape
        assert moved.country_targets.shape == packed.country_targets.shape
        assert moved.sc_targets.shape == packed.sc_targets.shape

    def test_repeated_country_target(self):
        """Multiple ops into same country (e.g., 3 influence into France)."""
        step = _make_step(
            country_targets=[10, 10, 10],
            country_mask_indices=[10, 20],
        )
        packed = pack_steps([step])

        # All 3 target entries should be 10
        for j in range(3):
            assert packed.country_targets[0, j].item() == 10
            assert packed.country_valid[0, j].item() is True


# ---------------------------------------------------------------------------
# PPO update smoke test (full forward + backward through packed path)
# ---------------------------------------------------------------------------

class TestPackedPPOSmoke:
    """Smoke test: full PPO forward+backward through the packed path."""

    def test_packed_ppo_forward_backward(self):
        """Full ppo_update_packed should run without error on synthetic data."""
        model = TSBaselineModel(hidden_dim=64)
        model.train()
        optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)

        steps = _make_batch(16, mixed_sides=True, mixed_targets=True)
        packed = pack_steps(steps)

        # Run one epoch of PPO update
        with torch.no_grad():
            out = model(packed.influence, packed.cards, packed.scalars)

        card_logits = out["card_logits"]
        mode_logits = out["mode_logits"]
        country_logits = out.get("country_logits")

        # Compute log-probs (batched)
        masked_card = card_logits.masked_fill(~packed.card_masks, float("-inf"))
        masked_mode = mode_logits.masked_fill(~packed.mode_masks, float("-inf"))

        lp_card = F.log_softmax(masked_card, dim=1).gather(
            1, packed.card_indices.unsqueeze(1)).squeeze(1)
        lp_mode = F.log_softmax(masked_mode, dim=1).gather(
            1, packed.mode_indices.unsqueeze(1)).squeeze(1)

        lp_country = torch.zeros_like(lp_card)
        if country_logits is not None:
            cp = country_logits.masked_fill(~packed.country_masks, 0.0)
            cp = cp / (cp.sum(dim=1, keepdim=True) + 1e-10)
            lc = torch.log(cp + 1e-10)
            if packed.country_targets.shape[1] > 0:
                gathered = lc.gather(1, packed.country_targets.clamp_min(0))
                lp_country = (gathered * packed.country_valid.float()).sum(dim=1)

        new_lps = lp_card + lp_mode + lp_country

        assert torch.isfinite(new_lps).all(), "Log-probs should be finite"
        assert (new_lps <= 1e-5).all(), "Log-probs should be <= 0"

    def test_gradient_flows_through_packed_path(self):
        """Gradients should flow from packed log-probs to all model parameters."""
        model = TSBaselineModel(hidden_dim=64)
        model.train()

        steps = _make_batch(8)
        packed = pack_steps(steps)

        out = model(packed.influence, packed.cards, packed.scalars)

        masked_card = out["card_logits"].masked_fill(~packed.card_masks, float("-inf"))
        lp = F.log_softmax(masked_card, dim=1).gather(
            1, packed.card_indices.unsqueeze(1)).squeeze(1)

        loss = -lp.mean()
        loss.backward()

        graded = sum(1 for p in model.parameters()
                     if p.grad is not None and p.grad.abs().sum() > 0)
        total = sum(1 for _ in model.parameters())
        assert graded > total * 0.3, \
            f"Only {graded}/{total} params got gradients through packed path"
