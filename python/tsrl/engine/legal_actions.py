"""
Legal action generator for Twilight Struggle.

Given a PublicState + player hand, enumerates legal ActionEncodings.

Scope (Month 1 scaffold):
  - Card legality: which cards in hand can be played this round.
  - Mode legality: INFLUENCE / COUP / REALIGN / SPACE / EVENT per card.
  - Target legality: which countries are valid for each mode.
  - Full action enumeration for COUP, REALIGN, SPACE, EVENT.
  - For INFLUENCE: enumerate all full-ops allocations (multisets of
    accessible countries of size == card.ops).

Implemented:
  - Bear Trap / Quagmire restrictions (scoring-card exemption)
  - DEFCON regional coup/realign restrictions
  - NATO / US-Japan Pact protection for accessible_countries
  - CMC coup-lock (blocks all BG coups while active)
  - Effective ops modifiers (Containment, Brezhnev, Red Scare, Iran-Contra, Vietnam Revolts)
  - Chernobyl regional influence block
  - China Card +1 Asia ops (in enumerate_actions / sample_action)
  - NATO prerequisite enforcement (Warsaw Pact or Marshall Plan required)
  - UN Intervention (32): EVENT blocked when player holds no eligible opponent cards

Remaining stubs (not yet enforced in legality):
  - (none of note for Month 1)
"""
from __future__ import annotations

from itertools import combinations_with_replacement
from typing import Sequence

from tsrl.engine.adjacency import load_adjacency
from tsrl.etl.game_data import CardSpec, load_cards, load_countries
from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Region, Side

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_CHINA_CARD_ID: int = 6
# DEFCON levels at which coup is illegal in battlegrounds.
_COUP_FORBIDDEN_DEFCON: int = 2  # at DEFCON 2 and below, coups in BGs would end game

# Last turn of each era and ARs per turn (for scoring-card forced-play rule).
# Scoring cards must be played before the end of their era's last turn.

# ---------------------------------------------------------------------------
# DEFCON regional restriction for coup / realign
# ---------------------------------------------------------------------------
# Per official TS rules, coups AND realignments are forbidden in certain
# regions depending on DEFCON level:
#   DEFCON 5: all regions open
#   DEFCON 4: Europe forbidden (threshold=4 → forbidden when defcon <= 4)
#   DEFCON 3: Europe + Asia/SE-Asia forbidden (threshold=3)
#   DEFCON 2: Europe + Asia/SE-Asia + Middle East forbidden (threshold=2)
#   Africa, Central America, South America: never forbidden by DEFCON
#
# A region is forbidden at the current DEFCON level when:
#   pub.defcon <= _DEFCON_REGION_THRESHOLD[region]
_DEFCON_REGION_THRESHOLD: dict[Region, int] = {
    Region.EUROPE:         4,  # forbidden at DEFCON ≤ 4
    Region.ASIA:           3,  # forbidden at DEFCON ≤ 3
    Region.SOUTHEAST_ASIA: 3,  # SE Asia counts with Asia
    Region.MIDDLE_EAST:    2,  # forbidden at DEFCON ≤ 2
    Region.AFRICA:         1,  # never forbidden (DEFCON 1 = game over anyway)
    Region.CENTRAL_AMERICA: 1,
    Region.SOUTH_AMERICA:  1,
}

# Superpower anchor IDs — never valid coup/realign targets.
_SUPERPOWER_IDS: frozenset[int] = frozenset({81, 82})

# Space Race: roll requirements to advance each level.
# Index i = current space level (0..7); value = max die roll that advances (≤ to succeed).
# Empirically verified from corpus logs ("Needed X or less" lines at each level).
_SPACE_ADVANCE_THRESHOLD = [3, 4, 3, 4, 3, 4, 3, 2]  # ≤ this to advance

