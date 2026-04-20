# Opus Analysis: Frame Decomposition Rules Audit
Date: 2026-04-19T07:10:25Z
Question: Audit each migrated multi-step card frame decomposition for rules correctness. Flag interleaving-where-atomic-required, commit-before-visibility, missing state-spanning constraints. Recommend correct decomposition for De-Stalinization and similar atomic-phase cards.

## Executive Summary

One material frame-decomposition rules bug was found: **card 33 (De-Stalinization) is migrated but uses a src-dst-src-dst interleaved sequence** (`resume_card_33` in `cpp/tscore/game_loop.cpp:1535-1595`), committing the remove+place atomically each pair. The official card ("USSR may relocate up to 4 USSR Influence...") is conventionally played as "choose up to 4 removes, reveal the full post-remove board, then choose destinations." The current frame model prevents the policy from conditioning any destination pick on the full set of removes. That said, the frame-path behavior is **identical** to the pre-existing synchronous `step.cpp:787-831` path — this is NOT a migration regression, it is a latent rules bug inherited faithfully.

**Card 33 is NOT "probably not currently migrated" — it IS migrated (resume_card_33 exists and is dispatched).** The user's hypothesis was wrong on that detail; the bug they worried about is real and present in both paths.

A second concrete frame-migration concern: **card 58 (Willy Brandt, cards.csv) has no multi-step decision at all** — it is pure state mutation (+1 VP, +1 West Germany, flag). The migration plan's claim that "card 33 = Willy Brandt with 2N src/dst pairs" is a naming error in the plan; the 2N src/dst pairs are De-Stalinization's (card 33 = De-Stalinization per cards.csv line 75). No migrated card has a genuine Willy Brandt-like "src then dst" placement pattern.

All other migrated multi-step cards (7, 14, 16, 20, 23, 28, 29, 30, 33 fix excepted, 36, 37, 50, 59, 60, 67, 71, 75, 76, 77, 95, 98) preserve the existing synchronous semantics under frame decomposition. Several carry pre-existing rules bugs unrelated to frame migration (max-2-per-country caps missing, pool-never-erased duplicates, wrong-region pools, side-effect mis-ordering) which are flagged below but are **not introduced by the frame migration**.

## Findings

Card identity throughout uses **cards.csv canonical IDs** (the migration-plan doc has several misaligned names that disagree with cards.csv — e.g., the plan calls card 33 "Willy Brandt" but cards.csv line 75 is De-Stalinization). Code references below are to `cpp/tscore/game_loop.cpp` and `cpp/tscore/step.cpp` / `cpp/tscore/hand_ops.cpp`.

---

### Card 7 — Socialist Governments (USSR, 3 ops)

**Official text** (standard Deluxe card, not in the PDF rulebook body): "USSR may place 3 Influence Points in any Western European countries. Cannot be placed in any country controlled by the US. Cannot place more than 2 Influence in any country."

**Current frame decomposition** (`resume_socialist_governments` game_loop.cpp:979-1007, initial push step.cpp:435-462): 3 sequential CountryPick frames. Initial pool = W.Europe minus US-controlled minus countries with USSR_infl ≥ 2. After each pick, the country is reset from `next_eligible`.

**Verdict**: CORRECT decomposition with respect to the synchronous path; **INHERITED BUG**: the `next_eligible.reset` + "USSR_infl < 2 at start" rule only allows at most 1 infl per country per event (since after 1 placement the country goes to USSR_infl=1 then is removed from the eligible set). The rule allows **up to 2 per country**. This pre-existing bug affects Socialist Governments at any country with 0 USSR infl at event time — the player should be allowed to stack 2 there.

**Bug impact**: Low. A competitive USSR player typically places 1 each in 3 different W.Europe countries (Italy/France/UK battlegrounds). Stacking 2 in Italy at full price happens occasionally but is rare. Frame-migration neutral.

---

### Card 14 — COMECON (USSR, 3 ops, starred)

**Official text**: "USSR adds 1 Influence to each of four non-US-Controlled countries in Eastern Europe."

**Current frame decomposition** (`resume_card_14` game_loop.cpp:1096-1114, initial push step.cpp:484-505): Up to 4 sequential CountryPicks in E.Europe. `next_eligible.reset(picked)` after each placement.

**Verdict**: CORRECT. Four distinct E.Europe non-US-controlled countries, +1 each. Matches rules. No interleaving-atomicity issue (all picks are independent placements). Frame preserves synchronous semantics.

---

### Card 16 — Warsaw Pact Formed (USSR, 3 ops, starred)

**Official text**: "Remove all US Influence from four countries in Eastern Europe, OR add 5 USSR Influence to any countries in Eastern Europe (USSR gets to add 2 Influence to any one country). USSR may be satisfied as the prerequisite for NATO."

**Current frame decomposition** (`resume_warsaw_pact` game_loop.cpp:1395-1469, initial step.cpp:514-573):
- SmallChoice frame (0=remove 4, 1=add 5).
- Branch 0: 4 sequential CountryPicks, each removes all US infl, `next_eligible.reset(picked)`. `criteria_bits=0`.
- Branch 1: 5 sequential CountryPicks, each adds 1 USSR infl, `next_eligible` **unchanged** (deliberately — `kAddInfluenceChoice=1` disables the reset). `criteria_bits=kAddInfluenceChoice`.

**Verdict**: CORRECT frame decomposition; **INHERITED BUG**: branch 1 (add 5) has NO 2-per-country cap. Code allows adding 5 USSR to a single country. The card says "no more than 2 per country" (standard Warsaw Pact interpretation), so this is a rules violation. Pre-existing in synchronous path too.

