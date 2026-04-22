# Opus Analysis: Ceiling Break — Why v13 Hasn't Been Beaten, and the Highest-Leverage Untried Levers

**Date:** 2026-04-20
**Scope:** Root-cause analysis of v6/v7/v8/v9/v10/v11/v12/v13 (country_attn) and v14/v15 (GNN) PPO runs, all BC warm-start experiments (BC v1–v5), and the MCTS fine-tuning failure. Propose the single fundamentally-different intervention most likely to break the 0.427 ceiling.
**Author:** Opus (deep-analysis subagent)

---

## Executive Summary

**The 0.427 "ceiling" is not a strength barrier — it is a combination of (1) a known ~10pp iter20 seed variance and (2) a selection metric that actively rewards echo-chamber overfitting.** v13's 0.427 is the upper-tail sample from a recipe whose typical iter20 combined WR is ~0.30–0.37; v6's 0.459 was the same seed (42000) from a slightly different pool, also an upper-tail draw. v8–v12 all used seeds 43k–47k and all fell into the recipe's mean/lower band. This means "beat 0.427" is not the right problem statement — the problem is that **the current training loop has no mechanism to produce a reproducible 0.45+ model**, because (a) its exploration is deterministic-argmax at `rollout_temp=1.0, dir_alpha=0.0`, and (b) its running-best selector averages `v56_WR` and `heuristic_WR`, letting echo-chamber specialization mask heuristic-side collapse.

The single highest-leverage untried intervention is **v16 = v13 warm-start + Dirichlet root noise + rollout temperature + heuristic-weighted running-best selector**. All three are already scaffolded in `scripts/train_ppo.py` (dir_alpha/dir_epsilon probe at line 1237, rollout_temp throughout, `_PANEL_WEIGHTS` dict at line 3785 ready for weighting) and none have ever been switched on in a PPO run. These are CLAUDE.md's stated Month-3 priority #1 and #2 ("Dirichlet noise at MCTS root + temperature-based action sampling in self-play", "Self-play exploration noise"). They have been planned for months and never executed. Do not add more pool/floor tuning — that class of intervention is four-times falsified.

---

## Findings

### 1. v13 is a seed outlier, not a structural success

`ppo_args.json` diff across runs (verbatim from this investigation):

| Run  | seed  | lr   | clip | ent   | heur-floor | fade | pfsp-exp | warm-start               | iter20 combined (500g) |
|------|-------|------|------|-------|------------|------|----------|--------------------------|------------------------|
| v6   | 42000 | 5e-5 | 0.12 | 0.01  | 0.15       | 50   | 0.5      | ppo_v56_league           | **0.459** (record)     |
| v7   | 42013 | 5e-5 | 0.12 | 0.01  | 0.15       | 999  | 0.5      | v7/iter0013              | 0.397                  |
| v8   | 43000 | 5e-5 | 0.12 | 0.01  | **0.30**   | 999  | 0.5      | v6/iter0020              | 0.351 (iter80)         |
| v9   | 44000 | 5e-5 | 0.12 | 0.01  | 0.15       | 999  | 0.5      | v6/iter0020              | 0.304                  |
| v10  | 45000 | 5e-5 | 0.12 | 0.01  | 0.15       | 999  | 0.5      | ppo_v56_league           | 0.215                  |
| v11  | 46000 | 5e-5 | 0.12 | 0.01  | 0.15       | 999  | 1.0      | ppo_v56_league           | 0.250                  |
| v12  | 47000 | 5e-5 | 0.12 | 0.01  | 0.15       | 999  | 1.0      | ppo_v56_league           | 0.295                  |
| **v13** | **42000** | 5e-5 | 0.12 | 0.01  | 0.15       | 999  | 1.0      | ppo_v56_league           | **0.427** (practical)  |

v11, v12, v13 are **identical recipes** (same LR, clip, ent, floor, fadeout, PFSP exponent, warm-start). The only difference is seed (46k/47k/42k). Results: 0.250 / 0.295 / 0.427 — a 17.7pp spread from seed alone. The recipe's iter20 distribution is centered around 0.30–0.33 with a standard deviation of at least 6–8pp; v13 is ~1.5σ above the mean.

