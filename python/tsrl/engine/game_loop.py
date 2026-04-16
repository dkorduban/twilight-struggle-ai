"""
Minimal game loop for Twilight Struggle self-play.

Provides:
  - GameLoop: drives a game to completion given two policy callables.
  - random_policy: factorized random action sampler (for rollouts).
  - play_random_game: convenience wrapper.

The loop handles:
  - Headline phase (simultaneous choice then reveal; higher ops first, US wins ties).
  - Action rounds (alternating, USSR first each turn).
  - End-of-turn: advance DEFCON, check final scoring, deal new cards.
  - Game end: VP threshold (±20), DEFCON 1, end of Turn 10.

Events that fire at specific game phases (e.g. DEFCON cleanup, mid/late war
deck injection) are implemented here.  Per-card event effects are dispatched
through events.py (standard cards) and cat_c_events.py (hand-manipulation cards).

Usage::

    from tsrl.engine.game_loop import play_random_game
    result = play_random_game(seed=42)
    print(result)  # {'winner': Side.USSR, 'turn': 5, 'vp': 15}
"""
from __future__ import annotations

from ._deprecation import warn_engine_deprecated

warn_engine_deprecated(__name__)

from dataclasses import dataclass, field
from typing import Callable, Generator, Optional

import numpy as np

from tsrl.engine.rng import RNG, make_rng

from tsrl.engine.cat_c_events import _CAT_C_CARD_IDS, apply_hand_event
from tsrl.engine.game_state import (
    GamePhase,
    GameState,
    _ars_for_turn,
    advance_to_late_war,
    advance_to_mid_war,
    clone_game_state,
    deal_cards,
    reset,
)
from tsrl.engine.legal_actions import enumerate_actions, legal_cards, sample_action
from tsrl.engine.step import _check_vp_win, _copy_pub, apply_action
from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Side

# ---------------------------------------------------------------------------
# Policy type
# ---------------------------------------------------------------------------

# A policy callable receives (pub, hand, holds_china) and returns one action (or None).
# Does NOT receive a pre-enumerated legal list — policies sample or enumerate themselves.
Policy = Callable[
    [PublicState, frozenset[int], bool],
    Optional[ActionEncoding],
]


# ---------------------------------------------------------------------------
# Random policy (factorized sampler — fast for rollouts)
# ---------------------------------------------------------------------------


def _apply_action_with_hands(
    gs: GameState,
    action: ActionEncoding,
    side: Side,
    rng: RNG,
) -> tuple[PublicState, bool, Optional[Side]]:
    """Apply an action, routing Cat C EVENT cards through apply_hand_event.

    Cat C cards (hand/deck manipulation) need access to GameState.hands and
    GameState.deck, so they cannot go through the PublicState-only apply_action.
    All other cards and modes go through the standard apply_action path.
    """
    # §5.2: firing opponent's event when playing their card for ops.
    if action.mode != ActionMode.EVENT:
        from tsrl.etl.game_data import load_cards as _lc

        _cards = _lc()
        opp = Side.US if side == Side.USSR else Side.USSR
        card_spec = _cards.get(action.card_id)
        if card_spec is not None and card_spec.side == opp:
            new_pub, over, winner = fire_opponent_event(gs, action.card_id, opp, rng)
            gs.pub = new_pub
            if over:
                return new_pub, True, winner

    if action.mode == ActionMode.EVENT and action.card_id in _CAT_C_CARD_IDS:
        new_pub, over, winner = apply_hand_event(gs, action, side, rng)
    else:
        new_pub, over, winner = apply_action(gs.pub, action, side, rng=rng)
        gs.pub = new_pub

    if over:
        return new_pub, True, winner

    # §6.4.4 level 6: if opponent has the first-to-reach-6 advantage, they discard a card.
    if action.mode == ActionMode.SPACE:
        opp = Side.US if side == Side.USSR else Side.USSR
        l6_holder = gs.pub.space_level6_first
        # Advantage is cancelled if both sides have reached level 6.
        if (
            l6_holder == opp
            and gs.pub.space[int(opp)] >= 6
            and gs.pub.space[int(side)] < 6
        ):
            opp_hand = gs.hands[opp]
            if opp_hand:
                discard_card = min(opp_hand)
                gs.hands[opp] = opp_hand - {discard_card}
                new_pub_copy = _copy_pub(gs.pub)
                new_pub_copy.discard = new_pub_copy.discard | {discard_card}
                gs.pub = new_pub_copy
                new_pub = gs.pub

    return new_pub, over, winner


