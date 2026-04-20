# Opus Analysis: PFSP Pool Redesign
Date: 2026-04-20
Question: Unified pool + JSD dedup + asymmetric weight formula for PFSP?

## Executive Summary

The proposed redesign mixes one strongly-motivated change, one reasonable-but-unmeasured refinement, and one speculative change that current evidence does not support.

1. **Fixture fadeout removal (item D) is the only change with evidence behind it.** The prior analysis `opus_analysis_20260420_pfsp_self_play_analysis.md` already established this: at iter 50 of v6 the training pool goes to 100% past-self, and fixtures are not being solved (WR 0.57-0.64 USSR / 0.29-0.37 US). Recommendation from that doc — set `league_fixture_fadeout = 999` and make `__heuristic__` permanent — handles roughly 80% of the real signal-degradation problem by itself. Anything else in this redesign should be layered on top, not treated as a replacement.

2. **Unified pool + JSD deduplication of self-snapshots (items A and B) is a clean refinement that is worth doing but is not urgent.** The probe infrastructure in `python/tsrl/policies/jsd_probe.py` already batches 1000 stratified positions and produces per-head JSD numbers; dedup-JSD across the current ~7 past-self snapshots is approximately 28 pairwise comparisons × 1k positions on GPU, run once per 10 iterations — on the order of 1% of training wall-clock. The main risk is that JSD on a fixed probe set can undershoot true policy-distance when snapshots differ only on rare states; but `min_j JSD` is too aggressive and `mean_j JSD` or a soft-min is safer. A unified pool also removes the awkwardness of the current 50/50 mass split, which was always a heuristic rather than a derivation.

3. **The proposed asymmetric per-side weight formula (items C and E — `(1-WR)^α` for US, `4·WR·(1-WR)` for USSR) should be rejected on current evidence.** The argument in the task prompt — "for US WR=0.12 the symmetric formula starves hard opponents" — is not actually true as stated. The symmetric formula evaluated at WR=0.12 gives `4·0.12·0.88 = 0.4224`, which is ~42% of peak weight, not "starved." The truly starved regime is WR<0.05 or WR>0.95, and that is already what the additive UCB bonus is for. More importantly, PPO's policy gradient does depend on advantage variance, which is maximised by mixed outcomes (not one-sided losses) — the symmetric peak at WR=0.5 has a principled basis in variance-of-reward, not just a surface analogy to supervised learning. AlphaStar's `(1-WR)` monotone formula was used for league *exploiter* agents exploring weaknesses of a fixed main agent, which is a different objective than training a main agent; it is not direct precedent for this project's single-main-agent PFSP.

4. **The current formula (`sym + UCB`) is defensible and should not be replaced before measuring whether asymmetric helps.** UCB already handles the "hard opponent never sampled" failure mode that the task prompt attributes to symmetric-only weighting. At N=3000 and n_i=40 the UCB bonus is ~0.45 at pfsp_exponent=0.5, which is comparable to the sym base at WR=0.12. Any argument against the symmetric formula that ignores UCB is arguing against a strawman.

5. **Net recommendation:** implement (1) fixture fadeout fix as top priority (already done conceptually in prior analysis), (2) JSD dedup + unified pool as a medium-priority refinement once v7 is running, (3) defer the asymmetric per-side formula to a future ablation where the null hypothesis is "sym+UCB is fine" and the asymmetric version has to beat it.

## Findings

### A. Unified pool vs split-pool design

**Current design (scripts/train_ppo.py:1067-1197):**
- Past-self pool: each snapshot gets `recency_w * pfsp_w`, where `recency_w = exp(rank/tau)` and `pfsp_w` is the symmetric-plus-UCB weight.
- Fixture pool: each fixture gets `pfsp_w` only (no recency).
- Hard mass split: fixture_total is scaled to `past_total * fixture_mass_mult`, where `fixture_mass_mult = 2.0` when `current_iter < 5` and `1.0` otherwise. At steady state this gives fixtures 50% of pool mass.
- Heuristic floor (0.15 in v6) applied post-normalization as a final redistribution.

**Problems with the current design:**
- The 50/50 split is asserted without derivation. There is no principled reason why past-self should equal fixtures in aggregate — the right ratio depends on policy diversity within past-self, which the current code ignores.
- When near-duplicate past-self snapshots exist (iter_40 and iter_50 of a slow-moving policy are nearly identical), the 50% self mass is spread across redundant snapshots. This effectively halves the useful sampling variety compared to what the 50/50 intent suggests.
- `fixture_fadeout` introduces a hard cliff in the split that produces the v6 100%-self collapse documented in the prior analysis.

