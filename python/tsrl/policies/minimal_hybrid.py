"""Minimal hybrid rollout policy compatible with the current engine API.

This policy intentionally stays inside the current live-play contract:
    Policy(pub, hand, holds_china) -> ActionEncoding | None

It ranks legal ActionEncoding candidates deterministically using a small
heuristic blend of:
  - ops-first play
  - stage-based regional weighting
  - Early War Asia / Thailand bias
  - Mid War Africa / South America bias
  - restrained realignment and space usage
  - conservative early China usage
"""
from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass
from functools import lru_cache

from tsrl.engine.game_state import _ars_for_turn
from tsrl.engine.legal_actions import enumerate_actions, legal_cards
from tsrl.etl.game_data import CardSpec, CountrySpec, load_cards, load_countries
from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Region, Side

Policy = Callable[[PublicState, frozenset[int], bool], ActionEncoding | None]

_THAILAND_ID = 79
_CHINA_CARD_ID = 6
_EARLY_LAST_TURN = 3
_MID_LAST_TURN = 7
_OFFSIDE_OPS_PENALTY_BASE = 8.0
_OFFSIDE_OPS_PENALTY_PER_OP = 4.0
_NON_COUP_MILOPS_URGENCY_SCALE = 6.0
_NON_COUP_MILOPS_LATE_PENALTY = 3.0
_COUP_EXPECTED_SWING_SCALE = 6.0
_COUP_ACCESS_OPENING_BONUS = 5.0
_COUP_MILOPS_URGENCY_SCALE = 2.0
_OPENING_IRAN_COUP_BONUS = 35.0
_EMPTY_COUP_PENALTY = 15.0
_DEFCON2_BATTLEGROUND_SUICIDE_PENALTY = 1_000_000.0

_EARLY_REGION_WEIGHT = (0.85, 1.35, 1.10, 0.60, 0.55, 0.65, 1.25)
_MID_REGION_WEIGHT = (0.95, 1.00, 1.00, 0.95, 1.20, 1.20, 0.90)
_LATE_REGION_WEIGHT = (1.10, 0.95, 0.95, 1.05, 1.10, 1.00, 0.75)

_EUROPE_CORE_BONUS: frozenset[str] = frozenset({
    "France",
    "Italy",
    "West Germany",
    "East Germany",
})
_MID_WAR_ENTRY_BONUS: frozenset[str] = frozenset({
    "Angola",
    "South Africa",
    "Panama",
    "Mexico",
    "Chile",
    "Argentina",
})


@dataclass(frozen=True)
class MinimalHybridParams:
    """First-pass tunable parameters for minimal_hybrid.

    This keeps the tuning surface explicit and policy-local:
      - 21 region weights
      - action-mode priors
      - tactical bonuses / penalties
      - country-value hooks
    """

    early_region_weights: tuple[float, ...] = _EARLY_REGION_WEIGHT
    mid_region_weights: tuple[float, ...] = _MID_REGION_WEIGHT
    late_region_weights: tuple[float, ...] = _LATE_REGION_WEIGHT
    influence_mode_bonus: float = 6.0
    coup_mode_bonus: float = 4.0
    realign_mode_bonus: float = -1.0
    space_mode_bonus: float = 1.0
    ops_card_penalty: float = 0.15
    control_break_bonus: float = 5.0
    access_bonus: float = 1.5
    coup_battleground_bonus: float = 2.5
    coup_defcon2_penalty: float = -8.0
    coup_defcon3_penalty: float = -2.5
    realign_base_penalty: float = -4.0
    realign_country_scale: float = 0.55
    realign_defcon2_bonus: float = 2.0
    space_when_behind_bonus: float = 2.0
    space_early_bonus: float = 1.0
    space_offside_bonus: float = 2.0
    headline_ops_scale: float = 0.75
    headline_friendly_bonus: float = 2.0
    china_early_penalty: float = -2.5
    china_asia_target_bonus: float = 1.5
    country_region_scale: float = 5.0
    country_battleground_bonus: float = 7.0
    country_non_battleground_bonus: float = 1.0
    country_stability_scale: float = 0.6
    country_thailand_early_bonus: float = 6.0
    country_europe_core_bonus: float = 2.0
    country_mid_war_entry_bonus: float = 2.0

    def region_weight(self, stage: str, region: Region) -> float:
        if stage == "early":
            return self.early_region_weights[int(region)]
        if stage == "mid":
            return self.mid_region_weights[int(region)]
        return self.late_region_weights[int(region)]


