# Twilight Struggle rollout policy pseudocode (revised from TwilightStrategy.com)
#
# This version intentionally changes the earlier pseudocode in 7 important ways:
# 1) EVENTS are now scored more conservatively; Ops are the default efficient currency.
# 2) SPACE is now sparse; only catastrophic / unmitigable cards or bonus-track situations get spaced.
# 3) REALIGNMENTS are now mostly DEFCON-2 / access-kill / +1-modifier plays.
# 4) REGION weights are stage-based: Asia/Thailand early, Africa/South America mid, Europe mostly emergency/static, Central America usually lower.
# 5) CHINA is now treated as: Asia hammer + hand-flex insurance + late-game VP swing, not just "generic 4 Ops".
# 6) AR7/AR6 control-breaks are explicit objectives, but filtered by "does this just hand the opponent a profitable coup/access?".
# 7) OVERCONTROL is no longer penalized blindly; some battlegrounds want a prophylactic buffer (Thailand, Nigeria/Zaire/Angola, hot Asia battlegrounds).

## 0. Core philosophy

# "Events create opportunities; Operations exploit them."
# Therefore:
# - default stance = prefer Ops
# - event play must earn its keep by doing something Ops struggle to do:
#   * open a closed region
#   * remove opponent access
#   * break a stalemate / flip a hard control
#   * create multiple actions / tempo
#   * swing urgent scoring
#   * create a major VP swing
#
# Also:
# - do not over-space
# - do not over-realign
# - do not over-chase Europe unless there is a real scoring/control emergency
# - do not underweight Thailand / Early War Asia
# - do not underweight Africa / South America in the Mid War


## 1. Data model

enum Side:
  US
  USSR

enum Stage:
  EARLY
  MID
  LATE

enum Phase:
  HEADLINE
  ACTION_ROUND
  END_TURN

enum ActionType:
  PLAY_SCORING
  PLAY_EVENT
  PLAY_OPS_INFLUENCE
  PLAY_OPS_COUP
  PLAY_OPS_REALIGN_SEQUENCE
  SPACE_CARD
  PLAY_CHINA_INFLUENCE
  PLAY_CHINA_COUP
  PLAY_CHINA_REALIGN_SEQUENCE
  HEADLINE_CARD

enum Region:
  EUROPE
  ASIA
  MIDDLE_EAST
  CENTRAL_AMERICA
  SOUTH_AMERICA
  AFRICA
  SOUTHEAST_ASIA

enum RegionPosture:
  ATTACK
  DEFEND
  DENY_DOM
  MAINTAIN_DOM
  HOT_BG_LOCK
  STATIC_THRESHOLD_DEFENSE

struct Card:
  id
  name
  ops
  alignment: Side | NEUTRAL
  is_scoring: bool
  scoring_region: Region | null
  removed_after_event: bool
  is_china: bool
  can_space: bool

struct Country:
  name
  stability
  battleground: bool
  regions: set[Region]
  influence[Side]: int
  neighbors: list[CountryName]
  adjacent_to_superpower[Side]: bool

struct PersistentEffects:
  flags
  space_bonus_reveal_headline[Side]: bool
  extra_space_attempt[Side]: bool
  region_op_bonus           # e.g. Vietnam Revolts-style / card-hook-driven
  coup_modifiers
  realign_modifiers
  placement_modifiers

struct State:
  turn: int
  ar: int
  phase: Phase
  side_to_move: Side
  stage: Stage
  vp: int
  defcon: int
  milops[Side]: int
  space_pos[Side]: int
  space_attempts_used[Side]: int
  china_owner: Side
  china_face_up: bool
  hand[Side]: list[Card]
  countries: map[CountryName, Country]
  effects: PersistentEffects
  discard_pile
  removed_pile
  recent_actions
  sampled_hidden_info      # for determinized rollout if needed

struct Action:
  type: ActionType
  card: Card | null

  # scoring
  scoring_region: Region | null

  # influence
  placements: list[(CountryName, count)]

  # coup
  target_country: CountryName | null

  # realignment
  realign_targets: list[CountryName]

  # only relevant when opponent event is triggered by Ops
  event_timing: BEFORE_OPS | AFTER_OPS | NONE

  tags: set[string]


## 2. Weights

struct Weights:
  ILLEGAL_PENALTY                 = -1e15
  AUTO_LOSS_PENALTY               = -1e15

  # hard urgency
  MUST_PLAY_SCORING_BONUS         = +60000
  EUROPE_INSTANT_WIN_BONUS        = +45000
  EUROPE_INSTANT_LOSS_PENALTY     = -45000
  BAD_SPACE_DISPOSAL_BONUS        = +9000
  MILOPS_EMERGENCY_BONUS          = +2500
  THAILAND_EMERGENCY_BONUS        = +3000
  AR7_BREAK_CONTROL_BONUS         = +2200

  # global terms
  IMMEDIATE_VP                    = 30
  SCORING_REPAIR                  = 26
  BG_SWING                        = 15
  DOMINATION_SWING                = 13
  COUNTRY_COUNT_DENIAL            = 11
  ACCESS_CREATION                 = 10
  ACCESS_DENIAL                   = 11
  DEFENSE_BUFFER                  = 8
  MILOPS_PROGRESS                 = 8
  TEMPO_SWING                     = 8
  CHINA_ASIA_SYNERGY              = 8
  HOT_BG_LOCK                     = 10

  # penalties
  DEFCON_MOBILITY_LOSS            = -20
  LIVE_OFFSIDE_EVENT_COST         = -24
  WASTED_OPS                      = -16
  BLIND_OVERCONTROL               = -8
  SPACE_OPPORTUNITY_COST          = -15
  NON_GAMECHANGER_EVENT_OPPORTUNITY_COST = -12
  BAD_REALIGNMENT_PENALTY         = -20
  BAD_HEADLINE_SCORING_PENALTY    = -18
  CHINA_T1_HOLD_RISK_PENALTY      = -25
  PROFITABLE_ACCESS_COUP_PENALTY  = -18

  # sampling
  TOP_K_ACTIONS                   = 6
  TEMP_CALM                       = 0.45
  TEMP_URGENT                     = 0.20
  TEMP_EMERGENCY                  = 0.08


## 3. Urgency state

struct Urgency:
  stage: Stage
  ars_left: int
  must_play_scoring_regions: list[Region]
  region_weight: map[Region, float]
  region_posture: map[Region, RegionPosture]
  europe_emergency: float
  thailand_emergency: float
  milops_need: int
  milops_urgency: float
  ar7_mode: bool
  bad_space_candidates: list[Card]
  hand_flex_value: float
  danger_level: "CALM" | "URGENT" | "EMERGENCY"


## 4. Entry points

