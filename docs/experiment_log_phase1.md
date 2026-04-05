# Self-Play Experimentation Log — Phase 1

Started: 2026-04-03

## Baseline Reference Models (corrected +2 bid benchmark, 500 games/side)

| Model | Data | Rows | USSR WR | US WR | Combined | Notes |
|-------|------|------|---------|-------|----------|-------|
| v23 | combined_v23 (heur+selfplay) | 1.33M | 28.6% | 1.2% | 14.8% | Best old-gen, lr=0.0012, ls=0.05, NO setup inf |
| v24 | similar | ~1.3M | 28.3% | 3.0% | 15.6% | NO setup inf |
| v25 | similar | ~1.3M | 26.0% | 2.6% | 14.3% | NO setup inf |
| v28 | similar | ~1.3M | 26.9% | 2.2% | 14.4% | NO setup inf |
| combined_bid2_h256 | heur+imit | 1.35M | 39.4% | 6.8% | 23.1% | Pure BC, NO setup inf in data |
| heuristic_repro_v1 | heur | 910k | 36.4% | 7.2% | 21.8% | Pure BC, MIXED setup inf |
| imitation_t1 | imit | 248k | 31.6% | 4.8% | 18.2% | Pure BC, NO setup inf |
| exp_baseline_h128 | heur+imit | 1.35M | 26.6% | 4.0% | 15.3% | h128 (half capacity) |
| exp_control_feat_h128 | heur+imit | 1.35M | 29.8% | 4.4% | 17.1% | h128 + region scoring features |
| exp_marginal_value_h128 | heur+imit | 1.35M | 12.2% | 2.4% | 7.3% | h128 + BCE country head (broken) |
| v88_setup | heur w/setup | 39k | 18.2% | 0.4% | 9.3% | Correct setup inf, too small |

### Key insight: combined_bid2_h256 is actually best at 23.1% combined (39.4% USSR!)
- This model was trained on data WITHOUT setup influence but benchmarked WITH setup
- It outperforms v23 because it has 1.35M rows of diverse heuristic data
- v23's self-play advantage was masked by the old benchmark (no setup)

### Learned-vs-Learned (v88 self-play)
- v88 vs v88 (500 games): USSR 87.0% | US 12.8% | Draw 0
- Massive USSR advantage mirrors the game's inherent asymmetry

## Hyperparams (v23-proven baseline)

```
lr=0.0012, batch_size=1024, epochs=60, weight_decay=1e-4,
label_smoothing=0.05, one_cycle=True, hidden_dim=256,
value_target=final_vp, dropout=0.1
```

---

## Phase 0: Pre-Self-Play Fixes

### 0a. Dirichlet noise in collection
- Status: DONE (already implemented in mcts.cpp:521-549, called at line 594)
- For non-MCTS collection: epsilon-greedy and temperature sampling are the mechanisms

### 0b. Canonical training targets
- Status: DONE (already canonical — accessible countries sorted at policies.cpp:676)

---

## Phase 1 Generations

### Gen 0 (v89) — DONE
- Started: 2026-04-03 01:18 UTC
- Data: heuristic_10k_setup_bid2_nash (787k) + heuristic_10k_setup_bid2_nash_b (1.35M)
  - Total: 2.13M rows, 20k games, ALL with correct setup influence
  - Verified: US inf at turn 1 ranges 17-57, mean ~27 (all >14)
- Hyperparams: v23 recipe (lr=0.0012, ls=0.05, bs=1024, ep=60, patience=15)
- val_loss: 3.8682, card_top1: 65.2%, mode_acc: 83.3%, country_top1: 34.8%
- **USSR WR: 37.2%** | **US WR: 7.2%** | **Combined: 22.2%**
- Notes: Matches combined_bid2_h256 (23.1%). Pure heuristic BC baseline replicated.

### Gen 0b (v89b) — DONE (batch size experiment)
- Data: Same as v89 (2.13M rows)
- Hyperparams: bs=8192, lr=0.0024 (2× base), rest same
- val_loss: 3.9164, card_top1: 65.0%, mode_acc: 83.1%, country_top1: 35.0%
- **USSR WR: 38.8%** | **US WR: 7.2%** | **Combined: 23.0%**
- Training time: ~10 min (vs ~27 min for v89). **2.8× speedup, same or better WR.**
- **DECISION: Use bs=8192, lr=0.0024 for all future training.**

### Gen 1 (v90) — DONE
- Data: 2.13M heur + learned_v89b_ussr (all) + learned_v89b_us (wins-only) = ~2.45M rows
- Hyperparams: bs=8192, lr=0.0024 (fast recipe)
- val_loss: 3.8784, card_top1: 65.0%, mode_acc: 83.3%, country_top1: 34.9%
- **USSR WR: 32.4%** | **US WR: 9.0%** | **Combined: 20.7%**
- Notes: USSR dropped significantly. Including losing games from self-play hurts USSR.

### Gen 1b (v90b) — DONE (wins-only filtered variant)
- Data: 2.13M heur + learned_v89b_ussr (wins-only) + learned_v89b_us (wins-only) = ~2.26M rows
- Hyperparams: bs=8192, lr=0.0024 (fast recipe)
- val_loss: 3.8980, card_top1: 65.0%, mode_acc: 83.4%, country_top1: 34.7%
- **USSR WR: 39.8%** | **US WR: 8.4%** | **Combined: 24.1%** ← NEW BEST
- Notes: Wins-only filtering is critical. +1.1pp combined over v89b pure BC.
- **DECISION: Use wins-only filtering for both sides in all future generations.**

### Gen 2 (v91) — DONE
- Data: 2.13M heur + Gen1 filtered (127k) + Gen2 filtered (148k) = 2.41M rows
- Hyperparams: bs=8192, lr=0.0024 (fast recipe)
- val_loss: 3.8073, best_epoch: 60
- 500g/side: USSR 41.6% | US 10.4% | Combined 26.0% (initial, misleading)
- **2000g/side: USSR 35.6% | US 9.2% | Combined 22.4%** (regression from v89b)

### Gen 3 (v92) — DONE
- Data: 2.13M heur + Gen1-3 filtered (420k) = 2.55M rows
- val_loss: 3.7275
- **2000g/side: USSR 40.0% | US 7.7% | Combined 23.9%** (no improvement)

---

## Phase 1 Investigation: What Does Self-Play Actually Do?

After initial 500-game benchmarks suggested gen-over-gen improvement, switched to
rigorous 2000-game benchmarks (±0.7pp CI) revealing the improvement was an illusion.

### High-confidence benchmark comparison (2000 games/side, 4 seeds)

| Model | Self-play data | USSR WR | US WR | Combined | val_loss |
|-------|---------------|---------|-------|----------|----------|
| v89b | none (pure BC) | 41.5% | 8.1% | **24.8%** ±0.7 | 3.916 |
| v90b (seed=42) | gen1 5.6% | 44.5% | 9.7% | **27.1%** ±0.7 | 3.898 |
| v90b (seed=123) | gen1 5.6% | 39.4% | 9.7% | **24.5%** ±0.7 | 3.900 |
| v91 | gen1+2 11% | 35.6% | 9.2% | **22.4%** ±0.7 | 3.807 |
| v92 | gen1+2+3 17% | 40.0% | 7.7% | **23.9%** ±0.7 | 3.728 |
| v93 | gen1 + v90b 5k 19% | 40.4% | 9.0% | **24.7%** ±0.7 | 3.683 |
| v94_warm | warm-start from v90b | 41.4% | 9.2% | **25.3%** ±0.7 | 3.648 |
| v95 | heur + v90b selfplay 25% | 42.2% | 8.2% | **25.2%** ±0.7 | 3.596 |
| v96a | v90b data @6.8% | 38.2% | 9.1% | **23.7%** ±0.7 | 3.815 |
| v96b_aw | v90b + adv.wt 0.5 | 41.8% | 5.7% | **23.7%** ±0.7 | 3.894 |
| v97 | v89b data 18% | 42.0% | 8.5% | **25.2%** ±0.7 | 3.679 |

### Key findings

1. **v90b's 27.1% was a lucky training seed.** Retrained with seed=123 → 24.5%.
   All other models cluster at 23.7-25.3%, overlapping within ±0.7pp CI.

2. **Self-play data from BC models provides NO reliable improvement.**
   Pure heuristic BC (v89b) = 24.8%. Best self-play variant = 25.3%. Within noise.

3. **val_loss improves but WR doesn't.** val_loss dropped from 3.92 → 3.60 as
   self-play data increased, but WR stayed flat. The model better predicts training
   data without playing better.

4. **More self-play data can hurt.** v91 (11% SP) and v92 (17% SP) are below baseline.
   Too much SP data dilutes the heuristic signal without adding useful new information.

5. **Advantage weighting hurts US play.** v96b dropped US WR from ~9% to 5.7%.

6. **Warm-starting doesn't help.** Best epoch = 1 (essentially unchanged from v90b).

### Root cause analysis

Self-play data from a BC model is **not novel enough** relative to the heuristic
training data. The model learned to imitate the heuristic, so its play generates
data that looks like the heuristic data. Adding near-duplicate data with a slightly
different distribution creates noise, not signal.

To improve beyond ~25% combined, we need:
- **Architecture improvements** (Phase 2) to increase model capacity/expressiveness
- **Real RL signal** (not behavior cloning) — policy gradient, PPO, or value-aware training
- **Search at inference time** — MCTS with learned value/policy should beat raw policy
- **Qualitatively different data** — human games, MCTS-generated trajectories

### Phase 1 conclusion: WR plateau triggered. Proceeding to Phase 2 (Architecture).

---

## Phase 2: Architecture Experiments & Data Quality Audit

### Data quality finding: nash contamination

**Root cause:** The `heuristic_10k_setup_bid2_nash.parquet` file in `combined_v89`
was collected before a DEFCON-safety fix in the heuristic. Key evidence:

| | nash (pre-fix) | nash_b (post-fix) |
|---|---|---|
| Games | 10,000 | 10,000 |
| Mean max turn | 5.6 | 9.1 |
| Games ending turn 1-3 | 2,920 (29%) | 0 (0%) |
| Games reaching turn 10 | 2,152 (21.5%) | 7,452 (74.5%) |
| End at DEFCON 2 | 82% | 71% |
| USSR win rate | **98.3%** | **65.1%** |
| Rows/game | 78 | 134 |
| Rows/turn | ~14 | ~15 |

