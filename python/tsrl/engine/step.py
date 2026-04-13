"""
Play-mode step interface for Twilight Struggle.

apply_action(pub, action, side, rng) → new PublicState

Fully implemented:
  - INFLUENCE placement (deterministic).
  - COUP (dice-based; DEFCON reduced in battlegrounds).
  - REALIGN (dice-based; influence removed from loser).
  - SPACE RACE (dice-based; level advanced on success).
  - EVENT (scoring cards apply scoring; all other events → discard only).

Event dispatch is intentionally minimal: non-scoring card events are no-ops
(card discarded, no board effect).  A full event registry will be added in
Month 2 without changing this interface.

Usage::

    from tsrl.engine.rng import make_rng
    from tsrl.engine.step import apply_action
    from tsrl.schemas import ActionEncoding, ActionMode, Side

    rng = make_rng(42)
    new_pub = apply_action(pub, action, side, rng=rng)
"""
from __future__ import annotations

from ._deprecation import warn_engine_deprecated

warn_engine_deprecated(__name__)

import copy
from typing import Optional

import numpy as np

from tsrl.engine.rng import RNG, make_rng

from tsrl.engine.adjacency import neighbors, load_adjacency
from tsrl.engine.dice import coup_result, realign_result, space_result
from tsrl.engine.legal_actions import _CHINA_CARD_ID, effective_ops
from tsrl.engine.scoring import apply_scoring_card, ScoringResult
from tsrl.etl.game_data import load_cards
from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Region, Side

# War cards that trigger Flower Power when US plays them for their event.
# Korean War(11), Arab-Israeli War(13), Indo-Pakistani War(24), Brush War(39), Iran-Iraq War(105).
_WAR_CARD_IDS: frozenset[int] = frozenset({11, 13, 24, 39, 105})

# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def apply_action(
    pub: PublicState,
    action: ActionEncoding,
    side: Side,
    *,
    rng: Optional[RNG] = None,
) -> tuple[PublicState, bool, Optional[Side]]:
    """Apply a legal action, returning (new_pub, game_over, winner).

    Args:
        pub:    Current public state (not mutated).
        action: Legal ActionEncoding for this side.
        side:   The acting player.
        rng:    Random number generator for stochastic actions.
                Pass None to use the module-level default RNG.

    Returns:
        (new_pub, game_over, winner):
          - new_pub:   Updated PublicState.
          - game_over: True if this action ended the game.
          - winner:    Side that won, or None if game continues.
    """
    mode = action.mode

    if mode == ActionMode.INFLUENCE:
        new_pub = _apply_influence(pub, action, side)
    elif mode == ActionMode.COUP:
        new_pub = _apply_coup(pub, action, side, rng=rng)
    elif mode == ActionMode.REALIGN:
        new_pub = _apply_realign(pub, action, side, rng=rng)
    elif mode == ActionMode.SPACE:
        new_pub = _apply_space(pub, action, side, rng=rng)
    elif mode == ActionMode.EVENT:
        new_pub, over, winner = _apply_event(pub, action, side, rng=rng)
        if over:
            return new_pub, True, winner
    else:
        raise ValueError(f"Unknown ActionMode: {mode}")

    # Check VP win condition after action.
    over, winner = _check_vp_win(new_pub)
    return new_pub, over, winner


# ---------------------------------------------------------------------------
# Influence (deterministic)
# ---------------------------------------------------------------------------


def _apply_influence(
    pub: PublicState,
    action: ActionEncoding,
    side: Side,
) -> PublicState:
    """Place 1 influence per target entry.

    Each target entry costs 1 op.  For contested placement (opponent has
    influence, side has none) the cost is 2 ops — the caller (enumerate_actions)
    is responsible for passing the correct number of target entries.
    """
    new_pub = _copy_pub(pub)
    for country_id in action.targets:
        own = new_pub.influence.get((side, country_id), 0)
        new_pub.influence[(side, country_id)] = own + 1
    _handle_card_played(new_pub, action.card_id, side, mode=ActionMode.INFLUENCE)
    # §6.3.1 CMC cancellation: auto-detect if player removed required influence.
    if new_pub.cuban_missile_crisis_active:
        _CUBA = 36
        _TURKEY = 16
        _WEST_GERMANY = 18
        ussr_cuba = new_pub.influence.get((Side.USSR, _CUBA), 0)
        us_turkey = new_pub.influence.get((Side.US, _TURKEY), 0)
        us_wg = new_pub.influence.get((Side.US, _WEST_GERMANY), 0)
        if side == Side.USSR and ussr_cuba == 0:
            new_pub.cuban_missile_crisis_active = False
        elif side == Side.US and (us_turkey == 0 or us_wg == 0):
            new_pub.cuban_missile_crisis_active = False
    return new_pub


