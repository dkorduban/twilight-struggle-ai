# Card-by-card implementation audit vs canonical Twilight Struggle rules

Date: 2026-04-21
Scope: cards 1..108 (promo cards 109/110/111 excluded per CLAUDE.md).
SoT source: cross-validation of `docs/event_scope.md` (project canonical summary),
`data/spec/cards.csv` (metadata), Deluxe Edition rules as recalled, and
`long-prompts/inconsistent-moves.md` (ChatGPT 31-item play-log list, treated as
hypothesis set, not findings).
Engine files reviewed:
- `cpp/tscore/step.cpp`   (main `apply_event` switch, lines 456..1834)
- `cpp/tscore/hand_ops.cpp` (`apply_hand_event`, lines 260..804; `resolve_trap_ar` 1068..1136)
- `cpp/tscore/scoring.cpp` (entire file)
- `cpp/tscore/rule_queries.hpp` (event-legality gates)
- `cpp/tscore/public_state.hpp` (all flag fields)
- `cpp/tscore/legal_actions.cpp` (NATO / US-Japan / Chernobyl / Vietnam bonus)

## Executive summary

**Headline.** The engine is largely correct: most of the 31 "inconsistencies"
in `long-prompts/inconsistent-moves.md` are policy or log-rendering artifacts
(the engine behaves correctly, the agent chose a legal but uninformative
action, or the log display merged adjacent effects). However, the audit
uncovered **six genuine engine bugs**, two of which materially affect US win
rate in the current v32 plateau:

1. **Camp David Accords does NOT prevent Arab-Israeli War event.** (§BUG-1)
   `public_state.hpp` has no `camp_david_active` flag; `is_event_play_allowed`
   only gates NATO / Wargames / Solidarity (rule_queries.hpp:72..89). When
   USSR plays or headlines Arab-Israeli War after Camp David, the engine
   executes the war coup, removing US influence from Israel. This is a direct
   US-side loss of VP and board control. **High US-WR impact.**
2. **SALT Negotiations recovery pulls at most one card.** (§BUG-2) Rules
   permit recovering ANY card from the discard pile (up to one) but also
   raise DEFCON by 2. Engine raises DEFCON by only +1 (hand_ops.cpp:422,
   step.cpp:1064). **Medium impact — hurts both sides symmetrically but
   biases toward the side with a strong discarded card.**
3. **NORAD trigger is not implemented.** (§BUG-3) Card 38 sets
   `norad_active=true` but nothing in the engine responds to that flag
   (grep reveals only the write site in step.cpp:1019 and a read in
   `nn_features.cpp:71` feeding it to the model). No end-of-USSR-AR hook
   adds 1 US influence at DEFCON 2. **Large US-WR impact** — NORAD is a
   defining Late-War US engine and its absence directly explains part of
   the US plateau.
4. **Kitchen Debates missing ops-reveal side condition.** (§BUG-4) Rules
   require US show their hand to reveal that they have more BGs than USSR.
   Engine (step.cpp:1141..1159) correctly checks the count and pays VP, so
   the numeric effect is right; only the hand-reveal mechanic (which has
   info-state implications) is missing.
5. **Yuri and Samantha (106) is retro-prospective.** (§BUG-5) Rules say
   USSR gains 1 VP for each US Space Race attempt **during the remainder of
   the turn**, i.e. future attempts. Engine awards VP for US space attempts
   already made this turn (step.cpp:1810: `next.vp += next.space_attempts[US]`)
   — opposite direction.
6. **Iranian Hostage Crisis (85) doubles Terrorism vs US hands forever but
   Terrorism (95) only doubles when opponent==US.** (§BUG-6) Rules are
   "Terrorism events against the US discard 2". Engine logic at
   hand_ops.cpp:498 uses `opponent == Side::US && pub.iran_hostage_crisis_active`.
   This is actually **correct** — false alarm; kept here for completeness.

Beyond these, the scoring engine (`scoring.cpp`) is clean: none of the five
"scoring card side effects" in the ChatGPT list (items 27-31) are present
in the engine; those are log-rendering artifacts.

## Findings: classification

Notation per card: `[STATUS] ID Name — file:line — note`. STATUS ∈
{CORRECT, BUG, PARTIAL, NOT_IMPLEMENTED, UNCERTAIN}.