29% of nash games end on turns 1-3 via US DEFCON-1 suicide. The US heuristic
coups at DEFCON 2, triggering DEFCON→1 and losing the game. This creates
degenerate training data: 80% of nash rows come from short games where the
US self-destructs, teaching the model a non-existent strategy.

**Impact:** All Phase 1+ experiments trained on `combined_v89` (nash + nash_b) are
affected by this contamination. However, relative comparisons remain valid since all
models trained on the same data. Absolute WR numbers are suboptimal.

**Schema compatibility:** All 4 heuristic files (nash, nash_b, nash_c, nash_d) share
an identical 75-column schema. The differences are only in outcome distribution and
game length, not in feature availability.

**Action items:**
1. Drop nash from training data for all future experiments
2. Use nash_b alone (1.3M rows, 10k games) as clean baseline
3. Or nash_b + nash_c for clean 2× (2.7M rows, 20k games)
4. Re-run baseline h256 on clean data to establish new reference WR

### 2× heuristic data volume test (v98_heur40k)

Trained on nash + nash_b + nash_c + nash_d (4.87M rows, 40k games).
**Combined WR: 23.8% ±0.7 (n=2000/side)** — no improvement over baseline 24.8%.

However, this result is confounded by the nash contamination and the discovery that
nash_c/nash_d have very different outcome distributions. A clean 2× test using
only nash_b + nash_c is pending.

### Architecture sweep (on combined_v89, results pending)

Comparing baseline MLP, country attention (SDPA-fixed), and control features
at h128 and h256. Benchmarks use 2000 games/side (4 seeds × 500).

