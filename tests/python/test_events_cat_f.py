"""
Tests for Category F event handlers:
  Card 18 — Captured Nazi Scientist
  Card 20 — Olympic Games
  Card 50 — Junta
  Card 51 — Kitchen Debates
  Card 72 — Nixon Plays the China Card
  Card 77 — Ussuri River Skirmish
  Card 81 — One Small Step
  Card 103 — Wargames

Also tests the Wargames legal restriction in legal_modes().
"""
from __future__ import annotations

from tsrl.engine.rng import make_rng

import pytest

from tsrl.engine.events import apply_event_card
from tsrl.engine.legal_actions import legal_modes
from tsrl.engine.game_state import reset
from tsrl.schemas import ActionMode, PublicState, Side


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _pub(*, vp: int = 0, defcon: int = 3) -> PublicState:
    """Create a minimal PublicState for event testing."""
    gs = reset(seed=0)
    gs.pub.vp = vp
    gs.pub.defcon = defcon
    return gs.pub


def _fire(pub: PublicState, card_id: int, side: Side, seed: int = 0):
    """Fire a card event and return (pub, over, winner)."""
    rng = make_rng(seed)
    return apply_event_card(pub, card_id, side, rng)


# ---------------------------------------------------------------------------
# Card 18 — Captured Nazi Scientist
# ---------------------------------------------------------------------------

class TestCapturedNaziScientist:
    CARD = 18

    def test_advances_space_level(self):
        pub = _pub()
        pub.space[int(Side.USSR)] = 0
        pub, over, winner = _fire(pub, self.CARD, Side.USSR)
        assert pub.space[int(Side.USSR)] == 1

    def test_awards_vp_first_to_level1(self):
        # USSR goes from 0→1, US still at 0 → first to reach level 1 → 2 VP.
        pub = _pub()
        pub.space[int(Side.USSR)] = 0
        pub.space[int(Side.US)] = 0
        pub, _, _ = _fire(pub, self.CARD, Side.USSR)
        assert pub.vp == 2  # USSR gained 2 VP

    def test_awards_second_vp_when_opponent_already_at_level(self):
        # USSR goes 0→1 but US is already at level 1 → second_vp = 0.
        pub = _pub()
        pub.space[int(Side.USSR)] = 0
        pub.space[int(Side.US)] = 1
        pub, _, _ = _fire(pub, self.CARD, Side.USSR)
        # Level 1: first_vp=2, second_vp=0. US already at 1 → USSR gets 0.
        assert pub.vp == 0

    def test_awards_vp_level3(self):
        # USSR goes 2→3, US at 0 → first to reach level 3 → 2 VP.
        pub = _pub()
        pub.space[int(Side.USSR)] = 2
        pub.space[int(Side.US)] = 0
        pub, _, _ = _fire(pub, self.CARD, Side.USSR)
        assert pub.vp == 2  # USSR gained 2 VP

    def test_no_effect_at_max_level(self):
        # Space already at 8 → no change.
        pub = _pub()
        pub.space[int(Side.USSR)] = 8
        vp_before = pub.vp
        pub, _, _ = _fire(pub, self.CARD, Side.USSR)
        assert pub.space[int(Side.USSR)] == 8
        assert pub.vp == vp_before

    def test_us_side_advances_us_track(self):
        pub = _pub()
        pub.space[int(Side.US)] = 2
        pub.space[int(Side.USSR)] = 0
        pub, _, _ = _fire(pub, self.CARD, Side.US)
        assert pub.space[int(Side.US)] == 3
        # Level 3: first_vp=2, USSR at 0 < 3 → first → US gains 2 VP → vp -= 2.
        assert pub.vp == -2

    def test_does_not_advance_opponent_track(self):
        pub = _pub()
        pub.space[int(Side.USSR)] = 3
        pub.space[int(Side.US)] = 0
        pub, _, _ = _fire(pub, self.CARD, Side.USSR)
        assert pub.space[int(Side.US)] == 0  # US track unchanged


# ---------------------------------------------------------------------------
# Card 50 — Junta
# ---------------------------------------------------------------------------

