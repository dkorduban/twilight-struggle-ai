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

from tsrl._tscore import get_tscore
from tsrl.etl.game_data import CardSpec, CountrySpec, load_cards, load_countries
from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Region, Side

Policy = Callable[[PublicState, frozenset[int], bool], ActionEncoding | None]

_THAILAND_ID = 79
_CHINA_CARD_ID = 6
_EARLY_LAST_TURN = 3
_MID_LAST_TURN = 7
_OFFSIDE_OPS_PENALTY_BASE = 7.0
_OFFSIDE_OPS_PENALTY_PER_OP = 4.0
_NON_COUP_MILOPS_URGENCY_SCALE = 10.0
_NON_COUP_MILOPS_LATE_PENALTY = 3.0
_COUP_EXPECTED_SWING_SCALE = 5.5
_COUP_ACCESS_OPENING_BONUS = 9.0
_COUP_MILOPS_URGENCY_SCALE = 4.0
_OPENING_IRAN_COUP_BONUS = 35.0
_EMPTY_COUP_PENALTY = 15.0
_DEFCON2_BATTLEGROUND_SUICIDE_PENALTY = 1_000_000.0
_MAX_INFLUENCE_TARGETS = 86
_DEFCON3_BATTLEGROUND_SUICIDE_PENALTY = 1_000_000.0
# Non-BG coups don't lower DEFCON — explicitly reward them as the safe milops path.
# Human data: at DEFCON 3, humans do 748 non-BG coups vs only 115 BG coups.
# At DEFCON 2, humans coup exclusively in non-BG countries (Colombia, Saharan, Nicaragua).
_DEFCON3_NONBG_SAFE_COUP_BONUS = 5.0   # tip balance vs BG's higher expected swing
_DEFCON2_NONBG_SAFE_COUP_BONUS = 12.0  # strong preference when BG = certain death

# Cards whose event ALWAYS lowers DEFCON by 1.
# At DEFCON 2: triggering their event is nuclear suicide for the phasing player.
# At DEFCON 3: triggering their event brings DEFCON to 2 (very dangerous).
# Includes war cards that do free coups against BG countries — at DEFCON 2 this is instant death.
_DEFCON_LOWERING_CARDS: frozenset[int] = frozenset({
    4,   # Duck and Cover (US) — DEFCON -1, US gains VP
    53,  # We Will Bury You (USSR) — DEFCON -1, USSR gains 3 VP
    92,  # Soviets Shoot Down KAL 007 (US) — DEFCON -1, US gains 2 VP
    105, # Iran-Iraq War* — coups Iran or Iraq (both BGs) → always lowers DEFCON
    # War cards: their events do free BG coups → always lowers DEFCON when event fires.
    11,  # Korean War (USSR) — coup South Korea (BG, stab 3)
    13,  # Arab-Israeli War (USSR) — coup Israel (BG, stab 4)
    24,  # Indo-Pakistani War (USSR) — coup Pakistan or India (both BG, stab 2)
    # Additional cards confirmed to trigger DEFCON-1 from DEFCON 2 via coup/war effects:
    39,  # Brush War (USSR) — free coup in any non-BG country (lowers DEFCON)
    49,  # How I Learned to Stop Worrying (USSR) — free coup in any country
    83,  # Che (USSR) — free coup attempt in LA or Africa
    48,  # Summit — can lower DEFCON as side effect at DEFCON 2
    20,  # Olympic Games (Neutral) — boycott path drops DEFCON
    50,  # Junta (Neutral) — free coup in Central/South America
})
_DEFCON_LOWERING_SUICIDE_PENALTY = 1_000_000.0
_DEFCON_LOWERING_DEFCON3_PENALTY = 20.0  # softer: brings DEFCON to 2, not instant death

# Cards whose event has a ~100% chance of lowering DEFCON when played at low DEFCON.
# Olympic Games (20): the OPPONENT decides whether to boycott. A rational opponent
# ALWAYS boycotts at DEFCON 2 (phasing player loses). At DEFCON 3, opponent boycotts
# if it benefits them (typically yes, since DEFCON 2 is dangerous for phasing player).
# Treat as near-certain DEFCON drop at DEFCON 2, and risky at DEFCON 3.
_DEFCON_PROB_LOWERING_CARDS: frozenset[int] = frozenset({
    20,  # Olympic Games (neutral) — opponent CHOOSES boycott → DEFCON -1
})
_DEFCON_PROB_SUICIDE_PENALTY = 1_000_000.0  # at DEFCON 2, opponent always boycotts = certain death
_DEFCON_PROB_DEFCON3_PENALTY = 50.0         # at DEFCON 3, opponent likely boycotts = near-certain DEFCON 2

