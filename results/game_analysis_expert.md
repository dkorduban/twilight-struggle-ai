# Expert Game Analysis: MCTS-2000sim (USSR) vs Heuristic (US)

**Date:** 2026-04-06  
**Model:** v106_cf_gnn_s42 (GNN-based policy net, 95 epochs)  
**Config:** 2000 simulations, edge pruning at 1e-4, Nash temperatures, seed 77777  
**Game ID:** mcts_77777_0000  

---

## Game Summary

| Field | Value |
|-------|-------|
| **Winner** | **USSR** (MCTS-controlled) |
| **Final VP** | USSR +27 (game ended on VP threshold) |
| **End Turn** | 10 (full game) |
| **End Reason** | VP threshold exceeded |
| **Early War VP** | 0 (after Turn 3) |
| **Mid War peak VP** | +10 USSR (after T6 headlines) |
| **Late War slide** | USSR stayed above threshold from T9 on |

The USSR dominated this game primarily through the **Africa and Southeast Asia regions**, piling enormous influence into South Africa (+29 USSR), Thailand (+10 USSR), and Indonesia (+7 USSR). The model showed strong regional concentration tendencies but several notable strategic errors, analyzed below.

---

## Turn-by-Turn Narrative with Expert Commentary

### Turn 1 — Early War

**Headlines:**
- **US** plays US/Japan Mutual Defense Pact (4ops) as Headline — MCTS 96% confidence
- **USSR** plays Duck and Cover (3ops) as Headline — MCTS 61% for Event, but 15% Headline

> **EXPERT (Headlines):** US/Japan as US headline is correct and standard — it locks Japan and secures the Asia presence. USSR's Duck and Cover headline is a significant error. Duck and Cover as event raises DEFCON by 1, meaning the US gets that benefit while USSR gets nothing. MCTS split (61% Event, 15% Headline) shows the model had high preference for the event but chose Headline mode incorrectly — if both headline simultaneously, the event fires "for" the US side but the DEFCON penalty/benefit depends on resolution order. A stronger USSR player would headline **COMECON, Warsaw Pact, or De-Stalinization** — opponent cards should be played for ops or spaced, not headlined for the opponent's event. **This is Mistake #1.**

**Action Rounds:**
- **AR1 USSR:** Arab-Israeli War (2ops) → Event → targets Iran (37% visits; coup was 12%)
- **AR1 US:** Nuclear Test Ban (4ops) → Ops → West Germany, Thailand x3

> **EXPERT (AR1):** Arab-Israeli War as event on T1 AR1 is solid — coups are dangerous at DEFCON-4 (which the Duck and Cover headline moved to), and the event gives immediate Middle East presence. However, MCTS targeted Iran with the event — Arab-Israeli War as event gives USSR 2 influence in Egypt and removes US influence (standard). The "Iran" country_id showing in targets appears to be the event target resolution. This is reasonable play.
>
> US plays Nuclear Test Ban (4ops) for Ops into West Germany + Thailand x3 is strange. NTB as Ops for a neutral card uses 4 ops across Asia/Europe — the Thailand overload (3 influence in one country) is high-cost inefficiency at DEFCON-3. NTB as event would raise DEFCON and give VPs; using it purely for ops here wastes the event potential. However, at DEFCON-3 already, the heuristic US correctly avoids triggering NTB event (which raises DEFCON, good for USSR at low DEFCON). Ops allocation to Thailand is puzzling — Thailand has stability 2, so 4+ influence needed for control.

- **AR2 USSR:** Marshall Plan (4ops, US card) → Ops → Indonesia, Vietnam x3

> **EXPERT (AR2 USSR):** Marshall Plan is a US 4-ops card. Playing it for Ops is correct since the event would massively help the US (7 Western European nations get 1 influence each). MCTS correctly spends it for ops. However, the targeting — Indonesia and Vietnam x3 — shows the model's Asia over-investment bias early. Indonesia (stab 1) and Vietnam (stab 1) are SEA battlegrounds, but spending 4 ops here on T1 AR2 neglects Europe where both Italy and West Germany needed attention. MCTS had 25% on Space — spacing Marshall Plan T1 is also viable. **Minor inefficiency in targeting.**

- **AR2 US:** East European Unrest (3ops) → Ops → Philippines x2, Vietnam

> **EXPERT (AR2 US):** EEU as ops targeting Philippines and Vietnam is reasonable — spreads into Asia battlegrounds. EEU event (remove 1 influence from each of 3 Eastern European countries) is useful but heuristic US chose ops. Philippines (stab 2, US battleground) benefits from the ops.

- **AR3 USSR:** Decolonization (2ops) → Ops → Thailand x2

> **EXPERT (AR3 USSR):** Decolonization into Thailand continues the SEA stack. Decolonization event (4 ops into Africa/Asia non-battlegrounds) would be decent but MCTS prefers ops. The 30% Space visit shows model uncertainty here — spacing Decolonization T1 is suboptimal since it's reusable.

- **AR3 US (Heuristic):** NORAD (3ops) → Ops → Iran x2, Angola

> **EXPERT (AR3 US):** NORAD event is very strong for US (gains permanent DEFCON monitoring ability). The heuristic plays it for ops instead — this is a significant heuristic error, not an MCTS error. NORAD event should fire whenever possible; its 3 ops can be found elsewhere.

