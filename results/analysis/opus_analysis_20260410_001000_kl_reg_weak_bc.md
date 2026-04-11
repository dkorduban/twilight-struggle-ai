---
# Opus Analysis: KL Regularization with Weak BC Policy
Date: 2026-04-10T00:10:00Z

## Executive Summary

The previous Opus recommendation to KL-regularize toward the BC policy was **wrong about the anchor point but right about the mechanism**. KL regularization toward a weak BC policy would actively harm training by pulling the 2109-Elo v22 model backward toward a ~1500-Elo prior. However, the underlying diagnosis --- that v23 collapsed due to unanchored logit compression --- is correct, and the fix is simpler than the previous analysis suggested. The primary cause of the v23 collapse was a **log-probability mismatch bug** introduced by the T=1.2 rollout temperature: the C++ rollout stores log_prob under the temperature-scaled distribution (logits/1.2), while the Python PPO update recomputes log_prob under the unscaled distribution (logits/1.0). This systematic mismatch in the importance sampling ratio drives the policy toward higher entropy regardless of any anchoring mechanism. Fixing this bug is the highest-priority action and may be sufficient on its own. If additional stabilization is needed, the correct anchor is the **previous run's best checkpoint** (v22), not the BC policy.

## Findings

### 1. The Log-Prob Mismatch Bug (Root Cause of v23 Collapse)

The v23 collapse has a clear proximate cause that has nothing to do with anchoring or regularization.

**During rollout** (C++ `sample_index_from_masked_logits`, mcts_batched.cpp line 3482-3491):
```cpp
auto scaled = masked / temperature;  // logits / 1.2
auto probs = torch::softmax(scaled, 0);
const auto log_prob = torch::log_softmax(scaled, 0).index({sampled_idx}).item<float>();
```
The stored `log_prob` = log(softmax(logits/1.2))[action].

**During PPO update** (Python `ppo_update`, train_ppo.py line 1418-1420):
```python
masked_card = card_logits_b.masked_fill(~card_masks_b, float("-inf"))
log_prob_card = F.log_softmax(masked_card, dim=1).gather(...)
```
The recomputed `new_log_prob` = log(softmax(logits/1.0))[action].

**The importance ratio is therefore wrong:** ratio = exp(new_log_prob - old_log_prob) is NOT exp(log pi_new(a) - log pi_old(a)). It is exp(log_softmax(logits_new/1.0) - log_softmax(logits_old/1.2)). Even when the model weights have not changed (new = old), this ratio is != 1 for any action where the logit is not the same as the mean logit.

Specifically, for the highest-logit action, log_softmax(logits/1.0) > log_softmax(logits/1.2) because softmax at lower temperature concentrates more probability on the top action. So the ratio is > 1 for the best action, and < 1 for worse actions. The PPO clip then clips the "too-high" ratios, but the gradient from the "too-low" ratios on negative-advantage actions pushes the policy toward uniform. This is exactly the v23 signature: entropy rises, logit range compresses, policy becomes diffuse.

**This is not a temperature problem per se --- it is an importance sampling correctness bug.** T=1.2 rollout is fine if the stored log_prob uses the same temperature as the PPO update, or equivalently, if the PPO update also divides logits by T before computing log_softmax. The v22 run did not have this bug because it used T=1.0 (the default), where both computations agree.

### 2. KL Toward BC Policy: Would It Help?

Even if the log-prob bug is fixed, would KL regularization toward the BC policy be a good idea? No, for three reasons:

**a) The BC policy is far weaker than the current model.** The BC policy was trained on heuristic self-play data (heuristic Elo ~1500) plus 51 human games. Its effective Elo is roughly 1500-1600. The current best model (v22) is at 2109 Elo, representing 500+ Elo points of learned improvement. KL-regularizing toward the BC policy would create a constant gradient pulling the model back toward weak play. The KL penalty would be largest exactly where the model has improved most (i.e., on decisions where BC plays poorly and v22 plays well).

**b) KL regularization does not prevent improvement, but it taxes it.** The mechanics of KL(pi_current || pi_BC) add a gradient term proportional to log(pi_current(a) / pi_BC(a)) for each action. This means: if pi_current increases probability on an action that pi_BC already liked, the penalty is small; if pi_current increases probability on an action that pi_BC disliked, the penalty is large. Since the BC policy was trained on weak data, the actions it dislikes include many objectively good actions that v22 has learned through RL. The regularization would systematically penalize learning novel good strategies.

**c) AlphaStar's use case was fundamentally different.** AlphaStar KL-regularized toward a BC policy trained on grandmaster-level human replays --- a policy that was already near-optimal in many situations. The BC prior served as a "common sense" anchor against degenerate strategies. Our BC policy is not near-optimal; it is the output of a weak heuristic-trained model. Using it as "common sense" would anchor the model to bad common sense.

### 3. Better Anchor: Previous Run's Best Checkpoint

