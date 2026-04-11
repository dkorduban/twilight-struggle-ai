---
# Opus Analysis: JSD for Fixture Pruning
Date: 2026-04-11T12:37:00Z
Question: JSD is already implemented -- should we use it directly for fixture pruning? Is lineage a useful axis or a lazy heuristic?

## Executive Summary

JSD is fully implemented (`python/tsrl/policies/jsd_probe.py`), already integrated into `train_ppo.py`, and has a frozen 996-position probe set at `data/probe_positions.parquet`. Computing pairwise JSD for all 34 fixture models takes approximately 2-3 minutes on the RTX 3050 -- this is cheap enough to run before every PPO generation. The previous analysis incorrectly called JSD "expensive to implement" when the implementation already existed and was production-ready. Lineage is a lazy heuristic that happens to correlate with behavioral diversity but cannot detect same-lineage divergence or cross-lineage convergence. **Use JSD directly as the primary diversity axis for fixture pruning, with Elo tier as the strength axis. Drop lineage as a pruning input.**

## Findings

### JSD Implementation Status

The implementation is complete and battle-tested:

- **`python/tsrl/policies/jsd_probe.py`**: `ProbeEvaluator` class with `compare(model_a, model_b) -> ProbeMetrics`. Computes per-head JSD (card, mode, country) with proper legal-action masking, plus value MAE and top-1 agreement. Phase-stratified (early/mid/late) card JSD included.
- **`scripts/build_probe_set.py`**: Builds a stratified 1000-position probe set from rollout parquet. Already run; output at `data/probe_positions.parquet` (996 positions, well-distributed across turns 1-10).
- **`scripts/train_ppo.py`**: Already integrated -- `--probe-set`, `--probe-every`, `--probe-bc-checkpoint` CLI args are live. JSD vs previous checkpoint and vs BC baseline logged to W&B every N iterations.
- **`tests/python/test_jsd_probe.py`**: Unit tests exist and pass.

The `_jsd()` static method is numerically stable (log-sum-exp, clamped, normalized by log(2) to [0,1] range), handles masked legal actions correctly, and supports both raw-logit and already-probability inputs (for the country mixture-of-softmaxes head).

What exists today: pairwise model comparison on a frozen probe set. What is needed for fixture pruning: running this N*(N-1)/2 times to build a full distance matrix, then selecting a diverse subset. The core math and I/O are already done -- only the outer loop and selection algorithm are new.

### Lineage Axis Critique

Lineage (grouping models by version number ranges like "v8-v22 = early-gen, v44-v61 = late-gen") is a **lazy heuristic** with three fundamental problems:

1. **It assumes version distance implies behavioral distance.** This is plausible but unverified. Sequential PPO generations (v55 -> v56 -> v57) might converge to nearly identical policies if training signal is weak, making them behaviorally redundant despite being "different versions." Conversely, a single PPO run with high exploration noise might produce an iter_40 checkpoint that plays very differently from iter_80, but they would be classified as "same lineage."

2. **It cannot detect cross-lineage convergence.** If v17 (early-gen) and v48 (late-gen) happen to converge to similar strategies from different starting points, lineage says "diverse" but JSD says "redundant." This is a real risk in self-play training where Nash equilibria attract policies from different initializations.

3. **Lineage boundaries are arbitrary.** The v22-to-v44 gap in version numbers reflects a gap in scripted checkpoint availability (the v27-v43 era was excluded as corrupted), not a meaningful training branch point. Calling v22 and v44 "different lineages" is an artifact of what checkpoints survived, not a signal about behavioral diversity.

4. **It provides no gradation.** Lineage is categorical (early/mid/late), not continuous. JSD gives a precise 0-1 distance between any pair. With lineage, v8 and v22 are "same group" despite being 14 generations apart, while v22 and v44 are "different groups" despite potentially playing similarly.

**Where lineage is useful:** As a zero-cost tie-breaker when JSD is unavailable or when two models have identical JSD to everything else. It is also useful as a sanity check -- if JSD says two models from very different lineages are identical, that is worth investigating.

**Verdict:** Lineage is a poor man's JSD. Now that JSD is implemented and cheap, use JSD directly. Keep lineage only as a diagnostic label, not a pruning axis.

### Concrete JSD Pruning Algorithm

**Step 0: Compute pairwise JSD matrix (one-time, ~3 min)**

```python
from tsrl.policies.jsd_probe import ProbeEvaluator
import torch, json, itertools
from pathlib import Path

probe = ProbeEvaluator("data/probe_positions.parquet", device="cuda")

# Load all fixture models (scripted .pt files)
fixture_dir = Path("data/checkpoints/scripted_for_elo")
models = {}
for p in sorted(fixture_dir.glob("*_scripted.pt")):
    name = p.stem.replace("_scripted", "")
    models[name] = torch.jit.load(str(p), map_location="cuda")

names = sorted(models.keys())
N = len(names)
jsd_matrix = [[0.0] * N for _ in range(N)]  # card_jsd as primary

for i, j in itertools.combinations(range(N), 2):
    m = probe.compare(models[names[i]], models[names[j]])
    jsd_matrix[i][j] = m.card_jsd  # or weighted: 0.6*card + 0.3*mode + 0.1*country
    jsd_matrix[j][i] = jsd_matrix[i][j]
```

