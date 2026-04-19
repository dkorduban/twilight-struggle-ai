import torch
from tsrl.constants import (
    CARD_DIM,
    INFLUENCE_DIM,
    MODEL_REGISTRY,
    NUM_COUNTRIES,
    SCALAR_DIM,
)
from tsrl.policies.dp_decoder import bounded_knapsack_dp
from tsrl.policies.model import CountryAllocHead, TSCountryAllocHeadModel


def test_country_alloc_head_shape():
    head = CountryAllocHead(hidden_dim=64, max_ops=4)
    feat = torch.randn(2, 72, 64)

    out = head(feat, budget=3)

    assert out.shape == (2, 72)


def test_knapsack_dp_budget_constraint():
    scores = torch.zeros(2, 5, 4)
    scores[0, 1, :] = torch.tensor([8.0, 7.0, 6.0, 5.0])
    scores[1, 3, :] = torch.tensor([9.0, 8.0, 7.0, 6.0])
    budget = torch.tensor([3, 2])
    legal_mask = torch.ones(2, 5, dtype=torch.bool)

    alloc = bounded_knapsack_dp(scores, budget, legal_mask)

    assert torch.equal(alloc.sum(dim=1), budget)


def test_model_registry():
    model = MODEL_REGISTRY["country_alloc_head"](hidden_dim=256)

    assert model is not None


def test_country_alloc_model_forward_shapes():
    model = TSCountryAllocHeadModel(hidden_dim=64)
    influence = torch.randn(2, INFLUENCE_DIM)
    cards = torch.randint(0, 2, (2, CARD_DIM)).float()
    scalars = torch.rand(2, SCALAR_DIM)

    with torch.no_grad():
        out = model(influence, cards, scalars, country_budget=3)

    assert out["country_logits"].shape == (2, NUM_COUNTRIES)
    assert out["country_allocations"].shape == (2, NUM_COUNTRIES)
    assert torch.equal(out["country_allocations"].sum(dim=1), torch.tensor([3, 3]))
    assert torch.allclose(out["country_logits"].sum(dim=1), torch.ones(2))
