---
# Opus Analysis: Measuring Policy Divergence Between Model Versions
Date: 2026-04-09 UTC
Question: Is KL divergence at frozen positions a good way to measure vX vs vY difference?

## Executive Summary

KL divergence at a frozen probe set is a strong complement to the current H2H Elo approach, not a replacement. It is deterministic, cheap (~2 seconds for 1000 positions on GPU vs ~10 minutes for 400 H2H games), and sensitive to changes that H2H win rates cannot resolve at practical sample sizes. However, it has real failure modes: it is distribution-dependent (sensitive to which positions you evaluate on), asymmetric (KL(P||Q) != KL(Q||P)), and can miss behaviorally critical changes if the probe set does not cover the relevant game phases. The recommended approach is to compute **Jensen-Shannon divergence (JSD)** across all three masked heads (card, mode, country) on a curated probe set of 500-1000 positions stratified by turn, side, DEFCON, and phase. This gives a symmetric, bounded, deterministic similarity metric that can detect policy collapse, plateau, and regression faster than Elo. Implementation cost is roughly 150-200 lines and 2-3 hours of work.

## What to Compute KL On (Heads and Masking)

The model produces three factorized policy heads:

1. **Card logits** (111 dims): which card to play. Must be masked by the legal hand (card_mask, typically 5-9 cards hot).
2. **Mode logits** (5 dims): influence/coup/realign/space/event. Must be masked by mode_mask (depends on card + game state).
3. **Country logits** (86 dims, mixed probability): where to place influence/coup/realign. Must be masked by country_mask (depends on mode + rules). Only relevant for modes 0/1/2; modes 3/4 (space/event) have no country target.

Plus a value head (scalar), which is not a policy head but is also worth comparing.

**Recommendation**: compute divergence on all three heads independently, then combine. Each head captures different information:
- Card KL catches strategic drift (different card priorities)
- Mode KL catches tactical drift (e.g., shifting from coup-heavy to influence-heavy play)
- Country KL catches positional drift (e.g., focusing on different regions)

**Critical masking requirement**: You MUST apply the same legal mask to both models before computing softmax/KL. If model A sees 6 legal cards and model B sees 6 legal cards, the distributions are over those 6 cards only. Without masking, you are comparing distributions over illegal actions, which is meaningless noise. The existing codebase already has `card_mask`, `mode_mask`, and `country_mask` per decision point (see `Step` dataclass in train_ppo.py, lines 154-187), so the masks are available.

**Value head**: additionally compute mean absolute difference and correlation of value predictions. This is not KL but is a useful complementary signal (value drift often precedes policy drift in PPO).

## Constructing a Good Probe Position Set

A good probe set must satisfy:

1. **Diversity of game phase**: turns 1-3 (early), 4-6 (mid), 7-10 (late). Roughly equal representation.
2. **Both sides**: roughly 50% USSR, 50% US positions.
3. **DEFCON spread**: positions at DEFCON 2, 3, 4, 5. DEFCON 2 positions are critical because they restrict coup/event options.
4. **Action round spread**: headline (AR 0) plus AR 1-7.
5. **VP spread**: positions where USSR is ahead, tied, and behind.
6. **Legal hand diversity**: positions with different hand sizes and card mixes (early/mid/late war cards).
7. **Reachability**: every position must be reachable from a real game, not synthetically constructed. Using positions sampled from actual self-play parquet files is the cleanest approach.

**Practical construction**:
- Sample 1000 positions from existing self-play parquet files (there are 80+ parquet files available in `data/selfplay/`).
- Stratify: ~100 positions per turn bucket (T1-3, T4-6, T7-10), ~50/50 side split.
- Filter to ensure DEFCON and VP diversity (reject samples that over-represent DEFCON 5 + VP near 0).
- Store as a single parquet file (`data/probe_positions.parquet`) with full state columns (influence, cards, scalars, masks).
- Freeze this file and never modify it. Append a hash to the filename or metadata for reproducibility.

**Source data**: the parquet files already contain `ussr_influence`, `us_influence`, `vp`, `defcon`, `turn`, `ar`, `phasing`, `actor_known_in`, `actor_possible`, `discard_mask`, `removed_mask`, plus hand/mask information. This is sufficient to reconstruct the full model input tensors.

## Failure Modes and Limitations of KL

### 1. Distribution dependence
KL divergence depends heavily on which positions you evaluate. Two models might agree perfectly on "boring" mid-game positions but diverge dramatically on critical late-game scoring positions or DEFCON-2 situations. If your probe set over-represents boring positions, KL will understate the real difference. **Mitigation**: stratify the probe set and report per-turn-bucket KL.

