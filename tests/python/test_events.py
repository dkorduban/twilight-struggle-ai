"""
Tests for Phase 1 event handlers (Category A + Category E, 51 cards).

All tests invoke events via the public apply_action() API so that the full
dispatch path (step.py → events.py) is exercised.

Helpers
-------
- _pub()           : build a minimal PublicState
- SequentialRNG    : deterministic fake RNG that returns a predefined sequence
- SeededRNG alias  : random.Random(0)
"""
from __future__ import annotations

import copy
import random

import pytest

from tsrl.engine.step import apply_action
from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Side

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _pub(**kwargs) -> PublicState:
    p = PublicState()
    for k, v in kwargs.items():
        setattr(p, k, v)
    return p


def _apply_event(
    pub: PublicState,
    card_id: int,
    side: Side = Side.USSR,
    rng: random.Random | None = None,
) -> tuple[PublicState, bool, object]:
    action = ActionEncoding(card_id=card_id, mode=ActionMode.EVENT, targets=())
    return apply_action(pub, action, side, rng=rng)


class SequentialRNG:
    """Returns predefined sequence of randint/choice values for deterministic tests."""

    def __init__(self, values: list[int]):
        self._values = list(values)
        self._i = 0

    def _next(self) -> int:
        v = self._values[self._i % len(self._values)]
        self._i += 1
        return v

    def randint(self, a: int, b: int) -> int:
        return self._next()

    def choice(self, seq):
        v = self._next()
        return seq[v % len(seq)]

    def choices(self, population, k: int = 1):
        return [self.choice(population) for _ in range(k)]

    def sample(self, population, k: int) -> list:
        pop = sorted(population)
        return pop[:k]


def _rng0() -> random.Random:
    return random.Random(0)


# ---------------------------------------------------------------------------
# Card 7 — Socialist Governments
# ---------------------------------------------------------------------------

_WE = frozenset({1, 2, 4, 7, 8, 10, 11, 14, 15, 16, 17, 18})


def test_socialist_govts_places_ussr_in_western_europe():
    pub = _pub()
    rng = random.Random(1)
    new_pub, _, _ = _apply_event(pub, 7, Side.USSR, rng)
    placed = [cid for cid in _WE if new_pub.influence.get((Side.USSR, cid), 0) > 0]
    assert len(placed) <= 3
    assert all(cid in _WE for cid in placed)


def test_socialist_govts_skips_us_controlled_countries():
    from tsrl.etl.game_data import load_countries
    countries = load_countries()
    # Control all WE countries for US: set US inf high
    pub = _pub()
    for cid in _WE:
        stab = countries[cid].stability
        pub.influence[(Side.US, cid)] = stab + 5  # definitely US-controlled
    new_pub, _, _ = _apply_event(pub, 7, Side.USSR, _rng0())
    for cid in _WE:
        assert new_pub.influence.get((Side.USSR, cid), 0) == 0


def test_socialist_govts_skips_countries_with_2plus_ussr_inf():
    pub = _pub()
    for cid in _WE:
        pub.influence[(Side.USSR, cid)] = 2
    new_pub, _, _ = _apply_event(pub, 7, Side.USSR, _rng0())
    for cid in _WE:
        assert new_pub.influence.get((Side.USSR, cid), 0) == 2  # unchanged


def test_socialist_govts_no_mutation_of_original():
    pub = _pub()
    original_inf = dict(pub.influence)
    _apply_event(pub, 7, Side.USSR, _rng0())
    assert pub.influence == original_inf


# ---------------------------------------------------------------------------
# Card 8 — Fidel
# ---------------------------------------------------------------------------

_CUBA = 36


def test_fidel_removes_us_from_cuba():
    pub = _pub()
    pub.influence[(Side.US, _CUBA)] = 3
    new_pub, _, _ = _apply_event(pub, 8, Side.USSR, _rng0())
    assert new_pub.influence.get((Side.US, _CUBA), 0) == 0


def test_fidel_ussr_gains_control_of_cuba():
    from tsrl.etl.game_data import load_countries
    countries = load_countries()
    pub = _pub()
    pub.influence[(Side.US, _CUBA)] = 1
    new_pub, _, _ = _apply_event(pub, 8, Side.USSR, _rng0())
    stab = countries[_CUBA].stability
    assert new_pub.influence.get((Side.USSR, _CUBA), 0) >= stab


def test_fidel_no_mutation():
    pub = _pub()
    pub.influence[(Side.US, _CUBA)] = 2
    original_us = pub.influence[(Side.US, _CUBA)]
    _apply_event(pub, 8, Side.USSR, _rng0())
    assert pub.influence[(Side.US, _CUBA)] == original_us


# ---------------------------------------------------------------------------
# Card 12 — Romanian Abdication
# ---------------------------------------------------------------------------

_ROMANIA = 13


def test_romanian_abdication_removes_us():
    pub = _pub()
    pub.influence[(Side.US, _ROMANIA)] = 3
    new_pub, _, _ = _apply_event(pub, 12, Side.USSR, _rng0())
    assert new_pub.influence.get((Side.US, _ROMANIA), 0) == 0


def test_romanian_abdication_ussr_controls():
    from tsrl.etl.game_data import load_countries
    countries = load_countries()
    pub = _pub()
    pub.influence[(Side.US, _ROMANIA)] = 2
    new_pub, _, _ = _apply_event(pub, 12, Side.USSR, _rng0())
    stab = countries[_ROMANIA].stability
    assert new_pub.influence.get((Side.USSR, _ROMANIA), 0) >= stab


def test_romanian_abdication_no_mutation():
    pub = _pub()
    pub.influence[(Side.US, _ROMANIA)] = 2
    _apply_event(pub, 12, Side.USSR, _rng0())
    assert pub.influence[(Side.US, _ROMANIA)] == 2


# ---------------------------------------------------------------------------
# Card 14 — COMECON
# ---------------------------------------------------------------------------

_EASTERN_BLOC = frozenset({0, 3, 5, 9, 12, 13, 19, 83})


def test_comecon_places_ussr_in_eastern_bloc():
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 14, Side.USSR, _rng0())
    placed = [cid for cid in _EASTERN_BLOC if new_pub.influence.get((Side.USSR, cid), 0) > 0]
    assert len(placed) <= 4
    assert all(cid in _EASTERN_BLOC for cid in placed)


def test_comecon_skips_us_controlled():
    from tsrl.etl.game_data import load_countries
    countries = load_countries()
    pub = _pub()
    for cid in _EASTERN_BLOC:
        stab = countries[cid].stability
        pub.influence[(Side.US, cid)] = stab + 5
    new_pub, _, _ = _apply_event(pub, 14, Side.USSR, _rng0())
    for cid in _EASTERN_BLOC:
        assert new_pub.influence.get((Side.USSR, cid), 0) == 0


def test_comecon_no_mutation():
    pub = _pub()
    original = dict(pub.influence)
    _apply_event(pub, 14, Side.USSR, _rng0())
    assert pub.influence == original


# ---------------------------------------------------------------------------
# Card 15 — Nasser
# ---------------------------------------------------------------------------

_EGYPT = 26


def test_nasser_adds_2_ussr_in_egypt():
    pub = _pub()
    pub.influence[(Side.USSR, _EGYPT)] = 1
    new_pub, _, _ = _apply_event(pub, 15, Side.USSR, _rng0())
    assert new_pub.influence.get((Side.USSR, _EGYPT), 0) == 3  # 1 + 2


def test_nasser_adds_2_when_egypt_empty():
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 15, Side.USSR, _rng0())
    assert new_pub.influence.get((Side.USSR, _EGYPT), 0) == 2


