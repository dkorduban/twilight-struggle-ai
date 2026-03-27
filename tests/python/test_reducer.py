"""Tests for the PublicState and HandKnowledge reducers."""
import pytest
from tsrl.etl.reducer import (
    HAND_SIZE_EARLY,
    HAND_SIZE_LATE,
    ReducerError,
    reduce_hand,
    reduce_public,
)
from tsrl.schemas import EventKind, HandKnowledge, PublicState, ReplayEvent, Side


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

ALL_CARDS = frozenset(range(1, 111))  # cards 1-110

def ev(**kwargs) -> ReplayEvent:
    """Build a ReplayEvent with defaults for fields not specified."""
    defaults = dict(kind=EventKind.UNKNOWN, turn=1, ar=1, phasing=Side.USSR)
    defaults.update(kwargs)
    return ReplayEvent(**defaults)


def fresh_pub() -> PublicState:
    return PublicState()


def fresh_hand(observer: Side) -> HandKnowledge:
    return HandKnowledge(observer=observer, possible_hidden=ALL_CARDS)


# ---------------------------------------------------------------------------
# PublicState reducer
# ---------------------------------------------------------------------------


def test_turn_start_resets_milops():
    s = fresh_pub()
    s.milops = [3, 2]
    s2 = reduce_public(s, ev(kind=EventKind.TURN_START, turn=2))
    assert s2.milops == [0, 0]
    assert s2.turn == 2


def test_defcon_change():
    s = fresh_pub()
    s2 = reduce_public(s, ev(kind=EventKind.DEFCON_CHANGE, amount=3))
    assert s2.defcon == 3


def test_defcon_out_of_range_raises():
    s = fresh_pub()
    with pytest.raises(ReducerError):
        reduce_public(s, ev(kind=EventKind.DEFCON_CHANGE, amount=6))
    with pytest.raises(ReducerError):
        reduce_public(s, ev(kind=EventKind.DEFCON_CHANGE, amount=0))


def test_vp_change_accumulates():
    s = fresh_pub()
    s2 = reduce_public(s, ev(kind=EventKind.VP_CHANGE, amount=3))
    assert s2.vp == 3
    s3 = reduce_public(s2, ev(kind=EventKind.VP_CHANGE, amount=-5))
    assert s3.vp == -2


def test_discard_card():
    s = fresh_pub()
    s2 = reduce_public(s, ev(kind=EventKind.DISCARD, card_id=42))
    assert 42 in s2.discard


def test_remove_card():
    s = fresh_pub()
    s2 = reduce_public(s, ev(kind=EventKind.REMOVE, card_id=7))
    assert 7 in s2.removed


def test_remove_also_clears_discard():
    s = fresh_pub()
    s.discard = frozenset({7})
    s2 = reduce_public(s, ev(kind=EventKind.REMOVE, card_id=7))
    assert 7 in s2.removed
    assert 7 not in s2.discard


def test_china_card_pass():
    s = fresh_pub()
    assert s.china_held_by == Side.USSR
    s2 = reduce_public(s, ev(kind=EventKind.CHINA_CARD_PASS, phasing=Side.US))
    assert s2.china_held_by == Side.US
    assert s2.china_playable is True


def test_china_card_play_passes_to_opponent():
    """When USSR plays China Card (card_id=6) for ops, it passes face-down to US.

    Regression: previously PLAY card_id=6 was a no-op in the reducer, so
    china_held_by was never updated, causing scoring errors.
    """
    s = fresh_pub()
    assert s.china_held_by == Side.USSR
    # USSR plays China Card for ops
    s2 = reduce_public(s, ev(kind=EventKind.PLAY, card_id=6, phasing=Side.USSR))
    assert s2.china_held_by == Side.US, (
        "After USSR plays China Card, US should hold it"
    )
    assert s2.china_playable is False, (
        "China Card is face-down (not yet playable) after being played"
    )


