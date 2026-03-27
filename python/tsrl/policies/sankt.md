# Twilight Struggle rollout policy pseudocode (Sankt / Aragorn corrected, from https://maninmotiongoingnowhere.wordpress.com/2017/02/14/twilight-struggle-the-collected-musings-of-sankt/)
#
# Main corrections vs. the previous baseline:
# - evaluate Ops by expected VP / tempo / persistence, not by raw influence count
# - Europe is the major exception to "let it go"; France + Italy + Europe control get special weight
# - battlegrounds first; non-BGs are usually only for access, domination fillers, shields, or SE Asia value
# - Asia is often "good enough at parity"; do not pour Ops into the Asian black hole unless the state justifies it
# - score cards are usually played on the latest safe slot, not auto-fired the first chance
# - early space is a real VP race ("7th region"), not just a garbage dump
# - the policy must avoid control-breaking without capitalizing
# - if behind, increase variance; if ahead, suppress variance
#
# Scope:
# - this pseudocode is for rollout policy + optional opening/setup hooks
# - it is deliberately heuristic and cheap
# - exact rules legality / event text resolution are delegated to the engine when possible


## 0. Enums / high-level data

enum Side:
  US
  USSR

enum Stage:
  EARLY
  MID
  LATE

enum Phase:
  SETUP
  HEADLINE
  ACTION_ROUND
  END_TURN

enum RiskProfile:
  EV_MAX
  GAMBLE
  CONSERVE

enum ActionType:
  INITIAL_SETUP
  HEADLINE_CARD
  PLAY_SCORING
  PLAY_EVENT
  PLAY_OPS_INFLUENCE
  PLAY_OPS_COUP
  PLAY_OPS_REALIGN
  SPACE_CARD
  PLAY_CHINA_INFLUENCE
  PLAY_CHINA_COUP
  PLAY_CHINA_REALIGN

enum EventTiming:
  NONE
  BEFORE_OPS
  AFTER_OPS

enum Region:
  EUROPE
  ASIA
  MIDDLE_EAST
  CENTRAL_AMERICA
  SOUTH_AMERICA
  AFRICA
  SOUTHEAST_ASIA

struct Country:
  name
  stability
  battleground: bool
  regions: set[Region]
  influence[Side]: int
  neighbors: list[CountryName]
  adjacent_to_superpower[Side]: bool

struct Card:
  id
  name
  ops
  alignment: Side | NEUTRAL
  is_scoring: bool
  scoring_region: Region | null
  removed_after_event: bool
  is_china: bool

struct State:
  turn: int
  ar: int
  phase: Phase
  side_to_move: Side
  defcon: int
  vp: int
  milops[Side]: int
  space_pos[Side]: int
  space_attempts_used[Side]: int
  china_owner: Side
  china_face_up: bool
  hand[Side]: list[Card]
  countries: map[CountryName, Country]
  effects
  discard_pile
  removed_pile
  # plus any engine-specific fields for persistent events, optional cards, etc.

struct Action:
  type: ActionType
  card: Card | null
  scoring_region: Region | null
  placements: list[(CountryName, count)]              # influence plans
  target_country: CountryName | null                  # coup / realign target
  event_timing: EventTiming
  setup_assignment: map[CountryName, int] | null
  tags: set[string]


## 1. Constants / strategic tables

struct Weights:
  AUTO_LOSS                  = -1e15
  ILLEGAL                    = -1e15

  # urgency / deadlines
  FORCE_SCORING              = +60000
  EUROPE_AUTOWIN             = +50000
  EUROPE_AUTOLOSS            = -50000
  LATEST_SAFE_SCORING_BONUS  = +12000
  EARLY_SCORING_DELAY        = -9000

  # base evaluation
  IMMEDIATE_VP               = 35
  SCORING_SAFETY             = 28
  EUROPE_SWING               = 22
  BG_SWING                   = 16
  DOMINATION_SWING           = 14
  ACCESS_CREATION            = 10
  SHIELD_VALUE               = 9
  DEFENSE_BUFFER             = 8
  MILOPS_PROGRESS            = 8
  SPACE_RACE_VALUE           = 11
  SPACE_SPECIAL_ABILITY      = 14

  # penalties
  LIVE_OFFSIDE_EVENT_COST    = -24
  DEFCON_MOBILITY_LOSS       = -22
  WASTED_OPS                 = -15
  USELESS_NON_BG             = -12
  DANGLING_BREAK             = -18
  VANITY_COUP                = -16
  LOW_EDGE_REALIGN           = -8

  # risk modulation
  GAMBLE_WAR_EVENT_BONUS     = +10
  GAMBLE_REALIGN_BONUS       = +8
  CONSERVE_VARIANCE_PENALTY  = -10

  # sampling
  TOP_K                      = 6
  TEMP_CALM                  = 0.45
  TEMP_URGENT                = 0.20
  TEMP_EMERGENCY             = 0.08


# Rough battleground expected-value priors (Sankt/Aragorn style).
# Europe is dynamic: 3rd BG is huge, 4th BG is much smaller, 5th / control is enormous.
BG_VP_PRIOR = {
  ASIA: 5.0,
  MIDDLE_EAST: 4.5,
  CENTRAL_AMERICA: 5.0,
  SOUTH_AMERICA: 5.0,
  AFRICA: 4.0
}

# Non-BG baseline should be tiny unless one of the special reasons applies.
BASE_NON_BG_VALUE = 0.15
SEA_NON_BG_VALUE  = 1.10

# Durability / persistence heuristic:
# Sankt/Aragorn-style prioritizes persistent BGs and stable assets.
BG_STABILITY_BONUS = {
  1: 0.0,
  2: 0.8,
  3: 1.6,
  4: 2.0,
  5: 2.2
}

# Access-only countries usually want a light touch, not overinvestment.
ACCESS_ONLY_CAP = {
  "Malaysia": 1,
  "Afghanistan": 1,
  "Costa Rica": 1,
  "Lebanon": 1,
  "Jordan": 1
}

# Volatile realignment-shield countries.
REALIGN_SHIELD_COUNTRIES = {
  "Uruguay", "Paraguay", "Botswana", "Tunisia", "Peru"
}

# Country-specific hooks for common Sankt priorities.
# Values here are additive local bonuses before context scaling.
COUNTRY_HOOK = {
  "France":       {"base": 7.0, "europe_swing": 1},
  "Italy":        {"base": 6.0, "europe_swing": 1, "opening_coup_target": 1},
  "West Germany": {"base": 5.0, "europe_core": 1},
  "East Germany": {"base": 5.0, "europe_core": 1},
  "Thailand":     {"base": 5.5, "cheap_asia_bg": 1},
  "Egypt":        {"base": 5.0, "libya_access": 1},
  "Pakistan":     {"base": 4.5, "india_access": 1},
  "Malaysia":     {"base": 4.0, "access_only": 1},
  "Afghanistan":  {"base": 3.5, "access_only": 1},
  "Costa Rica":   {"base": 4.0, "access_only": 1, "panama_reentry": 1},
  "Lebanon":      {"base": 3.5, "access_only": 1},
  "Jordan":       {"base": 1.5, "access_only": 1},
  "Saudi Arabia": {"base": 2.2, "middle_east_fill": 1},
  "Iraq":         {"base": 2.5, "middle_east_fill": 1},
  "Cameroon":     {"base": 3.0, "africa_entry": 1},
  "South Africa": {"base": 3.0, "africa_anchor": 1},
  "Mexico":       {"base": 3.0, "t4_entry": 1},
  "Angola":       {"base": 3.0, "t4_entry": 1},
  "Algeria":      {"base": 3.0, "t4_entry": 1},
  "Panama":       {"base": 3.5, "t4_entry": 1},
  "Chile":        {"base": 2.5, "sa_entry": 1},
  "Argentina":    {"base": 2.5, "sa_entry": 1},
  "Syria":        {"base": 2.0, "domination_fill": 1},
  "Indonesia":    {"base": 3.0, "sea_value": 1},
  "Laos/Cambodia":{"base": 2.2, "sea_value": 1},
  "Philippines":  {"base": 2.4, "sea_value": 1},
  "Turkey":       {"base": 1.0},
  "Greece":       {"base": 1.0},
  "Burma":        {"base": 0.8}
}