function choose_rollout_action(state: State, side: Side) -> Action:
  opening = opening_book_override(state, side)
  if opening != null:
    return opening

  if state.phase == HEADLINE:
    return choose_headline(state, side)

  u = compute_urgency(state, side)

  candidates = enumerate_candidate_actions(state, side, u)
  candidates = [a for a in candidates if hard_filter_action(state, side, a, u)]

  if candidates is empty:
    return fallback_legal_action(state, side)

  forced = force_scoring_if_required_now(state, side, candidates, u)
  if forced != null:
    return forced

  forced = force_europe_emergency_if_required(state, side, candidates, u)
  if forced != null:
    return forced

  forced = force_thailand_emergency_if_required(state, side, candidates, u)
  if forced != null:
    return forced

  scored = []
  for a in candidates:
    s = score_action(state, side, a, u)
    scored.append((a, s))

  scored.sort(desc by s)

  temp = choose_temperature(u)
  return softmax_sample_top_k(scored, Weights.TOP_K_ACTIONS, temp)


function choose_headline(state: State, side: Side) -> Action:
  u = compute_urgency(state, side)

  candidates = enumerate_headline_candidates(state, side, u)
  candidates = [a for a in candidates if hard_filter_action(state, side, a, u)]

  if size(candidates) == 1:
    return candidates[0]

  scored = []
  for a in candidates:
    s = score_headline_action(state, side, a, u)
    scored.append((a, s))

  scored.sort(desc by s)
  temp = choose_temperature(u)
  return softmax_sample_top_k(scored, Weights.TOP_K_ACTIONS, temp)


## 5. Opening override
##
## Twilight Strategy is very explicit that Turn 1 is unusually special.
## We do not want generic rollout noise here.

function opening_book_override(state: State, side: Side) -> Action | null:
  if state.phase != ACTION_ROUND:
    return null
  if state.turn != 1:
    return null

  if side == USSR:
    return choose_ussr_turn1_opening(state)

  if side == US:
    return choose_us_turn1_reply(state)

  return null


function choose_ussr_turn1_opening(state: State) -> Action | null:
  if state.ar != 1:
    return null

  # Modern default: coup Iran first.
  # Prefer a 4-op coup; if no 4-op exists, China is a real option,
  # but do not spend China casually because of double-hold / hand-flex issues.
  iran_coups = legal_iran_coups_sorted_best_first(state, USSR)

  if iran_coups not empty:
    best = iran_coups[0]
    if best.card.is_china:
      if china_t1_is_worth_it(state, USSR):
        return best
      # if no non-China 4-op exists, still allow it as fallback
      alt = first_non_china_strong_iran_coup(iran_coups)
      if alt != null:
        return alt
      return best
    return best

  # Rare fallback if Iran coup is impossible / absurd in a card-hooked line
  return best_of_objectives(state, USSR, [
    "OPENING_ASIA_ACCESS",
    "OPENING_THAILAND_ROUTE",
    "OPENING_EUROPE_DENIAL",
    "BEST_GENERAL_VALUE"
  ])


function choose_us_turn1_reply(state: State) -> Action | null:
  if state.ar != 1:
    return null

  if ussr_just_couped_iran(state):
    if iran_coup_was_weak(state):
      cc = best_iran_countercoup(state, US)
      if cc != null:
        return cc

    # If Soviet Iran coup was strong, do not auto-countercoup.
    # Survive and route: protect Israel, race toward Libya, route to Thailand, pick up Greece/Turkey later.
    return best_of_objectives(state, US, [
      "OPENING_PROTECT_ISRAEL",
      "OPENING_LIBYA_ROUTE",
      "OPENING_THAILAND_ROUTE",
      "OPENING_GREECE_TURKEY",
      "BEST_GENERAL_VALUE"
    ])

  return null


function china_t1_is_worth_it(state: State, side: Side) -> bool:
  # Conservative policy:
  # - acceptable if it upgrades a weak 3-op Iran coup into a strong 4/5-op coup
  # - acceptable if the hand is miserable
  # - otherwise avoid because China protects hand flexibility and can enable US double-hold lines
  if side != USSR:
    return true

  if no_non_china_4op_in_hand(state, side) and iran_is_critical_now(state):
    return true

  if hand_is_miserable(state, side):
    return true

  return false


## 6. Candidate generation

function enumerate_candidate_actions(state: State, side: Side, u: Urgency) -> list[Action]:
  out = []
  hand = state.hand[side]

  # scoring cards are always explicit candidates
  for card in hand:
    if card.is_scoring:
      out.append(Action(
        type = PLAY_SCORING,
        card = card,
        scoring_region = card.scoring_region
      ))

  for card in hand:
    if card.is_scoring:
      continue

    # event candidate only if it is plausibly a gamechanger or there is a card-specific reason
    if can_play_event(state, side, card) and event_is_candidate(state, side, card, u):
      out.append(Action(
        type = PLAY_EVENT,
        card = card
      ))

    # space candidate only if it is truly worth a whole action round
    if card_is_space_candidate(state, side, card, u):
      out.append(Action(
        type = SPACE_CARD,
        card = card
      ))

    if card.is_china:
      out.extend(generate_china_ops_candidates(state, side, card, u))
    else:
      out.extend(generate_ops_candidates(state, side, card, u))

  return dedupe_actions(out)


function enumerate_headline_candidates(state: State, side: Side, u: Urgency) -> list[Action]:
  out = []
  for card in state.hand[side]:
    if card.is_china:
      continue

    # scoring can be headlined, but that is not the default plan
    out.append(Action(
      type = HEADLINE_CARD,
      card = card,
      scoring_region = card.scoring_region if card.is_scoring else null
    ))
  return out


function generate_ops_candidates(state: State, side: Side, card: Card, u: Urgency) -> list[Action]:
  out = []

  objectives = determine_influence_objectives(state, side, card, u)

  for objective in objectives:
    plan = build_influence_plan(state, side, card, objective, u, asia_only = false)
    if plan != null and plan.placements not empty:
      out.append(Action(
        type = PLAY_OPS_INFLUENCE,
        card = card,
        placements = plan.placements,
        event_timing = choose_event_timing_if_needed(state, side, card, plan),
        tags = {objective}
      ))

  for target in top_coup_targets(state, side, card, u, limit = 3):
    out.append(Action(
      type = PLAY_OPS_COUP,
      card = card,
      target_country = target,
      event_timing = choose_event_timing_if_needed(state, side, card, target)
    ))

  for seq in generate_realign_sequences(state, side, card, u):
    out.append(Action(
      type = PLAY_OPS_REALIGN_SEQUENCE,
      card = card,
      realign_targets = seq.targets,
      event_timing = choose_event_timing_if_needed(state, side, card, seq)
    ))

  return dedupe_actions(out)


