# Model Architecture Analysis

## Summary

The codebase implements **5 factorized policy + value models** for offline imitation learning on Twilight Struggle. All share a common trunk + policy/value head design but differ in **input encoder inductive biases**. The architecture search prioritized **factorized action modeling** (card → mode → country) over a single flattened action head, enabling efficient training on ~3M samples.

---

## Architecture Lineup

| Model | Params | Inductive Bias | Key Feature |
|-------|--------|----------------|-------------|
| **TSBaselineModel** | 447.4K | Flat MLPs | Baseline; no domain structure |
| **TSCardEmbedModel** | 464.2K | Card DeepSet | Per-card static features + pooling |
| **TSCountryEmbedModel** | 480.8K | Country MLP | Per-country + regional aggregation |
| **TSFullEmbedModel** | 497.6K | Card + Country | Both embeddings combined |
| **TSCountryAttnModel** | 547.4K | Country Attention | Self-attention over 86 country tokens |

### Parameter Count Details

**All models:**
- Influence encoder: Linear(172 → 128)
- Card encoder: Linear(448 → 128)
- Scalar encoder: Linear(11 → 64)
- Trunk: Linear(320 → 256) + 2×ResidualBlock(256)
- Policy heads: card(256→111), mode(256→5), strategy(256→336)
- Value branch: Linear(256→128) + Linear(128→1)

**Base (Baseline):** 447.4K params

**Card encoder additions:**
- CardEmbedEncoder: Linear(8→32) + Linear(128→128) = +16.8K
- Total TSCardEmbedModel: **464.2K** (3.8% larger)

**Country encoder additions:**
- CountryEmbedEncoder: Linear(13→32) + Linear(256→128) = +33.3K
- Total TSCountryEmbedModel: **480.8K** (7.5% larger)

**Full embed (Card + Country):** 
- Total TSFullEmbedModel: **497.6K** (11.2% larger)

**Country attention (Card + CountryAttn):**
- CountryAttnEncoder: Linear(13→64) + MultiheadAttention(64, 4heads) + Linear(512→128) = +78.9K
- Total TSCountryAttnModel: **547.4K** (22.4% larger)

---

## Architectural Patterns

### Baseline: Flat MLP (447.4K)

```
influence (B,172) --Linear(172→128)--> (B,128)
cards (B,448) -----Linear(448→128)--> (B,128)
scalars (B,11) ----Linear(11→64)----> (B,64)
                    Concat (B,320)
                    Linear(320→256) + ReLU + Dropout
                    ResidualBlock(256)
                    ResidualBlock(256)
                    |
                    +---> card_head: Linear(256→111)
                    +---> mode_head: Linear(256→5)
                    +---> strategy_head: Linear(256→336)
                    +---> value_branch: Linear(256→128) → Linear(128→1)
```

**Inductive bias:** None. Direct flattening of binary masks and influence counts.

---

### CardEmbedModel: DeepSet Card Encoder (464.2K)

```
cards (B,448) split into 4 masks:
  [0:112]     = actor_known_in
  [112:224]   = actor_possible
  [224:336]   = discard_mask
  [336:448]   = removed_mask

For each mask:
  card_feats (112, 8) --Linear(8→32)--> (112, 32)  [shared projection]
  masked_sum over each mask_i → 4 pools of (B, 32)
  Concat(B, 128) → Linear(128→128) → card_repr (B, 128)

Then:
  h_card = ReLU(Linear(448→128)(cards)) + card_repr  [additive fusion]
```

**Inductive bias:** 
- Per-card static features (ops, side, era, is_scoring, is_starred)
- Preserves identity signal while adding structural pooling
- Assumes independence of cards within each knowledge state (DeepSet)

---

### CountryEmbedModel: Per-Country MLP + Regional Pooling (480.8K)

