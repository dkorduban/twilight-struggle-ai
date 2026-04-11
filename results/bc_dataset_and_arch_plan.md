# BC Dataset & Architecture Evaluation Plan

## 1. Dataset Re-encoding Plan

### Goal
Re-encode `nash_bcd_combined` (4.08M rows) from 11-dim scalars to 32-dim scalars
without re-collecting games. The raw state columns already exist in the parquet files.

### Column mapping: scalars[11..31] from existing parquet columns

| Scalar index | Feature | Parquet column | Type | Encoding |
|---|---|---|---|---|
| 11 | bear_trap_active | `bear_trap_active` | Boolean | 1.0/0.0 |
| 12 | quagmire_active | `quagmire_active` | Boolean | 1.0/0.0 |
| 13 | cuban_missile_crisis | `cuban_missile_crisis_active` | Boolean | 1.0/0.0 |
| 14 | iran_hostage_crisis | `iran_hostage_crisis_active` | Boolean | 1.0/0.0 |
| 15 | norad_active | `norad_active` | Boolean | 1.0/0.0 |
| 16 | shuttle_diplomacy | `shuttle_diplomacy_active` | Boolean | 1.0/0.0 |
| 17 | salt_active | `salt_active` | Boolean | 1.0/0.0 |
| 18 | flower_power_active | `flower_power_active` | Boolean | 1.0/0.0 |
| 19 | flower_power_cancelled | `flower_power_cancelled` | Boolean | 1.0/0.0 |
| 20 | vietnam_revolts | `vietnam_revolts_active` | Boolean | 1.0/0.0 |
| 21 | north_sea_oil_extra_ar | `north_sea_oil_extra_ar` | Boolean | 1.0/0.0 |
| 22 | glasnost_extra_ar | `glasnost_extra_ar` | Boolean | 1.0/0.0 |
| 23 | nato_active | `nato_active` | Boolean | 1.0/0.0 |
| 24 | de_gaulle_active | `de_gaulle_active` | Boolean | 1.0/0.0 |
| 25 | nuclear_subs_active | `nuclear_subs_active` | Boolean | 1.0/0.0 |
| 26 | formosan_active | `formosan_active` | Boolean | 1.0/0.0 |
| 27 | awacs_active | `awacs_active` | Boolean | 1.0/0.0 |
| 28 | chernobyl_active | **MISSING** | -- | Default 0.0 |
| 29 | chernobyl_blocked_region | **MISSING** | -- | Default 0.0 |
| 30 | ops_modifier[USSR] | `ops_modifier` | List(Int64)[2] | `ops_modifier[0] / 3.0` |
| 31 | ops_modifier[US] | `ops_modifier` | List(Int64)[2] | `ops_modifier[1] / 3.0` |

### Missing columns: chernobyl

`chernobyl_blocked_region` is not present in the existing parquet files. Two options:

