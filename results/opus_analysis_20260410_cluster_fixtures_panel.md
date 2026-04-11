# Opus Analysis: Cluster-Based Fixtures and Eval Panel Design
Date: 2026-04-10
Question: Cluster-based opponent selection for H2H panel and league fixtures

## Executive Summary

Cluster-based opponent selection is theoretically appealing but practically unjustified for the current model lineage. All models v8-v22 share the same BC-to-PPO training lineage with monotonically increasing Elo (1942 to 2096). The cross-model win rate matrix shows near-perfect transitivity -- no model has a rock-paper-scissors advantage over another. This means there is effectively one cluster with a strength gradient, not meaningfully divergent playstyles. The complexity cost of defining, measuring, and maintaining clusters is not warranted.

For fixture management, the current setup (v8/v14/v19, fadeout at 50, heuristic at 10%) is close to optimal. The main recommendations are: (1) keep fixture count at 3, updating when the frontier moves 50+ Elo above the strongest fixture; (2) make heuristic an explicit fixture instead of a random coin flip; (3) do not grow fixtures unboundedly -- PFSP on past-self handles the "who is hardest" question for models within the current run; and (4) fixtures serve a different role than PFSP (diversity injection vs difficulty weighting), so they complement rather than replace each other.

## Findings

### Divergence clusters in current model lineage

**What would constitute a meaningful cluster?**
In multi-agent RL, divergence clusters arise when different training runs or branches develop qualitatively different strategies -- e.g., one agent specializes in early aggression while another plays positionally. In Twilight Struggle terms, this might mean:
- One model plays aggressively for VP via scoring cards while another prioritizes board control
- One model systematically dominates in Early War but collapses in Late War
- One model has a large USSR-vs-US asymmetry while another is balanced

**Do our models form meaningful clusters?**
No. The evidence from the Elo ladder is clear:

| Matchup | Win Rate (stronger) | Expected from Elo | Transitivity |
|---------|--------------------|--------------------|--------------|
| v8 vs v12 | 60.5% | ~58% | Yes |
| v12 vs v14 | 54.0% | ~52% | Yes |
| v14 vs v19 | 59.6% | ~59% | Yes |
| v19 vs v22 | 54.0% | ~52% | Yes |

The win rates closely track Elo predictions. There are no intransitivities (where a weaker model beats a stronger one in H2H despite lower Elo). This is the signature of a single lineage with monotonic improvement, not divergent strategies.

The one interesting signal: v24 and v25 are much weaker (1757 and 1820 Elo) with a large USSR/US asymmetry (v25: USSR=1915, US=1682). These represent a failed branch -- likely policy collapse from echo-chamber self-play, consistent with documented history. They do represent a genuinely different "cluster" but one we want to train *against* (via PFSP catching the asymmetry), not *emulate*.

**Cost of cluster detection:**
Defining clusters requires either (a) feature-space distance metrics on model weights/activations (expensive, unclear signal), (b) strategy fingerprints from game statistics (requires large sample sizes, domain-specific feature engineering), or (c) H2H intransitivity detection (requires O(N^2) matches, already done by the Elo tournament). Option (c) is the only practical one, and it already shows no meaningful clusters exist in the current lineage.

**Verdict:** Cluster-based selection adds complexity without benefit for the current single-lineage training setup. It would become relevant if the project runs multiple independent training branches (e.g., different architectures, different starting checkpoints, or different training objectives).

### Growing fixtures: benefits and costs

**Current setup:** 3 fixtures (v8, v14, v19) with fadeout at iteration 50.

**What happens with unbounded fixture growth (v8, v14, v19, v22, v27, v28...)?**

With mix_k=4 and 200 games/iter:
- Slot 0: self (50 games)
- Slots 1-3: sampled from pool (50 games each)

Fixtures compete with past-self checkpoints for slots 1-3. Each slot is sampled independently with probability proportional to combined_weights. More fixtures means each individual fixture gets fewer games on average.

At 3 fixtures + ~10 past-self checkpoints, the fixture pool is manageable. PFSP and recency weighting ensure the important ones get sampled. At 10+ fixtures, two problems emerge:

1. **Dilution:** Each fixture gets ~5 games/iter (or fewer), which is too few for reliable WR estimation. PFSP needs ~20 games per opponent to start adjusting weights (MIN_GAMES=10 per side). With 10 fixtures, it takes 2-4 iterations before PFSP can even begin to differentiate them. This creates a cold-start problem that grows linearly with fixture count.

2. **Redundancy:** Adjacent-Elo models (v19 and v22 are only 17 Elo apart) provide nearly identical training signal. Adding both as fixtures wastes slots that could go to more diverse opponents.

3. **PFSP weight collapse:** With many similar-difficulty opponents, PFSP weights become nearly uniform (since WR against all of them is similar), defeating the purpose of prioritized sampling.

**Sweet spot:** 3-4 fixtures is ideal for mix_k=4. This gives each fixture a reasonable chance of being sampled (~15-25% per non-self slot after PFSP weighting) while maintaining coverage across the Elo range.

