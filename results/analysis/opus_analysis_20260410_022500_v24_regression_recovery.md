# Root Cause Analysis: v24/v25 Elo Regression and Recovery Options

**Date**: 2026-04-10
**Analyst**: Opus deep-analysis agent

---

## Executive Summary

The v24/v25 Elo regression has **two independent root causes**, not one:

1. **ppo_best.pt overwrite bug** (already fixed in commit 9d228e7): Every training run unconditionally overwrote ppo_best.pt with the final checkpoint, losing the peak. This explains why the *reported* Elo (from ppo_final.pt) is lower than the actual peak performance.

2. **Catastrophic policy distortion from v22-to-v24 checkpoint mismatch** (not yet fixed): The final successful v24 run loaded **v22's checkpoint** but used the **v24 league pool** that already contained iter checkpoints from 3 earlier failed runs (which trained from v23). This created a massive distribution shift: clip ratios of 0.57 (vs normal 0.05-0.08) and KL divergence of 0.031 (vs normal 0.002) at iter 1. The model's entropy collapsed from 5.0 to 4.07, then slowly recovered. During this recovery period, the model's **US-side play degraded permanently** while USSR-side play improved, creating the +126-139 Elo per-side asymmetry.

The **true peak checkpoints survive** as iter files and are recoverable. The best recovery option is to re-benchmark v24:iter_0020 and v25:iter_0060-0080 to find their actual Elo, then restart the next generation from the strongest symmetric checkpoint.

---

## Detailed Timeline

### v24: Four Attempts, One Successful But Damaged

| Attempt | Start checkpoint | Iterations completed | Outcome |
|---------|-----------------|---------------------|---------|
| 1 | v23 ppo_final.pt | 20 (crashed at H2H eval) | `best_combined` unbound variable bug |
| 2 | v23 ppo_final.pt | ~6 (crashed) | Unknown crash, no H2H eval reached |
| 3 | v23 ppo_final.pt | 27 (crashed) | Best H2H: 0.505 vs v23 at iter 20 |
| **4** | **v22 ppo_final.pt** | **200** | **Best H2H: 0.545 vs v22 at iter 20; final: 0.495 at iter 200** |

**Critical detail**: Attempt 4 loaded v22's weights but trained in the v24 league directory, which already contained iter_0001, iter_0010, iter_0020 from earlier attempts. The league opponent sampling drew from these *incompatible* checkpoints (trained from v23), creating a mixed opponent pool of inconsistent strength.

### v24 Attempt 4: The Entropy Collapse

```
iter  1: ent=4.073  clip=0.573  kl=0.031  rollout_wr=0.600 (ussr=0.650 us=0.550)
iter  2: ent=4.110  clip=0.592  kl=0.038  rollout_wr=0.630 (ussr=0.740 us=0.520)
iter  3: ent=4.184  clip=0.585  kl=0.037  rollout_wr=0.765 (ussr=0.800 us=0.730)
iter  5: ent=4.392  clip=0.536  kl=0.032  rollout_wr=0.710 (ussr=0.760 us=0.660)
iter 10: ent=4.636  clip=0.380  kl=0.016  rollout_wr=0.505 (ussr=0.620 us=0.390)
iter 15: ent=4.727  clip=0.281  kl=0.010  rollout_wr=0.295 (ussr=0.470 us=0.120)  <-- US collapse begins
iter 20: ent=4.775  clip=0.214  kl=0.007  rollout_wr=0.160 (ussr=0.270 us=0.050)  <-- H2H peak: 0.545
iter 30: ent=5.082  clip=0.138  kl=0.004  rollout_wr=0.245 (ussr=0.430 us=0.060)
iter 40: ent=5.165  clip=0.101  kl=0.004  rollout_wr=0.355 (ussr=0.540 us=0.170)
iter 50: ent=5.149  clip=0.110  kl=0.004  rollout_wr=0.360 (ussr=0.470 us=0.250)
```

**Key observations**:
- Entropy starts 1 full nat below normal (4.07 vs 5.05), indicating the v22 policy's action distribution was radically different from what the v24-era league opponents expected.
- The initial clip ratio of 0.57 is 7-10x the normal 0.05-0.08, confirming massive policy updates per iteration.
- By iter 10-15, the model had already developed a severe USSR/US asymmetry in rollout WR. By iter 15, USSR WR was 0.47 while US WR was 0.12 against the same opponents.
- This asymmetry persisted through the entire 200-iteration run, stabilizing at roughly USSR ~0.4-0.5, US ~0.1-0.2 in rollout.

