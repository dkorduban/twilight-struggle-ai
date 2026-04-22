from __future__ import annotations

import pytest
import torch
import torch.nn.functional as F

from tsrl.constants import (
    CARD_DIM,
    INFLUENCE_DIM,
    MODEL_REGISTRY,
    NUM_CARDS,
    NUM_COUNTRIES,
    NUM_MODES,
    NUM_PLAYABLE_CARDS,
    NUM_STRATEGIES,
    SCALAR_DIM,
    SMALL_CHOICE_MAX,
)
from tsrl.policies.model import TSNovelModel, TransitionDiffHead


BATCH_SIZE = 4


def _make_batch(batch: int = BATCH_SIZE) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    g = torch.Generator().manual_seed(20260422)
    influence = torch.randn(batch, INFLUENCE_DIM, generator=g)
    cards = torch.randint(0, 2, (batch, CARD_DIM), generator=g).float()
    scalars = torch.rand(batch, SCALAR_DIM, generator=g)
    scalars[:, 10] = torch.tensor([0.0, 1.0, 0.0, 1.0])[:batch]
    return influence, cards, scalars


def _make_action_one_hot(batch: int = BATCH_SIZE) -> torch.Tensor:
    action = torch.zeros(batch, TransitionDiffHead._ACTION_ONE_HOT_DIM)
    action[:, 0] = 1.0
    action[:, NUM_PLAYABLE_CARDS] = 1.0
    action[:, NUM_PLAYABLE_CARDS + NUM_MODES] = 1.0
    action[:, NUM_PLAYABLE_CARDS + NUM_MODES + NUM_COUNTRIES] = 1.0
    return action


@pytest.mark.parametrize("n_mp", [0, 1, 2, 3])
def test_tsnovel_instantiates_with_mp_rounds(n_mp: int) -> None:
    model = TSNovelModel(n_mp=n_mp)
    assert model.influence_encoder_embed.n_mp == n_mp


def test_tsnovel_registered() -> None:
    assert MODEL_REGISTRY["tsnovel"] is TSNovelModel


def test_tsnovel_forward_shapes() -> None:
    model = TSNovelModel().eval()
    influence, cards, scalars = _make_batch()
    eligible_cards = torch.ones(BATCH_SIZE, NUM_CARDS, dtype=torch.uint8)
    eligible_countries = torch.ones(BATCH_SIZE, NUM_COUNTRIES, dtype=torch.uint8)
    action_one_hot = _make_action_one_hot()

    with torch.no_grad():
        out = model(
            influence,
            cards,
            scalars,
            eligible_cards_mask=eligible_cards,
            eligible_countries_mask=eligible_countries,
            action_one_hot=action_one_hot,
        )

    assert out["card_logits"].shape == (BATCH_SIZE, NUM_PLAYABLE_CARDS)
    assert out["mode_logits"].shape == (BATCH_SIZE, NUM_MODES)
    assert out["country_logits"].shape == (BATCH_SIZE, NUM_COUNTRIES)
    assert out["country_strategy_logits"].shape == (
        BATCH_SIZE,
        NUM_STRATEGIES,
        NUM_COUNTRIES,
    )
    assert out["strategy_logits"].shape == (BATCH_SIZE, NUM_STRATEGIES)
    assert out["value"].shape == (BATCH_SIZE, 1)
    assert out["small_choice_logits"].shape == (BATCH_SIZE, SMALL_CHOICE_MAX)
    assert out["country_pick_logits"].shape == (BATCH_SIZE, NUM_COUNTRIES)
    assert out["subframe_logits"].shape == (BATCH_SIZE, NUM_PLAYABLE_CARDS)
    assert out["belief_logits"].shape == (BATCH_SIZE, NUM_CARDS)
    assert out["state_diff_pred"]["d_influence"].shape == (BATCH_SIZE, NUM_COUNTRIES, 2)
    assert out["state_diff_pred"]["d_global"].shape == (BATCH_SIZE, 4)


def test_belief_head_receives_card_tokens() -> None:
    model = TSNovelModel().eval()
    influence, cards, scalars = _make_batch()
    seen: dict[str, tuple[int, ...]] = {}

    def hook(_module, args) -> None:
        seen["shape"] = tuple(args[0].shape)

    handle = model.belief_head.register_forward_pre_hook(hook)
    try:
        with torch.no_grad():
            model(influence, cards, scalars)
    finally:
        handle.remove()

    assert seen["shape"] == (BATCH_SIZE, NUM_CARDS, 128)