def fire_opponent_event(
    gs: GameState,
    card_id: int,
    opp_side: Side,
    rng: RNG,
) -> tuple[PublicState, bool, Optional[Side]]:
    """Fire the event on an opponent's card as a side effect of ops play (§5.2).

    This fires the full event effect AND card lifecycle (_handle_card_played /
    _card_played) for the card owner side. The ops path's _handle_card_played
    call will be a no-op because of the idempotency guard added there.

    Passing `opp_side` through the EVENT path preserves owner-side checks in
    step._apply_event. That matters for intercepts keyed to who is playing the
    event, such as Flower Power's "US plays a war card as an event" trigger.

    Cat C cards (hand/deck manipulation) go through apply_hand_event.
    All others go through apply_action with mode=EVENT.
    """
    from tsrl.schemas import ActionEncoding, ActionMode

    event_action = ActionEncoding(card_id=card_id, mode=ActionMode.EVENT, targets=())
    if card_id in _CAT_C_CARD_IDS:
        return apply_hand_event(gs, event_action, opp_side, rng)
    new_pub, over, winner = apply_action(gs.pub, event_action, opp_side, rng=rng)
    gs.pub = new_pub
    return new_pub, over, winner


def make_random_policy(rng: Optional[RNG] = None) -> Policy:
    """Return a Policy that uses factorized sampling (O(hand+accessible), not O(combos)).

    Each call: pick random card → pick random mode → sample random targets.
    Much faster than enumerating all actions for INFLUENCE/REALIGN.
    """
    from tsrl.engine.adjacency import load_adjacency as _load_adj
    _adj = _load_adj()
    _rng = rng

    def _policy(pub: PublicState, hand: frozenset[int], holds_china: bool):
        return sample_action(
            hand, pub, pub.phasing,
            holds_china=holds_china, adj=_adj, rng=_rng,
        )

    return _policy


# ---------------------------------------------------------------------------
# Game result
# ---------------------------------------------------------------------------


@dataclass
class GameResult:
    winner: Optional[Side]   # None = draw (DEFCON 1 mutual destruction)
    final_vp: int
    end_turn: int
    end_reason: str           # e.g. 'vp_threshold' | 'defcon1' | 'turn_limit' | 'europe_control' | 'scoring_card_held'


@dataclass
class DecisionRequest:
    side: Side
    pub: PublicState
    hand: frozenset[int]
    holds_china: bool


# ---------------------------------------------------------------------------
# Game loop
# ---------------------------------------------------------------------------

_MID_WAR_TURN: int = 4
_LATE_WAR_TURN: int = 8
_MAX_TURNS: int = 10
_SPACE_SHUTTLE_ARS: int = 8


def _ars_for_side(pub: PublicState, side: Side, normal_ars: int) -> int:
    """Return this side's AR allotment for the current turn.

    Reaching space race level 8 ("Space Shuttle") grants 8 action rounds for
    the rest of the game.
    """
    if pub.space[int(side)] >= _SPACE_SHUTTLE_ARS:
        return _SPACE_SHUTTLE_ARS
    return normal_ars


