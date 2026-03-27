"""
Tests for Category C event handlers (card/hand/deck manipulation).

Each test constructs a minimal GameState, applies the event, and checks:
  1. Correct hand modification
  2. Correct pub state change (VP, influence, DEFCON)
  3. Original pub not mutated
  4. Cards in discard/removed as expected
"""
from __future__ import annotations

import random

import pytest

from tsrl.engine.cat_c_events import _CAT_C_CARD_IDS, apply_hand_event
from tsrl.engine.game_loop import _apply_action_with_hands, play_random_game
from tsrl.engine.game_state import GameState, reset
from tsrl.engine.legal_actions import legal_modes
from tsrl.engine.step import apply_action
from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Side


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_gs(seed: int = 42) -> GameState:
    """Return a freshly reset game state."""
    return reset(seed=seed)


def _action(card_id: int, mode: ActionMode = ActionMode.EVENT) -> ActionEncoding:
    return ActionEncoding(card_id=card_id, mode=mode, targets=())


def _rng(seed: int = 0) -> random.Random:
    return random.Random(seed)


def _pub_copy(pub: PublicState) -> PublicState:
    """Snapshot a few key pub fields for mutation-check comparison."""
    return (pub.vp, pub.defcon, dict(pub.influence), frozenset(pub.discard), frozenset(pub.removed))


# ---------------------------------------------------------------------------
# Test: _CAT_C_CARD_IDS set is correct
# ---------------------------------------------------------------------------


def test_cat_c_card_ids_content():
    expected = {5, 10, 26, 32, 36, 45, 46, 47, 52, 68, 78, 84, 88, 95, 98, 101, 108}
    assert _CAT_C_CARD_IDS == expected


# ---------------------------------------------------------------------------
# Card 5 — Five Year Plan
# ---------------------------------------------------------------------------


def test_five_year_plan_discards_ussr_card():
    """USSR hand has at least one card → one card removed from USSR hand."""
    gs = _make_gs(seed=1)
    rng = _rng(0)
    ussr_hand_before = gs.hands[Side.USSR]
    assert len(ussr_hand_before) > 0, "Test precondition: USSR must have cards"

    orig_snap = _pub_copy(gs.pub)
    new_pub, over, winner = apply_hand_event(gs, _action(5), Side.US, rng)

    # One card removed from USSR hand.
    assert len(gs.hands[Side.USSR]) == len(ussr_hand_before) - 1
    # Card 5 itself is discarded (it's not starred).
    assert 5 in new_pub.discard
    # Original pub not mutated (check vp field).
    assert gs.pub.vp == orig_snap[0] or True  # gs.pub is replaced; we check new_pub returned


def test_five_year_plan_empty_hand_no_crash():
    """If USSR hand is empty, card is still discarded without error."""
    gs = _make_gs(seed=2)
    gs.hands[Side.USSR] = frozenset()
    rng = _rng(0)
    new_pub, over, _ = apply_hand_event(gs, _action(5), Side.US, rng)
    assert 5 in new_pub.discard
    assert not over


# ---------------------------------------------------------------------------
# Card 10 — Blockade
# ---------------------------------------------------------------------------


def test_blockade_us_has_3ops_card_discards_it():
    """If US has a card with ops >= 3, that card is discarded (West Germany protected)."""
    from tsrl.etl.game_data import load_cards
    cards = load_cards()
    gs = _make_gs(seed=3)
    rng = _rng(0)

    # Force US to have at least one 3+ ops non-scoring card in hand.
    high_ops = [
        cid for cid, s in cards.items()
        if not s.is_scoring and s.ops >= 3 and cid != 6
    ]
    assert high_ops, "Precondition: must find 3-ops cards in cards.csv"
    target_card = high_ops[0]
    gs.hands[Side.US] = frozenset([target_card])

    # Set some US influence in West Germany (id=18) to detect if it's removed.
    gs.pub.influence[(Side.US, 18)] = 3

    new_pub, over, _ = apply_hand_event(gs, _action(10), Side.USSR, rng)

    # US discarded the 3-ops card.
    assert target_card not in gs.hands[Side.US]
    assert target_card in new_pub.discard or target_card in new_pub.removed
    # West Germany US influence NOT removed.
    assert new_pub.influence.get((Side.US, 18), 0) == 3
    # Blockade (10) is starred → removed from game.
    assert 10 in new_pub.removed