function generate_china_ops_candidates(state: State, side: Side, china: Card, u: Urgency) -> list[Action]:
  out = []

  # China is primarily Asia / critical-score / hand-flex; do not generate broad junk uses.
  objectives = determine_china_objectives(state, side, u)

  for objective in objectives:
    plan = build_influence_plan(state, side, china, objective, u, asia_only = objective_requires_asia_only(objective))
    if plan != null and plan.placements not empty:
      out.append(Action(
        type = PLAY_CHINA_INFLUENCE,
        card = china,
        placements = plan.placements,
        tags = {objective}
      ))

  for target in top_coup_targets(state, side, china, u, limit = 2, asia_only = true):
    out.append(Action(
      type = PLAY_CHINA_COUP,
      card = china,
      target_country = target
    ))

  for seq in generate_realign_sequences(state, side, china, u, asia_only = true):
    out.append(Action(
      type = PLAY_CHINA_REALIGN_SEQUENCE,
      card = china,
      realign_targets = seq.targets
    ))

  return dedupe_actions(out)


function determine_influence_objectives(state: State, side: Side, card: Card, u: Urgency) -> list[string]:
  out = []

  # scoring first
  if size(u.must_play_scoring_regions) > 0:
    out.append("REPAIR_MUST_SCORE")
    out.append("ATTACK_MUST_SCORE")

  # last AR control-break mode
  if u.ar7_mode:
    out.append("AR7_CONTROL_BREAK")

  # Asia / Thailand / country-count logic
  if asia_is_hot(state, u):
    out.append("THAILAND_ROUTE")
    out.append("ASIA_BG_LOCK")
    if side == US:
      out.append("ASIA_COUNTRY_COUNT_DENIAL")

  # Mid War hot regions
  if u.stage == MID:
    out.append("AFRICA_BG_LOCK")
    out.append("SOUTH_AMERICA_LOCK")

  # Europe only when real
  if u.europe_emergency > 0:
    out.append("EUROPE_THRESHOLD_DEFENSE")

  out.append("BEST_GENERAL_VALUE")
  return unique_preserve_order(out)


function determine_china_objectives(state: State, side: Side, u: Urgency) -> list[string]:
  out = []

  if asia_not_fully_scored_out(state):
    out.append("CHINA_ASIA_CRITICAL_SWING")
    out.append("THAILAND_ROUTE")
    out.append("ASIA_BG_LOCK")
    if side == US:
      out.append("ASIA_COUNTRY_COUNT_DENIAL")

  if critical_region_scoring_this_turn(state, side):
    out.append("CRITICAL_SCORE_SWING")

  if u.ar7_mode and asia_is_hot(state, u):
    out.append("AR7_CONTROL_BREAK")

  # generic 4-op China use is allowed only after stronger reasons
  out.append("BEST_GENERAL_VALUE")
  return unique_preserve_order(out)


## 7. Hard filters

function hard_filter_action(state: State, side: Side, a: Action, u: Urgency) -> bool:
  if not engine_is_legal(state, side, a):
    return false

  if action_causes_immediate_self_loss_via_defcon(state, side, a):
    return false

  # do not offer empty-value spacing
  if a.type == SPACE_CARD and not card_is_space_candidate(state, side, a.card, u):
    return false

  # China headline impossible
  if a.type == HEADLINE_CARD and a.card.is_china:
    return false

  # realignments are sharply restricted in this version
  if a.type in [PLAY_OPS_REALIGN_SEQUENCE, PLAY_CHINA_REALIGN_SEQUENCE]:
    if not realignment_sequence_is_candidate(state, side, a, u):
      return false

  return true


## 8. Urgency / stage / region weighting

function compute_urgency(state: State, side: Side) -> Urgency:
  u = Urgency()
  u.stage = state.stage
  u.ars_left = remaining_action_rounds_in_turn(state, side)
  u.must_play_scoring_regions = scoring_regions_in_hand(state, side)
  u.region_weight = compute_region_weights(state, side, u)
  u.region_posture = compute_region_posture(state, side, u)
  u.europe_emergency = estimate_europe_emergency(state, side)
  u.thailand_emergency = estimate_thailand_emergency(state, side)
  u.milops_need = estimate_milops_target(state) - state.milops[side]
  u.milops_urgency = max(0, u.milops_need) / max(1, u.ars_left)
  u.ar7_mode = is_last_action_round_of_turn(state, side)
  u.bad_space_candidates = find_bad_space_candidates(state, side)
  u.hand_flex_value = estimate_hand_flex_value(state, side)

  if size(u.must_play_scoring_regions) > 0 and u.ars_left <= size(u.must_play_scoring_regions):
    u.danger_level = "EMERGENCY"
  else if u.europe_emergency > 0 or u.thailand_emergency > 0 or u.milops_urgency >= 1.0 or size(u.bad_space_candidates) > 0:
    u.danger_level = "URGENT"
  else:
    u.danger_level = "CALM"

  return u


function compute_region_weights(state: State, side: Side, u: Urgency) -> map[Region, float]:
  w = base_region_weights_for_stage_and_side(state.stage, side)

  # scoring in hand spikes a region immediately
  for r in u.must_play_scoring_regions:
    w[r] += 4.0

  # Europe is mostly static until it isn't
  if europe_scoring_is_potential_auto_end(state):
    w[EUROPE] += 5.0

  # Thailand / Asia / SE Asia coupling
  if thailand_is_contested(state):
    w[ASIA] += 1.5
    w[SOUTHEAST_ASIA] += 1.8

  # China makes Asia more volatile
  if china_is_live_and_relevant(state):
    w[ASIA] += 1.0

  # if Mid War and SA/Africa are open, keep them hot
  if state.stage == MID:
    if region_is_open_or_lopsided(state, SOUTH_AMERICA):
      w[SOUTH_AMERICA] += 1.5
    if region_is_open_or_lopsided(state, AFRICA):
      w[AFRICA] += 1.3

  # Central America usually stays lower unless scoring or existing foothold turns it on
  if central_america_is_dead_and_unscored(state):
    w[CENTRAL_AMERICA] -= 0.2
  else if side == USSR and ussr_has_cuba_or_mexico_track(state):
    w[CENTRAL_AMERICA] += 0.4

  # side-specific Middle East posture
  if side == US and state.stage in [EARLY, MID]:
    w[MIDDLE_EAST] += 0.5   # but posture will be DENY_DOM, not greedily ATTACK
  if side == USSR and state.stage in [EARLY, MID]:
    w[MIDDLE_EAST] += 0.8

  return w


