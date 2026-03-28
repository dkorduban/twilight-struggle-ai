"""Tests for python/tsrl/engine/scoring.py — focused on Formosan Resolution Taiwan logic."""

import pytest
from tsrl.engine.scoring import score_region
from tsrl.schemas import PublicState, Region, Side

_TAIWAN = 85
_SOUTH_KOREA = 25
_JAPAN = 26


def _asia_pub() -> PublicState:
    """Minimal PublicState with superpowers adjacent to Asia countries."""
    pub = PublicState()
    pub.turn = 3
    return pub


# ---------------------------------------------------------------------------
# Formosan Resolution: Taiwan as Asia battleground
# ---------------------------------------------------------------------------


def test_formosan_inactive_taiwan_ignored_in_asia_scoring():
    """Without Formosan, Taiwan (id=85) has no BG weight in Asia scoring."""
    pub = _asia_pub()
    # Give US 4 inf in Taiwan — should not matter
    pub.influence[(Side.US, _TAIWAN)] = 4
    result_without = score_region(Region.ASIA, pub)

    # Now explicitly set formosan_active=False
    pub.formosan_active = False
    result_with_false = score_region(Region.ASIA, pub)

    assert result_without.vp_delta == result_with_false.vp_delta


def test_formosan_active_taiwan_counts_as_battleground():
    """With Formosan active, US controlling Taiwan earns extra BG credit in Asia."""
    pub = _asia_pub()
    # US controls Taiwan (stability=3, need ≥3 inf with none opposed)
    pub.influence[(Side.US, _TAIWAN)] = 3

    result_without = score_region(Region.ASIA, pub)  # formosan_active=False default

    pub.formosan_active = True
    result_with = score_region(Region.ASIA, pub)

    # US gains a battleground — vp_delta should decrease (more US-favoured)
    assert result_with.vp_delta < result_without.vp_delta, (
        f"Formosan should shift Asia VP toward US. "
        f"Without: {result_without.vp_delta}, With: {result_with.vp_delta}"
    )


def test_formosan_taiwan_ussr_controlled_hurts_us():
    """If USSR controls Taiwan under Formosan, that BG counts for USSR."""
    pub = _asia_pub()
    # USSR controls Taiwan
    pub.influence[(Side.USSR, _TAIWAN)] = 4

    pub.formosan_active = True
    result = score_region(Region.ASIA, pub)

    # Compare to same position without Formosan
    pub.formosan_active = False
    result_no_formosan = score_region(Region.ASIA, pub)

    # USSR gains a BG under Formosan → vp_delta should increase (USSR-favoured)
    assert result.vp_delta > result_no_formosan.vp_delta, (
        f"USSR controlling Taiwan under Formosan should boost USSR VP. "
        f"Without: {result_no_formosan.vp_delta}, With: {result.vp_delta}"
    )


def test_formosan_taiwan_uncontrolled_does_not_shift_vp():
    """Taiwan at 0/0 inf under Formosan: neither side controls it, no BG bonus either way."""
    pub = _asia_pub()
    # Taiwan at 0/0 — neither controls it; BG exists but neither earns from it
    pub.formosan_active = True
    result_contested = score_region(Region.ASIA, pub)

    pub.formosan_active = False
    result_no_formosan = score_region(Region.ASIA, pub)

    # Neither side controls → no battleground swing either direction
    assert result_contested.vp_delta == result_no_formosan.vp_delta, (
        "Uncontrolled Taiwan under Formosan should not shift VP"
    )


def test_formosan_taiwan_does_not_affect_other_regions():
    """Formosan active should not change scoring for non-Asia regions."""
    pub = _asia_pub()
    pub.influence[(Side.US, _TAIWAN)] = 3

    # Score Europe — should be identical with/without Formosan
    result_off = score_region(Region.EUROPE, pub)
    pub.formosan_active = True
    result_on = score_region(Region.EUROPE, pub)

    assert result_off.vp_delta == result_on.vp_delta