def test_china_card_play_by_us_passes_to_ussr():
    """When US plays China Card (card_id=6) for ops, it passes face-up to USSR."""
    s = fresh_pub()
    s.china_held_by = Side.US
    s.china_playable = True
    # US plays China Card for ops
    s2 = reduce_public(s, ev(kind=EventKind.PLAY, card_id=6, phasing=Side.US))
    assert s2.china_held_by == Side.USSR, (
        "After US plays China Card, USSR should hold it"
    )
    assert s2.china_playable is True, (
        "China Card goes face-up to USSR after US plays it"
    )


def test_nixon_play_for_ops_does_not_transfer_china():
    """Nixon Plays The China Card (card_id=72) played for OPS should NOT transfer China.

    Only when Nixon fires as an EVENT should China transfer to US. Playing Nixon
    for influence ops is a normal ops play with no china effect.
    """
    s = fresh_pub()
    assert s.china_held_by == Side.USSR
    # US plays Nixon for ops — china should stay at USSR
    s2 = reduce_public(s, ev(kind=EventKind.PLAY, card_id=72, phasing=Side.US))
    assert s2.china_held_by == Side.USSR, (
        "Playing Nixon for ops should NOT transfer the China Card"
    )


def test_place_influence():
    s = fresh_pub()
    s2 = reduce_public(s, ev(
        kind=EventKind.PLACE_INFLUENCE,
        phasing=Side.US,
        country_id=10,
        amount=2,
    ))
    assert s2.influence.get((Side.US, 10), 0) == 2


def test_place_influence_accumulates():
    s = fresh_pub()
    s.influence[(Side.USSR, 5)] = 1
    s2 = reduce_public(s, ev(
        kind=EventKind.PLACE_INFLUENCE,
        phasing=Side.USSR,
        country_id=5,
        amount=2,
    ))
    assert s2.influence[(Side.USSR, 5)] == 3


def test_remove_influence_floor_zero():
    s = fresh_pub()
    s.influence[(Side.US, 3)] = 1
    s2 = reduce_public(s, ev(
        kind=EventKind.REMOVE_INFLUENCE,
        phasing=Side.US,
        country_id=3,
        amount=5,  # more than present
    ))
    assert s2.influence.get((Side.US, 3), 0) == 0


def test_reduce_public_does_not_mutate_input():
    s = fresh_pub()
    original_vp = s.vp
    reduce_public(s, ev(kind=EventKind.VP_CHANGE, amount=10))
    assert s.vp == original_vp  # original unchanged


def test_unknown_event_no_op():
    s = fresh_pub()
    s2 = reduce_public(s, ev(kind=EventKind.UNKNOWN))
    assert s2.vp == s.vp
    assert s2.defcon == s.defcon


# ---------------------------------------------------------------------------
# HandKnowledge reducer
# ---------------------------------------------------------------------------


def test_play_removes_from_known_in_hand():
    hk = HandKnowledge(
        observer=Side.USSR,
        known_in_hand=frozenset({10, 20}),
        possible_hidden=ALL_CARDS - {10, 20},
    )
    hk.hand_size = 2
    hk2 = reduce_hand(hk, ev(kind=EventKind.PLAY, phasing=Side.USSR, card_id=10), ALL_CARDS, fresh_pub())
    assert 10 not in hk2.known_in_hand
    assert 10 in hk2.known_not_in_hand
    assert hk2.hand_size == 1


def test_play_by_opponent_adds_to_not_in_hand():
    hk = fresh_hand(Side.USSR)
    hk2 = reduce_hand(hk, ev(kind=EventKind.PLAY, phasing=Side.US, card_id=42), ALL_CARDS, fresh_pub())
    assert 42 in hk2.known_not_in_hand
    assert 42 not in hk2.possible_hidden


def test_reveal_hand_adds_to_known_in_hand():
    hk = fresh_hand(Side.USSR)
    hk.hand_size = 0
    hk2 = reduce_hand(
        hk,
        ev(kind=EventKind.REVEAL_HAND, phasing=Side.USSR, aux_card_ids=(5, 6, 7)),
        ALL_CARDS,
        fresh_pub(),
    )
    assert frozenset({5, 6, 7}).issubset(hk2.known_in_hand)


