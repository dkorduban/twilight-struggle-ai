"""Tests for bounded-knapsack DP decoder.

Tests both exact DP and greedy approximation for correctness:
  - Budget constraint: allocation sums to budget
  - Capacity constraint: no country exceeds cap
  - Legal mask: illegal countries get zero allocation
  - Optimality: exact DP finds global optimum
  - Greedy: produces valid (if not always optimal) allocations
  - alloc_to_country_targets conversion
"""

from __future__ import annotations

import pytest
import torch

from tsrl.policies.dp_decoder import (
    dp_decode_hard,
    dp_decode_greedy,
    alloc_to_country_targets,
)


# ---------------------------------------------------------------------------
# Budget constraint tests
# ---------------------------------------------------------------------------

class TestBudgetConstraint:
    """Allocation must sum to exactly budget (or less if not enough legal countries)."""

    def test_exact_budget_usage(self):
        B, C, T = 2, 10, 4
        scores = torch.randn(B, C, T)
        budget = torch.tensor([3, 4])
        legal = torch.ones(B, C, dtype=torch.bool)

        alloc = dp_decode_hard(scores, budget, legal)
        for b in range(B):
            assert alloc[b].sum().item() == budget[b].item(), \
                f"Batch {b}: alloc sum={alloc[b].sum()} != budget={budget[b]}"

    def test_exact_budget_greedy(self):
        B, C, T = 2, 10, 4
        scores = torch.randn(B, C, T)
        budget = torch.tensor([3, 4])
        legal = torch.ones(B, C, dtype=torch.bool)

        alloc = dp_decode_greedy(scores, budget, legal)
        for b in range(B):
            assert alloc[b].sum().item() == budget[b].item()

    def test_zero_budget(self):
        B, C, T = 1, 5, 4
        scores = torch.randn(B, C, T)
        budget = torch.tensor([0])
        legal = torch.ones(B, C, dtype=torch.bool)

        alloc = dp_decode_hard(scores, budget, legal)
        assert alloc.sum().item() == 0

    def test_budget_one(self):
        B, C, T = 1, 5, 4
        scores = torch.randn(B, C, T)
        budget = torch.tensor([1])
        legal = torch.ones(B, C, dtype=torch.bool)

        alloc = dp_decode_hard(scores, budget, legal)
        assert alloc.sum().item() == 1


# ---------------------------------------------------------------------------
# Capacity constraint tests
# ---------------------------------------------------------------------------

class TestCapacityConstraint:
    """No country should exceed the per-country cap."""

    def test_cap_respected(self):
        B, C, T = 1, 3, 4
        # All scores very high for country 0 — should still respect cap
        scores = torch.zeros(B, C, T)
        scores[0, 0, :] = 100.0  # country 0 is very attractive
        budget = torch.tensor([8])  # budget > cap for a single country
        legal = torch.ones(B, C, dtype=torch.bool)

        alloc = dp_decode_hard(scores, budget, legal, cap=4)
        assert alloc[0, 0].item() <= 4, f"Country 0 allocated {alloc[0, 0]} > cap 4"
        assert alloc[0].sum().item() == 8

    def test_cap_respected_greedy(self):
        B, C, T = 1, 3, 4
        scores = torch.zeros(B, C, T)
        scores[0, 0, :] = 100.0
        budget = torch.tensor([8])
        legal = torch.ones(B, C, dtype=torch.bool)

        alloc = dp_decode_greedy(scores, budget, legal, cap=4)
        assert alloc[0, 0].item() <= 4

    def test_custom_cap(self):
        B, C, T = 1, 5, 4
        scores = torch.ones(B, C, T) * 10
        budget = torch.tensor([3])
        legal = torch.ones(B, C, dtype=torch.bool)

        alloc = dp_decode_hard(scores, budget, legal, cap=2)
        assert (alloc <= 2).all(), f"Some allocation exceeds cap=2: {alloc}"


# ---------------------------------------------------------------------------
# Legal mask tests
# ---------------------------------------------------------------------------

