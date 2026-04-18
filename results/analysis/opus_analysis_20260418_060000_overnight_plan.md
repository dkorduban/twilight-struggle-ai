# Opus Analysis: Overnight Work Plan
Date: 2026-04-18 UTC
Question: Design autonomous overnight work plan for Twilight Struggle AI

---
## ⚠ Corrections & Addendum (added 2026-04-18, after user feedback)

The following corrections supersede the original plan below:

### Panel composition (corrected)
- **Wrong in original**: plan referred loosely to "5+ models" without specifying
- **Correct panel v6**: `{ussr_only_v5, us_only_v5, v44, v55, v56, v54, v20}` + heuristic games for each
- **Naming collision in panel v5**: `ppo_best_scripted` in awr_panel_v5.parquet was a naming collision — both `ppo_ussr_only_v5/ppo_best_scripted.pt` AND `ppo_us_only_v5/ppo_best_scripted.pt` were tagged identically. Use `--model-names ussr_only_v5 us_only_v5 ...` going forward.
- **Post-v56 checkpoints**: v57–v318 PPO chain checkpoints are garbage (trained during broken/unstable period). Exclude from panel. v319_sc is NOT in the panel.

### Data format (corrected)
- **Wrong in original**: plan mentioned JSONL intermediate formats in places
- **Correct**: Always Parquet (zstd compressed). `pq.write_table(table, path, compression="zstd")`. `collect_awr_data.py` already does this — never add JSONL steps.

### AWR training depth (corrected)
- **Wrong in original**: 20 epochs used in FiLM experiment — too few. Models peaked at epoch 5 (cold-start issue), meaning later epochs may show further gains with proper init.
- **Correct**: **60 epochs minimum** for meaningful AWR arch comparison
- **Missing step**: After AWR training, **benchmark vs panel** (export to TorchScript → `benchmark_batched` vs v56 + specialists, N=200/side). `val_adv_card_acc` alone is insufficient signal.
- **Mini-PPO**: After best arch identified: run 10–15 PPO iterations warm-started from best AWR checkpoint to validate arch quality carries through to actual play.

### Dense reward shaping (new idea, not in original)
- Add shaped intermediate rewards on each VP change, annealed to 0 over training:
  - `r_shaped = delta_vp * alpha * anneal(step)`, `anneal = max(0, 1 - step/T_anneal)`
  - VP sources: scoring card plays, space race awards, milops at end of turn, DEFCON penalties
- `StepTrace` already has `vp_before`/`vp_after` — implement in `collect_selfplay_rows_jsonl.cpp`
- Teaches model to: flip regions before scoring, not fail milops, value incremental board position
- Anneal to 0 so final policy still optimizes true sparse win/loss reward

### Value calibration finding (measured, 2026-04-18)
- ppo_best (v319-era) on panel v5: **Brier=0.111, Bias=+0.116** (systematic overoptimism)
- Late game worst: Brier=0.211 at turns 8–10
- All models show positive bias (v56=+0.054, v319=+0.116)
- Confirmed: ISMCTS failure is partly compounded by value-head overoptimism under determinization

---

## Executive Summary
The highest-leverage overnight target is the **off-policy architecture-ranking loop** (AWR on a panel parquet), which already exists and just needs more / better data. Rich "full game traces" are only required to replay *richer features* (e.g. internal sub-decisions, dice outcomes, trap resolutions) — but the immediate bottleneck is **not** trace completeness; it is (a) panel diversity, (b) value-head calibration on known-hand states, and (c) one missing context feature (action-phase / AR-progress / hand-composition summary). An 8-hour schedule that spends ~2h on a minimal C++ "full trace v0" emitter, ~2h on a value-head calibration audit + fix proposal, ~2h on a full-info MCTS smoke test at 100 sims on 100 paired seeds, and ~2h on AWR arch shoot-out (with the context feature added) will produce actionable signal across all 5 priorities without touching PPO.

## Findings

### 1. Full Game Trace — Minimum Viable C++ Design