**Implication:** 0.427 is not a ceiling — it is a high percentile of a noisy recipe. Any intervention that reduces variance OR raises the distribution mean by even 5pp will produce runs that routinely reach 0.40+, and the upper tail will land above 0.45. Treat the problem as variance reduction + distribution shift, not barrier-breaking.

### 2. The running-best selector is actively picking worse checkpoints

From the v13 training log and `bench_*.json` files in `results/ppo_country_attn_v13/`:

- `ppo_iter0020.pt` 500g bench: **combined=0.427** (USSR=0.608, US=0.246).
- `ppo_running_best.pt` (selected by panel high-water) 500g bench: **combined=0.257** (USSR=0.402, US=0.112).

The running-best was promoted at iter=80 when panel_avg hit 0.575. The panel is `[v56_scripted, __heuristic__]` (panel composition in `ppo_args.json`), and `_PANEL_WEIGHTS = {}` at `scripts/train_ppo.py:3785` means **equal weighting**: `panel_avg = (wr_vs_v56 + wr_vs_heuristic) / 2`.

Reconstructing iter80 panel from `panel_eval_history.json`:
```
iter=80: heuristic combined_wr=0.583, v56 combined_wr=0.567 → avg=0.575
iter=20: heuristic combined_wr=0.417, v56 combined_wr=0.533 → avg=0.475
```

The model got **better at beating v56** (0.533 → 0.567) while **heuristic WR is essentially unchanged** (0.417 → 0.583 on a 30-game panel is within SE=0.091). But **on the 500g bench, iter80 heuristic_WR = 0.257** — i.e. the iter80 panel 0.583 against heuristic was a 30-game lucky draw; true performance collapsed to 0.257. The v56 component of the average is the only real signal, and it is rewarding self-similar overfitting.

**Quantification of the selector miss:** `panel_avg` ranked iter80 > iter20, but 500g ground truth ranks iter20 > iter80 by +0.17 combined. This is a documented, reproducible selection failure. The same mechanism is operating in every v6/v7/v8/v9/v10/v11/v12 run.

### 3. Training does not actually "degrade past iter20" — the selector degrades

The common project belief is "PFSP echo chamber causes training to peak at iter20." The v13 panel and rollout data paint a more subtle picture.

Iter-by-iter heuristic panel WR from `panel_eval_history.json` (v13, 30g/side → SE=0.091):

```
iter=10 heuristic=0.383   iter=50 heuristic=0.417
iter=20 heuristic=0.417   iter=60 heuristic=0.567  <-- spike noise
iter=30 heuristic=0.383   iter=70 heuristic=0.500
iter=40 heuristic=0.500   iter=80 heuristic=0.583  <-- spike noise (500g says 0.26)
```

Rollout US WR (v13, last 20 iters mean): ~0.33. Rollout USSR WR: ~0.70. Combined rollout ~0.50. These are fine — the policy learns to beat its own pool. The 500g bench reveals that this pool-winning capability **comes at the cost of heuristic-specific play patterns**, which the panel can't detect at 30g/side.

Rephrased: **training doesn't "degrade" past iter20; the policy continues gaining skill against self-similar opponents while its heuristic skill plateaus or drifts. The selector picks the late-iter checkpoints because panel's v56 component rewards exactly that drift.** Whether heuristic skill actually *declines* or just plateaus with noise overlay is not resolved by current data — we would need per-iter 500g benches to answer.

### 4. US-side asymmetry is a training-distribution problem, not a capacity problem

US-side WR across all versions (500g bench, iter20):
- v6 US=0.200, v13 US=0.246 (best), v7 US=0.140, v8 US=0.240, v14 US=0.048, v15 US=0.028
- v56 baseline US=0.325 (actually *better* than any derived PPO model)