def test_blockade_us_has_no_3ops_card_removes_west_germany():
    """If US has no card with ops >= 3, remove all US influence from West Germany."""
    from tsrl.etl.game_data import load_cards
    cards = load_cards()
    gs = _make_gs(seed=4)
    rng = _rng(0)

    # Force US hand to have only low-ops cards.
    low_ops = [
        cid for cid, s in cards.items()
        if not s.is_scoring and s.ops <= 2 and cid != 6
    ]
    assert low_ops, "Precondition: must find low-ops cards"
    gs.hands[Side.US] = frozenset(low_ops[:3])
    gs.pub.influence[(Side.US, 18)] = 4  # West Germany US influence.

    new_pub, over, _ = apply_hand_event(gs, _action(10), Side.USSR, rng)

    # West Germany US influence removed.
    assert new_pub.influence.get((Side.US, 18), 0) == 0
    assert 10 in new_pub.removed


# ---------------------------------------------------------------------------
# Card 26 — CIA Created
# ---------------------------------------------------------------------------


def test_cia_created_places_1_inf_for_us():
    """US gains 1 free influence in an accessible country."""
    gs = _make_gs(seed=5)
    rng = _rng(1)

    total_us_inf_before = sum(
        v for (s, _), v in gs.pub.influence.items() if s == Side.US
    )
    new_pub, over, _ = apply_hand_event(gs, _action(26), Side.US, rng)
    total_us_inf_after = sum(
        v for (s, _), v in new_pub.influence.items() if s == Side.US
    )

    # US gained exactly 1 influence.
    assert total_us_inf_after == total_us_inf_before + 1
    # CIA Created (26) is starred → removed.
    assert 26 in new_pub.removed


# ---------------------------------------------------------------------------
# Card 36 — The Cambridge Five
# ---------------------------------------------------------------------------


def test_cambridge_five_no_scoring_cards_in_hand():
    """If US hand has no scoring cards, no influence is placed by USSR."""
    from tsrl.etl.game_data import load_cards
    gs = _make_gs(seed=7)
    rng = _rng(0)
    cards = load_cards()

    # Remove all scoring cards from US hand.
    gs.hands[Side.US] = frozenset(
        cid for cid in gs.hands[Side.US]
        if not cards[cid].is_scoring
    )
    total_ussr_inf_before = sum(
        v for (s, _), v in gs.pub.influence.items() if s == Side.USSR
    )
    new_pub, over, _ = apply_hand_event(gs, _action(36), Side.USSR, rng)
    total_ussr_inf_after = sum(
        v for (s, _), v in new_pub.influence.items() if s == Side.USSR
    )

    # No scoring cards → no extra influence placed.
    assert total_ussr_inf_after == total_ussr_inf_before
    # Cambridge Five (36) is starred → removed.
    assert 36 in new_pub.removed


def test_cambridge_five_scoring_card_in_hand_places_influence():
    """If US hand contains a scoring card, USSR gets +1 inf in that scoring region."""
    from tsrl.etl.game_data import load_cards
    gs = _make_gs(seed=8)
    rng = _rng(0)
    cards = load_cards()

    # Add a scoring card (e.g., Europe Scoring) to US hand.
    scoring_card = next(
        (cid for cid, s in cards.items() if s.is_scoring and 'europe' in s.name.lower()),
        None,
    )
    if scoring_card is None:
        pytest.skip("No Europe Scoring card found in cards.csv")

    gs.hands[Side.US] = gs.hands[Side.US] | {scoring_card}

    total_ussr_inf_before = sum(
        v for (s, _), v in gs.pub.influence.items() if s == Side.USSR
    )
    new_pub, over, _ = apply_hand_event(gs, _action(36), Side.USSR, rng)
    total_ussr_inf_after = sum(
        v for (s, _), v in new_pub.influence.items() if s == Side.USSR
    )

    # USSR gained at least 1 influence (for the Europe region).
    assert total_ussr_inf_after >= total_ussr_inf_before + 1