def _run_game_gen(
    gs: GameState,
    rng: RNG,
    max_turns: int,
) -> Generator[DecisionRequest, Optional[ActionEncoding], GameResult]:
    for turn in range(1, max_turns + 1):
        gs.pub.turn = turn

        # --- Era deck injection ---
        if turn == _MID_WAR_TURN:
            advance_to_mid_war(gs, rng)
        elif turn == _LATE_WAR_TURN:
            advance_to_late_war(gs, rng)

        # --- Deal cards to both sides ---
        deal_cards(gs, Side.USSR, rng)
        deal_cards(gs, Side.US, rng)

        # --- Headline Phase ---
        result = yield from _run_headline_phase_gen(gs, rng)
        if result is not None:
            return result

        # --- Action Rounds ---
        total_ars = _ars_for_turn(turn)
        result = yield from _run_action_rounds_gen(gs, rng, total_ars)
        if result is not None:
            return result

        # --- North Sea Oil extra US AR (card 89) ---
        if gs.pub.north_sea_oil_extra_ar:
            gs.pub.north_sea_oil_extra_ar = False
            result = yield from _run_extra_ar_gen(gs, Side.US, rng)
            if result is not None:
                return result

        # --- Glasnost extra USSR AR (card 93, when SALT active) ---
        if gs.pub.glasnost_extra_ar:
            gs.pub.glasnost_extra_ar = False
            result = yield from _run_extra_ar_gen(gs, Side.USSR, rng)
            if result is not None:
                return result

        # --- End of turn ---
        result = _end_of_turn(gs, rng, turn)
        if result is not None:
            return result

    # Turn 10 end: final scoring already happened in _end_of_turn.
    winner: Optional[Side]
    if gs.pub.vp > 0:
        winner = Side.USSR
    elif gs.pub.vp < 0:
        winner = Side.US
    else:
        winner = None  # Tie (rare)
    return GameResult(
        winner=winner,
        final_vp=gs.pub.vp,
        end_turn=max_turns,
        end_reason="turn_limit",
    )


def run_game_cb(
    ussr_policy: Policy,
    us_policy: Policy,
    *,
    seed: Optional[int] = None,
) -> GameResult:
    """Drives the generator with callback policies."""
    rng = make_rng(seed)
    gs = reset(seed=int(rng.integers(0, 2**32)))
    gen = _run_game_gen(gs, rng, _MAX_TURNS)
    return _drive_policy_gen(gen, ussr_policy, us_policy)


def play_game(
    ussr_policy: Policy,
    us_policy: Policy,
    *,
    seed: Optional[int] = None,
) -> GameResult:
    """Backward-compatible interface."""
    return run_game_cb(ussr_policy, us_policy, seed=seed)


# ---------------------------------------------------------------------------
# Phase runners
# ---------------------------------------------------------------------------


