# Iteration tracking for policy handoffs; record each benchmarked change and whether it cleared the acceptance threshold.

| Iter | Blind Spot | Old WR | New WR | Delta | Status | Constants Changed |
| --- | --- | --- | --- | --- | --- | --- |
| 10 | non_coup_milops_penalty | 47.5 | 52.5 | +5.0 | PLATEAU after 3 attempts | influence_mode_bonus 5→6, _NON_COUP_MILOPS_URGENCY_SCALE 8→10 |
| 11 | coup_access_open | 52.5 | ??? | ??? | PENDING_BENCHMARK | _COUP_ACCESS_OPENING_BONUS 7→8 (estimated) |
| 12 | coup_access_refine | 52.5 | ??? | ??? | PENDING_BENCHMARK | _COUP_ACCESS_OPENING_BONUS 8→9 (estimated) |

---

Note: Iter 11-12 have rollout logs but benchmarks incomplete due to WSL memory pressure. Rerun benchmarks with nice 20 + 1 process max.