# Cards with strong Sankt-style event / space / hold tendencies.
# Keep this small and high-leverage.
CARD_POLICY = {
  "Captured Nazi Scientist": {
    "event_bias": +999,
    "space_bias": -999,
    "headline_bias_us_t1": +40
  },
  "Grain Sales to Soviets": {
    "event_bias": +999
  },
  "Aldrich Ames Remix": {
    "event_bias": +999
  },
  "Formosan Resolution": {
    "event_bias": -999
  },
  "COMECON": {
    "event_bias": -999
  },
  "NORAD": {
    "event_bias": -120,
    "space_bias_ussr": +30
  },
  "US/Japan Mutual Defense Pact": {
    "event_bias": +18,           # situational, not absolute
    "headline_bias_situational": +10
  },
  "NATO": {
    "event_bias": +8,            # situational, not autoplay
    "hold_bias_ussr_pre_t3": +18
  },
  "Five Year Plan": {
    "hold_bias_ussr_pre_t3": +40,
    "event_bias_when_single_bad_card_left": +35
  },
  "UN Intervention": {
    "hold_bias_ussr_pre_t3": +32
  },
  "Indo-Pakistani War": {
    "hold_bias_ussr_pre_t3": +18
  },
  "Duck and Cover": {
    "hold_bias_ussr_pre_t3": +14
  },
  "Defectors": {
    "hold_bias_ussr_pre_t3": +10
  },
  "Decolonization": {
    "space_bias_us_t1": +30
  },
  "De-Stalinization": {
    "hold_bias_us_pre_t3": +16
  },
  "Vietnam Revolts": {
    "space_bias_later": +16
  },
  "Korean War": {
    "space_bias_offside": +8,
    "event_ok_when_safe": +8
  },
  "Arab-Israeli War": {
    "space_bias_offside": +10
  },
  "Indo-Pakistani War (US side)": {
    "space_bias_offside": +10
  },
  "Brush War": {
    "space_bias_offside": +12
  },
  "ABM Treaty": {
    "headline_bias_ussr_when_break_plus_followup": +30
  },
  "Voice of America": {
    "custom_target_policy": 1
  },
  "OAS Founded": {
    "custom_target_policy": 1
  }
}


## 2. High-level context

struct Context:
  stage: Stage
  risk: RiskProfile
  ars_left_for_side: int
  scoring_cards_in_hand: list[Card]
  latest_safe_scoring_slots: list[int]
  region_weight: map[Region, float]
  europe_emergency: float
  space_pressure: float
  likely_bad_offside_space_card: Card | null
  opening_profile: string | null
  lost_region_cut: map[Region, float]


function compute_context(state: State, side: Side) -> Context:
  c = Context()

  c.stage = get_stage(state.turn)
  c.ars_left_for_side = count_remaining_actions_for_side_this_turn(state, side)
  c.scoring_cards_in_hand = [card for card in state.hand[side] if card.is_scoring]
  c.latest_safe_scoring_slots = compute_latest_safe_scoring_slots(
    state, side, size(c.scoring_cards_in_hand)
  )
  c.risk = compute_risk_profile(state, side)
  c.region_weight = compute_region_weights(state, side, c)
  c.europe_emergency = estimate_europe_emergency(state, side)
  c.space_pressure = estimate_space_pressure(state, side)
  c.likely_bad_offside_space_card = choose_bad_offside_card_to_space(state, side, c)
  c.opening_profile = detect_opening_profile(state, side)
  c.lost_region_cut = compute_lost_region_cut(state, side, c)

  return c


function get_stage(turn: int) -> Stage:
  if turn <= 3: return EARLY
  if turn <= 7: return MID
  return LATE


function compute_risk_profile(state: State, side: Side) -> RiskProfile:
  # Sankt/Aragorn correction:
  # if behind, raise variance; if ahead, lower variance; if close, maximize EV.
  margin = rough_global_eval(state, side)

  if state.turn == 10 and side_is_trailing(state, side):
    return GAMBLE

  if margin <= -7:
    return GAMBLE

  if margin >= +7 and position_is_stable(state, side):
    return CONSERVE

  return EV_MAX


function compute_region_weights(state: State, side: Side, c: Context) -> map[Region, float]:
  w = default_map(1.0)

  # Europe is always special.
  w[EUROPE] += 2.0

  # Scoring in hand spikes the region immediately.
  for card in c.scoring_cards_in_hand:
    w[card.scoring_region] += 4.0

  # Europe auto-end risk / chance is worth a huge premium.
  if europe_scoring_is_live_or_dangerous(state):
    w[EUROPE] += 3.5

  # Asia often becomes a sinkhole if you chase every cheap non-BG.
  # Prefer parity if the board is already acceptable and no scoring is urgent.
  if c.stage == EARLY and ASIA not in [card.scoring_region for card in c.scoring_cards_in_hand]:
    if asia_is_acceptable_at_parity(state, side):
      w[ASIA] *= 0.80

  # SE Asia gets extra weight when the special scoring is still live or Asia count is close.
  if southeast_asia_scoring_still_live(state):
    w[SOUTHEAST_ASIA] += 1.2
  if asia_country_count_is_close(state):
    w[SOUTHEAST_ASIA] += 0.6

  # Transition into Mid War: Mexico / Algeria / Angola / Panama matter.
  if state.turn == 3 and is_late_turn_slot(state, side):
    w[CENTRAL_AMERICA] += 0.8
    w[SOUTH_AMERICA] += 0.4
    w[AFRICA] += 0.8

  # If a region is badly lost and Europe is not involved, downweight rescue attempts
  # unless the score is imminent.
  for r in [ASIA, MIDDLE_EAST, CENTRAL_AMERICA, SOUTH_AMERICA, AFRICA]:
    if region_is_badly_lost(state, side, r) and r not in [card.scoring_region for card in c.scoring_cards_in_hand]:
      w[r] *= 0.65

  return w


function compute_lost_region_cut(state: State, side: Side, c: Context) -> map[Region, float]:
  cut = default_map(1.0)
  for r in [ASIA, MIDDLE_EAST, CENTRAL_AMERICA, SOUTH_AMERICA, AFRICA]:
    if region_is_badly_lost(state, side, r) and r not in [card.scoring_region for card in c.scoring_cards_in_hand]:
      cut[r] = 0.6
  cut[EUROPE] = 1.0
  return cut


function estimate_space_pressure(state: State, side: Side) -> float:
  # space is a real VP race, not just a trash can
  s = 0
  s += immediate_space_vp_gain_if_success(state, side)
  s += ability_value_if_reach_next_space_first(state, side)
  if state.space_pos[side] < state.space_pos[other(side)]:
    s += 1.5
  if state.turn <= 3:
    s += 1.0
  return s


function estimate_europe_emergency(state: State, side: Side) -> float:
  if not europe_scoring_is_live_or_dangerous(state):
    return 0.0

  if would_side_control_europe(state, side):
    return 10.0
  if would_side_control_europe(state, other(side)):
    return 10.0

  return 4.0


## 3. Public entry points

function choose_rollout_action(state: State, side: Side) -> Action:
  if state.phase == SETUP:
    return choose_initial_setup(state, side)

  if state.phase == HEADLINE:
    return choose_headline(state, side)

  c = compute_context(state, side)

  candidates = enumerate_candidate_actions(state, side, c)
  candidates = [a for a in candidates if hard_filter_action(state, side, a, c)]

  if candidates is empty:
    return fallback_legal_action(state, side)

  forced = choose_forced_action(state, side, candidates, c)
  if forced != null:
    return forced

  scored = []
  for a in candidates:
    s = score_action(state, side, a, c)
    scored.append((a, s))

  scored.sort(desc by s)

  return softmax_sample_top_k(
    scored,
    Weights.TOP_K,
    choose_temperature(c)
  )


function choose_temperature(c: Context) -> float:
  if c.europe_emergency >= 8 or must_spend_scoring_now(c):
    return Weights.TEMP_EMERGENCY
  if c.risk != EV_MAX or c.space_pressure >= 4:
    return Weights.TEMP_URGENT
  return Weights.TEMP_CALM


function choose_headline(state: State, side: Side) -> Action:
  c = compute_context(state, side)
  candidates = enumerate_headline_candidates(state, side, c)
  candidates = [a for a in candidates if hard_filter_action(state, side, a, c)]

  scored = []
  for a in candidates:
    scored.append((a, score_headline_action(state, side, a, c)))

  scored.sort(desc by second)

  return softmax_sample_top_k(
    scored,
    Weights.TOP_K,
    choose_temperature(c)
  )


## 4. Setup / opening hooks

function choose_initial_setup(state: State, side: Side) -> Action:
  if side == US:
    return choose_initial_setup_us(state)
  return choose_initial_setup_ussr(state)