def _run_headline_phase_gen(
    gs: GameState,
    rng: RNG,
) -> Generator[DecisionRequest, Optional[ActionEncoding], Optional[GameResult]]:
    """Both players choose headline cards simultaneously; resolve in ops order.

    Resolution order (confirmed by replay log evidence):
      - Higher ops card resolves first (regardless of side).
      - Ties: US card resolves first.
    The second headline sees the board state *after* the first has fully resolved.
    """
    from tsrl.etl.game_data import load_cards as _load_cards
    _cards_spec = _load_cards()

    gs.phase = GamePhase.HEADLINE
    gs.pub.ar = 0

    chosen: dict[Side, ActionEncoding] = {}

    # §6.4.4 level 4: if one side has the peek advantage, opponent picks first (blind).
    peek_side = gs.pub.space_level4_first
    if (
        peek_side is not None
        and gs.pub.space[int(peek_side)] >= 4
        and gs.pub.space[int(Side.US if peek_side == Side.USSR else Side.USSR)] >= 4
    ):
        peek_side = None

    if peek_side is not None:
        blind_side = Side.US if peek_side == Side.USSR else Side.USSR
        pick_order = [blind_side, peek_side]
    else:
        pick_order = [Side.USSR, Side.US]

    for side in pick_order:
        hand = gs.hands[side]
        holds_china = (side == Side.USSR and gs.ussr_holds_china) or \
                      (side == Side.US and gs.us_holds_china)
        if not hand:
            continue
        gs.pub.phasing = side
        from tsrl.engine.legal_actions import _cards
        playable = legal_cards(hand, gs.pub, side, holds_china=holds_china) - {6}
        headline_hand = frozenset(cid for cid in playable if cid in _cards())
        if not headline_hand:
            continue
        action = yield DecisionRequest(
            side=side,
            pub=gs.pub,
            hand=headline_hand,
            holds_china=holds_china,
        )
        action = _headline_pick(headline_hand, action)
        if action is None:
            continue
        chosen[side] = action
        # Remove headline card from hand immediately.
        gs.hands[side] = gs.hands[side] - {action.card_id}

    # Defectors (108) headline cancel: if US plays Defectors as headline,
    # USSR's headline card is discarded without effect (cancelled).
    _DEFECTORS_ID = 108
    if chosen.get(Side.US) is not None and chosen[Side.US].card_id == _DEFECTORS_ID:
        ussr_hl = chosen.pop(Side.USSR, None)
        if ussr_hl is not None:
            # Discard USSR's headline card without firing its event.
            # A cancelled card never fired as an event, so it always goes to
            # discard regardless of whether it has an asterisk (starred cards
            # are only removed when their event actually resolves).
            from tsrl.engine.step import _copy_pub
            pub = _copy_pub(gs.pub)
            pub.discard = pub.discard | {ussr_hl.card_id}
            gs.pub = pub

    # Sort chosen cards: higher ops first; ties broken by US first.
    def _resolve_key(side_action: tuple) -> tuple:
        side, action = side_action
        ops = _cards_spec[action.card_id].ops if action.card_id in _cards_spec else 0
        # Negate ops for descending sort; negate side int so US (1) sorts before USSR (0) on ties.
        return (-ops, -int(side))

    ordered = sorted(chosen.items(), key=_resolve_key)

    for side, action in ordered:
        new_pub, over, winner = _apply_action_with_hands(gs, action, side, rng)
        _sync_china(gs)
        if over:
            return GameResult(
                winner=winner,
                final_vp=gs.pub.vp,
                end_turn=gs.pub.turn,
                end_reason="europe_control" if winner is not None else "defcon1",
            )

    return None


def _run_headline_phase(
    gs: GameState,
    ussr_policy: Policy,
    us_policy: Policy,
    rng: RNG,
) -> Optional[GameResult]:
    gen = _run_headline_phase_gen(gs, rng)
    return _drive_policy_gen(gen, ussr_policy, us_policy)


def _resolve_trap_ar(
    gs: GameState,
    side: Side,
    rng: RNG,
) -> Optional[tuple[PublicState, bool, Optional[Side]]]:
    """Handle Bear Trap (USSR) / Quagmire (US) escape attempt for one AR.

    Returns None if the side is not trapped.
    If trapped: attempt to discard a 2+ ops non-scoring non-China card and roll d6.
      - Roll 1-4 (2/3 chance): escape — trap flag cleared, card discarded.
      - Roll 5-6 (1/3 chance): remain trapped, card discarded anyway.
    If no eligible card found: return (new_pub, over, winner) with trap still active
      (player forfeits this AR per rules).
    Returns (new_pub, game_over, winner) or None if not trapped.

    Note: escape roll implemented in game_loop._resolve_trap_ar.
    """
    from tsrl.etl.game_data import load_cards as _lc
    from tsrl.engine.step import _copy_pub, _check_vp_win

    is_bear_trap = pub_is_trapped = False
    if side == Side.USSR and gs.pub.bear_trap_active:
        is_bear_trap = True
        pub_is_trapped = True
    elif side == Side.US and gs.pub.quagmire_active:
        pub_is_trapped = True

    if not pub_is_trapped:
        return None

    cards_spec = _lc()

    # Find eligible escape card: non-scoring, non-China, ops >= 2.
    eligible = [
        cid for cid in gs.hands[side]
        if cid != 6  # not China Card
        and cards_spec.get(cid)
        and not cards_spec[cid].is_scoring
        and cards_spec[cid].ops >= 2
    ]
    if not eligible:
        # No eligible escape card — trapped player forfeits this AR per rules.
        from tsrl.engine.step import _copy_pub
        new_pub = _copy_pub(gs.pub)
        over, winner = _check_vp_win(new_pub)
        if new_pub.defcon <= 1:
            over = True
            winner = None
        return new_pub, over, winner

    # Pick one card at random to use as escape attempt.
    chosen = int(rng.choice(sorted(eligible)))
    gs.hands[side] = gs.hands[side] - {chosen}

    # Discard the card.
    from tsrl.engine.step import _copy_pub
    new_pub = _copy_pub(gs.pub)
    spec = cards_spec.get(chosen)
    if spec and spec.starred:
        new_pub.removed = new_pub.removed | {chosen}
    else:
        new_pub.discard = new_pub.discard | {chosen}

    # Roll d6: 1-4 = escape, 5-6 = remain trapped.
    roll = int(rng.integers(1, 7))
    if roll <= 4:
        # Escape!
        if is_bear_trap:
            new_pub.bear_trap_active = False
        else:
            new_pub.quagmire_active = False

    gs.pub = new_pub

    # Check game-over (DEFCON or VP — discard can't trigger this, but be safe).
    from tsrl.engine.step import _check_vp_win
    over, winner = _check_vp_win(new_pub)
    if new_pub.defcon <= 1:
        over = True
        winner = None
    return new_pub, over, winner


