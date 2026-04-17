"""
Event effect handlers for Twilight Struggle cards: Categories A, B, D, E, F.

Handler contract:
  - pub is already a mutable copy (caller called _copy_pub before dispatch)
  - Handlers mutate pub in-place and return it
  - Return (pub, game_over, winner)
  - Unregistered cards return (pub, False, None) — no-op

Category C cards (hand/deck manipulation) are handled in cat_c_events.py
because they need access to GameState.hands and GameState.deck.

Remaining stubs (noted in individual docstrings):
  - UN Intervention hand-check
"""
from __future__ import annotations

from ._deprecation import warn_engine_deprecated

warn_engine_deprecated(__name__)

from typing import Callable, Collection, Optional

import numpy as np

from tsrl.engine.rng import RNG
from tsrl.schemas import ActionMode, PublicState, Region, Side

# ---------------------------------------------------------------------------
# Region / country sets
# ---------------------------------------------------------------------------

_EASTERN_BLOC = frozenset({3, 5, 9, 12, 13, 19, 83})
# Czechoslovakia(3), EastGermany(5), Hungary(9), Poland(12),
# Romania(13), Yugoslavia(19), Bulgaria(83)
# Note: Austria(0) is NOT Eastern Bloc — it is neutral/Western-aligned in TS.

_WESTERN_EUROPE = frozenset({1, 2, 4, 7, 8, 10, 11, 14, 15, 16, 17, 18})
# Benelux(1), Canada(2), Denmark(4), France(7), Greece(8), Italy(10),
# Norway(11), SpainPortugal(14), Sweden(15), Turkey(16), UK(17), WestGermany(18)

_CENTRAL_AMERICA = frozenset({36, 37, 38, 39, 40, 41, 42, 43, 44, 45})
_SOUTH_AMERICA = frozenset({46, 47, 48, 49, 50, 51, 52, 53, 54, 55})
_AFRICA = frozenset({56, 57, 58, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74})
# NOTE: LibyaAfrica(64) excluded from _AFRICA set — erroneous duplicate entry.
# Real Libya is ID 33 (MiddleEast).
_SOUTHEAST_ASIA = frozenset({75, 76, 77, 78, 79, 80})
_ALL_EUROPE = frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 83})
# Excludes superpower anchors 81, 82

# OPEC countries (MiddleEast subset + Venezuela)
_OPEC_COUNTRIES = frozenset({26, 28, 33, 34, 29, 27, 55})
# Egypt(26), Iran(28), Libya(33), SaudiArabia(34), Iraq(29), GulfStates(27), Venezuela(55)

# Middle East country IDs (26-35)
_MIDDLE_EAST = frozenset(range(26, 36))

# Individual country IDs
_CUBA = 36
_ROMANIA = 13
_EAST_GERMANY = 5
_POLAND = 12
_EGYPT = 26
_ISRAEL = 30
_JORDAN = 31
_SOUTH_KOREA = 25
_INDIA = 21
_PAKISTAN = 24
_IRAN = 28
_IRAQ = 29
_LIBYA = 33   # MiddleEast Libya (the real one)
_SAUDI_ARABIA = 34
_LEBANON = 32
_NICARAGUA = 43
_ANGOLA = 57
_MOZAMBIQUE = 66
_SOUTH_AFRICA = 71
_CHILE = 49
_VENEZUELA = 55
_WEST_GERMANY = 18
_UK = 17
_FRANCE = 7
_YUGOSLAVIA = 19
_BULGARIA = 83
_HUNGARY = 9
_CZECHOSLOVAKIA = 3

# South Africa neighbors
_SOUTH_AFRICA_NEIGHBORS = [58, 69, 74]  # Botswana(58), SEAfricanStates(69), Zimbabwe(74)

# ---------------------------------------------------------------------------
# Handler type
# ---------------------------------------------------------------------------

EventHandler = Callable[[PublicState, Side, RNG], tuple[PublicState, bool, Optional[Side]]]

# ---------------------------------------------------------------------------
# Country data cache
# ---------------------------------------------------------------------------

_COUNTRY_CACHE = None


def _countries():
    global _COUNTRY_CACHE
    if _COUNTRY_CACHE is None:
        from tsrl.etl.game_data import load_countries
        _COUNTRY_CACHE = load_countries()
    return _COUNTRY_CACHE


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


def _controls(side: Side, cid: int, pub: PublicState) -> bool:
    """Return True if side controls country (own >= opp + stability)."""
    opp = Side.US if side == Side.USSR else Side.USSR
    own = pub.influence.get((side, cid), 0)
    opp_inf = pub.influence.get((opp, cid), 0)
    c = _countries()
    stability = c[cid].stability if cid in c else 1
    return own >= opp_inf + stability


def _add_influence(pub: PublicState, side: Side, cid: int, delta: int) -> None:
    cur = pub.influence.get((side, cid), 0)
    new_val = cur + delta
    if new_val <= 0:
        pub.influence.pop((side, cid), None)
    else:
        pub.influence[(side, cid)] = new_val


def _remove_all(pub: PublicState, side: Side, cid: int) -> None:
    pub.influence.pop((side, cid), None)


def _gain_control(pub: PublicState, side: Side, cid: int) -> None:
    """Ensure side controls cid by setting own inf to opp + stability if needed."""
    opp = Side.US if side == Side.USSR else Side.USSR
    opp_inf = pub.influence.get((opp, cid), 0)
    c = _countries()
    stability = c[cid].stability if cid in c else 1
    needed = opp_inf + stability
    cur = pub.influence.get((side, cid), 0)
    if cur < needed:
        pub.influence[(side, cid)] = needed


def _free_coup(
    pub: PublicState,
    side: Side,
    cid: int,
    ops: int,
    rng: RNG,
    *,
    defcon_immune: bool = False,
) -> int:
    """Apply a free coup (event-triggered, not ops-played).

    Returns net (positive = success).
    defcon_immune=True: battleground coup does NOT reduce DEFCON (war card rule per ITS rules).
    Updates MilOps for `side` to max(current, ops).
    """
    from tsrl.engine.dice import coup_result, roll_d6, coup_net
    from tsrl.engine.event_log import log_event
    opp = Side.US if side == Side.USSR else Side.USSR
    c = _countries()
    stability = c[cid].stability if cid in c else 1
    is_bg = c[cid].is_battleground if cid in c else False
    cname = c[cid].name if cid in c else f"country#{cid}"
    roll = roll_d6(rng)
    net = coup_net(roll, ops, stability)
    side_str = "USSR" if side == Side.USSR else "US"
    result_str = f"success (net {net})" if net > 0 else "fails"
    log_event(f"Coup {cname}: {side_str} rolls {roll} + {ops} ops - 2×{stability} stability = {net} → {result_str}")
    if net > 0:
        opp_inf = pub.influence.get((opp, cid), 0)
        removed = min(net, opp_inf)
        new_opp = opp_inf - removed
        if new_opp <= 0:
            pub.influence.pop((opp, cid), None)
        else:
            pub.influence[(opp, cid)] = new_opp
        excess = net - removed
        if excess > 0:
            own = pub.influence.get((side, cid), 0)
            pub.influence[(side, cid)] = own + excess
    if is_bg and not defcon_immune:
        pub.defcon = max(1, pub.defcon - 1)
    pub.milops[int(side)] = max(pub.milops[int(side)], ops)
    return net