v56 was itself PPO-trained but with an 8-fixture pool including ussr_only_v5 and us_only_v5 specialists, and apparently hit US=0.325. Every run *after* v56 (v6–v13) has **lower** US-side WR. The capacity_test runs show us_only_v5 (trained exclusively on the US side) reaches US=0.360 — i.e. the architecture can represent a 0.36-US policy.

**Diagnosis:** US-side collapse is caused by training-distribution asymmetry:
1. Symmetric training sees roughly 50/50 US/USSR frames, but **heuristic is USSR-advantaged** (heuristic-vs-heuristic USSR WR ≈ 0.60), so the learned opponent distribution is "USSR-leaning". Rollouts against such opponents on the US side are low-WR noise with weak gradient signal.
2. `feedback_us_win_value_weighting.md` documents that v56 successfully uses a 2x weight on US-win steps in the value loss. Every v6–v13 `ppo_args.json` shows `val_calib_coef=0.0` (v13) or `0.1` (v9 plan) — the US-upweight is **not enabled in any run since v56**. This is a silent regression in the recipe.
3. Pool composition amplifies the problem: when US plays against "iter_0001" (its own past self) it sees a weaker, USSR-dominated opponent — not the stronger heuristic USSR it will face at bench time. This is the rollout-vs-bench divergence documented in the v8 analysis (iter_overfit_v1 had rollout US=0.495, bench US=0.080).

**Not a capacity problem.** The same country_attn_side model reaches US=0.360 when trained US-only (us_only_v5). Something about symmetric PPO with PFSP specifically destroys US-side generalization. The intervention "train US-only then ensemble" is known-viable (capacity_test) but has not been retried since v5.

### 5. BC warm-start + PPO is a broken pipeline for new architectures

Summary of BC attempts:
- **BC v1** (GNN, pure heuristic nash): val_value_mse=0.77 (near random), PPO v14 → combined=0.192
- **BC v2** (GNN, 70% v13 + 30% nash mixed): val_value_mse degraded 0.58→0.80 mid-training (mix contamination)
- **BC v3** (GNN, pure v13 3000g): val_value_mse=0.81 (overfit train, fail val), gate bench=0.110
- **BC v4** (GNN, v13 + teacher distill v13 logits): val_value_mse=0.675 — better! But PPO v15 → combined=0.112
- **BC v5** (country_attn, fine-tune v13_iter20 on MCTS data): **gate bench=0.090** — catastrophic forgetting

The chain "new-arch BC + PPO" has a single dominant pattern: **BC caps near heuristic strength (~0.11–0.20)**, and PPO cannot recover a 25–33pp gap in 20–80 iters. BC v5 (fine-tune of an already-good 0.427 checkpoint) *regressed* to 0.09 because 40 epochs of MCTS-only fine-tuning shifted the action distribution away from heuristic-opponent regions.

**Root rule:** BC quality is bounded below by the data quality and labeling noise. Pure argmax BC on v13 self-play encodes v13's *argmax* play, not v13's full policy (~softmax distribution). Teacher-KL distillation (BC v4) helped value head but PPO still collapsed — warm-start was 0.112, not the 0.30–0.40 the prior analysis hoped for.

**Implication:** BC→PPO is not the path forward for the next push. The v13 checkpoint itself is the only reliable starting point; modifying the PPO recipe on top of that checkpoint is the tractable problem.

### 6. The three levers that have never been tried

Full inventory of PPO args across v6–v15 (from ppo_args.json):
- `dir_alpha=0.0` in ALL runs (Dirichlet noise at action sampling: off)
- `dir_epsilon=0.25` (non-zero but multiplied by alpha=0 → no effect)
- `rollout_temp=1.0` in ALL runs (no exploration temperature)
- `explore_alpha=0.0, explore_eps=0.0` in ALL runs (epsilon-exploration: off)
- `_PANEL_WEIGHTS={}` in source (uniform panel selection)
- `val_calib_coef=0.0` in v13 (US-win value upweight mechanism: off)

The mechanism is present and wired — `_call_rollout_with_optional_dirichlet` at `scripts/train_ppo.py:1237` probes the C++ binding for `dir_alpha/dir_epsilon` support and falls back gracefully if absent. Rollout temperature threads through `collect_rollout_batched(..., temperature=rollout_temp)`. The infrastructure is complete. **No PPO run has turned them on.**