function choose_initial_setup_us(state: State) -> Action:
  hand = state.hand[US]
  headline = guess_best_turn1_headline_us(hand)

  setup = base_standard_us_setup()

  # Sankt correction:
  # Marshall Plan setup is aggressive toward France / Europe domination.
  if headline.name == "Marshall Plan":
    setup = {
      "West Germany": 3,
      "Italy": 2,
      "France": 2,
      "UK": 0,
      "Iran": 1,
      "Israel": 1,
      "Japan": 1,
      "Australia": 4,
      "Philippines": 1,
      "South Korea": 1,
      "Panama": 1,
      "South Africa": 1
    }
    # Marshall event placements are not part of setup; headline/event logic handles them.

  else:
    # default Chinese-style non-Marshall opening is often 4/4/2
    if hand_contains_any(hand, ["Nasser", "Europe Scoring", "Suez Crisis", "Arab-Israeli War"]) or
       (contains(hand, "Middle East Scoring") and headline.name == "Middle East Scoring"):
      setup = standard_4_4_2()
    elif contains(hand, "Socialist Governments") or headline.name == "Red Scare/Purge":
      setup = standard_4_3_3()
    else:
      setup = standard_4_4_2()

  # Empty West Germany is almost never correct; do not do it unless a very special hand hook says so.
  if should_consider_empty_wg_exception(hand):
    setup = special_1_wg_3_fr_blockade_setup()

  return Action(type = INITIAL_SETUP, setup_assignment = setup)


function choose_initial_setup_ussr(state: State) -> Action:
  # standard USSR setup usually fine; exact opening branches are handled by AR1 / headline policy
  return Action(type = INITIAL_SETUP, setup_assignment = base_standard_ussr_setup())


function guess_best_turn1_headline_us(hand: list[Card]) -> Card:
  # approximate ranking from Sankt summary:
  # Marshall > strong Containment > ME Scoring = Red Scare/Purge > CNS > weaker Containment
  if contains(hand, "Marshall Plan"):
    return get_card(hand, "Marshall Plan")

  if contains(hand, "Containment") and containment_is_5plus_or_blockade_protection(hand):
    return get_card(hand, "Containment")

  if contains(hand, "Middle East Scoring"):
    return get_card(hand, "Middle East Scoring")

  if contains(hand, "Red Scare/Purge"):
    return get_card(hand, "Red Scare/Purge")

  if contains(hand, "Captured Nazi Scientist"):
    return get_card(hand, "Captured Nazi Scientist")

  if contains(hand, "Containment"):
    return get_card(hand, "Containment")

  return generic_best_headline_card(hand, US)


function detect_opening_profile(state: State, side: Side) -> string | null:
  if state.turn != 1:
    return null

  if side == US:
    return "US_T1"

  return "USSR_T1"


## 5. Forced overrides

function choose_forced_action(state: State, side: Side, candidates: list[Action], c: Context) -> Action | null:
  # 5.1 never choose self-nuke if any non-self-nuke action exists
  safe = [a for a in candidates if not action_causes_immediate_self_loss_via_defcon(state, side, a)]
  if size(safe) > 0:
    candidates = safe

  # 5.2 scoring must be scheduled, but not necessarily immediately
  forced_scoring = force_scoring_if_latest_safe_slot(state, side, candidates, c)
  if forced_scoring != null:
    return forced_scoring

  # 5.3 if there is an immediate Europe autowin or auto-loss branch, tunnel on it
  forced_europe = force_europe_branch(state, side, candidates, c)
  if forced_europe != null:
    return forced_europe

  # 5.4 Turn 10 final action / desperate endgame:
  # if normal lines do not win and we are behind, allow miracle realignment / high-variance lines
  forced_endgame = force_endgame_gamble(state, side, candidates, c)
  if forced_endgame != null:
    return forced_endgame

  # 5.5 if there is a toxic offside card that space cleanly fixes and the race is good, strongly prefer it
  forced_space = force_space_bad_card_when_superior(state, side, candidates, c)
  if forced_space != null:
    return forced_space

  return null


function force_scoring_if_latest_safe_slot(state: State, side: Side, candidates: list[Action], c: Context) -> Action | null:
  scoring_actions = [a for a in candidates if a.type == PLAY_SCORING]
  if scoring_actions is empty:
    return null

  current_slot = current_side_action_slot(state, side)
  if current_slot not in c.latest_safe_scoring_slots:
    return null

  # correction:
  # scoring is usually delayed to latest safe slot, not auto-played ASAP
  # however, if multiple scoring cards occupy multiple reserved slots, we must use the slot
  best = argmax(scoring_actions, lambda a: score_scoring_action(state, side, a, c))
  return best


function force_europe_branch(state: State, side: Side, candidates: list[Action], c: Context) -> Action | null:
  if c.europe_emergency < 8:
    return null

  best = null
  best_score = -1e18

  for a in candidates:
    delta = estimate_local_region_effect(state, side, a, EUROPE)
    if delta > best_score:
      best_score = delta
      best = a

  if best_score > 0:
    return best
  return null


function force_endgame_gamble(state: State, side: Side, candidates: list[Action], c: Context) -> Action | null:
  if c.risk != GAMBLE:
    return null

  if state.turn != 10:
    return null

  if not is_last_or_near_last_action_for_side(state, side):
    return null

  # if a normal influence line cannot win, try coup / realign / war-event variance
  tactical = [a for a in candidates if a.type in [
    PLAY_OPS_REALIGN, PLAY_CHINA_REALIGN, PLAY_OPS_COUP, PLAY_CHINA_COUP, PLAY_EVENT
  ]]

  if tactical is empty:
    return null

  best = argmax(tactical, lambda a: score_action(state, side, a, c))
  return best


function force_space_bad_card_when_superior(state: State, side: Side, candidates: list[Action], c: Context) -> Action | null:
  if c.likely_bad_offside_space_card == null:
    return null

  for a in candidates:
    if a.type == SPACE_CARD and a.card.id == c.likely_bad_offside_space_card.id:
      if score_action(state, side, a, c) >= best_non_space_score(candidates, state, side, c) - 3:
        return a

  return null


function must_spend_scoring_now(c: Context) -> bool:
  # if we are already on a reserved latest-safe slot, scoring is effectively forced
  return size(c.scoring_cards_in_hand) > 0 and size(c.latest_safe_scoring_slots) > 0


## 6. Candidate generation

function enumerate_candidate_actions(state: State, side: Side, c: Context) -> list[Action]:
  out = []

  # scoring cards are always legal candidates, but their timing is scored intelligently
  for card in state.hand[side]:
    if card.is_scoring:
      out.append(Action(
        type = PLAY_SCORING,
        card = card,
        scoring_region = card.scoring_region,
        event_timing = NONE
      ))

  for card in state.hand[side]:
    if card.is_scoring:
      continue

    # play event
    if can_play_event(state, side, card):
      out.append(Action(
        type = PLAY_EVENT,
        card = card,
        event_timing = NONE
      ))

    # space
    if can_space_card(state, side, card):
      out.append(Action(
        type = SPACE_CARD,
        card = card,
        event_timing = NONE
      ))

    # operations
    if card.is_china:
      out.extend(generate_china_ops_candidates(state, side, card, c))
    else:
      out.extend(generate_ops_candidates(state, side, card, c))

  return dedupe_actions(out)


function enumerate_headline_candidates(state: State, side: Side, c: Context) -> list[Action]:
  out = []

  for card in state.hand[side]:
    if card.is_china:
      continue

    out.append(Action(
      type = HEADLINE_CARD,
      card = card,
      scoring_region = card.scoring_region if card.is_scoring else null,
      event_timing = NONE
    ))

  return out


function generate_ops_candidates(state: State, side: Side, card: Card, c: Context) -> list[Action]:
  out = []

  # Opening templates first: they matter a lot and are cheap to encode.
  if c.opening_profile == "USSR_T1" and side == USSR:
    out.extend(generate_ussr_t1_opening_candidates(state, card, c))

  if c.opening_profile == "US_T1" and side == US:
    out.extend(generate_us_t1_opening_candidates(state, card, c))

  # Generic influence templates.
  for objective in [
    "EUROPE_SWING",
    "SCORING_REPAIR",
    "SCORING_ATTACK",
    "BG_COMPLETE",
    "ACCESS_TOUCH",
    "DOMINATION_FILL",
    "REALIGN_SHIELD",
    "T4_STAGING",
    "BEST_GENERAL_VALUE"
  ]:
    plan = build_influence_plan(state, side, card, objective, c, asia_only = false)
    if plan != null and plan.placements not empty:
      out.append(Action(
        type = PLAY_OPS_INFLUENCE,
        card = card,
        placements = plan.placements,
        event_timing = choose_event_timing_if_needed(state, side, card, plan),
        tags = set([objective])
      ))

  for target in top_coup_targets(state, side, card, c, limit = 3):
    out.append(Action(
      type = PLAY_OPS_COUP,
      card = card,
      target_country = target,
      event_timing = choose_event_timing_if_needed(state, side, card, target)
    ))

  for target in top_realign_targets(state, side, card, c, limit = 2):
    out.append(Action(
      type = PLAY_OPS_REALIGN,
      card = card,
      target_country = target,
      event_timing = choose_event_timing_if_needed(state, side, card, target)
    ))

  return dedupe_actions(out)