### 2. KL asymmetry
KL(P||Q) != KL(Q||P). If model P assigns probability 0.001 to an action and model Q assigns 0.5, KL(P||Q) is moderate but KL(Q||P) is enormous. This means "how different is vX from vY" gives a different answer depending on which model is the reference. **Mitigation**: use Jensen-Shannon divergence (JSD = 0.5 * KL(P||M) + 0.5 * KL(Q||M), where M = 0.5*(P+Q)). JSD is symmetric, bounded in [0, ln(2)], and more interpretable.

### 3. Sensitivity to near-zero probabilities
KL diverges to infinity when one model assigns zero probability and the other does not. After masking illegal actions, all remaining actions have non-zero softmax probability, so this is not a problem in practice. But if a model is very sharp (temperature < 1 effectively), tiny probability actions can dominate KL. **Mitigation**: use JSD, which is always finite.

### 4. Does not capture behavioral impact
Two models can have high KL but identical top-1 actions (they disagree on the tail but not the argmax). Conversely, two models can have low KL but different top-1 actions (both are nearly uniform but one slightly favors card A and the other card B). KL does not weight "how much does this disagreement matter for game outcomes." **Mitigation**: report top-1 agreement rate alongside KL/JSD as a complementary metric.

### 5. Country head special case
The country logits are already a probability mixture (not raw logits), and country targets are multi-hot with repeats (for influence allocation). KL on the country distribution is meaningful for single-target modes (coup/realign) but less interpretable for multi-ops influence allocation where the model distributes ops across multiple countries. **Mitigation**: for influence mode, compare the country probability vectors directly. For coup/realign, compare the distributions. Report country KL only for positions where a country target is relevant (modes 0/1/2).

### 6. Probe set staleness
As training progresses, the models visit different regions of the state space. A probe set sampled from v10 games might not cover the states that v50 actually encounters. **Mitigation**: periodically regenerate the probe set (e.g., every 20 versions), but keep old probe sets for longitudinal comparison.

## Better Alternatives or Complements

| Metric | Pros | Cons | Recommended? |
|--------|------|------|-------------|
| **KL divergence** | Standard, well-understood, sensitive | Asymmetric, unbounded, distribution-dependent | Use JSD variant |
| **Jensen-Shannon divergence (JSD)** | Symmetric, bounded [0, ln(2)], finite even with zeros | Still distribution-dependent | **Yes, primary metric** |
| **Top-1 agreement rate** | Intuitive ("do they pick the same card/mode?"), directly behavioral | Ignores distribution shape; two 51/49 models that disagree have 0% agreement | **Yes, complement** |
| **Top-3 agreement rate** | Less noisy than top-1 for card head (where top-3 matters for play quality) | Still binary | Yes, for card head |
| **Total variation (TV) distance** | Bounded [0,1], symmetric, easy to interpret | Less sensitive to tail differences than KL/JSD | Optional |
| **BC cross-entropy (model A's loss on model B's actions)** | Directly measures "how surprised is A by B's choices" | Requires action labels, not just distributions | Useful but heavier |
| **Value head MAE/correlation** | Captures value function drift independently of policy | Not a policy metric | **Yes, always include** |
| **Weight-space distance (L2 norm of param diff)** | Trivially cheap to compute | Does not account for reparameterization equivalences; two models with identical behavior can have very different weights | Weak signal, include as sanity check |
| **H2H win rate** | Ground truth for "who is stronger" | Noisy (400 games ~ +/- 5%), expensive (10+ min), non-transitive | Keep as gold standard |

**Recommended metric suite**:
1. JSD per head (card, mode, country) at probe positions -- primary divergence metric
2. Top-1 agreement rate per head -- primary behavioral metric
3. Value head MAE and Spearman correlation -- value drift
4. Weight-space L2 distance -- sanity check / early warning
5. H2H Elo -- ground truth, run less frequently

## Stability and Sample Size

How many probe positions are needed for stable JSD estimates?

- **Card head** (111 dims, ~6-9 legal): JSD converges quickly because the effective support is small. 100 positions give a standard error of ~0.005 nats. 500 positions are ample.
- **Mode head** (5 dims, ~3-5 legal): very low-dimensional, converges with ~50 positions.
- **Country head** (86 dims, ~30-50 legal): higher-dimensional, needs more samples. 200-500 positions for stable estimates.
- **Overall**: **500 positions is the practical minimum, 1000 is comfortable, 2000+ is overkill**. The computation cost is negligible (two forward passes through the model per position, ~2ms each on GPU, so 1000 positions = ~4 seconds total).

