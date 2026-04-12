---
# Opus Analysis: Overlapping candidate tournament design
Date: 2026-04-12T14:30:00Z
Question: WS7 made the candidate tournament non-blocking so run N+1 starts from ppo_final.pt immediately. But ppo_final.pt is historically often the WORST checkpoint. Can we do "true overlapping" where the next run doesn't start from a bad checkpoint, while still not blocking? Also rename "confirmation tournament" to "candidate tournament" throughout.
---

## Executive Summary

The data is unambiguous: **ppo_final.pt is systematically the worst or near-worst checkpoint**. Across 29 analyzed runs, 83% of the time (24/29) the final checkpoint is more than 1pp worse than the best, with an average panel WR gap of 4.7pp and an average Elo drop of 76 points (median 82, max 127). The best checkpoint falls in the first 30% of training 62% of the time (18/29 runs). Starting from ppo_final.pt wastes the first ~10-20 iters of the next run just recovering to the quality that ppo_best.pt already has.

**Recommended approach: Option F ("Eager Best")** -- a hybrid not in the original five options. Save ppo_running_best.pt during training whenever a new panel-eval high-water mark is achieved. The next run starts from the latest ppo_running_best.pt (which is available the moment the run ends, no tournament needed). The full candidate tournament still runs in the background for scripted_for_elo/ and Elo placement, but does NOT gate the next run's warm-start.

This gives all of WS7's non-blocking benefit while eliminating the ~76 Elo penalty of starting from ppo_final.pt. Implementation is ~20 lines of Python in train_ppo.py.

## Findings

### Historical ppo_final vs ppo_best divergence

#### Panel WR data (29 runs, v38-v65)

| Metric | Value |
|--------|-------|
| Runs where final > 1pp worse than best | 24/29 (83%) |
| Average gap (best - final) | 4.7pp |
| Best checkpoint in first 30% of training | 18/29 (62%) |
| Best checkpoint in first 50% of training | 22/29 (76%) |
| Best checkpoint IS the final checkpoint | 4/29 (14%) |

#### Elo data from confirmation tournaments (14 runs, v48-v61)

| Metric | Value |
|--------|-------|
| Mean Elo drop (best - final) | 76 |
| Median Elo drop | 82 |
| Max Elo drop | 127 (v61) |
| Runs with > 50 Elo drop | 9/14 (64%) |
| Runs with > 100 Elo drop | 2/14 (14%) |

The pattern is clear and consistent: PPO training in this setup peaks early (typically iter 10-30 out of 70-80) and then degrades. This is a known PPO pathology -- later iterations overfit to the current opponent distribution or suffer entropy collapse.

#### Why does training degrade?

The confirmation tournament Elo data shows a monotonically declining trend in the v55-v61 era:
- v55: iter20=2122, iter70=2024 (-98)
- v57: iter10=2079, iter70=1977 (-102)
- v59: iter10=2012, iter70=1915 (-97)
- v61: iter10=1983, iter70=1856 (-127)

This is consistent with PPO's well-known "unlearning" problem: the policy keeps improving its loss against the training distribution but degrades on the broader panel. Entropy annealing from 0.01 to 0.003 may be too aggressive, or the league opponents become too narrow late in training.

### Option analysis

#### Option A: Keep WS7 as-is (start from ppo_final.pt immediately)
- **Latency**: 0 min (non-blocking)
- **Quality**: Poor. On average, the next run starts from a checkpoint ~76 Elo worse than the run's best. The first 10-20 iters of the next run are wasted recovering this ground.
- **Wasted GPU-hours**: ~12-25% of each run (10-20 out of 80 iters just to recover)
- **Verdict**: Unacceptable as the permanent solution given the systematic degradation.

#### Option B: Start from ppo_best.pt of run N-1 (previous generation's vetted best)
- **Latency**: 0 min (non-blocking, ppo_best.pt from N-1 is always available when N finishes)
- **Quality**: Good for the warm-start, but skips an entire generation of learning. If run N made genuine progress, that progress is lost.
- **Risk**: Two consecutive bad runs could cause the lineage to stall since you always go back to N-1's best.
- **Verdict**: Safe but wasteful -- throws away all of run N's gains.

