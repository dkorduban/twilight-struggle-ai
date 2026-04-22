# Opus Analysis: Post-v36 Failure — Next Highest-EV Move Selection

Date: 2026-04-21T05:48:00Z
Question: Given the v36_dense_reward failure (mean combined=0.627 vs v32=0.650; panel 0.708 was 30g/side noise), and the v34/v35/v36 plateau at 0.62-0.65, what is the single highest-EV next autonomous move among (A) v32 teacher distillation, (B) US-specialist v37_us_only PPO, (C) ISMCTS@200 sims + Dirichlet, (D) 10k-game v32 self-play data + entropy/coverage diagnosis, (E) 32-dim NP-specific scalars?

## Executive Summary

**Primary recommendation: Option A — teacher distillation from frozen v32 — but structured as a two-stage program. Stage 1 (validation, ~4 GPU-hours) trains a same-architecture student (country_attn_side) from the v56 warmstart using teacher-KL on v32's full softmax distribution (not argmax-BC) and must hit ≥0.55 combined by epoch 5 or the pipeline is falsified. Stage 2 (only if Stage 1 passes) repurposes the same pipeline for a new architecture.** This is the only candidate with a genuinely untried mechanism and a cheap falsification gate. Options B, C, E are falsified-class: B is contradicted by the fresh Elo table (`us_only_v5.US=1194` is 132 Elo *below* v32.US=1326), C's blocker (value-head miscalibration on determinized states) is mechanism-unchanged by sim count or a newer value head, and E matches the v14/v15 weight-transfer/cold-BC failure mode. Option D (self-play + diagnostics) is a valid open-questions investigation but not a step-change move. Secondary fallback: a v35-config seed replicate at different seeds to resolve whether `lr=1e-6` is a real lever before declaring the plateau structural.

## Findings

### 1. v36 ended in KL-crash, not a 20-iter plateau

v36 stopped at iter12 with KL=8.36 (threshold 0.5). It was dense-reward + peer-pool + lr=3e-6 on top of v32. The 30-game panel flagged iter10 as a "new high-water mark" at 0.708 — formal 500g bench says 0.627. This is textbook panel false-positive at n=30 (SE≈0.09). Two signals come out of v36:

- **Dense reward at alpha=0.2 + lr=3e-6 is unstable** (KL explosion). The dense-reward lever is not independently dead, but it requires a lower LR to ride.
- **The 30g panel continues to mispromote.** The `_PANEL_WEIGHTS={"__heuristic__": 3.0}` fix from v16 only reweighted the average, not the sample size. This is a standing diagnostic hazard; addressed in Open Questions.

### 2. v35's +1.6pp uplift is within 500g bench σ and needs replication

v35 (peer-pool, lr=1e-6, no dense reward) reached 0.666 at iter20 vs v32=0.650 — uplift +1.6pp, passed the kill gate (0.66). SE on combined WR at n=500/side is ≈0.022 (two binomial proportions averaged), so the +1.6pp is about 0.7σ — not reliably different from v32. Before declaring "the chain is exhausted," two seed replicates of v35 would resolve whether `lr=1e-6` extended the chain or whether v35 is a lucky draw. This is cheap (~8 GPU-hours) and surfaces as a non-primary recommendation.

### 3. v32-only → new-arch distillation sidesteps the v14/v15 failure mode

The v14/v15 failure was: cold-BC on a new architecture (GNN) from heuristic data produced a ~0.19 combined warm-start; PPO could not close the ~25pp gap to v56's 0.44 in 20 iters because PFSP folds policy into its pool. Key mechanism: **argmax BC captures only the argmax slice of the teacher's policy** (Finding in `opus_analysis_20260420_overnight_summary.md`). BC v4 tried teacher-distillation from v13 logits and still failed (v15=0.112) but v13 was itself a 0.427 teacher; distilling from a noisy teacher can't produce a clean student.

Teacher distillation from **v32** is different:
- Teacher quality: v32 is the ceiling teacher (1370 combined Elo). Its full softmax distribution carries ~4-5× more information than the argmax slice (a rough entropy bound from the observed `entropy=3.33` in v36 rollouts — ~28 effective card actions).
- Loss: KL(student || teacher_softmax) + optional λ·MSE(student_value, teacher_value), evaluated on a *fresh* v32 self-play + v32-vs-heuristic mixture corpus.
- Mechanism: learns the full policy geometry, including the "which cards to consider" mass, not only "which card to pick." This is the only structural move left that does not match a falsified class.

