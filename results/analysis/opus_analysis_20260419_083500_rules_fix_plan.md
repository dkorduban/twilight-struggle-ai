# Opus Analysis: Rules Fix Plan and WR Measurement Strategy
Date: 2026-04-19T08:35:00Z
Question: Given the rules-bug audit in `opus_analysis_20260419_071025_frame_rules_audit.md`, (1) how do we measure the ISOLATED effect of rule fixes on policy WR and behavior without frame-migration effects contaminating the signal, (2) do the top panel models (v44/v54/v55/v56/v20 and `ppo_gnn_card_attn_v1/v2`) need warmstart / fine-tune / full retrain after engine fixes, and (3) what is the robust prioritized sequencing of engine fixes, frame migration completion, and architecture/training work — treating engine correctness as the #1 priority. A secondary question is whether the 50/5544 Slice-B parity test failures should be fixed before or after the rules bugs.

## Executive Summary

The cleanest isolation is a **paired-engine A/B** — freeze each checkpoint and benchmark it under (a) current engine and (b) rules-fixed engine with identical seeds and opponent. Retrain-based comparisons conflate "lost bug exploit" with "retraining variance" and should not be used for the isolation measurement. Do not commit a-priori to retraining the panel: run the A/B first, then gate (retrain only if ΔWR vs random drops >5pp or event-play rate on fixed cards changes >10pp). Sequencing is: (1) fix the 50 Slice-B parity failures first (cheap, narrow, unblocks parity as a regression gate for rule fixes), (2) batch all Tier-1 rules fixes (cards 30, 33, 77, 98) into one engine delta and one benchmark, (3) measure paired-engine ΔWR, then gate retraining. Tier-2 fixes (16, 76, 95, 60, 28) batch second; Tier-3 (75, 50) defer until next training cycle. Training data collected on the buggy engine (~1.35M rows) is contaminated and must be retired from the canonical BC pool once Tier-1 lands; a fresh BC warmstart corpus is needed before any new PPO chain starts. The existing Elo ladder (anchor = v14, 2015.0) becomes incomparable after Tier-1; freeze a new anchor `v14_e2` on the fixed engine.

## Findings

### F1. Measurement strategy (Q1)

Four candidate measurement protocols from the task:

| Option | What it measures | Issues |
|---|---|---|
| (a) Fix bugs, re-collect benchmark games vs heuristic | ΔWR conflated with heuristic behavior change | Heuristic is **not** bug-invariant: minimal_hybrid uses `apply_frame_ops_randomly_impl` and calls engine coup/realign/event primitives. When cards 30/33/77/98 change semantics, the heuristic's event-play outcomes change too. ΔWR is joint policy-and-opponent shift, not pure policy. |
| (b) BC on fixed engine, compare BC models | Policy regresses to retraining-variance noise | Measures *what the policy LEARNS* under fixed rules, not what the existing policy DOES under fixed rules. Requires BC training run (~2-4 hours) to get a single data point. Expensive and confounded. |
| (c) Re-run warmstart AWR on fixed engine | Same as (b) plus extra training compute | Worst option for isolation — combines "bug exploit loss" with "retraining variance" AND "new optimization hyperparameters". |
| (d) Paired-engine A/B on same checkpoint | Exact rule-fix effect on a frozen policy | Requires two engine builds (current + fixed). Zero retraining. Directly answers "how much of this checkpoint's WR depended on the bugs." |

**Option (d) is the only correct isolation measurement.** Protocol:

1. Build two engine binaries: `tscore_pre_fix` (HEAD) and `tscore_post_fix` (rules-patched branch).
2. Python imports each via a path switch (`TS_ENGINE_PATH` env or a second wheel). No Python code changes.
3. For each panel checkpoint X in {v44, v54, v55, v56, v20, ppo_gnn_card_attn_v1, ppo_gnn_card_attn_v2}:
   - Benchmark X vs random on identical seeds (say 500 seeds alternating sides) under both engines. Record `wr_pre(X)`, `wr_post(X)`.
   - Benchmark X vs heuristic under both engines (same seeds). This is a secondary signal; treat as corroboration.
   - **Do NOT benchmark X vs X self-play as a headline WR metric** — symmetric self-play is always ~50%; it only tells us whether decision quality shifts, not WR. Use it only to measure event-play rate changes on the 4 fixed cards.