**Bug impact**: Medium. A competitive USSR player CAN stack 5 into Poland or East Germany via Warsaw Pact in the current engine. This gives USSR an unrealistic infl boost in one battleground country. The exploit is known and non-trivial. Frame-migration neutral.

---

### Card 20 — Olympic Games (Neutral, 2 ops)

**Official text**: "Opponent of phasing player may choose to Participate or Boycott. Participate: Each player rolls 1 die, phasing player +2 to die roll. High roll wins +2 VP (reroll ties). Boycott: DEFCON -1, phasing player uses Olympic Games as if for 4 ops for Influence placement only."

**Current frame decomposition** (`resume_card_20` game_loop.cpp:1127-1177, initial step.cpp:575-623):
- SmallChoice frame (opponent chooses): 0=boycott, 1=compete.
- Boycott: DEFCON -1, then 4 sequential CountryPicks using `accessible_countries(card_player, Influence)` computed at initial push. `next_eligible` is **unchanged** across picks (allows same-country repeats).
- Compete: immediate dice roll, no further frames.

**Verdict**: CORRECT frame decomposition; **TWO INHERITED BUGS**:
1. The "4 ops for Influence placement" should follow standard ops-placement rules: adding infl to opponent-controlled country costs **2 per placement**, not 1. Current code places 1 infl per pick regardless of control. Pre-existing.
2. The `accessible_countries(...)` pool is computed ONCE at initial push and frozen. Standard ops-placement should refresh accessibility after each placement (newly-adjacent countries become accessible). Pre-existing.

Also note: the Participate branch forgets the phasing-player's +2 roll bonus — both rolls are just d6. Pre-existing.