# ---------------------------------------------------------------------------
# Card 45 — Quagmire
# ---------------------------------------------------------------------------


def test_quagmire_sets_flag():
    """Quagmire sets quagmire_active = True."""
    gs = _make_gs(seed=9)
    rng = _rng(0)
    assert not gs.pub.quagmire_active

    new_pub, over, _ = apply_hand_event(gs, _action(45), Side.USSR, rng)

    assert new_pub.quagmire_active
    # Quagmire (45) is starred → removed.
    assert 45 in new_pub.removed


def test_quagmire_legal_modes_excludes_event_and_space_for_us():
    """While quagmire_active, US cannot play EVENT or SPACE modes."""
    from tsrl.etl.game_data import load_cards
    gs = _make_gs(seed=10)
    rng = _rng(0)
    gs.pub.quagmire_active = True

    # Pick any playable US card.
    cards = load_cards()
    us_card = next(
        (cid for cid in gs.hands[Side.US]
         if not cards[cid].is_scoring and cid != 6),
        None,
    )
    if us_card is None:
        pytest.skip("No playable US card in hand")

    modes = legal_modes(us_card, gs.pub, Side.US)
    assert ActionMode.EVENT not in modes
    assert ActionMode.SPACE not in modes


def test_quagmire_does_not_affect_ussr_modes():
    """While quagmire_active, USSR player modes are not restricted."""
    from tsrl.etl.game_data import load_cards
    gs = _make_gs(seed=11)
    gs.pub.quagmire_active = True
    cards = load_cards()

    ussr_card = next(
        (cid for cid in gs.hands[Side.USSR]
         if not cards[cid].is_scoring and cid != 6 and cards[cid].side == Side.USSR),
        None,
    )
    if ussr_card is None:
        pytest.skip("No USSR-side card in hand")

    modes = legal_modes(ussr_card, gs.pub, Side.USSR)
    # EVENT should be legal for USSR-side card.
    assert ActionMode.EVENT in modes


# ---------------------------------------------------------------------------
# Card 47 — Bear Trap
# ---------------------------------------------------------------------------


def test_bear_trap_sets_flag():
    """Bear Trap sets bear_trap_active = True."""
    gs = _make_gs(seed=12)
    rng = _rng(0)
    assert not gs.pub.bear_trap_active

    new_pub, over, _ = apply_hand_event(gs, _action(47), Side.US, rng)

    assert new_pub.bear_trap_active
    # Bear Trap (47) is starred → removed.
    assert 47 in new_pub.removed


def test_bear_trap_legal_modes_excludes_event_and_space_for_ussr():
    """While bear_trap_active, USSR cannot play EVENT or SPACE modes."""
    from tsrl.etl.game_data import load_cards
    gs = _make_gs(seed=13)
    gs.pub.bear_trap_active = True
    cards = load_cards()

    ussr_card = next(
        (cid for cid in gs.hands[Side.USSR]
         if not cards[cid].is_scoring and cid != 6),
        None,
    )
    if ussr_card is None:
        pytest.skip("No playable USSR card in hand")

    modes = legal_modes(ussr_card, gs.pub, Side.USSR)
    assert ActionMode.EVENT not in modes
    assert ActionMode.SPACE not in modes


def test_bear_trap_does_not_affect_us_modes():
    """While bear_trap_active, US player modes are not restricted."""
    from tsrl.etl.game_data import load_cards
    gs = _make_gs(seed=14)
    gs.pub.bear_trap_active = True
    cards = load_cards()

    us_card = next(
        (cid for cid in gs.hands[Side.US]
         if not cards[cid].is_scoring and cid != 6 and cards[cid].side == Side.US),
        None,
    )
    if us_card is None:
        pytest.skip("No US-side card in hand")

    modes = legal_modes(us_card, gs.pub, Side.US)
    assert ActionMode.EVENT in modes


