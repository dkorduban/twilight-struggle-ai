# Spec: Experimental Heuristic Search Roadmap

Updated implementation plan for the isolated heuristic-search stack after the
first end-to-end baseline already landed in:

- `cpp/experimental/`
- `python/experimental/`

This version is aligned to the full `long-prompts/principled-heuristic.md`
document and prioritizes **strength per engineering week**, not maximal feature
completeness.

---

## 0. OODA Loop

Development should run in a fixed Observe-Orient-Decide-Act loop, not a
one-shot sequence:

1. Observe:
   - re-read the local experimental `AGENTS.md` policy before each new loop
     iteration so autonomy rules, cleanup discipline, and stop conditions stay
     current
   - re-read the full prompt and the latest benchmark / trace output
   - extract the dominant loss modes by seat, turn window, and terminal cause
2. Orient:
   - update this plan and the local experimental `AGENTS.md` rules if the
     highest-ROI bottleneck changed
   - reduce the problem to one seat, one failure family, and one metric
3. Decide:
   - select the single highest-ROI intervention
   - prefer proposal/eval fixes before deeper tree complexity
4. Act:
   - implement the smallest coherent patch
   - benchmark again on meaningful samples using the active evidence ladder:
     - `50` games per seat: screening only
     - `200` games per seat: tentative candidate validation
     - `800` games per seat: baseline promotion / rejection
   - do not use any sample below `50` games per seat for ranking, promotion,
     or rejection
5. Loop:
   - re-read the local policy again before restarting so the next iteration
     uses the current autonomy rules and bottleneck framing
   - after each completed OODA pass, re-read the local policy before the next
     benchmark, tuning run, or code change, even if the loop is continuing
     without a human-visible pause
   - if the current tier goal is not yet met, restart from step 1 immediately

Tiered goal order:

1. decisively beat `MinimalHybrid` in isolated experimental matchups across both seats
2. only after that, start the same loop again for `v266_sc`, first repairing the
   learned-policy matchup path and then iterating until that matchup is also
   decisively winning

This means proposal/value quality is higher priority than deeper tree complexity
until tier 1 is satisfied.

Evidence policy:

- `50` games per seat are screening runs and should not by themselves settle
  branch promotion
- `200` games per seat are the tentative-candidate threshold
- `800` games per seat are the promotion / rejection gate for a new working
  baseline branch
- prefer fixed explicit seed sets across branch comparisons

---

## 0. Current Status

The current experimental stack already has:

- isolated build targets and Python wrapper code
- a fresh evaluator that is not based on `minimal_hybrid`
- exact legality and exact action application through `tscore`
- exact callback-script solving for callback-driven event branches
- a self-contained experimental runner
- full-game heuristic self-play that reaches turn 10
- a focused regression smoke test
- an isolated experimental ISMCTS-style root search path
- a fast default runtime path again after narrowing exact post-UCT refinement:
  full self-play is currently around `~9.25s`, which is comfortably below the
  new `~30s/game` budget, so moderate search widening is now admissible if it
  produces real both-seat strength gains

What it does **not** have yet:

- belief-aware evaluation
- hierarchical card/mode/template proposal generation
- progressive widening / PUCT tree search
- prior / q0 child initialization
- imperfect-information ISMCTS with support-mask input
- a teacher-search API for data generation
- decisive strength against `MinimalHybrid`
- a working experimental matchup path against `v266_sc_scripted.pt`

Current strength snapshot from the latest clean explicit-seed 100-game seat
runs:

- `search` as USSR vs `minimal` as US:
  - `52-48`
  - average turn `9.43`
  - average final VP `-0.4` in USSR-positive convention
  - terminal causes:
    - `turn_limit`: `78`
    - `europe_control`: `21`
    - `defcon1`: `1`
