"""Learned policy wrapper for TSBaselineModel checkpoints."""
from __future__ import annotations

import math
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
from tsrl.etl.game_data import load_cards
from tsrl.policies.minimal_hybrid import _DEFCON_LOWERING_CARDS
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
    strategy_logits: torch.Tensor | None = None,  # (4,)
    country_strategy_logits: torch.Tensor | None = None,  # (4, 84)
) -> ActionEncoding | None:
    """Build an action using country_logits to score targets.

    COUP/REALIGN: sample one accessible country from the masked softmax.
    INFLUENCE: allocate ops with largest-remainder proportional assignment
               from the chosen strategy distribution.
    """
    accessible = sorted(accessible_countries(side, pub, adj, mode=mode))
    if not accessible:
        return None

    # Mask logits to accessible countries only (0-indexed = country_id, range 0..85).
    # Filter out superpower anchor IDs that are not board countries.
    valid_accessible = [c for c in accessible if 0 <= c <= 85]
    if not valid_accessible:
        return None
    indices = torch.tensor([c for c in valid_accessible], dtype=torch.long)
    source_logits = country_logits
    if strategy_logits is not None and country_strategy_logits is not None:
        strategy_idx = int(strategy_logits.argmax().item())
        source_logits = country_strategy_logits[strategy_idx]

    masked = torch.full_like(source_logits, float("-inf"))
    masked[indices] = source_logits[indices]
    probs = torch.softmax(masked, dim=0)

    # Multinomial samples a country_id directly (0-indexed, 0..85).
    if mode == ActionMode.COUP:
        target = int(torch.multinomial(probs, 1).item())
        return ActionEncoding(card_id=card_id, mode=mode, targets=(target,))

    if mode == ActionMode.REALIGN:
        target = int(torch.multinomial(probs, 1).item())
        return ActionEncoding(card_id=card_id, mode=mode, targets=(target,))

    # INFLUENCE: allocate integer ops by largest remainder after proportional split.
    ops = effective_ops(card_id, pub, side)
    accessible_probs = probs[indices]
    alloc = accessible_probs * ops
    floor_alloc = torch.floor(alloc).to(dtype=torch.long)
    remainder = ops - int(floor_alloc.sum().item())

    if remainder > 0:
        fractional = alloc - floor_alloc.to(dtype=alloc.dtype)
        order = sorted(
            range(len(valid_accessible)),
            key=lambda idx: (
                -float(fractional[idx].item()),
                valid_accessible[idx],
            ),
        )
        for idx in order[:remainder]:
            floor_alloc[idx] += 1

    targets_list: list[int] = []
    for country_id, count in zip(valid_accessible, floor_alloc.tolist()):
        targets_list.extend([country_id] * count)
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
        If True (default) and the checkpoint has strategy heads, use them to
        direct COUP/REALIGN/INFLUENCE target selection. Falls back to random
        target sampling when those heads are absent (old checkpoints).
    """
    if not os.path.exists(checkpoint_path):
        raise FileNotFoundError(checkpoint_path)

    checkpoint = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
    state_dict = checkpoint.get("model_state_dict", checkpoint)
    ckpt_args = checkpoint.get("args", {})
    hidden_dim = ckpt_args.get("hidden_dim", 256)
    model = TSBaselineModel(hidden_dim=hidden_dim)
    missing, unexpected = model.load_state_dict(state_dict, strict=False)
    has_strategy_heads = all(
        key in state_dict
        for key in (
            "strategy_heads.weight",
            "strategy_heads.bias",
            "strategy_mixer.weight",
            "strategy_mixer.bias",
        )
    )
    model.eval()
    try:
        model = torch.compile(model, dynamic=True)
    except Exception:
        pass  # torch.compile not available in this build

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
            strategy_logits = outputs.get("strategy_logits")
            if strategy_logits is not None:
                strategy_logits = strategy_logits[0]
            country_strategy_logits = outputs.get("country_strategy_logits")
            if country_strategy_logits is not None:
                country_strategy_logits = country_strategy_logits[0]

        # --- pick card ---
        # DEFCON safety at card-selection level: opponent-owned danger cards cannot be
        # played safely because their event fires for any ops mode, dropping DEFCON.
        _card_specs = load_cards()
        safe_card_ids = []
        for c in sorted(playable):
            if c in _DEFCON_LOWERING_CARDS:
                spec = _card_specs.get(c)
                is_opp = spec is not None and spec.side != side and spec.side != Side.NEUTRAL
                is_neutral = spec is not None and spec.side == Side.NEUTRAL
                if is_opp and pub.defcon <= 2:
                    continue  # mask out: event fires for any mode, DEFCON 2→1
                if is_opp and pub.defcon == 3 and pub.ar == 0:
                    continue  # mask out: opponent headline may fire first → DEFCON 2
                if is_neutral and pub.ar == 0 and pub.defcon <= 3:
                    continue  # mask out: neutral headline event at DEFCON ≤3 risky
            safe_card_ids.append(c)
        legal_card_ids = safe_card_ids if safe_card_ids else sorted(playable)
        masked_card = torch.full_like(card_logits, float("-inf"))
        legal_indices = torch.tensor([c - 1 for c in legal_card_ids], dtype=torch.long)
        masked_card[legal_indices] = card_logits[legal_indices]
        sampled_card_id = int(torch.multinomial(torch.softmax(masked_card, dim=0), 1).item()) + 1

        # --- pick mode (use mode_logits, not random choice) ---
        mode_logits = outputs["mode_logits"][0]
        modes = list(legal_modes(sampled_card_id, pub, side, adj=adj))
        if not modes:
            return None
        mode_mask = torch.full_like(mode_logits, float("-inf"))
        for m in modes:
            mode_mask[int(m)] = 0.0
        mode = ActionMode(int((mode_logits + mode_mask).argmax().item()))

        # --- DEFCON safety: never coup at DEFCON 2 (any coup drops to 1, phasing player loses) ---
        if mode == ActionMode.COUP and pub.defcon <= 2:
            safe_modes = [m for m in modes if m != ActionMode.COUP]
            if not safe_modes:
                return None  # only legal option is suicide coup — yield no action
            mode_mask2 = torch.full_like(mode_logits, float("-inf"))
            for m in safe_modes:
                mode_mask2[int(m)] = 0.0
            mode = ActionMode(int((mode_logits + mode_mask2).argmax().item()))

        # --- DEFCON safety: never play EVENT for DEFCON-lowering cards at DEFCON ≤ 2 ---
        # Cards like Duck and Cover (#4), We Will Bury You (#53), war cards (#11,#13,#24),
        # Iran-Iraq War (#105) lower DEFCON when their event fires. At DEFCON 2 this is
        # instant nuclear defeat for the phasing player.
        if mode == ActionMode.EVENT and pub.defcon <= 2 and sampled_card_id in _DEFCON_LOWERING_CARDS:
            safe_modes = [m for m in modes if m != ActionMode.EVENT]
            if not safe_modes:
                # All modes are EVENT (shouldn't happen) — try a different card
                safe_card_ids = [
                    c for c in legal_card_ids
                    if not (ActionMode.EVENT in legal_modes(c, pub, side, adj=adj)
                            and c in _DEFCON_LOWERING_CARDS
                            and all(m == ActionMode.EVENT for m in legal_modes(c, pub, side, adj=adj)))
                ]
                if safe_card_ids:
                    safe_card_mask = torch.full_like(card_logits, float("-inf"))
                    safe_indices = torch.tensor([c - 1 for c in safe_card_ids], dtype=torch.long)
                    safe_card_mask[safe_indices] = card_logits[safe_indices]
                    sampled_card_id = int(torch.multinomial(torch.softmax(safe_card_mask, dim=0), 1).item()) + 1
                    modes = list(legal_modes(sampled_card_id, pub, side, adj=adj))
                    mode_mask = torch.full_like(mode_logits, float("-inf"))
                    for m in modes:
                        mode_mask[int(m)] = 0.0
                    mode = ActionMode(int((mode_logits + mode_mask).argmax().item()))
                # else: no safe card found — fall through and accept the EVENT (rare edge case)
            else:
                mode_mask3 = torch.full_like(mode_logits, float("-inf"))
                for m in safe_modes:
                    mode_mask3[int(m)] = 0.0
                mode = ActionMode(int((mode_logits + mode_mask3).argmax().item()))

        if mode in (ActionMode.SPACE, ActionMode.EVENT):
            return ActionEncoding(card_id=sampled_card_id, mode=mode, targets=())

        rng = random.Random()
        # --- pick targets using country head if available ---
        if use_country_head and has_strategy_heads and country_logits is not None:
            action = _build_action_from_country_logits(
                sampled_card_id,
                mode,
                country_logits,
                pub,
                side,
                adj,
                rng,
                strategy_logits=strategy_logits,
                country_strategy_logits=country_strategy_logits,
            )
            if action is not None:
                return action

        # Fallback: random target sampling.
        action = _build_random_targets(sampled_card_id, mode, pub, side, adj, rng)
        return action

    return _policy


def make_model_candidate_fn(
    checkpoint_path: str,
    n_candidates: int = 10,
    *,
    temperature: float = 0.0,
    use_country_head: bool = True,
) -> Callable[[GameState, Side, bool, int], list[ActionEncoding]]:
    """Return an MCTS candidate function backed by a trained checkpoint."""
    if not os.path.exists(checkpoint_path):
        raise FileNotFoundError(checkpoint_path)

    checkpoint = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
    state_dict = checkpoint.get("model_state_dict", checkpoint)
    ckpt_args = checkpoint.get("args", {})
    hidden_dim = ckpt_args.get("hidden_dim", 256)
    model = TSBaselineModel(hidden_dim=hidden_dim)
    model.load_state_dict(state_dict, strict=False)
    has_strategy_heads = all(
        key in state_dict
        for key in (
            "strategy_heads.weight",
            "strategy_heads.bias",
            "strategy_mixer.weight",
            "strategy_mixer.bias",
        )
    )
    model.eval()
    try:
        model = torch.compile(model, dynamic=True)
    except Exception:
        pass

    adj = load_adjacency()

    def _candidate_fn(
        gs: GameState,
        side: Side,
        holds_china: bool,
        n: int,
        *,
        rng: random.Random | None = None,
    ) -> list[ActionEncoding]:
        hand = gs.hands[side]
        pub = gs.pub
        playable = sorted(legal_cards(hand, pub, side, holds_china=holds_china))
        if not playable:
            return []

        influence, cards, scalars = _extract_features(pub, hand, holds_china, side)
        with torch.no_grad():
            outputs = model(influence, cards, scalars)
            card_logits = outputs["card_logits"][0]
            mode_logits = outputs["mode_logits"][0]
            country_logits = outputs.get("country_logits")
            if country_logits is not None:
                country_logits = country_logits[0]
            strategy_logits = outputs.get("strategy_logits")
            if strategy_logits is not None:
                strategy_logits = strategy_logits[0]
            country_strategy_logits = outputs.get("country_strategy_logits")
            if country_strategy_logits is not None:
                country_strategy_logits = country_strategy_logits[0]

        card_probs = torch.softmax(card_logits, dim=0)
        mode_probs = torch.softmax(mode_logits, dim=0)

        scored_pairs: list[tuple[int, ActionMode, float]] = []
        for card_id in playable:
            card_score = float(card_probs[card_id - 1].item())
            modes = sorted(legal_modes(card_id, pub, side, adj=adj), key=int)
            for mode in modes:
                # DEFCON safety: skip EVENT for DEFCON-lowering cards at DEFCON ≤ 2.
                if mode == ActionMode.EVENT and pub.defcon <= 2 and card_id in _DEFCON_LOWERING_CARDS:
                    continue
                # DEFCON safety: skip COUP at DEFCON ≤ 2.
                if mode == ActionMode.COUP and pub.defcon <= 2:
                    continue
                scored_pairs.append((card_id, mode, card_score * float(mode_probs[int(mode)].item())))

        if not scored_pairs:
            # Fallback: safety filters removed all candidates (very rare edge case at low DEFCON).
            # Re-add all legal (card, mode) pairs without filtering so MCTS can still operate.
            for card_id in playable:
                card_score = float(card_probs[card_id - 1].item())
                modes = sorted(legal_modes(card_id, pub, side, adj=adj), key=int)
                for mode in modes:
                    scored_pairs.append((card_id, mode, card_score * float(mode_probs[int(mode)].item())))
            if not scored_pairs:
                return []

        limit = min(n, n_candidates, len(scored_pairs))
        if limit <= 0:
            return []

        selected_pairs: list[tuple[int, ActionMode]]
        if temperature <= 0.0:
            scored_pairs.sort(key=lambda item: (-item[2], item[0], int(item[1])))
            selected_pairs = [(card_id, mode) for card_id, mode, _ in scored_pairs[:limit]]
        else:
            _rng = rng or random.Random()
            remaining = list(scored_pairs)
            selected_pairs = []
            for _ in range(limit):
                max_score = max(score for _, _, score in remaining)
                weights = [
                    math.exp((score - max_score) / temperature)
                    for _, _, score in remaining
                ]
                target = _rng.random() * sum(weights)
                cumulative = 0.0
                for idx, ((card_id, mode, _), weight) in enumerate(zip(remaining, weights)):
                    cumulative += weight
                    if target <= cumulative or idx == len(remaining) - 1:
                        selected_pairs.append((card_id, mode))
                        remaining.pop(idx)
                        break

        _rng = rng or random.Random()
        actions: list[ActionEncoding] = []
        for card_id, mode in selected_pairs:
            if mode in (ActionMode.SPACE, ActionMode.EVENT):
                actions.append(ActionEncoding(card_id=card_id, mode=mode, targets=()))
                continue

            action = None
            if use_country_head and has_strategy_heads and country_logits is not None:
                action = _build_action_from_country_logits(
                    card_id,
                    mode,
                    country_logits,
                    pub,
                    side,
                    adj,
                    _rng,
                    strategy_logits=strategy_logits,
                    country_strategy_logits=country_strategy_logits,
                )
            if action is None:
                action = _build_random_targets(card_id, mode, pub, side, adj, _rng)
            if action is not None:
                actions.append(action)
        return actions

    return _candidate_fn


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
    ckpt_args = checkpoint.get("args", {})
    hidden_dim = ckpt_args.get("hidden_dim", 256)
    model = TSBaselineModel(hidden_dim=hidden_dim)
    model.load_state_dict(state_dict, strict=False)
    model.eval()
    try:
        model = torch.compile(model, dynamic=True)
    except Exception:
        pass

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
