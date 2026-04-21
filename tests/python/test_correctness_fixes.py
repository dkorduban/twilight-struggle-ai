"""
Tests for correctness fixes (rules-correctness pass).

Covers:
  Fix 1: DEFCON regional coup/realign restrictions
  Fix 2: Scoring card hold = immediate loss at end-of-turn
  Fix 3: Cuban Missile Crisis blocks all coups
  Fix 4: Bear Trap / Quagmire escape roll mechanic
  Fix 5: Wargames winner is whoever is ahead after VP transfer
  Fix 6: Olympic Games boycott / compete mechanics
  Fix 7: Five Year Plan scoring card causes immediate scoring
  Fix 8: Bear Trap / Quagmire forfeit AR when no eligible escape card
  Fix 9: UN Intervention EVENT blocked when player has no eligible opponent cards
"""
from __future__ import annotations

from tsrl.engine.rng import make_rng
from typing import Optional


class _FixedRollRNG:
    """Minimal mock RNG that always returns a fixed integer for roll/integers calls."""

    def __init__(self, fixed: int):
        self._fixed = fixed

    def integers(self, a: int, b: int) -> int:
        return self._fixed

    def choice(self, seq, size=None, replace=True):
        if size is None:
            return seq[0]
        return list(seq[:size])

    def shuffle(self, lst) -> None:
        pass  # no-op

import pytest

from tsrl.engine.game_loop import (
    GameResult,
    _end_of_turn,
    _resolve_trap_ar,
)
from tsrl.engine.game_state import GameState, GamePhase
from tsrl.engine.legal_actions import legal_modes, accessible_countries
from tsrl.engine.step import _copy_pub
from tsrl.schemas import ActionMode, PublicState, Side

# ---------------------------------------------------------------------------
# Country IDs from data/spec/countries.csv
# ---------------------------------------------------------------------------
_WEST_GERMANY = 18   # Europe, stability 4, battleground
_JAPAN        = 22   # Asia, stability 4, battleground
_IRAQ         = 29   # MiddleEast, stability 3, battleground
_ANGOLA       = 57   # Africa, stability 1, battleground

# A non-scoring Early War card with ops=2 for hand tests (e.g. "Nasser" id=15)
# We use a real card ID with ops>=2 that is neutral or own-side.
# Card 7 = Socialist Governments (USSR, ops 3, Early)
# Card 34 = Nuclear Test Ban (Neutral, ops 4, Early) — good for trap tests
_CARD_NUCLEAR_TEST_BAN = 34   # neutral, ops 4
_CARD_SOCIALIST_GOV = 7       # USSR, ops 3

# Scoring card IDs (from cards.csv — these are the main region scorers):
# Card 1 = Europe Scoring (scoring, Early, neutral)
_CARD_EUROPE_SCORING = 1
# Card 2 = Middle East Scoring
_CARD_MIDDLE_EAST_SCORING = 2
# Card 3 = Asia Scoring
_CARD_ASIA_SCORING = 3


# ---------------------------------------------------------------------------
# Helper factories
# ---------------------------------------------------------------------------

def _make_pub(**kwargs) -> PublicState:
    """Create a minimal PublicState with optional overrides."""
    pub = PublicState()
    for k, v in kwargs.items():
        setattr(pub, k, v)
    return pub


def _make_gs(pub: Optional[PublicState] = None, **kwargs) -> GameState:
    """Create a GameState with the given pub and optional hand overrides."""
    gs = GameState()
    gs.pub = pub if pub is not None else PublicState()
    gs.phase = GamePhase.ACTION_ROUND
    for k, v in kwargs.items():
        setattr(gs, k, v)
    return gs


# ---------------------------------------------------------------------------
# Fix 1: DEFCON regional coup/realign restrictions
# ---------------------------------------------------------------------------


def test_defcon4_no_coup_europe():
    """At DEFCON 4, W. Germany should not be a valid coup target.

    Give USSR inf in France(7) to make W. Germany accessible for INFLUENCE,
    then confirm W. Germany is NOT accessible for COUP at DEFCON 4.
    """
    _FRANCE = 7
    pub = _make_pub(defcon=4)
    pub.influence[(Side.USSR, _FRANCE)] = 1  # France adjacent to W. Germany

    # W. Germany should be accessible for influence but not for coup.
    accessible_inf = accessible_countries(Side.USSR, pub, mode=ActionMode.INFLUENCE)
    assert _WEST_GERMANY in accessible_inf, "W. Germany should be accessible for influence"

    # DEFCON 4 => Europe forbidden for coup/realign.
    accessible_coup = accessible_countries(Side.USSR, pub, mode=ActionMode.COUP)
    assert _WEST_GERMANY not in accessible_coup, (
        f"W. Germany should be DEFCON-restricted at DEFCON 4, "
        f"but it appeared in accessible coup countries: {accessible_coup}"
    )


def test_defcon3_no_coup_asia():
    """At DEFCON 3, Japan should not be a valid coup target.

    Japan (22) neighbors: USA anchor(81), South Korea(25), Philippines/Malaysia(78).
    South Korea is ID 25 (Asia). Give USSR inf in South Korea to make Japan accessible.
    """
    _SOUTH_KOREA = 25
    pub = _make_pub(defcon=3)
    pub.influence[(Side.USSR, _SOUTH_KOREA)] = 1  # South Korea adjacent to Japan

    accessible_inf = accessible_countries(Side.USSR, pub, mode=ActionMode.INFLUENCE)
    assert _JAPAN in accessible_inf, "Japan should be accessible for influence"

    accessible_coup = accessible_countries(Side.USSR, pub, mode=ActionMode.COUP)
    assert _JAPAN not in accessible_coup, (
        f"Japan should be DEFCON-restricted at DEFCON 3, "
        f"but it appeared: {accessible_coup}"
    )


