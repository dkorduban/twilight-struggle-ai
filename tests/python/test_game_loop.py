"""Tests for dice, scoring, game state, and the game loop."""
import pytest
from tsrl.engine.rng import make_rng

from tsrl.engine.dice import coup_net, coup_result, realign_result, space_result
from tsrl.engine.game_loop import GameResult, play_random_game, play_game, make_random_policy
from tsrl.engine.legal_actions import sample_action
from tsrl.engine.game_state import reset, _build_era_deck, _hand_size_for_turn, _ars_for_turn
from tsrl.engine.scoring import (
    Tier, _controls,
    score_region, score_southeast_asia, apply_scoring_card,
)
from tsrl.engine.step import apply_action
from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Region, Side


# ---------------------------------------------------------------------------
# Dice
# ---------------------------------------------------------------------------


def test_roll_d6_range():
    rng = make_rng(0)
    from tsrl.engine.dice import roll_d6
    for _ in range(100):
        r = roll_d6(rng)
        assert 1 <= r <= 6


def test_coup_net_positive():
    # roll=6, ops=4, stability=2 → net = 6+4-4 = 6
    assert coup_net(6, 4, 2) == 6


def test_coup_net_negative():
    assert coup_net(1, 1, 3) == -4  # fail


def test_coup_result_range():
    rng = make_rng(0)
    for _ in range(100):
        net = coup_result(3, 2, rng=rng)
        # net = roll(1-6) + 3 - 4; range: -3 to 5
        assert -100 < net < 100


def test_space_result_low_roll_succeeds():
    # Threshold at level 0 is 3; roll of 1 (≤ 3) should succeed.
    class FixedRNG:
        def integers(self, a, b): return 1
    result = space_result(0, rng=FixedRNG())
    assert result is True


def test_space_result_high_roll_fails():
    # Threshold at level 0 is 3; roll of 6 (> 3) should fail.
    class FixedRNG:
        def integers(self, a, b): return 6
    result = space_result(0, rng=FixedRNG())
    assert result is False


def test_space_result_max_level():
    rng = make_rng(0)
    assert space_result(8, rng=rng) is False


# ---------------------------------------------------------------------------
# Scoring helpers
# ---------------------------------------------------------------------------


def test_controls_false_no_influence():
    pub = PublicState()
    # France (id=7): stability=3; with 0 influence nothing is controlled.
    assert not _controls(Side.USSR, 7, pub)


def test_controls_true_enough_influence():
    pub = PublicState()
    # France stability=3, opp=0: need 0+3=3 influence to control.
    pub.influence[(Side.USSR, 7)] = 3
    assert _controls(Side.USSR, 7, pub)


def test_controls_false_not_enough_vs_opponent():
    pub = PublicState()
    # France stability=3; USSR=3, US=1: need 1+3=4 to control. 3 < 4 → not controlled.
    pub.influence[(Side.USSR, 7)] = 3
    pub.influence[(Side.US, 7)] = 1
    assert not _controls(Side.USSR, 7, pub)


def test_score_region_zero_with_no_influence():
    pub = PublicState()
    result = score_region(Region.ASIA, pub)
    assert result.vp_delta == 0
    assert not result.game_over


def test_score_region_ussr_presence():
    pub = PublicState()
    # North Korea (id=23): stability=3, battleground. USSR needs 3 to control.
    pub.influence[(Side.USSR, 23)] = 3
    result = score_region(Region.ASIA, pub)
    # USSR controls one battleground; US has nothing → USSR wins PRESENCE (3 VP).
    assert result.vp_delta > 0


def test_score_southeast_asia_zero():
    pub = PublicState()
    result = score_southeast_asia(pub)
    assert result.vp_delta == 0


def test_score_southeast_asia_thailand_worth_two():
    pub = PublicState()
    # Thailand (id=79): stability=2, is_battleground=True.
    # USSR needs 2 to control (opp=0: 2 >= 0+2).
    pub.influence[(Side.USSR, 79)] = 2
    result = score_southeast_asia(pub)
    assert result.vp_delta == 2  # Thailand = 2 VP


def test_indonesia_and_malaysia_scored_separately():
    """Indonesia (id=76, stab=1) and Malaysia (id=83, stab=2) are separate countries.

    Regression: previously combined as 'Indonesia/Malaysia' (id=76, stab=3),
    causing 2 VP under-count when both are controlled by the same player.

    The coup log confirms:
      Indonesia: 5 + 1 - 2x1 = 4  → stability=1
      Malaysia:  4 + 3 - 2x2 = 3  → stability=2

    SE Asia scoring = 1 VP per controlled country; Thailand = 2 VP.
    """
    pub = PublicState()
    # Indonesia (id=76, stab=1): US=1 controls (1 >= 0+1)
    pub.influence[(Side.US, 76)] = 1
    # Malaysia (id=83, stab=2): US=2 controls (2 >= 0+2)
    pub.influence[(Side.US, 84)] = 2
    result = score_southeast_asia(pub)
    assert result.vp_delta == -2, (
        f"US controls Indonesia and Malaysia → 2 VP US (delta=-2), got {result.vp_delta}"
    )


def test_indonesia_only_one_vp():
    """Indonesia alone (stab=1, US=1) → 1 VP for US."""
    pub = PublicState()
    pub.influence[(Side.US, 76)] = 1  # Indonesia stab=1, controlled
    result = score_southeast_asia(pub)
    assert result.vp_delta == -1


def test_malaysia_only_one_vp():
    """Malaysia alone (stab=2, US=2) → 1 VP for US."""
    pub = PublicState()
    pub.influence[(Side.US, 84)] = 2  # Malaysia stab=2, controlled
    result = score_southeast_asia(pub)
    assert result.vp_delta == -1


def test_score_europe_control_game_over():
    """Controlling all Europe BGs should trigger Europe Control game win."""
    pub = PublicState()
    # Europe BGs: East Germany(5), France(7), Italy(10), Poland(12),
    #              Turkey(16), UK(17), West Germany(18)
    bgs = [5, 7, 10, 12, 16, 17, 18]
    from tsrl.etl.game_data import load_countries
    countries = load_countries()
    for cid in bgs:
        stab = countries[cid].stability
        pub.influence[(Side.USSR, cid)] = stab  # just enough to control (opp=0)
    result = score_region(Region.EUROPE, pub)
    assert result.game_over
    assert result.winner == Side.USSR