# Space Race: each side may attempt once per turn; a second attempt requires
# the opponent to have already attempted (simplified: tracked via pub.space).
# For Month 1 we just check the ops requirement.
_SPACE_OPS_MINIMUM = [2, 2, 2, 2, 3, 3, 3, 4]  # min ops needed per level attempt
# Empirically verified from 50+ TSEspionage replay logs:
# levels 0-3 accept 2-ops cards; levels 4-6 require 3+; level 7 requires 4+.


# ---------------------------------------------------------------------------
# NATO / US-Japan protection
# ---------------------------------------------------------------------------

# Western Europe country IDs (same set as in events.py)
_NATO_WE: frozenset[int] = frozenset({1, 2, 4, 7, 8, 10, 11, 14, 15, 16, 17, 18})
# Benelux(1), Canada(2), Denmark(4), France(7), Greece(8), Italy(10),
# Norway(11), SpainPortugal(14), Sweden(15), Turkey(16), UK(17), WestGermany(18)

_JAPAN_ID: int = 22


# ---------------------------------------------------------------------------
# Country region cache for DEFCON restriction checks
# ---------------------------------------------------------------------------

_COUNTRY_REGION_CACHE: dict[int, Region] | None = None


def _country_regions() -> dict[int, Region]:
    """Return {country_id: Region} for DEFCON restriction checks. Cached."""
    global _COUNTRY_REGION_CACHE
    if _COUNTRY_REGION_CACHE is None:
        _COUNTRY_REGION_CACHE = {
            cid: spec.region for cid, spec in load_countries().items()
        }
    return _COUNTRY_REGION_CACHE


def _is_defcon_restricted(country_id: int, pub: PublicState) -> bool:
    """Return True if coup/realign in this country is forbidden at current DEFCON.

    Superpower anchor IDs are always excluded.
    A region is forbidden when pub.defcon <= the region's threshold.
    """
    if country_id in _SUPERPOWER_IDS:
        return True
    region = _country_regions().get(country_id)
    if region is None:
        return False
    threshold = _DEFCON_REGION_THRESHOLD.get(region, 1)
    return pub.defcon <= threshold


# ---------------------------------------------------------------------------
# Card loading helper
# ---------------------------------------------------------------------------

_CARDS: dict[int, CardSpec] | None = None


def _cards() -> dict[int, CardSpec]:
    global _CARDS
    if _CARDS is None:
        _CARDS = load_cards()
    return _CARDS


# ---------------------------------------------------------------------------
# Ops modifier / NATO helpers
# ---------------------------------------------------------------------------


def effective_ops(card_id: int, pub: PublicState, side: Side) -> int:
    """Return effective ops for a card considering current ops modifiers.

    Accounts for Containment (+1 US), Brezhnev Doctrine (+1 USSR),
    Red Scare/Purge (-1 opponent), Iran-Contra Scandal (-1 US).
    Vietnam Revolts is tracked globally via ops_modifier[USSR] as a
    slight simplification (bonus applies globally, not just SE Asia).
    Min effective ops = 1.
    """
    spec = _cards().get(card_id)
    if spec is None:
        return 1
    base = spec.ops
    mod = pub.ops_modifier[int(side)]
    return max(1, base + mod)


def _nato_prerequisite_met(pub: PublicState) -> bool:
    """Return True once any card that enables NATO has resolved."""
    return (
        pub.warsaw_pact_played
        or pub.marshall_plan_played
        or pub.truman_doctrine_played
    )


def _nato_protected(cid: int, pub: PublicState) -> bool:
    """Return True if cid is currently NATO-protected against USSR coups/realigns.

    A WE country is protected if:
      - NATO is active
      - The country is in the WE NATO set
      - The country is NOT excepted (France if de_gaulle_active; WG if willy_brandt_active)
      - The US controls the country
    """
    if not pub.nato_active:
        return False
    if cid not in _NATO_WE:
        return False
    if cid == 7 and pub.de_gaulle_active:   # France (7) excluded if De Gaulle active
        return False
    if cid == 18 and pub.willy_brandt_active:  # WestGermany (18) excluded if Willy Brandt active
        return False
    # Check US control: need US inf >= opp inf + stability
    from tsrl.engine.events import _controls as _ctrl
    return _ctrl(Side.US, cid, pub)


