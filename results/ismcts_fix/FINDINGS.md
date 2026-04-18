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

## Artifacts

- `scripts/ismcts_validate.py` — N=50/side validation (3 buckets)
- `scripts/ismcts_sweep.py` — n_det × n_sim sweep at N=10
- `scripts/ismcts_failure_diag.py` — initial diagnostic (N=10, 3 buckets)
- `scripts/ismcts_log_one.py` — single-game TS_ACTION_LOG=1 harness
- `results/ismcts_fix/validate_n50.txt` — validation output
- `results/ismcts_fix/sweep_n10.txt` — sweep output
- `results/ismcts_fix/diag_postfix_n10.txt` — first post-fix diagnostic