function base_region_weights_for_stage_and_side(stage: Stage, side: Side) -> map[Region, float]:
  if stage == EARLY:
    if side == USSR:
      return {
        EUROPE: 1.3,
        ASIA: 3.0,
        MIDDLE_EAST: 2.2,
        CENTRAL_AMERICA: 0.2,
        SOUTH_AMERICA: 0.3,
        AFRICA: 0.3,
        SOUTHEAST_ASIA: 1.7
      }
    else:
      return {
        EUROPE: 1.2,
        ASIA: 3.2,
        MIDDLE_EAST: 1.7,
        CENTRAL_AMERICA: 0.2,
        SOUTH_AMERICA: 0.3,
        AFRICA: 0.3,
        SOUTHEAST_ASIA: 1.8
      }

  if stage == MID:
    if side == USSR:
      return {
        EUROPE: 1.1,
        ASIA: 1.4,
        MIDDLE_EAST: 1.9,
        CENTRAL_AMERICA: 0.8,
        SOUTH_AMERICA: 2.6,
        AFRICA: 2.7,
        SOUTHEAST_ASIA: 0.5
      }
    else:
      return {
        EUROPE: 1.2,
        ASIA: 1.4,
        MIDDLE_EAST: 1.5,
        CENTRAL_AMERICA: 0.7,
        SOUTH_AMERICA: 2.8,
        AFRICA: 2.7,
        SOUTHEAST_ASIA: 0.5
      }

  # LATE
  if side == USSR:
    return {
      EUROPE: 1.5,
      ASIA: 1.0,
      MIDDLE_EAST: 1.6,
      CENTRAL_AMERICA: 0.7,
      SOUTH_AMERICA: 1.9,
      AFRICA: 1.7,
      SOUTHEAST_ASIA: 0.2
    }
  else:
    return {
      EUROPE: 1.8,
      ASIA: 1.0,
      MIDDLE_EAST: 1.4,
      CENTRAL_AMERICA: 0.7,
      SOUTH_AMERICA: 2.1,
      AFRICA: 1.8,
      SOUTHEAST_ASIA: 0.2
    }


function compute_region_posture(state: State, side: Side, u: Urgency) -> map[Region, RegionPosture]:
  p = default_map(ATTACK)

  p[EUROPE] = STATIC_THRESHOLD_DEFENSE

  if side == US and state.stage in [EARLY, MID]:
    p[MIDDLE_EAST] = DENY_DOM
  if side == USSR and state.stage in [EARLY, MID]:
    p[MIDDLE_EAST] = MAINTAIN_DOM

  if asia_is_hot(state, u):
    p[ASIA] = HOT_BG_LOCK
    p[SOUTHEAST_ASIA] = HOT_BG_LOCK

  if state.stage == MID:
    p[AFRICA] = HOT_BG_LOCK
    p[SOUTH_AMERICA] = HOT_BG_LOCK

  if state.stage == MID and central_america_is_dead_and_unscored(state):
    p[CENTRAL_AMERICA] = DEFEND

  return p


## 9. Forced overrides

function force_scoring_if_required_now(state: State, side: Side, candidates: list[Action], u: Urgency) -> Action | null:
  scoring_count = effective_must_play_scoring_count(state, side, u)

  if scoring_count == 0:
    return null

  if u.ars_left <= scoring_count:
    scoring_actions = [a for a in candidates if a.type == PLAY_SCORING]
    if scoring_actions is empty:
      return null
    return argmax(scoring_actions, lambda a: score_scoring_action(state, side, a, u))

  return null


function effective_must_play_scoring_count(state: State, side: Side, u: Urgency) -> int:
  count = size(u.must_play_scoring_regions)

  # exact generic deadline logic stays conservative
  # special scoring-discard exceptions belong in card-specific hooks
  # (Five Year Plan last-AR cases, Ask Not lines, etc.)
  count -= card_specific_scoring_discard_outs(state, side)

  return max(0, count)


function force_europe_emergency_if_required(state: State, side: Side, candidates: list[Action], u: Urgency) -> Action | null:
  if u.europe_emergency < 8.0:
    return null
  return argmax(candidates, lambda a: estimate_local_region_effect(state, side, a, EUROPE))


function force_thailand_emergency_if_required(state: State, side: Side, candidates: list[Action], u: Urgency) -> Action | null:
  if u.thailand_emergency < 7.0:
    return null
  return argmax(candidates, lambda a: estimate_country_effect(state, side, a, "Thailand"))


## 10. Top-level scoring

function score_action(state: State, side: Side, a: Action, u: Urgency) -> float:
  if not engine_is_legal(state, side, a):
    return Weights.ILLEGAL_PENALTY
  if action_causes_immediate_self_loss_via_defcon(state, side, a):
    return Weights.AUTO_LOSS_PENALTY

  s = 0

  if a.type == PLAY_SCORING:
    s += score_scoring_action(state, side, a, u)

  else if a.type == PLAY_EVENT:
    s += score_event_action(state, side, a, u)

  else if a.type in [PLAY_OPS_INFLUENCE, PLAY_CHINA_INFLUENCE]:
    s += score_influence_action(state, side, a, u)

  else if a.type in [PLAY_OPS_COUP, PLAY_CHINA_COUP]:
    s += score_coup_action(state, side, a, u)

  else if a.type in [PLAY_OPS_REALIGN_SEQUENCE, PLAY_CHINA_REALIGN_SEQUENCE]:
    s += score_realign_sequence_action(state, side, a, u)

  else if a.type == SPACE_CARD:
    s += score_space_action(state, side, a, u)

  s += score_hand_management_overlay(state, side, a, u)
  s += score_tempo_overlay(state, side, a, u)

  return s


## 11. Scoring cards

function score_scoring_action(state: State, side: Side, a: Action, u: Urgency) -> float:
  r = a.scoring_region

  net_now = exact_score_net_if_scored_now(state, side, r)
  repair1 = estimate_best_one_card_repair_value(state, side, r)
  repair2 = estimate_best_two_card_repair_value(state, side, r)

  s = 0
  s += Weights.MUST_PLAY_SCORING_BONUS
  s += Weights.IMMEDIATE_VP * net_now

  # if there is time to repair, slightly penalize immediate bad score
  if u.ars_left > 1:
    s -= 5 * max(0, repair1)
  if u.ars_left > 2:
    s -= 2 * max(0, repair2)

  # Asia special: country count denial matters
  if r == ASIA:
    s += Weights.COUNTRY_COUNT_DENIAL * asia_country_count_score_component(state, side)

  # Africa / South America are more lopsided than they look
  if r in [AFRICA, SOUTH_AMERICA]:
    s += 6 * estimate_lopsided_region_swing_value(state, side, r)

  # Southeast Asia should usually be taken promptly when favorable
  if r == SOUTHEAST_ASIA:
    s += 8 * southeast_asia_promptness_bonus(state, side)

  # Europe emergency
  if r == EUROPE:
    if would_side_control_europe(state, side):
      s += Weights.EUROPE_INSTANT_WIN_BONUS
    if would_side_control_europe(state, other(side)):
      s += Weights.EUROPE_INSTANT_LOSS_PENALTY

  return s


function score_headline_scoring(state: State, side: Side, a: Action, u: Urgency) -> float:
  s = score_scoring_action(state, side, Action(
    type = PLAY_SCORING,
    card = a.card,
    scoring_region = a.scoring_region
  ), u)

  # default policy: do NOT headline scoring just because it is scorable.
  # Headline scoring is now treated as a special-case tool.
  s += Weights.BAD_HEADLINE_SCORING_PENALTY

  if headline_scoring_is_tactically_good(state, side, a, u):
    s += 22

  if headline_scoring_is_defectors_style_dump(state, side, a):
    s += 18

  return s