# Cards whose event does a random coup in a pool that includes battleground countries.
# Playing these at DEFCON 2 risks hitting a BG → DEFCON 1.
# Brush War (39): random stab-1/2 worldwide (~10-15% chance of BG).
# Che (83): 2 coups in CA/SA/Africa stab-1/2 (~25-30% chance of hitting a BG).
# Penalty is applied when fired as EVENT (own card) OR via §5.2 (opponent plays for ops).
_DEFCON_RANDOM_COUP_CARDS: frozenset[int] = frozenset({
    39,  # Brush War (USSR) — free coup in random stab-1/2 country
    83,  # Che (USSR) — two free coups in CA/SA/Africa stab-1/2 countries
})
_OPPONENT_DEFCON_BOMB_CARDS: frozenset[int] = (
    _DEFCON_LOWERING_CARDS
    | _DEFCON_PROB_LOWERING_CARDS
    | _DEFCON_RANDOM_COUP_CARDS
)
_DEFCON_RANDOM_COUP_SUICIDE_PENALTY = 1_000_000.0  # same magnitude as direct DEFCON-lowering
_DEFCON_RANDOM_COUP_DEFCON3_PENALTY = 100.0        # risky at DEFCON 3 for EVENT (random BG coup)
_DEFCON_RANDOM_COUP_DEFCON3_OPS_PENALTY = 500.0    # §5.2 at DEFCON 3: strongly prefer EVENT dump instead
_LATE_TURN_DANGEROUS_OPP_EVENT_BONUS = 120.0
_FINAL_TWO_ARS_DANGEROUS_OPP_EVENT_BONUS = 260.0

# Cat-C cards that, via §5.2, randomly discard and fire US events from the USSR hand.
# Five Year Plan (5): discards a random USSR-held card; if it's a US card, fires its event.
# Grain Sales (68): US takes a random USSR-held card and plays it.
# If USSR holds Duck and Cover (4), KAL 007 (92), etc. and DEFCON is low, this is suicide.
_CAT_C_HAND_RISKY_CARDS: frozenset[int] = frozenset({5, 68})
# The set of US-side DEFCON-lowering cards (those that fire DEFCON-1 when their event is used).
_US_DEFCON_LOWERING_CARDS: frozenset[int] = frozenset({4, 92})  # Duck and Cover, KAL 007

_EARLY_REGION_WEIGHT = (0.85, 1.35, 1.10, 0.60, 0.55, 0.65, 1.25)
_MID_REGION_WEIGHT = (0.95, 1.00, 1.00, 0.95, 1.20, 1.20, 0.90)
_LATE_REGION_WEIGHT = (1.10, 0.95, 0.95, 1.05, 1.10, 1.20, 0.75)

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
    access_bonus: float = 2.0
    coup_battleground_bonus: float = 2.5
    coup_defcon2_penalty: float = -8.0
    coup_defcon3_penalty: float = -6.0
    coup_defcon3_bg_threshold: float = 0.65
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


@dataclass(frozen=True)
class DecisionContext:
    pub: PublicState
    side: Side
    params: MinimalHybridParams
    accessible_influence: frozenset[int]
    accessible_coup: frozenset[int]
    accessible_realign: frozenset[int]
    country_values: dict[int, float]
    own_influence: dict[int, int]
    opp_influence: dict[int, int]
    stabilities: dict[int, int]
    is_asia: dict[int, bool]
    card_cache: dict[int, CardSpec]
    country_cache: dict[int, CountrySpec]


DEFAULT_MINIMAL_HYBRID_PARAMS = MinimalHybridParams()


def load_adjacency() -> dict[int, frozenset[int]]:
    tscore = get_tscore()
    return {
        int(country_id): frozenset(int(neighbor) for neighbor in neighbors)
        for country_id, neighbors in tscore.load_adjacency().items()
    }


def _ars_for_turn(turn: int) -> int:
    return int(get_tscore().ars_for_turn(turn))


def accessible_countries(
    side: Side,
    pub: PublicState,
    adj: dict[int, frozenset[int]] | None = None,
    *,
    mode: ActionMode = ActionMode.INFLUENCE,
) -> frozenset[int]:
    del adj
    return frozenset(
        int(country_id)
        for country_id in get_tscore().accessible_countries(side, pub, mode)
    )


def effective_ops(card_id: int, pub: PublicState, side: Side) -> int:
    return int(get_tscore().effective_ops(card_id, pub, side))


def enumerate_actions(
    hand: frozenset[int],
    pub: PublicState,
    side: Side,
    *,
    holds_china: bool = False,
) -> list[object]:
    return list(get_tscore().enumerate_actions(hand, pub, side, holds_china, 84))


def legal_cards(
    hand: frozenset[int],
    pub: PublicState,
    side: Side,
    *,
    holds_china: bool = False,
) -> frozenset[int]:
    return frozenset(
        int(card_id)
        for card_id in get_tscore().legal_cards(hand, pub, side, holds_china)
    )


def legal_modes(
    card_id: int,
    pub: PublicState,
    side: Side,
    *,
    adj: dict[int, frozenset[int]] | None = None,
) -> frozenset[ActionMode]:
    del adj
    return frozenset(
        ActionMode(int(mode))
        for mode in get_tscore().legal_modes(card_id, pub, side)
    )