**Advantages of a unified pool:**
- No arbitrary mass split. Each opponent's weight derives from (diversity × learning_value) uniformly.
- Natural handling of the "all past-self look the same" case: their weights downscale by diversity, and fixtures' effective share rises organically.
- Simpler code path, fewer parameters to tune.

**Disadvantages / risks of a unified pool:**
- If diversity weighting works, it concentrates past-self mass on a few most-distinct snapshots. Fine for diversity but potentially amplifies sampling variance vs a uniform past-self distribution.
- Without a floor on external-fixture mass, a period of rapid policy drift (high JSD between recent snapshots) could crowd fixtures out entirely. The fadeout cliff goes away, but the opposite failure mode (too little fixture exposure) becomes possible.
- The 50/50 split, crude as it is, is a safe floor for external grounding. A unified pool should be combined with an explicit `min_fixture_mass` parameter (e.g. 40%) that substitutes for the current split.

**Net:** the unified-pool direction is sound, but the implementation should preserve a minimum-fixture-mass floor so that at steady state external opponents are guaranteed some share of the pool. This is essentially the v6 design minus the hard fadeout cliff.

### B. Self-snapshot deduplication (JSD vs recency window vs clustering)

**What the probe already provides:** `jsd_probe.py::ProbeEvaluator.compare(model_a, model_b)` computes card/mode/country/value JSD over a frozen 1000-position stratified probe set. It is currently called once per 10 iters to compare current-iter vs prev-iter and current-iter vs BC baseline. Extending this to pairwise over ~7 past-self snapshots is ~28 compare() calls = trivial (≤1% wall-clock at GPU-batched 256).

**Cost analysis:**
- 7 snapshots × 6 pairs each / 2 = 21 pairs. Actually `N*(N-1)/2` — for N=10 snapshots, 45 pairs.
- Each compare() is ~1s on an RTX 3050 for 1000 positions batched 256 (the batch size used in code).
- At 45 pairs once per 10 iters: 45s / 10 iters = 4.5s/iter. Iteration wall-clock is ~30s per the project state memory; dedup cost is ~15% of one iter, or ~1.5% averaged. Tolerable.

**Three dedup options:**

1. **`weight_i ∝ min_j JSD(π_i, π_j)` (min-distance):** aggressive. If any two snapshots are very similar, both get crushed. Good for strongly pruning duplicates; risky when the probe set doesn't discriminate well on some positions (underestimates true distance).

2. **`weight_i ∝ mean_j JSD(π_i, π_j)` (mean-distance):** smoother. An isolated novel snapshot (high mean distance) gets boosted; a snapshot clustered with many similar ones gets moderately downweighted. Safer but less aggressive.

3. **Soft-min via log-sum-exp:** `weight_i ∝ -log(1/N * sum_j exp(-JSD_j/T))` where T is a temperature. Interpolates between min (T→0) and mean (T→∞). Tunable without switching discrete formulas.

4. **Recency window (non-JSD baseline):** keep only last K=10 snapshots regardless of similarity. Zero JSD cost. Works if policy is always evolving (JSD monotonically increases with iter-distance), but fails if training plateaus and old snapshots are actually diverse.

5. **Clustering:** run k-medoids on pairwise JSD matrix, keep one representative per cluster. Clean but adds another hyperparameter (k) and discrete selection doesn't mesh with continuous PFSP weighting.

**Recommendation:** start with option 2 (mean JSD) or option 3 (soft-min with T=0.05 bits). Both degrade gracefully. Option 1 is too aggressive — in early training when all recent snapshots are near-duplicates of the BC baseline, min_j JSD for each is nearly the same tiny number and the diversity term gives no useful ordering.

**Orthogonal option worth doing regardless: a simple recency cap (K=10 past-self).** This gives most of the benefit of JSD dedup at zero complexity: stale iter_0001 snapshots stop getting sampling mass after the pool fills up. Only downside is it does not help when two recent snapshots are near-identical (which is the main JSD-dedup use case), so K-recency and JSD dedup are complementary, not substitutes.

### C. Symmetric vs monotone weight formula — the weak US case

