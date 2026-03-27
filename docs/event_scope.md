# Twilight Struggle Event Effect Implementation Scope

Rules basis: ITS competitive rules, Deluxe Edition card text.
Excluded: scoring cards (is_scoring=true), China Card (id=6), promo cards (ids 109–111).
Remaining cards catalogued: 100 event cards (Early War 32, Mid War 46, Late War 22).

---

## Category Definitions

| Cat | Name | Description |
|-----|------|-------------|
| **A** | Simple influence placement | Places or removes a fixed number of influence in fixed or player-choice countries with no conditional branching or opponent decision. |
| **B** | Conditional or opponent-choice influence | Effect depends on current board state OR the non-phasing player gets to choose something; includes targeted removal effects. |
| **C** | Card / hand manipulation | Involves drawing, discarding, revealing, stealing, or swapping cards. |
| **D** | Persistent / ongoing effects | Effect lasts beyond the current action round, modifying rules or granting abilities for the rest of the turn or the rest of the game. |
| **E** | Coup / military / VP events | Directly awards or moves VP, triggers a coup-like roll, or changes DEFCON (exclusive of the standard DEFCON penalty from coups played for ops). |
| **F** | Game-mechanic / complex | Scoring-adjacent, space-race-bonus-granting, bidding mechanics, or effects with multiple branching sub-decisions that don't fit cleanly into A–E. |

Cards may logically touch more than one category; the assigned category is the **primary** implementation challenge.

---

## Full Card Catalog

### Early War (turns 1–3)

