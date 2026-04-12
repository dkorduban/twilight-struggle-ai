# Opus Analysis: SC Plateau Breakthrough
Date: 2026-04-12

## Executive Summary

The SC chain is stuck at Elo ~2096 because it is **actively degrading a stronger starting checkpoint** rather than improving it. v72_sc started from v55 (Elo 2118) and ended 25 Elo lower. The root cause is a compounding triple failure:

1. **Entropy shock**: v55 was trained with ent_coef=0.01. v72_sc resets to ent_coef=0.03 with optimizer reset -- this immediately destabilizes the specialized policy v55 had learned, pushing it toward more uniform (weaker) action distributions.

2. **Fixture pool is illusory**: Despite 27 fixtures, PFSP concentrates on only 2 external opponents (v55 and v45). The other 25 fixtures are never sampled. The model is functionally doing self-play + playing two equal-strength opponents, producing ~43% overall WR -- pure noise with no gradient signal.

3. **Iteration starvation**: The v44-v55 lineage accumulated 4,233 iterations of training. The SC chain has done 150 total (28x fewer). Even v72_sc's 120 iters peaked at iter60 and stalled -- but this stall is at a LOCAL optimum 25 Elo below the starting checkpoint, not at a frontier.

The SC chain should be abandoned in its current form. The most productive path is to continue the v55 lineage directly (v56+), using self-play-dominated training with ent_coef=0.01 and 80-200 iters per generation -- the exact recipe that produced v55 in the first place.

## Root Cause of Plateau

### The entropy shock mechanism (primary cause)

v55 trained for 80 iterations at ent_coef=0.01, ending with actual policy entropy ~3.84. This is a well-specialized policy where the model has learned strong preferences.

