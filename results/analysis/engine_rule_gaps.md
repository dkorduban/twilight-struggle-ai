# C++ Engine Rule Gaps Analysis
Date: 2026-04-13

## Executive Summary
46 gaps found across 5 categories. The highest-impact problems are systemic rather than isolated: opponent cards played for ops are hardcoded to resolve in the wrong order, opponent cards played to Space still fire their events, the legal ops surface is heavily simplified, Cuban Missile Crisis is reduced to a permanent no-coup lock, and several war cards are modeled as coups instead of their own war mechanic.

## Gap Inventory

### Category: Headline Phase
- **[DONE]** **GAP-001**: China Card can be selected illegally as a headline in the generic/random path
  - Fix: 76f974a (block China Card headlines in the generic/random headline path)
  - Rule: The China Card cannot be played during the Headline Phase.
  - Engine: `run_headline_phase()` asks a general policy for any legal card, then force-converts the result to `ActionMode::Event`; only the heuristic `headline_actions()` path filters out the China Card, so the exploration/random path can still headline it.
  - File: `cpp/tscore/game_loop.cpp:80`, `cpp/tscore/game_loop.cpp:806`, `cpp/tscore/policies.cpp:604`
  - Impact: Medium — illegal headlines distort opening play and training traces.

### Category: Operations Phase
- **[PARTIAL]** **GAP-002**: Opponent cards played for ops always fire before the ops
  - Fix: 37bdd01 (ordering mode head), 6b8a6cc (rename to EventFirst / ops-first default); two-step deferred-ops flow is still incomplete
  - Rule: When the phasing player uses an opponent event card for ops, the phasing player chooses whether the opponent event resolves before or after the ops.
  - Engine: `apply_action_with_hands()` always fires the opponent event before resolving any non-event action.
  - File: `cpp/tscore/game_loop.cpp:718`
  - Impact: High — this changes core tactical sequencing on a large fraction of turns.

- **[DONE]** **GAP-003**: Spacing an opponent card incorrectly fires the opponent event
  - Fix: 953c783 (skip opponent events on Space Race plays)
  - Rule: Sending an opponent card to the Space Race avoids that opponent event entirely.
  - Engine: The same `apply_action_with_hands()` pre-hook fires the opponent event for `ActionMode::Space`, then performs the space attempt anyway.
  - File: `cpp/tscore/game_loop.cpp:718`
  - Impact: High — Space Race becomes unusable as the normal safety valve for enemy events.

- **[DONE]** **GAP-004**: Space Race legality ignores minimum ops requirements
  - Fix: 237e4d2 (enforce per-level Space Race ops minimums)
  - Rule: Space attempts require minimum ops values that rise as the space track advances.
  - Engine: `legal_modes()` checks attempt counts and current level but never uses `kSpaceOpsMinimum`, so any ops-valued card can be spaced at any level.
  - File: `cpp/tscore/legal_actions.cpp:24`, `cpp/tscore/legal_actions.cpp:155`
  - Impact: High — many illegal space actions are offered and can be chosen.

- **[DONE]** **GAP-005**: Normal ops placement is simplified away from real TS placement rules
  - Fix: d0e328c (1-hop adjacency / correct access scope), 4326635 (2-ops enemy-control surcharge)
  - Rule: Influence placement is limited to countries adjacent to existing influence/home superpower, and placing into enemy-controlled countries costs 2 ops per point.
  - Engine: `accessible_countries()` does a full BFS through the map from any friendly influence, effectively opening whole connected regions, and `apply_action()` just adds `+1` influence per target with no enemy-control surcharge.
  - File: `cpp/tscore/adjacency.cpp:65`, `cpp/tscore/step.cpp:1138`
  - Impact: High — the legal action set and the value of ops are both substantially wrong.

- **[PARTIAL]** **GAP-006**: Free borrowed/stolen ops are randomized instead of chosen, and their realignments are simplified
  - Fix: c949202 (PolicyCallback choice plumbing), 173d471 (route free-op targets through choose_country); helper still uses simplified coup/realign handling
  - Rule: When a card grants ops (UN Intervention, Missile Envy, Grain Sales, etc.), the acting player chooses mode, targets, and full realignment consequences.
  - Engine: `apply_ops_randomly()` randomly picks influence/coup/realign, randomly picks targets, omits home-superpower adjacency in realignment, and only removes 1 influence regardless of realignment margin.
  - File: `cpp/tscore/game_loop.cpp:174`
  - Impact: High — multiple card events lose strategic choice entirely.