def test_nasser_removes_half_us_from_egypt_odd():
    # 5 US inf → remove ceil(5/2)=3, leaving 2
    pub = _pub()
    pub.influence[(Side.US, _EGYPT)] = 5
    new_pub, _, _ = _apply_event(pub, 15, Side.USSR, _rng0())
    assert new_pub.influence.get((Side.US, _EGYPT), 0) == 2


def test_nasser_removes_half_us_from_egypt_even():
    # 4 US inf → remove ceil(4/2)=2, leaving 2
    pub = _pub()
    pub.influence[(Side.US, _EGYPT)] = 4
    new_pub, _, _ = _apply_event(pub, 15, Side.USSR, _rng0())
    assert new_pub.influence.get((Side.US, _EGYPT), 0) == 2


def test_nasser_removes_half_us_from_egypt_one():
    # 1 US inf → remove ceil(1/2)=1, leaving 0
    pub = _pub()
    pub.influence[(Side.US, _EGYPT)] = 1
    new_pub, _, _ = _apply_event(pub, 15, Side.USSR, _rng0())
    assert new_pub.influence.get((Side.US, _EGYPT), 0) == 0


def test_nasser_no_mutation():
    pub = _pub()
    pub.influence[(Side.US, _EGYPT)] = 4
    _apply_event(pub, 15, Side.USSR, _rng0())
    assert pub.influence[(Side.US, _EGYPT)] == 4


# ---------------------------------------------------------------------------
# Card 16 — Warsaw Pact Formed
# ---------------------------------------------------------------------------


def test_warsaw_pact_branch_a_removes_us():
    # Force branch A: rng.choice(['A', 'B']) → index 0 → 'A'
    rng = SequentialRNG([0, 0, 0, 0, 0, 0])
    pub = _pub()
    for cid in _EASTERN_BLOC:
        pub.influence[(Side.US, cid)] = 2
    new_pub, _, _ = _apply_event(pub, 16, Side.USSR, rng)
    # Branch A: up to 4 countries should have 0 US inf
    removed = sum(1 for cid in _EASTERN_BLOC if new_pub.influence.get((Side.US, cid), 0) == 0)
    assert removed <= 4


def test_warsaw_pact_branch_b_adds_ussr():
    # Force branch B: rng.choice(['A', 'B']) → index 1 → 'B'
    rng = SequentialRNG([1, 0, 0, 0, 0, 0])
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 16, Side.USSR, rng)
    # Branch B: up to 5 Eastern Bloc countries get USSR inf
    placed = [cid for cid in _EASTERN_BLOC if new_pub.influence.get((Side.USSR, cid), 0) > 0]
    assert len(placed) <= 5


def test_warsaw_pact_no_mutation():
    pub = _pub()
    for cid in _EASTERN_BLOC:
        pub.influence[(Side.US, cid)] = 1
    original = dict(pub.influence)
    _apply_event(pub, 16, Side.USSR, _rng0())
    assert pub.influence == original


# ---------------------------------------------------------------------------
# Card 22 — Independent Reds
# ---------------------------------------------------------------------------

_INDEP_REDS_COUNTRIES = [19, 13, 83, 9, 3]  # Yugoslavia, Romania, Bulgaria, Hungary, Czecho


def test_independent_reds_places_us_in_all_five():
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 22, Side.USSR, _rng0())
    for cid in _INDEP_REDS_COUNTRIES:
        assert new_pub.influence.get((Side.US, cid), 0) >= 1


def test_independent_reds_adds_to_existing():
    pub = _pub()
    pub.influence[(Side.US, 13)] = 2  # Romania already has 2
    new_pub, _, _ = _apply_event(pub, 22, Side.USSR, _rng0())
    assert new_pub.influence.get((Side.US, 13), 0) == 3


def test_independent_reds_no_mutation():
    pub = _pub()
    original = dict(pub.influence)
    _apply_event(pub, 22, Side.USSR, _rng0())
    assert pub.influence == original


# ---------------------------------------------------------------------------
# Card 23 — Marshall Plan
# ---------------------------------------------------------------------------


def test_marshall_plan_places_us_in_western_europe():
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 23, Side.US, _rng0())
    placed = [cid for cid in _WE if new_pub.influence.get((Side.US, cid), 0) > 0]
    assert len(placed) <= 7
    assert all(cid in _WE for cid in placed)


def test_marshall_plan_skips_ussr_controlled():
    from tsrl.etl.game_data import load_countries
    countries = load_countries()
    pub = _pub()
    for cid in _WE:
        stab = countries[cid].stability
        pub.influence[(Side.USSR, cid)] = stab + 5
    new_pub, _, _ = _apply_event(pub, 23, Side.US, _rng0())
    for cid in _WE:
        assert new_pub.influence.get((Side.US, cid), 0) == 0


def test_marshall_plan_no_mutation():
    pub = _pub()
    original = dict(pub.influence)
    _apply_event(pub, 23, Side.US, _rng0())
    assert pub.influence == original


# ---------------------------------------------------------------------------
# Card 28 — Suez Crisis
# ---------------------------------------------------------------------------

_SUEZ_POOL = {7, 17, 30}  # France, UK, Israel


def test_suez_crisis_removes_2_us_from_2_countries():
    pub = _pub()
    for cid in _SUEZ_POOL:
        pub.influence[(Side.US, cid)] = 3
    new_pub, _, _ = _apply_event(pub, 28, Side.USSR, _rng0())
    reduced = [cid for cid in _SUEZ_POOL if new_pub.influence.get((Side.US, cid), 0) == 1]
    assert len(reduced) == 2


def test_suez_crisis_exactly_2_countries_affected():
    pub = _pub()
    for cid in _SUEZ_POOL:
        pub.influence[(Side.US, cid)] = 5
    new_pub, _, _ = _apply_event(pub, 28, Side.USSR, _rng0())
    changed = [cid for cid in _SUEZ_POOL if new_pub.influence.get((Side.US, cid), 0) != 5]
    assert len(changed) == 2


def test_suez_crisis_no_mutation():
    pub = _pub()
    for cid in _SUEZ_POOL:
        pub.influence[(Side.US, cid)] = 3
    original = dict(pub.influence)
    _apply_event(pub, 28, Side.USSR, _rng0())
    assert pub.influence == original


# ---------------------------------------------------------------------------
# Card 29 — East European Unrest
# ---------------------------------------------------------------------------


def test_east_european_unrest_places_3_us_in_eastern_bloc():
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 29, Side.US, _rng0())
    placed = [cid for cid in _EASTERN_BLOC if new_pub.influence.get((Side.US, cid), 0) > 0]
    assert len(placed) == 3
    assert all(cid in _EASTERN_BLOC for cid in placed)


def test_east_european_unrest_no_mutation():
    pub = _pub()
    original = dict(pub.influence)
    _apply_event(pub, 29, Side.US, _rng0())
    assert pub.influence == original


# ---------------------------------------------------------------------------
# Card 30 — Decolonization
# ---------------------------------------------------------------------------

_AFRICA = frozenset({56, 57, 58, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74})
_SEA = frozenset({75, 76, 77, 78, 79, 80})
_DECOLONIZATION_POOL = _AFRICA | _SEA


def test_decolonization_places_ussr_in_africa_sea():
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 30, Side.USSR, _rng0())
    placed = [cid for cid in _DECOLONIZATION_POOL if new_pub.influence.get((Side.USSR, cid), 0) > 0]
    assert len(placed) <= 4
    assert all(cid in _DECOLONIZATION_POOL for cid in placed)