If KL regularization is desired (after fixing the log-prob bug), the correct reference distribution is the **previous run's best checkpoint** (v22 in the current case, or more generally, the initial checkpoint for each PPO run).

**This is actually what PPO already provides, approximately.** The PPO clipping mechanism (clip_eps=0.12) constrains the ratio exp(new_log_prob - old_log_prob) to [0.88, 1.12], which is equivalent to a soft KL constraint within each iteration. The --max-kl=0.3 early stop provides a hard constraint. Over 200 iterations, these constraints allow substantial drift from the initial policy, but this is by design --- the model is supposed to improve.

**If we want a tighter anchor to v22 specifically**, the options are:
- Reduce clip_eps (e.g., from 0.12 to 0.08): tighter per-iteration constraint, slower drift
- Reduce max-kl (e.g., from 0.3 to 0.1): earlier stopping on large updates
- Add explicit KL toward the initial checkpoint: loss += beta * KL(pi_current || pi_v22), with beta decaying to 0 over training

The third option is the most principled but also the most complex. It requires keeping a frozen copy of the initial model in memory (doubling GPU memory usage on a 4GB RTX 3050) and computing an additional forward pass per PPO minibatch. Given that the primary cause of v23 collapse was the log-prob bug, this complexity is likely unnecessary.

### 4. Entropy Regularization Alone (No KL Anchor)

The current system already has entropy regularization: `loss += ent_coef * (-entropy)`, which encourages higher entropy. The ent_coef decays from 0.03 to 0.005 over the global training schedule.

**Could we add a max-entropy constraint instead?** This would be: `loss += lambda * max(0, entropy - threshold)`, penalizing entropy above a threshold. This would prevent the entropy explosion observed in v23 (4.0 -> 5.2) without anchoring to any specific policy.

However, after fixing the log-prob bug, the entropy explosion should not recur. The entropy drift in v23 was a symptom of the mismatch, not an independent pathology. V22 trained stably at entropy ~4.0-4.2 for 200 iterations without any max-entropy constraint.

**Entropy ceiling as a safety net:** Adding a lightweight `loss += max(0, entropy - 5.0) * 0.1` would provide a soft ceiling at entropy 5.0 without constraining normal learning. This is cheap, simple, and does not require a reference model. It would have caught the v23 collapse around iteration 25-30 (when entropy first exceeded 5.0). This is worth adding as a safety mechanism even after fixing the log-prob bug.

### 5. What Actually Caused the v23 Collapse

The evidence points to a single root cause with compounding effects:

**Timeline reconstruction:**
- v22: trained with T=1.0 (default), finished at Elo 2109, entropy ~4.0, card_logits [-16, +13]
- v23 iter 1: T=1.2 introduced, entropy=3.985, card_logits [-15.72, +12.25] (starting from v22 weights)
- v23 iter 5: entropy=4.453, card_logits [-12.39, +11.03], rollout_wr=0.425 (already declining)
- v23 iter 10: entropy=4.619, card_logits [-10.84, +9.30], rollout_wr=0.220
- v23 iter 20: entropy=4.783, card_logits [-8.93, +5.30], rollout_wr=0.150
- v23 iter 50: entropy=5.079, card_logits [-5.99, +2.55], rollout_wr=0.215
- v23 iter 100: entropy=5.208, card_logits [-5.23, +2.31], rollout_wr=0.285
- v23 iter 200: entropy=4.983, card_logits [-4.20, +1.72], rollout_wr=0.175

The logit range monotonically compresses throughout training. The entropy rises for the first ~100 iterations then stabilizes near 5.0 as the ent_coef decays to its minimum. The model never recovers.

**This pattern is fully explained by the log-prob mismatch.** The systematically wrong importance ratios create a gradient that compresses logits toward zero (toward uniform distribution), which increases entropy and destroys the model's ability to discriminate between good and bad actions. PPO clipping limits the rate of damage but cannot prevent it because the mismatch is present in every single minibatch.

**Was it the league sampling?** No. V22 used the same league mechanism (with slightly different fixtures: v4/v8/v12 vs v8/v14/v19). The league sampling was essentially unchanged between v22 and v23.

**Was it the ent_coef schedule?** No. The ent_coef was already at or near its minimum (0.005) by v23. The entropy bonus was negligible.

### 6. UPGO with a Weak Value Function

UPGO (Upgoing Policy Gradient) clips negative advantages to zero, only reinforcing trajectories where G_t > V(s_t). The previous analysis recommended this as a complementary technique.

**Assessment in our context:**

UPGO is theoretically sound but has a subtle interaction with value function quality:

- **If the value function overestimates:** V(s_t) is too high, so G_t > V(s_t) rarely, and UPGO clips most advantages to zero. Learning is very slow. This is the "pessimistic UPGO" regime.
- **If the value function underestimates:** V(s_t) is too low, so G_t > V(s_t) often, and UPGO is a near-no-op. Equivalent to standard GAE.
- **If the value function is accurate:** UPGO correctly filters noise, keeping good trajectories and discarding bad luck.