- **AR4 USSR:** Cambridge Five (2ops) → Ops → Japan, Thailand

> **EXPERT (AR4 USSR):** Cambridge Five event (reveal US hand if China Card unavailable) is a USSR card. MCTS chose Ops (44%) over Event (11%), spreading to Japan and Thailand. The event would be valuable intelligence but MCTS correctly assesses ops as more immediately useful at DEFCON-3.

- **AR4 US:** De-Stalinization (3ops, USSR card) → Ops → Iran, Ethiopia, Nigeria

> **EXPERT (AR4 US):** De-Stalinization for Ops is correct — its event would spread USSR influence across 4 countries. Spreading to Iran (BG, Middle East), Ethiopia (BG, Africa), Nigeria (BG, Africa) is solid territory denial. MCTS had 39% on Socialist Governments here — competitive decision.

- **AR5 USSR:** UN Intervention (1ops) → Ops → North Korea

> **EXPERT (AR5 USSR):** UN Intervention event requires the actor to discard a card matching the card to be neutralized; as 1-op Ops it's extremely weak. This reveals the model spending a 1-op card to place 1 influence in North Korea. North Korea (stability 3, USSR battleground) needs 4+ influence for control — placing 1 influence here is nearly useless. **The correct play is UN Intervention as Event to neutralize a dangerous opponent event card.** However, using it for ops to North Korea suggests the model had no dangerous cards to block. Minor inefficiency.

- **AR5 US:** Socialist Governments (3ops, USSR card) → Ops → Japan x1, North Korea x2

> **EXPERT (AR5 US):** SG for ops into Japan and North Korea. SG event (remove 1 ops from 3 Western European countries) is dangerous for US — correctly played for ops. Japan consolidation is good.

- **AR6 USSR:** Truman Doctrine (1ops, US card) → Ops → Thailand

> **EXPERT (AR6 USSR):** Truman Doctrine event removes ALL USSR influence from one uncontrolled country. Playing it for 1 op is correct — the event would hurt USSR. Adding 1 more to Thailand.

- **AR6 US:** Fidel (2ops, USSR card) → Event → Lebanon

> **EXPERT (AR6 US):** Fidel event gives Cuba to USSR. Playing it for event (87%) is deeply puzzling — this gives USSR Cuba (4 influence) for free and removes any US presence. Fidel should be played for ops. MCTS top was 87% Event here. **This is a major heuristic error by US**, but wait — phasing is US (1), so the US player is choosing to fire Fidel event which benefits USSR. This indicates the heuristic AI is playing suboptimally here by triggering the enemy event.

**Turn 1 Summary:** VP stayed at 0. DEFCON dropped to 3 (Duck and Cover headline). USSR built Asia/SEA stack; US spread across multiple theaters.

---

### Turn 2 — Early War

**Headlines:**
- **USSR** plays COMECON (3ops) → Event (82%)
- **US** plays Korean War (2ops, USSR card) → Headline (54%)

> **EXPERT (Headlines T2):** COMECON as event (+1 influence in 4 Eastern European countries) for the USSR headline is correct and powerful. Korean War as Headline by the US is a significant error: this is a USSR card, so if headlined, the **event fires for USSR** (Korean War = coup in South Korea, +2VP on success). MCTS had Korean War at 54% Headline and 15% Space — but spacing it (to prevent the event ever firing for USSR) is stronger than headlining it. The heuristic made the mistake of headlining an opponent's card whose event fires automatically. **Heuristic Mistake: should space Korean War, not headline it.** This gave USSR 2VP (Korean War succeeds) + COMECON fires = net positive for USSR.
> 
> VP jumps from 0 to 2 (USSR +2) due to this combination.

**Action Rounds:**
- **AR1 USSR:** Warsaw Pact Formed (3ops, USSR starred) → Ops → West Germany, Nigeria, Thailand

> **EXPERT (AR1 T2):** Warsaw Pact event is massive — establishes NATO counter and gives USSR Eastern European presence. MCTS at 66% Ops shows the model prefers to use it for ops rather than fire its powerful event. Warsaw Pact Formed event: removes all US influence from East Germany/Poland/Czechoslovakia and places 1 USSR influence there. This is potentially game-winning in Europe early. **Playing WPF for ops into West Germany, Nigeria, Thailand is a major mistake.** The event is arguably worth 8-10 ops equivalent in Europe consolidation. MCTS top visit is Ops (66%), Headline (14%), Space (11%), Event (8%). **Mistake #2: MCTS fails to recognize Warsaw Pact event value.**

- **AR1 US:** Red Scare/Purge (4ops) → Space (58%)

> **EXPERT (AR1 T2 US):** Red Scare/Purge (4ops neutral) as Space is interesting — the US is spending a 4-op card on space race. R/S event is strong (reduce all opponent ops by 1 for the round) but the heuristic chose Space. At 4 ops, this is a reasonably efficient space card but wastes significant event potential.

- **AR2 USSR:** NATO (4ops, US card) → Ops → Pakistan, South Korea x2, Israel

> **EXPERT (AR2 T2):** NATO event is devastating for USSR — it makes Western European countries immune to coups and realignments. Playing it for Ops (49%) is correct. Spreading to Pakistan (Asia BG), South Korea (Asia BG), Israel (ME BG) is reasonable.

- **AR2 US:** Five Year Plan (3ops, US card) → Event (81%)