function headline_scoring_is_tactically_good(state: State, side: Side, a: Action, u: Urgency) -> bool:
  r = a.scoring_region

  if r == EUROPE and u.europe_emergency > 0:
    return true

  if exact_score_net_if_scored_now(state, side, r) > estimate_best_one_card_repair_value(state, side, r):
    # region is likely to get worse before we can score
    return true

  if opponent_has_high_probability_of_repair_or_gamechanger_before_we_score(state, side, r):
    return true

  return false


## 12. Events vs Ops correction

function event_is_candidate(state: State, side: Side, card: Card, u: Urgency) -> bool:
  if card_specific_event_candidate(state, side, card):
    return true

  return event_is_gamechanger(state, side, card, u)


function event_is_gamechanger(state: State, side: Side, card: Card, u: Urgency) -> bool:
  # Events need to do something Ops don't do cheaply.
  return (
    event_opens_closed_region(state, side, card) or
    event_removes_access(state, side, card) or
    event_breaks_stalemate(state, side, card) or
    event_creates_multi_action_tempo(state, side, card) or
    event_has_large_vp_swing(state, side, card) or
    event_solves_urgent_scoring_problem(state, side, card, u)
  )


function score_event_action(state: State, side: Side, a: Action, u: Urgency) -> float:
  card = a.card
  owner = event_owner_for_card(card)

  s = 0

  if event_is_gamechanger(state, side, card, u):
    s += 20 * estimate_event_value(state, side, card)
  else:
    # this is the big correction: do not play event just because event text looks "good"
    s += Weights.NON_GAMECHANGER_EVENT_OPPORTUNITY_COST

  if owner == other(side):
    s -= 25 * estimate_offside_event_cost(state, side, card)

  # if the event directly fixes urgent scoring / Europe / Thailand, bump it
  for r in u.must_play_scoring_regions:
    s += 8 * estimate_event_region_effect(state, side, card, r)
  s += 10 * estimate_event_region_effect(state, side, card, EUROPE) * u.europe_emergency
  s += 12 * estimate_event_country_effect(state, side, card, "Thailand") * max(1.0, u.thailand_emergency)

  return s


## 13. Space Race correction

function card_is_space_candidate(state: State, side: Side, card: Card, u: Urgency) -> bool:
  if not can_space_card(state, side, card):
    return false

  # never space just because the event is mildly annoying
  # space only when the event is truly awful / unmitigable / tempo-breaking / hand-toxic

  if card_causes_immediate_loss_or_defcon_suicide(state, side, card):
    return true

  if card_is_unmitigable_access_swing(state, side, card):
    return true

  if card_creates_extra_actions_or_action_lock(state, side, card):
    return true

  if card_gives_huge_vp_and_cannot_be_repaired(state, side, card):
    return true

  # if we already have the special "space two" or headline-peek context, threshold loosens slightly
  if special_space_track_context_active(state, side) and card_is_severe_but_not_catastrophic(state, side, card):
    return true

  return false


function score_space_action(state: State, side: Side, a: Action, u: Urgency) -> float:
  card = a.card

  if not card_is_space_candidate(state, side, card, u):
    return -1e12

  s = 0
  s += Weights.BAD_SPACE_DISPOSAL_BONUS
  s += 18 * catastrophe_value_of_not_spacing(state, side, card)
  s += 6 * special_space_track_bonus_value(state, side)
  s += Weights.SPACE_OPPORTUNITY_COST * ops_pressure_value(state, side, u)

  return s


## 14. Influence scoring

function score_influence_action(state: State, side: Side, a: Action, u: Urgency) -> float:
  before = snapshot_region_features(state, side)
  after_state = cheap_apply_action_for_eval(state, side, a)
  after = snapshot_region_features(after_state, side)

  s = 0

  for r in all_regions_including_seasia():
    weight = u.region_weight[r]
    posture = u.region_posture[r]

    local = 0
    local += Weights.SCORING_REPAIR * (after.scoring_safety[r] - before.scoring_safety[r])
    local += Weights.BG_SWING * (after.bg_margin[r] - before.bg_margin[r])
    local += Weights.DOMINATION_SWING * (after.domination_margin[r] - before.domination_margin[r])
    local += Weights.ACCESS_CREATION * (after.access[r] - before.access[r])
    local += Weights.ACCESS_DENIAL * (after.opp_access_denial[r] - before.opp_access_denial[r])
    local += Weights.DEFENSE_BUFFER * (after.stability_buffer[r] - before.stability_buffer[r])

    if posture == DENY_DOM:
      local += 6 * (after.domination_denial[r] - before.domination_denial[r])

    if posture == HOT_BG_LOCK:
      local += Weights.HOT_BG_LOCK * (after.hot_bg_lock[r] - before.hot_bg_lock[r])

    s += weight * local

  # Asia country-count denial is explicit
  if action_touches_asia_or_seasia(a) and side == US:
    s += Weights.COUNTRY_COUNT_DENIAL * asia_country_count_denial_gain(state, side, a)

  # AR7 control-break bonus
  if u.ar7_mode and action_breaks_control(a):
    s += score_ar7_control_break_bonus(state, side, a)

  # Thailand-specific urgency
  if action_touches_country(a, "Thailand"):
    s += Weights.THAILAND_EMERGENCY_BONUS * max(1.0, u.thailand_emergency)

  # wastage
  s += Weights.WASTED_OPS * estimate_wasted_ops(a)

  # corrected overcontrol logic: only punish OVERcontrol beyond desired buffers
  s += Weights.BLIND_OVERCONTROL * estimate_excess_overcontrol_beyond_needed_buffer(state, side, a, u)

  # offside event harm
  s -= Weights.LIVE_OFFSIDE_EVENT_COST * event_cost_if_ops_triggers_opponent_event(state, side, a)

  return s


function score_ar7_control_break_bonus(state: State, side: Side, a: Action) -> float:
  if not action_breaks_control(a):
    return 0

  target = primary_control_break_target(a)
  if target == null:
    return 0

  bonus = 0

  if target_is_hard_to_coup_at_defcon3(state, target):
    bonus += Weights.AR7_BREAK_CONTROL_BONUS

  if target_is_key_asia_country(target):
    bonus += 900

  if target_is_midwar_battleground_opponent_wants_to_coup_anyway(state, side, target):
    bonus -= 600

  if breaking_target_hands_opponent_profitable_access_coup(state, side, target):
    bonus += Weights.PROFITABLE_ACCESS_COUP_PENALTY

  return bonus


## 15. Influence plan builder

struct InfluencePlan:
  placements: list[(CountryName, count)]

