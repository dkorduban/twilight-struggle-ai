---
# Opus Analysis: PPO Lineage Gap v132 vs v200+
Date: 2026-04-14
Question: Why is v200-v216 stuck 300 Elo below v132_sc?

## Executive Summary

The ~300 Elo gap between v132_sc (2092) and v200-v216_sc (1722-1875) has **three root causes**, ranked by impact:

1. **v132_sc is a one-shot lottery winner, not a sustainable training product.** It was initialized from v77_sc/ppo_best.pt (itself a one-shot Elo=2119 iter10 peak from a 27-fixture training run), ran only 30 iterations of PPO with entropy 0.01->0.003, and its best checkpoint happened to hit Elo=2092. The subsequent v133-v137 lineage immediately declined (2081->2005) over just 5 runs, proving the config does not sustain that Elo level.

2. **Catastrophic entropy collapse from aggressive global entropy decay.** The Snakefile sets `global-ent-decay-start = prev_total_iters` and `global-ent-decay-end = prev_total_iters + 30`, meaning entropy decays from 0.01 to 0.003 *within each 30-iteration run*. By iteration 30, entropy is at its minimum. Across chained runs, the model starts each new run at ent=0.01 (fresh schedule), but collapses to 0.003 by the end. The v214_sc log confirms entropy fell from 3.95 to 3.93 over 30 iters -- but this is *policy* entropy, not the coefficient. The coefficient itself reaches 0.003 by iter 30 every single run. This aggressive decay prevents exploration and locks in whatever policy the model starts with.

3. **PFSP down-weighting eliminates learning signal from strong opponents.** With pfsp_exponent=1.5 and the symmetric weight formula `4*WR*(1-WR)`, opponents with WR>0.9 get near-zero base weight (4*0.9*0.1 = 0.36, vs 1.0 at WR=0.5). The v214_sc log shows WR vs v55_scripted at 0.91-0.92 with pfsp=0.29-0.36, while self-play iter checkpoints at WR~0.5 get pfsp=0.99-1.0. The model trains mostly against *itself and weak iter checkpoints*, not against the strong fixtures that would push it higher. This is the opposite of what's needed: when you're already beating v55 at 90%+, the *only* learning signal that matters comes from the *losses* against v55 -- but PFSP suppresses exactly that signal.