def _run_action_rounds_gen(
    gs: GameState,
    rng: RNG,
    total_ars: int,
    *,
    start_ar: int = 1,
    start_side_idx: int = 0,   # 0=USSR first, 1=US first within first AR
) -> Generator[DecisionRequest, Optional[ActionEncoding], Optional[GameResult]]:
    """Run action rounds, honoring per-side space level 8 extra ARs."""
    gs.phase = GamePhase.ACTION_ROUND
    sides = (Side.USSR, Side.US)

    for ar in range(start_ar, _SPACE_SHUTTLE_ARS + 1):
        _first_side = start_side_idx if ar == start_ar else 0
        ar_started = False
        for side in sides[_first_side:]:
            if ar > _ars_for_side(gs.pub, side, total_ars):
                continue
            if not ar_started:
                gs.pub.ar = ar
                ar_started = True
            gs.pub.phasing = side
            hand = gs.hands[side]
            holds_china = (side == Side.USSR and gs.ussr_holds_china) or \
                          (side == Side.US and gs.us_holds_china)

            # Handle Bear Trap / Quagmire escape attempt.
            trap_result = _resolve_trap_ar(gs, side, rng)
            if trap_result is not None:
                new_pub, over, winner = trap_result
                if over:
                    return GameResult(
                        winner=winner,
                        final_vp=new_pub.vp,
                        end_turn=gs.pub.turn,
                        end_reason=_end_reason(new_pub, winner),
                    )
                # AR consumed by trap attempt; skip policy call.
                continue

            # Skip yield if no legal actions (e.g. hand emptied by card event).
            if not legal_cards(hand, gs.pub, side, holds_china=holds_china):
                continue

            action = yield DecisionRequest(
                side=side,
                pub=gs.pub,
                hand=hand,
                holds_china=holds_china,
            )
            if action is None:
                # No legal actions: pass (shouldn't normally happen with cards in hand).
                continue

            # Remove played card from hand.
            if action.card_id in gs.hands[side]:
                gs.hands[side] = gs.hands[side] - {action.card_id}

            new_pub, over, winner = _apply_action_with_hands(gs, action, side, rng)
            _sync_china(gs)

            if over:
                return GameResult(
                    winner=winner,
                    final_vp=gs.pub.vp,
                    end_turn=gs.pub.turn,
                    end_reason=_end_reason(gs.pub, winner),
                )

            # NORAD (38): after USSR's AR, if DEFCON == 2 and NORAD is active,
            # US places 1 free influence in any country where US already has influence.
            # (GMT Deluxe rulebook: "place one Influence marker in any country that
            # already contains US Influence".)
            if side == Side.USSR and gs.pub.norad_active and gs.pub.defcon == 2:
                norad_result = _resolve_norad(gs, None, rng)
                if norad_result is not None:
                    norad_pub, norad_over, norad_winner = norad_result
                    if norad_over:
                        return GameResult(
                            winner=norad_winner,
                            final_vp=gs.pub.vp,
                            end_turn=gs.pub.turn,
                            end_reason=_end_reason(gs.pub, norad_winner),
                        )

    return None


