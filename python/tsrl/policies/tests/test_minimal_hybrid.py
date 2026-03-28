"""Tests for the minimal hybrid rollout policy."""

import hashlib
import json
import random

import pytest

from tsrl.engine.game_state import _ars_for_turn
from tsrl.engine.legal_actions import effective_ops
from tsrl.engine.legal_actions import enumerate_actions
from tsrl.etl.game_data import load_countries
from tsrl.policies.generate_minimal_hybrid_rollout_logs import (
    LogMode,
    _generate_game_artifacts,
)
from tsrl.policies.minimal_hybrid import (
    DEFAULT_MINIMAL_HYBRID_PARAMS,
    _action_sort_key,
    _best_influence_action_dp,
    _cards,
    _limited_accessible,
    _make_decision_context,
    _score_influence_action,
    analyze_minimal_hybrid_decision,
    choose_minimal_hybrid,
    make_minimal_hybrid_policy,
)
from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Side

_THAILAND_ID = 79
_VIETNAM_ID = 80
_COUNTRIES = load_countries()
_SOUTH_AFRICA_ID = next(
    country_id
    for country_id, spec in _COUNTRIES.items()
    if spec.name == "South Africa"
)
_MEXICO_ID = next(
    country_id
    for country_id, spec in _COUNTRIES.items()
    if spec.name == "Mexico"
)


def _pub(*, turn: int = 1, ar: int = 1, phasing: Side = Side.USSR) -> PublicState:
    pub = PublicState()
    pub.turn = turn
    pub.ar = ar
    pub.phasing = phasing
    return pub


def _random_sparse_public_state(rng: random.Random) -> PublicState:
    turn = rng.randint(1, 10)
    pub = _pub(
        turn=turn,
        ar=rng.randint(1, _ars_for_turn(turn)),
        phasing=rng.choice((Side.USSR, Side.US)),
    )
    pub.defcon = rng.randint(2, 5)
    pub.milops = [rng.randint(0, turn), rng.randint(0, turn)]
    pub.space = [rng.randint(0, 7), rng.randint(0, 7)]
    pub.china_held_by = rng.choice((Side.USSR, Side.US))
    pub.china_playable = rng.choice((True, False))

    country_ids = list(_COUNTRIES.keys())
    own_count = rng.randint(1, 2)
    opp_count = rng.randint(0, 2)
    own_ids = rng.sample(country_ids, own_count)
    remaining = [country_id for country_id in country_ids if country_id not in own_ids]
    opp_ids = rng.sample(remaining, opp_count)

    for country_id in own_ids:
        pub.influence[(pub.phasing, country_id)] = rng.randint(1, 2)
    other = Side.US if pub.phasing == Side.USSR else Side.USSR
    for country_id in opp_ids:
        pub.influence[(other, country_id)] = rng.randint(1, 3)
    return pub


def _random_dp_states(count: int) -> list[PublicState]:
    rng = random.Random(20260415)
    states: list[PublicState] = []
    attempts = 0
    while len(states) < count:
        attempts += 1
        if attempts > 10_000:
            raise AssertionError("failed to build enough sparse DP comparison states")
        pub = _random_sparse_public_state(rng)
        context = _make_decision_context(pub, pub.phasing, DEFAULT_MINIMAL_HYBRID_PARAMS)
        if context.accessible_influence:
            states.append(pub)
    return states


def _brute_force_best_influence_action(
    card_id: int,
    accessible: tuple[int, ...],
    context,
) -> tuple[ActionEncoding, float]:
    ops = effective_ops(card_id, context.pub, context.side)
    best_action: ActionEncoding | None = None
    best_score: float | None = None

    def _visit(index: int, remaining_ops: int, targets: tuple[int, ...]) -> None:
        nonlocal best_action, best_score
        if index == len(accessible):
            if remaining_ops != 0:
                return
            action = ActionEncoding(
                card_id=card_id,
                mode=ActionMode.INFLUENCE,
                targets=targets,
            )
            score = _score_influence_action(context, action)
            if best_action is None or _action_sort_key(action, score) < _action_sort_key(
                best_action,
                best_score,
            ):
                best_action = action
                best_score = score
            return

        country_id = accessible[index]
        for allocation in range(remaining_ops + 1):
            _visit(
                index + 1,
                remaining_ops - allocation,
                targets + ((country_id,) * allocation),
            )

    _visit(0, ops, ())
    assert best_action is not None
    assert best_score is not None
    return best_action, best_score