def test_apply_scoring_card_asia():
    pub = PublicState()
    # Asia: no influence → 0 VP + China Card bonus (USSR holds by default → +1)
    result = apply_scoring_card(1, pub)
    # No influence so region score = 0; China Card held by USSR → +1
    assert result.vp_delta == 1


def test_midgame_asia_scoring_includes_se_asia():
    """Mid-game Asia Scoring card (id=1) must count SE Asia countries.

    SE Asia countries (Thailand=79, Vietnam=80, etc.) also count for standard
    Asia Scoring. The SE Asia Scoring card has separate per-country values.

    Board: USSR controls only Vietnam (id=80, SE Asia, stab=1, non-BG).
    Standard Asia Scoring returns Presence(3) regional VP.
    """
    pub = PublicState()
    pub.china_held_by = Side.US
    # USSR controls Vietnam (SE Asia non-BG, stab=1): influence=1
    pub.influence[(Side.USSR, 80)] = 1
    result = score_region(Region.ASIA, pub)
    assert result.vp_delta == 3, (
        f"Mid-game Asia Scoring must include SE Asia countries (Vietnam id=80); "
        f"expected vp_delta=3, got {result.vp_delta}"
    )


def test_midgame_asia_scoring_counts_standard_asia():
    """Mid-game Asia Scoring (id=1) does count standard Asia countries.

    North Korea (id=23, Asia, stab=3, BG): USSR controls it → PRESENCE.
    USSR: Presence(3) + 1 BG + adj_bonus(NK adj USA=0) = 4 VP.
    """
    pub = PublicState()
    pub.china_held_by = Side.US   # neutral — no China bonus
    # North Korea (id=23, Asia, stab=3, BG): USSR needs 3 to control
    pub.influence[(Side.USSR, 23)] = 3
    result = score_region(Region.ASIA, pub)
    # USSR Presence: base(3) + 1 BG(NK). US has nothing → 0. Net = +4 USSR.
    assert result.vp_delta > 0, (
        f"Mid-game Asia Scoring must count standard Asia countries (North Korea id=23); "
        f"expected vp_delta>0, got {result.vp_delta}"
    )


# ---------------------------------------------------------------------------
# GameState / reset
# ---------------------------------------------------------------------------


def test_reset_initial_hands():
    gs = reset(seed=0)
    # Both sides should have 8 cards in hand (turn 1 hand size).
    assert len(gs.hands[Side.USSR]) == 8
    assert len(gs.hands[Side.US]) == 8


def test_reset_no_hand_overlap():
    gs = reset(seed=0)
    overlap = gs.hands[Side.USSR] & gs.hands[Side.US]
    assert len(overlap) == 0


def test_reset_starting_influence():
    gs = reset(seed=0)
    # USSR should start with influence in East Germany (id=5, ussr_start=3 fixed)
    assert gs.pub.influence.get((Side.USSR, 5), 0) == 3


def test_reset_china_card_with_ussr():
    gs = reset(seed=0)
    assert gs.ussr_holds_china
    assert not gs.us_holds_china


def test_hand_size_for_turn():
    assert _hand_size_for_turn(1) == 8
    assert _hand_size_for_turn(3) == 8
    assert _hand_size_for_turn(4) == 9
    assert _hand_size_for_turn(10) == 9


def test_ars_for_turn():
    assert _ars_for_turn(1) == 6
    assert _ars_for_turn(3) == 6
    assert _ars_for_turn(4) == 7
    assert _ars_for_turn(10) == 7


def test_era_deck_early_only():
    deck = _build_era_deck(era_max=0)
    assert len(deck) > 0
    # No China Card (id=6) in deck.
    assert 6 not in deck


def test_era_deck_includes_scoring_cards():
    """Scoring cards must be in the draw deck — they are dealt to players and played as events."""
    deck = _build_era_deck(era_max=2)
    scoring_ids = {1, 2, 3, 40, 41, 80, 82}
    # All 7 scoring cards should be in the full (all-era) deck.
    assert scoring_ids.issubset(set(deck)), f"Missing scoring cards: {scoring_ids - set(deck)}"


def test_era_deck_early_war_has_three_scoring_cards():
    """Early War deck has exactly 3 scoring cards: Asia(1), Europe(2), Middle East(3)."""
    deck = _build_era_deck(era_max=0)
    scoring_ids = {1, 2, 3}
    assert scoring_ids.issubset(set(deck)), f"Missing early-war scoring cards: {scoring_ids - set(deck)}"
    # Mid/Late War scoring cards should NOT be in Early War deck.
    late_scoring = {40, 41, 80, 82}
    assert not (late_scoring & set(deck)), f"Unexpected late-war scoring in early deck: {late_scoring & set(deck)}"


# ---------------------------------------------------------------------------
# apply_action (step.py)
# ---------------------------------------------------------------------------


def test_apply_action_influence_returns_tuple():
    pub = PublicState()
    pub.influence[(Side.USSR, 12)] = 1
    action = ActionEncoding(card_id=7, mode=ActionMode.INFLUENCE, targets=(5,))
    result = apply_action(pub, action, Side.USSR)
    assert isinstance(result, tuple)
    new_pub, game_over, winner = result
    assert isinstance(new_pub, PublicState)
    assert isinstance(game_over, bool)


def test_apply_action_coup_with_dice():
    rng = make_rng(42)
    pub = PublicState()
    pub.defcon = 5
    pub.influence[(Side.US, 5)] = 2   # East Germany: US has 2
    # East Germany stability=3; USSR coup with 4 ops.
    action = ActionEncoding(card_id=16, mode=ActionMode.COUP, targets=(5,))
    new_pub, over, winner = apply_action(pub, action, Side.USSR, rng=rng)
    # Regardless of outcome, pub.defcon should drop (EG is battleground).
    assert new_pub.defcon < pub.defcon