def test_transition_diff_head_receives_country_tokens_and_action() -> None:
    model = TSNovelModel().eval()
    influence, cards, scalars = _make_batch()
    action_one_hot = _make_action_one_hot()
    seen: dict[str, tuple[int, ...]] = {}

    def hook(_module, args) -> None:
        seen["country_tokens"] = tuple(args[0].shape)
        seen["action"] = tuple(args[2].shape)

    handle = model.transition_diff_head.register_forward_pre_hook(hook)
    try:
        with torch.no_grad():
            out = model(influence, cards, scalars, action_one_hot=action_one_hot)
    finally:
        handle.remove()

    assert seen["country_tokens"] == (BATCH_SIZE, NUM_COUNTRIES, 128)
    assert seen["action"] == (BATCH_SIZE, TransitionDiffHead._ACTION_ONE_HOT_DIM)
    assert out["state_diff_pred"]["d_influence"].shape == (BATCH_SIZE, NUM_COUNTRIES, 2)
    assert out["state_diff_pred"]["d_global"].shape == (BATCH_SIZE, 4)


def test_subframe_row_routing() -> None:
    model = TSNovelModel().eval()
    influence, cards, scalars = _make_batch()
    frame_kind = torch.tensor([1, 2, 3, 4], dtype=torch.long)

    with torch.no_grad():
        out = model(influence, cards, scalars, frame_kind=frame_kind)

    min_value = torch.finfo(out["subframe_logits"].dtype).min
    assert torch.allclose(
        out["subframe_logits"][0, :SMALL_CHOICE_MAX],
        out["small_choice_logits"][0],
    )
    assert torch.equal(
        out["subframe_logits"][0, SMALL_CHOICE_MAX:],
        torch.full_like(out["subframe_logits"][0, SMALL_CHOICE_MAX:], min_value),
    )

    assert torch.allclose(
        out["subframe_logits"][1, :NUM_COUNTRIES],
        out["country_pick_logits"][1],
    )
    assert torch.equal(
        out["subframe_logits"][1, NUM_COUNTRIES:],
        torch.full_like(out["subframe_logits"][1, NUM_COUNTRIES:], min_value),
    )

    assert torch.allclose(out["subframe_logits"][2], out["card_logits"][2])
    assert torch.allclose(out["subframe_logits"][3], out["card_logits"][3])


def test_tsnovel_backward_smoke_combined_loss() -> None:
    model = TSNovelModel()
    model.train()
    influence, cards, scalars = _make_batch()
    action_one_hot = _make_action_one_hot()
    out = model(influence, cards, scalars, action_one_hot=action_one_hot)

    card_target = torch.arange(BATCH_SIZE) % NUM_PLAYABLE_CARDS
    mode_target = torch.arange(BATCH_SIZE) % NUM_MODES
    country_target = torch.arange(BATCH_SIZE) % NUM_COUNTRIES
    small_choice_target = torch.arange(BATCH_SIZE) % SMALL_CHOICE_MAX
    value_target = torch.zeros(BATCH_SIZE, 1)
    belief_target = torch.zeros(BATCH_SIZE, NUM_CARDS)
    d_influence_target = torch.zeros(BATCH_SIZE, NUM_COUNTRIES, 2)
    d_global_target = torch.zeros(BATCH_SIZE, 4)

    country_loss = -torch.log(
        out["country_logits"][torch.arange(BATCH_SIZE), country_target] + 1e-8
    ).mean()
    policy_loss = (
        F.cross_entropy(out["card_logits"], card_target)
        + F.cross_entropy(out["mode_logits"], mode_target)
        + country_loss
        + F.cross_entropy(out["country_pick_logits"], country_target)
        + F.cross_entropy(out["small_choice_logits"], small_choice_target)
    )
    value_loss = F.mse_loss(out["value"], value_target)
    state_diff_loss = F.mse_loss(
        out["state_diff_pred"]["d_influence"],
        d_influence_target,
    ) + F.mse_loss(out["state_diff_pred"]["d_global"], d_global_target)
    belief_loss = F.binary_cross_entropy_with_logits(out["belief_logits"], belief_target)

    loss = policy_loss + value_loss + state_diff_loss + belief_loss
    assert torch.isfinite(loss)
    loss.backward()

    grad_sum = sum(
        p.grad.detach().abs().sum()
        for p in model.parameters()
        if p.grad is not None
    )
    assert grad_sum > 0
