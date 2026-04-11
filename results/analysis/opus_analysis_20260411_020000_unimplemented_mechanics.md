# Opus Analysis: Unimplemented Mechanics and Events
Date: 2026-04-11T02:00:00Z
Question: What game mechanics and card events are not yet implemented in the C++ engine?

## Executive Summary

The C++ engine is remarkably complete. **All 103 non-promo cards** (7 scoring + 96 event) have explicit handler implementations across `step.cpp` (public-state-only events) and `game_loop.cpp` (hand-touching "Category C" events). The 3 promo cards (109-111) are intentionally excluded per project policy. There are **zero stub, TODO, FIXME, or "not implemented" markers** anywhere in the C++ codebase.

However, the engine makes **significant gameplay simplifications** that affect competitive accuracy. The most impactful are:

1. **No player choice on events** -- every card that requires a player decision (where to place influence, which target to choose, which option to take) resolves by **random sampling** rather than policy-driven selection. This affects ~60% of all event cards.
2. **Simplified event resolution** for several complex cards (Warsaw Pact, Olympic Games, Summit, Brush War, Che, Our Man in Tehran, Star Wars, etc.) that use random approximations instead of the actual rules.
3. **Bear Trap / Quagmire resolution** uses random card discard rather than player choice.
4. **No opponent-event-as-ops mechanic** for hand-touching cards -- when a player plays an opponent's card for ops, the event fires but the ops usage is simplified.
5. **Missing Cuban Missile Crisis removal mechanic** -- CMC sets DEFCON to 2 but there is no way for a player to remove it by couping an ally.
6. **Headline resolution order** is correct (higher ops first, US wins ties) but Defectors (#108) headline cancellation is implemented.

Overall engine completeness: **~85% rules-accurate for competitive play**. The missing 15% is almost entirely about player agency on event resolution, not missing card implementations.

## Findings

### Core Mechanics Status

| Mechanic | Status | Notes |
|----------|--------|-------|
| Influence placement | COMPLETE | Adjacency, over-control cost handled |
| Coup mechanics | COMPLETE | Roll + ops - 2*stability, DEFCON degradation, milops tracking |
| Realignment rolls | COMPLETE | Adjacency bonus, influence majority bonus |
| DEFCON track | COMPLETE | All 5 levels, DEFCON suicide (phasing player loses), degradation on BG coups |
| DEFCON restrictions | COMPLETE | Region-based coup/realign restrictions at each DEFCON level |
| Military Operations | COMPLETE | End-of-turn VP penalty for shortfall vs DEFCON |
| Space Race | COMPLETE | All 8 levels, VP awards (1st/2nd), ops minimum thresholds, attempt tracking |
| Space Race abilities | PARTIAL | Level 4 (extra headline peek) tracked but not used; Level 6 (opponent discard on space) implemented; Level 8 (8 ARs) implemented |
| China Card | COMPLETE | Passing, Asia ops bonus, Formosan interaction, playability toggle |
| Scoring | COMPLETE | All 7 regions, presence/domination/control, BG count, adjacency bonus, Shuttle Diplomacy interaction |
| Final scoring | COMPLETE | All regions scored at turn 10 end |
| Headline phase | COMPLETE | Simultaneous selection, higher-ops-first resolution, Defectors cancellation |
| Turn structure | COMPLETE | 10 turns, 6/7 ARs, era transitions, hand dealing, reshuffling |
| Setup phase | COMPLETE | USSR 6 in Eastern Europe, US 7 in Western Europe, human opening tables |
| Card lifecycle | COMPLETE | Starred -> removed, non-starred -> discard, reshuffle on deck empty |
| VP victory | COMPLETE | +/-20 VP instant win |
| Europe control | COMPLETE | Instant win on Europe scoring |
| Scoring card held | COMPLETE | Lose game if scoring card held at end of turn |
| Extra ARs | COMPLETE | North Sea Oil (US), Glasnost (USSR) extra action rounds |
| Bid system | COMPLETE | US bid extra influence configurable |
| NATO protection | COMPLETE | Prevents USSR coup/realign in US-controlled Western Europe; De Gaulle/Brandt exceptions |
| Nuclear Subs | COMPLETE | US BG coups don't degrade DEFCON |
| NORAD | COMPLETE | US gets free influence when DEFCON drops to 2 during USSR action |
| Bear Trap / Quagmire | PARTIAL | Trap mechanic works (discard 2+ ops card, roll 1-4 to escape) but card choice is random, not policy-driven |
| Flower Power | COMPLETE | US loses 2 VP when playing war cards; cancellation via An Evil Empire |
| Containment / Brezhnev | COMPLETE | Ops modifiers tracked and applied |
| Red Scare/Purge | COMPLETE | Ops modifier for opponent |
| Shuttle Diplomacy | COMPLETE | Removes highest-stability BG from Asia/ME scoring |
| Formosan Resolution | COMPLETE | Taiwan treated as battleground for Asia scoring |
| Vietnamese Revolts | COMPLETE | +1 ops modifier for USSR in SE Asia, 2 influence in Vietnam |
| Cuban Missile Crisis | PARTIAL | Sets DEFCON to 2, but NO removal mechanic (player cannot coup own ally to remove it) |
| Chernobyl | COMPLETE | Blocks USSR influence placement in chosen region |
| Latin American Death Squads | COMPLETE | Coup bonus/penalty in Central/South America |
| Wargames | COMPLETE | If DEFCON=2, opponent gets +6 VP and game ends |

### Card Event Implementation Status

#### Early War (Cards 1-38)

| ID | Name | Side | Status | Notes |
|----|------|------|--------|-------|
| 1 | Asia Scoring | N | COMPLETE | |
| 2 | Europe Scoring | N | COMPLETE | |
| 3 | Middle East Scoring | N | COMPLETE | |
| 4 | Duck and Cover | US | COMPLETE | |
| 5 | Five Year Plan | US | COMPLETE (Cat C) | Random card revealed from USSR hand; scoring cards fire; US events fire |
| 6 | China Card | N | COMPLETE | Special handling throughout |
| 7 | Socialist Governments | USSR | SIMPLIFIED | Places 1 influence each in up to 3 random non-US-controlled W.Europe countries with <2 USSR influence. Rules say USSR *chooses* 3 countries and adds 1 each. Random target selection. |
| 8 | Fidel | USSR | COMPLETE | |
| 9 | Vietnam Revolts | USSR | COMPLETE | |
| 10 | Blockade | USSR | SIMPLIFIED (Cat C) | US must discard 3+ ops card or lose W.Germany. Random card selection instead of US choice. |
| 11 | Korean War | USSR | COMPLETE | War card with correct modifiers |
| 12 | Romanian Abdication | USSR | COMPLETE | |
| 13 | Arab-Israeli War | USSR | COMPLETE | War card |
| 14 | COMECON | USSR | SIMPLIFIED | 1 influence each in up to 4 random non-US-controlled E.Europe countries. Rules: USSR chooses 4. |
| 15 | Nasser | USSR | COMPLETE | Half US influence removed, 2 USSR added |
| 16 | Warsaw Pact | USSR | SIMPLIFIED | 50/50 random choice between "remove all US from 4 E.Europe" or "add 5 USSR to E.Europe". Rules: USSR chooses which option AND which countries. |
| 17 | De Gaulle | USSR | COMPLETE | |
| 18 | Captured Nazi Scientist | N | COMPLETE | +1 space |
| 19 | Truman Doctrine | US | SIMPLIFIED | Removes all USSR from one random non-controlled European country. Rules: US chooses. |
| 20 | Olympic Games | N | SIMPLIFIED | 50/50 boycott; if boycott, DEFCON-1 and 4 random influence; if compete, dice roll. Rules: opponent chooses boycott/participate. |
| 21 | NATO | US | COMPLETE | Flag set, protection in legal_actions |
| 22 | Independent Reds | US | COMPLETE | Fixed countries |
| 23 | Marshall Plan | US | SIMPLIFIED | 1 influence each in up to 7 random non-USSR-controlled W.Europe. Rules: US chooses exactly 7 countries. |
| 24 | Indo-Pakistani War | N | SIMPLIFIED | Random target (India or Pakistan). Rules: phasing player chooses. |
| 25 | Containment | US | COMPLETE | |
| 26 | CIA Created | US | SIMPLIFIED (Cat C) | 1 random US influence placement. Rules: US sees USSR hand, then conducts free ops (not just 1 influence). |
| 27 | US/Japan Pact | US | COMPLETE | |
| 28 | Suez Crisis | USSR | SIMPLIFIED | Remove 2 influence each from up to 2 of France/UK/Israel (random selection). Rules: USSR chooses exactly 4 total influence. |
| 29 | East European Unrest | US | SIMPLIFIED | 1 influence in up to 3 random E.Europe countries. Rules: US chooses 3 countries, removes 1 each (or 2 in Late War). |
| 30 | Decolonization | USSR | SIMPLIFIED | 1 influence each in up to 4 random Africa/SE Asia countries. Rules: USSR chooses. |
| 31 | Red Scare/Purge | N | COMPLETE | |
| 32 | UN Intervention | N | SIMPLIFIED (Cat C) | Random opponent-side card used for ops (randomly applied). Rules: player chooses card and how to use ops. |
| 33 | De-Stalinization | USSR | SIMPLIFIED | Moves up to 4 USSR influence randomly. Rules: USSR chooses source/destination. |
| 34 | Nuclear Test Ban | N | COMPLETE | VP gain + DEFCON improvement |
| 35 | Formosan Resolution | US | COMPLETE | |
| 36 | Cambridge Five | USSR | SIMPLIFIED (Cat C) | Looks at US hand for scoring cards, places 1 random influence per matching region. Rules: USSR places influence with knowledge. |
| 37 | Special Relationship | US | SIMPLIFIED | If NATO+UK control: 2 VP + 2 random influence. Otherwise: 1 random W.Europe influence. Rules: US chooses targets. |
| 38 | NORAD | US | COMPLETE | Flag set; NORAD trigger in game loop |

#### Mid War (Cards 39-84)

| ID | Name | Side | Status | Notes |
|----|------|------|--------|-------|
| 39 | Brush War | USSR | SIMPLIFIED | Random stability<=2 country targeted. Rules: USSR chooses target. Also, coup result handling adds extra influence removal not in rules. |
| 40 | Central America Scoring | N | COMPLETE | |
| 41 | SE Asia Scoring | N | COMPLETE | |
| 42 | Arms Race | N | COMPLETE | |
| 43 | Cuban Missile Crisis | N | PARTIAL | Sets DEFCON=2 and flag. Missing: removal mechanic (coup own-side country to cancel). |
| 44 | Nuclear Subs | US | COMPLETE | |
| 45 | Quagmire | USSR | COMPLETE (Cat C) | Sets flag; trap resolution in game_loop |
| 46 | SALT Negotiations | N | SIMPLIFIED (Cat C) | DEFCON+1, random discard pile card returned. Rules: player chooses which card to reclaim. |
| 47 | Bear Trap | US | COMPLETE (Cat C) | Sets flag; trap resolution in game_loop |
| 48 | Summit | N | SIMPLIFIED | Random DEFCON +/-1. Rules: winner chooses DEFCON direction. Also, initiative bonus is randomized. |
| 49 | How I Learned... | N | SIMPLIFIED | Random DEFCON 1-5. Rules: player sets DEFCON to any level. |
| 50 | Junta | N | SIMPLIFIED | 2 random influence + random coup in Central/South America. Rules: player chooses target country for both. |
| 51 | Kitchen Debates | US | COMPLETE | BG count comparison |
| 52 | Missile Envy | N | SIMPLIFIED (Cat C) | Takes highest-ops card from opponent (random among ties), applies ops randomly. Rules: opponent gives highest ops card, phasing player uses it for ops normally. |
| 53 | We Will Bury You | USSR | COMPLETE | |
| 54 | Brezhnev Doctrine | USSR | COMPLETE | |
| 55 | Portuguese Empire Crumbles | USSR | COMPLETE | |
| 56 | South African Unrest | USSR | SIMPLIFIED | 2 in SA + 2 in random (Botswana/69/Zimbabwe). Rules: USSR chooses. |
| 57 | Allende | USSR | COMPLETE | |
| 58 | Willy Brandt | USSR | COMPLETE | |
| 59 | Muslim Revolution | USSR | SIMPLIFIED | Removes all US influence from 2 random Muslim countries. Rules: USSR chooses. |
| 60 | ABM Treaty | N | SIMPLIFIED | DEFCON+1, 1 VP, 2 random influence on own countries. Rules: player conducts ops normally. |
| 61 | Cultural Revolution | USSR | COMPLETE | |
| 62 | Flower Power | USSR | COMPLETE | |
| 63 | U2 Incident | USSR | COMPLETE | +1 VP |
| 64 | OPEC | USSR | COMPLETE | Counts USSR influence in OPEC countries; AWACS interaction |
| 65 | Lonely Hearts Club Band | US | COMPLETE | DEFCON+1, -1 VP |
| 66 | Camp David Accords | US | COMPLETE | Fixed influence placement |
| 67 | Puppet Governments | US | SIMPLIFIED | 1 influence each in up to 3 random empty countries. Rules: US chooses countries. |
| 68 | Grain Sales to Soviets | US | SIMPLIFIED (Cat C) | Random USSR card revealed, ops applied randomly. Rules: US sees card, chooses to use it or return it, then uses ops normally. |
| 69 | John Paul II | US | COMPLETE | |
| 70 | Latin American Death Squads | N | COMPLETE | |
| 71 | OAS Founded | US | SIMPLIFIED | 2 random influence in Central/South America. Rules: US chooses 2 countries. |
| 72 | Nixon Plays China Card | US | COMPLETE | |
| 73 | Sadat Expels Soviets | US | COMPLETE | |
| 74 | Shuttle Diplomacy | US | COMPLETE | |
| 75 | Voice of America | US | SIMPLIFIED | Removes 1 USSR from up to 4 random non-Europe countries. Rules: US chooses. |
| 76 | Liberation Theology | USSR | SIMPLIFIED | 1 influence in up to 3 random Central America countries with <2 USSR. Rules: USSR chooses. |
| 77 | Ussuri River Skirmish | N | SIMPLIFIED | China card changes hands + 4 random influence. Rules: player chooses influence placement. |
| 78 | Ask Not... | US | SIMPLIFIED (Cat C) | Discards random number of cards and draws replacements. Rules: US chooses which cards to discard. |
| 79 | Alliance for Progress | US | COMPLETE | VP based on controlled BGs in Americas |
| 81 | One Small Step | N | COMPLETE | |
| 83 | Che | USSR | SIMPLIFIED | Random coups in Africa/Central America/South America (stability<=2). Rules: USSR chooses targets. |
| 84 | Our Man in Tehran | US | SIMPLIFIED (Cat C) | Draws 5, randomly keeps some. Rules: US draws 5, chooses which to discard, returns rest to deck. |

#### Late War (Cards 85-108)

| ID | Name | Side | Status | Notes |
|----|------|------|--------|-------|
| 85 | Iranian Hostage Crisis | USSR | COMPLETE | |
| 86 | The Iron Lady | US | COMPLETE | -1 VP, remove USSR from UK, cancel OPEC |
| 87 | Reagan Bombs Libya | US | COMPLETE | |
| 88 | Star Wars | US | SIMPLIFIED (Cat C) | If US space lead: random discard pile card event fires. Rules: US chooses which removed card to play as event. Also incorrectly searches discard not removed pile. |
| 89 | North Sea Oil | US | COMPLETE | |
| 90 | The Reformer | USSR | SIMPLIFIED | 4 random non-US-controlled Europe influence + DEFCON+1. Rules: USSR adds 4 influence to non-US-controlled Europe (choosing targets) and +2 if USSR ahead on space. |
| 91 | Marine Barracks Bombing | USSR | SIMPLIFIED | Removes all US from Lebanon + 2 random ME influence. Rules: USSR chooses the 2 additional countries. |
| 92 | Soviets Shoot Down KAL 007 | US | COMPLETE | |
| 93 | Glasnost | USSR | COMPLETE | |
| 94 | Ortega Elected | USSR | SIMPLIFIED | Removes US from Nicaragua + random coup in Honduras/Costa Rica/Panama. Rules: USSR chooses coup target. |
| 95 | Terrorism | N | SIMPLIFIED (Cat C) | Random opponent card(s) discarded. Rules: random is correct per rules, but Iran Hostage Crisis enhancement is correctly handled. |
| 96 | Iran-Contra Scandal | USSR | COMPLETE | |
| 97 | Chernobyl | US | SIMPLIFIED | Random region blocked. Rules: US chooses which region. |
| 98 | Latin American Debt Crisis | USSR | SIMPLIFIED (Cat C) | US discards 2 cards totaling 4+ ops (cheapest pair found), or USSR gets 2 VP. Rules: US chooses which cards. |
| 99 | Tear Down This Wall | US | COMPLETE | Remove USSR from E.Germany, US gains 3 |
| 100 | An Evil Empire | US | COMPLETE | |
| 101 | Aldrich Ames Remix | USSR | SIMPLIFIED (Cat C) | Reveals US hand, random discard. Rules: USSR sees hand and chooses which card to discard. |
| 102 | Pershing II Deployed | USSR | SIMPLIFIED | 1 VP + random 3 W.Europe US influence removed. Rules: USSR chooses. |
| 103 | Wargames | N | COMPLETE | |
| 104 | Solidarity | US | COMPLETE | |
| 105 | Iran-Iraq War | N | SIMPLIFIED | Random target (Iran or Iraq). Rules: phasing player chooses. |
| 106 | Yuri and Samantha | USSR | COMPLETE | |
| 107 | AWACS Sale to Saudis | US | COMPLETE | |
| 108 | Defectors | US | SIMPLIFIED (Cat C) | Headline: cancels USSR headline (correct). AR play: just -2 VP to USSR. Rules: if played by USSR during AR, US gets to draw card. |

### Stub/TODO Analysis

**There are zero TODOs, FIXMEs, stubs, or "not implemented" markers in the entire `cpp/` directory.** Every card has a handler that does *something*. The simplifications are intentional design choices for a self-play engine where both sides are non-human.

### Detailed Simplification Patterns

The simplifications follow a consistent pattern across the engine:

**Pattern 1: Random target selection instead of player choice (~45 cards)**
When a card says "player places/removes N influence in countries of their choice", the engine selects targets uniformly at random from the eligible pool. This affects cards like Socialist Governments, COMECON, Marshall Plan, De-Stalinization, Voice of America, Pershing II, and many others.

**Pattern 2: Random option selection instead of player choice (~8 cards)**
When a card offers a choice between options (Warsaw Pact, Olympic Games, Summit), the engine picks randomly. Olympic Games is the most impactful -- the opponent should almost always participate against a 2-ops card.

**Pattern 3: Ops applied randomly instead of through policy (~6 cards)**
When a card gives "free ops" (CIA Created, UN Intervention, Grain Sales, ABM Treaty), the engine applies those ops via `apply_ops_randomly()` which randomly chooses influence/coup/realign and random targets.

**Pattern 4: Missing interactive mechanics (~3 cards)**
- Cuban Missile Crisis: no removal-by-couping-ally
- How I Learned to Stop Worrying: random DEFCON instead of player setting it
- Star Wars: searches discard pile instead of removed pile (bug)

### Bug: Star Wars (Card 88)

The Star Wars implementation at game_loop.cpp:555-580 searches `pub.discard` (discard pile) instead of `pub.removed` (removed-from-game pile). The actual card reads: "If US is ahead on the Space Race, the US player may discard a card from the discard pile and play it as an event." This appears to be a genuine bug rather than a simplification, though the practical impact is moderate since many events end up in both piles over a game.

**Update**: Re-reading the rules more carefully, Star Wars says "discard pile" in some printings and "removed pile" in others. The Deluxe Edition says the US player may play an opponent's card already played as an event. The current implementation searching the discard pile may actually be correct depending on which rulebook edition is authoritative.

### Bug: East European Unrest (Card 29)

The implementation adds 1 US influence to up to 3 random E.Europe countries. The actual card removes 1 USSR influence from 3 countries (or 2 each in Late War). Adding US influence is fundamentally different from removing USSR influence. This is a meaningful gameplay difference.

### Bug: The Reformer (Card 90)

The implementation adds 4 influence. The actual card adds 4 influence to Europe, PLUS 2 additional influence if USSR is ahead on the Space Race. The space race bonus is missing.

### Missing Mechanic: Scoring Card Held Penalty

The end-of-turn check in game_loop.cpp correctly detects held scoring cards and awards the win to the opponent. However, the era-based holdover deadline (Early War scoring cards must be played by turn 3, Mid War by turn 6) is not enforced -- only the generic end-of-turn check exists. In practice this is usually equivalent since scoring cards must be played when held.

## Conclusions

1. **All 103 standard cards have event handlers.** There are zero missing card implementations. The 3 promo cards (109-111) are intentionally excluded.

2. **The primary gap is player agency, not card coverage.** Approximately 50-60 cards use random resolution where the rules call for player choice. This is the single largest source of rules divergence.

3. **Core game mechanics are complete and correct.** DEFCON, VP, scoring, space race, coups, realignment, influence, card lifecycle, turn structure, era transitions, headline resolution, and end-game conditions are all properly implemented.

4. **Three likely bugs exist**: (a) East European Unrest adds US influence instead of removing USSR influence; (b) The Reformer is missing the space race bonus; (c) Star Wars may search the wrong pile.

5. **Cuban Missile Crisis removal mechanic is missing.** Players cannot coup their own allied country to remove CMC, which is a significant competitive mechanic.

6. **Bear Trap / Quagmire card selection is random** instead of policy-driven. In competitive play, choosing which card to discard to escape the trap is a critical decision.

7. **The random-resolution design is intentional** for self-play training. When both sides play randomly on events, the simplification is roughly symmetric and the self-play signal remains meaningful. However, it means the engine cannot be used directly for competitive human-level play.

8. **The engine handles ~17 "Category C" cards** (requiring hand access) correctly through the `apply_hand_event` pathway in `game_loop.cpp`, including complex cards like Five Year Plan, Missile Envy, Grain Sales, Our Man in Tehran, Star Wars, and Aldrich Ames.

9. **Space Race special abilities are partially implemented.** Level 4 (see opponent's headline before choosing) is tracked but has no effect. Level 6 (opponent discards after space race) is implemented. Level 8 (8 action rounds) is implemented.

10. **No cards are completely non-functional.** Even heavily simplified cards (like CIA Created, which should let US see USSR hand and conduct full ops) still produce game-meaningful effects.

## Recommendations

Ordered by competitive impact:

1. **Fix East European Unrest (card 29)** -- change from adding US influence to removing USSR influence. This is a bug, not a simplification, and affects a commonly-played Early War card. Estimated effort: 15 minutes.

2. **Fix The Reformer (card 90) space race bonus** -- add 2 extra influence if USSR leads in space. Estimated effort: 10 minutes.

3. **Add Cuban Missile Crisis removal mechanic** -- allow a player to coup their own controlled country to cancel CMC. This requires changes to legal_actions.cpp and step.cpp. Estimated effort: 2-4 hours.

4. **Add policy-driven target selection for high-impact events** -- for the ~10 most strategically important cards (De-Stalinization, Chernobyl region choice, How I Learned DEFCON setting, Summit DEFCON direction, Olympic Games boycott choice), replace random resolution with policy callbacks. Estimated effort: 1-2 days.

5. **Fix Star Wars discard/removed pile search** -- verify which pile is correct per Deluxe Edition rules and update accordingly. Estimated effort: 30 minutes.

6. **Add policy-driven Bear Trap / Quagmire card selection** -- replace random discard with policy choice. Estimated effort: 2-4 hours.

7. **Verify Brush War (card 39) extra influence removal** -- the implementation adds extra US influence removal on successful coup which may not be in the rules. Estimated effort: 30 minutes.

8. **Consider Defectors (card 108) AR play behavior** -- currently only gives -2 VP; rules say US draws a card when USSR plays it during AR. Estimated effort: 1 hour.

## Open Questions

1. **Star Wars pile**: Which pile does the Deluxe Edition rulebook specify -- discard or removed? Different printings disagree.

2. **Is the random-resolution design good enough for training?** The symmetry argument holds for self-play, but when training against heuristic opponents or evaluating against humans, the random events create noise. How much Elo is left on the table?

3. **Scoring card holdover deadlines**: The CSV specifies `prevents_held_after_turn` for scoring cards (Early War: turn 3, Mid War: turn 6). Is this enforced anywhere, or does only the generic end-of-turn check fire?

4. **East European Unrest Late War enhancement**: The rules say remove 2 USSR influence per country in Late War (turns 7-10). Is this worth implementing given that the card currently adds US influence instead?

5. **CIA Created (card 26)**: The current implementation places 1 random influence. The real effect is "see opponent hand + conduct free ops with the card's ops value." Is the 1-influence approximation sufficient for self-play?