4. Compute ΔWR = `wr_post - wr_pre` per checkpoint, per opponent. 95% CI via bootstrapping on game outcomes.
5. Log per-checkpoint event-play rates for cards 30, 33, 77, 98 under both engines:
   - `p(play 30 as event | 30 in hand & USSR phasing & Early)`
   - `p(play 33 as event | 33 in hand & USSR phasing)`
   - etc.
6. **Bug-exploit signature diagnostic** (the direct causal evidence): in a 500-game sample, count how many times the pre-fix policy placed ≥3 influence in a single country via card 30 (Decolonization) — if the policy is exploiting the bug, this number is non-trivial; post-fix the engine won't allow it.

The Slice-B frame parity is a separate measurement concern — see F4 below.

### F2. Do panel models need retraining? (Q2)

**Card-frequency math.** The standard ITS deck is 110 cards (id 1-111 minus China). Early War deck = cards 1-38 (≈35 cards in play after deck-subset rules). Mid War adds 39-84 + promos. Late War adds 85-108 + 109-111 promos.

| Card | Era | Side | Starred | In deck every game | Drawn/turn-reachable | Exposure risk |
|---|---|---|---|---|---|---|
| 30 Decolonization | Early | USSR | NO | YES | Common — not starred so recurs; 2-op USSR event drawn in Early War most games | **Very high** |
| 33 De-Stalinization | Early | USSR | YES | YES | Very common in Early; starred but mandatory-USSR-event when drawn (ops 3) | **Very high** |
| 16 Warsaw Pact | Early | USSR | YES | YES | Common (3 ops, starred, USSR event) | **Medium-high** |
| 28 Suez Crisis | Early | USSR | YES | YES | Common (3 ops, USSR) | **Medium** |
| 77 Ussuri River Skirmish | Mid | Neutral | YES | YES | Once per game when drawn (Mid War, 3 ops) | **Medium** |
| 98 Latin American Debt Crisis | Late | USSR | YES | YES | Once per game at most; not every game reaches Late War | **Medium-low** (but catastrophic semantic error) |
| 76 Liberation Theology | Mid | USSR | NO | YES | Recurs; Central America 3-infl tool | **Medium** |
| 95 Terrorism | Late | Neutral | NO | YES | Late War only | **Low** |
| 60 ABM Treaty | Mid | Neutral | NO | YES | Recurs; but wrong-card behavior in current engine | **Low-medium** |
| 75 Voice of America | Mid | US | NO | YES | Recurs | **Low** |
| 50 Junta | Mid | Neutral | NO | YES | Common as neutral event | **Low-medium** |

**Heuristic argument for why panel v44/v54/v55/v56/v20 almost certainly learned bug exploits:**

- Card 30 Decolonization: the policy was trained on 1.35M rows (heuristic vs heuristic + self-play) where "+4 in one Africa/SE-Asia country" is legal and rewarded. The GNN card-attention architecture conditions target placement on country features. The value gradient through a 4-stack in a battleground (e.g., Angola) is strictly better than 4 spread placements — the policy's argmax over the target head will have shifted toward same-country stacking.
- Card 33 De-Stalinization: same argument. Stacking 4 in Italy (if not US-controlled) or Angola is a 2-VP-equivalent exploit. The current engine allows it; the policy has been shaped by the gradient.
- Card 77 Ussuri: rarer card but the exploit is huge when drawn. If the policy ever chose Asia pool when the engine only offered global pool, it couldn't; the policy head learned "pick any country with USSR-favorable margin", not "pick Asia battlegrounds".
- Card 98 LADC: the engine implements a completely different event. The policy's behavior on this card is **orthogonal** to the real card's semantics. The policy has no learned signal about "cancel via ops≥3 discard" or "double S.American infl" because those mechanics never existed in training.

**Threshold decision (do not commit a-priori).** Predicted ΔWR per exposure tier:

- Cards 30+33 (very high exposure): plausible ΔWR magnitude on USSR side **3-8pp** (policy loses a learned over-stacking exploit that was worth a few VP; games that were +3 or +4 VP wins on bug-exploit may flip to draws/losses).
- Card 77 (medium exposure, starred once-per-game when drawn): plausible ΔWR magnitude **1-3pp** on USSR.
- Card 98 (the catastrophic one, but rare): plausible ΔWR magnitude **0-5pp** depending on whether Late War is reached. **However**, the policy's behavior on LADC in the post-fix engine is *undefined* — it literally never trained on this mechanic. This is the only card where we should expect policy to possibly play it *worse* than random initially.

**Recommendation**: do not pre-commit to retrain. Run the paired A/B. Decision rule:

- If USSR-side ΔWR drop > 5pp on any panel checkpoint OR event-play rate on card 98 is qualitatively broken (e.g., the policy never plays LADC as event because its value head is miscalibrated for the new mechanic) → **retrain with fresh BC corpus**.
- Else → panel stays usable as a floor while `ppo_gnn_card_attn_v2` continues. The panel's relative ordering is likely preserved (all panel checkpoints were trained on the same buggy engine, so the Elo ranking among them is stable even if all shift down together).

### F3. Sequencing plan (Q3)

**Principle**: engine correctness > frame-migration completion > architecture changes > training throughput. Batch rule fixes by tier to minimize benchmark cost.

**Tier-1 (batch 1) — top game-impact, obvious wrong answer:**
- Card 98 LADC (reimplement from scratch — wrong event entirely)
- Card 77 Ussuri (Asia-only pool + 2-per-country cap)
- Card 30 Decolonization (distinct-country enforcement)
- Card 33 De-Stalinization (phase-1 remove / phase-2 place + 2-per-country cap + optional "up-to-N" SmallChoice)

**Tier-2 (batch 2) — systemic caps and logic errors:**
- Card 16 Warsaw Pact add-5 branch (2-per-country cap)
- Card 76 Liberation Theology (2-per-country cap)
- Card 95 Terrorism (random discard)
- Card 60 ABM Treaty (correct count=4, remove spurious +1 VP, correct pool)
- Card 28 Suez Crisis (distributable 4-op budget across 3 countries with 2-per-country cap)

**Tier-3 (batch 3) — low impact, defer to next training cycle:**
- Card 75 Voice of America (allow up-to-2 per country, remove forced-distinct constraint)
- Card 50 Junta (add realignment option; make coup optional)
- Card 7 Socialist Governments (2-per-country cap instead of <2 filter)
- Card 20 Olympic Games (fix accessibility refresh, per-control cost, die bonus — nice-to-have)

**Between tiers**, run the paired-engine A/B measurement from F1. Tier gates:

1. **Before Tier-1 lands**: fix the 50 Slice-B parity failures. These are not overlapping with Tier-1 rule fixes (see F4). Landing parity first makes parity a clean regression gate for subsequent rule-fix commits: Tier-1 commits must not increase parity failures.
2. **Tier-1 lands** → run A/B on all panel checkpoints + `ppo_gnn_card_attn_v1` + current v2 best checkpoint → gate retrain decision.
3. **If retrain gated ON**: stop `ppo_gnn_card_attn_v2` chain, invalidate 1.35M-row BC corpus, collect new BC rollout data with rules-fixed engine + heuristic-vs-heuristic + previous-best-vs-heuristic, warmstart BC, then restart PPO chain from the BC warmstart.
4. **If retrain gated OFF**: let `ppo_gnn_card_attn_v2` continue on the fixed engine (it will naturally unlearn bug exploits through its own PPO loop — just slower than a fresh warmstart). Log the decision and its risks.
5. **Tier-2 batch** lands + smaller A/B (panel checkpoints only; 200 games each) → if <2pp ΔWR on any checkpoint, skip retrain. Tier-2 caps individually are smaller-magnitude than Tier-1.
6. **Tier-3 batch** folds into next architecture/PPO cycle; no interim A/B.