def choose_minimal_hybrid(
    pub: PublicState,
    hand: frozenset[int],
    holds_china: bool,
    params: MinimalHybridParams = DEFAULT_MINIMAL_HYBRID_PARAMS,
) -> ActionEncoding | None:
    """Return the best legal action according to the minimal hybrid heuristic."""
    side = pub.phasing
    context = _make_decision_context(pub, side, params)
    candidates = _scored_candidate_actions(hand, holds_china, context)
    if not candidates:
        return None

    # Pre-compute: does our hand contain US DEFCON-lowering cards that Cat-C §5.2
    # could randomly discard and fire? (Checked once per call, not per-action.)
    _held_us_defcon_cards = hand & _US_DEFCON_LOWERING_CARDS

    scored: list[tuple[ActionEncoding, float]] = []
    for action, cached_score in candidates:
        score = cached_score if cached_score is not None else _score_action(context, action)
        if pub.ar == 0:
            score += _headline_adjustment(context, action)
        # Apply DEFCON safety unconditionally — INFLUENCE actions use cached scores that
        # bypass _card_bias, so this is the only place the penalty is guaranteed to fire.
        card = context.card_cache[action.card_id]
        score += _defcon_safety_penalty(context, action, card)
        # Cat-C hand-composition risk: Five Year Plan (5) and Grain Sales (68)
        # randomly discard / steal a card from our hand and fire its event.
        # - Five Year Plan: discards random USSR-held card; if US card, fires its event.
        #   Dangerous if we hold Duck and Cover (4) or KAL 007 (92).
        # - Grain Sales: US steals random card and plays it for ops (§5.2 fires if USSR card).
        #   Dangerous if we hold We Will Bury You (53).
        # This applies for BOTH EVENT mode (direct play) and non-EVENT (§5.2 trigger).
        if action.card_id in _CAT_C_HAND_RISKY_CARDS and pub.defcon <= 2:
            # US DEFCON-lowering cards in hand: Five Year Plan could fire them
            if _held_us_defcon_cards:
                hand_size_after = max(1, len(hand) - (0 if action.mode == ActionMode.EVENT else 1))
                p_disaster = len(_held_us_defcon_cards) / hand_size_after
                score -= _DEFCON_LOWERING_SUICIDE_PENALTY * p_disaster
            # USSR DEFCON-lowering cards in hand: Grain Sales could steal and fire them via §5.2
            if action.card_id == 68:  # Grain Sales specifically
                held_ussr_defcon = hand & frozenset({53})  # We Will Bury You
                if held_ussr_defcon:
                    hand_size_after = max(1, len(hand) - (0 if action.mode == ActionMode.EVENT else 1))
                    p_disaster = len(held_ussr_defcon) / hand_size_after
                    score -= _DEFCON_LOWERING_SUICIDE_PENALTY * p_disaster
        scored.append((action, score))

    # Grain Sales (#68, US card): §5.2 fires → US steals random USSR card and plays it.
    # Suicidal if USSR hand contains WWBY (#53, DEFCON-1) OR Brush War/Che (random BG coup).
    _grain_sales_risky_cards = hand & (frozenset({53}) | _DEFCON_RANDOM_COUP_CARDS)
    grain_sales_suicidal = pub.defcon <= 2 and bool(_grain_sales_risky_cards)
    safe = [
        (action, score)
        for action, score in scored
        if not _is_suicidal_action(action, context.card_cache[action.card_id], pub, side)
        and not (grain_sales_suicidal and action.card_id == 68)
    ]
    if safe:
        final_pool = safe
    else:
        tier2 = [
            (action, score)
            for action, score in scored
            if not (action.mode == ActionMode.COUP and pub.defcon <= 2)
        ]
        final_pool = tier2 if tier2 else scored
    return min(final_pool, key=lambda item: _action_sort_key(item[0], item[1]))[0]


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
    context = _make_decision_context(pub, side, params)
    actions = _candidate_actions(hand, holds_china, context)
    if not actions:
        return DecisionAnalysis(
            chosen_action=None,
            legal_action_count=0,
            ranked_actions=(),
        )

    ranked = tuple(
        sorted(
            (
                _score_action_breakdown(context, action)
                for action in actions
            ),
            key=lambda item: _action_sort_key(item.action, item.total_score),
        )
    )
    safe_ranked = tuple(
        item
        for item in ranked
        if not _is_suicidal_action(
            item.action,
            context.card_cache[item.action.card_id],
            pub,
            side,
        )
    )
    final_ranked = safe_ranked if safe_ranked else ranked
    if top_n is not None:
        final_ranked = final_ranked[:top_n]

    return DecisionAnalysis(
        chosen_action=final_ranked[0].action,
        legal_action_count=_legal_action_count(pub, hand, side, holds_china),
        ranked_actions=final_ranked,
    )


def _make_decision_context(
    pub: PublicState,
    side: Side,
    params: MinimalHybridParams,
) -> DecisionContext:
    country_cache = _countries()
    other_side = _other(side)
    stage = _stage_for_turn(pub.turn)

    if pub.ar == 0:
        accessible_influence = frozenset()
        accessible_coup = frozenset()
        accessible_realign = frozenset()
    else:
        adjacency = _adjacency()
        accessible_influence = frozenset(
            accessible_countries(side, pub, adjacency, mode=ActionMode.INFLUENCE)
        )
        accessible_coup = frozenset(
            accessible_countries(side, pub, adjacency, mode=ActionMode.COUP)
        )
        accessible_realign = frozenset(
            accessible_countries(side, pub, adjacency, mode=ActionMode.REALIGN)
        )

    own_influence: dict[int, int] = {}
    opp_influence: dict[int, int] = {}
    stabilities: dict[int, int] = {}
    is_asia: dict[int, bool] = {}
    country_values: dict[int, float] = {}

    for country_id, country in country_cache.items():
        own_influence[country_id] = pub.influence.get((side, country_id), 0)
        opp_influence[country_id] = pub.influence.get((other_side, country_id), 0)
        stabilities[country_id] = country.stability
        is_asia[country_id] = country.region in (Region.ASIA, Region.SOUTHEAST_ASIA)
        country_values[country_id] = _country_value_from_spec(stage, country_id, country, params)

    return DecisionContext(
        pub=pub,
        side=side,
        params=params,
        accessible_influence=accessible_influence,
        accessible_coup=accessible_coup,
        accessible_realign=accessible_realign,
        country_values=country_values,
        own_influence=own_influence,
        opp_influence=opp_influence,
        stabilities=stabilities,
        is_asia=is_asia,
        card_cache=_cards(),
        country_cache=country_cache,
    )