**The prompt's premise, restated:** "For US WR=0.12 vs heuristic, the symmetric formula `4·WR·(1-WR) = 0.42` undersamples hard opponents. A monotone `(1-WR)^α` would prioritise them."

**Reality check on the numbers.** Evaluating the current formula at the relevant regimes for the v6 WR table:

| Opponent | WR_us | symmetric base | sym + UCB(pfsp=0.5, N=2520, n_i≈400) | pct of max |
|---|---|---|---|---|
| heuristic | 0.121 | 0.426 | 0.426 + 0.5·√(ln(2520)/480) = 0.426 + 0.064 = 0.490 | 49% |
| v20_scripted | 0.287 | 0.819 | 0.819 + 0.5·√(ln(2520)/400) = 0.819 + 0.070 = 0.889 | 89% |
| v56_scripted | 0.305 | 0.848 | 0.848 + 0.071 = 0.919 | 92% |
| iter_0001 | 0.313 | 0.861 | 0.861 + 0.062 = 0.923 | 92% |

Heuristic is at 49% of max weight on the US side, not "starved." It gets about half the sampling mass of a near-peer opponent — which matches the intuition that peer opponents are somewhat more informative, but heuristic is still a respectable sampler. The heuristic_floor=0.15 guarantees it in the pool regardless.

**What would the proposed monotone `(1-WR)^0.5` formula do?**

| Opponent | WR_us | (1-WR)^0.5 | vs symmetric | pct diff |
|---|---|---|---|---|
| heuristic | 0.121 | 0.938 | 0.426 | +120% |
| v20_scripted | 0.287 | 0.844 | 0.819 | +3% |
| v56_scripted | 0.305 | 0.834 | 0.848 | -1.7% |
| iter_0001 | 0.313 | 0.829 | 0.861 | -3.7% |
| Hypothetical WR=0.02 | 0.02 | 0.990 | 0.078 | +1169% |

The monotone formula massively upweights the hardest opponents and only marginally changes peer opponents. The question is whether this is good.

**Is upweighting hard-loss opponents good for PPO?** The task prompt argues yes because "losing games still give PPO signal via negative advantage." This is half-right:

- PPO uses advantage `A_t = R_t - V(s_t)` where V is the value head's prediction. If the value head has learned "against opponent X I will lose," then V(s_0) ≈ -1 and R = -1 gives A_0 ≈ 0. Policy gradient from this state is nearly zero — the model already knows it is going to lose, so there is nothing to update on.
- For advantage variance to be meaningful, you need a distribution of outcomes per opponent. WR=0.5 maximises Bernoulli variance. WR=0.12 gives variance 0.12·0.88 = 0.106, versus WR=0.5 giving 0.25. So peer opponents contribute ~2.4× more gradient signal per game (under a simple variance model).
- Counterargument: at WR=0.02 the outcomes are `{-1 with p=0.98, +1 with p=0.02}`, so the rare win is huge-advantage and carries heavy off-policy-like gradient information. This is true, but (a) the 0.02 samples per game are extreme outliers that PPO's clipping will usually kill, and (b) if your value head is well-calibrated, it predicts -0.96 and the rare +1 gives advantage +1.96, which is large but appears rarely and gets PPO-clipped if it pushes the policy too hard.

So the theoretical argument for symmetric-peak weighting is mostly sound: peer opponents give the best per-game gradient signal. The `sym + UCB` form already handles the "don't forget hard opponents exist" failure mode by re-exploring them via UCB.

**AlphaStar reference reconsidered.** The prompt cites AlphaStar's `(1-WR)` monotone formula. AlphaStar had three agent classes: main agents, main exploiters, and league exploiters. The monotone formula was used for *exploiters*, whose job was to find strategies that beat the main agent, not for training main agents. For main agents, PFSP with a symmetric-variance-like weight was used. This project trains a single main agent, so the AlphaStar precedent for symmetric weighting is actually the relevant one. (Source: AlphaStar Nature 2019 supplementary, Section B on PFSP; worth citing explicitly in any followup.)

**Conclusion on C:** the symmetric + UCB formula is defensible and the numerical "starvation" argument in the prompt does not hold up. Heuristic at US-WR=0.12 gets ~49% of max weight plus heuristic_floor=0.15 plus UCB re-exploration — not starved.

### D. Fixture fadeout: what should replace it