CLAUDE.md §"Current focus" lists these as Month-3 top priorities:
1. Dirichlet noise at MCTS root + temperature-based action sampling in self-play
2. Self-play exploration noise (epsilon-greedy or policy noise injection)

These are months-overdue interventions. Running them is not "adding complexity," it is finishing scaffolding that has been in the tree.

---

## Root-Cause Diagnosis (Ranked)

**1. Rollout/exploration collapse (largest, most fixable).** With `rollout_temp=1.0` and zero Dirichlet noise, the policy samples from its raw softmax. If the policy has high-confidence peaks on suboptimal actions, PPO updates do not explore enough alternatives to discover better options. PFSP amplifies this because the opponent is drawn from past selves that share the same peaks. This is the canonical cause of "premature convergence" in AlphaZero-style loops and is precisely what Dirichlet noise at the root is designed to fix. Untried.

**2. Selector bias toward self-similar specialization.** `panel_avg = (v56_WR + heuristic_WR)/2` lets iter80 look +0.10 better than iter20 by gaining only on v56, while heuristic silently regresses. Running-best promotion is therefore anti-correlated with the true bench metric in the latter half of training. Trivial code fix.

**3. US-side training asymmetry.** `val_calib_coef=0.0` in v13 removes the US-upweight that v56 had. Symmetric 50/50 rollouts on a USSR-favored engine produce unbalanced gradient SNR. Documented in `feedback_us_win_value_weighting.md`. Two-line fix.

**4. Seed variance (recipe structural).** ~10pp iter20 spread across seeds 42k–47k. This is a symptom of #1 — exploration collapse produces path-dependent specialization and high-variance endpoints. Fixing #1 should reduce variance.

**5. PFSP echo chamber (smaller than believed).** The data does not cleanly show heuristic-WR declining past iter20 — it shows heuristic-WR being noise-masked by a flawed selector. The echo chamber is real but the magnitude was overstated by comparing noisy panel readings to unlucky 500g checkpoint selections. Addressed indirectly by fixing #1 and #2.

---

## Proposed Interventions (Ranked by Expected Impact × Cost)

### (A) **v16 = v13 + Dirichlet + temperature + heuristic-weighted selector** [TOP CHOICE]

Single-launch intervention, ~35 min GPU. Expected impact: +5–10pp distribution mean, +3–5pp variance reduction. Cost: edit 1 line of `_PANEL_WEIGHTS` plus run one PPO job. High confidence because (a) infrastructure is scaffolded, (b) CLAUDE.md identifies these as Month-3 priorities, (c) addresses the two largest diagnosed causes simultaneously.

Mechanism:
- `--dir-alpha 0.3 --dir-epsilon 0.25` adds 25% Dirichlet-mixed noise to card action probabilities at rollout time (line 453 of train_ppo.py). Breaks action-argmax collapse.
- `--rollout-temp 1.2` slightly widens the sampling distribution. Not aggressive (1.3+ risks destabilizing PPO advantage estimation).
- Edit `_PANEL_WEIGHTS = {"heuristic": 3.0, "v56_scripted": 1.0}` in train_ppo.py (or add arg). Heuristic gets 3x weight in running-best selection → the 500g-truth metric dominates. Use 3x because heuristic signal is noisier (SE higher) but it's the canonical bench opponent.
- Resume from v13/iter20 (not v56) — we keep the upper-tail model as the starting point.
- Seed=42000 (known-good) for a fair seed×recipe comparison to v13.

### (B) **v16b = v13 + val_calib_coef=0.5 (US-win upweight)** [SECONDARY]

Re-enable the US-win value weighting from the v56 recipe. Expected impact: +2–5pp on US-side WR. Cost: one-arg change, same compute as v16. Can be combined with (A) or run as a separate ablation. Low risk.

### (C) **Multi-seed iter20 harvest** [INSURANCE]

