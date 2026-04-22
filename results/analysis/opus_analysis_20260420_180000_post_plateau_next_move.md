# Opus Analysis: Post-Plateau Next Move — What to Run After v32
Date: 2026-04-20T18:00:00Z
Question: Given the fresh per-side Elo table (`results/elo/elo_fresh_panel.json`) and the project state, what is the highest-expected-value next autonomous move? Current chain has plateaued at v32_iter20 (0.650 combined, 1370 combined Elo). Previous GNN attempts (v14/v15) failed because BC warm-start gap (0.11 GNN BC vs 0.44 country_attn_side v56 warm-start) never recovered under PPO PFSP. We have: (1) v32 as a strong teacher for distillation, (2) per-side Elo showing v32 and v29 within 4 Elo (400 games) suggesting the chain is truly tied at the top, (3) Phase 2a/2b from the plan (GNN adjacency, regional scoring features). Key questions: (a) which Phase 2 intervention has the highest expected Elo gain given BC warm-start is the bottleneck; (b) can we break the bottleneck via weight transfer (load v32 trunk into a new arch and fine-tune only new layers) or direct teacher distillation; (c) is there a cheaper exploratory move before another 20–50 iter PPO run — e.g., ISMCTS at 200 sims with v32 value head; (d) diagnostic experiments (10× more collected games, temperature sweep, entropy).

## Executive Summary

The Elo table confirms the chain is genuinely saturated: v29→v31→v32→v33 span only 20 combined Elo (1345–1374), and v33 regresses from its own warmstart. The bottleneck is **not raw strength of the country_attn_side trunk** — it is that **PPO with heuristic-floor=0.50 + clip_eps=0.05 has exhausted the on-policy gradient signal available from heuristic-opponent data with a value head trained on terminal outcomes**. Dispatching another GNN BC→PPO attempt (Phase 2a) is strictly dominated — v14/v15 proved the warm-start gap is unrecoverable in 20 iters. The highest-EV next move is **weight-transfer + teacher distillation**: inject a regional-scoring head and a GNN country encoder **into the v32 trunk** (keep v32 trunk weights frozen for 1 epoch, then unfreeze at low LR), train on v32 soft targets over a newly collected 3000-game v32-vs-heuristic corpus, then run PPO v34 with the exact v32 ceiling recipe. This combines the Phase-2b regional scoring signal (cheap, +14 scalars) with a warm-start that cannot fall below v32 by construction. Expected gain: +10–30 Elo with ~70% probability. Reject: (a) cold-arch BC→PPO (falsified), (b) ISMCTS at 200 sims (value head still miscalibrated on determinized states, same mechanism as at 100 sims), (c) more seed sweeps (chain is at ceiling).

## Findings

### F1. The fresh Elo table says the top of the chain is saturated

From `results/elo/elo_fresh_panel.json` (anchor = heuristic-USSR=1200, bid+2):

| Cand | USSR Elo | US Elo | Combined |
|------|----------|--------|----------|
| v29_continue | 1419 | 1329 | **1374** |
| v32_continue | 1414 | 1326 | 1370 |
| v31_continue | 1405 | 1323 | 1364 |
| v33_continue | 1382 | 1329 | 1356 |
| v27_continue | 1395 | 1292 | 1344 |
| v25_continue | 1400 | 1275 | 1337 |
| v56          | 1331 | 1222 | 1277 |
| heuristic    | 1200 | 1062 | 1131 |

Three observations:

1. **v29 and v32 are statistically tied** (Δcombined = 4 Elo; at 400 games between every pair, SE ≈ 15–20 Elo). The "progressive warmstart chain peaked at v32" is a 500g-benchmark illusion produced by a lucky running-best selection; the Elo tournament (larger sample, round-robin, BayesElo prior) shows v29 on top.
2. **US side is the bottleneck**: v32's US Elo (1326) is only 97 Elo above v29's (1329)... in fact v29 is 3 Elo higher on US. The chain's progression from v22→v32 was almost entirely a USSR-side gain (v29 USSR 1419 vs v22 USSR 1307 = +112 Elo) while US-side stalled at 1275–1329 (only +54 Elo).
3. **v33 regressed on USSR (−37 vs v32) but held on US (+3)**. This is consistent with v33 iter10 panel already below its v32 warmstart — the ceiling recipe is symmetric-clipped to avoid USSR side-collapse but has no mechanism to push US further.