def _candidate_actions(
    hand: frozenset[int],
    holds_china: bool,
    context: DecisionContext,
) -> list[ActionEncoding]:
    return [action for action, _cached_score in _scored_candidate_actions(hand, holds_china, context)]


def _scored_candidate_actions(
    hand: frozenset[int],
    holds_china: bool,
    context: DecisionContext,
) -> list[tuple[ActionEncoding, float | None]]:
    pub = context.pub
    side = context.side
    if pub.ar == 0:
        return [
            (action, None)
            for action in _headline_actions(hand, pub, side, holds_china)
        ]

    adjacency = _adjacency()
    actions: list[tuple[ActionEncoding, float | None]] = []
    playable = sorted(legal_cards(hand, pub, side, holds_china=holds_china))
    accessible_coup = tuple(sorted(context.accessible_coup))
    accessible_realign = _limited_accessible(context.accessible_realign)
    accessible_influence = _limited_accessible(context.accessible_influence)

    for card_id in playable:
        if card_id not in context.card_cache:
            continue

        for mode in legal_modes(card_id, pub, side, adj=adjacency):
            if mode == ActionMode.SPACE:
                actions.append((ActionEncoding(card_id=card_id, mode=mode, targets=()), None))
                continue

            if mode == ActionMode.EVENT:
                actions.append((ActionEncoding(card_id=card_id, mode=mode, targets=()), None))
                continue

            if mode == ActionMode.COUP:
                if not accessible_coup:
                    continue
                for country_id in accessible_coup:
                    actions.append((
                        ActionEncoding(
                            card_id=card_id,
                            mode=mode,
                            targets=(country_id,),
                        ),
                        None,
                    ))
                continue

            if mode == ActionMode.REALIGN:
                if not accessible_realign:
                    continue
                action = _best_realign_action(card_id, accessible_realign, context)
                if action is not None:
                    actions.append((action, None))
                continue

            if not accessible_influence:
                continue
            action, score = _best_influence_action_dp(card_id, accessible_influence, context)
            actions.append((action, score))

    return actions


def _best_realign_action(
    card_id: int,
    accessible: tuple[int, ...],
    context: DecisionContext,
) -> ActionEncoding | None:
    if not accessible:
        return None

    country_values = {
        country_id: _country_value(context, country_id)
        for country_id in accessible
    }
    best_value = max(country_values.values())
    scored: list[tuple[ActionEncoding, float]] = []

    for country_id in accessible:
        if country_values[country_id] != best_value:
            continue
        action = ActionEncoding(
            card_id=card_id,
            mode=ActionMode.REALIGN,
            targets=(country_id,),
        )
        scored.append((action, _score_action(context, action)))

    return min(scored, key=lambda item: _action_sort_key(item[0], item[1]))[0]


def _best_influence_action_dp(
    card_id: int,
    accessible: tuple[int, ...],
    context: DecisionContext,
) -> tuple[ActionEncoding, float]:
    base_action = ActionEncoding(card_id=card_id, mode=ActionMode.INFLUENCE, targets=())
    if not accessible:
        return base_action, _score_influence_action(context, base_action)

    ops = effective_ops(card_id, context.pub, context.side)
    dp: list[list[list[tuple[ActionEncoding, float] | None]]] = [
        [[None, None] for _ in range(ops + 1)]
        for _ in range(len(accessible) + 1)
    ]
    dp[0][0][0] = (base_action, _score_influence_action(context, base_action))

    for index, country_id in enumerate(accessible, start=1):
        country_is_asia = _is_asia_or_sea(context, country_id)
        for used_ops in range(ops + 1):
            for has_asia in (0, 1):
                previous = dp[index - 1][used_ops][has_asia]
                if previous is None:
                    continue

                previous_action, previous_score = previous
                max_allocation = ops - used_ops
                for allocation in range(max_allocation + 1):
                    next_targets = previous_action.targets + ((country_id,) * allocation)
                    next_action = ActionEncoding(
                        card_id=card_id,
                        mode=ActionMode.INFLUENCE,
                        targets=next_targets,
                    )
                    next_has_asia = has_asia or (country_is_asia and allocation > 0)
                    next_score = _score_influence_action(context, next_action)
                    current = dp[index][used_ops + allocation][int(next_has_asia)]
                    candidate_key = _action_sort_key(next_action, next_score)
                    current_key = (
                        None if current is None else _action_sort_key(current[0], current[1])
                    )
                    if current is None or candidate_key < current_key:
                        dp[index][used_ops + allocation][int(next_has_asia)] = (
                            next_action,
                            next_score,
                        )

    best = dp[len(accessible)][ops][0]
    with_asia = dp[len(accessible)][ops][1]
    if with_asia is not None and (
        best is None
        or _action_sort_key(with_asia[0], with_asia[1]) < _action_sort_key(best[0], best[1])
    ):
        best = with_asia
    if best is None:
        return base_action, _score_influence_action(context, base_action)
    return best