function generate_china_ops_candidates(state: State, side: Side, china: Card, c: Context) -> list[Action]:
  out = []

  for objective in [
    "ASIA_PARITY_REPAIR",
    "ASIA_ATTACK_WHEN_WORTH_IT",
    "ASIA_BG_COMPLETE",
    "BEST_GENERAL_VALUE"
  ]:
    plan = build_influence_plan(state, side, china, objective, c, asia_only = true)
    if plan != null and plan.placements not empty:
      out.append(Action(
        type = PLAY_CHINA_INFLUENCE,
        card = china,
        placements = plan.placements,
        event_timing = NONE,
        tags = set([objective])
      ))

  for target in top_coup_targets(state, side, china, c, limit = 2, asia_only = true):
    out.append(Action(
      type = PLAY_CHINA_COUP,
      card = china,
      target_country = target,
      event_timing = NONE
    ))

  for target in top_realign_targets(state, side, china, c, limit = 2, asia_only = true):
    out.append(Action(
      type = PLAY_CHINA_REALIGN,
      card = china,
      target_country = target,
      event_timing = NONE
    ))

  return dedupe_actions(out)


function generate_ussr_t1_opening_candidates(state: State, card: Card, c: Context) -> list[Action]:
  out = []

  # Sankt correction:
  # prefer Italy over Iran if Italy coup odds are good enough; otherwise spread influence.
  if can_coup_country(state, USSR, "Italy"):
    out.append(Action(
      type = PLAY_OPS_COUP,
      card = card,
      target_country = "Italy",
      event_timing = choose_event_timing_if_needed(state, USSR, card, "Italy"),
      tags = set(["OPENING_ITALY"])
    ))

  if can_coup_country(state, USSR, "Iran"):
    out.append(Action(
      type = PLAY_OPS_COUP,
      card = card,
      target_country = "Iran",
      event_timing = choose_event_timing_if_needed(state, USSR, card, "Iran"),
      tags = set(["OPENING_IRAN"])
    ))

  # Influence spread option: Afghanistan + Israel often forces the US in two directions.
  plan = scripted_plan_if_affordable(state, USSR, card, [
    ("Afghanistan", 1),
    ("Israel", 1)
  ])
  if plan != null:
    out.append(Action(
      type = PLAY_OPS_INFLUENCE,
      card = card,
      placements = plan.placements,
      event_timing = choose_event_timing_if_needed(state, USSR, card, plan),
      tags = set(["OPENING_AFG_ISRAEL"])
    ))

  # Strong-opponent line: add West Germany pressure as well.
  plan = scripted_plan_if_affordable(state, USSR, card, [
    ("Afghanistan", 1),
    ("Israel", 1),
    ("West Germany", 1)
  ])
  if plan != null:
    out.append(Action(
      type = PLAY_OPS_INFLUENCE,
      card = card,
      placements = plan.placements,
      event_timing = choose_event_timing_if_needed(state, USSR, card, plan),
      tags = set(["OPENING_WG_PRESSURE"])
    ))

  return dedupe_actions(out)


function generate_us_t1_opening_candidates(state: State, card: Card, c: Context) -> list[Action]:
  out = []

  # If Italy got hit, rebuild Italy before panicking elsewhere.
  plan = scripted_plan_if_affordable(state, US, card, [
    ("Italy", required_to_reach_influence(state, US, "Italy", target = 3)),
    ("France", 1),
    ("Malaysia", 1),
    ("Egypt", 1)
  ])
  if plan != null:
    out.append(Action(
      type = PLAY_OPS_INFLUENCE,
      card = card,
      placements = plan.placements,
      event_timing = choose_event_timing_if_needed(state, US, card, plan),
      tags = set(["OPENING_REPAIR_ITALY"])
    ))

  # No USSR coup / DEFCON 5: Pakistan becomes a major priority.
  plan = scripted_plan_if_affordable(state, US, card, [
    ("Pakistan", 2),
    ("Egypt", 2)
  ])
  if plan != null:
    out.append(Action(
      type = PLAY_OPS_INFLUENCE,
      card = card,
      placements = plan.placements,
      event_timing = choose_event_timing_if_needed(state, US, card, plan),
      tags = set(["OPENING_PAK_EGYPT"])
    ))

  plan = scripted_plan_if_affordable(state, US, card, [
    ("Pakistan", 2),
    ("Malaysia", 1),
    ("France", 1)
  ])
  if plan != null:
    out.append(Action(
      type = PLAY_OPS_INFLUENCE,
      card = card,
      placements = plan.placements,
      event_timing = choose_event_timing_if_needed(state, US, card, plan),
      tags = set(["OPENING_PAK_MAL_FR"])
    ))

  # Costa Rica touch if Panama is exposed.
  plan = scripted_plan_if_affordable(state, US, card, [
    ("Costa Rica", 1)
  ])
  if plan != null:
    out.append(Action(
      type = PLAY_OPS_INFLUENCE,
      card = card,
      placements = plan.placements,
      event_timing = choose_event_timing_if_needed(state, US, card, plan),
      tags = set(["OPENING_COSTA_RICA"])
    ))

  return dedupe_actions(out)


## 7. Hard filters

function hard_filter_action(state: State, side: Side, a: Action, c: Context) -> bool:
  if not engine_is_legal(state, side, a):
    return false

  if action_causes_immediate_self_loss_via_defcon(state, side, a):
    return false

  if is_china_action(a) and china_play_would_strand_scoring(state, side, c):
    return false

  # Avoid pure dominated junk actions in rollout.
  if action_is_purely_zero_value_and_dominated(state, side, a):
    return false

  return true


function china_play_would_strand_scoring(state: State, side: Side, c: Context) -> bool:
  # Official rule forbids using China if it prevents scoring.
  scoring_count = size(c.scoring_cards_in_hand)
  ars_left = c.ars_left_for_side

  return scoring_count >= ars_left


## 8. Top-level scoring

function score_action(state: State, side: Side, a: Action, c: Context) -> float:
  if not engine_is_legal(state, side, a):
    return Weights.ILLEGAL
  if action_causes_immediate_self_loss_via_defcon(state, side, a):
    return Weights.AUTO_LOSS

  if a.type == PLAY_SCORING:
    return score_scoring_action(state, side, a, c)

  if a.type == PLAY_EVENT:
    return score_event_action(state, side, a, c)

  if a.type == SPACE_CARD:
    return score_space_action(state, side, a, c)

  if a.type in [PLAY_OPS_INFLUENCE, PLAY_CHINA_INFLUENCE]:
    return score_influence_action(state, side, a, c)

  if a.type in [PLAY_OPS_COUP, PLAY_CHINA_COUP]:
    return score_coup_action(state, side, a, c)

  if a.type in [PLAY_OPS_REALIGN, PLAY_CHINA_REALIGN]:
    return score_realign_action(state, side, a, c)

  return -999999


function score_headline_action(state: State, side: Side, a: Action, c: Context) -> float:
  card = a.card

  if card.is_scoring:
    return score_headline_scoring(state, side, a, c)

  s = 0

  # high-ops headline tempo matters
  s += 3 * card.ops

  # general event value
  s += 20 * estimate_event_value(state, side, card, c)

  # turn 1 US ranking hooks
  if state.turn == 1 and side == US:
    if card.name == "Marshall Plan":
      s += 60
    if card.name == "Containment" and containment_is_5plus_or_blockade_protection(state.hand[US]):
      s += 45
    if card.name == "Middle East Scoring":
      s += 35
    if card.name == "Red Scare/Purge":
      s += 35
    if card.name == "Captured Nazi Scientist":
      s += 28

  # USSR ABM headline hook
  if card.name == "ABM Treaty" and side == USSR and abm_break_plus_followup_exists(state, side):
    s += 30

  # offside headline safety
  if event_owner_for_card(card) == other(side):
    s -= 28 * estimate_offside_event_cost(state, side, card, c)

  # Europe emergency
  s += 12 * estimate_headline_region_effect(state, side, card, EUROPE) * c.europe_emergency

  # scoring timing repair / exploit
  for r in [x.scoring_region for x in c.scoring_cards_in_hand]:
    s += 8 * estimate_headline_region_effect(state, side, card, r)

  # custom per-card hook
  s += card_policy_bonus(state, side, card, mode = "headline", c = c)

  return s