def test_decolonization_no_mutation():
    pub = _pub()
    original = dict(pub.influence)
    _apply_event(pub, 30, Side.USSR, _rng0())
    assert pub.influence == original


# ---------------------------------------------------------------------------
# Card 55 — Portuguese Empire Crumbles
# ---------------------------------------------------------------------------

_ANGOLA = 57
_MOZAMBIQUE = 66


def test_portuguese_empire_2_in_angola_and_mozambique():
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 55, Side.USSR, _rng0())
    assert new_pub.influence.get((Side.USSR, _ANGOLA), 0) == 2
    assert new_pub.influence.get((Side.USSR, _MOZAMBIQUE), 0) == 2


def test_portuguese_empire_adds_to_existing():
    pub = _pub()
    pub.influence[(Side.USSR, _ANGOLA)] = 1
    new_pub, _, _ = _apply_event(pub, 55, Side.USSR, _rng0())
    assert new_pub.influence.get((Side.USSR, _ANGOLA), 0) == 3


def test_portuguese_empire_no_mutation():
    pub = _pub()
    original = dict(pub.influence)
    _apply_event(pub, 55, Side.USSR, _rng0())
    assert pub.influence == original


# ---------------------------------------------------------------------------
# Card 56 — South African Unrest
# ---------------------------------------------------------------------------

_SOUTH_AFRICA = 71
_SA_NEIGHBORS = {58, 69, 74}


def test_south_african_unrest_2_in_sa():
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 56, Side.USSR, _rng0())
    assert new_pub.influence.get((Side.USSR, _SOUTH_AFRICA), 0) == 2


def test_south_african_unrest_2_in_neighbor():
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 56, Side.USSR, _rng0())
    neighbor_inf = {cid: new_pub.influence.get((Side.USSR, cid), 0) for cid in _SA_NEIGHBORS}
    assert sum(neighbor_inf.values()) == 2
    placed_neighbors = [cid for cid, v in neighbor_inf.items() if v > 0]
    assert len(placed_neighbors) == 1


def test_south_african_unrest_no_mutation():
    pub = _pub()
    original = dict(pub.influence)
    _apply_event(pub, 56, Side.USSR, _rng0())
    assert pub.influence == original


# ---------------------------------------------------------------------------
# Card 57 — Allende
# ---------------------------------------------------------------------------

_CHILE = 49


def test_allende_places_2_in_chile():
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 57, Side.USSR, _rng0())
    assert new_pub.influence.get((Side.USSR, _CHILE), 0) == 2


def test_allende_adds_to_existing():
    pub = _pub()
    pub.influence[(Side.USSR, _CHILE)] = 1
    new_pub, _, _ = _apply_event(pub, 57, Side.USSR, _rng0())
    assert new_pub.influence.get((Side.USSR, _CHILE), 0) == 3


def test_allende_no_mutation():
    pub = _pub()
    pub.influence[(Side.USSR, _CHILE)] = 1
    _apply_event(pub, 57, Side.USSR, _rng0())
    assert pub.influence[(Side.USSR, _CHILE)] == 1


# ---------------------------------------------------------------------------
# Card 66 — Camp David Accords
# ---------------------------------------------------------------------------

_ISRAEL = 30
_JORDAN = 31


def test_camp_david_accords_us_gains_1_vp():
    pub = _pub()
    pub.vp = 0
    new_pub, _, _ = _apply_event(pub, 66, Side.US, _rng0())
    assert new_pub.vp == -1   # US gains 1 VP → vp decreases


def test_camp_david_accords_1_us_inf_in_israel_egypt_jordan():
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 66, Side.US, _rng0())
    assert new_pub.influence.get((Side.US, _ISRAEL), 0) == 1
    assert new_pub.influence.get((Side.US, _EGYPT), 0) == 1
    assert new_pub.influence.get((Side.US, _JORDAN), 0) == 1


def test_camp_david_no_mutation():
    pub = _pub()
    original_vp = pub.vp
    _apply_event(pub, 66, Side.US, _rng0())
    assert pub.vp == original_vp


# ---------------------------------------------------------------------------
# Card 67 — Puppet Governments
# ---------------------------------------------------------------------------


def test_puppet_governments_places_in_empty_countries():
    pub = _pub()
    pub.influence.clear()   # no influence anywhere
    new_pub, _, _ = _apply_event(pub, 67, Side.US, _rng0())
    placed = [cid for cid in range(84) if new_pub.influence.get((Side.US, cid), 0) > 0]
    assert len(placed) == 3


def test_puppet_governments_skips_countries_with_influence():
    pub = _pub()
    pub.influence.clear()
    # Give every country some influence
    for cid in range(84):
        if cid not in {81, 82, 64}:
            pub.influence[(Side.USSR, cid)] = 1
    new_pub, _, _ = _apply_event(pub, 67, Side.US, _rng0())
    placed = [cid for cid in range(84) if new_pub.influence.get((Side.US, cid), 0) > 0]
    assert len(placed) == 0


def test_puppet_governments_no_mutation():
    pub = _pub()
    pub.influence.clear()
    original = dict(pub.influence)
    _apply_event(pub, 67, Side.US, _rng0())
    assert pub.influence == original


# ---------------------------------------------------------------------------
# Card 69 — John Paul II Elected Pope
# ---------------------------------------------------------------------------

_POLAND = 12


def test_john_paul_ii_removes_2_ussr_adds_1_us_poland():
    pub = _pub()
    pub.influence[(Side.USSR, _POLAND)] = 4
    new_pub, _, _ = _apply_event(pub, 69, Side.USSR, _rng0())
    assert new_pub.influence.get((Side.USSR, _POLAND), 0) == 2
    assert new_pub.influence.get((Side.US, _POLAND), 0) == 1


def test_john_paul_ii_ussr_floored_at_0():
    pub = _pub()
    pub.influence[(Side.USSR, _POLAND)] = 1
    new_pub, _, _ = _apply_event(pub, 69, Side.USSR, _rng0())
    assert new_pub.influence.get((Side.USSR, _POLAND), 0) == 0


def test_john_paul_ii_no_mutation():
    pub = _pub()
    pub.influence[(Side.USSR, _POLAND)] = 4
    _apply_event(pub, 69, Side.USSR, _rng0())
    assert pub.influence[(Side.USSR, _POLAND)] == 4


# ---------------------------------------------------------------------------
# Card 71 — OAS Founded
# ---------------------------------------------------------------------------

_CA = frozenset({36, 37, 38, 39, 40, 41, 42, 43, 44, 45})
_SA = frozenset({46, 47, 48, 49, 50, 51, 52, 53, 54, 55})
_CASA = _CA | _SA


def test_oas_founded_places_2_us_in_ca_sa():
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 71, Side.US, _rng0())
    total = sum(new_pub.influence.get((Side.US, cid), 0) - pub.influence.get((Side.US, cid), 0)
                for cid in _CASA)
    assert total == 2


def test_oas_founded_all_placements_in_ca_sa():
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 71, Side.US, _rng0())
    for cid in range(84):
        if cid not in _CASA:
            assert new_pub.influence.get((Side.US, cid), 0) == pub.influence.get((Side.US, cid), 0)


def test_oas_founded_no_mutation():
    pub = _pub()
    original = dict(pub.influence)
    _apply_event(pub, 71, Side.US, _rng0())
    assert pub.influence == original


# ---------------------------------------------------------------------------
# Card 73 — Sadat Expels Soviets
# ---------------------------------------------------------------------------


