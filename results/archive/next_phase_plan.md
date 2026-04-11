# Next Phase Plan — 2026-04-07

## Executive Summary

- **League diversity is the #1 bottleneck**: PPO v3 league pool has zero real diversity (all checkpoints descend from v2b with identical architecture, same BC ancestor). This limits the learning signal and risks convergence to a narrow Nash subspace. Fix this first.
- **The heuristic benchmark is saturated at ~89%**: Further training produces real H2H improvements that the heuristic WR cannot measure. We need a fast proxy metric that discriminates beyond the ceiling.
- **Architecture gains are available but risky mid-training**: The biggest bang-for-buck architectural improvements (scoring urgency features, opponent hand estimates) require C++ feature changes. They should be validated on a fixed BC dataset before injecting into PPO.
- **Engine is feature-complete for all 111 cards**: No missing card implementations. The main engine issues are labeling bugs (Wargames/Europe control end_reason) and VP reward shaping inaccuracy, which affect training signal quality.
- **Recommended sequence**: (1) Fix end_reason + VP shaping bugs now (small, high-impact). (2) Implement league diversity mechanisms. (3) Add fast proxy metric. (4) Architecture experiments on BC, then distill into PPO.

---

## 1. League Diversity

### Current state

The league pool at `/data/checkpoints/league_v3/` contains checkpoints saved every 20 iterations, all from a single PPO v3 run that itself descends from PPO v2b (from PPO v1, from BC v106_cf_gnn_s42). The sampling distribution in `sample_league_opponent()` (`scripts/train_ppo.py`, line 706-724):

```
20% heuristic (anchor)
50% latest checkpoint (most recent iter_NNNN.pt in league dir)
30% random past checkpoint from pool
```

**Why this lacks diversity:**
1. All pool members share the same architecture (`TSControlFeatGNNSideModel`), same BC initialization, same training trajectory. Policy KL between consecutive checkpoints is likely small (~0.02-0.05 per 20 iters based on W&B KL logs).
2. The 50% "latest" allocation means half the training signal comes from near-self-play, which converges faster but narrows the explored strategy space.
3. There are no **exploiter agents** that specifically target weaknesses in the current best policy.
4. No mechanism to retire dominated checkpoints or promote strong challengers.

### Measurement approach

Before adding diversity, we need to quantify how similar current pool members actually are. Three complementary metrics:

**A. Policy KL on a fixed state set (cheapest, most informative)**
- Collect 500 states from a fixed seed rollout (store as tensors).
- For each pair of pool checkpoints, compute `KL(pi_a || pi_b)` averaged over the state set.
- If average KL < 0.05, checkpoints are policy-redundant.
- Implementation: ~50 lines in a new `scripts/league_diversity.py`. Uses existing `_export_temp_model` + forward pass. Run time: <5s per pair.

**B. H2H win matrix (most reliable, expensive)**
- Run `benchmark_model_vs_model_batched` between all pairs (100 games each).
- With N pool members, N*(N-1)/2 matchups. For N=10, that's 45 matchups * 100 games * ~0.05s/game = ~225s total.
- Derive a full BayesElo rating and identify redundant members (Elo within 20 of each other).

**C. Strategy fingerprinting (cheapest behavioral metric)**
- Use `collect_policy_stats()` (already in `train_ppo.py` line 1126) on each checkpoint.
- Compare mode distributions, region preferences, and split patterns across checkpoints.
- If two checkpoints have nearly identical strategy fingerprints, they're redundant.

**Recommended**: Run (A) first to identify the scale of the problem. If KL < 0.05 across all pairs, diversity is essentially zero and we need structural fixes.

### Concrete fixes (ranked by impact/effort)

**Fix 1: Diverse initialization seeds (HIGH IMPACT, LOW EFFORT)**
- Train 2-3 additional BC-to-PPO runs with different random seeds, different BC checkpoints (v99_cf_s7, v99_cf_s42), and/or different architectures (TSControlFeatModel without GNN).
- Add these as founding members of the league pool.
- **Why**: Different BC starting points create fundamentally different strategy basins. This is how AlphaGo league training works — the "main agent" trains alongside "exploiter agents" initialized from different points.
- **Effort**: Start a PPO v1-equivalent run (vs heuristic, 200 iters) from a different BC checkpoint. ~6 hours of GPU time. Then add the checkpoints to the league pool.
- **Implementation**: No code changes needed. Just run `train_ppo.py --checkpoint data/checkpoints/v99_cf_1x95_s7/baseline_best.pt --out-dir data/checkpoints/ppo_alt_seed/ ...` and copy milestones to `league_v3/`.

