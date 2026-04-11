"""Tests for PPO ratio and clipping math.

Catches regressions in:
  - PPO probability ratio computation (exp(new_lp - old_lp))
  - Clipping bounds enforcement
  - Surrogate objective correctness (min of clipped and unclipped)
  - KL divergence approximation
  - Interaction between ratio magnitude and advantage sign
  - Extreme ratio handling (very stale data)
"""

from __future__ import annotations

import pytest
import torch
import torch.nn.functional as F


# ---------------------------------------------------------------------------
# PPO ratio properties
# ---------------------------------------------------------------------------

class TestPPORatio:
    """Test probability ratio = exp(new_log_prob - old_log_prob)."""

    def test_identical_policies_give_ratio_one(self):
        """If policy hasn't changed, ratio should be 1.0."""
        old_lp = torch.tensor([-2.0, -1.5, -3.0, -0.5])
        new_lp = old_lp.clone()
        ratio = torch.exp(new_lp - old_lp)
        torch.testing.assert_close(ratio, torch.ones(4))

    def test_improved_policy_gives_ratio_above_one(self):
        """Higher new log-prob (less negative) → ratio > 1."""
        old_lp = torch.tensor([-3.0])
        new_lp = torch.tensor([-1.0])  # probability increased
        ratio = torch.exp(new_lp - old_lp)
        assert ratio.item() > 1.0

    def test_worsened_policy_gives_ratio_below_one(self):
        """Lower new log-prob (more negative) → ratio < 1."""
        old_lp = torch.tensor([-1.0])
        new_lp = torch.tensor([-3.0])  # probability decreased
        ratio = torch.exp(new_lp - old_lp)
        assert ratio.item() < 1.0

    def test_ratio_always_positive(self):
        """exp() guarantees ratio > 0 for any finite inputs."""
        old_lp = torch.randn(100) * 3
        new_lp = torch.randn(100) * 3
        ratio = torch.exp(new_lp - old_lp)
        assert (ratio > 0).all()

    def test_ratio_is_exp_difference(self):
        """Verify ratio = p_new/p_old via exp(log(p_new) - log(p_old))."""
        old_lp = torch.tensor([-2.0])
        new_lp = torch.tensor([-1.5])
        ratio = torch.exp(new_lp - old_lp)
        # ratio should equal exp(-1.5)/exp(-2.0) = exp(0.5)
        expected = torch.exp(torch.tensor(0.5))
        assert abs(ratio.item() - expected.item()) < 1e-6


# ---------------------------------------------------------------------------
# Clipping tests
# ---------------------------------------------------------------------------

class TestPPOClipping:
    """Test PPO clipping of the probability ratio."""

    @pytest.fixture(params=[0.1, 0.2, 0.3])
    def clip_eps(self, request):
        return request.param

    def test_clip_bounds_enforced(self, clip_eps):
        """Clipped ratio should be in [1 - eps, 1 + eps]."""
        ratios = torch.tensor([0.01, 0.5, 0.9, 1.0, 1.1, 1.5, 10.0])
        clipped = torch.clamp(ratios, 1.0 - clip_eps, 1.0 + clip_eps)

        assert (clipped >= 1.0 - clip_eps - 1e-6).all()
        assert (clipped <= 1.0 + clip_eps + 1e-6).all()

    def test_ratio_near_one_unchanged(self, clip_eps):
        """Ratios within clip range should not be changed."""
        ratio = torch.tensor([1.0, 1.0 + clip_eps * 0.5, 1.0 - clip_eps * 0.5])
        clipped = torch.clamp(ratio, 1.0 - clip_eps, 1.0 + clip_eps)
        torch.testing.assert_close(ratio, clipped)

    def test_extreme_ratio_clipped(self, clip_eps):
        """Very large or small ratios should be clamped."""
        ratio = torch.tensor([100.0])
        clipped = torch.clamp(ratio, 1.0 - clip_eps, 1.0 + clip_eps)
        assert clipped.item() == pytest.approx(1.0 + clip_eps)

        ratio = torch.tensor([0.001])
        clipped = torch.clamp(ratio, 1.0 - clip_eps, 1.0 + clip_eps)
        assert clipped.item() == pytest.approx(1.0 - clip_eps)


# ---------------------------------------------------------------------------
# Surrogate objective tests
# ---------------------------------------------------------------------------