def _stable_json_hash(value: object | None) -> str | None:
    if value is None:
        return None
    return hashlib.sha256(
        json.dumps(value, sort_keys=True).encode("utf-8")
    ).hexdigest()


def _trajectory_signature(
    payload: dict[str, object],
) -> tuple[tuple[str, ...], tuple[tuple[str, str | None], ...]]:
    actions: list[str] = []
    hashes: list[tuple[str, str | None]] = []
    for step in payload["steps"]:
        actions.append(json.dumps(step["chosen_action"], sort_keys=True))
        hashes.append((
            _stable_json_hash(step["public_state"]),
            _stable_json_hash(step.get("post_public_state")),
        ))
    return tuple(actions), tuple(hashes)


def _random_sparse_public_state_for_seed(seed: int) -> PublicState:
    rng = random.Random(seed)
    for _ in range(200):
        pub = _random_sparse_public_state(rng)
        context = _make_decision_context(pub, pub.phasing, DEFAULT_MINIMAL_HYBRID_PARAMS)
        if context.accessible_influence:
            return pub
    raise AssertionError(f"failed to build accessible sparse state for seed {seed}")


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


def test_policy_avoids_defcon3_battleground_coup_without_milops_urgency():
    pub = _pub(turn=1, ar=1, phasing=Side.US)
    pub.defcon = 3
    pub.influence[(Side.USSR, _MEXICO_ID)] = 2
    hand = frozenset({10})  # Blockade

    action = choose_minimal_hybrid(pub, hand, False)

    assert action is not None
    assert action.mode != ActionMode.COUP


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


def test_influence_dp_matches_brute_force():
    subset_rng = random.Random(20260415)
    for pub in _random_dp_states(10):
        context = _make_decision_context(pub, pub.phasing, DEFAULT_MINIMAL_HYBRID_PARAMS)
        accessible_pool = _limited_accessible(context.accessible_influence)
        accessible = tuple(
            sorted(
                subset_rng.sample(
                    accessible_pool,
                    k=min(6, len(accessible_pool)),
                )
            )
        )
        for card_id in sorted(_cards()):
            dp_action, dp_score = _best_influence_action_dp(card_id, accessible, context)
            brute_action, brute_score = _brute_force_best_influence_action(
                card_id,
                accessible,
                context,
            )
            assert dp_action == brute_action
            assert abs(dp_score - brute_score) < 1e-12


def test_dp_influence_zero_ops_card():
    zero_ops_cards = sorted(
        card_id for card_id, card in _cards().items() if card.ops == 0
    )
    if not zero_ops_cards:
        pytest.skip("no 0-op cards in card spec")

    pub = _pub(turn=1, ar=1, phasing=Side.USSR)
    context = _make_decision_context(pub, pub.phasing, DEFAULT_MINIMAL_HYBRID_PARAMS)
    card_id = zero_ops_cards[0]

    action, score = _best_influence_action_dp(card_id, (), context)

    assert action == ActionEncoding(
        card_id=card_id,
        mode=ActionMode.INFLUENCE,
        targets=(),
    )
    assert score == _score_influence_action(context, action)


def test_dp_influence_single_country():
    pub = _pub(turn=1, ar=1, phasing=Side.USSR)
    context = _make_decision_context(pub, pub.phasing, DEFAULT_MINIMAL_HYBRID_PARAMS)
    country_id = min(context.accessible_influence)
    accessible = (country_id,)
    card_id = next(
        cid for cid, card in sorted(_cards().items()) if card.ops > 0 and not card.is_scoring
    )

    action, score = _best_influence_action_dp(card_id, accessible, context)

    assert action == ActionEncoding(
        card_id=card_id,
        mode=ActionMode.INFLUENCE,
        targets=(country_id,) * effective_ops(card_id, context.pub, context.side),
    )
    assert abs(score - _score_influence_action(context, action)) < 1e-12