### Category: Card Events
- **[DONE]** **GAP-007**: Card 7 (Socialist Governments) — Western Europe targets are randomized
  - Fix: 49caca4 (replace random Socialist Governments targeting with choose_country)
  - Rule: USSR chooses up to 3 eligible Western European countries.
  - Engine: The event samples up to 3 eligible countries at random.
  - File: `cpp/tscore/step.cpp:268`
  - Impact: Medium — early-war Europe pressure is misplayed.

- **[DONE]** **GAP-008**: Card 11 (Korean War) — modeled as a coup instead of a war
  - Fix: 442643b (implement war-card resolution for Korean War / related war events)
  - Rule: Korean War uses the war-card success mechanic, not the normal coup table.
  - Engine: The event calls `apply_free_coup()` on South Korea.
  - File: `cpp/tscore/step.cpp:286`
  - Impact: High — war odds, outcome, and board swing are wrong.

- **[DONE]** **GAP-009**: Card 13 (Arab-Israeli War) — modeled as a coup instead of a war
  - Fix: 442643b (implement war-card resolution for Arab-Israeli War / related war events)
  - Rule: Arab-Israeli War uses the war-card success mechanic, not the normal coup table.
  - Engine: The event calls `apply_free_coup()` on Israel.
  - File: `cpp/tscore/step.cpp:301`
  - Impact: High — war odds and resulting state changes are wrong.

- **[DONE]** **GAP-010**: Card 16 (Warsaw Pact Formed) — branch-internal country choices are randomized
  - Fix: 49caca4 (replace Warsaw Pact branch targeting with choose_option / choose_country)
  - Rule: USSR chooses which 4 Eastern European countries lose all US influence, or how to distribute 5 USSR influence across Eastern Europe.
  - Engine: The branch choice exists, but country selection/allocation is sampled randomly and the add-influence branch forces one point into 5 distinct countries.
  - File: `cpp/tscore/step.cpp:329`
  - Impact: High — a major opener loses its key strategic choice.

- **[DONE]** **GAP-011**: Card 19 (Truman Doctrine) — target country is randomized
  - Fix: 49caca4 (replace Truman Doctrine random target with choose_country)
  - Rule: US chooses one uncontrolled European country from which to remove all USSR influence.
  - Engine: The event samples one eligible country uniformly at random.
  - File: `cpp/tscore/step.cpp:416`
  - Impact: Medium — this often hits the wrong country in Europe.

- **[DONE]** **GAP-012**: Card 20 (Olympic Games) — boycott placements are randomized
  - Fix: 49caca4 (replace Olympic Games boycott placement sampling with choose_country)
  - Rule: If the non-phasing player boycotts, the phasing player chooses how to spend the 4 influence placements.
  - Engine: The compete/boycott choice exists, but the 4 influence placements are assigned randomly among accessible countries.
  - File: `cpp/tscore/step.cpp:350`
  - Impact: Medium — the swing from boycott is often misallocated.

- **[DONE]** **GAP-013**: Card 23 (Marshall Plan) — target countries are randomized
  - Fix: 49caca4 (replace Marshall Plan random targets with choose_country)
  - Rule: US chooses up to 7 non-USSR-controlled Western European countries.
  - Engine: The event samples 7 eligible countries uniformly at random.
  - File: `cpp/tscore/step.cpp:383`
  - Impact: High — one of the most important opening events loses its main decision.

- **[DONE]** **GAP-014**: Card 24 (Indo-Pakistani War) — modeled as a coup instead of a war
  - Fix: 442643b (implement war-card resolution for Indo-Pakistani War / related war events)
  - Rule: The phasing player chooses India or Pakistan, then resolves the war-card success mechanic.
  - Engine: The target choice is exposed, but the resolution uses `apply_free_coup()`.
  - File: `cpp/tscore/step.cpp:397`
  - Impact: High — war odds and resulting influence swing are wrong.