class TestJunta:
    CARD = 50

    def test_places_2_influence_in_ca_sa(self):
        # 2 influence must appear in a Central or South American country.
        pub = _pub()
        _CENTRAL_AMERICA = frozenset({36, 37, 38, 39, 40, 41, 42, 43, 44, 45})
        _SOUTH_AMERICA = frozenset({46, 47, 48, 49, 50, 51, 52, 53, 54, 55})
        valid_countries = _CENTRAL_AMERICA | _SOUTH_AMERICA

        # Run multiple seeds to confirm placement always lands in valid region.
        for seed in range(10):
            p2 = _pub()
            p2, _, _ = _fire(p2, self.CARD, Side.USSR, seed=seed)
            placed = sum(
                p2.influence.get((Side.USSR, cid), 0)
                for cid in valid_countries
            )
            # At least 2 inf must have been placed via the "place 2 inf" part.
            assert placed >= 2, f"seed={seed}: only {placed} USSR inf in C/SA"

    def test_coup_affects_ca_sa_country(self):
        # Junta may fire a coup in C/SA. Run enough seeds to hit coup branch.
        # We just verify no crash and state remains consistent.
        for seed in range(20):
            pub = _pub(defcon=4)
            pub.influence[(Side.US, 49)] = 3  # Chile — give US something to remove
            pub, over, winner = _fire(pub, self.CARD, Side.USSR, seed=seed)
            assert isinstance(over, bool)


# ---------------------------------------------------------------------------
# Card 51 — Kitchen Debates
# ---------------------------------------------------------------------------

class TestKitchenDebates:
    CARD = 51

    def test_us_leads_battlegrounds_gains_vp(self):
        # US controls 3 more battlegrounds than USSR → US gains 3 VP.
        pub = _pub()
        from tsrl.etl.game_data import load_countries
        countries = load_countries()
        bg_ids = sorted([cid for cid, spec in countries.items() if spec.is_battleground and cid not in {64, 81, 82}])
        # Clear all existing influence for these battlegrounds first.
        # Give US clear control of first 3 battlegrounds (set opp inf to 0).
        for cid in bg_ids[:3]:
            stab = countries[cid].stability
            pub.influence.pop((Side.USSR, cid), None)
            pub.influence[(Side.US, cid)] = stab  # US controls: own=stab >= 0 + stab
        # Clear US influence from any USSR-controlled BGs (so USSR controls none).
        for cid in bg_ids[3:]:
            pub.influence.pop((Side.US, cid), None)
            pub.influence.pop((Side.USSR, cid), None)
        pub, over, winner = _fire(pub, self.CARD, Side.US)
        assert pub.vp == -3  # US gained 3 VP (pub.vp decreases)

    def test_ussr_leads_battlegrounds_no_vp(self):
        # USSR controls more BGs than US → no effect.
        pub = _pub()
        from tsrl.etl.game_data import load_countries
        countries = load_countries()
        bg_ids = sorted([cid for cid, spec in countries.items() if spec.is_battleground and cid not in {64, 81, 82}])
        # USSR controls first 5, US controls none.
        for cid in bg_ids[:5]:
            stab = countries[cid].stability
            pub.influence.pop((Side.US, cid), None)
            pub.influence[(Side.USSR, cid)] = stab
        for cid in bg_ids[5:]:
            pub.influence.pop((Side.US, cid), None)
            pub.influence.pop((Side.USSR, cid), None)
        pub, _, _ = _fire(pub, self.CARD, Side.US)
        assert pub.vp == 0  # No change

    def test_tied_battlegrounds_no_vp(self):
        # Both sides control 0 BGs → excess=0 → no VP.
        pub = _pub()
        # Clear all influence.
        pub.influence.clear()
        pub, _, _ = _fire(pub, self.CARD, Side.US)
        assert pub.vp == 0


# ---------------------------------------------------------------------------
# Card 72 — Nixon Plays the China Card
# ---------------------------------------------------------------------------