## 9. Scoring cards

function score_scoring_action(state: State, side: Side, a: Action, c: Context) -> float:
  r = a.scoring_region
  current_slot = current_side_action_slot(state, side)

  score_now = estimate_scoring_points(state, side, r) - estimate_scoring_points(state, other(side), r)
  repair_1 = estimate_best_one_card_repair_value(state, side, r)
  repair_2 = estimate_best_two_card_repair_value(state, side, r)

  s = 0
  s += Weights.IMMEDIATE_VP * score_now

  # latest-safe scheduling:
  # usually delay scoring to the latest safe slot, especially if the current score is bad.
  if current_slot in c.latest_safe_scoring_slots:
    s += Weights.LATEST_SAFE_SCORING_BONUS
  else:
    if score_now <= 0 and current_slot < max(c.latest_safe_scoring_slots):
      s += Weights.EARLY_SCORING_DELAY

  # if scoring now is strong and opponent repair risk is large, immediate cash-in can be right
  s += 6 * max(0, estimate_opponent_repair_risk_before_next_safe_slot(state, side, r))

  # if we still have slack and repair upside exists, delay
  if current_slot < max(c.latest_safe_scoring_slots):
    s -= 4 * max(0, repair_1)
    s -= 2 * max(0, repair_2)

  # Europe special handling
  if r == EUROPE:
    if would_side_control_europe(state, side):
      s += Weights.EUROPE_AUTOWIN
    if would_side_control_europe(state, other(side)):
      s += Weights.EUROPE_AUTOLOSS

  # SE Asia special handling
  if r == SOUTHEAST_ASIA:
    s += 3 * exact_seasia_score(state, side)

  # desperate nuance:
  # if scoring now immediately loses and we still have a later safe slot, do NOT cash it in yet
  if scoring_now_causes_immediate_loss(state, side, r) and current_slot < max(c.latest_safe_scoring_slots):
    s -= 20000

  return s


function score_headline_scoring(state: State, side: Side, a: Action, c: Context) -> float:
  r = a.scoring_region
  s = score_scoring_action(state, side, a, c)

  # headline scoring is best when current score is already favorable
  # and opponent repair tempo would be dangerous.
  s += 8 * estimate_opponent_repair_risk_if_not_headlined(state, side, r)

  # Europe scoring headline with huge position can simply be game-ending
  if r == EUROPE and would_side_control_europe(state, side):
    s += Weights.EUROPE_AUTOWIN

  return s


## 10. Events / space / hand management

function score_event_action(state: State, side: Side, a: Action, c: Context) -> float:
  card = a.card
  owner = event_owner_for_card(card)

  s = 0
  s += 18 * estimate_event_value(state, side, card, c)

  if owner == other(side):
    s -= 25 * estimate_offside_event_cost(state, side, card, c)

  s += card_policy_bonus(state, side, card, mode = "event", c = c)

  # region-sensitive hooks
  for r in [EUROPE, ASIA, MIDDLE_EAST, CENTRAL_AMERICA, SOUTH_AMERICA, AFRICA, SOUTHEAST_ASIA]:
    s += c.region_weight[r] * estimate_event_region_effect(state, side, card, r)

  # if the event can be burned with minimal effect and spacing it would waste a powerful event body,
  # prefer event over space
  if event_can_be_burned_cheaply_now(state, side, card):
    s += 10

  # if behind, war events and hand-disruption get extra volatility credit
  if c.risk == GAMBLE and event_is_high_variance_or_hand_attack(card):
    s += Weights.GAMBLE_WAR_EVENT_BONUS

  return s


function score_space_action(state: State, side: Side, a: Action, c: Context) -> float:
  card = a.card
  s = 0

  s += Weights.SPACE_RACE_VALUE * immediate_space_vp_gain_if_success(state, side)
  s += Weights.SPACE_SPECIAL_ABILITY * ability_value_if_reach_next_space_first(state, side)
  s += 8 * c.space_pressure

  # space is a safety valve
  if event_owner_for_card(card) == other(side):
    s += 15 * estimate_offside_event_cost(state, side, card, c)

  # space enemy war cards when possible; they can grant VP + MilOps on top of the board swing
  if is_enemy_war_card_for_side(card, side):
    s += 12

  # Korean War exception: sometimes just firing it is cleaner than spacing it
  if card.name == "Korean War" and korean_war_is_safe_to_burn(state, side):
    s -= 8

  # If the event is stronger burned on board with minimal effect, do not auto-space it.
  if event_can_be_burned_cheaply_now(state, side, card):
    s -= 12

  # Captured Nazi Scientist should effectively never be spaced.
  s += card_policy_bonus(state, side, card, mode = "space", c = c)

  # One Small Step caution:
  # do not love entering Mid War with a fragile 2-1 lead if OSS is likely to punish it.
  if entering_midwar_with_fragile_space_lead(state, side):
    s -= 4

  return s


function score_hand_management_overlay(state: State, side: Side, a: Action, c: Context) -> float:
  if a.card == null:
    return 0

  card = a.card
  s = 0

  # pre-T3 USSR hold priorities
  if side == USSR and state.turn <= 2:
    s -= hold_bias_pre_t3_ussr(card, state, side, c)

  # pre-T3 US specific handling
  if side == US and state.turn <= 2:
    s -= hold_bias_pre_t3_us(card, state, side, c)

  # China preservation:
  # generally save China for large Asia swings, unless a specific opening Italy line needs the 4-op body.
  if card.is_china:
    if action_targets_non_asia_regions(a):
      s -= 15
    if c.region_weight[ASIA] > 2.5:
      s += 8

  return s


function hold_bias_pre_t3_ussr(card: Card, state: State, side: Side, c: Context) -> float:
  bias = 0

  if card.name == "Five Year Plan":
    bias += 30
  elif card.name == "UN Intervention":
    if not already_have_strong_4op_us_event_to_pair(state.hand[USSR]):
      bias += 24
  elif strong_4op_us_event(card):
    bias += 20
  elif card.name == "Indo-Pakistani War":
    bias += 16
  elif card.name == "Duck and Cover":
    bias += 12
  elif card.name == "Defectors":
    bias += 8

  # if we are in a hard emergency, do not overpreserve
  if c.risk == GAMBLE or must_spend_scoring_now(c):
    bias *= 0.4

  return bias


function hold_bias_pre_t3_us(card: Card, state: State, side: Side, c: Context) -> float:
  bias = 0

  if card.name == "Decolonization" and state.turn == 1:
    # Sankt-style US often prefers to space Decol on T1 due to Blockade / hand-size realities,
    # so "hold" is actually negative here; using it or spacing it may be superior.
    bias -= 12

  if card.name == "De-Stalinization":
    bias += 12

  return max(0, bias)


## 11. Influence scoring

function score_influence_action(state: State, side: Side, a: Action, c: Context) -> float:
  before = snapshot_region_features(state, side)
  next_state = cheap_apply_action_for_eval(state, side, a)
  after = snapshot_region_features(next_state, side)

  s = 0

  for r in [EUROPE, ASIA, MIDDLE_EAST, CENTRAL_AMERICA, SOUTH_AMERICA, AFRICA, SOUTHEAST_ASIA]:
    w = c.region_weight[r] * c.lost_region_cut[r]

    s += w * (
      Weights.SCORING_SAFETY * (after.scoring_safety[r] - before.scoring_safety[r]) +
      Weights.BG_SWING * (after.bg_margin[r] - before.bg_margin[r]) +
      Weights.DOMINATION_SWING * (after.domination_margin[r] - before.domination_margin[r]) +
      Weights.ACCESS_CREATION * (after.access[r] - before.access[r]) +
      Weights.DEFENSE_BUFFER * (after.buffer[r] - before.buffer[r])
    )

  # special Europe premium
  s += Weights.EUROPE_SWING * estimate_local_region_effect(state, side, a, EUROPE)

  # do not control-break without capitalizing
  s += Weights.DANGLING_BREAK * count_dangling_control_breaks(state, side, a)

  # non-BG overinvestment is usually bad
  s += Weights.USELESS_NON_BG * count_useless_nonbg_placements(state, side, a, c)

  # wasted Ops
  s += Weights.WASTED_OPS * estimate_wasted_ops(state, side, a)

  # offside event cost if using opponent card for Ops
  s += Weights.LIVE_OFFSIDE_EVENT_COST * event_cost_if_ops_triggers_opponent_event(state, side, a, c)

  # China Asia-only bonus
  if is_china_action(a) and action_is_all_asia_or_seasia(a):
    s += 8

  # risk modulation
  if c.risk == CONSERVE:
    s -= estimate_line_variance(state, side, a) * 4

  return s