#### What exists today
`cpp/tscore/game_loop.cpp` produces a `TracedGame` whose `steps` list contains one `StepTrace` per **top-level decision point** (headline, AR action, extra AR, setup placement). Each `StepTrace` (see `game_state.hpp` / `game_loop.hpp`) already carries:
- `pub_snapshot` (full `PublicState` before the action)
- `hand_snapshot` of actor, `opp_hand_snapshot`, `deck_snapshot` (hidden info included!)
- `action` (`ActionEncoding`: card_id, mode, targets)
- `vp_before/after`, `defcon_before/after`, china-holder flags
- Phase-1e: `small_choice_target`, `small_choice_n_options`, `small_choice_logprob` (partial sub-decision capture)

`cpp/tools/collect_selfplay_rows_jsonl.cpp` already emits per-top-level-step JSONL rows that include `ussr_hand`, `us_hand`, `deck`, plus all public-state fields needed by `game_state_from_dict`. That is **already enough to regenerate any feature representation at each NN decision point**, because from a `GameState` equivalent we can recompute any feature deterministically.

#### What is actually missing for "replay any feature, anytime"
Three classes of events are **not** captured in the current `StepTrace`:
1. **Sub-decisions called via `PolicyCallbackFn`** during event resolution (e.g. Decolonization country picks, Alliance For Progress, Junta coup target, Grain Sales card choice, Cuban Missile Crisis removal, Glasnost free influence). These are "AR-less" decisions that happen inside `apply_action_with_hands` and never produce a `StepTrace`.
2. **Stochastic engine outcomes**: dice rolls (coup success, realignment), card draws after reshuffle, ABM wheel, random setup opening pick. Currently these are baked into the next `pub_snapshot` but the rolled value itself is lost.
3. **Internal state transitions between AR1 and AR2** when an event schedules deferred effects (norad, north_sea_oil, glasnost_free_ops). These are observable through before/after pub_snapshot diffs, but not as discrete events.

For the stated goal ("regenerate any feature representation in the future") **items 1 and 2 matter**; item 3 is already recoverable.

#### Minimum viable design — FullGameTrace v0
Add a second output channel to the engine: a `std::vector<EngineEvent>` appended in order, where `EngineEvent` is a tagged variant:

```
struct EngineEvent {
  enum class Kind {
    TopStep,          // = existing StepTrace, inlined
    SubChoice,        // PolicyCallback: card context, n_options, chosen index, mask
    Dice,             // coup / realign / space / ABM roll result
    Draw,             // deal_cards: cid, side
    Reshuffle,        // marker only
    EffectTick,       // norad target, glasnost placement, etc
  };
  Kind kind;
  int turn, ar;
  Side side;
  CardId context_card_id;
  // Tagged payload fields (union-ish):
  int int_arg0{0}, int_arg1{0};     // dice face, coup target, ...
  std::vector<int> int_vec;         // mask / options
  PublicStateDelta pub_delta;       // OPTIONAL: delta-compressed public snapshot
};
```

Cheapest implementation plan (≤2 hours):
- Add `std::vector<EngineEvent>* events` pointer next to the existing `trace_steps` argument on `apply_action_with_hands`, `resolve_trap_ar`, `resolve_norad`, `apply_influence_budget_impl`, and the `PolicyCallbackFn` sites.
- **Do not** snapshot `PublicState` in every `EngineEvent` (blows up size ~3×). Instead interleave `TopStep` events (which *do* carry full snapshots) with lightweight sub-events. A reader can replay sub-events against the prior TopStep's snapshot to reconstruct intermediate states — but only if the reducer is deterministic. Engine already is.
- Add a thin C++ emitter tool `cpp/tools/collect_full_traces_jsonl.cpp` modeled on `collect_selfplay_rows_jsonl.cpp` that writes one JSONL row per event, plus a per-game header row with deck seed and config. Group by `game_id`.
- The existing `--learned-model ... --learned-side ...` and dual `--ussr-model/--us-model` support carries over unchanged.