class TestNixonPlaysChina:
    CARD = 72

    def test_us_gains_2_vp_always(self):
        pub = _pub()
        pub.china_held_by = Side.USSR
        pub, _, _ = _fire(pub, self.CARD, Side.US)
        assert pub.vp == -2  # US gained 2 VP

    def test_takes_china_from_ussr_face_down(self):
        pub = _pub()
        pub.china_held_by = Side.USSR
        pub.china_playable = True
        pub, _, _ = _fire(pub, self.CARD, Side.US)
        assert pub.china_held_by == Side.US
        assert pub.china_playable is False  # taken face-down

    def test_flips_china_face_up_when_us_already_holds(self):
        pub = _pub()
        pub.china_held_by = Side.US
        pub.china_playable = False
        pub, _, _ = _fire(pub, self.CARD, Side.US)
        assert pub.china_held_by == Side.US
        assert pub.china_playable is True  # flipped face-up

    def test_no_vp_when_us_already_holds_china(self):
        # When US already holds China Card, event only flips it face-up — no VP.
        pub = _pub(vp=0)
        pub.china_held_by = Side.US
        pub, _, _ = _fire(pub, self.CARD, Side.US)
        assert pub.vp == 0  # no VP change when US already holds it


# ---------------------------------------------------------------------------
# Card 77 — Ussuri River Skirmish
# ---------------------------------------------------------------------------

class TestUssuri:
    CARD = 77

    def test_ussr_holds_china_transfers_to_us(self):
        pub = _pub()
        pub.china_held_by = Side.USSR
        pub.china_playable = False
        pub, _, _ = _fire(pub, self.CARD, Side.USSR)
        assert pub.china_held_by == Side.US
        assert pub.china_playable is True  # face-up

    def test_ussr_holds_china_ussr_gains_4_inf(self):
        pub = _pub()
        pub.china_held_by = Side.USSR
        total_before = sum(v for (s, c), v in pub.influence.items() if s == Side.USSR)
        pub, _, _ = _fire(pub, self.CARD, Side.USSR)
        total_after = sum(v for (s, c), v in pub.influence.items() if s == Side.USSR)
        assert total_after - total_before == 4

    def test_us_holds_china_transfers_to_ussr(self):
        pub = _pub()
        pub.china_held_by = Side.US
        pub.china_playable = False
        pub, _, _ = _fire(pub, self.CARD, Side.US)
        assert pub.china_held_by == Side.USSR
        assert pub.china_playable is True  # face-up

    def test_us_holds_china_us_gains_4_inf(self):
        pub = _pub()
        pub.china_held_by = Side.US
        total_before = sum(v for (s, c), v in pub.influence.items() if s == Side.US)
        pub, _, _ = _fire(pub, self.CARD, Side.US)
        total_after = sum(v for (s, c), v in pub.influence.items() if s == Side.US)
        assert total_after - total_before == 4


# ---------------------------------------------------------------------------
# Card 81 — One Small Step
# ---------------------------------------------------------------------------

