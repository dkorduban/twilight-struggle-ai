# Twilight Struggle minimal hybrid rollout policy
#
# Purpose:
# - combine the safest, current-engine-compatible parts of `classic.md` and `sankt.md`
# - stay within today's `Policy(pub, hand, holds_china) -> ActionEncoding | None` API
# - produce a small, deterministic rollout heuristic that ranks legal `ActionEncoding` values
#
# This file is intentionally narrower than the larger policy specs.
# It is the implementation target for the current engine, not a replacement for the
# broader long-form strategy notes.


## 0. Current-engine contract

function choose_minimal_hybrid(pub: PublicState, hand: frozenset[int], holds_china: bool) -> ActionEncoding | None:
  side = pub.phasing
  actions = enumerate_actions(hand, pub, side, holds_china = holds_china)
  if actions is empty:
    return null

  scored = []
  for action in actions:
    s = score_action(pub, hand, side, action)
    if pub.ar == 0:
      s += headline_adjustment(pub, side, action)
    scored.append((action, s))

  return deterministic_argmax(scored)


## 1. Explicit scope

# This policy may use:
# - `PublicState`
# - the actor's own hand
# - China ownership / face-up state via `holds_china` and `pub`
# - canonical card / country data from `tsrl.etl.game_data`
# - legal candidates from `tsrl.engine.legal_actions`
#
# This policy may NOT assume:
# - setup actions
# - custom headline action types
# - richer action structs than `ActionEncoding`
# - `event_timing`
# - determinized hidden information
# - direct `GameState` mutation
#
# Headline phase is handled by the same API. If `pub.ar == 0`, just score the
# legal `ActionEncoding` candidates as headline plays and return the best one.


## 1a. Small helpers

function other(side: Side) -> Side:
  if side == USSR: return US
  return USSR


function influence(pub: PublicState, side: Side, country_id: int) -> int:
  return pub.influence.get((side, country_id), 0)


function country_is_asia_or_sea(country_id: int) -> bool:
  region = countries[country_id].region
  return region in {ASIA, SOUTHEAST_ASIA}


## 2. Core philosophy

# Hybrid of the two larger docs:
# - default to Ops over non-scoring events
# - value battlegrounds and access more than raw influence count
# - weight Asia / Thailand more in Early War
# - weight Africa / South America more in Mid War
# - treat Europe as an emergency region, not a routine sink
# - use Space for decent offside disposal and real VP race situations
# - use Realignment sparingly
# - conserve China early unless it materially improves an Asia plan


## 3. Stage and region weights

function stage_for_turn(turn: int) -> Stage:
  if turn <= 3: return EARLY
  if turn <= 7: return MID
  return LATE


function region_weight(stage: Stage, region: Region) -> float:
  if stage == EARLY:
    table = {
      EUROPE: 0.85,
      ASIA: 1.35,
      MIDDLE_EAST: 1.10,
      CENTRAL_AMERICA: 0.60,
      SOUTH_AMERICA: 0.55,
      AFRICA: 0.65,
      SOUTHEAST_ASIA: 1.25,
    }
  else if stage == MID:
    table = {
      EUROPE: 0.95,
      ASIA: 1.00,
      MIDDLE_EAST: 1.00,
      CENTRAL_AMERICA: 0.95,
      SOUTH_AMERICA: 1.20,
      AFRICA: 1.20,
      SOUTHEAST_ASIA: 0.90,
    }
  else:
    table = {
      EUROPE: 1.10,
      ASIA: 0.95,
      MIDDLE_EAST: 0.95,
      CENTRAL_AMERICA: 1.05,
      SOUTH_AMERICA: 1.10,
      AFRICA: 1.00,
      SOUTHEAST_ASIA: 0.75,
    }
  return table[region]


## 4. Country-value heuristic

function country_value(pub: PublicState, side: Side, country_id: int) -> float:
  stage = stage_for_turn(pub.turn)
  c = countries[country_id]

  score = 0.0

  # Region posture.
  score += 5.0 * region_weight(stage, c.region)

  # Battlegrounds matter more than fillers.
  if c.is_battleground:
    score += 7.0
  else:
    score += 1.0

  # Stable countries persist longer.
  score += 0.6 * min(c.stability, 4)

  # Current-engine special hooks kept intentionally small.
  if c.name == "Thailand" and stage == EARLY:
    score += 6.0
  if c.name in {"France", "Italy", "West Germany", "East Germany"}:
    score += 2.0
  if c.name in {"Angola", "South Africa", "Panama", "Mexico", "Chile", "Argentina"} and stage == MID:
    score += 2.0

  return score


## 5. Card-value heuristic