- **[DONE]** **GAP-015**: Card 28 (Suez Crisis) — the two countries hit are randomized
  - Fix: 49caca4 (replace Suez Crisis random removals with choose_country)
  - Rule: USSR chooses which 2 of France, UK, and Israel lose 2 US influence.
  - Engine: The event samples 2 of the 3 countries at random.
  - File: `cpp/tscore/step.cpp:445`
  - Impact: Medium — the event often misses the most valuable targets.

- **[DONE]** **GAP-016**: Card 29 (East European Unrest) — the affected countries are randomized
  - Fix: 49caca4 (replace East European Unrest random targets with choose_country)
  - Rule: US chooses 3 Eastern European countries to lose USSR influence.
  - Engine: The event samples 3 Eastern European countries at random.
  - File: `cpp/tscore/step.cpp:451`
  - Impact: Medium — the event cannot be aimed where it matters.

- **[DONE]** **GAP-017**: Card 30 (Decolonization) — placements are randomized
  - Fix: 49caca4 (replace Decolonization random placements with choose_country)
  - Rule: USSR chooses four Africa/Southeast Asia placements.
  - Engine: The event samples four countries at random.
  - File: `cpp/tscore/step.cpp:461`
  - Impact: Medium — a major expansion event loses its targeting.

- **[PARTIAL]** **GAP-018**: Card 32 (UN Intervention) — borrowed ops are spent randomly
  - Fix: c949202 (PolicyCallback choice plumbing), 173d471 (free-op country targets via choose_country); borrowed ops still run through `apply_ops_randomly_impl()`
  - Rule: The acting player chooses how to spend the opponent card’s ops while suppressing its event.
  - Engine: After choosing the opponent card, the engine routes the ops through `apply_ops_randomly()`.
  - File: `cpp/tscore/game_loop.cpp:397`
  - Impact: High — the card no longer serves as a tactical tool.

- **[DONE]** **GAP-019**: Card 33 (De-Stalinization) — both the source and destination moves are randomized
  - Fix: 49caca4 (replace De-Stalinization random source/destination picks with choose_country)
  - Rule: USSR chooses up to 4 influence to move, including where to remove from and where to place it.
  - Engine: The event repeatedly samples random source and destination countries point-by-point.
  - File: `cpp/tscore/step.cpp:479`
  - Impact: High — the event’s core strategic purpose is lost.

- **[DONE]** **GAP-020**: Card 37 (Special Relationship) — follow-up placements are randomized
  - Fix: 49caca4 (replace Special Relationship random placements with choose_country)
  - Rule: US chooses the placement target(s) granted by the event.
  - Engine: The 2-influence NATO branch and the 1-influence non-NATO branch both place influence by random sampling.
  - File: `cpp/tscore/step.cpp:527`
  - Impact: Medium — the event often lands in low-value countries.

- **[DONE]** **GAP-021**: Card 39 (Brush War) — modeled as a coup instead of a war
  - Fix: 442643b (implement war-card resolution for Brush War / related war events)
  - Rule: Brush War uses war resolution, then applies its additional success effect.
  - Engine: It chooses a stability-1/2 target, then resolves `apply_free_coup()` and piggybacks extra US influence removal.
  - File: `cpp/tscore/step.cpp:548`
  - Impact: High — both success odds and DEFCON interaction are wrong.

- **[OPEN]** **GAP-022**: Card 49 (How I Learned to Stop Worrying) — DEFCON 1 is not a legal choice
  - Rule: The phasing player chooses any DEFCON level allowed by the card text, including DEFCON 1 even if that is suicidal.
  - Engine: The choice set is hardcoded to DEFCON 2-5 only.
  - File: `cpp/tscore/step.cpp:605`
  - Impact: Medium — a legal player decision is removed.

- **[PARTIAL]** **GAP-023**: Card 50 (Junta) — the free action is hardcoded to coup, and both targets are randomized
  - Fix: dd4a9b5 (wire CountrySelect for event decisions); the free action is still hardcoded to coup
  - Rule: The acting player chooses the influence target, then chooses whether the free action is a coup or a realignment and where to apply it.
  - Engine: The event picks an influence target, always performs a coup, and randomizes both chosen countries.
  - File: `cpp/tscore/step.cpp:613`
  - Impact: High — a flexible event is collapsed into one random line.