**Frame migration vs rule fixes.** Slices C/D/E/F/G of the frame migration are orthogonal to the rules fixes in this audit. Continue them in parallel worktrees on the fixed-engine branch. Each slice still runs the parity harness as its gate. The audit confirmed frame decomposition doesn't introduce new rules bugs — only rules bugs in both paths — so rule-fix commits should update both the synchronous `step.cpp` path AND the frame `resume_card_XX` path in a single atomic commit to maintain parity.

**Panel maintenance.** Post-Tier-1:
- **Do NOT retrain panel models as a matter of policy.** They're useful as a fixed Elo anchor set for comparing new checkpoints to the old ladder up to a shift constant.
- **Do freeze a new Elo anchor** — `v14_e2` on the fixed engine, rated at 2015.0 by definition (same number as the old anchor for continuity but on a different scale). Old Elo ratings become historical.
- **Do re-run the benchmark panel table** on the fixed engine (panel vs heuristic, panel vs random) so we have a post-fix baseline. This is one-time ~2-3 hours.

**When to re-trigger PPO.** The gate is F1's ΔWR + event-rate change on the top PPO checkpoint. The current `ppo_gnn_card_attn_v2` chain can either be stopped (if retrain is gated ON) or continue (if gated OFF) — but in either case the benchmark_history.json becomes split at the "Tier-1 fix" marker and all post-fix entries must be flagged explicitly.

### F4. Slice-B parity failures: fix before or after rule fixes? (Q4)

Advisor framing confirms what the audit implies: the 50/5544 parity failures are **migration regressions specific to Slice-B's 8 cards (24, 39, 83, 90, 91, 97, 102, 105)**. None of these 8 overlap with the Tier-1/Tier-2 rules-bug list (30, 33, 77, 98, 16, 76, 95, 60, 28).

Sequencing implication:

- **Fix parity first.** Narrow, isolated, low-risk. Once parity is green, any new parity failure introduced by a Tier-1 commit is provably a Tier-1 problem (asymmetric rule fix between `step.cpp` and `resume_card_XX`), not a latent Slice-B regression.
- **Do not fix rules first.** If Tier-1 lands with parity red, each new rule-fix commit must distinguish "my fix broke parity on card 30" from "Slice-B regression on card 83 is still there" — that's a diagnostic burden we don't need.

The parity failures on Slice-B cards should be bug-tracked and fixed in a focused 1-2 hour task before Tier-1 begins.

### F5. Practical cost estimates

For planning purposes:

- Parity fix for Slice-B (8 cards, 50 failures): 1-3 hours with Codex.
- Tier-1 rule fixes (4 cards, one of which is a full reimplementation): 4-8 hours with Codex. The De-Stal phase decomposition is the most complex; LADC reimplementation is comparable.
- Paired-engine A/B for 7 checkpoints × 2 opponents × 500 games + event-rate diagnostics: ~2-4 hours with GPU (checkpoints are small, game length is short).
- Tier-2 rule fixes: 6-10 hours with Codex.
- BC corpus re-collection (if gated ON): ~4-6 hours for 500k-1M rows on fixed engine.
- BC warmstart re-training (if gated ON): ~2-4 hours.
- PPO chain restart (if gated ON): days, but already budgeted.

Total critical-path time before PPO can confidently continue on fixed engine: **~12-24 hours of engine work + 2-4 hours of benchmarking + conditional retraining**. This is a 1-2 day critical path, not a multi-week overhaul.

## Conclusions

1. **The only correct isolation measurement is paired-engine A/B on frozen checkpoints.** Do not use BC-retraining or PPO-retraining to measure the rule-fix effect; both conflate lost-exploit with retraining variance. Run checkpoint X vs random AND vs heuristic under (pre-fix engine, post-fix engine) on identical seeds, and additionally log event-play rates on the 4 fixed cards.