**Fix 2: Exploiter mechanism (HIGH IMPACT, MEDIUM EFFORT)**
- Periodically (every 100 iters), fork the current best checkpoint and train a short "exploiter" run (50 iters) that plays exclusively against the current best (no pool, no heuristic). The exploiter discovers weaknesses in the current policy.
- Add the exploiter's best checkpoint to the pool.
- **Why**: This is the core mechanism from AlphaStar's league training. Without exploiters, the pool converges to a single strategy.
- **Implementation**: Add `--exploit-target <path>` flag to `train_ppo.py` that uses `rollout_model_vs_model_batched` against a fixed opponent. ~30 lines of code. The orchestration (when to fork) can be a simple bash script or Snakemake rule.

**Fix 3: Pool pruning and prioritized sampling (MEDIUM IMPACT, MEDIUM EFFORT)**
- Replace uniform-random 30% with **prioritized sampling** based on H2H results.
- Opponents that the current model struggles against (< 60% WR) get higher sampling weight.
- Prune checkpoints that the current model beats > 80% (they provide no learning signal).
- **Implementation**: Modify `sample_league_opponent()` to read a `league_elo.json` file (maintained by periodic H2H evaluation). Weight sampling by `1 / (win_rate + 0.1)` so harder opponents appear more often. ~50 lines in `train_ppo.py`.

**Fix 4: Architecture diversity in pool (MEDIUM IMPACT, HIGH EFFORT)**
- Train a pool member with `TSControlFeatModel` (no GNN) or `TSCountryAttnModel` (attention).
- Different architectures develop different blind spots, providing genuine strategic diversity.
- **Why**: Even with identical training data, different inductive biases produce different policies.
- **Effort**: Requires re-running BC training + PPO from scratch with a different architecture. ~12h GPU.

### Implementation details

**Immediate (this week):**
1. Run `league_diversity.py` (new script) to measure KL between existing pool members.
2. Start a PPO run from `v99_cf_1x95_s7` with seed=300000 (different basin).
3. Add that run's milestones to league pool once it reaches iter 60+.

**Next week:**
4. Implement exploiter fork mechanism.
5. Implement prioritized sampling.

**Changes to `scripts/train_ppo.py`:**
- `sample_league_opponent()` line 706: Add optional `elo_file` parameter. If provided, read opponent Elo ratings and sample proportional to `max(0, 1 - win_rate_vs_current)`.
- Add `--league-exploit-target` flag: when set, all non-heuristic games use `rollout_model_vs_model_batched` against this fixed target instead of pool sampling.
- Add `--league-diversity-seed` flag: periodically export a fresh checkpoint initialized from BC + short PPO to the pool.

---

## 2. Fast Proxy Metric

### Why current benchmark fails

The 500-game heuristic benchmark (`run_benchmark()` at `train_ppo.py` line 1343) has two problems:

1. **Speed**: ~50s per run (1000 games total, 500 per side). Acceptable for milestone checks every 20 iters, but too slow for architecture A/B tests where we want dozens of comparisons.

2. **Discrimination ceiling**: At 88.7% combined WR (PPO v3 iter 80), we're within ~1% of the theoretical ceiling against the Nash-temp heuristic. The experiment log shows heuristic WR fluctuating between 83-89% for checkpoints that differ by 50+ BayesElo points (e.g., v2b iter140 = 83.6% WR but 1841 BayesElo vs iter120 = 84.6% WR but 1776 BayesElo). **Heuristic WR is noisy and non-monotonic at this level.**

3. **H2H alternative**: `benchmark_model_vs_model_batched` is the correct metric but requires a reference opponent, and each matchup (200 games) takes ~20s. Not fast enough for architecture search.

### Candidate proxies (with pros/cons)