def _legal_action_count(
    pub: PublicState,
    hand: frozenset[int],
    side: Side,
    holds_china: bool,
) -> int:
    if pub.ar == 0:
        return len(_headline_actions(hand, pub, side, holds_china))
    return len(enumerate_actions(hand, pub, side, holds_china=holds_china))


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
    context: DecisionContext,
    action: ActionEncoding,
) -> float:
    card = context.card_cache[action.card_id]
    mode = action.mode
    score = 0.0

    if mode == ActionMode.INFLUENCE:
        best_action, best_score = _best_influence_action_dp(
            action.card_id,
            _limited_accessible(context.accessible_influence),
            context,
        )
        if action.targets == best_action.targets:
            return best_score
        return _score_influence_action(context, action)
    elif mode == ActionMode.COUP:
        score += context.params.coup_mode_bonus
        score += _score_coup(context, action.targets[0], card.ops)
    elif mode == ActionMode.REALIGN:
        score += context.params.realign_mode_bonus
        score += _score_realign(context, action.targets)
    elif mode == ActionMode.SPACE:
        score += context.params.space_mode_bonus
        score += _score_space(context, card)
    elif mode == ActionMode.EVENT:
        score += _score_event(context.side, card)

    score += _card_bias(context, action, card)
    score -= context.params.ops_card_penalty * card.ops
    if action.mode != ActionMode.COUP:
        score -= _non_coup_milops_penalty(context.pub, context.side)
    return score


def _score_action_breakdown(
    context: DecisionContext,
    action: ActionEncoding,
) -> ActionScoreBreakdown:
    card = context.card_cache[action.card_id]
    mode_prior = 0.0
    mode_detail = 0.0
    event_score = 0.0

    if action.mode == ActionMode.INFLUENCE:
        mode_prior = context.params.influence_mode_bonus
        mode_detail = _score_influence(context, action.targets)
    elif action.mode == ActionMode.COUP:
        mode_prior = context.params.coup_mode_bonus
        mode_detail = _score_coup(context, action.targets[0], card.ops)
    elif action.mode == ActionMode.REALIGN:
        mode_prior = context.params.realign_mode_bonus
        mode_detail = _score_realign(context, action.targets)
    elif action.mode == ActionMode.SPACE:
        mode_prior = context.params.space_mode_bonus
        mode_detail = _score_space(context, card)
    elif action.mode == ActionMode.EVENT:
        event_score = _score_event(context.side, card)

    card_bias = _card_bias(context, action, card)
    ops_penalty = -context.params.ops_card_penalty * card.ops
    headline_adjustment = _headline_adjustment(context, action) if context.pub.ar == 0 else 0.0
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
        notes=_action_notes(context, action, card),
    )


def _score_influence(
    context: DecisionContext,
    targets: tuple[int, ...],
) -> float:
    score = 0.0
    seen: dict[int, int] = defaultdict(int)

    for cid in targets:
        seen[cid] += 1
        score += _country_value(context, cid) / seen[cid]

        opp = _influence(context, _other(context.side), cid)
        own = _influence(context, context.side, cid)
        stability = context.stabilities[cid]

        if own < opp + stability and own + seen[cid] >= opp + stability:
            score += context.params.control_break_bonus
        if own == 0:
            score += context.params.access_bonus

    return score


def _score_influence_action(
    context: DecisionContext,
    action: ActionEncoding,
) -> float:
    card = context.card_cache[action.card_id]
    score = context.params.influence_mode_bonus
    score += _score_influence(context, action.targets)
    score += _card_bias(context, action, card)
    score -= context.params.ops_card_penalty * card.ops
    score -= _non_coup_milops_penalty(context.pub, context.side)
    return score


def _influence_allocation_delta(
    context: DecisionContext,
    country_id: int,
    allocation: int,
) -> float:
    if allocation <= 0:
        return 0.0

    score = 0.0
    country_value = _country_value(context, country_id)
    own = _influence(context, context.side, country_id)
    opp = _influence(context, _other(context.side), country_id)
    stability = context.stabilities[country_id]

    for seen in range(1, allocation + 1):
        score += country_value / seen
        if own < opp + stability and own + seen >= opp + stability:
            score += context.params.control_break_bonus
        if own == 0:
            score += context.params.access_bonus

    return score