For N=34 models: 34*33/2 = 561 pairs. Each `compare()` call does 2 forward passes over 996 positions in batches of 256 = ~8 batches * 2 models = 16 forward passes. Total: 561 * 16 = ~8,976 forward passes of batch-256. On RTX 3050 at ~5K-10K samples/sec, this is 90-180 seconds. Add model loading overhead (~0.5s each * 34 = 17s). **Total: 2-3 minutes.**

**Step 1: Greedy maximum-diversity selection (the pruning algorithm)**

Use a greedy facility-location / max-min diversification algorithm:

```python
def select_diverse_fixtures(
    jsd_matrix: list[list[float]],
    names: list[str],
    elo: dict[str, float],
    K: int = 14,
    mandatory: set[str] = {"heuristic"},
    elo_tiers: int = 4,
) -> list[str]:
    """Select K fixtures maximizing JSD diversity with Elo tier coverage."""
    import numpy as np

    N = len(names)
    D = np.array(jsd_matrix)
    name_to_idx = {n: i for i, n in enumerate(names)}

    # Mandatory seeds
    selected = [name_to_idx[n] for n in mandatory if n in name_to_idx]

    # Ensure Elo tier coverage: pick highest-JSD-sum model from each tier
    elo_vals = [elo.get(names[i], 0) for i in range(N)]
    tier_edges = np.quantile(elo_vals, np.linspace(0, 1, elo_tiers + 1))
    tier_edges[-1] += 1  # include max

    for t in range(elo_tiers):
        tier_members = [i for i in range(N)
                        if tier_edges[t] <= elo_vals[i] < tier_edges[t+1]
                        and i not in selected]
        if not tier_members:
            continue
        # Pick the one most different from already-selected
        if selected:
            best = max(tier_members, key=lambda i: min(D[i][s] for s in selected))
        else:
            best = max(tier_members, key=lambda i: D[i].sum())
        selected.append(best)

    # Greedy max-min fill: repeatedly add the model most distant from current set
    while len(selected) < K and len(selected) < N:
        remaining = [i for i in range(N) if i not in selected]
        if not remaining:
            break
        best = max(remaining, key=lambda i: min(D[i][s] for s in selected))
        selected.append(best)

    return sorted(names[i] for i in selected)
```

This is a standard greedy diversification that:
1. Seeds with mandatory models (heuristic).
2. Ensures at least one model per Elo quartile (strength coverage).
3. Fills remaining slots by max-min distance (behavioral diversity).

**Why max-min, not clustering?** Hierarchical clustering groups similar models together, then picks one per cluster. This is equivalent to max-min selection but harder to tune (how many clusters?). Max-min is simpler, deterministic, and directly optimizes the objective we care about: the minimum pairwise JSD in the selected set.

**Step 2: Integration into ppo_loop_step.sh**

Add a `scripts/select_league_fixtures.py` that:
1. Loads the pre-computed JSD matrix (cached as `data/jsd_fixture_matrix.json`).
2. Loads `results/elo_full_ladder.json` for Elo values.
3. Runs the selection algorithm.
4. Outputs the fixture list to stdout (one path per line).

In `ppo_loop_step.sh`, replace the current "all good versions" fixture loop with:

```bash
LEAGUE_FIXTURES=$(uv run python scripts/select_league_fixtures.py \
    --jsd-matrix data/jsd_fixture_matrix.json \
    --elo-ladder results/elo_full_ladder.json \
    --K 14 \
    --mandatory heuristic \
    --exclude "$NEXT" \
    --checkpoint-dir data/checkpoints/scripted_for_elo)
```

**Step 3: JSD matrix update schedule**

The JSD matrix only needs recomputation when new models are added to the fixture pool (i.e., after each PPO generation completes and its scripted checkpoint is exported). Cost is incremental: adding 1 new model requires N pairwise comparisons (~34 * 2 forward passes * 996 positions = 5 seconds). Full recomputation from scratch: 2-3 minutes.

**Recommended schedule:** Recompute the full matrix after every Elo tournament update (already runs between PPO generations). The 2-3 minute cost is negligible compared to the ~2-hour PPO training and ~30-minute Elo tournament.

### Cost Analysis

| Operation | Time | Frequency |
|-----------|------|-----------|
| Full N*N JSD matrix (N=34) | 2-3 min | Once per new fixture pool |
| Incremental +1 model | ~5 sec | After each PPO gen |
| Selection algorithm | <1 sec | Before each PPO run |
| Model loading (34 scripted) | ~17 sec | Part of matrix computation |