**Verifiable premise for Stage 1:** if we distill from v32 *into the same architecture (country_attn_side)* from v56's warmstart, the resulting student should reach v32's performance ± noise — a pipeline self-test. If it reaches ≥0.55 combined by epoch 5 (vs BC-from-heuristic's ~0.44 ceiling), the distillation signal is confirmed superior to argmax BC. Only then is the pipeline ready to feed a new architecture.

### 4. Option B (US-specialist v37_us_only) is contradicted by the Elo data

The fresh Elo panel (`results/elo/elo_fresh_panel.json`) shows:
- `v32_continue.US = 1326.4`
- `us_only_v5.US = 1194.9`  (132 Elo *worse* on US side)
- `ussr_only_v5.US = 1180.0`

The US-specialist checkpoint (`us_only_v5.iter0050`, which has already trained 50 iterations on US-filtered data per `results/capacity_test/ppo_us_only_v5/`) is **132 Elo below v32 on the very side it specialized on**. Training a new US-specialist from v32 is strictly unlikely to improve on `us_only_v5`'s recipe, and starting from v32 removes the diversity that gives US-only training its value (v32 has already over-fit to its pool).

Additionally, the infrastructure described in the task brief is already present:
- US data filtered to wins only (`feedback_game_asymmetry.md` — standard)
- 2x value loss weighting on US-win steps — **actually removed** (see §5 below); the active code in `ppo_update_packed` at line 2255 is unweighted `((values - returns) ** 2).mean()`. The `us_win_w` at line 1978 is in the *dead* `ppo_update` path (not called from the main training loop at line 3564). So this lever is available but has not been the dominant factor in v32 training.
- `--side us` flag is supported.

Even granting the "longer horizon" clause, the empirical ceiling of a US-specialist is already demonstrated by `us_only_v5`: it's below v32. **Reject Option B.**

### 5. Option C (ISMCTS@200) has unchanged blocker

Per `project_ismcts_verdict.md`, ISMCTS@100 sims produced delta=-0.225 vs greedy. Shelved because the value head is miscalibrated on *determinized* states — determinization creates off-policy joint distributions of hidden-card assignments that the value head never sees during training. 200 sims is 2× compute but:

- The mechanism blocker is value-head miscalibration on determinized states, not search depth.
- v32's value head is better on *observed* states (0.788 USSR WR, 0.512 US WR confirms value+policy agree on real distributions). There is **no evidence** this generalizes to determinized states. The value head was never trained on such inputs.
- Fixing this requires augmenting the training distribution with determinized positions — which is infrastructure work with no existing scaffolding.

**Reject Option C** until value-head retraining on determinized positions is completed (out of scope for the immediate next move).

### 6. Option E (32-dim NP scalars) is v14/v15 failure class

Adding 32-dim NP-specific scalars (NORAD, Quagmire, Bear Trap, SALT, Flower Power) changes the trunk input dim. Two paths:
- **Cold-BC on new-dim arch**: falsified by v14/v15.
- **Weight-transfer into random-init expansion dims**: matches the falsified class in `opus_analysis_20260420_post_plateau_v2.md` Finding C2 (trunk expansion). The non-zero subspace is effectively BC-from-scratch on the new dims; PPO warmstart benefit is nil on the random-init subspace.

There is also a premise question: *is* late-game US play actually starved of NP context? v32 already has `kModelScalarDim=40` scalars plus 42-dim region block. Quagmire/Bear Trap/SALT status are per-player binary flags that would cost ~5 dims, not 32. Before proposing this, we'd need a concrete ablation: does removing/randomizing the NP-state bits already in v32 degrade US-side decisions on late-game positions? No such ablation exists.

**Reject Option E** — falsified class, premise unverified.

### 7. Option D (10k-game diagnosis) is orthogonal, not primary

Collecting 10k v32 self-play games and diagnosing entropy/coverage is *useful diagnostic work* — it would answer whether the US-side plateau is data-starvation at hard states or a policy-geometry issue. But it doesn't move the ceiling; it only informs the next move. If Option A fails, Option D becomes essential. For now, promote to Open Questions.

### 8. Cost estimates (GPU-hours, H100-equivalent / RTX 3050 scaled)

| Option | GPU-h (A100 eq.) | Wall clock on local RTX 3050 | Risk of zero return |
|---|---|---|---|
| A Stage 1 (same-arch distill) | ~4h | ~8-12h | Low — pipeline test, clear pass/fail |
| A Stage 2 (new-arch distill) | ~8h (BC) + 20 PPO | ~24-30h | Medium — hinges on Stage 1 |
| B (US-specialist v37) | ~4h | ~6h | High — Elo data contradicts premise |
| C (ISMCTS@200 bench, not training) | ~2h bench | ~4h | Very high — unchanged blocker |
| D (10k self-play + diag) | ~6h collect + 2h analyze | ~12h | Zero structural return, high info |
| E (new scalars + BC + PPO) | ~10h total | ~24h+ | Very high — falsified class |
| v35 replicate (2 seeds) | ~4h | ~8h | Low — resolves v35 noise |

### 9. The "dense reward" lever is not dead; it needs a lower LR

v36 crashed at KL=8.36 with lr=3e-6 + dense_alpha=0.2. The interaction (dense reward distributes more per-step reward, amplifying gradient signal) destabilized at that LR. v35 ran without dense reward at lr=1e-6 and was stable. If dense reward matters, it needs lr ≤ 1e-6 and probably lower. This is a config-only retry but belongs in the fallback ladder after A, not as the primary move — the dense-reward mechanism is not orthogonal to the US-side structural issue.

## Conclusions

1. **Option A (v32 teacher distillation) is the only candidate with an untried mechanism and a cheap falsification gate.** All other options are either falsified-class (B by Elo data, C by mechanism, E by v14/v15) or diagnostic-not-structural (D).

2. **Stage 1 of Option A must validate the pipeline, not test a new architecture.** Distill from frozen v32 into country_attn_side (same arch), from v56 warmstart. If this does not beat v56's 0.44 BC-from-heuristic baseline within 5 epochs, the distillation pipeline is broken and Stage 2 is prohibited.

3. **v35 deserves seed replication before we declare the chain structurally exhausted.** Two seed replicates at ~8 GPU-hours resolve whether lr=1e-6 is a real lever or a 0.7σ draw. Not primary because A has higher upside, but a fast parallel run.

4. **Option B is explicitly contradicted by Elo data.** `us_only_v5.US = 1194` vs `v32.US = 1326` — the standalone US-specialist is already 132 Elo worse than v32's US side. US-specialist PPO is not going to beat v32.US.

5. **v36 killed itself at KL=8.36.** Dense reward at lr=3e-6 is unstable; dense reward at lr=1e-6 is untried. If Option A fails, dense-reward + lr=1e-6 is the next config-only retry, not architecture change.

6. **The 30g panel promotion bug remains a standing hazard.** v36 panel said 0.708, 500g says 0.627 — 8pp gap due to sampling noise. Every Opus analysis since v16 has surfaced this; it still costs us experiment time via false high-water marks.

## Recommendations

### Primary: Launch v37_distill_stage1 (Option A, Stage 1 validation)

**Goal:** Validate teacher-KL distillation pipeline. Does distilling v32's full softmax into a fresh country_attn_side student produce a stronger BC warmstart than heuristic-argmax BC?

**Launch spec (new script `scripts/train_distill.py` OR extend `scripts/train_bc.py` with `--teacher-kl` flag):**

```bash
# Stage 1: collect teacher rollouts (~2 GPU-hours)
uv run python scripts/collect_teacher_rollouts.py \
    --teacher data/checkpoints/scripted_for_elo/v32_continue_scripted.pt \
    --opponents __heuristic__ v29_continue v31_continue v33_continue \
    --games 2000 \
    --include-softmax \
    --include-values \
    --out data/distill/v32_teacher_2000g.parquet \
    --seed 77777

# Stage 1: BC with teacher KL (~3 GPU-hours, 30 epochs)
uv run python scripts/train_bc.py \
    --dataset data/distill/v32_teacher_2000g.parquet \
    --arch country_attn_side \
    --warmstart data/checkpoints/ppo_v56_league/ppo_best_6mode.pt \
    --teacher-kl-weight 1.0 \
    --argmax-ce-weight 0.0 \
    --teacher-value-weight 0.5 \
    --epochs 30 \
    --batch-size 4096 \
    --lr 1e-4 \
    --out-dir results/distill_v37_stage1 \
    --bench-every 5 \
    --bench-seeds 50000 50500 \
    --kill-gate-combined 0.55 \
    --kill-gate-epoch 5
```

**Kill criterion (hard):** If epoch-5 bench combined < 0.55, abort. The distillation pipeline is falsified (signal is no better than argmax-BC from heuristic data). Do not proceed to Stage 2.

**Success criterion:** Epoch-30 bench combined ≥ 0.60. This demonstrates teacher-KL extracts more signal than argmax BC (which caps near 0.44 on this arch from v56 data). A passing Stage 1 means Stage 2 (new architecture) becomes the lead item in the follow-up plan.

**Concrete Stage 2 sketch (only if Stage 1 passes):** `arch=control_feat_gnn_film` or `card_attn` student, same teacher-KL loss, same v32 teacher corpus. The v14/v15 failure was that cold-arch BC on argmax heuristic data caps at 0.19; if teacher-KL gets country_attn to 0.60 from v56, the same loss on a different arch has a much better prior than v14/v15 started with.

### Secondary (parallel, independent): v35 seed replicate

Two replicates of v35's config at seeds 66666 and 88888 (original was 55555). ~4 GPU-hours each, wall clock ~16h total if serialized. Decides whether lr=1e-6 + peer-pool is a real lever (would mean the chain continues) or noise (confirms plateau).

**Launch:** Copy `results/ppo_v35_peerpool_smallstep/ppo_args.json`, change `seed` and `out_dir`/`version`, launch.

### Fallback ladder (only if A Stage 1 and v35 replicate both fail)

1. **Dense reward + lr=1e-6 retry** (cheap, config-only). Not "dense reward is dead" — "dense reward at lr=3e-6 is dead." KL=8.36 at iter12 proves unfitness of the LR × alpha combination, not the lever.
2. **Option D: 10k v32 self-play + entropy/coverage diagnostic.** Establishes whether US-side plateau is data starvation or policy geometry. No structural return, but routes the next experiment.
3. **Shift to Month-3 priority #3: Elo as primary eval.** `elo_fresh_panel.json` is already authoritative. Add v34/v35/v36 to the ladder and accept that "combined WR vs heuristic" has hit its exploitation ceiling at ~0.65-0.67 given the 0.72/0.28 USSR-bias of the base heuristic.

### Explicit non-recommendations

- Do not launch Option B (US-specialist). Elo data says it can only regress.
- Do not launch Option C (ISMCTS@200). Value-head on determinized states is unaddressed.
- Do not launch Option E (NP scalars). Falsified weight-transfer/cold-BC class.
- Do not trust 30g panels for running-best selection. Every recent run has been misled at least once.
- Do not stack A Stage 2 onto the same run as Stage 1. Validate the pipeline first.

## Open Questions

1. **Does a 2000-game v32 teacher corpus contain enough hard US-side positions?** v32's US WR is 0.51, so ~1000 of the US-side games are losses. If the goal is to boost US-side student learning, we may need US-only teacher rollouts (v32 as US vs heuristic-USSR) at 2-3× volume. This is a stage-1 ablation.

2. **Is the 30g panel actively harmful?** Proposal: disable panel-based high-water-mark promotion entirely. Replace with a 200g iter10+iter20 bench only, accept longer wall clock. `feedback_ppo_benchmarking.md` says 500g is the standard; 30g has a 15pp CI. The panel mechanism should only be used as a *relative* signal for PFSP, never for checkpoint promotion.

3. **What's the combined Elo of v34/v35/v36 on the fresh ladder?** None of them are in `elo_fresh_panel.json` yet (timestamp 2026-04-21T00:35:37Z predates v36 completion). A single Elo run adds them for ~100 games × 6 opponents ≈ ~2 GPU-hours. Without this, we're comparing v34/v35/v36 only via heuristic WR, which is known noisy.

4. **Does v32's value head generalize to determinized states?** A 500-position ablation (construct determinized states from v32 self-play, score value head, compare to observed true values) would reopen Option C as an investigation path. Not a move, a measurement.

5. **Is `us_only_v5.US = 1194` reliable?** That checkpoint was trained from earlier capacity-test infrastructure. If its Elo is noisy (few matches in the ladder), the falsification of Option B weakens. Spot-check `n_matches_used=105` in the panel — this is a shared pool, so per-opponent counts are smaller. Worth a direct 400g head-to-head of `us_only_v5` vs `v32` on US side before fully shelving B.

6. **Does the dense-reward crash mean `gae_lambda=0.95` is wrong for dense reward?** With dense per-step reward, the advantage variance under λ=0.95 is higher than under sparse reward. Dense reward may require λ=0.85 or lower. Noted for config-only retry in the fallback ladder.
