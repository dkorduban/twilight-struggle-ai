# Opus Analysis: Engine Correctness Pivot
Date: 2026-04-21 ~19:55 UTC
Question: Should the project pause all policy training (BC, PPO, self-play) and pivot to completing the DecisionFrame migration + reaching a defensible "~99%" engine rule correctness bar before resuming training? Sub-question: can Claude (via Claude Code tooling) drive a browser-based third-party TS engine (e.g. TSEspionage) as an independent oracle, and if not, what alternatives exist?

## Executive Summary

**Yes — pivot now.** Frame migration has three well-bounded remaining fallback callsites in `hand_ops.cpp` (cards 19/52/68) plus peripheral fan-out; total effort is ~1 week of focused C++. The 171 `SCORING_VP_MISMATCH` violations on the 51-game human corpus are the single clearest pre-training bar: until validator runs clean on scoring, every BC/PPO run is training on a VP-miscomputing world model, which is the same failure mode that turned 0.650 → 0.48 after Plan B. **Claude cannot reliably drive a live JS webapp as an oracle** (no Playwright-MCP server configured here, WebFetch is read-only and the two main "TS online" clients — Playdek and twilightstrategy.com — are auth-walled SPAs), but we do not need one: the authoritative oracles are already in-hand (TS_Rules_Deluxe.pdf + the 51-game human validator corpus + a rules-lawyer PDF pipeline), and a third source — scraped TSEspionage / Playdek replay *text* piped through the existing `validate_replays.py` — gives us a cheap way to expand oracle coverage 20-100x without any browser automation. **Recommendation: kill in-flight BC #109, pause #96 distill, freeze warmstart chain at v32, run a 3-week correctness sprint, then resume training from a certified engine.**

## Findings

### 1. Frame Migration — State and Remaining Work

**What's already done (per `project_frame_context_status.md` and code inspection):**
- `FrameKind` enum and `DecisionFrame` struct live in `cpp/tscore/decision_frame.hpp` with 11 frame kinds (TopLevelAR, SmallChoice, CountryPick, CardSelect, ForcedDiscard, CancelChoice, FreeOpsInfluence, NoradInfluence, DeferredOps, SetupPlacement, Headline).
- `GameState::frame_stack_mode` flag is exposed through the pybind layer (`bindings/tscore_bindings.cpp:848`) and wired into `apply_frame_ops_impl` at each card-event site.
- `kModelScalarDim = 40` has absorbed 8 frame-context features (source_card, budget_remaining, step_index, frame_stack_empty, etc.); the network consumes them and `FrameContextScalarEncoder` handles backward-compat with 32-dim legacy checkpoints.
- `bindings/tscore_bindings.cpp` exposes the full `DecisionFrame` Python API (lines 762-809): kind, acting_side, source_card, step_index, total_steps, budget_remaining, stack_depth, parent_card, eligible_n, criteria_bits.
- CMakeLists test suite includes `test_frame_parity.cpp` and `test_frame_regression.cpp` which already enforce frame-vs-legacy parity on a golden corpus.

**What still uses the legacy `apply_ops_randomly_impl` fallback** (verified via Grep on `cpp/tscore`):

| # | File:Line | Card | Context |
|---|-----------|------|---------|
| 1 | `hand_ops.cpp:405` | 32 (UN Intervention) | after discarding the paired opponent card |
| 2 | `hand_ops.cpp:518` | 52 (Missile Envy) | after claiming opponent's highest-ops card |
| 3 | `hand_ops.cpp:590` | 68 (Grain Sales to Soviets) | after US claims a random USSR card |

In all three, the pattern is identical:
```cpp
if (gs.frame_stack_mode && policy_cb == nullptr &&
    apply_frame_ops_impl(gs, frame_log, card_id, side, ops, rng)) {
    return {gs.pub, false, std::nullopt};   // frame path succeeded
}
apply_ops_randomly_impl(pub, side, ops, card_id, rng, policy_cb, frame_log);  // fallback
```

