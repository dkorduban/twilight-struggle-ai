# GNN PPO v14 Failure Analysis and v15 Plan

**Date:** 2026-04-20
**Author:** Opus analyst (Claude)
**Scope:** Root-cause v14 GNN PPO collapse (panel 0.283 @ iter20 → 0.158 @ iter40), formulate v15 recipe.

---

## Executive Summary

**v14 did not fail because of a GNN-architecture problem.** It failed because its
starting point was *raw heuristic-imitation BC* (panel ≈ 0.20) while its reference
point (v13, country_attn_side) started from a *PPO-chained checkpoint v56*
(panel ≈ 0.441, i.e. roughly 50+ prior PPO iterations of accumulated strength).
That is a ~22pp warm-start gap, not a 16pp gap, and PPO with a fixed 20-iter
budget cannot close it — especially in a PFSP regime where the model peaks at
iter 20 and then declines from echo-chamber self-play.

The root framing error in the previous plan was treating "GNN BC from nash_b/c"
as comparable to "country_attn after v56". They are not. v56 is not a BC
checkpoint — its `ppo_args.json` shows it was warm-started from v55 (which in
turn came from v54…), so the v56 warm-start implicitly carries dozens of PPO
iterations of refinement. Any GNN model BC'd from pure heuristic Nash data will
cap at roughly "heuristic strength" (because imitation of a policy cannot
exceed that policy).