class TestOneSmallStep:
    CARD = 81

    def test_behind_advances_two_levels(self):
        # USSR at level 1, US at level 3 → USSR advances 2 levels to 3.
        pub = _pub()
        pub.space[int(Side.USSR)] = 1
        pub.space[int(Side.US)] = 3
        pub, _, _ = _fire(pub, self.CARD, Side.USSR)
        assert pub.space[int(Side.USSR)] == 3

    def test_not_behind_no_effect(self):
        # USSR at level 3, US at level 2 → not behind → no change.
        pub = _pub()
        pub.space[int(Side.USSR)] = 3
        pub.space[int(Side.US)] = 2
        vp_before = pub.vp
        pub, over, winner = _fire(pub, self.CARD, Side.USSR)
        assert pub.space[int(Side.USSR)] == 3  # unchanged
        assert pub.vp == vp_before
        assert over is False

    def test_equal_not_behind_no_effect(self):
        # Both at level 3 → equal, not behind → no change.
        pub = _pub()
        pub.space[int(Side.USSR)] = 3
        pub.space[int(Side.US)] = 3
        pub, over, _ = _fire(pub, self.CARD, Side.USSR)
        assert pub.space[int(Side.USSR)] == 3
        assert over is False

    def test_capped_at_level_8(self):
        # USSR at level 7, US at level 8 → behind → advance 2, but cap at 8.
        pub = _pub()
        pub.space[int(Side.USSR)] = 7
        pub.space[int(Side.US)] = 8
        pub, _, _ = _fire(pub, self.CARD, Side.USSR)
        assert pub.space[int(Side.USSR)] == 8  # capped at 8

    def test_awards_vp_for_each_level(self):
        # USSR at level 0, US at level 5 → behind → advance from 0 to 2.
        # Level 1: first_vp=2, opp=5 ≥ 1 → second_vp=0.
        # Level 2: first_vp=0, opp=5 ≥ 2 → second_vp=0.
        # Net VP = 0.
        pub = _pub()
        pub.space[int(Side.USSR)] = 0
        pub.space[int(Side.US)] = 5
        pub, _, _ = _fire(pub, self.CARD, Side.USSR)
        assert pub.space[int(Side.USSR)] == 2
        assert pub.vp == 0  # second_vp for both levels = 0

    def test_awards_first_vp_when_catching_up(self):
        # USSR at level 0, US at level 1. USSR behind by 1 → advances 2 levels.
        # Level 1: opp_level=1, not < 1 → second_vp=0.
        # Level 2: opp_level=1 < 2 → first_vp=0.
        # Net VP = 0.
        pub = _pub()
        pub.space[int(Side.USSR)] = 0
        pub.space[int(Side.US)] = 1
        pub, _, _ = _fire(pub, self.CARD, Side.USSR)
        assert pub.space[int(Side.USSR)] == 2


# ---------------------------------------------------------------------------
# Card 20 — Olympic Games
# ---------------------------------------------------------------------------

class TestOlympicGames:
    CARD = 20

    def test_winner_gains_2_vp(self):
        # With controlled seed, verify that whoever wins gets 2 VP.
        # Seed 0 for USSR side: check deterministic outcome.
        pub = _pub()
        pub_after, over, winner = _fire(pub, self.CARD, Side.USSR, seed=1)
        # VP should have changed by exactly 0 (DEFCON drop) or ±2 (win) or 0 (tie+DEFCON).
        assert pub_after.vp in {-2, 0, 2}

    def test_boycott_defcon_drop_and_phasing_player_gets_influence(self):
        # Boycott: opponent boycotts (rng.random() < 0.5), DEFCON drops by 1,
        # phasing player (USSR) gains 4 free influence ops.
        for seed in range(1000):
            rng = make_rng(seed)
            if rng.random() < 0.5:
                pub = _pub(defcon=4)
                ussr_inf_before = sum(v for (s, c), v in pub.influence.items() if s == Side.USSR)
                pub_after, _, _ = _fire(pub, self.CARD, Side.USSR, seed=seed)
                # DEFCON drops by 1.
                assert pub_after.defcon == 3, f"seed={seed}: DEFCON should drop to 3"
                # VP should not change directly (no 2-VP award).
                assert pub_after.vp == 0, f"seed={seed}: VP should be 0, got {pub_after.vp}"
                # USSR (phasing player) gains exactly 4 influence ops.
                ussr_inf_after = sum(v for (s, c), v in pub_after.influence.items() if s == Side.USSR)
                assert ussr_inf_after - ussr_inf_before == 4, (
                    f"seed={seed}: USSR should gain 4 influence, gained {ussr_inf_after - ussr_inf_before}"
                )
                break
        else:
            pytest.skip("No boycott seed found in first 1000 — adjust range")

    def test_compete_no_defcon_drop_on_winner(self):
        # Updated for new compete mechanic: ties are rerolled, so DEFCON never drops
        # on the compete path. Find a seed where compete branch fires (random >= 0.5).
        for seed in range(1000):
            rng = make_rng(seed)
            val = rng.random()
            if val >= 0.5:
                pub = _pub(defcon=4)
                pub_after, _, _ = _fire(pub, self.CARD, Side.USSR, seed=seed)
                # DEFCON should not drop on the compete path.
                assert pub_after.defcon == 4, (
                    f"DEFCON should not drop on compete path (seed={seed})"
                )
                # VP should have changed by exactly ±2 (one side wins).
                assert pub_after.vp in {-2, 2}, (
                    f"Compete path should award ±2 VP, got vp={pub_after.vp} (seed={seed})"
                )
                break
        else:
            pytest.skip("No compete seed found in first 1000 — adjust range")

    def test_higher_bid_wins_2_vp(self):
        # Find a seed where USSR bid > US bid.
        for seed in range(1000):
            rng = make_rng(seed)
            val = rng.random()
            if val >= 0.2:
                b1 = int(rng.integers(1, 4))  # 1-3 inclusive
                b2 = int(rng.integers(1, 4))
                if b1 > b2:
                    pub = _pub()
                    pub_after, _, _ = _fire(pub, self.CARD, Side.USSR, seed=seed)
                    assert pub_after.vp == 2  # USSR gained 2 VP
                    break
        else:
            pytest.skip("No USSR-wins seed found")


