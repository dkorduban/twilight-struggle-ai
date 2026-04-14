# Opus Analysis: v266_sc RL Bootstrap Viability and Improvement Path
Date: 2026-04-14 UTC
Question: Does v266_sc play decent TS and can it bootstrap RL? How to improve? Action items for EventFirst log completeness.

## Executive Summary

v266_sc (Elo 1910) plays advanced-beginner to low-intermediate Twilight Struggle. It understands basic game structure (opening placements, scoring card timing, space race usage, regional targeting), and an expert-LLM review estimated it at roughly 1200-1450 human-equivalent. Despite numerous card-management errors (headlining NORAD/CIA Created, spacing Fidel/Cambridge Five, the US headlining Che/Ortega/The Reformer), the model is a viable RL bootstrap: it generates complete 10-turn games with no DEFCON suicides, no scoring-card-held losses, and enough strategic structure to reward gradient descent. The highest-leverage improvements are (1) reward shaping for intermediate milestones, (2) fixing the ISMCTS scoring_card_held bug for inference-time search, and (3) self-play loop changes (opponent mixing, temperature schedule). A separate but important finding is that 43 of 165 decision points (26%) use EventFirst (mode=5), and the log suppresses the influence placement that follows every one of them, making the log substantially incomplete for analysis.

## Findings

### 1. Game Quality Assessment

**Opening placements (Turn 1 AR0):**
- USSR places 1 Austria, 1 E. Germany, 4 Poland. This is a recognizable Poland-heavy setup, reasonable if unimaginative. Missing the standard Syria/Afghanistan early contestation.
- US places 4 Italy, 3 W. Germany. Solid and standard.
- Overall: sane but formulaic. No Asia contestation from either side.

**Headline selection:**
- Turn 1: US headlines NORAD (a permanent effect with no immediate value; wastes headline slot). USSR headlines CIA Created (gives the US a free look at USSR hand + free influence in Jordan). Both are poor headlines — a mid-level player would never headline either.
- Turn 2: US headlines Indo-Pakistani War (good, takes Pakistan). USSR headlines Captured Nazi Scientist (decent, advances space).
- Turn 3: USSR headlines Nuclear Test Ban (good). US headlines Indo-Pakistani War again (good).
- Turn 7: US headlines Che (terrible — gives USSR Peru, DEFCON pressure, and military ops when US is ahead).
- Turn 8: US headlines Ortega (gives USSR free coup in Nicaragua area).
- Turn 9: US headlines The Reformer (gives USSR 6 free influence in Europe — catastrophic).
- Turn 9: US also gives away Glasnost as EventFirst (gives USSR 2 VP).
- Verdict: **Headline quality is the single biggest weakness.** The US repeatedly headlines opponent cards that directly help the USSR.

**Scoring card handling:**
- All scoring cards are played before end-of-turn. No scoring_card_held losses. The engine's forced-play mechanism works correctly.
- Timing is sometimes good (Asia Scoring T3 for +7 after US built up), sometimes passive (scoring cards played on last possible AR).

**Coup/realignment targeting:**
- Very few coups in the entire game. US coups Algeria 3 times (Turn 2, Turn 3, Turn 4) — the first two succeed well, the third fails. Algeria reaches 20 US influence by endgame, which is absurd overinvestment.
- US coups India 4 times (Turns 5-7) — reasonable target but repetitive.
- USSR does almost no direct coups. Most military ops come through war card events.
- No realignments observed at all. This is a significant strategic gap — realignments are essential in human TS.

**Influence placement patterns:**
- **Algeria parking**: The US places influence in Algeria on almost every turn. By Turn 10, Algeria has [20][0] — twenty US influence in a non-battleground stability-2 country. This is a massive resource sink with zero strategic value past about 5 influence.
- **Taiwan fixation**: Both sides pour influence into Taiwan throughout the late game. By Turn 10 it reaches [9][8]. While Taiwan can matter (Formosan Resolution makes it a BG), this level of investment is disproportionate.
- **India oscillation**: India swings wildly. US builds it to [8][0], then Indo-Pakistani War strips it, US rebuilds, stripped again. Both sides understand India matters, but neither plays it efficiently.
- **Good placements**: USSR's Decolonization targets (Ethiopia, Philippines, Thailand, Malaysia) are reasonable. USSR's Liberation Theology targets (Cuba, Haiti, Nicaragua) are good. US placing in Colombia, Venezuela, Syria shows awareness of multiple regions.