The fallback is reachable whenever (a) `frame_stack_mode == false` (legacy path), or (b) `policy_cb != nullptr` (MCTS leaf rollout, benchmarks, ISMCTS). That second case is the load-bearing one — **`mcts.cpp` has no references to `frame_stack_mode`, `DecisionFrame`, or `apply_frame_ops`** (I verified: zero matches). MCTS-driven decisions for cards 19/52/68 still randomize the mode and targets, which is GAP-006 ("free borrowed ops simplified"), marked PARTIAL in `engine_rule_gaps.md`.

**Estimated effort for full frame migration:**

1. **(2 days)** Replace the three callsites with a proper `apply_frame_ops_impl` that supports a policy callback path (currently `apply_frame_ops_impl` is guarded by `policy_cb == nullptr`). The cleanest design: promote the frame path to be the only path, and make `policy_cb` a sub-frame policy source that the frame dispatcher consults. Delete `apply_ops_randomly_impl` entirely once green.
2. **(2 days)** Wire `mcts.cpp` leaf expansion through the frame API. At the search frontier, MCTS currently builds an `ActionEncoding` directly; it needs to instead push/pop frames so sub-choices of card 19/52/68 (mode, country, realignment, etc.) become expandable search nodes. This is the high-value change — it also fixes GAP-006's MCTS leg.
3. **(1 day)** Extend `test_frame_parity.cpp` to cover cards 19/52/68 explicitly with a deterministic policy callback. Confirm zero behavioral diff between frame-on and frame-off across 1000 seeded rollouts, then flip the default to frame-always-on and retire `frame_stack_mode` as a toggle.
4. **(1 day)** Update `bindings/tscore_bindings.cpp` rollout functions (`rollout_model_vs_model_batched`, `play_game_scripted_vs_scripted`, etc.) to assume `frame_stack_mode=true` and remove the toggle from Python call sites. Search `python/tsrl` for `frame_stack_mode` assignments and prune.

**Total: ~6 working days = 1 calendar week.** Sequencing: step 1 → step 2 in parallel with step 3 → step 4.

### 2. Engine Correctness — Ranked Gap List

Authoritative sources:
- Most recent validator run: `results/analysis/validate_replays_20260421_111345.md` — 246 violations on 51 games, 6148 decisions.
- Audit of `v32_selfplay_seed42_greedy.txt`: `opus_analysis_20260421_085634_engine_bug_prioritization.md` — 9 real bugs out of 31 alleged.
- Category breakdown: `engine_rule_gaps.md` — 46 gaps, most marked DONE/PARTIAL.

**Ranked gaps blocking "99% defensible" status:**

| Rank | Source | Symptom | # affected | Severity |
|---:|---|---|---:|---|
| 1 | Validator | `SCORING_VP_MISMATCH` on card 1 (Asia Scoring) | 85 | **Critical** — VP model wrong ≈1.4× per game |
| 2 | Validator | `SCORING_VP_MISMATCH` on card 2 (Europe Scoring) | 65 | **Critical** — directly distorts end-game value targets |
| 3 | Validator | `TARGET_ILLEGAL` (67 total; card 5 top with 4) | 67 | High — indicates legal-action generator divergence |
| 4 | Validator | `SCORING_VP_MISMATCH` on card 80 (Africa Scoring) | 15 | High |
| 5 | Audit #4 | Card 22 Independent Reds: +1 to *all* eligible, should be *one* chosen | ≤1 per US game | High — gives US free domination points |
| 6 | Audit #9 | Card 56 South African Unrest: always does +2 SA AND +2 adj, should offer choice | ~1 per US game | Medium — misses strategic branch |
| 7 | Validator | `RESHUFFLE_EMPTY_DISCARD` | 5 | Low — edge case |
| 8 | Validator | `HEADLINE_ORDER_MISMATCH` | 3 | Low — already rare |
| 9 | GAP-006 (PARTIAL) | MCTS path still randomizes UN/Missile Envy/Grain Sales ops | every MCTS rollout | High — but fixed by §1 step 2 |
| 10 | GAP-043 | Cuban Missile Crisis reduced to permanent no-coup lock | ~1 game in 5 | Medium |
| 11 | `inconsistent-moves.md` audit residuals | 5 trace-formatter false positives (items 27-31) | all games | Cosmetic, but poisons future audits — fix Python formatter |