@dataclass(frozen=True)
class ActionScoreBreakdown:
    action: ActionEncoding
    total_score: float
    mode_prior: float
    mode_detail: float
    event_score: float
    card_bias: float
    ops_penalty: float
    headline_adjustment: float
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class DecisionAnalysis:
    chosen_action: ActionEncoding | None
    legal_action_count: int
    ranked_actions: tuple[ActionScoreBreakdown, ...]


DEFAULT_MINIMAL_HYBRID_PARAMS = MinimalHybridParams()


def choose_minimal_hybrid(
    pub: PublicState,
    hand: frozenset[int],
    holds_china: bool,
    params: MinimalHybridParams = DEFAULT_MINIMAL_HYBRID_PARAMS,
) -> ActionEncoding | None:
    """Return the best legal action according to the minimal hybrid heuristic."""
    side = pub.phasing
    actions = _headline_actions(hand, pub, side, holds_china) if pub.ar == 0 else enumerate_actions(
        hand,
        pub,
        side,
        holds_china=holds_china,
    )
    if not actions:
        return None

    scored: list[tuple[ActionEncoding, float]] = []
    for action in actions:
        score = _score_action(pub, side, action, params)
        if pub.ar == 0:
            score += _headline_adjustment(side, action, params)
        scored.append((action, score))

    return min(scored, key=lambda item: _action_sort_key(item[0], item[1]))[0]


def make_minimal_hybrid_policy(
    params: MinimalHybridParams = DEFAULT_MINIMAL_HYBRID_PARAMS,
) -> Policy:
    """Return the minimal hybrid policy as a Policy-shaped callable."""

    def _policy(pub: PublicState, hand: frozenset[int], holds_china: bool) -> ActionEncoding | None:
        return choose_minimal_hybrid(pub, hand, holds_china, params=params)

    return _policy


def analyze_minimal_hybrid_decision(
    pub: PublicState,
    hand: frozenset[int],
    holds_china: bool,
    params: MinimalHybridParams = DEFAULT_MINIMAL_HYBRID_PARAMS,
    *,
    top_n: int | None = None,
) -> DecisionAnalysis:
    """Return ranked action scores and the chosen action for one decision."""
    side = pub.phasing
    actions = _headline_actions(hand, pub, side, holds_china) if pub.ar == 0 else enumerate_actions(
        hand,
        pub,
        side,
        holds_china=holds_china,
    )
    if not actions:
        return DecisionAnalysis(
            chosen_action=None,
            legal_action_count=0,
            ranked_actions=(),
        )

    ranked = tuple(
        sorted(
            (
                _score_action_breakdown(pub, side, action, params)
                for action in actions
            ),
            key=lambda item: _action_sort_key(item.action, item.total_score),
        )
    )
    if top_n is not None:
        ranked = ranked[:top_n]

    return DecisionAnalysis(
        chosen_action=ranked[0].action,
        legal_action_count=len(actions),
        ranked_actions=ranked,
    )


def _headline_actions(
    hand: frozenset[int],
    pub: PublicState,
    side: Side,
    holds_china: bool,
) -> list[ActionEncoding]:
    """Return headline candidates under the current game-loop contract."""
    playable = sorted(legal_cards(hand, pub, side, holds_china=holds_china) - {_CHINA_CARD_ID})
    cards = _cards()
    return [
        ActionEncoding(card_id=card_id, mode=ActionMode.EVENT, targets=())
        for card_id in playable
        if card_id in cards
    ]


def _score_action(
    pub: PublicState,
    side: Side,
    action: ActionEncoding,
    params: MinimalHybridParams,
) -> float:
    card = _cards()[action.card_id]
    mode = action.mode
    score = 0.0

    if mode == ActionMode.INFLUENCE:
        score += params.influence_mode_bonus
        score += _score_influence(pub, side, action.targets, params)
    elif mode == ActionMode.COUP:
        score += params.coup_mode_bonus
        score += _score_coup(pub, side, action.targets[0], card.ops, params)
    elif mode == ActionMode.REALIGN:
        score += params.realign_mode_bonus
        score += _score_realign(pub, side, action.targets, params)
    elif mode == ActionMode.SPACE:
        score += params.space_mode_bonus
        score += _score_space(pub, side, card, params)
    elif mode == ActionMode.EVENT:
        score += _score_event(side, card)

    score += _card_bias(pub, side, action, card, params)
    score -= params.ops_card_penalty * card.ops
    if action.mode != ActionMode.COUP:
        score -= _non_coup_milops_penalty(pub, side)
    return score