def _run_action_rounds(
    gs: GameState,
    ussr_policy: Policy,
    us_policy: Policy,
    rng: RNG,
    total_ars: int,
    *,
    start_ar: int = 1,
    start_side_idx: int = 0,
) -> Optional[GameResult]:
    gen = _run_action_rounds_gen(
        gs,
        rng,
        total_ars,
        start_ar=start_ar,
        start_side_idx=start_side_idx,
    )
    return _drive_policy_gen(gen, ussr_policy, us_policy)


def _run_extra_ar_gen(
    gs: GameState,
    side: Side,
    rng: RNG,
) -> Generator[DecisionRequest, Optional[ActionEncoding], Optional[GameResult]]:
    """Run one extra AR for the given side (North Sea Oil, Glasnost, etc.).

    Handles Bear Trap / Quagmire; returns GameResult if game ends, else None.
    Callers are responsible for clearing the trigger flag before calling.
    """
    gs.pub.phasing = side
    holds_china = (side == Side.USSR and gs.ussr_holds_china) or \
                  (side == Side.US and gs.us_holds_china)
    hand = gs.hands[side]

    if not hand:
        return None

    trap_result = _resolve_trap_ar(gs, side, rng)
    if trap_result is not None:
        new_pub, over, winner = trap_result
        if over:
            return GameResult(
                winner=winner,
                final_vp=new_pub.vp,
                end_turn=gs.pub.turn,
                end_reason=_end_reason(new_pub, winner),
            )
        return None

    action = yield DecisionRequest(
        side=side,
        pub=gs.pub,
        hand=hand,
        holds_china=holds_china,
    )
    if action is None:
        return None

    if action.card_id in gs.hands[side]:
        gs.hands[side] = gs.hands[side] - {action.card_id}

    new_pub, over, winner = _apply_action_with_hands(gs, action, side, rng)
    _sync_china(gs)

    if over:
        return GameResult(
            winner=winner,
            final_vp=gs.pub.vp,
            end_turn=gs.pub.turn,
            end_reason=_end_reason(gs.pub, winner),
        )
    return None


def _run_extra_ar(
    gs: GameState,
    side: Side,
    policy: Policy,
    rng: RNG,
) -> Optional[GameResult]:
    gen = _run_extra_ar_gen(gs, side, rng)
    return _drive_policy_gen(gen, policy, policy)