- `search` as US vs `minimal` as USSR:
  - `10-90`
  - average turn `7.62`
  - average final VP `15.25` in USSR-positive convention
  - terminal causes:
    - `europe_control`: `45`
    - `turn_limit`: `36`
    - `vp`: `14`
    - `defcon1`: `3`
    - `scoring_card_held`: `2`

Latest accepted working baseline after the newer Europe-support proposal patch:

- key accepted change:
  - add a cheap Europe non-battleground support / country-count pressure bonus
    in the proposal `PrepScoring` lane
  - keep it as a lightweight proposal signal, not a new heavy planner branch
- accepted default setting:
  - `proposal_europe_support_pressure_bonus = 0.50`
- clean explicit-seed `50`-game validation on that branch:
  - `search` as USSR vs `minimal` as US:
    - `31-19`
    - average turn `9.12`
    - average final VP `3.88` in USSR-positive convention
    - terminal causes:
      - `turn_limit`: `34`
      - `europe_control`: `13`
      - `defcon1`: `2`
      - `vp`: `1`
  - `search` as US vs `minimal` as USSR:
    - `7-43`
    - average turn `7.80`
    - average final VP `14.56` in USSR-positive convention
    - terminal causes:
      - `europe_control`: `19`
      - `turn_limit`: `19`
      - `vp`: `9`
      - `defcon1`: `1`
      - `scoring_card_held`: `2`

Interpretation:

- this branch materially improved the USSR seat over the older authority
  baseline (`62%` vs `52%`)
- it also preserved the post-patch US-side improvement at `14%`, which is still
  poor but better than the older `10%` authority baseline
- this is now the working default baseline for the next OODA pass

Latest OODA observation after the corrected `800+800` authority benchmark:

- the earlier strong USSR-seat result was too optimistic; the clean explicit
  batch says the USSR seat is only slightly above parity
- the old terminal-cause split was polluted by a classification bug:
  mid-turn `vp_threshold` wins were being reported as `europe_control`
- the corrected clean `800+800` baseline is the new authority for loss-mode
  diagnosis:
  - `search` as USSR vs `minimal` as US:
    - `450 / 800 = 56.25%`
    - `avg_turn = 9.363`
    - `avg_final_vp = +1.627`
    - causes:
      - `turn_limit = 605`
      - `vp = 170`
      - `defcon1 = 23`
      - `wargames = 2`
  - `search` as US vs `minimal` as USSR:
    - `98 / 800 = 12.25%`
    - `avg_turn = 7.59`
    - `avg_final_vp = +14.83`
    - causes:
      - `vp = 468`
      - `turn_limit = 290`
      - `scoring_card_held = 33`
      - `defcon1 = 8`
      - `wargames = 1`
- on that corrected baseline, the weak US seat is mostly ordinary `vp` and
  `turn_limit` losses, plus a meaningful `scoring_card_held` tail
- the added global non-battleground broadening was still the wrong fix; it
  regressed both seats and should stay rejected
- exact one-step region-score deltas were worth keeping
- evaluator-side Europe cliff awareness was cheap enough to keep
- planner-side Europe-cliff deltas and exact event-mode ranking were too
  expensive for the target budget and did not improve the weak seat enough

Observed failure pattern after the corrected loss split:

- the weak seat is not primarily dying to Europe-control auto-losses
- the dominant corrected families are:
  - generic `vp` losses
  - `turn_limit` losses from finishing behind on final score
  - a small residual `scoring_card_held` tail
- proposal/evaluation work should therefore optimize general scoring quality
  and scoring-card play, not just Europe denial
- scoring-card handling had a real experimental bug:
  - when `must_play_scoring_card(...)` became true, proposal generation could
    still miss the scoring cards because it first truncated to a top-`k` card
    shortlist, then filtered the already-truncated actions
  - that could leave the proposal list empty and fall through to a generic
    legal fallback, producing avoidable `scoring_card_held` losses
  - this is now fixed by directly enumerating scoring-card event actions in the
    must-play case
  - a known failing US seed that previously ended `scoring_card_held` now
    continues to a normal VP loss

