# Opus Analysis v2: Post-Plateau Next Move — v34 PFSP Pool Refresh

Date: 2026-04-20 (second pass, post-falsification)
Prior analysis falsified: `results/analysis/opus_analysis_20260420_180000_post_plateau_next_move.md`
Chain status: v32_iter20 = 0.650 combined WR / 1370 combined Elo; v29/v31/v32/v33 statistically tied (±20 Elo at 400 games/pair).

## Executive Summary

The highest-EV next autonomous move is a **config-only PPO v34 with a refreshed PFSP pool**: swap the stale `league_fixtures=[v56, v55, v44, __heuristic__]` (all 70–100 Elo weaker than v32) for `[v29_continue, v31_continue, v33_continue, __heuristic__]` (the only peer-level opponents in the repo). v32 is *already* using PFSP — but its non-heuristic gradient is ~50% coming from opponents it dominates. No code, no BC stage, no weight transfer, no new architecture: one 20-iter PPO run, warm-started from v32_iter20 with the ceiling recipe otherwise unchanged. Primary verifiable premise: v29/v31/v33 are all 6-mode shape-compatible (**verified**) and all have combined Elo within 20 points of v32. Secondary parallel move: enable dense reward shaping (`reward_shaping=true, dense_reward_alpha=0.2`), which is currently **off** in v32 config — this is a live, untried lever (not a retune). Reject trunk expansion, US-specialist distillation, cold-arch experiments: all share the falsified class of the prior Opus rec.

## Premise corrections from the original task brief

The task brief contains three premise errors worth naming up front (these shaped earlier reasoning):

1. **"v32 PPO uses pure-heuristic rollouts"** — FALSE. `ppo_args.json` shows `league_fixtures=[v56, v55, v44, __heuristic__]`, `heuristic_floor=0.5`, `league_self_slot=true`. v32 is already ~50% heuristic + 50% PFSP over 3 fixtures + self-slot.
2. **"GAE lambda=1.0 (currently?)"** — FALSE. v32 uses `gae_lambda=0.95`. Already tuned.
3. **"heuristic-floor=0.50 is dense reward"** — conflation. `heuristic_floor` controls PFSP opponent selection (min probability of heuristic in the pool). Actual reward config: `reward_shaping=false, dense_reward_alpha=0.0, vp_reward_coef=0.0`. **Dense reward is OFF.** This means candidate #4 "different dense shaping signal" is not a retune; it is a truly untried lever.

These corrections shift the answer substantially. In particular, candidate #3 (PFSP mixture) reduces to "which fixtures?" not "add PFSP", and candidate #4 reduces to "turn on reward shaping" not "change lambda".

## Findings: evaluation of the 7 candidates

### C1. Data volume (Task #64: 4M row extended dataset) — DEFER
**Premise check:** PPO is on-policy. Fresh rollouts are 200 games/iter (~4000 games/run). A 4M-row offline dataset only matters for BC warm-start.
**Verdict:** Not applicable to the v32 chain without an architecture change. Helpful only if we later move off `country_attn_side`. Defer until such a move is on the table; at that point it becomes essential (prior lesson: cold-arch BC < 0.20 is unrecoverable).

### C2. Trunk capacity 256→512/768 + weight-transfer — REJECT
**Premise check:** TRUNK_HIDDEN=256 in `python/tsrl/policies/model.py:56`. Confirmed. Weight transfer from v32 to a 512-wide trunk would require random-init on the expansion dims + either full retrain (no warm-start benefit) or freeze-and-adapt (which only increases capacity in the random-init subspace = BC-from-scratch on the new dims).
**Class-match to prior falsified rec:** YES. R1 in the previous Opus analysis was weight-transfer + new head; it relied on the premise that "v32 trunk absorbs new features cheaply." Empirically this premise is unvalidated and matches the falsified pattern. v14/v15 cold-arch BC showed a 33pp warm-start gap is unrecoverable in 20 iters even with teacher KL; trunk-expansion produces a similar (smaller but non-zero) gap on the new-dim subspace.
**Cost/risk:** ~4 GPU-hours BC + 6 PPO + regression risk. Upside speculative (no prior evidence that 256 is capacity-bound).
**Verdict:** Reject. Higher cost than C3, matches falsified class, no verified premise of capacity-boundedness.