function build_influence_plan(state: State, side: Side, card: Card, objective: string, u: Urgency, asia_only: bool) -> InfluencePlan | null:
  ops = effective_ops_for_card_in_mode(state, side, card, "INFLUENCE", objective)
  if ops <= 0:
    return null

  working = clone_shallow(state)
  placements = []

  while ops > 0:
    choices = enumerate_single_placement_choices(working, side, objective, asia_only)

    best_country = null
    best_cost = null
    best_score_per_op = -1e18

    for c in choices:
      cost = placement_cost(working, side, c)
      if cost > ops:
        continue

      marginal = marginal_placement_value(working, side, c, objective, u)
      spop = marginal / cost

      if spop > best_score_per_op:
        best_score_per_op = spop
        best_country = c
        best_cost = cost

    if best_country == null:
      break

    apply_single_influence(working, side, best_country, +1)
    placements.append((best_country, 1))
    ops -= best_cost

  if placements empty:
    return null

  return InfluencePlan(placements = compress_adjacent_same_country(placements))


function enumerate_single_placement_choices(state: State, side: Side, objective: string, asia_only: bool) -> list[CountryName]:
  out = []

  for country in state.countries.values():
    if asia_only and not country_in_asia_or_seasia(country):
      continue
    if not can_place_in_country(state, side, country.name):
      continue
    out.append(country.name)

  return out


function marginal_placement_value(state: State, side: Side, country_name: CountryName, objective: string, u: Urgency) -> float:
  c = state.countries[country_name]
  value = 0

  region_score = sum(estimate_country_local_value(state, side, country_name, r) for r in c.regions)
  access = estimate_access_creation_value(state, side, country_name)
  opp_access_denial = estimate_access_denial_value(state, side, country_name)
  defense = estimate_defense_value(state, side, country_name)
  break_control = estimate_break_control_value(state, side, country_name)
  country_count = estimate_country_count_value(state, side, country_name)
  bg = 3 if c.battleground else 0
  hotlock = hot_bg_lock_value(state, side, country_name)

  if objective == "REPAIR_MUST_SCORE":
    value += 7 * region_score + 4 * defense + 3 * break_control + 2 * bg

  else if objective == "ATTACK_MUST_SCORE":
    value += 6 * region_score + 4 * break_control + 2 * access + 2 * bg

  else if objective == "AR7_CONTROL_BREAK":
    value += 7 * break_control + 4 * access + 2 * opp_access_denial
    if target_is_hard_to_coup_at_defcon3(state, country_name):
      value += 10
    if breaking_country_hands_opponent_profitable_access_coup(state, side, country_name):
      value -= 8

  else if objective == "THAILAND_ROUTE":
    value += thailand_route_value(state, side, country_name)

  else if objective == "ASIA_COUNTRY_COUNT_DENIAL":
    value += 6 * country_count + 2 * region_score + 1 * defense

  else if objective == "ASIA_BG_LOCK":
    value += 5 * bg + 3 * defense + 3 * hotlock + 2 * region_score

  else if objective == "AFRICA_BG_LOCK":
    value += 5 * bg + 4 * hotlock + 3 * access + 2 * defense
    if country_name in ["Botswana", "Algeria"]:
      value += 5

  else if objective == "SOUTH_AMERICA_LOCK":
    value += 4 * bg + 4 * access + 3 * opp_access_denial
    if country_name in ["Colombia", "Uruguay"]:
      value += 5

  else if objective == "OPENING_PROTECT_ISRAEL":
    if country_name in ["Lebanon", "Jordan", "Israel"]:
      value += 12
    else:
      value += region_score

  else if objective == "OPENING_LIBYA_ROUTE":
    if country_name in ["Egypt", "Libya"]:
      value += 12
    else:
      value += region_score

  else if objective == "OPENING_THAILAND_ROUTE":
    if country_name in ["Malaysia", "Thailand", "Laos/Cambodia", "Burma"]:
      value += 12
    else:
      value += region_score

  else if objective == "OPENING_GREECE_TURKEY":
    if country_name in ["Greece", "Turkey"]:
      value += 10
    else:
      value += region_score

  else if objective == "EUROPE_THRESHOLD_DEFENSE":
    if country_name in ["France", "Italy", "Greece", "Turkey", "Spain/Portugal"]:
      value += 10
    else:
      value += region_score

  else:
    value += 4 * region_score + 3 * access + 2 * defense + 2 * break_control + 1 * bg

  # desired overcontrol buffers are a positive, not waste
  value += desired_overcontrol_buffer_gain(state, side, country_name)

  return value


function thailand_route_value(state: State, side: Side, country_name: CountryName) -> float:
  if country_name == "Thailand":
    return 16
  if country_name == "Malaysia":
    return 10
  if country_name == "Laos/Cambodia":
    return 8
  if country_name == "Burma":
    return 8
  if country_name == "Vietnam":
    return 5
  return 0


function desired_overcontrol_buffer_gain(state: State, side: Side, country_name: CountryName) -> float:
  desired = desired_overcontrol_buffer(state, side, country_name)
  if desired <= 0:
    return 0

  current = control_buffer(state, side, country_name)
  return max(0, desired - current) * 2.5


function desired_overcontrol_buffer(state: State, side: Side, country_name: CountryName) -> int:
  # revised from previous version: some countries WANT overcontrol
  if country_name == "Thailand":
    if opponent_has_live_china_threat(state, side) or opponent_has_seasia_bonus_threat(state, side):
      return 2
    return 1

  if country_name in ["Nigeria", "Zaire", "Angola"]:
    return 2

  if country_name in ["South Korea", "Pakistan", "India"] and asia_is_hot(state, compute_urgency_light(state, side)):
    return 1

  if country_name in ["France", "Italy"] and europe_scoring_is_potential_auto_end(state):
    return 1

  return 0


function estimate_excess_overcontrol_beyond_needed_buffer(state: State, side: Side, a: Action, u: Urgency) -> float:
  if a.type not in [PLAY_OPS_INFLUENCE, PLAY_CHINA_INFLUENCE]:
    return 0

  penalty = 0
  simulated = clone_shallow(state)
  apply_action_to_clone_for_buffer_eval(simulated, side, a)

  touched = unique(country for (country, count) in a.placements)
  for country_name in touched:
    desired = desired_overcontrol_buffer(state, side, country_name)
    after = control_buffer(simulated, side, country_name)
    if after > desired + 2:
      penalty += after - (desired + 2)

  return penalty


## 16. Coups

function score_coup_action(state: State, side: Side, a: Action, u: Urgency) -> float:
  target = state.countries[a.target_country]
  ops = effective_ops_for_action(state, side, a)

  s = 0
  s += 8 * estimate_expected_coup_swing(target, ops, side, state)
  s += 4 * sum(u.region_weight[r] for r in target.regions) * estimate_country_local_value_scalar(state, side, target.name)

  # opening correction: Iran is special
  if state.turn == 1 and side == USSR and target.name == "Iran":
    s += 2500

  # coups that open closed regions matter
  s += 7 * access_opening_coup_bonus(state, side, target.name)

  # MilOps matter
  s += Weights.MILOPS_PROGRESS * estimate_milops_gain_from_coup(state, side, a) * max(1.0, u.milops_urgency)

  # battleground coup can cost DEFCON mobility
  if target.battleground:
    s += Weights.DEFCON_MOBILITY_LOSS * estimate_defcon_mobility_loss_from_bg_coup(state, side, a)

  # vanity coups into high stability are bad unless emergency
  s -= 2 * max(0, target.stability - ops)

  s -= Weights.LIVE_OFFSIDE_EVENT_COST * event_cost_if_ops_triggers_opponent_event(state, side, a)

  return s