**Update rule:** The current "update when frontier moves 50+ Elo above strongest fixture" is sound. A concrete rule:
- Keep 3 fixtures: one weak (bottom quartile), one mid (median), one strong (top quartile of available models)
- When the new frontier exceeds the strongest fixture by 50+ Elo, promote the strongest fixture to mid, drop the old mid, and add the new frontier as strongest
- Keep the weak fixture stable (v8 at 1942) as an anchor for floor-level difficulty

### Heuristic as fixture vs heuristic-pct

**Current mechanism:** Each non-self slot independently flips a coin with P=0.10 to play vs heuristic. Expected heuristic games per iteration: 3 slots * 0.10 * 50 games/slot = 15 games.

**Variance problem:** With a Bernoulli coin per slot, the actual number of heuristic games per iteration has high variance:
- P(0 heuristic slots) = 0.9^3 = 72.9%
- P(1 heuristic slot) = 24.3%
- P(2+ heuristic slots) = 2.8%

This means ~73% of iterations have zero heuristic games. When heuristic does appear, it gets a full 50-game batch (one slot), but that is inconsistent.

**Making heuristic an explicit fixture:**
If heuristic is added as a 4th fixture alongside v8/v14/v19, it competes in the combined pool with PFSP weighting. Since the model's WR vs heuristic is very high (~85-88%), PFSP assigns it a low weight: (1 - 0.87)^1.0 = 0.13, versus a typical past-self opponent at (1 - 0.50)^1.0 = 0.50. So heuristic would naturally get ~4x less sampling weight than a 50/50 opponent -- roughly 2-3% of non-self games, which is less than the current 10%.

**Better approach:** Keep heuristic_pct as a separate mechanism but make it per-iteration rather than per-slot. Instead of flipping per slot, decide once per iteration: "does this iteration include a heuristic slot?" with P=0.30 (to get ~30% of iterations having one heuristic slot = ~10% of total games). This gives more consistent exposure without the 73% zero-game problem.

Alternatively, the simplest improvement: guarantee exactly 1 heuristic slot every N iterations (e.g., every 3rd iteration). This is deterministic and gives ~17% of iterations with heuristic exposure, averaging ~8 games/iter over the long run.

**Why heuristic matters:** Heuristic is the only opponent in the pool that plays with a fundamentally different strategy (rule-based, not neural). It tests for robustness against non-neural play patterns. The documented policy collapse of v24/v25 (echo-chamber self-play) shows the risk of losing heuristic exposure. Consistent, guaranteed heuristic play is more valuable than random sporadic exposure.

### PFSP coverage and gaps

**What PFSP does well:**
The current PFSP implementation (weight by (1-WR)^p, averaged over both sides) is well-designed. It correctly:
- Upweights opponents the model struggles against
- Handles side asymmetry (averaging USSR and US WR)
- Requires minimum sample size before adjusting (MIN_GAMES=10)
- Combines multiplicatively with recency weighting

**What PFSP cannot do:**
PFSP can only adjust weights among opponents already in the pool. It cannot:
1. **Discover missing opponents:** If a model from a different training lineage would expose a critical weakness, PFSP cannot find it because that model is not in the pool. This is the strongest argument for fixtures -- they inject external diversity.
2. **Distinguish redundant opponents:** Two opponents with similar WR but different strategies get similar PFSP weights. PFSP optimizes for difficulty, not diversity.
3. **Adapt quickly:** With 50 games/slot, it takes 2-4 iterations to get reliable WR estimates for a new opponent. During this cold-start period, PFSP defaults to 0.5 WR (uniform weighting).

**Does PFSP make cluster-based selection redundant?**
Partially. Within the current single-lineage model pool, PFSP already solves the "who is hardest" problem effectively. The models that the current agent struggles against (typically the nearest-Elo ones) get upweighted, which is the correct behavior.

Cluster-based selection would add value only if there were multiple training lineages with different strategies that expose different weaknesses. Since we have a single lineage, PFSP on that lineage plus fixtures for Elo range coverage is sufficient.

**Gap analysis for current setup:**
The one genuine gap in PFSP coverage is that it cannot adjust for the heuristic opponent's qualitative difference from neural opponents. The heuristic plays rule-based patterns that neural models might overfit against or forget about. This is why dedicated heuristic exposure (via heuristic_pct) is a separate mechanism and should remain so.

### Practical fixture budget

**Constraints:**
- mix_k=4 (4 opponent slots per iteration)
- 200 games/iter (50 games per slot)
- fadeout=50 (fixtures removed after 50 iterations)
- Single GPU, ~45 minutes per iteration

**Current allocation (per iteration):**
| Slot | Content | Games |
|------|---------|-------|
| 0 | Self (current model) | 50 |
| 1-3 | Sampled from: past-self + fixtures (PFSP-weighted), 10% heuristic chance per slot | 150 |

**Recommended allocation:**

