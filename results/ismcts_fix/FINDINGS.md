# ISMCTS Failure Analysis — Post-Fix Findings

Date: 2026-04-17
Model: v55_scripted.pt
Search: 4 determinizations × 50 simulations (default)

## Root cause (FIXED)

Pre-fix symptom: ISMCTS vs heuristic = 9.5% combined WR; games ended turn 2-4 via
`defcon1` auto-loss.

Root cause: `AccessibleCache::build` in `cpp/tscore/search_common.hpp` enumerated
legal coup targets at DEFCON=2 without filtering battleground countries. A coup in
any battleground lowers DEFCON by 1; at DEFCON=2→1 the acting side loses (nuclear
war). Search expanded these self-destruct edges and the PUCT prior allowed them
when the NN policy assigned non-trivial mass.

Fix (commit c897a7c): at DEFCON=2, strip `country_spec(cid).is_battleground`
countries from `cache.coup` (not `cache.realign`, which never lowers DEFCON). All
search consumers (MCTS, ISMCTS, batched MCTS) share this choke point.

## Post-fix validation (N=50/side)

| Bucket | USSR WR | US WR | Combined | Mean end turn | Notes |
|---|---|---|---|---|---|
| Greedy NN vs heuristic (ceiling) | 62.0% | 40.0% | **51.0%** | 8.3 | |
| ISMCTS vs heuristic | 8.0% | 18.0% | **13.0%** | 7.8 | defcon1 only 5/100 |
| ISMCTS vs greedy-self | 36.0% | 48.0% | **42.0%** | 8.5 | defcon1 only 9/100 |

Raw: `results/ismcts_fix/validate_n50.txt`

End-reason shift confirms the fix worked:
- Pre-fix ISMCTS vs heuristic: ~50-70% of games ended `defcon1` by turn 4
- Post-fix: only 5/100 games end `defcon1`; majority reach `vp_threshold` or
  `turn_limit` (i.e. games play out normally)

## Why the ISMCTS-vs-self WR *dropped* from 77.5% (pre-fix) to 42% (post-fix)

At first glance this looks like a regression. It is not. The fix lives in
`AccessibleCache::build`, which is used by **both** the ISMCTS search tree **and**
`greedy_action_from_model` (ismcts.cpp:1298: `valid = (mode==Coup) ? cache.coup :
cache.realign`). So post-fix:

- Pre-fix: both sides could self-destruct. Opponent greedy NN occasionally picked a
  battleground coup at DEFCON=2 → nuclear war → opponent auto-loses → free ISMCTS
  win. The 77.5% was inflated by opponent blunders.
- Post-fix: neither side can self-destruct. Opponent plays safely. The "true"
  ISMCTS-vs-greedy-NN WR at 4×50 sims is 42%.

42% < 50% means search is slightly net-negative at this tiny sim budget — a
separate, unrelated phenomenon (noisy determinization + leaf miscalibration at low
simulation counts).

## Remaining gap: opponent-model mismatch (vs heuristic)

ISMCTS vs heuristic (13%) is still far below greedy vs heuristic (51%).
Same search, same model, same legality → the only variable is opponent type.

The NN was trained on self-play distribution (PPO). Its value head and policy prior
are calibrated against NN-like opponents. ISMCTS:
1. Samples opponent moves from NN policy in the tree
2. Evaluates leaf positions with the NN value head

Both assume future play is NN-like. Against heuristic:
- Opponent-in-tree distribution ≠ real opponent distribution
- Leaf values misestimate "what happens after this position" because rollouts
  wouldn't match real heuristic play
- Tree policy optimizes counter-moves against a fictional NN opponent, not against
  the heuristic actually at the board

This is structural, not a bug. Potential mitigations (not pursued here):
1. Use heuristic policy for opponent moves in tree (same as greedy-NN-vs-heuristic)
2. Use MC rollouts with heuristic policy for leaf evaluation (slower but matches
   real opponent)
3. Detect opponent type online and switch eval/policy mode

## Status

- Task #77 (root-cause analysis + fix): **COMPLETED** — defcon1 self-destruct bug
  fixed; 9.5% → 13% combined WR, end-reason distribution healthy
- Task #78 (re-run benchmarks, try n_det/n_sim): **COMPLETED** — sweep across
  (2,25)..(8,100) at N=10 showed no config matches greedy ceiling; opponent-model
  mismatch is structural, not fixable by search budget tuning

## Extended investigation (2026-04-17)

### Budget sweep vs greedy-self (N=20/side, seed=91000)