2. **Panel retraining is not a priori required.** Gate it on: USSR-side ΔWR drop >5pp on any panel checkpoint OR qualitatively broken event-play on card 98 (which is the only card where the policy's value head has no correct training signal). Predicted ΔWR from card-exposure reasoning: Tier-1 fixes cost USSR-side 3-8pp combined, mostly from cards 30 and 33.

3. **Fix Slice-B parity failures first** (1-3 hours). They are not in the rules-bug list and should not delay Tier-1. Once parity is green, it becomes a regression gate for every subsequent rule-fix commit.

4. **Batch rule fixes into three tiers and benchmark only at Tier-1 and Tier-2 boundaries.** Per-card benchmarking wastes compute and confounds interactions (cards 30 and 33 both shape USSR Early War opening and should be measured together).

5. **Rule-fix commits must touch both `step.cpp` and `resume_card_XX` atomically.** The frame layer faithfully inherits rule bugs in both directions, so asymmetric fixes would introduce new parity failures.

6. **The 1.35M-row BC corpus is contaminated after Tier-1.** If retrain is gated ON, do not reuse it for warmstart — collect a fresh corpus on the fixed engine. If retrain is gated OFF, flag it in benchmark_history.json as "pre-Tier-1 data; use for BC only with explicit awareness of drift."

7. **The existing Elo ladder is invalidated by Tier-1.** Freeze a new anchor `v14_e2` on the fixed engine and start a fresh ladder. Old ratings become historical; do not try to reconcile across the engine boundary.

8. **Frame migration Slices C-G continue in parallel on the fixed-engine branch.** Each slice still gates on parity harness. No conflict with the rule-fix workstream.

9. **Tier-3 fixes and Card 68 Grain Sales random-draw fix defer to next training cycle.** Impact is low enough that the paired A/B won't detect them at 500-game sample size.

10. **Card 98 LADC is the single highest-risk fix.** Because the current engine implements a different event entirely, the policy has no learned behavior for the correct mechanic. Even if overall ΔWR is <5pp, the policy may play LADC nonsensically (e.g., never as event, or with random country choices). Monitor event-play rate on card 98 as a first-class diagnostic; if the policy never plays it as event post-fix, retrain is gated ON regardless of ΔWR.

## Recommendations

Executable in order. Each step has a concrete input, output, and success criterion.

1. **Step 1 (1-3h): Slice-B parity bug fix.** Dispatch to Codex worktree. Input: the 50 parity failures. Output: green parity on `tests/cpp/test_frame_parity.cpp` for cards 24, 39, 83, 90, 91, 97, 102, 105. Success: 5544/5544 parity assertions pass.

2. **Step 2 (4-8h): Tier-1 rule-fix branch.** Create branch `fix/rules-tier-1`. Implement fixes in atomic commits (both paths per commit):
   - Commit A: Card 30 Decolonization distinct-country enforcement (`step.cpp` case 30 + `resume_card_30` next_eligible reset).
   - Commit B: Card 77 Ussuri Asia-only pool + 2-per-country cap using a new helper.
   - Commit C: Card 33 De-Stalinization phase-decomposition rewrite (see audit F1 section 3 recommendation for scratch-array-based 2-per-country cap).
   - Commit D: Card 98 LADC full reimplementation (remove from `kCatCCardIds`; implement opponent-cancel-choice + phasing-side double-infl picks).
   - Add parity tests for all 4 cards.
   - Success: parity stays at 5544/5544; new rule-specific tests pass.

3. **Step 3 (2-4h): Paired-engine A/B benchmark.** Script `scripts/benchmark_ab_engine.py` that takes two engine paths and a checkpoint list, runs 500 games per (checkpoint, opponent) pair under each engine on identical seeds. Opponents: random + heuristic. Checkpoints: v20, v44, v54, v55, v56, ppo_gnn_card_attn_v1, current best `ppo_gnn_card_attn_v2`. Log per-card event-play rates for 30/33/77/98 in both conditions. Output: `results/analysis/tier1_paired_ab_YYYYMMDD.json` with per-checkpoint ΔWR + 95% bootstrap CI + event-rate table.

4. **Step 4 (decision gate, 15 min review):** Apply the retrain gating rule:
   - If ANY panel checkpoint shows USSR ΔWR drop >5pp → gate RETRAIN ON.
   - OR if `ppo_gnn_card_attn_v2` shows >3pp combined ΔWR drop → gate RETRAIN ON.
   - OR if card 98 event-play rate post-fix is <50% of pre-fix rate (policy stops playing it as event) → gate RETRAIN ON.
   - Else → gate RETRAIN OFF; ppo_gnn_card_attn_v2 continues on fixed engine.

5. **Step 5a (if RETRAIN ON, 8-14h):** Stop `ppo_gnn_card_attn_v2`. Retire 1.35M-row BC corpus (move to `data/deprecated_buggy_engine/`). Collect fresh BC corpus on fixed engine (1M rows minimum — heuristic vs heuristic + previous-best vs heuristic + self-play of top checkpoint). BC-warmstart new model `ppo_gnn_card_attn_v3`. Resume PPO chain from BC warmstart.

6. **Step 5b (if RETRAIN OFF, 0h):** Let `ppo_gnn_card_attn_v2` continue on fixed engine. Add a `benchmark_history.json` marker entry `{"event": "tier1_engine_fix", "timestamp": "..."}`. Flag all post-fix Elo ratings explicitly.

7. **Step 6 (one-time, 2-3h): Elo ladder reset.** Freeze new anchor `v14_e2` at 2015.0 on fixed engine. Re-run panel-vs-panel tournament (200 games per pair, 5 checkpoints = 10 pairs = 2000 games) to establish fixed-engine panel Elo. Archive old ladder as `results/elo/elo_full_ladder_pre_tier1.json`.

8. **Step 7 (6-10h): Tier-2 rule-fix branch.** Batch cards 16, 76, 95, 60, 28. Same atomic-commit discipline (both paths). Run smaller A/B (panel only, 200 games each) — if no checkpoint shifts >2pp, skip retrain.

9. **Step 8 (parallel, ongoing): Frame migration Slices C-G.** Continue on fixed-engine branch. No conflict with rules work.

10. **Step 9 (defer to next architecture cycle): Tier-3 fixes** + cards 7, 68 random-draw cleanup. Fold into whichever PPO chain is current at that time.

## Open Questions

1. **Paired A/B script design**: does the benchmark suite support loading two pybind wheels in one process, or do we need to run each engine in its own subprocess and aggregate? Running in subprocesses is cleaner (no symbol pollution) but serializes the benchmark. For 500 games × 7 checkpoints × 2 opponents × 2 engines = 14k games, subprocess parallelization on the GPU is fine.

2. **Event-rate measurement harness**: do we already have per-card event-play logging in the benchmark? A quick inspection suggests `results/elo_tournament.lock` and `benchmark_history.json` don't capture event-play. Need a small addition to `scripts/benchmark.py` to log every event-card-play decision to a sidecar JSONL.

3. **Card 98 policy retraining fallback**: if the policy's event-play on LADC is qualitatively broken post-fix (as predicted), should we add a narrow BC cue dataset specifically for this card to patch the behavior without a full retrain? Might be 50k positions focused on LADC opportunities, 30min of BC fine-tuning. Alternative to Step 5a for "partial retrain" case.

4. **Heuristic recalibration**: the `minimal_hybrid` heuristic was tuned against the buggy engine. Its win rate vs random may shift post-fix (probably small, but uncertain). Do we recalibrate its thresholds, or accept the shift as part of the benchmark baseline? Recommendation: accept the shift — re-measuring heuristic-vs-random and documenting the new baseline (~expected 78-83% from prior memory) is sufficient.

5. **Card 58 Willy Brandt discrepancy from audit**: the audit noted the migration plan's naming was wrong (card 58 != card 33). Does this indicate deeper plan-doc drift, and should we sanity-audit all card identities in `docs/event_scope.md` against `data/spec/cards.csv`? Low priority but worth a grep.

6. **ppo_gnn_card_attn_v2 current iteration (~11+)**: if retrain is gated OFF and v2 continues, when does the Elo ladder reset (Step 6) run — before or after v2 reaches a checkpoint milestone? Suggest running Step 6 immediately regardless of v2 state; v2's new checkpoints rate into the new ladder naturally.