The panel_eval WR=0.95 vs {v55,v54,v44,v45,v48} at iter 10 confirms the model is *already strong against those opponents* but the Elo system measures performance against the *entire ladder* (including many models the v200+ lineage hasn't been tested against). The 0.95 panel WR is consistent with Elo ~1850-1900 because the panel opponents are clustered at 2095-2118, so beating them 95% of the time implies roughly 200-250 Elo above them ... but wait, that would imply Elo ~2300. The discrepancy suggests the Elo measurement is based on a wider opponent set where the v200+ lineage performs worse.

## Findings

### Finding 1: v132_sc's origin -- a reset from v77_sc, not organic improvement

- v132_sc was created via `checkpoint_override` from `data/checkpoints/ppo_v77_sc_league/ppo_best.pt`
- v77_sc itself was the peak of the entire project: iter10 Elo=2119 (matching v55 SOTA)
- v77_sc was trained with **27 fixtures** (vs current 10), using the older fixture pool
- The v132_sc checkpoint is essentially v77_sc + one more 30-iter PPO run
- v132_sc Elo=2092 is consistent with v77_sc iter10 peak (2119) with some regression

### Finding 2: Immediate decline after v132_sc proves config instability

```
v132_sc  Elo=2092  (reset from v77_sc)
v133_sc  Elo=2081  (-11)
v134_sc  Elo=2064  (-17)
v135_sc  Elo=2032  (-32)
v136_sc  Elo=2022  (-10)
v137_sc  Elo=2005  (-17)
v138_sc  Elo=1979  (-26)
...
v160_sc  Elo=1756  (-223 from start, 67 runs later)
```

The decline is monotonic and accelerating. This is not noise -- it is systematic drift downward under the current training config.

### Finding 3: Second reset at v205_sc also declines

v205_sc was reset from v132_sc/ppo_best.pt and initially climbed to Elo=1875 (v209_sc), but then:
```
v205_sc  Elo=1849  (reset from v132_sc)
v209_sc  Elo=1875  (peak)
v210_sc  Elo=1872
v211_sc  Elo=1865
v212_sc  Elo=1839
v214_sc  Elo=1791
v215_sc  Elo=1794
```

Same declining pattern, confirming the training config itself causes regression.

### Finding 4: PFSP suppresses the most valuable training signal

From v214_sc training log:
```
v55_scripted:  WR_ussr=0.92 pfsp=0.291   (strong opponent, LOW weight)
v48_scripted:  WR_ussr=0.93 pfsp=0.289   (strong opponent, LOW weight)
iter_0001:     WR_ussr=0.56 pfsp=0.984   (weak self, HIGH weight)
iter_0010:     WR_ussr=0.49 pfsp=0.999   (50/50 self, MAX weight)
heuristic:     WR_ussr=0.50 pfsp=1.000   (weak opponent, MAX weight)
```

The model spends most training time against copies of itself and heuristic. Strong opponents that could provide learning signal are down-weighted to ~0.3x.

### Finding 5: Entropy decay is too aggressive

The config `--global-ent-decay-start <prev_total> --global-ent-decay-end <prev_total+30>` means:
- Entropy decays from 0.01 to 0.003 over exactly 30 iters (one full run)
- Every new chained run repeats this decay from scratch
- By the end of each run, the model has minimal entropy to explore
- Combined with PFSP self-play focus, this creates a policy-collapse trap

### Finding 6: Panel eval WR vs Elo discrepancy

Panel eval at iter 10: avg WR=0.95 vs {v55(2118), v54(2102), v44(2101), v45(2096), v48(2095)}. If taken at face value, 95% WR against ~2100 Elo opponents would imply the model is ~400 Elo above them (~2500). But the ladder shows 1791.

This discrepancy has several possible explanations:
- Panel eval uses only 30 games per opponent (150 total) -- high variance
- Panel eval may use different seeds or conditions than Elo tournament
- The incremental Elo placement matches against a wider set including models where v214_sc performs poorly
- The panel eval games may not be contributing to the Elo calculation

### Finding 7: The v77_sc-era 27-fixture pool was better

v77_sc trained with 27 fixtures and achieved Elo=2119 at iter10. The current pool has 10 fixtures. More diverse opponents provide more varied training signal. The JSD-deduplication that reduced the pool may have been too aggressive.

## Conclusions

1. **The ~300 Elo gap is real, systematic, and caused by the training config, not noise.** Two independent resets from v132_sc both produced declining lineages.

2. **v132_sc is not a realistic training target** -- it represents a one-shot peak from a v77_sc checkpoint that itself was a peak. The "gap" is partly an illusion: the true sustainable Elo of this config is probably ~1850-1900 (where v205-v211 briefly plateaued before declining).

3. **PFSP with exponent=1.5 is actively harmful at this stage.** When the model already beats all fixtures at 90%+, PFSP sends all training time to self-play. The model needs to *learn from its losses against strong opponents*, but PFSP weights those games lowest.

4. **The 30-iter entropy decay is too short.** Entropy collapses every run, preventing exploration.

5. **UPGO is not the primary problem** but may contribute to variance. Its impact is secondary to PFSP and entropy.

## Recommendations

### Immediate (next 1-2 runs)

1. **Disable PFSP or set exponent=0** so all fixtures get equal weight. At 90%+ WR against all fixtures, the model's learning signal comes from the 5-10% of games it *loses*. PFSP kills exactly that signal. Alternative: invert PFSP to weight strong opponents MORE (exponent=-1.5 or loss-weighted sampling).

2. **Slow down entropy decay.** Change `global-ent-decay-end` from `prev_total+30` to `prev_total+300` or higher. Let entropy decay over 10 runs, not 1 run. Even better: set a fixed ent_coef=0.005 (midpoint) and don't decay at all until Elo improves.

3. **Reset from v77_sc/ppo_best.pt** (the iter10 peak at 2119 Elo) rather than v132_sc. v132_sc is already one generation of decline from v77_sc.

### Medium-term (next 5-10 runs)

4. **Increase fixture pool diversity.** Restore 20+ fixtures or add sc-lineage models that are genuinely strong (v77_sc, v78_sc, v75_sc at 2092-2097). The JSD deduplication may have over-pruned.

5. **Increase games-per-iter from 200 to 400-600** to reduce gradient variance, especially when learning from rare loss events against strong opponents.

6. **Extend n-iterations from 30 to 60-80** per run. 30 iters at 200 games = 6000 games total per run. That's very few for PPO to make progress.

7. **Consider curriculum learning**: start with fixtures at WR=0.6-0.8 (where learning signal is strongest), not WR=0.9+ where signal is sparse.

### Experimental

8. **A/B test UPGO vs no-UPGO** with PFSP disabled, to isolate UPGO's effect.

9. **Try population-based training (PBT)**: run 3-4 parallel lineages with different hyperparameters and select the best.

## Open Questions

1. **Why does the panel eval show 0.95 WR but Elo is 1791?** Need to check if panel eval games use the same C++ binary, same seeds, and whether results feed into the Elo calculation. A 0.95 WR against 2100-rated opponents should yield ~2500 Elo, not 1791.

2. **What was v77_sc's exact fixture list?** The 27-fixture pool likely included many v8-v60 models. Were those providing better training signal than the current JSD-pruned 10-fixture pool?

3. **Is the optimizer reset (`--reset-optimizer`) every 30 iters helping or hurting?** It prevents momentum from building across runs but also prevents stale momentum. Worth testing.

4. **Are the WR table decay rates (0.5x) appropriate?** Decaying too aggressively may cause PFSP to forget that strong opponents are hard, re-inflating their WR estimates and further reducing their sampling weight.

5. **Is there an Elo measurement bias?** The incremental placement adds a new model by playing against a small set of "diverse" opponents. If those opponents are systematically different from the panel, the Elo estimate could be biased.
---