- **[PARTIAL]** **GAP-024**: Card 52 (Missile Envy) — stolen ops are spent randomly
  - Fix: c949202 (PolicyCallback choice plumbing), 173d471 (free-op country targets via choose_country); stolen ops still run through `apply_ops_randomly_impl()`
  - Rule: After taking the highest-ops card, the acting player chooses how to spend its ops.
  - Engine: The stolen card is identified, but its ops go through `apply_ops_randomly()`.
  - File: `cpp/tscore/game_loop.cpp:471`
  - Impact: High — the main value of the event is lost.

- **[PARTIAL]** **GAP-025**: Card 59 (Muslim Revolution) — removals are randomized and can target zero-US countries
  - Fix: 49caca4 (replace random removals with choose_country); fallback pool can still include zero-US countries
  - Rule: USSR chooses 2 eligible countries from the allowed list that actually contain US influence.
  - Engine: If fewer than 2 countries currently contain US influence, the event repopulates the pool with all listed countries and then samples 2 at random.
  - File: `cpp/tscore/step.cpp:684`
  - Impact: Medium — the event can partially whiff even when a deterministic choice exists.

- **[DONE]** **GAP-026**: Card 67 (Puppet Governments) — the three placements are randomized
  - Fix: 49caca4 (replace Puppet Governments random placements with choose_country)
  - Rule: US chooses 3 zero-influence countries.
  - Engine: The event samples 3 zero-influence countries uniformly at random.
  - File: `cpp/tscore/step.cpp:765`
  - Impact: Medium — this frequently misses key access points.

- **[PARTIAL]** **GAP-027**: Card 68 (Grain Sales to Soviets) — stolen ops are spent randomly
  - Fix: c949202 (PolicyCallback choice plumbing), 173d471 (free-op country targets via choose_country); stolen ops still run through `apply_ops_randomly_impl()`
  - Rule: After the random Soviet card is revealed, the US player chooses how to spend its ops.
  - Engine: The stolen card itself is random, but the follow-up ops spending is routed through `apply_ops_randomly()`.
  - File: `cpp/tscore/game_loop.cpp:518`
  - Impact: High — the event no longer provides controlled tempo/value.

- **[DONE]** **GAP-028**: Card 71 (OAS Founded) — the placements are randomized
  - Fix: 49caca4 (replace OAS Founded random placements with choose_country)
  - Rule: US chooses how to distribute the 2 influence in Central/South America.
  - Engine: The event samples placement targets at random.
  - File: `cpp/tscore/step.cpp:787`
  - Impact: Medium — Latin America development becomes noisy instead of deliberate.

- **[DONE]** **GAP-029**: Card 75 (Voice of America) — removals are randomized
  - Fix: 49caca4 (replace Voice of America random removals with choose_country)
  - Rule: US chooses up to 4 non-European countries from which to remove 1 USSR influence each.
  - Engine: The event samples up to 4 eligible countries at random.
  - File: `cpp/tscore/step.cpp:820`
  - Impact: Medium — the event often removes the wrong influence points.

- **[DONE]** **GAP-030**: Card 76 (Liberation Theology) — distribution is randomized and forced into single points
  - Fix: 49caca4 (replace Liberation Theology random single-point placements with choose_country)
  - Rule: USSR chooses how to distribute 3 influence in Central America, with up to 2 in one country.
  - Engine: The event samples 3 countries and adds exactly 1 influence to each.
  - File: `cpp/tscore/step.cpp:839`
  - Impact: Medium — both targeting and legal allocation flexibility are reduced.

- **[DONE]** **GAP-031**: Card 77 (Ussuri River Skirmish) — the 4 influence placements are randomized
  - Fix: 49caca4 (replace Ussuri River Skirmish random placements with choose_country)
  - Rule: After the China Card changes hands, the benefiting side chooses how to distribute 4 influence.
  - Engine: The event assigns the 4 placements by random sampling.
  - File: `cpp/tscore/step.cpp:852`
  - Impact: Medium — the China swing is much less controllable than it should be.