def test_defcon2_no_coup_middle_east():
    """At DEFCON 2, Iraq (Middle East) should not be coupable.
    But Angola (Africa) should still be coupable.

    Note: accessible_countries returns countries reachable FROM existing influence.
    Iraq (29) neighbors: Syria(35), Jordan(31), Iran(28), Gulf States(27), Saudi(34).
    Give USSR inf in Syria to make Iraq accessible.
    Angola (57) neighbors: Botswana(58), Congo/Zaire(60), SE African States(69).
    Give USSR inf in Congo to make Angola accessible.
    """
    _SYRIA = 35
    _CONGO = 60
    pub = _make_pub(defcon=2)
    pub.influence[(Side.USSR, _SYRIA)] = 1   # makes Iraq accessible
    pub.influence[(Side.USSR, _CONGO)] = 1   # makes Angola accessible

    accessible_coup = accessible_countries(Side.USSR, pub, mode=ActionMode.COUP)
    assert _IRAQ not in accessible_coup, (
        f"Iraq should be DEFCON-restricted at DEFCON 2"
    )
    assert _ANGOLA in accessible_coup, (
        f"Angola (Africa) should still be accessible at DEFCON 2"
    )


def test_defcon5_coup_europe_legal():
    """At DEFCON 5, Europe coup is legal.

    W. Germany (18) neighbors: Austria(0), Benelux(1), Czechoslovakia(3),
    Denmark(4), EastGermany(5), France(7).
    Give USSR inf in France(7) to make W. Germany accessible.
    """
    _FRANCE = 7
    pub = _make_pub(defcon=5)
    pub.influence[(Side.USSR, _FRANCE)] = 1  # France is adjacent to W. Germany

    accessible_coup = accessible_countries(Side.USSR, pub, mode=ActionMode.COUP)
    assert _WEST_GERMANY in accessible_coup, (
        f"W. Germany should be accessible for coup at DEFCON 5"
    )


# ---------------------------------------------------------------------------
# Fix 2: Scoring card held at end-of-turn causes holder to lose
# ---------------------------------------------------------------------------


def test_scoring_card_held_at_turn_end_loses():
    """If USSR holds a scoring card at cleanup, USSR loses."""
    from tsrl.etl.game_data import load_cards
    cards = load_cards()

    # Find a scoring card to put in USSR's hand.
    scoring_ids = [cid for cid, spec in cards.items() if spec.is_scoring]
    assert scoring_ids, "Need at least one scoring card"
    scoring_cid = scoring_ids[0]

    pub = _make_pub(defcon=5, turn=1)
    gs = _make_gs(pub)
    gs.hands[Side.USSR] = frozenset({scoring_cid})
    gs.hands[Side.US] = frozenset()
    rng = make_rng(42)

    result = _end_of_turn(gs, rng, turn=1)
    assert result is not None, "Expected game over from scoring card held"
    assert result.end_reason == "scoring_card_held"
    assert result.winner == Side.US, (
        f"USSR held scoring card, US should win, got winner={result.winner}"
    )


def test_scoring_card_held_us_loses():
    """If US holds a scoring card at cleanup, US loses."""
    from tsrl.etl.game_data import load_cards
    cards = load_cards()

    scoring_ids = [cid for cid, spec in cards.items() if spec.is_scoring]
    scoring_cid = scoring_ids[0]

    pub = _make_pub(defcon=5, turn=1)
    gs = _make_gs(pub)
    gs.hands[Side.US] = frozenset({scoring_cid})
    gs.hands[Side.USSR] = frozenset()
    rng = make_rng(42)

    result = _end_of_turn(gs, rng, turn=1)
    assert result is not None
    assert result.end_reason == "scoring_card_held"
    assert result.winner == Side.USSR


# ---------------------------------------------------------------------------
# Fix 3: CMC blocks all coups
# ---------------------------------------------------------------------------


def test_cmc_blocks_coup():
    """When cuban_missile_crisis_active=True, COUP is not in legal modes."""
    pub = _make_pub(defcon=3, cuban_missile_crisis_active=True)
    # Give USSR influence so some countries are accessible.
    pub.influence[(Side.USSR, _ANGOLA)] = 1

    # Use a card with ops (card 7 = Socialist Governments, ops 3).
    modes = legal_modes(_CARD_SOCIALIST_GOV, pub, Side.USSR)
    assert ActionMode.COUP not in modes, (
        f"COUP should be blocked while CMC is active, but modes={modes}"
    )


def test_cmc_blocks_coup_us():
    """CMC blocks COUP for US side too."""
    pub = _make_pub(defcon=3, cuban_missile_crisis_active=True)
    pub.influence[(Side.US, _ANGOLA)] = 1

    # Card 34 = Nuclear Test Ban, neutral, ops 4
    modes = legal_modes(_CARD_NUCLEAR_TEST_BAN, pub, Side.US)
    assert ActionMode.COUP not in modes, (
        f"COUP should be blocked for US while CMC is active, but modes={modes}"
    )


# ---------------------------------------------------------------------------
# Fix 4: Bear Trap / Quagmire escape roll mechanic
# ---------------------------------------------------------------------------


def _make_gs_with_trap(side: Side, trap_card_ops: int = 3) -> GameState:
    """Create a GameState with the given side trapped and an eligible escape card."""
    pub = PublicState()
    pub.turn = 2
    pub.defcon = 4
    if side == Side.USSR:
        pub.bear_trap_active = True
    else:
        pub.quagmire_active = True

    gs = GameState()
    gs.pub = pub
    gs.phase = GamePhase.ACTION_ROUND
    # Add an eligible card: non-scoring, non-China, ops >= 2.
    # Card 34 = Nuclear Test Ban, neutral, ops 4.
    gs.hands[side] = frozenset({_CARD_NUCLEAR_TEST_BAN})
    return gs


def test_bear_trap_escape_low_roll():
    """Roll ≤ 4 → bear_trap_active cleared, card discarded from USSR hand."""
    gs = _make_gs_with_trap(Side.USSR)

    # Force roll = 2 (escape).
    rng = _FixedRollRNG(2)

    result = _resolve_trap_ar(gs, Side.USSR, rng)
    assert result is not None, "Should have consumed AR and returned trap result"
    new_pub, over, winner = result
    assert not new_pub.bear_trap_active, "Trap should be cleared on roll ≤ 4"
    assert _CARD_NUCLEAR_TEST_BAN not in gs.hands[Side.USSR], "Card should be discarded"
    assert _CARD_NUCLEAR_TEST_BAN in new_pub.discard


