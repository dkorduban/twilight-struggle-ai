import torch
from tsrl.policies.dp_decoder import (
    bounded_knapsack_dp,
    greedy_topk_alloc,
)


def test_budget_respected():
    scores = torch.zeros(2, 6, 4)
    scores[0, 0, :] = torch.tensor([8.0, 7.0, 6.0, 5.0])
    scores[1, 3, :] = torch.tensor([9.0, 8.0, 7.0, 6.0])
    budget = torch.tensor([3, 2])
    legal_mask = torch.ones(2, 6, dtype=torch.bool)

    alloc = bounded_knapsack_dp(scores, budget, legal_mask)

    assert torch.equal(alloc.sum(dim=1), budget)


def test_legal_mask_respected():
    scores = torch.zeros(1, 5, 4)
    scores[0, 0, :] = torch.tensor([10.0, 9.0, 8.0, 7.0])
    scores[0, 3, :] = torch.tensor([6.0, 5.0, 4.0, 3.0])
    budget = torch.tensor([3])
    legal_mask = torch.tensor([[False, True, False, True, False]])

    alloc = bounded_knapsack_dp(scores, budget, legal_mask)

    assert torch.equal(alloc[0, ~legal_mask[0]], torch.zeros(3, dtype=torch.long))


def test_cap_respected():
    scores = torch.zeros(1, 4, 4)
    scores[0, 0, :] = torch.tensor([10.0, 9.0, 8.0, 7.0])
    scores[0, 1, :] = torch.tensor([1.0, 1.0, 1.0, 1.0])
    budget = torch.tensor([4])
    legal_mask = torch.ones(1, 4, dtype=torch.bool)
    cap = torch.tensor([[2, 4, 4, 4]])

    alloc = bounded_knapsack_dp(scores, budget, legal_mask, cap=cap)

    assert torch.all(alloc <= cap)


def test_zero_budget():
    scores = torch.randn(3, 4, 4)
    budget = torch.tensor([0, 0, 0])
    legal_mask = torch.ones(3, 4, dtype=torch.bool)

    alloc = bounded_knapsack_dp(scores, budget, legal_mask)

    assert torch.equal(alloc, torch.zeros_like(alloc))


def test_greedy_topk_alloc():
    scores = torch.zeros(1, 5, 4)
    scores[0, :, 0] = torch.tensor([1.0, 9.0, 3.0, 7.0, 5.0])
    budget = torch.tensor([3])
    legal_mask = torch.tensor([[True, True, False, True, True]])

    alloc = greedy_topk_alloc(scores, budget, legal_mask)

    expected = torch.tensor([[0, 1, 0, 1, 1]])
    assert torch.equal(alloc, expected)


def test_batch_independence():
    scores = torch.zeros(2, 3, 4)
    scores[0, 0, :] = torch.tensor([9.0, 8.0, 7.0, 6.0])
    scores[0, 1, :] = torch.tensor([5.0, 1.0, 1.0, 1.0])
    scores[1, 1, :] = torch.tensor([10.0, 9.0, 8.0, 7.0])
    scores[1, 2, :] = torch.tensor([4.0, 4.0, 4.0, 4.0])
    budget = torch.tensor([1, 3])
    legal_mask = torch.ones(2, 3, dtype=torch.bool)

    alloc = bounded_knapsack_dp(scores, budget, legal_mask)

    assert torch.equal(alloc.sum(dim=1), budget)
    assert torch.equal(alloc[0], torch.tensor([1, 0, 0]))
    assert torch.equal(alloc[1], torch.tensor([0, 3, 0]))