def accessible_countries(
    side: Side,
    pub: PublicState,
    adj: dict[int, frozenset[int]] | None = None,
    *,
    mode: ActionMode = ActionMode.INFLUENCE,
) -> frozenset[int]:
    """Return countries reachable for ops placement.

    For COUP and REALIGN, excludes NATO-protected countries (if NATO active)
    and Japan (if US-Japan Pact active), for USSR only.
    """
    from tsrl.engine.adjacency import accessible_countries as _base_accessible
    base = _base_accessible(side, pub, adj)

    if mode == ActionMode.INFLUENCE:
        # Chernobyl (97): USSR cannot place ops-influence in the designated region this turn.
        if side == Side.USSR and pub.chernobyl_blocked_region is not None:
            countries = load_countries()
            blocked = frozenset(
                cid for cid in base
                if countries.get(cid) and countries[cid].region == pub.chernobyl_blocked_region
            )
            if blocked:
                return frozenset(base - blocked)
        return base

    # For COUP/REALIGN (both sides): filter DEFCON-restricted regions.
    excluded: set[int] = set()
    for cid in base:
        if _is_defcon_restricted(cid, pub):
            excluded.add(cid)

    # For USSR COUP/REALIGN only: also filter NATO-protected and Japan-pact-blocked.
    if side == Side.USSR:
        for cid in base:
            if _nato_protected(cid, pub):
                excluded.add(cid)
        if pub.us_japan_pact_active and _JAPAN_ID in base:
            excluded.add(_JAPAN_ID)

    if not excluded:
        return base
    return frozenset(base - excluded)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def legal_cards(
    hand: frozenset[int],
    pub: PublicState,
    side: Side,
    *,
    holds_china: bool = False,
) -> frozenset[int]:
    """Return the subset of hand cards that can legally be played this AR.

    Rules applied here:
      - China Card (id=6) is legal only if held face-up (holds_china=True).
      - All other hand cards are legal.

    Scoring card hold enforcement is NOT done here. The rules only say scoring
    cards may never be *held at cleanup* (GMT Deluxe §4.5D). Enforcement lives
    in _end_of_turn(): holding a scoring card there is an immediate loss.
    Forcing play via legal_cards would block legitimate VP-win plays on the same
    AR (e.g. VP=19, play +1 VP event to win before cleanup with scoring card still
    in hand).

    Not yet checked (stubs):
      - Bear Trap / Quagmire: card restricted to ops use only.
    """
    legal: set[int] = set(hand)

    # China Card: only legal if held face-up by this side.
    if _CHINA_CARD_ID in legal:
        if not holds_china:
            legal.discard(_CHINA_CARD_ID)

    return frozenset(legal)