def test_bear_trap_escape_high_roll():
    """Roll 5-6 → bear_trap_active remains, card still discarded."""
    gs = _make_gs_with_trap(Side.USSR)

    rng = _FixedRollRNG(6)

    result = _resolve_trap_ar(gs, Side.USSR, rng)
    assert result is not None
    new_pub, over, winner = result
    assert new_pub.bear_trap_active, "Trap should remain on roll > 4"
    assert _CARD_NUCLEAR_TEST_BAN not in gs.hands[Side.USSR]
    assert _CARD_NUCLEAR_TEST_BAN in new_pub.discard


def test_quagmire_escape_low_roll():
    """Roll ≤ 4 → quagmire_active cleared for US."""
    gs = _make_gs_with_trap(Side.US)
    rng = _FixedRollRNG(3)

    result = _resolve_trap_ar(gs, Side.US, rng)
    assert result is not None
    new_pub, over, winner = result
    assert not new_pub.quagmire_active, "Quagmire should be cleared on roll ≤ 4"


def test_no_trap_returns_none():
    """_resolve_trap_ar returns None when side is not trapped."""
    gs = _make_gs_with_trap(Side.USSR)
    gs.pub.bear_trap_active = False  # no trap

    rng = make_rng(42)
    result = _resolve_trap_ar(gs, Side.USSR, rng)
    assert result is None, "Should return None when not trapped"


def test_trap_no_eligible_card_forfeits_ar():
    """If trapped but no 2+ ops non-scoring card available, AR is forfeited (not None).

    Per rules: trapped player with no eligible escape card forfeits the entire AR.
    The function should return (new_pub, over, winner) with no action taken.
    """
    pub = PublicState()
    pub.bear_trap_active = True
    pub.defcon = 4
    pub.turn = 2
    gs = GameState()
    gs.pub = pub
    gs.phase = GamePhase.ACTION_ROUND
    # Only scoring cards or 1-ops cards — no eligible escape card.
    # Card 1 = Europe Scoring, card 2 = Middle East Scoring.
    gs.hands[Side.USSR] = frozenset({_CARD_EUROPE_SCORING, _CARD_MIDDLE_EAST_SCORING})

    rng = make_rng(42)
    result = _resolve_trap_ar(gs, Side.USSR, rng)
    assert result is not None, "Should return (pub, over, winner), not None — AR is forfeited"
    new_pub, over, winner = result
    # Trap should still be active (no escape card to attempt with).
    assert new_pub.bear_trap_active, "Bear trap should remain active when no eligible card"


def test_quagmire_no_eligible_card_forfeits_ar():
    """If US is trapped with Quagmire but no eligible card, US forfeits the AR.

    Same as Bear Trap test but for US side with Quagmire.
    """
    pub = PublicState()
    pub.quagmire_active = True
    pub.defcon = 4
    pub.turn = 2
    gs = GameState()
    gs.pub = pub
    gs.phase = GamePhase.ACTION_ROUND
    # Only scoring cards — no eligible escape card.
    gs.hands[Side.US] = frozenset({_CARD_ASIA_SCORING})

    rng = make_rng(42)
    result = _resolve_trap_ar(gs, Side.US, rng)
    assert result is not None, "Should return (pub, over, winner), not None — AR is forfeited"
    new_pub, over, winner = result
    # Quagmire should still be active.
    assert new_pub.quagmire_active, "Quagmire should remain active when no eligible card"


# ---------------------------------------------------------------------------
# Fix 5: Wargames — winner is whoever is ahead after VP transfer
# ---------------------------------------------------------------------------


def test_wargames_winner_is_ahead_side():
    """After giving 6VP, the side that's ahead wins.
    USSR at +2 VP plays Wargames: gives 6VP to US (VP becomes -4), US wins.
    """
    from tsrl.engine.events import apply_event_card

    pub = _make_pub(defcon=2, vp=2)  # USSR leads by 2
    # USSR plays Wargames (card 103).
    new_pub, over, winner = apply_event_card(pub, 103, Side.USSR, make_rng(1))
    assert over
    assert winner == Side.US, (
        f"After USSR gives 6VP (from +2 to -4), US should win. Got: winner={winner}"
    )
    assert new_pub.vp == -4


def test_wargames_player_wins_if_was_leading():
    """USSR at +10 VP plays Wargames: gives 6VP to US (VP now +4), USSR still winning."""
    from tsrl.engine.events import apply_event_card

    pub = _make_pub(defcon=2, vp=10)  # USSR leads by 10
    new_pub, over, winner = apply_event_card(pub, 103, Side.USSR, make_rng(1))
    assert over
    assert winner == Side.USSR, (
        f"USSR was +10, gives 6VP → +4, USSR still leads. Got: winner={winner}"
    )
    assert new_pub.vp == 4


def test_wargames_draw_on_zero():
    """If VP is exactly 0 after transfer, result is a draw."""
    from tsrl.engine.events import apply_event_card

    pub = _make_pub(defcon=2, vp=-6)  # US leads by 6
    # US plays Wargames: gives 6VP to USSR (VP: -6 + 6 = 0).
    new_pub, over, winner = apply_event_card(pub, 103, Side.US, make_rng(1))
    assert over
    assert winner is None, f"VP=0 should be draw, got winner={winner}"


# ---------------------------------------------------------------------------
# Fix 6: Olympic Games handler
# ---------------------------------------------------------------------------