| n_det | n_sim | rollouts | USSR WR | US WR | combined | secs |
|---|---|---|---|---|---|---|
| 2 | 25 | 50 | 55.0% | 30.0% | 42.5% | 30.3 |
| 2 | 50 | 100 | 40.0% | 25.0% | 32.5% | 50.4 |
| 4 | 50 | 200 | 45.0% | 30.0% | 37.5% | 99.5 |
| 4 | 100 | 400 | 35.0% | 50.0% | 42.5% | 200.1 |
| 8 | 100 | 800 | 35.0% | 40.0% | 37.5% | 452.5 |
| 16 | 100 | 1600 | (USSR half only) | — | — | crashed |

**No correlation between budget and combined WR.** If search worked, 800 rollouts
should dominate 50. Instead it's flat 32-42%. Raw: `sweep_vs_self.txt`.

### Policy-agreement proxy (N=50, USSR only, seed=92000, n_det=4 n_sim=50)

- Greedy USSR WR: 27/50 = **54.0%** (t=4.6s)
- ISMCTS USSR WR:  5/50 = **10.0%** (t=150.9s)
- Paired outcomes (same seed, same opponent):
  - Both win: 4
  - Both lose: 22
  - **Greedy only (ISMCTS flipped a win to loss): 23**
  - ISMCTS only (search rescued a loss): 1
- Mean end-turn: greedy=8.54 vs ismcts=7.78 (search games end 0.76 turns earlier
  → losing by VP threshold faster)

**Net search value: −22 wins out of 50.** Search systematically flips winning
positions into losing ones. Raw: `policy_agreement.txt`.

### Intermittent crash at (n_det=16, n_sim=100, pool=16)

The sweep's final row crashed with `free(): invalid pointer` after completing
all 20 USSR games (1708 batches, 2028088 NN items). Crash occurs during the
transition to US-side games (pool destruction or second-half init).

Repro attempt at **N=10/side** across 4 config variants (`crash_repro.txt`):
- A: n_det=16 n_sim=100 pool=16 (identical to crasher) — **OK** 30.0%
- B: n_det=16 n_sim=50  pool=16                       — **OK** 35.0%
- C: n_det=16 n_sim=100 pool=4                        — **OK** 30.0%
- D: n_det=12 n_sim=100 pool=16                       — **OK** 45.0%

**Crash is scale-dependent, not config-dependent.** Triggers only at
N≥20/side (~40 games total). Likely heap accumulation (fragmentation or small
OOB write that corrupts glibc metadata slowly) rather than an invariant break
per-search. Fixing requires valgrind or ASAN on a 40-game run; deferred as
lower-leverage than the systematic search-quality bug.

### Primary finding

The real bug is not the crash — it's the 23/50 same-seed win→loss flips.
Search with a 1600-rollout budget fails to match greedy argmax. Hypotheses:

1. **Value head miscalibrated under determinization.** NN value was trained on
   public state; ISMCTS feeds it a sampled full state (determinized opponent hand).
   If the sampled hand is wrong, leaf values mislead the search.
2. **Visit-argmax vs policy-argmax divergence.** ISMCTS returns the visit-argmax
   child. At low simulation counts, visits track PUCT priors more than value
   confidence; the final action may be the most-explored-due-to-prior, not the
   highest-value. Needs introspection binding (`ismcts_policy_at_state`).
3. **Opponent-model mismatch inside the tree.** Tree uses NN for opponent moves;
   opponent in the benchmark also plays NN-greedy. But the search side assumes
   stationary opponent policy; single-iteration PUCT may not converge to a
   best-response policy.

Next action: add `ismcts_policy_at_state` binding; at ~20 real root states
compare NN argmax, ISMCTS visit-argmax, and NN value estimate of each top-K
child. Localize whether the failure is selection (2) or evaluation (1).

### Distribution-shape diagnostic (2026-04-18)

Added `tscore.ismcts_search_from_state` binding (mirrors `mcts_search_from_state`
but calls `ismcts_search` on the equivalent Observation). Runs ISMCTS at a mined
root state and returns per-legal-action `prior` (NN softmax, post-mask) and
`visits` (ISMCTS visit count). Script: `scripts/ismcts_distribution_shape.py`.

Ran 50 mined v84 hard positions at n_det=4, n_sim=50, c_puct=1.5 with v55_scripted.

| metric | value |
|---|---|
| Edge-level top-1 match (card+mode) | **96% (48/50)** |
| Card-level top-1 match | **100% (50/50)** |
| Mean NN entropy (over legal actions) | 4.43 |
| Mean ISMCTS entropy | 2.49 |
| Mean max(NN prior) | 0.192 |
| Mean visit concentration (max/total) | 0.357 |
| Mean JS(NN‖ISMCTS) | 0.266 |
| Mean Spearman ρ over priors vs visits | +0.47 |
| q_gap > +0.01 (search found better) | 1/50 (2%) |
| q_gap < −0.01 (search found worse) | 1/50 (2%) |
| mean q_gap | −0.001 |

Raw: `results/ismcts_fix/distribution_shape.jsonl` + `.txt`.

