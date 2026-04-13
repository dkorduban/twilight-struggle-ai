"""
Category C event handlers — card/hand/deck manipulation.

These handlers require access to GameState (hands + deck), so they cannot
live in events.py (which only gets PublicState). They are dispatched from
game_loop.py via apply_hand_event().

Handler contract:
  - gs is the live GameState (mutable, not a copy)
  - Handlers call _copy_pub() to get a mutable pub copy, then modify it in-place
  - Handlers modify gs.hands and gs.deck in-place
  - Handlers set gs.pub = pub before returning
  - Return (new_pub, game_over, winner)
"""
from __future__ import annotations

from ._deprecation import warn_engine_deprecated

warn_engine_deprecated(__name__)

from typing import Optional

from tsrl.engine.rng import RNG

from tsrl.engine.adjacency import accessible_countries as _base_accessible
from tsrl.engine.adjacency import load_adjacency
from tsrl.engine.game_state import GameState
from tsrl.engine.step import _copy_pub
from tsrl.engine.events import (
    _check_win,
    _add_influence,
    _countries,
    _WESTERN_EUROPE,
    _EASTERN_BLOC,
    _ALL_EUROPE,
)
from tsrl.engine.legal_actions import effective_ops
from tsrl.etl.game_data import load_cards
from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Region, Side

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_CHINA_CARD_ID = 6
_WEST_GERMANY = 18

# Cat C card IDs: cards whose event handlers live here (require GameState).
_CAT_C_CARD_IDS: frozenset[int] = frozenset({
    98,   # Latin American Debt Crisis (US discard choice vs USSR +2VP)

    5,    # Five Year Plan
    10,   # Blockade
    26,   # CIA Created
    32,   # UN Intervention
    36,   # The Cambridge Five
    45,   # Quagmire
    46,   # SALT Negotiations (draw one card from discard to hand)
    47,   # Bear Trap
    52,   # Missile Envy
    68,   # Grain Sales to Soviets
    78,   # Ask Not What Your Country Can Do For You
    84,   # Our Man in Tehran
    88,   # Star Wars
    95,   # Terrorism
    101,  # Aldrich Ames Remix
    108,  # Defectors
})


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _card_played(pub: PublicState, card_id: int, side: Side) -> None:
    """Update discard/removed after a Cat C event fires. Mutates pub in-place.

    Mirrors _handle_card_played from step.py but without the 'mode' parameter.
    Cat C cards: starred events go to removed; others go to discard.
    China Card passes to opponent face-down.
    """
    if card_id == _CHINA_CARD_ID:
        opp = Side.US if side == Side.USSR else Side.USSR
        pub.china_held_by = opp
        pub.china_playable = False
        return
    cards = load_cards()
    spec = cards.get(card_id)
    if spec is None:
        return
    if spec.starred:
        pub.removed = pub.removed | {card_id}
    else:
        pub.discard = pub.discard | {card_id}


def _draw_n(gs: GameState, side: Side, rng: RNG, n: int) -> None:
    """Draw exactly n cards from gs.deck into gs.hands[side], reshuffling if needed."""
    hand_list = list(gs.hands[side])
    drawn = 0
    while drawn < n:
        if not gs.deck:
            # Reshuffle discard pile into deck.
            deck_list = list(gs.pub.discard - gs.pub.removed)
            if not deck_list:
                break
            rng.shuffle(deck_list)
            gs.deck = deck_list
            gs.pub.discard = frozenset()
        if not gs.deck:
            break
        card = gs.deck.pop()
        hand_list.append(card)
        drawn += 1
    gs.hands[side] = frozenset(hand_list)