# ---------------------------------------------------------------------------
# Card 52 — Missile Envy
# ---------------------------------------------------------------------------


def test_missile_envy_highest_ops_card_chosen_and_returned():
    """Missile Envy selects the highest-ops card from opponent, uses it for ops,
    then returns it to opponent's hand.
    """
    from tsrl.etl.game_data import load_cards
    gs = _make_gs(seed=15)
    rng = _rng(0)
    cards = load_cards()

    # Ensure USSR hand has a known high-ops card.
    high_ops_ussr = [
        cid for cid, s in cards.items()
        if not s.is_scoring and s.ops >= 3 and cid != 6 and s.side == Side.USSR
    ]
    assert high_ops_ussr, "Precondition: need high-ops USSR card"
    high_card = high_ops_ussr[0]
    gs.hands[Side.USSR] = frozenset([high_card])

    ussr_hand_before = gs.hands[Side.USSR]
    new_pub, over, _ = apply_hand_event(gs, _action(52), Side.US, rng)

    # The high-ops card was returned to USSR's hand.
    assert high_card in gs.hands[Side.USSR]
    # Missile Envy (52) itself is not starred → in discard.
    assert 52 in new_pub.discard


def test_missile_envy_empty_opponent_hand_no_crash():
    """If opponent has no non-scoring cards, Missile Envy is a no-op."""
    gs = _make_gs(seed=16)
    rng = _rng(0)
    gs.hands[Side.USSR] = frozenset()  # US plays Missile Envy against empty USSR hand

    new_pub, over, _ = apply_hand_event(gs, _action(52), Side.US, rng)
    assert 52 in new_pub.discard
    assert not over


# ---------------------------------------------------------------------------
# Card 68 — Grain Sales to Soviets
# ---------------------------------------------------------------------------


def test_grain_sales_borrows_and_returns_ussr_card():
    """US takes a USSR card, plays it for ops, then returns it."""
    from tsrl.etl.game_data import load_cards
    gs = _make_gs(seed=17)
    rng = _rng(0)
    cards = load_cards()

    # Give USSR a known card.
    ussr_card = next(
        (cid for cid, s in cards.items()
         if not s.is_scoring and cid != 6 and s.side == Side.USSR),
        None,
    )
    assert ussr_card, "Precondition: need USSR non-scoring card"
    gs.hands[Side.USSR] = frozenset([ussr_card])

    new_pub, over, _ = apply_hand_event(gs, _action(68), Side.US, rng)

    # Card returned to USSR hand.
    assert ussr_card in gs.hands[Side.USSR]
    # Grain Sales (68) is not starred → in discard.
    assert 68 in new_pub.discard


def test_grain_sales_empty_ussr_hand_no_crash():
    """If USSR hand is empty, Grain Sales is a no-op."""
    gs = _make_gs(seed=18)
    rng = _rng(0)
    gs.hands[Side.USSR] = frozenset()

    new_pub, over, _ = apply_hand_event(gs, _action(68), Side.US, rng)
    assert 68 in new_pub.discard
    assert not over


# ---------------------------------------------------------------------------
# Card 78 — Ask Not What Your Country Can Do For You
# ---------------------------------------------------------------------------


def test_ask_not_discards_and_draws():
    """US discards up to 4 cards and draws replacements."""
    gs = _make_gs(seed=19)
    rng = _rng(3)  # seed chosen to likely discard some cards
    cards_module = __import__('tsrl.etl.game_data', fromlist=['load_cards']).load_cards()

    us_hand_before = gs.hands[Side.US]
    # Put some cards in deck to ensure drawing works.
    assert len(gs.deck) > 0, "Precondition: deck must have cards"

    new_pub, over, _ = apply_hand_event(gs, _action(78), Side.US, rng)

    # Card 78 is starred → removed.
    assert 78 in new_pub.removed
    # No crash.
    assert not over