```
influence (B,172) split:
  ussr_inf (B,86) / 10
  us_inf (B,86) / 10

For each country c:
  concat([ussr_inf[:,c], us_inf[:,c], country_static[c]]) → (B, 13)
  Linear(13→32) → (B, 86, 32) [per-country embeddings]

Global pool: mean over 86 countries → (B, 32)
Regional pools: mean over 7 regions (Europe, Asia, MiddleEast, Africa, 
                CentralAmerica, SouthAmerica, SoutheastAsia) → 7×(B, 32)

Concat(B, 256) → Linear(256→128) → influence_repr (B, 128)

Then:
  h_inf = ReLU(Linear(172→128)(influence)) + influence_repr  [additive fusion]
```

**Inductive bias:**
- Per-country static features (stability, is_battleground, region, starting influence)
- Regional aggregation (assumes geographic locality matters)
- Normalizes influence by factor of 10 (scales to 0-1 range typical for influence counts)

---

### FullEmbedModel: Both Card + Country Encoders (497.6K)

Applies both CardEmbedEncoder and CountryEmbedEncoder in additive fusion.

**Inductive bias:**
- Combines card-level and country-level structure
- Assumes both independent card pooling AND geographic/regional locality matter
- Explicit modeling of game's multi-domain nature (cards ≠ countries)

---

### CountryAttnModel: Self-Attention over Countries (547.4K)

```
Per-country embeddings (B, 86, 64):
  Linear(13→64) over all countries

Self-attention layer:
  MultiheadAttention(embed_dim=64, num_heads=4)
  Produces (B, 86, 64) with cross-country dependencies

Global pool: mean → (B, 64)
Regional pools: 7×(B, 64)

Concat(B, 512) → Linear(512→128) → influence_repr (B, 128)
```

**Inductive bias:**
- Countries can attend to each other (e.g., neighboring superpowers influence each other)
- More expressive than fixed regional aggregation but adds ~100K params and attention overhead

---

## Training Dynamics

### Observed Training Times (RTX 3050, batch_size=8192, ~2.96M rows)

| Model | Data | Epochs | Time/Epoch | Total Time | Best Val Loss |
|-------|------|--------|-----------|-----------|---------------|
| TSBaselineModel (v67) | 2.96M | 120 | ~12-13s | ~24-26 min | 1.7638 |

