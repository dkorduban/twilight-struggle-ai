"""
PublicState and HandKnowledge reducers.

Implements the event-driven reducer pattern:

    next_state = reduce(prev_state, event)

Rules:
  - PublicState holds only publicly-observable information.
  - HandKnowledge is per-player, causal, and online-safe.
  - OfflineLabels are NEVER updated here (they live in smoother.py).
  - Invariants are checked after every reduction in debug mode.

Reducer design philosophy:
  - Be explicit about each event kind; do not use catch-all dispatch.
  - When a rule is ambiguous, raise ReducerError (never silently guess).
  - Preserve raw event in error messages for debuggability.
"""
from __future__ import annotations

import copy
from dataclasses import dataclass, replace
from typing import Final

from tsrl.schemas import (
    EventKind,
    HandKnowledge,
    InfluenceArray,
    LabelQuality,
    PublicState,
    ReplayEvent,
    Side,
)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

HAND_SIZE_EARLY: Final[int] = 8   # turns 1-3
HAND_SIZE_LATE: Final[int] = 9    # turns 4-10

_EARLY_WAR_LAST_TURN: Final[int] = 3
_MID_WAR_LAST_TURN: Final[int] = 6


# ---------------------------------------------------------------------------
# Errors
# ---------------------------------------------------------------------------


class ReducerError(Exception):
    """Raised when an event cannot be applied consistently to the current state."""


# ---------------------------------------------------------------------------
# PublicState reducer
# ---------------------------------------------------------------------------