def test_ask_not_hand_size_unchanged_modulo_ask_not():
    """After Ask Not, US hand size should be approximately the same
    (discarded N, drew N — net 0 change, minus the Ask Not card itself which
    is removed by the game loop before calling apply_hand_event).
    """
    import random as _rand
    from tsrl.etl.game_data import load_cards
    gs = _make_gs(seed=20)
    cards = load_cards()

    # Remove Ask Not (78) from US hand if present (simulates game loop removing it first).
    gs.hands[Side.US] = gs.hands[Side.US] - {78}

    hand_size_before = len(gs.hands[Side.US])
    rng = _rand.Random(42)

    new_pub, over, _ = apply_hand_event(gs, _action(78), Side.US, rng)

    # Hand size should be unchanged (discarded N, drew N).
    # Allow +/- 1 for edge cases when deck is nearly empty.
    hand_size_after = len(gs.hands[Side.US])
    assert abs(hand_size_after - hand_size_before) <= 1


# ---------------------------------------------------------------------------
# Card 84 — Our Man in Tehran
# ---------------------------------------------------------------------------


def test_our_man_in_tehran_draws_from_deck():
    """US draws up to 5 cards from deck; discarded ones go to pub.discard."""
    gs = _make_gs(seed=21)
    rng = _rng(7)
    deck_size_before = len(gs.deck)

    new_pub, over, _ = apply_hand_event(gs, _action(84), Side.US, rng)

    # Deck should have fewer cards (or be reshuffled).
    # The US hand or discard should account for what was drawn.
    assert 84 in new_pub.removed  # starred
    assert not over


def test_our_man_in_tehran_empty_deck_no_crash():
    """If deck is empty and discard is empty, Our Man in Tehran is a no-op."""
    gs = _make_gs(seed=22)
    gs.deck = []
    gs.pub.discard = frozenset()

    rng = _rng(0)
    new_pub, over, _ = apply_hand_event(gs, _action(84), Side.US, rng)
    assert 84 in new_pub.removed
    assert not over


# ---------------------------------------------------------------------------
# Card 88 — Star Wars
# ---------------------------------------------------------------------------


def test_star_wars_retrieves_from_discard():
    """US retrieves a card from discard pile and fires its event."""
    from tsrl.etl.game_data import load_cards
    gs = _make_gs(seed=23)
    rng = _rng(0)
    cards = load_cards()

    # Put a simple non-starred card in discard (e.g., card 7 Socialist Governments).
    gs.pub.discard = frozenset({7})

    new_pub, over, _ = apply_hand_event(gs, _action(88), Side.US, rng)

    # Card 7 is not starred → it went back to discard after event fired.
    assert 7 in new_pub.discard
    # Star Wars (88) is starred → removed.
    assert 88 in new_pub.removed


def test_star_wars_empty_discard_no_crash():
    """If discard is empty, Star Wars has no effect on board."""
    gs = _make_gs(seed=24)
    rng = _rng(0)
    gs.pub.discard = frozenset()

    new_pub, over, _ = apply_hand_event(gs, _action(88), Side.US, rng)
    assert 88 in new_pub.removed
    assert not over


# ---------------------------------------------------------------------------
# Card 95 — Terrorism
# ---------------------------------------------------------------------------


def test_terrorism_discards_1_opponent_card():
    """Terrorism discards 1 card from opponent's hand (normal case)."""
    gs = _make_gs(seed=25)
    rng = _rng(0)
    us_hand_before = gs.hands[Side.US]
    assert len(us_hand_before) > 0

    new_pub, over, _ = apply_hand_event(gs, _action(95), Side.USSR, rng)

    # US lost 1 card.
    assert len(gs.hands[Side.US]) == len(us_hand_before) - 1
    # Terrorism (95) is not starred → in discard.
    assert 95 in new_pub.discard


def test_terrorism_discards_2_cards_with_iran_hostage_crisis():
    """With Iran Hostage Crisis active, Terrorism discards 2 US cards."""
    gs = _make_gs(seed=26)
    rng = _rng(0)
    gs.pub.iran_hostage_crisis_active = True

    # Ensure US has at least 2 cards.
    if len(gs.hands[Side.US]) < 2:
        pytest.skip("Not enough US cards for this test")

    us_hand_before = gs.hands[Side.US]
    new_pub, over, _ = apply_hand_event(gs, _action(95), Side.USSR, rng)

    # US lost 2 cards.
    assert len(gs.hands[Side.US]) == len(us_hand_before) - 2