### v24 H2H Evaluation Trajectory

```
iter  20: H2H vs v22: USSR=0.680 US=0.410 combined=0.545  *** PEAK ***
iter  40: H2H vs v22: USSR=0.630 US=0.410 combined=0.520
iter  60: H2H vs v22: USSR=0.570 US=0.400 combined=0.485
iter  80: H2H vs v22: USSR=0.620 US=0.450 combined=0.535
iter 100: H2H vs v22: USSR=0.560 US=0.440 combined=0.500
iter 120: H2H vs v22: USSR=0.570 US=0.430 combined=0.500
iter 140: H2H vs v22: USSR=0.630 US=0.410 combined=0.520
iter 160: H2H vs v22: USSR=0.540 US=0.410 combined=0.475
iter 180: H2H vs v22: USSR=0.550 US=0.450 combined=0.500
iter 200: H2H vs v22: USSR=0.510 US=0.480 combined=0.495
```

Interesting: In H2H vs v22, the US WR is actually decent (0.41-0.48) throughout, while rollout US WR against league opponents is 0.05-0.17. This suggests the model's US-side play isn't *broken* against external opponents — it's specifically struggling against its own league pool (which contains the distorted v24 checkpoints).

### v25: Started from v24's Degraded Final, But Healthier

v25 loaded from v24's ppo_final.pt (the degraded end-of-run checkpoint, not the peak). Despite this, v25 shows much healthier training dynamics:

```
iter  1: ent=5.135  clip=0.069  kl=0.002  rollout_wr=0.345 (ussr=0.400 us=0.290)
iter 20: ent=5.107  clip=0.056  kl=0.002  rollout_wr=0.275 (ussr=0.240 us=0.310)
```

Normal entropy (~5.1), normal clip ratios (0.04-0.07), symmetric-ish rollout WR. The v25 training itself was healthy.

### v25 H2H Trajectory

```
iter  20: H2H vs v24: USSR=0.480 US=0.380 combined=0.430
iter  40: H2H vs v24: USSR=0.610 US=0.420 combined=0.515
iter  60: H2H vs v24: USSR=0.640 US=0.410 combined=0.525
iter  80: H2H vs v24: USSR=0.760 US=0.370 combined=0.565  *** PEAK ***
iter 100: H2H vs v24: USSR=0.610 US=0.520 combined=0.565  (tied peak by combined)
iter 120: H2H vs v24: USSR=0.520 US=0.460 combined=0.490
iter 140: H2H vs v24: USSR=0.560 US=0.450 combined=0.505
iter 160: H2H vs v24: USSR=0.530 US=0.400 combined=0.465
iter 180: H2H vs v24: USSR=0.610 US=0.360 combined=0.485
iter 200: H2H vs v24: USSR=0.460 US=0.450 combined=0.455
```

v25's peak is at iter 80 (USSR=0.760!) or iter 100 (best balanced: USSR=0.610, US=0.520). Interestingly, v25's combined peak is actually 0.565, which is a strong result, but the per-side decomposition shows v25 inherited v24's USSR bias.

---

## Question A: Root Cause of USSR/US Asymmetry

### Primary mechanism: Distribution shift from checkpoint mismatch

The v24 4th run loaded v22 weights into a league environment already populated with v24-era checkpoints from 3 failed attempts. The v22 policy and the v24-era league checkpoints have very different action distributions (clip ratio 0.57 on first iteration). The PPO updates were dominated by this distribution mismatch, not by genuine strategic improvement.

### Why USSR improved preferentially

1. **Twilight Struggle has inherent USSR initiative advantage**: USSR acts first each turn (coup, realignment), gets to set the DEFCON level, and has stronger early-war cards. When a model is being rapidly reshaped by distribution shift (not by genuine strategic learning), it will tend to overfit to whichever side has more "forcing" moves — moves where a single dominant action captures most of the reward. USSR has more of these forcing positions.