- **[DONE]** **GAP-032**: Card 78 (Ask Not What Your Country Can Do For You) — discard count and cards are randomized, and the 4-card cap is missing
  - Fix: 00f9e0a (player-chosen discard count/cards with 4-card cap)
  - Rule: US may choose to discard up to 4 cards, and chooses exactly which cards to cycle.
  - Engine: The engine draws a random discard count from 0 to the full hand-sized eligible set, then randomly chooses the discarded cards.
  - File: `cpp/tscore/game_loop.cpp:539`
  - Impact: High — a major hand-shaping card loses its core decision and can exceed the legal discard limit.

- **[PARTIAL]** **GAP-033**: Card 83 (Che) — coups are randomized and the second coup is forced whenever available
  - Fix: 49caca4 (replace random Che coup targets with choose_country); second coup is still forced when available
  - Rule: USSR chooses one or two eligible coup targets, with the second in a different region.
  - Engine: The event samples the first target randomly, then always takes a second random coup if a different-region target exists.
  - File: `cpp/tscore/step.cpp:897`
  - Impact: High — this materially changes risk management at DEFCON 3 and in Latin America/Africa.

- **[DONE]** **GAP-034**: Card 84 (Our Man in Tehran) — keep/discard decisions and return order are randomized
  - Fix: 185da26 (player-chosen Our Man in Tehran keep/discard decisions)
  - Rule: US chooses which of the 5 drawn cards to discard and the order of the cards returned to the bottom of the deck.
  - Engine: The event randomizes how many cards are kept, randomizes which ones are discarded, and randomizes the order of the returned cards.
  - File: `cpp/tscore/game_loop.cpp:567`
  - Impact: Medium — this strips the event of its information-management value.

- **[DONE]** **GAP-035**: Card 90 (The Reformer) — European placement targets are randomized
  - Fix: 49caca4 (replace The Reformer random placements with choose_country)
  - Rule: USSR chooses which eligible European countries receive the influence.
  - Engine: The event samples the placement countries at random.
  - File: `cpp/tscore/step.cpp:949`
  - Impact: Medium — a late-war positional event becomes noisy.

- **[DONE]** **GAP-036**: Card 91 (Marine Barracks Bombing) — the follow-up removals are randomized
  - Fix: 49caca4 (replace Marine Barracks Bombing random removals with choose_country)
  - Rule: USSR chooses the additional Middle East countries from which 1 US influence is removed.
  - Engine: The event samples up to 2 eligible countries at random.
  - File: `cpp/tscore/step.cpp:967`
  - Impact: Medium — the event often misses the best US-held targets.

- **[DONE]** **GAP-037**: Card 98 (Latin American Debt Crisis) — the US discard pair is hardcoded instead of chosen
  - Fix: aaa020f (player-chosen Latin American Debt Crisis discard pair)
  - Rule: The US player chooses whether and how to pay the 2-card, 4+ ops discard cost.
  - Engine: The event automatically discards the cheapest qualifying pair; if no pair exists it immediately gives USSR 2 VP.
  - File: `cpp/tscore/game_loop.cpp:628`
  - Impact: Medium — the defending player loses an important hand-management choice.

- **[DONE]** **GAP-038**: Card 105 (Iran-Iraq War) — target is randomized and the event is modeled as a coup
  - Fix: 442643b (implement war-card resolution for Iran-Iraq War / related war events)
  - Rule: The phasing player chooses Iran or Iraq, then resolves the war-card success mechanic.
  - Engine: The target is randomly sampled and resolved through `apply_free_coup()`.
  - File: `cpp/tscore/step.cpp:1090`
  - Impact: High — target selection, odds, and DEFCON interaction are all wrong.

### Category: Special / Persistent Mechanics
- **[DONE]** **GAP-039**: Card 9 (Vietnam Revolts) — the Southeast-Asia-only ops bonus is implemented as a global ops modifier
  - Fix: ae00688 (scope Vietnam Revolts bonus to SEA-only ops usage)
  - Rule: The extra ops apply only when USSR spends the entire card in Southeast Asia.
  - Engine: The event increments `ops_modifier[USSR]`, which boosts all USSR card ops for the turn regardless of region or usage.
  - File: `cpp/tscore/step.cpp:255`
  - Impact: High — the card materially over-buffs USSR operations.