def test_dp_influence_all_equal_value():
    pub = _pub(turn=1, ar=1, phasing=Side.USSR)
    context = _make_decision_context(pub, pub.phasing, DEFAULT_MINIMAL_HYBRID_PARAMS)
    accessible_by_stability: dict[int, list[int]] = {}
    for country_id in sorted(context.accessible_influence):
        accessible_by_stability.setdefault(context.stabilities[country_id], []).append(country_id)
    accessible = next(
        tuple(country_ids[:3])
        for stability, country_ids in sorted(accessible_by_stability.items())
        if stability > 1 and len(country_ids) >= 2
    )
    for country_id in context.country_values:
        context.country_values[country_id] = 10.0
    card_id = next(
        cid for cid, card in sorted(_cards().items()) if card.ops == 1 and not card.is_scoring
    )

    action1, score1 = _best_influence_action_dp(card_id, accessible, context)
    action2, score2 = _best_influence_action_dp(card_id, accessible, context)

    assert action1 == action2
    assert score1 == score2
    assert action1 == ActionEncoding(
        card_id=card_id,
        mode=ActionMode.INFLUENCE,
        targets=(min(accessible),),
    )


def test_game_determinism_10x_replay():
    seed = 20260401
    first_actions: tuple[str, ...] | None = None
    first_hashes: tuple[tuple[str, str | None], ...] | None = None

    for _ in range(10):
        _game_idx, payload, _markdown, _summary = _generate_game_artifacts(
            (0, seed, 5, LogMode.FAST, DEFAULT_MINIMAL_HYBRID_PARAMS)
        )
        actions, hashes = _trajectory_signature(payload)
        if first_actions is None:
            first_actions = actions
            first_hashes = hashes
            continue
        assert actions == first_actions
        assert hashes == first_hashes


def test_dp_precomputation_determinism():
    pub = _pub(turn=2, ar=2, phasing=Side.USSR)
    pub.influence[(Side.USSR, _VIETNAM_ID)] = 1
    hand = frozenset({15, 18, 19})

    actions = [choose_minimal_hybrid(pub, hand, False) for _ in range(5)]

    assert actions[0] is not None
    assert all(action == actions[0] for action in actions[1:])


def test_dp_vs_bruteforce_50_random_seeds():
    card_ids = [
        card_id
        for card_id, card in sorted(_cards().items())
        if card.ops > 0
    ][:20]

    for seed in range(50):
        pub = _random_sparse_public_state_for_seed(seed)
        context = _make_decision_context(pub, pub.phasing, DEFAULT_MINIMAL_HYBRID_PARAMS)
        accessible_pool = _limited_accessible(context.accessible_influence)
        subset_rng = random.Random(seed + 10_000)
        accessible = tuple(
            sorted(
                subset_rng.sample(
                    accessible_pool,
                    k=min(6, len(accessible_pool)),
                )
            )
        )
        for card_id in card_ids:
            dp_action, dp_score = _best_influence_action_dp(card_id, accessible, context)
            brute_action, brute_score = _brute_force_best_influence_action(
                card_id,
                accessible,
                context,
            )
            assert dp_action == brute_action
            assert abs(dp_score - brute_score) < 1e-12


def test_rollout_log_modes_preserve_chosen_actions():
    seed = 20260401
    payloads: dict[LogMode, dict[str, object]] = {}
    markdowns: dict[LogMode, str | None] = {}

    for mode in LogMode:
        _game_idx, payload, markdown, _summary = _generate_game_artifacts(
            (0, seed, 5, mode, DEFAULT_MINIMAL_HYBRID_PARAMS)
        )
        json.dumps(payload)
        payloads[mode] = payload
        markdowns[mode] = markdown

    expected = [
        step["chosen_action"]
        for step in payloads[LogMode.FAST]["steps"]
    ]
    assert expected == [
        step["chosen_action"]
        for step in payloads[LogMode.TRACE_TOPN]["steps"]
    ]
    assert expected == [
        step["chosen_action"]
        for step in payloads[LogMode.TRACE_FULL]["steps"]
    ]
    assert markdowns[LogMode.FAST] is None
    assert markdowns[LogMode.TRACE_TOPN] is None
    assert markdowns[LogMode.TRACE_FULL] is not None