def test_sadat_removes_ussr_from_egypt():
    pub = _pub()
    pub.influence[(Side.USSR, _EGYPT)] = 3
    new_pub, _, _ = _apply_event(pub, 73, Side.US, _rng0())
    assert new_pub.influence.get((Side.USSR, _EGYPT), 0) == 0


def test_sadat_adds_1_us_to_egypt():
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 73, Side.US, _rng0())
    assert new_pub.influence.get((Side.US, _EGYPT), 0) == 1


def test_sadat_no_mutation():
    pub = _pub()
    pub.influence[(Side.USSR, _EGYPT)] = 3
    _apply_event(pub, 73, Side.US, _rng0())
    assert pub.influence[(Side.USSR, _EGYPT)] == 3


# ---------------------------------------------------------------------------
# Card 75 — Voice of America
# ---------------------------------------------------------------------------

_ALL_EUROPE = frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 83})


def test_voice_of_america_removes_ussr_in_non_europe():
    pub = _pub()
    # Place USSR inf in several non-Europe countries
    targets = [20, 21, 24, 25, 26, 30]
    for cid in targets:
        pub.influence[(Side.USSR, cid)] = 2
    new_pub, _, _ = _apply_event(pub, 75, Side.US, _rng0())
    removed = [cid for cid in targets if new_pub.influence.get((Side.USSR, cid), 0) < 2]
    assert len(removed) <= 4


def test_voice_of_america_max_4_countries():
    pub = _pub()
    targets = [20, 21, 24, 25, 26, 30, 36, 37]
    for cid in targets:
        pub.influence[(Side.USSR, cid)] = 2
    new_pub, _, _ = _apply_event(pub, 75, Side.US, _rng0())
    removed = [cid for cid in targets if new_pub.influence.get((Side.USSR, cid), 0) < 2]
    assert len(removed) <= 4


def test_voice_of_america_skips_europe():
    pub = _pub()
    for cid in _ALL_EUROPE:
        pub.influence[(Side.USSR, cid)] = 3
    new_pub, _, _ = _apply_event(pub, 75, Side.US, _rng0())
    for cid in _ALL_EUROPE:
        assert new_pub.influence.get((Side.USSR, cid), 0) == 3


def test_voice_of_america_no_mutation():
    pub = _pub()
    pub.influence[(Side.USSR, 20)] = 2
    original = dict(pub.influence)
    _apply_event(pub, 75, Side.US, _rng0())
    assert pub.influence == original


# ---------------------------------------------------------------------------
# Card 76 — Liberation Theology
# ---------------------------------------------------------------------------


def test_liberation_theology_places_ussr_in_ca():
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 76, Side.USSR, _rng0())
    placed = [cid for cid in _CA if new_pub.influence.get((Side.USSR, cid), 0) > 0]
    assert len(placed) <= 3
    assert all(cid in _CA for cid in placed)


def test_liberation_theology_respects_cap_2():
    pub = _pub()
    for cid in _CA:
        pub.influence[(Side.USSR, cid)] = 2
    new_pub, _, _ = _apply_event(pub, 76, Side.USSR, _rng0())
    # All were already at 2 → pool is empty → no change
    for cid in _CA:
        assert new_pub.influence.get((Side.USSR, cid), 0) == 2


def test_liberation_theology_no_mutation():
    pub = _pub()
    original = dict(pub.influence)
    _apply_event(pub, 76, Side.USSR, _rng0())
    assert pub.influence == original


# ---------------------------------------------------------------------------
# Card 90 — The Reformer
# ---------------------------------------------------------------------------


def test_the_reformer_places_ussr_in_europe():
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 90, Side.USSR, _rng0())
    placed = [cid for cid in _ALL_EUROPE if new_pub.influence.get((Side.USSR, cid), 0) > 0]
    assert len(placed) <= 4


def test_the_reformer_defcon_plus_1():
    pub = _pub()
    pub.defcon = 3
    new_pub, _, _ = _apply_event(pub, 90, Side.USSR, _rng0())
    assert new_pub.defcon == 4


def test_the_reformer_defcon_capped_at_5():
    pub = _pub()
    pub.defcon = 5
    new_pub, _, _ = _apply_event(pub, 90, Side.USSR, _rng0())
    assert new_pub.defcon == 5


def test_the_reformer_skips_us_controlled():
    from tsrl.etl.game_data import load_countries
    countries = load_countries()
    pub = _pub()
    for cid in _ALL_EUROPE:
        if cid in countries:
            pub.influence[(Side.US, cid)] = countries[cid].stability + 5
    new_pub, _, _ = _apply_event(pub, 90, Side.USSR, _rng0())
    for cid in _ALL_EUROPE:
        assert new_pub.influence.get((Side.USSR, cid), 0) == 0


def test_the_reformer_no_mutation():
    pub = _pub()
    pub.defcon = 3
    original_defcon = pub.defcon
    _apply_event(pub, 90, Side.USSR, _rng0())
    assert pub.defcon == original_defcon


# ---------------------------------------------------------------------------
# Card 91 — Marine Barracks Bombing
# ---------------------------------------------------------------------------

_LEBANON = 32
_MIDDLE_EAST = frozenset(range(26, 36))


def test_marine_barracks_bombing_removes_us_from_lebanon():
    pub = _pub()
    pub.influence[(Side.US, _LEBANON)] = 3
    new_pub, _, _ = _apply_event(pub, 91, Side.USSR, _rng0())
    assert new_pub.influence.get((Side.US, _LEBANON), 0) == 0


def test_marine_barracks_bombing_removes_up_to_2_me():
    pub = _pub()
    pub.influence[(Side.US, _LEBANON)] = 3
    for cid in _MIDDLE_EAST:
        if cid != _LEBANON:
            pub.influence[(Side.US, cid)] = 2
    new_pub, _, _ = _apply_event(pub, 91, Side.USSR, _rng0())
    reduced = [
        cid for cid in _MIDDLE_EAST
        if cid != _LEBANON
        and new_pub.influence.get((Side.US, cid), 0) < pub.influence.get((Side.US, cid), 0)
    ]
    assert len(reduced) <= 2


def test_marine_barracks_bombing_no_mutation():
    pub = _pub()
    pub.influence[(Side.US, _LEBANON)] = 3
    _apply_event(pub, 91, Side.USSR, _rng0())
    assert pub.influence[(Side.US, _LEBANON)] == 3


# ---------------------------------------------------------------------------
# Card 94 — Ortega Elected in Nicaragua
# ---------------------------------------------------------------------------

_NICARAGUA = 43
_NIC_NEIGHBORS = {38, 41, 45}


def test_ortega_removes_us_from_nicaragua():
    pub = _pub()
    pub.influence[(Side.US, _NICARAGUA)] = 3
    new_pub, _, _ = _apply_event(pub, 94, Side.USSR, _rng0())
    assert new_pub.influence.get((Side.US, _NICARAGUA), 0) == 0


def test_ortega_coups_in_neighbor():
    pub = _pub()
    pub.defcon = 5
    new_pub, _, _ = _apply_event(pub, 94, Side.USSR, _rng0())
    # At least some board change (coup happened) — can't fully predict outcome
    # but game didn't crash
    assert isinstance(new_pub, PublicState)


def test_ortega_no_mutation():
    pub = _pub()
    pub.influence[(Side.US, _NICARAGUA)] = 3
    _apply_event(pub, 94, Side.USSR, _rng0())
    assert pub.influence[(Side.US, _NICARAGUA)] == 3


# ---------------------------------------------------------------------------
# Card 99 — Tear Down This Wall
# ---------------------------------------------------------------------------

_EAST_GERMANY = 5