### C3. Opponent diversity in PPO (peer-level PFSP pool refresh) — PRIMARY
**Premise check:** v32 `league_fixtures = [v56, v55, v44, __heuristic__]`. Per fresh Elo table: v56=1277 combined, v55 ≤ v56 (older), v44 ≤ v56. All are **70–100 Elo below v32 (1370)**. The only peer-level opponent in v32's training mix is itself (`league_self_slot=true`). **Verified:** v29_continue, v31_continue, v33_continue all have `mode_head.weight` shape `(6, 256)` identical to v32 (`torch.jit.load` check). v56 is 5-mode; trainer has been handling the mode-mismatch since 2026-04-19 engine fix. Swapping to 6-mode fixtures is strictly simpler.
**Expected effect:** PFSP's `(1-WR)` term is near zero against v56 (v32 beats v56 ~65–70% in combined rollouts), so those slots contribute weak gradient. Against v29/v31/v33, v32's WR is ~50% (by Elo), giving maximal gradient variance per PFSP theory. Breaking "v32 beats v32 by epsilon" requires opponents at v32's level — which only exist in the chain itself.
**Cost:** Zero code. One line change in the launch script: replace fixture paths. One 20-iter PPO run = ~4 hours wall clock (v32's observed rate).
**Risk:** If v29/v31/v33 are too similar to v32, the rollout mixture becomes approximate self-play, risking echo-chamber drift (v11/v12 pattern). Mitigation: `heuristic_floor=0.5` is *retained*, ensuring 50% of non-self slots stay on heuristic. This makes the change isolated to "replace 3 weak fixtures with 3 strong fixtures" in the other 50%.
**Verdict:** PRIMARY. Verifiable premise, lowest cost, directly addresses a measurable flaw.

### C4. Rethink reward shaping — SECONDARY (parallel)
**Premise check (corrected):** `reward_shaping=false, dense_reward_alpha=0.0, vp_reward_coef=0.0`. Dense reward is **OFF** in v32. This is not a retune — it's an untried lever.
**Expected effect:** With `gae_lambda=0.95` and sparse terminal reward, the value head learns from outcome signal only. Enabling `dense_reward_alpha=0.2` + `reward_shaping=true` gives per-step VP/ops signal. Risk: shapes the policy toward heuristic-style VP grabbing, which is double-edged (v32's US side under-plays; US is the bottleneck per prior analysis).
**Cost:** Zero code. Two config flags.
**Verdict:** SECONDARY. Run as a parallel third iteration if C3 returns a neutral/marginal result. Not primary because (a) reward-shaping's historical record in this repo is mixed, (b) the asymmetry of the current bottleneck (US-side) is not obviously addressed by dense VP reward.

### C5. Self-play with soft anchor — REJECT (for now)
**Premise check:** Self-play regressed v11/v12 (echo chamber). v32 is stronger now (+20–40 combined WR), but the mechanism of collapse (no outside anchor) is unchanged. The task brief proposes 30% self-play / 70% heuristic. However, v32 *already* has 50% heuristic + self-slot via `league_self_slot=true`. Moving to "true self-play collect" (model-vs-model rollouts generating gradient on both sides) is a separate code path.
**Class-match:** Similar risk class to v11/v12; inadequate verified premise that "v32 is strong enough to self-play without collapse".
**Verdict:** Reject for now. C3 is effectively a partial self-play (peer fixtures include v29/v31/v33 which are near-copies), with safer bounds.

### C6. Novel architectural delta — REJECT (until C3/C4 fail)
Every architectural intervention tried so far (GNN adj, FiLM, card_attn, country_alloc_head, cross-attn models) has failed to beat v32. The task brief asks for a novel delta "you haven't considered." Candidates I would consider:
- **Autoregressive country decoder** (sequential country-by-country with attention over prior picks)
- **Card embedding improvements** (learned card embeddings vs current linear `card_encoder` in `TSCountryAttnSideModel:1827`)
- **Multi-token action factorization** (separate heads for "which region first" → "which countries in region")

All of these require:
1. New architecture with weight-transfer OR cold-arch BC. Weight-transfer class: matches falsified prior rec. Cold-arch BC: falsified by v14/v15.
2. Prior infrastructure (teacher soft labels, BC pipeline, PPO warmstart).
**Verdict:** Reject until the *infrastructure* has been re-validated by a successful cheaper experiment. If C3 yields +10–30 Elo, the teacher quality is higher and a new arch has a better BC warm-start starting point.

### C7. Stop at 1370 Elo / shift metric to learned-opponent Elo — HONEST FALLBACK
**Premise check:** Heuristic-vs-heuristic is 72/28 USSR-favored (from memory / `feedback_game_asymmetry`). bid+2 is applied. If heuristic-USSR vs heuristic-US is ~72/28, a learned model playing US against heuristic-USSR has a ceiling somewhere between 0.28 (matching the losing side) and ~0.60 (if it perfectly exploits heuristic errors from the US side). v32's US WR = 0.512 is already well above the heuristic-US mirror result and suggests the *learned model playing US is beating the heuristic's US replay by ~23pp*. It's not at a structural bid+2 ceiling, but the remaining gap (0.512 → ~0.60) is small.
v32's USSR WR = 0.788, ~16pp above the heuristic-USSR mirror. Also probably near an exploitative ceiling against a deterministic heuristic.
**Implication:** The combined "0.650 vs heuristic" is *not* a hard structural bound, but it is approaching the "how much can you exploit a deterministic opponent" asymptote. Honest evaluation should use the per-side Elo ladder (which we have: `elo_fresh_panel.json`) as primary, not heuristic WR.
**Verdict:** Not a "give up" — a **metric shift for success criteria on C3/C4**. If C3 fails to move heuristic WR, but moves *combined Elo* on the fresh ladder by ≥20 points, that's still a win. Adopt combined Elo (not heuristic WR) as primary success metric for v34.

## Conclusions & ranking

1. **C3 (PFSP pool refresh) — PRIMARY v34.** Verified premise, zero code, ~4h run, targets measurable flaw (stale fixtures). Expected gain +10–30 Elo with ~55% probability; ±10 Elo with 25%; regression with 20%.
2. **C4 (enable dense reward shaping) — SECONDARY.** Also config-only. Less principled targeting of known bottleneck. Run as v35 if v34 returns neutral.
3. **C7 (metric shift) — ADOPT for success criteria.** Combined Elo on `elo_fresh_panel.json` is primary; heuristic WR is secondary/diagnostic.
4. **C1 (data volume), C2 (trunk expansion), C5 (self-play), C6 (novel arch) — REJECT/DEFER.** All either lack verifiable premises or match the falsified weight-transfer/BC class.

## Concrete v34 spec

### Launch script

Write `scripts/launch_ppo_v34.sh` (copy from `scripts/run_elo_tournament.py`-style template, or just modify the v32 launch command):

```bash
#!/usr/bin/env bash
set -euo pipefail

uv run python scripts/train_ppo.py \
    --checkpoint results/ppo_v32_continue/v32_continue.iter0020.pt \
    --reset-optimizer \
    --out-dir results/ppo_v34_peerpool \
    --version v34_peerpool \
    --n-iterations 20 \
    --games-per-iter 200 \
    --ppo-epochs 1 \
    --clip-eps 0.05 \
    --lr 3e-6 \
    --lr-schedule constant \
    --gamma 0.99 \
    --gae-lambda 0.95 \
    --ent-coef 0.01 \
    --ent-coef-final 0.003 \
    --vf-coef 0.5 \
    --minibatch-size 2048 \
    --eval-panel data/checkpoints/scripted_for_elo/v56_scripted.pt __heuristic__ \
    --eval-every 10 \
    --side both \
    --self-play false \
    --seed 55555 \
    --device cuda \
    --wandb \
    --wandb-project twilight-struggle-ai \
    --wandb-run-name ppo_v34_peerpool \
    --max-kl 0.5 \
    --ema-decay 0.995 \
    --target-kl 0.015 \
    --league results/ppo_v34_peerpool \
    --league-save-every 10 \
    --league-mix-k 4 \
    --league-fixtures \
        data/checkpoints/scripted_for_elo/v29_continue_scripted.pt \
        data/checkpoints/scripted_for_elo/v31_continue_scripted.pt \
        data/checkpoints/scripted_for_elo/v33_continue_scripted.pt \
        __heuristic__ \
    --heuristic-floor 0.5 \
    --league-recency-tau 20.0 \
    --league-fixture-fadeout 999 \
    --league-self-slot \
    --pfsp-exponent 1.0 \
    --panel-heuristic-weight 3.0 \
    --jsd-probe-path data/probe_positions.parquet \
    --jsd-probe-interval 10 \
    --jsd-probe-bc-checkpoint data/checkpoints/ppo_v56_league/ppo_best_6mode_scripted.pt \
    --skip-smoke-test
```

**Only three fields differ from v32's `ppo_args.json`:**
- `checkpoint`: v32_iter20 (was v31_iter20 in v32's training)
- `out-dir` / `version` / `wandb-run-name`: new run id
- `league-fixtures`: **v29/v31/v33/__heuristic__** (was v56/v55/v44/__heuristic__)

All other hyperparameters (clip_eps=0.05, lr=3e-6, heuristic_floor=0.5, seed=55555, gae_lambda=0.95, n_iterations=20, games_per_iter=200) are identical to v32's ceiling recipe.

### Prerequisite verification (one-time, ~30 seconds)

```python
import torch
for name in ['v29_continue', 'v31_continue', 'v32_continue', 'v33_continue']:
    m = torch.jit.load(f'data/checkpoints/scripted_for_elo/{name}_scripted.pt', map_location='cpu')
    mh_shape = m.state_dict()['mode_head.weight'].shape
    assert tuple(mh_shape) == (6, 256), f'{name}: {mh_shape}'
print('All 6-mode, (6, 256) — OK')
```

**Already verified during this analysis.** All four are `(6, 256)`.

### Bench schedule

After each of iter10 and iter20 (automatic via `eval_every=10`), plus a final formal bench:
1. `iter10_scripted.pt` → bench vs heuristic, 500g/side, seed 50000 and 50500.
2. `iter20_scripted.pt` → bench vs heuristic, 500g/side, seed 50000 and 50500.
3. **Elo tournament**: add v34_iter20 to the fresh panel (`scripts/run_fresh_elo_tournament.py`), run 400 games/pair vs v29/v31/v32/v33/v56/heuristic. Report combined Elo delta.

## Kill criteria

Abort v34 if **any** of:
- iter10 panel combined < 0.58 (v32 at iter10 was ~0.63; 5pp drop = pool is harmful).
- iter20 panel combined < 0.62 (v32 at iter20 was 0.65; 3pp drop past the eval_panel heuristic-weighted metric = regression).
- Training diverges (KL > 0.5 sustained, or rollout_wr drops below 0.55 for 3 consecutive iters).
- Rollout crashes from fixture loading (mode-mismatch error — would require immediate debug).

Abort + preserve learnings: record which fixture(s) "won" in the PFSP wr_table dump at iter10 and iter20 for future analysis.

## Success criteria (primary metric = combined Elo, not heuristic WR)

- **Strong success:** v34_iter20 combined Elo ≥ 1395 (+25 over v32, outside 1-σ noise band).
- **Neutral:** v34_iter20 combined Elo in [1355, 1395] (within noise; fall back to C4).
- **Failure:** v34_iter20 combined Elo < 1355 (below v32 − 15 Elo = regression; do not merge; move to fallback).

Heuristic WR is secondary diagnostic only. A v34 that matches v32 on heuristic WR (0.65) but gains 20 Elo on the peer ladder is a **success** — that's what "breaking the plateau" looks like under C7's metric shift.

## Fallback ladder if v34 fails

1. **v35 = C4 (dense reward shaping enabled)**: Identical config to v32, but `--reward-shaping true --dense-reward-alpha 0.2 --dense-reward-anneal-steps 500000`. Rationale: unexplored lever; low cost; orthogonal to C3.
2. **v36 = C3 + C4 combined**: peer pool AND dense reward. Only run if both v34 and v35 individually show partial progress.
3. **If all three fail**: the chain is at its `country_attn_side` + heuristic-exploit ceiling. Defer to Task #64 data collection and accept that the next real progress requires architecture change on a stronger teacher (v32 itself, with infrastructure built on a *successful* teacher-distillation pipeline — not the falsified weight-transfer class).

## Explicit non-recommendations

- Do not run trunk-expansion (256→512). Falsified-class.
- Do not run US-specialist distillation from us_only_v5. Kill criterion (teacher stronger on target side) already tripped.
- Do not run ISMCTS variants. Value-head miscalibration mechanism unchanged.
- Do not run novel architectures (card embed, autoreg country, multi-token factorization) until C3/C4 have established whether config-only moves can extend the chain. If C3 succeeds, the resulting v34 becomes a stronger teacher for future BC warm-starts.
- Do not run temperature sweeps as a training intervention. Prior sweep (v32_temperature_sweep.json) shows τ=0.0 → 0.625, τ=0.1 → 0.645, marginal.

## Open questions (non-blocking)

1. **PFSP selection telemetry**: dump `pfsp_weights` per fixture per iter. If v29 consistently pulls >60% of PFSP mass, v34 is effectively single-opponent — may indicate we need finer granularity (add v27, v25 to pool).
2. **Is `league_self_slot` actually active and feeding gradient?** Worth a 10-min audit of `train_ppo.py` to confirm self-slot rollouts produce gradient, not just evaluation.
3. **Does `panel_heuristic_weight=3.0` still produce meaningful signal when the panel is just `[v56, heuristic]`?** Consider expanding eval_panel to also include v29 (0-cost observation of peer panel accuracy).
