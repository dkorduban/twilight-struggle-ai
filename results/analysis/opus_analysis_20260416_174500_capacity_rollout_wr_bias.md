# Opus Analysis: Capacity Test v4 Rollout WR Bias and Interpretability

Date: 2026-04-16T17:45:00Z

Question: The capacity test v4 trains side-specific PPO models (USSR-only, US-only) from the v56 baseline over 80 iterations against a panel pool (5 models + heuristic). The rollout win rate reported each iteration is partly vs earlier versions of self (via the league), so it may not be as strong a signal as direct panel evaluation. How should we interpret the results given confounds from self-play inflation, cosine LR decay, and lack of independent evaluation?

## Executive Summary

The capacity test v4 rollout WR is **moderately inflated** by self-play but less than feared: cumulative opponent composition was ~68% self/self-copies vs ~32% panel fixtures, and self-copy WR (64.0%) is about 14 percentage points higher than panel-fixture WR (50.3%), meaning the reported ~65% rollout WR overstates true panel performance by roughly 4-5 percentage points. However, the more critical problem is the **cosine LR schedule freezing the model by iteration 50-60**: clip fraction collapsed from 0.20 to 0.01, KL from 0.007 to 0.0003, and inter-checkpoint JSD from 0.008 to 0.0008, meaning the last 20-30 iterations produced negligible policy change. The experiment is therefore **inconclusive on the capacity question** -- it shows the USSR-only model found *some* improvement over v56 as USSR (panel WR ~50% vs the fixtures, up from what was likely a lower baseline), but the premature LR death and absence of any independent Elo evaluation make it impossible to confidently attribute gains to freed capacity vs simply more USSR-focused training.

## Findings

### 1. Opponent Composition and Self-Play Inflation

Each iteration uses 3 opponent slots: 1 dedicated self-play slot + 2 from the PFSP-weighted pool.

**Pool composition across 80 iterations:**
- Pool slots with self-copies: 83/160 (52%)
- Pool slots with panel fixtures: 77/160 (48%)
- Including the dedicated self slot: 163/240 total slots (68%) are self or self-copies, 77/240 (32%) are panel fixtures

The PFSP table at iteration 80 gives cumulative WR against each opponent (model playing as USSR):

| Opponent | Type | WR | Games |
|----------|------|-----|-------|
| heuristic | panel fixture | 0.319 | 1782 |
| v20_scripted | panel fixture | 0.582 | 462 |
| v44_scripted | panel fixture | 0.595 | 660 |
| v54_scripted | panel fixture | 0.609 | 792 |
| v55_scripted | panel fixture | 0.632 | 462 |
| v56_scripted | panel fixture | 0.598 | 924 |
| iter_0001 | self-copy | 0.635 | 1782 |
| iter_0010 | self-copy | 0.664 | 660 |
| iter_0020 | self-copy | 0.644 | 1254 |
| iter_0030 | self-copy | 0.620 | 726 |
| iter_0040 | self-copy | 0.640 | 528 |
| iter_0050 | self-copy | 0.652 | 132 |
| iter_0060 | self-copy | 0.742 | 66 |
| iter_0070 | self-copy | 0.621 | 264 |
| iter_0080 | self-copy | 0.652 | 66 |

**Key insight**: The heuristic WR of 0.319 (model only wins 32% as USSR vs heuristic playing US) reflects the well-known TS asymmetry -- USSR is the disadvantaged side. The model beats panel models at 58-63% because those models are weaker than heuristic on US side (Elo: heuristic=1500, v56=1170, v44=1212).

**Weighted averages:**
- Panel-fixture WR: 0.503 (5082 games)
- Self-copy WR: 0.640 (5478 games)
- Gap: self-copy WR is 13.7 percentage points higher

**Inflation estimate**: With ~68% self-play and ~32% panel:
- Estimated blended WR: 0.68 * 0.640 + 0.32 * 0.503 = 0.596
- Reported average rollout WR: 0.647
- The reported WR is ~5 percentage points above the blended estimate, with variation from per-iteration sampling