For longitudinal tracking (JSD over training iterations), the stability of the probe set matters more than its size. Using the same frozen 1000 positions across all versions ensures that changes in JSD reflect real policy changes, not sampling noise.

**Bootstrap validation**: when first creating the probe set, compute JSD at a single model pair using the full 1000 positions, then subsample to 100, 200, 500 and check that the estimate is within 10% of the full-set value. If so, the set is stable.

## Implementation Sketch

```python
# scripts/compute_policy_divergence.py  (~150 lines)

"""Compute JSD / agreement metrics between two model checkpoints on frozen probe positions.

Usage:
    uv run python scripts/compute_policy_divergence.py \
        --model-a data/checkpoints/ppo_v40/ppo_best.pt \
        --model-b data/checkpoints/ppo_v50/ppo_best.pt \
        --probe-set data/probe_positions.parquet \
        --device cuda --out results/divergence_v40_v50.json
"""

# Core pseudocode:

def load_probe_set(path: str) -> list[dict]:
    """Load frozen probe positions from parquet. Each row -> input tensors + masks."""
    df = pl.read_parquet(path)
    positions = []
    for row in df.iter_rows(named=True):
        influence, cards, scalars = build_tensors(row)  # reuse extract_features logic
        card_mask, mode_mask, country_mask = build_masks(row)
        positions.append({
            "influence": influence, "cards": cards, "scalars": scalars,
            "card_mask": card_mask, "mode_mask": mode_mask,
            "country_mask": country_mask,
            "turn": row["turn"], "side": row["phasing"],
        })
    return positions

def compute_masked_jsd(logits_a, logits_b, mask):
    """JSD of two logit vectors after masking and softmax."""
    logits_a = logits_a.clone(); logits_a[~mask] = float("-inf")
    logits_b = logits_b.clone(); logits_b[~mask] = float("-inf")
    p = F.softmax(logits_a, dim=-1)
    q = F.softmax(logits_b, dim=-1)
    m = 0.5 * (p + q)
    jsd = 0.5 * F.kl_div(m.log(), p, reduction="sum") + \
          0.5 * F.kl_div(m.log(), q, reduction="sum")
    return jsd.item()

def compute_divergence(model_a, model_b, probe_set, device):
    results = {"card_jsd": [], "mode_jsd": [], "country_jsd": [],
               "card_agree": [], "mode_agree": [], "value_diff": []}
    for pos in probe_set:
        with torch.no_grad():
            out_a = model_a(pos["influence"].to(device), ...)
            out_b = model_b(pos["influence"].to(device), ...)

        # Card JSD
        card_jsd = compute_masked_jsd(
            out_a["card_logits"][0], out_b["card_logits"][0], pos["card_mask"])
        results["card_jsd"].append(card_jsd)

        # Top-1 agreement
        card_a = masked_argmax(out_a["card_logits"][0], pos["card_mask"])
        card_b = masked_argmax(out_b["card_logits"][0], pos["card_mask"])
        results["card_agree"].append(int(card_a == card_b))

        # Mode JSD, Country JSD, Value diff -- analogous
        ...

    return {k: {"mean": mean(v), "std": std(v)} for k, v in results.items()}
```

**Probe set generator** (~80 lines):
```python
# scripts/generate_probe_set.py
# Sample 1000 stratified positions from self-play parquet files
# Columns needed: influence, cards, scalars, masks, turn, ar, defcon, phasing
# Save as data/probe_positions.parquet
```

**Total implementation**: ~230 lines across two scripts. Estimated time: 2-3 hours including testing.

## Value Proposition vs Current H2H Approach

| Property | H2H Elo (current) | JSD at probe positions (proposed) |
|----------|-------------------|-----------------------------------|
| **Cost** | 400 games x 2 sides = ~10 min on GPU | 1000 forward passes x 2 models = ~4 seconds |
| **Determinism** | Stochastic (game randomness) | Deterministic (same probe set, same result) |
| **Resolution** | ~50 Elo points with 400 games (SE ~25) | Continuous, sub-1% changes detectable |
| **What it measures** | "Who wins more" (behavioral, end-to-end) | "How different are the policy distributions" (structural) |
| **Detects policy collapse** | Only after collapse causes win rate drop | Immediately (JSD -> 0 between consecutive versions) |
| **Detects plateau** | Elo stops changing (but high variance masks this) | JSD between consecutive versions trends to 0 |
| **Detects regression** | Win rate drops (noisy) | JSD increases vs baseline without direction info |
| **Transitivity** | Not guaranteed (A > B > C does not imply A > C) | Not applicable (divergence, not ranking) |
| **Tells you who is better** | Yes | No -- high JSD could mean improvement or regression |