def legal_modes(
    card_id: int,
    pub: PublicState,
    side: Side,
    adj: dict | None = None,
) -> frozenset[ActionMode]:
    """Return legal ActionModes for playing card_id given current state.

    Rules:
      - INFLUENCE: always legal if card has ops > 0 and accessible countries exist.
      - COUP: legal if card has ops ≥ 1, DEFCON > 1, and accessible countries exist.
        (Coups in battlegrounds at DEFCON 2 can trigger nuclear war — legal but risky.)
      - REALIGN: legal if card has ops ≥ 1 and accessible countries exist.
      - SPACE: legal if current space level < 8 and card meets ops minimum,
        and this side has not already space-raced this turn.
      - EVENT: legal if card-specific prerequisites are satisfied.

    Not yet checked (stubs):
      - Bear Trap / Quagmire forced ops restriction.
      - NORAD effect on coup legality.
      - Formosan Resolution / other special restrictions.
    """
    cards = _cards()
    if card_id not in cards:
        return frozenset()

    spec = cards[card_id]
    modes: set[ActionMode] = set()
    g = adj or load_adjacency()
    accessible_inf = accessible_countries(side, pub, g, mode=ActionMode.INFLUENCE)
    accessible_coup = accessible_countries(side, pub, g, mode=ActionMode.COUP)
    accessible_realign = accessible_countries(side, pub, g, mode=ActionMode.REALIGN)

    if spec.ops > 0:
        # INFLUENCE: need at least 1 accessible country.
        if accessible_inf:
            modes.add(ActionMode.INFLUENCE)

        # COUP: ops > 0, DEFCON > 1, accessible countries exist (after NATO filter).
        if pub.defcon > 1 and accessible_coup:
            modes.add(ActionMode.COUP)

        # REALIGN: ops > 0, accessible countries exist (after NATO filter).
        if accessible_realign:
            modes.add(ActionMode.REALIGN)

        # SPACE: any card with ops >= 1 may be played for Space Race (to discard it),
        # as long as space level < 8 and the per-turn attempt limit hasn't been reached.
        # §6.4.2 ops minimum (_SPACE_OPS_MINIMUM) gates whether an *advance* roll is
        # possible — not whether the play itself is legal.  The digital game (TSEspionage)
        # allows discarding any low-ops card via space (opponent cards with 1 op are
        # commonly discarded this way), confirmed by observed replay logs.
        # Exception: reaching space 2 (Animal in Space) grants the ability to
        # play 2 Space Race cards per turn; this ability is cancelled when the
        # opponent also reaches space 2 (§6.4.4).
        level = pub.space[int(side)]
        if level < 8:
            opp = Side.US if side == Side.USSR else Side.USSR
            opp_level = pub.space[int(opp)]
            max_space = 2 if (level >= 2 and opp_level < 2) else 1
            attempts = pub.space_attempts[int(side)]
            if attempts < max_space:
                modes.add(ActionMode.SPACE)

    # EVENT: legal for any card, regardless of which side it belongs to.
    # A player may always choose to play a card for its event effect.
    # - Own/neutral card: fires your event.
    # - Opponent's card: fires their event (rare, but legal — e.g. discarding
    #   a scoring card you can't hold across a turn boundary).
    # Trap restrictions below will remove EVENT if Bear Trap / Quagmire is active.
    modes.add(ActionMode.EVENT)
    if card_id == 21 and not _nato_prerequisite_met(pub):
        modes.discard(ActionMode.EVENT)

    # Trap enforcement: Bear Trap (USSR) and Quagmire (US).
    # While trapped, the player may only use cards for ops (INFLUENCE/COUP/REALIGN).
    # EVENT and SPACE modes are unavailable until the trap is broken.
    # Exception: scoring cards have 0 ops and cannot be played for ops at all.
    # A trapped player must still be able to play scoring cards as EVENT (the only
    # legal mode for them); otherwise the player has no legal move and deadlocks.
    spec = _cards().get(card_id)
    is_scoring = spec is not None and spec.is_scoring
    if pub.bear_trap_active and side == Side.USSR and not is_scoring:
        modes -= {ActionMode.EVENT, ActionMode.SPACE}
    if pub.quagmire_active and side == Side.US and not is_scoring:
        modes -= {ActionMode.EVENT, ActionMode.SPACE}

    # Cuban Missile Crisis: coups are illegal for both sides while CMC is active.
    if pub.cuban_missile_crisis_active and ActionMode.COUP in modes:
        modes = modes - {ActionMode.COUP}

    # Wargames (103) may only be played as EVENT at DEFCON 2.
    _WARGAMES_ID = 103
    if card_id == _WARGAMES_ID and ActionMode.EVENT in modes:
        if pub.defcon != 2:
            modes = modes - {ActionMode.EVENT}

    return frozenset(modes)