**Space Race usage:**
- USSR: Cambridge Five to L2 (T1), Captured Nazi Scientist to L3 (T2), We Will Bury You to L4 (T4), Wargames to L5 (T8). Excellent space race progression — 4 successes in 5 attempts, all with good card choices.
- US: Olympic Games to L1 (T1), Bear Trap to L2 (T5). Only 2 levels total. Poor space race management.
- Verdict: USSR's space race play is arguably the best-played dimension of the whole game.

**EventFirst usage (mode=5):**
- 43 of 165 decisions use EventFirst. This is very high but architecturally appropriate — EventFirst is the correct mode when playing an opponent's card for ops while the event fires first.
- Some EventFirst plays are sensible: NATO EventFirst (T2, USSR) is the "fire a dead event for ops" pattern noted by the expert reviewer. Five Year Plan EventFirst is reasonable.
- However, we cannot evaluate the ops allocation quality because the log suppresses the influence targets. This is a critical gap.

**DEFCON management:**
- No DEFCON suicides. DEFCON only drops to 3 once (Turn 3 from a Marshall Plan coup, and Turn 7 from Olympic Games boycott).
- The model is conservative on DEFCON — very few battleground coups. This avoids suicide but also avoids the aggressive DEFCON play that stronger players use.

**USSR vs US balance:**
- USSR plays more coherently. Better space race, better regional diversity, better event usage (South African Unrest, Liberation Theology, Fidel, Junta, Allende, Indo-Pakistani War twice).
- US plays reactively, over-insures safe positions (Algeria, India, Taiwan), and makes devastating headline errors.
- Expert assessment: USSR at low-intermediate, US at advanced-beginner.

**Obviously crazy plays:**
- 20 influence in Algeria (absurd)
- Headlining NORAD (wastes headline)
- Headlining CIA Created (reveals hand to opponent)
- US headlining Che (gives USSR free coups when US is ahead)
- US headlining The Reformer (gives USSR 6 free European influence)
- US playing Glasnost as EventFirst (gives USSR 2VP + Glasnost effect)
- No realignments in the entire game
- Austria reaches [52][28] (unclear how — possibly accumulated from many small placements; suspect this may be a display bug)

### 2. RL Bootstrap Viability

**Is v266_sc good enough to generate useful self-play data for PPO?**

Yes, with caveats. The key positive indicators are:
- Complete 10-turn games with no terminal pathologies (no DEFCON suicide, no scoring_card_held)
- Basic strategic understanding: scoring cards get played, scoring regions get contested, space race is used
- Both sides generate reasonable game states (contested regions, VP swings, regional scoring dynamics)
- Elo 1910 against the 6-mode panel (v209_sc anchor at 1875) confirms it is the strongest model produced so far

**Failure modes that would pollute self-play training data:**
1. **Algeria parking echo chamber**: If both copies of the model agree that dumping influence in Algeria is good, PPO will reinforce this behavior. This is the most dangerous systematic bias.
2. **Headline poison**: The model frequently headlines opponent events that hurt itself. Self-play data from these games will contain many "free gift" turns that don't occur against competent opponents.
3. **No realignment games**: Self-play will never generate realignment data, so the model will never learn this tool exists.
4. **Taiwan/India fixation**: Excessive focus on 2-3 countries creates a narrow strategic vocabulary.
5. **EventFirst overuse**: 26% of actions are EventFirst. If the engine resolves these with a separate internal policy (not the NN), the NN never learns from the ops allocation feedback.

**Systematic biases:**
- Algeria parking: severe, will echo-chamber
- Taiwan/India fixation: moderate, will narrow strategic range
- No realignments: will self-reinforce (no data = no learning = no data)
- Headline quality: moderate risk — both sides make similar mistakes, so the "worst headline" player loses but the signal is noisy
- Conservative DEFCON play: will limit the model's ability to learn DEFCON-aggressive strategies

**Overall assessment:** v266_sc is a viable but imperfect bootstrap. It will produce training data that gradually improves basic play but risks converging to a narrow strategy dominated by Algeria/Taiwan/India influence races. Explicit countermeasures (opponent mixing, data filtering, reward shaping) are needed to broaden the strategic repertoire.

### 3. Improvement Techniques

Ranked by expected improvement per effort:

**1. Reward shaping (HIGH impact, MODERATE effort)**

The log reveals clear intermediate-quality problems that pure win/loss RL cannot efficiently address:

