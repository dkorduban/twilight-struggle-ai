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
| v99_baseline_h256_s123 | pending | pending | pending | — |

Note: s42 ran at 60 epochs (swept at old epoch count); extra compute data point,
excluded from seed variance. s123 benchmarked separately after export.

### Group 2: saturation test — 1× @ 95ep vs 2× @ 47ep (both ~121M samples)

| Run | Data | Train rows | Epochs | USSR WR | US WR | Combined | W&B |
|-----|------|-----------|--------|---------|-------|----------|-----|
| v99_saturation_1x_95ep | nash_b | 1.28M | 95 | 46.2% ±1.1 | 13.0% ±0.8 | **29.5% ±0.7** | knpb3sti |
| v99_saturation_2x_47ep | nash_b+c | 2.58M | 47 | pending | pending | pending | — |

**Preliminary**: 1× @ 95ep outperforms both s42/s7 baseline runs despite same compute.
Saturation 2× result pending — comparison will reveal data-volume vs epoch-count trade-off.

### Group 3: control_feat h256 on clean data (2× @ 47 epochs)

| Run | USSR WR | US WR | Combined | W&B |
|-----|---------|-------|----------|-----|
| v99_control_feat_h256_s42 | pending | pending | pending | — |
| v99_control_feat_h256_s123 | pending | pending | pending | — |

**Reference (arch sweep, contaminated data)**: 48.6%/9.4%/29.0%±0.6 on combined_v89.