**Compared to current approach (no pruning):** Zero compute cost, but 34 fixtures means each gets ~3% of training games. With 14 fixtures, each gets ~7% -- roughly 2x more signal per fixture per iteration.

**Compared to lineage-based pruning:** Same selection time (<1 sec), but lineage requires zero pre-computation while JSD requires 2-3 minutes. This 2-3 minute cost is trivially amortized against the hours of PPO training it informs.

**Memory:** 996 probe positions * batch_size=256 * 2 models in memory simultaneously. Peak GPU memory ~200MB above baseline. No concern on RTX 3050 (4GB).

## Conclusions

1. **JSD is already implemented, tested, and production-integrated.** The previous analysis was wrong to call it "expensive to implement" -- the ProbeEvaluator, probe set, and train_ppo.py integration all exist and work. The only missing piece is the outer N*N loop and selection script (~50 lines of new code).

2. **Pairwise JSD for 34 models costs 2-3 minutes on the RTX 3050.** This is negligible compared to PPO training time and should not be deferred. It can run as part of the Elo tournament step that already happens between generations.

3. **Lineage is a lazy heuristic that JSD strictly dominates.** Lineage correlates with behavioral diversity but cannot detect same-lineage convergence or cross-lineage redundancy. It provides categorical bins where JSD provides continuous distances. With JSD available at trivial cost, lineage should be demoted to a diagnostic label.

4. **The right algorithm is greedy max-min diversification with Elo tier seeding.** This is simpler and more principled than stratified Pareto selection with lineage bins. It directly optimizes behavioral spread while ensuring strength coverage.

5. **JSD should replace lineage as a diversity axis, not complement Pareto.** Pareto (strength frontier) + JSD (behavioral diversity) is the right 2-axis framework. Lineage adds no information that JSD does not already capture better.

6. **card_jsd is the primary diversity signal.** Card selection is the highest-entropy decision in Twilight Struggle and most sensitive to strategic differences. Mode and country JSD are useful secondary signals but card_jsd alone captures the majority of behavioral variation.

## Recommendations

1. **Write `scripts/compute_jsd_matrix.py`** (~80 lines): loads all scripted fixtures, runs pairwise ProbeEvaluator.compare(), outputs `data/jsd_fixture_matrix.json` with the N*N card_jsd matrix plus model names. Run it once now to validate.

2. **Write `scripts/select_league_fixtures.py`** (~60 lines): reads the JSD matrix + Elo ladder, runs greedy max-min selection with Elo tier seeding, outputs fixture paths. Replace the current all-versions loop in `ppo_loop_step.sh`.

3. **Add JSD matrix recomputation to the Elo tournament step** in `ppo_loop_step.sh`: after `run_elo_tournament.py` completes, run `compute_jsd_matrix.py` with `--incremental` flag (only compute new pairs).

4. **Set K=14 as initial target**, matching the previous analysis. Validate by checking that the selected set has min pairwise JSD > 0.05 (models are meaningfully different) and covers all 4 Elo quartiles.

5. **Log the JSD matrix as a W&B artifact** for historical tracking. This lets you see how fixture behavioral diversity evolves across generations.

6. **Drop lineage from the pruning algorithm entirely.** If you want to track it for diagnostics, add a `lineage` column to the Elo ladder JSON, but do not use it for selection decisions.

7. **After the first JSD matrix is computed, validate the lineage assumption.** Check whether models within a "lineage group" (e.g., v44-v50) actually have low pairwise JSD, and whether cross-lineage models (e.g., v17 vs v48) actually have high JSD. This answers the empirical question of whether lineage was ever a useful proxy.

## Open Questions

1. **Should the JSD diversity signal use card_jsd alone, or a weighted combination of card/mode/country/value?** Card is highest-entropy, but a model that plays the same cards with different mode choices (event vs influence) is genuinely diverse. Suggested starting point: `diversity = 0.6*card_jsd + 0.25*mode_jsd + 0.15*country_jsd`.

2. **Should the probe set be updated when the training data distribution shifts significantly?** The current probe set was built from `ppo_rollout_combined` data. If future generations explore very different game states, the probe set might not cover the relevant decision points. Low priority -- the current 996 positions span all turns and DEFCON levels.

3. **Is there a minimum JSD threshold below which two models are "effectively identical" for training purposes?** If two models have card_jsd < 0.01, they probably produce indistinguishable training signal. This threshold could be used for automatic deduplication.

4. **Should the selection be deterministic or stochastic?** Greedy max-min is deterministic. An alternative is to sample fixtures proportional to their minimum distance from the current set (like farthest-point sampling with temperature). Deterministic is simpler and preferred unless there is evidence that stochastic selection helps.
---
