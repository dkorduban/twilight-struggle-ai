"""Learned policy wrapper for TSBaselineModel checkpoints."""
from __future__ import annotations

import os
import random

import torch

from tsrl.engine.game_loop import Policy
from tsrl.engine.legal_actions import enumerate_actions
from tsrl.etl.dataset import _card_mask, _influence_array
from tsrl.policies.model import TSBaselineModel
from tsrl.schemas import ActionEncoding, PublicState, Side


def _extract_features(
    pub: PublicState,
    hand: frozenset[int],
    holds_china: bool,
    side: Side,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    hand_mask = _card_mask(hand)
    influence = torch.tensor(
        _influence_array(pub, Side.USSR) + _influence_array(pub, Side.US),
        dtype=torch.float32,
    ).unsqueeze(0)
    cards = torch.tensor(
        hand_mask + hand_mask + _card_mask(pub.discard) + _card_mask(pub.removed),
        dtype=torch.float32,
    ).unsqueeze(0)
    scalars = torch.tensor(
        [
            pub.vp / 20.0,
            (pub.defcon - 1) / 4.0,
            pub.milops[Side.USSR] / 6.0,
            pub.milops[Side.US] / 6.0,
            pub.space[Side.USSR] / 9.0,
            pub.space[Side.US] / 9.0,
            float(int(pub.china_held_by)),
            float(holds_china),
            pub.turn / 10.0,
            pub.ar / 8.0,
            float(int(side)),
        ],
        dtype=torch.float32,
    ).unsqueeze(0)
    return influence, cards, scalars


def make_learned_policy(checkpoint_path: str, side: Side) -> Policy:
    """Return a Policy backed by a trained TSBaselineModel checkpoint."""
    if not os.path.exists(checkpoint_path):
        raise FileNotFoundError(checkpoint_path)

    checkpoint = torch.load(checkpoint_path, map_location="cpu")
    state_dict = checkpoint.get("model_state_dict", checkpoint)
    model = TSBaselineModel()
    model.load_state_dict(state_dict)
    model.eval()

    def _policy(
        pub: PublicState,
        hand: frozenset[int],
        holds_china: bool,
    ) -> ActionEncoding | None:
        hand_set = frozenset(hand)
        legal_actions = enumerate_actions(
            hand_set,
            pub,
            side,
            holds_china=holds_china,
        )
        if not legal_actions:
            return None

        influence, cards, scalars = _extract_features(pub, hand_set, holds_china, side)
        with torch.no_grad():
            card_logits = model(influence, cards, scalars)["card_logits"][0]

        legal_card_ids = sorted({action.card_id for action in legal_actions if action.card_id in hand_set})
        if not legal_card_ids:
            return None

        masked_logits = torch.full_like(card_logits, float("-inf"))
        legal_indices = torch.tensor([card_id - 1 for card_id in legal_card_ids], dtype=torch.long)
        masked_logits[legal_indices] = card_logits[legal_indices]
        sampled_card_id = int(torch.multinomial(torch.softmax(masked_logits, dim=0), 1).item()) + 1
        matching = [action for action in legal_actions if action.card_id == sampled_card_id]
        return random.choice(matching) if matching else None

    return _policy
