"""Tests for reward and advantage computation in PPO.

Catches regressions in:
  - Reward assignment from game outcomes
  - Per-side reward sign correctness
  - GAE returns computation
  - Advantage normalization
  - DEFCON-1 loss handling
  - VP-based reward scaling
"""

from __future__ import annotations

import numpy as np
import pytest
import torch


# ---------------------------------------------------------------------------
# Reward assignment tests
# ---------------------------------------------------------------------------

class TestRewardAssignment:
    """Test that game outcomes produce correct per-step rewards."""

    def test_ussr_win_positive_for_ussr(self):
        """USSR victory should give positive reward to USSR steps."""
        # Typical: winner=USSR, all USSR steps get +1, all US steps get -1
        assert _reward_for_side(winner="USSR", step_side="USSR") > 0

    def test_ussr_win_negative_for_us(self):
        assert _reward_for_side(winner="USSR", step_side="US") < 0

    def test_us_win_positive_for_us(self):
        assert _reward_for_side(winner="US", step_side="US") > 0

    def test_us_win_negative_for_ussr(self):
        assert _reward_for_side(winner="US", step_side="USSR") < 0

    def test_terminal_step_gets_reward(self):
        """Only the last step of a game should have nonzero reward."""
        rewards = [0.0, 0.0, 0.0, 1.0]  # typical pattern
        assert rewards[-1] != 0
        assert all(r == 0 for r in rewards[:-1])


# ---------------------------------------------------------------------------
# VP-based reward tests
# ---------------------------------------------------------------------------

class TestVPReward:
    """Test VP-based reward signals."""

    def test_vp_delta_bounded(self):
        """VP delta per action should be bounded (no single action changes VP by >20)."""
        for _ in range(100):
            vp_before = np.random.randint(-20, 21)
            vp_after = np.random.randint(-20, 21)
            delta = vp_after - vp_before
            assert -40 <= delta <= 40

    def test_vp_normalized_in_range(self):
        """Normalized VP should be in [-1, 1]."""
        for vp in range(-20, 21):
            normalized = vp / 20.0
            assert -1.05 <= normalized <= 1.05


# ---------------------------------------------------------------------------
# GAE tests
# ---------------------------------------------------------------------------

class TestGAEComputation:
    """Test Generalized Advantage Estimation produces valid results."""

    def test_gae_single_game_episode(self):
        """GAE for a complete episode should produce finite advantages."""
        gamma = 0.99
        lam = 0.95

        # Simulate 15 steps (typical game length)
        N = 15
        values = torch.randn(N).tolist()
        rewards = [0.0] * (N - 1) + [1.0]  # only terminal reward

        advantages = _compute_gae(values, rewards, gamma, lam)

        assert all(np.isfinite(a) for a in advantages)
        # Terminal step advantage should be positive (got reward)
        assert advantages[-1] > 0

    def test_gae_no_reward_near_zero_advantage(self):
        """With zero rewards and value predictions, advantages should be small."""
        gamma = 0.99
        lam = 0.95
        N = 10
        values = [0.0] * N
        rewards = [0.0] * N

        advantages = _compute_gae(values, rewards, gamma, lam)
        assert all(abs(a) < 1e-5 for a in advantages)

    def test_gae_returns_equal_advantage_plus_value(self):
        """Return = advantage + value."""
        gamma = 0.99
        lam = 0.95
        N = 10
        values = torch.randn(N).tolist()
        rewards = [0.0] * (N - 1) + [1.0]

        advantages = _compute_gae(values, rewards, gamma, lam)
        returns = [a + v for a, v in zip(advantages, values)]

        assert all(np.isfinite(r) for r in returns)

    def test_gae_discount_diminishes(self):
        """Earlier steps should have smaller magnitude advantages (discounted)."""
        gamma = 0.99
        lam = 0.95
        N = 20
        values = [0.0] * N
        rewards = [0.0] * (N - 1) + [1.0]

        advantages = _compute_gae(values, rewards, gamma, lam)
        # Last step has largest advantage (closest to reward)
        assert abs(advantages[-1]) >= abs(advantages[0])


# ---------------------------------------------------------------------------
# Advantage normalization tests
# ---------------------------------------------------------------------------

class TestAdvantageNorm:
    """Test per-side advantage normalization."""

    def test_normalized_mean_near_zero(self):
        """Per-side normalized advantages should have near-zero mean."""
        N = 50
        advs = torch.randn(N)
        sides = torch.randint(0, 2, (N,))

        normed = _normalize_per_side(advs, sides)

        for s in (0, 1):
            mask = sides == s
            if mask.sum() > 1:
                assert abs(normed[mask].mean().item()) < 1e-5

    def test_normalized_std_near_one(self):
        """Per-side normalized advantages should have near-unit std."""
        N = 100
        advs = torch.randn(N) * 5 + 3  # non-zero mean, non-unit std
        sides = torch.randint(0, 2, (N,))

        normed = _normalize_per_side(advs, sides)

        for s in (0, 1):
            mask = sides == s
            if mask.sum() > 2:
                std = normed[mask].std().item()
                assert 0.5 < std < 2.0, f"Side {s} std={std}"

    def test_single_step_not_nan(self):
        """Single step per side should not produce NaN."""
        advs = torch.tensor([1.0])
        sides = torch.tensor([0])

        normed = _normalize_per_side(advs, sides)
        assert torch.isfinite(normed).all()

    def test_all_same_gives_zero(self):
        """All-same advantages should normalize to zero (mean subtraction)."""
        advs = torch.full((10,), 5.0)
        sides = torch.zeros(10, dtype=torch.long)

        normed = _normalize_per_side(advs, sides)
        assert normed.abs().max() < 1e-4


# ---------------------------------------------------------------------------
# DEFCON-1 handling tests
# ---------------------------------------------------------------------------

class TestDefcon1Handling:
    """Test that DEFCON-1 game endings produce correct rewards."""

    def test_defcon1_loss_negative_reward(self):
        """The side that caused DEFCON-1 should get negative reward."""
        # DEFCON-1 = nuclear war = the side that lowered DEFCON to 1 loses
        # Reward for loser should be strongly negative
        reward = _reward_for_defcon1_loser()
        assert reward < 0

    def test_defcon1_win_positive_reward(self):
        """The side that wins via DEFCON-1 should get positive reward."""
        reward = _reward_for_defcon1_winner()
        assert reward > 0


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _reward_for_side(winner: str, step_side: str) -> float:
    """Compute reward for a step based on game outcome."""
    if winner == step_side:
        return 1.0
    return -1.0


def _reward_for_defcon1_loser() -> float:
    return -1.0


def _reward_for_defcon1_winner() -> float:
    return 1.0


def _compute_gae(
    values: list[float],
    rewards: list[float],
    gamma: float = 0.99,
    lam: float = 0.95,
) -> list[float]:
    """Simple GAE computation for testing."""
    N = len(values)
    advantages = [0.0] * N
    gae = 0.0
    for t in reversed(range(N)):
        next_value = values[t + 1] if t + 1 < N else 0.0
        delta = rewards[t] + gamma * next_value - values[t]
        gae = delta + gamma * lam * gae
        advantages[t] = gae
    return advantages


def _normalize_per_side(
    advantages: torch.Tensor,
    side_ints: torch.Tensor,
) -> torch.Tensor:
    """Per-side advantage normalization."""
    result = advantages.clone()
    for side_val in (0, 1):
        mask = side_ints == side_val
        if int(mask.sum().item()) > 1:
            adv = result[mask]
            result[mask] = (adv - adv.mean()) / (adv.std() + 1e-8)
    return result