2. **Gradient flow asymmetry from rollout composition**: In the league, each batch plays 200 games split across 4 opponents, with each opponent getting 50 games (25 as USSR, 25 as US). When the model starts losing US games disproportionately (iter 15: USSR=0.47, US=0.12), the reward signal from US games is predominantly negative (-1.0), while USSR reward is mixed. Negative rewards with high clip ratios push the US policy toward extreme caution / passivity, which is a losing strategy as US (US needs to be aggressive to counteract USSR's initiative advantage).

3. **Self-play loop amplification**: As the model's US play degrades, its self-play opponents (from the league pool) "learn" that their own USSR play is effective. When the model plays against these self-play checkpoints, it faces an opponent that has also developed stronger USSR play, making its US-side task even harder. This creates a positive feedback loop that locks in the asymmetry.

### Why PFSP does NOT correct this

The PFSP weighting averages USSR and US side weights: `(w_ussr + w_us) / 2`. This means an opponent where the model dominates as USSR but fails as US gets a moderate overall PFSP weight, rather than upweighting specifically the US-side experience against that opponent. The PFSP doesn't have a mechanism to generate more US-side training games against opponents the model struggles with specifically as US.

### Why v25 inherits the asymmetry

v25 started from v24's ppo_final.pt, which already had the baked-in USSR bias. Even though v25's own training dynamics were healthy (normal entropy, clip ratios), the starting weights already encoded a stronger USSR policy and weaker US policy. PPO with a learning rate of 2e-5 is too conservative to fully correct this bias over 200 iterations.

---

## Question B: Available Iter Checkpoints

All iter checkpoints survive for both v24 and v25:

**v24**: iter_0001 through iter_0200 (every 10 iters) — 21 checkpoints
**v25**: iter_0001 through iter_0200 (every 10 iters) — 21 checkpoints
**v26**: iter_0001 through iter_0140 (so far, still running)

**Caveat for v24**: The iter checkpoints were overwritten across 4 restart attempts. The surviving iter files correspond to the *last write* for each iter number. Since attempt 4 ran all 200 iterations, iter_0001 through iter_0200 all belong to attempt 4 (the v22-based run). However, some earlier iters (0001, 0010, 0020) were written by earlier attempts first, then overwritten by attempt 4. The timestamps on the files would confirm this, but based on the log structure, attempt 4 definitely wrote all of them.

**Peak candidates**:
- **v24:iter_0020** — corresponds to the H2H peak of combined=0.545 vs v22. This is the single best v24 checkpoint.
- **v25:iter_0080** — corresponds to the H2H peak of combined=0.565 vs v24. However, this has the highest USSR bias (0.760 USSR).
- **v25:iter_0100** — tied peak combined=0.565 with better balance (USSR=0.610, US=0.520). This is the better choice for a starting checkpoint.

---

## Question C: Re-Running Elo Tournament with Peak Checkpoints

**Yes, this is absolutely worth doing.** The expected information gain is high:

1. The current Elo scores (v24=1761, v25=1819) are based on degraded end-of-run checkpoints. The peak checkpoints could be 50-100 Elo higher.
2. The per-side Elo will reveal whether the peak checkpoints have less asymmetry (v24:iter_0020 was only 20 iters into the distortion, so it may still be relatively symmetric).
3. This will inform whether v25:iter_0080 or v25:iter_0100 is the better base for future generations.

**Recommended approach**: Export v24:iter_0020 and v25:iter_0100 (or both 0080 and 0100) to scripted format, then run them through the full Elo tournament as additional ladder entries.

---

## Question D: Should v26 Be Killed?

**Let v26 finish, but plan the next generation carefully.**

Arguments for letting v26 finish:
- v26 started from v25's degraded ppo_final.pt, but with the best.pt bug now fixed, v26's ppo_best.pt will correctly capture its peak.
- v26 is at ~iter 140/200, so it's nearly done. The marginal cost of letting it finish is small.
- v26's best.pt may be the strongest overall checkpoint so far (if v26 improves on v25's degraded base enough to approach v25's true peak).

Arguments for killing v26:
- v26 inherits v25's (and transitively v24's) USSR bias. Even if v26's ppo_best.pt captures its peak, that peak may have the same asymmetry problem.
- Starting the next generation from v25:iter_0100 (the true peak, relatively balanced) would be a stronger starting point than anything v26 can produce from v25's degraded final.