# ---------------------------------------------------------------------------
# Coup
# ---------------------------------------------------------------------------


def _apply_coup(
    pub: PublicState,
    action: ActionEncoding,
    side: Side,
    *,
    rng: Optional[RNG],
) -> PublicState:
    """Apply a coup in action.targets[0].

    Rules:
      - Roll 1d6 + ops.  Net = roll + ops - 2 × stability.
      - If net > 0: remove net opponent influence; excess becomes own influence.
      - If net ≤ 0: no effect.
      - If target is a battleground: DEFCON drops by 1.
      - MilOps increased by card ops (or card.ops; min is used vs requirement later).
    """
    assert len(action.targets) == 1, "Coup requires exactly one target"
    country_id = action.targets[0]
    new_pub = _copy_pub(pub)
    opp = Side.US if side == Side.USSR else Side.USSR

    countries = _countries()
    ops = effective_ops(action.card_id, pub, side)
    # China Card: +1 ops if target country is in Asia (§6.x China Card bonus).
    if (
        action.card_id == _CHINA_CARD_ID
        and country_id in countries
        and countries[country_id].region == Region.ASIA
    ):
        ops += 1

    stability = countries[country_id].stability if country_id in countries else 1
    is_bg = countries[country_id].is_battleground if country_id in countries else False

    net = coup_result(ops, stability, rng=rng)

    # Latin American Death Squads (70): phasing side gets +1 to roll in C/S America;
    # opponent gets -1.  Simulated as a net modifier applied after the roll.
    if pub.latam_coup_bonus is not None:
        country_region = countries[country_id].region if country_id in countries else None
        if country_region in (Region.CENTRAL_AMERICA, Region.SOUTH_AMERICA):
            net += 1 if side == pub.latam_coup_bonus else -1

    if net > 0:
        opp_inf = new_pub.influence.get((opp, country_id), 0)
        removed = min(net, opp_inf)
        new_pub.influence[(opp, country_id)] = opp_inf - removed
        excess = net - removed
        if excess > 0:
            own = new_pub.influence.get((side, country_id), 0)
            new_pub.influence[(side, country_id)] = own + excess

    # DEFCON drops if the target is a battleground.
    # Nuclear Subs (44): US coups don't degrade DEFCON while active.
    if is_bg:
        if not (side == Side.US and new_pub.nuclear_subs_active):
            new_pub.defcon = max(1, new_pub.defcon - 1)

    # MilOps tracking.
    new_pub.milops[int(side)] = max(new_pub.milops[int(side)], ops)

    _handle_card_played(new_pub, action.card_id, side, mode=ActionMode.COUP)
    return new_pub


# ---------------------------------------------------------------------------
# Realign
# ---------------------------------------------------------------------------