- **Scoring region control milestones**: Award intermediate reward for achieving Presence/Domination/Control in scoring regions. This directly counters the Algeria-parking problem by rewarding influence in countries that affect scoring.
- **Military ops compliance**: Penalize ending a turn short on military ops. The USSR misses milops on Turn 2 (giving away 4 VP) — this is a learnable mistake with the right reward signal.
- **Headline quality proxy**: Penalize headlining opponent events that have large positive effects for the opponent (e.g., The Reformer giving 6 USSR influence). This is harder to implement but high-value.
- **Scoring card timing urgency**: Reward playing scoring cards when the player has an advantage in that region, rather than just avoiding the end-of-turn penalty.
- **Influence efficiency**: Penalize placing influence in countries where you already have an overwhelming advantage (e.g., Algeria at 20).

**2. ISMCTS search at inference (HIGH impact, HIGH effort — blocked)**

The ISMCTS sweep showed that search is currently broken (97/100 scoring_card_held losses on v210_sc). Once fixed:
- Budget of 8 determinizations x 50-100 simulations should be the starting point
- Pre-fix results on older binaries showed 94.5% win rate with ISMCTS vs 60.5% raw on v210_sc — huge potential uplift
- ISMCTS would instantly fix headline quality (search would reject self-harmful headlines) and Algeria parking (search would see those ops yield no scoring improvement)
- **Blocker**: ISMCTS tree transition model does not simulate real AR/cleanup mechanics; EventFirst missing from draft space. Both bugs documented in ismcts_budget_sweep_20260414.md.

**3. Self-play loop changes (MODERATE impact, LOW effort)**

- **Opponent mixing (PFSP)**: Already implemented. Ensure the fixture pool includes diverse opponents, not just recent iterations. The current 6-mode-only pool (v262-v267) is too narrow.
- **Temperature schedule**: Current games appear to be greedy (T=0). Adding T=0.3-0.5 in early training iterations would increase exploration and break fixation patterns.
- **Data filtering**: Filter out games where Algeria influence exceeds 8 or where the winner headlined an opponent 4-ops card. This prevents the worst self-play artifacts from entering training.
- **Asymmetric training**: Filter US self-play data to wins only (per standing rule about TS asymmetry) to reduce training on US blunder games.

**4. Architecture changes (LOW impact for now)**