def _score_action_breakdown(
    pub: PublicState,
    side: Side,
    action: ActionEncoding,
    params: MinimalHybridParams,
) -> ActionScoreBreakdown:
    card = _cards()[action.card_id]
    mode_prior = 0.0
    mode_detail = 0.0
    event_score = 0.0

    if action.mode == ActionMode.INFLUENCE:
        mode_prior = params.influence_mode_bonus
        mode_detail = _score_influence(pub, side, action.targets, params)
    elif action.mode == ActionMode.COUP:
        mode_prior = params.coup_mode_bonus
        mode_detail = _score_coup(pub, side, action.targets[0], card.ops, params)
    elif action.mode == ActionMode.REALIGN:
        mode_prior = params.realign_mode_bonus
        mode_detail = _score_realign(pub, side, action.targets, params)
    elif action.mode == ActionMode.SPACE:
        mode_prior = params.space_mode_bonus
        mode_detail = _score_space(pub, side, card, params)
    elif action.mode == ActionMode.EVENT:
        event_score = _score_event(side, card)

    card_bias = _card_bias(pub, side, action, card, params)
    ops_penalty = -params.ops_card_penalty * card.ops
    headline_adjustment = _headline_adjustment(side, action, params) if pub.ar == 0 else 0.0
    total_score = (
        mode_prior
        + mode_detail
        + event_score
        + card_bias
        + ops_penalty
        + headline_adjustment
    )
    return ActionScoreBreakdown(
        action=action,
        total_score=total_score,
        mode_prior=mode_prior,
        mode_detail=mode_detail,
        event_score=event_score,
        card_bias=card_bias,
        ops_penalty=ops_penalty,
        headline_adjustment=headline_adjustment,
        notes=_action_notes(pub, side, action, card, params),
    )


def _score_influence(
    pub: PublicState,
    side: Side,
    targets: tuple[int, ...],
    params: MinimalHybridParams,
) -> float:
    score = 0.0
    seen: dict[int, int] = defaultdict(int)

    for cid in targets:
        seen[cid] += 1
        score += _country_value(pub, side, cid, params) / seen[cid]

        opp = _influence(pub, _other(side), cid)
        own = _influence(pub, side, cid)
        stability = _countries()[cid].stability

        if own < opp + stability and own + seen[cid] >= opp + stability:
            score += params.control_break_bonus
        if own == 0:
            score += params.access_bonus

    return score


def _score_coup(
    pub: PublicState,
    side: Side,
    country_id: int,
    ops: int,
    params: MinimalHybridParams,
) -> float:
    country = _countries()[country_id]
    score = _country_value(pub, side, country_id, params)
    opp_inf = _influence(pub, _other(side), country_id)
    own_inf = _influence(pub, side, country_id)

    needed_milops = max(0, pub.turn - pub.milops[int(side)])
    score += min(needed_milops, ops)
    score += _coup_expected_swing(country, ops) * _COUP_EXPECTED_SWING_SCALE
    if own_inf == 0 and opp_inf > 0:
        score += _COUP_ACCESS_OPENING_BONUS
    score += _milops_urgency(pub, side) * _COUP_MILOPS_URGENCY_SCALE
    if opp_inf == 0:
        score -= _EMPTY_COUP_PENALTY

    if country.is_battleground:
        score += params.coup_battleground_bonus
        if pub.defcon == 2:
            if _defcon2_battleground_coup_is_free(pub, side, country):
                pass
            else:
                score += params.coup_defcon2_penalty
                score -= _DEFCON2_BATTLEGROUND_SUICIDE_PENALTY
        elif pub.defcon == 3:
            score += params.coup_defcon3_penalty

    if pub.turn == 1 and side == Side.USSR and country.name == "Iran":
        score += _OPENING_IRAN_COUP_BONUS

    return score


def _score_realign(
    pub: PublicState,
    side: Side,
    targets: tuple[int, ...],
    params: MinimalHybridParams,
) -> float:
    score = params.realign_base_penalty
    for cid in targets:
        score += params.realign_country_scale * _country_value(pub, side, cid, params)
    if pub.defcon == 2:
        score += params.realign_defcon2_bonus
    return score


def _score_space(
    pub: PublicState,
    side: Side,
    card: CardSpec,
    params: MinimalHybridParams,
) -> float:
    score = 0.0
    if pub.space[int(side)] < pub.space[int(_other(side))]:
        score += params.space_when_behind_bonus
    if pub.turn <= _EARLY_LAST_TURN:
        score += params.space_early_bonus
    if card.side not in (side, Side.NEUTRAL) and not card.is_scoring:
        score += params.space_offside_bonus
    return score