**Scoring resolver — why 171 violations?** The top-3 ranks are all the major region-scoring cards (Asia=1, Europe=2, Africa=80). The presence of 85+65+15 = 165 violations on *just* these three cards across 51 games means the scoring resolver is systematically wrong, not sporadically. Likely culprits to investigate (not yet confirmed):
- Battleground count for regions that treat subregions specially (Europe has sub-scoring, Asia has Taiwan flag, Southeast Asia has per-country VP).
- Shuttle Diplomacy / Formosan Resolution / China Card bonus not applied.
- Domination threshold math when both sides have Presence but neither has Domination (should be 0 VP diff, not Presence-Presence delta).
- VP cap (`max VP per scoring = +/- region total`) miscounted.

This investigation is the single highest-leverage unit of work in the pivot. If it's a one-line bug we get 165/246 violations for free.

**Testing protocol for "defensible 99%+":**

- (A) **Validator green on 51 human games:** `SCORING_VP_MISMATCH = 0`, `TARGET_ILLEGAL ≤ 5`, all remaining violations annotated with a rules-lawyer explanation committed to `docs/rules_decisions.md` (file does not yet exist — create it).
- (B) **Golden-log regression: 20 curated games from different eras** — current `tests/cpp/fixtures/` has them; extend to 50 and make `test_frame_regression.cpp` hash-compare every public-state transition.
- (C) **Per-card unit tests:** for all 110 non-promo cards, at least one test that (i) reads the rule from the PDF (paste as comment), (ii) asserts the engine effect in a deterministic fixture. Currently we have `test_events_cat_c.py`, `test_events_cat_f.py`, `test_events_phase2.py` — audit coverage and fill gaps. Target: 100% per-card coverage.
- (D) **Differential fuzzer vs. rules-lawyer oracle:** for each card, sample 10 random legal states, execute the event, feed the `(pre-state, action, post-state)` triple to a Haiku rules-lawyer agent with the PDF attached, and fail the test if the LLM flags a rule violation. This is cheap (~$1 per card per pass) and catches rule-interpretation bugs a human might miss. Not a hard gate but a strong CI signal.
- (E) **Expanded replay corpus:** scrape ~200 additional game logs from TSEspionage / ACTS / RecordedGames forum archives (all static HTML, no login needed) and rerun `validate_replays.py`. Target validator clean on 250+ games before declaring 99%.
- (F) **Determinism invariant:** `deterministic_replay_hash_match = 1.0` on all of (B) and (E).

A "defensible 99%" claim should cite passing gates (A), (B), (C), (F) at minimum. (D) and (E) give 99.5%.

### 3. External JS Engine Oracle — Realistic Options

**Is there an open-source TS engine we can oracle against?**

- **TSEspionage** (twilightstrategy.com): live play client, closed-source JS SPA behind login. Replays are publicly viewable HTML — these are the "human logs" we already ingest. The *engine* is not accessible.
- **Playdek Twilight Struggle**: desktop/mobile Unity app, closed-source, licensed. No programmatic access.
- **twilight-struggle-gym** (GitHub, a few Python projects with that name): all are *partial* reimplementations, none are known to be rule-complete. Using one as an oracle would move bugs sideways, not eliminate them.
- **BoardGameArena**: does not host TS.
- **ColdWarGame / similar JS clones**: a few hobby projects exist on GitHub (e.g. `jrojek/twilight-struggle`, `rollingwolf/twilight-struggle-online`) but none I'm aware of are rule-complete enough to be trusted more than our own engine.
- **Human TS-Bot Discord bots**: some play random/weak moves, not rule oracles.

**Can Claude drive a webapp?**

- **WebFetch** (the Claude Code tool): read-only HTML + JS-free scrape. Fine for pulling static replay pages from TSEspionage's archive URLs. *Not* capable of auth, not capable of executing JS to step a live game.
- **Playwright-MCP** (hypothetical): this repo has **no Playwright MCP server configured** (no matching entry in `~/.claude.json` mcpServers; only `codex` is registered). Standing up one is a half-day project (`npx @playwright/mcp` + auth cookie extraction), but:
  - TSEspionage requires a login + an opponent. A bot vs. a live user is abusive; a bot vs. a bot requires two accounts. Not a realistic oracle.
  - Playdek is native, no web surface.