In our case, the value function is trained concurrently with the policy and starts from the v22 checkpoint, which had value_loss ~0.10 (a reasonable level). The value function is not perfect but is not severely miscalibrated. UPGO should be modestly beneficial.

**However, UPGO is orthogonal to the v23 collapse.** UPGO addresses variance in the policy gradient; the v23 collapse was caused by bias (systematic log-prob mismatch). UPGO would not have prevented the collapse.

**Recommendation on UPGO:** Good to implement as a general PPO improvement, but not urgent. It should be lower priority than fixing the log-prob bug. Implementation is simple (~5 lines: `advantages = torch.clamp(advantages, min=0)` before computing the policy loss, while keeping unclamped advantages for value function training).

## Conclusions

1. **The v23 collapse was caused by a log-probability mismatch bug, not by lack of KL regularization.** The C++ rollout stores log_prob(logits/T) while the Python PPO update computes log_prob(logits/1.0). When T=1.2, this creates systematically wrong importance ratios that push the policy toward uniform.

2. **KL regularization toward the BC policy would be actively harmful.** The BC policy is 500+ Elo points weaker than the current best model. Anchoring to it would penalize exactly the improvements that RL has learned. The AlphaStar analogy does not apply because their BC policy was trained on grandmaster replays, not weak heuristic data.

3. **The simplest fix is to make the PPO update use the same temperature as the rollout.** Either: (a) divide logits by T in the Python log_prob computation, matching the C++ rollout, or (b) have the C++ rollout store log_prob at T=1.0 (the model's native distribution) while still sampling at T=1.2. Option (b) is cleaner because it keeps the importance sampling ratio correct without requiring the PPO code to know the rollout temperature.

4. **If additional stabilization is needed after the bug fix, the correct anchor is the initial checkpoint (v22), not the BC policy.** But this may be unnecessary since v22 was stable for 200 iterations at T=1.0.

5. **An entropy ceiling (soft penalty when entropy > 5.0) is a worthwhile safety mechanism** that would catch future collapse modes without anchoring to any specific policy. Cheap, simple, one line of code.

6. **UPGO is a good general improvement but is orthogonal to the collapse and lower priority.** It addresses variance, not the bias that caused the collapse.

## Recommendations

**Priority 1 (Critical Fix):** Fix the log-probability mismatch. In `sample_index_from_masked_logits` (mcts_batched.cpp), compute and store log_prob using the unscaled logits (T=1.0) while keeping the sampling distribution at T=rollout_temp. This is a ~3-line change:
```cpp
const auto log_prob = torch::log_softmax(masked, 0).index({sampled_idx}).item<float>();
// ^-- use 'masked' (unscaled), not 'scaled' (logits/T)
```
The same fix should be applied to country target sampling if temperature is applied there.

**Priority 2 (Safety Net):** Add a soft entropy ceiling to the PPO loss:
```python
ent_ceiling_penalty = torch.clamp(entropies.mean() - 5.0, min=0.0) * 0.1
loss = policy_loss + vf_coef * value_loss + ent_coef * entropy_loss + ent_ceiling_penalty
```

**Priority 3 (Validation):** Rerun v23 from the v22 checkpoint with the log-prob fix and T=1.2 to confirm the fix resolves the collapse. Compare against a control run with T=1.0 (which should reproduce v22-like behavior).

**Priority 4 (Optional):** If T=1.2 still shows instability after the bug fix, reduce to T=1.05-1.1 as a more conservative exploration setting.

**Do NOT implement:**
- KL regularization toward the BC policy
- KL regularization toward any fixed anchor (the PPO clip mechanism already provides per-iteration drift control)

**Defer to later:**
- UPGO (good idea, but orthogonal to the collapse; implement after confirming the fix works)
- KL toward v22 (unnecessary if the bug fix resolves the instability)

## Open Questions

1. **Country target log-prob:** Does the country head also have a temperature mismatch? The country targets use a different probability computation (mixture probabilities, not logits), so the mismatch may not apply. Needs verification in the C++ code.

2. **Was the mismatch present in earlier runs?** All runs before v23 used T=1.0, so the mismatch was (1.0/1.0) = no mismatch. The bug has always been latent in the code; T=1.2 activated it.

3. **Optimal rollout temperature after fix:** With correct importance ratios, T=1.2 may still be too aggressive for a 200-iteration run. The optimal temperature depends on the model's current sharpness and the diversity of opponents. Empirical tuning needed.

4. **Does the nash_temperatures heuristic opponent temperature create a similar mismatch for the heuristic's side?** No --- the heuristic opponent's actions do not contribute to the learned model's log_prob computation. The mismatch only affects the learned model's own action log_probs.

5. **Interaction with PPO epochs:** The bug is present in every minibatch of every PPO epoch (default 4 epochs). More epochs compound the bias. Reducing to 1 epoch would mitigate the damage but not fix the root cause.