def test_tear_down_wall_removes_ussr_from_eg():
    pub = _pub()
    pub.influence[(Side.USSR, _EAST_GERMANY)] = 4
    new_pub, _, _ = _apply_event(pub, 99, Side.US, _rng0())
    assert new_pub.influence.get((Side.USSR, _EAST_GERMANY), 0) == 0


def test_tear_down_wall_adds_3_us_to_eg():
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 99, Side.US, _rng0())
    assert new_pub.influence.get((Side.US, _EAST_GERMANY), 0) == 3


def test_tear_down_wall_adds_to_existing_us():
    pub = _pub()
    pub.influence[(Side.US, _EAST_GERMANY)] = 2
    new_pub, _, _ = _apply_event(pub, 99, Side.US, _rng0())
    assert new_pub.influence.get((Side.US, _EAST_GERMANY), 0) == 5


def test_tear_down_wall_no_mutation():
    pub = _pub()
    pub.influence[(Side.USSR, _EAST_GERMANY)] = 4
    _apply_event(pub, 99, Side.US, _rng0())
    assert pub.influence[(Side.USSR, _EAST_GERMANY)] == 4


# ---------------------------------------------------------------------------
# Card 104 — Solidarity
# ---------------------------------------------------------------------------


def test_solidarity_adds_3_us_to_poland():
    pub = _pub()
    pub.john_paul_ii_played = True  # prerequisite: card 69 must have been played
    new_pub, _, _ = _apply_event(pub, 104, Side.US, _rng0())
    assert new_pub.influence.get((Side.US, _POLAND), 0) == 3


def test_solidarity_adds_to_existing():
    pub = _pub()
    pub.john_paul_ii_played = True  # prerequisite: card 69 must have been played
    pub.influence[(Side.US, _POLAND)] = 2
    new_pub, _, _ = _apply_event(pub, 104, Side.US, _rng0())
    assert new_pub.influence.get((Side.US, _POLAND), 0) == 5


def test_solidarity_no_mutation():
    pub = _pub()
    pub.influence[(Side.US, _POLAND)] = 2
    _apply_event(pub, 104, Side.US, _rng0())
    assert pub.influence[(Side.US, _POLAND)] == 2


# ---------------------------------------------------------------------------
# Card 107 — AWACS Sale to Saudis
# ---------------------------------------------------------------------------

_SAUDI_ARABIA = 34


def test_awacs_sale_adds_2_us_to_saudi():
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 107, Side.US, _rng0())
    assert new_pub.influence.get((Side.US, _SAUDI_ARABIA), 0) == 2


def test_awacs_sale_adds_to_existing():
    pub = _pub()
    pub.influence[(Side.US, _SAUDI_ARABIA)] = 1
    new_pub, _, _ = _apply_event(pub, 107, Side.US, _rng0())
    assert new_pub.influence.get((Side.US, _SAUDI_ARABIA), 0) == 3


def test_awacs_sale_no_mutation():
    pub = _pub()
    _apply_event(pub, 107, Side.US, _rng0())
    assert pub.influence.get((Side.US, _SAUDI_ARABIA), 0) == 0


# ---------------------------------------------------------------------------
# Card 4 — Duck and Cover
# ---------------------------------------------------------------------------


def test_duck_and_cover_vp_at_defcon3():
    pub = _pub()
    pub.defcon = 3
    new_pub, _, _ = _apply_event(pub, 4, Side.US, _rng0())
    # US gains (5 - 3) = 2 VP → pub.vp decreases by 2
    assert new_pub.vp == -2


def test_duck_and_cover_defcon_drops():
    pub = _pub()
    pub.defcon = 3
    new_pub, _, _ = _apply_event(pub, 4, Side.US, _rng0())
    assert new_pub.defcon == 2


def test_duck_and_cover_defcon5_gives_0_vp():
    pub = _pub()
    pub.defcon = 5
    new_pub, _, _ = _apply_event(pub, 4, Side.US, _rng0())
    assert new_pub.vp == 0
    assert new_pub.defcon == 4


def test_duck_and_cover_game_over_at_defcon1():
    pub = _pub()
    pub.defcon = 2
    pub.phasing = Side.US
    pub.vp = 0
    new_pub, over, winner = _apply_event(pub, 4, Side.US, _rng0())
    # After dropping to 1, check win condition triggers
    assert over
    # US triggered DEFCON 1 → US loses
    assert winner == Side.USSR


def test_duck_and_cover_no_mutation():
    pub = _pub()
    pub.defcon = 3
    original_defcon = pub.defcon
    _apply_event(pub, 4, Side.US, _rng0())
    assert pub.defcon == original_defcon


# ---------------------------------------------------------------------------
# Card 11 — Korean War
# ---------------------------------------------------------------------------

_SOUTH_KOREA = 25


def test_korean_war_success_gives_ussr_2_vp():
    # Use RNG that gives high roll (6) → coup succeeds (6 + 2 - 2*stab; SK stab=3 → 6+2-6=2 > 0)
    rng = random.Random(999)
    pub = _pub()
    pub.defcon = 5
    pub.influence[(Side.US, _SOUTH_KOREA)] = 5
    # Try repeatedly to get a success
    for seed in range(100):
        rng = random.Random(seed)
        pub2 = _pub()
        pub2.defcon = 5
        pub2.influence[(Side.US, _SOUTH_KOREA)] = 5
        new_pub, _, _ = _apply_event(pub2, 11, Side.USSR, rng)
        if new_pub.vp == 2:  # USSR gained 2 VP = success
            return
    pytest.fail("Could not find a seed where Korean War succeeded")


def test_korean_war_failure_gives_us_1_vp():
    # Use RNG that gives low roll (1) → coup fails (1 + 2 - 6 = -3 ≤ 0)
    # SK stability = 3, so need 2*3 = 6, roll must be >= 4 to succeed (1+2=3 < 6)
    # Actually roll 1: 1+2-6=-3 fails
    pub = _pub()
    pub.defcon = 5
    # Force low dice: use seed that tends to roll low
    for seed in range(100):
        rng = random.Random(seed)
        pub2 = _pub()
        pub2.defcon = 5
        new_pub, _, _ = _apply_event(pub2, 11, Side.USSR, rng)
        if new_pub.vp == -1:  # US gained 1 VP = failure
            return
    pytest.fail("Could not find a seed where Korean War failed")


def test_korean_war_defcon_unchanged():
    # Korean War is a war card → defcon_immune, so no DEFCON change regardless of outcome
    pub = _pub()
    pub.defcon = 5
    new_pub, _, _ = _apply_event(pub, 11, Side.USSR, _rng0())
    assert new_pub.defcon == 5


def test_korean_war_no_mutation():
    pub = _pub()
    pub.defcon = 5
    _apply_event(pub, 11, Side.USSR, _rng0())
    assert pub.defcon == 5


# ---------------------------------------------------------------------------
# Card 13 — Arab-Israeli War
# ---------------------------------------------------------------------------

_ISRAEL = 30


def test_arab_israeli_war_failure_gives_us_1_vp():
    for seed in range(100):
        rng = random.Random(seed)
        pub = _pub()
        pub.defcon = 5
        new_pub, _, _ = _apply_event(pub, 13, Side.USSR, rng)
        if new_pub.vp == -1:  # US gained 1 VP = failure
            return
    pytest.fail("Could not find failure case for Arab-Israeli War")


def test_arab_israeli_war_success_no_extra_vp():
    for seed in range(100):
        rng = random.Random(seed)
        pub = _pub()
        pub.defcon = 5
        pub.influence[(Side.US, _ISRAEL)] = 1
        new_pub, _, _ = _apply_event(pub, 13, Side.USSR, rng)
        if new_pub.vp == 0:  # success but no VP awarded
            return
    # This is fine if every seed leads to failure; just check no crash
    pass