**Interpretation:** The chain has converged in US space. USSR is still improving slightly (v29→v32 +5 Elo on USSR side) but is within noise. Any future gains on `combined` must come from US-side improvement. That's the constraint that determines which intervention is highest-EV.

### F2. Phase 2a (GNN adjacency) has the worst expected value of all options

v14 (cold GNN BC→PPO, heuristic data) → combined 0.192 @ iter20.
v15 (cold GNN BC→PPO, v13 self-play data + teacher KL) → combined 0.112 @ iter10 best.

Both failed for the *same* structural reason: the GNN model started at ~0.11 BC panel and PPO with a 20-iter budget plus PFSP echo chamber cannot close a 33pp gap. The opus_analysis_20260420_gnn_v14_failure_v15_plan.md analysis was internally consistent but its core premise — "a better BC recipe can get GNN to panel 0.35–0.40" — was falsified by v15 in the same day. Teacher KL on v13-self-play at teacher_weight=0.5 produced BC panel 0.14 at best.

The lesson in `continuation_plan.json` is explicit: *"GNN architecture needs a different warm-start path (weight transfer from v13 or direct MCTS distillation). BC→PPO pipeline broken for new archs when warm-start <0.20."* This is correct. Cold-arch BC is dead. The v13 and v32 trunks encode months of PPO credit assignment that no BC objective can imitate from outcomes alone.

**Verdict:** Do not run another cold-arch BC→PPO. Phase 2a must be delivered via weight transfer from v32, not BC-from-scratch. (See Recommendations for the specific plan.)

### F3. Direct teacher distillation from v32 at action-distribution level is feasible and cheap

The infrastructure already exists:
- `scripts/train_baseline.py` supports `--teacher-targets` (parquet with teacher_card_logits / teacher_mode_logits / teacher_value) and `--teacher-weight`, `--teacher-value-weight` flags (lines 275–287 of the script).
- `data/teacher_targets/v13_3000g_soft_teacher.parquet` already exists (334K rows, 111-dim card softmax, 6-dim mode softmax, tanh value) from the v13 distillation attempt.
- The panel-best is now v32, not v13. Producing a v32 soft-teacher cache is 1 GPU-hour on ~3000 games of v32-vs-heuristic rollouts (forward-pass only; batched via tscore bindings).

**But the v15 attempt already tried exactly this (from v13) and failed.** Why? Two candidate reasons, one correct:

1. *Cold BC trunk cannot learn PPO-accumulated credit even from soft targets.* This is the correct reason. At `teacher_weight=0.5` and student trunk random, the KL term fights the argmax CE term and the trunk fits neither. Evidence: `bc_v3_root_cause` says "val_value_mse=0.81 worsening — overfitting" despite the teacher value column being present.
2. *The teacher was v13, not v32, and v13 itself only at 0.427.* Partially true but secondary — v32 soft logits are sharper and better calibrated, but that doesn't fix the cold-trunk problem.

**The fix is weight transfer, not more distillation.** A new arch's new layers (e.g. GNN encoder, regional-scoring head) must be added **on top of the v32 trunk**, not as replacements for it. Then teacher distillation on v32 soft targets operates as a **regularizer** keeping the trunk close to v32 while the new heads/encoders learn. This is the standard "add capacity, don't restart" trick used in progressive networks and LoRA-style fine-tuning.

### F4. ISMCTS at 200 sims will not fix the value-head miscalibration at 100

From `project_ismcts_verdict.md`: at 50 sims, ISMCTS USSR WR = 0.250 vs greedy 0.475. Δ = −0.225. Root cause: value head was trained on partial-information states; ISMCTS feeds determinized states; value head hallucinates.