- **Headless browser shelled from Bash**: possible but brittle; same auth/account problem.

**Verdict: external JS engine oracle is not a viable path.** The cost is too high and the benefit marginal vs. what we already have in-hand.

**Alternative oracle stack (what we should actually build):**

1. **Rules-lawyer LLM oracle** (authoritative primary): Claude Haiku agent with `docs/TS_Rules_Deluxe.pdf` in its context window, fed structured `(pre-state, event, post-state)` triples from engine fuzz tests. Infrastructure: `scripts/rules_lawyer_oracle.py` that wraps the existing `rules-batcher` skill. Cost: ~$0.05/triple, so 10k triples = $500 one-time. Catches semantic bugs our unit tests don't.
2. **Scraped replay text + existing validator** (authoritative secondary): pull 200-500 static replay pages from TSEspionage archive (WebFetch is sufficient; no JS required), run through `scripts/validate_replays.py`. This 10× expands the current corpus.
3. **Per-card golden tests with PDF-quoted rules** (authoritative tertiary): paste the rule text into each test case as a comment-quoted source. This is the "defense" part of defensible.
4. **Human-review pipeline** (audit sampling): 5 randomly-seeded self-play games/week manually reviewed by the maintainer, logged to `results/analysis/human_review_*.md`. Low cost, high signal.

None of these require browser automation.

### 4. Training Pause — Recommendations

Current in-flight state (per continuation_plan.json / git status):

- **#109 BC-on-fixed-engine** (epoch ~25/30): training on the post-Plan-B engine. Value: produces a clean BC baseline that *will* be stale after scoring fixes land. **Kill.** The 5-6 hours remaining would bake in the 171 scoring bugs.
- **#96 v37 distill stage 1 (Opus Option A)**: pending. **Pause.** Distill is downstream of a correct PPO chain; correcting the engine first avoids distilling scoring errors.
- **AWR sweep / v4/v5 specialist training** (per `results/capacity_test/`): stop spawning new runs. Existing artifacts remain as frozen baselines.
- **Elo tournament / benchmark runs**: these are engine-agnostic consumers of frozen checkpoints and are fine to leave running for reference.

**Why kill rather than continue:** the memory file `feedback_plan_b_regression.md` / `project_policy_collapse.md` pattern documents exactly this failure mode — training on a buggy engine produces a model whose value estimates are anchored to the wrong game, and the resulting policy looks fine in self-play but collapses vs. heuristic opponents on the corrected engine. The v56 → v5 regression is the proof-of-harm. Repeating the experiment is negative-EV.

**Warmstart freeze:** crown v32 (`ppo_gnn_card_attn_v3` / panel=0.459) as the certified-legacy baseline. After engine fixes land, the BC re-warmstart from v32's exploration traces is the defensible restart point. Do not accept any new warmstart into the best-model ledger during the pause.

**Timeline recommendation:** 3-week correctness sprint, then a 2-week training restart sprint, for a 5-week total pivot.

### 5. Concrete 3-Week Sequencing

#### Week 1 — Close the frame migration and fix the scoring resolver

- **Day 1-2**: Triage the 171 `SCORING_VP_MISMATCH` violations. Dump the first 10 mismatches with full pre/post state + expected vs. actual VP. Hand-compute against PDF. Classify by card ID. Expected outcome: 1-3 root causes (likely Europe sub-scoring, Asia Taiwan/battleground, China Card bonus). Create `docs/rules_decisions.md` and `docs/scoring_resolver_bugs.md` tracking issues.
- **Day 3-4**: Fix scoring resolver. Add `test_scoring_resolver.py` with 10 hand-computed fixtures from real human games. Commit only when `validate_replays.py` shows `SCORING_VP_MISMATCH = 0`.
- **Day 5**: Complete frame migration (callsites 1/2/3 at `hand_ops.cpp:405/518/590`). Delete `apply_ops_randomly_impl`. Green `test_frame_parity.cpp`.