#### Option C: Start from ppo_final.pt, inject checkpoint switch mid-run
- **Latency**: 0 min start, ~20-30 min to switch
- **Quality**: Theoretically optimal -- the next run recovers once ppo_best.pt is available
- **Complexity**: Very high. Requires:
  - Hot-reloading model weights mid-training
  - Preserving optimizer state or deciding to reset it
  - Preserving WR table / UCB state
  - Handling the case where first 10 iters are now from a different lineage
  - Making league pool iter_*.pt consistent despite the switch
- **Risk**: Subtle bugs from mid-run checkpoint switching. Mixed lineage iter checkpoints confuse the next candidate tournament.
- **Verdict**: Too complex for the benefit. The "wasted" 10 iters from Option A are cheaper than debugging this.

#### Option D: Revert WS7 (block on candidate tournament, parallelize Elo placement)
- **Latency**: 20-30 min (candidate tournament blocks, Elo placement parallelized)
- **Quality**: Optimal -- always starts from ppo_best.pt
- **GPU utilization**: GPU idle for 20-30 min between runs (~10-20% utilization loss for 2-4h runs)
- **Verdict**: Correct but wasteful. 20-30 min idle per 2-4h run is ~8-15% GPU waste, comparable to the iter-recovery waste from Option A. Net effect is roughly a wash, but at least the quality is predictable.

#### Option E: Pre-start tournament on last N iters before training finishes
- **Latency**: Near-zero if prediction works
- **Quality**: Good, but requires:
  - Predicting when training will end (easy if fixed 80 iters)
  - Running tournament on the last-seen checkpoints, which may not include the actual best
  - Re-running tournament if a checkpoint after the prediction is better
- **Complexity**: Moderate. Need a "trigger at iter 70" mechanism.
- **Risk**: If best is iter 10 (as is common), running tournament on iters 60-80 misses it entirely.
- **Verdict**: Does not solve the core problem -- best is usually early, not late.

#### Option F (RECOMMENDED): Eager Best -- save ppo_running_best.pt during training
- **Latency**: 0 min (non-blocking)
- **Quality**: Near-optimal. The running best is updated every eval-every iters during training. By the time training ends, ppo_running_best.pt IS the best checkpoint (identical to what the candidate tournament would select, minus the round-robin tiebreaker noise).
- **Complexity**: Minimal (~20 lines in train_ppo.py)
- **Implementation**:
  1. After each panel eval in train_ppo.py, compare avg_combined_wr to a running high-water mark
  2. If new high, copy the current checkpoint to `ppo_running_best.pt` and `ppo_running_best_scripted.pt`
  3. In ppo_loop_step.sh, prefer ppo_running_best.pt > ppo_best.pt > ppo_final.pt
  4. Background candidate tournament still runs for Elo anchoring and scripted_for_elo/, but does NOT gate the warm-start
- **Risk**: Almost none. The running best is exactly the same as what ppo_confirm_best.py selects (both use panel eval WR). The only difference is that ppo_confirm_best.py runs a round-robin among top-N to break ties, but with avg gaps of 76 Elo, there's no meaningful tie to break.
- **GPU waste**: 0 min idle, 0 wasted recovery iters
- **Verdict**: Best of all options.

### Comparison matrix

| Option | Latency | Quality | Complexity | GPU waste |
|--------|---------|---------|------------|-----------|
| A (WS7 as-is) | 0 min | Poor (-76 Elo) | None | ~15% (recovery iters) |
| B (N-1 best) | 0 min | Mediocre (skip gen) | Low | ~0% but skips generation |
| C (inject switch) | 0 min | Best | Very high | ~0% |
| D (revert WS7) | 20-30 min | Optimal | Low | ~10% (GPU idle) |
| E (pre-start) | ~5 min | Poor (misses early best) | Moderate | ~5% |
| **F (Eager Best)** | **0 min** | **Near-optimal** | **Low (~20 LoC)** | **~0%** |

## Conclusions

1. **ppo_final.pt is systematically bad**: 83% of runs show degradation, averaging 4.7pp / 76 Elo. This is not noise -- it's a structural PPO unlearning problem where the best checkpoint is in the first 30% of training 62% of the time.