#### Schema suggestion
JSONL lines with fields:
- `game_id`, `event_idx`, `kind` (string), `turn`, `ar`, `side` (-1 none), `context_card_id`
- For `TopStep`: the full existing row schema from `collect_selfplay_rows_jsonl.cpp` (pub state + both hands + deck + action).
- For `SubChoice`: `options` (int[]), `chosen`, `logprob` (if available), `choice_kind` (enum as string: `"decolonization_country"`, `"junta_coup_target"`, etc).
- For `Dice`: `roll`, `ops`, `target_country`, `modifiers_applied` (string).
- For `Draw`: `card_id`, `to_side`.
- For `Reshuffle`: (empty).

That is sufficient to replay any feature: given a sequence of events + initial state, you reconstruct every intermediate `GameState` by running the deterministic reducer. **Crucially**, the initial state is recoverable from game_id + seed already (engine is deterministic from the 4-word seed).

#### Realistic overnight target
A **v0 that only adds SubChoice + Dice events** (items 1+2) covers 95% of the future-feature-regeneration use case. Effects (item 3) can be added later; the current snapshot-per-top-step approach already lets us recompute those. Scope v0 to ~2h of work routed through `/dispatch` (small, C++ local).

### 2. Off-Policy Training Revival

#### State today
- `scripts/train_awr.py` works on `data/awr_eval/awr_panel_v5.parquet` (per-model advantage norm, tau grid, CRR-lite filter). ~3-5 min per arch on GPU. Already consumed by `results/awr_sweep/` and the in-flight FiLM run.
- Architectures are registered in `tsrl.constants.MODEL_REGISTRY`; FiLM variants are recent additions (commits c34b666, 8619e44).
- Data for AWR comes from a **panel parquet** — rolled up from multiple checkpoints, each contributing states + actions + advantages. This file is 5 models × N games already.

#### Fast path to a working pipeline with "full traces"
The current AWR parquet schema is **state-keyed**: one row = one top-level decision. It does not need sub-choice events; sub-choices belong to different heads (small_choice, DP decoder) that currently don't sit in MODEL_REGISTRY-tracked arch variants. So:

- **No schema change is required** for the core AWR arch-ranking loop. The main priority tonight is *more / better panel data*, not richer rows.
- To widen the panel: generate a new `awr_panel_v6.parquet` from 5-7 checkpoints spanning v55..v319_sc + heuristic. Existing tooling (whatever produced v5; likely `scripts/collect_awr_rollouts.py` or similar) should already do this. If missing, repurpose `cpp/tools/collect_selfplay_rows_jsonl.cpp` + a Python rollup that computes advantages via GAE on the reward trace.
- AWR trains with `val_adv_card_acc` (advantage-weighted card top-1 on held-out fold) as the arch-ranking metric. That metric is **already computed** in `train_awr.py` — no change.

#### Proposed overnight AWR arch shoot-out
1. Confirm FiLM 5-variant run finishes (PID 441373). Collect results.
2. Add **one** new context feature (see §5) to the scalars input and the model input plumbing.
3. Re-run AWR on the *existing* v5 panel for 3-4 arch variants: `country_attn_film` (baseline), `country_attn_film+ctx`, `control_feat_gnn_film`, `card_country_cross_attn`. ~15-20 minutes total.
4. Compare `val_adv_card_acc` and `val_adv_mode_acc` with confidence intervals; rank.

### 3. MCTS Full-Info Smoke Test

#### Script design
`tscore.mcts_search_from_state(state_dict, model_path, n_sim, c_puct, calib_a, calib_b, seed)` takes a full `GameState` dict (public + hands + deck). Under the hood it calls native PUCT MCTS with full info — no determinization. That is exactly the full-info smoke test.

Approach — `scripts/mcts_fullinfo_smoke.py`:
```
for seed in 50000..50099 (100 seeds, paired both sides):
  for side in [USSR, US]:
    state_trace = tscore.greedy_state_trace(model, side, seed)
    # Walk every learned-side decision; at each, compare:
    #   greedy_action (step.action in trace) vs
    #   mcts_action = mcts_search_from_state(step.state, model, n_sim=100, seed=seed*7)
    # Record agreement, visit-entropy, root_value.
  # Also play paired games: two games per seed, MCTS-vs-heuristic and greedy-vs-heuristic
  # using same initial seed → fair comparison.
```

