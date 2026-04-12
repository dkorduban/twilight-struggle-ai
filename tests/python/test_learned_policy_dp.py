import random

import torch

from tsrl.engine.legal_actions import accessible_countries, effective_ops, load_adjacency
from tsrl.policies.learned_policy import _build_action_from_country_logits
from tsrl.schemas import ActionMode, PublicState, Side


def test_build_action_from_country_logits_uses_dp_for_influence():
    adj = load_adjacency()
    pub = PublicState()
    side = Side.USSR
    card_id = 7
    budget_val = effective_ops(card_id, pub, side)
    accessible = sorted(
        c
        for c in accessible_countries(side, pub, adj, mode=ActionMode.INFLUENCE)
        if 0 <= c <= 85
    )
    assert accessible

    preferred = accessible[0]
    country_logits = torch.full((86,), -10.0)
    country_logits[accessible[-1]] = 100.0

    strategy_logits = torch.tensor([0.0, 6.0, 0.0, 0.0])
    country_strategy_logits = torch.full((4, 86), -10.0)
    country_strategy_logits[1, preferred] = 5.0
    if len(accessible) > 1:
        country_strategy_logits[1, accessible[1]] = 1.0

    action = _build_action_from_country_logits(
        card_id=card_id,
        mode=ActionMode.INFLUENCE,
        country_logits=country_logits,
        pub=pub,
        side=side,
        adj=adj,
        rng=random.Random(0),
        strategy_logits=strategy_logits,
        country_strategy_logits=country_strategy_logits,
    )

    assert action is not None
    assert len(action.targets) == budget_val
    assert all(0 <= target <= 85 for target in action.targets)
    assert all(target in accessible for target in action.targets)
    assert action.targets == (preferred,) * budget_val