2. **Option F (Eager Best) is the clear winner**: It combines WS7's zero-latency non-blocking property with near-optimal checkpoint quality, at minimal implementation cost.

3. **The candidate tournament should still run** for two purposes: (a) producing the scripted checkpoint for scripted_for_elo/ with proper Elo anchoring, and (b) validating that the running-best selection is correct. But it should be purely informational -- it should not gate the next run.

4. **The deeper problem is PPO unlearning**: The fact that iter 10 is usually best suggests training runs are too long, entropy annealing is too aggressive, or the league distribution shifts too much during a run. Consider: (a) reducing runs to 40 iters instead of 80, (b) making entropy annealing slower, or (c) implementing early stopping based on panel eval. However, these are separate from the overlapping-tournament question.

5. **Rename**: "confirmation tournament" should become "candidate tournament" throughout, since its purpose is to select the best candidate checkpoint, not to "confirm" anything.

## Recommendations

### Immediate (implement now)

1. **Add running-best tracking to train_ppo.py**: After each panel eval, compare to high-water mark and save ppo_running_best.pt if improved. ~20 lines of code.

2. **Update ppo_loop_step.sh checkpoint preference order**: `ppo_running_best.pt > ppo_best.pt > ppo_final.pt`.

3. **Rename "confirmation" to "candidate"** in:
   - `scripts/ppo_loop_step.sh` (comments and log messages)
   - `scripts/ppo_confirm_best.py` (docstring, print messages; optionally rename file to `ppo_candidate_best.py`)
   - `scripts/post_train_confirm.sh` (comments and log messages; optionally rename to `post_train_candidate.sh`)
   - `Snakefile.ppo` (rule names and comments)
   - `results/autonomous_decisions.log` entries (future only)

### Short-term (next iteration)

4. **Consider reducing run length from 80 to 40 iters**: Since the best checkpoint is almost always in the first 30 iters, running 80 iters wastes GPU time on degradation. Two 40-iter runs with candidate selection would be strictly better than one 80-iter run.

5. **Consider panel-eval-based early stopping**: If panel WR has declined for 3 consecutive eval points (30 iters), stop the run early and save GPU time.

### Implementation sketch for Option F

```python
# In train_ppo.py, after panel eval results are computed:
if avg_combined_wr > best_combined_wr:
    best_combined_wr = avg_combined_wr
    best_combined_iter = iteration
    # Save running best
    running_best_path = os.path.join(args.out_dir, "ppo_running_best.pt")
    shutil.copy2(new_ckpt_path, running_best_path)
    running_best_scripted = os.path.join(args.out_dir, "ppo_running_best_scripted.pt")
    shutil.copy2(scripted_path, running_best_scripted)
    logger.info(f"New running best: iter {iteration} (combined_wr={avg_combined_wr:.3f})")
```

```bash
# In ppo_loop_step.sh, update checkpoint selection:
FINISHED_CHECKPOINT="${FINISHED_DIR}/ppo_final.pt"
if [ -f "${FINISHED_DIR}/ppo_running_best.pt" ]; then
  FINISHED_CHECKPOINT="${FINISHED_DIR}/ppo_running_best.pt"
  echo "... Using ppo_running_best.pt ..." >> results/autonomous_decisions.log
elif [ -f "${FINISHED_DIR}/ppo_best.pt" ]; then
  FINISHED_CHECKPOINT="${FINISHED_DIR}/ppo_best.pt"
fi
```

## Open Questions

1. **Should we rename the file ppo_confirm_best.py to ppo_candidate_best.py?** This is a cosmetic rename with no functional impact but affects script references in logs.

2. **Is 80 iters justified?** The data strongly suggests 40 iters would capture all meaningful learning. This is independent of the overlapping-tournament question but would halve both training time and the final-vs-best gap.

3. **What causes the early-peak pattern?** Is it entropy collapse, league distribution shift, or optimizer state issues? Understanding this would inform whether to fix the symptom (better checkpoint selection) or the cause (shorter runs / better entropy schedule).

4. **Should the candidate tournament still produce ppo_best.pt?** With running-best tracking, ppo_best.pt from the tournament becomes redundant for warm-starting. It could still be useful for scripted_for_elo/ if the tournament's round-robin gives a more reliable Elo estimate than panel eval alone.
