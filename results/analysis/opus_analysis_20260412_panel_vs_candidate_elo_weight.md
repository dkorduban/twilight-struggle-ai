---
# Opus Analysis: Panel Eval vs Candidate Pool, Elo-Weighted Scoring
Date: 2026-04-12T18:45:00Z
Question: The PPO training loop runs a "panel eval" every 10 iterations against a fixed set of opponents. This panel WR is used to select the best checkpoint (Option F: save ppo_running_best.pt on high-water mark). The post-training "candidate tournament" uses a 5-opponent pool (v55 + v14 + v54 + v44 + v45, no heuristic). The questions are: (1) Is the panel eval equivalent to the 5-opponent candidate pool? (2) How is the panel WR computed/weighted? (3) Can we weight opponents by Elo impact?
---

## Executive Summary

The panel eval and candidate pool are **not equivalent** -- they use different opponent sets and different scoring methods. The within-training panel eval uses 4 opponents {v8 (Elo 1915), v14 (Elo 2015), v22 (Elo 2096), heuristic (Elo 1751)} with a simple unweighted mean of combined WR. The "5-opponent candidate pool" mentioned in the question refers to the Elo placement fixture pool (`elo_fixture_pool.json`: v55, v14, v54, v44, v45), which is used for a separate Elo calibration step -- NOT for the confirmation tournament. The actual confirmation tournament (in `ppo_confirm_best.py`) uses the **same 4 opponents as the panel eval** (v8, v14, v22, heuristic), but scores via BayesElo round-robin rather than simple mean WR.

The current simple-mean scoring gives equal weight to heuristic (Elo 1751) and v22 (Elo 2096). This means a checkpoint that gains 5pp against heuristic but loses 5pp against v22 scores identically to one that does the opposite -- despite the latter being far more impressive. Elo-weighted scoring would fix this, giving approximately 3x more weight to v22 wins than to heuristic wins.

**Option F (ppo_running_best.pt on high-water mark) has NOT been implemented yet.** The analysis document recommending it exists (`opus_analysis_20260412_candidate_tournament_overlap.md`), but `train_ppo.py` contains no `running_best` or `high_water` logic. Currently, `ppo_confirm_best.py` is the only mechanism for selecting best checkpoints, and it runs post-training.

## Findings

### Panel eval opponents and Elo ratings

The panel eval is configured in `ppo_loop_step.sh` (lines 25-27) and passed to `train_ppo.py` via `--eval-panel`:

| Opponent | Variable | Elo (full ladder) | Elo gap vs anchor v14 |
|----------|----------|-------------------:|----------------------:|
| v8       | PANEL_WEAKEST  | 1915.5 | -99.5 |
| v14      | PANEL_MID      | 2015.0 | 0.0 (anchor) |
| v22      | PANEL_FRONTIER | 2096.0 | +80.9 |
| heuristic| (literal)      | 1750.7 | -264.3 |

The eval runs every 10 iterations (`--eval-every 10`), at "milestone" checkpoints. It plays 200 games per opponent (100 per side) in a background CPU process (`_panel_eval_worker`), producing per-opponent `combined_wr = (ussr_wins + us_wins) / total_games`.

### Candidate pool composition

There are actually **three** different opponent sets in the pipeline:

1. **Panel eval (within-training)**: {v8, v14, v22, heuristic} -- 4 opponents, simple WR
2. **Confirmation tournament (post-training, `ppo_confirm_best.py`)**: Same {v8, v14, v22, heuristic} -- passed as `--fixtures` in `ppo_loop_step.sh` lines 75-79. Scores via BayesElo round-robin among top-8 panel-eval checkpoints + these 4 fixtures.
3. **Elo fixture pool (separate calibration)**: {v55, v14, v54, v44, v45, v48, v22, v57, v20, ...} -- used in `elo_fixture_pool.json` for Elo placement of candidates against the broader ladder. This is NOT the confirmation tournament.

**Key finding**: The "5-opponent pool" in the question likely refers to the fixture pool in `elo_candidates_v65_v66sc.json`, which is a **separate Elo calibration step** for placing the winner on the full ladder. It does not feed back into checkpoint selection.

### Current WR aggregation method

In `ppo_confirm_best.py`, the `score_candidates()` function (lines 61-81):

```python
avg_wr = sum(v["combined_wr"] for v in valid.values()) / len(valid)
```

This is a **simple unweighted arithmetic mean** across all opponents with valid results. Each opponent contributes equally regardless of strength. So beating heuristic 90% counts the same as beating v22 90%.