**Notes:**
- Single 4GB RTX 3050 GPU
- Batch size 8192 (limited by VRAM; can fit ~3.5M rows in memory at once)
- Learned rate: 2.4e-3, one-cycle schedule
- Patience=12 (stops if val_loss doesn't improve for 12 epochs)
- Typical convergence: epoch 60-100

### Estimated Relative Costs

Based on +param count and encoder overhead:

| Model | Relative Overhead | Est. Time/Epoch |
|-------|------------------|-----------------|
| Baseline | — | 12-13s (baseline) |
| CardEmbed | +3.8% params, +DeepSet pooling | ~12.5-13.5s (+4%) |
| CountryEmbed | +7.5% params, +per-country MLP | ~13-14s (+7%) |
| FullEmbed | +11.2% params, +both | ~14-15s (+12%) |
| CountryAttn | +22.4% params, +attention | ~15-17s (+25%) |

**Expected total training times (120 epochs):**
- Baseline: 24-26 min
- CardEmbed: 25-27 min
- CountryEmbed: 26-28 min
- FullEmbed: 28-30 min
- CountryAttn: 30-34 min

---

## Performance on Offline Data

### Known Results (from pipeline v58–v67)

**Benchmark win% vs heuristic (500 games, n_sim=0):**

| Gen | Model (Inferred) | Win % | Val Loss | Notes |
|-----|------------------|-------|----------|-------|
| v58 | Baseline | 18.5% | — | first with self-play data |
| v61 | Baseline | 18.5% | — | peak early |
| v62–v63 | Baseline | 14.9% | — | oscillation dip |
| v64–v65 | Baseline | 16.8–17.4% | — | recovery |
| v67 | Baseline | ? | 1.7638 | benchmark in progress |

**Observations:**
- All production runs use TSBaselineModel (simplest, fewest params)
- No ablation study comparing Card/Country/Full/Attn encoders on same data
- BC ceiling ~18.5% broken by self-play; oscillation suggests sensitivity to data mix

### Why Baseline Was Chosen

1. **Parsimonious:** 447K params fit comfortably in 4GB VRAM with batch_size=8192
2. **Fast:** ~12-13s/epoch leaves room for distributed collection (16 workers in parallel)
3. **No measured gain from embeddings:** Given BC plateau at ~15-18%, added inductive bias unlikely to yield step-change without more diverse training signal
4. **Simpler deployment:** Fewer buffers (card/country features) to track, easier debugging

---

## Architecture Decisions: Factorized Action Model

All models use **factorized action heads**, not a single flat 336-dimensional action classifier:

```
Per-card logits: (B, 111)        [logits for each playable card]
Per-mode logits: (B, 5)          [logits for mode: INFLUENCE/COUP/REALIGN/SPACE/EVENT]
Per-country logits: (B, 4, 84)   [soft country targets per strategy; 4 = # strategies]
```

**Why:**
- Action space is **~4500 per position** (111 cards × up to 40 countries × 1-2 modes per card)
- Flat classification would require 4500-dim head = 256×4500 ≈ 1.1M params just for one head
- Factorized reduces to 111 + 5 + 336 = 452 dims = 256×452 ≈ 116K params
- **Matches game structure:** card choice precedes mode, which precedes country allocation

**During inference:**
1. Sample top-K cards by probability
2. For each, sample legal modes
3. For each (card, mode), sample countries via learned strategy mixture
4. Enumerate actions, pick top-K by combined probability

---

## Value Head Design

Separate value branch after trunk:

```
trunk_hidden (B, 256)
  → Linear(256 → VALUE_BRANCH_HIDDEN=128)
  → ReLU
  → Linear(128 → 1)
  → Tanh  [scale to [-1, 1]]
```

**Why separate:**
- Avoids capacity competition between policy and value objectives
- Value is **USSR-perspective scalar** (positive = USSR advantage, negative = US advantage)
- Tanh output forces calibration to [-1, 1] range (soft target via MSE during training)

---

## Dropout & Regularization

- **No per-block dropout** (removed; cut training time ~30% with no quality loss at 447K params)
- **Trunk-level dropout** only: `nn.Dropout(p=0.1)` at trunk input
- **Primary regularization:** weight_decay=1e-4 + label_smoothing=0.05 (applied via dataset generation, not loss)

---

## Unused / Deprecated Architectures

The codebase also defines:
- `TSCountryEmbedModel` — not used in production (likely inferior to full embed or attn without explicit test)
- `TSCountryAttnModel` — too expensive (+25% time) for unclear gain on BC data

Future experiment: train all 5 on identical data split and compare.

---

## Lessons & Future Directions

1. **Parameter count is not the bottleneck:** Even at 547K (CountryAttn), still <200MB; WSL 4GB GPU rarely saturated at batch_size=8192.

2. **BC ceiling is data, not architecture:** Baseline at 447K plateaued at 18.5% win%; adding structural bias unlikely to break through without self-play or teacher search (Month 2).

3. **Factorized action model wins:** ~11× reduction in action head params vs flat classification; cleaner to sample from during MCTS.

4. **Value calibration matters:** vs-heuristic data causes +0.4-0.6 overconfidence on positive predictions. Self-play data is better calibrated (Month 2 Sec 8: Platt scaling).

5. **Next ablation:** Once Month 2 teacher search is complete, compare embedding variants on teacher-target + self-play mix. Structural bias may help more on harder positions.

---

## Code Locations

- Model definitions: `python/tsrl/policies/model.py`
- Training script: `scripts/train_baseline.py`
- Feature extraction: `python/tsrl/policies/learned_policy.py` (_extract_features, _normalize_influence_features)
- Benchmark script (uses any model): `scripts/benchmark_vf_mcts.py`