At 200 sims, the value head is invoked **more**, not less. UCB's exploration term decays as 1/√N, so with more visits the search is more dominated by the Q-value estimate, which is the miscalibrated value head. The mechanism that makes ISMCTS lose at 50 sims makes it lose *more* at 200 sims. Extra compute does not cure systematic bias.

The three exceptions documented in memory (a) separate value head trained on determinized states, (b) heuristic rollouts instead of value head, (c) retrain model with determinization during self-play — are all several-week projects. None is a cheap exploratory move.

**Verdict:** ISMCTS at 200 sims is rejected. If we revisit ISMCTS, do it with heuristic rollouts (option b) — ~100 LOC change in the MCTS wrapper, ~5× slower per sim but unbiased. That's a separate optional experiment, not the highest-EV one.

### F5. 10× data volume will probably not help v32 train on its own games

The continuation_plan explicitly flags `pivot3_mcts_distillation` as FAILED: *"MCTS data fine-tuning destroys heuristic WR. MCTS positions (AI-vs-AI) have different state distribution than heuristic opponent games."* v32-on-v32 rollouts will drift into the same echo chamber. v32-vs-heuristic rollouts are what the current training loop already consumes. The marginal return on 30000 games vs 3000 games of v32-vs-heuristic is <2pp combined WR based on the rollout_wr trajectory in v32/v33 logs (rollout_wr saturates within ~5 iters of a new warmstart).

**Verdict:** Do not collect 10× data. Collect enough data to produce one high-quality teacher cache (~3000 games of v32-vs-heuristic and ~1000 games of v32-self-play). Diminishing returns beyond that.

### F6. Temperature/entropy sweeps are a cheap diagnostic but not a lever

A v32 temperature sweep (τ ∈ {0.3, 0.5, 0.7, 1.0, 1.5}) benched against heuristic would reveal whether v32's policy entropy is too peaked (→ τ>1 helps) or too flat (→ τ<1 helps). Cost: 5 benches × 200g/side ≈ 30 min GPU.

Prior: the current ceiling recipe uses greedy (τ=1.0 with argmax). If a temperature sweep shows τ=0.5 improves combined by 2+pp, that's a free +5–10 Elo with zero training. If not, we've spent 30 minutes and learned the policy is already at its decoding optimum.

**Expected finding:** τ=1.0 greedy will win on heuristic side (because heuristic is deterministic; any stochasticity in our policy against it adds variance). On v56 side, τ=0.5–0.7 may win. Net effect on Elo: probably ±5 Elo, not a breakthrough. **But it is a legitimate cheap diagnostic and should be run in parallel to the main intervention.**

### F7. US-side training is structurally the untapped frontier

v32 US Elo = 1326. us_only_v5 (capacity test) US combined WR = 0.360. The capacity_test specialists trained on a single side without the coupling constraint of a shared trunk reach *higher* US-side combined WR than v32 on the merged ladder. This is the strongest signal that **the US side has capacity to grow**; it is the trunk's shared bottleneck that holds it back.

Two options:
1. **Distill us_only_v5's US-side weights into v32 as an initialization**, then PPO-finetune. This is weight transfer in the opposite direction (specialist → generalist). Infrastructure exists (same architecture).
2. **Train a US-side adapter** on top of v32 trunk using us_only_v5 as the teacher. Less invasive; trunk preserved.

Either move targets the Elo-revealed bottleneck directly. Expected gain: +20–50 Elo on US side alone (i.e. US Elo 1326→1370+), which propagates to +10–25 combined Elo.

### F8. What's in-repo that unblocks the plan today

- `data/teacher_targets/mcts_dir_1000g_soft.parquet` — 52.8K rows of v13-soft on MCTS states (visit-count calibrated)
- `data/teacher_targets/v13_3000g_soft_teacher.parquet` — 334K rows v13-soft on v13-vs-heuristic states
- `data/teacher_targets/v72 ... v85` — newer teacher caches (provenance unknown to me; worth a 2-minute audit)
- `data/checkpoints/scripted_for_elo/v32_iter20_scripted.pt` — the teacher to use
- `scripts/train_baseline.py --teacher-targets` — supports teacher KL with value-KL
- `python/tsrl/policies/model.py:1911` — TSControlFeatGNNFiLMModel (GNN + FiLM, drop-in replacement for country_attn)
- `python/tsrl/policies/model.py:2018` — TSCountryAttnFiLMModel (FiLM conditioning variant of v32 arch)

