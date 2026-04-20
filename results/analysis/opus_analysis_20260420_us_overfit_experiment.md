# Opus Analysis: US Overfitting Experiment
Date: 2026-04-20
Question: Can we deliberately overfit to get US WR > 50%? Is it worth trying?

## Executive Summary

The proposed experiment has effectively already been run. `ppo_us_only_v5`
(side="us", v56 warmstart, 50 iters, 100% scripted-fixtures + heuristic_floor)
is the US overfitting run and reached **36% US WR vs heuristic** (benchmark
ladder). This is the all-time high-water mark for US play in the project.

The task asks whether we can push >50%. The structural ceiling argument says
this is very unlikely:

- Heuristic-vs-heuristic US WR is ~42% (game is asymmetric, USSR-favored).
- To reach 50% as US, the model must play USSR-counter-strategy meaningfully
  *better than the heuristic* — not just match it. We have no evidence the
  current architecture carries that much headroom on the US side.
- us_only_v5 is 6pp below the "fair" 42% asymmetric baseline, meaning current
  models do not even match what a symmetric copy of the heuristic would do.
  Closing that 6pp gap is plausible; adding another +8pp to exceed 50% is not.

**Headline verdict**: a second US-specialist run with the newer value-weighting
machinery (added after us_only_v5 trained) plus a us_only_v5 warmstart is
worth **one small run (30-40 iters)** as a falsification test. Prediction: plateau
at 38-42% US WR vs heuristic. If it exceeds 45%, that changes the picture; if
it plateaus below 40%, we have confirmed a structural ceiling and should stop
allocating attention to "can we train a US-specialist" as a path.

Do **not** run 80 iters. Do **not** touch v6/v7 symmetric policy. Run as a
fully isolated capacity-test directory.

## Findings

### Historical US WR ceiling

From `results/continuation_plan.json` (benchmark_ladder, 500 games/side,
post-DEFCON-1-fix engine):

| Model | US WR | USSR WR | Combined | Notes |
|-------|-------|---------|----------|-------|
| us_only_v5 | **0.360** | 0.506 | 0.433 | Single-side specialist — all-time US high |
| ussr_only_v5 | 0.316 | 0.588 | 0.452 | — |
| v56 (symmetric) | 0.325 | 0.558 | 0.441 | Current symmetric best |
| v4_ppo_iter50 | 0.160 | 0.500 | 0.330 | Wrong arch, killed |
| v3_best | 0.150 | 0.398 | 0.274 | AWR-damaged |

v6 panel eval (30 games/side per opponent, noisy) US WR vs heuristic:
iter20=26.7%, iter40=16.7%, iter60=20.0%. This is the v6 symmetric policy —
it is **not** a failed US specialist. The 17→27 swing is within 30-game noise.

Recorded in-training heuristic US WR for us_only_v5: 457/1914 = **23.9%**, but
this is during PFSP training vs a rotating league where the heuristic slot
gets only a minority of games, and rollouts are collected with exploration
temperature. The benchmark number (36%) is the honest answer.

### Game asymmetry constraints

Per `feedback_game_asymmetry.md`: heuristic-vs-heuristic US WR is ~42%. This
is the "structural floor" any US-specialist must clear just to match two
equal players sitting across from each other. Below 42% means the model is
playing *worse US than the heuristic plays US*.

**Current state**: best US model (us_only_v5) at 36% is **6pp below** the
heuristic-parity floor. The symmetric v56 at 32.5% is 9.5pp below.

For US WR to exceed 50%, the model would need:
1. Close the 6pp gap vs heuristic-parity.
2. Add another 8pp by playing US meaningfully better than heuristic-USSR
   plays USSR — i.e., the model must out-strategize the heuristic on the
   structurally disadvantaged side.

Step 1 is plausible with training. Step 2 requires evidence we don't have —
no checkpoint anywhere in project history has shown US WR >40% vs the
heuristic. Best observed symmetric-player US WR is ~42% (heuristic itself),
and no learned model has matched that. The architecture capacity appears to
cap well below 50% on the US side specifically.

### Training recipe design