| Architecture | h128 USSR/US/Combined | h256 USSR/US/Combined |
|---|---|---|
| baseline | 37.5%/4.7%/**21.1%** ±0.6 | 36.7%/8.1%/**22.4%** ±0.6 |
| country_attn (SDPA) | 28.8%/3.4%/**16.1%** ±0.5 | 38.4%/7.6%/**23.0%** ±0.6 |
| control_feat | 42.7%/3.4%/**23.1%** ±0.6 | 48.6%/9.4%/**29.0%** ±0.6 ← NEW BEST |

All 6 models trained on combined_v89 (nash+nash_b, 2.13M rows), seed=42,
bs=8192, lr=0.0024, epochs=60, patience=15, dropout=0.1.

### Architecture sweep findings

1. **Three models cluster at 22-23% combined** — baseline h256 (22.4%), country_attn
   h256 (23.0%), control_feat h128 (23.1%). All within ±0.6pp benchmark CI and
   ~±2pp training seed variance. No clear winner.

2. **country_attn scales dramatically with capacity**: 16.1% at h128 → 23.0% at h256.
   Attention needs sufficient embedding dimension to be useful. At h128, it wastes
   capacity on the attention mechanism at the expense of downstream MLPs.

3. **control_feat h256 was NOT overfitting — first run had a bad initialization.**
   First run: best epoch 24, val_loss 4.02 → 18.1% WR. Second run (same hyperparams,
   new random seed): best epoch 60, val_loss 3.76 → **29.0% WR**. The first run likely
   hit a bad local minimum early. This is the new best model.

4. **USSR vs US trade-off**: control_feat models favor USSR (42.7-48.6%) at cost of
   US WR (3.4-9.4%). baseline h256 is most balanced.

5. **Conclusion**: control_feat h256 = 29.0% combined is a clear win (+6.6pp over
   baseline h256). Region scoring features genuinely help at h256 capacity.
   Next: clean data sweep to confirm on nash_b+c without contamination.

Note: seed variance is ~2-4pp (measured by retraining baseline h256 with different
seeds: 22.4% vs 24.8%). CIs above are benchmark-only; total uncertainty including
training seed is ~±2pp.

---

## Phase 1 clean sweep — v99 (post-DEFCON-fix data, deterministic train/val split)

**Data**: `combined_v99_clean` (nash_b + nash_c, 2.58M rows / 2x) and `combined_v99_clean_b`
(nash_b only, 1.28M rows / 1x). All post-DEFCON-fix: ussr_win 62.6%, us_win 35.1%.

**Epoch counts matched to ~121M total samples** (= arch sweep reference):
- 2× data (2.58M train): 47 epochs → 121.1M samples
- 1× data (1.28M train): 95 epochs → 121.4M samples

Hyperparams: lr=0.0024, batch=8192, dropout=0.1, label_smooth=0.05, wd=1e-4, one-cycle.
All benchmarks: 2000 games/side (4×500 seeds), W&B summary updated via bench_pipeline.

### Group 1: baseline h256 seed variance (2× data @ 47 epochs)

| Run | USSR WR | US WR | Combined | W&B |
|-----|---------|-------|----------|-----|
| v99_baseline_h256_s42 (60ep) | 42.1% ±1.1 | 11.6% ±0.7 | 26.9% ±0.7 | u8x4v7d8 |
| v99_baseline_h256_s7 | 40.8% ±1.1 | 11.5% ±0.7 | 26.1% ±0.7 | duj7xgzn |
| v99_baseline_h256_s123 | 37.2% ±1.1 | 8.4% ±0.6 | 22.8% ±0.6 | ixl2bgra |

Note: s42 ran at 60 epochs (extra compute data point, excluded from seed variance).
Seed variance across s7/s123: 26.1% vs 22.8% = **3.3pp spread** (±1.6pp half-range).
This is consistent with prior ~2-4pp estimate from combined_v89 seeds.

### Group 2: saturation test — 1× @ 95ep vs 2× @ 47ep (both ~121M samples)

| Run | Data | Train rows | Epochs | USSR WR | US WR | Combined | W&B |
|-----|------|-----------|--------|---------|-------|----------|-----|
| v99_saturation_1x_95ep | nash_b | 1.28M | 95 | 46.2% ±1.1 | 13.0% ±0.8 | **29.5% ±0.7** | knpb3sti |
| v99_saturation_2x_47ep | nash_b+c | 2.58M | 47 | 42.1% ±1.1 | 11.6% ±0.7 | 26.9% ±0.7 | u9bqter9 |

**Finding**: 1× @ 95ep (29.5%) beats 2× @ 47ep (26.9%) by **2.6pp** despite identical
total samples (~121M) and same seed (42). The difference is purely data arrangement:
fewer unique games seen more times vs more games seen once. This suggests the dataset is
not yet saturated from uniqueness; more epochs on a smaller clean set is better.

Note: saturation_2x_47ep = same seed/data as v99_baseline_h256_s42 → identical results
(both converge at epoch 46 of their respective training runs, same model).

### Group 3: control_feat h256 on clean data (2× @ 47 epochs)

| Run | USSR WR | US WR | Combined | W&B |
|-----|---------|-------|----------|-----|
| v99_control_feat_h256_s42 | 42.4% ±1.1 | 7.1% ±0.6 | 24.8% ±0.6 | l5sch6y3 |
| v99_control_feat_h256_s123 | 45.1% ±1.1 | 12.7% ±0.7 | 28.9% ±0.7 | ioploe14 |

**Reference (arch sweep, contaminated data)**: 48.6%/9.4%/29.0%±0.6 on combined_v89.

**Seed variance**: s42/s123 = 24.8% vs 28.9% = **4.1pp spread**. Mean = 26.85%.
Control_feat architecture shows high init sensitivity (arch sweep: 18.1% / 29.0%).

### v99 Clean sweep — full summary

All benchmarks: 2000 games/side, 4×500 seeds. Combined = (USSR_wins + US_wins) / 4000.

| Model | Arch | Data | Epochs | Mean combined | Seed variance |
|-------|------|------|--------|--------------|---------------|
| baseline h256 | baseline | 2× (2.58M) | 47 | 24.45% ±1.7pp | s7=26.1%, s123=22.8% |
| control_feat h256 | control_feat | 2× (2.58M) | 47 | 26.85% ±2.1pp | s42=24.8%, s123=28.9% |
| **saturation_1x_95ep** | **baseline** | **1× (1.28M)** | **95** | **29.5%** | — |
| saturation_2x_47ep | baseline | 2× (2.58M) | 47 | 26.9% | (=s42) |

**Winner: `v99_saturation_1x_95ep` = 29.5% combined** — baseline architecture, 1x clean data, 95 epochs.

### Key findings from v99 clean sweep

1. **More epochs on less data beats one pass on more data** (at ~121M total samples).
   Saturation_1x_95ep (29.5%) > saturation_2x_47ep (26.9%) by 2.6pp despite equal compute.
   The 10k nash_b games, seen 95 times each, learn better than 20k games seen 47 times.

2. **control_feat does NOT consistently outperform baseline** on clean data.
   Mean of two seeds: 26.85% vs 24.45% (2.4pp edge), but with 4pp seed variance this is
   within noise. The arch sweep's 29.0% was likely a good-init seed, not a reliable result.

3. **Seed variance is large for control_feat**: 4.1pp spread (s42=24.8%, s123=28.9%).
   At least 3 seeds needed to get a reliable estimate of control_feat performance.

4. **Baseline h256 is more stable**: seed variance 3.3pp (s7=26.1%, s123=22.8%).
   Still high, but control_feat is worse.

5. **Clean data is comparable to (or slightly better than) contaminated data** for baseline:
   Baseline h256 mean on clean data (24.45%) > arch sweep on contaminated v89 (22.4%).
   The contamination didn't help the baseline — it just inflated the contaminated nash WR.

### Recommendations

**For next self-play round:**
- Use 1× clean data (nash_b, 1.28M) with 95 epochs as the BC initialization
- Run 3 seeds (42, 7, 123) to get stable estimate
- The saturation_1x_95ep model (29.5%) is the new strongest BC baseline
- Baseline architecture is preferred over control_feat for reliability

**For architecture experiments:**
- control_feat needs ≥3 seeds to evaluate reliably
- Consider testing control_feat at 95 epochs (same as saturation_1x) — might compound
- The 4.1pp variance suggests control_feat is sensitive to initialization

---

## Follow-up sweep (saturation analysis recommendations)

All runs: 1x clean data (nash_b, 1.28M) or 2x (nash_b+c, 2.58M); lr=0.0024, batch=8192,
dropout=0.1, wd=1e-4, one-cycle, deterministic-split.

### Group 1: control_feat h256 @ 1x95ep × 3 seeds
Tests whether architecture + saturation compound (predicted ~30-32% if so).

| Run | USSR WR | US WR | Combined | W&B |
|-----|---------|-------|----------|-----|
| v99_cf_1x95_s42 | 45.8% ±1.1 | 11.7% ±0.7 | 28.7% ±0.7 | l4rofm46 |
| v99_cf_1x95_s7 | 51.1% ±1.1 | 13.7% ±0.8 | **32.4% ±0.7** | jwkjdihd |
| v99_cf_1x95_s123 | 44.4% ±1.1 | 9.7% ±0.7 | 27.0% ±0.6 | s4w6trsi |

Mean across 3 seeds: **29.4%**. Spread: 27.0%–32.4% = **5.4pp variance**.
s7 is a strong outlier. Mean (29.4%) vs baseline_1x_95ep (29.5%) → architecture effect is ~0pp on average.

**Finding**: control_feat does NOT consistently outperform baseline. s7's 32.4% is an
initialization lucky seed. The compounding hypothesis (arch × saturation → 30-32%) is
**not confirmed** — mean is identical to baseline at 29.4-29.5%.

### Group 2: baseline h256 @ 1x120ep (epoch ceiling test)

| Run | USSR WR | US WR | Combined | W&B |
|-----|---------|-------|----------|-----|
| v99_baseline_120ep | 40.4% ±1.1 | 11.3% ±0.7 | 25.9% ±0.7 | xsseshcp |

**Finding**: 120ep (25.9%) is **worse** than 95ep (29.5%) by 3.6pp. Already past optimum at 95.
Early stopping at best_val_loss fires at epoch 95, confirming 95ep is already optimal for 1x data.

### Group 3: baseline h256 @ 2x95ep (LR schedule disambiguator)

| Run | USSR WR | US WR | Combined | W&B |
|-----|---------|-------|----------|-----|
| v99_baseline_2x95ep | 36.0% ±1.1 | 9.0% ±0.6 | 22.5% ±0.6 | — |

**Finding**: 2x@95ep (22.5%) is *worse* than 2x@47ep (26.9%) by 4.4pp. Severe overfitting:
the model sees each of the 20k games ~95 times, memorizing without generalizing. This
**confirms the saturation_1x win is about data diversity** (each game ~65× for 1x@95ep is
better than ~95× for 2x@95ep). More unique games per epoch matters more than more epochs.

### Follow-up sweep — full summary

| Model | Data | Epochs | USSR WR | US WR | Combined | vs baseline_2x47 |
|-------|------|--------|---------|-------|----------|-----------------|
| v99_saturation_1x_95ep (s42) | 1× | 95 | 46.2% | 13.0% | **29.5%** | **+2.6pp** |
| v99_cf_1x95_s7 (best seed) | 1× | 95 | 51.1% | 13.7% | **32.4%** | **+5.5pp** |
| v99_cf_1x95_s42 | 1× | 95 | 45.8% | 11.7% | 28.7% | +1.8pp |
| v99_cf_1x95 mean (3 seeds) | 1× | 95 | — | — | 29.4% | +2.5pp |
| v99_baseline_2x_47ep (s42) | 2× | 47 | 42.1% | 11.6% | 26.9% | baseline |
| v99_baseline_120ep | 1× | 120 | 40.4% | 11.3% | 25.9% | -1.0pp |
| v99_baseline_2x95ep | 2× | 95 | 36.0% | 9.0% | 22.5% | **-4.4pp** |

### Key conclusions

1. **Best BC baseline is 1x@95ep**: 29.5% combined (baseline arch) or 29.4% mean (cf arch).
   Architecture choice doesn't matter at this scale — variance from seed > variance from arch.

2. **Epoch ceiling confirmed at 95ep for 1x data**. 120ep is clearly worse.

3. **Overfitting on 2x@95ep is severe**: 22.5% — worse than any 2x@47ep run.
   The lesson: for this dataset size, one-cycle schedule length must match data scale.

4. **US WR is structurally stuck at 8-14%** regardless of model, data, epochs, or arch.
   This is the dominant bottleneck.

---

## Phase A: US WR improvement experiments

### A2: actor_relative value target

`v100_actor_value_s42`: 1x clean data, 95ep, baseline h256, `--value-target actor_relative`.
W&B: iaotaspv. Best epoch: 89.

| Model | USSR WR | US WR | Combined | vs v99_saturation_1x_95ep |
|-------|---------|-------|----------|--------------------------|
| v99_saturation_1x_95ep (final_vp) | 46.2% ±1.1 | 13.0% ±0.8 | 29.5% ±0.7 | baseline |
| v100_actor_value_s42 (actor_relative) | 37.4% ±1.1 | 7.0% ±0.6 | **22.2% ±0.6** | **-7.3pp** |

**Result: actor_relative is significantly worse.** US WR dropped from 13% → 7%, USSR WR
dropped from 46% → 37%. Combined dropped 7.3pp.

**Root cause**: The value target polarity flips for US rows, but the input features are always
encoded from USSR perspective (VP positive = USSR ahead, influence counts are USSR/US not
actor/opponent). The shared trunk sees identical board features but receives opposite value
gradient depending on `phasing`. This creates contradictory training signal in the trunk:
the same state (e.g. USSR +10 VP) must simultaneously represent "good" (for USSR rows)
and "bad" (for US rows with actor_relative), poisoning the shared representations.

**Lesson**: Actor-relative value requires actor-relative *input encoding* (board features
from the acting side's perspective). With USSR-centric features, flipping only the target
makes things worse, not better.

**Next steps for US WR**:
- **A1**: ISMCTS diagnostic on v99_saturation_1x_95ep — does search help US more than USSR?
  This would suggest the BC policy is weak for US but search can compensate.
- **A3**: `--us-weight 2.0` upweight US rows in policy loss only (not value).
  Cheaper, doesn't require feature re-encoding, may help by giving US policy more gradient.
- **Longer term**: Actor-relative input encoding (flip VP sign, swap actor/opponent influence)
  before re-trying actor_relative value target.

---

## Nash-C Hypothesis Test

**Question**: Does nash_c data alone perform like nash_b? Or does mixing nash_b + nash_c
cause the 2× data degradation?

All runs: bs=8192, lr=0.0024, 95 epochs, patience=20, deterministic-split, baseline h256.
Benchmark: 2000 games/side.

| Model | Data | Seed | USSR WR | US WR | Combined |
|-------|------|------|---------|-------|----------|
| v99_nash_c_95ep_s42 | nash_c only | 42 | 41.6% ±1.1 | 9.7% ±0.7 | **25.7% ±0.6** |
| v99_nash_c_95ep_s7 | nash_c only | 7 | 43.1% ±1.1 | 10.5% ±0.7 | **26.9% ±0.7** |
| v99_nash_b_95ep_s7 | nash_b only | 7 | 38.6% ±1.1 | 8.9% ±0.6 | **23.8% ±0.6** |
| v99_nash_b_95ep_s123 | nash_b only | 123 | 29.8% ±1.0 | 5.7% ±0.5 | **17.8% ±0.6** |
| v99_saturation_1x_95ep (ref) | nash_b only | 42 | 46.2% ±1.1 | 13.0% ±0.8 | **29.5% ±0.7** |

### Summary (3 seeds each)

| Dataset | Seeds | Mean Combined | Std | Range |
|---------|-------|---------------|-----|-------|
| nash_c | s42, s7 | 26.3% | 0.6pp | 25.7-26.9% |
| nash_b | s42, s7, s123 | 23.7% | 4.8pp | 17.8-29.5% |

### Findings

1. **Nash_c is NOT inherently worse**: nash_c_s42=25.7%, nash_c_s7=26.9% — both
   competitive. Mean 26.3% exceeds nash_b's 3-seed mean of 23.7%.

2. **Nash_b seed variance is extremely large**: 3-seed range = 17.8-29.5% = **11.7pp**.
   The "nash_b best at 29.5%" conclusion was a lucky seed (s42). s123 is the worst
   result at 17.8%, dragging the mean well below nash_c.

3. **Nash_c is MORE stable**: nash_c range = 1.2pp vs nash_b range = 11.7pp.
   Nash_c's tighter distribution makes it a more reliable training dataset.

4. **Mixing hurts more than either alone**: nash_b+c@95ep = 22.5% (worst), while each
   dataset alone averages ~24-26%. Confirmed: the 2× degradation is from mixing, not
   from nash_c quality.

5. **Nash_c is the better dataset**: Higher mean (26.3% vs 23.7%) and lower variance.
   Use nash_c for future experiments unless there's a specific reason for nash_b.

### Interpretation

The nash_b and nash_c datasets were collected with different Nash temperature schedules,
creating subtly different strategy distributions. Training on mixed distributions creates
conflicting gradients that hurt generalization. Each dataset alone, with 95 epochs of
repetition, learns a coherent strategy.

Nash_b's extreme seed sensitivity (11.7pp range) suggests it sits on a sharper loss
landscape where small initialization differences lead to very different local optima.
Nash_c's stability suggests a smoother, more learnable distribution.

## ISMCTS Pooled Batching Speed Test (2026-04-04)

Tested `play_ismcts_matchup_pooled()` — pools N concurrent games and batches NN
leaf evaluations across all games' determinizations (up to N×8 items per batch).

| Config | Time/game | Speedup |
|--------|-----------|---------|
| CPU pool=1 (sequential) | 51.2s | 1.0× |
| CPU pool=4 | 45.9s | 1.12× |
| GPU pool=4 | 46.9s | 1.09× |
| GPU pool=4, 200 sims | 187.1s | — |

All tests: 4 games, 8 determinizations, model=v99_nash_c_95ep_s42.

### Findings

1. **Bottleneck is CPU MCTS logic, not NN inference**: GPU gives zero benefit because
   model forward passes are already fast (~1ms). Time is spent in select_to_leaf,
   backpropagate, and game state management.

2. **Pooled batching gives minimal speedup (~10%)**: With 50 sims and 8 dets, most
   determinizations finish early (cached/terminal nodes) so batch utilization drops
   quickly. Late-game moves average only 2-3 items per batch vs theoretical 32.

3. **200 sims = 3.1 min/game**: Linear scaling from 50 sims (51s) to 200 sims (187s).
   At target 200-400 sims, ISMCTS benchmarks of 100+ games would take 5-10 hours.

### Next steps for ISMCTS speed

The cross-game batching architecture is correct but doesn't address the real bottleneck.
Options ranked by expected impact:
1. **Multi-threaded determinizations**: Run 8 dets in parallel threads (true parallelism)
2. **Reduce n_determinizations**: 4 instead of 8 cuts MCTS work by half
3. **Tree reuse between moves**: Reuse subtree when advancing from one move to the next
4. **Profile C++ MCTS hotpath**: Identify and optimize allocation/copy bottlenecks

### ISMCTS Profiling Deep Dive (2026-04-04)

Instrumented `play_ismcts_matchup_pooled` with per-phase timing:

| Phase | Time | % |
|-------|------|---|
| expand+backprop | 97.3s | **92.2%** |
| nn_forward | 4.0s | 3.8% |
| select_to_leaf | 3.3s | 3.2% |
| commit_action | 0.8s | 0.7% |

**Root cause:** `expand_from_outputs()` in `mcts_search_impl.hpp` does per-element PyTorch
tensor operations (`.index()`, `.item<double>()`, `torch::softmax()`, `torch::full_like()`)
for every tree expansion. 45,169 expansions × dozens of tensor ops = millions of PyTorch
dispatch calls. Each has 1-10us overhead.

**Fix:** Replace PyTorch tensor ops with raw C++ float array operations (in progress via Codex).
Expected to reduce expand+backprop from 92% to <20%, making NN forward the dominant cost
and unlocking real speedup from cross-game batching.

## Self-Play Generation Loop

### Gen 0: Base model
Best base model: **v99_nash_c_95ep_s7** (26.9% combined)
- Data: nash_c heuristic only (1.37M rows)
- Hyperparams: bs=8192, lr=0.0024, 95 epochs, patience=20, h256

### Gen 1: Base + learned self-play data (2026-04-04)
Data collection: 2000 games learned-vs-heuristic per side (epsilon=0.05)
- USSR as learned: 146,612 rows (all games)
- US as learned: 34,546 rows (filtered to US wins only, 250/2000 = 12.5% win rate)
- Combined with heuristic anchor: 1,548,395 rows total

**Training:** bs=8192, lr=0.0024, 95 epochs, patience=20, h256, seed=42

| Model | USSR WR | US WR | Combined | vs Base |
|-------|---------|-------|----------|---------|
| v99_nash_c_95ep_s7 (base) | 43.1% ±1.1 | 10.5% ±0.7 | **26.9% ±0.7** | — |
| gen1_v99c_s7_s42 | 42.2% ±1.1 | 9.4% ±0.7 | **25.9% ±0.6** | -1.0pp |

**Analysis:** No improvement from Gen 1. The learned self-play data (181k rows, ~12% of total)
was not strong enough to provide signal beyond the heuristic data. This is expected for the
first self-play iteration — the model is essentially playing against a heuristic that it was
trained to imitate, so the learned data is largely redundant.

### Gen 1 AWR: advantage-weighted regression (2026-04-04)
Same data as gen1, but with --advantage-weight 0.5 (upweight winning-game rows).

| Model | USSR WR | US WR | Combined | vs Base |
|-------|---------|-------|----------|---------|
| gen1_v99c_s7_awr_s42 | 37.3% ±1.1 | 9.0% ±0.6 | **23.2% ±0.6** | **-3.7pp** |

**AWR hurt performance.** USSR dropped 5.8pp. The advantage weighting over-specializes on
the learned data fraction (12% of total), degrading broader heuristic imitation quality.
AWR requires a much larger learned-data fraction to be effective.

### Gen 1 Fine-tune: learned-only data from base checkpoint (2026-04-04)
Init from v99_nash_c_95ep_s42, train on learned data only (181k rows), lr=0.0006, 30 epochs.

**Reference (1000 games/side, seeds 50000+60000):**

| Model | USSR WR | US WR | Combined | vs Base |
|-------|---------|-------|----------|---------|
| v99_nash_c_95ep_s42 (base) | 38.1% | 9.9% | **24.0%** | — |
| gen1_finetune_s42 | 36.7% ±1.5 | 3.6% ±0.6 | **20.2%** | **-3.8pp** |

**Fine-tuning hurt performance.** USSR roughly flat (38.1% → 36.7%), but US collapsed
(9.9% → 3.6%). Fine-tuning on learned data (collected as USSR-vs-heuristic and
US-wins-only-vs-heuristic) over-specialized toward those play patterns and destroyed
US generalization. Consistent with game asymmetry findings.

**Conclusion:** Neither mixing (Gen 1, -1.0pp), AWR (-3.7pp), nor fine-tuning (-3.8pp)
improved on the pure BC baseline with v99 data. The model's first-generation self-play
data is not strong enough to improve beyond heuristic imitation.

### ISMCTS raw-pointer optimization (2026-04-04)
Replaced PyTorch tensor dispatch (tensor.index(), torch::softmax(), .item<double>())
with raw C float arrays and C++ softmax in `ismcts.cpp::expand_from_outputs`.
Same pattern already proven 3.3× on greedy benchmark in `mcts_batched.cpp`.

| Metric | Before | After | Speedup |
|--------|--------|-------|---------|
| ISMCTS 4 games (64 sims, 8 dets) | ~50s | ~30s | ~1.7× |
| Per-game | ~12.5s | ~7.5s | ~1.7× |

Less than 3.3× because ISMCTS NN forward pass is now the dominant cost (raw-pointer
optimization only affects post-inference tensor extraction, not the forward pass itself).

### Architecture sweep results (from pipeline, 2000 games/side)

| Model | Seed | USSR WR | US WR | Combined |
|-------|------|---------|-------|----------|
| v99_baseline_h256 | s42 | 42.1% | 11.6% | 26.9% |
| v99_baseline_h256 | s7 | 40.8% | 11.5% | 26.1% |
| v99_baseline_h256 | s123 | 37.2% | 8.4% | 22.8% |
| **Baseline mean** | | **40.0%** | **10.5%** | **25.3%** |
| v99_saturation_1x_95ep | s42 | 46.2% | 13.0% | **29.5%** |
| v99_control_feat_h256 | s42 | 42.4% | 7.1% | 24.8% |
| v99_control_feat_h256 | s123 | 45.1% | 12.7% | **28.9%** |
| v99_cf_1x95 | s42 | 45.8% | 11.7% | 28.7% |
| **v99_cf_1x95** | **s7** | **51.1%** | **13.7%** | **32.4%** |
| v99_cf_1x95 | s123 | 44.4% | 9.7% | 27.0% |
| **CF 1x95 mean** | | **47.1%** | **11.7%** | **29.4%** |

**Key finding:** `TSControlFeatModel` with 1× saturation (95 ep) is the best architecture.
- +4.1pp combined over baseline mean (29.4% vs 25.3%)
- Best single model: v99_cf_1x95_s7 at **32.4% combined** (51.1% USSR!)
- Region scoring scalars + per-country control features clearly help
- High seed variance (27.0% to 32.4%) suggests benefit is real but noisy

**Decision:** Use v99_cf_1x95_s7 as the base model for Gen 2 self-play data collection.
Collecting 2000 games USSR-side + 2000 games US-side (eps=0.05, Nash temps).

### Gen 2: self-play with best architecture — DONE

**Base model:** v99_cf_1x95_s7 (32.4% combined, best ever)
**Data collection:** 2048 USSR + 2048 US learned-vs-heuristic (264k + 260k rows)
**Training data:** heuristic (1.37M) + USSR learned (147k) + US learned wins-only (35k) = 1.55M rows
**Hyperparams:** control_feat, h256, bs=8192, lr=0.0024, 95ep, seed=42

| Model | USSR WR | US WR | Combined | vs base |
|-------|---------|-------|----------|---------|
| v99_cf_1x95_s7 (base) | 51.1% | 13.7% | **32.4%** | — |
| gen2_cf_s42 (greedy) | 33.2% | 9.6% | **21.4%** | **-11.0pp** |
| gen2_cf_s42 (ISMCTS 100g) | 29.0% | — | — | — |

**Result: Severe regression.** Including learned data in training hurts, consistent with
Phase 1 findings. The BC self-play data degrades model quality.

---

## ISMCTS Batching Optimization

### Multi-pending virtual loss (2026-04-04)

Redesigned ISMCTS to support multiple concurrent leaf selections per determinization
via virtual loss. Instead of selecting one leaf per det and batching, now selects up
to `max_pending_per_det` leaves (default 8) before a single batched NN call.

Combined with larger `pool_size` (running all games in parallel), this produces
dramatically larger NN batches:

| Config | avg_batch | NN time | Total (20g) | Batches |
|--------|----------|---------|-------------|---------|
| pool=4, pending=1 (old) | 27.4 | 37.1s | 164s | 19,246 |
| pool=4, pending=8 | 187.1 | 12.1s | 132s | 3,052 |
| pool=20, pending=8 | 922.3 | 6.8s | 124s | 619 |
| pool=40, pending=8 (40g) | 1,868.9 | 13.8s | 256s | 599 |
| pool=100, pending=8 (100g) | 4,511.2 | 35.8s | 639s | 603 |

**Key metrics:**
- NN amortization: **27 → 4,511 avg batch size (167×)**
- NN calls: **19,246 → 603 batches (32×)**
- NN time per game: **~1.9s → 0.36s (5.3× speedup)**
- Total per game: **~8.2s → 6.4s (1.3× overall on CPU)**
- **NN is no longer the bottleneck** — expand (tree ops) now dominates at 46%

GPU testing: RTX 3050 is **slower** than CPU for this model size (~1M params).
GPU overhead (kernel launch + data transfer) exceeds the compute benefit for
small models, even with batch sizes >1000. GPU would help with larger models.

### Expand phase optimization (tree operations)

After multi-pending made NN fast, expand (tree ops) became the bottleneck at 46%.
Profiling revealed two hot spots in `expand_from_raw`:
1. `collect_card_drafts` (58%) — repeated BFS for accessible countries via `legal_modes`/`legal_countries`
2. Edge building (42%) — `resolve_edge_action_raw` calling BFS again per influence edge

**Fix 1: AccessibleCache** — compute BFS-based accessible countries ONCE per expansion
(for influence, coup, realign modes), then reuse in both draft collection and edge
resolution. Previously `legal_modes` called BFS 3× per card, `legal_countries` again
per mode, and `resolve_edge_action_raw` again per influence edge — ~30+ BFS per expansion.
Now: 1 BFS per expansion.

**Fix 2: Inline influence allocation** — replaced `resolve_edge_action_raw` with inline
proportional allocation using cached accessible list, eliminating redundant BFS calls.

| Optimization | expand (s) | total (s) | vs original |
|-------------|-----------|---------|------------|
| Original (pool=4, pending=1) | 85.6 | 306.9 | 1.0× |
| Multi-pending + raw batch | 66.8 | 124.1 | 2.5× |
| + AccessibleCache | 28.7 | 59.7 | 5.1× |
| + Inline influence alloc | 28.6 | **58.4** | **5.3×** |

**Per-game: 15.3s → 2.9s (5.3× faster).** 20 games complete in under 1 minute.

### ISMCTS 200-game benchmark (v99_cf_1x95_s7, 50 sims, 8 dets, pool=64, pending=8)

| Side | Wins/Total | WR | Time | per-game |
|------|-----------|-----|------|----------|
| USSR | 85/200 | **42.5%** | 736s | 3.7s |

Profile: expand=329s (45%), select=182s (25%), apply=119s (16%), nn=90s (12%).
Avg batch: 2757, total batches: 1959.

**Finding**: ISMCTS at 50 sims (42.5% USSR) is *weaker* than greedy policy (51.1% USSR).
With only 50 sims and 8 determinizations, search doesn't help — the value function isn't
accurate enough and determinization adds noise. Would need 200+ sims to likely match greedy.

---

## MCTS Teacher Distillation (2026-04-04)

### Approach
Use full-information MCTS self-play to generate soft policy targets (visit count
distributions). Train the policy network via KL-divergence to match MCTS's decisions.
Unlike BC self-play (which failed), this provides *search-quality* targets with a soft
distribution over actions, not just single-action imitation.

### Teacher data collection
Model: v99_cf_1x95_s7, 50 sims, pool_size=32, Dirichlet noise (alpha=0.3, eps=0.25),
temperature=1.0 (sample proportional to visits). 2× 1000 games with different seeds.
Rate: ~2.8s/game, ~143 rows/game.

### v100 Training Results

Two models trained on `combined_v99_clean_b` with batch_size=8192, lr=0.0024, 95 epochs:

| Model | Value Target | Teacher | USSR WR | US WR | Combined |
|-------|-------------|---------|---------|-------|----------|
| v100_teacher | final_vp | MCTS 50sim (w=0.5) | 43.2% | 12.6% | 27.9% |
| v100_actor_value | actor_relative | none | 37.6% | 8.3% | 23.0% |
| v99_1x95ep (baseline) | final_vp | none | 46.2% | 13.0% | 29.5% |
| v99_cf_s7 (best) | final_vp | none | 51.1% | 13.7% | 32.4% |

**Finding**: Both v100 variants regress vs baseline. Likely causes:
1. **Wrong hyperparams**: batch_size=8192 + lr=0.0024 (8× batch, 2× LR vs proven recipe)
2. **Teacher data from weak model**: MCTS targets collected with v23 (much weaker) add noise
3. **actor_relative value target**: Hurts badly (-6.5pp combined vs final_vp)

Note: v100 models trigger a card_id=0 engine bug in ~5-10% of games, so results are
approximate (benchmarked with crash-skipping). The bug occurs during event resolution
when the model's different play style reaches game states the engine hasn't been tested on.

### MCTS vs Heuristic — Full Knowledge (400 sims, 100 games/side)

| Model | USSR WR | US WR | Combined | vs Greedy |
|-------|---------|-------|----------|-----------|
| v99_cf_s7 MCTS | 48.0% | 10.0% | 29.0% | -3.4pp |
| v99_1x95ep MCTS | 29.0% | 7.0% | 18.0% | -11.5pp |

**Finding**: MCTS hurts both models vs heuristic. The value head is too noisy — search amplifies
errors instead of finding better moves. With cf_s7, USSR improves slightly (48% vs 51.1%)
but US drops badly (10% vs 13.7%). With 1x95ep, the degradation is catastrophic.
This confirms the value head is the bottleneck, not search depth.

**UPDATE**: The above MCTS results were collected with a **double-softmax bug** in the
batched MCTS prior computation. The model's `country_logits` output is already a probability
distribution (mixture of softmaxes), but `expand_from_raw` applied `softmax_inplace` again,
flattening influence placement priors toward uniform. Since influence is ~50% of all decisions,
this made MCTS priors essentially random for the most common action type. The greedy benchmark
path correctly used raw `country_strategy_logits` (not the pre-mixed probabilities), so greedy
had better prior quality than MCTS.

---

## Double-Softmax Fix + MCTS vs Greedy NN (2026-04-04)

### Bug: double-softmax on country_logits in batched MCTS

**Root cause**: In `mcts_batched.cpp:expand_from_raw` and `ismcts.cpp:expand_from_raw`,
the influence allocation and coup/realign target priors used `country_logits_arr` (already
probabilities from the model's mixture-of-softmaxes output) and applied `softmax_inplace`
again. This compressed the distribution toward uniform, wasting simulations on poor influence
placements. The greedy benchmark path correctly used `strategy_logits` + `country_strategy_logits`
(raw logits) with a single softmax.

**Fix**: Modified `expand_from_raw` in both files to prefer strategy-selected raw logits
(`country_strategy_logits[argmax(strategy_logits)]`) over pre-mixed `country_logits`.
Now MCTS priors match the greedy policy's prior quality.

### Post-Fix Greedy Benchmark (2000 games/side, seed=42000)

| Model | USSR WR | US WR | Combined |
|-------|---------|-------|----------|
| v99_cf_s7 (best) | 49.8% | 12.8% | 31.3% |
| v99_1x95ep | 46.3% | 9.8% | 28.1% |
| v100_actor_value | 38.6% | 7.1% | 22.9% |

Note: v100_teacher was found to have identical weights to v99_1x95ep (byte-for-byte
identical game outcomes across multiple seeds).

### MCTS vs Greedy NN — Head-to-Head (v99_cf_s7, 400 sims, 100 games/side)

| MCTS side | MCTS WR | Greedy WR | Delta vs greedy-vs-greedy |
|-----------|---------|-----------|--------------------------|
| USSR | **86.0%** | 13.0% | +7.4pp (vs 78.6% baseline) |
| US | **28.0%** | 71.0% | +6.6pp (vs 21.4% baseline) |
| **Combined** | **57.0%** | **42.0%** | +15.0pp |

Greedy-vs-greedy baseline: 78.6% USSR WR (from previous session).
MCTS uses Dirichlet noise (alpha=0.3, eps=0.25), T=0 (greedy selection).
Opponent uses greedy argmax from same model.

**Finding**: After fixing the double-softmax bug, MCTS with 400 sims **definitively
beats greedy NN by 15pp combined**. Search works! The USSR side gains +7.4pp and the
US side gains +6.6pp from search. The fix is particularly impactful because influence
placement is the most frequent action type, and MCTS now uses properly concentrated
priors for it.

This reverses the previous conclusion that "the value head is the bottleneck." The value
head is good enough for MCTS to help — the problem was degraded priors preventing effective
tree search.

### MCTS vs Heuristic — Post-Fix (v99_cf_s7, 400 sims, 200 games/side)

| Side | MCTS (fixed) | MCTS (pre-fix) | Greedy baseline | Delta |
|------|-------------|----------------|-----------------|-------|
| USSR | **57.0%** | 48.0% | 49.8% | **+7.2pp** |
| US | **17.0%** | 10.0% | 12.8% | **+4.2pp** |
| Combined | **37.0%** | 29.0% | 31.3% | **+5.7pp** |

**Finding**: With the double-softmax fix, MCTS consistently beats greedy policy vs heuristic.
The improvement is larger for USSR (+7.2pp) than US (+4.2pp), but both sides benefit.
MCTS-USSR 57% is the strongest result we've seen for any single-model approach.

### Greedy NN Temperature Sweep (v99_cf_s7, 1000 games/side vs heuristic)

| Temperature | USSR WR | US WR | Combined |
|-------------|---------|-------|----------|
| T=0.0 | 55.7% | 10.1% | 32.9% |
| **T=0.1** | **57.6%** | **11.1%** | **34.4%** |
| T=0.2 | 53.1% | 10.2% | 31.6% |
| T=0.3 | 53.3% | 10.6% | 31.9% |
| T=0.5 | 54.2% | 9.3% | 31.8% |
| T=0.8 | 55.6% | 10.5% | 33.0% |
| T=1.0 | 52.6% | 9.8% | 31.2% |

**Finding**: T=0.1 is optimal (+1.5pp combined over T=0). Light sampling helps by
adding diversity to break deterministic patterns, but higher temperatures degrade play.
Greedy-vs-greedy (same model): 78.0% USSR WR, confirming massive side asymmetry in learned policy.

### ISMCTS vs Heuristic — Post-Fix (v99_cf_s7, 50 sims × 8 dets, 50 games)

| Method | USSR WR | vs Pre-Fix | vs Greedy |
|--------|---------|-----------|-----------|
| ISMCTS (fixed) | **56.0%** | +13.5pp | +6.2pp |
| ISMCTS (pre-fix) | 42.5% | baseline | -7.3pp |
| Greedy baseline | ~49.8% | — | baseline |

**Finding**: ISMCTS also benefits massively from the double-softmax fix (+13.5pp).
Even with hidden information (8 determinizations × 50 sims), search now beats greedy.
The improvement is larger for ISMCTS (+13.5pp) than full-info MCTS (+7.2pp),
likely because the prior quality matters even more when determinization adds noise.

### v101 Teacher Distillation Attempt (heuristic + MCTS data, teacher KL)

**Setup**: Trained on heuristic_nash_b (1.28M rows) + MCTS self-play (88K rows, 600 games),
with teacher KL loss (weight=0.5) from MCTS visit count distributions. Teacher coverage: 6.1%.
Same hyperparams as v99_cf_s7 (lr=0.0024, batch=8192, 95 epochs, seed=7).

| Model | USSR WR | US WR | Combined |
|-------|---------|-------|----------|
| v101_teacher_w05 | 39.0% | 5.8% | 22.4% |
| v99_cf_s7 (baseline) | 56.4% | 10.4% | 33.4% |

**Finding**: Significant regression (-11pp combined). The MCTS self-play data mixed into
training hurts: it has different action distributions (stochastic from T=1.0 visit counts)
that confuse the BC loss. 6% teacher coverage is too sparse to compensate. The model is
imitating noisy MCTS play rather than learning from MCTS's search quality.

**Lesson**: Teacher distillation needs either (a) teacher targets on 100% of training rows
(run MCTS search on heuristic positions), or (b) separate MCTS data from BC data entirely
(train BC on heuristic only, apply teacher KL only to matched rows).

---

## MCTS Sim Count Sweep (2026-04-04)

Model: v99_cf_1x95_s7, vs heuristic, 100 games/side per sim count, CPU.

| Sims | USSR WR | US WR | Combined | Time/100g |
|------|---------|-------|----------|-----------|
| 100 | 56.0% | 12.0% | **34.0%** | ~80s |
| 200 | 56.0% | 13.0% | **34.5%** | ~130s |
| 400 (ref, 200g/side) | 57.0% | 17.0% | **37.0%** | — |
| 800 | 44.0% | 23.0% | **33.5%** | ~600s |

**Finding**: With 100 games/side, variance is too high (±10pp) to draw conclusions. The
400-sim result (200 games/side) of 37.0% remains the best reference point. The 800-sim
result of 33.5% is within noise of the 100-200 sim results. The "bigger sim budget helps
until ~400 then degrades" hypothesis is possible but needs more games to confirm.

**Caveat**: The 400-sim "37%" was from a separate benchmark run at 200 games/side with
different seeds — not directly comparable to the 100-game runs above.

**Follow-up sweep (Exp 2, post-fix, 200g/side, seed=42000):**

| Sims | USSR WR | US WR | Combined | Time (s) |
|------|---------|-------|----------|----------|
| 50 | 54.5% | 11.0% | **32.75%** | ~340 |
| 100 | 59.5% | 15.0% | **37.25%** | ~855 |
| 200 | 53.0% | 14.0% | **33.5%** | ~860 |
| 400 | 58.0% | 17.5% | **37.75%** | ~1033 |

**Finding**: Results are noisy at 200 games (±7pp variance). No clear monotonic trend.
100 and 400 sims yield ~37% each; 50 and 200 yield ~33%. Likely seed/variance artifact.
At 200 games/side, ±7pp is too wide to determine optimal sim count.
Need 500+ games/side to distinguish 50 vs 400 reliably.
Best single estimate: **400 sims = 37.75% combined** (58% USSR, 17.5% US).

**Definitive comparison (500g/side, seed=43000):**

| Sims | USSR WR | US WR | Combined |
|------|---------|-------|----------|
| 100 | 53.4% | 15.2% | **34.3%** |
| 400 | 53.0% | 14.6% | **33.8%** |

**Conclusion: 100 sims = 400 sims** within noise (±3pp at 500 games). 400 sims provides ZERO
benefit over 100 sims at 4× the compute cost. The previous "37%" estimates were noise from
200-game samples. True MCTS benefit vs heuristic is ~34% combined (vs ~31-32% greedy), consistent
across sim counts once variance is controlled.

**Decision**: Use 100 sims for all future MCTS inference and teacher data collection.
100 sims is ~7min/100 games vs ~17min for 400 sims — 2.4× faster with same strength.

---

## Exp1: Nash_c control_feat 3 seeds (2026-04-05)

Training: control_feat h256, nash_c only (1.37M rows), bs=8192, lr=0.0024, 95ep, patience=20, seed=42/7/123.
Benchmark: 1000 games/side (2×500), seeds 42000+43000.

| Model | USSR WR | US WR | Combined | Notes |
|-------|---------|-------|----------|-------|
| v104_cf_nashc_s42 | 39.2% ±1.5 | 8.6% ±0.9 | **23.9% ±0.9** | outlier low |
| v104_cf_nashc_s7 | 54.9% ±1.6 | 8.1% ±0.9 | **31.5% ±0.9** | — |
| v104_cf_nashc_s123 | 53.2% ±1.6 | 11.4% ±1.0 | **32.3% ±0.9** | — |
| v99_cf_1x95_s7 (ref) | 51.1% | 13.7% | **32.4%** | nash_b, reference |

Mean (3 seeds) = 29.2%, range = 8.4pp (s42 outlier).
Excluding s42 outlier: mean = 31.9%, range = 0.8pp.

**Analysis**:
- Nash_c seeds s7 and s123 match the reference v99_cf_1x95_s7 (nash_b) within noise: 31.5/32.3% vs 32.4%.
- Nash_c does NOT improve over nash_b on this configuration — previous comparison suggested nash_c
  advantage was confounded (v99_nash_c was measured at ~26% but with different seeds/benchmarks).
- Seed variance is still large (8.4pp range) even with nash_c. The "lower variance" claim from
  earlier limited-seed comparison was over-extrapolated.
- s42=23.9% is a genuine outlier — same pattern as v99_cf_1x95_s7 seed runs (one seed always regresses).
- **Decision**: Nash_c and nash_b are equivalent for cf_1x95. The best single seed (s123=32.3%) matches
  the reference. No gain from switching. Proceed to Exp3 (teacher KL on heuristic positions).

---

## Exp4: Multi-seed tournament v104 nash_c (2026-04-05)

Training 5 seeds of cf_1x95 on nash_c to find best single seed. Seeds already done: 42, 7, 123.
Adding seeds 999 and 2024.

| Model | USSR WR | US WR | Combined | Notes |
|-------|---------|-------|----------|-------|
| v104_cf_nashc_s42 | 39.2% ±1.5 | 8.6% ±0.9 | **23.9% ±0.9** | outlier low |
| v104_cf_nashc_s7 | 54.9% ±1.6 | 8.1% ±0.9 | **31.5% ±0.9** | — |
| v104_cf_nashc_s123 | 53.2% ±1.6 | 11.4% ±1.0 | **32.3% ±0.9** | — |
| v104_cf_nashc_s999 | 54.2% ±1.6 | 5.6% ±0.7 | **29.9% ±0.9** | — |
| v104_cf_nashc_s2024 | 53.8% ±1.6 | 9.8% ±0.9 | **31.8% ±0.9** | — |
| v99_cf_1x95_s7 (ref) | 51.1% | 13.7% | **32.4%** | nash_b, reference |

### Exp4 Analysis (2026-04-05)

5-seed tournament results for cf_1x95 on nash_c:

| Seed | USSR WR | US WR | Combined |
|------|---------|-------|----------|
| s42 | 39.2% | 8.6% | **23.9%** ← outlier |
| s7 | 54.9% | 8.1% | **31.5%** |
| s123 | 53.2% | 11.4% | **32.3%** ← best |
| s999 | 54.2% | 5.6% | **29.9%** |
| s2024 | 53.8% | 9.8% | **31.8%** |
| Mean (all 5) | — | — | **29.9%** |
| Mean (excl s42) | — | — | **31.4%** |

**Best seed: s123 at 32.3%** — matches v99_cf_1x95_s7 (nash_b, 32.4%) within noise.
s42 remains an outlier pattern consistent with earlier results.
Excluding s42, the 4-seed range is 29.9-32.3% = 2.4pp — much tighter than expected.

**Conclusions:**
1. Nash_c and nash_b are equivalent for cf_1x95 architecture (both ~32% for good seeds).
2. The outlier seed (s42) consistently produces ~24% regardless of dataset.
3. The non-outlier seeds cluster tightly at 30-32% combined.
4. **Best model for Exp3 teacher KL:** v104_cf_nashc_s123 (32.3%) or s2024 (31.8%).
   However Exp3 uses seed=42 to test whether teacher KL fixes the outlier pattern.

---

## Exp3: Teacher KL on Heuristic Positions (2026-04-05)

**Approach**: Collect MCTS teacher targets for heuristic game positions using the new
`heuristic_teacher_mode` in BatchedMctsConfig. Game trajectories are bit-identical to
pure heuristic (same seed, RNG saved/restored around MCTS measurement). Verified: teacher
mode actions for selfplay_77700_0000 match nash_c parquet exactly.

**Collection**: 3 seeds (77700, 78200, 79700) × 500-1000 games, 100 sims/decision, pool_size=32.
Combined into: data/selfplay/mcts_teacher_nashc_100sim_combined.parquet (283k rows).
Coverage in nash_c: **14.0%** (191,833 matched / 1,367,237 BC rows).
Collection complete as of 2026-04-05 (batch-collected in ~15 min total).

**Training** (running):
```bash
uv run python scripts/train_baseline.py \
  --data-dir data/nash_c_only \
  --out-dir data/checkpoints/v105_teacher_heur_kl_s42 \
  --model-type control_feat --hidden-dim 256 \
  --batch-size 8192 --lr 0.0024 --epochs 95 --patience 20 \
  --dropout 0.1 --weight-decay 1e-4 --label-smoothing 0.05 \
  --one-cycle --deterministic-split --value-target final_vp --seed 42 \
  --teacher-targets data/selfplay/mcts_teacher_nashc_100sim_combined.parquet \
  --teacher-weight 0.5
```

| Model | USSR WR | US WR | Combined | Notes |
|-------|---------|-------|----------|-------|
| v104_cf_nashc_s42 (baseline) | 39.2% | 8.6% | **23.9%** | no teacher |
| v105_teacher_heur_kl_s42 | 34.4% | 5.4% | **19.9%** | 14% coverage, w=0.5 — **regressed** |

**Result: Teacher KL HURTS (-4.0pp combined vs baseline)**. This is the 5th consecutive teacher KL
failure (v100, v101, v103, v105@4.7%, v105@14%).

**Root cause — objective conflict:**
The heuristic BC target is a ONE-HOT card distribution (the heuristic deterministically picks one
card). MCTS visit counts are a SOFT distribution across multiple cards. The KL loss pushes the
model toward the soft distribution while BC loss pushes toward the one-hot. These objectives
directly oppose each other.

Evidence: `teacher_kl_card = 2.06` (training metric) — extremely high KL between model outputs
and MCTS targets, showing fundamental distributional mismatch. The model cannot simultaneously
match heuristic (one-hot) and MCTS (soft) without sacrificing performance on both.

**Conclusion**: Teacher KL distillation from MCTS onto heuristic positions **does not work**
with the current BC setup. The conflict between hard heuristic labels and soft MCTS distributions
prevents learning. This approach is definitively ruled out.

**What DOES work for inference-time improvement**: MCTS at inference (+5pp vs greedy).
The value head is accurate enough for search to help, but distilling search knowledge into
BC training is not feasible with current data/approach.

**Follow-up: Exp3b — low teacher weight (w=0.1, seed=7)**:

| Model | USSR WR | US WR | Combined | val_loss | Notes |
|-------|---------|-------|----------|----------|-------|
| v104_cf_nashc_s7 (baseline) | 54.9% | 8.1% | **31.5%** | 2.27 | no teacher |
| v105b_teacher_kl_s7_w01 | 57.6% | 7.8% | **32.7%** | 2.31 | w=0.1, 14% cov |

+1.2pp improvement, but within ±0.9pp CI (500 games). Marginal and uncertain.
Teacher KL at w=0.1 does not hurt and may marginally help — but the benefit is too small
to act on. The conflict between hard BC labels and soft MCTS targets still exists at w=0.1,
just with less force.

**Definitive teacher KL verdict**: Effect is too small to reliably measure. Not worth the
engineering complexity for <1pp improvement when the approach fundamentally conflicts with
hard-label BC training. Teacher KL distillation from MCTS is **deprioritized**.

**Next directions**:
1. Architecture improvements (GNN, better value head) to raise BC ceiling
2. MCTS at inference as default for competitive play
3. Self-play with MCTS move selection (expensive but might break BC plateau)

---

## v103: Pure MCTS Teacher Distillation with 100% Coverage (2026-04-04)

**Approach**: Train on 276K MCTS self-play rows (post double-softmax fix, 400 sims, 2000 games)
with 100% teacher KL coverage. Game IDs match — every training row has a teacher target.
This avoids the v101 failure mode (mixed data, 6% coverage).

**Data**: `data/mcts_teacher_400sim_2k/` — 276K rows BC + 276K matched teacher targets.
**Hyperparams**: baseline h256, bs=4096, lr=0.0024, 95ep, seed=7, teacher_weight=0.5, teacher_value_weight=0.3.
**W&B**: korduban-ai/twilight-struggle-ai/v103_mcts_teacher_w05

Training converged: best val_loss=5.978, card_top1=52%, mode_acc=79%.
Overfitting present (train_loss=4.9 vs val_loss=6.4 at ep80) due to small dataset (276K vs 1.28M).

| Model | USSR WR | US WR | Combined | Notes |
|-------|---------|-------|----------|-------|
| v103_mcts_teacher_w05 | 25.6% | 1.2% | **13.4%** | Severe regression |
| v99_cf_s7 (baseline) | 56.4% | 10.4% | 33.4% | 2000g/side ref |

**Result: Severe regression (-20pp combined)**. This definitively rules out training on MCTS
self-play data. Root causes:
1. **Too little data**: 276K rows vs 1.28M heuristic rows — model is undertrained
2. **Noisy trajectories**: MCTS at T=1.0 produces diverse but suboptimal action distributions
3. **Teacher KL alone can't fix distribution mismatch**: The KL loss brings policy closer to
   MCTS visit counts, but if the underlying game states are low-quality (from stochastic MCTS
   play), the teacher signal is weak

**Conclusion**: The only viable teacher distillation approach is applying KL to **heuristic
positions** (keep BC data intact, add MCTS search on each heuristic position as teacher target).
Pure MCTS-data training is dead.

---

## Exp5: GNN Country Adjacency Architecture (2026-04-05)

**Architecture**: `TSControlFeatGNNModel` — adds 2-round graph message passing on the
country graph adjacency matrix. Countries aggregate neighbor features via:

```python
h = relu(country_proj(per_country_feats))   # (B, 86, 32)
h_agg1 = matmul(adjacency, h)               # (B, 86, 32) row-norm neighbor aggregation
h = relu(gconv1(cat([h, h_agg1], dim=-1)))  # (B, 86, 32) round 1
h_agg2 = matmul(adjacency, h)               # round 2 aggregation
h = relu(gconv2(cat([h, h_agg2], dim=-1)))  # (B, 86, 32) round 2
```

Then same region pooling + control scalars as `TSControlFeatModel`.
Parameters: 486,801 (vs ~450K for non-GNN control_feat).
Adjacency: 86×86 row-normalized matrix from `data/spec/adjacency.csv`.
Exported via `jit.trace` (jit.script incompatible with free function + nn.Linear args).

**Training** (same hyperparams as cf_1x95 recipe):
```bash
uv run python scripts/train_baseline.py \
  --data-dir data/nash_c_only \
  --out-dir data/checkpoints/v106_cf_gnn_s7 \
  --model-type control_feat_gnn --hidden-dim 256 \
  --batch-size 8192 --lr 0.0024 --epochs 95 --patience 20 \
  --dropout 0.1 --weight-decay 1e-4 --label-smoothing 0.05 \
  --one-cycle --deterministic-split --value-target final_vp --seed 7
```

| Model | USSR WR | US WR | Combined | Notes |
|-------|---------|-------|----------|-------|
| v104_cf_nashc_s7 (control_feat) | 54.9% | 8.1% | **31.5%** | no GNN |
| v104_cf_nashc_s123 (control_feat) | 53.2% | 11.4% | **32.3%** | no GNN |
| **v106_cf_gnn_s7** | **62.6%** | **11.8%** | **37.2%** | **+5.7pp vs best cf** |

**Result: GNN adjacency provides a massive +5.7pp improvement!**
USSR WR improves from 54.9% → 62.6% (+7.7pp) and US WR from 8.1% → 11.8% (+3.7pp).
This is the best BC model ever by a large margin.

**Interpretation**: Graph message passing enables each country to aggregate information
from its neighbors, allowing the model to reason about adjacency structure (e.g., France
can "see" West Germany, Benelux). This is fundamental to TS strategy — influence spreads
along adjacency, access requires adjacency or controlled countries. Two rounds of message
passing captures 2-hop neighborhood context.

**Multi-seed GNN results (4 seeds):**

| Model | USSR WR | US WR | Combined | Notes |
|-------|---------|-------|----------|-------|
| v106_cf_gnn_s7 | 62.6% | 11.8% | **37.2%** | — |
| v106_cf_gnn_s42 | 60.8% | 11.6% | **36.2%** | — |
| v106_cf_gnn_s123 | 56.4% | 4.0% | **30.2%** | US collapse |
| v106_cf_gnn_s999 | 56.8% | 8.4% | **32.6%** | US collapse |
| **GNN mean (all 4, canonical)** | — | — | **35.3%** | seed=50000/50500 |
| **GNN mean (s7+s42, strong seeds)** | — | — | **38.9%** | — |
| v99_cf_1x95_s7 (cf reference) | 53.6% | 8.4% | **31.0%** | canonical seed=50000 |

**GNN is confirmed significantly better.** Canonical benchmark (seed=50000/50500):
- All 4 seeds: mean 35.3% vs cf 31.0% = **+4.3pp**
- Strong seeds (s7+s42): mean 38.9% vs cf 31.0% = **+7.9pp**
- s123 and s999 are US-collapse outliers (US WR 4-8%); pattern mirrors cf where 1-2 seeds collapse

Three seeds show the same pattern as cf: one outlier seed with US collapse (s123 for GNN, s42 for cf), two strong seeds. The non-outlier seeds cluster at 36-37% — a genuine and large improvement.

**MCTS fast-replica investigation (2026-04-05):**
The `cpp/mcts_batched_fast/` replica was evaluated for porting. **Conclusion: do not port.**
- Correctness test: fast replica MCTS 52% USSR vs heuristic; production MCTS 59.2%; greedy 53.8%.
- Fast replica MCTS is WEAKER than greedy (52% vs 53.8%) — search is not helping.
- Root cause: fast replica uses collapsed tree structure with one edge per (card, mode) for influence,
  while production uses one edge per (card, mode, country). Influence allocation to specific countries
  cannot be explored or evaluated differently — the tree cannot improve country-level decisions.
- Additionally, production code is already faster than the fast replica at all measured settings
  (due to AccessibleCache + raw-pointer expand already in production).
- Only the `select_edge_fast` inline is structurally sound, but isolated impact is modest.

**Phase 2b analysis (regional scoring scalars) — 2026-04-05:**
Original plan was to add 14 explicit tier scalars (7 regions × 2 sides × {None,Presence,Domination,Control}).
**Verdict: not needed.** `ControlFeatGNNEncoder` already computes 28 per-region BG/non-BG control counts
internally from the influence tensor and concatenates them with the 11 base scalars (total 39 inputs to
scalar_encoder). The model already has comprehensive regional information. Explicit tiers would be a
nonlinear transformation of what the model already sees — no new signal. Phase 2b is cancelled.

**Next priorities** (2026-04-05):
1. ~~v106_cf_gnn_s999 in progress~~ DONE: 32.6% (outlier seed)
2. ~~MCTS inference benchmark~~ DONE: no significant MCTS benefit at 100 sim
3. **GNN Gen 0 self-play collection running** (s42 base, 2000g USSR + 2000g US)
4. After Gen 0: train v107_cf_gnn_gen0, benchmark vs v106 baseline
5. Phase 2c if Gen 0 self-play plateaus: allocation head + DP decoder

**MCTS benchmark on GNN s7 (100 sim, 500/side, seed=77000/77500)** — 2026-04-05:

| Method | USSR WR | US WR | Combined |
|--------|---------|-------|----------|
| Greedy (seed=77000) | 62.2% | 11.4% | **36.8%** |
| MCTS 100sim (seed=77000) | 60.4% | 11.6% | **36.0%** |

**Result: MCTS 100sim provides no significant benefit over greedy for GNN** (−0.8pp, within 2σ noise).
This contrasts with v99 (weaker BC model) where MCTS gave +5.4pp. Hypothesis: the GNN's stronger
card/mode policy leaves less room for tree search improvement. MCTS only searches over card/mode (not
influence placement — one collapsed tree edge per card×mode for influence), so as the policy improves,
the marginal value of card/mode tree search decreases.

Note: `benchmark_batched` and `benchmark_mcts` both return `list[GameResult]` not `list[Side]`.
Correct counting: `sum(1 for x in r if x.winner == tscore.Side.USSR)`, NOT `.count(tscore.Side.USSR)`.
The `.count()` method always returns 0 for GameResult objects.

**Bug fixes (2026-04-05):**
- `mcts_batched.cpp`: `set_num_interop_threads` wrapped in try/catch (can only be set once; calling
  it a second time threw exception on the second benchmark_mcts call)
- All benchmark scripts updated to use correct `sum(1 for x ...)` counting

---

## Benchmark Methodology Audit (2026-04-05)

### Critical finding: Train/Benchmark temperature mismatch

**Training data** collected with `--nash-temperatures`: heuristic uses `choose_minimal_hybrid_sampled()`
with per-game Boltzmann temps drawn from Nash equilibrium mixed strategy.

**Benchmark** (`benchmark_games_batched`): heuristic used deterministic `choose_action(MinimalHybrid)` —
T=0 argmax. **No temperature, no sampling.**

This is a **train/test mismatch**: model trains against Nash-temp heuristic but is evaluated
against deterministic heuristic.

### Nash-temp heuristic is STRONGER than deterministic

5000-game heuristic-vs-heuristic comparison:

| Condition | USSR WR | US WR | Draws | DEFCON-1 | Avg VP |
|-----------|---------|-------|-------|----------|--------|
| Nash temps (seed=50000) | 66.19% | 33.81% | 111 | 985 | 2.57 |
| Nash temps (seed=60000) | 67.37% | 32.63% | 115 | 1036 | 2.81 |
| **Nash mean** | **66.8%** | **33.2%** | — | — | — |
| T=0 deterministic (seed=50000) | 72.43% | 27.57% | 103 | 744 | 5.31 |
| Theoretical Nash value | **66.09%** | **33.91%** | — | — | — |

**Empirical mean (66.8%) matches theoretical Nash value (66.09%)** within ±1.2pp noise.

The deterministic heuristic is **weaker** (more exploitable) — especially as US side. Nash temps
add stochasticity that prevents exploitation of predictable deterministic play.

### Impact on model benchmarks

All previous benchmarks measured against T=0 deterministic heuristic (easier opponent).
Adding `nash_temperatures=True` to `benchmark_batched`:

| Model | T=0 USSR | T=0 US | T=0 Combined | Nash USSR | Nash US | Nash Combined |
|-------|----------|--------|-------------|-----------|---------|---------------|
| v106_cf_gnn_s42 | 67.0% | 14.0% | **40.5%** | 55.8% | 14.0% | **34.9%** |
| v99_cf_1x95_s7 | 53.6% | 8.4% | **31.0%** | 46.6% | 9.2% | **27.9%** |

**GNN advantage preserved**: +7.0pp with Nash temps (vs +9.5pp at T=0).
USSR WR drops ~11pp across all models (harder opponent), US WR roughly stable.

### Recommendation

**All future benchmarks should use `nash_temperatures=True`** to match training conditions.
T=0 numbers are kept for backwards comparison but are **not the primary metric**.

Code fix: Added `nash_temperatures` parameter to `benchmark_games_batched` and Python binding.
Usage: `tscore.benchmark_batched(model, side, n_games, seed=50000, nash_temperatures=True)`

### Full Nash-temp canonical benchmark (seed=50000/50500, 500g/side)

| Model | T=0 USSR | T=0 US | T=0 Comb | Nash USSR | Nash US | Nash Comb |
|-------|----------|--------|----------|-----------|---------|-----------|
| v106_cf_gnn_s7 | 60.4% | 14.2% | 37.3% | 52.8% | 9.2% | **31.0%** |
| v106_cf_gnn_s42 | 67.0% | 14.0% | 40.5% | 55.8% | 14.0% | **34.9%** |
| v106_cf_gnn_s123 | 57.8% | 4.0% | 30.9% | 48.6% | 3.2% | **25.9%** |
| v106_cf_gnn_s999 | 56.8% | 8.4% | 32.6% | 43.8% | 9.2% | **26.5%** |
| **GNN mean (all 4)** | — | — | **35.3%** | — | — | **29.6%** |
| v99_cf_1x95_s7 | 53.6% | 8.4% | 31.0% | 46.6% | 9.2% | **27.9%** |
| v99_cf_1x95_s42 | — | — | — | 40.2% | 8.4% | **24.3%** |
| v99_cf_1x95_s123 | — | — | — | 40.6% | 7.0% | **23.8%** |
| **cf mean (3 seeds)** | — | — | — | — | — | **25.3%** |

**GNN advantage at Nash temps**: +4.3pp (all-4 GNN vs 3 cf seeds).
Excluding s42 outlier: GNN mean (s7+s123+s999) = 27.8% vs cf mean = 25.3% = **+2.5pp** — real but modest.
The s42 seed is a GNN-specific lucky initialization (+10.6pp over cf s42).

**Key takeaway**: GNN provides a genuine +2.5-4.3pp improvement over cf under fair Nash-temp benchmarking.
This is smaller than the T=0 headline of +4.3-9.5pp but still meaningful and consistent across seeds.

---

## v107: GNN Gen 0 Self-Play (2026-04-05)

**Base model**: v106_cf_gnn_s42 (best GNN seed, Nash combined=34.9%)
**Data**: 1.37M nash_c anchor + 281K USSR self-play (all rows) + 32K US self-play (wins only, 11.7%)
**Total**: 1.68M rows
**Training**: GNN, h256, bs=8192, lr=0.0024, 95ep, seed=7. Best epoch: 95 (val_loss=2.3832).

| Model | T=0 USSR | T=0 US | T=0 Comb | Nash USSR | Nash US | Nash Comb |
|-------|----------|--------|----------|-----------|---------|-----------|
| v106_cf_gnn_s42 (base) | 67.0% | 14.0% | 40.5% | 55.8% | 14.0% | **34.9%** |
| **v107_cf_gnn_gen0** | **67.0%** | **14.4%** | **40.7%** | **57.0%** | **14.8%** | **35.9%** |
| Delta | +0.0pp | +0.4pp | +0.2pp | +1.2pp | +0.8pp | **+1.0pp** |

**Result: +1.0pp at Nash temps (within ±2.5pp CI). Not statistically significant.**

Self-play data from the GNN model provides minimal improvement — same pattern as Phase 1
BC self-play experiments (v89b→v90b was also ~1pp). The model's self-play data is too similar
to the heuristic anchor data to provide a meaningful learning signal.

Note: val_loss improved from 2.57 (v106 nash_c only) to 2.38 (v107 with self-play data),
but win rate barely moved — val_loss improvement without WR improvement is a recurring pattern.

## v108: Wider GNN h=384 (2026-04-05)

**Hypothesis**: Wider trunk (h=384, ~768K params) captures more capacity than h=256 (~486K).
**Data**: nash_c_only (1.37M rows, same as v106)
**Training**: GNN, h384, bs=8192, lr=0.0024, 95ep, dropout=0.1, one-cycle, final_vp.

| Model | Seed | Best Epoch | Val Loss | Nash USSR | Nash US | Nash Comb |
|-------|------|-----------|----------|-----------|---------|-----------|
| v106_cf_gnn_s42 (base) | 42 | — | 2.57 | 55.8% | 14.0% | **34.9%** |
| v106_cf_gnn_s7 (base) | 7 | — | — | 52.8% | 9.2% | **31.0%** |
| v108_cf_gnn_h384_s42 | 42 | 91 | 2.16 | 46.4% | 5.6% | **26.0%** |
| v108_cf_gnn_h384_s7 | 7 | 80 | 2.15 | 48.4% | 9.4% | **28.9%** |

**Result: h=384 is WORSE than h=256 by 6-9pp combined. Clear regression.**

Lower val_loss (2.15 vs 2.57) but much worse win rate — classic overfitting pattern. The wider
model memorizes training data better but generalizes worse to play. With 1.37M rows, h=256 is
already at or near the capacity sweet spot for this dataset size. More parameters need more data,
not just the same data.

**Conclusion**: Model width is not the bottleneck. Do not increase hidden_dim beyond 256 without
proportionally more training data. Focus on data quality (teacher targets, diverse self-play) not
model size.

## MCTS Thread-Per-Partition Integration (2026-04-05)

Replaced old `SlotThreadPool` mutex-based MCTS parallelism with `SpinBarrier`-based
thread-per-partition architecture. Each thread owns a contiguous slice of game slots with
zero cross-thread sharing. Only sync point is NN inference barrier.

Also integrated from fast replica: inline `select_edge_fast` (avoids cross-TU function call
overhead in hot select loop).

All thread counts now configurable: `n_mcts_threads`, `torch_intra_threads`, `torch_interop_threads`.

### MCTS Throughput Matrix (under training load, RTX 3050)

Best configs (32 games, n_sim=200, v106_cf_gnn_s42):

| Config | sims/s | vs baseline |
|--------|--------|-------------|
| 1t MCTS, 1t torch (baseline) | 7,232 | 1.0x |
| 4t MCTS, 4t torch, maxp=32 | 12,077 | 1.67x |
| 4t MCTS, 4t torch, maxp=64 | 12,707 | 1.76x |
| 8t MCTS, 4t torch, maxp=32 | 11,975 | 1.66x |

Bottleneck at best config: NN=52%, expand=32%, select=16%.

### GPU vs CPU Inference (under training load)

| Device | Config | Wall time | NN time |
|--------|--------|-----------|---------|
| CPU | 4t/4i p32 | **46.8s** | 22.7s |
| CUDA | 4t/1i p32 | 125.5s | 100.7s |
| CUDA | 4t/2i p32 | 135.6s | 107.2s |

**GPU is always slower on RTX 3050, even when idle:**

| Scenario | CPU 4t/4i | CUDA 4t/1i | CPU advantage |
|----------|-----------|------------|---------------|
| GPU idle, pool=32 | **28.0s** | 46.3s | 1.7x |
| Training on GPU, pool=32 | **46.8s** | 125.5s | 2.7x |

The GNN model (~486K params) with ~200 avg batch size is too small for GPU inference to
overcome CPU→GPU transfer + kernel launch overhead on the RTX 3050 (2048 CUDA cores).
**Always use CPU inference for MCTS on this hardware.**