def _end_of_turn(
    gs: GameState,
    rng: RNG,
    turn: int,
) -> Optional[GameResult]:
    """End-of-turn: discard hands, check final scoring on Turn 10, advance DEFCON."""
    gs.phase = GamePhase.CLEANUP

    # MilOps penalty: each side loses VP if milops < DEFCON level.
    # Per rules end-of-turn sequence, MilOps check (step E) comes BEFORE
    # DEFCON recovers (step H).  Use the CURRENT (pre-advance) DEFCON here.
    # USSR shortfall → US gains VP (pub.vp decreases).
    # US shortfall → USSR gains VP (pub.vp increases).
    defcon = gs.pub.defcon  # pre-advance DEFCON (correct per rules)
    for side_idx, side in enumerate((Side.USSR, Side.US)):
        shortfall = max(0, defcon - gs.pub.milops[side_idx])
        if shortfall > 0:
            if side == Side.USSR:
                gs.pub.vp -= shortfall   # US gains VP
            else:
                gs.pub.vp += shortfall   # USSR gains VP

    # Check if the VP swing from milops penalties ended the game.
    over, winner = _check_vp_win(gs.pub)
    if over:
        return GameResult(
            winner=winner,
            final_vp=gs.pub.vp,
            end_turn=gs.pub.turn,
            end_reason="vp",
        )

    # Advance DEFCON by 1 AFTER milops check (rules step H comes after step E).
    gs.pub.defcon = min(5, gs.pub.defcon + 1)

    gs.pub.milops = [0, 0]
    gs.pub.space_attempts = [0, 0]
    gs.pub.ops_modifier = [0, 0]
    gs.pub.vietnam_revolts_active = False
    gs.pub.north_sea_oil_extra_ar = False
    gs.pub.glasnost_extra_ar = False
    gs.pub.chernobyl_blocked_region = None
    gs.pub.latam_coup_bonus = None

    # Turn 10 final scoring: score all 6 regions (§10.3.2).
    # SE Asia is included in Asia scoring, not scored separately.
    # This happens after MilOps penalties and held-card checks, but before discarding hands.
    # Scoring card hold = immediate loss (the holder loses).
    # Per TS rules, a player who still holds a scoring card at end-of-turn
    # cleanup loses the game immediately before turn-10 final scoring.
    from tsrl.etl.game_data import load_cards as _load_cards
    _cards_spec = _load_cards()
    for side in (Side.USSR, Side.US):
        for cid in gs.hands[side]:
            spec = _cards_spec.get(cid)
            if spec and spec.is_scoring:
                loser = side
                winner_side = Side.US if loser == Side.USSR else Side.USSR
                return GameResult(
                    winner=winner_side,
                    final_vp=gs.pub.vp,
                    end_turn=gs.pub.turn,
                    end_reason="scoring_card_held",
                )

    if turn == 10:
        from tsrl.engine.scoring import apply_final_scoring
        final = apply_final_scoring(gs.pub)
        gs.pub.vp += final.vp_delta
        if final.game_over:
            return GameResult(
                winner=final.winner,
                final_vp=gs.pub.vp,
                end_turn=turn,
                end_reason="europe_control",
            )

    # Discard remaining hands.
    for side in (Side.USSR, Side.US):
        for card_id in gs.hands[side]:
            gs.pub.discard = gs.pub.discard | {card_id}
        gs.hands[side] = frozenset()

    return None


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _resolve_norad(
    gs: GameState,
    us_policy: Optional[Policy],
    rng: RNG,
) -> Optional[tuple]:
    """NORAD trigger: US places 1 free influence in a country already containing US influence.

    Called after each USSR AR when DEFCON == 2 and norad_active.
    For self-play: picks a random eligible country.
    Returns (new_pub, game_over, winner) or None if no eligible country.
    """
    from tsrl.engine.step import _copy_pub, _check_vp_win
    # Find countries where US already has influence.
    eligible = sorted(
        cid for (s, cid), inf in gs.pub.influence.items()
        if s == Side.US and inf > 0
    )
    if not eligible:
        return None
    country_id = int(rng.choice(eligible))
    pub = _copy_pub(gs.pub)
    pub.influence[(Side.US, country_id)] = pub.influence.get((Side.US, country_id), 0) + 1
    gs.pub = pub
    over, winner = _check_vp_win(pub)
    return pub, over, winner


def _headline_pick(
    headline_hand: frozenset[int],
    action: Optional[ActionEncoding],
) -> Optional[ActionEncoding]:
    """Validate a headline pick and force EVENT mode."""
    if not headline_hand or action is None:
        return None
    if action.card_id not in headline_hand:
        return None
    # Force mode to EVENT (headlines are always event plays).
    return ActionEncoding(card_id=action.card_id, mode=ActionMode.EVENT, targets=())


def _sync_china(gs: GameState) -> None:
    """Keep gs.ussr_holds_china / gs.us_holds_china in sync with pub.china_held_by."""
    gs.ussr_holds_china = (gs.pub.china_held_by == Side.USSR)
    gs.us_holds_china = (gs.pub.china_held_by == Side.US)


def _end_reason(pub: PublicState, winner: Optional[Side]) -> str:
    if pub.defcon <= 1:
        return "defcon1"
    if winner is not None:
        return "vp_threshold" if abs(pub.vp) >= 20 else "europe_control"
    return "vp_threshold"