def test_reveal_opponent_hand_updates_not_in_hand_for_observer():
    """When opponent's hand is revealed, observer knows those cards are not theirs."""
    hk = fresh_hand(Side.USSR)
    hk2 = reduce_hand(
        hk,
        ev(kind=EventKind.REVEAL_HAND, phasing=Side.US, aux_card_ids=(11, 12)),
        ALL_CARDS,
        fresh_pub(),
    )
    # Those cards are now in known_not_in_hand (from USSR observer's perspective —
    # they're in US hand, not USSR hand)
    assert 11 in hk2.known_not_in_hand
    assert 11 not in hk2.possible_hidden


def test_end_turn_held_adds_to_known_in_hand():
    hk = fresh_hand(Side.USSR)
    hk2 = reduce_hand(
        hk,
        ev(kind=EventKind.END_TURN_HELD, phasing=Side.USSR, aux_card_ids=(99,)),
        ALL_CARDS,
        fresh_pub(),
    )
    assert 99 in hk2.known_in_hand


def test_remove_clears_from_possible_hidden():
    hk = fresh_hand(Side.USSR)
    hk2 = reduce_hand(hk, ev(kind=EventKind.REMOVE, card_id=55), ALL_CARDS, fresh_pub())
    assert 55 not in hk2.possible_hidden
    assert 55 in hk2.known_not_in_hand


def test_invariant_violation_raises():
    """If reducer logic creates an invariant violation, it should raise."""
    # Manually create a bad HandKnowledge (overlap between in/not-in hand)
    # then verify that the invariant check fires if we try to validate it.
    from tsrl.etl.reducer import _verify_hand_invariants, ReducerError
    bad = HandKnowledge(
        observer=Side.USSR,
        known_in_hand=frozenset({1}),
        known_not_in_hand=frozenset({1}),  # overlap!
        possible_hidden=frozenset(),
    )
    with pytest.raises(ReducerError):
        _verify_hand_invariants(bad)


def test_reduce_hand_does_not_mutate_input():
    hk = HandKnowledge(
        observer=Side.USSR,
        known_in_hand=frozenset({10}),
        known_not_in_hand=frozenset(),
        possible_hidden=ALL_CARDS - {10},
        hand_size=1,
    )
    original_in_hand = hk.known_in_hand
    reduce_hand(hk, ev(kind=EventKind.PLAY, phasing=Side.USSR, card_id=10), ALL_CARDS, fresh_pub())
    assert hk.known_in_hand == original_in_hand  # unchanged


def test_china_card_pass_updates_holds_china():
    hk = HandKnowledge(observer=Side.USSR, holds_china=True, possible_hidden=frozenset())
    hk2 = reduce_hand(
        hk,
        ev(kind=EventKind.CHINA_CARD_PASS, phasing=Side.US),
        ALL_CARDS,
        fresh_pub(),
    )
    assert hk2.holds_china is False  # observer is USSR, China passed to US


def test_reshuffle_reopens_possible_hidden():
    """After reshuffle, discarded cards can be in hand again."""
    pub = fresh_pub()
    pub.discard = frozenset({10, 20})
    hk = HandKnowledge(
        observer=Side.USSR,
        known_not_in_hand=frozenset({10, 20}),  # they were discarded
        possible_hidden=ALL_CARDS - {10, 20},
    )
    hk2 = reduce_hand(hk, ev(kind=EventKind.RESHUFFLE), ALL_CARDS, pub)
    # After reshuffle, 10 and 20 may now be back in play
    assert 10 in hk2.possible_hidden or 10 not in hk2.known_not_in_hand


# ---------------------------------------------------------------------------
# Batch reducer smoke test
# ---------------------------------------------------------------------------