def _score_event(side: Side, card: CardSpec) -> float:
    if card.is_scoring:
        return 10000.0
    if card.card_id == _CHINA_CARD_ID:
        return -10.0
    if card.side in (side, Side.NEUTRAL):
        return 1.5
    return -3.0


def _headline_adjustment(
    side: Side,
    action: ActionEncoding,
    params: MinimalHybridParams,
) -> float:
    card = _cards()[action.card_id]
    score = params.headline_ops_scale * card.ops
    if card.side in (side, Side.NEUTRAL):
        score += params.headline_friendly_bonus
    return score


def _card_bias(
    pub: PublicState,
    side: Side,
    action: ActionEncoding,
    card: CardSpec,
    params: MinimalHybridParams,
) -> float:
    score = 0.0

    if action.mode == ActionMode.EVENT:
        if card.side in (side, Side.NEUTRAL):
            score += 1.0
        else:
            score -= 3.0

    if action.mode == ActionMode.SPACE:
        if card.side not in (side, Side.NEUTRAL) and not card.is_scoring:
            score += 5.0
        if pub.space[int(side)] < pub.space[int(_other(side))]:
            score += 2.5
        if card.ops >= 4:
            score += 1.0

    if action.mode in (ActionMode.INFLUENCE, ActionMode.COUP, ActionMode.REALIGN):
        if card.side not in (side, Side.NEUTRAL) and not card.is_scoring:
            score -= _OFFSIDE_OPS_PENALTY_BASE + (_OFFSIDE_OPS_PENALTY_PER_OP * card.ops)

    if card.card_id == _CHINA_CARD_ID:
        if pub.turn <= _EARLY_LAST_TURN:
            score += params.china_early_penalty
        if any(_is_asia_or_sea(cid) for cid in action.targets):
            score += params.china_asia_target_bonus
        if action.mode == ActionMode.EVENT:
            score -= 10.0

    return score


def _country_value(
    pub: PublicState,
    side: Side,
    country_id: int,
    params: MinimalHybridParams,
) -> float:
    stage = _stage_for_turn(pub.turn)
    country = _countries()[country_id]
    score = params.country_region_scale * _region_weight(stage, country.region, params)

    if country.is_battleground:
        score += params.country_battleground_bonus
    else:
        score += params.country_non_battleground_bonus

    score += params.country_stability_scale * min(country.stability, 4)

    if country_id == _THAILAND_ID and stage == "early":
        score += params.country_thailand_early_bonus
    if country.name in _EUROPE_CORE_BONUS:
        score += params.country_europe_core_bonus
    if country.name in _MID_WAR_ENTRY_BONUS and stage == "mid":
        score += params.country_mid_war_entry_bonus

    return score


def _action_sort_key(
    action: ActionEncoding,
    score: float,
) -> tuple[float, int, int, int, tuple[int, ...]]:
    card = _cards()[action.card_id]
    scoring_event_rank = 0 if (action.mode == ActionMode.EVENT and card.is_scoring) else 1
    return (-score, scoring_event_rank, int(action.mode), action.card_id, action.targets)


def _stage_for_turn(turn: int) -> str:
    if turn <= _EARLY_LAST_TURN:
        return "early"
    if turn <= _MID_LAST_TURN:
        return "mid"
    return "late"


def _region_weight(stage: str, region: Region, params: MinimalHybridParams) -> float:
    return params.region_weight(stage, region)


def _other(side: Side) -> Side:
    return Side.US if side == Side.USSR else Side.USSR


def _remaining_ars(pub: PublicState) -> int:
    if pub.ar <= 0:
        return _ars_for_turn(pub.turn)
    return max(1, _ars_for_turn(pub.turn) - pub.ar + 1)


def _milops_shortfall(pub: PublicState, side: Side) -> int:
    return max(0, pub.turn - pub.milops[int(side)])


def _milops_urgency(pub: PublicState, side: Side) -> float:
    shortfall = _milops_shortfall(pub, side)
    if shortfall <= 0:
        return 0.0
    return shortfall / max(1, _remaining_ars(pub))


def _non_coup_milops_penalty(pub: PublicState, side: Side) -> float:
    shortfall = _milops_shortfall(pub, side)
    if shortfall <= 0 or pub.ar <= 0:
        return 0.0
    remaining = _remaining_ars(pub)
    penalty = _NON_COUP_MILOPS_URGENCY_SCALE * _milops_urgency(pub, side)
    if remaining <= 2:
        penalty += _NON_COUP_MILOPS_LATE_PENALTY * shortfall
    return penalty