- **[DONE]** **GAP-040**: Card 35 (Formosan Resolution) — Taiwan is treated as a battleground even when the US does not control it
  - Fix: 2d61c3e (require US control for Formosan Taiwan battleground status)
  - Rule: Taiwan counts as a battleground for Asia scoring only while the US controls Taiwan.
  - Engine: `is_scoring_battleground()` checks only `pub.formosan_active`, not US control of Taiwan.
  - File: `cpp/tscore/scoring.cpp:32`
  - Impact: Medium — Asia scoring can be wrong in contested Taiwan positions.

- **[PARTIAL]** **GAP-041**: Card 43 (Cuban Missile Crisis) — the effect becomes a permanent no-coup lock with no cancellation path
  - Fix: 5c2e573 (restore turn-end cleanup and battleground-coup suicide path); explicit cancellation path is still missing
  - Rule: The effect lasts only until turn end or explicit cancellation, and battleground coups remain possible but suicidal unless the cancelling influence-removal option is taken.
  - Engine: The event sets `cuban_missile_crisis_active`; `legal_modes()` then deletes all coup actions outright, and the flag is never cleared in turn cleanup or by influence play.
  - File: `cpp/tscore/step.cpp:578`, `cpp/tscore/legal_actions.cpp:179`
  - Impact: High — this radically changes DEFCON play and permanently removes an action class.

- **[DONE]** **GAP-042**: Card 93 (Glasnost) — the SALT follow-up is upgraded to a full extra action round
  - Fix: 59fed5a (replace extra action round with pending Glasnost free ops)
  - Rule: With SALT active, Glasnost grants a limited extra operations effect, not a normal card play from hand.
  - Engine: The event sets `glasnost_extra_ar`, and the game loop resolves that as a full extra USSR action round using a normal hand card.
  - File: `cpp/tscore/step.cpp:1003`, `cpp/tscore/game_loop.cpp:1444`
  - Impact: High — the card can generate a much larger swing than the printed effect.

- **[DONE]** **GAP-043**: Card 104 (Solidarity) — prerequisite is not enforced in legality
  - Fix: 6d87fed (gate Solidarity event legality on John Paul II)
  - Rule: Solidarity may only be played after John Paul II Elected Pope has been played.
  - Engine: The event checks the flag and silently does nothing when it is absent, but `legal_modes()` still offers the event as playable.
  - File: `cpp/tscore/step.cpp:1070`, `cpp/tscore/legal_actions.cpp:163`
  - Impact: Low — the engine offers an effectively blank illegal event.

### Category: Missing Card Implementations
- **[WONTFIX]** **GAP-044**: Card 109 (Lone Gunman) — missing entirely
  - Rule: Lone Gunman has a printed event and should create a player decision when drawn.
  - Engine: The card is included in the deck build path, but there is no implementation in `step.cpp` or `apply_hand_event()`, so it falls through to the default no-op event.
  - File: `cpp/tscore/game_state.cpp:13`, `cpp/tscore/step.cpp:1113`, `cpp/tscore/game_loop.cpp:681`
  - Impact: High — a live deck card has no event logic at all.

- **[WONTFIX]** **GAP-045**: Card 110 (Colonial Rear Guards) — missing entirely
  - Rule: Colonial Rear Guards has a printed event and should create player targeting decisions.
  - Engine: The card is in the draw deck, but no event case exists, so it resolves as a no-op.
  - File: `cpp/tscore/game_state.cpp:13`, `cpp/tscore/step.cpp:1113`, `cpp/tscore/game_loop.cpp:681`
  - Impact: High — a live deck card has no event logic at all.

- **[WONTFIX]** **GAP-046**: Card 111 (Panama Canal Returned) — missing entirely
  - Rule: Panama Canal Returned has a printed event and should create player choice/country-selection logic.
  - Engine: The card is in the draw deck, but no event case exists, so it resolves as a no-op.
  - File: `cpp/tscore/game_state.cpp:13`, `cpp/tscore/step.cpp:1113`, `cpp/tscore/game_loop.cpp:681`
  - Impact: High — a live deck card has no event logic at all.