class TestLegalMask:
    """Illegal countries must receive zero allocation."""

    def test_illegal_countries_zero(self):
        B, C, T = 1, 5, 4
        scores = torch.randn(B, C, T)
        budget = torch.tensor([3])
        legal = torch.zeros(B, C, dtype=torch.bool)
        legal[0, 1] = True
        legal[0, 3] = True

        alloc = dp_decode_hard(scores, budget, legal)
        assert alloc[0, 0].item() == 0
        assert alloc[0, 2].item() == 0
        assert alloc[0, 4].item() == 0

    def test_illegal_countries_zero_greedy(self):
        B, C, T = 1, 5, 4
        scores = torch.randn(B, C, T)
        budget = torch.tensor([3])
        legal = torch.zeros(B, C, dtype=torch.bool)
        legal[0, 1] = True
        legal[0, 3] = True

        alloc = dp_decode_greedy(scores, budget, legal)
        assert alloc[0, 0].item() == 0
        assert alloc[0, 2].item() == 0
        assert alloc[0, 4].item() == 0

    def test_all_illegal_gives_zero_alloc(self):
        B, C, T = 1, 5, 4
        scores = torch.randn(B, C, T)
        budget = torch.tensor([3])
        legal = torch.zeros(B, C, dtype=torch.bool)

        alloc = dp_decode_hard(scores, budget, legal)
        assert alloc.sum().item() == 0

    def test_single_legal_country(self):
        B, C, T = 1, 5, 4
        scores = torch.randn(B, C, T)
        budget = torch.tensor([3])
        legal = torch.zeros(B, C, dtype=torch.bool)
        legal[0, 2] = True

        alloc = dp_decode_hard(scores, budget, legal)
        assert alloc[0, 2].item() == min(3, 4)  # budget capped by T_MAX
        assert alloc[0].sum().item() == 3


# ---------------------------------------------------------------------------
# Optimality tests
# ---------------------------------------------------------------------------

class TestOptimality:
    """Exact DP should find the globally optimal allocation."""

    def test_obvious_optimum(self):
        """When one country clearly dominates, all budget goes there."""
        B, C, T = 1, 5, 4
        scores = torch.zeros(B, C, T)
        scores[0, 2, :] = torch.tensor([10.0, 9.0, 8.0, 7.0])  # strong decreasing
        budget = torch.tensor([3])
        legal = torch.ones(B, C, dtype=torch.bool)

        alloc = dp_decode_hard(scores, budget, legal)
        assert alloc[0, 2].item() == 3, f"Expected 3 in country 2, got {alloc[0, 2]}"

    def test_split_allocation(self):
        """When marginals cross, optimal splits across countries."""
        B, C, T = 1, 2, 4
        scores = torch.zeros(B, C, T)
        scores[0, 0, :] = torch.tensor([10.0, 1.0, 1.0, 1.0])  # strong first, weak after
        scores[0, 1, :] = torch.tensor([9.0, 8.0, 7.0, 6.0])   # consistently strong
        budget = torch.tensor([3])
        legal = torch.ones(B, C, dtype=torch.bool)

        alloc = dp_decode_hard(scores, budget, legal)
        # Optimal: 1 in country 0 (gain 10), 2 in country 1 (gain 9+8=17) = total 27
        # vs 2 in 0, 1 in 1: gain 11 + 9 = 20
        # vs 3 in 1: gain 24
        # vs 0 in 0, 3 in 1: gain 24
        # 1 in 0 + 2 in 1 = 27 is optimal
        assert alloc[0, 0].item() == 1
        assert alloc[0, 1].item() == 2

    def test_greedy_matches_dp_with_decreasing_marginals(self):
        """Greedy is optimal when marginals are decreasing."""
        B, C, T = 2, 10, 4
        # Construct decreasing marginals
        scores = torch.randn(B, C, T).abs()
        scores, _ = scores.sort(dim=-1, descending=True)  # ensure decreasing

        budget = torch.tensor([4, 3])
        legal = torch.ones(B, C, dtype=torch.bool)

        alloc_dp = dp_decode_hard(scores, budget, legal)
        alloc_greedy = dp_decode_greedy(scores, budget, legal)

        # With decreasing marginals, greedy should be optimal
        for b in range(B):
            dp_value = sum(scores[b, c, :alloc_dp[b, c]].sum() for c in range(C))
            greedy_value = sum(scores[b, c, :alloc_greedy[b, c]].sum() for c in range(C))
            assert abs(dp_value - greedy_value) < 1e-4, \
                f"Batch {b}: DP={dp_value:.4f} vs greedy={greedy_value:.4f}"


