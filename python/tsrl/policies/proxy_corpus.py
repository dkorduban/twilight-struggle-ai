"""Richer fixed proxy corpus for minimal_hybrid tuning.

This corpus is policy-local and deterministic. It mixes exact-action
expectations and softer action-property expectations so tuning has a cheap
signal beyond pure baseline action agreement.
"""
from __future__ import annotations

from dataclasses import dataclass

from tsrl.policies.minimal_hybrid import DEFAULT_MINIMAL_HYBRID_PARAMS, choose_minimal_hybrid
from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Side

_THAILAND_ID = 79
_VIETNAM_ID = 80


@dataclass(frozen=True)
class ProxyCase:
    name: str
    pub: PublicState
    hand: frozenset[int]
    holds_china: bool
    expected_action: ActionEncoding | None = None
    expected_card_id: int | None = None
    forbidden_card_id: int | None = None
    expected_mode: ActionMode | None = None
    required_target: int | None = None
    weight: float = 1.0


def _pub(
    *,
    turn: int,
    ar: int,
    phasing: Side,
    defcon: int = 5,
    influence: tuple[tuple[Side, int, int], ...] = (),
    china_held_by: Side = Side.USSR,
    china_playable: bool = True,
    milops: tuple[int, int] = (0, 0),
    space: tuple[int, int] = (0, 0),
) -> PublicState:
    pub = PublicState()
    pub.turn = turn
    pub.ar = ar
    pub.phasing = phasing
    pub.defcon = defcon
    pub.china_held_by = china_held_by
    pub.china_playable = china_playable
    pub.milops = list(milops)
    pub.space = list(space)
    for side, country_id, amount in influence:
        pub.influence[(side, country_id)] = amount
    return pub


