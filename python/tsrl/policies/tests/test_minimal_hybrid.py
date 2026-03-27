"""Tests for the minimal hybrid rollout policy."""

from tsrl.engine.legal_actions import enumerate_actions
from tsrl.etl.game_data import load_countries
from tsrl.policies.minimal_hybrid import (
    analyze_minimal_hybrid_decision,
    choose_minimal_hybrid,
    make_minimal_hybrid_policy,
)
from tsrl.schemas import ActionMode, PublicState, Side

_THAILAND_ID = 79
_VIETNAM_ID = 80
_COUNTRIES = load_countries()
_SOUTH_AFRICA_ID = next(
    country_id
    for country_id, spec in _COUNTRIES.items()
    if spec.name == "South Africa"
)


def _pub(*, turn: int = 1, ar: int = 1, phasing: Side = Side.USSR) -> PublicState:
    pub = PublicState()
    pub.turn = turn
    pub.ar = ar
    pub.phasing = phasing
    return pub


def test_policy_returns_none_when_no_actions():
    pub = _pub()
    assert choose_minimal_hybrid(pub, frozenset(), False) is None


def test_policy_returns_legal_action_deterministically():
    pub = _pub(turn=1, ar=1, phasing=Side.USSR)
    hand = frozenset({7, 15})

    action1 = choose_minimal_hybrid(pub, hand, False)
    action2 = choose_minimal_hybrid(pub, hand, False)

    legal = enumerate_actions(hand, pub, Side.USSR, holds_china=False)

    assert action1 is not None
    assert action1 == action2
    assert action1 in legal


def test_policy_prefers_scoring_card_in_action_round():
    pub = _pub(turn=1, ar=1, phasing=Side.USSR)
    hand = frozenset({1, 7})  # Asia Scoring + Socialist Governments

    action = choose_minimal_hybrid(pub, hand, False)

    assert action is not None
    assert action.card_id == 1
    assert action.mode == ActionMode.EVENT


def test_policy_prefers_scoring_card_in_headline():
    pub = _pub(turn=1, ar=0, phasing=Side.USSR)
    hand = frozenset({1, 7})

    action = choose_minimal_hybrid(pub, hand, False)

    assert action is not None
    assert action.card_id == 1
    assert action.mode == ActionMode.EVENT


def test_policy_values_thailand_in_early_war():
    pub = _pub(turn=1, ar=1, phasing=Side.USSR)
    pub.influence[(Side.USSR, _VIETNAM_ID)] = 1
    hand = frozenset({15})  # Nasser, 1 op

    action = choose_minimal_hybrid(pub, hand, False)

    assert action is not None
    assert action.targets
    assert action.targets[0] == _THAILAND_ID


def test_policy_conserves_china_when_similar_non_china_card_exists():
    pub = _pub(turn=1, ar=1, phasing=Side.US)
    pub.china_held_by = Side.US
    pub.china_playable = True
    hand = frozenset({6, 23})  # China Card, Marshall Plan

    action = choose_minimal_hybrid(pub, hand, True)

    assert action is not None
    assert action.card_id == 23


def test_policy_prefers_friendly_ops_card_over_offside_ops_card():
    pub = _pub(turn=1, ar=1, phasing=Side.US)
    hand = frozenset({14, 23})  # COMECON, Marshall Plan

    action = choose_minimal_hybrid(pub, hand, False)

    assert action is not None
    assert action.card_id == 23


def test_policy_uses_coup_when_milops_shortfall_is_urgent():
    pub = _pub(turn=5, ar=7, phasing=Side.US)
    pub.defcon = 3
    pub.influence[(Side.USSR, _SOUTH_AFRICA_ID)] = 2
    hand = frozenset({26})  # CIA Created

    action = choose_minimal_hybrid(pub, hand, False)

    assert action is not None
    assert action.mode == ActionMode.COUP


def test_policy_avoids_defcon2_battleground_coup_without_nuclear_subs():
    pub = _pub(turn=5, ar=7, phasing=Side.US)
    pub.defcon = 2
    pub.influence[(Side.USSR, _SOUTH_AFRICA_ID)] = 2
    hand = frozenset({26})  # CIA Created

    action = choose_minimal_hybrid(pub, hand, False)

    assert action is not None
    if action.mode == ActionMode.COUP:
        assert not _COUNTRIES[action.targets[0]].is_battleground


def test_policy_allows_nuclear_subs_battleground_coup_at_defcon2():
    pub = _pub(turn=5, ar=7, phasing=Side.US)
    pub.defcon = 2
    pub.nuclear_subs_active = True
    pub.influence[(Side.USSR, _SOUTH_AFRICA_ID)] = 2
    hand = frozenset({26})  # CIA Created

    action = choose_minimal_hybrid(pub, hand, False)

    assert action is not None
    assert action.mode == ActionMode.COUP
    assert _COUNTRIES[action.targets[0]].is_battleground


def test_policy_wrapper_matches_direct_function():
    pub = _pub(turn=1, ar=1, phasing=Side.USSR)
    hand = frozenset({7, 15})

    policy = make_minimal_hybrid_policy()

    assert policy(pub, hand, False) == choose_minimal_hybrid(pub, hand, False)


def test_decision_analysis_matches_policy_choice():
    pub = _pub(turn=2, ar=2, phasing=Side.US)
    pub.space = [0, 2]
    hand = frozenset({5, 7})

    analysis = analyze_minimal_hybrid_decision(pub, hand, False, top_n=3)

    assert analysis.chosen_action == choose_minimal_hybrid(pub, hand, False)
    assert analysis.legal_action_count >= len(analysis.ranked_actions) >= 1
    assert analysis.ranked_actions[0].action == analysis.chosen_action