def reduce_public(state: PublicState, event: ReplayEvent) -> PublicState:
    """Apply a single ReplayEvent to PublicState, returning a new state.

    Does NOT mutate the input state.  Returns a shallow copy with fields
    updated according to the event.
    """
    s = _copy_public(state)

    kind = event.kind

    if kind == EventKind.GAME_START:
        from tsrl.etl.game_data import initial_influence
        s.influence = InfluenceArray(initial_influence())

    elif kind == EventKind.TURN_START:
        s.turn = event.turn
        s.ar = 0
        # Reset per-turn counters at the start of each turn.
        s.milops = [0, 0]
        s.space_attempts = [0, 0]
        # ops_modifier is NOT reset here; it persists until CARD_EXPIRED events fire.

    elif kind == EventKind.HEADLINE_PHASE_START:
        s.turn = event.turn
        s.ar = 0
        # Real TSEspionage logs use HEADLINE_PHASE_START as the turn boundary.
        # TURN_START is never emitted by the game server; reset per-turn counters here.
        # NOTE: milops penalty is applied in reduce_game (not here) because it depends
        # on whether the log already emitted Cleanup VP_CHANGE events via TURN_END.
        s.milops = [0, 0]
        s.space_attempts = [0, 0]
        # ops_modifier is NOT reset here; it persists until CARD_EXPIRED events fire.

    elif kind == EventKind.ACTION_ROUND_START:
        s.ar = event.ar
        s.phasing = event.phasing

    elif kind == EventKind.TURN_END:
        pass  # milops reset happens at TURN_START

    elif kind == EventKind.GAME_END:
        pass

    elif kind == EventKind.RESHUFFLE:
        # Discard is shuffled back into deck. Public tracking: discard → deck_remaining.
        s.discard = frozenset()
        # deck_remaining now includes all reshuffled cards.
        # We do not track exact deck_remaining here (would require knowing what
        # is in each hand); that is left to the HandKnowledge reducer.

    elif kind == EventKind.PLAY:
        if event.card_id == 6:
            # China Card played for ops — passes to opponent.
            # When USSR plays it → goes face-down to US.
            # When US plays it → goes face-up to USSR.
            if event.phasing in (Side.USSR, Side.US):
                opponent = Side.US if event.phasing == Side.USSR else Side.USSR
                s.china_held_by = opponent
                # Face-up when returning to USSR; face-down when going to US.
                s.china_playable = (opponent == Side.USSR)
        elif event.card_id is not None:
            # Card leaves play: it will be discarded or removed (handled by
            # separate DISCARD / REMOVE events that should follow).
            pass

    elif kind == EventKind.DISCARD:
        if event.card_id is not None:
            s.discard = s.discard | {event.card_id}

    elif kind == EventKind.REMOVE:
        if event.card_id is not None:
            s.removed = s.removed | {event.card_id}
            # Also remove from discard if present
            s.discard = s.discard - {event.card_id}

    elif kind == EventKind.DEFCON_CHANGE:
        if event.amount is not None:
            new_defcon = int(event.amount)
            if not (1 <= new_defcon <= 5):
                raise ReducerError(
                    f"DEFCON out of range [{new_defcon}] at line {event.line_number}"
                )
            s.defcon = new_defcon

    elif kind == EventKind.VP_CHANGE:
        if event.amount is not None:
            s.vp += int(event.amount)

    elif kind == EventKind.MILOPS_CHANGE:
        if event.amount is not None and event.phasing in (Side.USSR, Side.US):
            idx = int(event.phasing)
            s.milops[idx] = int(event.amount)

    elif kind == EventKind.CHINA_CARD_PASS:
        # Phasing field on the event = new holder
        if event.phasing in (Side.USSR, Side.US):
            s.china_held_by = event.phasing
            s.china_playable = True  # passed face-up

    elif kind == EventKind.PLACE_INFLUENCE:
        if event.country_id is not None and event.phasing in (Side.USSR, Side.US):
            cid = event.country_id
            if event.us_bracket is not None and event.ussr_bracket is not None:
                # Bracket values are authoritative absolute state from the game server.
                # Use them directly so implicit pre-placed influence (not shown as
                # separate events) and any cumulative drift are corrected automatically.
                if event.us_bracket > 0:
                    s.influence[(Side.US, cid)] = event.us_bracket
                else:
                    s.influence.pop((Side.US, cid), None)
                if event.ussr_bracket > 0:
                    s.influence[(Side.USSR, cid)] = event.ussr_bracket
                else:
                    s.influence.pop((Side.USSR, cid), None)
            elif event.amount is not None:
                key = (event.phasing, cid)
                s.influence[key] = s.influence.get(key, 0) + int(event.amount)

    elif kind == EventKind.REMOVE_INFLUENCE:
        if event.country_id is not None and event.phasing in (Side.USSR, Side.US):
            cid = event.country_id
            if event.us_bracket is not None and event.ussr_bracket is not None:
                if event.us_bracket > 0:
                    s.influence[(Side.US, cid)] = event.us_bracket
                else:
                    s.influence.pop((Side.US, cid), None)
                if event.ussr_bracket > 0:
                    s.influence[(Side.USSR, cid)] = event.ussr_bracket
                else:
                    s.influence.pop((Side.USSR, cid), None)
            elif event.amount is not None:
                key = (event.phasing, cid)
                s.influence[key] = max(0, s.influence.get(key, 0) - int(event.amount))

    elif kind == EventKind.HANDICAP:
        if event.amount is not None and event.phasing in (Side.USSR, Side.US):
            if event.phasing == Side.USSR:
                s.handicap_ussr += event.amount
            else:
                s.handicap_us += event.amount

    elif kind == EventKind.FORCED_DISCARD:
        # Card is discarded from a player's hand (forced by an opponent's card).
        # Add to the public discard pile so deck tracking stays consistent.
        if event.card_id is not None:
            s.discard = s.discard | {event.card_id}

    elif kind == EventKind.SPACE_RACE:
        # SPACE_RACE events carry the absolute new space level in event.amount.
        # "USSR/US advances to N in the Space Race." → update pub.space[side].
        if event.amount is not None and event.phasing in (Side.USSR, Side.US):
            s.space[int(event.phasing)] = event.amount

    elif kind == EventKind.CARD_IN_PLAY:
        # Track ops-modifier effects from persistent-effect cards.
        # These effects last until end-of-turn (ops_modifier is reset at HEADLINE_PHASE_START).
        _apply_ops_modifier_effect(s, event.card_id, event.phasing, delta=+1)
        # Track one-time prerequisite flags and ongoing effects.
        cid = event.card_id
        if cid == 16:   # Warsaw Pact Formed: enables NATO
            s.warsaw_pact_played = True
        elif cid == 23: # Marshall Plan: enables NATO
            s.marshall_plan_played = True
        elif cid == 19: # Truman Doctrine: enables NATO (also removes USSR inf from neutral EU)
            s.truman_doctrine_played = True
        elif cid == 21: # NATO: active protection for US-controlled WE countries
            s.nato_active = True
        elif cid == 74: # Shuttle Diplomacy: next Asia/ME scoring ignores highest-stability BG
            s.shuttle_diplomacy_active = True
        elif cid == 35: # Formosan Resolution: Taiwan counts as BG for US in Asia scoring (permanent)
            s.formosan_active = True
        elif cid == 17: # De Gaulle Leads France: France excluded from NATO protection
            s.de_gaulle_active = True
        elif cid == 58: # Willy Brandt: West Germany excluded from NATO protection
            s.willy_brandt_active = True

    elif kind == EventKind.CARD_EXPIRED:
        # Reverse the ops-modifier applied when the card came into play.
        _apply_ops_modifier_effect(s, event.card_id, event.phasing, delta=-1)
        # Clear ongoing-effect flags for cards that can expire.
        cid = event.card_id
        if cid == 74:   # Shuttle Diplomacy consumed by Asia/ME scoring
            s.shuttle_diplomacy_active = False
        elif cid == 17: # De Gaulle expires
            s.de_gaulle_active = False
        elif cid == 58: # Willy Brandt expires
            s.willy_brandt_active = False

    elif kind in (
        EventKind.COUP,
        EventKind.REALIGN,
        EventKind.SCORING,
        EventKind.HEADLINE,
        EventKind.REVEAL_HAND,
        EventKind.TRANSFER,
        EventKind.DRAW,
        EventKind.END_TURN_HELD,
        EventKind.ACTION_ROUND_START,
        EventKind.TURN_END,
    ):
        # These events may affect HandKnowledge but not PublicState directly
        # (their board effects come via PLACE_INFLUENCE / REMOVE_INFLUENCE /
        # DEFCON_CHANGE / VP_CHANGE / DISCARD / REMOVE follow-up events).
        pass

    elif kind == EventKind.UNKNOWN:
        # Unknown lines are preserved but do not update state.
        pass

    else:
        raise ReducerError(
            f"Unhandled EventKind {kind!r} at line {event.line_number}. "
            "Add a branch to reduce_public()."
        )

    return s