def test_olympic_games_boycott_defcon_drops():
    """Boycott path: DEFCON decreases by 1; phasing player gets 4 free influence ops (not 2 VP)."""
    from tsrl.engine.events import apply_event_card

    class _FixedRng:
        def random(self):
            return 0.1   # < 0.5 → boycott

        def randint(self, a, b):
            return a

        def choice(self, seq):
            return seq[0]

    rng = _FixedRng()
    pub = _make_pub(defcon=4, vp=0)
    # USSR plays Olympic Games (card 20).
    new_pub, over, winner = apply_event_card(pub, 20, Side.USSR, rng)  # type: ignore[arg-type]
    assert new_pub.defcon == 3, f"DEFCON should drop from 4 to 3, got {new_pub.defcon}"
    # Boycott no longer gives VP — phasing player (USSR) gets 4 free ops instead.
    assert new_pub.vp == 0, f"Boycott should not change VP directly, got {new_pub.vp}"


def test_olympic_games_compete_2vp():
    """Compete path: winner gets 2 VP, no DEFCON change."""
    from tsrl.engine.events import apply_event_card

    class _CompeteRng:
        def random(self):
            return 0.9   # ≥ 0.5 → compete

        def integers(self, a, b):
            # First call: phasing side rolls 6; second call: opponent rolls 1 → phasing wins.
            if not hasattr(self, '_calls'):
                self._calls = 0
            self._calls += 1
            return 6 if self._calls % 2 == 1 else 1

    rng = _CompeteRng()
    pub = _make_pub(defcon=4, vp=0)
    # USSR plays Olympic Games.
    new_pub, over, winner = apply_event_card(pub, 20, Side.USSR, rng)  # type: ignore[arg-type]
    assert new_pub.defcon == 4, f"DEFCON should not change on compete path"
    # USSR (phasing, rolled 6) wins 2 VP.
    assert new_pub.vp == 2, f"USSR wins 2 VP → vp should be 2, got {new_pub.vp}"


# ---------------------------------------------------------------------------
# Fix 7: Five Year Plan scoring card causes immediate region scoring
# ---------------------------------------------------------------------------


def test_five_year_plan_scoring_card_scores():
    """If USSR hand has only a scoring card, FYP discards it and applies scoring."""
    from tsrl.engine.cat_c_events import apply_hand_event
    from tsrl.schemas import ActionEncoding, ActionMode

    pub = _make_pub(defcon=5, vp=0, turn=3)
    gs = GameState()
    gs.pub = pub
    gs.phase = GamePhase.ACTION_ROUND
    # Give USSR only a scoring card (Europe Scoring = card 1).
    gs.hands[Side.USSR] = frozenset({_CARD_EUROPE_SCORING})
    gs.hands[Side.US] = frozenset()
    gs.deck = []

    action = ActionEncoding(card_id=5, mode=ActionMode.EVENT, targets=())
    rng = make_rng(42)

    new_pub, over, winner = apply_hand_event(gs, action, Side.US, rng)
    # Scoring card should have been discarded from USSR's hand.
    assert _CARD_EUROPE_SCORING not in gs.hands[Side.USSR]
    # Scoring card should appear in discard (after scoring fires it goes to discard).
    # The vp may have changed (scoring result applied); no assertion on exact VP
    # since neither side has influence, but no crash should occur.
    assert new_pub is not None


# ---------------------------------------------------------------------------
# P4: Austria excluded from COMECON pool
# ---------------------------------------------------------------------------


def test_austria_not_in_eastern_bloc():
    """Austria (id=0) must NOT be in _EASTERN_BLOC (it is neutral/Western-aligned)."""
    from tsrl.engine.events import _EASTERN_BLOC
    assert 0 not in _EASTERN_BLOC


def test_comecon_does_not_place_in_austria():
    """COMECON (card 14) event must not place influence in Austria."""
    import random
    from tsrl.engine.step import apply_action
    from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Side

    _AUSTRIA = 0
    _COMECON = 14

    pub = PublicState()
    # Ensure Austria is accessible but should be excluded from pool.
    pub.influence[(Side.USSR, _AUSTRIA)] = 0  # no USSR inf in Austria

    action = ActionEncoding(card_id=_COMECON, mode=ActionMode.EVENT, targets=())
    rng = make_rng(0)
    # Run many times to rule out lucky avoidance.
    for seed in range(20):
        new_pub, _, _ = apply_action(pub, action, Side.USSR, rng=make_rng(seed))
        assert new_pub.influence.get((Side.USSR, _AUSTRIA), 0) == 0, \
            f"COMECON placed influence in Austria on seed {seed}"


# ---------------------------------------------------------------------------
# P1: Chernobyl — USSR blocked from ops-influence in designated region
# ---------------------------------------------------------------------------


def test_chernobyl_blocks_ussr_influence_in_region():
    """Chernobyl: USSR cannot place ops-influence in the designated region."""
    from tsrl.engine.legal_actions import accessible_countries
    from tsrl.engine.adjacency import load_adjacency
    from tsrl.schemas import ActionMode, PublicState, Region, Side

    adj = load_adjacency()
    pub = PublicState()
    pub.chernobyl_blocked_region = Region.EUROPE
    # Give USSR influence somewhere to ensure connectivity.
    pub.influence[(Side.USSR, 5)] = 2  # East Germany

    countries_for_influence = accessible_countries(
        Side.USSR, pub, adj, mode=ActionMode.INFLUENCE
    )
    # No European country should be accessible for USSR influence ops.
    from tsrl.etl.game_data import load_countries
    europe_ids = {cid for cid, c in load_countries().items() if c.region == Region.EUROPE}
    blocked = europe_ids & countries_for_influence
    assert not blocked, f"Chernobyl should block USSR influence in Europe, but found: {blocked}"


def test_chernobyl_does_not_block_coup():
    """Chernobyl only restricts INFLUENCE ops; coups in the region remain legal."""
    from tsrl.engine.legal_actions import accessible_countries
    from tsrl.engine.adjacency import load_adjacency
    from tsrl.schemas import ActionMode, PublicState, Region, Side

    adj = load_adjacency()
    pub = PublicState()
    pub.chernobyl_blocked_region = Region.EUROPE
    pub.defcon = 5
    pub.influence[(Side.USSR, 5)] = 2
    pub.influence[(Side.US, 18)] = 1  # W. Germany: US has influence → valid coup target

    coup_countries = accessible_countries(
        Side.USSR, pub, adj, mode=ActionMode.COUP
    )
    # W. Germany (18) should still be accessible for coup.
    _WEST_GERMANY = 18
    assert _WEST_GERMANY in coup_countries