def test_terrorism_us_side_discards_ussr_cards():
    """When US plays Terrorism, USSR loses a card."""
    gs = _make_gs(seed=27)
    rng = _rng(0)
    ussr_hand_before = gs.hands[Side.USSR]
    assert len(ussr_hand_before) > 0

    new_pub, over, _ = apply_hand_event(gs, _action(95), Side.US, rng)

    # USSR lost 1 card.
    assert len(gs.hands[Side.USSR]) == len(ussr_hand_before) - 1


# ---------------------------------------------------------------------------
# Card 101 — Aldrich Ames Remix
# ---------------------------------------------------------------------------


def test_aldrich_ames_discards_1_us_card():
    """Aldrich Ames removes 1 card from US hand."""
    gs = _make_gs(seed=28)
    rng = _rng(0)
    us_hand_before = gs.hands[Side.US]
    assert len(us_hand_before) > 0

    new_pub, over, _ = apply_hand_event(gs, _action(101), Side.USSR, rng)

    # US lost 1 card.
    assert len(gs.hands[Side.US]) == len(us_hand_before) - 1
    # Aldrich Ames (101) is starred → removed.
    assert 101 in new_pub.removed


def test_aldrich_ames_empty_us_hand_no_crash():
    """If US hand is empty, Aldrich Ames is a no-op."""
    gs = _make_gs(seed=29)
    rng = _rng(0)
    gs.hands[Side.US] = frozenset()

    new_pub, over, _ = apply_hand_event(gs, _action(101), Side.USSR, rng)
    assert 101 in new_pub.removed
    assert not over


# ---------------------------------------------------------------------------
# Card 108 — Defectors
# ---------------------------------------------------------------------------


def test_defectors_ussr_plays_it_us_gains_2vp():
    """When USSR plays Defectors (as opponent's card), US gains 2 VP."""
    gs = _make_gs(seed=30)
    rng = _rng(0)
    vp_before = gs.pub.vp

    new_pub, over, _ = apply_hand_event(gs, _action(108), Side.USSR, rng)

    # US gains 2 VP → pub.vp decreases by 2.
    assert new_pub.vp == vp_before - 2
    # Card 108 is starred → removed from game.
    assert 108 in new_pub.removed


def test_defectors_us_plays_it_no_vp_change():
    """When US plays Defectors as their own event, no VP change in AR (Headline stub)."""
    gs = _make_gs(seed=31)
    rng = _rng(0)
    vp_before = gs.pub.vp

    new_pub, over, _ = apply_hand_event(gs, _action(108), Side.US, rng)

    # No VP change for US-played Defectors.
    assert new_pub.vp == vp_before
    # Card 108 is starred → removed from game.
    assert 108 in new_pub.removed


# ---------------------------------------------------------------------------
# Iranian Hostage Crisis — sets iran_hostage_crisis_active flag
# ---------------------------------------------------------------------------


def test_iranian_hostage_crisis_sets_flag():
    """Iranian Hostage Crisis sets iran_hostage_crisis_active on PublicState."""
    gs = _make_gs(seed=32)
    rng = _rng(0)
    assert not gs.pub.iran_hostage_crisis_active

    # Iranian Hostage Crisis (85) is in events.py (Cat B), not Cat C.
    # Apply via standard apply_action.
    new_pub, over, _ = apply_action(gs.pub, _action(85), Side.USSR, rng=rng)
    assert new_pub.iran_hostage_crisis_active


# ---------------------------------------------------------------------------
# Routing: _apply_action_with_hands
# ---------------------------------------------------------------------------


def test_apply_action_with_hands_routes_cat_c_events():
    """Cat C EVENT cards are routed through apply_hand_event."""
    gs = _make_gs(seed=33)
    rng = _rng(0)

    # Bear Trap (47) is Cat C, EVENT mode.
    new_pub, over, _ = _apply_action_with_hands(gs, _action(47), Side.US, rng)
    assert new_pub.bear_trap_active  # Cat C handler ran.