# ---------------------------------------------------------------------------
# HandKnowledge reducer
# ---------------------------------------------------------------------------


def reduce_hand(
    knowledge: HandKnowledge,
    event: ReplayEvent,
    all_card_ids: frozenset[int],
    public: PublicState,
) -> HandKnowledge:
    """Apply a single ReplayEvent to HandKnowledge, returning new knowledge.

    Args:
        knowledge: Current hand knowledge for the observer.
        event: The event being applied.
        all_card_ids: Set of all valid card ids (from cards.csv, excl. China).
        public: The PREVIOUS public state (before reduce_public was called).

    Returns:
        Updated HandKnowledge.  Invariants are verified before returning.

    Invariants:
        - known_in_hand ∩ known_not_in_hand == ∅
        - possible_hidden ∩ known_not_in_hand == ∅
        - No card actually in hand may appear in known_not_in_hand.
    """
    hk = _copy_hand(knowledge)
    obs = knowledge.observer
    phasing = event.phasing

    kind = event.kind

    if kind == EventKind.TURN_START:
        # Hand size resets at turn start (after drawing).
        # We do NOT update hand_size here; that comes from the DRAW events.
        # But we can update expected hand size for future validation.
        pass

    elif kind == EventKind.DRAW:
        # A player draws cards.  If card_id is known, add to known_in_hand.
        if phasing == obs and event.card_id is not None:
            hk.known_in_hand = hk.known_in_hand | {event.card_id}
            hk.known_not_in_hand = hk.known_not_in_hand - {event.card_id}
            hk.hand_size = min(hk.hand_size + 1, HAND_SIZE_LATE)

    elif kind in (EventKind.PLAY, EventKind.HEADLINE):
        # A player plays a card — it leaves their hand.
        if event.card_id is not None:
            if phasing == obs:
                hk.known_in_hand = hk.known_in_hand - {event.card_id}
            # Card is now definitely not in this player's hand (or opponent's)
            # — follow-up DISCARD/REMOVE event handles public tracking.
            hk.known_not_in_hand = hk.known_not_in_hand | {event.card_id}
            hk.possible_hidden = hk.possible_hidden - {event.card_id}
            if phasing == obs:
                hk.hand_size = max(0, hk.hand_size - 1)

    elif kind == EventKind.FORCED_DISCARD:
        if event.card_id is not None:
            if phasing == obs:
                hk.known_in_hand = hk.known_in_hand - {event.card_id}
            hk.known_not_in_hand = hk.known_not_in_hand | {event.card_id}
            hk.possible_hidden = hk.possible_hidden - {event.card_id}
            if phasing == obs:
                hk.hand_size = max(0, hk.hand_size - 1)

    elif kind == EventKind.REVEAL_HAND:
        # All cards in aux_card_ids are now known to be in phasing player's hand.
        for cid in event.aux_card_ids:
            if phasing == obs:
                hk.known_in_hand = hk.known_in_hand | {cid}
                hk.known_not_in_hand = hk.known_not_in_hand - {cid}
            else:
                # We now know the opponent has these cards: they're not in deck/discard
                hk.known_not_in_hand = hk.known_not_in_hand | {cid}
                hk.possible_hidden = hk.possible_hidden - {cid}

    elif kind == EventKind.END_TURN_HELD:
        # Cards held into next turn are revealed (they stayed in hand).
        for cid in event.aux_card_ids:
            if phasing == obs:
                hk.known_in_hand = hk.known_in_hand | {cid}
                hk.known_not_in_hand = hk.known_not_in_hand - {cid}

    elif kind == EventKind.TRANSFER:
        # Card moves from one player to another.
        if event.card_id is not None:
            # Sender loses the card, receiver gains it.
            # phasing = sender; aux_country_ids not used; we need to know recipient.
            # For now, mark card as not-in-sender's-hand.
            if phasing == obs:
                hk.known_in_hand = hk.known_in_hand - {event.card_id}
                hk.hand_size = max(0, hk.hand_size - 1)
            else:
                # Opponent sent a card (e.g. China Card pass)
                hk.known_not_in_hand = hk.known_not_in_hand | {event.card_id}
                hk.possible_hidden = hk.possible_hidden - {event.card_id}

    elif kind == EventKind.RESHUFFLE:
        # Discard goes back to deck. The possible_hidden mask expands to include
        # previously-discarded cards that were in known_not_in_hand.
        # Specifically, any card that was only known-not-in-hand because it was
        # discarded is now possibly back in someone's hand.
        # We conservatively re-open the mask to all non-removed, non-in-hand cards.
        discarded_cards = public.discard  # from the public state before reshuffle
        hk.known_not_in_hand = hk.known_not_in_hand - discarded_cards
        # Recompute possible_hidden:
        hk.possible_hidden = (
            all_card_ids
            - hk.known_not_in_hand
            - hk.known_in_hand
            - public.removed
        )

    elif kind == EventKind.REMOVE:
        if event.card_id is not None:
            hk.known_in_hand = hk.known_in_hand - {event.card_id}
            hk.known_not_in_hand = hk.known_not_in_hand | {event.card_id}
            hk.possible_hidden = hk.possible_hidden - {event.card_id}

    elif kind == EventKind.CHINA_CARD_PASS:
        # China Card ownership changes.
        hk.holds_china = (event.phasing == obs)

    # All other kinds do not affect HandKnowledge
    _verify_hand_invariants(hk)
    return hk


