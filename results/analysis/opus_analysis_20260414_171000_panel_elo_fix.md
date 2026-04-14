---
# Opus Analysis: Panel Elo Measurement Broken for 6-Mode Models
Date: 2026-04-14T17:10:00Z
Question: The panel-based Elo measurement system produces fake ratings for 6-mode models. v260_sc got 2393 Elo by crushing 5-mode panel models at 94-97% WR, but lost to v227_sc (a real 6-mode opponent) at 42% WR (84/200). True Elo is ~1735. Should we replace the panel? Is one run enough to evaluate the peak-era config fix? Should maybe_override be adjusted? Should we try mode_head perturbation?

## Executive Summary

The panel Elo system is fatally broken for 6-mode models because 7 of 8 opponents in the incremental placement pool are 5-mode models that 6-mode models crush at 94-97% WR regardless of actual strength. The single informative match (v260_sc vs v227_sc at 42% WR) implies true Elo of ~1735, confirming the chain is stuck. The panel must be replaced with 6-mode _sc models immediately. One run (v260_sc) is sufficient to conclude the peak-era config did not produce a breakthrough -- 42% WR against v227_sc (1791 Elo) means v260_sc is weaker, not stronger, than v217_sc (1837). The maybe_override threshold is now unreachable on the fake scale and must be recalibrated before v262_sc.

## Findings

### Finding 1: The 5-mode panel provides zero discrimination for 6-mode models

v260_sc match results against the current incremental placement pool:

| Opponent | Type | WR | Games | Discriminating? |
|----------|------|-----|-------|-----------------|
| v55 | 5-mode | 94.5% | 200 | No (ceiling) |
| v54 | 5-mode | 94.0% | 200 | No (ceiling) |
| v44 | 5-mode | 95.0% | 200 | No (ceiling) |
| v45 | 5-mode | 97.0% | 200 | No (ceiling) |
| v14 (=v48) | 5-mode | 95.5% | 200 | No (ceiling) |
| v46 | 5-mode | 96.5% | 200 | No (ceiling) |
| v78_sc | 5-mode era | 94.0% | 200 | No (ceiling) |
| v171_sc | 6-mode (weak) | 87.0% | 200 | Marginal |
| **v227_sc** | **6-mode** | **42.0%** | **200** | **YES** |

The problem is structural: 5-mode models (mode_head has 5 outputs) cannot produce EventFirst mode actions. When a 6-mode model plays EventFirst correctly, the 5-mode opponent literally cannot respond in kind. This creates a systematic ~94-97% WR floor that persists regardless of whether the 6-mode model is truly strong or weak. v217_sc (1837 Elo) would also crush these same opponents at ~94-97%.

The Elo solver treats these 7 extreme matches as strong evidence that v260_sc is vastly superior to the entire pool. The single contradictory match (42% vs v227_sc) is outvoted 7-to-1 in the BayesElo likelihood.

**Incremental Elo from the solver: 2393.** True Elo from H2H vs v227_sc (1791): 1735.

The error is +658 Elo. This is not noise -- it is a systematic measurement failure.

### Finding 2: The extension tournament made it worse, not better

The "promising model extension" code triggered because v260_sc=2393 was within 50 Elo of the top (v55=2118 in the main ladder). It played v260_sc against 5 more opponents: v55, v54, v44, v46, v78_sc -- **all 5-mode**. The extension used v260_sc as anchor at 2015, but with only 5-mode opponents (all losing at 94-97%), the solver kept v260_sc at the anchor value. The merged result became 2015 in the full ladder.

Neither the incremental placement (2393) nor the extension (2015) is meaningful. Both pools lack same-era 6-mode opponents.

### Finding 3: v260_sc vs v227_sc definitively shows the peak-era config did not help

v227_sc has Elo=1791 in the ladder (also likely inflated by 5-mode measurement, true strength probably ~1750-1780). v260_sc lost to v227_sc at 42% WR (84 wins, 114 losses, 2 draws out of 200 games).

From Elo theory: 42% WR implies v260_sc is ~56 Elo below v227_sc.

v217_sc (the restart anchor) is at 1837 Elo (ladder), and was the direct predecessor for both v227_sc and v260_sc. The fact that v260_sc (restart from v217_sc with full peak-era config: ent=0.01 + reset_opt=true) loses to v227_sc (an earlier v217_sc restart with weaker config) means:

- The peak-era config alone is not sufficient to escape the local optimum.
- v260_sc may have regressed from v217_sc during its 30-iter PPO run.
- The "exploration phase" from ent=0.01 may be destructive when starting from a v217_sc-era checkpoint, unlike when it started from the random-mode-head v205_sc checkpoint.

**One run IS sufficient to conclude the config fix alone is not a breakthrough.** The 200-game H2H against v227_sc has standard error of ~3.5% WR, so the true WR is in [35%, 49%] at 95% confidence. Even the upper bound (49%) would still place v260_sc below v227_sc.

However, v261_sc (same config, also a v217_sc restart) should still be evaluated against v227_sc before concluding the config is entirely useless. There is run-to-run variance in PPO, and it is possible (though unlikely given the margin) that v260_sc was unlucky.

### Finding 4: maybe_override is completely broken on the fake Elo scale

The maybe_override threshold is 1750 (real Elo scale). v260_sc got 2015 in the ladder after the extension re-anchoring. Since 2015 > 1750, no restart was triggered for v262_sc. This means:

- v261_sc will chain from v217_sc (pre-seeded override from v259_sc < 1750).
- v262_sc will chain from v261_sc's ppo_best.pt (no override, because v260_sc=2015 > 1750).

If v261_sc also gets fake Elo ~2000+, then v263_sc will also chain from v261_sc. The override mechanism is effectively disabled.

### Finding 5: Panel eval during training is equally broken

The `_panel_eval_worker` in `train_ppo.py` evaluates every milestone iteration against v55, v54, v44, v45, v14 (all 5-mode). The weighted panel average drives `ppo_running_best.pt` selection. At 93-97% WR, every iteration looks equally strong. The "best" checkpoint is selected essentially at random based on noise in a ceiling-compressed metric.

This affects:
- `ppo_running_best.pt` quality (may not be the actual best iteration)
- Panel eval history used by candidate tournaments
- W&B panel metrics (uninformative for 6-mode tracking)

### Finding 6: Available 6-mode _sc models for replacement panel

From the fixture pool and full ladder, the available 6-mode _sc models are:

| Model | Ladder Elo | True strength estimate | Available as scripted? |
|-------|-----------|------------------------|----------------------|
| v217_sc | 1837 | ~1800-1840 (best anchor) | Yes |
| v228_sc | 1796 | ~1770-1800 | Yes |
| v232_sc | 1811 | ~1780-1810 | Yes |
| v209_sc | 1875 | ~1840-1875 (peak) | Check |
| v227_sc | 1791 | ~1760-1790 | Yes (used in placement) |
| v205_sc | 1849 | ~1810-1850 | Check |

Note: All these Elo values are themselves measured against the same broken 5-mode panel, so they are all systematically inflated. The relative ordering is more reliable than the absolute values, because the inflation is roughly constant across 6-mode models of similar strength.

## Conclusions

1. **The 5-mode panel is completely non-discriminating for 6-mode models.** 94-97% WR means no useful Elo signal. Every 6-mode model gets approximately the same fake Elo from panel opponents, with the final number determined almost entirely by the 1-2 diverse opponents (which are also mostly 5-mode).

2. **v260_sc true Elo is ~1735, not 2393 or 2015.** The only informative match (vs v227_sc at 42% WR) places v260_sc approximately 56 Elo below v227_sc. v227_sc itself is at ~1791 (ladder, also inflated). True v260_sc strength is likely 1720-1740.

3. **The peak-era config (ent=0.01 + reset_opt=true) did not produce improvement in one run.** v260_sc restarted from v217_sc(1837) with the exact peak-era config and came out weaker (42% vs v227_sc). One run is borderline sufficient evidence -- wait for v261_sc as confirmation, but do not expect a breakthrough.

4. **maybe_override is broken.** The 1750 threshold on the inflated scale means no restarts will trigger. v260_sc=2015(fake) > 1750, so v262_sc chains from v261_sc instead of restarting from the anchor.

5. **Panel eval during training is also broken.** The ppo_running_best selection mechanism cannot distinguish checkpoint quality at 93-97% WR ceiling.

6. **The chain has been stuck at true Elo ~1700-1810 for 55+ runs (v205-v260).** Config fixes (entropy, optimizer, PFSP) have not broken through. The local optimum around v217_sc's policy basin appears to be a hard barrier for PPO continuation.

## Recommendations

### IMMEDIATE (before v262_sc launches): Fix measurement