Keep mix_k=4 with this rule:
1. **Slot 0:** Self (always). 50 games.
2. **Slot 1:** Guaranteed fixture slot. Sample one fixture from {v8, v14, v19} with PFSP weighting. 50 games.
3. **Slot 2-3:** PFSP-weighted from past-self pool. 100 games.
4. **Heuristic:** Every 3rd iteration, replace slot 3 with heuristic. ~17 games/iter average.

This guarantees fixture exposure every iteration (not probabilistic), ensures past-self gets the majority of training signal (which is what drives PPO learning), and provides consistent heuristic exposure.

**Fixture update protocol:**
- Maintain exactly 3 fixtures spanning [weakest meaningful, mid, near-frontier]
- Current: v8 (1942), v14 (2018), v19 (2079) -- good spread of ~70 Elo between each
- Update when frontier exceeds strongest fixture by 50+ Elo
- Next update: when a model reaches ~2130+, rotate v14->drop, v19->mid, new model->frontier, keep v8

**Fadeout timing:**
The current fadeout=50 is reasonable. By iteration 50, the past-self pool has 5 checkpoints (saved every 10 iters), providing enough diversity. Fixtures have served their purpose of bootstrapping the league in early iterations when past-self is empty or homogeneous.

## Conclusions

1. **Cluster-based selection is not warranted for the current lineage.** All models v8-v22 form a single monotonic Elo progression with transitive win rates. There are no meaningful strategy clusters to exploit. The complexity of cluster detection (weight-space distance, strategy fingerprints, or intransitivity analysis) is not justified by the expected benefit. Revisit only if multiple independent training branches are introduced.

2. **Fixtures should not grow unboundedly.** With mix_k=4 and 200 games/iter, 3 fixtures is the sweet spot. More fixtures dilute games-per-opponent below the threshold needed for PFSP to function (MIN_GAMES=10 per side). Adjacent-Elo models provide redundant training signal.

3. **Heuristic should get guaranteed, consistent exposure.** The current 10% per-slot coin flip results in 73% of iterations having zero heuristic games. Either make heuristic an explicit "every Nth iteration" slot, or switch to a per-iteration coin flip with higher probability. Do not make heuristic a PFSP-weighted fixture, as its high WR would cause PFSP to suppress it below useful levels.

4. **PFSP and fixtures serve complementary roles.** PFSP optimizes for difficulty within the existing pool; fixtures inject external diversity from outside the current run. Both are needed. PFSP cannot discover opponents not in the pool, and fixtures cannot adapt to the model's current weaknesses. Together they cover both needs.

5. **The current fixture set {v8, v14, v19} is well-chosen.** It spans 137 Elo with roughly equal spacing. Update to {v8, v19, v_new} when a model exceeds v19 by 50+ Elo (i.e., reaches ~2130).

## Recommendations

### Immediate (no code change needed)
- **Keep the current fixture set and update rule.** {v8, v14, v19} with "update when frontier > strongest fixture + 50 Elo" is correct.
- **Do not implement cluster-based selection.** It adds complexity without measurable benefit for a single-lineage model pool.

### Low-effort improvements (worth implementing)
1. **Deterministic heuristic scheduling.** Replace the per-slot 10% coin flip with "every 3rd iteration, slot 3 = heuristic". This is a 5-line change in `sample_K_league_opponents` and eliminates the 73% zero-heuristic-game problem.

2. **Guaranteed fixture slot.** Change slot 1 from probabilistic sampling to "always one fixture (PFSP-weighted among the 3)". This ensures every iteration has at least one non-self, non-heuristic external opponent, even early in training when the past-self pool is empty.

### Deferred (revisit if conditions change)
- **Cluster-based selection:** Only relevant if the project introduces multiple independent training branches (different architectures, different BC seeds, or adversarial training).
- **Growing fixture list:** Only relevant if the model pool becomes large enough (20+ models) that curating 3 fixtures by hand is burdensome. At that point, automated selection by maximum pairwise Elo spread might be useful.
- **Heuristic as PFSP fixture:** Would require modifying PFSP to have a minimum weight floor for designated opponents. Not worth the complexity -- the deterministic scheduling approach is simpler and more predictable.

## Open Questions

1. **Should the eval panel (for ppo_best.pt selection) differ from the training fixtures?** Currently, eval uses a single H2H opponent (v22). A panel of {heuristic, v8, v14, v22} would be more robust but 4x more expensive. Given that eval runs every 20 iterations and uses only 100 games, a 4-opponent panel would cost 400 games every 20 iters -- about 10% overhead. This may be worth the robustness gain.

2. **What happens when v24/v25-style collapses occur?** The current system detects collapse via the Elo tournament post-hoc, but does not prevent it during training. Should the heuristic WR during training serve as an early warning? (e.g., if WR vs heuristic drops below 70% for 5 consecutive iterations, trigger an alert.)

3. **Is fadeout=50 optimal?** This was chosen heuristically. If past-self diversity is the main concern, we could compute the effective diversity of the past-self pool (e.g., number of checkpoints with WR between 40-60% against current) and only fade out fixtures when this exceeds a threshold.