def test_reduce_game_smoke():
    from tsrl.etl.reducer import reduce_game
    from tsrl.etl.parser import parse_replay

    # Use real TSEspionage/ACTS format
    log = "\n".join([
        "SETUP: : PlayerA will play as USSR.",
        "PlayerB will play as USA.",
        "Turn 1, Headline Phase: Duck and Cover & COMECON:",
        "USSR Headlines Duck and Cover",
        "US Headlines COMECON",
        "Turn 1, USSR AR1: Captured Nazi Scientist*: Event: Captured Nazi Scientist*",
        "USSR gains 3 VP. Score is USSR 3.",
        "DEFCON degrades to 4",
        "Turn 1, Cleanup: : ",
    ])
    result = parse_replay(log)
    triples = reduce_game(result.events, ALL_CARDS)
    assert len(triples) == len(result.events)
    final_pub = triples[-1][0]
    assert final_pub.vp == 3
    assert final_pub.defcon == 4


def test_game_start_seeds_standard_influence():
    """GAME_START initializes pub.influence from countries.csv starting positions."""
    from tsrl.etl.game_data import load_countries
    pub = PublicState()
    game_start = ev(kind=EventKind.GAME_START, turn=0, ar=0)
    new_pub = reduce_public(pub, game_start)
    countries = load_countries()
    for cid, spec in countries.items():
        if spec.ussr_start > 0:
            assert new_pub.influence.get((Side.USSR, cid), 0) == spec.ussr_start, \
                f"USSR start wrong for {spec.name}: expected {spec.ussr_start}"
        if spec.us_start > 0:
            assert new_pub.influence.get((Side.US, cid), 0) == spec.us_start, \
                f"US start wrong for {spec.name}: expected {spec.us_start}"


def test_game_start_east_germany_and_iran():
    """Spot-check the two countries that caused silent bugs in competitive logs."""
    pub = PublicState()
    new_pub = reduce_public(pub, ev(kind=EventKind.GAME_START, turn=0, ar=0))
    # East Germany (id=5): USSR=3 standard
    assert new_pub.influence.get((Side.USSR, 5), 0) == 3
    # Iran (id=28): US=1 standard
    assert new_pub.influence.get((Side.US, 28), 0) == 1


def test_setup_placement_adds_on_top_of_standard():
    """Setup PLACE_INFLUENCE is additive on top of the standard starting state."""
    from tsrl.etl.parser import parse_replay
    from tsrl.etl.resolver import resolve_names
    from tsrl.etl.reducer import reduce_game
    from tsrl.etl.game_data import load_cards, load_countries
    # Competitive log: EG standard=3, log places +1 → expect EG USSR=4
    log = "\n".join([
        "SETUP: : PlayerA will play as USSR.",
        "PlayerB will play as USA.",
        "USSR +1 in East Germany [0][4]",
        "US +1 in Iran [2][0]",
        "Turn 1, Headline Phase: Duck and Cover & COMECON:",
        "USSR Headlines Duck and Cover",
        "US Headlines COMECON",
    ])
    result = parse_replay(log)
    resolved = resolve_names(result.events, load_cards(), load_countries())
    triples = reduce_game(resolved, ALL_CARDS)
    final_pub = triples[-1][0]
    assert final_pub.influence.get((Side.USSR, 5), 0) == 4, "EG should be 3+1=4"
    assert final_pub.influence.get((Side.US, 28), 0) == 2, "Iran should be 1+1=2"


def test_milops_reset_at_headline_phase_start():
    """Milops must reset to [0,0] at HEADLINE_PHASE_START (turn boundary in real logs).

    Real TSEspionage logs never emit TURN_START; turn transitions use
    HEADLINE_PHASE_START.  If milops are not reset there, end-of-turn penalty
    checks will use stale values from the previous turn.
    """
    pub = PublicState(milops=[3, 2])  # leftover from some prior turn
    new_pub = reduce_public(pub, ev(kind=EventKind.HEADLINE_PHASE_START, turn=2, ar=0))
    assert new_pub.milops == [0, 0], (
        f"milops should reset to [0,0] at HEADLINE_PHASE_START, got {new_pub.milops}"
    )