# ---------------------------------------------------------------------------
# Batch reducer
# ---------------------------------------------------------------------------


def reduce_game(
    events: list[ReplayEvent],
    all_card_ids: frozenset[int],
    *,
    check_invariants: bool = True,
) -> list[tuple[PublicState, HandKnowledge, HandKnowledge]]:
    """Reduce a full game replay into a list of (public, ussr_hand, us_hand) triples.

    Returns one triple per event, representing the state AFTER applying the event.

    Args:
        events: Ordered list of events from parse_replay().
        all_card_ids: All valid card ids (from game_data.load_cards(), excl. China).
        check_invariants: If True, verify HandKnowledge invariants after each step.

    Returns:
        List of (PublicState, HandKnowledge[USSR], HandKnowledge[US]) tuples.
    """
    from tsrl.schemas import Side  # avoid circular

    pub = PublicState()
    ussr_hand = HandKnowledge(
        observer=Side.USSR,
        possible_hidden=all_card_ids,
    )
    us_hand = HandKnowledge(
        observer=Side.US,
        possible_hidden=all_card_ids,
    )

    results: list[tuple[PublicState, HandKnowledge, HandKnowledge]] = []

    # Track whether the current turn had an explicit Cleanup (TURN_END) event.
    # Some log formats include "Turn N, Cleanup: VP" lines (emitted as TURN_END +
    # VP_CHANGE), which already apply the milops penalty.  When such events exist,
    # we must NOT double-apply the penalty at HEADLINE_PHASE_START.
    cleanup_seen_this_turn: bool = False

    for event in events:
        prev_pub = pub

        if event.kind == EventKind.TURN_END:
            cleanup_seen_this_turn = True

        pub = reduce_public(pub, event)

        # Apply end-of-turn milops VP penalty only if the log did NOT emit it as a
        # Cleanup VP_CHANGE event.  The penalty = max(0, DEFCON - milops) per side,
        # using the DEFCON and milops from BEFORE the headline reset.
        if event.kind == EventKind.HEADLINE_PHASE_START and event.turn > 1 and not cleanup_seen_this_turn:
            defcon = prev_pub.defcon
            ussr_shortfall = max(0, defcon - prev_pub.milops[int(Side.USSR)])
            us_shortfall = max(0, defcon - prev_pub.milops[int(Side.US)])
            penalty = us_shortfall - ussr_shortfall
            if penalty != 0:
                pub = _copy_public(pub)
                pub.vp += penalty

        if event.kind == EventKind.HEADLINE_PHASE_START:
            cleanup_seen_this_turn = False

        ussr_hand = reduce_hand(ussr_hand, event, all_card_ids, prev_pub)
        us_hand = reduce_hand(us_hand, event, all_card_ids, prev_pub)
        results.append((pub, ussr_hand, us_hand))

    return results


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Ops-modifier card table
# ---------------------------------------------------------------------------
# Cards that set a persistent ops_modifier effect for the remainder of the turn.
# Key: card_id → (side_affected, delta_per_play)
# For Red Scare/Purge: side_affected is the OPPONENT of the player who plays it.
_USSR_SIDE: int = int(Side.USSR)
_US_SIDE: int = int(Side.US)