Recipe for a "US overfit v6" run (propose, don't launch yet):

**Starting point**: `results/capacity_test/ppo_us_only_v5/ppo_best.pt`
(the 36% US-WR peak), NOT v56 (32.5% US floor) — start from the best
known US player, not the best symmetric player.

**Delta from us_only_v5 recipe** (knobs not yet tried):

| Knob | us_only_v5 | Proposed | Rationale |
|------|------------|----------|-----------|
| value_loss weight | 1x | 2x on US wins | Per `feedback_us_win_value_weighting`; added AFTER us_only_v5 |
| val_calib_coef | 0 | 0.1 | Mean-bias correction on value head |
| US-win filter for value targets | no | evaluate | Per `feedback_game_asymmetry` — consider but optional |
| Warmstart | v56 | us_only_v5 | Start at 36% instead of 32.5% |
| League fixtures | 5 scripted + heuristic | Heuristic-only | Pure signal, eliminate scripted-opponent noise |
| n_iterations | 50 | **40** (not 80) | Predict plateau; don't waste compute |
| ent_coef | 0.01 → 0.003 | 0.005 → 0.002 | Lower exploration; commit to US strategy |
| lr | 5e-5 constant | 3e-5 constant | Gentler finetune from already-trained US model |
| side | us | us | Same |
| heuristic_floor | 0.15 | 1.0 (100% heuristic) | Max signal, max overfit exposure |
| league_self_slot | false | false | Same |
| self_play | false | false | Same |

**Key new knob not on the table in us_only_v5**: the 2x US-win value
weighting. us_only_v5 was trained with equal value-loss weighting, and it is
possible the value head mis-orders US-winning states — a known failure mode
that the weighting fix was added to address. Rerunning with the fix is a
clean A/B against a clean baseline.

**Do not** enable dense reward shaping — that was the AWR family, confirmed
dead for policy training.

### What success/failure tells us

**If US WR >50% at iter 40**: evidence the architecture had untapped US
capacity that only emerged with value-weighting + better warmstart. Validates
spending Month-3 time on per-side heads or side-conditioned training. Also
raises the question of whether a symmetric policy can absorb this via
multi-task distillation.

**If US WR plateaus at 38-42% (most likely per prediction)**: confirms the
current architecture's US capacity is near heuristic-parity, which is the
structural floor. This is actually useful — it tells us the bottleneck is
feature expressiveness or side-conditioning, not hyperparameters. Next steps
would be architectural (dedicated US head, US-specific features like "coup
budget remaining", etc.), not more training.

**If US WR regresses below 36%**: means the value-weighting + pure-heuristic
fixtures hurt rather than helped. Would suggest us_only_v5's 36% was reached
via implicit regularization from the scripted fixtures, and the hypothesis
(overfit harder → higher WR) is wrong. Also informative.

All three outcomes produce a clear takeaway in 40 iters × ~1 min/iter on
GPU ≈ 40 minutes of training plus one benchmark. Cheap.

### Risk analysis

**Main risks**:

- **Contamination of symmetric policy**: zero risk if isolated to its own
  capacity_test directory. Don't touch v6/v7 weights.
- **Compute opportunity cost**: ~40-60 minutes of GPU time. Low.
- **Analysis noise**: 30 games/side per panel eval is very noisy (±10pp).
  Must use the post-train formal benchmark (500 games/side, fixed seeds
  50000/50500) for the verdict, not panel eval during training.
- **Checkpoint sprawl**: keep only iters 10, 20, 30, 40 + best. Delete
  rolling checkpoints aggressively.
- **Being fooled by an outlier**: a single 45% panel eval doesn't mean the
  model reached 45%. Require ≥2 consecutive iters above threshold OR
  confirmation via formal benchmark before updating beliefs.

**Not a risk** (despite task prompt language):

- "Damaging the symmetric policy" — only if we overwrite v6/v7, which we won't.
- "Specialization collapsing one side" — already true of us_only_v5 (USSR WR
  50.6% only because it was never trained as USSR in that run); expected for
  a single-side specialist.

### Abort / go criteria at iter 10

Using panel eval vs heuristic (30 games/side = noisy, but sufficient for
directional check):

- **Abort** if US WR at iter 10 is < 25% (below us_only_v5's in-training
  level — means value weighting + warmstart actively hurting).
- **Continue to iter 20** if 25% ≤ US WR < 40%.
- **Continue + run formal benchmark** at iter 20 if US WR ≥ 40% at iter 10.
- **Headline if US WR ≥ 50% at iter 10**: halt, verify with full 500-game
  benchmark immediately, document.

At iter 20, run a 200-game informal benchmark against heuristic only as a
mid-run checkpoint — cheaper than the full 1000-game sweep and sufficient
to decide whether to continue to iter 40.

## Conclusions

1. The experiment effectively already ran (`us_only_v5`, 36% US WR). The
   question is whether a *better-tuned* second run can break 50%.

2. Structural argument (heuristic-vs-heuristic US WR = 42%) implies >50%
   requires the model to beat the heuristic as US by 8pp on the
   disadvantaged side, which has no precedent in this project's history.

3. Most plausible outcome: 38-42% US WR. That would be a new high but would
   not reach 50%. This is still informative — it confirms the ceiling is
   architectural, not training-recipe.

4. Least plausible but not impossible: >45% US WR via the combination of
   us_only_v5 warmstart + 2x US-win value weighting + val_calib — knobs
   that did not exist when us_only_v5 was trained.

5. Running the experiment is cheap (~1 GPU hour) and has clean isolation.
   The information value of either outcome (confirmed ceiling vs surprise
   breakthrough) justifies the cost.

6. **Recommendation**: run, with the recipe above, 40 iters max, in
   `results/capacity_test/ppo_us_overfit_v1/`. Abort at iter 10 if US WR
   < 25%. Formal benchmark at end.

## Recommendations

### Concrete launch command (dry run — do NOT auto-launch without user confirm)

```bash
nohup uv run python scripts/train_ppo.py \
  --checkpoint results/capacity_test/ppo_us_only_v5/ppo_best.pt \
  --reset-optimizer \
  --out-dir results/capacity_test/ppo_us_overfit_v1 \
  --version us_overfit_v1 \
  --n-iterations 40 \
  --games-per-iter 200 \
  --ppo-epochs 4 \
  --clip-eps 0.12 \
  --lr 3e-5 \
  --lr-schedule constant \
  --gamma 0.99 --gae-lambda 0.95 \
  --ent-coef 0.005 --ent-coef-final 0.002 \
  --vf-coef 0.5 --val-calib-coef 0.1 \
  --minibatch-size 2048 \
  --eval-panel __heuristic__ \
  --eval-every 10 \
  --side us \
  --seed 42100 --device cuda \
  --wandb --wandb-project twilight-struggle-ai \
  --wandb-run-name ppo_us_overfit_v1 \
  --max-kl 0.03 --ema-decay 0.995 --target-kl 0.015 \
  --league results/capacity_test/ppo_us_overfit_v1 \
  --league-save-every 999 \
  --league-mix-k 2 \
  --league-fixtures __heuristic__ \
  --heuristic-floor 1.0 \
  --league-recency-tau 20 \
  --league-heuristic-pct 1.0 \
  --league-fixture-fadeout 999 \
  --league-self-slot \
  --pfsp-exponent 0.5 \
  --upgo \
  --skip-smoke-test \
  > results/capacity_test/ppo_us_overfit_v1/train.log 2>&1 &
```

(Verify the exact flag names against `scripts/train_ppo.py` argparse block
before launch — I worked from a mix of ppo_args.json keys and code
inspection; naming may need minor translation. `--league-self-slot` is
included so the model also rolls out vs itself; pure heuristic-only tends to
create a one-note opponent.)

### Decision gates

1. At iter 10: check panel US WR vs heuristic. If <25%, kill. If <35%, continue
   but lower expectations.
2. At iter 20: run 200-game benchmark (`python scripts/bench_vs_heuristic.py
   --ckpt ... --n 200 --side us`). If <35%, kill. If ≥40%, continue.
3. At iter 40: formal 500-game/side benchmark. Record in benchmark_history.
4. Whatever happens: add a row to `results/continuation_plan.json`
   benchmark_ladder and a note to the MEMORY log.

### Follow-up experiments (only if iter 40 shows >42% US WR)

- Same recipe but with US-win value filter (only score value loss on US-win
  steps; skip US-loss steps entirely).
- Try lr=1e-5 and 80 iters for longer-tail finetune.
- Distill the US-specialist into the symmetric policy via a KL-reg finetune
  of v6 toward the US-specialist on US-side-only states.

## Open Questions

- Is the 42% heuristic-vs-heuristic US WR figure still accurate post-DEFCON-1
  engine fix? The memory is from 17 days ago and the fix changed base rates.
  Worth measuring fresh: 1000 games heuristic-vs-heuristic and report US WR.
  If the true number is e.g. 38%, it shifts all the targets down proportionally.
- Does `ppo_us_only_v5/ppo_best.pt` load cleanly into current-head-of-main
  training code? Frame-context scalar dim changed (32→40); the loader has
  auto-padding per continuation_plan.json, but us_only_v5 was trained before
  the frame migration. Verify before launching.
- Is a dedicated US-specific feature set (coup budget, DEFCON margin, Asia
  influence deficit, etc.) the actual bottleneck? This experiment doesn't
  test that — it only tests whether existing features + better training can
  reach 50%.