function card_bias(side: Side, card: CardSpec, mode: ActionMode, pub: PublicState, action: ActionEncoding) -> float:
  score = 0.0

  if card.is_scoring and mode == EVENT:
    return 10000.0

  if mode == EVENT:
    # Current engine does not yet justify aggressive event-first play.
    if card.side == side or card.side == Side.NEUTRAL:
      score += 1.0
    else:
      score -= 3.0

  if mode == SPACE:
    # Space is a real race, but still mostly a disposal / tempo tool here.
    if card.side != side and not card.is_scoring:
      score += 5.0
    if pub.space[side] < pub.space[other(side)]:
      score += 2.5
    if card.ops >= 4:
      score += 1.0

  if card.card_id == 6:
    has_asia_target = any(country_is_asia_or_sea(t) for t in action.targets)
    if pub.turn <= 3 and not has_asia_target:
      score -= 4.0
    if has_asia_target:
      score += 5.0

  return score


## 6. Action scoring

function score_action(pub: PublicState, hand: frozenset[int], side: Side, action: ActionEncoding) -> float:
  card = cards[action.card_id]
  mode = action.mode
  score = 0.0

  # Mode priors.
  if mode == INFLUENCE: score += 6.0
  if mode == COUP:      score += 4.0
  if mode == REALIGN:   score += 0.0
  if mode == SPACE:     score += 1.0
  if mode == EVENT:     score += 0.0

  score += card_bias(side, card, mode, pub, action)

  if mode == INFLUENCE:
    score += score_influence(pub, side, action.targets)
  else if mode == COUP:
    score += score_coup(pub, side, action.targets[0], card.ops)
  else if mode == REALIGN:
    score += score_realign(pub, side, action.targets)
  else if mode == SPACE:
    score += score_space(pub, side, card)
  else if mode == EVENT:
    score += score_event(pub, side, card)

  # Mild preference for using lower-op cards when action quality is otherwise close.
  score -= 0.15 * card.ops

  return score


function score_influence(pub: PublicState, side: Side, targets: tuple[int, ...]) -> float:
  score = 0.0
  seen = default_map(0)

  for cid in targets:
    seen[cid] += 1
    base = country_value(pub, side, cid)

    # Diminishing returns on stacking the same target.
    score += base / seen[cid]

    opp = influence(pub, other(side), cid)
    own = influence(pub, side, cid)
    stability = countries[cid].stability

    # Reward breaking or taking control.
    if own < opp + stability and own + seen[cid] >= opp + stability:
      score += 5.0

    # Small access bonus.
    if own == 0:
      score += 1.5

  return score


function score_coup(pub: PublicState, side: Side, country_id: int, ops: int) -> float:
  c = countries[country_id]
  score = country_value(pub, side, country_id)

  # MilOps catch-up matters in a rollout.
  needed_milops = max(0, pub.turn - pub.milops[side])
  score += min(needed_milops, ops)

  if c.is_battleground:
    score += 2.5
    if pub.defcon == 2:
      score -= 8.0
    else if pub.defcon == 3:
      score -= 2.5

  return score


function score_realign(pub: PublicState, side: Side, targets: tuple[int, ...]) -> float:
  score = -4.0
  for cid in targets:
    score += 0.55 * country_value(pub, side, cid)

  # Realign is a niche tool in this minimal policy.
  if pub.defcon == 2:
    score += 2.0

  return score


function score_space(pub: PublicState, side: Side, card: CardSpec) -> float:
  score = 0.0

  if pub.space[side] < pub.space[other(side)]:
    score += 2.0
  if pub.turn <= 3:
    score += 1.0
  if card.side != side and not card.is_scoring:
    score += 2.0

  return score


function score_event(pub: PublicState, side: Side, card: CardSpec) -> float:
  if card.is_scoring:
    return 10000.0

  # Minimal current-engine stance: non-scoring events are playable but not default.
  if card.side == side or card.side == Side.NEUTRAL:
    return 1.5
  return -3.0


## 7. Headline handling

# Headline uses the same legal candidate set and the same return type.
# Add only two small adjustments:
# - modest bonus to high-ops cards
# - modest bonus to same-side / neutral events

function headline_adjustment(pub: PublicState, side: Side, action: ActionEncoding) -> float:
  card = cards[action.card_id]
  score = 0.75 * card.ops
  if action.mode == EVENT and (card.side == side or card.side == Side.NEUTRAL):
    score += 2.0
  return score


## 8. Tie-break and determinism

function deterministic_argmax(scored: list[(ActionEncoding, float)]) -> ActionEncoding:
  # Sort by:
  # 1. higher score
  # 2. lower ActionMode enum value except keep scoring EVENT first
  # 3. lower card_id
  # 4. lexicographic targets
  #
  # This keeps rollouts reproducible under fixed seeds.
  return stable_best(scored)


## 9. Intended implementation notes

# Recommended implementation shape:
# - one Python module for the policy
# - helper functions for stage, region weights, and per-mode scoring
# - country/card lookups cached via `load_cards()` / `load_countries()`
# - candidate generation delegated to `enumerate_actions(...)`
#
# Recommended tests:
# - returns `None` on empty legal set
# - always returns a legal `ActionEncoding`
# - deterministic for fixed `(pub, hand, holds_china)`
# - prefers a scoring play over non-scoring alternatives when a scoring card is present
# - values Thailand / Asia influence above low-value fillers in Early War
# - conserves China early unless the chosen action is Asia-focused