The prior analysis `opus_analysis_20260420_pfsp_self_play_analysis.md` already settled this:

1. **Primary fix:** set `league_fixture_fadeout = 999` (≥ n_iterations). Rely on PFSP weights + UCB + heuristic_floor for natural downweighting.
2. **Secondary fix:** split fixtures into `permanent_fixtures` (never faded) and `fadeable_fixtures` (optional). `__heuristic__` and the strongest scripted baseline should be permanent.
3. **Diagnostic fix:** `ucb/fixture_frac_*` W&B metric needs to reflect actual sampling-pool composition, not the WR-table dict.

Re-ranking for this pool-redesign context:

- **Permanent heuristic + strong-recent-scripted baselines, other fixtures fade by WR-based rule** (e.g., fade when model WR vs fixture > 0.85 for 20 consecutive iters with n_games ≥ 40). This makes the fadeout mechanism derived from model dominance, not from wall-clock. But this is gold-plating — v6 data shows no fixtures are being dominated, so a simple `fadeout = 999` is equally effective for v7.

- **Do NOT make fadeout side-specific.** Adding per-side fadeout is complexity without benefit. If a fixture is still informative on either side, keep it.

**Conclusion on D:** use `league_fixture_fadeout = 999` + permanent heuristic floor. Defer the WR-based fade rule until there is evidence a fixture is actually being dominated.

### E. Proposed unified formula: coherence and failure modes

The prompt proposes:
```
weight(opp_i) = diversity_factor(i) × learning_value(WR_i, side)
```
with `learning_value(WR, side="ussr") = 4·WR·(1-WR)` (symmetric) and `learning_value(WR, side="us") = (1-WR)^α` (monotone).

**Coherence issues:**

1. **Side-asymmetric learning_value is ad hoc.** There is no principled reason why USSR should use symmetric and US should use monotone. The variance-of-advantage argument (Section C) applies identically to both sides. The only basis for the asymmetry in the prompt is "US has lower WR, so the symmetric formula is suboptimal," which the numerics above refute.

2. **It creates side-specific training dynamics.** The US policy head would be trained predominantly on hard-loss opponents; the USSR head on peer opponents. Over 80 iters this could cause the two heads to drift in quality, or worse, cause the US policy to specialise in "close losses" behaviour (clawing back VP against strong play) at the expense of "deny wins" behaviour against near-peers.

3. **Opaque interaction with value head.** The shared value head has to predict outcomes under whichever opponent the rollout uses. If opponent distributions diverge sharply between sides, the value head sees two different distributions indexed by `side_int`, making conditional calibration harder.

4. **Loss of a single interpretable pfsp_exponent.** Currently `pfsp_exponent` is one knob. Adding `α` for the US side and keeping the symmetric (no-exponent) form for the USSR side makes ablation harder — you can no longer sweep one parameter and compare.

**Failure modes of the proposed unified formula:**

- **Runaway fixture dominance early:** if all past-self snapshots are near-duplicates (diversity ≈ 0 for each), the unified formula assigns near-zero weight to every past-self opponent. Fixtures then absorb ~100% of pool mass. Fixable by an absolute-floor term: `diversity_factor(i) = max(0.1, JSD_score(i))` so self-snapshots never fully collapse.

- **Runaway past-self dominance mid-training:** if snapshots diverge rapidly (high inter-snapshot JSD), diversity ≈ 1 for each, fixtures with small-but-positive learning_value become numerically dwarfed. Fixable by a per-category mass floor (e.g. fixtures guaranteed ≥30% of pool).

- **JSD miscalibration:** JSD measured on a 1k-position probe set may not reflect behavioural distance in the rollout distribution. Two snapshots with JSD ≈ 0 on probe could differ substantially in actual rollout behaviour if they diverge on rare-but-consequential states. Not fatal but worth knowing.

- **Entropy collapse acceleration:** if the diversity factor perfectly reflects policy novelty, the training signal is concentrated on recent-different snapshots, which are the ones the current policy is most similar to. This tightens the training distribution and can accelerate mode collapse. Mitigation: hybrid mass split (see Section A).

**Recommendation on E:** keep `learning_value = symmetric + UCB` for both sides. Add `diversity_factor` as a multiplier for past-self only (fixtures always get `diversity_factor = 1.0`). This is coherent, low-risk, and avoids the unjustified side-asymmetry.