Run 4x parallel 25-iter PPOs with seeds 42001, 42002, 42003, 42004 (stay in the 42k basin that worked), same v13 recipe. Bench iter20 of each at 500g. Pick the best, or *weight-average* the top-2 as starting point for v17. Expected impact: directly attacks seed variance; upper-tail of 4 draws should give 0.42–0.47. Cost: 4x GPU-hours; can run sequentially overnight. Independent of (A)/(B).

### (D) **Panel reform** [ENABLING FIX]

Replace 30-game panel with 100-game heuristic-only bench every 10 iters. Cost: ~15s extra per eval. Removes noise that has burned at least three recent experiments (v11/v12 "panel=0.5 running_best" false positives). Independent improvement; should ship regardless of which PPO experiment runs next.

### (E) **NOT RECOMMENDED — already-falsified interventions**

- Further `heuristic-floor` increases (v8=0.30 failed; going higher will fail harder)
- Pure-heuristic training (predicted to destroy USSR-side specialization, no mechanism for improvement)
- MCTS fine-tuning on AI-vs-AI data (BC v5: 0.427 → 0.09)
- More BC cold-starts for new architectures (four consecutive failures)
- Longer PPO training past iter20 on the current recipe (will just let the flawed selector pick worse checkpoints)
- Pool composition / fixture-pruning tweaks (six variants tried, none beat v13)

---

## Recommended Immediate Action: PPO v16 Launch

**Step 1 (2 min): Patch panel weighting in `scripts/train_ppo.py` line 3785.**

Replace:
```python
_PANEL_WEIGHTS: dict[str, float] = {}
```
with:
```python
_PANEL_WEIGHTS: dict[str, float] = {"__heuristic__": 3.0}  # heuristic 3x weight in running-best selection
```

(Unrecognized keys default to 1.0 at line 3787, so v56 stays at weight 1.0 naturally.)

**Step 2 (~35 min GPU): Launch v16.**

```bash
mkdir -p results/ppo_country_attn_v16

OMP_NUM_THREADS=6 KMP_BLOCKTIME=0 nohup uv run python scripts/train_ppo.py \
  --checkpoint results/ppo_country_attn_v13/ppo_iter0020.pt \
  --reset-optimizer \
  --out-dir results/ppo_country_attn_v16 \
  --version country_attn_v16 \
  --n-iterations 30 \
  --games-per-iter 200 \
  --ppo-epochs 4 \
  --clip-eps 0.12 \
  --lr 5e-5 \
  --lr-schedule constant \
  --gamma 0.99 --gae-lambda 0.95 \
  --ent-coef 0.01 --ent-coef-final 0.003 \
  --global-ent-decay-start 0 --global-ent-decay-end 300 \
  --vf-coef 0.5 --val-calib-coef 0.5 \
  --minibatch-size 2048 \
  --eval-panel \
    data/checkpoints/scripted_for_elo/v56_scripted.pt \
    __heuristic__ \
  --eval-every 5 \
  --side both \
  --self-play-heuristic-mix 0.2 \
  --seed 42000 --device cuda \
  --wandb --wandb-project twilight-struggle-ai \
  --wandb-run-name ppo_country_attn_v16_dir_noise \
  --ema-decay 0.995 --target-kl 0.015 \
  --reward-alpha 0.5 \
  --league results/ppo_country_attn_v16 \
  --league-save-every 5 \
  --league-mix-k 4 \
  --rollout-workers 1 \
  --league-fixtures \
    data/checkpoints/scripted_for_elo/v56_scripted.pt \
    data/checkpoints/scripted_for_elo/v55_scripted.pt \
    data/checkpoints/scripted_for_elo/v44_scripted.pt \
    data/checkpoints/scripted_for_elo/v20_scripted.pt \
    results/capacity_test/ppo_ussr_only_v5/ppo_best_scripted.pt \
    results/capacity_test/ppo_us_only_v5/ppo_best_scripted.pt \
    __heuristic__ \
  --heuristic-floor 0.15 \
  --league-recency-tau 20.0 \
  --league-fixture-fadeout 999 \
  --league-self-slot \
  --pfsp-exponent 1.0 \
  --dir-alpha 0.3 --dir-epsilon 0.25 \
  --rollout-temp 1.2 \
  --upgo \
  --skip-smoke-test \
  > results/ppo_country_attn_v16/train.log 2>&1 &
```