def _score_coup(
    context: DecisionContext,
    country_id: int,
    ops: int,
) -> float:
    pub = context.pub
    side = context.side
    country = context.country_cache[country_id]
    score = _country_value(context, country_id)
    opp_inf = _influence(context, _other(side), country_id)
    own_inf = _influence(context, side, country_id)

    needed_milops = max(0, pub.turn - pub.milops[int(side)])
    score += min(needed_milops, ops)
    score += _coup_expected_swing(country, ops) * _COUP_EXPECTED_SWING_SCALE
    if own_inf == 0 and opp_inf > 0:
        score += _COUP_ACCESS_OPENING_BONUS
    score += _milops_urgency(pub, side) * _COUP_MILOPS_URGENCY_SCALE
    if opp_inf == 0:
        score -= _EMPTY_COUP_PENALTY

    if country.is_battleground:
        score += context.params.coup_battleground_bonus
        if pub.defcon == 2:
            if _defcon2_battleground_coup_is_free(pub, side, country):
                pass
            else:
                score += context.params.coup_defcon2_penalty
                score -= _DEFCON2_BATTLEGROUND_SUICIDE_PENALTY
        elif pub.defcon == 3:
            score += context.params.coup_defcon3_penalty
            if _milops_urgency(pub, side) < context.params.coup_defcon3_bg_threshold:
                score -= _DEFCON3_BATTLEGROUND_SUICIDE_PENALTY
    else:
        # Non-BG coups never lower DEFCON — reward them as the safe milops path.
        # Human data shows 748 non-BG vs 115 BG coups at DEFCON 3.
        if pub.defcon == 3:
            score += _DEFCON3_NONBG_SAFE_COUP_BONUS
        elif pub.defcon == 2:
            score += _DEFCON2_NONBG_SAFE_COUP_BONUS

    if pub.turn == 1 and side == Side.USSR and country.name == "Iran":
        score += _OPENING_IRAN_COUP_BONUS

    return score


def _score_realign(
    context: DecisionContext,
    targets: tuple[int, ...],
) -> float:
    score = context.params.realign_base_penalty
    for cid in targets:
        score += context.params.realign_country_scale * _country_value(context, cid)
    if context.pub.defcon == 2:
        score += context.params.realign_defcon2_bonus
    return score


def _score_space(
    context: DecisionContext,
    card: CardSpec,
) -> float:
    pub = context.pub
    side = context.side
    score = 0.0
    if pub.space[int(side)] < pub.space[int(_other(side))]:
        score += context.params.space_when_behind_bonus
    if pub.turn <= _EARLY_LAST_TURN:
        score += context.params.space_early_bonus
    if card.side not in (side, Side.NEUTRAL) and not card.is_scoring:
        score += context.params.space_offside_bonus
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
    context: DecisionContext,
    action: ActionEncoding,
) -> float:
    card = context.card_cache[action.card_id]
    score = context.params.headline_ops_scale * card.ops
    if card.side in (context.side, Side.NEUTRAL):
        score += context.params.headline_friendly_bonus
    return score


def _defcon_safety_penalty(
    context: DecisionContext,
    action: ActionEncoding,
    card: CardSpec,
) -> float:
    """Return a large negative penalty for actions that risk nuclear war.

    This function is applied unconditionally to every candidate action,
    including INFLUENCE whose scores are pre-cached by _best_influence_action_dp
    and therefore bypass the main _card_bias path.
    """
    pub = context.pub
    side = context.side
    penalty = 0.0

    if action.mode == ActionMode.EVENT:
        if action.card_id in _DEFCON_LOWERING_CARDS:
            if pub.defcon <= 2:
                penalty -= _DEFCON_LOWERING_SUICIDE_PENALTY
            elif pub.defcon == 3:
                if card.side not in (side, Side.NEUTRAL):
                    # Opponent's DEFCON-lowering card at DEFCON 3: dump it now via EVENT.
                    # Firing it drops DEFCON to 2, but DEFCON recovers at end of turn.
                    # Holding it until DEFCON 2 = forced nuclear war.  Forward-looking
                    # bonus that beats typical influence plays (~20 pts).
                    penalty += 50.0
                else:
                    # Own DEFCON-lowering card: penalty for voluntarily lowering DEFCON.
                    penalty -= _DEFCON_LOWERING_DEFCON3_PENALTY
            elif pub.defcon >= 4 and card.side not in (side, Side.NEUTRAL):
                # "Dump early" bonus: fire opponent's DEFCON-lowering card as EVENT now
                # while DEFCON is high, rather than risk forced suicide at DEFCON 2.
                # DEFCON 5: nearly free (no VP loss, DEFCON recovers end of turn).
                # DEFCON 4: small VP cost — far better than game-ending at DEFCON 2.
                # These must be large enough to beat valuable influence/coup plays.
                penalty += 200.0 if pub.defcon >= 5 else 100.0
        if action.card_id in _DEFCON_PROB_LOWERING_CARDS:
            if pub.defcon <= 2:
                penalty -= _DEFCON_PROB_SUICIDE_PENALTY
            elif pub.defcon == 3:
                penalty -= _DEFCON_PROB_DEFCON3_PENALTY
        # Brush War / Che: their events do random coups that may hit battlegrounds.
        if action.card_id in _DEFCON_RANDOM_COUP_CARDS:
            if pub.defcon <= 2:
                penalty -= _DEFCON_RANDOM_COUP_SUICIDE_PENALTY
            elif pub.defcon == 3:
                penalty -= _DEFCON_RANDOM_COUP_DEFCON3_PENALTY
    else:
        # §5.2: playing any opponent card for ops/space fires the opponent's event.
        if card.side not in (side, Side.NEUTRAL):
            if action.card_id in _DEFCON_LOWERING_CARDS:
                if pub.defcon <= 2:
                    penalty -= _DEFCON_LOWERING_SUICIDE_PENALTY
                elif pub.defcon == 3:
                    # Using opponent DEFCON-lowering card for ops at DEFCON 3:
                    # same DEFCON consequence as EVENT dump but WITHOUT the priority benefit.
                    # Large penalty to force EVENT dump instead.
                    penalty -= 200.0
                # Ops modes at DEFCON 4-5: penalise hard to push toward EVENT (dump early).
                # Must overcome the value of influence plays in contested countries.
                elif pub.defcon >= 4:
                    penalty -= 150.0
            if action.card_id in _DEFCON_PROB_LOWERING_CARDS:
                if pub.defcon <= 2:
                    penalty -= _DEFCON_PROB_SUICIDE_PENALTY
                elif pub.defcon == 3:
                    penalty -= _DEFCON_PROB_DEFCON3_PENALTY
            if action.card_id in _DEFCON_RANDOM_COUP_CARDS:
                if pub.defcon <= 2:
                    penalty -= _DEFCON_RANDOM_COUP_SUICIDE_PENALTY
                    if action.mode == ActionMode.COUP:
                        penalty -= _DEFCON_RANDOM_COUP_SUICIDE_PENALTY
                elif pub.defcon == 3:
                    # Non-EVENT ops at DEFCON 3 triggers §5.2 → random BG coup without the
                    # strategic benefit of dumping the card early.  Heavily penalise to force
                    # EVENT dump instead (which fires the same risk but retires the card).
                    penalty -= _DEFCON_RANDOM_COUP_DEFCON3_OPS_PENALTY

    return penalty