def _apply_realign(
    pub: PublicState,
    action: ActionEncoding,
    side: Side,
    *,
    rng: Optional[RNG],
) -> PublicState:
    """Apply one realignment attempt per target in action.targets.

    Rules per attempt:
      - Each side rolls 1d6.
      - Modifiers: +1 if more influence in country; +1 per adjacent controlled nation.
      - Higher roll wins; loser removes 1 influence from the country.
      - Ties: no effect.
    """
    new_pub = _copy_pub(pub)
    opp = Side.US if side == Side.USSR else Side.USSR
    adj = load_adjacency()
    countries = _countries()
    cards = load_cards()
    spec = cards.get(action.card_id)
    ops = spec.ops if spec else 1

    for country_id in action.targets:
        ussr_inf = new_pub.influence.get((Side.USSR, country_id), 0)
        us_inf = new_pub.influence.get((Side.US, country_id), 0)
        stability = countries[country_id].stability if country_id in countries else 1

        # Count adjacent nations controlled by each side.
        # Superpower home spaces (id 81=USA, id 82=USSR) are excluded here
        # because they have no influence markers; their adjacency bonus is
        # applied separately via the superpower anchor check below.
        _USA_ID, _USSR_ID = 81, 82
        def _adj_controlled(s: Side) -> int:
            count = 0
            for nbr in adj.get(country_id, frozenset()):
                if nbr in (_USA_ID, _USSR_ID):
                    continue  # handled by superpower anchor check below
                own = new_pub.influence.get((s, nbr), 0)
                op = new_pub.influence.get(
                    (Side.US if s == Side.USSR else Side.USSR, nbr), 0
                )
                if own >= op + (countries[nbr].stability if nbr in countries else 1):
                    count += 1
            return count

        # §6.2.2: "+1 if your Superpower is adjacent to the target country."
        # Each side's superpower home space is always treated as controlled
        # by that side — no influence markers needed.
        neighbors = adj.get(country_id, frozenset())
        ussr_sp_bonus = 1 if _USSR_ID in neighbors else 0
        us_sp_bonus   = 1 if _USA_ID  in neighbors else 0

        ussr_total, us_total = realign_result(
            ussr_inf, us_inf,
            _adj_controlled(Side.USSR) + ussr_sp_bonus,
            _adj_controlled(Side.US)   + us_sp_bonus,
            rng=rng,
        )

        if ussr_total > us_total:
            # USSR wins: US loses min(diff, us_influence) influence.
            diff = ussr_total - us_total
            cur = new_pub.influence.get((Side.US, country_id), 0)
            new_pub.influence[(Side.US, country_id)] = max(0, cur - diff)
        elif us_total > ussr_total:
            # US wins: USSR loses min(diff, ussr_influence) influence.
            diff = us_total - ussr_total
            cur = new_pub.influence.get((Side.USSR, country_id), 0)
            new_pub.influence[(Side.USSR, country_id)] = max(0, cur - diff)

    _handle_card_played(new_pub, action.card_id, side, mode=ActionMode.REALIGN)
    return new_pub


# ---------------------------------------------------------------------------
# Space Race
# ---------------------------------------------------------------------------

# VP awards for reaching each space level (index = level reached, 1-8).
# Values: (first_to_reach_vp, second_to_reach_vp).
# Source: TS rulebook space race table, ITS rules.
_SPACE_VP: dict[int, tuple[int, int]] = {
    1: (2, 0),
    2: (0, 0),
    3: (2, 0),
    4: (0, 0),
    5: (3, 1),
    6: (0, 0),
    7: (4, 2),
    8: (2, 0),
}


def _apply_space(
    pub: PublicState,
    action: ActionEncoding,
    side: Side,
    *,
    rng: Optional[RNG],
) -> PublicState:
    """Attempt to advance in the Space Race.

    Roll 1d6; if ≥ threshold for current level, advance to next level.
    Award VP if level reached (first or second to reach).
    """
    new_pub = _copy_pub(pub)
    opp = Side.US if side == Side.USSR else Side.USSR
    current_level = new_pub.space[int(side)]

    success = space_result(current_level, rng=rng)
    if success:
        new_level = current_level + 1
        new_pub.space[int(side)] = new_level
        # Track first-to-reach for level 4 and level 6 special abilities.
        if new_level == 4 and new_pub.space_level4_first is None:
            new_pub.space_level4_first = side
        if new_level == 6 and new_pub.space_level6_first is None:
            new_pub.space_level6_first = side

        # VP award: +vp to USSR if USSR side, else +vp to US.
        first_vp, second_vp = _SPACE_VP.get(new_level, (0, 0))
        opp_level = new_pub.space[int(opp)]
        vp = first_vp if opp_level < new_level else second_vp
        if side == Side.USSR:
            new_pub.vp += vp
        else:
            new_pub.vp -= vp

    # Track per-turn space attempts for Yuri and Samantha (card 106).
    new_pub.space_attempts[int(side)] += 1

    _handle_card_played(new_pub, action.card_id, side, mode=ActionMode.SPACE)
    return new_pub