**Option A (recommended)**: Set indices 28-29 to 0.0 for all re-encoded rows.
Chernobyl (#94) is a Late War card (turns 8-10 only). In heuristic self-play data,
it activates in <2% of rows. The signal loss is negligible for BC training.

**Option B**: Re-derive from game logs. Not worth the effort for 4M heuristic rows
when the feature fires rarely. If we collect new PPO rollout data, the C++ collector
already writes chernobyl state since `kScalarDim=32` is compiled in.

### Re-encoding pipeline

The re-encoding does NOT require modifying `TS_SelfPlayDataset`. Instead, we modify
the dataset class to read the 21 extra features from the parquet columns at load time,
exactly as it currently reads the 11 core scalars. This is the cleanest approach because:

1. No intermediate re-encoded parquet files needed
2. The original data stays immutable
3. The dataset class already handles column presence checks

**Code change in `python/tsrl/policies/dataset.py`**:

```python
# After the existing 11 scalars, append 21 new features:
# [11-21] Active effects (booleans)
_EFFECT_BOOL_COLS = [
    "bear_trap_active", "quagmire_active", "cuban_missile_crisis_active",
    "iran_hostage_crisis_active", "norad_active", "shuttle_diplomacy_active",
    "salt_active", "flower_power_active", "flower_power_cancelled",
    "vietnam_revolts_active", "north_sea_oil_extra_ar",
    "glasnost_extra_ar", "nato_active", "de_gaulle_active",
    "nuclear_subs_active", "formosan_active", "awacs_active",
]

# Build extended scalars array
extended_features = []
for col_name in _EFFECT_BOOL_COLS:
    if col_name in df.columns:
        extended_features.append(df[col_name].cast(pl.Float32).to_numpy())
    else:
        extended_features.append(np.zeros(N, dtype=np.float32))

# [28-29] Chernobyl (missing in existing data, zeros)
extended_features.append(np.zeros(N, dtype=np.float32))  # chernobyl_active
extended_features.append(np.zeros(N, dtype=np.float32))  # chernobyl_region

# [30-31] Ops modifier
if "ops_modifier" in df.columns:
    ops_mod = np.array(df["ops_modifier"].to_list(), dtype=np.float32)  # (N, 2)
    extended_features.append(ops_mod[:, 0] / 3.0)  # USSR
    extended_features.append(ops_mod[:, 1] / 3.0)  # US
else:
    extended_features.append(np.zeros(N, dtype=np.float32))
    extended_features.append(np.zeros(N, dtype=np.float32))

# Stack all 21 new features and concat with base 11
extra = np.stack(extended_features, axis=1)  # (N, 21)
scalars = np.concatenate([scalars, extra], axis=1)  # (N, 32)
```

**Model change**: Bump `SCALAR_DIM = 32` in `model.py` and update
`nn.Linear(SCALAR_DIM + self._REGION_SCALAR_DIM, SCALAR_HIDDEN)` in GNN models.

### Time estimate
- Code changes to dataset.py + model.py: ~30 min
- Re-test with existing data (load + verify shapes): ~10 min
- No separate re-encoding step needed (the dataset does it on-the-fly)

### Risk: `_NEEDED_COLS` filter
The dataset's `_NEEDED_COLS` set (line 169) must be expanded to include all 17
boolean columns plus `ops_modifier`. Without this, `_read_slim()` will skip them
and the columns won't be available. This is a one-line change.


## 2. New Data Collection Plan

### What data already exists

| Dataset | Rows | Source | Quality | Use |
|---|---|---|---|---|
| nash_bcd_combined | 4.08M | Heuristic self-play (Nash temps) | Medium | BC training |
| PPO v3 rollouts | ~500k (est) | PPO self-play at ~89% WR | High | Not yet in BC format |

### Should we collect new data for architecture experiments?

**No, not initially.** Here's why:

1. **The 4.08M rows are sufficient for a fair GNN vs Attention comparison.**
   The prior experiment (Phase 1) compared these architectures at 2.13M rows.
   At 4.08M we have nearly 2x more. If attention still underperforms at 4.08M,
   the "needs more data" hypothesis is weakened.

2. **PPO rollout data requires format conversion work.** The PPO rollouts store
   pre-encoded tensors (influence, cards, scalars) plus raw state. Converting
   these to the BC parquet schema requires a new script. This is useful but
   should come after the baseline comparison.

3. **Mixing data quality levels confounds the experiment.** If we train on
   heuristic + PPO data and attention beats GNN, we won't know if it's the
   architecture or the data quality. Clean comparison first.

### When to collect new data

Collect new data ONLY if the 4.08M experiment shows attention is within 2pp of GNN.
That would justify the hypothesis that attention benefits more from data quality/quantity.

If triggered:
```bash
# Collect 2000 games (US+USSR) of PPO v3 self-play rollouts
# (~130k rows per 1000 games at ~65 steps/game average)
# Target: ~260k high-quality rows
build/ts_collect_selfplay_rows_jsonl \
    --model checkpoints/ppo_v3_best.pt \
    --games 1000 --side both \
    --opponent model --opponent-model checkpoints/ppo_v3_best.pt \
    --seed 60000 --output data/selfplay/ppo_v3_selfplay_2k.jsonl

uv run python scripts/jsonl_to_parquet.py \
    --input data/selfplay/ppo_v3_selfplay_2k.jsonl \
    --out data/ppo_v3_selfplay/ppo_v3_2k.parquet
```

### Data size estimates for future experiments

| Experiment | Data needed | How to get it | Time |
|---|---|---|---|
| GNN vs Attn baseline | 4.08M (existing) | Re-encode scalars in dataset.py | 0 min collection |
| GNN vs Attn + more data | 4.08M + 2M new heur | `collect_selfplay_rows_jsonl` 15k games | ~30 min |
| PPO-quality comparison | 4.08M heur + 260k PPO | Collect from best PPO checkpoint | ~10 min |


## 3. Architecture Experiment Protocol

### The comparison

**GNN**: `TSControlFeatGNNSideModel` (current best BC architecture)
- 2-hop message passing over 86-country adjacency graph
- Encodes that adjacent countries matter (correct for TS: coups, realignments, influence placement)
- Produces 28 region scalars as side output
- ~350k parameters (h=256)

**Attention**: `TSCountryAttnModel`
- 4-head self-attention over 86 country tokens
- No adjacency prior; must learn spatial relationships from data
- Also uses CardEmbedEncoder (GNN model does not)
- ~340k parameters (h=256)

### Is the GNN's inductive bias correct?

**Yes, substantially.** In Twilight Struggle:
- Coups/realignments can only target countries where the opponent has influence
- Influence placement can only go to countries where you have influence OR adjacent to such countries
- Scoring depends on control of countries in a region (regional proximity)
- Access chains (influence propagation) follow the adjacency graph exactly

The adjacency graph is THE fundamental structure of the game board. The GNN's bias
is not an approximation -- it encodes the actual game mechanics. Self-attention
must learn this structure from data, which is inherently less sample-efficient.

### ML theory on dataset size requirements

**Graph Neural Networks vs Transformers for small fixed graphs:**

The relevant comparison is not "GNN vs Transformer" in the NLP/CV sense (where
transformers need billions of examples). Here both operate on a fixed 86-node graph.

Key factors:
1. **Inductive bias reduces sample complexity.** The GNN effectively starts with
   the adjacency structure as prior knowledge. This is ~3700 edges of relational
   information that attention must learn from scratch.

2. **Fixed graph size limits attention's disadvantage.** With only 86 tokens and
   4 heads, the attention pattern has 86x86=7396 potential edges to learn. This is
   tractable even with moderate data. The issue isn't total parameters but whether
   the training signal distinguishes "adjacent and relevant" from "distant and irrelevant."

3. **Empirical estimate**: Based on the Phase 1 results:
   - At 2.13M rows: attention (23.0%) matched baseline (22.4%) but trailed
     control_feat (29.0%) significantly.
   - The GNN at 1.28M rows (37.2%) crushed attention at 2.13M rows (23.0%).
   - The gap is 14.2pp -- this is not a "needs 2x more data" situation.

**Prediction**: Attention will NOT match GNN even at 4M+ rows of heuristic data.
The adjacency prior is too valuable for a game where adjacency literally defines
legal actions. However, the experiment is still worth running to:
(a) confirm the prediction rigorously on clean data
(b) establish whether a GNN+Attention hybrid could capture both local and global patterns

### Experiment design

**Controlled variables:**
- Dataset: nash_bcd_combined (4.08M rows), 32-dim scalars
- Split: deterministic by game_id hash (val_fraction=0.1)
- Hyperparams: bs=8192, lr=0.0024, epochs=60, patience=15
- Weight decay: 1e-4
- Label smoothing: 0.05
- Dropout: 0.1
- Value target: final_vp
- OneCycleLR: yes
- Hidden dim: 256 (both models)

**Varying:**
- Architecture: {control_feat_gnn_side, country_attn}
- Seeds: {7, 42, 123} (3 seeds each, 6 total runs)

**Metrics (primary → secondary):**
1. **Proxy eval loss** on held-out set (card_top1, mode_acc, combined val_loss)
   -- 3 seeds give mean + std. Primary decision metric for architecture ranking.
2. **500-game benchmark** on best seed per architecture (secondary confirmation)
   -- only run this if proxy metrics are ambiguous (within 1pp)
3. W&B tracked: all losses, LR, gradient norms per epoch

**Decision criteria:**
- If GNN mean val_loss < Attention mean val_loss by >0.05 (>1 seed std), GNN wins.
  Skip benchmark for attention.
- If within 0.05 val_loss: run 500-game benchmarks on best seed of each. If GNN
  leads by >3pp combined WR (>benchmark CI), GNN wins.
- If within 3pp combined WR: GNN wins by default (adjacency prior is free and
  attention adds no benefit).

**Why 3 seeds is sufficient:**
Phase 1 measured seed variance at 3-4pp for BC models. With 3 seeds we get
std_err ~= 2pp / sqrt(3) ~= 1.2pp. A 3pp difference is >2 standard errors,
giving ~95% confidence the difference is real. Adding a 4th seed buys only
~15% tighter CI.

### Training commands

```bash
# GNN seeds
for seed in 7 42 123; do
  uv run python scripts/train_baseline.py \
    --data-dir data/nash_bcd_combined \
    --out-dir data/checkpoints/arch_gnn_s${seed} \
    --model-type control_feat_gnn_side --hidden-dim 256 \
    --batch-size 8192 --lr 0.0024 --epochs 60 --patience 15 \
    --dropout 0.1 --weight-decay 1e-4 --label-smoothing 0.05 \
    --one-cycle --deterministic-split --value-target final_vp \
    --seed ${seed}
done

# Attention seeds
for seed in 7 42 123; do
  uv run python scripts/train_baseline.py \
    --data-dir data/nash_bcd_combined \
    --out-dir data/checkpoints/arch_attn_s${seed} \
    --model-type country_attn --hidden-dim 256 \
    --batch-size 8192 --lr 0.0024 --epochs 60 --patience 15 \
    --dropout 0.1 --weight-decay 1e-4 --label-smoothing 0.05 \
    --one-cycle --deterministic-split --value-target final_vp \
    --seed ${seed}
done
```

**Time estimate**: ~15 min/run on RTX 3050 (4.08M rows, bs=8192) = ~90 min total for 6 runs.

### Important confound: TSCountryAttnModel lacks features that GNN has

The current `TSCountryAttnModel` is missing several features present in
`TSControlFeatGNNSideModel`:

1. **No region scalars**: GNN model produces 28 region-level features (BG/non-BG
   control counts per region) and feeds them to the scalar encoder. Attention model
   does not. This alone could explain most of the gap.

2. **No side embedding**: GNN_Side model has a learned 32-dim side embedding.
   Attention model uses the scalar `phasing` flag only.

3. **No stability features**: GNN uses `_STABILITY` buffer for control computation.
   Attention uses only raw influence counts.

4. **Different SCALAR_DIM**: GNN's scalar_encoder takes `SCALAR_DIM + 28 = 39` inputs.
   Attention takes `SCALAR_DIM = 11`.

**This means the Phase 1 comparison was not a clean GNN-vs-Attention test.**
It was "GNN + region scalars + stability + side embed" vs "Attention + card embed".

**Recommendation**: Before running the full experiment, create `TSCountryAttnSideModel`
that matches GNN features: add region scalars, side embedding, and stability features
to the attention model. Then the comparison isolates the adjacency message passing
vs self-attention question.


## 4. Proxy Eval Set Design

### Purpose
A 5k-state evaluation set that gives a fast proxy for playing strength, avoiding
the need for 500+ game benchmarks during architecture search.

### Composition

| Criterion | Count | Rationale |
|---|---|---|
| Early game (turns 1-3) | 1500 | Setup influence, headline, early positioning |
| Mid game (turns 4-7) | 2000 | Most strategically complex; scoring regions contested |
| Late game (turns 8-10) | 1500 | Final scoring push, high-value decisions |
| **Total** | **5000** | |

Within each turn bucket:
- 50% USSR acting, 50% US acting
- Stratified by action mode: ~40% influence, ~25% event, ~20% coup, ~10% realign, ~5% space

### State selection criteria

**Non-trivial positions only.** Exclude:
- States with only 1 legal action (forced plays)
- Setup influence allocation (card_id=0)
- States where all legal cards are opponent-owned events (no real choice)

**Diverse games.** Sample at most 5 states per game to avoid correlation within
the eval set.

### Labeling method

**Option A (fast, recommended for now)**: Use the actual action from the game as the
"ground truth" label. This is what val_loss already measures. The eval set is just
a curated, stratified subset of the validation split.

**Option B (ideal, expensive)**: Run MCTS at 2000 simulations with pruning on each
of the 5000 states to get a search-improved policy. This gives a better proxy for
"what a strong player would do" but costs ~40 GPU-minutes on RTX 3050.

**Recommendation**: Start with Option A. If proxy loss correlates well with benchmark
WR (check using existing checkpoints), it's sufficient. Only invest in Option B if
the correlation is weak.

### Collection

```python
# In dataset.py or a separate script:
# 1. Load nash_bcd_combined with deterministic split
# 2. From the validation split, filter out trivial positions
# 3. Stratify by turn bucket and side
# 4. Sample 5000 states (max 5 per game)
# 5. Save as data/eval/proxy_5k.parquet
```

### Validating the proxy

Before using the proxy, calibrate it against known benchmark results:

| Checkpoint | Benchmark combined WR | Proxy card_top1 | Proxy val_loss |
|---|---|---|---|
| v89 (baseline) | 22.2% | ? | ? |
| v99_cf_1x95 | 31.0% | ? | ? |
| v106_cf_gnn_s42 | 34.9% (Nash) | ? | ? |

If proxy metrics are monotonically correlated with benchmark WR, the proxy is
trustworthy for architecture comparison. If not (e.g., lower val_loss but lower WR),
the proxy must include MCTS-derived labels.


## 5. Sequenced Plan

### Phase A: Prerequisite code changes (Day 1, ~2 hours)

1. **Expand `_NEEDED_COLS`** in `dataset.py` to include the 17 boolean columns
   plus `ops_modifier`. (~5 min)

2. **Add 32-dim scalar encoding** to `TS_SelfPlayDataset.__init__()`.
   Gracefully handle missing `chernobyl_blocked_region` (default 0.0).
   Add a `scalar_dim` parameter (default 11 for backward compat, 32 for new). (~30 min)

3. **Bump `SCALAR_DIM`** in `model.py` from 11 to 32. Ensure all model classes
   that reference SCALAR_DIM handle both 11 and 32 (via constructor parameter). (~20 min)

4. **Create `TSCountryAttnSideModel`**: clone `TSCountryAttnModel`, add region
   scalars from `ControlFeatCountryEncoder`'s region computation, add side
   embedding. This gives a fair comparison with GNN. (~45 min)

5. **Test**: Load dataset with 32-dim scalars, forward pass through each model
   architecture, verify shapes match. (~15 min)

### Phase B: Proxy eval set (Day 1, ~1 hour)

1. Write `scripts/build_proxy_eval.py`:
   - Load nash_bcd_combined, deterministic split, take val set
   - Filter trivial positions (single legal action)
   - Stratify by turn + side
   - Sample 5000 states (max 5/game)
   - Write `data/eval/proxy_5k.parquet`

2. Write `scripts/eval_proxy.py`:
   - Load a checkpoint + proxy eval set
   - Compute card_top1, mode_acc, val_loss, country_top1
   - Output one-line summary

3. Calibrate proxy against known checkpoints (v89, v99, v106).

### Phase C: Architecture experiment (Day 2, ~2 hours active + ~90 min training)

1. Run 6 training jobs (3 GNN seeds + 3 Attention seeds) on `nash_bcd_combined`
   with 32-dim scalars. Each job: ~15 min on RTX 3050.

2. Evaluate all 6 checkpoints on proxy eval set.

3. Compute mean + std for each architecture.

4. If decision criteria met (>0.05 val_loss gap): done.

5. If ambiguous: run 500-game benchmark on best seed of each (~10 min each).

### Phase D: Conditional follow-up (Day 3, only if needed)

If attention is within 2pp of GNN:
1. Collect 2000 games of PPO v3 self-play (~260k rows)
2. Train both architectures on heuristic + PPO data
3. Compare again

If GNN wins decisively (expected):
1. Skip attention experiments
2. Invest time in GNN improvements: 3-hop, learnable edge weights, or GNN+Attention hybrid
3. Move to PPO v4 with 32-dim scalars and GNN architecture

### Total timeline

| Phase | Duration | Blocking? |
|---|---|---|
| A: Code changes | 2 hours | Yes |
| B: Proxy eval | 1 hour | Yes (needs Phase A) |
| C: Training | 90 min GPU + 30 min analysis | Yes (needs A+B) |
| D: Follow-up | 2-4 hours (conditional) | No |
| **Total** | **~5 hours** (without Phase D) | |


## Appendix: Why Attention Probably Loses

The Phase 1 experiment showed GNN beating attention by **14.2pp** (37.2% vs 23.0%)
at comparable data sizes. This gap is unlikely to close with more data because:

1. **The adjacency structure is not just a useful prior -- it IS the game board.**
   Legal moves in TS are defined by adjacency. The model predicting country targets
   must understand which countries are accessible from current influence, which is
   literally a graph reachability query. GNN computes this natively; attention must
   learn it from data.

2. **The Phase 1 attention model was disadvantaged by missing features** (no region
   scalars, no side embedding, no stability). Creating a fair attention variant
   (Phase A step 4) will narrow the gap, but the remaining gap is the adjacency
   information itself.

3. **86 countries is a small graph.** Transformers shine when the graph structure
   is unknown or variable. Here the graph is fixed and known -- encoding it
   directly is strictly better information-theoretically.

4. **Data quality won't help.** PPO rollout data has better action labels, but the
   spatial structure of the game board is identical. Attention's failure to encode
   adjacency is a structural limitation, not a data limitation.

The experiment is still worth running (to confirm rigorously and to measure the
fair-comparison gap after adding region scalars to attention), but the expected
outcome is GNN winning by 5-10pp.