def test_apply_action_space_advances_or_stays():
    rng = make_rng(99)
    pub = PublicState()
    pub.space[int(Side.USSR)] = 0
    action = ActionEncoding(card_id=7, mode=ActionMode.SPACE, targets=())
    new_pub, over, winner = apply_action(pub, action, Side.USSR, rng=rng)
    # Space level either advances or stays.
    assert new_pub.space[int(Side.USSR)] in (0, 1)


def test_apply_action_event_scoring_card():
    pub = PublicState()
    # Asia Scoring (id=1): no influence → 0 region VP, China held by USSR → +1
    action = ActionEncoding(card_id=1, mode=ActionMode.EVENT, targets=())
    new_pub, over, winner = apply_action(pub, action, Side.USSR)
    assert new_pub.vp == 1  # China bonus to USSR


# ---------------------------------------------------------------------------
# Game loop
# ---------------------------------------------------------------------------


def test_play_random_game_completes():
    result = play_random_game(seed=42)
    assert isinstance(result, GameResult)
    assert result.end_reason in ("vp_threshold", "defcon1", "turn_limit", "europe_control", "scoring_card_held")


def test_play_random_game_has_winner_or_draw():
    result = play_random_game(seed=0)
    if result.winner is not None:
        assert result.winner in (Side.USSR, Side.US)


def test_play_random_game_deterministic():
    r1 = play_random_game(seed=7)
    r2 = play_random_game(seed=7)
    assert r1.winner == r2.winner
    assert r1.final_vp == r2.final_vp
    assert r1.end_turn == r2.end_turn


def test_play_random_game_different_seeds():
    results = [play_random_game(seed=i) for i in range(5)]
    # At least some games should differ.
    vps = [r.final_vp for r in results]
    assert len(set(vps)) > 1


def test_play_random_game_vp_reasonable():
    """Final VP should be within the ±40 or so range; extreme outliers would indicate bugs."""
    for seed in range(10):
        result = play_random_game(seed=seed)
        assert -100 < result.final_vp < 100


def test_play_random_multiple_games():
    """Run 20 games; all should complete without exceptions."""
    for seed in range(20):
        play_random_game(seed=seed)


# ---------------------------------------------------------------------------
# Headline resolution order (higher ops first; US wins ties)
# ---------------------------------------------------------------------------


def test_headline_higher_ops_resolves_first():
    """USSR plays 1-op card, US plays 4-op card: US headline should resolve first."""
    from tsrl.engine.game_loop import _run_headline_phase
    from tsrl.engine.game_state import GameState, GamePhase, reset
    from tsrl.schemas import ActionEncoding, ActionMode, Side

    # Card 12 = Romanian Abdication (USSR, ops 1, no board effect in phase 1)
    # Card 21 = NATO (US, ops 4) — fires an effect, but we just care about ORDER
    # Use Defcon-safe state; both cards must be in hands.
    gs = reset(seed=0)
    gs.pub.turn = 1
    gs.pub.defcon = 5
    _USSR_CARD = 12   # Romanian Abdication, ops=1
    _US_CARD   = 21   # NATO, ops=4

    gs.hands[Side.USSR] = frozenset({_USSR_CARD})
    gs.hands[Side.US]   = frozenset({_US_CARD})
    gs.ussr_holds_china = False
    gs.us_holds_china   = False

    resolution_order = []

    def _ussr_policy(pub, hand, holds_china):
        return ActionEncoding(card_id=_USSR_CARD, mode=ActionMode.EVENT, targets=())

    def _us_policy(pub, hand, holds_china):
        return ActionEncoding(card_id=_US_CARD, mode=ActionMode.EVENT, targets=())

    # Wrap _apply_action_with_hands to record side order.
    from tsrl.engine import game_loop as _gl
    orig = _gl._apply_action_with_hands

    def _recording(gs, action, side, rng):
        resolution_order.append(side)
        return orig(gs, action, side, rng)

    _gl._apply_action_with_hands = _recording
    try:
        _run_headline_phase(gs, _ussr_policy, _us_policy, make_rng(0))
    finally:
        _gl._apply_action_with_hands = orig

    # US (4-op) must resolve before USSR (1-op)
    assert resolution_order[0] == Side.US
    assert resolution_order[1] == Side.USSR


def test_headline_tie_us_resolves_first():
    """Both sides play 0-ops scoring cards: US resolves first (ties go to US)."""
    from tsrl.engine.game_loop import _run_headline_phase
    from tsrl.engine.game_state import reset
    from tsrl.schemas import ActionEncoding, ActionMode, Side

    # Asia Scoring (1) and Europe Scoring (2) both ops=0.
    _USSR_CARD = 1   # Asia Scoring
    _US_CARD   = 2   # Europe Scoring

    gs = reset(seed=0)
    gs.pub.turn = 1
    gs.hands[Side.USSR] = frozenset({_USSR_CARD})
    gs.hands[Side.US]   = frozenset({_US_CARD})
    gs.ussr_holds_china = False
    gs.us_holds_china   = False

    resolution_order = []

    def _ussr_policy(pub, hand, holds_china):
        return ActionEncoding(card_id=_USSR_CARD, mode=ActionMode.EVENT, targets=())

    def _us_policy(pub, hand, holds_china):
        return ActionEncoding(card_id=_US_CARD, mode=ActionMode.EVENT, targets=())

    from tsrl.engine import game_loop as _gl
    orig = _gl._apply_action_with_hands

    def _recording(gs, action, side, rng):
        resolution_order.append(side)
        return orig(gs, action, side, rng)

    _gl._apply_action_with_hands = _recording
    try:
        _run_headline_phase(gs, _ussr_policy, _us_policy, make_rng(0))
    finally:
        _gl._apply_action_with_hands = orig

    assert resolution_order[0] == Side.US