| Proxy | Speed | Discriminating? | Correlates with strength? | Implementation |
|-------|-------|----------------|--------------------------|----------------|
| **BC loss on fixed dataset** | ~2s for 10k samples | High (continuous loss) | Medium — BC loss can diverge from play strength | Need fixed eval dataset |
| **Policy entropy on fixed states** | ~1s | Low (noisy) | Weak — lower entropy can mean either stronger or degenerate | Already logged |
| **KL divergence vs reference model** | ~2s | Medium | Unknown — needs calibration | New, ~30 lines |
| **Rollout game length distribution** | ~10s (200 games) | Medium | Weak | Already collected |
| **Value head accuracy on fixed games** | ~5s | Medium-High | Medium — value accuracy predicts play quality | Need labeled states |
| **Rollout VP spread at terminal** | ~10s (200 games) | Low | Weak | Already collected |
| **Head-to-head mini-match** | ~5s (50 games) | High | Strong (direct comparison) | Existing API |

### Recommended approach: Two-tier proxy system

**Tier 1 (screening, <3s): BC-style loss on a fixed evaluation set**

Create a fixed evaluation dataset of ~5,000 states from PPO v3 rollouts (diverse positions from turns 1-10, both sides). For each state, record the "expert" action (from the strongest checkpoint). Compute:
- `card_cross_entropy`: CE loss on card head predictions
- `mode_accuracy`: fraction of modes matching expert
- `value_mae`: mean absolute error of value head vs actual game outcome

This runs in <3s on GPU and provides a continuous signal. Use it to screen architecture candidates: if BC-loss is worse, the architecture is not worth a full benchmark.

**Tier 2 (confirmation, ~5-10s): Mini H2H match (50 games)**

For candidates that pass Tier 1, run a quick 50-game H2H match against the current best checkpoint using `benchmark_model_vs_model_batched`. At 50 games, statistical power is limited (need ~60% WR for p<0.05), but it catches large regressions.

### Implementation

**Fixed evaluation set** (`scripts/build_eval_set.py`):
```python
# Collect states from PPO v3 rollouts with their outcomes
# Save as: data/eval/proxy_eval_5k.pt
# Contains: influence, cards, scalars, expert_card_idx, expert_mode_idx, game_outcome
```

**Proxy metric function** (add to `scripts/train_ppo.py` or separate `scripts/proxy_metric.py`):
```python
def compute_proxy_metric(model, eval_set_path, device) -> dict:
    """~2s on GPU. Returns card_ce, mode_acc, value_mae."""
    ...
```

**Integration**: Call after each architecture experiment. Log to W&B alongside heuristic WR and H2H Elo. Over time, calibrate which proxy thresholds predict real strength gains.

---

## 3. Architecture Improvements

### Current architecture summary

**Best model**: `TSControlFeatGNNSideModel` (`model.py` line 1358)

```
Encoders:
  influence_encoder_flat: Linear(172 -> 128)  # raw influence counts
  influence_encoder_embed: ControlFeatGNNEncoder  # per-country MLP + 2-round GNN + regional pooling
  card_encoder: Linear(448 -> 128)  # flat binary mask encoding
  scalar_encoder: Linear(39 -> 64)  # 11 base scalars + 28 region scoring scalars
  side_embed: Embedding(2, 32)  # USSR/US learned embedding

Trunk:
  Linear(352 -> 256) + 2x ResidualBlock(256)  # 352 = 128+128+64+32

Policy heads:
  card_head: Linear(256 -> 111)
  mode_head: Linear(256 -> 5)
  strategy_heads: Linear(256 -> 4*86=344)  # K=4 mixture-of-softmaxes
  strategy_mixer: Linear(256 -> 4)

Value heads (per-side):
  value_branch_ussr: Linear(256 -> 128) + Linear(128 -> 1)
  value_branch_us: Linear(256 -> 128) + Linear(128 -> 1)
```

**Feature dimensions**: influence(172) + cards(448) + scalars(11) + region_scalars(28) = 659 raw input dims.

**What the model sees**:
- Per-country: raw influence counts, static features (stability, BG, region), control status, 2-hop GNN neighborhood
- Cards: binary masks for hand, possible, discard, removed (4 x 112 = 448 flat bits)
- Scalars: VP/20, DEFCON/4, milops, space race, china, turn/10, AR/8, side