def _card_bias(
    context: DecisionContext,
    action: ActionEncoding,
    card: CardSpec,
) -> float:
    pub = context.pub
    side = context.side
    score = 0.0

    if action.mode == ActionMode.EVENT:
        if card.side in (side, Side.NEUTRAL):
            score += 1.0
        else:
            score -= 3.0
        # DEFCON safety for EVENT mode is handled by _defcon_safety_penalty (applied globally).

        # "Dump early" bonus: proactively fire an opponent's DEFCON-lowering card as EVENT
        # while DEFCON is still high, before we risk being stuck with it at DEFCON 2.
        # At DEFCON 5: costs 0 VP, DEFCON recovers end of turn — almost free.
        # At DEFCON 4: costs ~1 VP max — much better than forced suicide at DEFCON 2.
        # At DEFCON 3: brings DEFCON to 2, but STILL BETTER than holding until DEFCON 2
        #   (because at DEFCON 2 the card causes forced nuclear war on any mode).
        if card.side not in (side, Side.NEUTRAL) and action.card_id in _DEFCON_LOWERING_CARDS:
            if pub.defcon >= 5:
                score += 150.0  # nearly free: DEFCON recovers, minimal VP loss
            elif pub.defcon == 4:
                score += 80.0   # small cost, strongly prefer over holding until DEFCON 2
            elif pub.defcon == 3:
                score += 40.0   # dumps to DEFCON 2 now, but avoids -1M forced suicide later
        # Brush War / Che: random coups can suicide at low DEFCON — dump early too.
        # At DEFCON 3, the safety penalty is -100 but the EXPECTED cost of holding until DEFCON 2
        # is far larger (forced suicide risk).  Needs a large bonus to override the penalty.
        if card.side not in (side, Side.NEUTRAL) and action.card_id in _DEFCON_RANDOM_COUP_CARDS:
            if pub.defcon >= 5:
                score += 80.0
            elif pub.defcon == 4:
                score += 120.0  # decisively prefer dump over own-card COUP (+30)
            elif pub.defcon == 3:
                score += 300.0  # must override -100 safety penalty + beat own-card options

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

    # At DEFCON 3, holding an opponent DEFCON-lowering or random-coup card is a ticking bomb.
    # If DEFCON drops to 2 before it's played (via BG coup), ALL modes become -1M forced suicide.
    # Apply a priority bonus to play it NOW (any mode) while DEFCON is still 3.
    if pub.defcon == 3 and card.side not in (side, Side.NEUTRAL):
        if action.card_id in _DEFCON_LOWERING_CARDS:
            score += 50.0  # strong: play it now before DEFCON can drop further
        elif action.card_id in _DEFCON_RANDOM_COUP_CARDS:
            score += 30.0  # similar risk: random coup may hit BG and drop DEFCON to 2

    if (
        pub.defcon >= 3
        and pub.ar > 0
        and card.side not in (side, Side.NEUTRAL)
        and action.card_id in _OPPONENT_DEFCON_BOMB_CARDS
    ):
        remaining = _remaining_ars(pub)
        if remaining <= 3:
            urgency = _LATE_TURN_DANGEROUS_OPP_EVENT_BONUS
            if remaining <= 2:
                urgency += _FINAL_TWO_ARS_DANGEROUS_OPP_EVENT_BONUS
            if action.mode == ActionMode.EVENT:
                score += urgency
            else:
                score -= urgency

    # DEFCON safety for non-EVENT §5.2 cases is handled by _defcon_safety_penalty (applied globally).

    if card.card_id == _CHINA_CARD_ID:
        if pub.turn <= _EARLY_LAST_TURN:
            score += context.params.china_early_penalty
        if any(_is_asia_or_sea(context, cid) for cid in action.targets):
            score += context.params.china_asia_target_bonus
        if action.mode == ActionMode.EVENT:
            score -= 10.0

    return score