class TestSurrogateObjective:
    """Test the PPO clipped surrogate objective."""

    def _ppo_objective(
        self,
        ratio: torch.Tensor,
        advantages: torch.Tensor,
        clip_eps: float,
    ) -> torch.Tensor:
        """Compute PPO clipped surrogate loss (to minimize)."""
        clipped = torch.clamp(ratio, 1.0 - clip_eps, 1.0 + clip_eps)
        return -torch.min(ratio * advantages, clipped * advantages).mean()

    def test_positive_advantage_prefers_higher_ratio(self):
        """With positive advantage, objective improves as ratio increases (up to clip)."""
        adv = torch.tensor([1.0])
        clip_eps = 0.2

        loss_low = self._ppo_objective(torch.tensor([0.9]), adv, clip_eps)
        loss_high = self._ppo_objective(torch.tensor([1.1]), adv, clip_eps)

        # Higher ratio with positive advantage → lower loss (better)
        assert loss_high < loss_low

    def test_negative_advantage_prefers_lower_ratio(self):
        """With negative advantage, objective prefers lower ratio (reduce bad action)."""
        adv = torch.tensor([-1.0])
        clip_eps = 0.2

        loss_low = self._ppo_objective(torch.tensor([0.9]), adv, clip_eps)
        loss_high = self._ppo_objective(torch.tensor([1.1]), adv, clip_eps)

        # Lower ratio with negative advantage → lower loss
        assert loss_low < loss_high

    def test_zero_advantage_gives_zero_loss(self):
        """With zero advantage, objective should be 0 regardless of ratio."""
        adv = torch.tensor([0.0])
        ratio = torch.tensor([2.0])
        loss = self._ppo_objective(ratio, adv, 0.2)
        assert abs(loss.item()) < 1e-6

    def test_clipping_prevents_too_large_update(self):
        """Clipping should prevent ratio * advantage from growing unboundedly."""
        adv = torch.tensor([10.0])  # large advantage
        clip_eps = 0.2

        # Without clipping, loss would be -ratio * 10 → very negative for large ratio
        ratio_extreme = torch.tensor([100.0])
        loss_clipped = self._ppo_objective(ratio_extreme, adv, clip_eps)

        # The clipped loss should be bounded by -(1 + eps) * advantage
        max_magnitude = (1.0 + clip_eps) * 10.0
        assert abs(loss_clipped.item()) <= max_magnitude + 1e-5

    def test_min_selects_pessimistic_bound(self):
        """PPO min() should select the more conservative estimate."""
        adv = torch.tensor([1.0])
        clip_eps = 0.2

        # Ratio > 1+eps: unclipped gives more, clipped caps it
        ratio = torch.tensor([1.5])
        clipped = torch.clamp(ratio, 0.8, 1.2)
        obj_unclip = ratio * adv
        obj_clip = clipped * adv
        selected = torch.min(obj_unclip, obj_clip)
        assert selected.item() == pytest.approx(obj_clip.item())

    def test_batch_with_mixed_advantages(self):
        """Batch with both positive and negative advantages should work."""
        ratios = torch.tensor([1.1, 0.9, 1.3, 0.7])
        advs = torch.tensor([1.0, -1.0, 0.5, -0.5])
        clip_eps = 0.2

        loss = self._ppo_objective(ratios, advs, clip_eps)
        assert torch.isfinite(loss)


# ---------------------------------------------------------------------------
# Clip fraction metric
# ---------------------------------------------------------------------------

class TestClipFraction:
    """Test clip fraction computation (diagnostic metric)."""

    def test_no_clipping_gives_zero_fraction(self):
        """If all ratios are within clip range, fraction should be 0."""
        ratios = torch.ones(100)  # all exactly 1.0
        clip_eps = 0.2
        clip_frac = ((ratios - 1.0).abs() > clip_eps).float().mean().item()
        assert clip_frac == 0.0

    def test_all_clipped_gives_one_fraction(self):
        """If all ratios are outside clip range, fraction should be 1."""
        ratios = torch.full((100,), 5.0)  # all way above 1+eps
        clip_eps = 0.2
        clip_frac = ((ratios - 1.0).abs() > clip_eps).float().mean().item()
        assert clip_frac == 1.0

    def test_half_clipped(self):
        """50 within, 50 outside → fraction ≈ 0.5."""
        ratios = torch.cat([
            torch.ones(50),       # within
            torch.full((50,), 3.0),  # outside
        ])
        clip_eps = 0.2
        clip_frac = ((ratios - 1.0).abs() > clip_eps).float().mean().item()
        assert abs(clip_frac - 0.5) < 1e-5


