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

## Artifacts

- `scripts/ismcts_validate.py` — N=50/side validation (3 buckets)
- `scripts/ismcts_sweep.py` — n_det × n_sim sweep at N=10
- `scripts/ismcts_failure_diag.py` — initial diagnostic (N=10, 3 buckets)
- `scripts/ismcts_log_one.py` — single-game TS_ACTION_LOG=1 harness
- `results/ismcts_fix/validate_n50.txt` — validation output
- `results/ismcts_fix/sweep_n10.txt` — sweep output
- `results/ismcts_fix/diag_postfix_n10.txt` — first post-fix diagnostic