#### Week 2 — MCTS frame-ification and remaining engine bugs

- **Day 6-7**: Wire `mcts.cpp` through the frame API (§1 step 2). Benchmark ISMCTS runs with frame-aware sub-choices. Verify no regression on `test_ismcts_regression.cpp`.
- **Day 8**: Fix Card 22 Independent Reds (should be single country, not all eligible) and Card 56 South African Unrest (add branch choice). Add per-card unit tests.
- **Day 9**: Investigate and fix `TARGET_ILLEGAL` top-5 (Card 5 at 4, +63 others). Likely legal-action generator divergence from the event code.
- **Day 10**: Fix Python trace formatter (`run_traced_game.py::_post_snapshot_for_step`): snapshot *before* turn cleanup, not after, so last-AR events don't inherit next-turn state. This unblocks future audits.

#### Week 3 — Oracle + golden corpus + declare

- **Day 11-12**: Stand up rules-lawyer LLM oracle: `scripts/rules_lawyer_oracle.py` that feeds `(pre, event, post)` triples to Haiku with the PDF. Run against 10 samples per card × 110 cards = 1100 triples; expect ≤5 flagged. Triage.
- **Day 13**: Scrape ~200 TSEspionage replay pages via WebFetch. Ingest through parser; fix any unknown-line buckets; rerun validator. Target: clean on 250 total games.
- **Day 14**: Expand `test_frame_regression.cpp` to include 50 games (from 20). Run full C++ test suite + full Python test suite. Confirm deterministic hash match on all 250 replays.
- **Day 15**: Write `docs/engine_correctness_certification_v1.md` citing gates (A)-(F) with numbers. Tag git commit `engine-v1.0-certified`. End pivot.

#### Weeks 4-5 — Training restart

- **Day 16-17**: BC warmstart from v32 exploration traces on certified engine. Target epoch-30 BC accuracy ≥ prior BC run's accuracy on the corrected validation split.
- **Day 18-25**: PPO v33 on certified engine from BC warmstart. First benchmark at iter 50 to check combined-WR vs. frozen v32. If regression > 3pp, stop and investigate (may indicate remaining hidden engine bug). If ≥ parity, continue to iter 200 + standard eval.

### Risk Register

- **Risk: scoring resolver fix is a 2-day root-cause chase, not 1-day.** Mitigation: if Day 2 doesn't land a root cause, escalate to rules-batcher + manual PDF read of Europe/Asia scoring pages on Day 3. Budget 1 extra day.
- **Risk: MCTS frame-ification breaks ISMCTS.** Mitigation: keep a feature flag `mcts_use_frames` (default on) and `test_ismcts_regression.cpp` as the gate. Revert flag if regression.
- **Risk: new engine changes invalidate all frozen checkpoint Elo ratings.** Accept this — we already acknowledge in `feedback_elo_tournament_cache.md` that post-engine-fix runs require `--no-cache`. Budget 1 evening of Elo-rebuild CPU time at the end of Week 3.
- **Risk: rules-lawyer LLM flags many false positives.** Mitigation: treat its output as triage-signal, not ground truth. Human-in-the-loop review of every flagged case.
- **Risk: pause demotivates; drift toward "just one more training run."** Mitigation: commit the freeze publicly in `continuation_plan.json` and `autonomous_decisions.log`; set a hard calendar checkpoint for restart (Day 16) that the session-start hook reads.

## Conclusions