def _drive_policy_gen(
    gen: Generator[DecisionRequest, Optional[ActionEncoding], GameResult | Optional[GameResult]],
    ussr_policy: Policy,
    us_policy: Policy,
) -> GameResult | Optional[GameResult]:
    try:
        req = next(gen)
    except StopIteration as e:
        return e.value
    while True:
        policy = ussr_policy if req.side == Side.USSR else us_policy
        action = policy(req.pub, req.hand, req.holds_china)
        try:
            req = gen.send(action)
        except StopIteration as e:
            return e.value


# ---------------------------------------------------------------------------
# Convenience wrappers
# ---------------------------------------------------------------------------


def _play_from_state_gen(
    gs: GameState,
    rng: RNG,
) -> Generator[DecisionRequest, Optional[ActionEncoding], GameResult]:
    """Continue a game from an existing GameState to completion.

    Clones gs first so the original is not mutated.
    Used for MCTS rollouts from mid-game positions.

    The continuation starts from where the GameState currently is:
      - If phase == ACTION_ROUND: finish remaining ARs of current turn, then cleanup,
        then continue turns.
      - Other phases: start from current turn's headline.
    """
    gs = clone_game_state(gs)

    current_turn = gs.pub.turn
    total_ars = _ars_for_turn(current_turn)

    # Finish the current turn from its current phase.
    if gs.phase == GamePhase.ACTION_ROUND:
        # Continue from the NEXT side in the current AR.
        # pub.phasing is the side that just acted; next = the other side.
        if gs.pub.phasing == Side.USSR:
            # USSR just went; US still needs to act this AR.
            start_side = 1
        else:
            # US just went; both sides done this AR; start next AR with USSR.
            start_side = 0
            gs.pub.ar += 1  # advance AR counter before resuming

        result = yield from _run_action_rounds_gen(
            gs, rng, total_ars,
            start_ar=gs.pub.ar, start_side_idx=start_side,
        )
        if result:
            return result

    elif gs.phase == GamePhase.HEADLINE:
        result = yield from _run_headline_phase_gen(gs, rng)
        if result:
            return result
        result = yield from _run_action_rounds_gen(gs, rng, total_ars)
        if result:
            return result

    result = _end_of_turn(gs, rng, current_turn)
    if result:
        return result

    # Continue subsequent turns.
    for turn in range(current_turn + 1, _MAX_TURNS + 1):
        gs.pub.turn = turn
        if turn == _MID_WAR_TURN:
            advance_to_mid_war(gs, rng)
        elif turn == _LATE_WAR_TURN:
            advance_to_late_war(gs, rng)
        deal_cards(gs, Side.USSR, rng)
        deal_cards(gs, Side.US, rng)
        result = yield from _run_headline_phase_gen(gs, rng)
        if result:
            return result
        result = yield from _run_action_rounds_gen(gs, rng,
                                    _ars_for_turn(turn))
        if result:
            return result
        result = _end_of_turn(gs, rng, turn)
        if result:
            return result

    if gs.pub.vp > 0:
        return GameResult(Side.USSR, gs.pub.vp, _MAX_TURNS, "turn_limit")
    if gs.pub.vp < 0:
        return GameResult(Side.US, gs.pub.vp, _MAX_TURNS, "turn_limit")
    return GameResult(None, gs.pub.vp, _MAX_TURNS, "turn_limit")


def play_from_state_cb(
    gs: GameState,
    ussr_policy: Policy,
    us_policy: Policy,
    *,
    rng: Optional[RNG] = None,
) -> GameResult:
    _rng = rng or make_rng()
    gen = _play_from_state_gen(gs, _rng)
    return _drive_policy_gen(gen, ussr_policy, us_policy)


def play_from_state(
    gs: GameState,
    ussr_policy: Policy,
    us_policy: Policy,
    *,
    rng: Optional[RNG] = None,
) -> GameResult:
    return play_from_state_cb(gs, ussr_policy, us_policy, rng=rng)


def play_random_game(seed: Optional[int] = None) -> GameResult:
    """Play one complete game with both sides using random policies."""
    rng = make_rng(seed)
    policy = make_random_policy(rng)
    return play_game(policy, policy, seed=seed)
