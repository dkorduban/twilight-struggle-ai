"""
Tests for the MilOps end-of-turn VP penalty in game_loop._end_of_turn.

Rules: At end of turn, if a side's milops < current DEFCON level, that side
suffers a VP penalty equal to the shortfall.
  - USSR shortfall → US gains VP (pub.vp decreases).
  - US shortfall → USSR gains VP (pub.vp increases).
"""
from __future__ import annotations

from tsrl.engine.rng import make_rng

import pytest

from tsrl.engine.game_loop import GameResult, _end_of_turn
from tsrl.engine.game_state import reset
from tsrl.schemas import Side


def _make_gs(
    *,
    defcon: int = 3,
    ussr_milops: int = 0,
    us_milops: int = 0,
    vp: int = 0,
    turn: int = 1,
):
    """Create a fresh GameState with the given parameters for testing.

    Sets pub.defcon to the actual pre-advance DEFCON.  Per rules §X end-of-turn
    sequence, milops are checked BEFORE DEFCON advances; the engine must use the
    current (pre-advance) DEFCON for the penalty formula.
    """
    gs = reset(seed=42)
    gs.pub.defcon = defcon  # pre-advance DEFCON; engine checks milops, THEN advances
    gs.pub.milops[int(Side.USSR)] = ussr_milops
    gs.pub.milops[int(Side.US)] = us_milops
    gs.pub.vp = vp
    gs.pub.turn = turn
    return gs


def _run_eot(gs, *, turn: int = 1):
    rng = make_rng(0)
    return _end_of_turn(gs, rng, turn)


class TestMilOpsPenaltyUSSRShortfall:
    """USSR has fewer milops than DEFCON requirement → US gains VP."""

    def test_ussr_shortfall_basic(self):
        # DEFCON will be 3 after advance. USSR milops=1, shortfall=2. US gains 2 VP (vp decreases).
        gs = _make_gs(defcon=3, ussr_milops=1, us_milops=3)
        _run_eot(gs)
        assert gs.pub.vp == -2  # US gained 2 VP

    def test_ussr_shortfall_exact(self):
        # DEFCON 4, USSR milops=3, shortfall=1.
        gs = _make_gs(defcon=4, ussr_milops=3, us_milops=4)
        _run_eot(gs)
        assert gs.pub.vp == -1  # US gained 1 VP

    def test_ussr_shortfall_zero_milops(self):
        # DEFCON 3, USSR milops=0, shortfall=3.
        gs = _make_gs(defcon=3, ussr_milops=0, us_milops=5)
        _run_eot(gs)
        assert gs.pub.vp == -3  # US gained 3 VP


class TestMilOpsPenaltyUSShortfall:
    """US has fewer milops than DEFCON requirement → USSR gains VP."""

    def test_us_shortfall_basic(self):
        # DEFCON 3, US milops=1, shortfall=2. USSR gains 2 VP (vp increases).
        gs = _make_gs(defcon=3, ussr_milops=3, us_milops=1)
        _run_eot(gs)
        assert gs.pub.vp == 2  # USSR gained 2 VP

    def test_us_shortfall_exact(self):
        # DEFCON 4, US milops=0, shortfall=4.
        gs = _make_gs(defcon=4, ussr_milops=4, us_milops=0)
        _run_eot(gs)
        assert gs.pub.vp == 4  # USSR gained 4 VP


class TestMilOpsPenaltyBothShortfall:
    """Both sides short — penalties applied simultaneously."""

    def test_both_shortfall_equal(self):
        # DEFCON 3, both milops=0, each shortfall=3. Net effect: VP += 3 (USSR), VP -= 3 (US) → net 0.
        gs = _make_gs(defcon=3, ussr_milops=0, us_milops=0)
        _run_eot(gs)
        # USSR shortfall=3 → vp -= 3; US shortfall=3 → vp += 3; net = 0.
        assert gs.pub.vp == 0

    def test_both_shortfall_asymmetric(self):
        # DEFCON 4, USSR milops=1 (shortfall=3), US milops=2 (shortfall=2).
        # vp starts at 0 → vp -= 3 (US gain) + vp += 2 (USSR gain) → vp = -1.
        gs = _make_gs(defcon=4, ussr_milops=1, us_milops=2)
        _run_eot(gs)
        assert gs.pub.vp == -1


class TestMilOpsPenaltyNone:
    """Both sides meet the requirement → no VP change."""

    def test_both_meet_requirement(self):
        # DEFCON 3, both milops=3. No penalty.
        gs = _make_gs(defcon=3, ussr_milops=3, us_milops=3)
        vp_before = gs.pub.vp
        _run_eot(gs)
        assert gs.pub.vp == vp_before

    def test_both_exceed_requirement(self):
        # DEFCON 2, both milops=5. No penalty.
        gs = _make_gs(defcon=2, ussr_milops=5, us_milops=5)
        vp_before = gs.pub.vp
        _run_eot(gs)
        assert gs.pub.vp == vp_before

    def test_exactly_at_defcon(self):
        # DEFCON 4, both milops=4. No penalty.
        gs = _make_gs(defcon=4, ussr_milops=4, us_milops=4)
        vp_before = gs.pub.vp
        _run_eot(gs)
        assert gs.pub.vp == vp_before


class TestMilOpsPenaltyResetsAfter:
    """MilOps are reset to [0, 0] after penalties are applied."""

    def test_milops_reset(self):
        gs = _make_gs(defcon=3, ussr_milops=2, us_milops=1)
        _run_eot(gs)
        assert gs.pub.milops == [0, 0]

    def test_milops_reset_when_no_penalty(self):
        gs = _make_gs(defcon=3, ussr_milops=5, us_milops=5)
        _run_eot(gs)
        assert gs.pub.milops == [0, 0]


class TestMilOpsPenaltyCanEndGame:
    """If shortfall pushes VP to ±20, game ends with a GameResult."""

    def test_us_wins_from_penalty(self):
        # Start at vp=-19 (US is 1 VP away from winning).
        # DEFCON 3, USSR milops=0 → shortfall=3. vp -= 3 → vp=-22 → US wins.
        gs = _make_gs(defcon=3, ussr_milops=0, us_milops=3, vp=-19)
        result = _run_eot(gs)
        assert result is not None
        assert result.winner == Side.US

    def test_ussr_wins_from_penalty(self):
        # Start at vp=19 (USSR is 1 VP away from winning).
        # DEFCON 3, US milops=0 → shortfall=3. vp += 3 → vp=22 → USSR wins.
        gs = _make_gs(defcon=3, ussr_milops=3, us_milops=0, vp=19)
        result = _run_eot(gs)
        assert result is not None
        assert result.winner == Side.USSR

    def test_no_game_over_when_penalties_insufficient(self):
        # vp=18, DEFCON 3, US milops=2 → US shortfall=1. vp += 1 = 19 → not enough.
        gs = _make_gs(defcon=3, ussr_milops=3, us_milops=2, vp=18)
        result = _run_eot(gs)
        # Should not end game — 19 < 20.
        assert result is None
        assert gs.pub.vp == 19

    def test_end_reason_is_vp(self):
        # DEFCON 3, USSR milops=0, US milops=3, vp=-19 → US wins with reason 'vp'.
        gs = _make_gs(defcon=3, ussr_milops=0, us_milops=3, vp=-19)
        result = _run_eot(gs)
        assert result is not None
        assert result.end_reason == "vp"