def test_headline_defectors_cancels_ussr_headline():
    """If US headlines Defectors (108), USSR's headline card is discarded without firing."""
    from tsrl.engine.game_loop import _run_headline_phase
    from tsrl.engine.game_state import reset
    from tsrl.schemas import ActionEncoding, ActionMode, Side

    # Card 108 = Defectors (US, ops 2).
    # Card 8 = Fidel (USSR, ops 2) — would place 2 USSR inf in Cuba if it fired.
    _DEFECTORS = 108
    _FIDEL = 8
    _CUBA = 36

    gs = reset(seed=0)
    gs.pub.turn = 1
    gs.pub.defcon = 5
    gs.hands[Side.USSR] = frozenset({_FIDEL})
    gs.hands[Side.US]   = frozenset({_DEFECTORS})
    gs.ussr_holds_china = False
    gs.us_holds_china   = False

    def _ussr_policy(pub, hand, holds_china):
        return ActionEncoding(card_id=_FIDEL, mode=ActionMode.EVENT, targets=())

    def _us_policy(pub, hand, holds_china):
        return ActionEncoding(card_id=_DEFECTORS, mode=ActionMode.EVENT, targets=())

    rng = make_rng(0)
    _run_headline_phase(gs, _ussr_policy, _us_policy, rng)

    # Fidel would place USSR inf in Cuba; if cancelled, Cuba should have no USSR inf.
    assert gs.pub.influence.get((Side.USSR, _CUBA), 0) == 0
    # Fidel must be in discard (cancelled = discarded without effect).
    assert _FIDEL in gs.pub.discard


# ---------------------------------------------------------------------------
# NORAD: US free influence after USSR AR at DEFCON 2
# ---------------------------------------------------------------------------


def test_norad_triggers_at_defcon2_after_ussr_ar():
    """With NORAD active and DEFCON=2, US gains 1 influence in Italy after USSR AR.

    We track Italy specifically (not total US inf) because card events may also
    place influence as side effects.  NORAD places in a country where US already
    has influence; Italy(10) is pre-seeded with US inf and is the only eligible
    target here, so the +1 must land there.
    """
    from tsrl.engine.game_loop import _run_action_rounds
    from tsrl.engine.game_state import reset, GamePhase
    from tsrl.schemas import ActionEncoding, ActionMode, Side

    _ITALY = 10

    gs = reset(seed=0)
    gs.pub.turn = 1
    gs.pub.defcon = 2
    gs.pub.norad_active = True
    # CLEAR all existing US influence so Italy is the only NORAD target.
    gs.pub.influence = {k: v for k, v in gs.pub.influence.items() if k[0] != Side.US}
    gs.pub.influence[(Side.US, _ITALY)] = 2

    # Use SPACE mode so no event side-effects fire and alter influence counts.
    _USSR_CARD = 12
    _US_CARD   = 22
    gs.hands[Side.USSR] = frozenset({_USSR_CARD})
    gs.hands[Side.US]   = frozenset({_US_CARD})
    gs.ussr_holds_china = False
    gs.us_holds_china   = False

    italy_before = gs.pub.influence.get((Side.US, _ITALY), 0)

    def _policy(pub, hand, holds_china):
        cid = next(iter(hand)) if hand else None
        if cid is None:
            return None
        return ActionEncoding(card_id=cid, mode=ActionMode.SPACE, targets=())

    _run_action_rounds(gs, _policy, _policy, make_rng(0), total_ars=1)

    italy_after = gs.pub.influence.get((Side.US, _ITALY), 0)
    assert italy_after == italy_before + 1


def test_norad_does_not_trigger_at_defcon3():
    """NORAD should NOT grant free influence when DEFCON > 2."""
    from tsrl.engine.game_loop import _run_action_rounds
    from tsrl.engine.game_state import reset
    from tsrl.schemas import ActionEncoding, ActionMode, Side

    _ITALY = 10

    gs = reset(seed=0)
    gs.pub.turn = 1
    gs.pub.defcon = 3
    gs.pub.norad_active = True
    gs.pub.influence = {k: v for k, v in gs.pub.influence.items() if k[0] != Side.US}
    gs.pub.influence[(Side.US, _ITALY)] = 2

    _USSR_CARD = 12
    _US_CARD   = 22
    gs.hands[Side.USSR] = frozenset({_USSR_CARD})
    gs.hands[Side.US]   = frozenset({_US_CARD})
    gs.ussr_holds_china = False
    gs.us_holds_china   = False

    italy_before = gs.pub.influence.get((Side.US, _ITALY), 0)

    def _policy(pub, hand, holds_china):
        cid = next(iter(hand)) if hand else None
        if cid is None:
            return None
        return ActionEncoding(card_id=cid, mode=ActionMode.SPACE, targets=())

    _run_action_rounds(gs, _policy, _policy, make_rng(0), total_ars=1)

    italy_after = gs.pub.influence.get((Side.US, _ITALY), 0)
    assert italy_after == italy_before   # no NORAD trigger at DEFCON 3


# ---------------------------------------------------------------------------
# Scoring card hold: enforced only at cleanup, NOT in legal_cards
# ---------------------------------------------------------------------------


def test_scoring_card_legal_on_any_ar():
    """A scoring card is always legal — legal_cards does not force its play early."""
    from tsrl.engine.legal_actions import legal_cards
    from tsrl.schemas import PublicState, Side

    pub = PublicState()
    pub.turn = 3
    pub.ar = 1   # early in the turn — not last AR
    hand = frozenset({1, 12})   # Asia Scoring + Romanian Abdication

    legal = legal_cards(hand, pub, Side.USSR)
    # Both cards legal; not restricted to just the scoring card.
    assert 1 in legal
    assert 12 in legal


def test_scoring_card_legal_on_last_ar_too():
    """Even on the last AR, legal_cards does NOT restrict to scoring cards only."""
    from tsrl.engine.legal_actions import legal_cards
    from tsrl.schemas import PublicState, Side

    pub = PublicState()
    pub.turn = 3
    pub.ar = 6   # last early-war AR
    hand = frozenset({1, 12})   # Asia Scoring + Romanian Abdication

    legal = legal_cards(hand, pub, Side.USSR)
    assert 1 in legal
    assert 12 in legal   # non-scoring card still legal