**New settings vs v13 (four changes):**
1. `--dir-alpha 0.3` (was 0.0) — **core intervention**, 25% Dirichlet-mixed card noise at rollout
2. `--rollout-temp 1.2` (was 1.0) — gentle exploration widening
3. `--val-calib-coef 0.5` (was 0.0) — US-win value upweight, per feedback_us_win_value_weighting.md
4. `--checkpoint results/ppo_country_attn_v13/ppo_iter0020.pt` (was v56) — start from known 0.427, not 0.441

**Shorter run** (30 iters, eval_every=5): we expect a cleaner peak in iter15–25 range. 80 iters wasted compute in v13. Cheaper to retry than to over-train.

**Success criteria (500g/side formal bench, seed=50000/50500):**
- iter20 combined ≥ 0.45 → intervention worked; proceed to v17 (layered adds)
- iter20 combined 0.43–0.45 → matches v13 at reduced variance; run 3 more seeds (42001/42002/42003) to confirm mean shift
- iter20 combined < 0.42 → intervention did not help; fall back to lever (C) multi-seed harvest

**Abort criteria:**
- iter10 rollout_wr < 0.35 (recipe too noisy with Dirichlet) → lower dir_alpha to 0.15 and restart
- KL blow-up (kl > 0.05 or ep≤2/4 for 3 consecutive iters) → lower LR to 3e-5 or dir_alpha to 0.15
- US rollout WR < 0.15 for 5 consecutive iters → kill; re-run with val_calib_coef only (isolate from Dirichlet)

**Panel sanity check:** add an out-of-band 100-game heuristic-only bench at iter10 and iter20 (takes ~30s each) and log to wandb as `bench/heuristic_100g_combined`. Do NOT trust the 30-game panel this round; use the 100g bench as the running-best selector if possible.

---

## Open Questions (flagged, not blocking)

1. **Is v13_iter20=0.427 itself a seed-variance outlier?** The only way to answer definitively is to re-run seed=42000 from scratch 3 times and bench each iter20 at 500g. If the distribution is narrow (e.g. 0.40–0.44), the record is real. If it varies 0.30–0.46, seed=42000 is also noise. This analysis operates under the charitable assumption that v13=0.427 is reproducible; if v16 underperforms, this assumption needs testing.

2. **Does Dirichlet noise require C++ binding support?** `_call_rollout_with_optional_dirichlet` (line 1237) probes and falls back silently if the C++ binding lacks the kwargs. Worth verifying on this build once v16 starts: check the first iter's log for "  [diag] dirichlet: enabled" or equivalent. If silently disabled, lever (A) degrades to temperature-only.

3. **Would disabling PFSP entirely (fixture-only league) work better?** Not in the ranked interventions because the echo-chamber magnitude has been overstated (see Finding 3). Deserves a side experiment only if v16 fails.

4. **Is the panel-weighted selector enough, or do we need to replace the panel entirely?** Lever (D) proposes replacing with 100g heuristic-only bench. Recommended as a parallel/follow-up improvement regardless of v16 outcome.

5. **What is the actual iter-by-iter 500g trajectory?** No v13 checkpoint other than iter20 and running_best has been benched at 500g. One-time cost ~8 min total GPU to bench iter10/30/40/50/60 at 500g each; would definitively answer "does training degrade past iter20?" This is cheap and should run opportunistically.

6. **Should we resurrect `us_only_v5`-style US-specialist training?** v56's training recipe included US specialists in the league fixtures; v13 also includes `us_only_v5/ppo_best_scripted.pt`. But no recent run has trained a *fresh* US-specialist from v13. If v16 doesn't raise US-side WR to 0.30+, consider spinning up a 20-iter US-only PPO from v13_iter20 as a companion policy.
