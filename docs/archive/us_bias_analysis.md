# US Side Bias Analysis and Experiment Plan

Date: 2026-04-03
Status: Active investigation

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Root Cause Analysis](#root-cause-analysis)
3. [Why Pure BC Cannot Fix US Play](#why-pure-bc-cannot-fix-us-play)
4. [Assessment of Current Experiment Plan](#assessment-of-current-experiment-plan)
5. [Candidate Interventions](#candidate-interventions)
6. [MCTS as a Path Forward](#mcts-as-a-path-forward)
7. [Prioritized Experiment Plan](#prioritized-experiment-plan)
8. [Success Criteria and Targets](#success-criteria-and-targets)
9. [Risk Analysis](#risk-analysis)
10. [Appendix: Data and Configuration Reference](#appendix)

---

## 1. Executive Summary

Our best BC model (saturation_1x_95ep) achieves 46.2% USSR WR but only 13.0%
US WR against the heuristic, for a combined 29.5%. The heuristic itself achieves
~35% US WR against itself. This means our model is **22 percentage points worse
than its own training data source** when playing as US, while being
**11 percentage points better** than the heuristic's ~35% when playing as USSR
(the heuristic gets ~65% as USSR, our model gets 46.2% — but against the
heuristic, not against itself).

The US deficit is the single largest opportunity for improvement. Raising US WR
from 13% to 25% would increase combined WR from 29.5% to 35.6% — a gain
equivalent to everything we have achieved so far from BC.

This document analyzes why the deficit exists, evaluates candidate fixes, and
proposes a concrete prioritized experiment plan.

---

## 2. Root Cause Analysis

The US WR deficit has **multiple reinforcing causes**, not a single root cause.

### 2a. Data imbalance: USSR actions dominate the training set

The heuristic has a 65:35 USSR:US win ratio. Because the game alternates turns
(USSR and US each take actions every action round), both sides contribute
roughly equal numbers of decision rows. However, the **value targets** are
skewed:

- ~62.6% of rows have winner_side = +1 (USSR win)
- ~35.1% of rows have winner_side = -1 (US win)
- ~2.3% draws

When using `final_vp/20` as the value target, there is a continuous bias toward
positive values (USSR-favorable outcomes). The value head learns that most
positions are USSR-favorable, which is **correct for the heuristic's play** but
not for optimal play.

**Impact on policy**: The model's policy head learns both USSR and US actions
from the same games. But the USSR actions in these games are the actions of the
**winning side** 62.6% of the time, while US actions are from the winning side
only 35.1% of the time. The model implicitly learns that USSR-style actions
are "good" (correlated with winning) and US-style actions are "bad" (correlated
with losing).

### 2b. Asymmetric task difficulty

US play in Twilight Struggle is **strategically more demanding** than USSR play
in the early-mid game:

- USSR has initiative advantage: DEFCON favors early USSR coups (USSR goes
  first in ARs 1-3, DEFCON drops from 5 to 2 in early turns)
- US must play reactively in turns 1-3: counter USSR coups, manage DEFCON,
  protect Europe, while holding opponent cards
- US card pool in early war is weaker: more USSR events in the early war deck
- US relies more on long-term positional play: influence placement for scoring
  cards, preventing domination

This means US play has a higher branching factor of "reasonable" moves and
requires more look-ahead to evaluate. A pure imitation learner needs to see
more US-winning examples to learn the subtle patterns, but the data has fewer
of them.

### 2c. Value head miscalibration poisons US policy (the key mechanism)

This is the most important and most actionable cause.

The value head, trained on heuristic games, learns V(s) that is systematically
USSR-biased. When the model plays as US:

1. The value head evaluates US positions as worse than they actually are
2. If advantage-weighting is used (v96b experiment), US actions get
   **downweighted** because the model thinks US positions are bad
3. Even without advantage-weighting, the biased value head means the model
   does not properly learn which US actions lead to better outcomes — they
   all look like they lead to losses

The v96b experiment confirmed this directly: adding advantage-weighting
(alpha=0.5) caused US WR to **drop from ~9% to 5.7%**. The advantage weights
correctly identified that US positions have negative residuals (value_target <
value_pred for US... wait, actually value_target is worse than value_pred
because the model is predicting USSR-favorable values and US games often
lose). This caused US-side training examples to be downweighted, making the
model even worse at US play.

### 2d. No side-conditional policy learning

The model uses a single policy head for both sides. The `phasing` scalar (0 for
USSR, 1 for US) is the only signal telling the model which side is acting. This
is a single scalar buried in an 11-dimensional input, competing with VP, DEFCON,
turn number, etc.

The model must use this one scalar to modulate its entire policy. In practice,
with a 256-hidden MLP trunk, the model likely learns a weak "side offset" but
cannot learn fundamentally different strategies for each side.

### 2e. Heuristic US play is mediocre (floor effect)

The heuristic achieves ~35% US WR against itself. This means the BC training
target for US play is already a weak policy. Even perfect imitation of the
heuristic's US play would only yield ~35% US WR. Our model achieves 13%,
which means it is imitating the heuristic's US play poorly.

Why? Because:
- The heuristic's US mistakes and the heuristic's US successes look similar in
  the raw action data — the model cannot distinguish "this US influence
  placement led to winning" from "this US influence placement was futile"
  without good value signal
- The value signal is biased (see 2c above)
- The model averages over all US actions (winning and losing games), learning
  a blended policy that is worse than the heuristic's deterministic play

### Summary of causes (ranked by impact)

| Cause | Impact | Fixability |
|-------|--------|------------|
| Value head miscalibration | High | Medium — needs de-biased value targets |
| No side-conditional learning | Medium-High | Easy — add side embedding or separate heads |
| Data imbalance (outcome distribution) | Medium | Easy — reweight or stratify |
| Heuristic US play is weak | Medium | Hard — need non-BC data source |
| Asymmetric task difficulty | Low (structural) | Cannot fix, must accommodate |

---

## 3. Why Pure BC Cannot Fix US Play

We have established empirically (Phase 1 investigation) that:

1. **More data from the same heuristic does not help.** saturation_2x_47ep
   (26.9%) did not beat saturation_1x_95ep (29.5%). The heuristic's US play
   has a fixed ceiling.

2. **Self-play from BC models is circular.** The BC model learned the
   heuristic's policy, so its self-play data is near-duplicate of heuristic
   data. v91 and v92 showed no improvement.

3. **Advantage weighting hurts US.** The biased value head makes advantage
   weights penalize US actions (v96b: US WR 5.7% vs 9%).

4. **The BC objective has no mechanism to discover better US play.** BC
   minimizes KL divergence to the heuristic policy. Even if the model perfectly
   clones the heuristic, US WR maxes out at ~35%, and in practice it will be
   lower due to averaging effects.

**Theoretical US WR ceiling from pure BC:**
- Perfect heuristic cloning: ~35% (heuristic's own US WR)
- Realistic BC with current architecture: ~15-20% (accounting for approximation
  error, value head bias, averaging over winning/losing games)
- Current best: 13%

There is maybe 5-7pp of headroom in pure BC by fixing the value calibration
and side-conditioning. Beyond that requires non-BC signal.

---

## 4. Assessment of Current Experiment Plan

The planned follow-up sweep (control_feat x 3 seeds, epoch ceiling, 2x@95ep)
**does not address the US bias at all**. Specifically:

| Planned experiment | Addresses US bias? | Expected US WR gain |
|---|---|---|
| control_feat x 3 seeds | No — measures seed variance | 0pp (diagnostic only) |
| control_feat 1x@95ep | Marginal — more epochs might help slightly | 0-2pp |
| 2x@95ep (4× compute) | No — already shown more data doesn't help | 0pp |

**Recommendation: Do not run the remaining pure BC experiments.** They are
useful for understanding seed variance and architecture sensitivity, but they
will not move US WR. The 3-seed control_feat experiment is worth finishing
only if it is already in progress, as a data point for the architecture
decision.

The priority should shift to interventions that directly target the US bias.

---

## 5. Candidate Interventions

### 5a. Side-conditional value de-biasing (HIGHEST PRIORITY)

**Theory**: The value target should not be the raw game outcome. It should be
calibrated per-side so that the value head learns "how good is this position
for the acting side" rather than "USSR usually wins."

**Concrete implementation**: Center value targets by side.

Currently:
```
value_target = final_vp / 20  (range approximately -1 to +1)
```

This means USSR-side rows get value targets that are positive ~63% of the time,
and US-side rows get value targets that are negative ~63% of the time. The
value head learns V(s) ≈ +0.25 on average (USSR-biased).

Fix: Use a **side-relative value target**.

Option A — Zero-centered per-side:
```python
# For USSR rows: value_target = final_vp / 20 (unchanged, USSR prefers positive)
# For US rows:   value_target = -final_vp / 20 (flip sign: US prefers negative VP)
```
This makes the value head predict "how good for the acting side" on a [-1, +1]
scale. Both sides' good outcomes map to +1 and bad outcomes to -1.

Option B — Side-centered with empirical bias correction:
```python
# Compute empirical mean value per side from training data:
#   mean_ussr_value ≈ +0.25
#   mean_us_value ≈ -0.25
# Subtract side-specific mean:
#   value_target_ussr = final_vp / 20 - mean_ussr_value
#   value_target_us = final_vp / 20 - mean_us_value
```

Option A is simpler and more principled. **Recommend Option A.**

Note: this requires corresponding changes at inference time. When the model
evaluates a position as US, the value output represents "probability of US
winning" (positive = good for US). The benchmark and MCTS code must flip the
sign when converting to USSR-perspective values.

**Implementation effort**: Small. Changes in dataset.py and train_baseline.py.
One new flag `--value-perspective actor` (default: `ussr` for backward compat).

### 5b. Side embedding / side-gated trunk (HIGH PRIORITY)

**Theory**: The model needs stronger side-conditioning than a single scalar in
the 11-dim input. A side embedding or gating mechanism lets the trunk learn
fundamentally different representations for each side.

**Concrete implementations (pick one)**:

Option 1 — Side embedding concatenated to trunk input:
```python
side_embed = self.side_embedding(phasing_int)  # (B, 32)
trunk_input = torch.cat([influence_hidden, card_hidden, scalar_hidden, side_embed], dim=-1)
```
Adds 32 parameters to the trunk input. Cheap, easy to test.

Option 2 — Side-gated trunk (FiLM-style):
```python
gamma = self.side_gamma(phasing_int)  # (B, trunk_hidden)
beta = self.side_beta(phasing_int)    # (B, trunk_hidden)
trunk_out = gamma * trunk_out + beta
```
Lets the side modulate every trunk neuron multiplicatively. More expressive but
slightly more complex.

Option 3 — Separate value heads per side:
```python
if phasing == 0:
    value = self.value_head_ussr(trunk)
else:
    value = self.value_head_us(trunk)
```
Does not help the policy heads but isolates value calibration per side.
Lightweight and easy to test.

**Recommendation**: Start with Option 1 (side embedding) + Option 3 (separate
value heads). If insufficient, try Option 2.

**Implementation effort**: Small. New model variant `TSSideCondModel` or
modify existing model with a flag.

### 5c. US-weighted training (MEDIUM PRIORITY)

**Theory**: Upweight US-side rows in the loss function to compensate for
outcome imbalance.

**Concrete implementation**:
```python
# In training loop:
side_weight = torch.where(phasing == 1, us_weight_multiplier, 1.0)
loss = (side_weight * per_row_loss).mean()
```

Hyperparameter to sweep: `us_weight_multiplier` in {1.5, 2.0, 3.0}.

At 2.0, US rows contribute 2x to the loss, roughly compensating for the
62:35 outcome imbalance (making effective contribution more balanced).

**Implementation effort**: Tiny. One line in train_baseline.py.

**Risk**: May hurt USSR WR if US weight is too high. The combined WR matters.

### 5d. US-winning-only value targets (MEDIUM PRIORITY)

**Theory**: For US-side training rows, only use value targets from games where
US won. This gives the value head examples of "what US-winning positions look
like" without the noise of US-losing positions.

**Concrete implementation**: Filter US-side rows where winner_side != -1 out of
the value loss (but keep them for policy loss). Or, more aggressively, filter
US-side losing rows entirely.

We already do wins-only filtering for self-play data. The question is whether
to apply it to heuristic data.

**Risk**: Removes ~65% of US-side rows from value training. May make the value
head overfit to the remaining 35%.

**Recommendation**: Try as a secondary experiment after 5a and 5b.

### 5e. MCTS at inference time (HIGH PRIORITY, see Section 6)

**Theory**: Even with a biased policy and value, tree search can improve play
by looking ahead. The policy prior from BC is decent for move ordering; the
value head, even if biased, provides some ranking signal among positions. MCTS
amplifies whatever signal exists.

ISMCTS is already implemented in C++. The question is configuration.

### 5f. Generating US-side teacher targets with MCTS (MEDIUM-HIGH PRIORITY)

**Theory**: Run MCTS from US positions in the training data. Use the improved
policy (visit counts) as teacher targets for the BC model. This is a form of
"search-then-distill" that specifically targets US play quality.

**Concrete implementation**:
1. Sample US-side positions from the training set (e.g., 50k positions)
2. Run ISMCTS with 8 determinizations x 200 sims per position
3. Extract visit-count policy targets and root value estimates
4. Add these as teacher targets in training

The existing teacher_search.py infrastructure supports this workflow.

**Implementation effort**: Medium. Need to run teacher search on US positions
specifically, which requires a position selection script.

**Risk**: Biased MCTS may reinforce bias (see heuristic-imbalance.md). However,
because we are using the BC model's own policy as the prior (not the raw
heuristic), and because we average over 8 determinizations, the bias is
somewhat mitigated. The key insight from the design doc applies: trust the
**relative action ranking** from search, not the absolute value.

### 5g. Side-swap data augmentation (LOW PRIORITY)

**Theory**: Twilight Struggle is not symmetric — you cannot swap sides on the
board. But you can try a softer version: for each US-winning game, the model
has seen the "successful" US actions. Weight these more heavily. This is
essentially what 5c and 5d do.

True side-swap (mirror the board to create synthetic USSR/US data) is not
possible in TS due to asymmetric card effects, DEFCON rules, and country
importance.

**Recommendation**: Skip this. The per-side weighting (5c) achieves the same
goal more directly.

### 5h. Residual value learning: learn delta over heuristic (LONG-TERM)

**Theory**: From the heuristic-imbalance doc — model predicts V(s) = H(s) +
delta(s), where H(s) is the heuristic's evaluation. The model only needs to
learn where the heuristic is wrong.

**Why not now**: We don't have a continuous heuristic value function H(s).
The heuristic is a policy (action-selection rule), not an evaluator. Building
a heuristic value function requires either (a) rollout estimates, which are
slow and biased, or (b) a separate evaluation function, which doesn't exist.

**Recommendation**: Defer to Month 3 Phase 2, after MCTS provides better value
estimates that can serve as H(s).

---

## 6. MCTS as a Path Forward

### The bias problem with MCTS

From heuristic-imbalance.md: "if your rollout / default policy is the same
heuristic that already has a built-in USSR skew, then plain MCTS values are
not ground truth."

However, our ISMCTS setup is different from naive rollout MCTS:

1. **We use the learned model as the policy prior**, not the raw heuristic.
   The model provides action probabilities at each node, which are used for
   PUCT selection. The heuristic is only the opponent during benchmarking.

2. **We use the learned value head for leaf evaluation**, not rollout-to-
   terminal. This avoids compounding bias through long rollouts.

3. **Determinization averages over hidden information**, which adds diversity
   to the search.

The remaining bias is in the value head (which is USSR-biased, as analyzed in
Section 2c). This means MCTS leaf evaluations are biased, and the search
tree's backed-up values are biased.

### How to mitigate MCTS bias for US play

**Key insight**: MCTS with PUCT doesn't need accurate absolute values — it
needs accurate **relative values** between sibling actions. Even a biased value
head can rank actions correctly if the bias is roughly constant across siblings
at the same node.

For US play specifically:

1. **Side-relative value** (intervention 5a) is critical before using MCTS.
   If the value head predicts "value for acting side" rather than "value for
   USSR," then US-side leaf evaluations are directly useful for US action
   selection.

2. **More simulations help US more than USSR.** USSR play is simpler (aggression
   pays off); US play requires more look-ahead to evaluate positional
   consequences. More MCTS simulations disproportionately benefit US play.

3. **Dirichlet noise at root helps exploration.** Already implemented. Default
   dir_epsilon=0.25, dir_alpha is automatically set. This prevents the search
   from collapsing to the prior's top action.

### Recommended MCTS configuration for US play improvement

For **benchmarking** (measuring US WR improvement from search):
```
n_determinizations = 8
n_simulations = 200   # per determinization
temperature = 0.0     # greedy at test time
dir_epsilon = 0.25
```

For **teacher target generation** (generating improved US policy targets):
```
n_determinizations = 16
n_simulations = 400   # higher budget for teacher
temperature = 1.0     # proportional visits for soft targets
dir_epsilon = 0.25
```

For **initial diagnostic** (fast, cheap, just to see if MCTS helps US at all):
```
n_determinizations = 4
n_simulations = 50
temperature = 0.0
```

### Expected US WR gain from MCTS

Based on analogies to other imperfect-information games:
- MCTS with 200 sims / 8 dets typically adds 5-15pp WR over raw policy
- The gain is larger for the weaker side (US) because there is more room
  for improvement
- Conservative estimate: US WR 13% → 18-22% with MCTS at test time
- This alone would bring combined from 29.5% to ~33-35%

---

## 7. Prioritized Experiment Plan

### Phase A: Quick wins (1-2 days, no architecture changes)

#### A1. MCTS diagnostic benchmark (2 hours)

Run the existing ISMCTS benchmark with current best model (saturation_1x_95ep)
to measure how much search helps each side:

```bash
# Quick diagnostic: 4 det x 50 sims, 500 games/side
nice -n 10 uv run python scripts/benchmark_suite.py \
    --checkpoint checkpoints/v99_saturation_1x_95ep.pt \
    --n-games 500 \
    --ismcts --n-det 4 --n-sim 50 \
    --seeds 42,7,123,456

# Full benchmark: 8 det x 200 sims, 500 games/side (slower)
nice -n 10 uv run python scripts/benchmark_suite.py \
    --checkpoint checkpoints/v99_saturation_1x_95ep.pt \
    --n-games 500 \
    --ismcts --n-det 8 --n-sim 200 \
    --seeds 42,7,123,456
```

**Purpose**: Measure the MCTS uplift on US WR specifically. If MCTS at 4x50
already moves US WR from 13% to 17%+, then search-based approaches are clearly
worth pursuing. If not, we need training-side fixes first.

**Expected output**: USSR WR and US WR with MCTS, compared to raw policy.

#### A2. Side-relative value target training (4 hours)

Implement the actor-perspective value target (intervention 5a, Option A) and
retrain the baseline model.

Implementation changes:
1. In `python/tsrl/policies/dataset.py`: add `value_target_mode='actor_relative'`
   that flips the sign of `final_vp` for US-side rows.
2. In `scripts/train_baseline.py`: add the new choice to `--value-target`.
3. At inference/benchmark time: when the model predicts value for a US position,
   the output already represents "good for US" (positive = US advantage). The
   benchmark code needs to negate the value when computing from USSR perspective.

Training run:
```bash
nice -n 10 uv run python scripts/train_baseline.py \
    --data-dir data/selfplay/combined_v99_clean_b \
    --out-dir checkpoints/v100_actor_value \
    --arch baseline --hidden-dim 256 \
    --epochs 95 --batch-size 8192 --lr 0.0024 \
    --value-target actor_relative \
    --seed 42 \
    --wandb --wandb-name v100_actor_value_s42
```

**Purpose**: Test whether fixing the value perspective alone improves US WR.
This is the single most impactful cheap intervention.

**Expected outcome**: US WR improves 2-5pp (from 13% to 15-18%) because the
value head no longer penalizes US positions. USSR WR may drop 1-3pp due to
the value head no longer being USSR-biased at inference. Combined should
improve 1-3pp.

#### A3. US-weighted training (2 hours)

Simple loss reweighting. Can run in parallel with A2 since it uses different
model variant.

```bash
# Sweep us_weight in {1.5, 2.0, 3.0}
for w in 1.5 2.0 3.0; do
    nice -n 10 uv run python scripts/train_baseline.py \
        --data-dir data/selfplay/combined_v99_clean_b \
        --out-dir checkpoints/v100_usweight_${w} \
        --arch baseline --hidden-dim 256 \
        --epochs 95 --batch-size 8192 --lr 0.0024 \
        --value-target final_vp \
        --us-weight $w \
        --seed 42 \
        --wandb --wandb-name "v100_usweight_${w}_s42"
    done
```

Note: `--us-weight` flag needs to be implemented in train_baseline.py.

**Purpose**: Measure pure loss reweighting effect, independent of value
perspective change.

### Phase B: Architecture changes (2-3 days)

#### B1. Side embedding model

Add a side embedding (32-dim) concatenated to the trunk input, plus separate
value heads for each side.

```python
# In model.py, new variant TSSideCondModel:
class TSSideCondModel(TSBaselineModel):
    def __init__(self, hidden_dim=256):
        super().__init__(hidden_dim)
        self.side_embedding = nn.Embedding(2, 32)
        # Expand trunk input by 32
        self.trunk = nn.Sequential(
            nn.Linear(TRUNK_IN + 32, hidden_dim),
            nn.ReLU(), nn.Dropout(0.1),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(), nn.Dropout(0.1),
        )
        # Separate value heads
        self.value_head_ussr = nn.Sequential(
            nn.Linear(hidden_dim, VALUE_BRANCH_HIDDEN),
            nn.ReLU(),
            nn.Linear(VALUE_BRANCH_HIDDEN, 1),
            nn.Tanh(),
        )
        self.value_head_us = nn.Sequential(
            nn.Linear(hidden_dim, VALUE_BRANCH_HIDDEN),
            nn.ReLU(),
            nn.Linear(VALUE_BRANCH_HIDDEN, 1),
            nn.Tanh(),
        )
```

Train with actor-relative value targets:
```bash
nice -n 10 uv run python scripts/train_baseline.py \
    --data-dir data/selfplay/combined_v99_clean_b \
    --out-dir checkpoints/v101_sidecond \
    --arch side_cond --hidden-dim 256 \
    --epochs 95 --batch-size 8192 --lr 0.0024 \
    --value-target actor_relative \
    --seed 42 \
    --wandb --wandb-name v101_sidecond_s42
```

#### B2. Combined: side embedding + actor-relative value + US weight 2.0

Run the full combination of all Phase A and B1 interventions together:

```bash
nice -n 10 uv run python scripts/train_baseline.py \
    --data-dir data/selfplay/combined_v99_clean_b \
    --out-dir checkpoints/v101_combined \
    --arch side_cond --hidden-dim 256 \
    --epochs 95 --batch-size 8192 --lr 0.0024 \
    --value-target actor_relative \
    --us-weight 2.0 \
    --seed 42 \
    --wandb --wandb-name v101_combined_s42
```

### Phase C: Search-based improvements (3-5 days)

#### C1. MCTS teacher targets for US positions

After Phase A/B establishes the best training configuration, generate teacher
targets specifically for US positions:

1. Select 50k US-side positions from the training data (stratified by turn)
2. Run ISMCTS with the best model from Phase B
3. Extract improved policy targets
4. Retrain with teacher distillation

```bash
# Step 1: Extract US positions
nice -n 10 uv run python scripts/mine_us_positions.py \
    --data-dir data/selfplay/combined_v99_clean_b \
    --out data/teacher/us_positions_50k.parquet \
    --n-positions 50000 --seed 42

# Step 2: Run teacher search
nice -n 10 uv run python scripts/teacher_search.py \
    --positions data/teacher/us_positions_50k.parquet \
    --checkpoint checkpoints/v101_combined.pt \
    --n-det 16 --n-sim 400 \
    --out data/teacher/us_teacher_50k.parquet

# Step 3: Retrain with teacher targets
nice -n 10 uv run python scripts/train_baseline.py \
    --data-dir data/selfplay/combined_v99_clean_b \
    --out-dir checkpoints/v102_us_teacher \
    --arch side_cond --hidden-dim 256 \
    --epochs 95 --batch-size 8192 --lr 0.0024 \
    --value-target actor_relative \
    --us-weight 2.0 \
    --teacher-targets data/teacher/us_teacher_50k.parquet \
    --seed 42 \
    --wandb --wandb-name v102_us_teacher_s42
```

#### C2. MCTS at benchmark time (ongoing)

Once the value head is de-biased (Phase A2), run all benchmarks with MCTS
to measure the combined effect of better training + search:

```bash
nice -n 10 uv run python scripts/benchmark_suite.py \
    --checkpoint checkpoints/v101_combined.pt \
    --n-games 500 \
    --ismcts --n-det 8 --n-sim 200 \
    --seeds 42,7,123,456
```

### Phase D: Advanced interventions (week 2+, only if needed)

#### D1. Self-play with de-biased model

If Phase A-C achieve US WR > 20%, the model is strong enough for productive
self-play. Run self-play specifically as US side against the heuristic:

```bash
nice -n 10 uv run python scripts/collect_learned_selfplay.py \
    --checkpoint checkpoints/v101_combined.pt \
    --side us --opponent heuristic \
    --n-games 5000 --seed 42 \
    --out data/selfplay/v101_us_vs_heuristic_5k.parquet
```

Filter to winning games and add to training data.

#### D2. Population training

Train a pool of models (different seeds, different architectures) and use
them as opponents for each other. This reduces the dependence on the single
biased heuristic.

#### D3. RL fine-tuning (REINFORCE / PPO)

Once BC + search reaches a plateau, switch to RL with the de-biased value head.
Use games against the heuristic as the environment. Reward = game outcome from
actor's perspective (not USSR perspective).

This is the long-term path to truly strong US play, but requires the
foundation from Phases A-C.

---

## 8. Success Criteria and Targets

### Short-term targets (Phase A-B, this week)

| Metric | Current | Target | Method |
|--------|---------|--------|--------|
| US WR vs heuristic | 13.0% | 18%+ | Actor-relative value + US weight |
| USSR WR vs heuristic | 46.2% | 42%+ | Accept small drop for balance |
| Combined WR | 29.5% | 32%+ | Net gain from US improvement |

### Medium-term targets (Phase C, next 1-2 weeks)

| Metric | Current | Target | Method |
|--------|---------|--------|--------|
| US WR vs heuristic | 13.0% | 22%+ | De-biased training + MCTS at inference |
| USSR WR vs heuristic | 46.2% | 44%+ | Maintain or slight drop |
| Combined WR | 29.5% | 35%+ | Balanced improvement |
| US WR with MCTS | N/A | 28%+ | MCTS at inference (8x200) |

### Definition of "fixed US bias"

The US bias is "fixed" when:
1. US WR is at least 60% of the heuristic's own US WR (i.e., 0.6 x 35% = 21%)
2. The USSR-to-US WR ratio is no worse than 3:1 (currently 3.5:1)
3. Combined WR is at least 33% (up from 29.5%)

### Is 20% US WR achievable with BC alone?

**Yes, probably.** The heuristic achieves 35% US WR. If we fix the value
calibration (5a) and add side-conditioning (5b), the model should be able to
imitate the heuristic's US play more faithfully. The gap from 13% to 20%
represents going from "badly distorted imitation" to "decent imitation."

Getting US WR above 25% likely requires search (MCTS) or RL, because the
heuristic's US play itself is not that good (only 35%), and the model would
need to play better than its training data.

### Is 30%+ US WR achievable?

**Only with search or RL.** 30% US WR approaches the heuristic's own US WR
(35%), which means the model would need to play nearly as well as the
heuristic as US. Since the model is smaller and approximate, it needs search
at inference time to bridge the gap.

With MCTS (8x200 sims), 28-32% US WR is plausible if the value head is
properly calibrated.

---

## 9. Risk Analysis

### Risk: Actor-relative value breaks USSR play

**Probability**: Medium-low.
**Mitigation**: The value head for USSR should be equivalent (just different
convention). If USSR WR drops, it means the model was relying on the biased
absolute value convention, which is unhealthy anyway. Accept a 2-3pp USSR drop
for a 5+pp US gain.

### Risk: US weight multiplier is too aggressive

**Probability**: Medium.
**Mitigation**: Sweep {1.5, 2.0, 3.0}. At 3.0, US rows dominate the loss
and USSR play will degrade. Start with 1.5-2.0.

### Risk: MCTS reinforces value head bias

**Probability**: Medium if value head is still USSR-biased. Low if value
head uses actor-relative targets.
**Mitigation**: Fix the value head first (Phase A2) before using MCTS for
teacher target generation.

### Risk: Side embedding overfits with limited data

**Probability**: Low. A 32-dim embedding is tiny compared to the model.
**Mitigation**: Can use 16-dim instead. Also, the trunk already sees the
`phasing` scalar; the embedding just provides a richer representation.

### Risk: seed variance drowns out treatment effects

**Probability**: High. Measured at 3-4pp for baseline, 4pp+ for control_feat.
**Mitigation**: For Phase A experiments, run 2 seeds minimum. Only declare a
win if the mean improvement exceeds 3pp across seeds.

---

## 10. Appendix: Data and Configuration Reference

### Current best model

- Checkpoint: `checkpoints/v99_saturation_1x_95ep.pt`
- Architecture: baseline h256 (TSBaselineModel)
- Data: nash_b 1.28M rows, 10k games
- Epochs: 95
- Hyperparams: bs=8192, lr=0.0024, dropout=0.1, ls=0.05, wd=1e-4, one-cycle
- Value target: final_vp
- Benchmark: USSR 46.2% ±1.1, US 13.0% ±0.8, Combined 29.5% ±0.7

### Dataset statistics (nash_b, post-DEFCON-fix)

- Total rows: 1.28M (training after split)
- Games: 10,000
- USSR wins: 62.6%
- US wins: 35.1%
- Draws: 2.3%
- Mean game length: 9.1 turns
- USSR-side rows: ~640k (50%)
- US-side rows: ~640k (50%)
- US-side rows from US-winning games: ~225k (35% of US rows)

### ISMCTS configuration in C++

Location: `cpp/tscore/ismcts.cpp`, `include/ismcts.hpp`
Binding: `bindings/tscore_bindings.cpp` line 593+

Default config:
- n_determinizations: 8
- n_simulations per det: 50
- MCTS: PUCT with c_puct configurable
- Dirichlet noise: dir_epsilon=0.25, dir_alpha auto-set

### Key files to modify

| File | Change |
|------|--------|
| `python/tsrl/policies/dataset.py` | Add `actor_relative` value target mode |
| `scripts/train_baseline.py` | Add `--value-target actor_relative`, `--us-weight` |
| `python/tsrl/policies/model.py` | Add `TSSideCondModel` variant |
| `scripts/benchmark_suite.py` | Handle actor-relative value at inference |

### Experiment execution order

```
Day 1:
  Morning:  A1 (MCTS diagnostic, 2h)
  Afternoon: A2 (actor-relative value, training ~4h)
  Evening:  A3 (US weight sweep, 3 runs ~6h each, overnight)

Day 2:
  Morning:  Benchmark A2 and A3 results
  Afternoon: B1 (side embedding model, implement + train)
  Evening:  B2 (combined, overnight)

Day 3:
  Morning:  Benchmark B1 and B2
  Afternoon: C1 start (teacher target generation for US positions)
  Evening:  C2 (MCTS benchmark of best Phase B model)

Day 4-5:
  C1 training with teacher targets
  D1 if needed (self-play data collection)
```

### Key decision points

1. **After A1**: If MCTS gives <3pp US WR gain, the value head bias is severe
   and Phase A2 becomes critical. If MCTS gives >5pp, search is the primary
   lever and Phase C should be prioritized.

2. **After A2**: If actor-relative value gives >3pp US WR gain, the value
   perspective was a major cause. Proceed to B1/B2. If <2pp gain, the problem
   is deeper (policy head, not just value).

3. **After B2**: If combined interventions give <5pp total US WR gain
   (US WR still <18%), then BC-based fixes are insufficient and the priority
   shifts to Phase C (search) and D (RL).

4. **After C2**: If MCTS + de-biased model gives US WR >25%, the approach is
   working and we should invest in teacher target generation (C1) to distill
   search improvements back into the model for faster inference.

---

## Summary of Prioritized Actions

| Priority | Experiment | Expected US WR gain | Effort |
|----------|-----------|---------------------|--------|
| 1 (critical) | A1: MCTS diagnostic benchmark | Diagnostic | 2 hours |
| 2 (critical) | A2: Actor-relative value targets | +2-5pp | 4 hours + training |
| 3 (high) | A3: US loss weight sweep | +1-3pp | 2 hours + training |
| 4 (high) | B1: Side embedding model | +1-3pp | 4 hours + training |
| 5 (high) | B2: Combined all fixes | +3-7pp cumulative | Training only |
| 6 (medium) | C1: US teacher targets from MCTS | +2-5pp | 1-2 days |
| 7 (medium) | C2: MCTS at benchmark time | +5-10pp at inference | Configuration |
| 8 (lower) | D1: US self-play data | +1-3pp | 1 day |
| 9 (lower) | D3: RL fine-tuning | +5-15pp long-term | 1+ week |

**Stop the current pure-BC sweep.** The remaining control_feat seeds and
epoch-ceiling experiments address seed variance, not the US bias. They should
be deprioritized in favor of Phases A-C above.

The single most important experiment is A2 (actor-relative value targets).
If we can only run one thing, run that.