def test_vp_win_before_cleanup_with_held_scoring_card():
    """A VP win during an AR ends the game before cleanup; held scoring card is not penalised."""
    from tsrl.engine.game_loop import _end_of_turn
    from tsrl.engine.game_state import GameState, GamePhase
    from tsrl.schemas import PublicState, Side

    # Simulate: the game has already ended via VP win inside the AR loop.
    # _end_of_turn is never called in that path, so held scoring cards are irrelevant.
    # Here we verify _end_of_turn's scoring-hold check does NOT trigger when the
    # game's VP is already at win threshold — because in the real loop the game
    # would have ended before _end_of_turn ran.
    # (Indirect test: just confirm _end_of_turn fires the hold-loss at VP<20 but game
    # loop returns early before that when VP>=20.)
    from tsrl.engine.game_loop import _run_action_rounds
    from tsrl.engine.game_state import reset
    from tsrl.schemas import ActionEncoding, ActionMode

    gs = reset(seed=0)
    gs.pub.turn = 3
    gs.pub.ar = 6
    gs.pub.vp = 19    # one more VP and USSR wins
    # Give USSR a card whose event gives +1 VP (Nuclear Test Ban, card 34, ops 4, +1 VP)
    # and US a simple card. USSR holds Asia Scoring(1) too.
    _NTB = 34    # Nuclear Test Ban: USSR plays → DEFCON+1, VP+? — actually not +VP
    # Use VP_CHANGE path: just use a scoring card that in empty-board state gives +1 China bonus
    _ASIA = 1    # Asia Scoring: gives +1 VP (China bonus) when board is empty
    _US_CARD = 22
    gs.hands[Side.USSR] = frozenset({_ASIA})
    gs.hands[Side.US]   = frozenset({_US_CARD})
    gs.ussr_holds_china = True    # China bonus → +1 VP
    gs.us_holds_china = False

    def _ussr_policy(pub, hand, holds_china):
        return ActionEncoding(card_id=_ASIA, mode=ActionMode.EVENT, targets=())

    def _us_policy(pub, hand, holds_china):
        cid = next(iter(hand))
        return ActionEncoding(card_id=cid, mode=ActionMode.EVENT, targets=())

    result = _run_action_rounds(gs, _ussr_policy, _us_policy, __import__('random').Random(0), total_ars=1)
    # USSR should win via VP (19 + 1 China bonus = 20)
    assert result is not None


# ---------------------------------------------------------------------------
# Issue #1: Final scoring at Turn 10
# ---------------------------------------------------------------------------


def _make_turn10_gs(vp: int = 0, defcon: int = 3):
    """GameState positioned at end of Turn 10 (cleanup about to run)."""
    gs = reset(seed=42)
    gs.pub.turn = 10
    gs.pub.vp = vp
    gs.pub.defcon = defcon
    gs.pub.milops = [defcon, defcon]  # both sides meet MilOps so no penalty
    return gs


def test_final_scoring_fires_at_turn_10():
    """_end_of_turn on turn 10 must apply regional scoring to pub.vp.

    Board: USSR controls a single South America presence country.
    Expected: after final scoring, vp changes by at least 2 (SA Presence for USSR = +2).
    With no scoring, vp would stay at 0.
    """
    from tsrl.engine.game_loop import _end_of_turn
    from tsrl.engine.game_state import reset

    gs = _make_turn10_gs(vp=0)
    # USSR controls Venezuela (id=55, SA, BG, stab=2): influence=2 → controls it
    gs.pub.influence[(Side.USSR, 55)] = 2
    gs.pub.milops = [5, 5]  # no MilOps penalty

    vp_before = gs.pub.vp
    rng = make_rng(0)
    _end_of_turn(gs, rng, turn=10)

    # SA Presence for USSR = base 2 + 1 BG bonus. US has NONE (0).
    # vp_delta = +3 minimum. vp must have increased from 0.
    assert gs.pub.vp != vp_before, (
        "Final scoring at Turn 10 must change pub.vp; "
        f"vp was {vp_before} before and {gs.pub.vp} after — no change detected. "
        "_end_of_turn should apply final regional scoring here."
    )
    assert gs.pub.vp > vp_before, (
        f"USSR controls Venezuela (SA BG); vp should increase; got {gs.pub.vp}"
    )


def test_final_scoring_all_regions_scored():
    """Final scoring at T10 applies all 6 regions, not just one.

    Put USSR at Presence in every region. vp_delta should be at least
    sum-of-Presence-VPs = 2+3+3+1+2+1 = 12 (minus whatever US has).
    """
    from tsrl.engine.game_loop import _end_of_turn
    from tsrl.engine.game_state import reset

    gs = _make_turn10_gs(vp=0)
    # Give USSR one non-BG controlled country in each of the 6 main regions.
    # Benelux (1, Europe, stab=3, non-BG): influence=3
    # Afghanistan (20, Asia, stab=2, non-BG): influence=2
    # Lebanon (32, ME, stab=1, non-BG): influence=1
    # Haiti (40, CA, stab=1, non-BG): influence=1
    # Bolivia (47, SA, stab=2, non-BG): influence=2
    # Cameroon (59, Africa, stab=1, non-BG): influence=1
    for cid, inf in [(1, 3), (20, 2), (32, 1), (40, 1), (47, 2), (59, 1)]:
        gs.pub.influence[(Side.USSR, cid)] = inf
    gs.pub.milops = [5, 5]

    vp_before = gs.pub.vp
    _end_of_turn(gs, reset(seed=42).pub.__class__.__new__(reset(seed=42).pub.__class__)
                 .__class__.__new__ if False else make_rng(0),
                 turn=10)
    # USSR Presence in all 6: Europe(3)+Asia(3)+ME(3)+CA(1)+SA(2)+Africa(1) = 13 VP minimum
    assert gs.pub.vp >= vp_before + 10, (
        f"Expected vp to increase by ≥10 (6-region Presence); "
        f"before={vp_before}, after={gs.pub.vp}"
    )