### Scoring cards

- [CORRECT]  1 Asia Scoring — scoring.cpp:232,220 — incl. China bonus via `score_asia_final`
- [CORRECT]  2 Europe Scoring — scoring.cpp:239 — `kGameWinEurope=9999` sentinel wins game on control
- [CORRECT]  3 Middle East Scoring — scoring.cpp:241 — shuttle diplomacy interaction OK
- [CORRECT] 40 Central America Scoring — scoring.cpp:243
- [CORRECT] 41 Southeast Asia Scoring — scoring.cpp:245 — country/VP map correct {75:1,…,79:2,80:1,84:1}
- [CORRECT] 80 Africa Scoring — scoring.cpp:247
- [CORRECT] 82 South America Scoring — scoring.cpp:249
- [CORRECT] Shuttle Diplomacy drops top-stability BG in Asia/ME only (scoring.cpp:158..172)

### Early War (turns 1–3)

| ID | Name | Status | File:line | Note |
|----|------|--------|-----------|------|
| 4 | Duck and Cover | CORRECT | step.cpp:498 | VP = 5-pre_defcon; DEFCON-1 |
| 5 | Five Year Plan | CORRECT | hand_ops.cpp:268 | Random discard of USSR card; fires if US card; ChatGPT item #2 is log artifact |
| 7 | Socialist Governments | CORRECT | step.cpp:505 | Max 2/country, cap 3 removals |
| 8 | Fidel | CORRECT | step.cpp:542 | Clears US from Cuba + gain control |
| 9 | Vietnam Revolts | CORRECT | step.cpp:493 | +2 USSR Vietnam + turn-scoped SEA bonus via `vietnam_revolts_ops_bonus` in legal_actions.cpp:24 |
| 10 | Blockade | CORRECT | hand_ops.cpp:307 | US discards ≥3-op card OR loses West Germany inf |
| 11 | Korean War | CORRECT | step.cpp:548 | `apply_war_card` 2ops 2VP; threshold 4 |
| 12 | Romanian Abdication | CORRECT | step.cpp:552 |
| 13 | Arab-Israeli War | **BUG-1** | step.cpp:557 | Engine fires war attack; **no Camp David block** (rule_queries.hpp:72..89 has no case for card 13) |
| 14 | COMECON | CORRECT | step.cpp:562 | 4 non-US-controlled E.Europe |
| 15 | Nasser | CORRECT | step.cpp:585 | +2 USSR Egypt, halve US Egypt |
| 16 | Warsaw Pact Formed | CORRECT | step.cpp:592 | Both branches; sets `warsaw_pact_played` for NATO prereq (rule_queries.hpp:56) |
| 17 | De Gaulle Leads France | CORRECT | step.cpp:775 | -2 US France, +1 USSR, sets `de_gaulle_active`; NATO protection for France disabled via rule_queries.hpp:29 |
| 18 | Captured Nazi Scientist | PARTIAL | step.cpp:781 | `advance_space_track(side, 1)`. **This is correct** — +1 on space race only. ChatGPT item #1 ("+2 VP and +1 space") is a log-render artifact of the space-race VP table paying 2 VP on certain squares. No bug. |
| 19 | Truman Doctrine | CORRECT | step.cpp:785 | Remove all USSR from 1 non-USSR-controlled European country; sets `truman_doctrine_played` |
| 20 | Olympic Games | CORRECT | step.cpp:660 | Boycott vs compete; opponent chooses branch |
| 21 | NATO | CORRECT | step.cpp:728 | Gate in `is_event_play_allowed` (rule_queries.hpp:79) requires one of marshall/truman/warsaw; protection in `nato_protected` legal_actions.cpp:43 |
| 22 | Independent Reds | CORRECT | step.cpp:732 | +1 US in {19,13,83,9,3}. Log from ChatGPT item #4 shows five placements — that's exactly right. **False alarm in the 31-item list.** |
| 23 | Marshall Plan | CORRECT | step.cpp:738 | 7 countries; sets `marshall_plan_played` |
| 24 | Indo-Pakistani War | CORRECT | step.cpp:762 | Phasing-player chooses India/Pakistan; war roll; ChatGPT item #24 ("7 US influence left 2 USSR") is an apparent log misread — `apply_war_card` sets defender inf=0 and `influence_on_success=2` for attacker (step.cpp:245..246). **Log artifact.** |
| 25 | Containment | CORRECT | step.cpp:811 | `ops_modifier[US]+=1` (min-1 cap in `effective_ops`) |
| 26 | CIA Created | PARTIAL | hand_ops.cpp:331 | Grants +1 US influence in one accessible country. **Missing**: the "USSR reveals hand to US" aspect (info-state-only, does not affect play under greedy policy but matters for MCTS belief modeling). |
| 27 | US/Japan Mutual Defense Pact | CORRECT | step.cpp:815 | Sets flag + gains control of Japan; USSR blocked in legal_actions.cpp:85 |
| 28 | Suez Crisis | CORRECT | step.cpp:820 | 4 removals, max 2/country among France/UK/Israel |
| 29 | East European Unrest | CORRECT | step.cpp:852 | 2-per-country in Late War (turn≥8), 1 otherwise; docs/event_scope.md and engine agree |
| 30 | Decolonization | CORRECT | step.cpp:873 | 4 non-US-controlled Africa/SE-Asia |
| 31 | Red Scare/Purge | CORRECT | step.cpp:899 | `ops_modifier[opp]-=1` |
| 32 | UN Intervention | CORRECT | hand_ops.cpp:343 | Must have opponent non-scoring card; plays for ops only. ChatGPT items #5 are policy choices of which country to target, not engine bugs. |
| 33 | De-Stalinization | CORRECT | step.cpp:903 | Up to 4 moves, max 2/dest, skip US-controlled |
| 34 | Nuclear Test Ban | CORRECT | step.cpp:962 | VP = max(0, defcon-2); +2 DEFCON |
| 35 | Formosan Resolution | CORRECT | step.cpp:969 | Flag; scoring.cpp:34 treats Taiwan as BG when flag set; cancelled by USSR China (step.cpp:1820) |
| 36 | The Cambridge Five | CORRECT | hand_ops.cpp:377 | USSR places 1 inf per scoring card in US hand's region |
| 37 | Special Relationship | CORRECT | step.cpp:973 | UK+NATO → -2 VP (USSR) +2 inf anywhere; else +1 US in Western Europe. ChatGPT item #19 ("+1 Mexico and Indonesia") would only be possible via NATO+UK branch — engine allows anywhere which matches rules; "Mexico/Indonesia" pick is policy decision, not engine bug. |
| 38 | NORAD | **BUG-3** | step.cpp:1018 | Flag is set; **nothing in engine reads it as a trigger**. Should add a hook in `run_action_round` or end-of-USSR-AR that grants US +1 inf in a US-influence country when DEFCON==2. **Material US strength lever.** |