Latest OODA update after the next two candidate branches:

- a targeted planner-side Europe-control-denial patch looked promising on a
  tiny `10+10` probe (`70%` USSR seat, `20%` US seat), but failed a broader
  `20+20` explicit-seed probe (`45%` USSR seat, `15%` US seat), so it is
  rejected
- a wider-root config (`proposal_limit=12`, `search_candidate_limit=2`) is
  also rejected under the older tighter runtime gate because it left straggler
  games before finishing a small probe cleanly; with the relaxed `~30s/game`
  budget it can be reconsidered, but only if it improves both-seat strength on
  a meaningful sample
- a local sweep of the new `proposal_europe_support_pressure_bonus` around the
  first accepted value found:
  - `0.50`: best local both-seat result on a `10+10` explicit-seed sweep
  - `0.75`: clearly worse on the US seat
  - `1.00`: improved USSR seat but not US seat
  - `1.25`: too unstable, regressing the USSR seat badly
- a follow-up US-side-only breadth probe on top of the accepted `0.50`
  baseline:
  - `proposal_limit_us=12` reached `15%` on a `20`-game explicit-seed US-seat
    sample, but the gain over the new `14%` baseline is too small and too noisy
    to accept yet
  - treat it as a candidate for later confirmation, not a new default

So the next loop should not widen the root or add heavy planner-side Europe
logic again without stronger evidence. The active next step is cheaper than
that:

1. rerun the post-fix baseline on at least `200+200`, then `800+800`, before
   treating old `scoring_card_held` rates as current
2. compare the post-fix baseline against the most plausible screened branches
   on matched seeds:
   - `proposal_limit_us = 12`
   - `proposal_europe_support_pressure_bonus = 0.0`
3. only keep branches that improve both seats enough to justify their runtime
   under the `~30s/game` budget
4. from the accepted `proposal_europe_support_pressure_bonus = 0.50` baseline,
   prioritize US-side-only breadth / weight tuning for generic scoring/play
   quality that cannot damage the now stronger USSR seat

So the current code is a **working isolated heuristic/ISMCTS baseline**, but it
is still below the tier-1 target and still has an unresolved learned-policy
integration bug. The active loop priority is now:

1. use the relaxed runtime budget to search a broader strength/runtime frontier
   while preserving clean benchmarkability
2. retune and re-evaluate both seats until the heuristic decisively beats
   `MinimalHybrid` across both seats
3. only then reopen the learned-policy matchup path and start the tier-2 loop

---

## 1. Hard Constraints

Keep these constraints unchanged:

- do not break or redesign existing `cpp/tscore` behavior
- do not change existing `bindings/tscore_bindings.cpp`
- do not change existing `python/tsrl` behavior
- keep new work isolated to:
  - `cpp/experimental/`
  - `python/experimental/`
- use additive root/test/build edits only when necessary

The experimental stack must continue to compile rich internal plans down to:

1. one top-level `ts::ActionEncoding`
2. one deterministic `PolicyCallbackFn` replay script

This is still the right boundary.

---

## 2. Design Principles From The Prompt

The prompt’s strongest ideas are:

1. exact `scoreNow(region)` terms with urgency weighting
2. explicit structural board terms:
   - battleground pressure
   - access
   - overcontrol
   - MilOps edge
   - DEFCON edge
   - space edge
   - China edge
3. residual special-card valuation:
   - persistent flags
   - paired-card threats
   - special cards in hand
   - information value under belief, not determinization truth
4. hierarchical proposal generation:
   - card
   - mode
   - tactical template
   - concrete action
5. bounded materialization:
   - beam search for influence allocations
   - shortlists for coups, realigns, and event choices
6. search integration:
   - progressive widening
   - priors
   - q0 / pseudo-count child init
7. ISMCTS-specific handling:
   - support-mask-compatible determinization
   - availability counts
   - no knowledge leakage into evaluator terms