### 2. Cosine LR Schedule: Premature Learning Death

The cosine schedule decays LR from 5e-5 to 5e-6 over 80 iterations:

| Iteration | LR | LR Multiplier |
|-----------|-----|---------------|
| 1 | 5.00e-5 | 1.000x |
| 20 | 4.39e-5 | 0.878x |
| 40 | 2.79e-5 | 0.559x |
| 60 | 1.17e-5 | 0.235x |
| 70 | 6.76e-6 | 0.135x |
| 80 | 5.00e-6 | 0.100x |

**Evidence of frozen policy from diagnostics:**

| Metric | Iter 1-20 avg | Iter 21-40 avg | Iter 41-60 avg | Iter 61-80 avg |
|--------|---------------|----------------|----------------|----------------|
| Clip fraction | 0.20 | 0.20 | 0.13 | 0.04 |
| KL divergence | 0.007 | 0.007 | 0.004 | 0.001 |
| Entropy | 3.65 | 3.68 | 3.60 | 3.45 |

**JSD between consecutive checkpoints:**
- Iter 10->20: 0.0078
- Iter 20->30: 0.0064
- Iter 30->40: 0.0062
- Iter 40->50: 0.0036
- Iter 50->60: 0.0027
- Iter 60->70: 0.0017
- Iter 70->80: 0.0008

By iteration 60, the policy is changing at 1/3 the rate of iteration 20. By iteration 80, it is changing at 1/10 the rate. The clip fraction of 0.005-0.013 in the final iterations means the PPO clipping mechanism is essentially inactive -- updates are too small to clip.

**Despite this, rollout WR did NOT collapse.** Phase averages:
- Iter 1-20: 0.598
- Iter 21-40: 0.664
- Iter 41-60: 0.660
- Iter 61-80: 0.666

The improvement from iter 1-20 (0.598) to iter 21-40 (0.664) is genuine learning. The plateau from iter 21-80 reflects a frozen policy that happens to be better than baseline, not continued improvement.

### 3. The Capacity Question: What Can We Actually Conclude?

The experiment was designed to test: "Does the shared (both-sides) model architecture limit per-side performance? Would a side-specific model reach higher strength?"

**What the data shows:**
- USSR-only model achieved ~50% panel-fixture WR as USSR, with the heuristic being hardest (32% WR) and older models easiest (58-63%)
- The v56 baseline was Elo 1170 vs heuristic=1500 in the full Elo ladder, corresponding to ~12.8% overall WR against heuristic
- The USSR-only model's 32% WR vs heuristic as USSR is hard to compare directly to v56's 12.8% overall WR (which includes both sides)

**What the data does NOT show:**
- No independent Elo evaluation exists -- all 4 confirm attempts failed with FileNotFoundError
- No comparison to v56's USSR-specific panel WR (v56 was never benchmarked in USSR-only mode)
- No way to tell if the ~65% rollout WR represents genuine improvement over v56 or just more USSR-focused training that any model would achieve
- The LR freeze after iter 40-50 means we only saw ~40 iterations of real learning, not 80

### 4. Confound Analysis

| Confound | Severity | Impact |
|----------|----------|--------|
| Self-play inflation | Moderate | ~5pp inflation on reported WR; panel-only WR is ~50% not ~65% |
| Cosine LR death | Severe | Last 30+ iterations wasted; effective experiment was only ~50 iterations |
| No independent eval | Critical | Cannot quantify actual strength gain vs v56 baseline |
| Missing baseline comparison | High | v56 was never benchmarked as USSR-only, so no before/after delta |
| Small sample per opponent | Moderate | Only 66-462 games per panel fixture; high variance on individual WR estimates |
| PFSP selection bias | Low | Weaker opponents get sampled more (by design), but with pfsp_exponent=0.5 the effect is mild |

### 5. US-Only Run (In Progress)