1. **Frame migration is ~90% complete.** Three fallback callsites in `hand_ops.cpp` (cards 19/52/68) remain, plus `mcts.cpp` never integrated with the frame API at all. Total finish cost is ~5 working days.
2. **The 171 `SCORING_VP_MISMATCH` violations are the single largest engine defect and the correct top priority.** They dwarf every other bug by count (165/246 = 67% of all validator violations) and they directly corrupt value targets in every PPO run.
3. **"Defensible 99%" is achievable in 3 weeks** via (A) validator clean on 51 games, (B) 50-game golden regression, (C) per-card unit tests, (D) rules-lawyer LLM oracle, (E) scrape-expanded 250-game corpus, (F) deterministic hash match.
4. **No external JS engine is a viable oracle.** TSEspionage is auth-walled, Playdek is native, Playwright-MCP is not configured, and existing open-source clones are not rule-complete enough to trust. This is not a blocker.
5. **The real oracle stack is already within reach**: PDF + rules-lawyer LLM + scraped replays + per-card unit tests. Cost: ~$500 in Haiku calls + a few days of plumbing.
6. **Continuing in-flight training is negative-EV.** BC #109 will bake in the scoring bugs; Distill #96 will distill corrupted value estimates. The 0.650 → 0.48 regression memo is the proof-of-harm. Kill both.
7. **v32 is the right warmstart anchor** for post-pivot retraining. The memory file `project_fresh_elo_panel.md` already treats it as the authoritative top-tier model; freeze it.

## Recommendations

1. **Today**: kill BC #109 and mark #96 paused. Write the pivot decision to `autonomous_decisions.log` and update `continuation_plan.json` so the SessionStart hook reflects the new mode. Stop-spawn flag on all training scripts (simple environment guard).
2. **Today**: create `docs/rules_decisions.md` and `docs/scoring_resolver_bugs.md` with headings ready to be filled; open git issues #S1-#S5 for scoring resolver triage.
3. **Day 1 deliverable**: a triage report dumping first 10 `SCORING_VP_MISMATCH` cases side-by-side (expected vs. actual) for Europe/Asia/Africa scoring. This alone likely reveals root cause.
4. **Day 5 deliverable**: frame migration complete, `apply_ops_randomly_impl` deleted, `test_frame_parity.cpp` green at 10k seeds.
5. **Week 2 deliverable**: MCTS frame-aware; Card 22 and Card 56 fixed; `TARGET_ILLEGAL` ≤ 5 on validator.
6. **Week 3 deliverable**: `docs/engine_correctness_certification_v1.md` signed; git tag `engine-v1.0-certified`.
7. **Do not** stand up Playwright-MCP, do not scrape live JS webapps, do not attempt to use TSEspionage as a live oracle. Instead budget ½ day of WebFetch scraping of static replay HTML + PDF + rules-lawyer LLM.
8. **Do** scrape 200 additional TS replays from static sources (ACTS PBEM archive, forum games, TSEspionage viewer URLs when they're static) to expand the validator corpus 5×.
9. **Do** extend `test_frame_regression.cpp` coverage to 50 games and make hash-match the CI gate.
10. **Do not** accept any new top-of-ladder claim during the pivot. Elo tournaments may run for observational value but not for leaderboard updates.

## Open Questions

- Does the scoring resolver bug actually concentrate on Europe sub-scoring, or is it China Card bonus, or Shuttle Diplomacy interaction? Day-1 triage will answer. Hypothesis: Europe sub-scoring (highest violation rate on card 2).
- Are there any `TARGET_ILLEGAL` violations that are actually validator-side bugs (wrong legal-action model in the validator, not engine bugs)? Some "illegal" targets may be legal per exotic card interactions; spot-check 10 before blanket fixing.
- Is the `docs/rules_decisions.md` file referenced in CLAUDE.md actually expected to exist yet? It's listed as owned by rules-lawyer but was not created. Treat its creation as part of this pivot.
- Should `apply_ops_randomly_impl` be deleted immediately or kept as a fallback behind a `#ifdef DEBUG_FALLBACK` for one more release cycle? Recommend delete — the frame path subsumes it and keeping dead code breeds ambiguity.
- Is the `long-prompts/inconsistent-moves.md` audit comprehensive, or are there further latent bugs not caught by either the validator or that ChatGPT audit? Week-3 rules-lawyer sweep over all 110 cards is the defense-in-depth answer.
- How many TSEspionage replay pages are actually static HTML vs. JS-rendered? Needs a 5-minute WebFetch probe on Day 11 before committing to that data-expansion plan; if JS-rendered, drop (E) and accept (A)+(D) alone as sufficient for "99% defensible".