function access_opening_coup_bonus(state: State, side: Side, country_name: CountryName) -> float:
  # coups are not just for influence swing; they can create access.
  if coup_opens_region_access(state, side, country_name):
    return 1.5
  return 0.0


function top_coup_targets(state: State, side: Side, card: Card, u: Urgency, limit: int, asia_only: bool = false) -> list[CountryName]:
  tmp = []
  ops = effective_ops_for_card_in_mode(state, side, card, "COUP", objective = null)

  for c in state.countries.values():
    if asia_only and not country_in_asia_or_seasia(c):
      continue
    if not can_coup_country(state, side, c.name):
      continue

    expected = estimate_expected_coup_swing(c, ops, side, state)
    local = estimate_country_local_value_scalar(state, side, c.name)
    access_bonus = access_opening_coup_bonus(state, side, c.name)
    milops = estimate_milops_gain_from_coup_target(state, side, c.name)
    defcon_pen = estimate_defcon_penalty_for_coup_target(state, side, c.name)

    score = 8 * expected + 4 * local + 7 * access_bonus + 5 * milops - 4 * defcon_pen

    if state.turn == 1 and side == USSR and c.name == "Iran":
      score += 2500

    tmp.append((c.name, score))

  tmp.sort(desc by score)
  return [name for (name, score) in take_first(tmp, limit)]


## 17. Realignments (heavily corrected)

struct RealignSequence:
  targets: list[CountryName]
  mod_edge: int
  access_kill: bool
  hotspot: string

function realignment_sequence_is_candidate(state: State, side: Side, a: Action, u: Urgency) -> bool:
  if state.defcon != 2 and not rare_europe_realign_window(state, side, a):
    return false

  if a.realign_targets empty:
    return false

  primary = a.realign_targets[0]
  if state.countries[primary].stability == 1 and can_coup_country(state, side, primary):
    return false

  seq = analyze_realign_sequence(state, side, a.realign_targets)
  if seq.access_kill:
    return true
  if seq.mod_edge >= 1:
    return true

  # very rare speculative -1 access-kill attempts are allowed only with a big card
  if seq.mod_edge == -1 and seq.access_kill and effective_ops_for_action(state, side, a) >= 4:
    return true

  return false


function generate_realign_sequences(state: State, side: Side, card: Card, u: Urgency, asia_only: bool = false) -> list[RealignSequence]:
  out = []

  if state.defcon != 2 and not rare_card_or_europe_window_for_realign(state, side, card):
    return out

  hotspots = detect_realign_hotspots(state, side, asia_only)

  for h in hotspots:
    if h.access_kill or h.mod_edge >= 1 or (h.mod_edge == -1 and h.access_kill and card.ops >= 4):
      seq = build_realign_sequence_from_hotspot(state, side, h, card)
      if seq != null:
        out.append(seq)

  return top_n_realign_sequences(out, 2)


function detect_realign_hotspots(state: State, side: Side, asia_only: bool) -> list[RealignSequence]:
  out = []

  # access-kill hotspots
  maybe_add_hotspot(out, analyze_hotspot(state, side, "Cuba"))
  maybe_add_hotspot(out, analyze_hotspot(state, side, "South Africa"))
  maybe_add_hotspot(out, analyze_hotspot(state, side, "Angola"))
  maybe_add_hotspot(out, analyze_hotspot(state, side, "Mexico"))
  maybe_add_hotspot(out, analyze_hotspot(state, side, "Algeria"))

  # Latin America chains
  for country_name in ["Venezuela", "Brazil", "Argentina", "Chile"]:
    maybe_add_hotspot(out, analyze_hotspot(state, side, country_name))

  # rare Europe line
  if state.defcon == 5:
    for country_name in ["Italy", "France", "East Germany"]:
      maybe_add_hotspot(out, analyze_hotspot(state, side, country_name))

  return out


function analyze_hotspot(state: State, side: Side, country_name: CountryName) -> RealignSequence | null:
  if not can_realign_country(state, side, country_name):
    return null

  mod_edge = compute_realign_modifier_edge(state, side, country_name)
  access_kill = realign_here_kills_access(state, side, country_name)

  return RealignSequence(
    targets = [country_name, country_name],   # default: repeated pull on same hotspot
    mod_edge = mod_edge,
    access_kill = access_kill,
    hotspot = country_name
  )


function score_realign_sequence_action(state: State, side: Side, a: Action, u: Urgency) -> float:
  seq = analyze_realign_sequence(state, side, a.realign_targets)
  primary = a.realign_targets[0]

  s = 0

  if not realignment_sequence_is_candidate(state, side, a, u):
    return -1e12

  if seq.access_kill:
    s += 1800

  s += 10 * seq.mod_edge
  s += 7 * estimate_expected_realign_value(state, side, primary)
  s += 4 * estimate_country_local_value_scalar(state, side, primary)

  # 1-stability battlegrounds generally want coups / influence, not realigns
  if state.countries[primary].stability == 1:
    s += Weights.BAD_REALIGNMENT_PENALTY

  # does not help MilOps
  if u.milops_urgency > 1.0:
    s -= 4

  s -= Weights.LIVE_OFFSIDE_EVENT_COST * event_cost_if_ops_triggers_opponent_event(state, side, a)

  return s


## 18. Headline scoring / headline events

function score_headline_action(state: State, side: Side, a: Action, u: Urgency) -> float:
  card = a.card

  if card.is_scoring:
    return score_headline_scoring(state, side, a, u)

  s = 0

  # high Ops matters more in headline than normal
  s += 4 * card.ops

  # event must still be a real gamechanger
  if event_is_gamechanger(state, side, card, u):
    s += 20 * estimate_event_value(state, side, card)
  else:
    s -= 6

  # if card is an offside event, be very cautious
  if event_owner_for_card(card) == other(side):
    s -= 30 * estimate_offside_event_cost(state, side, card)

  # specific headline-use bonuses
  s += 8 * estimate_bonus_from_headline_resolve_order(state, side, card)
  s += 8 * estimate_headline_region_effect(state, side, card, EUROPE) * u.europe_emergency
  s += 10 * estimate_headline_country_effect(state, side, card, "Thailand") * max(1.0, u.thailand_emergency)

  return s


## 19. Hand management overlay (corrected)