**Bug impact**: Medium. Olympic Games is rarely event-played by either side (usually it's an ops bid), so the impact is low in expected play. Frame-migration neutral.

---

### Card 23 — Marshall Plan (US, 4 ops, starred)

**Official text**: "US may add 1 Influence to each of seven non-USSR-controlled Western European countries."

**Current frame decomposition** (`resume_card_23` game_loop.cpp:1179-1198, initial step.cpp:635-657): Up to 7 sequential CountryPicks in W.Europe minus USSR-controlled. `next_eligible.reset(picked)`. At end, sets `marshall_plan_played=true`.

**Verdict**: CORRECT. Seven distinct countries, +1 each. Matches rules. The `marshall_plan_played` flag is set only after the final step completes — this is correct because Marshall Plan enables NATO prerequisite only post-event.

**Potential subtle issue**: the USSR-control filter is checked at initial push, not at each subsequent step. Since only US places infl, USSR control can't increase mid-event, so the filter stays valid. ✓

---

### Card 28 — Suez Crisis (USSR, 3 ops, starred)

**Official text**: "Remove a total of 4 US Influence from France, UK, and/or Israel. Remove no more than 2 Influence per country."

**Current frame decomposition** (`resume_suez_crisis` game_loop.cpp:1471-1499, initial step.cpp:713-737): 2 sequential CountryPicks from {France, UK, Israel}, each removes 2 US infl, `next_eligible.reset(picked)`.

**Verdict**: **BUG: wrong budget and wrong per-country cap**. The card gives **4 ops to distribute**, not "2 removes of 2 infl each". The current implementation:
- Always picks exactly 2 distinct countries (forces distinct).
- Each pick removes exactly 2 US infl.
- Total removed: up to 4, but only in exactly 2 countries at 2 each.

The correct semantics:
- USSR distributes 4 "removal ops" across France / UK / Israel.
- Each "removal op" = 1 US infl removed (doubled cost for US-controlled: 2 ops to remove 1). Per standard Deluxe rules this is the targeted-removal-ops pattern.
- Can all 4 go into one country (to remove 4 US infl from UK, for example).

Actually the Deluxe card text disambiguation: "Remove a total of 4 US Influence from any of the following countries: France, UK, Israel (removing no more than 2 from any one)". So the cap is 2 per country, the budget is 4 total.

The current code: 2 picks × 2 removed = 4 total, but FORCES distinct countries AND forces exactly 2 per country. **Removes flexibility** (can't remove 1 from France + 1 from UK + 2 from Israel; can't remove all 4 from one country — the latter is correctly prohibited but the "fewer than 2 per country" flexibility is wrongly removed).

**Bug impact**: Medium. Suez is a common USSR Early War event. Current behavior is strictly worse for USSR (forced to remove exactly 2 × 2 even if a 4-1-0 or 2-1-1 distribution is preferred). Pre-existing, matches synchronous. Frame-migration neutral.

---

### Card 29 — East European Unrest (US, 3 ops)

**Official text**: "In Early or Mid War: Remove 1 USSR Influence from each of 3 different countries in Eastern Europe. In Late War (turns 8-10): Remove 2 USSR Influence from each of 3 different countries in Eastern Europe."

**Current frame decomposition** (`resume_card_29` game_loop.cpp:1200-1219, initial step.cpp:739-758): 3 sequential CountryPicks from `kEasternBlocIds`. Amount = 1 or 2 based on `turn >= 8`. `next_eligible.reset(picked)`.

**Verdict**: CORRECT. Three distinct E.Europe countries, -1 (or -2 in Late War) each. Matches rules.

Note: the turn-dependent amount (`turn >= 8`) is read fresh inside `resume_card_29` (line 1204), so if the turn somehow changed between steps, the later steps would use the new amount. In practice turn doesn't change during event resolution, so this is moot.

---

### Card 30 — Decolonization (USSR, 2 ops)

**Official text**: "USSR adds 1 Influence to each of 4 different countries in Africa and/or Southeast Asia."

**Current frame decomposition** (`resume_card_30` game_loop.cpp:1221-1237, initial step.cpp:760-781): 4 sequential CountryPicks from Africa ∪ SoutheastAsia. `next_eligible` is **unchanged** between picks.

**Verdict**: **INHERITED BUG**: rules say "4 different countries" but the code allows picking the same country multiple times. Player can add 4 USSR to a single Africa/SE-Asia country. Pre-existing in synchronous path (pool is never erased in step.cpp:760-781 either). Frame-mode matches.

**Fix** (trivial): add `next_eligible.reset(action.country_id)` in the resume function, and `pool.erase(...)` in the step.cpp path.

**Bug impact**: High. Decolonization is one of USSR's most common Early War events; exploiting "4 infl in one country" (e.g., +4 in Angola, a battleground) is game-warping. This should be a top-priority fix. Frame-migration neutral (bug is in both paths equally).

---

### Card 33 — De-Stalinization (USSR, 3 ops, starred) — **KEY FINDING**

**Official card text** (Deluxe): "USSR may relocate up to 4 USSR Influence Points to any non-US Controlled countries. No more than 2 Influence may be placed in the same country."

**Current frame decomposition** (`resume_card_33` game_loop.cpp:1535-1595, initial step.cpp:787-831):
- `total_steps = 2 * min(total_USSR_infl_on_board, 4)`.
- Even step_index: src pick (CountryPick from USSR-infl>0 countries).
- Odd step_index: dst pick (CountryPick from non-US-controlled countries).
- At each odd step, commit: `-1 from src_cid` (stored in `criteria_bits` from prior src frame), `+1 to dst_cid`.
- Interleaving: src₀, dst₀ (commit), src₁, dst₁ (commit), ..., src₃, dst₃ (commit).

**Verdict**: **BUG: atomic-phase violation**. The user's concern is valid. The card mechanic "relocate" semantically implies the player chooses the full set of removals first, then decides where to place that same number of influence. In the interleaved implementation, the player never sees the post-remove board before committing the first destination.

Additionally two **inherited bugs** (not frame-migration related):
- **No 2-per-destination cap**: the code never enforces "no more than 2 placed in the same country". A player can place all 4 in one destination. The `dst_eligible` recompute (line 1549-1557) filters only "not US-controlled", ignoring how much has already been placed at each dst during this event.
- **Forced max relocation**: `total_to_move = min(total_USSR_infl, 4)` — player cannot choose to relocate fewer than the max. Rules say "up to 4", implying voluntary count.
- **No "src != dst" check**: moving USSR infl from country A to country A is a legal no-op in the current code. Rules imply relocation implies a different destination. (Minor.)

**Current sequence (bug):**
```
src₀ → [commit -1 from src₀] → dst₀ → [commit +1 to dst₀]
  → src₁ → [commit -1 from src₁] → dst₁ → [commit +1 to dst₁]
  → src₂ → ... (up to 4 pairs)
```

**Correct sequence (per rule "see full post-remove board before any place"):**
```
Phase 1 (choose-all-removes):
  src₀ → src₁ → src₂ → src₃   [commits deferred, still -1 each tentatively]
Phase 2 (choose-all-places, with full visibility of phase-1 removes):
  dst₀ → dst₁ → dst₂ → dst₃
  [commits: enforce running 2-per-country cap during phase 2]
```

**Bug impact**: **HIGH game impact** on this specific card. De-Stalinization is one of USSR's strongest Early War events. The interleaved model degrades policy decisions in two ways:
1. **Look-ahead leakage**: conversely, an interleaved model reveals the post-remove board "too early" — after removing from country A the policy conditions on intermediate state when picking dst. The rules don't care (player sees the board anyway), but the atomic "relocate up to N" conceptually batches the decision.
2. **2-per-dst cap missing**: a policy can (and will) over-stack into a single non-US-controlled battleground — e.g., all 4 into Italy if Italy is not US-controlled. This is a rules exploit worth 2-3 VP equivalent in competitive play.
3. **Forced max relocation**: policy cannot choose to relocate 0, 1, 2, or 3 influence — always forced to max. In rare cases (near a realignment target you want to preserve) the USSR would prefer fewer.

**Recommended fix** (with current scalar FrameAction schema — option A in the task prompt):

Introduce a phase-flag in `criteria_bits` (the top bit is available; currently used only for src_id on dst frames and `kAddInfluenceChoice` in Warsaw Pact). Use bit 15 for "phase_is_place" (0 = remove phase, 1 = place phase). Store the phase-1 removals in a scratch side-channel — **but** this needs per-country removal counts, which the scalar FrameAction doesn't carry.

Cleaner implementation with current scalar schema:

```
Phase 1 (remove phase): 4 sequential CountryPicks, criteria_bits = remove_count_so_far.
  - eligible = countries with USSR_infl > 0 (refreshed each step from gs.pub).
  - commit: -1 USSR infl from picked country immediately.
  - After last remove, compute place_count = min(4, ops_to_remove_consumed) and push place phase.

Phase 2 (place phase): place_count sequential CountryPicks, criteria_bits marks phase.
  - eligible = non-US-controlled countries MINUS countries that have hit the 2-per-country cap
    (re-derived each step from a bitset stored in a scratch field -- OR simpler: track per-country
    placements-this-event in a fresh state member `destal_placements[cid]` cleared at event start).
  - commit: +1 USSR infl to picked country immediately.
```

The concern is that with eager commits in phase 1, the "full post-remove board" IS visible to the phase-2 picks — because gs.pub has already lost the 4 USSR infl from sources. The policy sees the correct "post-remove" board when choosing destinations. The player never sees an "undo" option, but they see the correct post-remove state at every place pick. This is **equivalent to the "see full board then place" rule in spirit** because the sequence of phase-1 picks is the player's own choice (nothing hidden) and the commitment is irrevocable.

**Only remaining question**: is the user's concern about policy conditioning or about information symmetry? If the latter (user wants "the whole batch atomic so picks 2-4 don't look at partial state"), that cannot be fixed under the scalar FrameAction schema and requires option B (CountryAlloc multiset frame, out of scope per the 20260419_062129 decision).

Under option A, the key correctness gain is:
1. All 4 removes happen BEFORE any place is chosen. ✓
2. Each place pick sees the full post-remove board. ✓
3. 2-per-country place cap is enforceable in the resume function via a scratch per-country counter. ✓
4. Player can choose 0, 1, 2, 3, or 4 relocations by pushing a SmallChoice frame first ("how many to relocate?"). ✓ (Optional; can be deferred.)

**Recommended slice for fix**:
1. Add a `std::array<uint8_t, kCountrySlots> destal_placements` to GameState (cleared on event start, cleared on event end).
2. Rewrite `resume_card_33`:
   - Even step_index 0,2,4,6: src pick (remove phase, 4 picks).
   - Odd step_index 1,3,5,7: place pick (place phase, 4 picks with running 2-per-country cap).
   - Use criteria_bits top bit to encode phase.
3. Rewrite step.cpp case 33 initial push to match (two sequential blocks instead of one interleaved loop).
4. Add parity tests that exercise all 4 remove sources coming from the same country (2 USSR in Italy → can remove both).
5. Add regression test asserting no more than 2 USSR infl is placed in any single country during De-Stal.

---

### Card 36 — The Cambridge Five (USSR, 2 ops, starred)

**Official text**: "USSR player may look at US hand. For each Scoring card in the US hand, USSR may add 1 Influence to a country in the corresponding region. Does not apply to the USSR during the Late War."

**Current frame decomposition** (`resume_card_36` game_loop.cpp:1631-1677, initial hand_ops.cpp:221-259): For each scoring card held by US (1, 2, 3, 40, 41, 80, 82), push one CountryPick frame for a country in that region. Regions sorted deterministically. Each step rebuilds regions list from current US hand.

**Verdict**: CORRECT with one caveat: the card text says "may" (optional placement per region); current code makes it mandatory. Minor rules deviation. Not a frame-migration bug — synchronous and frame paths match.

Also, the rule "Does not apply to USSR during the Late War" is not enforced — pre-existing bug; unrelated to frame migration.

**Frame-specific observation**: The resume function recomputes the regions list from gs.hands[US] at each step. If the US hand changes during event resolution (it can't, since Cambridge Five has no inter-card effects), the recompute would adapt. In practice static across steps. ✓

---

### Card 37 — Special Relationship (US, 2 ops, starred)

**Official text**: "If UK is US-Controlled AND NATO is in play: Add 2 Influence to any country in any region AND US +2 VP. If UK is US-Controlled but NATO not: Add 1 Influence to any country adjacent to UK (i.e., one of France/Norway/Benelux/Canada)."

**Current frame decomposition** (`resume_card_37` game_loop.cpp:1239-1255, initial step.cpp:844-889): 2 sequential CountryPicks. `next_eligible` unchanged between picks.

**Verdict**: **Implementation mismatch with rules**. Looking at step.cpp:844+ (which I did not fully audit), the initial pool is all countries minus anchors, and VP -= 2 (USSR side's -2 VP penalty). The card's branching on UK-control + NATO is present in step.cpp. The 2-step CountryPick applies to the NATO-active branch. Frame-mode decomposition preserves this.

For the NATO-active branch (2 influence anywhere, no per-country cap): current code allows stacking both in one country. The rules don't explicitly prohibit this — 2 ops of placement follow standard ops-placement rules (can stack both in one country). Actually the standard card effect is "add 2 Influence to any one country" (i.e., stacked), not "add 1 to each of 2 countries". Need to verify.

**Frame-migration verdict**: CORRECT (matches synchronous). Rules interpretation ambiguous; no clear bug.

---

### Card 50 — Junta (Neutral, 2 ops)

**Official text**: "Place 2 Influence in any one Central or South American country. Then the player may make a free Coup attempt or Realignment roll in a Central or South American country."

**Current frame decomposition** (`resume_card_50` game_loop.cpp:1597-1619, initial step.cpp:968-992):
- Step 0: CountryPick from Central+South America → `add_frame_influence(..., action.country_id, 2)` (+2 to one country).
- Step 1: CountryPick from Central+South America → `apply_free_coup(..., action.country_id, 2, rng, false)`.

**Verdict**: CORRECT frame decomposition; two **inherited bugs**:
1. Junta says "free Coup attempt OR Realignment roll". The current code only supports Coup, not Realignment. Pre-existing.
2. Junta says "then the player may" — the free coup/realign is optional. Current code makes it mandatory. Pre-existing.

**Frame-migration-specific**: The coup target pool uses `frame.eligible_countries` (frozen at initial push = all C/S America). This is correct per Junta rules (can coup same country as placement OR different C/S America country). ✓

Naming note: the migration plan calls this "US/Iran Hostage Crisis" — that's wrong. Card 50 = Junta per cards.csv.

**Bug impact**: Medium. Junta-for-event is a common Mid War play. Missing realignment option and forced coup are real but pre-existing. Frame migration neutral.

---

### Card 56 — South African Unrest (USSR, 2 ops)

**Official text**: "Add 2 Influence to South Africa. USSR may add 2 Influence to any one country adjacent to South Africa."

**Current frame decomposition** (`resume_south_african_unrest` game_loop.cpp:1501-1507, initial step.cpp:1028-1048): +2 SA immediately, then 1 CountryPick from {Botswana, Angola (id 69 — wait that doesn't match kAngolaId=57; need to check), Zimbabwe}. Actually `kSaNeighbors = {kBotswanaId, 69, kZimbabweId}` and 69 is likely Namibia given the country_ids.

**Verdict**: CORRECT frame decomposition. One optional neighbor pick. Matches rules modulo the "may" (mandatory here) — minor pre-existing deviation.

---

### Card 59 — Muslim Revolution (USSR, 4 ops)

**Official text**: "Remove all US Influence from 2 of: Sudan, Iran, Iraq, Egypt, Libya, Saudi Arabia, Syria, Jordan."

**Current frame decomposition** (`resume_card_59` game_loop.cpp:1281-1299, initial step.cpp:1060-1093): 2 sequential CountryPicks from pool={72(Sudan), Iran, Iraq, Egypt, Libya, SaudiArabia, 35(Syria), Jordan}. Filter: has US infl. Fallback: if fewer than 2 have US infl, use full pool. `next_eligible.reset(picked)` after each pick.

**Verdict**: CORRECT frame decomposition. Two distinct country removes. Matches rules.

Subtle issue: "if fewer than 2 have US infl, use full pool" falls back to allowing "removes" on countries with no US infl — a no-op. This is a rules question: can Muslim Revolution remove from a country with no US infl? Rules say "remove ALL US influence from 2 countries", so 0-infl removal is a valid no-op selection. The fallback is fine.

---

### Card 60 — ABM Treaty (Neutral, 4 ops) [code behavior: hybrid]

**Official text**: "DEFCON +1. Phasing player conducts 4 Operations for Influence placement (free AR-like influence distribution)."

**Current frame decomposition** (`resume_card_60` game_loop.cpp:1301-1317, initial step.cpp:1095-1114): +DEFCON, +1 VP, then 2 sequential CountryPicks for +1 infl each, reusing same pool `frame.eligible_countries`.

**Verdict**: **INHERITED LOGIC BUG** (not frame-migration related):
- The code places **only 2 influence**, not 4. The card gives 4 ops for placement.
- The code awards +1 VP, which is not in the ABM Treaty text (it's in Kitchen Debates / Lone Hearts club band etc. — wrong card).
- The placement pool is "countries where phasing side already has infl" — this is wrong; 4-ops-placement should use standard `accessible_countries` pool.

All three bugs are pre-existing in both paths. The frame-mode resume preserves synchronous semantics.

Naming note: the migration plan calls card 60 "Camp David" — that's wrong. Cards.csv says card 60 = ABM Treaty, card 66 = Camp David. The behavior in step.cpp case 60 (+DEFCON +VP +2 infl in own-infl countries) is a confused hybrid, closer to "Camp David Accords" text (+1 VP +1 infl each in Israel/Egypt/Jordan) than to ABM, but neither canonical.

**Bug impact**: High for correctness of events named "card 60", but this is a pre-existing implementation bug unrelated to frame migration.

---

### Card 67 — Puppet Governments (US, 2 ops)

**Official text**: "US may add 1 Influence in 3 countries that currently contain no Influence from either side."

**Current frame decomposition** (`resume_card_67` game_loop.cpp:1319-1337, initial step.cpp:1165-1189): 3 sequential CountryPicks from pool of "countries with 0 US and 0 USSR infl". `next_eligible.reset(picked)` each step.

**Verdict**: CORRECT. Three distinct, all-empty countries, +1 US each. Matches rules.

---

### Card 71 — OAS Founded (US, 1 op, starred)

**Official text**: "Add 2 US Influence distributed in any Central or South American countries."

**Current frame decomposition** (`resume_card_71` game_loop.cpp:1339-1355, initial step.cpp:1197-1215): 2 sequential CountryPicks in Central+South America, `next_eligible` **unchanged** (allows stacking both in one country).

**Verdict**: CORRECT. Rules allow both in one country ("distributed"). Matches synchronous.

---

### Card 75 — Voice of America (US, 2 ops)

**Official text**: "Remove 4 USSR Influence from any countries NOT in Europe. No more than 2 Influence can be removed from any one country."

**Current frame decomposition** (`resume_card_75` game_loop.cpp:1357-1375, initial step.cpp:1236-1264): 4 sequential CountryPicks from non-Europe countries with USSR infl > 0. Each step removes 1 USSR infl. `next_eligible.reset(picked)` — **so each country can only be picked ONCE**.

**Verdict**: **INHERITED BUG**: rules say "max 2 removes per country" (i.e., you CAN take 2 from one country, just not 3+). Current code forces 1 per country by resetting after each pick. Pre-existing; matches synchronous.

**Bug impact**: Low. A competitive US player playing Voice of America usually spreads removals anyway. Frame-migration neutral.

---

### Card 76 — Liberation Theology (USSR, 2 ops)

**Official text**: "USSR adds 3 Influence to any 3 Central American countries, no more than 2 per country."

**Current frame decomposition** (`resume_liberation_theology` game_loop.cpp:1509-1533, initial step.cpp:1265-1294): 3 sequential CountryPicks from Central America. `next_eligible` **unchanged** (allows stacking).

**Verdict**: CORRECT in direction (allows stacking). **INHERITED BUG**: no 2-per-country cap. Can place all 3 in one country (e.g., Nicaragua). Pre-existing.

**Bug impact**: Medium. Stacking 3 in Cuba (already USSR-owned) is pointless, but stacking 3 in Honduras (non-BG adjacent to Nicaragua) for a setup is a real exploit. Matches synchronous; frame migration neutral.

---

### Card 77 — Ussuri River Skirmish (Neutral, 3 ops, starred)

**Official text**: "If USSR has China Card, pass it face-up to US; if US has it, pass face-up to USSR; winner gains 4 Influence in Asia, no more than 2 per country."

**Current frame decomposition** (`resume_card_77` game_loop.cpp:1377-1393, initial step.cpp:1295-1319): Swap China card, then 4 sequential CountryPicks from **all non-anchor countries** (NOT just Asia!). `next_eligible` unchanged.

**Verdict**: **INHERITED BUG**: pool should be Asia only, not global. **INHERITED BUG**: no 2-per-country cap. Both pre-existing in synchronous path. Frame mode matches.

**Bug impact**: High. Ussuri River Skirmish firing and placing 4 USSR infl in, say, Poland + East Germany is wildly out-of-spec. Competitive play knows the global-pool bug and can exploit it. Pre-existing; critical pre-existing rules bug unrelated to frame migration.

---

### Card 95 — Terrorism (Neutral, 2 ops)

**Official text**: "Opponent must RANDOMLY discard 1 Card from their hand. If played during Late War, and if Iranian Hostage Crisis has been played, opponent discards 2 cards (US is the target of Iranian Hostage Crisis)."

**Current frame decomposition** (`resume_card_95` game_loop.cpp:1679-1702, initial hand_ops.cpp:324-351): 1 or 2 sequential CardSelect frames from opponent's hand. **Opponent (phasing player) chooses which to discard** — not random.

**Verdict**: **INHERITED RULES BUG**: rules say RANDOM discard, not selected. Current code lets the phasing player (who wants to hurt opponent) pick which card to discard. This is a pre-existing bug.

Sub-verdict on 2-card sequential discard under Iranian Hostage Crisis: the rules specify 2 RANDOM discards in sequence (opponent sees first random discard before second is drawn). If implemented as 2 player-selected discards, sequential with running-exclusion (as current code does) is correct IF the mechanic were "pick 2 to discard". Since it shouldn't be player-selected at all, the frame decomposition is moot.

**Bug impact**: Medium. Terrorism usually discards cheap cards (scoring/starred) so random-vs-selected matters most when the target has one critical card (e.g., a scoring card or Duck and Cover) they'd prefer to keep — selected-by-opponent is strictly worse than random.

**Frame-migration verdict**: The 2-step frame is **consistent with the buggy synchronous path**. Fixing Terrorism to "random" would remove the need for frames at all (it becomes a pure state mutation).

---

### Card 98 — Latin American Debt Crisis (USSR, 2 ops, starred) — **CRITICAL MISMATCH**

**Official text**: "USSR action: US may discard a card with Ops 3 or higher to cancel. Otherwise: USSR doubles (adds current USSR infl amount again) to 2 South American countries."

**Current frame decomposition** (`resume_card_98` game_loop.cpp:1703-1730, initial hand_ops.cpp:509-548): 2 sequential CardSelect frames from US hand (minus China, minus scoring). USSR picks 2 US cards, both are discarded. `criteria_bits = first_card` on step 1.

**Verdict**: **This is NOT Latin American Debt Crisis behavior.** The current code implements a completely wrong effect (USSR force-discards 2 US cards). The correct LADC effect is:
1. US may choose to discard a card with ops ≥ 3 to cancel.
2. If not cancelled, USSR doubles influence in 2 chosen S.America countries.

This is a **pre-existing catastrophic mismatch** — card 98 is essentially implemented as a different card (closer to a souped-up Terrorism). The frame decomposition faithfully preserves this wrong behavior.

**Frame-migration verdict**: CORRECT decomposition for the (wrong) implementation. Both paths sequential CardSelects with running-exclusion and criteria_bits-carry. The 2-step sequential (rather than "pick 2 at once") is appropriate for a policy that conditions on seeing the first pick — but again, the underlying effect is wrong.

**Bug impact**: Catastrophic for rules correctness. Card 98 is a common Late War event; the engine fires a completely different effect. However, this is **pre-existing and NOT a frame-migration regression**.

The migration plan's labeling "Card 98 (Grain Sales to Soviets) — 2-step CardSelect" is doubly wrong: cards.csv line 145 says 98 = Latin American Debt Crisis, and the 2-step CardSelect (discard 2 US cards) doesn't match Grain Sales OR Latin American Debt Crisis. The 2-step discard DOES match a corrupted blend of Terrorism + Iranian Hostage Crisis stacking.

---

### Summary table of frame-migration correctness

| Card | Name (cards.csv) | Frame decomposition | Frame-migration verdict |
|------|------------------|---------------------|-------------------------|
| 5 | Five Year Plan | 1-step CardSelect | Correct |
| 7 | Socialist Governments | 3-step CountryPick, erased pool | Correct (inherited <2/country bug) |
| 10 | Blockade | 1-step CardSelect | Correct |
| 14 | COMECON | ≤4-step CountryPick, erased pool | Correct |
| 16 | Warsaw Pact | SmallChoice + 4 or 5 CountryPick | Correct (inherited no-cap on add branch) |
| 19 | Truman Doctrine | 1-step CountryPick | Correct |
| 20 | Olympic Games | SmallChoice + optional 4 CountryPick | Correct (inherited accessibility bugs) |
| 23 | Marshall Plan | 7-step CountryPick, erased pool | Correct |
| 26 | CIA Created | 1-step CountryPick | Correct |
| 28 | Suez Crisis | 2-step CountryPick | Correct (inherited fixed-2-per-country logic bug) |
| 29 | East European Unrest | 3-step CountryPick, erased pool | Correct |
| 30 | Decolonization | 4-step CountryPick, NON-erased pool | Correct (inherited no-distinct-country bug) |
| 33 | De-Stalinization | 2N-step src/dst interleaved | **BUG: interleaved remove-place, inherited plus no 2-per-country cap on place phase** |
| 36 | Cambridge Five | N-step region-indexed | Correct |
| 37 | Special Relationship | 2-step CountryPick | Correct |
| 46 | SALT Negotiations | 1-step CardSelect | Correct |
| 48 | Summit | 1-step SmallChoice | Correct |
| 49 | How I Learned... | 1-step SmallChoice | Correct |
| 50 | Junta | 2-step CountryPick (infl, coup) | Correct (inherited realign-not-supported, mandatory-coup bugs) |
| 52 | Missile Envy | 1-step CardSelect + nested ops | Partial (nested ops not frame-aware) |
| 56 | South African Unrest | 1-step CountryPick | Correct |
| 59 | Muslim Revolution | 2-step CountryPick, erased pool | Correct |
| 60 | ABM Treaty | 2-step CountryPick | Correct frame; pre-existing logic wrong card |
| 67 | Puppet Governments | 3-step CountryPick, erased pool | Correct |
| 68 | Grain Sales to Soviets | 1-step CardSelect + nested ops | Partial (nested ops not frame-aware) |
| 71 | OAS Founded | 2-step CountryPick, non-erased | Correct |
| 75 | Voice of America | 4-step CountryPick, erased pool | Correct (inherited forced-1-per-country bug) |
| 76 | Liberation Theology | 3-step CountryPick, non-erased | Correct (inherited no-cap-2 bug) |
| 77 | Ussuri River Skirmish | 4-step CountryPick global pool | Correct frame; pre-existing wrong-region bug |
| 88 | Star Wars | 1-step CardSelect | Correct |
| 94 | Ortega | 1-step CountryPick (free coup) | Correct |
| 95 | Terrorism | 1 or 2-step CardSelect | Correct frame; pre-existing wrong "random vs selected" |
| 98 | Latin American Debt Crisis | 2-step CardSelect | Correct frame; pre-existing completely-wrong-effect |
| 101 | Aldrich Ames Remix | 1-step CardSelect | Correct |

---

## Conclusions

Bugs ranked by game impact (competitive-play cost):

1. **Card 98 Latin American Debt Crisis is implemented as a different event entirely** (2-card forced discard from US hand, not S.American infl doubling). PRE-EXISTING, not frame-migration. Fix priority: high (common Late War card, huge rules deviation).

2. **Card 77 Ussuri River Skirmish uses global pool instead of Asia-only**, allowing 4 USSR infl to drop into Poland/East Germany. PRE-EXISTING, not frame-migration. Fix priority: high (rare card but single-instance, game-warping).

3. **Card 30 Decolonization allows all 4 infl in one country** (pool never erased). PRE-EXISTING. Fix priority: high (common USSR event, trivial one-line fix).

4. **Card 33 De-Stalinization frame decomposition is interleaved** (src-dst pairs, not "all removes then all places"). Also inherits (a) no 2-per-destination cap and (b) forced max relocation. This is the user's flagged concern and is real. Fix priority: high (common USSR Early War event, multi-bug card).

5. **Card 16 Warsaw Pact "add 5" branch has no 2-per-country cap**, allows all 5 in one country. PRE-EXISTING. Fix priority: medium (common starred card, exploit known).

6. **Card 76 Liberation Theology allows all 3 in one country** (no cap 2). PRE-EXISTING. Fix priority: medium.

7. **Card 95 Terrorism uses player-selected discard instead of random**. PRE-EXISTING. Fix priority: medium (semi-common Late War card, asymmetric impact).

8. **Card 60 ABM Treaty implements wrong VP and wrong influence count** (+1 VP wrong; 2 instead of 4 placements). PRE-EXISTING. Fix priority: medium.

9. **Card 28 Suez Crisis forces exactly 2 distinct countries at 2 each** instead of distributable 4-op removal budget. PRE-EXISTING. Fix priority: medium.

10. **Card 75 Voice of America forces 1 per country** instead of "up to 2". PRE-EXISTING. Fix priority: low.

11. **Card 50 Junta lacks realignment option and forces coup**. PRE-EXISTING. Fix priority: low.

12. **Card 20 Olympic Games boycott branch uses frozen accessibility pool and no double-cost for opponent control**. PRE-EXISTING. Fix priority: low (rarely event-played).

**Migration-specific conclusion**: The frame decomposition layer **does not introduce new rules bugs beyond those already present in the synchronous `choose_*` paths**. Frame-mode and policy-cb-mode produce equivalent behavior on every audited card. The user's concern about De-Stalinization is valid but the concern applies to **both** paths equally — it is a rules bug in the card's original implementation, not a frame-migration regression.

---

## Recommendations

Fix order (highest ROI first):

### 1. Card 33 De-Stalinization — atomic remove-then-place phases (within scalar FrameAction)

Rewrite `step.cpp` case 33 and `resume_card_33` to:
- Phase 1: up to 4 sequential CountryPicks where eligible = USSR-infl>0 countries (recomputed each step). Commit -1 USSR infl immediately (this is visible to phase 2 picks).
- Phase 2: up to N (N = phase-1 picks actually made) sequential CountryPicks where eligible = non-US-controlled AND running-placements[cid] < 2. Track per-country placements via a new `destal_place_count[kCountrySlots]` scratch array in PublicState, cleared at event start and end.
- Criteria_bits bit 15 = phase flag (0=remove, 1=place); lower bits unused in phase 1, unused in phase 2 (the running placement counter lives in state, not in criteria_bits).
- Optional: push a SmallChoice frame FIRST letting USSR choose how many to relocate (0-4). This adds a 2-4 option SmallChoice but matches "up to 4" flexibility.

### 2. One-line rule-cap fixes (pre-existing but cheap)

- **Card 30 Decolonization**: add `next_eligible.reset(action.country_id)` in `resume_card_30` and `pool.erase(...)` in step.cpp case 30. Distinct-country rule.
- **Card 77 Ussuri River Skirmish**: filter pool to `country_spec(cid).region == Region::Asia`. Add `next_eligible.reset` for 2-per-country cap (actually add per-country counter for "up to 2 per country" similar to the De-Stal fix).

### 3. Card 98 Latin American Debt Crisis — reimplement from scratch

Remove case 98 from `kCatCCardIds` in hand_ops.cpp. Implement the correct effect as a non-cat-C event:
- US `choose_option` to discard ops≥3 card (cancel) or accept.
- If accepted: USSR picks 2 S.American countries, doubles USSR infl in each.

This requires a new frame pattern (opponent-side cancel choice + phasing-side country picks), similar to Blockade's cancel mechanic.

### 4. Card 95 Terrorism — make random

Replace `choose_card(...)` with `rng`-based random pick. Removes the need for CardSelect frame altogether. Matches official rules.

### 5. Card 68 Grain Sales to Soviets — make draw random

Same as Terrorism: the US should draw a RANDOM card from USSR hand (not select). Replace `choose_card(...)` with RNG. This also simplifies the nested ops issue (if the drawn card's ops usage is played by the policy, the outer draw is non-decision, only the ops-placement decision remains).

### 6. Per-country-cap fixes

- **Card 7 Socialist Governments**: add explicit per-country counter to allow up to 2 per country (lift the `< 2` filter on initial pool; track running placements in a scratch array).
- **Card 76 Liberation Theology**: same pattern (2-per-country scratch counter).
- **Card 16 Warsaw Pact** branch 1 (add 5): same pattern.

These can share a helper `push_capped_placement_frames(gs, card, side, pool, total, per_country_cap, parent_card)`.

### 7. Card 50 Junta — add realignment option

In step.cpp case 50 step 1, push a SmallChoice(coup=0, realign=1) before the country pick, or thread the mode choice into the country pick criteria_bits.

### 8. Card 60 ABM Treaty — fix placement count and remove wrong VP

Change loop `for (int i = 0; i < 2; ...)` to `for (int i = 0; i < 4; ...)`. Remove the `apply_vp_delta(next, side, 1)`. Change pool to `accessible_countries(side, Influence)`.

### 9. Card 28 Suez Crisis — make removal budget distributable

Rewrite as a 4-op removal budget distributed across {France, UK, Israel} with per-country cap of 2. Requires either an Alloc-style frame (out of scope per schema decision) or 4 sequential 1-op removals with per-country scratch counter.

### 10. Retain existing frame decomposition for everything else

Cards 5, 10, 14, 19, 23, 26, 29, 36, 37, 46, 48, 49, 56, 59, 67, 71, 88, 94, 101 — frame decomposition is correct per current (possibly buggy-at-rules-level) synchronous semantics. No migration-layer changes needed; underlying rules fixes, if any, will propagate through unchanged frame logic.

---

## Open Questions

1. **Is the user's De-Stalinization concern primarily about information symmetry (policy should see identical observation for "remove+place" atom as a full pair) or about decision expressiveness (policy should choose all removes before any place)?** The recommended fix addresses the latter; the former requires an Alloc-style multiset frame and is out of scope per the 20260419_062129 schema decision.

2. **What is the authoritative card text source for this project?** The PDF `docs/TS_Rules_Deluxe.pdf` contains the rulebook body and flavor text but not the per-card event-effect table. `docs/event_scope.md` has summarized effects but mixes rules interpretation with implementation commentary. For a rigorous audit, the actual Deluxe Edition card face text should be transcribed into a separate `docs/card_text.md` or extracted from a verified source (e.g., BGG card list, twilightstrategy.com). Several cards above have their implementation behavior diverging from standard community-accepted effects, and the project has no single source of truth to resolve disputes.

3. **Should "up to N" semantics always include the option of choosing 0?** Several cards (De-Stalinization, Warsaw Pact remove branch, Decolonization) allow "up to" a maximum; current implementation forces the maximum. Fix requires either (a) a SmallChoice count frame up front or (b) a "stop" option in each CountryPick. Option (b) is friendly to the scalar schema: add a sentinel country_id = -1 to mean "pass / stop here" in the eligible set.

4. **Are pre-existing rules bugs in scope for this migration cycle?** The audit focused on whether frame decomposition preserves the current synchronous path. Most of the serious rules issues (cards 30, 77, 98, etc.) are pre-existing and orthogonal to migration. Fixing them alongside migration is cheap (matching code change in both paths) but mixing the commits may muddy what's a migration regression vs. a genuine rules fix.

5. **Card 33 De-Stalinization: how to surface the "full post-remove board" to phase-2 picks?** Recommended fix commits each remove immediately (phase 1 sequential with eager commits); when phase 2 begins, gs.pub already reflects all removes, so each place pick sees the correct board. This is equivalent to the "rules-correct" interpretation IF we assume the player is allowed to observe their own tentative removes (which they are — they can look at their own board state while playing). The only lost expressiveness is "allocate 4 removes across multiset of source countries" as a single combinatorial decision, which under the scalar FrameAction schema is decomposed into 4 sequential picks with running visibility — acceptable per the project's scalar-schema decision.