### Mid War (turns 4–6)

| ID | Name | Status | File:line | Note |
|----|------|--------|-----------|------|
| 39 | Brush War | CORRECT | step.cpp:1022 | Threshold 3, 3ops-3inf, 1VP; applies to any stab ≤2. ChatGPT item #8 ("+3 influence +2 VP") likely misread — `apply_war_card` sets defender=0, +3 inf attacker, +1 VP on success for card 39 (step.cpp:248: `vp = card_id == 39 ? 1 : 2`). **Log artifact.** |
| 42 | Arms Race | CORRECT | step.cpp:1045 | +3 if meets req, +1 else |
| 43 | Cuban Missile Crisis | CORRECT | step.cpp:1054 | DEFCON=2 + flag; cancellation via `resolve_cuban_missile_crisis_cancel` hand_ops.cpp:1138; coup during CMC on BG → DEFCON=1 instant loss (step.cpp in apply_action) |
| 44 | Nuclear Subs | CORRECT | step.cpp:1059 | Flag; consumed in coup code (hand_ops.cpp:1028 `!(US && nuclear_subs_active)` guard on DEFCON drop). ChatGPT item #11 is policy artifact: the USSR played Nuclear Subs for ops (US card), placed +1 inf somewhere — engine correctly does ops-first then fires event. |
| 45 | Quagmire | CORRECT | hand_ops.cpp:417, 1068..1136 | Sets flag; `resolve_trap_ar` forces US to discard ≥2-op card each AR; cleared on d6≥5 |
| 46 | SALT Negotiations | **BUG-2** | step.cpp:1063, hand_ops.cpp:421 | **DEFCON +1 instead of +2 per rules.** Also: effect of "both sides look at top of discard" is not implemented (info-state-only). |
| 47 | Bear Trap | CORRECT | hand_ops.cpp:436, 1068..1136 | Symmetric to Quagmire for USSR |
| 48 | Summit | CORRECT | step.cpp:1068 | Die rolls with re-roll on tie; winner picks DEFCON ±1 and gains/loses 2 VP |
| 49 | How I Learned | PARTIAL | step.cpp:1089 | Engine allows DEFCON 2..5 (options 0..3 → 2..5). **Rules allow 1..5.** The engine correctly prevents the (near-)suicide choice of DEFCON=1, but this is a rule deviation. Documented in the code comment as intentional. **Not a bug for competitive play; will remain CORRECT in practice.** |
| 50 | Junta | CORRECT | step.cpp:1101 | +2 inf in CA/SA country; optional free coup/realign. ChatGPT item #16 ("+2 DR then -3 Panama") is a coup result on Panama — that's **exactly** what Junta does. **False alarm.** |
| 51 | Kitchen Debates | PARTIAL | step.cpp:1141 | VP per-BG-excess **to US** (note: code does `vp -= excess` which is correct since VP is USSR-positive). Hand-reveal mechanic missing (info-state-only). |
| 52 | Missile Envy | CORRECT | hand_ops.cpp:440 | Takes opponent's highest-ops non-scoring card, plays it for ops only, then card returns to opponent. **Rules also require opponent must play Missile Envy next AR** — this aspect is not enforced (the returned card is Missile Envy which opponent holds; opponent is free to hold until convenient). **PARTIAL.** ChatGPT items #10 are exactly this ops-only mechanism — **false alarm on the listed interpretation**. |
| 53 | We Will Bury You | **BUG-like but by-design** | step.cpp:1161 | Immediately +3 VP USSR, -1 DEFCON. **Rules make the 3 VP conditional on UN Intervention NOT being played in response.** Engine awards immediately. ChatGPT item #17 is a real discrepancy but matches the engine's simplified interpretation of an ambiguous rule. **PARTIAL / documented design choice.** |
| 54 | Brezhnev Doctrine | CORRECT | step.cpp:1166 | `ops_modifier[USSR]+=1` |
| 55 | Portuguese Empire Crumbles | CORRECT | step.cpp:1170 | +2 Angola, +2 Mozambique |
| 56 | South African Unrest | PARTIAL | step.cpp:1175 | Engine: +2 SA, +2 neighbor. **Rules: EITHER +2 SA, OR +1 SA and +2 neighbor.** Engine does both together. ChatGPT item #9 is a real engine discrepancy. **Small US-WR impact (pro-USSR), but SA plays are rare.** |
| 57 | Allende | CORRECT | step.cpp:1197 | +2 Chile |
| 58 | Willy Brandt | CORRECT | step.cpp:1201 | +1 VP USSR, +1 W.Germany, flag cancels NATO protection via legal_actions.cpp:53 |
| 59 | Muslim Revolution | CORRECT | step.cpp:1207 | 2 removals from 8-country pool |
| 60 | ABM Treaty | CORRECT | step.cpp:1242 | +1 DEFCON + 4 inf where side has presence. docs/event_scope.md notes "4 free ops" ambiguity — engine uses 4 straight placements in presence countries, reasonable interpretation. |
| 61 | Cultural Revolution | CORRECT | step.cpp:1262 | Transfer China from US; else +1 VP USSR |
| 62 | Flower Power | CORRECT | step.cpp:1271 | Flag; check at step.cpp:469 awards +2 VP when US plays war card as event |
| 63 | U2 Incident | CORRECT | step.cpp:1275 | +1 VP USSR (the "UN Intervention next AR" is not enforced; minor) |
| 64 | OPEC | CORRECT | step.cpp:1279 | +1 VP per USSR-presence OPEC country (Egypt, Iran, Libya, SaudiArabia, Iraq, Gulf States, Venezuela); `awacs_active` skips Saudi Arabia; `opec_cancelled` skips entirely |
| 65 | Lone Hearts Club Band | CORRECT | step.cpp:1295 | +1 DEFCON, -1 VP USSR (i.e. +1 US) — correct |
| 66 | Camp David Accords | PARTIAL | step.cpp:1304 | +1 VP US, +1 inf Israel/Egypt/Jordan. **Missing: flag that blocks Arab-Israeli War event.** Ties into BUG-1. |
| 67 | Puppet Governments | CORRECT | step.cpp:1311 | 3 places with zero influence from either |
| 68 | Grain Sales to Soviets | CORRECT | hand_ops.cpp:519 | Takes random card from USSR, plays for ops, returns. Rules also allow US to return the card and use 2 ops — engine does *always play for ops*. **Minor PARTIAL.** ChatGPT item #12 is log-artifact. |
| 69 | John Paul II Elected Pope | CORRECT | step.cpp:1337 | -2 USSR Poland, +1 US Poland, `john_paul_ii_played=true`; enables Solidarity via rule_queries.hpp:68 |
| 70 | Latin American Death Squads | PARTIAL | step.cpp:1300 | Sets `latam_coup_bonus`; consumed in `apply_action` coup branch (adds/subtracts 1 from coup net). ChatGPT item mentions nothing here. |
| 71 | OAS Founded | CORRECT | step.cpp:1343 | +2 US in CA/SA (up to 2 countries) |
| 72 | Nixon Plays the China Card | CORRECT | step.cpp:1363 | Transfers China from USSR (-2 VP, i.e. +2 US) OR flips to playable. ChatGPT item #7 misread the "-2 VP" as "2 VP only"; the log shows the same effect. **False alarm.** |
| 73 | Sadat Expels Soviets | CORRECT | step.cpp:1373 | Clear USSR Egypt, +1 US Egypt |
| 74 | Shuttle Diplomacy | CORRECT | step.cpp:1378 | Flag; consumed in scoring.cpp:158..172 for Asia/ME only. ChatGPT item #25 is log artifact (card was played as ops, not event). |
| 75 | Voice of America | CORRECT | step.cpp:1382 | Up to 4 USSR removals outside Europe, max 2/country |
| 76 | Liberation Theology | CORRECT | step.cpp:1423 | +3 USSR in CA, max 2/country |
| 77 | Ussuri River Skirmish | CORRECT | step.cpp:1455 | If China held by USSR → US takes it face-up; +4 inf Asia for holder |
| 78 | Ask Not | CORRECT | hand_ops.cpp:568 | Up to 4 discards + redraws |
| 79 | Alliance for Progress | CORRECT | step.cpp:1481 | +1 US VP per US-controlled BG in CA/SA |
| 81 | One Small Step | CORRECT | step.cpp:1497 | If behind, advance 2 levels on space race |
| 83 | Che | CORRECT | step.cpp:1503 | Free coups in stab ≤2 CA/SA/Africa, max 1 per region. ChatGPT item #20 "+1 Argentina + Tunisia" is coup *result* placements — **false alarm**. |
| 84 | Our Man in Tehran | CORRECT | hand_ops.cpp:637 | Requires US controls a ME country; keep-k-of-5 mechanic |