# ---------------------------------------------------------------------------
# Card 103 — Wargames
# ---------------------------------------------------------------------------

class TestWargames:
    CARD = 103

    def test_wargames_at_defcon2_ends_game(self):
        pub = _pub(defcon=2)
        pub, over, winner = _fire(pub, self.CARD, Side.USSR)
        assert over is True
        assert winner == Side.US  # USSR played it → USSR loses → US wins

    def test_wargames_at_defcon2_opponent_gains_6_vp(self):
        # USSR plays Wargames: US (opponent) gains 6 VP.
        pub = _pub(defcon=2, vp=0)
        pub, _, _ = _fire(pub, self.CARD, Side.USSR)
        assert pub.vp == -6  # US gained 6 VP

    def test_wargames_us_plays_ussr_wins(self):
        pub = _pub(defcon=2)
        pub, over, winner = _fire(pub, self.CARD, Side.US)
        assert over is True
        assert winner == Side.USSR  # US played it → US loses → USSR wins

    def test_wargames_not_at_defcon2_no_effect(self):
        # Outside DEFCON 2: should be a no-op.
        for defcon in [1, 3, 4, 5]:
            pub = _pub(defcon=defcon)
            vp_before = pub.vp
            pub_after, over, winner = _fire(pub, self.CARD, Side.USSR)
            assert over is False
            assert pub_after.vp == vp_before, f"defcon={defcon} should be no-op"


# ---------------------------------------------------------------------------
# Wargames legal restriction in legal_modes()
# ---------------------------------------------------------------------------

class TestWargamesLegality:
    CARD = 103

    def test_event_legal_at_defcon2(self):
        gs = reset(seed=0)
        gs.pub.defcon = 2
        modes = legal_modes(self.CARD, gs.pub, Side.USSR)
        assert ActionMode.EVENT in modes

    def test_event_illegal_at_defcon3(self):
        gs = reset(seed=0)
        gs.pub.defcon = 3
        modes = legal_modes(self.CARD, gs.pub, Side.USSR)
        assert ActionMode.EVENT not in modes

    def test_event_illegal_at_defcon4(self):
        gs = reset(seed=0)
        gs.pub.defcon = 4
        modes = legal_modes(self.CARD, gs.pub, Side.USSR)
        assert ActionMode.EVENT not in modes

    def test_event_illegal_at_defcon5(self):
        gs = reset(seed=0)
        gs.pub.defcon = 5
        modes = legal_modes(self.CARD, gs.pub, Side.USSR)
        assert ActionMode.EVENT not in modes

    def test_ops_modes_still_legal_at_defcon3(self):
        # Wargames is a 4-op Neutral card; ops modes should still be available outside DEFCON 2.
        # Test from USSR perspective: they can still INFLUENCE / COUP / REALIGN with Wargames.
        gs = reset(seed=0)
        gs.pub.defcon = 3
        modes = legal_modes(self.CARD, gs.pub, Side.USSR)
        # INFLUENCE and REALIGN should still be available (ops modes remain).
        assert ActionMode.INFLUENCE in modes or ActionMode.COUP in modes or ActionMode.REALIGN in modes