def build_proxy_corpus() -> tuple[ProxyCase, ...]:
    """Return a deterministic labeled proxy corpus.

    Cases are intentionally small and policy-shaped:
      - some exact-action regression anchors
      - some softer invariants that tuned params should preserve
    """
    cases = [
        ProxyCase(
            name="empty_hand_returns_none",
            pub=_pub(turn=1, ar=1, phasing=Side.USSR),
            hand=frozenset(),
            holds_china=False,
            expected_action=None,
        ),
        ProxyCase(
            name="scoring_action_round_ussr",
            pub=_pub(turn=1, ar=1, phasing=Side.USSR),
            hand=frozenset({1, 7}),
            holds_china=False,
            expected_card_id=1,
            expected_mode=ActionMode.EVENT,
            weight=3.0,
        ),
        ProxyCase(
            name="scoring_action_round_us",
            pub=_pub(turn=1, ar=1, phasing=Side.US),
            hand=frozenset({3, 5}),
            holds_china=False,
            expected_card_id=3,
            expected_mode=ActionMode.EVENT,
            weight=3.0,
        ),
        ProxyCase(
            name="scoring_headline_ussr",
            pub=_pub(turn=1, ar=0, phasing=Side.USSR),
            hand=frozenset({1, 7}),
            holds_china=False,
            expected_card_id=1,
            expected_mode=ActionMode.EVENT,
            weight=3.0,
        ),
        ProxyCase(
            name="scoring_headline_us",
            pub=_pub(turn=1, ar=0, phasing=Side.US),
            hand=frozenset({3, 23}),
            holds_china=False,
            expected_card_id=3,
            expected_mode=ActionMode.EVENT,
            weight=3.0,
        ),
        ProxyCase(
            name="thailand_early_war_ussr",
            pub=_pub(
                turn=1,
                ar=1,
                phasing=Side.USSR,
                influence=((Side.USSR, _VIETNAM_ID, 1),),
            ),
            hand=frozenset({15}),
            holds_china=False,
            expected_mode=ActionMode.INFLUENCE,
            required_target=_THAILAND_ID,
            weight=2.5,
        ),
        ProxyCase(
            name="conserve_china_us_early",
            pub=_pub(
                turn=1,
                ar=1,
                phasing=Side.US,
                china_held_by=Side.US,
                china_playable=True,
            ),
            hand=frozenset({6, 23}),
            holds_china=True,
            forbidden_card_id=6,
            weight=2.5,
        ),
        ProxyCase(
            name="conserve_china_ussr_early",
            pub=_pub(
                turn=2,
                ar=2,
                phasing=Side.USSR,
                china_held_by=Side.USSR,
                china_playable=True,
            ),
            hand=frozenset({6, 15}),
            holds_china=True,
            forbidden_card_id=6,
            weight=2.0,
        ),
        ProxyCase(
            name="space_offside_when_behind",
            pub=_pub(
                turn=2,
                ar=2,
                phasing=Side.USSR,
                space=(0, 2),
            ),
            hand=frozenset({5}),
            holds_china=False,
            expected_card_id=5,
            expected_mode=ActionMode.SPACE,
            weight=1.75,
        ),
        ProxyCase(
            name="space_offside_when_behind_us",
            pub=_pub(
                turn=2,
                ar=3,
                phasing=Side.US,
                space=(2, 0),
            ),
            hand=frozenset({7}),
            holds_china=False,
            expected_card_id=7,
            expected_mode=ActionMode.SPACE,
            weight=1.75,
        ),
        ProxyCase(
            name="mid_africa_entry_ussr",
            pub=_pub(
                turn=5,
                ar=3,
                phasing=Side.USSR,
                influence=((Side.USSR, 57, 1),),
            ),
            hand=frozenset({15}),
            holds_china=False,
            expected_mode=ActionMode.INFLUENCE,
            required_target=57,
            weight=1.5,
        ),
        ProxyCase(
            name="prefer_scoring_even_with_china",
            pub=_pub(
                turn=2,
                ar=1,
                phasing=Side.US,
                china_held_by=Side.US,
                china_playable=True,
            ),
            hand=frozenset({3, 6}),
            holds_china=True,
            expected_card_id=3,
            expected_mode=ActionMode.EVENT,
            weight=3.0,
        ),
        ProxyCase(
            name="headline_never_china",
            pub=_pub(
                turn=2,
                ar=0,
                phasing=Side.USSR,
                china_held_by=Side.USSR,
                china_playable=True,
            ),
            hand=frozenset({6, 15}),
            holds_china=True,
            forbidden_card_id=6,
            weight=2.0,
        ),
        ProxyCase(
            name="baseline_anchor_opening_ussr",
            pub=_pub(turn=1, ar=1, phasing=Side.USSR),
            hand=frozenset({7, 15}),
            holds_china=False,
        ),
        ProxyCase(
            name="baseline_anchor_mid_us",
            pub=_pub(turn=5, ar=2, phasing=Side.US, defcon=3, space=(0, 2)),
            hand=frozenset({4, 5}),
            holds_china=False,
        ),
        ProxyCase(
            name="baseline_anchor_late_ussr",
            pub=_pub(
                turn=8,
                ar=5,
                phasing=Side.USSR,
                defcon=4,
                milops=(0, 2),
                influence=((Side.USSR, 12, 1), (Side.USSR, 14, 1)),
            ),
            hand=frozenset({7, 15}),
            holds_china=False,
        ),
    ]

    baseline_anchored = []
    for case in cases:
        if (
            case.expected_card_id is None
            and case.forbidden_card_id is None
            and case.expected_action is None
        ):
            baseline_action = choose_minimal_hybrid(
                case.pub,
                case.hand,
                case.holds_china,
                params=DEFAULT_MINIMAL_HYBRID_PARAMS,
            )
            baseline_anchored.append(
                ProxyCase(
                    name=case.name,
                    pub=case.pub,
                    hand=case.hand,
                    holds_china=case.holds_china,
                    expected_action=baseline_action,
                    weight=1.0,
                )
            )
        else:
            baseline_anchored.append(case)
    return tuple(baseline_anchored)


def score_proxy_action(case: ProxyCase, action: ActionEncoding | None) -> float:
    """Return a normalized score in [0, 1] for one proxy case."""
    if case.expected_action is None and case.expected_card_id is None and action is None:
        return 1.0
    if action is None:
        return 0.0

    checks = 0
    passed = 0

    if case.expected_action is not None:
        checks += 1
        if action == case.expected_action:
            passed += 1
    if case.expected_card_id is not None:
        checks += 1
        if action.card_id == case.expected_card_id:
            passed += 1
    if case.forbidden_card_id is not None:
        checks += 1
        if action.card_id != case.forbidden_card_id:
            passed += 1
    if case.expected_mode is not None:
        checks += 1
        if action.mode == case.expected_mode:
            passed += 1
    if case.required_target is not None:
        checks += 1
        if case.required_target in action.targets:
            passed += 1

    if checks == 0:
        return 0.0
    return passed / checks