1. **Replace the panel with 6-mode _sc models.** New panel for both incremental placement and training panel eval:
   - v217_sc (1837, anchor-strength)
   - v228_sc (1796, mid-strength)
   - v232_sc (1811, mid-strength)
   - v227_sc (1791, diverse)
   - Keep v55 as a single 5-mode reference (provides cross-era anchoring)
   
   Panel weights: v217_sc=0.30, v232_sc=0.25, v228_sc=0.20, v227_sc=0.20, v55=0.05.
   
   This gives WR in the 40-55% range (discriminating) instead of 94-97% (ceiling).

2. **Update the diverse opponent selection** in `post_train_confirm.sh` to prefer 6-mode models. The current algorithm picks bottom-quartile, median, and top from the full ladder -- which is dominated by 5-mode models. Add a `_sc` preference or a `--prefer-suffix _sc` flag.

3. **Recalibrate maybe_override threshold.** On the 6-mode panel scale, a model at v217_sc-level strength should score ~50% WR against the new panel (since v217_sc IS in the panel). Set threshold to the Elo that corresponds to <45% average panel WR (significantly weaker than anchor). Concretely: set to 1720 on the new scale, or better, use direct WR comparison instead of Elo: "restart if avg panel WR < 0.42".

4. **Disable maybe_override for v262_sc** immediately (create `results/checkpoint_override_v262_sc.txt` pointing to v217_sc anchor). Do not let v262_sc chain from v261_sc's output, which was trained with the broken panel eval driving checkpoint selection.

### SHORT-TERM (next 3-5 runs): Assess peak-era config properly

5. **Run v261_sc (already pre-seeded with v217_sc restart + peak-era config).** Evaluate it against the new 6-mode panel. If it also scores <45% against v227_sc, the peak-era config is confirmed insufficient.

6. **Run one more v217_sc restart (v262_sc) with increased entropy** (ent=0.015 instead of 0.01) as a diagnostic. If the policy is stuck in a narrow basin, higher initial entropy might help escape. If this also fails, the problem is not entropy but the weight-space basin itself.

### MEDIUM-TERM: Escape the local optimum

7. **BC re-initialization is the strongest remaining lever.** Train BC on the top ~500 games from v209_sc era (the strongest 6-mode checkpoint). Use BC weights as the PPO starting point. This gives a fresh weight-space starting point while retaining the behavioral knowledge of the peak model. The v205_sc precedent (random mode_head + strong trunk from v132_sc) shows that weight-space perturbation is what enabled the initial breakthrough.

8. **Mode_head perturbation as a cheaper alternative.** Add Gaussian noise (std=0.1 of weight norm) to mode_head weights at the start of each PPO run. This forces re-learning of the EventFirst decision policy while preserving the value function and card/country heads. It is cheaper than BC re-init but may be sufficient.

9. **Consider a 6-mode-only round-robin tournament** across v205_sc through v260_sc (with 200 games per pair) to establish a true Elo ladder for the 6-mode era. This provides proper retrospective evaluation and reveals whether any checkpoint in the v220-v260 range actually improved over v217_sc. Cost: ~30 _sc models x 29/2 pairs x 200 games = ~87k games, ~6-8 hours on CPU.

## Open Questions

1. **Is v209_sc genuinely stronger than v217_sc, or is it also inflated?** v209_sc's 1875 Elo was measured against the same broken 5-mode panel. A direct H2H (v209_sc vs v217_sc, 400 games) would establish the true relative strength and reveal whether there was genuine improvement in the v205-v217 era chain.

2. **Why do 6-mode models crush 5-mode models at 94-97%?** Is it purely the EventFirst mode advantage, or are 6-mode models also better at the 5 shared modes? Running a 6-mode model with its EventFirst probability zeroed out (forced to choose among the 5 original modes) would isolate this.

3. **What is the actual strength ladder within 6-mode models?** The relative ordering of v205-v260 _sc models is uncertain because they were all measured against the same non-discriminating panel. Only H2H matches between 6-mode models provide reliable signal.

4. **Is the v217_sc basin truly hard to escape via PPO, or is it a measurement artifact?** It is possible that some v220-v260 models are genuinely stronger than v217_sc but appear equal because the panel cannot distinguish them. The 6-mode round-robin tournament (recommendation 9) would answer this.

5. **Should training PFSP fixtures also be 6-mode?** The selected_fixtures.json currently includes 7 5-mode models + 3 _sc models. Training against 5-mode opponents may encourage exploitation of the EventFirst advantage rather than developing stronger shared-mode play. Consider shifting to a 6-mode-heavy fixture set for PFSP.
---
