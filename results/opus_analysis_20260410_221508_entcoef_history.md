# Opus Analysis: Entropy Coefficient History
Date: 2026-04-10T22:15:08Z
Question: Story of ent_coef hyperparameter changes after v22, and its interaction with policy entropy.

## Executive Summary

The entropy coefficient (`ent_coef`) has gone through three distinct phases across v1-v44:

1. **v3-v6**: `ent_coef=0.01` (constant or with `final=0.001`). This was the initial setting, inherited from standard PPO defaults.
2. **v7**: `ent_coef=0.03` (no decay). First bump, introduced when switching to attention architecture. Immediately noted as causing "entropy inflated to 3.4-3.5 (vs v6's 2.8)".
3. **v8-v11**: `ent_coef=0.05 -> 0.01`. Aggressive entropy bonus during the early scoring-tier-features era.
4. **v12-v44**: `ent_coef=0.03 -> 0.005`. Settled here and never changed again. This is the current pipeline default in `ppo_loop_step.sh`.

The entropy coefficient was **never the primary cause** of the v23-v44 regression. The root cause was a C++ log_prob mismatch (hard-argmax vs soft-mixture in country head), identified and fixed in commit `11c084c5`. However, `ent_coef=0.03` applied to a policy that already has entropy ~4.0-4.5 is arguably too high -- it provides a strong gradient signal to keep entropy elevated, which can resist the policy sharpening needed for strength gains. The global entropy decay schedule (decay from 0.03 to 0.005 over global iterations 400-2000) was introduced in commit `7f3bed9c` (Apr 9) but has a critical flaw: `global_iter_offset` is never persisted across chained runs, so each new v(N) run starts with `global_iter=1`, meaning the decay schedule restarts from `ent_coef=0.03` every run (since 1 < 400). The intended long-horizon decay never actually takes effect.

## Findings

### ent_coef Values Across Versions

| Version Range | ent_coef | ent_coef_final | Decay Schedule | rollout_temp | Notes |
|---------------|----------|----------------|----------------|-------------|-------|
| v3-v5 | 0.01 | 0.001 | Per-run linear | N/A (1.0 implicit) | Initial PPO runs |
| v6 | 0.01 | None (constant) | None | N/A | Constant entropy |
| v7 | 0.03 | None (constant) | None | N/A | Attn arch cold-start; entropy noted as inflated |
| v8-v11 | 0.05 | 0.01 | Per-run linear | N/A | Most aggressive entropy bonus |
| v12-v22 | 0.03 | 0.005 | Per-run linear | N/A (1.0 implicit) | Settled value; v22 = peak Elo (2109) |
| v23-v43 | 0.03 | 0.005 | Global (broken) | 1.2 | Global schedule introduced but offset bug |
| v44 | 0.03 | 0.005 | Global (broken) | 1.0 | Reverted to T=1.0, no Dirichlet |

### How ent_coef Is Applied in the Loss

The entropy bonus is computed as:
```
entropy = ent_card + ent_mode + ent_country
entropy_loss = -entropy.mean()
loss = policy_loss + vf_coef * value_loss + ent_coef * entropy_loss
```

Where each component entropy is the standard `-(p * log p).sum()` over the masked action distribution. Since `entropy_loss` is negated, `ent_coef > 0` **encourages** higher entropy (i.e., more uniform distributions).

Key detail: **country entropy is always included**, even for decisions with no country targets. The code notes: "using all countries inflates entropy but allows gradient flow." This means the reported entropy number (~4.0-4.5) includes a large country-head component that is partially uninformative.

### Entropy Decay Schedule

Two decay mechanisms exist:

1. **Per-run linear decay** (original, pre-v23): `current = ent_coef + (iter/n_iters) * (final - initial)`. Simple linear interpolation within a single run of 200 iterations. Each new run resets to `ent_coef=0.03`.

2. **Global decay** (introduced Apr 9, commit `7f3bed9c`): Uses `global_iter = global_iter_offset + iteration` and decays between `global_ent_decay_start=400` and `global_ent_decay_end=2000`. BUT: `global_iter_offset` is not stored in `ppo_args.json` for any version (all show `?`), meaning it defaults to 0. Since each run is 200 iterations, `global_iter` never exceeds 200, which is always below `global_ent_decay_start=400`. **The decay never triggers.** Every iteration of every post-v23 run uses the full `ent_coef=0.03`.

### Interaction with Low-Entropy Starting Policy

v22 finished with entropy around 4.08 (from the commit message context and log evidence at v22 iter 146). When a new run starts from v22's checkpoint:

- With `ent_coef=0.03`, the entropy bonus gradient pushes the policy to maintain or increase its current entropy level.
- At entropy=4.08, the per-step entropy bonus in the loss is approximately `0.03 * 4.08 = 0.12`, which is comparable in magnitude to typical policy losses (which range from -0.03 to 0.04).
- This is not necessarily harmful -- entropy 4.08 in a game with ~110 country slots + ~40 card choices is actually quite low. The concern would be if the entropy bonus is preventing the policy from sharpening on critical decisions.