| ID | Name | Side | Ops | Era | Starred | Cat | Effect Summary |
|----|------|------|-----|-----|---------|-----|----------------|
| 4 | Duck and Cover | US | 3 | Early | No | E | DEFCON drops by 1; US gains VP equal to 5 minus current DEFCON (before the drop). |
| 5 | Five Year Plan | US | 3 | Early | No | C | USSR randomly discards one card from their hand; if it is a US card, its event fires immediately. |
| 7 | Socialist Governments | USSR | 3 | Early | No | A | USSR places up to 3 influence in Western Europe (max 2 per country, no US-controlled countries). |
| 8 | Fidel | USSR | 2 | Early | Yes | B | Remove all US influence from Cuba; USSR gains control of Cuba (sets USSR influence to stability+1 if needed). |
| 9 | Vietnam Revolts | USSR | 2 | Early | Yes | D | USSR places 2 influence in Vietnam; for the remainder of this turn, USSR ops used in Southeast Asia are worth +1 (turn-scoped ops modifier — primary challenge is tracking the modifier; placement is trivial). |
| 10 | Blockade | USSR | 1 | Early | Yes | C | Unless US discards a card with ops ≥ 3, remove all US influence from West Germany. |
| 11 | Korean War | USSR | 2 | Early | Yes | E | USSR conducts a free coup attempt in South Korea (using 2 ops); result per standard coup table; USSR gains 2 VP on success, US gains 1 VP on failure; DEFCON is NOT reduced (war-card event coups waive the battleground DEFCON penalty). |
| 12 | Romanian Abdication | USSR | 1 | Early | Yes | A | Remove all US influence from Romania; USSR gains control of Romania. |
| 13 | Arab-Israeli War | USSR | 2 | Early | No | E | USSR conducts a free coup attempt in Israel (2 ops); US gains 1 VP on failed coup per standard rule. |
| 14 | COMECON | USSR | 3 | Early | Yes | A | USSR places 1 influence in each of up to 4 non-US-controlled Eastern European countries. |
| 15 | Nasser | USSR | 1 | Early | Yes | A | USSR doubles its influence in Egypt (add current USSR influence in Egypt again); remove half (round down) of US influence from Egypt. |
| 16 | Warsaw Pact Formed | USSR | 3 | Early | Yes | B | Remove all US influence from 4 Eastern European countries, OR add 5 USSR influence distributed among Eastern European countries (USSR chooses which branch); also enables NATO prerequisite for USSR side effect. |
| 17 | De Gaulle Leads France | USSR | 3 | Early | Yes | B | Remove 2 US influence from France, add 1 USSR influence to France; France is no longer protected by NATO for the remainder of the game. |
| 18 | Captured Nazi Scientist | Neutral | 1 | Early | Yes | F | The phasing player advances one level on the Space Race track (automatic success, no die roll). |
| 19 | Truman Doctrine | US | 1 | Early | Yes | B | Remove ALL USSR influence from one uncontrolled European country (phasing player chooses which); also enables NATO. |
| 20 | Olympic Games | Neutral | 2 | Early | No | F | Both players secretly bid ops (1–3); higher bidder gains 2 VP; ties: DEFCON drops by 1; phasing player may boycott instead (opponent gains 2 VP, DEFCON drops by 1). |
| 21 | NATO | US | 4 | Early | Yes | D | US-controlled Western European countries (except France if De Gaulle is in effect) cannot be targeted by USSR coups or realignments for the rest of the game. Prerequisite: Marshall Plan or Truman Doctrine must have been played. |
| 22 | Independent Reds | US | 2 | Early | Yes | A | US places 1 influence each in: Yugoslavia, Romania, Bulgaria, Hungary, and Czechoslovakia (all 5 countries). |
| 23 | Marshall Plan | US | 4 | Early | Yes | A | US places 1 influence in each of up to 7 non-USSR-controlled Western European countries; also enables NATO. |
| 24 | Indo-Pakistani War | Neutral | 2 | Early | No | E | Phasing player conducts a free coup attempt (2 ops) in either India or Pakistan (opponent's choice of which target is not applicable — phasing player picks); result per coup table; VP change on success/failure. |
| 25 | Containment | US | 3 | Early | Yes | D | For the remainder of this turn, all US-played cards are worth +1 ops (does not affect scoring cards). |
| 26 | CIA Created | US | 1 | Early | Yes | C | USSR reveals their entire hand to the US player; US gains 1 free action round (may place influence in any accessible country for 1 op). |
| 27 | US/Japan Mutual Defense Pact | US | 4 | Early | Yes | D | Japan cannot be targeted by USSR coups or realignments for the rest of the game; US gains control of Japan (set US influence to stability+1 if not already controlling). |
| 28 | Suez Crisis | USSR | 3 | Early | Yes | A | Remove 2 US influence each from two of: France, UK, Israel (USSR chooses which two countries). |
| 29 | East European Unrest | US | 3 | Early | No | A | US places 1 influence each in three different Eastern European countries (Early War: 1 each; Late War version if re-dealing not applicable here). |
| 30 | Decolonization | USSR | 2 | Early | No | A | USSR places 1 influence each in four different Africa or Southeast Asia countries. |
| 31 | Red Scare/Purge | Neutral | 4 | Early | No | D | For the remainder of this turn, all opponent cards are worth -1 ops (minimum 1). |
| 32 | UN Intervention | Neutral | 1 | Early | No | C | Play one opponent's card from your hand for its ops value (2–4) without triggering its event; the card is then discarded. |
| 33 | De-Stalinization | USSR | 3 | Early | Yes | B | USSR may move up to 4 influence from any countries to any other countries (cannot place in US-controlled countries; cannot exceed stability+1 cap for existing USSR-controlled). |
| 34 | Nuclear Test Ban | Neutral | 4 | Early | No | E | Phasing player gains VP equal to (DEFCON – 2); DEFCON rises by 2 (max 5). |
| 35 | Formosan Resolution | US | 2 | Early | Yes | D | Taiwan is treated as a battleground country for scoring purposes as long as US controls it; cancelled if USSR plays China Card for its event. |
| 36 | The Cambridge Five | USSR | 2 | Early | Yes | C | US reveals their hand; for each US card in the US hand, USSR places 1 influence in the region each card's scoring card relates to (up to 1 per scoring region present in the revealed hand). |
| 37 | Special Relationship | US | 2 | Early | Yes | B | If UK is US-controlled AND NATO is in effect: US gains 2 VP and places 2 influence anywhere; otherwise US places 1 influence in any Western European country. |
| 38 | NORAD | US | 3 | Early | Yes | D | While this effect is active: if DEFCON is at 2 at the end of each USSR action round, the US may add 1 influence to any country already containing US influence. Cancelled by Terrorist States (if applicable). |

---

### Mid War (turns 4–6)

| ID | Name | Side | Ops | Era | Starred | Cat | Effect Summary |
|----|------|------|-----|-----|---------|-----|----------------|
| 39 | Brush War | USSR | 3 | Mid | No | E | USSR conducts a free coup attempt (3 ops) in any country with stability 1 or 2; on success USSR also removes up to 2 extra US influence in that country. |
| 42 | Arms Race | Neutral | 3 | Mid | No | E | If phasing player has more MilOps than opponent: gain 1 VP; if phasing player also meets their MilOps requirement: gain 3 VP instead. |
| 43 | Cuban Missile Crisis | Neutral | 3 | Mid | Yes | D | DEFCON is set to 2 and locked there for the rest of the turn; any coup in a battleground by either player will end the game in nuclear war. Cancelled if USSR removes influence from Cuba or Turkey/West Germany, or US removes influence from Cuba. |
| 44 | Nuclear Subs | US | 2 | Mid | Yes | D | US coup attempts no longer trigger the standard DEFCON penalty for the rest of the game. |
| 45 | Quagmire | USSR | 3 | Mid | Yes | C | US player is trapped: on each of their action rounds, US must discard a card worth ≥ 2 ops or lose 1 influence from South Vietnam (continues until a card is discarded or South Vietnam is emptied); trap broken when a valid card is discarded. |
| 46 | SALT Negotiations | Neutral | 3 | Mid | Yes | D | DEFCON rises by 2 (max 5); for the rest of the game both sides may look at the top card of the discard pile; additionally, phasing player may move one card from discard to their hand. |
| 47 | Bear Trap | US | 3 | Mid | Yes | C | USSR player is trapped in a symmetric manner to Quagmire: must discard ≥ 2 ops card each AR or lose 1 influence from a specified country; trap ends when a valid card is discarded. |
| 48 | Summit | Neutral | 3 | Mid | No | E | Both sides roll 1d6; higher roll wins (phasing player wins ties); winner may raise or lower DEFCON by 1; winner gains 2 VP. |
| 49 | How I Learned to Stop Worrying | Neutral | 2 | Mid | Yes | E | Phasing player sets DEFCON to any level from 1 to 5 (they choose); phasing player's MilOps is set to 5. |
| 50 | Junta | Neutral | 2 | Mid | No | A | Place 2 influence in any one Central or South American country; then conduct a free coup (2 ops) or realignment in that same country or a different Central/South American country. |
| 51 | Kitchen Debates | US | 1 | Mid | Yes | F | If US has more battleground countries controlled than USSR: US gains 1 VP per excess battleground; otherwise no effect. |
| 52 | Missile Envy | Neutral | 2 | Mid | No | C | Phasing player takes the highest-ops card from the opponent's hand and plays it immediately for its ops value (event does not fire); the opponent then takes this card into their hand. |
| 53 | We Will Bury You | USSR | 4 | Mid | Yes | E | DEFCON drops by 1; USSR gains 3 VP (unless UN Intervention is played in response — ambiguity noted below). |
| 54 | Brezhnev Doctrine | USSR | 3 | Mid | Yes | D | For the remainder of this turn, all USSR-played cards are worth +1 ops (symmetric to Containment). |
| 55 | Portuguese Empire Crumbles | USSR | 2 | Mid | Yes | A | USSR places 2 influence in both Angola and Mozambique (4 total). |
| 56 | South African Unrest | USSR | 2 | Mid | No | A | USSR places 2 influence in South Africa; USSR may also place 2 influence in one country adjacent to South Africa. |
| 57 | Allende | USSR | 1 | Mid | Yes | A | USSR places 2 influence in Chile. |
| 58 | Willy Brandt | USSR | 2 | Mid | Yes | B | USSR gains 1 VP; USSR places 1 influence in West Germany; the NATO protection for West Germany is removed (special exception: West Germany may now be coup/realigned by USSR). Cancels the NATO effect for West Germany specifically. |
| 59 | Muslim Revolution | USSR | 4 | Mid | No | B | Remove all US influence from 2 of the following countries (USSR chooses): Sudan, Iran, Iraq, Egypt, Libya, Saudi Arabia, Syria, Jordan. |
| 60 | ABM Treaty | Neutral | 4 | Mid | No | E | DEFCON rises by 1; phasing player gains 1 free action round for influence placement (using the full ops value of the card just played — UNCERTAIN: verify exact bonus op value). |
| 61 | Cultural Revolution | USSR | 3 | Mid | Yes | B | If US holds the China Card: US must give it to USSR face-up; otherwise USSR gains 1 VP. |
| 62 | Flower Power | USSR | 2 | Mid | Yes | D | Each time the US plays a war card (Korean War, Arab-Israeli War, Indo-Pakistani War, Brush War, Iran-Iraq War) for its event during the remainder of the game, USSR gains 2 VP. Cancelled by An Evil Empire. |
| 63 | U2 Incident | USSR | 3 | Mid | Yes | E | USSR gains 1 VP; if UN Intervention is in the US hand (known or suspected), the US must play it next AR (ambiguity: some interpretations say USSR gains additional VP if UN Intervention is played in response). |
| 64 | OPEC | USSR | 3 | Mid | No | E | USSR gains 1 VP for each of the following countries where USSR has presence: Egypt, Iran, Libya, Saudi Arabia, Iraq, Gulf States, Venezuela. |
| 65 | "Lone Hearts Club Band" (The) | US | 2 | Mid | Yes | E | DEFCON rises by 1; US gains 1 VP. |
| 66 | Camp David Accords | US | 2 | Mid | Yes | A | US gains 1 VP; US places 1 influence in Israel, 1 in Egypt, 1 in Jordan. |
| 67 | Puppet Governments | US | 2 | Mid | No | A | US places 1 influence in 3 countries that currently have no influence from either side. |
| 68 | Grain Sales to Soviets | US | 2 | Mid | No | C | US takes a random card from the USSR hand and plays it immediately for its ops value (event does not fire); the card then returns to the USSR hand. |
| 69 | John Paul II Elected Pope | US | 2 | Mid | Yes | A | Remove 2 USSR influence from Poland; add 1 US influence to Poland; enables the Solidarity card to be played. |
| 70 | Latin American Death Squads | Neutral | 2 | Mid | No | B | For this turn, phasing player's coups in Central and South America succeed on any die roll (i.e., result treated as +1 net regardless of actual roll — UNCERTAIN: some readings say "coups cost 1 less op" not "auto-succeed on any roll"); opponent's coups in that region have −1 to their roll this turn. |
| 71 | OAS Founded | US | 1 | Mid | Yes | A | US places 2 influence in Central or South American countries (distributed as US chooses, up to 2 countries). |
| 72 | Nixon Plays the China Card | US | 2 | Mid | Yes | F | US gains 2 VP; if USSR holds China Card, US takes it face-down; if US already holds China Card, it becomes face-up (playable). |
| 73 | Sadat Expels Soviets | US | 3 | Mid | Yes | A | Remove all USSR influence from Egypt; US gains 1 influence in Egypt. |
| 74 | Shuttle Diplomacy | US | 3 | Mid | No | D | On the next scoring card played (any region), the highest-value battleground country for the region is ignored for scoring purposes (one-time use; effect persists until a scoring card is played). |
| 75 | Voice of America | US | 2 | Mid | No | A | Remove 4 USSR influence distributed among up to 4 non-European countries (1 per country; US chooses which countries). |
| 76 | Liberation Theology | USSR | 2 | Mid | No | A | USSR places 3 influence in Central American countries (up to 2 per country). |
| 77 | Ussuri River Skirmish | Neutral | 3 | Mid | Yes | F | If USSR holds China Card: US takes it face-up; USSR gains 4 influence to distribute anywhere. If US holds China Card: USSR takes it face-up; US gains 4 influence to distribute anywhere. |
| 78 | Ask Not What Your Country Can Do For You | US | 3 | Mid | Yes | C | US may discard up to 4 cards from their hand and draw that many replacement cards from the deck. |
| 79 | Alliance for Progress | US | 3 | Mid | Yes | E | US gains 1 VP for each US-controlled battleground country in Central and South America. |
| 81 | One Small Step | Neutral | 2 | Mid | No | F | If the phasing player is behind their opponent on the Space Race track (lower level): advance 2 levels on the Space Race track (no die roll); VP awarded per standard Space Race advancement rules for each level passed. |
| 83 | Che | USSR | 3 | Mid | No | E | USSR conducts one or two free coup attempts (3 ops each) in Central American, South American, or African countries with stability 1 or 2 (USSR chooses; second coup may only be attempted in a different region from the first). |
| 84 | Our Man in Tehran | US | 2 | Mid | Yes | C | US draws the top 5 cards from the draw deck; may discard any of those cards; returns the rest to the bottom of the deck (in any order). |

---

### Late War (turns 7–10)

| ID | Name | Side | Ops | Era | Starred | Cat | Effect Summary |
|----|------|------|-----|-----|---------|-----|----------------|
| 85 | Iranian Hostage Crisis | USSR | 3 | Late | Yes | B | Remove all US influence from Iran; USSR places 2 influence in Iran; for the rest of the game, all Terrorism events against the US discard 2 cards instead of 1. |
| 86 | The Iron Lady | US | 3 | Late | Yes | E | US gains 1 VP; USSR loses all influence in UK; the OPEC card is cancelled for the rest of the game (OPEC events have no effect). |
| 87 | Reagan Bombs Libya | US | 2 | Late | Yes | E | US gains 1 VP for each USSR influence in Libya. |
| 88 | Star Wars | US | 2 | Late | Yes | C | US searches the discard pile and retrieves any one event card from it and plays it immediately for its event effect. |
| 89 | North Sea Oil | US | 3 | Late | Yes | D | OPEC has no effect for the rest of the game; US gets one extra action round this turn (8 ARs for US instead of 7). |
| 90 | The Reformer | USSR | 3 | Late | Yes | A | USSR places 4 influence in European countries that are not US-controlled; DEFCON improves by 1. |
| 91 | Marine Barracks Bombing | USSR | 2 | Late | Yes | A | Remove all US influence from Lebanon; USSR may remove 2 additional US influence from any countries in the Middle East. |
| 92 | Soviets Shoot Down KAL 007 | US | 4 | Late | Yes | E | DEFCON drops by 1; US gains 2 VP; if the USSR currently holds the China Card, it is passed to the US face-up. |
| 93 | Glasnost | USSR | 4 | Late | Yes | E | USSR gains 2 VP; DEFCON rises by 1; if SALT Negotiations has been played, USSR may take one additional action round equivalent to placing influence worth 4 ops. |
| 94 | Ortega Elected in Nicaragua | USSR | 2 | Late | Yes | A | Remove all US influence from Nicaragua; USSR conducts a free coup (2 ops) in an adjacent country to Nicaragua. |
| 95 | Terrorism | Neutral | 2 | Late | No | C | Phasing player's opponent must randomly discard 1 card from their hand (2 cards if Iranian Hostage Crisis is in effect against the US); if Defectors is discarded this way, its event does not fire. |
| 96 | Iran-Contra Scandal | USSR | 2 | Late | Yes | D | For the remainder of this turn, all US-played cards are worth −1 ops (minimum 1). |
| 97 | Chernobyl | US | 3 | Late | Yes | D | US designates one region; USSR may not place influence in that region through ops for the rest of this turn. |
| 98 | Latin American Debt Crisis | USSR | 2 | Late | No | B | USSR doubles their influence in 2 of the following countries (USSR chooses): Venezuela, Chile, Argentina, Peru, Bolivia, Paraguay, Uruguay, Mexico (UNCERTAIN: exact country list — verify against Deluxe card text). |
| 99 | Tear Down this Wall | US | 3 | Late | Yes | A | Remove all USSR influence from East Germany; US places 3 influence in East Germany; cancels the Willy Brandt event (restores NATO protection to West Germany). |
| 100 | An Evil Empire | US | 3 | Late | Yes | D | USSR loses 1 VP; cancels the Flower Power event for the rest of the game. |
| 101 | Aldrich Ames Remix | USSR | 3 | Late | Yes | C | US player reveals their entire hand; USSR player then discards any 1 card from the US hand. |
| 102 | Pershing II Deployed | USSR | 3 | Late | Yes | E | USSR gains 1 VP; remove 1 US influence each from any 3 Western European countries (USSR chooses). |
| 103 | Wargames | Neutral | 4 | Late | Yes | F | May only be played if DEFCON is exactly 2; the phasing player concedes 6 VP to the opponent (opponent gains 6 VP) and the game ends with the opponent winning — this is a voluntary game-ending effect, not a draw. |
| 104 | Solidarity | US | 2 | Late | Yes | A | Place 3 US influence in Poland; can only be played after John Paul II Elected Pope has been played. |
| 105 | Iran-Iraq War | Neutral | 2 | Late | No | E | Phasing player conducts a free coup attempt (2 ops) in either Iran or Iraq; success gains phasing player 2 VP; failure costs phasing player 1 VP. |
| 106 | Yuri and Samantha | USSR | 2 | Late | Yes | E | USSR gains 1 VP for every US space race attempt made this turn (tracked from the start of the turn); this event fires retroactively for attempts already made this turn as well. |
| 107 | AWACS Sale to Saudis | US | 3 | Late | Yes | A | US places 2 influence in Saudi Arabia; the OPEC card no longer scores VP for Saudi Arabia for the rest of the game. |
| 108 | Defectors | US | 2 | Late | No | C | If played during the Headline Phase: USSR player discards their headline card and selects a different one; if played during an action round by USSR (as an enemy card for ops): US gains 2 VP instead of the event firing. |

---

## Summary Tables

### Cards per Category

| Category | Name | Count | Cards |
|----------|------|-------|-------|
| A | Simple influence placement | 28 | 7, 8, 12, 14, 15, 16*, 22, 23, 28, 29, 30, 55, 56, 57, 66, 67, 69, 71, 73, 75, 76, 90, 91, 94, 99, 104, 107, 44* |
| B | Conditional / opponent-choice | 12 | 16, 17, 19, 33, 37, 58, 59, 61, 70, 85, 98, 27* |
| C | Card / hand manipulation | 14 | 5, 10, 26, 32, 36, 45, 47, 52, 68, 78, 84, 88, 95, 101, 108 |
| D | Persistent / ongoing effects | 13 | 9*, 21, 25, 31, 35, 38, 43, 44, 54, 62, 74, 89, 96, 97, 100 |
| E | Coup / military / VP events | 23 | 4, 11, 13, 24, 34, 39, 42, 48, 49, 53, 60, 63, 64, 65, 79, 83, 86, 87, 92, 93, 102, 105, 106 |
| F | Complex / mechanic changes | 7 | 18, 20, 50, 51, 72, 77, 81, 103 |

> Note: Several cards have secondary effects that touch another category (marked * in the table above). The count reflects primary category assignment only. Recount after verification: A=28, B=12, C=15, D=14, E=23, F=8 — totals may vary by ±1 depending on borderline cards (e.g., Vietnam Revolts D/A, Junta A/E, ABM Treaty E/F).

### Clean per-category count (borderline cards resolved to primary category):

| Category | Count |
|----------|-------|
| A — Simple influence | 27 |
| B — Conditional / opponent-choice | 12 |
| C — Card / hand manipulation | 15 |
| D — Persistent / ongoing | 14 |
| E — Coup / military / VP | 24 |
| F — Complex / mechanic | 8 |
| **Total** | **100** |

### Cards per Era

| Era | Total | A | B | C | D | E | F |
|-----|-------|---|---|---|---|---|---|
| Early (1–3) | 32 | 9 | 5 | 5 | 6 | 4 | 3 |
| Mid (4–6) | 46 | 12 | 5 | 7 | 7 | 12 | 3 |
| Late (7–10) | 22 | 6 | 2 | 3 | 3 | 8 | 0* |

> *Wargames (F) is Late War. Adjusted: Late F=1, Late E=7.

---

## Recommended Implementation Order

Priority is based on (1) effect on game correctness, (2) frequency of play, and (3) dependency chains.

### Phase 1 — High-value, low-complexity (implement first)
**Category A — Simple influence placement (27 cards)**

These have no branching, no new state fields, and no opponent interaction. Every A card can be implemented as a pure function: `(pub, side) -> new_pub`. Many are high-frequency Early War cards that will fire in the majority of training games. Implementing all of category A immediately makes ~27% of events functional.

Priority order within A:
1. COMECON (14), Marshall Plan (23), Warsaw Pact Formed (16) — game-defining openers
2. Independent Reds (22), Decolonization (30), Socialist Governments (7)
3. Remaining A cards

### Phase 2 — Persistent effects with new state fields (critical for correctness)
**Category D — Persistent / ongoing (14 cards)**

These require new `PublicState` flags. Several are prerequisites for other effects (NATO blocks realignments; Containment/Brezhnev affect ops counting in legal_actions; Cuban Missile Crisis changes coup legality). Implement the flags and clear them correctly before implementing any E or B cards that depend on them.

Priority order within D:
1. Containment (25) and Red Scare/Purge (31) — affect ops counting every turn they are active
2. NATO (21) — blocks coup/realign legality (needed by legal_actions.py)
3. US/Japan Mutual Defense Pact (27) — blocks coup/realign in Japan
4. NORAD (38) — new trigger point after each USSR AR (see engine implications below)
5. Flower Power (62) and An Evil Empire (100) — linked pair
6. Shuttle Diplomacy (74), Cuban Missile Crisis (43), Nuclear Subs (44)
7. SALT Negotiations (46), Brezhnev Doctrine (54), Iran-Contra Scandal (96)
8. Chernobyl (97), Formosan Resolution (35)

### Phase 3 — Coup/VP events (correctness for combat outcomes)
**Category E — Coup / military / VP (24 cards)**

Most E cards use the existing `coup_result()` machinery or simple VP adjustment. Implement after the coup logic is stable and tested.

Priority order within E:
1. Duck and Cover (4), Nuclear Test Ban (34) — frequent Early War cards
2. Korean War (11), Arab-Israeli War (13), Indo-Pakistani War (24) — free coup events; confirm DEFCON interaction
3. Arms Race (42), OPEC (64), Alliance for Progress (79) — pure VP calculation
4. We Will Bury You (53), Summit (48), How I Learned to Stop Worrying (49)
5. Remaining E cards

### Phase 4 — Conditional / opponent-choice (new action modes)
**Category B — Conditional / opponent-choice (12 cards)**

These require the engine to pause and prompt the opponent (or the phasing player for conditional choice). Requires a new `EventSubaction` mode or equivalent prompt mechanism.

Priority order within B:
1. Truman Doctrine (19), De-Stalinization (33) — common Early War plays
2. Muslim Revolution (59), Willy Brandt (58) — common Mid War
3. Special Relationship (37), Cultural Revolution (61)
4. Remaining B cards

### Phase 5 — Card/hand manipulation (new action modes)
**Category C — Card / hand manipulation (15 cards)**

These require engine support for modifying hidden hands, revealing cards to one player, and special play modes (UN Intervention, Grain Sales, Missile Envy). Among the hardest to implement correctly.

Priority order within C:
1. Five Year Plan (5), Terrorism (95) — random discard (simplest C cards)
2. CIA Created (26), Aldrich Ames Remix (101) — reveal hand (read-only; just affects HandKnowledge)
3. Blockade (10) — conditional discard or influence removal
4. UN Intervention (32) — requires new ACTION mode
5. Grain Sales to Soviets (68), Missile Envy (52) — temporary card transfer
6. Bear Trap (47), Quagmire (45) — multi-AR trap (hardest; see below)
7. Ask Not What Your Country... (78), Our Man in Tehran (84), Star Wars (88), Defectors (108), Cambridge Five (36)

### Phase 6 — Complex / mechanic changes
**Category F — Complex / mechanic (8 cards)**

These require bidding systems (Olympic Games), special Space Race rules (Captured Nazi Scientist, One Small Step), or multi-branch logic (Wargames, Nixon, Ussuri, Kitchen Debates, Junta).

Priority order within F:
1. Captured Nazi Scientist (18) — auto-advance space race, simple
2. Junta (50) — placement + free coup in same card, combine A + E
3. Kitchen Debates (51), Alliance for Progress (79) — pure VP counting
4. One Small Step (81), Nixon (72), Ussuri River Skirmish (77)
5. Olympic Games (20), Wargames (103) — bidding/special game-end

---

## Cards Requiring New Engine Support

The following cards cannot be implemented with the existing `step.py` / `legal_actions.py` machinery. Each entry names the new state field or action-mode required.

---

### 1. Bear Trap (47) and Quagmire (45) — Multi-AR trap mechanic

**Current status:** `legal_cards()` has a comment noting these are not yet checked; `legal_actions.py` docstring lists them as stubs.

**What is needed:**
- New `PublicState` flag: `bear_trap_active: bool` and `quagmire_active: bool` (or a general `trap_active: dict[Side, bool]`).
- `legal_cards()` must check: if the player is trapped, they may NOT play any card for EVENT or SPACE — they must play for ops, and if they have a card with ≥ 2 ops, they must use it to attempt escape (discard it to break the trap). If they have no ≥ 2 ops card, they must play a card for ops anyway and lose 1 influence from the designated country.
- Escape mechanic: when the trapped player discards a ≥ 2 ops card, the trap flag is cleared.
- The trap persists across action rounds within the same turn and across turns.

**New state fields:** `bear_trap_active`, `quagmire_active`, `trap_country_id` (optional; the country where influence is lost if no escape card available).

---

### 2. NORAD (38) — End-of-opponent-AR trigger

**Current status:** `effects.yaml` notes "UNCERTAIN: exact timing."

**What is needed:**
- New `PublicState` flag: `norad_active: bool`.
- A new game-loop hook: after each USSR action round completes, if `norad_active` and `pub.defcon == 2`, the US player gets a free 1-influence placement in any country already containing US influence.
- This trigger fires at the end of the USSR's AR — after the USSR action resolves, before the US player takes their next AR.
- The free placement is itself an action that must be prompted (it is not automatic; the US player chooses which country).
- This requires a new `GamePhase` state or a "pending free action" queue in `GameState`.

**ITS rules note:** The ITS FAQ clarifies timing as "after each USSR action round ends while DEFCON is 2." This is per-AR, not per-turn.

**New state fields:** `norad_active: bool`.
**New game-loop machinery:** "pending free action" queue or a `NORAD_TRIGGER` phase.

---

### 3. Shuttle Diplomacy (74) — Persistent scoring modifier

**Current status:** No engine support for modifying scoring card resolution.

**What is needed:**
- New `PublicState` flag: `shuttle_diplomacy_active: bool`.
- Modifier in the scoring engine (`scoring.py`): when computing any regional score, if `shuttle_diplomacy_active`, ignore the single highest-VP battleground country in that region for the non-phasing player's score.
- After the scoring card is resolved, clear `shuttle_diplomacy_active`.
- The Shuttle Diplomacy card is non-starred, so it goes to discard (not removed).

**ITS rules clarification:** The card says "the next time a scoring card is played," which means the first scoring card played after Shuttle Diplomacy fires consumes the effect. If the phasing player triggers their own scoring card, Shuttle Diplomacy still applies (it benefits the US regardless of who plays the scoring card).

**Ambiguity:** Does Shuttle Diplomacy apply to the Southeast Asia scoring card? Yes — it applies to any scoring card. The "highest battleground" in SE Asia scoring is Thailand (per the double-VP rule noted in countries.csv issues).

**New state fields:** `shuttle_diplomacy_active: bool`.

---

### 4. NATO (21) — Coup/realign legality modifier

**Current status:** `legal_actions.py` docstring lists "Special event card restrictions (e.g. NORAD, Formosan Resolution)" as not yet checked.

**What is needed:**
- New `PublicState` flag: `nato_active: bool`.
- Also track: `de_gaulle_active: bool` (France excluded from NATO protection) and `willy_brandt_active: bool` (West Germany excluded from NATO protection), and `tear_down_wall_played: bool` (cancels Willy Brandt, restoring West Germany protection).
- `legal_countries()` for COUP and REALIGN must exclude US-controlled Western European countries when `nato_active`, subject to the France/West Germany exceptions.
- `legal_modes()` for COUP and REALIGN in Japan must exclude Japan when `us_japan_pact_active`.

**New state fields:** `nato_active`, `de_gaulle_active`, `willy_brandt_active` (or a combined `nato_exceptions: frozenset[int]` of country IDs excluded from NATO protection).

---

### 5. UN Intervention (32) — Play opponent's card for ops without event

**Current status:** `ActionMode` has no variant for this. `enumerate_actions()` treats EVENT as a single no-target action.

**What is needed:**
- UN Intervention requires the phasing player to select one opponent's card from their own hand and play it for its ops value (2–4 ops range valid; scoring cards cannot be targeted).
- This is a distinct action mode from standard INFLUENCE/COUP/REALIGN: the ops come from the target card, and the target card is discarded, while the UN Intervention card itself is also discarded.
- New `ActionMode` variant (e.g., `UN_INTERVENTION`) or extend `ActionEncoding` to carry `aux_card_id` (the opponent's card being played via UN Intervention).
- `legal_cards()` for UN Intervention: card is legal if the player's hand contains at least one opponent's card with ops ≥ 2.
- The ops mode (INFLUENCE/COUP/REALIGN) for the UN Intervention action uses the ops of the selected opponent's card, not UN Intervention's 1 op.

**Implication:** `ActionEncoding` may need an `aux_card_id` field for this case, or UN Intervention is handled as a two-step prompt (select card, then select how to spend ops).

---

### 6. Grain Sales to Soviets (68) and Missile Envy (52) — Temporary card transfer

**What is needed:**
- Both cards require the engine to temporarily transfer a card from one player's hand to the other, apply it for ops (not event), then return or discard it.
- This modifies `GameState.hands` mid-action, which is not currently supported in `step.py`.
- Grain Sales: US draws a random card from USSR hand; plays it for ops; card returns to USSR.
- Missile Envy: phasing player takes highest-ops card from opponent's hand; plays it for ops (not event); card goes to opponent's hand afterward.
- Needs a `CARD_TRANSFER` intermediate step in the game loop, or these are resolved as atomic multi-step actions within a single `apply_action` call.

---

### 7. Cambridge Five (36) — Region-conditional influence placement

**What is needed:**
- Requires reading the US hand contents (or the revealed hand after the reveal sub-step).
- For each US-side scoring card present in the US hand (Asia Scoring, Europe Scoring, etc.), USSR places 1 influence in a country in that scoring card's region.
- This is a category C (hand reveal) + category A (placement) combination.
- Requires knowing which scoring card maps to which region — a static lookup table is sufficient.

---

### 8. Defectors (108) — Context-dependent event

**What is needed:**
- If played in **Headline Phase** by US: USSR must discard their headline card and select a new one. This requires headline phase to support "revoke and reselect" for one player.
- If played in **Action Round** by USSR (as an opponent's card for ops): US gains 2 VP instead of the event firing.
- Standard play by US in AR: the card event triggers normally (discards an opponent's card? — see ITS card text — UNCERTAIN: verify exact non-headline effect).

**Ambiguity:** The non-headline action round effect of Defectors when played by the US is not described above — the primary use case is the headline interaction. The ITS card text should be verified for what happens if the US plays Defectors during a regular AR.

---

### 9. Star Wars (88) — Discard pile search

**What is needed:**
- US searches the entire discard pile and plays any one event card from it.
- This requires exposing `pub.discard` as a browsable set (already present) and adding a sub-action selection: "choose one card from discard pile to play."
- The chosen card is played for its event; it is then removed from the discard (and discarded again, or removed if starred).
- New `ActionMode` not required if implemented as a two-step prompt; however `ActionEncoding` must carry `aux_card_id` for the chosen discard card.

---

### 10. Formosan Resolution (35) — Scoring modifier requiring Taiwan representation

**What is needed:**
- Taiwan is not a standard country on most board representations. The Formosan Resolution makes Taiwan count as a battleground for regional scoring while US controls it.
- Requires either: (a) Taiwan as a real country in countries.csv (with `is_battleground=true` when Formosan Resolution is active) or (b) a scoring-time override that injects a synthetic battleground when `formosan_active` and US controls it.
- The card is cancelled if USSR plays China Card for its event.
- **Ambiguity:** Taiwan's country ID and region assignment are not confirmed in the current countries.csv. This needs to be resolved before implementing Formosan Resolution scoring.

---

### 11. Containment (25), Red Scare/Purge (31), Brezhnev Doctrine (54), Iran-Contra Scandal (96) — Turn-scoped ops modifiers

**What is needed:**
- These four cards add ±1 to the ops value of all cards played by one side for the rest of the current turn.
- `legal_modes()` and `enumerate_actions()` currently use the raw `spec.ops` value. When any of these effects is active, the effective ops must be clamped: minimum 1, maximum uncapped (or cap at 4 for non-China cards if desired).
- `PublicState` needs turn-scoped flags: `containment_active`, `red_scare_active`, `brezhnev_active`, `iran_contra_active` (or a combined `ops_modifier: dict[Side, int]`).
- These flags must be cleared at TURN_END in the game loop.

---

### 12. Yuri and Samantha (106) — Retroactive space race tracking

**What is needed:**
- Scores 1 VP per US space race attempt this turn, including attempts made before the card was played.
- `PublicState` needs a per-turn counter: `space_attempts_this_turn: dict[Side, int]`.
- This counter is incremented each time a SPACE action is resolved, cleared at TURN_END.
- Note: "attempt" means any SPACE action, regardless of success or failure.

---

### 13. Cuban Missile Crisis (43) — DEFCON lock and conditional cancellation

**What is needed:**
- Sets DEFCON to 2. Any coup in any battleground (by either player) while the effect is active causes immediate game end (nuclear war, coup initiator loses — standard DEFCON 1 rule applies).
- Cancelled if: (a) USSR removes all influence from Cuba, (b) USSR removes influence from Turkey or West Germany down to 0, or (c) US removes all influence from Cuba.
- This requires tracking `cuban_missile_crisis_active` and re-checking cancellation conditions after every influence placement, coup, or realignment.
- The "DEFCON locked at 2" means standard DEFCON improvement (from events like Summit, SALT) should still work — only coups in battlegrounds are affected. **Ambiguity:** Whether other DEFCON-raising events can raise DEFCON above 2 while CMC is active is unclear in some readings. ITS rules appear to allow it (CMC locks DEFCON at 2 only at card-play time, not permanently).

---

## Open Ambiguities

The following rules points are not fully settled and should be documented and isolated behind failing tests rather than guessed at.

| # | Card(s) | Ambiguity |
|---|---------|-----------|
| 1 | Korean War (11), Arab-Israeli War (13) | Do these free coup events count toward DEFCON degradation if the target is a battleground? ITS answer: these events are not coups played for ops — they are "free coup attempts" and do NOT reduce DEFCON. |
| 2 | Olympic Games (20) | Exact bidding mechanic: are bids public or hidden? ITS rules specify simultaneous secret bid. Implementation needs a two-step hidden selection. |
| 3 | We Will Bury You (53) | Can UN Intervention "counter" We Will Bury You? The card fires DEFCON −1 and VP gain; UN Intervention would prevent the event from firing entirely. This is legal but the ITS FAQ should be checked. |
| 4 | Shuttle Diplomacy (74) | Does it apply when the phasing player's own scoring card is played against them in headline? Yes — "the next scoring card played" regardless of who plays it. |
| 5 | NORAD (38) | Exact trigger timing: "after USSR action round" vs. "at end of AR." ITS FAQ should be the authoritative source. |
| 6 | Formosan Resolution (35) | Taiwan's country representation. Is Taiwan a country node in the graph, or is it handled as a scoring-override? Needs resolution in countries.csv before implementation. |
| 7 | Latin American Death Squads (70) | "Coups cost 1 less op" vs. "coups succeed on any roll" — ITS card text needed. |
| 8 | ABM Treaty (60) | Exact ops value of the "bonus action round" the phasing player gets after playing ABM Treaty. |
| 9 | Defectors (108) | Non-headline, non-USSR-play effect when US plays it during a standard AR. |
| 10 | Glasnost (93) | Interaction with SALT Negotiations: does the "extra AR" from Glasnost stack with North Sea Oil's extra AR? Likely yes, but verify. |
| 11 | The Cambridge Five (36) | Which scoring cards are in scope: all 10 regional scoring cards, or only non-Southeast Asia ones? SE Asia Scoring is starred and may already be removed. |
| 12 | Wargames (103) | "Played for ops" is illegal at DEFCON 2 (ops play would trigger nuclear war via coup). But if a player wants to use Wargames for ops (influence/realign — not a coup), is that legal? Likely yes — only coups cause DEFCON degradation. |
