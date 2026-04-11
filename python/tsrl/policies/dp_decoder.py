"""Bounded-knapsack DP decoder for CountryAllocHead (Phase 2, Pragmatic Heads plan).

Replaces the K=4 mixture-of-softmaxes proportional allocation with an exact
integer DP that respects ops budget and per-country caps.
"""

import torch
from torch import Tensor


def bounded_knapsack_dp(
    scores: Tensor,
    budget: Tensor,
    legal_mask: Tensor,
    cap: Tensor | None = None,
    cost: Tensor | None = None,
) -> Tensor:
    """Exact integer DP allocating ops to countries to maximize total score."""
    batch_size, country_count, t_max = scores.shape
    device = scores.device
    budget = budget.to(device=device, dtype=torch.long).clamp_min(0)
    legal_mask = legal_mask.to(device=device, dtype=torch.bool)
    cap = (
        torch.full((batch_size, country_count), t_max, device=device, dtype=torch.long)
        if cap is None
        else cap.to(device=device, dtype=torch.long)
    ).clamp_(min=0, max=t_max)
    cost = (
        torch.ones((batch_size, country_count), device=device, dtype=torch.long)
        if cost is None
        else cost.to(device=device, dtype=torch.long)
    ).clamp_min_(1)
    cap = torch.where(legal_mask, cap, torch.zeros_like(cap))
    prefix_scores = torch.zeros(
        batch_size, country_count, t_max + 1, device=device, dtype=scores.dtype
    )
    prefix_scores[:, :, 1:] = scores.cumsum(dim=-1)

    alloc = torch.zeros(batch_size, country_count, device=device, dtype=torch.long)
    neg_inf = torch.tensor(float("-inf"), device=device, dtype=scores.dtype)

    for b in range(batch_size):
        max_budget = int(budget[b].item())
        if max_budget == 0:
            continue
        dp = torch.full(
            (country_count + 1, max_budget + 1),
            neg_inf,
            device=device,
            dtype=scores.dtype,
        )
        choice = torch.zeros((country_count, max_budget + 1), device=device, dtype=torch.long)
        dp[0, 0] = 0
        for c in range(country_count):
            dp[c + 1] = dp[c]
            take_cap = int(cap[b, c].item())
            step_cost = int(cost[b, c].item())
            if take_cap == 0:
                continue
            gains = prefix_scores[b, c]
            for spent in range(max_budget + 1):
                if not torch.isfinite(dp[c, spent]):
                    continue
                max_take = min(take_cap, (max_budget - spent) // step_cost)
                for take in range(1, max_take + 1):
                    new_spent = spent + take * step_cost
                    candidate = dp[c, spent] + gains[take]
                    if candidate > dp[c + 1, new_spent]:
                        dp[c + 1, new_spent] = candidate
                        choice[c, new_spent] = take
        remaining = max_budget
        if not torch.isfinite(dp[country_count, remaining]):
            remaining = int(dp[country_count].argmax().item())
        for c in range(country_count - 1, -1, -1):
            take = int(choice[c, remaining].item())
            alloc[b, c] = take
            remaining -= take * int(cost[b, c].item())
    if not scores.requires_grad:
        return alloc

    soft_logits = scores[:, :, 0].masked_fill(~legal_mask, -1e9)
    soft_weights = torch.softmax(soft_logits, dim=1) * legal_mask.to(scores.dtype)
    normalizer = soft_weights.sum(dim=1, keepdim=True)
    soft_weights = torch.where(
        normalizer > 0,
        soft_weights / normalizer,
        torch.zeros_like(soft_weights),
    )
    soft_alloc = soft_weights * budget.to(dtype=scores.dtype).unsqueeze(1)
    soft_alloc = torch.minimum(soft_alloc, cap.to(dtype=scores.dtype))
    return alloc.to(dtype=scores.dtype) + soft_alloc - soft_alloc.detach()


def greedy_topk_alloc(
    scores: Tensor,
    budget: Tensor,
    legal_mask: Tensor,
    cap: Tensor | None = None,
) -> Tensor:
    """Fast top-k approximation using only first-op marginal scores."""
    batch_size, country_count, _ = scores.shape
    device = scores.device
    budget = budget.to(device=device, dtype=torch.long).clamp_min(0)
    legal_mask = legal_mask.to(device=device, dtype=torch.bool)
    if cap is None:
        can_take = legal_mask
    else:
        can_take = legal_mask & (cap.to(device=device, dtype=torch.long) > 0)

    first_gain = scores[:, :, 0].masked_fill(~can_take, float("-inf"))
    order = first_gain.argsort(dim=1, descending=True)
    alloc = torch.zeros(batch_size, country_count, device=device, dtype=torch.long)
    for b in range(batch_size):
        take = min(int(budget[b].item()), int(can_take[b].sum().item()))
        if take > 0:
            alloc[b, order[b, :take]] = 1
    return alloc
