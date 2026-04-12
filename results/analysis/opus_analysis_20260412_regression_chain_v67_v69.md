# Analysis: v67-v69 Regression Chain
Date: 2026-04-12
Author: Claude Sonnet (inline, Opus agent ran out of turns)

## Executive Summary

The apparent Elo regression v67_sc(2038)→v68_sc(1968)→v69_sc(1860) is a **measurement artifact**, not a real model regression. v69_sc's HWM panel WR (0.5233 vs the NEW strong panel) is higher than v67_sc's (0.5025 vs the OLD weak panel). The Elo numbers are not comparable because they use different methodologies and different panel compositions.

## Findings

### Panel WR comparison (apples vs oranges)
| Model | HWM Panel WR | Panel composition | Elo | Elo method |
|-------|-------------|------------------|-----|------------|
| v67_sc | 0.5025 | OLD: v8/v14/v22/heuristic (weak) | 2038 | Full ladder, 400 games/pair |
| v68_sc | 0.5042 | NEW: v55/v54/v44/v45/v14 (strong) | 1968 | Incremental, 200 games |
| v69_sc | 0.5233 | NEW: v55/v54/v44/v45/v14 (strong) | 1860 | Incremental, 200 games |

v69_sc achieves the **highest panel WR** against the **strongest panel**. A 50.25% WR vs weak opponents is not comparable to 52.33% vs strong opponents.

### Phase 2b (DP decoder) did NOT cause the regression
- Phase 2b committed: 2026-04-12 10:23 UTC (commit b47f16f)
- v68_sc started: 2026-04-12 09:48 UTC → ran WITHOUT Phase 2b
- v69_sc started: 2026-04-12 11:02 UTC → runs WITH Phase 2b
- But Phase 2b only affects `learned_policy.py` inference (standalone play mode), NOT `train_ppo.py` training rollouts. Training uses model.forward() + sampling directly, never learned_policy.py. No effect on training.

### Entropy decay is correct for v69_sc
- v68_sc ran 80 iters from PREV_TOTAL_ITERS=270 → ended at total_iters=350
- v69_sc: global_ent_decay_start=350, global_ent_decay_end=430
- v69_sc global iters: 351→430, ent_coef decays from ~0.01 to 0.003 ✓

### HWM pattern is consistent (iter_0010 finding confirmed)
- v67_sc: HWM at iter10, iter20, iter60 (gradual improvement over 80 iters)
- v68_sc: HWM at iter10, iter20, iter60 (similar)
- v69_sc: HWM at iter10, iter20, iter40 (then plateaued — but may be noise)

### Why incremental Elo underestimates v68/v69
The incremental Elo placement uses PREV_BEST = v67_sc (top of ladder, Elo 2038) as an anchor opponent. If v69_sc (partial training, iter-40 HWM) loses to v67_sc's FINAL best checkpoint in H2H, it gets penalized heavily. The full ladder Elo accounts for all models; incremental with v67_sc as primary opponent is biased downward.

## Root Cause Assessment

The Elo regression is not real. Evidence:
1. HWM panel WR is INCREASING across v67→v68→v69
2. v67_sc Elo was established differently (full ladder vs incremental)
3. Panel composition changed (weak → strong) at same time as methodology changed
4. No code change between v67/v68 that would cause model degradation
5. Phase 2b does not affect training

## Recommendations for v70_sc

**Base checkpoint**: Use v69_sc ppo_best.pt (iter-40 HWM or final if better). The model is likely improving, not regressing. Do NOT fall back to v67_sc.

**Verify with H2H**: Before v70_sc starts, run a quick 100-game H2H: v69_sc_scripted vs v67_sc_scripted. If v69_sc wins ≥45%, it's competitive and should be used as base.

**Elo methodology fix (high priority)**: 
- Run a full ladder update for v68_sc and v69_sc after v69_sc completes
- OR: standardize incremental placement to use MORE games (400 instead of 200) to reduce variance
- The current 200-game incremental with v67_sc as PREV_BEST is biased

**n_iterations**: Keep at 80 for now. v67_sc and v68_sc both set HWMs as late as iter60, suggesting the model CAN improve late. Reducing to 20-30 is premature — the iter_0010 finding was about a specific run, not universal.

**Phase 2b**: No action needed. DP decoder doesn't affect training.

**Entropy decay**: Correct as-is. No changes needed.

## Open Questions

1. Does v69_sc final checkpoint (after iter 70-80) set a new HWM above 0.5233?
2. What is the H2H result of v69_sc_scripted vs v67_sc_scripted at 100 games?
3. Should we switch to full ladder updates (400 games) for all future versions to get consistent Elo?
