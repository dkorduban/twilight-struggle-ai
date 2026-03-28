# Iteration tracking for policy handoffs; record each benchmarked change and whether it cleared the acceptance threshold.

| Iter | Blind Spot | Old WR | New WR | Delta | Status | Constants Changed |
| --- | --- | --- | --- | --- | --- | --- |
| 10 | non_coup_milops_penalty | 47.5 | 52.5 | +5.0 | ACCEPT | influence_mode_bonus 5→6, _NON_COUP_MILOPS_URGENCY_SCALE 8→10 |
| 11 | coup_access_open | 52.5 | 52.7 | +0.2 | BELOW_THRESHOLD | _COUP_ACCESS_OPENING_BONUS 7→8 (est) |
| 12 | coup_access_refine | 52.7 | 53.0 | +0.3 | BELOW_THRESHOLD | _COUP_ACCESS_OPENING_BONUS 8→9 |

---

Symmetric benchmark iter 10 vs iter 12: 100 paired games (200 total), draws=6. Iter 11-12 cumulative +0.5% from iter 10 baseline (below individual 2% threshold). Plateau approaching; recommend structural improvement phase next.

## Baseline Established

baseline_established: true
baseline_version: iter12_wr53.0%
baseline_policy_file: python/tsrl/policies/baseline_iter12.py
next_phase: structural_improvements (DEFCON-4 safety, endgame gamble, region balance, scoring urgency)