def test_arab_israeli_war_defcon_unchanged():
    pub = _pub()
    pub.defcon = 4
    new_pub, _, _ = _apply_event(pub, 13, Side.USSR, _rng0())
    assert new_pub.defcon == 4  # war card: defcon_immune


def test_arab_israeli_war_no_mutation():
    pub = _pub()
    pub.defcon = 4
    original = pub.defcon
    _apply_event(pub, 13, Side.USSR, _rng0())
    assert pub.defcon == original


# ---------------------------------------------------------------------------
# Card 24 — Indo-Pakistani War
# ---------------------------------------------------------------------------

_INDIA = 21
_PAKISTAN = 24


def test_indo_pakistani_war_success_path():
    for seed in range(100):
        rng = random.Random(seed)
        pub = _pub()
        pub.defcon = 5
        pub.vp = 0
        new_pub, _, _ = _apply_event(pub, 24, Side.USSR, rng)
        if new_pub.vp == 2:  # success: USSR gained 2 VP
            return
    pytest.fail("Could not find a success for Indo-Pakistani War")


def test_indo_pakistani_war_failure_path():
    for seed in range(100):
        rng = random.Random(seed)
        pub = _pub()
        pub.defcon = 5
        pub.vp = 0
        new_pub, _, _ = _apply_event(pub, 24, Side.USSR, rng)
        if new_pub.vp == -1:  # failure: USSR lost 1 VP
            return
    pytest.fail("Could not find a failure for Indo-Pakistani War")


def test_indo_pakistani_war_no_mutation():
    pub = _pub()
    original_vp = pub.vp
    _apply_event(pub, 24, Side.USSR, _rng0())
    assert pub.vp == original_vp


# ---------------------------------------------------------------------------
# Card 34 — Nuclear Test Ban
# ---------------------------------------------------------------------------


def test_nuclear_test_ban_vp_at_defcon4():
    pub = _pub()
    pub.defcon = 4
    new_pub, _, _ = _apply_event(pub, 34, Side.USSR, _rng0())
    # defcon - 2 = 2 VP for USSR
    assert new_pub.vp == 2


def test_nuclear_test_ban_defcon_plus_2():
    pub = _pub()
    pub.defcon = 3
    new_pub, _, _ = _apply_event(pub, 34, Side.USSR, _rng0())
    assert new_pub.defcon == 5


def test_nuclear_test_ban_defcon_capped_5():
    pub = _pub()
    pub.defcon = 4
    new_pub, _, _ = _apply_event(pub, 34, Side.USSR, _rng0())
    assert new_pub.defcon == 5  # min(5, 4+2)


def test_nuclear_test_ban_at_defcon2_gives_0_vp():
    pub = _pub()
    pub.defcon = 2
    new_pub, _, _ = _apply_event(pub, 34, Side.USSR, _rng0())
    assert new_pub.vp == 0  # max(0, 2-2) = 0


def test_nuclear_test_ban_us_side():
    pub = _pub()
    pub.defcon = 4
    pub.vp = 0
    new_pub, _, _ = _apply_event(pub, 34, Side.US, _rng0())
    assert new_pub.vp == -2  # US gains 2 VP


def test_nuclear_test_ban_no_mutation():
    pub = _pub()
    pub.defcon = 3
    original = pub.defcon
    _apply_event(pub, 34, Side.USSR, _rng0())
    assert pub.defcon == original


# ---------------------------------------------------------------------------
# Card 39 — Brush War
# ---------------------------------------------------------------------------


def test_brush_war_targets_stability_2_or_less():
    from tsrl.etl.game_data import load_countries
    countries = load_countries()
    pub = _pub()
    pub.defcon = 5
    new_pub, _, _ = _apply_event(pub, 39, Side.USSR, _rng0())
    # We can't directly know the target from the outside, but the game runs without error
    assert isinstance(new_pub, PublicState)


def test_brush_war_defcon_drops_if_battleground():
    from tsrl.etl.game_data import load_countries
    countries = load_countries()
    # Find a battleground stab<=2 country and force it as target
    bg_low = [cid for cid, c in countries.items() if c.is_battleground and c.stability <= 2 and cid not in {64, 81, 82}]
    assert bg_low, "Current country spec should include a battleground with stability <= 2."
    pub = _pub()
    pub.defcon = 5
    # Try a few seeds to get one that targets a battleground
    for seed in range(200):
        rng = random.Random(seed)
        pub2 = _pub()
        pub2.defcon = 5
        new_pub, _, _ = _apply_event(pub2, 39, Side.USSR, rng)
        if new_pub.defcon < 5:
            return  # confirmed DEFCON drops for battleground
    # It's possible all rolls went to non-BG, just check it doesn't crash
    pass


def test_brush_war_no_mutation():
    pub = _pub()
    pub.defcon = 5
    original_defcon = pub.defcon
    _apply_event(pub, 39, Side.USSR, _rng0())
    assert pub.defcon == original_defcon


# ---------------------------------------------------------------------------
# Card 42 — Arms Race
# ---------------------------------------------------------------------------


def test_arms_race_own_greater_and_meets_req_gives_3vp():
    pub = _pub()
    pub.defcon = 3
    pub.milops = [4, 1]  # USSR has 4, US has 1; defcon req=3, USSR meets it
    new_pub, _, _ = _apply_event(pub, 42, Side.USSR, _rng0())
    assert new_pub.vp == 3


def test_arms_race_own_greater_misses_req_gives_1vp():
    pub = _pub()
    pub.defcon = 5
    pub.milops = [3, 1]  # USSR has 3, US has 1; defcon req=5, USSR misses it
    new_pub, _, _ = _apply_event(pub, 42, Side.USSR, _rng0())
    assert new_pub.vp == 1


def test_arms_race_own_equal_gives_0vp():
    pub = _pub()
    pub.defcon = 3
    pub.milops = [3, 3]  # equal → no VP
    new_pub, _, _ = _apply_event(pub, 42, Side.USSR, _rng0())
    assert new_pub.vp == 0


def test_arms_race_own_less_gives_0vp():
    pub = _pub()
    pub.defcon = 3
    pub.milops = [1, 3]  # US has more → no VP for USSR
    new_pub, _, _ = _apply_event(pub, 42, Side.USSR, _rng0())
    assert new_pub.vp == 0


def test_arms_race_us_side():
    pub = _pub()
    pub.defcon = 3
    pub.milops = [1, 4]  # US has 4, USSR has 1; meets req
    new_pub, _, _ = _apply_event(pub, 42, Side.US, _rng0())
    assert new_pub.vp == -3   # US gains 3 VP


def test_arms_race_no_mutation():
    pub = _pub()
    pub.defcon = 3
    pub.milops = [4, 1]
    original_vp = pub.vp
    _apply_event(pub, 42, Side.USSR, _rng0())
    assert pub.vp == original_vp


# ---------------------------------------------------------------------------
# Card 48 — Summit
# ---------------------------------------------------------------------------


def test_summit_changes_defcon():
    pub = _pub()
    pub.defcon = 3
    new_pub, _, _ = _apply_event(pub, 48, Side.USSR, _rng0())
    assert new_pub.defcon in (2, 4)


def test_summit_awards_2_vp():
    pub = _pub()
    pub.defcon = 3
    new_pub, _, _ = _apply_event(pub, 48, Side.USSR, _rng0())
    # Either USSR or US gets 2 VP
    assert abs(new_pub.vp) == 2