# ---------------------------------------------------------------------------
# Approximate KL divergence
# ---------------------------------------------------------------------------

class TestApproxKL:
    """Test approximate KL divergence computation used in train_ppo."""

    def test_identical_policies_zero_kl(self):
        """Identical policies should have KL ≈ 0."""
        old_lp = torch.tensor([-2.0, -1.5, -3.0])
        new_lp = old_lp.clone()
        ratio = torch.exp(new_lp - old_lp)
        approx_kl = ((ratio - 1.0) - (new_lp - old_lp)).mean().item()
        assert abs(approx_kl) < 1e-6

    def test_kl_nonnegative_for_small_changes(self):
        """KL should be approximately non-negative for small policy changes.

        The approximation (ratio - 1) - log(ratio) is always >= 0 analytically
        (since x - 1 >= log(x) for x > 0).
        """
        for _ in range(10):
            old_lp = torch.randn(50) * 2
            new_lp = old_lp + torch.randn(50) * 0.1  # small perturbation
            ratio = torch.exp(new_lp - old_lp)
            # Per-element KL: (ratio - 1) - log(ratio) >= 0
            per_element_kl = (ratio - 1.0) - torch.log(ratio)
            assert (per_element_kl >= -1e-5).all(), \
                f"Per-element KL should be non-negative: min={per_element_kl.min()}"

    def test_large_change_gives_large_kl(self):
        """Large policy change should give large KL."""
        old_lp = torch.tensor([-1.0, -1.0, -1.0])
        new_lp = torch.tensor([-10.0, -10.0, -10.0])  # huge change
        ratio = torch.exp(new_lp - old_lp)
        approx_kl = ((ratio - 1.0) - (new_lp - old_lp)).mean().item()
        assert approx_kl > 1.0, f"Large policy change should give large KL: {approx_kl}"


# ---------------------------------------------------------------------------
# Entropy tests
# ---------------------------------------------------------------------------

class TestEntropy:
    """Test entropy computation from masked logits."""

    def _compute_entropy(self, logits: torch.Tensor, mask: torch.Tensor) -> float:
        """Compute entropy from masked logits."""
        masked = logits.masked_fill(~mask, float("-inf"))
        log_p = F.log_softmax(masked, dim=-1).clamp(min=-20)
        entropy = -(log_p.exp() * log_p).sum(dim=-1)
        return entropy.item()

    def test_uniform_distribution_max_entropy(self):
        """Uniform distribution should have maximum entropy."""
        n_legal = 10
        logits = torch.zeros(20)  # uniform over legal
        mask = torch.zeros(20, dtype=torch.bool)
        mask[:n_legal] = True

        ent = self._compute_entropy(logits, mask)
        expected = torch.log(torch.tensor(float(n_legal))).item()
        assert abs(ent - expected) < 0.1, f"Uniform entropy should be ~{expected}, got {ent}"

    def test_peaked_distribution_low_entropy(self):
        """Very peaked distribution should have low entropy."""
        logits = torch.tensor([100.0, 0.0, 0.0, 0.0, 0.0])
        mask = torch.ones(5, dtype=torch.bool)
        ent = self._compute_entropy(logits, mask)
        assert ent < 0.1, f"Peaked distribution entropy should be ~0, got {ent}"

    def test_single_legal_zero_entropy(self):
        """With only one legal option, entropy should be 0."""
        logits = torch.randn(10)
        mask = torch.zeros(10, dtype=torch.bool)
        mask[3] = True
        ent = self._compute_entropy(logits, mask)
        assert abs(ent) < 1e-4, f"Single legal option entropy should be ~0, got {ent}"

    def test_more_options_higher_entropy(self):
        """More legal options (with uniform logits) should give higher entropy."""
        logits = torch.zeros(20)
        mask_2 = torch.zeros(20, dtype=torch.bool)
        mask_2[:2] = True
        mask_10 = torch.zeros(20, dtype=torch.bool)
        mask_10[:10] = True

        ent_2 = self._compute_entropy(logits, mask_2)
        ent_10 = self._compute_entropy(logits, mask_10)
        assert ent_10 > ent_2

    def test_entropy_nonnegative(self):
        """Entropy should always be non-negative."""
        for _ in range(20):
            logits = torch.randn(111)
            mask = torch.rand(111) > 0.5
            mask[0] = True
            ent = self._compute_entropy(logits, mask)
            assert ent >= -1e-5, f"Entropy should be non-negative: {ent}"