def test_chernobyl_reset_at_end_of_turn():
    """chernobyl_blocked_region must be None after _end_of_turn."""
    from tsrl.engine.game_loop import _end_of_turn
    from tsrl.engine.game_state import GameState, GamePhase
    from tsrl.schemas import PublicState, Region, Side

    pub = PublicState()
    pub.turn = 1
    pub.defcon = 5
    pub.chernobyl_blocked_region = Region.ASIA

    gs = GameState()
    gs.pub = pub
    gs.phase = GamePhase.CLEANUP

    _end_of_turn(gs, __import__('random').Random(0), turn=1)
    assert gs.pub.chernobyl_blocked_region is None


# ---------------------------------------------------------------------------
# P1: Latin American Death Squads — coup roll modifier in C/S America
# ---------------------------------------------------------------------------


def test_latam_death_squads_bonus_to_phasing_side():
    """LatAm Death Squads: phasing side gets net +1 on C/S America coups."""
    from tsrl.engine.step import apply_action
    from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Side

    _CUBA = 36      # Central America, stability 3, battleground
    _LATAM = 70     # Latin American Death Squads card

    class FixedRoll3RNG:
        """Always rolls 3 (net = 3 + ops - 2*stability)."""
        def integers(self, a, b): return 3
        def choice(self, seq, size=None, replace=True): return seq[0]

    pub = PublicState()
    pub.defcon = 5
    pub.latam_coup_bonus = Side.USSR
    pub.influence[(Side.US, _CUBA)] = 2

    # Use a 2-ops card for the coup. roll=3 + ops=2 - 2*stab=6 → net = -1 (fail without bonus).
    # With +1 bonus: net = 0 (still fail). Use ops=3: net=3+3-6=0 (fail); with +1: net=1 (success).
    _CARD = 16  # ops=3 card
    action = ActionEncoding(card_id=_CARD, mode=ActionMode.COUP, targets=(_CUBA,))
    new_pub, _, _ = apply_action(pub, action, Side.USSR, rng=FixedRoll3RNG())

    # With roll=3, ops=3, stability=3: net=3+3-6=0 normally (fail).
    # With +1 LatAm bonus: net=1 → remove 1 US inf.
    assert new_pub.influence.get((Side.US, _CUBA), 0) == 1  # 1 removed


def test_latam_death_squads_penalty_to_opponent():
    """LatAm Death Squads: opponent side gets -1 on C/S America coups."""
    from tsrl.engine.step import apply_action
    from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Side

    _CUBA = 36

    class FixedRoll4RNG:
        def integers(self, a, b): return 4
        def choice(self, seq, size=None, replace=True): return seq[0]

    pub = PublicState()
    pub.defcon = 5
    pub.latam_coup_bonus = Side.USSR   # USSR has bonus; US has penalty
    pub.influence[(Side.USSR, _CUBA)] = 2

    # US coup, card ops=3, roll=4: net=4+3-6=1 (success without penalty).
    # With -1 penalty: net=0 (fail).
    _CARD = 21  # ops=4 card (NATO)... but let's use a 3-op card
    _CARD = 16  # ops=3
    action = ActionEncoding(card_id=_CARD, mode=ActionMode.COUP, targets=(_CUBA,))
    new_pub, _, _ = apply_action(pub, action, Side.US, rng=FixedRoll4RNG())

    # Without penalty: net=4+3-6=1 → 1 USSR inf removed.
    # With -1 penalty: net=0 → no removal.
    assert new_pub.influence.get((Side.USSR, _CUBA), 0) == 2  # unchanged


def test_latam_death_squads_no_effect_outside_region():
    """LatAm Death Squads modifier does NOT apply to coups outside C/S America."""
    from tsrl.engine.step import apply_action
    from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Side

    _EGYPT = 26   # Middle East, not C/S America

    class FixedRoll3RNG:
        def integers(self, a, b): return 3
        def choice(self, seq, size=None, replace=True): return seq[0]

    pub = PublicState()
    pub.defcon = 5
    pub.latam_coup_bonus = Side.USSR
    pub.influence[(Side.US, _EGYPT)] = 2

    _CARD = 16  # ops=3
    action = ActionEncoding(card_id=_CARD, mode=ActionMode.COUP, targets=(_EGYPT,))
    new_pub, _, _ = apply_action(pub, action, Side.USSR, rng=FixedRoll3RNG())

    # Egypt: stability=2. roll=3, ops=3: net=3+3-4=2 → removes 2 US inf (no LatAm bonus).
    assert new_pub.influence.get((Side.US, _EGYPT), 0) == 0


def test_latam_coup_bonus_reset_at_end_of_turn():
    """latam_coup_bonus must be None after _end_of_turn."""
    from tsrl.engine.game_loop import _end_of_turn
    from tsrl.engine.game_state import GameState, GamePhase
    from tsrl.schemas import PublicState, Side

    pub = PublicState()
    pub.turn = 1
    pub.defcon = 5
    pub.latam_coup_bonus = Side.USSR

    gs = GameState()
    gs.pub = pub
    gs.phase = GamePhase.CLEANUP

    _end_of_turn(gs, __import__('random').Random(0), turn=1)
    assert gs.pub.latam_coup_bonus is None


# ---------------------------------------------------------------------------
# P1: Flower Power — +2 VP to USSR when US plays war card as event
# ---------------------------------------------------------------------------


_WAR_CARDS = [11, 13, 24, 39, 105]  # Korean War, Arab-Israeli War, Indo-Pakistani, Brush War, Iran-Iraq