**Interpretation.** ISMCTS is essentially a no-op at the card level at these roots.
It just sharpens the per-action distribution. The 2 edge disagreements were
different *modes* of the same card (coup vs event vs space); q-gap to the NN
pick was zero within noise.

This rules out "search picks a different card and loses" at the root. The
−22/50 win-flip signal from `policy_agreement.txt` must therefore come from:

1. **Cumulative mode flips across ~20 decisions/game.** 4% edge-level disagreement
   per decision × 20 decisions ≈ 56% of games have ≥1 mode flip. If these flips
   are systematically worse (e.g. coup→event when coup was correct), they
   compound into game losses.
2. **Mined positions ≠ typical game states.** v84 hard positions may skew toward
   stable decisions where search agrees with greedy. In-game states from the
   heuristic-opponent benchmark likely contain more ambiguous mid-value
   situations where NN argmax is itself unconfident (low max-prior) and small
   differences in leaf value estimation flip the top action.
3. **Determinization variance under ISMCTS.** With n_det=4 and n_sim=50, each
   determinization only gets 50 rollouts; aggregated visits are noisy.

**Next probe.** Extract ~50 actual mid-game decision states (not v84 mined
positions) via a collector callback that dumps state_dicts during a real
heuristic-opponent benchmark, then re-run the diagnostic. If disagreement rate
climbs from 4% to 20-30% on in-game states, hypothesis (2) is correct.

### Two source bugs landed (2026-04-18)

Opus strategy review found two latent bugs in source:

**Bug 1 — UAF in `cpp/tscore/ismcts.cpp:RawBatchOutputs::extract`.**
`auto cont_card = outputs.card_logits.contiguous()` is a local Tensor; its
storage is freed when `extract()` returns. `raw.card_logits` then points to
freed memory. The sibling `mcts_batched.cpp:RawBatchOutputs` keeps `_storage`
Tensor fields as members. Transplanted the `_storage` pattern into ismcts.cpp.
This is the likely root cause of the scale-dependent `free(): invalid pointer`
crash seen at n_det=16 n_sim=100 pool=16 N≥20/side (task #80).

**Bug 2 — Dirichlet noise leaks into eval benchmarks.** `MctsConfig` defaults
to `dir_alpha=0.2, dir_epsilon=0.25`. `IsmctsConfig::mcts_config` inherits
these defaults. `apply_root_dirichlet_noise` is called unconditionally in all
four ISMCTS paths (ismcts.cpp:2061,2112,2246,2296). Fix: override `IsmctsConfig`
default initializer to set `mcts_config.dir_alpha=0, dir_epsilon=0`. Benchmarks
that want noise can opt in explicitly (same as `mcts_batched.hpp` already does).

Commit: see `Fix ISMCTS UAF + Dirichlet leak` — closes task #80.

### Post-fix measurements (2026-04-18)

| Metric | Pre-fix | Post-fix |
|---|---|---|
| Mined-pos edge top-1 match (N=50) | 96.0% | **100.0%** |
| Mined-pos card top-1 match | 100.0% | 96.0% |
| Mean NN entropy | 4.43 | 3.61 |
| Mean ISMCTS entropy | 2.49 | 2.03 |
| Mean max(prior) | 0.19 | 0.26 |
| Mean visit concentration | 0.36 | 0.40 |
| Paired benchmark: greedy USSR WR | 54% (27/50) | 54% (27/50) |
| Paired benchmark: ISMCTS USSR WR | 10% (5/50) | 12% (6/50) |
| Net search value (win flips) | −22 | **−21** |

Raw: `distribution_shape_postfix.{jsonl,txt}`, `policy_agreement_postfix.txt`.

**Interpretation.** The Dirichlet fix sharpened the NN prior distribution and
removed the 2 mined-position edge-flips (they were noise). But the in-game
search-harm is essentially unchanged (−22 → −21). Therefore:

1. ISMCTS agrees with NN argmax 100% at mined v84 root states.
2. ISMCTS disagrees enough with NN argmax at **in-game states** during the
   heuristic-opponent benchmark to flip 24 wins to losses.
3. These two facts together imply that **v84 mined positions are not a
   representative sample of the states ISMCTS encounters in real games**.
   Mined positions come from self-play trajectories where the NN was confident
   enough to act. The benchmark-against-heuristic reaches different mid-game
   states where NN priors are shallower and visit concentration flips the top
   pick.

**Remaining action.** Per Opus strategy §5: if vs-heuristic stays weak while
vs-self recovers, do not chase further here. FINDINGS.md already documents
opponent-model mismatch as structural. Punt to follow-up:

- [x] Re-run `ismcts_sweep_vs_self.py` post-fix: still flat (results/ismcts_fix/sweep_vs_self_postfix.txt shows 42% at 800 rollouts); UAF+Dirichlet did NOT fix the plateau
- [ ] Add state_dict collector for in-game states (out of scope for this investigation pass)
- [ ] Value-head-under-determinization probe (§4 Opus strategy): root cause identified below

### First-divergence probe (2026-04-17/18)

Added `tscore.greedy_state_trace` binding (C++/pybind11, commit e789c3a): plays a
greedy-NN vs heuristic game and returns per-decision state dicts with both hands and
deck, compatible with `game_state_from_dict`. Added `scripts/ismcts_first_divergence.py`
to find the first state where ISMCTS disagrees with greedy.

**Key results:**
- Seed 12345 (skip-headline): first divergence at step 1 (turn=1, AR1)
  - Greedy: card 24 (Indo-Pak War), mode 0 (Influence), targets [11=Norway, 16=Turkey]
  - ISMCTS: card 24, mode 3 (Space), targets []
- Seed 54321 (skip-headline): first divergence at step 1 (turn=1, AR1)
  - Greedy: card 24, mode 1 (Coup), targets [4=Denmark]
  - ISMCTS: card 24, mode 0 (Influence), targets []
- Pattern: card choice is consistent with greedy; **mode choice flips**

### Budget convergence probe (2026-04-18)

Script `scripts/ismcts_budget_convergence.py`: load seed-12345 AR1 divergence state,
run ISMCTS at n_det=4 with n_sim=50,100,200,400,800. Does mode converge to greedy?

| n_sim | ISMCTS pick | visits | root_value |
|-------|-------------|--------|------------|
| 50    | card 24 mode 3 (Space) | 44 | -0.124 |
| 100   | card 24 mode 3 (Space) | 74 | -0.127 |
| 200   | card 24 mode 3 (Space) | 130 | -0.147 |
| 400   | card 24 mode 3 (Space) | 173 | -0.170 |
| 800   | card 24 mode 3 (Space) | 245 | -0.189 |

**ISMCTS never converges to greedy's Influence pick at any budget.** Root value
degrades monotonically as budget grows (more rollouts → more pessimism → search is
drawing more negative values from the tree, not converging to greedy confidence).

Mode 0 (Influence) has HIGHER prior (0.176 > 0.133) than mode 3 (Space), but PUCT
consistently gives more visits to mode 3. This means the rollouts from Space nodes
return consistently BETTER values than rollouts from Influence nodes, flipping the
visit-argmax against the NN prior.

### Root-cause conclusion: value-head bias under determinization

The greedy NN (evaluated on the true observation with the true opponent hand) says
"Influence is best." ISMCTS rollouts (sampling opponent hand from the unknown
pool) say "Space is better." This disagreement is **stable across 800 simulations**
and does not converge. This is the value-head-under-determinization hypothesis from
Opus §1.3(c):

> *If the value head's error on hallucinated hands is biased rather than zero-mean,
> search will consistently over- or under-weight particular subtrees and not converge.*

Mechanically: when the opponent hand is sampled, USSR's aggressive Influence plays
in contested regions may look riskier (more powerful opponent cards in hand),
pushing the search toward the safer Space play. The true opponent hand is weaker,
so the real-game Influence play is strong but the search doesn't know this.

**This requires a training-side fix**, not a search-side patch:
- Option A: Train value head on determinized observations (expose sampled opponent
  hand during training so the head learns to handle hallucinated hands)
- Option B: Replace NN value head with MC rollouts using the true (heuristic) opponent
  in the benchmark (structural fix, not general)
- Option C: Retrain with opponent-hand awareness in the observation encoder

All three are out of scope for a search-only patch. **ISMCTS with v55 is not
production-ready** — the value head was not trained to handle determinized states.

**Investigation closed on this model.** Reopen when a new model trains with
determinization-aware observations or when Option B is tested.

## Artifacts

- `scripts/ismcts_validate.py` — N=50/side validation (3 buckets)
- `scripts/ismcts_sweep.py` — n_det × n_sim sweep at N=10
- `scripts/ismcts_failure_diag.py` — initial diagnostic (N=10, 3 buckets)
- `scripts/ismcts_log_one.py` — single-game TS_ACTION_LOG=1 harness
- `scripts/ismcts_first_divergence.py` — find first greedy/ISMCTS disagreement in a game
- `scripts/ismcts_budget_convergence.py` — load divergence state, sweep n_sim, check convergence
- `results/ismcts_fix/validate_n50.txt` — validation output
- `results/ismcts_fix/sweep_n10.txt` — sweep output
- `results/ismcts_fix/diag_postfix_n10.txt` — first post-fix diagnostic
- `results/ismcts_fix/first_divergence_v55_ar.json` — seed=12345 AR1 divergence state
- `results/ismcts_fix/first_divergence_v55_ar_s54321.json` — seed=54321 AR1 divergence state
- `results/ismcts_fix/budget_convergence.json` — n_sim sweep on seed-12345 AR1 state