## Summary Table
| Gap ID | Category | Card/Location | Impact | Gap Type |
|--------|----------|---------------|--------|----------|
| GAP-001 | Headline Phase | China Card headline path | Medium | Missing condition check |
| GAP-002 | Operations Phase | Opponent card for ops | High | Hardcoded ordering |
| GAP-003 | Operations Phase | Opponent card for Space | High | Simplified mechanic |
| GAP-004 | Operations Phase | Space legality | High | Missing condition check |
| GAP-005 | Operations Phase | Core ops placement legality | High | Simplified mechanic |
| GAP-006 | Operations Phase | `apply_ops_randomly()` | High | Wrong randomization |
| GAP-007 | Card Events | 7 Socialist Governments | Medium | Wrong randomization |
| GAP-008 | Card Events | 11 Korean War | High | Simplified mechanic |
| GAP-009 | Card Events | 13 Arab-Israeli War | High | Simplified mechanic |
| GAP-010 | Card Events | 16 Warsaw Pact Formed | High | Wrong randomization |
| GAP-011 | Card Events | 19 Truman Doctrine | Medium | Wrong randomization |
| GAP-012 | Card Events | 20 Olympic Games | Medium | Wrong randomization |
| GAP-013 | Card Events | 23 Marshall Plan | High | Wrong randomization |
| GAP-014 | Card Events | 24 Indo-Pakistani War | High | Simplified mechanic |
| GAP-015 | Card Events | 28 Suez Crisis | Medium | Wrong randomization |
| GAP-016 | Card Events | 29 East European Unrest | Medium | Wrong randomization |
| GAP-017 | Card Events | 30 Decolonization | Medium | Wrong randomization |
| GAP-018 | Card Events | 32 UN Intervention | High | Wrong randomization |
| GAP-019 | Card Events | 33 De-Stalinization | High | Wrong randomization |
| GAP-020 | Card Events | 37 Special Relationship | Medium | Wrong randomization |
| GAP-021 | Card Events | 39 Brush War | High | Simplified mechanic |
| GAP-022 | Card Events | 49 How I Learned | Medium | Missing player choice |
| GAP-023 | Card Events | 50 Junta | High | Missing player choice |
| GAP-024 | Card Events | 52 Missile Envy | High | Wrong randomization |
| GAP-025 | Card Events | 59 Muslim Revolution | Medium | Wrong randomization |
| GAP-026 | Card Events | 67 Puppet Governments | Medium | Wrong randomization |
| GAP-027 | Card Events | 68 Grain Sales to Soviets | High | Wrong randomization |
| GAP-028 | Card Events | 71 OAS Founded | Medium | Wrong randomization |
| GAP-029 | Card Events | 75 Voice of America | Medium | Wrong randomization |
| GAP-030 | Card Events | 76 Liberation Theology | Medium | Wrong randomization |
| GAP-031 | Card Events | 77 Ussuri River Skirmish | Medium | Wrong randomization |
| GAP-032 | Card Events | 78 Ask Not | High | Wrong randomization |
| GAP-033 | Card Events | 83 Che | High | Missing player choice |
| GAP-034 | Card Events | 84 Our Man in Tehran | Medium | Wrong randomization |
| GAP-035 | Card Events | 90 The Reformer | Medium | Wrong randomization |
| GAP-036 | Card Events | 91 Marine Barracks Bombing | Medium | Wrong randomization |
| GAP-037 | Card Events | 98 Latin American Debt Crisis | Medium | Missing player choice |
| GAP-038 | Card Events | 105 Iran-Iraq War | High | Simplified mechanic |
| GAP-039 | Special / Persistent Mechanics | 9 Vietnam Revolts | High | Simplified mechanic |
| GAP-040 | Special / Persistent Mechanics | 35 Formosan Resolution | Medium | Missing condition check |
| GAP-041 | Special / Persistent Mechanics | 43 Cuban Missile Crisis | High | Simplified mechanic |
| GAP-042 | Special / Persistent Mechanics | 93 Glasnost | High | Simplified mechanic |
| GAP-043 | Special / Persistent Mechanics | 104 Solidarity | Low | Missing condition check |
| GAP-044 | Missing Card Implementations | 109 Lone Gunman | High | Missing mechanic |
| GAP-045 | Missing Card Implementations | 110 Colonial Rear Guards | High | Missing mechanic |
| GAP-046 | Missing Card Implementations | 111 Panama Canal Returned | High | Missing mechanic |