function snapshot_region_features(state: State, side: Side):
  f = object()
  for r in [EUROPE, ASIA, MIDDLE_EAST, CENTRAL_AMERICA, SOUTH_AMERICA, AFRICA, SOUTHEAST_ASIA]:
    f.scoring_safety[r] = estimate_scoring_points(state, side, r) - estimate_scoring_points(state, other(side), r)
    f.bg_margin[r] = estimate_bg_margin(state, side, r)
    f.domination_margin[r] = estimate_domination_margin(state, side, r)
    f.access[r] = estimate_region_access(state, side, r)
    f.buffer[r] = estimate_region_buffer(state, side, r)
  return f


## 12. Influence plan builder (corrected)
#
# Key correction:
# - do NOT greedily place single points only
# - generate small bundles per country so the plan can complete control,
#   not merely break control and drift away
# - placement cost must be sequence-aware in enemy-controlled countries
#   (breaking control can make later points cheaper inside the same action)

struct InfluencePlan:
  placements: list[(CountryName, count)]


function build_influence_plan(
  state: State,
  side: Side,
  card: Card,
  objective: string,
  c: Context,
  asia_only: bool
) -> InfluencePlan | null:

  ops = effective_ops_for_card_in_mode(state, side, card, mode = "INFLUENCE", asia_only = asia_only)
  if ops <= 0:
    return null

  working = clone_shallow(state)
  placements = []

  while ops > 0:
    options = []

    for country in legal_influence_targets(working, side, asia_only):
      for bundle_size in feasible_bundle_sizes(working, side, country, ops):
        cost = placement_sequence_cost_to_add_n(working, side, country, bundle_size)
        if cost > ops:
          continue

        value = bundled_placement_value(working, side, country, bundle_size, objective, c)
        value_per_op = value / max(1, cost)

        options.append((country, bundle_size, cost, value_per_op, value))

    if options is empty:
      break

    best = argmax(options, lambda x: x.value_per_op)

    if best.value_per_op <= 0:
      break

    apply_n_influence_sequence_aware(working, side, best.country, best.bundle_size)
    placements.append((best.country, best.bundle_size))
    ops -= best.cost

  if placements empty:
    return null

  return InfluencePlan(placements = compress_same_country(placements))


function feasible_bundle_sizes(state: State, side: Side, country_name: CountryName, ops_available: int) -> list[int]:
  # small bundles only; cheap enough for rollout
  out = [1]

  break_need = placements_needed_to_break_control(state, side, country_name)
  take_need = placements_needed_to_take_control(state, side, country_name)

  if break_need > 1:
    out.append(min(break_need, 3))

  if take_need > 1:
    out.append(min(take_need, 4))

  if break_need < take_need and take_need <= 5:
    out.append(take_need)

  # also allow 2-point bundle when access + defense or domination filler matters
  out.append(2)

  return dedupe(sorted(filter(x > 0, out)))


function bundled_placement_value(
  state: State,
  side: Side,
  country_name: CountryName,
  bundle_size: int,
  objective: string,
  c: Context
) -> float:

  before = cheap_country_eval_context(state, side, country_name)
  next_state = clone_shallow(state)
  apply_n_influence_sequence_aware(next_state, side, country_name, bundle_size)
  after = cheap_country_eval_context(next_state, side, country_name)

  country = state.countries[country_name]
  value = 0

  # base country value
  value += country_local_value(state, side, country_name, c)

  # control capture matters much more than control break alone
  if before.we_control == false and after.we_control == true:
    value += 8.0
  elif before.they_control == true and after.they_control == false and after.we_control == false:
    value += 1.5
    value -= 3.0   # dangling break unless scoring / access says otherwise

  # region changes
  for r in country.regions:
    value += c.region_weight[r] * (
      3.5 * (after.scoring_safety[r] - before.scoring_safety[r]) +
      2.5 * (after.bg_margin[r] - before.bg_margin[r]) +
      2.0 * (after.domination_margin[r] - before.domination_margin[r]) +
      1.5 * (after.access[r] - before.access[r])
    )

  # objective-specific shaping
  if objective == "EUROPE_SWING":
    if EUROPE in country.regions:
      value += 7.0
    else:
      value -= 2.0

  elif objective == "SCORING_REPAIR":
    value += 5.0 * biggest_scoring_region_safety_delta(before, after)

  elif objective == "SCORING_ATTACK":
    value += 4.0 * biggest_opponent_scoring_damage_delta(before, after)

  elif objective == "BG_COMPLETE":
    if country.battleground:
      value += 5.0
    else:
      value -= 2.0

  elif objective == "ACCESS_TOUCH":
    value += 4.0 * (after.access_total - before.access_total)

  elif objective == "DOMINATION_FILL":
    if not country.battleground:
      value += 3.0 * (after.domination_margin_total - before.domination_margin_total)

  elif objective == "REALIGN_SHIELD":
    if country_name in REALIGN_SHIELD_COUNTRIES:
      value += 5.0

  elif objective == "T4_STAGING":
    if country_name in ["Mexico", "Algeria", "Angola", "Panama"]:
      value += 5.0

  elif objective == "ASIA_PARITY_REPAIR":
    if ASIA in country.regions or SOUTHEAST_ASIA in country.regions:
      value += 4.0
    else:
      value -= 3.0

  elif objective == "ASIA_ATTACK_WHEN_WORTH_IT":
    if ASIA in country.regions or SOUTHEAST_ASIA in country.regions:
      value += 3.0
    else:
      value -= 3.0

  # if country is access-only and we already have the touch, further points are often bad
  if country_name in ACCESS_ONLY_CAP:
    cap = ACCESS_ONLY_CAP[country_name]
    if next_state.countries[country_name].influence[side] > cap and not immediate_scoring_or_domination_need(next_state, side, country_name):
      value -= 4.0 * (next_state.countries[country_name].influence[side] - cap)

  # Asia black-hole correction:
  # extra Asia non-BG points beyond parity / domination needs should be punished.
  if (ASIA in country.regions or SOUTHEAST_ASIA in country.regions) and not country.battleground:
    if asia_extra_nonbg_is_not_needed(next_state, side, country_name):
      value -= 3.0

  return value


function country_local_value(state: State, side: Side, country_name: CountryName, c: Context) -> float:
  country = state.countries[country_name]
  value = COUNTRY_HOOK.get(country_name, {}).get("base", 0.0)

  if country.battleground:
    if EUROPE in country.regions:
      value += dynamic_europe_bg_value(state, side, country_name)
    else:
      base_region = any_non_seasia_region(country.regions)
      value += BG_VP_PRIOR.get(base_region, 0.0)

    value += BG_STABILITY_BONUS[country.stability]

  else:
    value += BASE_NON_BG_VALUE

    if country_name in ACCESS_ONLY_CAP:
      if state.countries[country_name].influence[side] == 0:
        value += 3.0

    if country_name in REALIGN_SHIELD_COUNTRIES:
      value += 2.5

    if SOUTHEAST_ASIA in country.regions:
      value += SEA_NON_BG_VALUE

  # France / Europe correction: do not be too afraid of De Gaulle / Suez if the score geometry says France matters
  if country_name == "France" and europe_scoring_is_live_or_dangerous(state):
    value += 6.0

  # Italy is huge in Europe opening / scoring geometry
  if country_name == "Italy" and europe_scoring_is_live_or_dangerous(state):
    value += 4.0

  # Thailand logic: extremely valuable, but US often wants Malaysia touch before Thailand at DEFCON 5
  if country_name == "Thailand" and side == US and state.defcon == 5 and not asia_scoring_urgent(state, side):
    value -= 2.0

  # Pakistan / Egypt / Costa Rica / Lebanon specific early-game boosts
  if country_name == "Pakistan" and side == US and state.turn == 1 and state.defcon == 5:
    value += 3.5
  if country_name == "Egypt" and side == US and state.turn <= 2:
    value += 3.0
  if country_name == "Costa Rica" and side == US and panama_is_exposed(state):
    value += 3.0
  if country_name == "Lebanon" and side == US and state.turn <= 2:
    value += 2.0

  # USSR early Greece / Turkey minimalism
  if side == USSR and state.turn == 1 and country_name in ["Greece", "Turkey"]:
    value -= 2.5

  # Do not let hypothetical enemy events scare you off good immediate-return countries too much.
  value -= looming_enemy_event_fear_penalty(state, side, country_name) * 0.25

  return value