**What the model does NOT see**:
1. **Scoring urgency**: Which scoring cards are still in the draw pile? How many APs remain before the turn ends? (The model has `turn` and `ar` but not "how many APs until cleanup" or "has Europe Scoring been played this turn")
2. **Opponent hand estimate**: The model only sees its own hand. In competitive play, card counting (tracking which cards the opponent might hold based on discard/removed) is critical.
3. **Active effects**: Bear Trap, Quagmire, Flower Power, CMC, SALT, etc. — these are encoded as booleans in PublicState but NOT passed to the model via `nn_features.cpp`. The model must infer them from indirect signals.
4. **Scoring potential per region**: How many VP would a scoring card yield right now? (Partially addressed by the 28 region scalars, but not the actual VP delta.)
5. **Card-specific features**: The flat 448-dim card encoder loses structural information. CardEmbedEncoder exists but isn't used in the GNN model.
6. **Game phase**: Headline vs action round vs event resolution. Currently implicit in AR.

### Tier 1 improvements (highest impact)

**T1.1: Active effects as explicit scalar features (HIGH IMPACT, LOW EFFORT)**
- **What**: Add ~15 boolean scalars for active game effects: `bear_trap_active`, `quagmire_active`, `flower_power_active`, `cmc_active`, `salt_active`, `norad_active`, `north_sea_oil_extra_ar`, `glasnost_extra_ar`, `shuttle_diplomacy_active`, `formosan_active`, `iran_hostage_crisis_active`, `awacs_active`, `chernobyl_blocked_region` (onehot 7), `red_scare_active` (per-side).
- **Why**: These effects dramatically change legal moves and optimal strategy. The model currently must infer them from indirect signals, which is lossy.
- **Impact estimate**: +2-5pp heuristic WR, possibly more in H2H where active effects create asymmetric information advantages.
- **Effort**: ~1 hour. Add fields to `fill_scalars()` in `nn_features.cpp`, update `kScalarDim`, update Python `SCALAR_DIM` constant, retrain.
- **Data format change**: `SCALAR_DIM` increases from 11 to ~28. Requires model retraining from BC (cannot fine-tune existing checkpoints).
- **Files to modify**: `cpp/tscore/nn_features.cpp` (fill_scalars), `cpp/tscore/nn_features.hpp` (kScalarDim), `python/tsrl/policies/model.py` (SCALAR_DIM), `scripts/train_ppo.py` (SCALAR_DIM).