However, the real problem post-v22 was not entropy coefficient but the **C++ log_prob mismatch**: the rollout stored log_probs computed with hard-argmax strategy selection, while the Python PPO update computed log_probs with soft-mixture. This created biased importance sampling ratios that caused clip/KL spikes and entropy drops, especially at T>1.0. The entropy coefficient was a red herring in the v23-v37 investigation.

### Interaction with Rollout Temperature

At `rollout_temp=1.0` (v3-v22, v44): actions are sampled from the raw policy logits. The stored `old_log_prob` matches the training-time recomputed `new_log_prob` (before any policy updates).

At `rollout_temp=1.2` (v23-v43): actions are sampled from `softmax(logits / 1.2)`, which is a flatter distribution. The stored `old_log_prob` should reflect this temperature-scaled distribution. However, the C++ bug meant the stored log_prob did NOT correctly account for temperature in the country head, creating a mismatch that broke importance sampling.

The combination of `T=1.2` + `ent_coef=0.03` is doubly exploratory: temperature flattens the sampling distribution, and entropy bonus penalizes the policy for sharpening. In principle this is fine for exploration, but when the IS ratios are wrong (due to the C++ bug), the doubly-exploratory setup amplifies the damage.

### Timeline of Changes

| Date | Commit/Event | Change |
|------|-------------|--------|
| Apr 7 | `8d79f559` | `--ent-coef-final` introduced (per-run linear decay) |
| Apr 7 | `f81926e4` | Initial entropy computation in PPO (card + mode + country) |
| Apr 8 | v7 launch | `ent_coef` bumped from 0.01 to 0.03 for Attn arch |
| Apr 8 | v8 launch | `ent_coef` bumped to 0.05 (most aggressive) |
| Apr 8 | v12 launch | `ent_coef` settled to 0.03/0.005 (final value) |
| Apr 9 | `7f3bed9c` | Global entropy schedule introduced (decay_start=400, decay_end=2000) |
| Apr 9 | v23 launch | First run with T=1.2 + Dirichlet + global ent schedule. Collapsed to 1733 Elo. |
| Apr 10 | `11c084c5` | C++ log_prob mismatch fix identified as root cause of v23+ regression |
| Apr 10 | v27-v43 | All restarted from v22, all use ent_coef=0.03/0.005, none surpass v22 |
| Apr 10 | v44 | Reverted to T=1.0, no Dirichlet, still ent_coef=0.03/0.005 |

## Conclusions

1. **ent_coef=0.03 has been constant since v12 and was never the root cause of the v23+ regression.** The root cause was the C++ log_prob mismatch in country head (hard-argmax vs soft-mixture).

2. **The global entropy decay schedule is broken.** It was designed to decay ent_coef from 0.03 to 0.005 across global iterations 400-2000, but `global_iter_offset` is never persisted or passed between chained runs. Every 200-iteration run stays at the full `ent_coef=0.03` for all iterations (since max local iter 200 < decay_start 400).

3. **The effective entropy coefficient for every post-v12 run has been a constant 0.03.** The decay to 0.005 never activates.

4. **ent_coef=0.03 at entropy~4.0 is moderate, not extreme.** The entropy bonus contributes ~0.12 to the loss, comparable to policy loss magnitude. It prevents premature sharpening but is not obviously harmful. The real question is whether the policy *should* be sharpening more aggressively.

5. **v22 reached peak Elo (2109) with ent_coef=0.03 and T=1.0.** This combination worked. The post-v22 regression correlates with the introduction of T=1.2 and Dirichlet noise (both starting v23), compounded by the C++ log_prob bug.

## Recommendations

1. **Fix the global entropy decay by passing `--global-iter-offset` explicitly in `ppo_loop_step.sh`.** Compute it as `(version - start_version) * 200` or read it from the previous run's final state. Without this fix, `ent_coef_final=0.005` is dead code.

2. **For v44 (restarting from v22 with T=1.0):** The current ent_coef=0.03 constant is the same setting v22 was trained with. This is the correct baseline for a controlled experiment. Do not change it yet.

3. **If v44 recovers v22-level Elo:** Then consider reducing ent_coef to 0.01-0.02 for v45+ to allow more policy sharpening. The v12-v22 climb happened at ent_coef=0.03, but the policy may now be mature enough that less entropy bonus would help.

4. **If v44 does NOT recover:** The problem is not ent_coef but something else in the post-v22 pipeline (optimizer state, league composition, or residual C++ bugs).

5. **Consider decoupling entropy reporting:** Track card entropy, mode entropy, and country entropy separately in W&B. The aggregate "entropy=4.08" mixes uninformative country entropy with decision-relevant card/mode entropy.

## Open Questions

1. What is v22's actual card-head entropy vs country-head entropy? If card entropy is already very low (~1.0), then ent_coef=0.03 is mostly maintaining country diversity, not card diversity.

2. Does the optimizer state from v22 (which was trained at constant ent_coef=0.03) have momentum/adaptive state that assumes this coefficient? `--reset-optimizer` (used in v43/v44) clears this, which might cause a transient.

3. Should ent_coef be reduced for the country head specifically (different coefficient per action head)?

4. Is the per-run linear decay (pre-v23 mechanism) still active, or was it fully replaced by the (broken) global mechanism? Code shows it was replaced -- the old `t_frac = iter/n_iters` code was removed in `7f3bed9c`.