def _vp_delta(pub: PublicState, side: Side, delta: int) -> None:
    """Award delta VP to side. USSR gains → pub.vp increases; US gains → pub.vp decreases."""
    from tsrl.engine.event_log import log_event
    side_str = "USSR" if side == Side.USSR else "US"
    if delta != 0:
        log_event(f"VP: {side_str} {'gains' if delta > 0 else 'loses'} {abs(delta)} VP")
    if side == Side.USSR:
        pub.vp += delta
    else:
        pub.vp -= delta


def _check_win(pub: PublicState) -> tuple[bool, Optional[Side]]:
    """Check VP and DEFCON win conditions."""
    if pub.vp >= 20:
        return True, Side.USSR
    if pub.vp <= -20:
        return True, Side.US
    if pub.defcon <= 1:
        loser = pub.phasing
        winner = Side.US if loser == Side.USSR else Side.USSR
        return True, winner
    return False, None


def _sample_up_to(pool: Collection[int], n: int, rng: RNG) -> list[int]:
    """Sample min(n, len(pool)) distinct items from pool. Sorted pool for determinism."""
    pool_list = sorted(pool)
    k = min(n, len(pool_list))
    if k <= 0:
        return []
    return [int(x) for x in rng.choice(pool_list, size=k, replace=False)]


# ---------------------------------------------------------------------------
# Category A handlers — simple influence placement / removal
# ---------------------------------------------------------------------------