US-only has completed 14/80 iterations with rollout WR averaging ~0.47. This is notably lower than the USSR-only early performance (~0.58), which is counter-intuitive given TS is US-favored. However, the US model is playing against panel opponents who are playing as USSR (the easier side for opponents), plus the heuristic as USSR. Early US results are too noisy to draw conclusions yet.

## Conclusions

1. **The reported ~65-68% rollout WR for USSR-only is inflated by approximately 4-5 percentage points** due to the self-play component. The actual weighted panel-fixture WR is approximately 50%, heavily dragged down by the heuristic matchup (32% WR as USSR vs heuristic as US).

2. **The cosine LR schedule rendered iterations 50-80 essentially useless for learning.** Clip fraction dropped below 0.05, KL below 0.002, and inter-checkpoint JSD to 0.0008. The model was frozen in place for the final 30+ iterations. The effective experiment duration was ~40-50 iterations, not 80.

3. **The experiment is inconclusive on the capacity question** because (a) there is no independent Elo evaluation of the trained checkpoints (all 4 confirm attempts failed), (b) there is no USSR-specific panel WR for the v56 baseline to compare against, and (c) the self-play inflation makes rollout WR unreliable as a strength signal.

4. **The self-copy WR of 64% is expected and informative in one way**: it shows the model is meaningfully improving over its earlier snapshots, which confirms learning is happening. But it does not tell us whether the final model is stronger than v56 as USSR.

5. **The 32% WR vs heuristic as USSR is a hard signal** -- it is uncontaminated by self-play and comes from 1782 games (reasonably large sample). If v56's USSR-specific WR vs heuristic was lower than 32%, then the capacity test showed genuine side-specific improvement. But we do not have that baseline number.

6. **The experiment's value is primarily as a proof-of-concept** for the side-specific training infrastructure, not as evidence for or against capacity constraints.

## Recommendations

1. **Run a direct panel benchmark of the USSR-only checkpoint** using the standard 2000-game benchmark script, measuring USSR-specific WR against heuristic and the panel. Also benchmark v56 in USSR-only mode to get the before/after delta. This is the single most important follow-up.

2. **Fix the Elo confirm pipeline** -- all 4 attempts failed with a FileNotFoundError on `data/checkpoints/scripted_for_elo/ussr_only_v4_scripted.pt`. The confirm hook is looking for a pre-exported scripted model that does not exist. The export step is failing before the tournament runs.

3. **If repeating the experiment, use a constant LR or a much gentler schedule.** The cosine decay to 10% over 80 iterations is far too aggressive. Consider: (a) constant LR with max-KL early stopping, or (b) cosine decay to 50% instead of 10%, or (c) a longer horizon (300+ iterations) so the decay is gradual.

4. **Reduce self-play proportion for capacity experiments.** For future capacity tests, consider `--league-self-slot false` to eliminate the dedicated self-play slot, or use `--league-fixture-fadeout 999` with more fixtures and fewer self-play snapshots. Alternatively, log panel-only WR separately from self-play WR.

5. **Add per-opponent WR reporting to the training loop.** Currently, rollout_wr is a single blended number. Adding `rollout_wr_vs_panel` and `rollout_wr_vs_self` as separate logged metrics would make future experiments much easier to interpret.

6. **Defer conclusions about capacity until the US-only run completes and both are properly benchmarked.** The US-only data (14 iters, ~47% WR) is too early to interpret, but will be equally important for the capacity question.

## Open Questions

1. What is v56's USSR-specific WR against heuristic? This single number would make the capacity experiment interpretable.
2. Why did the Elo confirm pipeline fail on all 4 attempts? Is it a path issue or a model format issue?
3. Is the 32% USSR vs heuristic WR actually good or bad? For context, what does the main PPO chain's best model (Elo 1833) achieve as USSR vs heuristic?
4. Would a longer experiment (200+ iterations) with constant LR show continued improvement, suggesting the capacity ceiling was not reached?
5. The entropy dropped from ~3.65 to ~3.45 -- is this reflecting policy sharpening (good) or premature collapse toward a suboptimal mode? The JSD data suggests the former (gradual convergence, not sudden collapse).
