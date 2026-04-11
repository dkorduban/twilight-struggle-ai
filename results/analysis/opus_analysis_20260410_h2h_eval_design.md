# Opus Analysis: H2H Eval Design for ppo_best.pt Selection

Date: 2026-04-10
Question: Is h2h_combined_wr vs a single fixed opponent a good criterion for ppo_best.pt selection?

## Executive Summary

Using h2h_combined_wr against a single fixed eval opponent to select ppo_best.pt is **a reasonable but flawed heuristic** that has already contributed to a multi-generation regression (v24-v25-v26 lineage, all 270+ Elo below v22). The core problems are:

1. **200 games gives ~3.5% standard error**, making the signal extremely noisy at the typical win-rate range (45-57%). Most "best" selections are statistically indistinguishable from neighboring checkpoints.
2. **When the eval opponent is weak** (v25 eval'd against v24, which was 340 Elo below v22), beating it harder does not correlate with general strength -- it selects for exploiting the weak opponent's specific blind spots.
3. **The metric is directionally correct when starting from the eval opponent** (v24 started from v22, eval'd vs v22 -- the signal is valid there), but breaks down in subsequent generations where the eval opponent drifts from the frontier.
4. **The cost (7 min per run) is negligible**, so the question is not whether to eval but what to eval against.

The best near-term fix is to eval against a **fixed panel** (heuristic + v8 + v14 + v22) rather than the just-finished model. This prevents the echo chamber without adding meaningful compute cost.

## Findings

### 1. Statistical power of 200-game H2H eval

With 200 games and true win rate p, the standard error is sqrt(p(1-p)/200). At p=0.50, SE=0.035 (3.5%). At p=0.55, SE=0.035.

The v25 H2H series against v24 shows combined WR bouncing between 0.430 and 0.565 across 10 eval points. The "best" (0.565 at iter 80) is within 1 SE of the 5th eval (0.565 at iter 100) and within 2 SE of the final eval (0.455). This level of noise means the "best" checkpoint is often selected by random fluctuation, not genuine strength differences.

For checkpoint selection to be reliable at 200 games, the best checkpoint would need to be at least ~7% WR above the runner-up -- which rarely happens during stable PPO training.

### 2. V24 eval'd vs v22 (valid signal)

V24 started from v22 weights and eval'd against v22. The H2H trajectory:
- iter 20: 0.390 (still close to v22, slightly below due to early PPO perturbation)
- iter 40: 0.505 (first beat v22)
- iter 60: 0.545 (peak -- saved as ppo_best)
- iters 80-200: oscillates 0.475-0.535

This is a **reasonable signal**: we see the model improve from its starting point, peak mid-training, then plateau. The peak selection at iter 60 is defensible.

However, the Elo tournament later showed v24 at 1757 Elo vs v22 at 2096 -- a 339 Elo gap. V24's "best vs v22" checkpoint was still dramatically worse than v22. The H2H said 54.5%, which implies a ~31 Elo advantage, but the true full-panel Elo was -339. This disconnect arises because v24 suffered entropy collapse (USSR/US asymmetry: USSR Elo 1798 vs US Elo 1679), which artificially inflated the H2H combined WR by winning as USSR and being tolerable as US.

### 3. V25 eval'd vs v24 (misleading signal)

V25 started from v24 and eval'd against v24. The problem: v24 was a weak model (1757 Elo, 340 below frontier). Beating v24 by more does not mean getting closer to v22 strength.

The v25 H2H peaked at 0.565 (iter 80), but the final Elo was only 1820 -- still 276 Elo below v22. The H2H selected for "best at exploiting v24's weaknesses" rather than "strongest general player." The USSR/US asymmetry persisted (v25 USSR Elo 1915 vs US Elo 1682), suggesting the model continued to exploit v24's weak US play rather than developing balanced strength.

### 4. Echo chamber dynamics

The v24->v25->v26 chain demonstrates the echo chamber risk:
- v24 starts from v22, eval'd vs v22 (valid)
- v24 regresses due to entropy collapse -> Elo 1757
- v25 starts from v24, eval'd vs v24 (weak opponent)
- v25 improves on v24 but diverges from frontier -> Elo 1820
- v26 starts from v25, eval'd vs v25 (still weak)
- Decision: restart v27 from v22 (breaking the chain)

The pattern shows that **once one generation regresses, using it as the next eval opponent perpetuates the regression**. The ppo_loop_step.sh sets `--eval-opponent "$FINISHED_SCRIPTED"` (line 234), which means each generation evals against its predecessor -- creating exactly this chain.

### 5. Alternatives analysis

| Criterion | Cost | Signal quality | Risk |
|-----------|------|---------------|------|
| H2H vs predecessor (current) | 7 min | Noisy, degrades with weak predecessors | Echo chamber |
| H2H vs fixed panel (v8+v14+v22+heuristic) | 28 min | Much better -- measures general strength | None if panel stays relevant |
| H2H vs v22 only (strongest known) | 7 min | Good directional signal | Single-opponent exploit risk remains |
| H2H vs heuristic only | 7 min | Stable baseline, but ceiling at ~83% WR | Cannot differentiate strong models |
| rollout_wr (already computed) | 0 min | Measures training-distribution performance, not eval | Self-play WR is ~50% by design in league |
| Final checkpoint only (no selection) | 0 min | Avoids selection bias entirely | Misses mid-run peaks from PPO overshoot |
| Elo tournament mid-training | ~5 min per eval | Gold standard | Expensive, requires scripted exports |

### 6. Cost analysis

Current: 200 games x 10 evals = 2000 games at ~0.2s/game = ~7 min overhead.
Fixed panel (4 opponents): 200 games x 4 opponents x 10 evals = 8000 games = ~28 min.
Elo tournament (6 models, round-robin): ~30 min per eval point, impractical mid-training.

The fixed panel is the sweet spot: 4x the games but still under 30 min total overhead across a 55-min training run.

## Conclusions

1. **H2H vs a single predecessor is a weak selection criterion** that has contributed to a multi-generation regression. The noise from 200 games makes it barely better than random selection among checkpoints within ~5% WR of each other.

2. **The echo chamber is the primary failure mode**, not the H2H metric itself. When the predecessor is strong (v22), the signal is directionally correct. When the predecessor is weak (v24), the signal is actively misleading.

3. **V27's setup (starting from v22, eval vs v22) is the correct configuration** for single-opponent H2H. But the ppo_loop_step.sh default of eval'ing against the predecessor will recreate the problem once v27 finishes.

4. **A fixed diverse panel is the clear improvement**: eval against {heuristic, v8, v14, v22} gives a robust general-strength signal at 4x cost (still cheap).

5. **rollout_wr is not a substitute** because league self-play targets ~50% WR by construction, so it does not differentiate checkpoints well.

## Recommendations

### Immediate (v28 onwards)
1. **Change `--eval-opponent` to accept multiple opponents** separated by commas. Compute average combined WR across all opponents. Select ppo_best.pt by highest average.
2. **Fix the panel to known-strong models**: `v8_scripted.pt,v14_scripted.pt,v22_scripted.pt,heuristic` (or pass `--eval-panel`). Do NOT use the predecessor.
3. **In ppo_loop_step.sh, stop setting `--eval-opponent "$FINISHED_SCRIPTED"`**. Instead, set a fixed panel that includes the best known model (v22 currently).

### Medium-term
4. **Increase eval games per opponent to 400** (currently 200) for ~2.5% SE instead of 3.5%. This costs ~14 min for a 4-opponent panel -- still negligible.
5. **Add a "regressed beyond threshold" early-stop**: if the panel WR drops below 0.40 for 3 consecutive evals, stop training and save the current best. This catches entropy collapse faster.
6. **Log side-specific WR asymmetry** and flag if |USSR_WR - US_WR| > 0.15 across the panel, since this was a leading indicator of the v24 collapse.

### Not recommended
- Using rollout_wr for selection (self-play league targets ~50% by design)
- Running full Elo tournaments mid-training (too expensive)
- Dropping eval entirely and using ppo_final.pt (misses PPO overshoot peaks)

## Open Questions

1. **Should ppo_best.pt selection use a weighted panel?** (e.g., 2x weight for v22 since it is the frontier). Or just unweighted average?
2. **When a new generation beats v22 in Elo, should v22 be replaced in the panel?** The panel should probably always include the current Elo champion + 2-3 weaker models + heuristic.
3. **Is there value in tracking per-opponent WR trends?** E.g., if a model improves vs v22 but regresses vs heuristic, that might indicate narrowing generalization.
4. **Would EWA (exponentially weighted average) of H2H scores across evals be more robust than max?** Max-selection is sensitive to lucky runs; EWA would smooth the noise but introduce lag.