function dynamic_europe_bg_value(state: State, side: Side, country_name: CountryName) -> float:
  bg_count = count_controlled_bgs_in_region(state, side, EUROPE)

  # rough Sankt/Aragorn style:
  # 3rd BG huge, 4th BG smallish, 5th BG / control enormous
  if would_this_country_be_nth_europe_bg(state, side, country_name, 3):
    return 8.0
  if would_this_country_be_nth_europe_bg(state, side, country_name, 4):
    return 2.0
  if would_this_country_enable_europe_control(state, side, country_name):
    return 100.0

  return 4.0


## 13. Coup / realignment

function score_coup_action(state: State, side: Side, a: Action, c: Context) -> float:
  target = state.countries[a.target_country]
  ops = effective_ops_for_action(state, side, a)

  expected_swing = estimate_expected_coup_swing(state, side, a.target_country, ops)
  local_value = country_local_value(state, side, a.target_country, c)

  s = 0
  s += 8 * expected_swing
  s += 5 * local_value
  s += Weights.MILOPS_PROGRESS * estimate_milops_gain_from_coup(state, side, a)

  # isolated BGs can effectively unlock more BG value than the raw target
  s += 4 * expected_followup_access_bonus_from_coup(state, side, a.target_country)

  # opening Italy correction
  if side == USSR and state.turn == 1 and a.target_country == "Italy":
    if italy_coup_success_prob(state, side, ops) >= (2.0 / 3.0):
      s += 30
    else:
      s -= 25

  # early Iran correction
  if side == USSR and state.turn == 1 and a.target_country == "Iran" and not hand_has_de_cards(state.hand[USSR]):
    s -= 20

  # vanity coups into 2-stability non-BGs are usually inefficient
  if not target.battleground and target.stability == 2:
    s += Weights.VANITY_COUP

  # battleground coups cost DEFCON mobility
  if target.battleground:
    s += Weights.DEFCON_MOBILITY_LOSS * estimate_defcon_mobility_loss_from_bg_coup(state, side, a)

  # risk shaping
  if c.risk == CONSERVE:
    s -= estimate_line_variance(state, side, a) * 5
  elif c.risk == GAMBLE:
    s += estimate_line_variance(state, side, a) * 2

  # offside event cost if using opponent card for Ops
  s += Weights.LIVE_OFFSIDE_EVENT_COST * event_cost_if_ops_triggers_opponent_event(state, side, a, c)

  return s


function score_realign_action(state: State, side: Side, a: Action, c: Context) -> float:
  target = a.target_country
  edge = compute_realign_modifier_edge(state, side, target)
  local = country_local_value(state, side, target, c)

  s = 0
  s += 8 * edge
  s += 4 * local

  # Africa / South America are naturally more realignment-centric
  if target_country_is_in_regions(state, target, [AFRICA, SOUTH_AMERICA]):
    s += 6

  # last-turn miracles live here
  if c.risk == GAMBLE:
    s += Weights.GAMBLE_REALIGN_BONUS
  else:
    if edge <= 0:
      s += Weights.LOW_EDGE_REALIGN

  # realignment does not solve MilOps shortage
  if milops_shortage_is_urgent(state, side):
    s -= 6

  # offside event cost if using opponent card for Ops
  s += Weights.LIVE_OFFSIDE_EVENT_COST * event_cost_if_ops_triggers_opponent_event(state, side, a, c)

  return s


function top_coup_targets(state: State, side: Side, card: Card, c: Context, limit: int, asia_only: bool = false) -> list[CountryName]:
  tmp = []
  ops = effective_ops_for_card_in_mode(state, side, card, "COUP", asia_only)

  for country in state.countries.values():
    if asia_only and not country_in_asia_or_seasia(country):
      continue
    if not can_coup_country(state, side, country.name):
      continue

    a = Action(type = PLAY_OPS_COUP, card = card, target_country = country.name)
    score = score_coup_action(state, side, a, c)
    tmp.append((country.name, score))

  tmp.sort(desc by second)
  return [name for (name, score) in take_first(tmp, limit)]


function top_realign_targets(state: State, side: Side, card: Card, c: Context, limit: int, asia_only: bool = false) -> list[CountryName]:
  tmp = []

  for country in state.countries.values():
    if asia_only and not country_in_asia_or_seasia(country):
      continue
    if not can_realign_country(state, side, country.name):
      continue

    a = Action(type = PLAY_OPS_REALIGN, card = card, target_country = country.name)
    score = score_realign_action(state, side, a, c)
    tmp.append((country.name, score))

  tmp.sort(desc by second)
  return [name for (name, score) in take_first(tmp, limit)]


## 14. Event-order choice for opponent cards played for Ops

function choose_event_timing_if_needed(state: State, side: Side, card: Card, payload) -> EventTiming:
  if event_owner_for_card(card) != other(side):
    return NONE

  before_cost = estimate_event_order_cost(state, side, card, payload, BEFORE_OPS)
  after_cost  = estimate_event_order_cost(state, side, card, payload, AFTER_OPS)

  if before_cost <= after_cost:
    return BEFORE_OPS
  return AFTER_OPS


function event_cost_if_ops_triggers_opponent_event(state: State, side: Side, a: Action, c: Context) -> float:
  if a.card == null:
    return 0
  if event_owner_for_card(a.card) != other(side):
    return 0
  return estimate_event_order_cost(state, side, a.card, a, a.event_timing)


## 15. Card policy hooks

function card_policy_bonus(state: State, side: Side, card: Card, mode: string, c: Context) -> float:
  if card.name not in CARD_POLICY:
    return 0

  p = CARD_POLICY[card.name]
  s = 0

  if mode == "event":
    s += p.get("event_bias", 0)

    if side == USSR and c.stage == EARLY:
      s += p.get("event_bias_ussr_early", 0)

    if side == US and state.turn == 1:
      s += p.get("event_bias_us_t1", 0)

    # situational US/Japan / NATO style hooks
    if card.name == "US/Japan Mutual Defense Pact":
      if missile_envy_pressure_is_high(state):
        s += 8
      if japan_security_is_important(state, side):
        s += 8

    if card.name == "NORAD":
      if can_realistically_activate_norad_with_low_opportunity_cost(state, side):
        s += 12
      else:
        s -= 20

    if card.name == "Voice of America":
      s += 12 * best_access_denial_value_for_voa(state, side)

    if card.name == "OAS Founded":
      if open_america_bgs_remain(state):
        s -= 15

    if card.name == "ABM Treaty" and side == USSR and abm_break_plus_followup_exists(state, side):
      s += 18

    if card.name == "Five Year Plan":
      if five_year_plan_can_discard_bad_scoring_or_bad_lowop(state, side):
        s += 20

    return s

  if mode == "space":
    s += p.get("space_bias", 0)

    if side == USSR:
      s += p.get("space_bias_ussr", 0)

    if side == US and state.turn == 1:
      s += p.get("space_bias_us_t1", 0)

    if c.stage != EARLY:
      s += p.get("space_bias_later", 0)

    if event_owner_for_card(card) == other(side):
      s += p.get("space_bias_offside", 0)

    return s

  if mode == "headline":
    s += p.get("headline_bias_us_t1", 0)
    if side == USSR:
      s += p.get("headline_bias_ussr_when_break_plus_followup", 0)
    s += p.get("headline_bias_situational", 0)
    return s

  return 0


## 16. Low-level estimators (stubs / interfaces)

# These are intentionally abstract. In a real engine, plug them into exact board logic.
# The rollout policy depends on them being fast and reasonably correlated with true value.