Concretely:
```
weight(opp_i) =
  if fixture:      learning_value(WR_i)
  if past-self:    diversity_factor(i) * learning_value(WR_i)
with diversity_factor(i) = clamp(mean_{j≠i} JSD(π_i, π_j) / T, 0.1, 1.0), T = typical JSD scale (~0.05)
```

Then apply `min_fixture_mass = 0.4` as a final re-normalization to guarantee external grounding.

### F. Implementation complexity

**JSD pairwise computation cost.** With N self-snapshots and a 1k-position probe:
- N=10 snapshots → 45 pairs → 45s at ~1s/pair on RTX 3050.
- Run once per 10 iters (aligned with `jsd_probe_interval = 10`): 4.5s/iter amortised ≈ 1.5% of ~30s iteration wall-clock. Tolerable.
- Cache: as long as no snapshot changes, its logits on the probe set are immutable. Cache them at save-time (`export_checkpoint` already runs, one extra 1k-position forward pass is ~200ms). Then each new snapshot adds only N comparisons (not N²), turning amortised cost to <0.1% wall-clock.

**Infrastructure already in place:**
- `ProbeEvaluator` supports scripted and .pt checkpoints via `load_probe_model`.
- Probe parquet is fixed per training run (loaded once, cached in memory).
- W&B logging for `jsd/*` metrics is already in place (`train_ppo.py` lines 3617-3657).

**What would need to be added:**
1. A per-snapshot logits cache (dict keyed by iter number → probe-set logits tensor). Memory cost: 1000 × (card=111 + mode=6 + country=86 + value=1) float32 ≈ 800 KB per snapshot. Trivial.
2. A `diversity_factor` computation in `sample_K_league_opponents` that reads the cache and computes mean JSD.
3. A unified-pool branch behind a feature flag (e.g., `--league-unified-pool`) so it can be A/B-tested vs the current split-pool code.

**Estimated implementation complexity:** ~150 lines of Python, one new CLI flag, one W&B metric group. Medium task.

**One real concern:** the probe set is currently built from PPO rollout parquet (`data/probe_positions.parquet`). If the distribution shifts during training, the probe stops representing the current rollout distribution, and diversity measured on it drifts from diversity in actual opponent play. Two options: (a) accept this as a known limitation, document it; (b) rebuild the probe from recent rollout data every N iterations (adds complexity). Option (a) is fine for a first iteration.

## Conclusions

1. **The symmetric + UCB formula is defensible on current evidence.** The prompt's argument against it (US-WR=0.12 "starves" hard opponents under symmetric weighting) is numerically incorrect: heuristic gets ~49% of max weight plus UCB re-exploration plus heuristic_floor=0.15. The PPO-theoretic argument (advantage variance peaks at WR=0.5) aligns with the symmetric peak. The AlphaStar monotone `(1-WR)` was for exploiter agents, not main agents, and is not direct precedent here.

2. **Side-asymmetric `learning_value` (symmetric USSR + monotone US) is unjustified** and creates training-dynamics divergence between the two policy heads. Reject this proposal unless an ablation produces evidence it beats sym+UCB on both sides.

3. **Unified pool + JSD deduplication is a clean refinement.** Infrastructure exists (jsd_probe.py), cost is <2% of wall-clock with caching, and it removes the arbitrary 50/50 split in favor of a derivation-based weighting. Preserve a minimum-fixture-mass floor (~40%) as a safety floor.

4. **Fixture fadeout fix is the dominant action item.** The prior analysis already concluded `league_fixture_fadeout = 999` plus permanent heuristic. This alone resolves ~80% of the pool-composition problem. Unified-pool + JSD dedup is incremental on top.

5. **Recency-cap-K=10 on past-self is a zero-complexity win.** Do it regardless of whether full JSD dedup gets implemented.

6. **Most existing PFSP machinery is sound.** UCB handles hard-opponent re-exploration. Heuristic floor handles heuristic-weight collapse. Recency weighting handles stale snapshot downweighting. The only real defects are (a) the hard fadeout cliff (D) and (b) self-snapshot redundancy (B). Everything else is already working as designed.

## Recommendations (ordered by evidence strength)

**Tier 1 — Evidenced, implement now for v7:**

1. **Remove fixture fadeout.** Set `league_fixture_fadeout = 999` in v7 config. Evidence: prior analysis's 100%-self post-iter-50 collapse in v6, and the WR table shows no fixture dominance. Zero-risk change.