**T1.2: Opponent hand card counting features (HIGH IMPACT, MEDIUM EFFORT)**
- **What**: Add a 112-dim `opponent_possible` mask to the card features. For each card not in our hand, not in discard, not removed: it might be in the opponent's hand. This is already available as `CardSet` logic in the C++ engine.
- **Why**: Card counting is fundamental to competitive TS play. Knowing the opponent can't hold Europe Scoring changes strategy completely.
- **Impact estimate**: +3-5pp in H2H strength. Less impact vs heuristic (which doesn't hold scoring cards intelligently).
- **Effort**: ~2 hours. Add 5th card mask slot to `fill_cards()` in `nn_features.cpp`. CARD_DIM goes from 448 to 560.
- **Data format change**: `CARD_DIM` increases. Requires model retraining.
- **Files**: `cpp/tscore/nn_features.cpp`, `cpp/tscore/nn_features.hpp`, `python/tsrl/policies/model.py`.

**T1.3: Scoring VP delta features (MEDIUM IMPACT, MEDIUM EFFORT)**
- **What**: For each of the 7 scoring regions, compute the actual VP delta that would result if that region were scored right now. Pass as 7 additional scalar features.
- **Why**: The model has region control fractions (28 scalars) but not the actual scoring output. The scoring function has complex tier logic (presence/domination/control + BG bonus + adjacency bonus) that the model must learn implicitly.
- **Impact estimate**: +1-3pp. The model already has regional control counts which capture most of this.
- **Effort**: ~3 hours. Call `score_region()` for each region in the feature extraction, pass results as scalars.
- **Files**: `cpp/tscore/nn_features.cpp`, `cpp/tscore/scoring.hpp`.

### Tier 2 improvements

**T2.1: CardEmbedEncoder in GNN model (MEDIUM IMPACT, LOW EFFORT)**
- Replace flat `Linear(448 -> 128)` card encoder with additive `CardEmbedEncoder + Linear` (same pattern as `TSCardEmbedModel`).
- Already implemented and tested. Just needs to be wired into `TSControlFeatGNNSideModel`.
- Adds structural inductive bias for card features (per-card static attributes like ops, era, side).

**T2.2: Deeper trunk (3 residual blocks) (LOW IMPACT, LOW EFFORT)**
- Currently 2 residual blocks. Add a 3rd. Parameter increase is modest (~66K).
- Quick to test. Use proxy metric to evaluate.

**T2.3: Attention over country tokens in place of GNN (UNKNOWN IMPACT, MEDIUM EFFORT)**
- `CountryAttnEncoder` already exists. Self-attention can capture longer-range dependencies than 2-hop GNN.
- BUT: the GNN won over attention in BC experiments (Phase 1 results). Worth re-testing with PPO.

**T2.4: Hand-conditioned country head (MEDIUM IMPACT, HIGH EFFORT)**
- Current country head ignores which card was selected. In TS, the optimal influence placement depends heavily on which card you're playing (e.g., playing a USSR event card as US means you want to place influence in specific defensive locations).
- Pass the selected card embedding into the country head as additional conditioning.
- Requires changes to the factorized action model architecture.

### Validation protocol

1. Train BC on the current dataset (nash_bcd_combined or equivalent) with the modified architecture. ~20 min.
2. Run proxy metric (Tier 1 from Section 2). If BC loss is worse, stop.
3. If BC loss improves, run 50-game H2H vs the current best BC checkpoint. If WR > 55%, proceed.
4. Run PPO from the new BC checkpoint for 100 iters. Benchmark at iter 20/40/60/80/100.
5. If PPO produces higher BayesElo than current best, adopt the architecture.

---

## 4. Engine Completeness

### Known gaps

**All 111 cards are implemented.** Cards are split between two files:
- `cpp/tscore/step.cpp` (`apply_event()`): Cards whose effects are state mutations without player interaction (85 cards)
- `cpp/tscore/game_loop.cpp` (`handle_interactive_event()`): Cards requiring player choice during resolution — Five Year Plan (5), Blockade (10), CIA Created (26), UN Intervention (32), Cambridge Five (36), Quagmire (45), Bear Trap (47), Missile Envy (52), Grain Sales (68), Ask Not (78), Our Man in Tehran (84), Star Wars (88), Terrorism (95), Aldrich Ames (101), Defectors (108)
- Promo cards 109-111: Per CLAUDE.md, these are intentionally NOT implemented for self-play/training (event effects excluded, IDs exist only for log parsing).

**No TODOs, FIXMEs, or stubs found in step.cpp.** The implementation appears complete.

### Priority fixes

**Fix 1: `end_reason()` mislabeling (HIGH PRIORITY, LOW EFFORT)**

File: `cpp/tscore/game_loop.cpp` lines 723-731.

```cpp
std::string end_reason(const PublicState& pub, std::optional<Side> winner) {
    if (pub.defcon <= 1) {
        return "defcon1";
    }
    if (winner.has_value()) {
        return "europe_control";  // BUG: assumes any winner = europe control
    }
    return "vp_threshold";
}
```

This function is called for ALL game-ending events (scoring card resolution, Wargames, coups that trigger VP threshold, etc.). When a game ends via Wargames (card 103, which gives opponent +6 VP), the winner is set but `end_reason` returns `"europe_control"` instead of `"wargames"`.

**Impact on training**: The `end_reason` field is used in game summaries (line 1608: `if (result.end_reason == "defcon1") ++summary.defcon1`) but NOT directly in the reward function. So this is a **logging/analysis bug, not a training bug**. However, it means game outcome statistics are wrong — some games labeled "europe_control" are actually Wargames wins.

**Fix**: Make `end_reason` context-aware. Either:
1. Add a `last_event_card_id` field to PublicState and check for card 103.
2. Pass end_reason as a parameter from the calling site (each game-ending code path knows why it ended).

Option 2 is cleaner. The calling sites already know the context:
- After scoring card: `"scoring"` (or `"europe_control"` only when `result.game_over` from Europe scoring)
- After Wargames: `"wargames"`
- After VP threshold: `"vp_threshold"`
- After DEFCON: `"defcon1"`
- After turn limit: `"turn_limit"`

**Effort**: ~30 minutes. Remove `end_reason()` function, set `.end_reason` explicitly at each GameResult construction site.

**Fix 2: VP reward shaping for Wargames (MEDIUM PRIORITY, LOW EFFORT)**

File: `scripts/train_ppo.py` line 455-466.

```python
def _compute_reward(result, side_int, vp_coef=0.0):
    ...
    vp_scaled = max(-1.0, min(1.0, result.final_vp / 20.0))
```

When a game ends via Wargames (card 103), the opponent receives +6 VP before the game ends. So `result.final_vp` already includes this +6 VP transfer. If PPO uses `--vp-reward-coef > 0`, the VP shaping component undervalues Wargames wins because the VP is post-transfer.

Example: USSR wins via Wargames. Before Wargames, VP = +4 (USSR ahead). Wargames gives US +6 VP, making final_vp = -2. The reward function sees final_vp = -2 and applies negative VP shaping even though USSR won.

**Impact**: PPO v3 uses `--vp-reward-coef 0.1`, so this affects 10% of the reward signal. For games ending via Wargames (which are rare in practice), the VP shaping component contradicts the win/loss signal.

**Fix**: Detect Wargames endings (via `end_reason == "wargames"` once Fix 1 is done) and use pre-transfer VP for shaping. Or simply set `vp_scaled = base` (i.e., +1/-1) for Wargames games.

**Fix 3: Europe control sentinel value in VP (LOW PRIORITY)**

`scoring.cpp` line 7: `constexpr int kGameWinEurope = 9999;` — Europe control is a game-ending event, not a VP value. The VP delta from `score_region(Region::Europe, ...)` never actually returns 9999 because the function returns early via `ScoringResult{.game_over = true}`. The sentinel is only used in the control-check comparison (line 199). This is not a bug — just a potential confusion source.

### Impact on training

The engine is functionally correct for training. The bugs affect:
1. **Game statistics accuracy** (end_reason mislabeling) — affects analysis but not learning
2. **VP reward shaping quality** (Wargames VP) — affects ~0.1 * (fraction of Wargames games) of the reward signal, which is negligible
3. **No missing card events** — all 108 playable cards (excluding 3 promos) have complete implementations

The engine has been validated through hundreds of thousands of PPO rollout games without crashes or assertion failures (after the Country ID 64 fix at PPO v1 iter 48). The DEFCON-1 rate has been brought to ~6% (documented in memory), and scoring VP regressions have been resolved.

---

## Recommended Sequence

### Week 1: Foundation fixes + diversity measurement

1. **Fix end_reason bug** in `game_loop.cpp` (~30 min). This is a quick correctness fix that improves logging quality.
2. **Fix Wargames VP shaping** in `train_ppo.py` (~15 min). Negligible impact but easy to fix alongside #1.
3. **Build league diversity measurement** (`scripts/league_diversity.py`) — compute policy KL matrix across pool members. This tells us how bad the diversity problem actually is. (~1 hour)
4. **Start alternative PPO run** from a different BC checkpoint (v99_cf_1x95_s7 or similar). Let it run for 100+ iters in the background. No code changes needed.

### Week 2: Architecture experiment infrastructure

5. **Build fixed evaluation set** for proxy metric (5k states from PPO v3 rollouts). (~1 hour)
6. **Implement proxy metric function** (BC loss on eval set + mini H2H). (~2 hours)
7. **Add active effects to scalar features** (T1.1) — train BC, validate with proxy metric. (~3 hours total)
8. If T1.1 shows improvement: start PPO from the new BC checkpoint.

### Week 3: League improvements + architecture experiments

9. **Add alternative checkpoint(s) to league pool** (from step 4). Measure pool diversity again.
10. **Implement prioritized league sampling** based on H2H results. (~2 hours)
11. **Add opponent hand counting features** (T1.2) if T1.1 was successful. Validate same way.
12. **Implement exploiter fork mechanism** if diversity measurement shows it's needed.

### Week 4: Integration + strength push

13. **Run PPO v4** with: fixed architecture, diverse league pool, prioritized sampling, fixed VP shaping.
14. **Full BayesElo evaluation** against all previous checkpoints.
15. **Assess whether to pursue T2 architecture changes** based on proxy metric calibration.

### Why this order

- **Fixes first** (end_reason, VP shaping): Tiny effort, removes noise from all future experiments.
- **Diversity before architecture**: The league diversity problem limits ALL future training. Even a perfect architecture won't help if the training signal is degenerate. Diverse opponents > better features.
- **Proxy metric before architecture experiments**: Without a fast discriminating metric, architecture experiments are expensive guesswork. Build the measurement tool first.
- **Architecture last**: Architecture changes require retraining from BC and are only valuable if the PPO training loop is healthy (diverse opponents, correct rewards, good measurement).