Those are the right targets. The plan below is the shortest practical path to
them.

---

## 3. Gap Analysis Vs Current Code

### 3.1 Evaluator gaps

Current evaluator already has:

- VP
- final-scoring proxy
- board-control-ish terms
- space / MilOps / DEFCON / China
- crude hand-shape value

Missing or underdeveloped:

- scoring urgency from live/gone/known/reshuffle-aware state
- exact `scoreNow(region)` terms weighted per prompt
- persistent flag residuals
- paired-card threat terms
- special-hand card value
- information-card value from belief/support mask
- region-specific access and battleground-pressure helpers

### 3.2 Proposal gaps

Current planner still does:

- flat `enumerate_actions(...)`
- light local ranking
- exact one-ply afterstate scoring

Missing:

- card/mode/template hierarchy
- dedicated event candidate generation
- beam-search influence allocations
- specialized coup and realignment proposal families
- candidate priors and q0 values

Observed concrete proposal pathology:

- US-side traces repeatedly spend Ops on battleground-only allocations in
  Europe / Asia / Africa while under-sampling non-battleground support
  countries, country-count stabilizers, and safer scoring-prep lines
- the influence beam truncation is likely too aggressive and too
  battleground-biased for the current marginal score

### 3.3 Search gaps

Current stack has no real search tree. It is effectively:

- shortlist legal actions
- exact one-ply evaluate top few
- choose best

Missing:

- search node stats
- progressive widening
- PUCT/UCT over materialized children
- transposition/cache strategy
- rollout/deeper-search integration

### 3.4 Imperfect-information gaps

Current stack is still effectively perfect-information in its planner/evaluator.

Missing:

- `ExperimentalObservation`
- `BeliefSummary`
- support-mask input bridge
- availability-aware ISMCTS bookkeeping
- info-card valuation from belief rather than hidden truth

### 3.5 Tooling gaps

Missing:

- proper teacher-search entrypoints
- benchmark harnesses against legacy agents
- weight-tuning and offline-search-target generation pipeline
- clean Python import path that avoids collision with the repo’s existing
  top-level `experimental/` package

---

## 4. Prioritized Roadmap By ROI

This is the updated plan of work. The ordering is by:

1. biggest expected strength gain
2. lowest architecture risk
3. compatibility with the current isolated baseline

### Phase A: Make The Evaluator Actually Prompt-Shaped

Budget:

- `1-2` focused engineering days

Goal:

- turn the current evaluator from “reasonable board heuristic” into a true
  TS-specific heuristic value function

Implement:

- exact `scoreNow(region)` terms:
  - Europe
  - Asia
  - Middle East
  - Central America
  - South America
  - Africa
  - Southeast Asia
- scoring urgency:
  - `0` if scoring is gone
  - high if known in current hand
  - medium if live unseen
  - reduced if only after reshuffle
- region weights from the prompt as initial defaults
- explicit battleground pressure
- explicit access swing
- explicit overcontrol
- China edge split into:
  - available
  - unavailable
  - Asia-live bonus
- persistent-flag residuals:
  - Containment
  - Brezhnev
  - Red Scare/Purge
  - Vietnam Revolts
  - North Sea Oil
  - Yuri and Samantha
  - Latin American Death Squads
  - Iran-Contra
  - Chernobyl
  - NORAD
  - Quagmire
  - Bear Trap
  - Cuban Missile Crisis
  - Nuclear Subs
  - SALT
  - We Will Bury You
  - U2
  - Formosan
  - Shuttle
  - NATO
  - US/Japan
  - Willy Brandt
  - Reformer
  - Flower Power
- paired-card threats:
  - Camp David vs Arab-Israeli War
  - John Paul II vs Solidarity
  - Hostage Crisis vs Terrorism
  - Iron Lady vs Socialist Governments
  - AWACS vs Muslim Revolution
  - North Sea Oil vs OPEC

Acceptance:

- evaluator has clear sign-correct unit tests
- self-play still runs to turn 10
- obvious special-flag scenarios move the value in the intended direction

### Phase B: Replace Flat Proposal Ranking With Prompt-Style Card/Mode/Template Generation

Budget:

- `1-2` focused engineering days

Goal:

- fix the current biggest practical weakness: poor candidate generation, especially
  for the US side in mixed-seat games

Implement:

- card scoring by best plausible use:
  - event
  - ops
  - space
- top-card shortlist (`CARD_K`)
- top-mode shortlist per card (`MODE_K`)
- tactical templates from the prompt:
  - `COUP_BG`
  - `COUP_NONBG_MILOPS`
  - `REALIGN_LINCHPIN`
  - `DEFEND_CONTROL`
  - `BREAK_CONTROL`
  - `GAIN_ACCESS`
  - `PREP_SCORING`
  - `OVERPROTECT_BG`
- candidate materialization limits by template family
- priors from proposal scores
- keep exact scripted execution only for the finally chosen action

Acceptance:

- self-play stays sane to turn 10
- mixed-seat traces stop showing obvious tactical misses at root
- matchup results versus `MinimalHybrid` improve before touching deeper search

### Phase C: Iterate The Loop Until Tier 1 Is Met

Budget:

- ongoing until `MinimalHybrid` is beaten decisively

Goal:

- run the execution loop repeatedly instead of moving prematurely to belief/sc266 work

Current subgoal ordering inside tier 1:

1. fix US-side Europe-control losses
2. fix US-side held-scoring losses
3. only after that, retune both seats jointly on 50-100 game samples

Implement / repeat:

- inspect the latest mixed-seat matchup traces
- identify the dominant failure mode:
  - evaluator sign/weight issue
  - proposal miss
  - search selection bug
  - callback/event-choice blind spot
- make the smallest highest-ROI fix
- re-benchmark

Immediate diagnostic rules:

- if `europe_control` dominates US-side losses, prioritize proposal diversity,
  country-count / support heuristics, and Europe-defense shaping
- if `scoring_card_held` persists above noise, increase scoring backlog pressure
  and replay those exact seeds before deeper search changes
- if `vp` losses dominate after the Europe fix, then revisit evaluator urgency
  and event-mode ranking

Acceptance:

- `MinimalHybrid` loses clearly in both seat assignments over repeated seeds
- only then move on to the second loop against `v266_sc`

### Phase D: Repair Learned-Policy Integration And Run The Second Loop

Budget:

- after tier 1 is met

Goal:

- get the experimental runner to play cleanly against `v266_sc`
- then keep repeating the same analysis / implementation / benchmark loop until
  that matchup is decisively winning too

Implement:

- fix the experimental learned-agent integration crash
- verify headline and non-headline behavior against the existing native learned tool
- benchmark both seat assignments against `v266_sc`
- inspect traces and restart the same loop if the result is not yet strong enough

Acceptance:

- learned-policy matchup path is stable
- `v266_sc` is beaten decisively across repeated seeds and both seats

Why this is first:

- it directly improves every later search layer
- it does not require new interfaces
- it is the single largest current gap to the prompt

### Phase B: Add Special-Hand And Info-Card Value

Budget:

- `1` engineering day after Phase A

Goal:

- make the evaluator respect cards whose main value is not immediate board delta

Implement:

- special-hand terms for:
  - Wargames
  - Missile Envy
  - Defectors
  - UN Intervention
  - CIA Created
  - Lone Gunman
  - Aldrich Ames Remix
  - Cambridge Five
  - Our Man in Tehran
  - Star Wars
  - Ask Not
  - Grain Sales
  - China-transfer cards
- first perfect-information version:
  - exact or approximate card-in-hand value using full state
- then belief-facing interface:
  - route these terms through `BeliefSummary`, not sampled truth

Acceptance:

- exact-state heuristic chooses or values these cards more sensibly in targeted
  fixtures