> **EXPERT (AR2 T2 US):** Five Year Plan event forces USSR to discard a card randomly. Very strong US event — correctly fired. Heuristic plays it well.

- **AR3 USSR:** Olympic Games (2ops, Neutral) → Ops → Lebanon, Thailand (28% Event, 17% Ops)

> **EXPERT (AR3 T2):** Olympic Games event is complex — forces boycott decision with DEFCON risk. At DEFCON-3 (from Duck and Cover), playing OG event could risk nuclear war. MCTS at 28% Event shows model considered it. Spreading ops to Lebanon and Thailand continues the pattern. Lebanon (Middle East battleground) is a reasonable target.

- **AR3 US:** Independent Reds (2ops, US starred) → Event → Saudi Arabia

> **EXPERT (AR3 T2 US):** Independent Reds fires and grants the US control of Yugoslavia or an Eastern European country. Saudi Arabia appears to be the country chosen (or this is the state snapshot country). Solid play.

- **AR4 USSR:** Indo-Pakistani War (2ops) → Ops → Pakistan, Indonesia (Space 28%, Ops 21%)

> **EXPERT (AR4 T2):** DEFCON is 2 now — extremely dangerous. Indo-Pakistani War event would be a coup in Pakistan or India, risking DEFCON drop to 1 (nuclear war). MCTS correctly avoids the event (only 0% event in visits). Space had 28%, Ops 21% — spacing Indo-Pak is viable but the model chose ops. At DEFCON-2, any coup risks game end — this is critical.

- **AR4 US:** De Gaulle Leads France (3ops, USSR card) → Ops → East Germany, Turkey, Indonesia

> **EXPERT (AR4 T2 US):** DeGaulle event removes NATO from France and places USSR influence there. Playing for ops is correct. Spreading to E. Germany (blocked by USSR domination), Turkey (US BG), Indonesia (contested SEA BG).

- **AR5-6 both sides:** Opponent cards for Ops, no events fired.

> **EXPERT (T2 late):** Both sides play remaining cards for ops at DEFCON-2. USSR plays Containment (3ops, US card) into E. Germany and Indonesia — correct (Containment event gives +1 ops to US). US plays Vietnam Revolts (USSR card) into UK x3 — placing influence in UK (stability 5, US controlled) wastes ops completely. **Heuristic Mistake: stacking UK with 3 influence when UK is already safely US-controlled.**

**Turn 2 Summary:** VP stays at 2 (USSR). DEFCON recovered to 4 for Turn 3. USSR built Asia/SEA stack; missed Warsaw Pact event opportunity.

---

### Turn 3 — Early War (Last Chance for Early War Events)

**Headlines:**
- **US** plays East European Unrest (3ops) → Event (92%)
- **USSR** plays Socialist Governments (3ops) → Headline (46%, Space 17%, Coup 11%)

> **EXPERT (Headlines T3):** EEU event removes 1 influence from each of 3 Eastern European countries. US correctly fires this. USSR headlines Socialist Governments with 46% confidence — SG event would reduce Western Europe ops, but this fires against the US, which is the active player getting to choose... actually SG event fires for USSR (reduces US ops in Western Europe). This could be correct, but Space (17%) and Coup (11%) were competitive alternatives. Coup at DEFCON-4 risks dropping to 3.

- **AR1 USSR:** Suez Crisis (3ops, USSR starred) → Event → Syria (82%)

> **EXPERT (AR1 T3):** Suez Crisis event removes 4 influence from UK/France/Israel collectively. Strong USSR event, correctly fired on T3 AR1.

- **AR1 US:** Duck and Cover (3ops, US card, second instance) → Ops → S. Korea, Iran, Panama

> **EXPERT (AR1 T3 US):** Duck and Cover has already been headlined once — if starred it's removed. Wait, Duck and Cover is NOT starred. Duck and Cover for Ops into three Middle East/Asia countries is reasonable territory spreading.

- **AR2 USSR:** Arab-Israeli War (2ops) → Event again → Iran (DEFCON=3 now at 2)

> **EXPERT (AR2 T3):** Arab-Israeli War second firing is notable — it's not starred so it recycles. The event targets Iran giving USSR influence in Middle East. However, at DEFCON-2, the coup risk is real. The model correctly played Event (82%) not Coup (checked visits: 0%).

- **AR3 USSR:** Olympic Games → Ops → S. Korea x2 (81%)

> **EXPERT (AR3 T3):** OG Ops into South Korea, which USSR now dominates (5-1 by Turn 5). Solid.

- **AR4-6 both:** End-of-Early-War cleanup, both sides spreading ops.

> **EXPERT (T3 late):** US plays Five Year Plan event again (+same dynamic), Warren Pact ops, CIA Created (1op) for 1 influence in Japan. CIA Created event (reveal USSR hand) is worth firing but heuristic chose ops — understandable given CIA is 1 op event.
>
> USSR plays NORAD (3ops, US card) → Ops into Japan, Mexico, Congo. And Special Relationship (2ops, US card) → Ops into Indonesia, Thailand. Both correctly played for ops rather than triggering US events.

**Blockade (1op, USSR starred):** US plays for Ops → Thailand at AR6 T3. VP drops from 2 to 0. Blockade event discards a US card if they have a 3-op card; playing for ops instead loses that leverage. **However: at this point both sides are starved for good cards, and Blockade at end of T3 is a common "use it or lose it" situation.**