def legal_countries(
    card_id: int,
    mode: ActionMode,
    pub: PublicState,
    side: Side,
    adj: dict | None = None,
) -> frozenset[int]:
    """Return the set of countries that are valid primary targets for (card, mode).

    For INFLUENCE / COUP / REALIGN: accessible countries.
    For SPACE / EVENT: empty (no country target).
    """
    if mode in (ActionMode.SPACE, ActionMode.EVENT):
        return frozenset()
    g = adj or load_adjacency()
    return accessible_countries(side, pub, g, mode=mode)


def enumerate_actions(
    hand: frozenset[int],
    pub: PublicState,
    side: Side,
    *,
    holds_china: bool = False,
    adj: dict | None = None,
    max_influence_targets: int = 84,
) -> list[ActionEncoding]:
    """Enumerate all legal actions for a player at an action round.

    For COUP, REALIGN, SPACE, EVENT: one ActionEncoding per (card, mode[, country]).
    For INFLUENCE: all multisets of size card.ops from accessible countries
    (combinatorially complete but bounded by max_influence_targets to avoid explosion).

    Args:
        max_influence_targets: cap on accessible countries considered for influence
            allocation enumeration.  Set to a small value (e.g. 10) for fast random
            play; None or large value for complete enumeration.
    """
    g = adj or load_adjacency()
    cards_spec = _cards()
    playable = legal_cards(hand, pub, side, holds_china=holds_china)
    actions: list[ActionEncoding] = []

    _UN_INTERVENTION_ID = 32
    for card_id in sorted(playable):
        if card_id not in cards_spec:
            continue
        spec = cards_spec[card_id]
        modes = legal_modes(card_id, pub, side, adj=g)
        # UN Intervention (32): EVENT is a wasted no-op if player holds no eligible
        # opponent cards to discard.  Remove EVENT mode in that case.
        if card_id == _UN_INTERVENTION_ID and not _has_eligible_opponent_card(hand, side):
            modes = modes - {ActionMode.EVENT}

        for mode in modes:
            if mode == ActionMode.SPACE:
                actions.append(ActionEncoding(card_id=card_id, mode=mode, targets=()))
                continue

            if mode == ActionMode.EVENT:
                actions.append(ActionEncoding(card_id=card_id, mode=mode, targets=()))
                continue

            ops = effective_ops(card_id, pub, side)
            accessible = sorted(accessible_countries(side, pub, g, mode=mode))
            if not accessible:
                continue

            if mode == ActionMode.COUP:
                for country in accessible:
                    actions.append(ActionEncoding(
                        card_id=card_id, mode=mode, targets=(country,),
                    ))

            elif mode == ActionMode.REALIGN:
                # Each op is one realignment attempt at a country; ops realigns total.
                # Enumerate as multisets of size ops from accessible countries.
                pool = accessible[:max_influence_targets]
                for combo in _multisets(pool, ops):
                    actions.append(ActionEncoding(
                        card_id=card_id, mode=mode, targets=combo,
                    ))
                # China Card: also enumerate 5-op (ops+1) combos if all targets are in Asia.
                if card_id == _CHINA_CARD_ID:
                    _ctry = load_countries()
                    asia_pool = [c for c in accessible if _ctry.get(c) and _ctry[c].region == Region.ASIA]
                    asia_pool = asia_pool[:max_influence_targets]
                    if asia_pool:
                        for combo in _multisets(asia_pool, ops + 1):
                            actions.append(ActionEncoding(
                                card_id=card_id, mode=mode, targets=combo,
                            ))

            elif mode == ActionMode.INFLUENCE:
                # Each op places 1 influence in a country.
                # Enumerate all multisets of size ops from accessible countries.
                pool = accessible[:max_influence_targets]
                for combo in _multisets(pool, ops):
                    actions.append(ActionEncoding(
                        card_id=card_id, mode=mode, targets=combo,
                    ))
                # China Card: also enumerate 5-op (ops+1) combos if all targets are in Asia.
                if card_id == _CHINA_CARD_ID:
                    _ctry = load_countries()
                    asia_pool = [c for c in accessible if _ctry.get(c) and _ctry[c].region == Region.ASIA]
                    asia_pool = asia_pool[:max_influence_targets]
                    if asia_pool:
                        for combo in _multisets(asia_pool, ops + 1):
                            actions.append(ActionEncoding(
                                card_id=card_id, mode=mode, targets=combo,
                            ))

    return actions