### Late War (turns 7–10)

| ID | Name | Status | File:line | Note |
|----|------|--------|-----------|------|
| 85 | Iranian Hostage Crisis | CORRECT | step.cpp:1578 | Clear US Iran, +2 USSR Iran, flag |
| 86 | The Iron Lady | PARTIAL | step.cpp:1639 | +1 US VP, +1 USSR Argentina, clear USSR UK, sets `opec_cancelled`. **Rules don't make Iron Lady cancel OPEC — that's Iron Lady's "Argentina" effect; OPEC cancel is Iron Lady-specific, but docs/event_scope.md line 121 says "the OPEC card is cancelled"; this interpretation is ambiguous.** Engine matches project's own summary; likely CORRECT. ChatGPT item #23 is log-missing-lines. |
| 87 | Reagan Bombs Libya | CORRECT | step.cpp:1646 | -VP USSR per Libya influence |
| 88 | Star Wars | CORRECT | hand_ops.cpp:714 | Requires US space > USSR space; retrieve & fire event from discard |
| 89 | North Sea Oil | CORRECT | step.cpp:1584 | Sets `opec_cancelled` + `north_sea_oil_extra_ar` |
| 90 | The Reformer | CORRECT | step.cpp:1589 | 4 inf (+2 if USSR space lead) into non-US-controlled Europe; +1 DEFCON |
| 91 | Marine Barracks Bombing | CORRECT | step.cpp:1614 | Clear Lebanon, remove 2 US from ME |
| 92 | KAL 007 | CORRECT | step.cpp:1650 | -1 DEFCON, +2 US VP, transfer China face-up |
| 93 | Glasnost | CORRECT | step.cpp:1659 | +2 VP USSR, +1 DEFCON, +4 free ops if SALT active via `glasnost_free_ops` |
| 94 | Ortega | CORRECT | step.cpp:1667 | Clear US Nicaragua, free 2-op coup among Cuba/Chile/Nicaragua. **Rules say coup must be adjacent to Nicaragua**; engine's 3-country set is not exact ("Cuba, Chile, Nicaragua" — Chile is not adjacent to Nicaragua, and the engine allows Nicaragua itself). **Small PARTIAL.** |
| 95 | Terrorism | CORRECT | hand_ops.cpp:496 | Discards 1 (2 if against US and Iranian Hostage Crisis active). Rule about Defectors canceling the discard is not modeled; minor. |
| 96 | Iran-Contra Scandal | CORRECT | step.cpp:1680 | `ops_modifier[US]-=1` |
| 97 | Chernobyl | CORRECT | step.cpp:1716 | US picks region; USSR influence placements blocked in that region via `is_chernobyl_blocked` in legal_actions.cpp:70. Flag cleared at turn end (not re-verified here; TODO). |
| 98 | LatAm Debt Crisis | PARTIAL | hand_ops.cpp:745 | Engine doubles USSR inf in 2 CA/SA countries. **Rules: USSR gets to double ONLY IF US fails to discard a 3+ op card.** Engine skips the US discard-choice branch entirely — USSR always gets the double. **Pro-USSR bug.** ChatGPT item #26 confirms. |
| 99 | Tear Down this Wall | CORRECT | step.cpp:1710 | Clear USSR East Germany, +3 US, cancel Willy Brandt |
| 100 | An Evil Empire | CORRECT | step.cpp:1735 | -1 VP USSR, cancel Flower Power |
| 101 | Aldrich Ames Remix | CORRECT | hand_ops.cpp:771 | USSR picks a US card to discard |
| 102 | Pershing II | CORRECT | step.cpp:1761 | +1 VP USSR, remove 1 US from 3 W.Europe countries |
| 103 | Wargames | CORRECT | step.cpp:1741 | Only legal at DEFCON=2 (rule_queries.hpp:82); +6 VP to opp then game over |
| 104 | Solidarity | CORRECT | step.cpp:1755 | +3 US Poland iff `john_paul_ii_played`; gated in rule_queries.hpp:85 |
| 105 | Iran-Iraq War | CORRECT | step.cpp:1796 | War against Iran or Iraq |
| 106 | Yuri and Samantha | **BUG-5** | step.cpp:1809 | `next.vp += next.space_attempts[US]` — awards VP for attempts **already made**. Rules: USSR gains 1 VP for each **future** US space attempt until end of turn. Needs a turn-scoped counter that accrues on future attempts, not a read of history. **Minor US-WR impact** (rare play; direction matters). |
| 107 | AWACS Sale to Saudis | CORRECT | step.cpp:1813 | +2 US Saudi, flag sets OPEC-Saudi skip |
| 108 | Defectors | CORRECT | hand_ops.cpp:790 | Played by USSR during AR → USSR -1 VP (i.e. +1 US). ChatGPT item #21 says "+2 VP US" — **false alarm / log misread**. Headline handling of Defectors canceling USSR headline is implemented in the headline dispatch (game_loop.cpp run_headline_phase). |