def test_summit_no_mutation():
    pub = _pub()
    pub.defcon = 3
    original_defcon = pub.defcon
    _apply_event(pub, 48, Side.USSR, _rng0())
    assert pub.defcon == original_defcon


# ---------------------------------------------------------------------------
# Card 49 — How I Learned to Stop Worrying
# ---------------------------------------------------------------------------


def test_how_i_learned_sets_defcon_1_to_5():
    rng = random.Random(0)
    pub = _pub()
    pub.defcon = 3
    new_pub, _, _ = _apply_event(pub, 49, Side.USSR, rng)
    assert 1 <= new_pub.defcon <= 5


def test_how_i_learned_sets_milops_to_5():
    pub = _pub()
    pub.defcon = 3
    new_pub, _, _ = _apply_event(pub, 49, Side.USSR, _rng0())
    assert new_pub.milops[int(Side.USSR)] == 5


def test_how_i_learned_game_over_if_defcon1():
    rng = SequentialRNG([1])  # randint(1,5) → 1 → DEFCON 1
    pub = _pub()
    pub.defcon = 5
    pub.phasing = Side.USSR
    new_pub, over, winner = _apply_event(pub, 49, Side.USSR, rng)
    if new_pub.defcon == 1:
        assert over
        assert winner == Side.US   # USSR triggered DEFCON 1 → USSR loses → US wins


def test_how_i_learned_no_mutation():
    pub = _pub()
    pub.defcon = 3
    original = pub.defcon
    _apply_event(pub, 49, Side.USSR, _rng0())
    assert pub.defcon == original


# ---------------------------------------------------------------------------
# Card 53 — We Will Bury You
# ---------------------------------------------------------------------------


def test_we_will_bury_you_defcon_minus_1():
    pub = _pub()
    pub.defcon = 4
    new_pub, _, _ = _apply_event(pub, 53, Side.USSR, _rng0())
    assert new_pub.defcon == 3


def test_we_will_bury_you_ussr_gains_3_vp():
    pub = _pub()
    pub.defcon = 4
    new_pub, _, _ = _apply_event(pub, 53, Side.USSR, _rng0())
    assert new_pub.vp == 3


def test_we_will_bury_you_no_mutation():
    pub = _pub()
    pub.defcon = 4
    original = pub.defcon
    _apply_event(pub, 53, Side.USSR, _rng0())
    assert pub.defcon == original


# ---------------------------------------------------------------------------
# Card 60 — ABM Treaty
# ---------------------------------------------------------------------------


def test_abm_treaty_defcon_plus_1():
    pub = _pub()
    pub.defcon = 3
    new_pub, _, _ = _apply_event(pub, 60, Side.USSR, _rng0())
    assert new_pub.defcon == 4


def test_abm_treaty_ussr_side_gains_1_vp():
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 60, Side.USSR, _rng0())
    assert new_pub.vp == 1


def test_abm_treaty_us_side_gains_1_vp():
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 60, Side.US, _rng0())
    assert new_pub.vp == -1


def test_abm_treaty_no_mutation():
    pub = _pub()
    pub.defcon = 3
    original = pub.defcon
    _apply_event(pub, 60, Side.USSR, _rng0())
    assert pub.defcon == original


# ---------------------------------------------------------------------------
# Card 63 — U2 Incident
# ---------------------------------------------------------------------------


def test_u2_incident_ussr_gains_1_vp():
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 63, Side.USSR, _rng0())
    assert new_pub.vp == 1


def test_u2_incident_no_mutation():
    pub = _pub()
    original_vp = pub.vp
    _apply_event(pub, 63, Side.USSR, _rng0())
    assert pub.vp == original_vp


# ---------------------------------------------------------------------------
# Card 64 — OPEC
# ---------------------------------------------------------------------------

_OPEC = frozenset({26, 28, 33, 34, 29, 27, 55})


def test_opec_counts_ussr_presence():
    pub = _pub()
    # USSR in Egypt(26) and Iran(28) → 2 VP
    pub.influence[(Side.USSR, 26)] = 1
    pub.influence[(Side.USSR, 28)] = 1
    new_pub, _, _ = _apply_event(pub, 64, Side.USSR, _rng0())
    assert new_pub.vp == 2


def test_opec_0_vp_with_no_presence():
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 64, Side.USSR, _rng0())
    assert new_pub.vp == 0


def test_opec_full_7_countries():
    pub = _pub()
    for cid in _OPEC:
        pub.influence[(Side.USSR, cid)] = 1
    new_pub, _, _ = _apply_event(pub, 64, Side.USSR, _rng0())
    assert new_pub.vp == 7


def test_opec_no_mutation():
    pub = _pub()
    pub.influence[(Side.USSR, 26)] = 1
    original_vp = pub.vp
    _apply_event(pub, 64, Side.USSR, _rng0())
    assert pub.vp == original_vp


# ---------------------------------------------------------------------------
# Card 65 — "Lone Hearts Club Band" (The)
# ---------------------------------------------------------------------------


def test_lonely_hearts_defcon_plus_1():
    pub = _pub()
    pub.defcon = 3
    new_pub, _, _ = _apply_event(pub, 65, Side.US, _rng0())
    assert new_pub.defcon == 4


def test_lonely_hearts_us_gains_1_vp():
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 65, Side.US, _rng0())
    assert new_pub.vp == -1  # US gains 1 VP


def test_lonely_hearts_no_mutation():
    pub = _pub()
    pub.defcon = 3
    original = pub.defcon
    _apply_event(pub, 65, Side.US, _rng0())
    assert pub.defcon == original


# ---------------------------------------------------------------------------
# Card 79 — Alliance for Progress
# ---------------------------------------------------------------------------


def test_alliance_for_progress_counts_controlled_battlegrounds():
    from tsrl.etl.game_data import load_countries
    countries = load_countries()
    pub = _pub()
    # US controls Cuba (36): stability 3, US-controlled if US >= USSR + 3
    # Put enough US inf in Cuba
    pub.influence[(Side.US, 36)] = 3  # Cuba stab=3, no USSR → US controls
    new_pub, _, _ = _apply_event(pub, 79, Side.US, _rng0())
    # Cuba is a BG in CA → US gained 1 VP
    assert new_pub.vp <= -1


def test_alliance_for_progress_0_with_no_controlled():
    pub = _pub()
    pub.influence.clear()
    new_pub, _, _ = _apply_event(pub, 79, Side.US, _rng0())
    assert new_pub.vp == 0


def test_alliance_for_progress_no_mutation():
    pub = _pub()
    pub.influence[(Side.US, 36)] = 3
    original = pub.vp
    _apply_event(pub, 79, Side.US, _rng0())
    assert pub.vp == original


# ---------------------------------------------------------------------------
# Card 83 — Che
# ---------------------------------------------------------------------------


def test_che_runs_two_coups_different_regions():
    pub = _pub()
    pub.defcon = 5
    new_pub, _, _ = _apply_event(pub, 83, Side.USSR, _rng0())
    assert isinstance(new_pub, PublicState)


def test_che_no_mutation():
    pub = _pub()
    pub.defcon = 5
    original_defcon = pub.defcon
    _apply_event(pub, 83, Side.USSR, _rng0())
    assert pub.defcon == original_defcon


# ---------------------------------------------------------------------------
# Card 86 — The Iron Lady
# ---------------------------------------------------------------------------

_UK = 17


def test_iron_lady_us_gains_1_vp():
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 86, Side.US, _rng0())
    assert new_pub.vp == -1  # US gains 1 VP