def sample_action(
    hand: frozenset[int],
    pub: PublicState,
    side: Side,
    *,
    holds_china: bool = False,
    adj: dict | None = None,
    rng=None,
) -> "ActionEncoding | None":
    """Sample one random legal action without enumerating all actions.

    O(|hand| + |accessible|) instead of O(C(accessible+ops, ops)).
    Returns None if no legal actions exist.
    """
    import random as _rand
    r = rng if rng is not None else _rand
    g = adj or load_adjacency()
    cards_spec = _cards()

    playable = sorted(legal_cards(hand, pub, side, holds_china=holds_china))
    r.shuffle(playable)

    _UN_INTERVENTION_ID = 32
    for card_id in playable:
        if card_id not in cards_spec:
            continue
        spec = cards_spec[card_id]
        modes = legal_modes(card_id, pub, side, adj=g)
        if card_id == _UN_INTERVENTION_ID and not _has_eligible_opponent_card(hand, side):
            modes = modes - {ActionMode.EVENT}
        modes = sorted(modes)
        if not modes:
            continue
        mode = r.choice(modes)

        if mode in (ActionMode.SPACE, ActionMode.EVENT):
            return ActionEncoding(card_id=card_id, mode=mode, targets=())

        accessible = sorted(accessible_countries(side, pub, g, mode=mode))
        if not accessible:
            continue

        if mode == ActionMode.COUP:
            target = r.choice(accessible)
            return ActionEncoding(card_id=card_id, mode=mode, targets=(target,))

        # INFLUENCE or REALIGN: sample ops countries with replacement.
        ops = effective_ops(card_id, pub, side)
        # China Card: with 50% probability, sample 5 ops from Asia-only pool.
        if card_id == _CHINA_CARD_ID:
            _ctry = load_countries()
            asia_accessible = [c for c in accessible if _ctry.get(c) and _ctry[c].region == Region.ASIA]
            if asia_accessible and r.random() < 0.5:
                targets = tuple(r.choice(asia_accessible) for _ in range(ops + 1))
                return ActionEncoding(card_id=card_id, mode=mode, targets=targets)
        targets = tuple(r.choice(accessible) for _ in range(ops))
        return ActionEncoding(card_id=card_id, mode=mode, targets=targets)

    return None


def has_legal_action(
    hand: frozenset[int],
    pub: PublicState,
    side: Side,
    *,
    holds_china: bool = False,
    adj: dict | None = None,
) -> bool:
    """Return True iff the player has at least one legal action.

    Faster than enumerate_actions for game-end detection purposes.
    """
    g = adj or load_adjacency()
    playable = legal_cards(hand, pub, side, holds_china=holds_china)
    for card_id in playable:
        modes = legal_modes(card_id, pub, side, adj=g)
        if modes:
            return True
    return False


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _has_eligible_opponent_card(hand: frozenset[int], side: Side) -> bool:
    """Return True if hand contains at least one non-scoring opponent-side card.

    Used for UN Intervention (32) legality: the card is a no-op if the player
    holds no opponent cards to discard.
    """
    cards_spec = _cards()
    opp = Side.US if side == Side.USSR else Side.USSR
    return any(
        cid != _CHINA_CARD_ID
        and cid in cards_spec
        and cards_spec[cid].side == opp
        and not cards_spec[cid].is_scoring
        for cid in hand
    )


def _multisets(pool: list[int], size: int) -> list[tuple[int, ...]]:
    """All multisets of given size drawn from pool (with replacement)."""
    if size == 0:
        return [()]
    if not pool:
        return []
    return [combo for combo in combinations_with_replacement(pool, size)]