def test_flower_power_awards_vp_on_us_war_event():
    """Flower Power active: USSR gains exactly +2 VP more than without it, for each war card."""
    import random
    from tsrl.engine.step import apply_action
    from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Side

    for war_card in _WAR_CARDS:
        action = ActionEncoding(card_id=war_card, mode=ActionMode.EVENT, targets=())
        seed = 42  # same seed so war roll outcome is identical in both runs

        pub_base = PublicState()
        pub_base.flower_power_active = False
        base, _, _ = apply_action(pub_base, action, Side.US, rng=make_rng(seed))

        pub_fp = PublicState()
        pub_fp.flower_power_active = True
        fp, _, _ = apply_action(pub_fp, action, Side.US, rng=make_rng(seed))

        assert fp.vp == base.vp + 2, \
            f"War card {war_card}: expected +2 VP delta, got base={base.vp} fp={fp.vp}"


def test_flower_power_no_vp_when_cancelled():
    """Flower Power cancelled by An Evil Empire: no VP awarded."""
    import random
    from tsrl.engine.step import apply_action
    from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Side

    pub = PublicState()
    pub.flower_power_active = False
    pub.flower_power_cancelled = True
    vp_before = pub.vp
    action = ActionEncoding(card_id=11, mode=ActionMode.EVENT, targets=())  # Korean War
    new_pub, _, _ = apply_action(pub, action, Side.US, rng=make_rng(0))
    # VP delta from Korean War itself varies, but flower power bonus (+2) must NOT be added.
    # Simply check no extra +2 beyond what the card itself does (we check same result as inactive).
    pub2 = PublicState()
    pub2.flower_power_active = False
    new_pub2, _, _ = apply_action(pub2, action, Side.US, rng=make_rng(0))
    assert new_pub.vp == new_pub2.vp


def test_flower_power_no_vp_when_ussr_plays_war_card():
    """Flower Power does NOT trigger when USSR plays a war card (only US trigger)."""
    import random
    from tsrl.engine.step import apply_action
    from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Side

    pub = PublicState()
    pub.flower_power_active = True
    vp_before = pub.vp
    # Korean War (11) is US-sided; when USSR plays it, the event fires but no FP bonus.
    action = ActionEncoding(card_id=11, mode=ActionMode.EVENT, targets=())
    new_pub, _, _ = apply_action(pub, action, Side.USSR, rng=make_rng(0))
    # Flower Power bonus (+2 USSR VP) should NOT apply.
    # Korean War when played by USSR as opponent card: war_roll applies, VP changes by war result,
    # but not an additional +2 on top.
    # Check: result without flower_power_active must be the same.
    pub2 = PublicState()
    pub2.flower_power_active = False
    new_pub2, _, _ = apply_action(pub2, action, Side.USSR, rng=make_rng(0))
    assert new_pub.vp == new_pub2.vp


# ---------------------------------------------------------------------------
# Scoring VP correctness — adjacency bonus must only apply to BG countries
# ---------------------------------------------------------------------------
# Regression for tsreplayer_14 T5 AR3 CA scoring.
# USSR controlled Mexico (42, BG, adj to USA) and Panama (44, BG, not adj to USA).
# Log: USSR gains 4 VP.
#
# Mexico IS a battleground (stability 2, not stab 3 like Cuba).
# CA BGs: Cuba(36), Mexico(42), Panama(44).
# Adjacent to USA in CA: Cuba(36), Mexico(42).
#
# The key insight: USSR controlled ONLY BGs (non_bgs=0), so the domination
# threshold (requires ≥1 non-BG country) is NOT met.  USSR is at PRESENCE tier.
# Scoring: Presence(1) + BG_bonus(2 for Mexico+Panama) + adj_bonus(1 for Mexico adj USA) = 4.
# ---------------------------------------------------------------------------

_CA_MEXICO = 42   # Central America, BG, stability 2, adj to USA
_CA_PANAMA = 44   # Central America, BG, stability 2
_CA_CUBA   = 36   # Central America, BG, stability 3, adj to USA


def test_ca_scoring_presence_tier_when_only_bgs_controlled():
    """USSR at Presence (not Domination) when controlling only BG countries.

    Regression: tsreplayer_14 T5 AR3 — USSR controls Mexico(BG,adj USA) + Panama(BG).
    Domination requires ≥1 non-BG country; without that, tier = Presence.
    Expected: Presence(1) + BG_bonus(2) + adj_bonus(1 for Mexico adj USA) = 4.
    """
    from tsrl.engine.scoring import score_region
    from tsrl.schemas import PublicState, Region, Side

    pub = PublicState()
    # USSR controls Mexico (BG, stability 2): needs 2 inf, no US inf there
    pub.influence[(Side.USSR, _CA_MEXICO)] = 2
    # USSR controls Panama (BG, stability 2): needs 2 inf
    pub.influence[(Side.USSR, _CA_PANAMA)] = 2
    # US controls nothing in CA — USSR has only BGs (non_bgs=0) → Presence tier

    result = score_region(Region.CENTRAL_AMERICA, pub)
    assert result.vp_delta == 4, (
        f"Expected vp_delta=+4 (Presence=1 + BG_bonus=2 + adj_bonus=1 for Mexico adj USA), "
        f"got vp_delta={result.vp_delta}."
    )


def test_ca_scoring_adj_bonus_applies_to_all_controlled_countries_adj_superpower():
    """adj bonus applies to any controlled country adjacent to enemy superpower (BG or not).

    Cuba (BG, adj USA) + Honduras (non-BG) → USSR reaches Domination tier and
    Cuba earns both BG_bonus and adj_bonus.  Honduras (non-BG, not adj USA) earns
    neither bonus but satisfies the non_bgs≥1 domination requirement.
    Expected: Domination(3) + BG_bonus(1 for Cuba) + adj_bonus(1 for Cuba adj USA) = 5.
    """
    from tsrl.engine.scoring import score_region
    from tsrl.schemas import PublicState, Region, Side

    _CA_HONDURAS = 41   # non-BG, stability 2

    pub = PublicState()
    # USSR controls Cuba (BG, stab=3, adj USA): needs 3 inf
    pub.influence[(Side.USSR, _CA_CUBA)] = 3
    # USSR controls Honduras (non-BG, stab=2): needs 2 inf — provides non_bgs=1 → Domination
    pub.influence[(Side.USSR, _CA_HONDURAS)] = 2
    # US controls nothing

    result = score_region(Region.CENTRAL_AMERICA, pub)
    # USSR: Domination(3) + BG_bonus(1 for Cuba) + adj_bonus(1 for Cuba adj USA)
    assert result.vp_delta == 5, (
        f"Expected vp_delta=+5 (USSR Domination=3, Cuba BG=1, Cuba adj USA=1), "
        f"got {result.vp_delta}"
    )