def _coup_expected_swing(country: CountrySpec, ops: int) -> float:
    return max(0.0, 3.5 + ops - (2.0 * country.stability))


def _defcon2_battleground_coup_is_free(
    pub: PublicState,
    side: Side,
    country: CountrySpec,
) -> bool:
    if pub.defcon != 2 or not country.is_battleground:
        return True
    return side == Side.US and pub.nuclear_subs_active


def _influence(pub: PublicState, side: Side, country_id: int) -> int:
    return pub.influence.get((side, country_id), 0)


def _is_asia_or_sea(country_id: int) -> bool:
    region = _countries()[country_id].region
    return region in (Region.ASIA, Region.SOUTHEAST_ASIA)


def _action_notes(
    pub: PublicState,
    side: Side,
    action: ActionEncoding,
    card: CardSpec,
    params: MinimalHybridParams,
) -> tuple[str, ...]:
    notes: list[str] = []

    if action.mode == ActionMode.INFLUENCE:
        seen: dict[int, int] = defaultdict(int)
        for cid in action.targets:
            seen[cid] += 1
            country = _countries()[cid]
            notes.append(
                f"influence:{country.name}:{_country_value(pub, side, cid, params) / seen[cid]:.2f}"
            )
            opp = _influence(pub, _other(side), cid)
            own = _influence(pub, side, cid)
            stability = country.stability
            if own < opp + stability and own + seen[cid] >= opp + stability:
                notes.append(f"control_break:{country.name}")
            if own == 0:
                notes.append(f"access_touch:{country.name}")
    elif action.mode == ActionMode.COUP:
        country = _countries()[action.targets[0]]
        notes.append(f"coup_target:{country.name}")
        if country.is_battleground:
            notes.append("battleground_coup")
        needed_milops = max(0, pub.turn - pub.milops[int(side)])
        if needed_milops > 0:
            notes.append(f"milops_need:{needed_milops}")
            notes.append(f"milops_urgency:{_milops_urgency(pub, side):.2f}")
        if country.is_battleground and pub.defcon in (2, 3):
            notes.append(f"defcon_penalty:{pub.defcon}")
        if country.is_battleground and pub.defcon == 2:
            if _defcon2_battleground_coup_is_free(pub, side, country):
                notes.append("defcon2_free_battleground_coup")
            else:
                notes.append("defcon2_suicide_veto")
        if (
            _influence(pub, side, action.targets[0]) == 0
            and _influence(pub, _other(side), action.targets[0]) > 0
        ):
            notes.append("coup_access_open")
        if _influence(pub, _other(side), action.targets[0]) == 0:
            notes.append("empty_coup_penalty")
        if _coup_expected_swing(country, card.ops) > 0:
            notes.append(f"expected_swing:{_coup_expected_swing(country, card.ops):.1f}")
        if pub.turn == 1 and side == Side.USSR and country.name == "Iran":
            notes.append("opening_iran_coup_bonus")
    elif action.mode == ActionMode.REALIGN:
        if pub.defcon == 2:
            notes.append("defcon2_realign_window")
    elif action.mode == ActionMode.SPACE:
        if pub.space[int(side)] < pub.space[int(_other(side))]:
            notes.append("space_when_behind")
        if card.side not in (side, Side.NEUTRAL) and not card.is_scoring:
            notes.append("space_offside_disposal")
    elif action.mode == ActionMode.EVENT:
        if card.is_scoring:
            notes.append("forced_scoring_priority")
        elif card.side not in (side, Side.NEUTRAL):
            notes.append("offside_event")

    if card.card_id == _CHINA_CARD_ID:
        if pub.turn <= _EARLY_LAST_TURN:
            notes.append("china_early_penalty")
        if any(_is_asia_or_sea(cid) for cid in action.targets):
            notes.append("china_asia_bonus")
    if (
        action.mode != ActionMode.EVENT
        and card.side not in (side, Side.NEUTRAL)
        and not card.is_scoring
    ):
        notes.append("offside_ops_penalty")
    non_coup_penalty = _non_coup_milops_penalty(pub, side)
    if action.mode != ActionMode.COUP and non_coup_penalty > 0:
        notes.append(f"non_coup_milops_penalty:{non_coup_penalty:.2f}")
    if pub.ar == 0:
        notes.append("headline_context")

    return tuple(notes)


@lru_cache(maxsize=1)
def _cards() -> dict[int, CardSpec]:
    return load_cards()


@lru_cache(maxsize=1)
def _countries() -> dict[int, CountrySpec]:
    return load_countries()