**TSCountryAttnFiLMModel is the key file.** It has the *same* country_attn_side encoder as v32 but replaces the side-embedding concat with FiLM conditioning. This means its trunk parameters are shape-compatible with v32's up to the FiLM-gamma/beta projection. A weight-transfer script that copies v32's trunk into TSCountryAttnFiLMModel and initializes only the FiLM projectors is ~30 LOC.

## Conclusions

1. The Elo ladder confirms the chain is saturated at the top; v29/v31/v32 are within noise of each other and v33 regressed. "Beat 0.650" is not the right objective; "push US-side Elo past 1350" is.
2. Phase 2a (cold GNN BC→PPO) is falsified. Do not run it again. Phase 2a must be delivered via weight transfer from v32, not from scratch.
3. Direct teacher distillation from v32 is feasible and the infrastructure exists; the failure mode of v15 was cold-trunk, not bad-teacher. With a warm trunk from v32, teacher distillation becomes a regularizer, not a learner.
4. ISMCTS at 200 sims is rejected. More sims amplify the value-head bias, not cancel it. Only value-head retraining on determinized states or heuristic-rollout ISMCTS can unblock search.
5. 10× data volume will not help; diminishing returns beyond 3000 games of v32-vs-heuristic.
6. A temperature sweep of v32 is a cheap (~30 min) diagnostic that should run in parallel to the main intervention; expected impact ±5 Elo.
7. The biggest Elo-revealed bottleneck is US-side strength. us_only_v5 shows structural capacity exists. An intervention that specifically lifts US Elo (US-specialist distillation into v32) has the best expected value per GPU-hour.
8. The highest-EV single experiment is **v34 = weight-transfer of v32 trunk into FiLM-augmented country_attn + +14 regional-scoring scalars + 1-epoch frozen-trunk BC with v32 soft targets + PPO with v32 ceiling recipe + heuristic-floor=0.50**. This is the minimal move that actually changes the architecture without discarding v32's accumulated credit.
9. A parallel exploratory track — **v35 = US-specialist distillation**, transferring us_only_v5's US-side weights into v32's US head — targets the US-Elo bottleneck directly and is independent of v34.
10. Do not commit GPU-weeks to a single monolithic experiment. Launch v34 and v35 in sequence (or in parallel if GPU allows), gate each on a 100g/side panel benchmark, kill early if the panel regresses below v32's 0.650.

## Recommendations

### R1. PRIMARY: v34 — Weight-transfer + regional-scoring augmentation from v32

**Plan:**

1. Add **14 regional-scoring scalars** to `cpp/.../nn_features.cpp` (Phase 2b): per-region (Europe, Asia, MidEast, CSA, Africa, SEA, SA) `(our_presence, their_domination_pending)` or similar. ~150 LOC C++, ~30 LOC Python binding update.
2. Extend `TSCountryAttnSideModel`: add a **regional-scoring head** that takes the existing region-scalar block (`42` → now `56`) through a small MLP and fuses it into the trunk pre-heads. Architecture: `TSCountryAttnSideModelV2`. Keep scalar_dim and country_attn_encoder identical to v32. ~80 LOC Python.
3. **Weight transfer script** (`scripts/transfer_v32_to_v34.py`): load `v32_iter20_scripted.pt`, copy every parameter whose name and shape match the new model, randomly-initialize only the regional-scoring head and any projection layers touching the new scalars. Save to `results/bc_v34/v32_transferred.pt`. ~50 LOC.
4. **BC v34 stage 1** (frozen trunk, 3 epochs): `train_baseline.py --init-from v32_transferred.pt --freeze-trunk true --teacher-targets v32_soft_teacher.parquet --teacher-weight 0.5 --teacher-value-weight 0.3 --epochs 3 --lr 2e-4`. Only new layers get gradients. Aim to match v32 panel (combined ≥ 0.60 at 100g/side). **Gate:** combined ≥ 0.60; else abort and re-init.
5. **BC v34 stage 2** (unfreeze, 5 epochs): same data + teacher KL, but `--freeze-trunk false --lr 2e-5`. Gentle adaptation of trunk to the new regional-scoring signal. **Gate:** combined ≥ 0.64 at 100g/side.
6. **PPO v34**: exact v32 ceiling recipe (clip_eps=0.05, heuristic_floor=0.50, ppo_epochs=1, max_kl=9999, lr=3e-6, seed=55555, 20 iters, warmstart from BC v34 stage 2). Bench at iter10/iter20.