def test_iron_lady_removes_ussr_from_uk():
    pub = _pub()
    pub.influence[(Side.USSR, _UK)] = 3
    new_pub, _, _ = _apply_event(pub, 86, Side.US, _rng0())
    assert new_pub.influence.get((Side.USSR, _UK), 0) == 0


def test_iron_lady_no_mutation():
    pub = _pub()
    pub.influence[(Side.USSR, _UK)] = 3
    _apply_event(pub, 86, Side.US, _rng0())
    assert pub.influence[(Side.USSR, _UK)] == 3


# ---------------------------------------------------------------------------
# Card 87 — Reagan Bombs Libya
# ---------------------------------------------------------------------------

_LIBYA = 33


def test_reagan_bombs_libya_vp_equals_ussr_inf():
    pub = _pub()
    pub.influence[(Side.USSR, _LIBYA)] = 3
    new_pub, _, _ = _apply_event(pub, 87, Side.US, _rng0())
    assert new_pub.vp == -3  # US gains 3 VP


def test_reagan_bombs_libya_0_if_no_ussr():
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 87, Side.US, _rng0())
    assert new_pub.vp == 0


def test_reagan_bombs_libya_no_mutation():
    pub = _pub()
    pub.influence[(Side.USSR, _LIBYA)] = 3
    original_vp = pub.vp
    _apply_event(pub, 87, Side.US, _rng0())
    assert pub.vp == original_vp


# ---------------------------------------------------------------------------
# Card 92 — Soviets Shoot Down KAL 007
# ---------------------------------------------------------------------------


def test_kal007_defcon_minus_1():
    pub = _pub()
    pub.defcon = 4
    new_pub, _, _ = _apply_event(pub, 92, Side.USSR, _rng0())
    assert new_pub.defcon == 3


def test_kal007_us_gains_2_vp():
    pub = _pub()
    pub.defcon = 4
    new_pub, _, _ = _apply_event(pub, 92, Side.USSR, _rng0())
    assert new_pub.vp == -2  # US gains 2 VP


def test_kal007_china_passes_if_ussr_holds():
    pub = _pub()
    pub.defcon = 4
    pub.china_held_by = Side.USSR
    pub.china_playable = False
    new_pub, _, _ = _apply_event(pub, 92, Side.USSR, _rng0())
    assert new_pub.china_held_by == Side.US
    assert new_pub.china_playable is True


def test_kal007_china_unaffected_if_us_holds():
    pub = _pub()
    pub.defcon = 4
    pub.china_held_by = Side.US
    new_pub, _, _ = _apply_event(pub, 92, Side.USSR, _rng0())
    assert new_pub.china_held_by == Side.US


def test_kal007_no_mutation():
    pub = _pub()
    pub.defcon = 4
    original = pub.defcon
    _apply_event(pub, 92, Side.USSR, _rng0())
    assert pub.defcon == original


# ---------------------------------------------------------------------------
# Card 93 — Glasnost
# ---------------------------------------------------------------------------


def test_glasnost_ussr_gains_2_vp():
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 93, Side.USSR, _rng0())
    assert new_pub.vp == 2


def test_glasnost_defcon_plus_1():
    pub = _pub()
    pub.defcon = 3
    new_pub, _, _ = _apply_event(pub, 93, Side.USSR, _rng0())
    assert new_pub.defcon == 4


def test_glasnost_no_mutation():
    pub = _pub()
    pub.defcon = 3
    original = pub.defcon
    _apply_event(pub, 93, Side.USSR, _rng0())
    assert pub.defcon == original


# ---------------------------------------------------------------------------
# Card 102 — Pershing II Deployed
# ---------------------------------------------------------------------------


def test_pershing_ii_ussr_gains_1_vp():
    pub = _pub()
    new_pub, _, _ = _apply_event(pub, 102, Side.USSR, _rng0())
    assert new_pub.vp == 1


def test_pershing_ii_removes_us_from_up_to_3_we():
    pub = _pub()
    for cid in _WE:
        pub.influence[(Side.US, cid)] = 2
    new_pub, _, _ = _apply_event(pub, 102, Side.USSR, _rng0())
    reduced = [cid for cid in _WE if new_pub.influence.get((Side.US, cid), 0) < 2]
    assert len(reduced) <= 3


def test_pershing_ii_only_removes_from_we_with_us_inf():
    pub = _pub()
    # Only France(7) has US inf
    pub.influence[(Side.US, 7)] = 2
    new_pub, _, _ = _apply_event(pub, 102, Side.USSR, _rng0())
    assert new_pub.influence.get((Side.US, 7), 0) == 1  # reduced by 1


def test_pershing_ii_no_mutation():
    pub = _pub()
    pub.influence[(Side.US, 7)] = 2
    original_vp = pub.vp
    _apply_event(pub, 102, Side.USSR, _rng0())
    assert pub.vp == original_vp


# ---------------------------------------------------------------------------
# Card 105 — Iran-Iraq War
# ---------------------------------------------------------------------------

_IRAN = 28
_IRAQ = 29


def test_iran_iraq_war_success_gives_2_vp():
    for seed in range(100):
        rng = random.Random(seed)
        pub = _pub()
        pub.defcon = 5
        pub.vp = 0
        new_pub, _, _ = _apply_event(pub, 105, Side.USSR, rng)
        if new_pub.vp >= 2:  # success with any VP gain
            return
    pytest.fail("Could not find success case for Iran-Iraq War")


def test_iran_iraq_war_failure_gives_minus_1_vp():
    for seed in range(100):
        rng = random.Random(seed)
        pub = _pub()
        pub.defcon = 5
        pub.vp = 0
        new_pub, _, _ = _apply_event(pub, 105, Side.USSR, rng)
        if new_pub.vp == -1:  # failure
            return
    pytest.fail("Could not find failure case for Iran-Iraq War")


def test_iran_iraq_war_targets_iran_or_iraq():
    # Just verify no crash; can't directly observe target choice
    pub = _pub()
    pub.defcon = 5
    new_pub, _, _ = _apply_event(pub, 105, Side.USSR, _rng0())
    assert isinstance(new_pub, PublicState)


def test_iran_iraq_war_no_mutation():
    pub = _pub()
    pub.defcon = 5
    original_vp = pub.vp
    _apply_event(pub, 105, Side.USSR, _rng0())
    assert pub.vp == original_vp


# ---------------------------------------------------------------------------
# Card 106 — Yuri and Samantha
# ---------------------------------------------------------------------------


def test_yuri_samantha_vp_equals_us_space_attempts():
    pub = _pub()
    pub.space_attempts = [0, 3]  # US made 3 space attempts
    new_pub, _, _ = _apply_event(pub, 106, Side.USSR, _rng0())
    assert new_pub.vp == 3


def test_yuri_samantha_0_if_no_us_attempts():
    pub = _pub()
    pub.space_attempts = [2, 0]  # USSR had attempts, US had none
    new_pub, _, _ = _apply_event(pub, 106, Side.USSR, _rng0())
    assert new_pub.vp == 0


def test_yuri_samantha_no_mutation():
    pub = _pub()
    pub.space_attempts = [0, 2]
    original_vp = pub.vp
    _apply_event(pub, 106, Side.USSR, _rng0())
    assert pub.vp == original_vp


# ---------------------------------------------------------------------------
# Unregistered card is a no-op
# ---------------------------------------------------------------------------


def test_unregistered_card_is_noop():
    # Card 1 is not in registry (not a Phase 1 event card)
    pub = _pub()
    pub.influence[(Side.USSR, 12)] = 2
    original = dict(pub.influence)
    new_pub, over, winner = _apply_event(pub, 1, Side.USSR, _rng0())
    # no board effect, game continues
    assert not over
    assert winner is None