def _apply_ops_randomly(
    pub: PublicState,
    side: Side,
    ops: int,
    rng: RNG,
    adj: dict,
) -> None:
    """Apply ops randomly for self-play: pick a random mode and execute it.

    Used by Missile Envy (52) and Grain Sales (68) where a borrowed card's ops
    are played without triggering its event.
    """
    from tsrl.engine.dice import coup_result, realign_result
    accessible = sorted(_base_accessible(side, pub, adj))
    if not accessible:
        return

    # For self-play, pick a mode: INFLUENCE is most common; COUP/REALIGN less so.
    mode = rng.choice([ActionMode.INFLUENCE, ActionMode.INFLUENCE, ActionMode.COUP, ActionMode.REALIGN])
    opp = Side.US if side == Side.USSR else Side.USSR
    c = _countries()

    if mode == ActionMode.INFLUENCE:
        for _ in range(ops):
            target = rng.choice(accessible)
            pub.influence[(side, target)] = pub.influence.get((side, target), 0) + 1

    elif mode == ActionMode.COUP:
        # Never coup a battleground at DEFCON ≤ 2 — that lowers DEFCON to 1 (nuclear war).
        safe_targets = (
            [t for t in accessible if not (c.get(t) and c[t].is_battleground)]
            if pub.defcon <= 2
            else accessible
        )
        target = rng.choice(safe_targets if safe_targets else accessible)
        stability = c[target].stability if target in c else 1
        is_bg = c[target].is_battleground if target in c else False
        net = coup_result(ops, stability, rng=rng)
        if net > 0:
            opp_inf = pub.influence.get((opp, target), 0)
            removed = min(net, opp_inf)
            new_opp = opp_inf - removed
            if new_opp <= 0:
                pub.influence.pop((opp, target), None)
            else:
                pub.influence[(opp, target)] = new_opp
            excess = net - removed
            if excess > 0:
                own = pub.influence.get((side, target), 0)
                pub.influence[(side, target)] = own + excess
        if is_bg and not (side == Side.US and pub.nuclear_subs_active):
            pub.defcon = max(1, pub.defcon - 1)
        pub.milops[int(side)] = max(pub.milops[int(side)], ops)

    else:  # REALIGN
        for _ in range(min(ops, len(accessible))):
            target = rng.choice(accessible)
            ussr_inf = pub.influence.get((Side.USSR, target), 0)
            us_inf = pub.influence.get((Side.US, target), 0)

            def _adj_ctrl(s: Side) -> int:
                count = 0
                for nbr in adj.get(target, frozenset()):
                    own = pub.influence.get((s, nbr), 0)
                    op = pub.influence.get((Side.US if s == Side.USSR else Side.USSR, nbr), 0)
                    stab = c[nbr].stability if nbr in c else 1
                    if own >= op + stab:
                        count += 1
                return count

            ut, ust = realign_result(ussr_inf, us_inf, _adj_ctrl(Side.USSR), _adj_ctrl(Side.US), rng=rng)
            if ut > ust:
                cur = pub.influence.get((Side.US, target), 0)
                if cur > 0:
                    pub.influence[(Side.US, target)] = cur - 1
                    if pub.influence[(Side.US, target)] == 0:
                        pub.influence.pop((Side.US, target), None)
            elif ust > ut:
                cur = pub.influence.get((Side.USSR, target), 0)
                if cur > 0:
                    pub.influence[(Side.USSR, target)] = cur - 1
                    if pub.influence[(Side.USSR, target)] == 0:
                        pub.influence.pop((Side.USSR, target), None)


# ---------------------------------------------------------------------------
# Individual Cat C handlers
# ---------------------------------------------------------------------------