**Key insight**: JSD tells you **how much** models differ, not **which is better**. It is a diagnostic tool for training health, not a replacement for Elo. The combination is powerful:
- JSD trending to 0 between iterations -> training has plateaued, change learning rate or data
- JSD large but Elo unchanged -> model is changing but not improving (possible circular drift)
- JSD small but Elo dropping -> model is stuck near a local minimum that is slowly degrading (value drift more likely than policy drift)
- JSD large and Elo improving -> healthy learning

**Policy collapse detection**: the project has already experienced policy collapse from echo-chamber self-play (v11/v12 regression, per MEMORY.md). JSD between consecutive PPO iterations would have caught this immediately -- if vN+1 has near-zero JSD from vN while Elo is stagnant, the model has stopped learning. If JSD from the BC baseline is also near-zero, the model never left the initial distribution.

## Conclusions

1. KL divergence at frozen positions is a sound idea, but **Jensen-Shannon divergence (JSD) is strictly better** for this use case: symmetric, bounded, and avoids the infinity issues of raw KL.

2. The approach fills a genuine gap in the current evaluation stack. H2H Elo is the only model comparison tool, and it is expensive (10 min), noisy (SE ~25 Elo at 400 games), and unable to detect policy collapse or plateau until they affect win rates.

3. The three-head factorized model is well-suited for per-head divergence analysis. Card JSD reveals strategic drift, mode JSD reveals tactical drift, country JSD reveals positional drift. Reporting these separately is more informative than a single aggregate number.

4. Legal-action masking is non-negotiable. The masks are already computed per decision point and available in the parquet data. Computing JSD on unmasked logits would be meaningless.

5. The probe set should be sampled from real self-play games (not synthetically constructed), stratified by turn/side/DEFCON/VP, and frozen for reproducibility. 500-1000 positions are sufficient; more is cheap but unnecessary.

6. Value head comparison (MAE + correlation) should always be included alongside policy JSD, as value drift and policy drift provide independent diagnostic signals.

7. Weight-space L2 distance is near-free to compute and provides a useful sanity check, but should not be relied on as a primary metric.

## Recommendations

1. **Implement JSD + top-1 agreement as the primary divergence metrics.** Use the implementation sketch above. Target: ~230 lines, 2-3 hours.

2. **Generate and freeze a probe set of 1000 positions** from the existing self-play parquet corpus, stratified by turn, side, DEFCON, and VP. Store as `data/probe_positions.parquet`.

3. **Integrate into the PPO training loop.** Every K iterations (e.g., K=10), compute JSD between the current model and (a) the previous checkpoint, (b) the BC baseline. Log to W&B. This gives a real-time training health signal at negligible cost.

4. **Do not replace H2H Elo.** JSD tells you "how different" but not "which is better." Keep Elo as the gold standard for ranking, but run it less frequently (every 20-50 iterations instead of every 10) since JSD now provides early warning.

5. **Report per-turn-bucket JSD** (early/mid/late war) in addition to the aggregate. This helps diagnose whether drift is concentrated in a specific game phase (e.g., "the model changed its late-war play but not its opening").

6. **Periodically regenerate the probe set** (every ~20 PPO versions) to avoid staleness, but keep old probe sets for longitudinal comparison.

## Open Questions

1. **Country head semantics**: the country logits are a probability mixture, not raw logits. Should JSD be computed on the probabilities directly, or on the underlying strategy logits (country_strategy_logits, shape (4, 84))? The strategy logits are richer but harder to compare across architectures.

2. **Headline phase positions**: headline decisions have a different structure (no mode choice, just card selection). Should these be handled separately or excluded from the probe set?

3. **Weighting by game-theoretic importance**: should positions be weighted by some importance measure (e.g., value uncertainty, position criticality)? This would make JSD more predictive of Elo but introduces subjectivity.

4. **Multi-model tracking**: for the full league (v1 through v80+), should we compute an NxN JSD matrix? This would show clustering and lineage patterns but is O(N^2) in forward passes. At 80 models x 1000 positions, this is still only ~160K forward passes (~5 minutes), so it is feasible.

5. **Threshold calibration**: what JSD threshold corresponds to "meaningfully different" vs "noise"? This needs empirical calibration by computing JSD between models with known Elo gaps (e.g., v10 vs v20, v20 vs v30) and correlating JSD with Elo difference.