v72_sc starts from v55 but with:
- `ent_coef=0.03` (3x higher than v55's training)
- `--reset-optimizer` (wipes Adam momentum/variance)
- Entropy bonus decaying from 0.03 to 0.01 over 120 iterations

The 3x entropy bonus immediately pushes the policy toward more uniform distributions. Combined with the optimizer reset (which loses all accumulated gradient statistics), this is equivalent to deliberately blurring a sharp policy. The model spends 60 iterations recovering from this self-inflicted wound, reaching its local HWM at iter60 -- but never recovers to v55's original quality because:

- The entropy bonus (ent_coef=0.02 at iter60) is still 2x what v55 had
- The policy has been pushed into a different region of parameter space
- Self-play and strong fixtures provide no gradient to escape

Evidence: v72_sc actual entropy is 3.93-4.10 throughout training (higher than v55's 3.84-4.17 range, but v55 started higher and fell to 3.84 by iter80). The entropy bonus prevents the policy from sharpening.

### The fixture concentration failure (secondary cause)

The SC fixture pool has 27 models, but PFSP with exp=1.5 concentrates all external games onto v55_scripted (69 selections in 120 iters) and v45_scripted (61 selections). The other 25 fixtures were never selected once.

This means the "scripted curriculum" is functionally: self-play + v55 + v45. The model faces two opponents it can barely beat (both Elo 2095-2118), producing 50% WR -- pure noise. There is no difficulty gradient in the curriculum.

Compare to v55's training: almost exclusively self-play (5 total external games in 80 iters). Self-play is also ~50% WR, but it has a crucial advantage: the opponent evolves with the learner, creating a natural curriculum. Fixed fixtures don't evolve.

### Why iter10 is always the HWM in 30-iter runs

In 30-iter runs (v75_sc, v76_sc), iter10 is always the HWM because:

1. **Iter 1-10**: The optimizer is fresh (reset). The first 10 iterations make the largest per-step improvement because KL divergence is unconstrained and gradient signals from the WR-table warmup are strongest. This is the "easy gains" phase where the model recovers basic competence after the entropy/optimizer reset.

2. **Iter 10-30**: The model has already converged to its local optimum. With ent_coef decaying linearly from 0.03 to 0.01 over 30 iters, the entropy bonus is still relatively high (0.02-0.01). The policy loss (pl=-0.012 to -0.015) and value loss (vl=0.10-0.12) show no trend -- the model is oscillating, not improving.

3. **Panel measurement noise**: With 30 games per panel opponent (150 total), the 95% CI on panel avg is approximately +/- 4 percentage points. A measured HWM of 0.472 vs 0.488 is within noise. The iter10 HWM is likely a measurement artifact as much as a real peak.

In v72_sc's 120-iter run, the pattern is more revealing: panel WR oscillates between 0.42-0.57 with no trend. Iter60 (0.565) and iter100 (0.549) are the highest, but iter30 (0.424) and iter20 (0.448) are lowest. This is noise around ~0.49, not a learning curve.

## Why the Chain Starts at 2097 and Stays at 2097

The chain has converged to a stable attractor:

- v72_sc: starts from v55 (2118), degrades to 2097
- v75_sc: starts from v72_sc best (2097), stays at 2096  
- v76_sc: starts from v75_sc best (~2096), expected to stay at ~2096

The 2096-2097 Elo point is where the entropy-shocked, fixture-trained policy naturally settles. It is approximately 22 Elo below v55 because:

1. The ent_coef=0.03 start permanently softens the policy compared to v55's ent_coef=0.01 final state
2. Training against v55_scripted and v45_scripted provides no upward gradient (50% WR = noise)
3. 30 iterations is not enough to sharpen the policy back to v55-level specialization
4. The chain preserves the damage: each generation starts from the previous damaged best, not from v55

This is a **convergent trap**, not a plateau. More iterations within the same config will not help -- v72_sc proved this with 120 iters showing no improvement after iter60.

## Specific Recommendations (ranked by expected impact)

### 1. Abandon SC, resume v55 lineage (expected: +0-30 Elo, highest confidence)

The v44-v55 recipe works. Resume it:
- Start v56 from v55 ppo_best
- Config: ent_coef=0.01 (constant, no decay), lr=2e-05, clip=0.12
- Self-play only (no external fixtures), k=4-6
- 80-200 iterations
- Panel eval against v55/v54/v44/v45/v14

This is the lowest-risk path. v44-v55 accumulated strength over 1233 iterations of self-play. The SC chain disrupted this by introducing entropy shock and fixture noise.

### 2. If continuing SC: remove entropy shock (expected: +10-25 Elo recovery)

If SC must continue, the single most impactful change is:
- Start from v55 ppo_best
- Use `ent_coef=0.01` (matching v55's training), NOT 0.03
- Do NOT reset optimizer (use `--no-reset-optimizer` if available)
- This preserves v55's policy specialization instead of destroying it

Without the entropy shock, SC training might at least maintain v55's strength. Whether it can improve beyond v55 is uncertain.

### 3. Fix the fixture pool (expected: +5-15 Elo if combined with #2)

The current 27-fixture pool is dysfunctional -- PFSP ignores 25 of them. Either:

**Option A**: Shrink to 5-6 hand-picked fixtures spanning a difficulty range:
  - heuristic (Elo 1763) -- easy, reliable positive signal
  - v14 (Elo 2015) -- medium
  - v22 (Elo 2088) -- medium-hard
  - v44 (Elo 2101) -- hard
  - v55 (Elo 2118) -- hardest
  
**Option B**: Reduce pfsp_exponent to 0.5-1.0 (more uniform sampling) so more fixtures get played.

**Option C**: Use round-robin fixture rotation instead of PFSP.

### 4. More iterations (expected: diminishing returns, low priority)

v72_sc ran 120 iters and peaked at iter60. Running 60-120 more iterations will NOT break the plateau -- it has already been tried. The issue is not iteration count but training signal quality.

Exception: if #2 (remove entropy shock) is applied, then 120-200 iterations may be worthwhile to allow the un-shocked policy time to improve.

### 5. Different starting checkpoint -- v55 itself (expected: neutral)

v72_sc already started from v55. Starting again from v55 without changing the entropy/fixture config will produce the same 2096 result. This has been empirically confirmed: v75_sc restarted from v72_sc best (which was derived from v55) and got 2096 again.

Starting from v55 is necessary but not sufficient. It must be combined with #2 (matching entropy config).

### 6. Architecture change (expected: uncertain, high risk)

The plateau is not caused by model capacity. v55 (same architecture) reached 2118. Architecture changes are a distraction from the real issue (training config).

## Whether to Continue SC Chain

**No. Stop the SC chain.**

The SC chain is solving a problem that does not exist. The stated goal of SC is to provide a "scripted curriculum" of diverse opponents. But:

1. The actual diversity is 2 fixtures (v55, v45) -- no curriculum exists
2. The entropy shock from the SC config degrades the starting checkpoint
3. The v44-v55 lineage proves that self-play alone reaches 2118 Elo
4. 150 SC iterations cannot undo 4233 iterations of self-play accumulation

The productive path is:
1. Stop v76_sc when it finishes (do not launch v77_sc)
2. Resume the v55 lineage: v56 from v55 ppo_best with v55's exact config
3. If v56 also plateaus at ~2118, THEN investigate whether fixtures or curriculum can help -- but from a position of strength, not weakness

## Open Questions

1. **Why was ent_coef=0.03 chosen for SC?** The prior analysis identified ent_coef=0.01 -> 0.003 as entropy starvation. The fix overcorrected to 0.03, which is appropriate for a fresh start (like v44 from v22) but destructive when applied to a specialized checkpoint (v55).

2. **Can v55's lineage continue to improve?** The v44-v55 chain showed ~2 Elo improvement per generation (v44=2101, v55=2118 over 12 generations). At this rate, v55+12 generations would reach ~2140. But diminishing returns are likely -- the noise floor of the eval system is ~12 Elo (CI width).

3. **Is the Elo ceiling a measurement artifact?** v55's 2118 is measured against a fixed anchor (v14=2015). If all models in the 2080-2120 range play 50/50 against each other, the Elo system may be compressing true skill differences. A different anchor or more games might reveal larger or smaller gaps.

4. **Would asymmetric training help?** All models are significantly stronger as USSR (elo_ussr >> elo_us for every model). Focused US-side training might be the biggest marginal improvement opportunity.

5. **Is there a fundamentally different approach needed to break 2120?** The self-play lineage may be approaching its ceiling with the current architecture, action space, and game representation. Breaking 2120 may require ISMCTS, better value estimation, or architectural improvements -- not training config changes.