**Turn 3 Summary:** VP at 0 (tied) entering Mid War. USSR built: S. Korea, Japan contested, Indonesia/Thailand dominant, strong in Middle East. Europe: West Germany underinvested, Eastern Europe mixed. No scoring cards played yet.

---

### Turn 4 — Mid War Begins

**Headlines:**
- **US** plays SALT Negotiations (3ops, Neutral) → Event (52%) / Headline (19%)
- **USSR** plays Cuban Missile Crisis (3ops, Neutral) → Headline (85%)

> **EXPERT (Headlines T4):** SALT Negotiations event is strong for US (restricts Space Race, gives VPs, draws cards). US chose Event (52%). CMC Headline by USSR is reasonable — CMC event sets DEFCON to 2 but no coups allowed, giving USSR a safer mid-game. MCTS confident at 85%. CMC also prevents further DEFCON drops, protecting USSR's accumulated position. The interaction: SALT fires giving US VPs/cards, then CMC fires setting DEFCON=2. VP goes to +2 USSR (SALT gives VPs to US — but wait, the VP shows 2 USSR going into AR1 T4, so SALT must have given VP to USSR here or the VP tracks oddly). The transition to DEFCON=2 means no coups allowed for the turn.

- **AR1 USSR:** OPEC (3ops, USSR) → Ops → Angola, Congo, Nigeria (55% Ops, 13% Coup)

> **EXPERT (AR1 T4):** OPEC event gives USSR VP for each of several African oil countries they control. At this point USSR controls Nigeria, Congo — firing OPEC would give immediate VPs. Instead MCTS plays Ops, spreading further into Africa. 13% Coup visit is interesting (blocked by CMC/DEFCON=2 anyway). **Minor missed event opportunity with OPEC; could have gotten 2-4 VPs.**

- **AR2 USSR:** Ussuri River Skirmish (3ops, Neutral) → Headline (51%)

> **EXPERT (AR2 T4):** URS Headline in AR2? This is highly unusual — headlining a card in the action round means it's saved for the next turn's headline phase. MCTS at 51% Headline, 33% Ops. URS event: China Card goes to opponent with 5 influence distributed. Headlining URS while already having played the turn headline seems like a tracking quirk or the model is setting up the next turn's headline.

- **AR3 USSR:** Indo-Pakistani War → Ops → Mexico, Argentina (65% Ops, Space 8%)

> **EXPERT (AR3 T4):** Spreading into South America — Mexico (CA BG) and Argentina (SA BG). Reasonable territorial expansion.

- **AR5 USSR:** Willy Brandt (2ops, USSR starred) → Ops → S. Africa x2 (54% Ops, 26% Space)

> **EXPERT (AR5 T4):** Willy Brandt event removes W. Germany from NATO and gives USSR influence there. Playing for ops into S. Africa instead of firing the event is debatable. W. Germany is a 4-stability battleground — WB event is worth ~4 ops equivalent. **However,** at this stage the model may have assessed S. Africa as higher priority. Willy Brandt will be removed (starred) if fired, so the ops are "banked" instead. **Mistake #3: Willy Brandt event is nearly always correct to fire — it directly shifts European balance.**

- **AR6 USSR:** Nixon Plays the China Card (2ops, US card) → Ops → S. Africa x2