def test_final_scoring_europe_control_ends_game():
    """At end of Turn 10, if a side controls Europe, _end_of_turn returns a GameResult win.

    USSR controls all 7 European battlegrounds + more total countries → CONTROL.
    """
    from tsrl.engine.game_loop import _end_of_turn
    from tsrl.etl.game_data import load_countries

    countries = load_countries()
    gs = _make_turn10_gs(vp=0)
    gs.pub.milops = [5, 5]

    # Give USSR control of all Europe battlegrounds.
    # Must clear US starting influence first (reset gives UK=5, WG=4, etc.),
    # then set USSR >= opp + stability.
    for cid, spec in countries.items():
        if spec.region == Region.EUROPE and spec.is_battleground:
            us_inf = gs.pub.influence.get((Side.US, cid), 0)
            gs.pub.influence.pop((Side.US, cid), None)
            gs.pub.influence[(Side.USSR, cid)] = us_inf + spec.stability + 1
    # Also give USSR a non-BG Europe presence for total-country dominance
    gs.pub.influence[(Side.USSR, 0)] = 1  # Austria (non-BG, stab=4)

    result = _end_of_turn(gs, make_rng(0), turn=10)

    assert result is not None, (
        "Europe Control at Turn 10 final scoring must return a GameResult win"
    )
    assert result.winner == Side.USSR, f"Expected USSR win, got {result.winner}"


def test_final_scoring_turn_10_does_not_emit_vp_threshold():
    """Turn-10 final scoring should flow into turn-limit resolution, not vp-threshold."""
    from tsrl.engine.game_loop import _end_of_turn

    gs = _make_turn10_gs(vp=19)
    gs.pub.milops = [5, 5]
    gs.pub.influence[(Side.USSR, 55)] = 2  # Venezuela -> SA Presence + BG

    result = _end_of_turn(gs, make_rng(0), turn=10)

    assert gs.pub.vp > 20, f"Expected final scoring to push VP above 20, got {gs.pub.vp}"
    assert result is None, (
        "Turn-10 final scoring without Europe Control should not produce an "
        "immediate vp-threshold result inside _end_of_turn."
    )


def test_end_reason_midgame_vp_threshold_is_not_europe_control():
    """Immediate wins at |VP| >= 20 are VP-threshold wins, not Europe Control."""
    from tsrl.engine.game_loop import _end_reason

    pub = PublicState(vp=20, defcon=3)

    assert _end_reason(pub, Side.USSR) == "vp_threshold"


def test_end_reason_europe_control_stays_distinct_from_vp_threshold():
    """Europe Control scoring wins can end the game without the VP track hitting ±20."""
    from tsrl.engine.game_loop import _end_reason

    pub = PublicState(vp=7, defcon=3)

    assert _end_reason(pub, Side.USSR) == "europe_control"


def test_final_scoring_se_asia_included_in_asia():
    """SE Asia countries count toward Asia Presence/Domination at Turn 10.

    Board: USSR controls only Vietnam (id=80, SE Asia, stab=1, non-BG) — no standard Asia.
    If SE Asia is included in final Asia scoring, USSR gets Asia Presence (+3).
    If SE Asia is excluded (bug), USSR gets NONE for Asia (0).
    """
    from tsrl.engine.game_loop import _end_of_turn
    from tsrl.engine.game_state import reset

    gs = _make_turn10_gs(vp=0)
    gs.pub.milops = [5, 5]
    # USSR controls only Vietnam (SE Asia non-BG)
    gs.pub.influence[(Side.USSR, 80)] = 1  # stab=1, so influence=1 controls it

    _end_of_turn(gs, make_rng(0), turn=10)

    # If SE Asia excluded: Asia contribution = 0, total VP from all regions ≈ 0.
    # If SE Asia included: Asia contribution = +3 (Presence).
    # The vp after final scoring must be > 0 to confirm SE Asia is counted.
    assert gs.pub.vp > 0, (
        f"SE Asia (Vietnam) should count toward Asia final scoring; "
        f"vp={gs.pub.vp} (expected > 0). SE Asia is not being included in Asia scoring."
    )


def test_final_scoring_china_card_bonus_in_asia():
    """Asia final scoring awards +1 VP to the China Card holder."""
    from tsrl.engine.game_loop import _end_of_turn

    gs = _make_turn10_gs(vp=0)
    gs.pub.milops = [5, 5]
    gs.pub.china_held_by = Side.USSR
    gs.pub.china_playable = True
    # USSR at Asia Presence (Afghanistan, non-BG, stab=2)
    gs.pub.influence[(Side.USSR, 20)] = 2

    _end_of_turn(gs, make_rng(0), turn=10)
    vp_with_china = gs.pub.vp

    gs2 = _make_turn10_gs(vp=0)
    gs2.pub.milops = [5, 5]
    gs2.pub.china_held_by = Side.US
    gs2.pub.china_playable = True
    gs2.pub.influence[(Side.USSR, 20)] = 2
    _end_of_turn(gs2, make_rng(0), turn=10)
    vp_us_holds_china = gs2.pub.vp

    assert vp_with_china == vp_us_holds_china + 2, (
        f"China Card: USSR holding should give +1 vs US holding (net +2 diff). "
        f"USSR holds: vp={vp_with_china}, US holds: vp={vp_us_holds_china}"
    )


def test_turn_10_scoring_card_held_loses_before_final_scoring():
    """Held scoring cards still lose on turn 10 because reveal happens before final scoring."""
    from tsrl.engine.game_loop import _end_of_turn
    from tsrl.etl.game_data import load_cards

    cards = load_cards()
    scoring_cid = next(cid for cid, spec in cards.items() if spec.is_scoring)

    gs = _make_turn10_gs(vp=0)
    gs.pub.milops = [5, 5]
    gs.pub.influence[(Side.USSR, 55)] = 2  # Would otherwise help USSR in final scoring.
    gs.hands[Side.USSR] = frozenset({scoring_cid})
    gs.hands[Side.US] = frozenset()

    result = _end_of_turn(gs, make_rng(0), turn=10)

    assert result is not None, "Expected held scoring card to end the game on turn 10"
    assert result.end_reason == "scoring_card_held"
    assert result.winner == Side.US