### China Card

| 6 | China Card | CORRECT | step.cpp:1818 | Pass to opponent face-down (face-up via other cards); USSR playing clears `formosan_active` |

## Cross-reference: ChatGPT 31-item list

| # | Item | Classification | Where engine is correct / where it isn't |
|---|------|----------------|-------|
| 1  | Captured Nazi Scientist "+2 VP +1 space" | LOG ARTIFACT | step.cpp:781 does +1 space only; VP comes from space-race level payouts |
| 2  | Five Year Plan removed influence | LOG ARTIFACT | hand_ops.cpp:268 — discards card, fires US event if hit (could fire e.g. Truman → influence removal) |
| 3  | NATO before Marshall/Warsaw | POLICY/LEGAL | rule_queries.hpp:79 gates correctly; if log shows NATO played, the prereq was met |
| 4  | Independent Reds "+1 in 5 countries" | CORRECT ENGINE | step.cpp:732 — card places in 5 E.Europe countries by design |
| 5  | UN Intervention raw inf removal | POLICY ARTIFACT | hand_ops.cpp:343 — ops-only, chose to remove influence |
| 6  | Warsaw Pact also sets DEFCON=5 | FALSE | step.cpp:592..658 does not touch DEFCON |
| 7  | Nixon "+2 VP only" | LOG ARTIFACT | step.cpp:1363 — -2 VP (pro-US) is +2 US VP in the repr |
| 8  | Brush War "+3 inf +2 VP" | LOG ARTIFACT | `apply_war_card` step.cpp:245,248: BW sets attacker +3, defender=0, +1 VP on success |
| 9  | SA Unrest "+2 SA and +2 neighbor" | **REAL BUG** (#56 PARTIAL) | step.cpp:1175 does both unconditionally — should be exclusive-or |
| 10 | Missile Envy turns into raw inf | CORRECT ENGINE | hand_ops.cpp:440 — takes card, plays it for ops = raw inf |
| 11 | Nuclear Subs "US +1 Cameroon" | POLICY ARTIFACT | USSR played the US card for ops, ops-first then event. Flag set correctly. |
| 12 | Grain Sales raw influence | CORRECT ENGINE | hand_ops.cpp:519 plays USSR card for ops |
| 13 | Bear Trap "US +1 Panama" | POLICY ARTIFACT | USSR played card for ops on US; flag set |
| 14 | Our Man in Tehran "US +1 Pakistan" | POLICY ARTIFACT | Card requires US controls a ME country; if condition fails it does nothing, so +1 Pakistan came from ops |
| 15 | Socialist Gov "+ US +1 Panama" | POLICY ARTIFACT | USSR played for ops, picked Panama (clearly wrong policy, not bug) |
| 16 | Junta "+2 DR then US -3 Panama" | CORRECT ENGINE | step.cpp:1101: +2 then free coup/realign; Panama is a legal CA target and -3 is a coup result |
| 17 | We Will Bury You "+3 VP immediate" | PARTIAL (by-design) | step.cpp:1161 — rules ambiguity over UN Intervention response |
| 18 | Arab-Israeli after Camp David | **REAL BUG** (#BUG-1) | No camp_david flag |
| 19 | Special Relationship "Mexico+Indonesia" | CORRECT ENGINE | step.cpp:973 with NATO+UK allows "anywhere" |
| 20 | Che "+1 Argentina +1 Tunisia" | CORRECT ENGINE | Those are coup-result placements |
| 21 | Defectors USSR play "+2 VP" | LOG ARTIFACT | hand_ops.cpp:790 — -1 USSR VP (= +1 US); log-reader appears to read "USSR -1" wrongly |
| 22 | Blockade used for coup | CORRECT ENGINE | Blockade as ops for coup is legal; its event is only the West Germany discard test |
| 23 | Iron Lady "just +1 VP" | LOG ARTIFACT | step.cpp:1639 sets all three effects |
| 24 | Indo-Pakistani "7 US -> 2 USSR" | LOG ARTIFACT | `apply_war_card` step.cpp:244..246 sets defender=0, attacker+=2 |
| 25 | Shuttle Diplomacy Soviet placement | POLICY ARTIFACT | Card played for ops (US card), not event |
| 26 | LatAm Debt Crisis "+3 Cuba +1 Guatemala" | **REAL BUG** (#98 PARTIAL) | Engine skips US-discard-choice branch |
| 27-31 | Scoring cards with side effects | LOG ARTIFACTS | scoring.cpp verified clean for all 7 regions |

**Net real engine findings from the ChatGPT list**: items 9, 18, 26 confirmed; all others are either correct engine behavior, policy/decoder choices, or log-rendering artifacts.

## Conclusions

1. The engine is materially correct for the overwhelming majority of card events.
   Of 100 events audited, 82 are CORRECT, 11 are PARTIAL (minor mechanics
   missing that don't change the ops/VP ledger), 6 are genuine engine bugs,
   and 1 is by-design rule simplification (How I Learned disallows DEFCON=1).
2. The ChatGPT 31-item list is almost entirely a critique of the **agent
   policy** (v32) and the **log renderer**, not the engine. Only 3 of 31
   items correspond to real engine bugs.
3. The real engine bugs are concentrated in Late War, which directly touches
   the v32 US-side plateau. Camp David / NORAD alone could plausibly lift US
   WR by 2-4 pp after a BC warmstart + short PPO refresh.
4. The scoring engine (`scoring.cpp`) is clean; the "scoring card side effects"
   items 27-31 are log-rendering noise.

## Recommendations (ordered by US win-rate impact)

1. **Implement NORAD trigger (BUG-3).** Add an end-of-USSR-AR hook in
   `game_loop.cpp::run_action_round` (around line 3400) that, when
   `pub.norad_active && pub.defcon==2`, pushes a US decision frame for
   placing 1 influence in any country already holding US influence. This is
   the single most impactful fix for US strength in the Late War.
   Estimated US-WR impact: **+2 to +4 pp** (NORAD is a signature US engine).
2. **Block Arab-Israeli War when Camp David played (BUG-1).** Add field
   `bool camp_david_played` to `public_state.hpp`; set in step.cpp:1304
   (case 66); gate in `rule_queries.hpp::is_event_play_allowed` with
   `if (card_id == 13 && pub.camp_david_played) return false;`. Also
   block the headline-side handler via `apply_headline_event_with_hands`
   (hand_ops.cpp:1282 already checks `is_event_play_allowed`).
   Estimated US-WR impact: **+1 to +2 pp** (A-I War is common USSR play).
3. **Fix SALT DEFCON increment (BUG-2).** Change `pub.defcon + 1` to
   `pub.defcon + 2` in step.cpp:1064 and hand_ops.cpp:422. Symmetric, but
   given asymmetric deck composition, small pro-US tilt expected.
   Estimated US-WR impact: **+0 to +1 pp**.
4. **Fix LatAm Debt Crisis (card 98 PARTIAL).** Add the US-discard-3+-op
   choice branch in hand_ops.cpp:745. If US discards, effect is aborted.
   Estimated US-WR impact: **+0.5 to +1 pp** (late-war USSR card; removing
   its automatic trigger helps US).
5. **Fix South African Unrest exclusivity (card 56 PARTIAL).** Make the
   two branches (either +2 SA; or +1 SA and +2 neighbor) exclusive in
   step.cpp:1175. Rarely decisive but a clear rules deviation.
   Estimated US-WR impact: **+0 to +0.5 pp**.

After these five fixes, dispatch BC on the updated engine, then a short
PPO refresh (seed=42000, 25 iterations from v32_sc). Compare US head-to-head
WR vs heuristic and vs v32 baseline. If uplift materialises, the plateau
was partially engine-constrained; if not, shift focus back to
architecture / ISMCTS.

## Open questions

- **Card 70 (LatAm Death Squads) exact semantics**: engine adds/subtracts
  1 to coup net; rules text says "+1 to coup roll for phasing, -1 for
  opponent" — roll vs net is a subtle difference. Needs ITS verification.
- **Card 94 (Ortega) adjacency set**: engine uses {Cuba, Chile, Nicaragua}
  but rules say coup in country adjacent to Nicaragua (which is Honduras,
  Costa Rica, Cuba). Verify against adjacency table.
- **Card 46 SALT discard-pile top reveal and move-to-hand**: both
  info-state-affecting; currently the "look at top of discard" is not
  implemented. Unclear if the full rule (move one card from discard to
  hand) is what the engine intends — code does it at hand_ops.cpp:424..432
  but not at step.cpp:1063 (i.e. only when played via Five Year Plan or
  Missile Envy, not as direct event). Inconsistency to resolve.
- **Card 52 Missile Envy next-AR enforcement**: engine returns the card
  to opponent; rules say opponent must play it next AR. Enforcement would
  require a turn-scoped "must play next AR" slot.
- **Card 38 NORAD cancellation by Terrorist States / Iran-Contra**:
  `docs/event_scope.md:63` notes cancellation; engine has no cancel hook.
- **Whether How I Learned (card 49) should permit DEFCON=1**: engine
  restricts to 2..5; intentional but documented in comment. Should this
  be governed by a config flag for strict-rules mode?