## Gaps by Impact
### High Impact (affects strategy significantly)
- GAP-002: Opponent cards played for ops always fire before the ops.
- GAP-003: Spacing an opponent card incorrectly fires the opponent event.
- GAP-004: Space Race legality ignores minimum ops requirements.
- GAP-005: Normal ops placement is simplified away from real TS placement rules.
- GAP-006: Free borrowed/stolen ops are randomized instead of chosen, and their realignments are simplified.
- GAP-008: Card 11 (Korean War) — modeled as a coup instead of a war.
- GAP-009: Card 13 (Arab-Israeli War) — modeled as a coup instead of a war.
- GAP-010: Card 16 (Warsaw Pact Formed) — branch-internal country choices are randomized.
- GAP-013: Card 23 (Marshall Plan) — target countries are randomized.
- GAP-014: Card 24 (Indo-Pakistani War) — modeled as a coup instead of a war.
- GAP-018: Card 32 (UN Intervention) — borrowed ops are spent randomly.
- GAP-019: Card 33 (De-Stalinization) — both the source and destination moves are randomized.
- GAP-021: Card 39 (Brush War) — modeled as a coup instead of a war.
- GAP-023: Card 50 (Junta) — the free action is hardcoded to coup, and both targets are randomized.
- GAP-024: Card 52 (Missile Envy) — stolen ops are spent randomly.
- GAP-027: Card 68 (Grain Sales to Soviets) — stolen ops are spent randomly.
- GAP-032: Card 78 (Ask Not) — discard count/cards are randomized, and the 4-card cap is missing.
- GAP-033: Card 83 (Che) — coups are randomized and the second coup is forced whenever available.
- GAP-038: Card 105 (Iran-Iraq War) — target is randomized and the event is modeled as a coup.
- GAP-039: Card 9 (Vietnam Revolts) — the Southeast-Asia-only ops bonus is implemented as a global ops modifier.
- GAP-041: Card 43 (Cuban Missile Crisis) — the effect becomes a permanent no-coup lock with no cancellation path.
- GAP-042: Card 93 (Glasnost) — the SALT follow-up is upgraded to a full extra action round.
- GAP-044: Card 109 (Lone Gunman) — missing entirely.
- GAP-045: Card 110 (Colonial Rear Guards) — missing entirely.
- GAP-046: Card 111 (Panama Canal Returned) — missing entirely.

### Medium Impact (suboptimal but playable)
- GAP-001: China Card can be selected illegally as a headline in the generic/random path.
- GAP-007: Card 7 (Socialist Governments) — Western Europe targets are randomized.
- GAP-011: Card 19 (Truman Doctrine) — target country is randomized.
- GAP-012: Card 20 (Olympic Games) — boycott placements are randomized.
- GAP-015: Card 28 (Suez Crisis) — the two countries hit are randomized.
- GAP-016: Card 29 (East European Unrest) — the affected countries are randomized.
- GAP-017: Card 30 (Decolonization) — placements are randomized.
- GAP-020: Card 37 (Special Relationship) — follow-up placements are randomized.
- GAP-022: Card 49 (How I Learned) — DEFCON 1 is not a legal choice.
- GAP-025: Card 59 (Muslim Revolution) — removals are randomized and can target zero-US countries.
- GAP-026: Card 67 (Puppet Governments) — the three placements are randomized.
- GAP-028: Card 71 (OAS Founded) — the placements are randomized.
- GAP-029: Card 75 (Voice of America) — removals are randomized.
- GAP-030: Card 76 (Liberation Theology) — distribution is randomized and forced into single points.
- GAP-031: Card 77 (Ussuri River Skirmish) — the 4 influence placements are randomized.
- GAP-034: Card 84 (Our Man in Tehran) — keep/discard decisions and return order are randomized.
- GAP-035: Card 90 (The Reformer) — European placement targets are randomized.
- GAP-036: Card 91 (Marine Barracks Bombing) — the follow-up removals are randomized.
- GAP-037: Card 98 (Latin American Debt Crisis) — the US discard pair is hardcoded instead of chosen.
- GAP-040: Card 35 (Formosan Resolution) — Taiwan is treated as a battleground even when the US does not control it.

### Low Impact (edge cases, rare situations)
- GAP-043: Card 104 (Solidarity) — prerequisite is not enforced in legality.