The top-N candidates by `avg_wr` are then entered into a BayesElo round-robin tournament (using `run_elo_tournament.py`), and the **Elo winner** (not the WR leader) becomes `ppo_best.pt`. So the final selection IS Elo-based, but the **pre-screening** (which N checkpoints enter the tournament) uses unweighted mean WR.

In `train_ppo.py`, the panel eval results are logged to W&B as `panel/avg_combined_wr` (line 3253-3254) using the same unweighted mean. This is the metric that would drive a future `ppo_running_best.pt` high-water mark if Option F were implemented.

### Proposed Elo-weighted scoring

#### Problem with simple mean

Consider two checkpoints at iteration 20 and 40:

| Checkpoint | vs heuristic | vs v8 | vs v14 | vs v22 | Simple mean |
|------------|------------:|------:|-------:|-------:|------------:|
| iter_0020  | 0.88 | 0.72 | 0.62 | 0.52 | **0.685** |
| iter_0040  | 0.92 | 0.78 | 0.58 | 0.44 | **0.680** |

Simple mean says iter_0020 is marginally better. But iter_0020 is much stronger against the frontier (v22: 0.52 vs 0.44), which matters far more for actual Elo. The simple mean overweights easy opponents.

#### Weighting schemes

**Option 1: Linear Elo weights** -- `weight_i = Elo_i / sum(Elo_j)`

Produces: heuristic=0.225, v8=0.246, v14=0.259, v22=0.270. Too compressed -- only 1.2x difference between weakest and strongest.

**Option 2: Elo-gap exponential** -- `weight_i = exp(Elo_i / T)` where T is a temperature

With T=200 (reasonable for Elo scale):
- heuristic: exp(1751/200) = exp(8.75) = 6310
- v8: exp(1915/200) = exp(9.58) = 14,500
- v14: exp(2015/200) = exp(10.08) = 23,800
- v22: exp(2096/200) = exp(10.48) = 35,500

Normalized: heuristic=0.079, v8=0.181, v14=0.297, v22=0.443. This gives v22 about 5.6x the weight of heuristic.

**Option 3: Rank-based (simplest, recommended)** -- assign weights by strength rank:

| Rank | Opponent | Weight | Normalized |
|------|----------|-------:|----------:|
| 1 (strongest) | v22 | 4 | 0.40 |
| 2 | v14 | 3 | 0.30 |
| 3 | v8 | 2 | 0.20 |
| 4 (weakest) | heuristic | 1 | 0.10 |