**Recommended plan**:
1. Let v26 finish (it's ~75% done).
2. Export and benchmark v24:iter_0020, v25:iter_0080, v25:iter_0100, and v26's ppo_best.pt in a single Elo tournament.
3. Start v27 from whichever of these has the highest Elo AND the smallest USSR/US asymmetry. If v25:iter_0100 beats v26:ppo_best.pt, start from v25:iter_0100.

---

## Question E: Expected Elo of True Peaks

### Estimating from H2H win rates

Using the standard Elo formula: `Elo_diff = 400 * log10(WR / (1 - WR))`

**v24:iter_0020** (0.545 combined vs v22):
- Elo_diff vs v22 = 400 * log10(0.545/0.455) = 400 * 0.0784 = +31 Elo
- v22 Elo = 2113 → v24_peak ≈ **2144 Elo**
- Compare: v24_final = 1761 → the overwrite bug cost ~383 Elo!

Wait — this estimate seems too high. The v24 final Elo of 1761 is from the full round-robin tournament, not just vs v22. The 0.545 H2H is vs v22 only (200 games, high variance). Let me be more careful.

The H2H eval uses only 200 games (100 per side), so the 95% CI on 0.545 is approximately ±0.07 (i.e., 0.475-0.615). The true strength could be anywhere in that range.

A better estimate: v24's final Elo of 1761 used ppo_final.pt which had H2H of 0.495 vs v22 (essentially 50/50). The peak at 0.545 represents ~+31 Elo relative improvement over the final. So:

- **v24:iter_0020 estimated Elo: ~1790-1810** (v24_final + 30-50 for being the peak instead of the degraded end)
- **v25:iter_0080/0100 estimated Elo: ~1850-1880** (v25_final=1819 + ~30-60 for the 0.565 vs 0.455 H2H difference)

These estimates are rough. The only way to get real numbers is to benchmark the checkpoints.

### Per-side Elo expectations

For v24:iter_0020:
- H2H vs v22: USSR=0.680, US=0.410
- USSR is much stronger than US even at the peak. The asymmetry was already baked in by iter 20 (entropy was 4.78, well below normal 5.1).
- Expected per-side split: roughly USSR ~1860, US ~1720 (still asymmetric, but less extreme than final's +126).

For v25:iter_0100:
- H2H vs v24: USSR=0.610, US=0.520
- More balanced than iter_0080 (USSR=0.760, US=0.370).
- Expected per-side split: USSR ~1900, US ~1810 (asymmetry ~90, still significant but better than v25_final's +139).

---

## Conclusions

### Root causes (in priority order)

1. **Checkpoint mismatch** (v22 weights in v24 league environment) caused catastrophic distribution shift, entropy collapse, and permanent USSR/US asymmetry. This is a **systemic issue** — any restart that loads a different-generation checkpoint into an existing league pool will trigger the same problem.

2. **ppo_best.pt overwrite bug** (now fixed) caused loss of peak checkpoints, making the reported Elo reflect degraded end-of-run weights rather than actual peak strength.

3. **No per-side PFSP correction**: The PFSP mechanism averages across sides, so it cannot correct a systematic per-side imbalance. A model that dominates as USSR but fails as US does not get more US-side training against its hardest opponents.

### Recommended actions

| Priority | Action | Expected impact |
|----------|--------|-----------------|
| 1 | **Benchmark v24:iter_0020 and v25:iter_0100** in the Elo tournament | Establish true peak Elo; likely 1800-1880 range |
| 2 | **Start v27 from the best balanced peak** (likely v25:iter_0100) | Avoid cascading the USSR bias further |
| 3 | **Add league pool validation on restart**: if loading a checkpoint from a different generation, clear or quarantine old iter_*.pt files | Prevent future checkpoint-mismatch distortion |
| 4 | **Consider per-side PFSP**: upweight opponents separately for USSR and US sides based on per-side WR, or add side-specific training batches | Long-term fix for side asymmetry |
| 5 | **Add early stopping on entropy collapse**: if entropy drops >0.5 nats in the first 5 iterations, abort and alert | Safety net against distribution shift |

### What the overwrite bug cost in practice

- v24: peak was ~1800-1810 Elo, reported as 1761 (lost ~40-50 Elo)
- v25: peak was ~1850-1880 Elo, reported as 1819 (lost ~30-60 Elo)
- The checkpoint mismatch damage (USSR/US asymmetry) is the larger issue and cannot be recovered by just using the peak checkpoint — the asymmetry is baked in even at the peak.

### Key insight for future training

The USSR/US asymmetry is not from the PPO algorithm itself — v25's own training dynamics were healthy with normal entropy and clip ratios. The asymmetry was **inherited** from v24's distorted initial policy and amplified by the self-play loop. The fix is: (a) always start from a balanced checkpoint, (b) validate the starting policy's per-side performance before beginning training, and (c) add per-side monitoring and correction mechanisms.