Runtime estimate: mcts_search_from_state at n_sim=100 on RTX 3050 ≈ 0.5-1.0 s/call. A game has ~40 learned-side decision points. So 100 seeds × 2 sides × 40 points ≈ 8000 calls ≈ **1-2 hours** total. Instead use the **paired-play benchmark** route:
- A fast paired-play route would require a "search_policy_fn" wrapper, which exists in `play_callback_matchup` / `play_traced_game_with_callback`. Check binding names in bindings/tscore_bindings.cpp.
- If not trivial, fall back to *100 decision points* (5-10 per game × 20 seeds) vs greedy to get a cheap "does MCTS disagree? does it agree with clear improvements (e.g. avoids DEFCON-dangerous plays)?" signal.

Expected signal:
- If full-info MCTS **agrees** with greedy >95% on in-distribution states, value head is calibrated at full-info → ISMCTS failure was purely determinization (matches FINDINGS.md).
- If full-info MCTS **disagrees** but wins more vs heuristic, the policy head is lossy and search helps even with a calibrated value head.
- If full-info MCTS disagrees but *loses* to greedy on self-play pairs, value head is miscalibrated even on known hands → structural training issue.

### 4. Value Head Calibration

#### Metric
For each state `s` from greedy self-play:
- `v_pred = model.value(s)` ∈ [-1, 1]
- `z_true = 1` if USSR wins the game this state came from, `-1` if US wins, `0` draw
- `brier = (v_pred - z_true)^2`
- Stratify by `turn` bucket (1-3, 4-7, 8-10) and by state-value sign.

Also report **calibration** via reliability diagram binned into 10 buckets of `v_pred`.

#### Data
Use existing panel-style full greedy games. `scripts/check_value_calibration.py` already exists — check if it computes per-turn Brier. Run on:
- v319_sc on 200 paired seeds vs heuristic (full-info observations, known hands)
- v319_sc on same 200 vs greedy-self

#### Expected outcome
Project memory ("ISMCTS failure") claims value head is miscalibrated under determinization — it may or may not also be miscalibrated on known-hand mid/late-game states. Overnight job: quantify. If late-turn Brier >> early-turn, policy improvement / distillation targets should weight late-turn states more. If value heavily biased toward draws (overconfident in middle), propose adding a value-loss term with per-turn temperature scaling OR a reward-shape fix during PPO.

#### Fix proposals (depends on findings)
1. **If overall miscalibrated**: add temperature-scaling post-hoc fit (1-param logistic on `v_pred` → `z_true`) as a runtime inference wrapper. Cheapest, no retraining.
2. **If late-turn bias**: upweight late-turn states in value loss (per-turn λ in GAE or per-sample weights).
3. **If overconfident under opponent-hand uncertainty** (the ISMCTS case): that is the structural fix in `continuation_plan.json` — train on determinized observations. Requires PPO restart; out of scope for overnight.

Deliverable: `results/value_calibration/v319_sc_fullinfo_report.md` + Brier/ECE JSON.

### 5. Context Features — Highest Bang-for-Buck

Looking at the current scalar input (`SCALAR_DIM=11` per `constants.py`), the likely missing context features ranked by ROI:

1. **`ar_progress_in_turn`** — (current AR) / (total ARs this turn, 6 or 7 with space). This tells the policy "am I on last AR this turn?" which changes scoring-card timing and held-card risk radically. Cheap: 1 scalar.
2. **`opp_hand_ops_sum_upper_bound`** — sum of max-ops over opponent's possible-hand mask. Encodes "how hard can opp hit DEFCON this turn". Cheap: 1 scalar.
3. **`my_scoring_cards_in_hand_region_flags`** — 6 region flags (Europe/Asia/MidEast/CA/SA/Africa) indicating scoring-card-held-for-this-region. Cheap: 6 binary.
4. **`turns_since_last_defcon_change`** — 1 scalar.
5. **`n_events_played_this_turn`** — 1 scalar (for countering opponent opening pressure).