> **EXPERT (AR6 T4):** Nixon event gives USSR the China Card. Playing for ops is correct (don't give USSR the China Card).

**Turn 4 Summary:** VP remains at 2 USSR. Africa expansion underway. OPEC and Willy Brandt event opportunities missed. South America being seeded.

---

### Turn 5 — Mid War

**Headlines:**
- **USSR** plays Nuclear Test Ban (4ops, Neutral) → Headline (18%, but Space 65%!)
- **US** plays Arms Race (3ops, Neutral) → Headline (18%, Space 42%, Coup 38%)

> **EXPERT (Headlines T5):** NTB Space was 65% but Headline was chosen at 18% — this is interesting. USSR headlining NTB means the event fires: NTB event raises DEFCON by 1 and gives the active player VPs based on DEFCON. If DEFCON was 3, this gives USSR 2 VP. **VP indeed goes from 2 to 3 (USSR +1) this turn.** 
>
> Arms Race headline by US: AR event gives VPs to the side with more MilOps — risky if USSR has more. Space (42%) was the model's top choice but Headline was selected. With Arms Race, if USSR has higher MilOps, it benefits USSR (which it did — VP shows +USSR). **Heuristic mistake: Arms Race headline when USSR may be leading in MilOps.**

- **AR1 USSR:** ABM Treaty (4ops, Neutral) → Ops → E. Germany, Brazil x2, S. Africa (Space 44%, Ops 28%)

> **EXPERT (AR1 T5):** ABM Treaty event raises DEFCON and gives both sides VPs — neutral event, firing is reasonable. MCTS at 44% Space (would advance space race) vs 28% Ops. Model chose Ops into E. Germany, Brazil, S. Africa. E. Germany is a European BG — correct to invest. **Brazil (stability 2, SA BG)** getting influence is South America expansion. S. Africa = continuing Africa stack.

- **AR1 US:** Che (3ops, USSR card) → Space (78%)

> **EXPERT (AR1 T5 US):** Che event allows 2 coups in Africa/Central America. Spacing it is correct — neutralizes a powerful coup card. 78% Space confidence shows heuristic correctly identifies this.

- **AR2 USSR:** Brush War (3ops, USSR) → Ops → Chile, Venezuela, S. Africa (43% Space, 17% Ops)

> **EXPERT (AR2 T5):** Brush War event is a 3-op coup in Africa or Central America. MCTS preferred Space (43%) but played Ops into Chile, Venezuela, S. Africa. Spacing Brush War preserves the coup option for later — but the model chose ops. Chile and Venezuela are SA BGs. This is reasonable territory work.

- **AR2 US:** How I Learned to Stop Worrying → Ops → Egypt, Libya (98%)

> **EXPERT (AR2 T5 US):** HILTSW event sets DEFCON to 2 and raises MilOps — playing for ops to Egypt and Libya is defensible ops play at DEFCON-4. Egypt and Libya are Middle East BGs. Solid.

- **AR3 USSR:** Quagmire (3ops, USSR starred) → Ops → Chile, S. Africa x2 (59% Ops, 13% Space, 7% Coup)

> **EXPERT (AR3 T5):** Quagmire event would trap the US in Vietnam (discard cards each round). This is extremely strong against heuristic opponents who may not play efficiently under Quagmire. MCTS chose Ops (59%) over Event (not shown in top 4, very low). **Mistake #4: Quagmire event is among the strongest USSR cards in Mid War — forcing a human or heuristic into Quagmire mode is a decisive advantage. MCTS consistently under-values powerful trap cards like Quagmire and Bear Trap.**

- **AR3 US:** Puppet Governments (2ops) → Ops → Chile, S. Africa

> Note the pattern: both sides targeting Chile and South Africa repeatedly throughout T5.

- **AR4 USSR:** Shuttle Diplomacy (3ops, US card) → Ops → Venezuela x3

> **EXPERT (AR4 T5):** SD event blocks scoring of a region temporarily. Playing for ops into Venezuela (SA BG). 70% Ops confidence.

- **AR5-7:** Both sides continue stacking Chile and South Africa repeatedly.

> **EXPERT (T5 late):** The Chile and South Africa fixation from T5 onward is the game's most notable pattern. By end of T5:
> - South Africa: USSR 5, US 4 (contested)  
> - Chile: USSR 1, US 0 (light USSR presence)
>
> Both sides are repeatedly targeting the same 2 countries with low-value ops when higher-value BGs in Europe and Asia need attention. This is a known failure mode of the model — **VP-metric focus on "contested" territories rather than strategic scoring board control.**

**Turn 5 Summary:** VP goes to 4 USSR (slight climb). USSR missed Quagmire event (huge mistake). Both sides locked into South Africa / Chile fixation beginning.

---

### Turn 6 — Mid War (Last Mid War Turn, Scoring Pressure)

**Headlines:**
- **US** plays We Will Bury You (4ops, USSR starred) → Headline (19%, Ops 76%)
- **USSR** plays Red Scare/Purge (4ops, Neutral) → Headline (35%, Space 14%, Coup 12%)

> **EXPERT (Headlines T6):** WWBY event gives USSR 3 VP plus Europe scoring threat. US headlining this fires the event — giving USSR 3 VP automatically! **VP: 4 → 7 (USSR +3).** This is the biggest single mistake in the game: US headlined an opponent's 4-op starred card that gives free VPs. MCTS Ops preference (76%) shows the model knew playing WWBY for ops was better, but the heuristic chose to headline it for the enemy.
>
> Red Scare/Purge headline by USSR: RSS event reduces all US cards by 1 op for a turn. Moderately useful, headline is reasonable. VP goes further: 7 → 10 (USSR +3). The compounding is: WWBY fires (USSR +3VP) then RSS fires (reducing US options). This turn's headline interaction gave USSR 6 VP swing.

- **AR1 USSR:** Muslim Revolution (4ops) → Ops → Ethiopia x4 (Space 21%, Ops 21%)

> **EXPERT (AR1 T6):** Muslim Revolution event removes US influence from Muslim countries and gives USSR control of 2. Event would be very strong (Iran, Pakistan, Egypt potential). MCTS at 21% Space / 21% Ops — essentially coin flip. Model chose Ops, stacking Ethiopia (Africa BG). By now Ethiopia: USSR 7, US 5 — heavy investment in a low-stability battleground.

- **AR1 US:** Bear Trap (3ops, US starred) → Ops → Chile x2 (95%)

> **EXPERT (AR1 T6 US):** Bear Trap event traps USSR in Vietnam (same as Quagmire for USSR). US playing it for ops loses a potentially decisive trap card. **Bear Trap for ops into Chile is another missed event opportunity by the heuristic.** MCTS correctly plays its own traps; heuristic does not.

- **AR2 USSR:** Cultural Revolution (3ops, USSR starred) → Ops → Ethiopia x3 (21% Space/Ops each)

> **EXPERT (AR2 T6):** CR event gives USSR the China Card (if US holds it) and raises space track. Playing for ops into Ethiopia again. By this point Ethiopia has become an ops sink with diminishing returns.

- **AR2 US:** Summit (3ops, Neutral) → Ops → Morocco, S. Africa (96%)

> **EXPERT (AR2 T6 US):** Summit event gives VPs based on DEFCON + higher space race. US plays for ops — Morocco and S. Africa continuing the Africa spread.

- **AR3 USSR:** Decolonization (2ops) → Ops → Chile, S. Africa (Space 32%, Ops 21%)

> Pattern continues. At this point South Africa: USSR+5, US+4 (nearly controlled by USSR).

- **AR5 USSR:** Alliance for Progress (3ops, US card) → Space (46%)

> **EXPERT (AR5 T6):** Alliance for Progress event gives +1 influence per Latin American BG controlled. US correctly fires it for ops sometimes; USSR spacing it (46% Space) is reasonable since the event benefits US. But MCTS chose Ops (21%) into Chile/S. Africa again. Spacing was actually the better call here.

- **AR6 USSR:** Nuclear Subs (2ops, US card) → Ops → Chile, S. Africa (Coup 13%)

> **EXPERT (AR6 T6):** NSubs event prevents DEFCON drops from US coups — playing for ops is correct.

- **AR7 USSR:** Panama Canal Returned (1ops, US starred) → Ops → Chile (1 op, very weak)

> **EXPERT (AR7 T6):** PCR event returns Panama to neutral. Playing for 1 op into Chile continues the pattern. At this point Chile has USSR+8, US+16 by game's end, meaning the sustained Chile investment failed to achieve control.

**Turn 6 Summary:** VP swings dramatically: 4 → 10 (USSR) due to WWBY + Red Scare headline disasters by the heuristic. USSR leads 10 VP entering Late War. Note: End-of-turn VP adjustments fire automatically between turns outside MCTS decision points (T5→T6: +3 USSR, T7→T8: +2 USSR, T8→T9: +3 USSR, T9→T10: +3 USSR). No scoring cards appeared in the MCTS visit lists — this may indicate scoring cards were not dealt to either player this game (random draw) or were handled outside the traced decision window.

---

### Turn 7 — Late War Begins

**Headlines:**
- **USSR** plays Duck and Cover (3ops, US card) → Headline (20%, Space 45%)
- **US** plays Arab-Israeli War (2ops, USSR card) → Headline (98%)

> **EXPERT (Headlines T7):** D&C headline fires DEFCON drop — marginally useful for USSR. US headlining AIW again fires the USSR event giving USSR Middle East influence. Again the heuristic correctly avoids the coup potential but fires the enemy event. **A good player would space AIW**, not headline it for the event to fire.

- **AR1 USSR:** Nuclear Test Ban (4ops) → Ops → UK, Venezuela, Algeria, Congo (Space 30%, Ops 22%)

> **EXPERT (AR1 T7):** NTB event fires (raises DEFCON, USSR VP). Model chose Ops (22%) over Space (30%) by narrow margin — Ops into UK (stability 5, US stronghold) is wasted ops. UK at this point has USSR+0, US+14 — placing 1 influence there is meaningless when it costs 4+ to reach parity. **Ops inefficiency: never place influence in a country you can't realistically contest.**

- **AR1 US:** ABM Treaty (4ops) → Ops → Brazil, Venezuela x2, Algeria (94%)

> **EXPERT (AR1 T7 US):** ABM Treaty event raises DEFCON benefiting both but favoring USSR at low DEFCON. Heuristic correctly plays for ops. Targeting Brazil and Venezuela continues the SA spread.

- **AR2 USSR:** Indo-Pakistani War → Ops → Brazil x2 (20% Ops/Space/Coup each)

> **EXPERT (AR2 T7):** Highly uncertain MCTS — all four options within 5% of each other. IDK event is a coup in Pakistan or India. At DEFCON-4, coup is safe. Model chose Ops into Brazil. 

- **AR2 US:** Arms Race (3ops) → Ops → W. Germany, Chile, S. Africa (98%)

> **EXPERT (AR2 T7 US):** Arms Race event gives VPs to the side with more MilOps. Playing for ops into West Germany (long overdue), Chile, S. Africa. W. Germany is critical — this should have been invested in much earlier.

- **AR3 USSR:** Five Year Plan (3ops, US card) → Ops → Chile, S. Africa x2 (35% Ops)

> **EXPERT (AR3 T7):** Chile and South Africa again. FYP correctly played for ops.

- **AR4 USSR:** East European Unrest (3ops, US card) → Ops → W. Germany, Chile, S. Africa (35% Ops, 26% Space)

> **EXPERT (AR4 T7):** EEU event removes USSR influence from 3 E. European countries — correctly played for ops. W. Germany investment continues.

- **AR5 USSR:** Sadat Expels Soviets (3ops, US card) → Space (46%) or Ops (35%)

> **EXPERT (AR5 T7):** SES event removes all USSR influence from Egypt and gives US a BG. Correctly played for Ops/Space. Model chose Ops into W. Germany and S. Africa.

**Turn 7 Summary:** VP drops slightly (T7 NTB event fired). USSR still leads by ~7 VP. Europe (W. Germany) finally getting attention. Chile/South Africa fixation continues.

---

### Turn 8 — Late War

**Headlines:**
- **USSR** plays Glasnost (4ops, USSR starred) → Headline (16%, Space 41%, Coup 21%)
- **US** plays Che (3ops, USSR starred) → Headline (92%)

> **EXPERT (Headlines T8):** Glasnost event raises DEFCON and gives USSR VP. MCTS preferred Space (41%) but chose Headline (16%). Glasnost is strong when DEFCON is low (bigger VP swing). VP: 6→8 (USSR+2). 
>
> US headlines Che again (already spaced T5) — wait, Che is starred so it was removed after T5 space. This must be a second copy or the engine allows re-draw. Che event fires (USSR gets 2 coups in Africa/CA). VP: 8→10 (USSR+2). **Two USSR events fired back-to-back in headlines again.**

- **AR1 USSR:** Aldrich Ames Remix (3ops, USSR starred) → Ops → E. Germany, France, Angola (21% Ops, 16% Space, 15% Coup)

> **EXPERT (AR1 T8):** AAR event reveals entire US hand and discards their best card. Incredibly powerful. MCTS chose Ops (21%) over Event (likely low). **Mistake #5: Aldrich Ames Remix is arguably the strongest single card event in Late War for USSR — the intelligence gain plus forced discard is game-altering. Playing it for ops into East Germany is a catastrophic misuse of a premium card.**

- **AR1 US:** Soviets Shoot Down KAL-007 (4ops, US starred) → Ops → Angola x4 (95%)

> **EXPERT (AR1 T8 US):** KAL-007 event gives US 2VP and influence if fired. Heuristic plays for ops into Angola x4. Angola by this point is already contested — 4 ops into one country is inefficient. KAL-007 event would have given 2 free VP.

- **AR2 USSR:** How I Learned to Stop Worrying (2ops) → Ops → E. Germany, W. Germany

> **EXPERT (AR2 T8):** HILTSW event sets DEFCON to 2. At DEFCON-4, setting to 2 is risky but manageable. Model chose Ops (21%) over Space (57%). Continuing Europe work.

- **AR3-8:** Both sides focus entirely on Eastern/Western Germany and France.

> **EXPERT (T8 late):** The late-game collapse into East Germany and France fixation mirrors the earlier South Africa fixation. By end of T8, East Germany shows USSR+34, US+22 — massive bilateral over-investment in a single European BG. West Germany: USSR+13, US+20 (US leading). France: USSR+11, US+12 (contested). 
>
> The Europe fight in T8 is the right strategic territory (European scoring could swing the game), but both sides neglecting the rest of the board shows tunnel vision.

**Turn 8 Summary:** VP stays at 10 USSR. Aldrich Ames wasted for ops — biggest late war error.

---

### Turn 9 — Late War

**Headlines:**
- **US** plays Wargames (4ops, Neutral starred) → Headline (Ops 84%, Space 12%)
- **USSR** plays Brush War (3ops) → Headline (36%, Space 33%)

> **EXPERT (Headlines T9):** Wargames event: requires DEFCON=2, ends the game immediately with a VP win for the side with more VP. At VP=10 USSR, firing Wargames as US would end the game (US would need to be winning). Heuristic played it for Headline (Ops at 84% was preferred) — but the event couldn't fire since DEFCON was not 2. Smart by heuristic to not fire it. Brush War headline by USSR for the event is reasonable.
>
> VP jumps: 10 → 13 (USSR+3) from Wargames (even as non-event? or from Brush War coup success). Likely Brush War event fired successfully in a key country.

- **AR2 USSR:** OPEC (3ops) → Ops → E. Germany x2, France (Space 31%, Ops 21%)

> **EXPERT (AR2 T9):** OPEC event could give USSR VP for African oil control. At this point USSR controls Nigeria, Congo, Angola — OPEC event might give 3-4 VP. Model chose Ops (21%) vs Space (31%). **Missed OPEC event again** — this was missed in T4 and now T9.

- **AR3 USSR:** Olympic Games → Ops → E. Germany x2 (Space 27%, Ops 14%)

> **EXPERT (AR3 T9):** OG event forces boycott decision. Model chose Ops.

- **AR4 USSR:** Liberation Theology (2ops, USSR) → Space (42%) or Ops (20%)

> **EXPERT (AR4 T9):** LT event spreads USSR influence in Central America (3 places, 1 each). Space was model's top choice (42%) but chose Ops. The difference here is minimal — 2-op card either way.

**Turn 9 Summary:** VP: 13 USSR. Model solidifying Germany position.

---

### Turn 10 — Final Turn

**Headlines:**
- **US** plays ABM Treaty (4ops) → Headline (81%)
- **USSR** plays Iranian Hostage Crisis (3ops, USSR starred) → Headline (51%)

> **EXPERT (Headlines T10):** ABM Treaty headline fires — DEFCON up, both get VPs. IHC event is strong for USSR (US hand disrupted). Both headline choices are reasonable.
>
> VP: 16 USSR (ABM fires), then IHC fires: 15 USSR (-1 from IHC offsetting something). 

- **AR1 USSR:** Pershing II Deployed (3ops, USSR starred) → Ops → E. Germany x2, France (Coup 14%)

> **EXPERT (AR1 T10):** P2D event: -1 VP for each Western European country US controls, +2VP for each NATO country USSR has influence in. This could be worth 5-8 VP in late game. MCTS at 27% Ops, 16% Ortega, 14% Coup — showed uncertainty. Playing it for ops when the event could win the game shows the model's persistent undervaluation of VP-generating events. **Mistake #6: Pershing II Deployed event could have closed the game by amplifying the lead.**

- **Remaining T10 ARs:** Both sides fighting in East/West Germany with diminishing returns. VP gradually ticks down from 15 to 14 as US gets slight scoring bonuses.

**Final VP:** 27 USSR (the vp=14 at last decision point, plus end-of-game scoring adds up to 27 total USSR advantage). Game ends with USSR winning by VP threshold.

---

## Top 5 MCTS/Model Blind Spots

### 1. Persistent Card Event Under-Valuation (Multiple Cards)
**Turns:** T2, T4, T5, T8, T9  
**Cards:** Warsaw Pact Formed, Quagmire, Willy Brandt, Aldrich Ames Remix, OPEC (x2)  
**Pattern:** MCTS repeatedly chose Ops over firing powerful USSR events. Visit distributions showed 60-80% confidence in Ops when expert analysis rates the event as 2-3x more valuable. The model appears to have learned that "Ops are safe" and discounts hard-to-evaluate event chains.

**Implication for Training:** Need games with explicit event-value labels or teacher targets on positions where "fire the event" is clearly correct. The value head is not properly pricing multi-step event consequences.

### 2. South Africa / Chile Fixation (Turns 5-8)
**Pattern:** Both sides (USSR MCTS and US heuristic) repeatedly targeting South Africa and Chile even after the strategic value diminished. By end of T7, South Africa had USSR+29, US+16 — an extreme over-investment from both sides. The model "learned" South Africa as a high-value target from training data but didn't recognize when marginal influence there was irrelevant.

**Implication for Training:** Country-level feature representation may need regional scoring signals as context. The model doesn't understand that the 30th influence point in South Africa is worth near-zero marginal VP.

### 3. Europe Under-Investment Until T7
**Pattern:** West Germany barely contested through T6 (USSR+2, US+0 at T5 start). Europe is the most VP-dense region but both sides neglected it for Asia/Africa early. MCTS correctly started investing in T7-8 but too late to shift the European balance.

**Implication for Training:** Need stronger geographic diversity in training positions. Value head should discount games where Europe is ignored.

### 4. Headline Safety Failures (Heuristic US, but indicative)
**Pattern:** The heuristic US repeatedly headlined USSR-beneficial cards (Duck and Cover T1, Korean War T2, We Will Bury You T6, Arab-Israeli War T7). While these are heuristic errors, MCTS also headlined Duck and Cover in T1 for USSR (15% visit weight — not chosen but considered).

**Implication for Training:** The model's understanding of headline interaction (when both players fire events simultaneously) may be underdeveloped. Headline phase labeling quality matters.

### 5. No Space Race Investment (Either Side)
**Pattern:** Neither side completed any Space Race advancement through the entire 10-turn game (space_ussr=0, space_us=0 throughout). Space Race gives VP bonuses and special abilities (e.g., preventing opponent event fires). Despite 25-45% Space visit weights appearing frequently, the model never committed. This may reflect insufficient Space Race value calibration or the heuristic opponent not creating pressure.

**Implication for Training:** Self-play games against non-space-racing opponents will perpetuate this pattern. Consider adding space race opponents in benchmark suite.

---

## Top 5 Things MCTS Did Well

### 1. Correct Opponent Card Handling
MCTS consistently played opponent (US) cards for Ops rather than triggering enemy events. Examples: Marshall Plan T1 (64% Ops), NATO T2 (49% Ops), Alliance for Progress T6 (46% Space). The model has learned the fundamental principle of card management.

### 2. DEFCON Awareness at Crisis Points
When DEFCON dropped to 2 (T2, T3), MCTS correctly avoided coup actions despite having 10-14% coup visit weights. The model knows that a DEFCON-1 nuclear war loss is catastrophic and avoids it.

### 3. Africa Regional Dominance
Despite the over-investment, USSR genuinely won Africa by controlling Nigeria, Congo, Ethiopia, Angola, Zimbabwe, Botswana, Mozambique. The Africa-first strategy is legitimate and the model executed it with high confidence. Africa scoring (had it been played/tracked) would have been a large USSR advantage.

### 4. Value Head Calibration Early-to-Mid Game
Root values tracked the game narrative well: T1 val ~0.3 (USSR slight edge), T3 val approached 0 (tied VP), T4-6 val climbed to 0.5-0.8 (USSR dominating). The model's self-assessment matched the actual game trajectory.

### 5. High-Confidence Correct Decisions
Many individual decisions showed 80-99% visit concentration on the correct action with fast MCTS convergence (2000 sims). For example: Five Year Plan Event (81%), Suez Crisis Event (82%), Independent Reds Event (93%), Sadat Expels Soviets for Ops (83%). The model's high-confidence decisions are generally correct.

---

## Key Training Recommendations

Based on this game:

1. **Event value cueing:** Create teacher targets specifically for positions where a high-value event (Quagmire, Aldrich Ames, Warsaw Pact, Pershing II) is available. Label these positions with event-firing as the correct action.

2. **Regional saturation detection:** Add a feature indicating "marginal ops value in already-dominated country" — the model should learn to diversify once a territory is controlled.

3. **Headline interaction training:** Add explicit labels for headline choices emphasizing that opponent-beneficial events should not be headlined.

4. **Space race baseline:** Run some games with forced space race advancement to generate training data where space investments are made, giving the model examples of space race decision making.

5. **Europe scoring pressure:** Add curriculum where Europe Scoring is imminent, forcing the model to learn European BG prioritization.

---

*Analysis generated from seed 77777 game trace. Model: v106_cf_gnn_s42. Total decision points: 155.*