def test_north_sea_oil_extra_ar_fires():
    """North Sea Oil (89): US should take an extra AR after regular ARs complete.

    We use a 1-AR turn, give US two cards, and set north_sea_oil_extra_ar=True.
    The extra AR consumes the second card, so US hand should be empty after the
    full turn cycle (including the extra AR) but still have one card after the
    regular 1 AR.
    """
    from tsrl.engine.game_loop import _run_action_rounds, _run_extra_ar
    from tsrl.engine.game_state import reset, GamePhase

    _US_CARD_1 = 22   # Containment, 3 ops, no tricky event
    _US_CARD_2 = 28   # NATO, 4 ops

    gs = reset(seed=0)
    gs.pub.turn = 1
    gs.pub.defcon = 3
    gs.pub.north_sea_oil_extra_ar = True
    gs.hands[Side.USSR] = frozenset({12})   # give USSR 1 card
    gs.hands[Side.US]   = frozenset({_US_CARD_1, _US_CARD_2})
    gs.ussr_holds_china = False
    gs.us_holds_china   = False

    def _space_policy(pub, hand, holds_china):
        cid = min(hand) if hand else None
        if cid is None:
            return None
        return ActionEncoding(card_id=cid, mode=ActionMode.SPACE, targets=())

    # After 1 regular AR: US plays one card (lower id = _US_CARD_1)
    _run_action_rounds(gs, _space_policy, _space_policy, make_rng(0), total_ars=1)
    assert len(gs.hands[Side.US]) == 1, "US should have 1 card left after regular AR"

    # Fire the extra AR (mimicking what play_game does after _run_action_rounds)
    assert gs.pub.north_sea_oil_extra_ar is True  # flag survives regular ARs
    gs.pub.north_sea_oil_extra_ar = False  # caller clears flag before _run_extra_ar
    _run_extra_ar(gs, Side.US, _space_policy, make_rng(0))
    assert len(gs.hands[Side.US]) == 0, "US should have used both cards after extra AR"


def test_formosan_resolution_adds_taiwan_as_battleground():
    """Formosan Resolution promotes Taiwan into the Asia battleground pool."""
    from tsrl.engine.events import apply_event_card

    _AFGHANISTAN = 20
    _TAIWAN = 85

    pub = PublicState()
    pub.influence[(Side.US, _AFGHANISTAN)] = 2
    pub.influence[(Side.US, _TAIWAN)] = 3

    pub, _, _ = apply_event_card(pub, 35, Side.US, make_rng(0))
    result = score_region(Region.ASIA, pub)

    # US: Domination(7) + BG_bonus(1 for Taiwan) + adj_bonus(1 for Afghanistan adj USSR) = 9
    assert result.vp_delta == -9, (
        "With Formosan active, Taiwan counts as Asia BG; Afghanistan(non-BG) adj USSR adds +1."
    )


def test_formosan_inactive_taiwan_not_counted_as_battleground():
    """Without Formosan, Taiwan counts only as a normal Asia country."""
    _AFGHANISTAN = 20
    _TAIWAN = 85

    pub = PublicState()
    pub.influence[(Side.US, _AFGHANISTAN)] = 2
    pub.influence[(Side.US, _TAIWAN)] = 3

    result = score_region(Region.ASIA, pub)

    # US: Presence(3) + BG_bonus(0) + adj_bonus(1 for Afghanistan adj USSR) = 4
    assert result.vp_delta == -4, (
        "Without Formosan, Taiwan is not a BG; Afghanistan(non-BG) adj USSR adds +1 adj bonus."
    )


def _count_action_round_opportunities(*, ussr_space: int, us_space: int = 0, turn: int = 1):
    from tsrl.engine.game_loop import _run_action_rounds

    gs = reset(seed=0)
    gs.pub.turn = turn
    gs.pub.space[int(Side.USSR)] = ussr_space
    gs.pub.space[int(Side.US)] = us_space

    counts = {Side.USSR: 0, Side.US: 0}

    def _counting_policy(pub, hand, holds_china):
        counts[pub.phasing] += 1
        return None

    _run_action_rounds(
        gs,
        _counting_policy,
        _counting_policy,
        make_rng(0),
        total_ars=_ars_for_turn(turn),
    )
    return counts


def test_space_level_8_gives_8_ars_per_turn():
    counts = _count_action_round_opportunities(ussr_space=8)

    assert counts[Side.USSR] == 8
    assert counts[Side.US] == 6


def test_space_level_below_8_gives_normal_ars():
    counts = _count_action_round_opportunities(ussr_space=7)

    assert counts[Side.USSR] == 6
    assert counts[Side.US] == 6


# ---------------------------------------------------------------------------
# §5.2 opponent event firing on ops play
# ---------------------------------------------------------------------------


def test_ussr_event_fires_when_us_plays_ussr_card_for_ops():
    from tsrl.engine.game_loop import _apply_action_with_hands

    _ROMANIA = 13
    _FRANCE = 7
    _ROMANIAN_ABDICATION = 12

    gs = reset(seed=0)
    gs.pub = PublicState()
    gs.pub.phasing = Side.US
    gs.pub.influence[(Side.US, _ROMANIA)] = 2

    action = ActionEncoding(
        card_id=_ROMANIAN_ABDICATION,
        mode=ActionMode.INFLUENCE,
        targets=(_FRANCE,),
    )

    new_pub, over, winner = _apply_action_with_hands(gs, action, Side.US, make_rng(0))

    assert not over
    assert winner is None
    assert new_pub.influence.get((Side.US, _ROMANIA), 0) == 0
    assert new_pub.influence.get((Side.USSR, _ROMANIA), 0) > 0
    assert new_pub.influence.get((Side.US, _FRANCE), 0) == 1


def test_us_event_fires_when_ussr_plays_us_card_for_ops():
    from tsrl.engine.game_loop import _apply_action_with_hands

    _FRANCE = 7
    _DUCK_AND_COVER = 4

    gs = reset(seed=0)
    gs.pub = PublicState()
    gs.pub.phasing = Side.USSR
    gs.pub.defcon = 5

    action = ActionEncoding(
        card_id=_DUCK_AND_COVER,
        mode=ActionMode.INFLUENCE,
        targets=(_FRANCE,),
    )

    new_pub, over, winner = _apply_action_with_hands(gs, action, Side.USSR, make_rng(0))

    assert not over
    assert winner is None
    assert new_pub.defcon == 4
    assert new_pub.influence.get((Side.USSR, _FRANCE), 0) == 1