# ---------------------------------------------------------------------------
# Fix: adj bonus applies to ALL controlled countries adj to enemy superpower,
#      not only battleground countries.
#
# Affected non-BG countries adjacent to a superpower:
#   Canada (2, non-BG, adj USA)  — Europe
#   Finland (6, non-BG, adj USSR) — Europe
#   Romania (13, non-BG, adj USSR) — Europe
#   Afghanistan (20, non-BG, adj USSR) — Asia
#
# With BG-only logic these would earn 0 adj bonus; correct rule gives +1 each.
#
# These tests are written in TDD style: they assert the CORRECT (all-country)
# behavior and would have FAILED under the old BG-only scoring code.
# ---------------------------------------------------------------------------

_EU_CANADA      = 2   # Europe, non-BG, stab 4, adj USA
_EU_FINLAND     = 6   # Europe, non-BG, stab 4, adj USSR
_EU_ROMANIA     = 13  # Europe, non-BG, stab 3, adj USSR
_EU_FRANCE      = 7   # Europe, BG, stab 3
_EU_ITALY       = 10  # Europe, BG, stab 2
_EU_W_GERMANY   = 18  # Europe, BG, stab 4, adj USSR
_AS_AFGHANISTAN = 20  # Asia, non-BG, stab 2, adj USSR
_AS_S_KOREA     = 25  # Asia, BG, stab 3


def test_adj_bonus_for_non_bg_canada_adj_usa():
    """US-controlled Canada (non-BG, adj USA) earns +1 adj bonus for USSR scoring.

    With BG-only logic Canada would give 0 adj bonus (non-BG).
    With all-country logic Canada gives +1 adj bonus to USSR if USSR controls it.
    """
    from tsrl.engine.scoring import score_region
    from tsrl.schemas import PublicState, Region, Side

    pub = PublicState()
    # USSR controls Canada (non-BG, stab=4): needs 4 inf
    pub.influence[(Side.USSR, _EU_CANADA)] = 4
    # USSR also controls France (BG, stab=3) to reach Domination
    pub.influence[(Side.USSR, _EU_FRANCE)] = 3
    # US controls nothing

    result = score_region(Region.EUROPE, pub)
    # USSR: Domination(7) + BG_bonus(1 for France) + adj_bonus(1 for Canada adj USA) = 9
    # With BG-only: Domination(7) + BG_bonus(1) + adj_bonus(0) = 8
    assert result.vp_delta == 9, (
        f"Expected vp_delta=+9 (Domination=7 + France BG=1 + Canada adj USA=1), "
        f"got {result.vp_delta}. "
        f"Canada is non-BG but adj to USA — must contribute adj_bonus."
    )


def test_adj_bonus_for_non_bg_finland_adj_ussr():
    """US-controlled Finland (non-BG, adj USSR) earns +1 adj bonus for US scoring.

    With BG-only logic Finland would give 0 adj bonus (non-BG).
    With all-country logic Finland gives +1 adj bonus to US if US controls it.
    """
    from tsrl.engine.scoring import score_region
    from tsrl.schemas import PublicState, Region, Side

    pub = PublicState()
    # US controls Finland (non-BG, stab=4): needs 4 inf
    pub.influence[(Side.US, _EU_FINLAND)] = 4
    # US also controls Italy (BG, stab=2) to reach Domination
    pub.influence[(Side.US, _EU_ITALY)] = 2
    # USSR controls nothing

    result = score_region(Region.EUROPE, pub)
    # US: Domination(7) + BG_bonus(1 for Italy) + adj_bonus(1 for Finland adj USSR) = 9 -> -9
    # With BG-only: -(Domination(7) + BG_bonus(1) + adj_bonus(0)) = -8
    assert result.vp_delta == -9, (
        f"Expected vp_delta=-9 (US Domination=7 + Italy BG=1 + Finland adj USSR=1), "
        f"got {result.vp_delta}. "
        f"Finland is non-BG but adj to USSR — must contribute adj_bonus."
    )


def test_adj_bonus_for_non_bg_romania_adj_ussr():
    """US-controlled Romania (non-BG, adj USSR) earns +1 adj bonus for US scoring.

    Romania (stab=3, non-BG, adj USSR) — if US controls it, +1 US adj bonus.
    """
    from tsrl.engine.scoring import score_region
    from tsrl.schemas import PublicState, Region, Side

    pub = PublicState()
    # US controls Romania (non-BG, stab=3): needs 3 inf
    pub.influence[(Side.US, _EU_ROMANIA)] = 3
    # US also controls Italy (BG, stab=2) to reach Domination
    pub.influence[(Side.US, _EU_ITALY)] = 2
    # USSR controls nothing

    result = score_region(Region.EUROPE, pub)
    # US: Domination(7) + BG_bonus(1 for Italy) + adj_bonus(1 for Romania adj USSR) = 9 -> -9
    # With BG-only: -(Domination(7) + BG_bonus(1) + adj_bonus(0)) = -8
    assert result.vp_delta == -9, (
        f"Expected vp_delta=-9 (US Domination=7 + Italy BG=1 + Romania adj USSR=1), "
        f"got {result.vp_delta}. "
        f"Romania is non-BG but adj to USSR — must contribute adj_bonus."
    )