The log does not reveal obvious expressiveness limits. The model can represent complex multi-region strategies (the USSR's Turn 7-9 comeback through India/Africa/CA). The main problem is not "can't represent" but "hasn't learned" — which is a training signal problem, not an architecture problem.

One possible exception: the **country scoring head** may be too uniform. The Algeria parking suggests the country logits have a fixed bias toward certain countries rather than being state-conditional. Check whether the country head is attending to the current influence state or just using positional features.

**5. Data filtering (MODERATE impact, LOW effort)**

- Filter self-play games by quality metrics before training:
  - Discard games where either side parks >10 influence in any non-BG country
  - Discard games where the winner headlined 3+ opponent events
  - Weight games by length (full 10-turn games are more informative than Turn 1-2 blowouts)

### 4. EventFirst Log Completeness — Action Items

The problem has two parts:

**Part A: The Python callback returns empty targets for EventFirst (mode=5)**

In `scripts/run_traced_game.py`, the `_make_model_callback` function (line 465) handles target allocation only for mode 0 (Influence), 1 (Coup), and 2 (Realign). Mode 5 (EventFirst) falls through to the `else` branch at line 537 which returns `targets = []`.

However, this is actually correct behavior given the engine architecture. For EventFirst, the C++ engine handles the two-step process internally:
1. `apply_action_with_hands()` fires the event via `fire_event_with_state()` (hand_ops.cpp:755-756)
2. Then calls `execute_deferred_ops()` (hand_ops.cpp:761) which enumerates legal ops actions internally and uses a `PolicyCallbackFn` to choose among them

The Python callback in `play_traced_game_with_callback` is NOT the same as the C++ `PolicyCallbackFn` used by `execute_deferred_ops`. The deferred ops resolution uses the engine's internal policy mechanism, not the Python callback. So the influence targets are chosen by the engine, not by the model.

**Part B: The rendering code has no case for mode 5**

In `scripts/run_traced_game.py`, the `_rich_detail` function (line 132) handles modes 0-4 explicitly but has no branch for mode 5. When an EventFirst step is encountered, it skips the mode-specific detail block entirely. Only VP/milops/space changes are shown (from the generic code at lines 228-241).

However, the influence changes ARE capturable. The `_influence_diff_lines` function (line 93) computes diffs between pre and post state snapshots. For EventFirst, the post snapshot includes both the event effects AND the influence placement. The function just needs to be called for mode 5.

**Specific action items:**

**Item 1 (CRITICAL): Add mode 5 rendering in `_rich_detail`**
File: `scripts/run_traced_game.py`, line 132-241

After the `elif mode == _MODE_EVENT:` block (ending around line 218), add an explicit branch for EventFirst that shows both the event and the influence placement:

```python
elif mode == 5:  # EventFirst
    card_spec = cards.get(action.card_id)
    ops = card_spec.ops if card_spec else 1
    lines.append(f"  EventFirst: {_card_name(action.card_id, cards)} (event fires, then {ops} Ops influence):")
    lines.extend(_influence_diff_lines(pre, post, countries))
    if post["defcon"] < pre["defcon"]:
        lines.append(f"    DEFCON degrades to {post['defcon']}")
    elif post["defcon"] > pre["defcon"]:
        lines.append(f"    DEFCON improves to {post['defcon']}")
```

This will show all influence changes (event + ops combined) between pre and post snapshots. It won't separate "event effects" from "ops placement" but it will show the total board change, which is a vast improvement over showing nothing.

**Item 2 (IMPORTANT): Define `_MODE_EVENT_FIRST = 5` constant**
File: `scripts/run_traced_game.py`, line 33

Add `_MODE_EVENT_FIRST = 5` alongside the other mode constants. Currently only modes 0-4 have named constants. The `_mode_str` function at line 58 uses a literal `5` in its dict, which is fragile.

**Item 3 (NICE-TO-HAVE): Separate event effects from ops placement**

To fully disambiguate what the event did vs what the ops placement did, the engine would need to record an intermediate state snapshot (after event, before ops). This requires C++ changes:

File: `cpp/tscore/game_loop.hpp`, StepTrace struct (line 25)
- Add an optional `PublicState event_intermediate_snapshot` field

File: `cpp/tscore/hand_ops.cpp`, `apply_action_with_hands` (line 754-761)
- After `fire_event_with_state` returns and before `execute_deferred_ops`, snapshot `gs.pub` into the intermediate field

This is more invasive and can be deferred. Item 1 alone provides 80% of the value.

**Item 4 (NICE-TO-HAVE): Log the chosen deferred-ops action**

The `execute_deferred_ops` function (hand_ops.cpp:609) resolves the ops allocation internally. To surface the actual influence targets chosen:

File: `cpp/tscore/hand_ops.cpp`, line 645-648
- After `apply_action` returns, store the chosen `ops_actions[idx]` somewhere accessible (e.g., in the StepTrace or as a secondary trace entry)

File: `cpp/tscore/game_loop.cpp`, at each `trace_steps->push_back` call
- For EventFirst steps, also record the deferred ops action

This requires more significant refactoring and should be deferred until after Item 1 proves useful.

## Conclusions

1. **v266_sc plays recognizable, non-crazy Twilight Struggle** at an advanced-beginner to low-intermediate level (expert estimate: ~1200-1450 human equivalent). It understands game structure, scoring timing, space race, and regional targeting.

2. **v266_sc is viable as an RL bootstrap** but has systematic biases (Algeria parking, Taiwan fixation, terrible headline selection, zero realignments) that will echo-chamber into training without countermeasures.

3. **The biggest single weakness is headline/card-management quality.** The US side repeatedly headlines opponent events that give massive free value to the USSR (Che, The Reformer, Ortega, Glasnost). This is the #1 area where reward shaping or search would help.

4. **Algeria parking is the most dangerous training artifact.** 20 influence in a non-BG country is pure waste. If both self-play copies agree this is good, PPO will reinforce it. Explicit penalties or data filtering are needed.

5. **EventFirst actions account for 26% of all decisions** (43/165), and the log currently shows zero detail for any of them. This makes the log substantially incomplete for human analysis and debugging.

6. **ISMCTS is the highest-ceiling improvement** but is currently blocked by bugs (scoring_card_held in tree transitions, EventFirst missing from draft space). Raw greedy at 60.5% vs ISMCTS at 94.5% (pre-bug) shows the search uplift potential.

7. **Reward shaping is the best near-term investment**: scoring region milestones, milops compliance, headline quality proxy, and influence efficiency penalties would all directly address the observed weaknesses.

8. **The model plays USSR significantly better than US.** USSR has better space race play, better regional diversification, and fewer self-harmful event plays. US-side training may need additional attention.

## Recommendations

1. **Implement reward shaping for scoring region control milestones** — award intermediate reward when a player achieves/maintains Presence or Domination in a scoring region. This directly counters Algeria parking and Taiwan fixation by making influence in scoring-relevant countries more rewarding than influence in already-dominated non-BG countries.

2. **Fix the EventFirst log rendering** (Items 1-2 from Section 4) — this is a 15-minute code change that makes 26% of the game log readable. Essential for all future game analysis.

3. **Fix ISMCTS bugs** (scoring_card_held tree transition + EventFirst draft space) — once fixed, even low-budget ISMCTS at inference time would dramatically improve headline quality and influence allocation.

4. **Add temperature T=0.3-0.5 to early self-play iterations** — break the greedy fixation patterns (Algeria, Taiwan, India) by forcing exploration of different countries and strategies.

5. **Filter self-play training data** — discard games with >10 influence in any non-BG country, and down-weight games where the winner headlined 3+ opponent events.

6. **Add opponent mixing beyond the current narrow 6-mode pool** — include the heuristic opponent in the PFSP fixture pool to prevent echo-chamber convergence.

7. **Investigate the country scoring head** — the Algeria parking pattern suggests the country logits may have a learned fixed bias. Check whether country scores are properly state-conditional.

8. **Defer architecture changes** — the model's strategic vocabulary (multi-region pressure, scoring timing, space race) shows adequate representational capacity. The bottleneck is training signal quality, not architecture.

## Action Items: EventFirst Log Completeness

Priority order:

1. **[P0] `scripts/run_traced_game.py` line ~33**: Add `_MODE_EVENT_FIRST = 5` constant alongside existing mode constants.

2. **[P0] `scripts/run_traced_game.py` line ~218 (in `_rich_detail`)**: Add an `elif mode == _MODE_EVENT_FIRST:` branch that calls `_influence_diff_lines(pre, post, countries)` and reports DEFCON changes. This surfaces the combined event+ops influence changes for all 43 EventFirst plays in the log.

3. **[P0] `scripts/run_traced_game.py` line ~537 (in `_make_model_callback`)**: For mode 5, add the same influence target allocation as mode 0 (Influence). Currently EventFirst returns `targets=[]`, which means the Python callback doesn't tell the engine where to place influence. Instead, `execute_deferred_ops` in C++ resolves this internally. If the intent is for the model to control influence allocation on EventFirst plays, this needs to match the Influence path.

4. **[P1] `scripts/run_traced_game.py` line ~663 (`_format_target_summary`)**: Handle mode 5 the same as mode 0 for target display in the summary line.

5. **[P2] `cpp/tscore/game_loop.hpp` line ~25 (StepTrace)**: Add optional `PublicState post_event_snapshot` to allow disambiguating event effects from ops placement in EventFirst steps.

6. **[P2] `cpp/tscore/hand_ops.cpp` line ~755-761 (`apply_action_with_hands`)**: Snapshot `gs.pub` after `fire_event_with_state` returns and before `execute_deferred_ops`, storing it in the StepTrace.

## Open Questions

1. **Austria [52][28] anomaly**: The game log shows Austria reaching [52][28] by Turn 10. This seems impossible from normal play (ABM Treaty placed 1 USSR there, Missile Envy placed 1 more, and later 1 more). Is this a display bug, an accumulation error, or an engine issue? Needs investigation.

2. **EventFirst ops allocation policy**: When the C++ engine resolves `execute_deferred_ops`, which policy does it use? If it uses the Python callback (via `PolicyCallbackFn`), the model is choosing targets but they aren't logged. If it uses an internal heuristic, the model isn't learning from these decisions at all. This affects 26% of all game actions and needs clarification.

3. **Africa Scoring Turn 9 influence**: The Africa Scoring event on Turn 9 AR7 shows influence changes (USSR +1 Norway, USSR +2 Uruguay, USSR +1 Congo/Zaire) that should not be caused by a scoring card. Is this a coincidental cleanup/NORAD effect, or a bug?

4. **Milops penalty at end-of-turn**: The expert review mentions USSR missing milops on Turn 2 for 4 VP. The log shows "US gains 4 VP" at end of T2 (line 279). Confirm this is the milops penalty and not some other effect.

5. **ISMCTS fix timeline**: The ISMCTS bugs (scoring_card_held + EventFirst draft) are documented but not yet fixed. What is the estimated timeline for fixes? This determines whether to prioritize reward shaping (works now) or ISMCTS (higher ceiling but blocked).