This is simple, stable (doesn't change if Elo ratings shift by 10 points), and gives 4x weight to frontier vs heuristic. It also doesn't require loading elo_full_ladder.json at training time.

**Recommended: Option 3 (rank-based)** for the running_best high-water mark in train_ppo.py, with Option 2 (Elo exponential) available as a flag for ppo_confirm_best.py pre-screening.

### Risk assessment

#### Overfit to single opponent
If v22 gets 40% weight in the score, a checkpoint could win by overfitting to v22's specific weaknesses. Mitigation:
- The confirmation tournament uses BayesElo (not weighted WR) for final selection, so overfit checkpoints that lose to other opponents still get penalized.
- The panel eval uses 200 games/opponent (100/side), which limits variance. A 5pp WR fluke at n=200 is within 1 standard error.
- Having 4 opponents with non-zero weight prevents total single-opponent overfit.

#### Heuristic devaluation
Heuristic WR is actually a useful health check -- if it drops below ~80%, something is wrong with the model. With 10% weight, a heuristic collapse from 90% to 60% would only move the weighted score by 3pp, which might not trigger a high-water miss. Mitigation: add a separate floor check (`if heuristic_wr < 0.75: flag_regression()`) independent of the weighted score.

#### Perverse incentive: "give up on frontier"
A model that gives up on v22 entirely (0% WR) and maxes out against weak opponents would score: `0.10*0.95 + 0.20*0.85 + 0.30*0.70 + 0.40*0.00 = 0.475`. A balanced model scoring `0.10*0.88 + 0.20*0.72 + 0.30*0.62 + 0.40*0.52 = 0.626` easily wins. So the weighting doesn't create "give up on frontier" incentives -- it strengthens them.

## Conclusions

1. **Panel eval and candidate tournament use the SAME 4 opponents** (v8, v14, v22, heuristic). The "5-opponent pool" in the question refers to the separate Elo fixture pool, which is used only for ladder placement -- not checkpoint selection.

2. **Current scoring is simple unweighted mean WR.** This makes heuristic wins (trivially achievable) count as much as frontier wins (actually discriminating). The `ppo_confirm_best.py` final selection is BayesElo-based, but the pre-screening filter (top-N by avg WR) and any future running_best logic use unweighted mean.

3. **Elo-weighted scoring is straightforward and recommended.** Rank-based weights {v22: 0.40, v14: 0.30, v8: 0.20, heuristic: 0.10} give 4x more credit for frontier wins without requiring dynamic Elo lookups. Risk of single-opponent overfit is low with 4 opponents and 200 games each, and the confirmation tournament's BayesElo scoring provides a backstop.

4. **Option F (ppo_running_best.pt) is NOT yet implemented.** This is the prerequisite for Elo-weighted scoring to have any practical impact during training. Without it, the weighted score only affects `ppo_confirm_best.py`'s pre-screening of which checkpoints enter the confirmation tournament.

## Recommendations

### Priority 1: Implement Option F (ppo_running_best.pt high-water mark)

In `train_ppo.py`, after collecting panel eval results (~line 3253):

```python
# After computing avg_combined:
weighted_panel_wr = _compute_weighted_panel_wr(valid_opps, panel_weights)
if weighted_panel_wr > best_weighted_panel_wr:
    best_weighted_panel_wr = weighted_panel_wr
    shutil.copy2(current_ckpt, os.path.join(args.out_dir, "ppo_running_best.pt"))
    shutil.copy2(current_scripted, os.path.join(args.out_dir, "ppo_running_best_scripted.pt"))
```

Add `best_weighted_panel_wr = 0.0` at training init. About 15-20 lines total.

### Priority 2: Elo-weighted scoring in both places

**In `train_ppo.py`**: Use rank-based weights (hardcoded, since panel opponents are hardcoded):

```python
PANEL_WEIGHTS = {"heuristic": 0.10, "v8": 0.20, "v14": 0.30, "v22": 0.40}

def _compute_weighted_panel_wr(valid_opps: dict, weights: dict = PANEL_WEIGHTS) -> float:
    total_w = sum(weights.get(k, 0.25) for k in valid_opps)
    return sum(weights.get(k, 0.25) * v["combined_wr"] for k, v in valid_opps.items()) / total_w
```

**In `ppo_confirm_best.py`**: Replace the unweighted mean in `score_candidates()`:

```python
PANEL_WEIGHTS = {"heuristic": 0.10, "v8": 0.20, "v14": 0.30, "v22": 0.40}

def _weighted_wr(valid: dict) -> float:
    total_w = sum(PANEL_WEIGHTS.get(k, 0.25) for k in valid)
    return sum(PANEL_WEIGHTS.get(k, 0.25) * v["combined_wr"] for k, v in valid.items()) / total_w

# In score_candidates():
avg_wr = _weighted_wr(valid)  # replaces simple mean
```

### Priority 3: Add heuristic floor check

Independent of weighted scoring, flag any checkpoint where heuristic WR < 75% as a regression. This catches catastrophic failures that the weighted score might underweight.

### Priority 4: Consider upgrading panel opponents

The current panel is stale: v22 was frontier 40+ generations ago. v55 (Elo 2124) is now the top model. Consider upgrading to {heuristic, v14, v44, v55} to make the frontier opponent actually challenging. This would also make the panel more similar to the Elo fixture pool, reducing the gap between in-training and post-training evaluation.

## Open Questions

1. **Should the confirmation tournament also use Elo-weighted pre-screening?** Currently it takes top-8 by unweighted mean. With weighted scoring, the top-8 set could change. Given BayesElo final selection, this is low risk.

2. **Should panel weights be dynamic (loaded from elo_full_ladder.json)?** Only needed if panel opponents change frequently. Currently they're hardcoded as PANEL_WEAKEST/MID/FRONTIER in ppo_loop_step.sh, so hardcoded weights are fine.

3. **Should we upgrade the panel to include v55?** This would make the panel more discriminating for current-era checkpoints, but would break comparability with historical panel_eval_history.json data. Could add v55 as a 5th panel opponent without removing existing ones.

4. **Is the 200-game sample size per opponent sufficient for weighted scoring?** At n=200, WR standard error is ~sqrt(0.5*0.5/200) = 3.5pp. With 4x weight on v22, a 3.5pp error translates to 1.4pp in the weighted score vs 0.9pp unweighted. This is acceptable but not great -- consider increasing to 400 games for the frontier opponent specifically.