# ---------------------------------------------------------------------------
# alloc_to_country_targets tests
# ---------------------------------------------------------------------------

class TestAllocToTargets:
    """Test conversion from allocation tensor to country_targets list."""

    def test_basic_conversion(self):
        alloc = torch.tensor([[0, 2, 1, 0, 3]])
        targets = alloc_to_country_targets(alloc)
        assert len(targets) == 1
        assert sorted(targets[0]) == [1, 1, 2, 4, 4, 4]

    def test_zero_allocation(self):
        alloc = torch.tensor([[0, 0, 0]])
        targets = alloc_to_country_targets(alloc)
        assert targets == [[]]

    def test_single_country(self):
        alloc = torch.tensor([[0, 0, 4, 0, 0]])
        targets = alloc_to_country_targets(alloc)
        assert targets[0] == [2, 2, 2, 2]

    def test_batch(self):
        alloc = torch.tensor([
            [1, 0, 2],
            [0, 3, 0],
        ])
        targets = alloc_to_country_targets(alloc)
        assert len(targets) == 2
        assert targets[0] == [0, 2, 2]
        assert targets[1] == [1, 1, 1]

    def test_target_length_matches_budget(self):
        """Output list length should equal allocation sum."""
        B, C = 3, 10
        alloc = torch.randint(0, 3, (B, C))
        targets = alloc_to_country_targets(alloc)
        for b in range(B):
            assert len(targets[b]) == alloc[b].sum().item()


# ---------------------------------------------------------------------------
# Edge case tests
# ---------------------------------------------------------------------------

class TestEdgeCases:
    """Edge cases that might cause crashes or invalid results."""

    def test_large_budget_small_countries(self):
        """Budget exceeds total capacity — should fill all legal countries to cap."""
        B, C, T = 1, 3, 4
        scores = torch.ones(B, C, T)
        budget = torch.tensor([20])  # way more than 3 * 4 = 12
        legal = torch.ones(B, C, dtype=torch.bool)

        alloc = dp_decode_hard(scores, budget, legal, cap=4)
        # Can only allocate up to 12, rest is unspent
        assert alloc.sum().item() <= 12

    def test_batch_different_budgets(self):
        """Different budgets per batch element."""
        B, C, T = 3, 5, 4
        scores = torch.randn(B, C, T)
        budget = torch.tensor([1, 3, 4])
        legal = torch.ones(B, C, dtype=torch.bool)

        alloc = dp_decode_hard(scores, budget, legal)
        for b in range(B):
            assert alloc[b].sum().item() == budget[b].item()

    def test_single_country_single_budget(self):
        B, C, T = 1, 1, 4
        scores = torch.tensor([[[5.0, 3.0, 1.0, 0.5]]])
        budget = torch.tensor([2])
        legal = torch.ones(B, C, dtype=torch.bool)

        alloc = dp_decode_hard(scores, budget, legal)
        assert alloc[0, 0].item() == 2

    def test_negative_scores(self):
        """Negative scores should still produce valid allocations."""
        B, C, T = 1, 3, 4
        scores = torch.tensor([[[-1.0, -2.0, -3.0, -4.0],
                                  [-0.5, -1.5, -2.5, -3.5],
                                  [-0.1, -0.2, -0.3, -0.4]]])
        budget = torch.tensor([2])
        legal = torch.ones(B, C, dtype=torch.bool)

        alloc = dp_decode_hard(scores, budget, legal)
        assert alloc.sum().item() == 2
        # Should prefer country 2 (least negative marginals)
        assert alloc[0, 2].item() >= 1