**Recommendation**: add #1 and #3 (7 scalars). Low risk, high prior — both are known human-strong heuristics. Schema impact: one `scalars` dim bump, rebuild parquet, re-run AWR.

### 6. Cleanup Protocol

#### Stale in `results/continuation_plan.json`
1. `current_task` says "next: task #65 decision-context-features merge". Check if that worktree has been merged already (project_ws6_plan mentions it). If merged, drop.
2. `next_tasks` contains 5 items; cross-check each:
   - Task #65 "Merge decision context features" — verify status via `git log --all --grep "decision.context"`.
   - Phase 2b DP decoder — done according to `pragmatic_heads: ALL DONE`.
   - Task #64 "Collect 4M row extended dataset" — check `data/` for outputs.
   - Task #61 "Replace actor_possible mask with opp hand support" — grep schemas.
3. `completed_this_session` can be moved into a session-log file; `continuation_plan.json` should reflect current state only.

#### Cleanup protocol — safe, non-destructive
1. Create `results/session_log/20260417_ismcts_investigation.md` summarizing the long `completed_this_session` list. (User prefers move-not-delete.)
2. Rewrite `continuation_plan.json` with:
   - `active_background`: empty (or PID 441373 FiLM job)
   - `current_task`: "Overnight: full-trace v0, AWR arch shoot-out, value-head calibration, full-info MCTS smoke"
   - `next_tasks`: re-derived next-3 items after filtering.
3. Clean `ts_play_*.jsonl` root-level stragglers by **moving** (`mv`) them into `results/selfplay/misc/` — never rm.
4. For the `MEMORY.md` task list (if lives under `~/.claude/...`), leave untouched unless user asks — autonomous policy says "don't silently alter user memory".

### 7. 8-Hour Prioritized Schedule

Phase A — Orientation + cleanup (0.5 h)
- Read FiLM run status; gather its metrics if complete.
- Rewrite `results/continuation_plan.json` per §6; move stale jsonl files.
- Write overnight log file `results/overnight_log_20260418.md` for progress.

Phase B — Value-head calibration (1.5 h, CPU+GPU)
- Use `scripts/check_value_calibration.py` on v319_sc over 200 seeds vs heuristic + 200 vs greedy-self.
- Write `results/value_calibration/v319_sc_fullinfo_report.md` with Brier, ECE, per-turn stratification.
- Propose fix (temp-scaling or weighted retrain) as a follow-up task.

Phase C — Full-info MCTS smoke test (2 h, mostly GPU)
- `scripts/mcts_fullinfo_smoke.py` as designed in §3.
- Start with 20 seeds × 2 sides × per-decision agreement (fits in 30 min), then scale to 100 seeds if compute allows.
- Output: agreement rate, disagreement categories (card vs mode vs target), paired WR vs greedy-self.
- Write `results/mcts_fullinfo/v319_sc_smoke.md`.

Phase D — AWR arch shoot-out with new context feature (2 h)
- Add `ar_progress_in_turn` + 6 region-scoring-held flags to scalars (C++ + Python). Rebuild parquet via existing rollout tool. If that tool is missing, postpone to Phase F and use v5 panel as-is.
- Re-run `scripts/train_awr.py` on 3-4 arch variants (country_attn_film, country_attn_film+ctx, gnn_film, cross_attn_v2) × tau∈{0.5, 1.0}. 20-30 min total.
- Rank by `val_adv_card_acc`; write `results/awr_sweep/arch_ranking_20260418.md`.

Phase E — Full-trace C++ v0 emitter via /dispatch (1.5 h)
- Dispatch a C++-local task to `cpp-engine-builder`: add `EngineEvent` variant, add event-vector threading through `PolicyCallbackFn`-fed helpers, add `collect_full_traces_jsonl.cpp` tool modeled after the existing rows tool. Test with a single-game run + a replay-to-state check (can we reconstruct every `GameState` by replaying events?).
- This is the groundwork for future richer AWR targets; not required for overnight arch ranking.