# Cards with persistent ops-modifier effects.
# Format: card_id → (side_idx_or_None, magnitude)
# - side_idx is None for Red Scare/Purge (affects opponent of phasing side).
# - For all other cards the affected side is fixed, regardless of who played it.
_OPS_MODIFIER_CARDS: dict[int, tuple[int | None, int]] = {
    9:  (int(Side.USSR), +1),   # Vietnam Revolts → USSR +1 (tracked globally)
    25: (int(Side.US),  +1),    # Containment* → US +1
    31: (None,          -1),    # Red Scare/Purge → opponent of phasing side, -1
    54: (int(Side.USSR), +1),   # Brezhnev Doctrine → USSR +1
    96: (int(Side.US),  -1),    # Iran-Contra Scandal → US -1
}


def _apply_ops_modifier_effect(
    s: "PublicState",
    card_id: int | None,
    phasing: "Side",
    delta: int,
) -> None:
    """Apply (or reverse) the ops-modifier effect of a card coming into play.

    delta=+1 when card comes into play; delta=-1 when it expires.
    """
    if card_id is None or card_id not in _OPS_MODIFIER_CARDS:
        return
    side_idx, magnitude = _OPS_MODIFIER_CARDS[card_id]
    if side_idx is None:
        # Red Scare/Purge: affects the opponent of whoever played the card.
        if phasing not in (Side.USSR, Side.US):
            return
        side_idx = 1 - int(phasing)
    s.ops_modifier[side_idx] += delta * magnitude


def _copy_public(s: PublicState) -> PublicState:
    """Shallow copy of PublicState with mutable fields copied."""
    c = copy.copy(s)
    c.milops = list(s.milops)
    c.space = list(s.space)
    c.space_attempts = list(s.space_attempts)
    c.ops_modifier = list(s.ops_modifier)
    c.influence = s.influence.copy()
    # frozensets are immutable — safe to share
    return c


def _copy_hand(hk: HandKnowledge) -> HandKnowledge:
    """Return a mutable copy of HandKnowledge."""
    return HandKnowledge(
        observer=hk.observer,
        known_in_hand=hk.known_in_hand,
        known_not_in_hand=hk.known_not_in_hand,
        possible_hidden=hk.possible_hidden,
        hand_size=hk.hand_size,
        holds_china=hk.holds_china,
    )


def _verify_hand_invariants(hk: HandKnowledge) -> None:
    """Assert HandKnowledge invariants.  Raises ReducerError on violation."""
    overlap = hk.known_in_hand & hk.known_not_in_hand
    if overlap:
        raise ReducerError(
            f"HandKnowledge invariant violated: cards appear in both "
            f"known_in_hand and known_not_in_hand: {sorted(overlap)}"
        )
    leaking = hk.possible_hidden & hk.known_not_in_hand
    if leaking:
        raise ReducerError(
            f"HandKnowledge invariant violated: possible_hidden contains "
            f"cards in known_not_in_hand: {sorted(leaking)}"
        )
