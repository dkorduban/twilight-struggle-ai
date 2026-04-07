# PPO Implementation Review

Date: 2026-04-07
Reviewer: Claude Opus 4.6

## Critical Bugs

### 1. GAE terminal delta is wrong (HIGH)

**Location:** `compute_gae()` lines 469-471

```python
if t == T - 1:
    next_value = 0.0
    delta = steps[t].reward - steps[t].value
```

The terminal delta should be `reward + gamma * 0 - value = reward - value`. This part is correct for terminal states. However, for **non-terminal intermediate steps**, `steps[t].reward` is always 0.0 (reward is only assigned to the last step of a game). This means `delta = 0 + gamma * V(t+1) - V(t)`, which is correct.

**Verdict:** GAE is actually correct. The sparse reward (only on last step) is handled properly.

### 2. old_log_prob computed without gradient but log_prob recomputation needs matching semantics (MEDIUM)

**Location:** `_sample_action_and_step()` line 256 vs `ppo_update()` line 562

During rollout, the model is set to `model.eval()` with `torch.no_grad()` (line 255-256). During update, the model is in `model.train()`. If the model uses dropout (it does, `dropout=0.1`), the forward pass outputs will differ between rollout and update, causing a mismatch between `old_log_prob` and `new_log_prob` even at iteration 0 before any weight update.

**Impact:** The ratio `exp(new_log_prob - old_log_prob)` will not start at exactly 1.0. This creates spurious KL divergence and may trigger early stopping. The PPO clipping mechanism mitigates this somewhat, but dropout noise adds uncontrolled variance to the surrogate objective.

**Fix:** Either (a) set `model.eval()` during the PPO update forward pass (just for log_prob/value computation, keep gradients flowing), or (b) disable dropout entirely for PPO (set `dropout=0.0` when loading). Option (a) is standard practice.

### 3. Country log_prob: gradient detachment via `.clone()` (MEDIUM-HIGH)

**Location:** `_compute_log_prob()` lines 223-228

```python
probs = country_logits.clone()
probs[~country_mask] = 0.0
probs = probs / (probs.sum() + 1e-10)
for c in country_targets:
    log_prob_country = log_prob_country + torch.log(probs[c] + 1e-10)
```

`country_logits` from the model is already a probability (output of mixture-of-softmaxes, summing to ~1.0). The `.clone()` preserves the computation graph, and in-place masking + renormalization should maintain gradient flow. This looks correct for autograd.

**However:** The IID assumption for INFLUENCE multi-ops is a significant approximation. When placing 3 ops with proportional allocation, the country log_prob is `sum of log(p_i)` treating each op placement as independent. In reality, the ops are allocated deterministically via the proportional scheme (floor + largest remainder). The log_prob of a deterministic allocation is not well-defined as a product of IID draws. This creates a noisy but non-zero gradient signal.

**Impact:** The gradient for country targets in INFLUENCE mode is theoretically incorrect, but since the country distribution is what we want to optimize, the gradient still pushes probability mass toward countries that led to wins. This is a reasonable approximation for a first implementation.

### 4. Approx KL has wrong sign (LOW-MEDIUM)

**Location:** `ppo_update()` line 599

```python
approx_kl = (old_log_probs - new_log_probs).mean().item()
```

The standard approximation is `KL(pi_old || pi_new) ~= E[log(pi_old/pi_new)] = E[old_log_prob - new_log_prob]`. This is correct in expectation. However, the more common and numerically better approximation from Schulman is `KL ~= E[(ratio - 1) - log(ratio)]`. The current version can go negative, which makes the `max_kl` early stopping unreliable (it only stops on large positive values, which correspond to the new policy moving away from old, but a negative mean could mask a high-variance KL).

**Impact:** The early stopping on `max_kl=0.1` may not trigger when it should, or may trigger spuriously. Not a training-breaking issue but reduces the safety net.

## Performance / Stability Issues

### 5. Per-step loop in PPO update is extremely slow (HIGH)

**Location:** `ppo_update()` lines 556-574

The inner loop iterates over each step in the minibatch individually, calling `_compute_log_prob()` one at a time. With `minibatch_size=2048` and `ppo_epochs=4`, this is ~8K individual forward-pass-equivalent operations per iteration (though the forward pass is batched, the log_prob computation is not).

**Impact:** The PPO update phase will be very slow -- likely slower than rollout. Each minibatch requires 2048 individual log_prob computations with Python-level loops.

**Fix:** Vectorize `_compute_log_prob` to work on batched tensors. The card and mode heads are straightforward to vectorize. Country is harder but can use `gather()` + `scatter()`.

### 6. Entropy missing country head contribution (LOW-MEDIUM)

**Location:** `ppo_update()` lines 570-574

```python
entropies[i] = ent_card + ent_mode
```

Country entropy is not included. For INFLUENCE/COUP/REALIGN steps, the country distribution entropy can be significant and is the primary exploration mechanism for target selection. Without it, the entropy bonus only encourages card and mode diversity, not country diversity.