# ---------------------------------------------------------------------------
# Event dispatch (minimal: scoring cards implemented, others → no-op)
# ---------------------------------------------------------------------------


def _apply_event(
    pub: PublicState,
    action: ActionEncoding,
    side: Side,
    *,
    rng: Optional[RNG] = None,
) -> tuple[PublicState, bool, Optional[Side]]:
    """Apply card event.  Scoring cards: compute score.  Others: discard only."""
    from tsrl.etl.game_data import load_cards as _lc
    new_pub = _copy_pub(pub)
    cards = _lc()
    spec = cards.get(action.card_id)

    # Flower Power (62): USSR gains +2 VP each time US plays a war card for its event.
    if (side == Side.US
            and action.card_id in _WAR_CARD_IDS
            and new_pub.flower_power_active
            and not new_pub.flower_power_cancelled):
        new_pub.vp += 2  # USSR gains 2 VP

    if spec and spec.is_scoring:
        result: ScoringResult = apply_scoring_card(action.card_id, new_pub)
        new_pub.vp += result.vp_delta
        if result.clear_shuttle:
            new_pub.shuttle_diplomacy_active = False
        if result.game_over:
            _handle_card_played(new_pub, action.card_id, side, mode=ActionMode.EVENT)
            return new_pub, True, result.winner

    # Dispatch to event registry for non-scoring cards.
    from tsrl.engine.events import apply_event_card
    r = rng or make_rng()
    new_pub, over, winner = apply_event_card(new_pub, action.card_id, side, r)
    if over:
        _handle_card_played(new_pub, action.card_id, side, mode=ActionMode.EVENT)
        return new_pub, True, winner

    _handle_card_played(new_pub, action.card_id, side, mode=ActionMode.EVENT)
    return new_pub, False, None


# ---------------------------------------------------------------------------
# Win condition checks
# ---------------------------------------------------------------------------


def _check_vp_win(pub: PublicState) -> tuple[bool, Optional[Side]]:
    """Check for VP-based or DEFCON win condition.

    DEFCON 1: the phasing player (pub.phasing) triggered nuclear war and loses.
    """
    if pub.vp >= 20:
        return True, Side.USSR
    if pub.vp <= -20:
        return True, Side.US
    if pub.defcon <= 1:
        # Nuclear war: the side that caused DEFCON to reach 1 loses.
        # That side is pub.phasing (they played the coup / took the action).
        loser = pub.phasing
        winner = Side.US if loser == Side.USSR else Side.USSR
        return True, winner
    return False, None


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


_COUNTRY_CACHE = None


def _countries():
    global _COUNTRY_CACHE
    if _COUNTRY_CACHE is None:
        from tsrl.etl.game_data import load_countries
        _COUNTRY_CACHE = load_countries()
    return _COUNTRY_CACHE


def _handle_card_played(
    pub: PublicState,
    card_id: int,
    side: Side,
    *,
    mode: ActionMode,
) -> None:
    """Update card location after playing (mutates pub in-place).

    - China Card: passes to opponent face-down.
    - Starred card played for EVENT: removed from game.
    - All others: go to discard.
    """
    # Idempotency guard: card lifecycle runs once even if called from both event and ops paths.
    if card_id in pub.removed or card_id in pub.discard:
        return

    if card_id == _CHINA_CARD_ID:
        opp = Side.US if side == Side.USSR else Side.USSR
        pub.china_held_by = opp
        pub.china_playable = False
        return

    cards = load_cards()
    spec = cards.get(card_id)
    if spec is None:
        return

    if mode == ActionMode.EVENT and spec.starred:
        pub.removed = pub.removed | {card_id}
    else:
        pub.discard = pub.discard | {card_id}


def _copy_pub(pub: PublicState) -> PublicState:
    """Shallow copy of PublicState with mutable containers deep-copied."""
    c = copy.copy(pub)
    c.milops = list(pub.milops)
    c.space = list(pub.space)
    c.space_attempts = list(pub.space_attempts)
    c.ops_modifier = list(pub.ops_modifier)
    c.influence = pub.influence.copy()
    return c