def _country_value(
    context: DecisionContext,
    country_id: int,
) -> float:
    return context.country_values[country_id]


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


def _country_value_from_spec(
    stage: str,
    country_id: int,
    country: CountrySpec,
    params: MinimalHybridParams,
) -> float:
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


def _limited_accessible(accessible: frozenset[int]) -> tuple[int, ...]:
    return tuple(sorted(accessible))[:_MAX_INFLUENCE_TARGETS]


def _other(side: Side) -> Side:
    return Side.US if side == Side.USSR else Side.USSR


@lru_cache(maxsize=1)
def _adjacency():
    return load_adjacency()


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


def _is_suicidal_action(
    action: ActionEncoding,
    card: CardSpec,
    pub: PublicState,
    side: Side,
) -> bool:
    # Headline picks are always executed as EVENT, regardless of the policy's chosen mode.
    if pub.ar == 0:
        if action.card_id in _DEFCON_RANDOM_COUP_CARDS and pub.defcon <= 3:
            return True
        if action.card_id in _DEFCON_LOWERING_CARDS and pub.defcon <= 2:
            return True
        if action.card_id in _DEFCON_PROB_LOWERING_CARDS and pub.defcon <= 2:
            return True

    # SPACE mode never triggers §5.2 — the card goes directly to the space track
    # without firing any event. Always safe regardless of card content.
    if action.mode == ActionMode.SPACE:
        return False

    if action.mode == ActionMode.COUP:
        country = _countries()[action.targets[0]]
        # Direct suicide: BG coup at DEFCON=2 lowers DEFCON to 1.
        if (
            pub.defcon <= 2
            and country.is_battleground
            and not _defcon2_battleground_coup_is_free(pub, side, country)
        ):
            return True
        # §5.2 suicide: opponent's Brush War / Che played as COUP (any target) at DEFCON=2.
        # The §5.2 rule fires their event — a random BG coup — which will lower DEFCON to 1.
        if (
            pub.defcon <= 2
            and card.side not in (side, Side.NEUTRAL)
            and action.card_id
            in (
                _DEFCON_RANDOM_COUP_CARDS
                | _DEFCON_LOWERING_CARDS
                | _CAT_C_HAND_RISKY_CARDS
            )
        ):
            return True
        return False

    if pub.defcon > 2:
        return False

    if action.mode == ActionMode.EVENT:
        if action.card_id == 83 and pub.defcon <= 3:
            return True
        if action.card_id == 39 and pub.defcon <= 2:
            return True
        # Cat-C cards randomly interact with the opponent hand when their event fires.
        # At DEFCON 2, that can reveal and fire a DEFCON-lowering event immediately.
        if action.card_id in _CAT_C_HAND_RISKY_CARDS and pub.defcon <= 2:
            return True
        return (
            action.card_id in _DEFCON_LOWERING_CARDS
            or action.card_id in _DEFCON_PROB_LOWERING_CARDS
        )

    if card.side in (side, Side.NEUTRAL):
        return False

    if (
        action.card_id in _CAT_C_HAND_RISKY_CARDS
        and action.mode != ActionMode.EVENT
        and pub.defcon <= 2
    ):
        return True

    return (
        action.card_id in _DEFCON_LOWERING_CARDS
        or action.card_id in _DEFCON_RANDOM_COUP_CARDS
        or action.card_id in _DEFCON_PROB_LOWERING_CARDS
    )


def _influence(context: DecisionContext, side: Side, country_id: int) -> int:
    if side == context.side:
        return context.own_influence[country_id]
    return context.opp_influence[country_id]


def _is_asia_or_sea(context: DecisionContext, country_id: int) -> bool:
    return context.is_asia[country_id]


def _action_notes(
    context: DecisionContext,
    action: ActionEncoding,
    card: CardSpec,
) -> tuple[str, ...]:
    pub = context.pub
    side = context.side
    notes: list[str] = []

    if action.mode == ActionMode.INFLUENCE:
        seen: dict[int, int] = defaultdict(int)
        for cid in action.targets:
            seen[cid] += 1
            country = context.country_cache[cid]
            notes.append(
                f"influence:{country.name}:{_country_value(context, cid) / seen[cid]:.2f}"
            )
            opp = _influence(context, _other(side), cid)
            own = _influence(context, side, cid)
            stability = context.stabilities[cid]
            if own < opp + stability and own + seen[cid] >= opp + stability:
                notes.append(f"control_break:{country.name}")
            if own == 0:
                notes.append(f"access_touch:{country.name}")
    elif action.mode == ActionMode.COUP:
        country = context.country_cache[action.targets[0]]
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
            _influence(context, side, action.targets[0]) == 0
            and _influence(context, _other(side), action.targets[0]) > 0
        ):
            notes.append("coup_access_open")
        if _influence(context, _other(side), action.targets[0]) == 0:
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
        if any(_is_asia_or_sea(context, cid) for cid in action.targets):
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