function rough_global_eval(state: State, side: Side) -> float
function position_is_stable(state: State, side: Side) -> bool
function side_is_trailing(state: State, side: Side) -> bool
function engine_is_legal(state: State, side: Side, action: Action) -> bool
function other(side: Side) -> Side
function can_play_event(state: State, side: Side, card: Card) -> bool
function can_space_card(state: State, side: Side, card: Card) -> bool
function can_coup_country(state: State, side: Side, country_name: CountryName) -> bool
function can_realign_country(state: State, side: Side, country_name: CountryName) -> bool
function count_remaining_actions_for_side_this_turn(state: State, side: Side) -> int
function compute_latest_safe_scoring_slots(state: State, side: Side, n_scoring: int) -> list[int]
function current_side_action_slot(state: State, side: Side) -> int
function count_controlled_bgs_in_region(state: State, side: Side, region: Region) -> int
function estimate_scoring_points(state: State, side: Side, region: Region) -> int
function estimate_best_one_card_repair_value(state: State, side: Side, region: Region) -> float
function estimate_best_two_card_repair_value(state: State, side: Side, region: Region) -> float
function estimate_opponent_repair_risk_before_next_safe_slot(state: State, side: Side, region: Region) -> float
function estimate_opponent_repair_risk_if_not_headlined(state: State, side: Side, region: Region) -> float
function estimate_event_value(state: State, side: Side, card: Card, c: Context) -> float
function estimate_offside_event_cost(state: State, side: Side, card: Card, c: Context) -> float
function estimate_event_region_effect(state: State, side: Side, card: Card, region: Region) -> float
function estimate_headline_region_effect(state: State, side: Side, card: Card, region: Region) -> float
function action_causes_immediate_self_loss_via_defcon(state: State, side: Side, action: Action) -> bool
function event_owner_for_card(card: Card) -> Side | NEUTRAL
function effective_ops_for_card_in_mode(state: State, side: Side, card: Card, mode: string, asia_only: bool) -> int
function effective_ops_for_action(state: State, side: Side, action: Action) -> int
function legal_influence_targets(state: State, side: Side, asia_only: bool) -> list[CountryName]
function placement_sequence_cost_to_add_n(state: State, side: Side, country_name: CountryName, n: int) -> int
function apply_n_influence_sequence_aware(state: State, side: Side, country_name: CountryName, n: int) -> void
function placements_needed_to_break_control(state: State, side: Side, country_name: CountryName) -> int
function placements_needed_to_take_control(state: State, side: Side, country_name: CountryName) -> int
function estimate_expected_coup_swing(state: State, side: Side, country_name: CountryName, ops: int) -> float
function estimate_milops_gain_from_coup(state: State, side: Side, action: Action) -> float
function estimate_defcon_mobility_loss_from_bg_coup(state: State, side: Side, action: Action) -> float
function compute_realign_modifier_edge(state: State, side: Side, country_name: CountryName) -> float
function estimate_line_variance(state: State, side: Side, action: Action) -> float
function cheap_apply_action_for_eval(state: State, side: Side, action: Action) -> State
function is_china_action(action: Action) -> bool
function action_targets_non_asia_regions(action: Action) -> bool
function action_is_all_asia_or_seasia(action: Action) -> bool
function country_in_asia_or_seasia(country: Country) -> bool
function target_country_is_in_regions(state: State, country_name: CountryName, regions: list[Region]) -> bool
function count_dangling_control_breaks(state: State, side: Side, action: Action) -> int
function count_useless_nonbg_placements(state: State, side: Side, action: Action, c: Context) -> int
function estimate_wasted_ops(state: State, side: Side, action: Action) -> float
function cheap_country_eval_context(state: State, side: Side, country_name: CountryName)
function biggest_scoring_region_safety_delta(before, after) -> float
function biggest_opponent_scoring_damage_delta(before, after) -> float
function immediate_scoring_or_domination_need(next_state: State, side: Side, country_name: CountryName) -> bool
function asia_extra_nonbg_is_not_needed(next_state: State, side: Side, country_name: CountryName) -> bool
function any_non_seasia_region(regions: set[Region]) -> Region
function looming_enemy_event_fear_penalty(state: State, side: Side, country_name: CountryName) -> float
function europe_scoring_is_live_or_dangerous(state: State) -> bool
function would_side_control_europe(state: State, side: Side) -> bool
function would_this_country_be_nth_europe_bg(state: State, side: Side, country_name: CountryName, n: int) -> bool
function would_this_country_enable_europe_control(state: State, side: Side, country_name: CountryName) -> bool
function asia_is_acceptable_at_parity(state: State, side: Side) -> bool
function southeast_asia_scoring_still_live(state: State) -> bool
function asia_country_count_is_close(state: State) -> bool
function is_late_turn_slot(state: State, side: Side) -> bool
function region_is_badly_lost(state: State, side: Side, region: Region) -> bool
function panama_is_exposed(state: State) -> bool
function hand_contains_any(hand: list[Card], names: list[string]) -> bool
function contains(hand: list[Card], name: string) -> bool
function get_card(hand: list[Card], name: string) -> Card
function generic_best_headline_card(hand: list[Card], side: Side) -> Card
function containment_is_5plus_or_blockade_protection(hand_or_state) -> bool
function should_consider_empty_wg_exception(hand: list[Card]) -> bool
function base_standard_us_setup() -> map[CountryName, int]
function standard_4_4_2() -> map[CountryName, int]
function standard_4_3_3() -> map[CountryName, int]
function special_1_wg_3_fr_blockade_setup() -> map[CountryName, int]
function base_standard_ussr_setup() -> map[CountryName, int]
function fallback_legal_action(state: State, side: Side) -> Action
function dedupe_actions(actions: list[Action]) -> list[Action]
function dedupe(list_like) -> same_type
function compress_same_country(placements) -> list[(CountryName, count)]
function scripted_plan_if_affordable(state: State, side: Side, card: Card, items: list[(CountryName, count)]) -> InfluencePlan | null
function required_to_reach_influence(state: State, side: Side, country_name: CountryName, target: int) -> int
function best_non_space_score(candidates, state, side, c) -> float
function scoring_now_causes_immediate_loss(state: State, side: Side, region: Region) -> bool
function is_last_or_near_last_action_for_side(state: State, side: Side) -> bool
function force_endgame_gamble(state, side, candidates, c) -> Action | null
function force_space_bad_card_when_superior(state, side, candidates, c) -> Action | null
function immediate_space_vp_gain_if_success(state: State, side: Side) -> float
function ability_value_if_reach_next_space_first(state: State, side: Side) -> float
function choose_bad_offside_card_to_space(state: State, side: Side, c: Context) -> Card | null
function event_can_be_burned_cheaply_now(state: State, side: Side, card: Card) -> bool
function event_is_high_variance_or_hand_attack(card: Card) -> bool
function entering_midwar_with_fragile_space_lead(state: State, side: Side) -> bool
function is_enemy_war_card_for_side(card: Card, side: Side) -> bool
function korean_war_is_safe_to_burn(state: State, side: Side) -> bool
function missile_envy_pressure_is_high(state: State) -> bool
function japan_security_is_important(state: State, side: Side) -> bool
function can_realistically_activate_norad_with_low_opportunity_cost(state: State, side: Side) -> bool
function best_access_denial_value_for_voa(state: State, side: Side) -> float
function open_america_bgs_remain(state: State) -> bool
function abm_break_plus_followup_exists(state: State, side: Side) -> bool
function five_year_plan_can_discard_bad_scoring_or_bad_lowop(state: State, side: Side) -> bool
function strong_4op_us_event(card: Card) -> bool
function already_have_strong_4op_us_event_to_pair(hand: list[Card]) -> bool
function hand_has_de_cards(hand: list[Card]) -> bool
function italy_coup_success_prob(state: State, side: Side, ops: int) -> float
function expected_followup_access_bonus_from_coup(state: State, side: Side, country_name: CountryName) -> float
function action_is_purely_zero_value_and_dominated(state: State, side: Side, action: Action) -> bool
function current_side_action_slot(state: State, side: Side) -> int
function count_remaining_actions_for_side_this_turn(state: State, side: Side) -> int
function count_remaining_actions_for_side_this_turn(state: State, side: Side) -> int
function exact_seasia_score(state: State, side: Side) -> int
function softmax_sample_top_k(scored_actions: list[(Action, float)], k: int, temperature: float) -> Action
function argmax(items, key_fn)
function take_first(items, n)


## 17. Rollout loop

function rollout_policy_playout(state: State) -> TerminalResult:
  working = clone(state)

  while not is_terminal(working):
    side = working.side_to_move
    action = choose_rollout_action(working, side)
    working = engine_apply_action(working, side, action)

  return terminal_result(working)


## 18. Practical summary of what this version fixes

# 1) Europe / France / Italy:
#    The previous policy was too generic. This one treats Europe as exceptional and values
#    France/Italy through score geometry, not just influence arithmetic.

# 2) Non-BG policy:
#    The previous policy was still too willing to spend on random fillers.
#    This version only likes non-BGs for access, domination, volatility shields, or SE Asia value.

# 3) Asia:
#    The previous policy would overchase Asia country-count clutter.
#    This version is comfortable with parity and punishes extra low-value non-BG Asia investment.

# 4) Space:
#    The previous policy still treated space too much like a trash can.
#    This version races for VP + abilities and spaces early more often.

# 5) Control-breaking bug:
#    The previous greedy single-placement logic could break control and wander off.
#    This version uses bundle search so it can finish captures and avoid dangling breaks.

# 6) Timing of scoring:
#    The previous forced-scoring logic was too eager.
#    This version schedules scoring to latest safe slots unless immediate cash-in is superior.

# 7) Risk profile:
#    The previous policy was too uniform.
#    This version changes variance appetite depending on whether the side is ahead or behind.

# 8) Opening behavior:
#    This version adds strong T1 hooks for US spreading and USSR Italy logic, which matters a lot
#    because rollout error in the first turn propagates through the whole game.