- the API shape for belief-aware special-card value exists even if the first
  belief model is simple

Why this is second:

- the prompt is explicit that these cards need bespoke treatment
- this materially improves move quality even before tree search

### Phase C: Replace Flat Action Ranking With Hierarchical Proposal Generation

Budget:

- `2-4` engineering days

Goal:

- stop scoring every legal action flat and instead propose a compact, strong
  candidate set

Implement:

- `score_card_use(...)`
- card-level choice:
  - event
  - ops
  - space
- mode-level scoring:
  - `estimateBestEventMode`
  - `estimateBestOpsMode`
  - `estimateSpaceMode`
- ops templates:
  - `COUP_BG`
  - `COUP_NONBG_MILOPS`
  - `REALIGN_LINCHPIN`
  - `DEFEND_CONTROL`
  - `BREAK_CONTROL`
  - `GAIN_ACCESS`
  - `PREP_SCORING`
  - `OVERPROTECT_BG`
- event candidate generators for meaningful choice cards
- dedicated coup candidate generation
- dedicated realignment beam search
- dedicated influence-allocation beam search
- candidate deduplication by resulting action key
- softmax prior attachment
- q0 from quick exact afterstate eval

Target defaults from the prompt:

- `CARD_K = 5`
- `MODE_K = 2`
- `MAX_CHILD_CANDS = 12`
- `COUP_K = 4`
- `REALIGN_K = 4`
- `INF_FINAL_K = 6`

Acceptance:

- root candidate sets stay small and deterministic
- candidate quality is visibly better than flat `enumerate_actions` ranking
- runtime remains good enough for self-play smoke

Why this is third:

- this is the key bridge between evaluator quality and real search
- it reduces branching before any tree-search work starts

### Phase D: Add Real Search For Perfect-Information States

Budget:

- `2-4` engineering days

Goal:

- move from exact one-ply to bounded real search under the prompt’s recipe

Implement:

- `SearchNode` / edge stats:
  - visits
  - value sum
  - prior
  - q0
  - pseudo visits
- progressive widening:
  - `K = 4 + floor(1.5 * N^0.40)`
- selection:
  - PUCT over materialized children
- expansion:
  - one new child from proposal generator when under widening cap
- child init:
  - prior
  - q0
  - pseudo-count initialization
- backup:
  - root-player value convention
- exact afterstate child application for now
- search result object mirroring existing `SearchResult` where practical

Important:

- do **not** add `quickApplyApprox` before this works
- do **not** add wide/deep rollouts first
- keep the first tree exact and small

Acceptance:

- perfect-information search beats the current exact one-ply planner in direct
  mirrors at fixed budget
- root child priors and q0 values are observable in logs/results

Why this is fourth:

- it is the first point where the prompt’s “heuristic search engine” really
  exists rather than a strong action selector

### Phase E: Support-Mask / Belief Integration

Budget:

- `2-4` engineering days

Goal:

- make the heuristic usable in imperfect-information settings without knowledge
  leakage

Implement:

- `ExperimentalObservation`
- `BeliefSummary`
- bridge from existing support-mask sources into experimental inputs
- simple belief statistics:
  - `prob_card_live`
  - `prob_card_in_opp_hand`
  - `prob_card_before_reshuffle`
- support-compatible determinization
- exact-state evaluator wrappers replaced, where needed, with belief-facing
  versions

Non-goal for the first pass:

- full particle filter
- sophisticated belief update machinery

Acceptance:

- hidden-info value terms no longer read hidden truth directly
- info cards become stronger/weaker as support masks narrow/widen

Why this is fifth:

- the prompt is right that this matters a lot
- but it is lower ROI than perfect-information strength until the search core
  exists

### Phase F: Heuristic ISMCTS With Availability Counts

Budget:

- `2-4` engineering days

Goal:

- implement the prompt’s imperfect-information search shape, not just
  determinized one-ply play

Implement:

