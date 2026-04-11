"""Bounded-knapsack DP decoder for country allocation.

Converts per-country marginal value scores into integer allocation decisions
that respect budget and per-country capacity constraints.

Two paths:
  - ``dp_decode_hard``: exact integer DP for inference (argmax, no gradients)
  - ``dp_decode_soft``: differentiable relaxation for training (TODO Phase 2c)

The decoder operates on marginal-value logits from TSMarginalValueModel:
  scores[c, t] = logit for placing the t-th point in country c

Budget comes from the card's ops count (1-4, potentially modified by events).
Legal mask comes from country_mask (which countries are accessible).
"""

from __future__ import annotations

import torch
from torch import Tensor


def dp_decode_hard(
    scores: Tensor,      # (B, C, T) marginal value logits
    budget: Tensor,       # (B,) integer ops budget per sample
    legal_mask: Tensor,   # (B, C) bool — which countries are accessible
    cap: int = 4,         # max points per country (T_MAX)
) -> Tensor:
    """Exact bounded-knapsack DP — allocate `budget` points across countries.

    For each sample in the batch, solves:
        max  sum_c sum_{t=0}^{alloc[c]-1} scores[c, t]
        s.t. sum_c alloc[c] = budget
             0 <= alloc[c] <= min(cap, T)
             alloc[c] = 0 if not legal_mask[c]

    Returns:
        alloc: (B, C) integer allocation per country (0-indexed threshold count)
    """
    B, C, T = scores.shape
    device = scores.device
    max_budget = int(budget.max().item())

    # Precompute cumulative scores: cum_scores[b, c, k] = sum of scores[b, c, 0:k]
    # k=0 → 0 (place 0 points), k=1 → scores[c,0], k=2 → scores[c,0]+scores[c,1], etc.
    # Shape: (B, C, T+1) where index 0 = no allocation
    cum_scores = torch.zeros(B, C, T + 1, device=device)
    cum_scores[:, :, 1:] = scores.cumsum(dim=-1)

    # Make illegal country allocations impossible (-inf gain for k >= 1)
    illegal = ~legal_mask.unsqueeze(-1).expand_as(cum_scores)
    # k=0 stays 0 (no allocation); k>=1 gets -inf for illegal countries
    cum_scores[:, :, 1:][illegal[:, :, 1:]] = float("-inf")

    # DP: process countries sequentially
    # dp[b, j] = max total value achievable using first i countries with j points spent
    max_alloc_per_country = min(cap, T)
    dp = torch.full((B, max_budget + 1), float("-inf"), device=device)
    dp[:, 0] = 0.0
    # backtrack[b, i, j] = how many points were allocated to country i when
    # reaching state (i, j)
    backtrack = torch.zeros(B, C, max_budget + 1, dtype=torch.long, device=device)

    for c_idx in range(C):
        new_dp = dp.clone()
        new_bt = backtrack[:, c_idx].clone()
        for k in range(1, max_alloc_per_country + 1):
            # Cost of placing k points in country c_idx
            gain = cum_scores[:, c_idx, k]  # (B,)
            # For each budget level j >= k: check if placing k here improves
            for j in range(k, max_budget + 1):
                candidate = dp[:, j - k] + gain  # (B,)
                better = candidate > new_dp[:, j]
                new_dp[:, j] = torch.where(better, candidate, new_dp[:, j])
                new_bt[:, j] = torch.where(better, torch.tensor(k, device=device), new_bt[:, j])
        dp = new_dp
        backtrack[:, c_idx] = new_bt

    # Backtrack to recover allocations
    alloc = torch.zeros(B, C, dtype=torch.long, device=device)
    remaining = budget.clone().long()
    for c_idx in range(C - 1, -1, -1):
        for b in range(B):
            r = remaining[b].item()
            if r >= 0:
                k = backtrack[b, c_idx, r].item()
                alloc[b, c_idx] = k
                remaining[b] -= k

    return alloc


def dp_decode_greedy(
    scores: Tensor,      # (B, C, T) marginal value logits
    budget: Tensor,       # (B,) integer ops budget per sample
    legal_mask: Tensor,   # (B, C) bool — which countries are accessible
    cap: int = 4,         # max points per country (T_MAX)
) -> Tensor:
    """Greedy approximation — much faster than exact DP for large batches.

    Repeatedly picks the (country, threshold) pair with highest marginal gain
    until budget is exhausted. Greedy is optimal when costs are uniform and
    marginal values are decreasing, which holds for well-trained models.

    Returns:
        alloc: (B, C) integer allocation per country
    """
    B, C, T = scores.shape
    device = scores.device
    max_cap = min(cap, T)

    alloc = torch.zeros(B, C, dtype=torch.long, device=device)
    remaining = budget.clone().long()  # (B,)

    # Current threshold per country (next point to potentially place)
    thresholds = torch.zeros(B, C, dtype=torch.long, device=device)

    # Build score matrix: next_gain[b, c] = gain from placing next point in c
    # If threshold >= cap or not legal, set to -inf
    next_gain = scores[:, :, 0].clone()  # (B, C) — gain from first point
    next_gain[~legal_mask] = float("-inf")

    for _ in range(int(budget.max().item())):
        # Pick best (country) for each batch element
        best_c = next_gain.argmax(dim=1)  # (B,)

        # Only allocate if budget remains and gain is finite
        has_budget = remaining > 0
        gain_finite = next_gain.gather(1, best_c.unsqueeze(1)).squeeze(1) > float("-inf")
        do_alloc = has_budget & gain_finite

        if not do_alloc.any():
            break

        # Update allocations
        for b in range(B):
            if do_alloc[b]:
                c = best_c[b].item()
                alloc[b, c] += 1
                remaining[b] -= 1
                thresholds[b, c] += 1
                t = thresholds[b, c].item()
                if t >= max_cap:
                    next_gain[b, c] = float("-inf")
                else:
                    next_gain[b, c] = scores[b, c, t]

    return alloc


def alloc_to_country_targets(
    alloc: Tensor,  # (B, C) integer allocation
) -> list[list[int]]:
    """Convert allocation tensor to country_targets format (list of country IDs with repeats).

    Example: alloc[b] = [0, 0, 3, 0, 1, ...] → [2, 2, 2, 4]
    (3 points in country 2, 1 point in country 4)
    """
    B, C = alloc.shape
    result = []
    for b in range(B):
        targets = []
        for c in range(C):
            k = alloc[b, c].item()
            targets.extend([c] * k)
        result.append(targets)
    return result