function score_hand_management_overlay(state: State, side: Side, a: Action, u: Urgency) -> float:
  if a.card == null:
    return 0

  card = a.card
  owner = event_owner_for_card(card)
  s = 0

  # bad offside card: spacing is good only if it really is catastrophic
  if a.type == SPACE_CARD and owner == other(side):
    s += 12 * catastrophe_value_of_not_spacing(state, side, card)

  # opponent card used for Ops: choose timing + mitigate
  if owner == other(side) and a.type not in [SPACE_CARD, PLAY_EVENT]:
    s -= 4 * estimate_offside_event_cost(state, side, card)

  # preserve strong own/neutral events unless board absolutely needs Ops
  if (owner == side or owner == NEUTRAL) and a.type not in [PLAY_EVENT, HEADLINE_CARD]:
    s -= 3 * max(0, estimate_event_value(state, side, card))

  # China corrections
  if card.is_china:
    s += china_hand_management_score(state, side, a, u)

  # known hand relief tools
  if side == US and has_card_named(state, side, "Ask Not What Your Country Can Do For You..."):
    s += ask_not_hand_relief_bonus(state, side, a)

  if side == USSR and has_card_named(state, side, "Five Year Plan"):
    s += five_year_plan_discard_bonus(state, side, a)

  if has_card_named(state, side, "UN Intervention"):
    s += un_intervention_relief_bonus(state, side, a)

  return s


function china_hand_management_score(state: State, side: Side, a: Action, u: Urgency) -> float:
  s = 0

  # early / open Asia -> China is premium
  if asia_not_fully_scored_out(state):
    if action_is_decisive_asia_swing(a):
      s += 14
    else:
      s += 4

  # but USSR should not casually spend China on Turn 1
  if side == USSR and state.turn == 1 and not china_t1_is_worth_it(state, side):
    s += Weights.CHINA_T1_HOLD_RISK_PENALTY

  # China as hand-flex insurance
  if hand_is_toxic(state, side):
    if a.card.is_china and a.type in [PLAY_CHINA_INFLUENCE, PLAY_CHINA_COUP, PLAY_CHINA_REALIGN_SEQUENCE]:
      s -= 6   # spending it loses insurance
    else:
      s += 0

  # generic 4-op China use is fine only when region swing this turn matters
  if critical_region_scoring_this_turn(state, side):
    s += 8

  # Turn 10: holding China is roughly a 2VP swing unless the move is better
  if state.turn == 10:
    if not action_is_massive_turn10_swing(a):
      s -= 10

  return s


function ask_not_hand_relief_bonus(state: State, side: Side, a: Action) -> float:
  if side != US:
    return 0

  # Ask Not lets US hold bad cards and dump them together later,
  # but is card-specific and dangerous if it overdraws into scoring.
  if hand_contains_bad_cards(state, side):
    return 4
  return 0


function five_year_plan_discard_bonus(state: State, side: Side, a: Action) -> float:
  if side != USSR:
    return 0

  # Last-AR special lines are handled in card hooks; generic policy just acknowledges value.
  if is_last_action_round_of_turn(state, side):
    return 3
  return 0


function un_intervention_relief_bonus(state: State, side: Side, a: Action) -> float:
  # UN is a legitimate relief valve, but cuts hand size.
  if hand_contains_catastrophic_offside(state, side):
    return 2
  return 0


## 20. Event timing for opponent cards used for Ops

function choose_event_timing_if_needed(state: State, side: Side, card: Card, payload) -> BEFORE_OPS | AFTER_OPS | NONE:
  if event_owner_for_card(card) != other(side):
    return NONE

  cost_before = estimate_event_order_cost(state, side, card, payload, BEFORE_OPS)
  cost_after  = estimate_event_order_cost(state, side, card, payload, AFTER_OPS)

  if cost_before <= cost_after:
    return BEFORE_OPS
  return AFTER_OPS


function event_cost_if_ops_triggers_opponent_event(state: State, side: Side, a: Action) -> float:
  if a.card == null:
    return 0
  if event_owner_for_card(a.card) != other(side):
    return 0
  return estimate_event_order_cost(state, side, a.card, a, a.event_timing)


## 21. Helpers

function choose_temperature(u: Urgency) -> float:
  if u.danger_level == "EMERGENCY":
    return Weights.TEMP_EMERGENCY
  if u.danger_level == "URGENT":
    return Weights.TEMP_URGENT
  return Weights.TEMP_CALM


function best_of_objectives(state: State, side: Side, objectives: list[string]) -> Action | null:
  dummy_u = compute_urgency(state, side)
  all_actions = []
  for card in state.hand[side]:
    if card.is_scoring:
      continue
    for obj in objectives:
      if card.is_china and not objective_is_legal_for_china(obj):
        continue
      plan = build_influence_plan(state, side, card, obj, dummy_u, asia_only = false)
      if plan != null and plan.placements not empty:
        all_actions.append(Action(
          type = PLAY_CHINA_INFLUENCE if card.is_china else PLAY_OPS_INFLUENCE,
          card = card,
          placements = plan.placements,
          tags = {obj}
        ))

  if all_actions empty:
    return null

  return argmax(all_actions, lambda a: score_action(state, side, a, dummy_u))


## 22. Card-hook layer (much more important after applying Twilight Strategy)

# The generic rollout is still not enough without a small set of explicit hooks.
# Minimum recommended hook list:
# - Defectors
# - Vietnam Revolts
# - De-Stalinization
# - Decolonization
# - Blockade
# - Grain Sales to Soviets
# - Five Year Plan
# - Ask Not What Your Country Can Do For You...
# - Ussuri River Skirmish
# - OPEC
# - Muslim Revolution
# - Liberation Theology
# - Brush War
# - Tear Down This Wall
# - Junta
# - Quagmire / Bear Trap
# - Chernobyl
# - The China Card and associated China events

interface CardHeuristicHook:
  function event_candidate(state, side, card, urgency) -> bool
  function event_value(state, side, card, urgency) -> float
  function offside_event_cost(state, side, card, urgency) -> float
  function headline_value(state, side, card, urgency) -> float
  function special_scoring_discard_outs(state, side) -> int
  function opening_override(state, side) -> Action | null

CARD_HOOKS = {}


## 23. Diagnostics for this revised version

# Expected behavioral differences vs the previous pseudocode:
# - USSR Turn 1 AR1 should overwhelmingly prefer Iran coup or very narrow book alternatives.
# - Space rate should drop noticeably.
# - Realignment rate should cluster at DEFCON 2 and around Cuba / South Africa / Angola / Mexico / South America chains.
# - Thailand should receive more overcontrol.
# - Mid War attention should move up toward Africa / South America.
# - Central America should stop absorbing too many "best general value" placements.
# - Europe should become quieter unless scoring / control emergency is live.
# - China should be held more often for hand flexibility and late-game value.

function rollout_policy_playout(state: State) -> TerminalResult:
  working = clone(state)

  while not is_terminal(working):
    side = working.side_to_move
    action = choose_rollout_action(working, side)
    working = engine_apply_action(working, side, action)

  return terminal_result(working)


## 24. One-line summary

# Revised policy:
# "Use Ops by default, treat events as gamechangers, space only true disasters,
# realign mostly at DEFCON 2 with access-kill / +1 setups, fight hard for Early War Asia and Thailand,
# shift up to Africa / South America in Mid War, keep Europe mostly threshold-based,
# and treat the China Card as both a swing card and hand-insurance resource."