- one determinization per simulation from `ExperimentalObservation`
- support-mask-compatible hidden sampling
- availability counts per edge
- availability-aware UCB/PUCT denominator
- progressive widening over candidates legal in the sampled state

Acceptance:

- deterministic fixed-seed behavior
- no action-key explosions
- sane partial-info smoke tests

Why this is sixth:

- this is where the prompt’s ISMCTS-specific advice really lands
- but it is not the first strength bottleneck compared to Phases A-D

### Phase G: Teacher Search And Data Generation

Budget:

- `1-2` engineering days

Goal:

- turn the heuristic engine into a practical baseline for BC and search targets

Implement:

- perfect-information teacher search API first
- Python wrappers for:
  - single state
  - traced game positions
  - batch position evaluation/search
- result payload:
  - best action
  - root value
  - root priors / visit distribution if tree search is active

Acceptance:

- Python can request heuristic search on a full known state
- outputs are easy to store alongside BC rows

Why this is seventh:

- it is the point where the heuristic becomes operationally useful for training

### Phase H: Optimization Passes Only After Search Works

Budget:

- ongoing

Only do these after the search engine above is in place:

- cache evaluator subterms
- precompute region/country masks
- incremental `quickApplyApprox`
- small-sample averaging for random events
- action/result transposition caches
- branch-specific callback-script memoization

This is explicitly lower priority than getting the search architecture itself
right.

---

## 5. What To Defer

These are reasonable to defer until the stronger baseline exists:

- exhaustive subset enumeration for rare event cards
- fancy belief models beyond support masks
- double progressive widening at chance nodes
- CMA-ES / SPSA tuning loops
- large-scale benchmark harnesses
- broad optimization of rollout depth / stochastic sampling

The prompt’s own ordering supports this:

- get evaluator shape right
- get proposal generation right
- add widening and priors
- only then optimize and tune

---

## 6. Recommended Time-Budgeted Targets

### If only `1-2` more days are available

Do:

- Phase A
- Phase B
- the minimum viable part of Phase C

Expected outcome:

- much stronger exact one-ply heuristic baseline
- better special-card and scoring-card behavior
- still no full search tree

### If `3-5` more days are available

Do:

- Phase A
- Phase B
- Phase C
- first half of Phase D

Expected outcome:

- strong proposal policy
- real perfect-information heuristic search
- useful baseline for teacher search and BC

### If `1-2` more weeks are available

Do:

- Phases A through G

Expected outcome:

- the strongest reasonable heuristic baseline under current architecture
- perfect-info teacher search
- support-mask-aware heuristic ISMCTS
- meaningful training-time baseline without disturbing legacy code

---

## 7. Immediate Next Implementation Order

The next concrete work items should be:

1. keep the current fast path intact
2. run clean paired-seat 50-100 game benchmarks against `MinimalHybrid`
3. inspect the losing-seat traces, starting with US-side `europe_control`,
   `vp`, and `scoring_card_held` losses
4. land the first US-side corrective pass:
   - reduce pure battleground tunnel vision in influence generation
   - add non-battleground support / country-count signals
   - tighten scoring-card backlog pressure
5. tune evaluator and proposal weights using:
   - paired seeds
   - both seats
   - black-box SPSA / random-search
6. repeat until `MinimalHybrid` is beaten decisively across both seats
7. only then repair learned-policy integration and start the `v266_sc` loop

This ordering is the best strength-per-time path from the current codebase.

---

## 8. Explicit Anti-Goals

Do not spend time on these before the roadmap above:

- porting or reusing `minimal_hybrid`
- redesigning legacy `tscore` APIs
- making the experimental runner perfectly mirror every legacy path detail
- tuning weights before evaluator/proposal/search structure is in place
- implementing wide approximations before exact small search works

The current baseline already proves the isolation strategy works. The strongest
next move is to make the evaluator and proposal policy match the prompt more
closely, then add real widening-based search on top.