**(a) Estimated Elo gain:** +10–30 combined Elo with ~70% probability. Upside: regional scoring is a known-useful feature class in TS (humans use it constantly for "which region can I contest this turn"), and the current network has no direct signal for regional domination math — only implicit learning through country attention. Downside: can fail if the regional-scoring head is too easy to overfit (use dropout 0.2 on that head).

**(b) Cost:** ~330 LOC (150 C++ + 110 Python + 50 script + 20 config). Runtime: BC ≈ 3h, PPO ≈ 6h = 9 GPU-hours wall clock. C++ binding rebuild ≈ 15 min.

**(c) Prerequisites:**
- Generate `data/teacher_targets/v32_soft_teacher.parquet` from 3000 games of v32-vs-heuristic rollouts. ~1 GPU-hour.
- Verify TSCountryAttnSideModelV2 produces identical output to TSCountryAttnSideModel when regional-scoring head is zero-initialized (unit test).
- Verify weight-transfer script copies correct parameter subset (diff v32 state_dict keys against V2 state_dict).

**(d) Kill criteria:**
- BC stage 1 combined < 0.55 at 100g/side (warm trunk copied wrong or new head destabilizes).
- BC stage 2 combined drops below v32's 0.650 (trunk adaptation hurts).
- PPO v34 iter10 combined < 0.60 (warmstart gap not absorbed).
- PPO v34 iter20 combined < 0.64 (no improvement — Phase 2b regional scoring doesn't help).

### R2. PARALLEL: v35 — US-specialist distillation into v32

**Plan:**

1. Generate `data/teacher_targets/us_only_v5_us_side_soft.parquet` from 2000 games of us_only_v5 playing US (only) vs heuristic. ~45 min GPU.
2. BC v35: `train_baseline.py --init-from v32_iter20 --teacher-targets us_only_v5_us_side_soft.parquet --teacher-weight 1.0 --teacher-value-weight 0.5 --epochs 5 --lr 1e-5 --filter side==us`. Fine-tune v32 only on US-side frames with us_only_v5 as the teacher. USSR-side frames untouched (filtered out).
3. Bench v35 at 200g/side vs heuristic + v56. **Gate:** US combined ≥ 0.56 AND USSR combined ≥ 0.78 (i.e. US improves from 0.51 without USSR regressing below v32's 0.79 − 1pp).
4. If gate passes, PPO v35 with v32 ceiling recipe. If gate fails, iterate teacher_weight (0.5 → 1.5).

**(a) Estimated Elo gain:** +10–40 combined Elo (median +20) if it works. US side has the most headroom per Elo table. Note that us_only_v5's *own* US combined is 0.36; v32's is 0.51. It is possible us_only_v5 is NOT actually a good US teacher (specialists often have worse merged performance). **Verify this before running** by benching us_only_v5 at 500g/side vs heuristic specifically on the US side; if us_only_v5's US WR is below v32's, abort.

**(b) Cost:** ~60 LOC (filter flag in train_baseline.py, teacher cache script, bench script). Runtime: ~3 GPU-hours.

**(c) Prerequisites:**
- Verify us_only_v5 has a scripted export in `data/checkpoints/scripted_for_elo/`. The provenance analysis says it does NOT yet; export it first.
- Confirm us_only_v5's US-side WR > v32's US-side WR at 500g/side. If not, this experiment is dead on arrival.

**(d) Kill criteria:**
- us_only_v5 US combined < v32 US combined at 500g/side (teacher is not stronger than student on target side).
- BC v35 post-fine-tune: USSR combined drops below 0.72 (catastrophic forgetting of USSR side).
- BC v35: US combined unchanged (<0.52) — distillation didn't transfer anything.

### R3. CHEAP DIAGNOSTIC (run in parallel, ~30 min): v32 temperature sweep

`scripts/run_elo_tournament.py` or equivalent: bench v32 against heuristic at τ ∈ {0.3, 0.5, 0.7, 1.0, 1.5}, seeds 50000/50500, 200g/side.

**(a) Estimated Elo gain:** ±5 Elo. If τ=0.5 wins on v56 opponent by 5+pp and loses on heuristic by <3pp, switch the chain's evaluation temperature.

**(b) Cost:** ~20 LOC (add `--rollout-temp` flag to bench script if missing). Runtime: 30 min.

**(c) Prerequisites:** None.

**(d) Kill criteria:** All temperatures within 2pp of each other (policy is at decoding optimum; no free Elo here).

### R4. REJECT / DO NOT RUN

- Cold GNN BC→PPO (v16/v17 flavor). Falsified twice.
- ISMCTS at 200 sims with unchanged value head. Mechanism unchanged from 50-sim attempt; more sims worsens bias.
- Pure MCTS-data fine-tuning of v32. Falsified (pivot3_mcts_distillation).
- Another PPO seed sweep on v32 recipe. Elo table shows chain saturated; variance is already within 15 Elo.
- 10× data volume of v32-vs-heuristic rollouts. Diminishing returns beyond 3000 games.

### R5. Ordering and GPU allocation

Given 1 GPU and autonomous operation:
1. **Day 0, 30 min:** R3 temperature sweep (in parallel with R1 data collection).
2. **Day 0, 1 h:** Collect `v32_soft_teacher.parquet` (3000 games v32-vs-heuristic).
3. **Day 0, 1 h:** Build TSCountryAttnSideModelV2 + weight transfer script + unit test.
4. **Day 1, 9 h:** Run BC v34 stage 1 + stage 2 + PPO v34. Gate at each stage.
5. **Day 1, 3 h (if v34 running and R2 prereqs clear):** Run R2 (v35 US-specialist distillation). Completely independent of v34 training; can share GPU if VRAM permits (both are <3GB models).
6. **Day 2, 1 h:** Elo-bench v34 and v35 against current 14-candidate panel. Update `elo_fresh_panel.json`.

**Abort criterion on the whole plan:** If v34 + v35 both fail their kill criteria, do NOT escalate to Phase 3 architecture search. Instead escalate to the advisor for a structural rethink — probably towards MCTS with retrained value head (a several-week project not suitable for autonomous mode).

## Open Questions

1. **Is the `v32_iter20_scripted.pt` hash-identical to `v32_continue_scripted.pt`?** The provenance analysis flagged this; if different, R1's weight transfer needs the correct source. Verify once with a SHA256 diff.
2. **Does us_only_v5 actually outperform v32 on US side at 500g/side?** R2 is blocked on this answer. Bench first.
3. **Do the `data/teacher_targets/v72 ... v85` caches correspond to any known model?** If one is a v32-soft cache, we can skip R1's data-collection step. 2-minute audit worth doing.
4. **Is TSCountryAttnSideModelV2 the right name collision?** Repository already has `TSCountryAttnFiLMModel` and `TSCountryAttnFiLMNormalInitModel` for FiLM variants. If we want to ALSO do FiLM + regional scoring, that's a v34b variant. Recommend shipping v34 with concat side-embed (v32 arch) first, FiLM second only if v34 passes gates.
5. **Is the 6-mode head preserved across weight transfer?** Chain is 6-mode; V2 must also be 6-mode. Trivial to verify but worth a unit test.
6. **What's the right PPO seed for v34?** v32 used 55555; v29 used 12345 and currently leads on USSR Elo. Might be worth seed=12345 for v34 to recover v29's USSR-side advantage.
7. **Should R3 also run a temperature sweep at PPO training rollout level**, not just evaluation? That would be a different (larger) experiment; defer to v34 post-mortem.