def _h_five_year_plan(
    gs: GameState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 5: Five Year Plan. Randomly discard one card from USSR hand.
    If the discarded card is a US-side card, its event fires immediately.
    """
    pub = _copy_pub(gs.pub)
    cards = load_cards()
    ussr_hand = sorted(gs.hands[Side.USSR])
    if not ussr_hand:
        _card_played(pub, 5, side)
        gs.pub = pub
        return pub, *_check_win(pub)

    target = rng.choice(ussr_hand)
    gs.hands[Side.USSR] = gs.hands[Side.USSR] - {target}
    spec = cards.get(target)
    if spec and spec.starred:
        pub.removed = pub.removed | {target}
    else:
        pub.discard = pub.discard | {target}

    # If the discarded card is a scoring card, the region scores immediately.
    if spec and spec.is_scoring:
        from tsrl.engine.scoring import apply_scoring_card
        gs.pub = pub  # sync before scoring call
        result = apply_scoring_card(target, pub)
        pub.vp += result.vp_delta
        pub.discard = pub.discard | {target}
        if result.game_over:
            _card_played(pub, 5, side)
            gs.pub = pub
            return pub, True, result.winner
    # If the discarded card is a US-side non-scoring card, its event fires immediately.
    elif spec and spec.side == Side.US and not spec.is_scoring:
        from tsrl.engine.events import apply_event_card
        pub, over, winner = apply_event_card(pub, target, Side.US, rng)
        if over:
            _card_played(pub, 5, side)
            gs.pub = pub
            return pub, True, winner

    _card_played(pub, 5, side)
    gs.pub = pub
    return pub, *_check_win(pub)


def _h_blockade(
    gs: GameState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 10: Blockade*. Unless US discards a card with ops >= 3,
    remove all US influence from West Germany.
    """
    pub = _copy_pub(gs.pub)
    cards = load_cards()
    us_hand = gs.hands[Side.US]
    # Eligible: US hand cards (not China Card) with effective ops >= 3.
    eligible = [
        cid for cid in us_hand
        if cid != _CHINA_CARD_ID
        and cards.get(cid)
        and effective_ops(cid, pub, Side.US) >= 3
    ]
    if eligible:
        # US discards one randomly (for self-play).
        chosen = rng.choice(sorted(eligible))
        gs.hands[Side.US] = us_hand - {chosen}
        spec = cards.get(chosen)
        if spec and spec.starred:
            pub.removed = pub.removed | {chosen}
        else:
            pub.discard = pub.discard | {chosen}
    else:
        # No eligible card: remove all US inf from West Germany.
        pub.influence.pop((Side.US, _WEST_GERMANY), None)

    _card_played(pub, 10, side)
    gs.pub = pub
    return pub, *_check_win(pub)


def _h_cia_created(
    gs: GameState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 26: CIA Created*. USSR reveals their hand (no public state change needed).
    US gains 1 free influence placement in any accessible country.
    """
    pub = _copy_pub(gs.pub)
    adj = load_adjacency()
    accessible = sorted(_base_accessible(Side.US, pub, adj))
    if accessible:
        target = rng.choice(accessible)
        pub.influence[(Side.US, target)] = pub.influence.get((Side.US, target), 0) + 1

    _card_played(pub, 26, side)
    gs.pub = pub
    return pub, *_check_win(pub)


def _h_un_intervention(
    gs: GameState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 32: UN Intervention. Play one opponent's card from your hand for its ops
    value (without triggering its event). The card is then discarded.
    UN Intervention itself is also discarded.
    """
    pub = _copy_pub(gs.pub)
    cards = load_cards()
    opp = Side.US if side == Side.USSR else Side.USSR
    my_hand = gs.hands[side]

    # Eligible: opponent-side non-scoring cards.
    eligible = [
        cid for cid in my_hand
        if cid != _CHINA_CARD_ID
        and cards.get(cid)
        and cards[cid].side == opp
        and not cards[cid].is_scoring
    ]
    if not eligible:
        # No eligible card: no ops effect.
        _card_played(pub, 32, side)
        gs.pub = pub
        return pub, *_check_win(pub)

    chosen = rng.choice(sorted(eligible))
    ops = effective_ops(chosen, pub, side)

    # Remove chosen card from hand; event does NOT fire.
    gs.hands[side] = my_hand - {chosen}
    spec_chosen = cards.get(chosen)
    if spec_chosen and spec_chosen.starred:
        pub.removed = pub.removed | {chosen}
    else:
        pub.discard = pub.discard | {chosen}

    # Apply the chosen card's ops randomly (simplified for self-play).
    adj = load_adjacency()
    _apply_ops_randomly(pub, side, ops, rng, adj)

    _card_played(pub, 32, side)
    gs.pub = pub
    return pub, *_check_win(pub)


def _h_cambridge_five(
    gs: GameState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 36: The Cambridge Five*. US reveals their hand.
    For each scoring card in the US hand, USSR places 1 influence in a country
    in that scoring card's region.
    """
    pub = _copy_pub(gs.pub)
    cards = load_cards()

    # Build scoring card -> Region map from card names.
    scoring_name_keywords: dict[str, Region] = {
        'europe': Region.EUROPE,
        'asia': Region.ASIA,
        'middle east': Region.MIDDLE_EAST,
        'central america': Region.CENTRAL_AMERICA,
        'south america': Region.SOUTH_AMERICA,
        'africa': Region.AFRICA,
        'southeast asia': Region.SOUTHEAST_ASIA,
    }
    scoring_region_map: dict[int, Region] = {}
    for cid, spec in cards.items():
        if spec.is_scoring:
            name_lower = spec.name.lower()
            for keyword, region in scoring_name_keywords.items():
                if keyword in name_lower:
                    scoring_region_map[cid] = region
                    break

    # Region -> list of valid country IDs (excluding special IDs 64, 81, 82).
    c = _countries()
    region_to_countries: dict[Region, list[int]] = {}
    for cid_c, spec_c in c.items():
        if cid_c not in {64, 81, 82}:
            r = spec_c.region
            region_to_countries.setdefault(r, []).append(cid_c)

    # Find scoring cards in US hand.
    us_hand = gs.hands[Side.US]
    regions_present: set[Region] = set()
    for cid in us_hand:
        if cid in scoring_region_map:
            regions_present.add(scoring_region_map[cid])

    # For each region present, USSR places 1 influence in a country in that region.
    for region in sorted(regions_present, key=lambda r: int(r)):
        country_pool = region_to_countries.get(region, [])
        if country_pool:
            target = rng.choice(sorted(country_pool))
            pub.influence[(Side.USSR, target)] = pub.influence.get((Side.USSR, target), 0) + 1

    _card_played(pub, 36, side)
    gs.pub = pub
    return pub, *_check_win(pub)


def _h_quagmire(
    gs: GameState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 45: Quagmire*. US player is trapped: each AR US must discard a card worth
    >= 2 ops; trap broken when a valid card is discarded.

    This handler sets the quagmire_active flag. Legal action enforcement is in
    legal_modes() which removes EVENT and SPACE for US while quagmire_active.

    Escape mechanic implemented in game_loop._resolve_trap_ar:
    each AR the trapped player discards a 2+ ops non-scoring card and rolls 1d6;
    roll 1-4 = escape (trap cleared), roll 5-6 = remain trapped.
    """
    pub = _copy_pub(gs.pub)
    pub.quagmire_active = True
    _card_played(pub, 45, side)
    gs.pub = pub
    return pub, *_check_win(pub)


def _h_bear_trap(
    gs: GameState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 47: Bear Trap*. USSR player is trapped symmetrically to Quagmire.

    Sets bear_trap_active flag; legal_modes() removes EVENT and SPACE for USSR.

    Escape mechanic implemented in game_loop._resolve_trap_ar (symmetric to Quagmire).
    """
    pub = _copy_pub(gs.pub)
    pub.bear_trap_active = True
    _card_played(pub, 47, side)
    gs.pub = pub
    return pub, *_check_win(pub)


def _h_missile_envy(
    gs: GameState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 52: Missile Envy. Take the highest-ops card from opponent's hand and play
    it immediately for its ops value (event does not fire); opponent then gets it back.
    """
    pub = _copy_pub(gs.pub)
    cards = load_cards()
    opp = Side.US if side == Side.USSR else Side.USSR

    opp_hand = sorted(gs.hands[opp])
    non_scoring = [
        cid for cid in opp_hand
        if cid != _CHINA_CARD_ID and cards.get(cid) and not cards[cid].is_scoring
    ]
    if not non_scoring:
        _card_played(pub, 52, side)
        gs.pub = pub
        return pub, *_check_win(pub)

    # Find highest-ops card; ties broken randomly via sorted+choice.
    max_ops = max(effective_ops(cid, pub, opp) for cid in non_scoring)
    candidates = [cid for cid in non_scoring if effective_ops(cid, pub, opp) == max_ops]
    chosen = rng.choice(sorted(candidates))

    # Temporarily remove from opponent's hand.
    gs.hands[opp] = gs.hands[opp] - {chosen}

    # Play chosen card for ops (event does NOT fire).
    ops = effective_ops(chosen, pub, side)
    adj = load_adjacency()
    _apply_ops_randomly(pub, side, ops, rng, adj)

    # Return card to opponent's hand.
    gs.hands[opp] = gs.hands[opp] | {chosen}

    # Missile Envy itself (52) is discarded normally.
    _card_played(pub, 52, side)
    gs.pub = pub
    return pub, *_check_win(pub)


def _h_grain_sales(
    gs: GameState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 68: Grain Sales to Soviets. US takes a random card from USSR hand,
    plays it immediately for its ops value (event does not fire), then returns
    it to the USSR hand.
    """
    pub = _copy_pub(gs.pub)
    cards = load_cards()

    ussr_hand = sorted(gs.hands[Side.USSR])
    non_scoring = [
        cid for cid in ussr_hand
        if cid != _CHINA_CARD_ID and cards.get(cid) and not cards[cid].is_scoring
    ]
    if not non_scoring:
        _card_played(pub, 68, side)
        gs.pub = pub
        return pub, *_check_win(pub)

    chosen = rng.choice(sorted(non_scoring))

    # Temporarily remove from USSR hand.
    gs.hands[Side.USSR] = gs.hands[Side.USSR] - {chosen}

    # US plays it for ops (event does NOT fire).
    ops = effective_ops(chosen, pub, Side.US)
    adj = load_adjacency()
    _apply_ops_randomly(pub, Side.US, ops, rng, adj)

    # Return card to USSR hand.
    gs.hands[Side.USSR] = gs.hands[Side.USSR] | {chosen}

    _card_played(pub, 68, side)
    gs.pub = pub
    return pub, *_check_win(pub)


def _h_ask_not(
    gs: GameState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 78: Ask Not What Your Country Can Do For You*.
    US may discard up to 4 cards from hand and draw replacements from deck.
    For self-play: randomly discard 0-4 non-scoring, non-China cards, draw same count.
    """
    pub = _copy_pub(gs.pub)
    cards = load_cards()

    hand = list(gs.hands[Side.US])
    discardable = [
        cid for cid in hand
        if cid != _CHINA_CARD_ID and cards.get(cid) and not cards[cid].is_scoring
    ]
    n_discard = int(rng.integers(0, len(discardable) + 1))
    if n_discard > 0:
        to_discard = [int(x) for x in rng.choice(sorted(discardable), size=n_discard, replace=False)]
        for cid in to_discard:
            gs.hands[Side.US] = gs.hands[Side.US] - {cid}
            pub.discard = pub.discard | {cid}
        # Draw exactly n_discard replacements.
        gs.pub = pub  # _draw_n reads gs.pub.discard for reshuffling
        _draw_n(gs, Side.US, rng, n_discard)
        pub = gs.pub  # _draw_n may update pub.discard on reshuffle

    _card_played(pub, 78, side)
    gs.pub = pub
    return pub, *_check_win(pub)


def _h_our_man_in_tehran(
    gs: GameState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 84: Our Man in Tehran*. US draws top 5 cards from deck; may discard any;
    returns rest to bottom of deck.
    For self-play: randomly choose to keep or discard each drawn card.
    """
    pub = _copy_pub(gs.pub)
    countries = _countries()
    us_controls_middle_east = any(
        countries[cid].region == Region.MIDDLE_EAST
        and pub.influence.get((Side.US, cid), 0)
        >= pub.influence.get((Side.USSR, cid), 0) + countries[cid].stability
        for cid in countries
    )
    if not us_controls_middle_east:
        _card_played(pub, 84, side)
        gs.pub = pub
        return pub, *_check_win(pub)
    cards = load_cards()
    gs.pub = pub  # keep pub in sync before draw operations

    drawn: list[int] = []
    for _ in range(5):
        if not gs.deck:
            deck_list = list(pub.discard - pub.removed)
            if not deck_list:
                break
            rng.shuffle(deck_list)
            gs.deck = deck_list
            pub.discard = frozenset()
            gs.pub = pub
        if not gs.deck:
            break
        drawn.append(gs.deck.pop())

    if not drawn:
        _card_played(pub, 84, side)
        gs.pub = pub
        return pub, *_check_win(pub)

    # Randomly decide how many to keep vs discard.
    n_keep = int(rng.integers(0, len(drawn) + 1))
    shuffled = drawn[:]
    rng.shuffle(shuffled)
    to_discard = shuffled[:len(drawn) - n_keep]
    to_return = shuffled[len(drawn) - n_keep:]

    for cid in to_discard:
        spec = cards.get(cid)
        if spec and spec.starred:
            pub.removed = pub.removed | {cid}
        else:
            pub.discard = pub.discard | {cid}

    # Return rest to bottom of deck (front of list = next drawn).
    gs.deck = to_return + gs.deck

    _card_played(pub, 84, side)
    gs.pub = pub
    return pub, *_check_win(pub)


def _h_star_wars(
    gs: GameState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 88: Star Wars*. US searches discard pile, retrieves any one event card
    and plays it for its event. (Scoring cards excluded; China Card excluded.)
    """
    pub = _copy_pub(gs.pub)
    if pub.space[int(Side.US)] <= pub.space[int(Side.USSR)]:
        _card_played(pub, 88, side)
        gs.pub = pub
        return pub, *_check_win(pub)
    cards = load_cards()

    # Eligible: any card in pub.discard, not China Card, not scoring.
    eligible = [
        cid for cid in pub.discard
        if cid != _CHINA_CARD_ID and cards.get(cid) and not cards[cid].is_scoring
    ]
    if eligible:
        chosen = rng.choice(sorted(eligible))
        # Remove from discard before firing event.
        pub.discard = pub.discard - {chosen}

        from tsrl.engine.events import apply_event_card
        pub, over, winner = apply_event_card(pub, chosen, side, rng)
        if over:
            _card_played(pub, 88, side)
            gs.pub = pub
            return pub, True, winner

        # Re-discard or remove the retrieved card after its event fires.
        spec = cards.get(chosen)
        if spec and spec.starred:
            pub.removed = pub.removed | {chosen}
        else:
            pub.discard = pub.discard | {chosen}

    _card_played(pub, 88, side)
    gs.pub = pub
    return pub, *_check_win(pub)


def _h_terrorism(
    gs: GameState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 95: Terrorism. Opponent discards 1 card randomly (2 cards if Iranian
    Hostage Crisis is active and opponent is US).
    """
    pub = _copy_pub(gs.pub)
    cards = load_cards()
    opp = Side.US if side == Side.USSR else Side.USSR

    # Number of cards to discard.
    n = 2 if (opp == Side.US and pub.iran_hostage_crisis_active) else 1

    opp_hand = sorted(gs.hands[opp])
    discardable = [cid for cid in opp_hand if cid != _CHINA_CARD_ID]
    actual_n = min(n, len(discardable))
    if actual_n > 0:
        to_discard = [int(x) for x in rng.choice(sorted(discardable), size=actual_n, replace=False)]
        for cid in to_discard:
            gs.hands[opp] = gs.hands[opp] - {cid}
            spec = cards.get(cid)
            if spec and spec.starred:
                pub.removed = pub.removed | {cid}
            else:
                pub.discard = pub.discard | {cid}

    _card_played(pub, 95, side)
    gs.pub = pub
    return pub, *_check_win(pub)


def _h_aldrich_ames(
    gs: GameState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 101: Aldrich Ames Remix*. US reveals hand; USSR discards any 1 card from US hand.
    For self-play: USSR discards randomly.
    """
    pub = _copy_pub(gs.pub)
    cards = load_cards()

    us_hand = sorted(gs.hands[Side.US])
    discardable = [cid for cid in us_hand if cid != _CHINA_CARD_ID]
    if discardable:
        chosen = rng.choice(sorted(discardable))
        gs.hands[Side.US] = gs.hands[Side.US] - {chosen}
        spec = cards.get(chosen)
        if spec and spec.starred:
            pub.removed = pub.removed | {chosen}
        else:
            pub.discard = pub.discard | {chosen}

    _card_played(pub, 101, side)
    gs.pub = pub
    return pub, *_check_win(pub)


def _h_defectors(
    gs: GameState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 108: Defectors.
    - If played by USSR (as an ops play where US event fires): US gains 2 VP.
    - If played by US as Headline: USSR's Headline card is cancelled (implemented in
      _run_headline_phase in game_loop.py — card is discarded without effect there).
    - If played by US during action rounds: no board effect (Headline cancel only applies
      to Headline phase; AR play just discards the card).

    In practice this handler is called only when played as an EVENT.
    US plays it as their own event: no VP change (Headline cancellation handled upstream).
    USSR plays it (§5.2 opponent card triggers event): US gains 2 VP.
    """
    pub = _copy_pub(gs.pub)
    if side == Side.USSR:
        # USSR played opponent's card triggering the Defectors event → US gains 2 VP.
        pub.vp -= 2
    _card_played(pub, 108, side)
    gs.pub = pub
    return pub, *_check_win(pub)


# ---------------------------------------------------------------------------
# Dispatch registry
# ---------------------------------------------------------------------------

def _h_salt_negotiations(
    gs: GameState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 46: SALT Negotiations*. DEFCON +1; phasing player draws one card from discard to hand.

    events.py handles the DEFCON +1 and sets salt_active flag; this handler takes over
    to move one card from pub.discard to the phasing player's hand (requires GameState).
    For self-play: picks a random card from the discard pile.
    If the discard is empty, only the DEFCON+1 from events.py fires (no card drawn).
    """
    from tsrl.engine.events import apply_event_card
    pub = _copy_pub(gs.pub)

    # First apply the base event (DEFCON +1, salt_active flag) from events.py.
    pub, over, winner = apply_event_card(pub, 46, side, rng)
    if over:
        _card_played(pub, 46, side)
        gs.pub = pub
        return pub, over, winner

    # Draw one card from discard to phasing player's hand.
    available = sorted(pub.discard)
    if available:
        chosen = rng.choice(available)
        pub.discard = pub.discard - {chosen}
        gs.hands[side] = gs.hands[side] | {chosen}

    _card_played(pub, 46, side)
    gs.pub = pub
    return pub, *_check_win(pub)


def _h_latin_american_debt_crisis(
    gs: "GameState",
    side: Side,
    rng: RNG,
) -> tuple["PublicState", bool, Optional[Side]]:
    """Card 98: Latin American Debt Crisis*. US must discard two cards totalling 4+ ops
    or USSR gains 2 VP.

    For self-play: US discards the two cheapest non-scoring cards that sum to 4+ ops
    (prefer sacrificing low-value cards).  If no valid pair exists, USSR gains 2 VP.
    """
    from tsrl.etl.game_data import load_cards as _lc
    from itertools import combinations
    cards = _lc()
    pub = _copy_pub(gs.pub)

    # Candidates: non-scoring, non-China cards in US hand
    candidates = sorted(
        cid for cid in gs.hands[Side.US]
        if cid != 6 and cards.get(cid) and not cards[cid].is_scoring
    )

    # Find the pair with minimum total ops that still meets the 4+ ops threshold
    best_pair: Optional[tuple[int, int]] = None
    best_total = 999
    for a, b in combinations(candidates, 2):
        total = (cards[a].ops if cards.get(a) else 0) + (cards[b].ops if cards.get(b) else 0)
        if total >= 4 and total < best_total:
            best_pair = (a, b)
            best_total = total

    if best_pair is not None:
        a, b = best_pair
        gs.hands[Side.US] = gs.hands[Side.US] - {a, b}
        for cid in (a, b):
            spec = cards.get(cid)
            if spec and spec.starred:
                pub.removed = pub.removed | {cid}
            else:
                pub.discard = pub.discard | {cid}
    else:
        pub.vp += 2   # USSR gains 2 VP (US cannot pay)

    _card_played(pub, 98, side)
    gs.pub = pub
    return pub, *_check_win(pub)


_CAT_C_HANDLERS: dict[int, object] = {
    5:   _h_five_year_plan,
    10:  _h_blockade,
    26:  _h_cia_created,
    32:  _h_un_intervention,
    36:  _h_cambridge_five,
    45:  _h_quagmire,
    46:  _h_salt_negotiations,
    47:  _h_bear_trap,
    52:  _h_missile_envy,
    68:  _h_grain_sales,
    78:  _h_ask_not,
    84:  _h_our_man_in_tehran,
    88:  _h_star_wars,
    95:  _h_terrorism,
    98:  _h_latin_american_debt_crisis,
    101: _h_aldrich_ames,
    108: _h_defectors,
}


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def apply_hand_event(
    gs: GameState,
    action: ActionEncoding,
    side: Side,
    rng: RNG,
) -> tuple[PublicState, bool, Optional[Side]]:
    """Dispatch Cat C event to the appropriate handler.

    gs is the live mutable GameState (not a copy).
    Returns (new_pub, game_over, winner).
    """
    handler = _CAT_C_HANDLERS.get(action.card_id)
    if handler is None:
        # Fallback: discard card, no board effect.
        pub = _copy_pub(gs.pub)
        _card_played(pub, action.card_id, side)
        gs.pub = pub
        return pub, False, None
    return handler(gs, side, rng)  # type: ignore[operator]