def test_game_over_propagates_if_opponent_event_ends_game():
    from tsrl.engine.game_loop import _apply_action_with_hands

    _FRANCE = 7
    _DUCK_AND_COVER = 4

    gs = reset(seed=0)
    gs.pub = PublicState()
    gs.pub.phasing = Side.USSR
    gs.pub.defcon = 2

    action = ActionEncoding(
        card_id=_DUCK_AND_COVER,
        mode=ActionMode.INFLUENCE,
        targets=(_FRANCE,),
    )

    new_pub, over, winner = _apply_action_with_hands(gs, action, Side.USSR, make_rng(0))

    assert over
    assert winner == Side.US
    assert new_pub.defcon == 1
    assert new_pub.influence.get((Side.USSR, _FRANCE), 0) == 0


def test_neutral_card_ops_does_not_fire_event():
    from tsrl.engine.game_loop import _apply_action_with_hands

    _FRANCE = 7
    _NUCLEAR_TEST_BAN = 34

    base_pub = PublicState()
    base_pub.phasing = Side.USSR
    base_pub.defcon = 3
    base_pub.vp = 4

    action = ActionEncoding(
        card_id=_NUCLEAR_TEST_BAN,
        mode=ActionMode.INFLUENCE,
        targets=(_FRANCE,),
    )

    expected_pub, expected_over, expected_winner = apply_action(
        base_pub,
        action,
        Side.USSR,
        rng=make_rng(0),
    )

    gs = reset(seed=0)
    gs.pub = base_pub
    actual_pub, actual_over, actual_winner = _apply_action_with_hands(
        gs,
        action,
        Side.USSR,
        make_rng(0),
    )

    assert actual_pub == expected_pub
    assert actual_over == expected_over
    assert actual_winner == expected_winner


def test_starred_card_in_removed_not_discard_after_ops_play():
    from tsrl.engine.game_loop import _apply_action_with_hands

    _ROMANIA = 13
    _FRANCE = 7
    _ROMANIAN_ABDICATION = 12

    gs = reset(seed=0)
    gs.pub = PublicState()
    gs.pub.phasing = Side.US
    gs.pub.influence[(Side.US, _ROMANIA)] = 2

    action = ActionEncoding(
        card_id=_ROMANIAN_ABDICATION,
        mode=ActionMode.INFLUENCE,
        targets=(_FRANCE,),
    )

    new_pub, over, winner = _apply_action_with_hands(gs, action, Side.US, make_rng(0))

    assert not over
    assert winner is None
    assert _ROMANIAN_ABDICATION in new_pub.removed
    assert _ROMANIAN_ABDICATION not in new_pub.discard


def test_space_level4_first_tracks_first_side():
    class FixedRNG:
        def integers(self, a, b):
            return 1

    action = ActionEncoding(card_id=22, mode=ActionMode.SPACE, targets=())

    pub = PublicState()
    pub.space[int(Side.USSR)] = 3
    new_pub, over, winner = apply_action(pub, action, Side.USSR, rng=FixedRNG())

    assert not over
    assert winner is None
    assert new_pub.space[int(Side.USSR)] == 4
    assert new_pub.space_level4_first == Side.USSR

    new_pub.space[int(Side.US)] = 3
    newer_pub, over, winner = apply_action(new_pub, action, Side.US, rng=FixedRNG())

    assert not over
    assert winner is None
    assert newer_pub.space[int(Side.US)] == 4
    assert newer_pub.space_level4_first == Side.USSR


def test_space_level6_discard_when_opponent_spaces():
    from tsrl.engine.game_loop import _apply_action_with_hands

    gs = reset(seed=0)
    gs.pub = PublicState()
    gs.pub.space[int(Side.USSR)] = 6
    gs.pub.space_level6_first = Side.USSR
    gs.hands[Side.USSR] = frozenset({5, 10})
    gs.hands[Side.US] = frozenset()

    action = ActionEncoding(card_id=22, mode=ActionMode.SPACE, targets=())
    new_pub, over, winner = _apply_action_with_hands(gs, action, Side.US, make_rng(0))

    assert not over
    assert winner is None
    assert gs.hands[Side.USSR] == frozenset({10})
    assert 5 in new_pub.discard


def test_space_level6_cancelled_when_both_reach_6():
    from tsrl.engine.game_loop import _apply_action_with_hands

    gs = reset(seed=0)
    gs.pub = PublicState()
    gs.pub.space[int(Side.USSR)] = 6
    gs.pub.space[int(Side.US)] = 6
    gs.pub.space_level6_first = Side.USSR
    gs.hands[Side.USSR] = frozenset({5, 10})
    gs.hands[Side.US] = frozenset()

    action = ActionEncoding(card_id=22, mode=ActionMode.SPACE, targets=())
    new_pub, over, winner = _apply_action_with_hands(gs, action, Side.US, make_rng(0))

    assert not over
    assert winner is None
    assert gs.hands[Side.USSR] == frozenset({5, 10})
    assert 5 not in new_pub.discard


def test_space_level4_peek_order():
    from tsrl.engine.game_loop import _run_headline_phase

    _USSR_CARD = 12
    _US_CARD = 21

    gs = reset(seed=0)
    gs.pub.turn = 1
    gs.pub.defcon = 5
    gs.pub.space[int(Side.USSR)] = 4
    gs.pub.space_level4_first = Side.USSR
    gs.hands[Side.USSR] = frozenset({_USSR_CARD})
    gs.hands[Side.US] = frozenset({_US_CARD})
    gs.ussr_holds_china = False
    gs.us_holds_china = False

    pick_order = []

    def _ussr_policy(pub, hand, holds_china):
        pick_order.append(Side.USSR)
        return ActionEncoding(card_id=_USSR_CARD, mode=ActionMode.EVENT, targets=())

    def _us_policy(pub, hand, holds_china):
        pick_order.append(Side.US)
        return ActionEncoding(card_id=_US_CARD, mode=ActionMode.EVENT, targets=())

    _run_headline_phase(gs, _ussr_policy, _us_policy, make_rng(0))

    assert pick_order == [Side.US, Side.USSR]