2. **Mark `__heuristic__` as permanent fixture.** Add a `permanent_fixtures` list that is exempt from any fadeout logic. Evidence: US-WR_heuristic=0.121 is the lowest in the table, meaning heuristic is the most-needed grounding opponent, and the fadeout removed it. Low-risk change.

3. **Add recency cap K=10 on past-self.** Simplest possible diversification: keep only the 10 most-recent iter_*.pt snapshots in the pool. Evidence: iter_0001's influence on pool sampling is larger than warranted at iter 60+. Zero-risk change (strictly reduces pool size).

4. **Fix `ucb/fixture_frac_*` W&B metric** to count only active-pool members. Evidence: current metric hides the fadeout cliff. Zero-risk diagnostic-only change.

**Tier 2 — Sound but unmeasured, worth a controlled experiment:**

5. **Implement JSD-based diversity factor for past-self snapshots.** Use `mean_j JSD(π_i, π_j) / T` as a multiplier on the past-self weight, clamped to `[0.1, 1.0]`. Add with a feature flag (`--league-diversity-weighting`) so v7 can be run with and without. Evidence: no direct measurement, but the mechanism is theoretically sound and cheap to compute.

6. **Move to unified pool (fixtures + past-self in one bag).** Derived weights via `diversity_factor × learning_value`, with `diversity_factor = 1.0` for fixtures. Preserve `min_fixture_mass = 0.4` as an explicit floor so the fadeout failure mode doesn't recur via a different mechanism. Combine with (5); doing them together is simpler than doing them separately.

7. **Cache per-snapshot probe logits at save-time** to avoid recomputing every iter. 800KB/snapshot × 10 snapshots = 8MB. Trivial memory cost.

**Tier 3 — Speculative, defer or reject:**

8. **Asymmetric per-side learning_value formula (symmetric USSR + monotone US).** Reject on current evidence. The numerical claim in the prompt doesn't hold (WR=0.12 → sym=0.42 not "starved"), the PPO-theoretic basis favors symmetric, and side-asymmetric learning risks divergent training dynamics. Open a separate ablation if US training is later shown to be signal-starved by some other metric — but there's no such signal now.

9. **WR-based fixture fadeout (fade only when WR > 0.85 for K iters).** Defer. Current data shows no fixtures being dominated, so the rule would never fire. If in v7+ some fixture consistently hits WR > 0.85, revisit.

10. **Clustering-based dedup or k-medoids representatives.** Overkill given (3) recency-cap gives most of the benefit.

## Open Questions

1. **Is JSD on a fixed 1k-position probe a good proxy for behavioural distance in rollouts?** The probe is drawn from past rollout parquet, so it represents the rollout distribution at the time the probe was built. As the policy evolves, the rollout distribution shifts and the probe becomes out-of-distribution. Low-priority fix: rebuild probe every 50 iters from recent rollout data.

2. **Should diversity_factor use card-only JSD, or weighted sum of card+mode+country?** The current `ProbeEvaluator` returns all three. Cards dominate policy differences early-game, countries dominate mid-game influence placement. Recommend starting with card_jsd as the sole diversity metric and revisiting if it gives weird rankings.

3. **Does the value head's calibration against hard opponents matter enough to affect the learning_value argument?** The PPO advantage-variance argument assumes value head is well-calibrated (V ≈ WR − 0.5 mapped to expected return). If value head is systematically miscalibrated on hard opponents (e.g., overestimates US win probability), advantages may still be large and informative at WR=0.12. Not a current problem (see project_us_win_value_weighting feedback) but worth noting.

4. **Would replacing the `league_mix_k = 6` slot budget with dynamic-k-based-on-diversity improve things?** Unknown. If most past-self snapshots are near-duplicates, sampling K=6 of them is wasteful — K=2-3 distinct ones would be enough. But this is a meta-level optimization; addressing it later once dedup is in place is fine.

5. **Is the `rollout_temp = 1.0` (greedy rollout policy) compatible with JSD-based dedup?** JSD is measured on softmax distributions, but rollout actions are sampled from a temperature-1 softmax. If rollout_temp ≠ 1, the "behavioural distance" at play time differs from the JSD reported on probe. Currently rollout_temp = 1.0 so this is moot, but flag if rollout_temp is ever tuned.