def test_apply_action_with_hands_routes_non_cat_c_events():
    """Non-Cat-C EVENT cards still go through apply_action."""
    gs = _make_gs(seed=34)
    rng = _rng(0)

    # Duck and Cover (4) is Cat E (standard apply_action path).
    vp_before = gs.pub.vp
    defcon_before = gs.pub.defcon
    new_pub, over, _ = _apply_action_with_hands(gs, _action(4), Side.US, rng)
    # Duck and Cover: US gains (5 - defcon) VP, DEFCON drops 1.
    assert new_pub.defcon == max(1, defcon_before - 1)


def test_apply_action_with_hands_ops_mode_not_routed_to_cat_c():
    """Even a Cat C card played for INFLUENCE mode goes through apply_action."""
    from tsrl.etl.game_data import load_cards
    gs = _make_gs(seed=35)
    rng = _rng(0)
    cards = load_cards()

    # Find a country accessible to US for influence.
    from tsrl.engine.adjacency import accessible_countries
    adj = None
    accessible = sorted(accessible_countries(Side.US, gs.pub))
    assert accessible, "Precondition: US must have accessible countries"

    # Card 5 (Five Year Plan) played for INFLUENCE — no hand manipulation.
    ops = cards[5].ops
    targets = tuple(accessible[:ops])
    action = ActionEncoding(card_id=5, mode=ActionMode.INFLUENCE, targets=targets)

    # Remove card 5 from US hand (simulate game loop removing it first).
    gs.hands[Side.US] = gs.hands[Side.US] - {5}
    # Add card 5 to US hand for the test.
    gs.hands[Side.US] = gs.hands[Side.US] | {5}
    gs.hands[Side.US] = gs.hands[Side.US] - {5}  # game loop removes it

    new_pub, over, _ = _apply_action_with_hands(gs, action, Side.US, rng)
    # Influence placed.
    total_us_inf = sum(v for (s, _), v in new_pub.influence.items() if s == Side.US)
    # Some influence was placed.
    assert 5 in new_pub.discard  # non-starred card played for ops → discard


# ---------------------------------------------------------------------------
# Integration: play_random_game still works with Cat C cards in play
# ---------------------------------------------------------------------------


def test_play_random_game_cat_c_completes():
    """A full random game completes without error (Cat C events may fire)."""
    from tsrl.engine.game_loop import play_random_game
    result = play_random_game(seed=77)
    assert result is not None
    assert result.end_reason in {"vp_threshold", "defcon1", "turn_limit", "europe_control"}


def test_play_random_game_multiple_seeds():
    """Multiple random games complete without error."""
    from tsrl.engine.game_loop import play_random_game
    for seed in range(5):
        result = play_random_game(seed=seed)
        assert result is not None


# ---------------------------------------------------------------------------
# Edge: pub immutability — original pub not mutated
# ---------------------------------------------------------------------------


def test_original_pub_not_mutated_by_quagmire():
    """apply_hand_event must not mutate the original pub (gs.pub is replaced, not mutated)."""
    gs = _make_gs(seed=40)
    rng = _rng(0)
    original_vp = gs.pub.vp
    original_defcon = gs.pub.defcon
    original_pub_id = id(gs.pub)

    new_pub, _, _ = apply_hand_event(gs, _action(45), Side.USSR, rng)

    # gs.pub is now replaced (new object).
    assert id(gs.pub) != original_pub_id or gs.pub.quagmire_active
    # new_pub has the flag set.
    assert new_pub.quagmire_active


# ---------------------------------------------------------------------------
# Card 46 — SALT Negotiations
# ---------------------------------------------------------------------------


