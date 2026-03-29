"""Learned policy wrapper for TSBaselineModel checkpoints."""
from __future__ import annotations

import os
import random
from typing import Callable

import torch

from tsrl.engine.game_loop import Policy
from tsrl.engine.game_state import GameState
from tsrl.engine.legal_actions import (
    accessible_countries,
    effective_ops,
    legal_cards,
    legal_modes,
    load_adjacency,
)
from tsrl.etl.dataset import _card_mask, _influence_array
from tsrl.policies.model import TSBaselineModel
from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Side

_CHINA_CARD_ID = 6


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


def _build_action_from_country_logits(
    card_id: int,
    mode: ActionMode,
    country_logits: torch.Tensor,  # (84,)
    pub: PublicState,
    side: Side,
    adj: dict,
    rng: random.Random,
) -> ActionEncoding | None:
    """Build an action using country_logits to score targets.

    COUP/REALIGN: sample one accessible country from the masked softmax.
    INFLUENCE: sample one accessible country per op from the same masked
               softmax, independently and with replacement.
    """
    accessible = sorted(accessible_countries(side, pub, adj, mode=mode))
    if not accessible:
        return None

    # Mask logits to accessible countries only (0-indexed = country_id - 1).
    # Filter out IDs that exceed the model's 84-country vocabulary (e.g. superpower
    # anchors USA=81 / USSR=82 are not board countries; Taiwan=85 is beyond index 83).
    valid_accessible = [c for c in accessible if 1 <= c <= 84]
    if not valid_accessible:
        return None
    indices = torch.tensor([c - 1 for c in valid_accessible], dtype=torch.long)
    masked = torch.full((84,), float("-inf"))
    masked[indices] = country_logits[indices]
    probs = torch.softmax(masked, dim=0)

    # Multinomial samples an index into the 84-dim vector; add 1 for country_id.
    if mode == ActionMode.COUP:
        target = int(torch.multinomial(probs, 1).item()) + 1
        return ActionEncoding(card_id=card_id, mode=mode, targets=(target,))

    if mode == ActionMode.REALIGN:
        target = int(torch.multinomial(probs, 1).item()) + 1
        return ActionEncoding(card_id=card_id, mode=mode, targets=(target,))

    # INFLUENCE: allocate ops one at a time via independent draws.
    ops = effective_ops(card_id, pub, side)
    targets_list: list[int] = []
    for _ in range(ops):
        target = int(torch.multinomial(probs, 1).item()) + 1
        targets_list.append(target)
    return ActionEncoding(card_id=card_id, mode=mode, targets=tuple(targets_list))


def make_learned_policy(checkpoint_path: str, side: Side, *, use_country_head: bool = True) -> Policy:
    """Return a Policy backed by a trained TSBaselineModel checkpoint.

    Parameters
    ----------
    checkpoint_path:
        Path to a .pt checkpoint file produced by train_baseline.py.
    side:
        The side this policy plays (USSR or US).
    use_country_head:
        If True (default) and the checkpoint has a country_head, use
        country_logits to direct COUP/REALIGN/INFLUENCE target selection.
        Falls back to random sampling if the head is absent (old checkpoints).
    """
    if not os.path.exists(checkpoint_path):
        raise FileNotFoundError(checkpoint_path)

    checkpoint = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
    state_dict = checkpoint.get("model_state_dict", checkpoint)
    model = TSBaselineModel()
    missing, unexpected = model.load_state_dict(state_dict, strict=False)
    has_country_head = "country_head.weight" in state_dict
    model.eval()

    adj = load_adjacency()

    def _policy(
        pub: PublicState,
        hand: frozenset[int],
        holds_china: bool,
    ) -> ActionEncoding | None:
        hand_set = frozenset(hand)

        playable = legal_cards(hand_set, pub, side, holds_china=holds_china)
        if not playable:
            return None

        influence, cards, scalars = _extract_features(pub, hand_set, holds_china, side)
        with torch.no_grad():
            outputs = model(influence, cards, scalars)
            card_logits = outputs["card_logits"][0]
            country_logits = outputs.get("country_logits")
            if country_logits is not None:
                country_logits = country_logits[0]

        # --- pick card ---
        legal_card_ids = sorted(playable)
        masked_card = torch.full_like(card_logits, float("-inf"))
        legal_indices = torch.tensor([c - 1 for c in legal_card_ids], dtype=torch.long)
        masked_card[legal_indices] = card_logits[legal_indices]
        sampled_card_id = int(torch.multinomial(torch.softmax(masked_card, dim=0), 1).item()) + 1

        # --- pick mode ---
        modes = list(legal_modes(sampled_card_id, pub, side, adj=adj))
        if not modes:
            return None
        rng = random.Random()
        mode = rng.choice(modes)

        if mode in (ActionMode.SPACE, ActionMode.EVENT):
            return ActionEncoding(card_id=sampled_card_id, mode=mode, targets=())

        # --- pick targets using country head if available ---
        if use_country_head and has_country_head and country_logits is not None:
            action = _build_action_from_country_logits(
                sampled_card_id, mode, country_logits, pub, side, adj, rng
            )
            if action is not None:
                return action

        # Fallback: random target sampling.
        action = _build_random_targets(sampled_card_id, mode, pub, side, adj, rng)
        return action

    return _policy


def _build_random_targets(
    card_id: int,
    mode: ActionMode,
    pub: PublicState,
    side: Side,
    adj: dict,
    rng: random.Random,
) -> ActionEncoding | None:
    """Fall back to random target sampling for a given card+mode."""
    accessible = sorted(accessible_countries(side, pub, adj, mode=mode))
    if not accessible:
        return None
    if mode in (ActionMode.COUP, ActionMode.REALIGN):
        return ActionEncoding(card_id=card_id, mode=mode, targets=(rng.choice(accessible),))
    ops = effective_ops(card_id, pub, side)
    targets = tuple(rng.choice(accessible) for _ in range(ops))
    return ActionEncoding(card_id=card_id, mode=mode, targets=targets)


def make_value_function(checkpoint_path: str) -> Callable[[GameState], float]:
    """Return a value function backed by a trained TSBaselineModel checkpoint.

    The returned function takes a GameState and returns a float in [-1, +1]
    representing the game value from USSR's perspective (+1 = USSR wins, -1 = US wins).

    This is suitable for use as the value_fn parameter in uct_mcts() for
    value-function-based tree search (replacing random rollouts).

    Parameters
    ----------
    checkpoint_path:
        Path to a .pt checkpoint file produced by train_baseline.py.
    """
    if not os.path.exists(checkpoint_path):
        raise FileNotFoundError(checkpoint_path)

    checkpoint = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
    state_dict = checkpoint.get("model_state_dict", checkpoint)
    model = TSBaselineModel()
    model.load_state_dict(state_dict, strict=False)
    model.eval()

    def _value_fn(gs: GameState) -> float:
        """Evaluate the value of a GameState using the learned model.

        Returns value from USSR's perspective: +1 = USSR wins, -1 = US wins.
        """
        pub = gs.pub
        side = pub.phasing
        holds_china = (side == Side.USSR and gs.ussr_holds_china) or \
                      (side == Side.US and gs.us_holds_china)
        hand = gs.hands[side]

        influence, cards, scalars = _extract_features(pub, hand, holds_china, side)
        with torch.no_grad():
            outputs = model(influence, cards, scalars)
            value = outputs["value"][0, 0].item()  # scalar from [-1, +1]
        return value

    return _value_fn