Phase F — Advisor checkpoint + commit + report (0.5 h)
- Commit each phase's artifacts as they land (per "commit often" rule).
- advisor() before declaring done.
- Emit a final summary in `results/overnight_log_20260418.md`.

Safety rails honored throughout: no rm, no PPO restart, nice builds, 8-hour budget.

## Conclusions

1. The engine **already captures enough state at each top-level decision** (via `StepTrace.pub_snapshot` + hands + deck) to regenerate any per-decision feature representation; the current JSONL row emitter proves this.
2. The real missing pieces are **sub-decisions resolved via PolicyCallbackFn** and **dice-roll outcomes** — these require a new `EngineEvent` stream, not a richer `StepTrace`. Call this "FullGameTrace v0" and keep it additive (do not change existing schemas).
3. Off-policy AWR **does not need richer traces tonight**. The highest-leverage AWR work is adding one context feature and rerunning the arch shoot-out on the existing v5 panel.
4. Full-info MCTS smoke test is cheap (~1-2 h at n_sim=100 over 20-100 seeds) and directly tests whether the value head is calibrated on known-hand states — a critical data point for interpreting the ISMCTS failure.
5. Value-head calibration on existing self-play games is a **prerequisite** to any search-side improvement; it should precede more MCTS tuning. Run it first tonight.
6. `continuation_plan.json` has stale "next_tasks" that can be safely re-derived; move, don't delete.
7. The 8-hour schedule is front-loaded on **measurement** (calibration + MCTS smoke + arch ranking) because those return actionable numbers; C++ trace plumbing is the last piece because it unlocks tomorrow's work, not tonight's.

## Recommendations

1. **[0.5 h] Clean up**: rewrite `continuation_plan.json`, move stray `ts_play_*.jsonl` into `results/selfplay/misc/`, open `results/overnight_log_20260418.md`.
2. **[1.5 h] Value calibration audit**: run `check_value_calibration.py` on v319_sc against 200 paired seeds vs heuristic and 200 vs greedy-self; stratify by turn; write a report; propose temperature-scaling fix if ECE > 0.05.
3. **[2 h] Full-info MCTS smoke test**: `scripts/mcts_fullinfo_smoke.py` — 20-100 seeds × per-decision agreement + paired WR at n_sim=100; write `results/mcts_fullinfo/v319_sc_smoke.md`.
4. **[2 h] AWR arch shoot-out with one new context feature**: add `ar_progress_in_turn` + 6 region-scoring-held flags to scalars; rebuild parquet (or reuse v5 if rebuild tool missing); re-run AWR on 4 arch variants; rank by `val_adv_card_acc`.
5. **[1.5 h] Dispatch full-trace C++ v0**: /dispatch a `cpp-engine-builder` task to add `EngineEvent` stream + `collect_full_traces_jsonl.cpp` tool with a minimal replay-invariant test.
6. **[0.5 h] Advisor + commit + summary**: commit each phase; advisor() before declaring done; final summary in overnight log.
7. **Do NOT** restart PPO (user halt); do NOT delete files (use mv); do NOT skip the build niceness rule; do NOT touch `~/.claude/MEMORY.md` without user request.

## Open Questions

1. Is there an existing AWR rollout-collection script, and does it support multiple checkpoints in one run? If not, Phase D is parquet-reuse only.
2. What is the exact FiLM experiment (PID 441373) reporting metric? If `val_adv_card_acc`, Phase D simply appends variants; if something else, we need to align metrics before ranking.
3. Does `mcts_search_from_state` with full hands actually accept the output of `greedy_state_trace` (which stores hands in `augment_state_dict_with_hidden`)? If not, a thin wrapper is needed.
4. Is the FullGameTrace v0 worth doing tonight or deferring? It is mostly unlocking tomorrow's work — valid to defer if Phases B-D overrun.
5. Are the 5+ panel models already exported to TorchScript `scripted.pt`? If some are only `ppo_best.pt`, export step is needed before trace collection.