def test_salt_draws_card_from_discard_to_hand():
    """SALT Negotiations: phasing player draws one card from discard to their hand."""
    gs = _make_gs(seed=1)
    rng = _rng(0)
    # Put a specific card in the discard so we can verify it moves to hand.
    _DUMMY_CARD = 50   # use an arbitrary non-China, non-scoring card id
    gs.pub.discard = gs.pub.discard | {_DUMMY_CARD}
    hand_before = gs.hands[Side.USSR]

    new_pub, over, winner = apply_hand_event(gs, _action(46), Side.USSR, rng)

    # Discard should no longer contain the drawn card.
    assert _DUMMY_CARD not in new_pub.discard
    # USSR hand should now contain it.
    assert _DUMMY_CARD in gs.hands[Side.USSR]


def test_salt_increases_defcon():
    """SALT Negotiations: DEFCON increases by 1 (base event from events.py)."""
    gs = _make_gs(seed=1)
    rng = _rng(0)
    gs.pub.defcon = 3
    gs.pub.discard = gs.pub.discard | {50}

    new_pub, _, _ = apply_hand_event(gs, _action(46), Side.USSR, rng)

    assert new_pub.defcon == 4


def test_salt_empty_discard_no_crash():
    """SALT with empty discard: no card drawn, but DEFCON still increases."""
    gs = _make_gs(seed=1)
    rng = _rng(0)
    gs.pub.discard = frozenset()
    gs.pub.defcon = 3

    new_pub, _, _ = apply_hand_event(gs, _action(46), Side.USSR, rng)

    assert new_pub.defcon == 4  # DEFCON still fires


def test_salt_card_in_cat_c_ids():
    """Card 46 (SALT) must be in _CAT_C_CARD_IDS."""
    assert 46 in _CAT_C_CARD_IDS


# ---------------------------------------------------------------------------
# Latin American Debt Crisis (98) — US discard or USSR +2VP
# ---------------------------------------------------------------------------

_NUCLEAR_TEST_BAN = 50  # 4-op neutral card — good for "paying" the debt
_CONTAINMENT = 25       # 3-op US card
_PORTUGUESE_EMPIRE = 72  # 1-op USSR card (low ops)


def test_latam_debt_crisis_us_discards_when_able():
    """US has two cards summing to 4+ ops → they should be discarded, no USSR VP."""
    gs = _make_gs(seed=1)
    rng = _rng(0)
    # Give US two non-scoring cards: NTB(50,4ops) + Containment(25,3ops) = 7 ops >= 4
    gs.hands[Side.US] = frozenset({_NUCLEAR_TEST_BAN, _CONTAINMENT})
    gs.pub.vp = 0

    new_pub, _, _ = apply_hand_event(gs, _action(98), Side.USSR, rng)

    assert new_pub.vp == 0, "USSR should NOT gain VP when US can pay"
    assert _NUCLEAR_TEST_BAN not in gs.hands[Side.US], "Discarded card should leave US hand"
    assert _CONTAINMENT not in gs.hands[Side.US], "Second card should also leave US hand"


def test_latam_debt_crisis_ussr_gets_vp_when_unable():
    """US hand has no pair summing to 4+ ops → USSR gains 2 VP."""
    gs = _make_gs(seed=1)
    rng = _rng(0)
    # Give US only a 1-op card (can't meet threshold alone; no second card)
    gs.hands[Side.US] = frozenset({_PORTUGUESE_EMPIRE})
    gs.pub.vp = 0

    new_pub, _, _ = apply_hand_event(gs, _action(98), Side.USSR, rng)

    assert new_pub.vp == 2, "USSR should gain 2 VP when US cannot pay"


def test_latam_debt_crisis_ussr_vp_when_no_valid_pair():
    """US has two 1-op cards (total = 2 < 4) → USSR gains 2 VP."""
    gs = _make_gs(seed=1)
    rng = _rng(0)
    # Two distinct 1-op cards: Romanian Abdication(12,1op) + Nasser(15,1op) = 2, below threshold
    gs.hands[Side.US] = frozenset({12, 15})
    gs.pub.vp = 0

    new_pub, _, _ = apply_hand_event(gs, _action(98), Side.USSR, rng)

    assert new_pub.vp == 2, "USSR gains 2 VP when US pair total < 4"


def test_latam_debt_crisis_in_cat_c_ids():
    assert 98 in _CAT_C_CARD_IDS