**Fix:** Add country entropy for steps where `country_mask is not None`:
```python
if ctm is not None:
    country_probs_masked = clgts.clone()
    country_probs_masked[~ctm] = 0
    country_probs_masked = country_probs_masked / (country_probs_masked.sum() + 1e-10)
    ent_country = -(country_probs_masked * torch.log(country_probs_masked + 1e-10)).sum()
    entropies[i] += ent_country
```

### 7. Value target may be poorly calibrated (MEDIUM)

The value head was trained on BC data with `tanh` output in [-1, 1] (line 1363 of model.py). The PPO returns are computed as `advantage + value`, where advantages are GAE-computed from sparse {-1, +1} rewards with gamma=0.99. For a ~150-step game, the discounted return at step 0 is `gamma^150 * reward ~= 0.22 * (+/-1)`. The returns will be in roughly [-1, 1] which matches the tanh range.

**However:** The value loss uses `F.mse_loss(values_b, batch_returns)` where `values_b` is tanh-bounded but `batch_returns` is unbounded (though practically bounded by the reward range). If returns ever exceed [-1, 1] (unlikely with these hyperparams), the tanh output cannot represent them, creating persistent gradient pressure.

**Verdict:** Likely fine with current hyperparams. Monitor value loss -- if it's persistently high, this is the cause.

### 8. No learning rate schedule (LOW)

PPO often benefits from linear LR decay to zero over training. The current implementation uses constant LR. Not critical for a first experiment but worth adding if training is unstable in later iterations.

## Missing Features (Ordered by Importance)

### Must-have for first experiment

1. **Vectorized log_prob computation** (#5 above) -- without this, training will be prohibitively slow
2. **Dropout handling during update** (#2 above) -- use `model.eval()` or `dropout=0`
3. **Country entropy in bonus** (#6 above)

### Important for training quality

4. **Separate value network or stop-gradient on shared trunk** -- PPO literature (Andrychowicz et al. 2021, "What Matters In On-Policy Reinforcement Learning") found that sharing the trunk between policy and value heads hurts performance. With warm-start from BC this is less critical, but the value gradient can corrupt the policy trunk.
5. **Observation normalization** -- the input features have different scales (influence counts vs normalized scalars). Running mean/std normalization is a top-3 implementation detail per Huang et al. 2022.
6. **Reward normalization** -- normalize returns by running std (not the per-batch normalization of advantages, which is already done).

### Nice-to-have

7. **Value function clipping** -- clip value updates to prevent large value swings
8. **Linear LR annealing**
9. **Global gradient norm logging** (already clipping at 0.5, but logging the pre-clip norm helps diagnose issues)

## Side-Mixing Concern

Training on both USSR and US steps in the same PPO batch is fine in principle -- the advantage normalization handles different reward scales (both are {-1, +1}). The policy sees `side_int` as an input feature (scalar index 10), so it can learn side-dependent behavior. The value function similarly conditions on side.

**One subtle issue:** When training "both" sides, the model plays against MinimalHybrid as both USSR and US. The advantages from USSR games and US games have different baselines (USSR is inherently harder/easier). Mixing them in the same advantage normalization batch could create side-dependent bias. Consider normalizing advantages separately per side, or at minimum logging per-side metrics.

## Rollout Efficiency

Playing 1 game at a time via `play_callback_matchup` is the main bottleneck. The C++ engine supports batched play (`benchmark_batched`), but the callback interface requires synchronous Python callbacks.

**Options:**
1. **Thread pool with multiple games** -- launch N games in parallel threads, each with its own callback. Python GIL limits true parallelism but C++ releases GIL during engine computation.
2. **Async callback batching** -- modify C++ binding to collect decision points from multiple games, batch the neural net call, then distribute results back. This is the ideal solution but requires C++ changes.
3. **Accept the overhead** -- for 200 games/iter with ~150 steps/game, if each step takes ~1ms for inference, rollout is ~30s. With 500 games for benchmark adding ~60s, each iteration is ~2-3 minutes. For 200 iterations that's 7-10 hours. Slow but feasible for a first experiment.

## Summary of Priorities

| Priority | Issue | Impact | Effort |
|----------|-------|--------|--------|
| P0 | Vectorize log_prob in update loop (#5) | 10-50x speedup on update phase | Medium |
| P0 | Fix dropout eval/train mismatch (#2) | Prevents spurious KL / ratio noise | Trivial |
| P1 | Add country entropy (#6) | Better exploration of targets | Easy |
| P1 | Per-side advantage normalization | Prevents side bias | Easy |
| P2 | Observation normalization | Training stability | Medium |
| P2 | Separate value head or stop-gradient | Prevents value-policy interference | Medium |
| P3 | Better KL approximation (#4) | More reliable early stopping | Trivial |
| P3 | LR schedule | Late-training stability | Trivial |

The implementation is structurally sound and the PPO formulation is correct in its core components (GAE, clipped surrogate, advantage normalization). The main risks are: (1) speed -- the per-step loop will make the update phase very slow, and (2) the dropout train/eval mismatch creating noisy ratio estimates. Fix these two and the first experiment should produce meaningful signal.