def _event_socialist_governments(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 7: Socialist Governments.
    Place 1 USSR inf in up to 3 Western Europe countries that are
    not US-controlled and where USSR inf < 2.
    """
    pool = [
        cid for cid in _WESTERN_EUROPE
        if not _controls(Side.US, cid, pub)
        and pub.influence.get((Side.USSR, cid), 0) < 2
    ]
    chosen = _sample_up_to(pool, 3, rng)
    for cid in chosen:
        _add_influence(pub, Side.USSR, cid, 1)
    return pub, False, None


def _event_fidel(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 8: Fidel*. Remove all US inf from Cuba; USSR gains control."""
    _remove_all(pub, Side.US, _CUBA)
    _gain_control(pub, Side.USSR, _CUBA)
    return pub, False, None


def _event_romanian_abdication(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 12: Romanian Abdication*. Remove all US from Romania; USSR gains control."""
    _remove_all(pub, Side.US, _ROMANIA)
    _gain_control(pub, Side.USSR, _ROMANIA)
    return pub, False, None


def _event_comecon(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 14: COMECON*. Place 1 USSR inf in up to 4 Eastern Bloc countries
    not US-controlled.
    """
    pool = [cid for cid in _EASTERN_BLOC if not _controls(Side.US, cid, pub)]
    chosen = _sample_up_to(pool, 4, rng)
    for cid in chosen:
        _add_influence(pub, Side.USSR, cid, 1)
    return pub, False, None


def _event_nasser(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 15: Nasser*. Add 2 USSR influence in Egypt; remove half (round up) US influence from Egypt."""
    _add_influence(pub, Side.USSR, _EGYPT, 2)
    cur_us = pub.influence.get((Side.US, _EGYPT), 0)
    remove = (cur_us + 1) // 2  # ceil(cur_us / 2)
    if remove > 0:
        _add_influence(pub, Side.US, _EGYPT, -remove)
    return pub, False, None


def _event_warsaw_pact(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 16: Warsaw Pact Formed*.
    Branch A: remove all US inf from up to 4 Eastern Bloc countries.
    Branch B: place 5 USSR inf (1 each) in up to 5 Eastern Bloc countries.
    Branch chosen randomly.
    Sets the NATO prerequisite flag for future plays.
    """
    branch = rng.choice(['A', 'B'])
    if branch == 'A':
        pool = [cid for cid in _EASTERN_BLOC if pub.influence.get((Side.US, cid), 0) > 0]
        chosen = _sample_up_to(pool, 4, rng)
        for cid in chosen:
            _remove_all(pub, Side.US, cid)
    else:
        pool = sorted(_EASTERN_BLOC)
        chosen = _sample_up_to(pool, 5, rng)
        for cid in chosen:
            _add_influence(pub, Side.USSR, cid, 1)
    pub.warsaw_pact_played = True
    return pub, False, None


def _event_independent_reds(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 22: Independent Reds*. Place 1 US inf in each of 5 fixed countries."""
    for cid in [_YUGOSLAVIA, _ROMANIA, _BULGARIA, _HUNGARY, _CZECHOSLOVAKIA]:
        _add_influence(pub, Side.US, cid, 1)
    return pub, False, None


def _event_marshall_plan(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 23: Marshall Plan*. Place 1 US inf in up to 7 WE countries not USSR-controlled.
    Sets the NATO prerequisite flag for future plays.
    """
    pool = [cid for cid in _WESTERN_EUROPE if not _controls(Side.USSR, cid, pub)]
    chosen = _sample_up_to(pool, 7, rng)
    for cid in chosen:
        _add_influence(pub, Side.US, cid, 1)
    pub.marshall_plan_played = True
    return pub, False, None


def _event_suez_crisis(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 28: Suez Crisis*. Remove 2 US inf from each of 2 sampled countries
    from {France(7), UK(17), Israel(30)}.
    """
    pool = [_FRANCE, _UK, _ISRAEL]
    chosen = _sample_up_to(pool, 2, rng)
    for cid in chosen:
        _add_influence(pub, Side.US, cid, -2)
    return pub, False, None


def _event_east_european_unrest(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 29: East European Unrest. Place 1 US inf in 3 Eastern Bloc countries."""
    chosen = _sample_up_to(_EASTERN_BLOC, 3, rng)
    for cid in chosen:
        _add_influence(pub, Side.US, cid, 1)
    return pub, False, None


def _event_decolonization(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 30: Decolonization. Place 1 USSR inf in up to 4 Africa or SEA countries."""
    pool = _AFRICA | _SOUTHEAST_ASIA
    chosen = _sample_up_to(pool, 4, rng)
    for cid in chosen:
        _add_influence(pub, Side.USSR, cid, 1)
    return pub, False, None


def _event_portuguese_empire_crumbles(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 55: Portuguese Empire Crumbles*. 2 USSR inf in Angola and Mozambique."""
    _add_influence(pub, Side.USSR, _ANGOLA, 2)
    _add_influence(pub, Side.USSR, _MOZAMBIQUE, 2)
    return pub, False, None


def _event_south_african_unrest(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 56: South African Unrest. 2 USSR inf in South Africa;
    2 USSR inf in one sampled neighbor of South Africa.
    """
    _add_influence(pub, Side.USSR, _SOUTH_AFRICA, 2)
    neighbor = int(rng.choice(_SOUTH_AFRICA_NEIGHBORS))
    _add_influence(pub, Side.USSR, neighbor, 2)
    return pub, False, None


def _event_allende(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 57: Allende*. 2 USSR inf in Chile."""
    _add_influence(pub, Side.USSR, _CHILE, 2)
    return pub, False, None


def _event_camp_david_accords(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 66: Camp David Accords*. US gains 1 VP; 1 US inf in Israel, Egypt, Jordan."""
    _vp_delta(pub, Side.US, 1)
    _add_influence(pub, Side.US, _ISRAEL, 1)
    _add_influence(pub, Side.US, _EGYPT, 1)
    _add_influence(pub, Side.US, _JORDAN, 1)
    return pub, *_check_win(pub)


def _event_puppet_governments(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 67: Puppet Governments. Place 1 US inf in 3 countries where both sides
    have 0 influence (excludes superpowers 81, 82 and LibyaAfrica 64).
    """
    pool = [
        cid for cid in range(84)
        if cid not in {64, 81, 82}
        and pub.influence.get((Side.USSR, cid), 0) == 0
        and pub.influence.get((Side.US, cid), 0) == 0
    ]
    chosen = _sample_up_to(pool, 3, rng)
    for cid in chosen:
        _add_influence(pub, Side.US, cid, 1)
    return pub, False, None


def _event_john_paul_ii(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 69: John Paul II Elected Pope*. -2 USSR inf, +1 US inf in Poland."""
    _add_influence(pub, Side.USSR, _POLAND, -2)
    _add_influence(pub, Side.US, _POLAND, 1)
    pub.john_paul_ii_played = True
    return pub, False, None


def _event_oas_founded(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 71: OAS Founded*. Place 2 total US inf: sample 2 slots with replacement
    from CA | SA, place 1 US inf each.
    """
    pool = sorted(_CENTRAL_AMERICA | _SOUTH_AMERICA)
    chosen = [int(x) for x in rng.choice(pool, size=2, replace=True)]
    for cid in chosen:
        _add_influence(pub, Side.US, cid, 1)
    return pub, False, None


def _event_sadat_expels_soviets(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 73: Sadat Expels Soviets*. Remove all USSR inf from Egypt; add 1 US inf."""
    _remove_all(pub, Side.USSR, _EGYPT)
    _add_influence(pub, Side.US, _EGYPT, 1)
    return pub, False, None


def _event_voice_of_america(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 75: Voice of America. Remove 1 USSR inf from up to 4 non-Europe countries
    where USSR has >= 1 inf (excludes _ALL_EUROPE and LibyaAfrica 64).
    """
    pool = [
        cid for cid in range(84)
        if cid not in _ALL_EUROPE
        and cid not in {64, 81, 82}
        and pub.influence.get((Side.USSR, cid), 0) >= 1
    ]
    chosen = _sample_up_to(pool, 4, rng)
    for cid in chosen:
        _add_influence(pub, Side.USSR, cid, -1)
    return pub, False, None


def _event_liberation_theology(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 76: Liberation Theology. Place 1 USSR inf in up to 3 CA countries
    where USSR inf < 2.
    """
    pool = [
        cid for cid in _CENTRAL_AMERICA
        if pub.influence.get((Side.USSR, cid), 0) < 2
    ]
    chosen = _sample_up_to(pool, 3, rng)
    for cid in chosen:
        _add_influence(pub, Side.USSR, cid, 1)
    return pub, False, None


def _event_the_reformer(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 90: The Reformer*. Place 1 USSR inf in up to 4 European countries
    not US-controlled. DEFCON +1.
    """
    pool = [
        cid for cid in _ALL_EUROPE
        if not _controls(Side.US, cid, pub)
    ]
    chosen = _sample_up_to(pool, 4, rng)
    for cid in chosen:
        _add_influence(pub, Side.USSR, cid, 1)
    pub.defcon = min(5, pub.defcon + 1)
    return pub, False, None


def _event_marine_barracks_bombing(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 91: Marine Barracks Bombing*. Remove all US inf from Lebanon;
    remove 1 US inf from up to 2 other Middle East countries with US inf >= 1.
    """
    _remove_all(pub, Side.US, _LEBANON)
    pool = [
        cid for cid in _MIDDLE_EAST
        if cid != _LEBANON
        and pub.influence.get((Side.US, cid), 0) >= 1
    ]
    chosen = _sample_up_to(pool, 2, rng)
    for cid in chosen:
        _add_influence(pub, Side.US, cid, -1)
    return pub, False, None


def _event_ortega(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 94: Ortega Elected in Nicaragua*. Remove all US from Nicaragua;
    free 2-ops USSR coup in a sampled neighbor of Nicaragua.
    """
    _remove_all(pub, Side.US, _NICARAGUA)
    neighbors = [38, 41, 45]  # ElSalvador(38), Honduras(41), CostaRica(45)
    neighbor = int(rng.choice(neighbors))
    _free_coup(pub, Side.USSR, neighbor, 2, rng, defcon_immune=False)
    return pub, *_check_win(pub)


def _event_tear_down_this_wall(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 99: Tear Down This Wall*. Remove all USSR from East Germany;
    add 3 US inf to East Germany. Cancels Willy Brandt (restores NATO to West Germany).
    """
    _remove_all(pub, Side.USSR, _EAST_GERMANY)
    cur = pub.influence.get((Side.US, _EAST_GERMANY), 0)
    pub.influence[(Side.US, _EAST_GERMANY)] = cur + 3
    pub.willy_brandt_active = False   # NATO protection restored to West Germany
    return pub, False, None


def _event_solidarity(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 104: Solidarity*. Add 3 US inf in Poland.
    Fires only if john_paul_ii_played=True.
    """
    if not pub.john_paul_ii_played:
        return pub, False, None  # prerequisite not met - no effect
    cur = pub.influence.get((Side.US, _POLAND), 0)
    pub.influence[(Side.US, _POLAND)] = cur + 3
    return pub, False, None


def _event_awacs_sale(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 107: AWACS Sale to Saudis*. Add 2 US inf in Saudi Arabia.
    OPEC (64) no longer scores Saudi Arabia for the rest of the game (awacs_active flag).
    """
    _add_influence(pub, Side.US, _SAUDI_ARABIA, 2)
    pub.awacs_active = True
    return pub, False, None


# ---------------------------------------------------------------------------
# Category E handlers — coups / VP / DEFCON
# ---------------------------------------------------------------------------


def _event_duck_and_cover(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 4: Duck and Cover. US gains (5 - defcon) VP; DEFCON drops by 1."""
    from tsrl.engine.event_log import log_event
    pre_defcon = pub.defcon
    vp_gain = 5 - pre_defcon
    log_event(f"Duck and Cover: DEFCON {pre_defcon}→{max(1, pre_defcon-1)}, US gains {vp_gain} VP")
    pub.vp -= vp_gain
    pub.defcon = max(1, pub.defcon - 1)
    return pub, *_check_win(pub)


def _event_korean_war(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 11: Korean War*. Free 2-ops USSR coup in South Korea (war card: defcon_immune).
    Success: USSR gains 2 VP. Failure: US gains 1 VP.
    """
    from tsrl.engine.event_log import log_event
    log_event("Korean War: target is South Korea")
    net = _free_coup(pub, Side.USSR, _SOUTH_KOREA, 2, rng, defcon_immune=True)
    if net > 0:
        pub.vp += 2   # USSR gains 2 VP
    else:
        pub.vp -= 1   # US gains 1 VP on failure
    return pub, *_check_win(pub)


def _event_arab_israeli_war(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 13: Arab-Israeli War. Free 2-ops USSR coup in Israel (war card: defcon_immune).
    Failure: US gains 1 VP. No extra VP on success.
    """
    from tsrl.engine.event_log import log_event
    log_event("Arab-Israeli War: target is Israel")
    net = _free_coup(pub, Side.USSR, _ISRAEL, 2, rng, defcon_immune=True)
    if net <= 0:
        pub.vp -= 1   # US gains 1 VP on failure
    return pub, *_check_win(pub)


def _event_indo_pakistani_war(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 24: Indo-Pakistani War. Phasing player coups randomly in India or Pakistan.
    Success: phasing gains 2 VP. Failure: phasing loses 1 VP.
    """
    from tsrl.engine.event_log import log_event
    target = int(rng.choice([_INDIA, _PAKISTAN]))
    cname = _countries()[target].name if target in _countries() else f"#{target}"
    log_event(f"Indo-Pakistani War: target is {cname}")
    net = _free_coup(pub, side, target, 2, rng, defcon_immune=True)
    if net > 0:
        _vp_delta(pub, side, 2)
    else:
        _vp_delta(pub, side, -1)
    return pub, *_check_win(pub)


def _event_nuclear_test_ban(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 34: Nuclear Test Ban. Phasing player gains (defcon - 2) VP; DEFCON +2."""
    vp_gain = max(0, pub.defcon - 2)
    _vp_delta(pub, side, vp_gain)
    pub.defcon = min(5, pub.defcon + 2)
    return pub, *_check_win(pub)


def _event_brush_war(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 39: Brush War. USSR coups a random stability-1 or -2 country with 3 ops.
    On success, remove up to 2 more US influence from the target beyond what coup removed.
    """
    c = _countries()
    pool = [
        cid for cid in range(84)
        if cid not in {64, 81, 82}
        and cid in c
        and c[cid].stability <= 2
    ]
    if not pool:
        return pub, False, None
    target = int(rng.choice(sorted(pool)))
    from tsrl.engine.event_log import log_event
    cname = c[target].name if target in c else f"#{target}"
    log_event(f"Brush War: target is {cname}")
    net = _free_coup(pub, Side.USSR, target, 3, rng, defcon_immune=False)
    if net > 0:
        # Additional removal: up to 2 more US influence beyond what coup already removed
        remaining = pub.influence.get((Side.US, target), 0)
        extra = min(2, remaining)
        if extra > 0:
            _add_influence(pub, Side.US, target, -extra)
    return pub, *_check_win(pub)


def _event_arms_race(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 42: Arms Race. If phasing player has more MilOps than opponent:
    if own meets DEFCON requirement → 3 VP; else → 1 VP.
    """
    own = pub.milops[int(side)]
    opp_idx = 1 - int(side)
    opp_mo = pub.milops[opp_idx]
    req = pub.defcon
    if own > opp_mo:
        if own >= req:
            _vp_delta(pub, side, 3)
        else:
            _vp_delta(pub, side, 1)
    return pub, *_check_win(pub)


def _event_summit(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 48: Summit. Both sides roll d6; higher roll wins 2 VP.
    DEFCON changes randomly by ±1. USSR wins ties when USSR is phasing.
    """
    from tsrl.engine.dice import roll_d6
    ussr_roll = roll_d6(rng)
    us_roll = roll_d6(rng)
    if side == Side.USSR:
        winner_side = Side.USSR if ussr_roll >= us_roll else Side.US
    else:
        winner_side = Side.US if us_roll >= ussr_roll else Side.USSR
    defcon_change = int(rng.choice([-1, 1]))
    pub.defcon = max(1, min(5, pub.defcon + defcon_change))
    _vp_delta(pub, winner_side, 2)
    return pub, *_check_win(pub)


def _event_how_i_learned(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 49: How I Learned to Stop Worrying*. DEFCON set to random 1-5;
    phasing player MilOps set to 5.
    """
    pub.defcon = int(rng.integers(1, 6))
    pub.milops[int(side)] = 5
    return pub, *_check_win(pub)


def _event_we_will_bury_you(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 53: We Will Bury You*. DEFCON -1; USSR gains 3 VP."""
    pub.defcon = max(1, pub.defcon - 1)
    pub.vp += 3   # USSR gains 3 VP
    return pub, *_check_win(pub)


def _event_abm_treaty(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 60: ABM Treaty. DEFCON +1; phasing player gains 1 VP; phasing player
    may immediately place 2 Influence in any countries already containing their influence.
    """
    pub.defcon = min(5, pub.defcon + 1)
    _vp_delta(pub, side, 1)
    # Bonus: place 2 inf in countries where phasing player already has influence.
    # For self-play: random selection (with replacement).
    eligible = sorted(cid for (s, cid), inf in pub.influence.items() if s == side and inf > 0)
    for _ in range(2):
        if eligible:
            cid = int(rng.choice(eligible))
            _add_influence(pub, side, cid, 1)
    return pub, *_check_win(pub)


def _event_u2_incident(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 63: U2 Incident*. USSR gains 1 VP.
    Per rules, playing UN Intervention nullifies U2 Incident's VP (hand-check not enforced).
    """
    pub.vp += 1   # USSR gains 1 VP
    return pub, *_check_win(pub)


def _event_opec(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 64: OPEC. USSR gains 1 VP per OPEC country where USSR has presence.
    Cancelled by Iron Lady (86) or North Sea Oil (89).
    AWACS Sale (107) removes Saudi Arabia from the OPEC pool.
    """
    if pub.opec_cancelled:
        return pub, False, None
    opec_pool = _OPEC_COUNTRIES if not pub.awacs_active else (_OPEC_COUNTRIES - {_SAUDI_ARABIA})
    count = sum(1 for cid in opec_pool if pub.influence.get((Side.USSR, cid), 0) > 0)
    pub.vp += count
    return pub, *_check_win(pub)


def _event_lonely_hearts(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 65: "Lone Hearts Club Band" (The)*. DEFCON +1; US gains 1 VP."""
    pub.defcon = min(5, pub.defcon + 1)
    pub.vp -= 1   # US gains 1 VP
    return pub, *_check_win(pub)


def _event_alliance_for_progress(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 79: Alliance for Progress*. US gains 1 VP per US-controlled battleground
    in Central America or South America.
    """
    c = _countries()
    count = sum(
        1 for cid in (_CENTRAL_AMERICA | _SOUTH_AMERICA)
        if c.get(cid) and c[cid].is_battleground and _controls(Side.US, cid, pub)
    )
    pub.vp -= count   # US gains count VP
    return pub, *_check_win(pub)


def _event_che(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 83: Che. USSR makes two free 3-ops coups in stability-1/2 countries,
    each in a different region among CA, SA, Africa.
    """
    c = _countries()
    eligible_set = _CENTRAL_AMERICA | _SOUTH_AMERICA | _AFRICA

    def _region_of(cid: int) -> str:
        if cid in _CENTRAL_AMERICA:
            return 'ca'
        if cid in _SOUTH_AMERICA:
            return 'sa'
        return 'af'

    pool = [
        cid for cid in eligible_set
        if cid not in {64}
        and cid in c
        and c[cid].stability <= 2
    ]
    if not pool:
        return pub, False, None

    first = int(rng.choice(sorted(pool)))
    first_region = _region_of(first)
    _free_coup(pub, Side.USSR, first, 3, rng, defcon_immune=False)

    # Second coup: different region
    second_pool = [cid for cid in pool if _region_of(cid) != first_region]
    if second_pool:
        second = int(rng.choice(sorted(second_pool)))
        _free_coup(pub, Side.USSR, second, 3, rng, defcon_immune=False)

    return pub, *_check_win(pub)


def _event_iron_lady(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 86: The Iron Lady*. US gains 1 VP; remove all USSR inf from UK;
    cancel OPEC for the rest of the game.
    """
    pub.vp -= 1   # US gains 1 VP
    _remove_all(pub, Side.USSR, _UK)
    pub.opec_cancelled = True
    return pub, *_check_win(pub)


def _event_reagan_bombs_libya(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 87: Reagan Bombs Libya*. US gains 1 VP per USSR inf in Libya (ID 33)."""
    count = pub.influence.get((Side.USSR, _LIBYA), 0)
    pub.vp -= count   # US gains VP = USSR Libya influence
    return pub, *_check_win(pub)


def _event_soviets_kal007(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 92: Soviets Shoot Down KAL 007*. DEFCON -1; US gains 2 VP.
    If USSR holds China Card, it passes to US face-up.
    """
    pub.defcon = max(1, pub.defcon - 1)
    pub.vp -= 2   # US gains 2 VP
    if pub.china_held_by == Side.USSR:
        pub.china_held_by = Side.US
        pub.china_playable = True
    return pub, *_check_win(pub)


def _event_glasnost(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 93: Glasnost*. USSR gains 2 VP; DEFCON +1.
    If SALT Negotiations is in effect, USSR may take one extra AR.
    """
    pub.vp += 2   # USSR gains 2 VP
    pub.defcon = min(5, pub.defcon + 1)
    if pub.salt_active:
        pub.glasnost_extra_ar = True
    return pub, *_check_win(pub)


def _event_pershing_ii(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 102: Pershing II Deployed*. USSR gains 1 VP; remove 1 US inf from up to
    3 Western Europe countries that have US inf >= 1.
    """
    pub.vp += 1   # USSR gains 1 VP
    pool = [cid for cid in _WESTERN_EUROPE if pub.influence.get((Side.US, cid), 0) >= 1]
    chosen = _sample_up_to(pool, 3, rng)
    for cid in chosen:
        _add_influence(pub, Side.US, cid, -1)
    return pub, *_check_win(pub)


def _event_iran_iraq_war(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 105: Iran-Iraq War. Phasing player coups randomly in Iran or Iraq (2 ops).
    DEFCON drops if target is battleground (not defcon_immune).
    Success: phasing gains 2 VP. Failure: phasing loses 1 VP.
    """
    from tsrl.engine.event_log import log_event
    target = int(rng.choice([_IRAN, _IRAQ]))
    cname = _countries()[target].name if target in _countries() else f"#{target}"
    log_event(f"Iran-Iraq War: target is {cname}")
    net = _free_coup(pub, side, target, 2, rng, defcon_immune=False)
    if net > 0:
        _vp_delta(pub, side, 2)
    else:
        _vp_delta(pub, side, -1)
    return pub, *_check_win(pub)


def _event_yuri_and_samantha(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 106: Yuri and Samantha*. USSR gains 1 VP per US space attempt this turn."""
    us_attempts = pub.space_attempts[int(Side.US)]
    pub.vp += us_attempts   # USSR gains VP = US space attempts this turn
    return pub, *_check_win(pub)


# ---------------------------------------------------------------------------
# Category D handlers — persistent / ongoing effects
# ---------------------------------------------------------------------------


def _event_vietnam_revolts(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 9: Vietnam Revolts*. Place 2 USSR inf in Vietnam; USSR gets +1 ops this turn.

    Note: the +1 ops modifier is applied globally as a simplification of the
    SE-Asia-only rule. Turn-scoped; cleared at end of turn.
    """
    _add_influence(pub, Side.USSR, 80, 2)  # Vietnam = 80
    pub.vietnam_revolts_active = True
    pub.ops_modifier[int(Side.USSR)] += 1
    return pub, False, None


def _event_nato(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 21: NATO*. US-controlled WE countries blocked from USSR coups/realigns.

    Prerequisite: Marshall Plan (23), Truman Doctrine (19), or Warsaw Pact (16) must
    have been played first. Enforcement lives in legal_actions.py.
    """
    pub.nato_active = True
    return pub, False, None


def _event_containment(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 25: Containment*. All US cards are worth +1 ops for the remainder of this turn."""
    pub.ops_modifier[int(Side.US)] += 1
    return pub, False, None


def _event_red_scare_purge(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 31: Red Scare/Purge. All opponent's cards -1 ops this turn (min 1)."""
    opp = Side.US if side == Side.USSR else Side.USSR
    pub.ops_modifier[int(opp)] -= 1
    return pub, False, None


def _event_formosan_resolution(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 35: Formosan Resolution*. Taiwan treated as battleground for Asia scoring
    while US controls it. Cancelled if USSR plays China Card for its event.

    Taiwan (id=85) is in countries.csv; scoring.py counts Taiwan as a
    battleground when formosan_active=True.
    """
    pub.formosan_active = True
    return pub, False, None


def _event_norad(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 38: NORAD*. While active: if DEFCON=2 at end of USSR AR, US may add 1 inf.

    Trigger handled in game_loop._run_action_rounds after each USSR AR.
    """
    pub.norad_active = True
    return pub, False, None


def _event_cuban_missile_crisis(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 43: Cuban Missile Crisis*. DEFCON set to 2; locked there.
    Any BG coup by either player ends the game in nuclear war.

    DEFCON lock (cuban_missile_crisis_active) and BG-coup-game-over are
    enforced in legal_actions.py and step.py.
    Cancellation: USSR removes all inf from Cuba, or US removes all inf from
    Turkey or West Germany → clears the flag. Implemented in step.py _apply_influence.
    """
    pub.defcon = 2
    pub.cuban_missile_crisis_active = True
    return pub, *_check_win(pub)


def _event_nuclear_subs(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 44: Nuclear Subs*. US coups no longer trigger the DEFCON penalty.

    Enforcement is in step.py _apply_coup: checks pub.nuclear_subs_active.
    """
    pub.nuclear_subs_active = True
    return pub, False, None


def _event_salt_negotiations(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 46: SALT Negotiations*. DEFCON +1; discard visibility; phasing player may
    take one discard card to hand.

    The card-draw is handled by cat_c_events._h_salt_negotiations (needs hand access).
    This handler only applies DEFCON +1 and sets salt_active; cat_c takes over from here.
    """
    pub.defcon = min(5, pub.defcon + 1)
    pub.salt_active = True
    return pub, *_check_win(pub)


def _event_brezhnev_doctrine(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 54: Brezhnev Doctrine*. All USSR cards worth +1 ops for the remainder of this turn."""
    pub.ops_modifier[int(Side.USSR)] += 1
    return pub, False, None


def _event_flower_power(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 62: Flower Power*. USSR gains 2VP each time US plays a war card for its event.

    Interception is handled in step.py _apply_event (checks flower_power_active flag).
    Cancelled by An Evil Empire (card 100).
    """
    pub.flower_power_active = True
    return pub, False, None


def _event_shuttle_diplomacy(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 74: Shuttle Diplomacy. Next Asia or Middle East scoring card excludes
    the highest-stability battleground in that region for both sides.

    Enforced in scoring.py score_region(); flag cleared by apply_scoring_card()
    after one Asia or ME scoring fires (ScoringResult.clear_shuttle signal).
    """
    pub.shuttle_diplomacy_active = True
    return pub, False, None


def _event_north_sea_oil(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 89: North Sea Oil*. Cancels OPEC for the rest of the game.
    US also gets one extra AR this turn.
    """
    pub.opec_cancelled = True
    pub.north_sea_oil_extra_ar = True
    return pub, False, None


def _event_iran_contra_scandal(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 96: Iran-Contra Scandal*. All US cards worth -1 ops for the remainder of this turn."""
    pub.ops_modifier[int(Side.US)] -= 1
    return pub, False, None


def _event_chernobyl(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 97: Chernobyl*. US designates one region; USSR may not place inf there via ops this turn.

    For self-play: US picks a random region (excluding SOUTHEAST_ASIA, which has no standalone
    influence placement and is a sub-region of Asia for scoring purposes).
    Enforced in accessible_countries() when mode==INFLUENCE for USSR side.
    Cleared at end of turn in _end_of_turn().
    """
    # Regions eligible for Chernobyl designation (all primary map regions)
    _regions = [
        Region.EUROPE, Region.ASIA, Region.MIDDLE_EAST,
        Region.CENTRAL_AMERICA, Region.SOUTH_AMERICA, Region.AFRICA,
    ]
    pub.chernobyl_blocked_region = rng.choice(_regions)
    return pub, False, None


def _event_an_evil_empire(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 100: An Evil Empire*. USSR loses 1 VP; cancels Flower Power."""
    pub.vp -= 1   # USSR loses 1 VP (pub.vp moves toward US)
    pub.flower_power_cancelled = True
    pub.flower_power_active = False
    return pub, *_check_win(pub)


# ---------------------------------------------------------------------------
# Category B handlers — conditional / opponent-choice effects
# ---------------------------------------------------------------------------


def _event_de_gaulle_leads_france(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 17: De Gaulle Leads France*. Remove 2 US inf, add 1 USSR inf in France;
    France no longer protected by NATO.
    """
    _add_influence(pub, Side.US, _FRANCE, -2)
    _add_influence(pub, Side.USSR, _FRANCE, 1)
    pub.de_gaulle_active = True
    return pub, False, None


def _event_truman_doctrine(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 19: Truman Doctrine*. Remove ALL USSR inf from one uncontrolled European country.

    'Uncontrolled' = USSR does not control (USSR inf < opp inf + stability).
    For random self-play: sample one eligible country.
    Sets the NATO prerequisite flag for future plays.
    """
    pool = [
        cid for cid in _ALL_EUROPE
        if pub.influence.get((Side.USSR, cid), 0) > 0
        and not _controls(Side.USSR, cid, pub)
    ]
    if pool:
        target = int(rng.choice(sorted(pool)))
        _remove_all(pub, Side.USSR, target)
    pub.truman_doctrine_played = True
    return pub, False, None


def _event_us_japan_pact(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 27: US/Japan Mutual Defense Pact*. Japan cannot be USSR coup/realigned;
    US gains control of Japan.
    """
    pub.us_japan_pact_active = True
    _gain_control(pub, Side.US, 22)  # Japan = 22
    return pub, False, None


def _event_de_stalinization(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 33: De-Stalinization*. USSR may move up to 4 influence from any countries
    to any other non-US-controlled countries.

    For random self-play: move influence randomly from sources to eligible destinations.
    """
    sources = sorted(
        cid for cid in range(84)
        if cid not in {64, 81, 82}
        and pub.influence.get((Side.USSR, cid), 0) > 0
    )
    destinations = sorted(
        cid for cid in range(84)
        if cid not in {64, 81, 82}
        and not _controls(Side.US, cid, pub)
    )
    if not sources or not destinations:
        return pub, False, None

    total_to_move = min(4, sum(pub.influence.get((Side.USSR, s), 0) for s in sources))
    for _ in range(total_to_move):
        avail_sources = [s for s in sources if pub.influence.get((Side.USSR, s), 0) > 0]
        avail_dests = destinations
        if not avail_sources or not avail_dests:
            break
        src = int(rng.choice(avail_sources))
        dst = int(rng.choice(avail_dests))
        _add_influence(pub, Side.USSR, src, -1)
        _add_influence(pub, Side.USSR, dst, 1)
    return pub, False, None


def _event_special_relationship(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 37: Special Relationship*. If UK is US-controlled AND NATO is active:
    US gains 2 VP + 2 inf anywhere. Otherwise: 1 inf in any WE country.
    """
    if _controls(Side.US, _UK, pub) and pub.nato_active:
        pub.vp -= 2  # US gains 2 VP
        # Place 2 inf in random accessible countries (any)
        pool = sorted(
            cid for cid in range(84)
            if cid not in {64, 81, 82}
        )
        for _ in range(2):
            if pool:
                dst = int(rng.choice(pool))
                _add_influence(pub, Side.US, dst, 1)
    else:
        target = int(rng.choice(sorted(_WESTERN_EUROPE)))
        _add_influence(pub, Side.US, target, 1)
    return pub, *_check_win(pub)


def _event_willy_brandt(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 58: Willy Brandt*. USSR gains 1 VP; 1 USSR inf in West Germany;
    West Germany no longer NATO-protected.
    """
    pub.vp += 1   # USSR gains 1 VP
    _add_influence(pub, Side.USSR, _WEST_GERMANY, 1)
    pub.willy_brandt_active = True
    return pub, *_check_win(pub)


def _event_muslim_revolution(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 59: Muslim Revolution. Remove all US inf from 2 of:
    Sudan(72), Iran(28), Iraq(29), Egypt(26), Libya(33), Saudi Arabia(34), Syria(35), Jordan(31).
    """
    _MUSLIM_REV_POOL = [72, 28, 29, 26, 33, 34, 35, 31]
    eligible = [cid for cid in _MUSLIM_REV_POOL if pub.influence.get((Side.US, cid), 0) > 0]
    if len(eligible) < 2:
        eligible = _MUSLIM_REV_POOL
    chosen = [int(x) for x in rng.choice(sorted(eligible), size=min(2, len(eligible)), replace=False)]
    for cid in chosen:
        _remove_all(pub, Side.US, cid)
    return pub, False, None


def _event_cultural_revolution(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 61: Cultural Revolution*. If US holds China Card: US must give it to USSR face-up.
    Otherwise: USSR gains 1 VP.
    """
    if pub.china_held_by == Side.US:
        pub.china_held_by = Side.USSR
        pub.china_playable = False  # taken face-down per card text
    else:
        pub.vp += 1
    return pub, *_check_win(pub)


def _event_latin_american_death_squads(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 70: Latin American Death Squads. Phasing player's coups in C/S America +1 to die roll;
    opponent's coups in C/S America -1 to die roll this turn.

    pub.latam_coup_bonus = playing side. Enforced in _apply_coup() in step.py.
    Cleared at end of turn in _end_of_turn().
    """
    pub.latam_coup_bonus = side
    return pub, False, None


def _event_iranian_hostage_crisis(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 85: Iranian Hostage Crisis*. Remove all US inf from Iran; add 2 USSR inf to Iran.
    Sets iran_hostage_crisis_active so Terrorism (95) discards 2 US cards instead of 1.
    """
    _remove_all(pub, Side.US, _IRAN)
    _add_influence(pub, Side.USSR, _IRAN, 2)
    pub.iran_hostage_crisis_active = True
    return pub, False, None


def _event_latin_american_debt_crisis(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 98: Latin American Debt Crisis*. US must discard two cards totalling 4+ ops,
    or USSR gains 2 VP.

    Full implementation with US discard choice is in cat_c_events._h_latin_american_debt_crisis.
    This fallback fires only when called outside the game loop (e.g. direct apply_event_card
    calls in tests); it always takes the USSR-gains-2VP branch.
    """
    pub.vp += 2   # USSR gains 2 VP (fallback: assume US cannot pay)
    return pub, *_check_win(pub)


# ---------------------------------------------------------------------------
# Category F handlers — space race / VP / China Card / special
# ---------------------------------------------------------------------------

# VP awards for reaching each space level.  (first_to_reach_vp, second_to_reach_vp)
# Duplicated locally to avoid importing from step.py.
_SPACE_VP_F: dict[int, tuple[int, int]] = {
    1: (2, 0),
    2: (0, 0),
    3: (2, 0),
    4: (0, 0),
    5: (3, 1),
    6: (0, 0),
    7: (4, 2),
    8: (2, 0),
}


def _event_captured_nazi_scientist(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 18: Captured Nazi Scientist*.
    Phasing player advances ONE level on the Space Race track (automatic, no die roll).
    Awards VP per space race table.
    """
    current = pub.space[int(side)]
    if current < 8:
        new_level = current + 1
        pub.space[int(side)] = new_level
        opp = Side.US if side == Side.USSR else Side.USSR
        opp_level = pub.space[int(opp)]
        first_vp, second_vp = _SPACE_VP_F.get(new_level, (0, 0))
        vp = first_vp if opp_level < new_level else second_vp
        _vp_delta(pub, side, vp)
    return pub, *_check_win(pub)


def _event_olympic_games(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 20: Olympic Games. Non-phasing player (opponent) decides compete or boycott.
    Compete: both roll d6; higher roll wins 2 VP (reroll ties).
    Boycott: DEFCON -1; phasing player gains 4 free influence ops.
    Self-play: opponent boycotts with 50% probability.
    """
    opp = Side.US if side == Side.USSR else Side.USSR
    if rng.random() < 0.5:
        # Boycott: DEFCON drops; phasing player receives 4 free influence ops.
        pub.defcon = max(1, pub.defcon - 1)
        from tsrl.engine.adjacency import load_adjacency as _la
        from tsrl.engine.legal_actions import accessible_countries as _ac

        _adj = _la()
        _accessible = sorted(_ac(side, pub, _adj, mode=ActionMode.INFLUENCE))
        if _accessible:
            _choice = getattr(rng, "choice", None)
            for _ in range(4):
                if _choice is not None:
                    country = _choice(_accessible)
                else:
                    country = int(rng.integers(0, len(_accessible)))
                pub.influence[(side, country)] = pub.influence.get((side, country), 0) + 1
    else:
        # Compete: both roll d6, reroll ties.
        my_roll = int(rng.integers(1, 7))
        opp_roll = int(rng.integers(1, 7))
        while my_roll == opp_roll:
            my_roll = int(rng.integers(1, 7))
            opp_roll = int(rng.integers(1, 7))
        winner_side = side if my_roll > opp_roll else opp
        _vp_delta(pub, winner_side, 2)
    return pub, *_check_win(pub)


def _event_junta(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 50: Junta.
    Place 2 influence in any one Central or South American country.
    Then conduct a free coup (2 ops) in that or a different C/S American country.
    """
    pool = sorted(_CENTRAL_AMERICA | _SOUTH_AMERICA)
    if not pool:
        return pub, False, None
    # Place 2 influence in a randomly chosen C/S American country.
    place_target = int(rng.choice(pool))
    _add_influence(pub, side, place_target, 2)
    # Then: free coup (2 ops) in same or different C/S American country.
    action_target = int(rng.choice(pool))
    _free_coup(pub, side, action_target, 2, rng, defcon_immune=False)
    return pub, *_check_win(pub)


def _event_kitchen_debates(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 51: Kitchen Debates*.
    If US controls more battleground countries than USSR: US gains 1 VP per excess.
    """
    c = _countries()
    all_bg = [cid for cid, spec in c.items() if spec.is_battleground and cid not in {64, 81, 82}]
    us_bg = sum(1 for cid in all_bg if _controls(Side.US, cid, pub))
    ussr_bg = sum(1 for cid in all_bg if _controls(Side.USSR, cid, pub))
    excess = us_bg - ussr_bg
    if excess > 0:
        pub.vp -= excess   # US gains VP
    return pub, *_check_win(pub)


def _event_nixon_china(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 72: Nixon Plays the China Card*.
    If USSR holds China Card: US takes it face-down and gains 2 VP.
    If US already holds China Card face-down: it becomes face-up (playable). No VP.
    """
    if pub.china_held_by == Side.USSR:
        pub.vp -= 2              # US gains 2 VP only when taking from USSR
        pub.china_held_by = Side.US
        pub.china_playable = False   # taken face-down
    elif pub.china_held_by == Side.US:
        pub.china_playable = True    # already held: flip face-up, no VP
    return pub, *_check_win(pub)


def _event_ussuri(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 77: Ussuri River Skirmish*.
    If USSR holds China Card: US takes it face-up; USSR gains 4 influence to distribute anywhere.
    If US holds China Card: USSR takes it face-up; US gains 4 influence to distribute anywhere.
    """
    c = _countries()
    all_countries = sorted(cid for cid in c if cid not in {64, 81, 82})
    if pub.china_held_by == Side.USSR:
        pub.china_held_by = Side.US
        pub.china_playable = True
        # USSR gains 4 influence anywhere (random for self-play).
        for _ in range(4):
            target = int(rng.choice(all_countries))
            _add_influence(pub, Side.USSR, target, 1)
    else:  # US holds (or neutral — treat as US holds for default)
        pub.china_held_by = Side.USSR
        pub.china_playable = True
        # US gains 4 influence anywhere.
        for _ in range(4):
            target = int(rng.choice(all_countries))
            _add_influence(pub, Side.US, target, 1)
    return pub, *_check_win(pub)


def _event_one_small_step(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 81: One Small Step.
    If the phasing player is BEHIND on the Space Race (lower level than opponent):
    advance 2 levels automatically (no die roll); award VP per table for each level passed.
    """
    opp = Side.US if side == Side.USSR else Side.USSR
    my_level = pub.space[int(side)]
    opp_level = pub.space[int(opp)]
    if my_level >= opp_level:
        # Not behind: no effect.
        return pub, False, None
    for _ in range(2):
        if my_level >= 8:
            break
        my_level += 1
        pub.space[int(side)] = my_level
        first_vp, second_vp = _SPACE_VP_F.get(my_level, (0, 0))
        vp = first_vp if opp_level < my_level else second_vp
        _vp_delta(pub, side, vp)
    return pub, *_check_win(pub)


def _event_wargames(
    pub: PublicState, side: Side, rng: RNG
) -> tuple[PublicState, bool, Optional[Side]]:
    """Card 103: Wargames*. Only playable at DEFCON 2.
    Playing player gives opponent 6 VP, then game ends immediately.
    Winner is whoever is ahead after the VP transfer (or draw if tied).
    """
    if pub.defcon != 2:
        # Can't fire outside DEFCON 2; treat as no-op if somehow played.
        return pub, False, None
    opp = Side.US if side == Side.USSR else Side.USSR
    _vp_delta(pub, opp, 6)   # give opponent 6 VP
    # Game ends — check who's ahead now.
    if pub.vp > 0:
        return pub, True, Side.USSR
    elif pub.vp < 0:
        return pub, True, Side.US
    else:
        return pub, True, None  # draw


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

_REGISTRY: dict[int, EventHandler] = {
    # Category E (Phase 1)
    4:   _event_duck_and_cover,
    11:  _event_korean_war,
    13:  _event_arab_israeli_war,
    24:  _event_indo_pakistani_war,
    34:  _event_nuclear_test_ban,
    39:  _event_brush_war,
    42:  _event_arms_race,
    48:  _event_summit,
    49:  _event_how_i_learned,
    53:  _event_we_will_bury_you,
    60:  _event_abm_treaty,
    63:  _event_u2_incident,
    64:  _event_opec,
    65:  _event_lonely_hearts,
    79:  _event_alliance_for_progress,
    83:  _event_che,
    87:  _event_reagan_bombs_libya,
    92:  _event_soviets_kal007,
    93:  _event_glasnost,
    105: _event_iran_iraq_war,
    106: _event_yuri_and_samantha,
    # Category A (Phase 1)
    7:   _event_socialist_governments,
    8:   _event_fidel,
    12:  _event_romanian_abdication,
    14:  _event_comecon,
    15:  _event_nasser,
    16:  _event_warsaw_pact,
    22:  _event_independent_reds,
    23:  _event_marshall_plan,
    28:  _event_suez_crisis,
    29:  _event_east_european_unrest,
    30:  _event_decolonization,
    55:  _event_portuguese_empire_crumbles,
    56:  _event_south_african_unrest,
    57:  _event_allende,
    66:  _event_camp_david_accords,
    67:  _event_puppet_governments,
    69:  _event_john_paul_ii,
    71:  _event_oas_founded,
    73:  _event_sadat_expels_soviets,
    75:  _event_voice_of_america,
    76:  _event_liberation_theology,
    86:  _event_iron_lady,
    90:  _event_the_reformer,
    91:  _event_marine_barracks_bombing,
    94:  _event_ortega,
    99:  _event_tear_down_this_wall,
    102: _event_pershing_ii,
    104: _event_solidarity,
    107: _event_awacs_sale,
    # Category D (Phase 2) — persistent effects
    9:   _event_vietnam_revolts,
    21:  _event_nato,
    25:  _event_containment,
    31:  _event_red_scare_purge,
    35:  _event_formosan_resolution,
    38:  _event_norad,
    43:  _event_cuban_missile_crisis,
    44:  _event_nuclear_subs,
    46:  _event_salt_negotiations,
    54:  _event_brezhnev_doctrine,
    62:  _event_flower_power,
    74:  _event_shuttle_diplomacy,
    89:  _event_north_sea_oil,
    96:  _event_iran_contra_scandal,
    97:  _event_chernobyl,
    100: _event_an_evil_empire,
    # Category B (Phase 2) — conditional / opponent-choice
    17:  _event_de_gaulle_leads_france,
    19:  _event_truman_doctrine,
    27:  _event_us_japan_pact,
    33:  _event_de_stalinization,
    37:  _event_special_relationship,
    58:  _event_willy_brandt,
    59:  _event_muslim_revolution,
    61:  _event_cultural_revolution,
    70:  _event_latin_american_death_squads,
    85:  _event_iranian_hostage_crisis,
    98:  _event_latin_american_debt_crisis,
    # Category F — space race / VP / China Card / special
    18:  _event_captured_nazi_scientist,
    20:  _event_olympic_games,
    50:  _event_junta,
    51:  _event_kitchen_debates,
    72:  _event_nixon_china,
    77:  _event_ussuri,
    81:  _event_one_small_step,
    103: _event_wargames,
}


def apply_event_card(
    pub: PublicState,
    card_id: int,
    side: Side,
    rng: RNG,
) -> tuple[PublicState, bool, Optional[Side]]:
    """Dispatch to registered handler. pub is already a mutable copy.
    Unregistered cards are no-ops (return (pub, False, None)).
    """
    handler = _REGISTRY.get(card_id)
    if handler is None:
        return pub, False, None
    return handler(pub, side, rng)