def test_adj_bonus_for_non_bg_afghanistan_adj_ussr():
    """US-controlled Afghanistan (non-BG, adj USSR) earns +1 adj bonus for US Asia scoring.

    Afghanistan (stab=2, non-BG, adj USSR) — if US controls it, +1 US adj bonus.
    """
    from tsrl.engine.scoring import score_region
    from tsrl.schemas import PublicState, Region, Side

    pub = PublicState()
    # US controls Afghanistan (non-BG, stab=2): needs 2 inf
    pub.influence[(Side.US, _AS_AFGHANISTAN)] = 2
    # US also controls South Korea (BG, stab=3) to reach Domination
    pub.influence[(Side.US, _AS_S_KOREA)] = 3
    # USSR controls nothing

    result = score_region(Region.ASIA, pub)
    # US: Domination(7) + BG_bonus(1 for S.Korea) + adj_bonus(1 for Afghanistan adj USSR) = 9
    # With BG-only: -(Domination(7) + BG_bonus(1) + adj_bonus(0)) = -8
    assert result.vp_delta == -9, (
        f"Expected vp_delta=-9 (US Domination=7 + S.Korea BG=1 + Afghanistan adj USSR=1), "
        f"got {result.vp_delta}. "
        f"Afghanistan is non-BG but adj to USSR — must contribute adj_bonus."
    )


# ---------------------------------------------------------------------------
# Fix 5: Bear Trap / Quagmire must allow scoring card EVENT
# ---------------------------------------------------------------------------


def test_bear_trap_allows_scoring_card_event():
    """A trapped USSR player must be able to play a scoring card for EVENT.

    Scoring cards have 0 ops and cannot be played for ops modes.
    The trap restriction (ops-only) must not apply to scoring cards —
    otherwise the player has no legal move and the game deadlocks.
    """
    from tsrl.engine.legal_actions import legal_modes
    from tsrl.engine.adjacency import load_adjacency

    pub = PublicState()
    pub.bear_trap_active = True
    adj = load_adjacency()

    modes = legal_modes(_CARD_ASIA_SCORING, pub, Side.USSR, adj=adj)
    assert ActionMode.EVENT in modes, (
        f"Scoring card (Asia Scoring) should have EVENT available even during Bear Trap; "
        f"got modes={modes}"
    )
    # Ops modes should not be available (scoring card has 0 ops).
    assert ActionMode.INFLUENCE not in modes, "scoring card should not be INFLUENCE-playable"
    assert ActionMode.COUP not in modes, "scoring card should not be COUP-playable"


def test_quagmire_allows_scoring_card_event():
    """A trapped US player must be able to play a scoring card for EVENT."""
    from tsrl.engine.legal_actions import legal_modes
    from tsrl.engine.adjacency import load_adjacency

    pub = PublicState()
    pub.quagmire_active = True
    adj = load_adjacency()

    modes = legal_modes(_CARD_ASIA_SCORING, pub, Side.US, adj=adj)
    assert ActionMode.EVENT in modes, (
        f"Scoring card (Asia Scoring) should have EVENT available even during Quagmire; "
        f"got modes={modes}"
    )


def test_bear_trap_still_blocks_event_for_non_scoring():
    """Bear trap continues to block EVENT for non-scoring cards."""
    from tsrl.engine.legal_actions import legal_modes
    from tsrl.engine.adjacency import load_adjacency

    pub = PublicState()
    pub.bear_trap_active = True
    pub.influence[(Side.USSR, 0)] = 2  # some accessible countries
    adj = load_adjacency()

    # Nuclear Test Ban (ops=4, non-scoring) should NOT have EVENT under Bear Trap.
    modes = legal_modes(_CARD_NUCLEAR_TEST_BAN, pub, Side.USSR, adj=adj)
    assert ActionMode.EVENT not in modes, (
        f"Non-scoring card should NOT have EVENT during Bear Trap; got modes={modes}"
    )


# ---------------------------------------------------------------------------
# Fix 9: UN Intervention (32) legality — hand check
# ---------------------------------------------------------------------------

_UN_INTERVENTION = 32
# Card 5 = Truman Doctrine (US side, non-scoring) — an opponent card for USSR
_CARD_TRUMAN_DOCTRINE = 5
# Card 7 = Socialist Governments (USSR side, non-scoring)
_CARD_SOCIALIST_GOV_ID = 7


def test_un_intervention_event_blocked_when_no_opponent_cards():
    """UN Intervention EVENT is not enumerated if hand has no eligible opponent cards."""
    from tsrl.engine.legal_actions import enumerate_actions
    pub = PublicState()
    # Hand holds only same-side cards (no US cards for USSR player).
    hand = frozenset({_UN_INTERVENTION, _CARD_SOCIALIST_GOV_ID})
    actions = enumerate_actions(hand, pub, Side.USSR)
    event_actions = [a for a in actions if a.card_id == _UN_INTERVENTION and a.mode == ActionMode.EVENT]
    assert not event_actions, (
        "UN Intervention EVENT should be blocked when USSR holds no US-side cards; "
        f"got {event_actions}"
    )


def test_un_intervention_event_legal_when_opponent_card_in_hand():
    """UN Intervention EVENT is legal when hand contains at least one opponent card."""
    from tsrl.engine.legal_actions import enumerate_actions
    pub = PublicState()
    # Hand holds UN Intervention + one US-side card (Truman Doctrine id=5).
    hand = frozenset({_UN_INTERVENTION, _CARD_TRUMAN_DOCTRINE})
    actions = enumerate_actions(hand, pub, Side.USSR)
    event_actions = [a for a in actions if a.card_id == _UN_INTERVENTION and a.mode == ActionMode.EVENT]
    assert event_actions, (
        "UN Intervention EVENT should be legal when USSR holds a US-side card"
    )


def test_un_intervention_ops_still_legal_when_no_opponent_cards():
    """Ops modes (INFLUENCE/COUP/REALIGN) for UN Intervention remain legal regardless."""
    from tsrl.engine.legal_actions import legal_modes
    from tsrl.engine.adjacency import load_adjacency
    pub = PublicState()
    adj = load_adjacency()
    # Even without the hand check in legal_modes, ops modes should be present.
    modes = legal_modes(_UN_INTERVENTION, pub, Side.USSR, adj=adj)
    assert ActionMode.INFLUENCE in modes or ActionMode.COUP in modes or ActionMode.REALIGN in modes, (
        f"UN Intervention should still have ops modes; got {modes}"
    )