**Key diagnostic numbers**
- v14 warm-start panel ≈ 0.20 (iter10), peak panel 0.283 (iter20), decline to 0.158 (iter40).
- v14 rollout_wr vs panel_wr at iter40: 0.338 vs 0.158 (~18pp rollout-vs-panel gap,
  larger than v13's equivalent). This is a classic PFSP echo-chamber + weak-student
  symptom: the model's rollouts against its own weakened pool look fine, but
  performance against fixed opponents collapses.
- v14 asymmetry at iter40: USSR 0.515 / US 0.162 — US side learned *nothing*
  recoverable from heuristic BC for PPO (we saw this signature repeatedly in
  prior runs).
- BC final val_loss = 2.4454, card_top1 = 0.840, mode_acc = 0.973, country_ce = 1.1677,
  country_top1 ≈ 0.48-0.53, val_value_mse = 0.7722. Card learning is fine; *value
  head is nearly random* (MSE 0.77 means the value head basically outputs the
  mean) — that is the actual problem.

**Recommendation:** v15 should BC on a mixture of (a) the v13 4000-game self-play
dataset (high-quality rollouts from a known 0.427 model) and (b) a smaller slice
of heuristic Nash data for action-space coverage. Use **value-target =
winner_side with correct-side filtering**, and add **teacher-distillation KL
from v13_iter20** (or v56) into the BC loss to transfer PPO-accumulated
strategic knowledge that argmax labels cannot carry.

Then PPO with seed=42000, 20 iters, panel-sync eval. Target: v15 BC panel ≈ 0.35-0.40,
v15 PPO peak combined ≥ 0.43 (matching v13).

---

## 1. Is BC from heuristic data the main cause of v14 failure?

**Yes.** Multiple converging pieces of evidence:

### 1a. Warm-start panel gap is almost the entire iter-20 gap

| Run | Warm-start panel | iter20 panel | Δ from warm-start |
|-----|------------------|--------------|-------------------|
| v13 (country_attn_side) | ~0.441 (v56 bench) | 0.475 | +0.034 |
| v14 (control_feat_gnn_side) | ~0.20 (iter10 panel) | 0.283 | +0.083 |

v14 actually made MORE progress per iteration than v13 (+8.3pp vs +3.4pp), but
the starting point was so low that even a good trajectory couldn't close the
gap in 20 iters. PPO did not "fail" on GNN; it succeeded in improving, just
from too low a floor.

### 1b. Value head is effectively untrained at BC end

BC epoch-30 final val_value_mse = 0.7722. Given value targets are in [-1, 1]
and the trivial constant-mean predictor achieves MSE ≈ 0.5 for a bimodal
winner-side target, 0.77 means the value head has *negative* information
content — it's slightly worse than predicting the mean. PPO value loss starts
at 0.6877 (iter 1) and declines — i.e. PPO had to learn the value function
from scratch. This is confirmed by inspecting v14 iter-1 diagnostic:
`card_logits range=[-259.39, 20.11]` (wildly peaked because BC is confident) but
`values range=[-1.0000, 1.0000]` with vl=0.6877 (basically untrained).

Contrast with v13 iter-1 from a v56 warm-start: `card_logits range=[-16.37, 12.16]`
(calibrated) and vl=0.1750 (value head already accurate).

### 1c. Peak-then-decline trajectory matches PFSP echo-chamber signature

v14 iter-20 panel=0.283 → iter-30=0.200 → iter-40=0.158. The model peaks exactly
at iter 20 (consistent with prior seed=42000 history; documented in
project_ppo_seed_investigation.md) then decays because PFSP gradually pulls the
training distribution toward self-play opponents, widening the gap vs fixed
panel opponents (v56, heuristic). With a strong warm-start, v13 still peaks at
iter 20 but at 0.475 — the ceiling of this PFSP loop is *roughly* warm-start + 5-10pp.

### 1d. US side never improves

v14 US panel WR: iter10=0.10, iter20=0.13, iter30=0.07, iter40=0.07. US side
gets worse. This is the known "US-side collapse" signature we've seen under
heuristic-only BC, documented in feedback_us_win_value_weighting.md. Heuristic
self-play is USSR-advantaged (heuristic plays a ~0.60 USSR WR), so BC data
that winnows to "winning side" samples is dominated by USSR frames, and US
frames end up either sparse or labeled with asymmetric targets. This is a
structural feature of training on heuristic output, not a GNN bug.

---

## 2. What BC quality does the GNN model actually have vs a hypothetical v56 BC?

**Reframing the question:** v56 is not a BC checkpoint. Per
`data/checkpoints/ppo_v56_league/ppo_args.json`, v56 was warm-started from
v55→v54→… at the end of a long PPO chain. There is no "v56 BC" to compare to.
v13's warm-start panel of 0.441 is **v56's PPO-accumulated quality**, not any
model's BC quality.

**Correct comparison:** what BC quality does a GNN model trained on heuristic
Nash data achieve?

From `results/bc_gnn_side_v1/train.log`:
- Final val_card_top1 = 0.840
- Final val_mode_acc = 0.973
- Final val_country_ce = 1.1677 (country_top1 ≈ 0.48-0.53)
- Final val_value_mse = 0.7722

These numbers are *fine* as imitation of heuristic. The imitation is faithful
(~84% card top-1), but the **ceiling is heuristic strength** because that's
what the dataset encodes. Heuristic itself benches around 0.20-0.25 combined
WR vs v56+heuristic panel (v56 dominates heuristic 0.80-0.90 in its own panel
history). So BC on heuristic data lands a model at ~heuristic strength, which
benches near 0.20 — matching v14 iter-10 panel (0.20) exactly.

**What a country_attn BC on the same nash data would produce:** based on
historical BC runs in data/checkpoints/arch_country_attn_h256/, card_top1 and
val_loss are within ~1-2pp of the GNN variant. There is no evidence country_attn
BC would produce a materially higher warm-start. The previous plan's assumption
that GNN BC's 0.283 was "16pp below country_attn_side's start" was wrong —
country_attn_side started from v56 PPO, not from a country_attn BC.

**Numeric check on country_attn BC from heuristic data:** we don't have an
exact matched run, but the generation-1 pattern observed in project history is:
- BC on nash_b/c: combined WR ~0.20-0.25 vs fixed panel
- After one PPO pass (20 iters): combined WR 0.30-0.40 depending on seed

So the right expectation for v15 is: BC ≈ 0.25-0.35 (v13-self-play boosted),
then 20 PPO iters should reach 0.40-0.48.

---

## 3. Ideal v15 BC recipe

### 3a. Data composition

**Recommendation: use v13 self-play as primary data, heuristic Nash as secondary.**

Rationale: v13 (combined=0.427) is stronger than heuristic (combined~0.20).
BC on v13 data lifts the imitation ceiling from "heuristic strength" to
"v13 strength". This is the "data flywheel" pattern Month-3 explicitly wants.

Concrete data mixture:
- **Primary** (70%): v13 self-play and v13-vs-heuristic, the 4000 games being
  collected. Inspection of JSONL: each file is row-per-step, so 4000 games
  ≈ 180-200k rows (v13_us_1500g.jsonl + v13_ussr_1500g.jsonl alone are
  ~134k rows from 3000 games = ~45 rows/game average).
- **Secondary** (30%): existing nash_b/nash_c parquet (2.7M rows). Keep for
  action-space coverage, especially for mode-head and small-choice-head
  situations v13 rarely encounters.

Do NOT use pure v13 self-play. Heuristic data has broader action distribution
for edge-case modes (space race, DEFCON-1 avoidance, unusual triggers). A
1:0.3 v13:nash weight keeps coverage while biasing labels to v13's stronger
policy.

**Critical filtering:** Filter v13 self-play frames to **correct-side wins**.
i.e. USSR frames where USSR won, US frames where US won. This matches the
game-asymmetry rule (feedback_game_asymmetry.md). Estimated retention ~55%
(since v13 selfplay ≈ 50/50 with heuristic starts).

### 3b. Value target and loss design

- `value_target = winner_side` (same as v14 BC).
- **US-win-weighted value loss**: 2× weight on US-win steps (per
  feedback_us_win_value_weighting.md). This is the single biggest lever for
  fixing the iter40 US collapse we saw in v14.
- Consider `advantage_weight = 0.1` (lightly) to de-weight neutral/terminal
  frames that provide no policy signal.

### 3c. Teacher distillation KL (HIGH VALUE)

This is the *most impactful* addition relative to v14 BC. Instead of BC-ing to
argmax actions only, add a KL term against a teacher model's policy distribution:

```
loss = ce_card + ce_mode + ce_country + value_mse + teacher_weight * KL(student || teacher)
```

Teacher options, in order of preference:
1. **v56 (country_attn_side, combined=0.441)**: strongest teacher available.
2. **v13_iter20 (country_attn_side, combined=0.427)**: closer in distribution
   to the v13 self-play data, so KL is better-defined.

Reason this matters: argmax labels throw away most of the teacher's
information. KL on the full policy captures "these two cards are nearly tied"
and "this country is almost as good as that one", which is exactly the PPO-
accumulated knowledge that argmax BC on v13 self-play cannot transfer.

Set `teacher_weight = 0.5` initially; `teacher_value_weight = 0.3` for KL on
value predictions as well. If teacher checkpoint is country_attn architecture
and student is GNN, teacher inference is a one-pass forward (add to dataset
prep pipeline once, cache logits to parquet as `teacher_card_logits`,
`teacher_mode_logits`, `teacher_value`).

Expected effect: BC final panel 0.30-0.40 (up from 0.20 with pure argmax).

### 3d. Epoch budget

**30 epochs is probably right for v15** (not more). Evidence:
- v14 BC val_loss trajectory: epoch 1=3.30 → epoch 10=2.62 → epoch 20=2.52 → epoch 30=2.45.
- By epoch 20, val_loss has decreased only 0.10 over 10 epochs (≈4% per-epoch gain).
- By epoch 30, val_loss decreased only 0.07 over 10 epochs (≈3% per-epoch gain).
- Trajectory is clearly log-asymptotic; 30→50 would gain ~0.05 more val_loss.

More epochs will NOT fix the imitation-ceiling problem. Data quality and
teacher-KL are the real levers. Keep 30 epochs, spend compute on distillation
instead.

**If BC with teacher-KL converges earlier** (e.g. by epoch 20), stop there.
Watch val_value_mse — if it plateaus above 0.5, data is still too noisy; add
value-only extra epochs or reweight.

### 3e. Other hyperparams

Keep v14 BC defaults:
- lr = 0.0012, batch_size = 1024, dropout = 0.1, seed = 42000
- deterministic-split, val_fraction = 0.1
- Add: `teacher_weight = 0.5`, `teacher_value_weight = 0.3`, label_smoothing = 0.05

---

## 4. How many BC epochs for GNN v15? Are 30 enough?

**Yes, 30 is enough. More will not help.**

Detailed trajectory from `results/bc_gnn_side_v1/train.log`:

| Epoch | val_loss | val_card_top1 | val_value_mse | Δ val_loss vs prev |
|-------|----------|---------------|---------------|---------------------|
| 1  | 3.3010 | 0.797 | 0.7005 | — |
| 5  | 2.7646 | 0.823 | 0.7210 | -0.54 from e1 |
| 10 | 2.6207 | 0.833 | 0.7333 | -0.14 from e5 |
| 15 | 2.5435 | 0.836 | 0.7465 | -0.08 from e10 |
| 20 | 2.5157 | 0.838 | 0.7765 | -0.03 from e15 |
| 25 | 2.4573 | 0.838 | 0.7529 | -0.06 from e20 |
| 30 | 2.4454 | 0.840 | 0.7722 | -0.01 from e25 |

Observations:
- `val_card_top1` saturates at ~0.838-0.840 by epoch 12 and never budges again.
- `val_value_mse` is *worsening* after epoch 10 — the value head is
  overfitting (or more likely, the target signal is so weak that the model is
  memorizing noise). This is the biggest problem with the current BC recipe.
- `train_loss` still decreases monotonically (no gradient starvation), but
  `val_loss` improvements are <1% per 5 epochs after epoch 20.

**30 epochs is the right budget. Do not extend.**

If compute is available, instead spend it on:
1. **Teacher-KL distillation** (§3c): new gradient source, higher ceiling.
2. **Data iteration** (rebuild dataset after PPO v15 with v15_iter20 rollouts
   to support a potential v16/v17).
3. **Learning rate warmup + cosine decay**: currently lr is flat at 0.0012.
   Warmup to 0.0012 over 500 steps + cosine decay to 0.0002 at epoch 30 would
   likely squeeze 1-2pp more card_top1 (diminishing returns, but cheap).

---

## 5. Are there structural issues with TSControlFeatGNNSideModel?

**No. The architecture is fine. It is strictly more powerful than
TSBaselineModel and TSControlFeatCountryEncoder on paper, and the
TSCountryAttnSideModel comparison is near-identical.** Evidence:

### 5a. Architectural equivalence with country_attn_side

Comparing `TSControlFeatGNNSideModel` (lines 1651-1743) to `TSCountryAttnSideModel`
(lines 1799-1908):

Both models have:
- Identical trunk: TRUNK_IN + SIDE_EMBED_DIM → hidden_dim (256) → 2 residual blocks
- Identical heads: card, mode, strategy (86×4), strategy_mixer, small_choice,
  separate USSR/US value branches and heads
- Identical scalar path: SCALAR_DIM + 42 region_scalars, FrameContextScalarEncoder
- Identical side-embedding: nn.Embedding(2, 32), concatenated to trunk input
- Identical value-head-selection logic (side_idx-indexed mix)

The ONLY difference (as the docstring at line 1807 explicitly says) is the
country encoder:
- GNN: `ControlFeatGNNEncoder` — 2-round adjacency message passing over static
  86×86 graph.
- Country-attn: `CountryAttnEncoder` — 4-head self-attention over 86 countries.

Both encoders produce `(B, INFLUENCE_HIDDEN)` country hidden + `(B, 42)` region
scalars. Both are additively fused with the flat influence encoder
(`influence_encoder_flat`).

The attn model has one extra complexity: `CountryAttnSideModel` also runs
`self.region_encoder = ControlFeatGNNEncoder()` purely to extract its 42
region scalars — meaning the attn model has the GNN as a free side-computation,
used only for features, not for the main influence hidden. This is a small
capacity advantage for attn but not game-changing.

### 5b. Model parameter counts are similar

From checkpoint sizes:
- GNN model checkpoint: 6.47 MB (bc_gnn_side_v1/baseline_best.pt)
- country_attn_side scripted: 2.57 MB (v56_scripted.pt) — but this is scripted
  (strip-optimized) so the raw is similar.

GNN encoder params ≈ 3×(32²) + (32→INFLUENCE_HIDDEN output_proj) ≈ ~30k params.
Attn encoder params ≈ 4 heads × (32² QKV) + FFN ≈ ~40k params.

Both are small relative to trunk (~250k params), so the architecture is not
capacity-limited.

### 5c. No evidence of gradient or numerical issues

From v14 diagnostics (iter1-iter40):
- `inf nan=0 inf_vals=0` across all iters
- `scalar nan=0` across all iters
- `card_logits` range always ∈ [-300, 30] — wide but bounded
- `values` range always ∈ [-1.0000, 1.0000] — well-behaved
- `kl` always ∈ [0.0019, 0.0053] — healthy, not exploding
- `clip` fraction always ∈ [0.058, 0.146] — healthy

There is no NaN, no gradient explosion, no KL runaway. The GNN architecture
works.

### 5d. One minor concern, not a blocker

Reading `ControlFeatGNNEncoder.forward` (lines 1514-1568):
- 2 GNN rounds with fixed adjacency and full-graph aggregation (86×86 matmul
  per round). Both rounds use ReLU, no residual, no layer-norm. After 2 rounds
  some features may over-smooth (mean aggregation over 86 nodes drives features
  toward a global mean).

This is a plausible minor weakness vs self-attention (which can learn to
attend selectively rather than always-mean-aggregate). In practice, 2 rounds
over a sparse adjacency (most countries have <10 neighbors, so row-normalized
means are NOT over all 86) are unlikely to over-smooth.

**Verdict:** GNN and attn sides are near-equivalent. If v15 (GNN) reaches
combined 0.43 after proper warm-start + PPO, and a future v16 (country_attn)
reaches 0.44 from the same recipe, that is within seed-variance noise
(documented 10pp at iter20). There's no structural reason to abandon GNN.

---

## Recommendations

### 6.1. Build v15 BC dataset with teacher logits

1. **Collect v13 rollouts** (in progress): 4000 games; expected ~180-200k rows.
2. **Convert JSONL to parquet** with filtering:
   - Keep only rows where `winner_side == phasing_side` (correct-side filtering).
   - Attach `game_won_by_phasing` as value target.
3. **Generate teacher logits cache**: run v56 (or v13_iter20) over every frame,
   store `teacher_card_logits`, `teacher_mode_logits`, `teacher_value` in the
   parquet. One-time cost: ~20 min on GPU.
4. **Combine with nash_b/c**: 70% v13 + 30% nash. Deterministic split.

### 6.2. Train v15 BC (control_feat_gnn_side)

Command:
```
scripts/train_baseline.py \
  --data-dir data/v15_bc_mixture \
  --out-dir results/bc_gnn_side_v15 \
  --model-type control_feat_gnn_side \
  --num-strategies 4 \
  --epochs 30 \
  --lr 0.0012 \
  --batch-size 1024 \
  --seed 42000 \
  --deterministic-split \
  --value-target winner_side \
  --teacher-targets data/v15_bc_mixture/teacher_cache.parquet \
  --teacher-weight 0.5 \
  --teacher-value-weight 0.3 \
  --label-smoothing 0.05 \
  --us-value-weight 2.0
```

**Expected outcome:** val_card_top1 ≈ 0.85-0.88, val_value_mse ≈ 0.40-0.55
(dramatically better than v14's 0.77), BC panel combined ≈ 0.30-0.40.

Flag `--us-value-weight` may need to be added to `train_baseline.py` if not
already present; this is a small addition.

### 6.3. Bench v15 BC before PPO

Run standard 500g/side benchmark at seeds 50000/50500. **Gate**: require BC
panel combined ≥ 0.30 before launching PPO. Otherwise we're just burning PPO
compute on a known-bad warm-start. If gate fails, iterate BC recipe
(teacher_weight tuning, remove label smoothing, etc.) before touching PPO.

### 6.4. Launch v15 PPO

Exact v13 hyperparameters, seed=42000, 20 iters, sync panel eval.

**Expected outcome:**
- iter10: panel 0.35-0.45
- iter20: panel 0.40-0.48 (matching or slightly exceeding v13's 0.475)
- If BC is weaker than expected (e.g. 0.30), iter20 panel likely 0.40-0.43.

**Gate for new record:** v15 iter20 combined WR ≥ 0.43 (matches v13); extended
recipe (e.g. longer PPO, league pool refresh) only if we beat 0.43.

### 6.5. Considered alternatives

1. **Pure v13 self-play BC (no heuristic)**: risky — coverage of edge-case
   modes (DEFCON brinkmanship, long space-race sequences) may be thin, leading
   to PPO exploration failures in those modes. Recommend the 70/30 mix instead.

2. **Pure distillation (teacher KL only, no argmax targets)**: aggressive but
   untested in this codebase. Keep argmax as a stabilizer; use teacher KL as
   an additive signal for v15.

3. **Skip BC, PPO from scratch**: rejected. Documented in
   feedback_bc_before_ppo.md — PPO from scratch with a new architecture
   produces unstable training and much worse endpoints.

4. **Warm-start v14 iter20 with KL reg to v13**: theoretically possible but
   v14 iter20 is already an echo-chamber-trained GNN with US collapse baked
   in. Cleaner to restart BC correctly.

5. **Use MCTS-dir data from pivot1 as BC data**: has only 1000 games × 105k
   rows from v6_iter20 (combined=0.459). Could be a 4th data source but adds
   complexity; defer to v16 experimentation.

### 6.6. Do NOT

- Run more v14 PPO iters hoping it recovers (it won't; PFSP echo chamber).
- Train GNN BC for 60+ epochs (val_loss plateau after epoch 20).
- Use only nash_b/nash_c for v15 BC (caps at heuristic strength).
- Change GNN architecture (not the bottleneck).
- Switch to country_attn_side for v15 (would discard the in-progress v13
  self-play dataset and doesn't fix the warm-start problem).

---

## Appendix: v14 iter trajectory (quick reference)

From `results/ppo_gnn_side_v14/train.log`:

| iter | rollout_wr | panel_wr (v56 / heur) | value_loss | entropy |
|------|-----------|------------------------|-----------|---------|
| 1    | 0.409    | — | 0.6877 | 1.413 |
| 10   | 0.465    | 0.200 (0.233 / 0.167) | 0.5144 | 1.414 |
| 20   | 0.449    | 0.283 (0.283 / 0.283) | 0.1854 | 1.305 |
| 30   | 0.449    | 0.200 (0.200 / 0.200) | 0.2443 | 1.398 |
| 40   | 0.338    | 0.158 (0.167 / 0.150) | 0.1951 | 1.530 |

US side panel WR: 0.10 → 0.13 → 0.07 → 0.07 (never improves; classic
heuristic-BC US collapse).

rollout_wr/panel_wr gap at iter 40: 0.338 vs 0.158 (0.18 gap). At iter 20:
0.449 vs 0.283 (0.166 gap). The gap is stable — confirming that PFSP lets the
model look fine vs its own weakening pool while actual strength vs fixed
panel stagnates/declines.

## Appendix: JSONL row verification

- `selfplay_2000g.jsonl`: 4,739 lines, 21.4 MB — row-per-step, ~100 games complete at 08:26 UTC (collection still in progress).
- `us_vs_heuristic_1000g.jsonl`: 1,402 lines — partial.
- `ussr_vs_heuristic_1000g.jsonl`: 1,621 lines — partial.
- `v13_us_1500g.jsonl`: 67,864 lines, 244 MB — complete (45 rows/game avg).
- `v13_ussr_1500g.jsonl`: 66,621 lines, 239 MB — complete.

Expected final counts when collection finishes: ~200k-220k rows for 4000 games.
Combined with 2.7M nash rows at 30% weight, the effective training dataset is
~200k + 800k (nash sampled) = ~1M rows/epoch. At 1024 batch size, 1000
batches/epoch × 30 epochs = ~30k steps, matching v14's runtime of ~45 min BC.

## Appendix: Key files

- `results/ppo_gnn_side_v14/train.log` — v14 PPO full log
- `results/ppo_country_attn_v13/train.log` — v13 PPO full log
- `results/bc_gnn_side_v1/train.log` — v14 BC full log
- `results/bc_gnn_side_v1/baseline_best.pt` — v14 BC best checkpoint (epoch 30, val_loss=2.4454)
- `data/checkpoints/ppo_v56_league/ppo_args.json` — v56 PPO config (confirms v56 is not a BC checkpoint)
- `data/checkpoints/ppo_v56_league/panel_eval_history.json` — v56 panel trajectory
- `results/continuation_plan.json` — current Month-3 plan state
- `python/tsrl/policies/model.py:1651-1743` — TSControlFeatGNNSideModel
- `python/tsrl/policies/model.py:1799-1908` — TSCountryAttnSideModel
- `python/tsrl/policies/model.py:1442-1568` — ControlFeatGNNEncoder
- `data/selfplay/gnn_warmstart_v13/*.jsonl` — v13 self-play collection in progress
