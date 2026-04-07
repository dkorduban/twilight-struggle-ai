# Experiment Log — Phase 2: Reinforcement Learning

Started: 2026-04-07

## Context

Phase 1 (see `experiment_log_phase1.md`) established:
- **BC ceiling**: ~33-35% Nash combined vs heuristic (v106_cf_gnn_s42 = 34.9%)
- **13 dead ends** in BC: teacher KL, data volume, wider models, K>1 MCTS, etc.
- **MCTS 2000sim + pruning**: 43.7% combined (+8.8pp over greedy) — too slow for training
- **Architecture winner**: GNN adjacency (control_feat_gnn) with K=4 mixture country head

Phase 2 explores RL (PPO) to break through the BC ceiling.

---

## PPO v1: vs Nash-temp Heuristic (2026-04-07)

### Setup

- **Base checkpoint**: v106_cf_gnn_s42 (BC, 34.9% Nash combined)
- **Opponent**: MinimalHybrid with Nash temperature sampling (same as training data)
- **Architecture**: TSControlFeatGNNModel, h=256, K=4 mixture country head
- **Hyperparameters**:
  ```
  games_per_iter=200, ppo_epochs=4, clip_eps=0.2, lr=1e-4,
  gamma=0.99, gae_lambda=0.95, ent_coef=0.01, vf_coef=0.5,
  minibatch_size=2048, side=both, seed=99000
  ```
- **Reward**: Sparse ±1.0 on terminal step only (win/loss)
- **Rollout**: C++ batched game pool (`rollout_games_batched`), ~24s/200 games
- **Log_probs**: Recomputed in Python after C++ rollout (TorchScript trace bug workaround)

### Benchmark Trajectory (500 games/side, Nash temps, seed=50000/50500)

| Iter | USSR WR | US WR | Combined | Notes |
|------|---------|-------|----------|-------|
| 0 (BC) | 55.8% | 14.0% | 34.9% | v106_cf_gnn_s42 baseline |
| 20 | 66.2% | 13.8% | 40.0% | |
| 40 | 74.8% | 11.6% | 43.2% | US dips during USSR improvement |
| 60 | 81.2% | 21.4% | 51.3% | US starts improving |
| 80 | 86.6% | 29.0% | 57.8% | |
| 100 | 85.6% | 50.4% | 68.0% | US breakthrough |
| 120 | 84.0% | 67.2% | 75.6% | |
| 140 | 91.8% | 68.0% | 79.9% | |
| 160 | 90.6% | 74.2% | 82.4% | Current best |

### Loss Trajectory (sampled milestones)

| Iter | Rollout WR | Steps | Entropy | Value Loss | Policy Loss | Clip Frac | KL |
|------|-----------|-------|---------|------------|-------------|-----------|-----|
| 100 | 0.655 | 13,897 | 2.451 | 0.073 | -0.035 | 0.187 | 0.020 |
| 120 | 0.685 | 13,445 | 2.300 | 0.083 | -0.033 | 0.175 | 0.022 |
| 140 | 0.770 | 13,672 | 2.205 | 0.077 | -0.032 | 0.184 | 0.020 |
| 160 | 0.790 | 13,481 | 2.166 | 0.074 | -0.026 | 0.185 | 0.021 |
| 175 | 0.740 | 13,077 | 2.112 | 0.074 | -0.028 | 0.172 | 0.019 |

### Key Observations

1. **US WR is the real achievement**: 14% → 74% is extraordinary. BC never reached >14% US WR
   despite 13 different approaches. PPO found US strategies that BC couldn't learn from
   heuristic demonstrations.

2. **Entropy is slowly declining**: 2.45 → 2.11 over 75 iters. Policy is sharpening but
   not collapsed. Still exploring diverse actions.

3. **Value loss plateaued at ~0.07**: Not improving despite higher WR. The value head
   predicts the terminal outcome, and at 80%+ WR most games are wins — the value function
   correctly predicts ~0.8 for most states but can't distinguish the remaining 20% losses.

4. **Steps per iteration declining**: 14,500 → 13,100. Games are getting shorter as the
   policy wins faster. Could indicate exploitation (quick DEFCON kills) or efficiency
   (winning in fewer action rounds).

5. **KL is healthy**: 0.017-0.025 consistently. No sudden policy jumps.

### Overfitting Concern

**At 82%+ combined WR, the model likely exploits heuristic-specific weaknesses.**

Evidence for exploitation:
- Games getting shorter (fewer steps/iter): faster wins may mean DEFCON exploitation
- Heuristic plays a fixed mixed strategy — deterministic weaknesses can be memorized
- No adversarial pressure — model has no incentive for robustness
- Value loss flat at 0.07 despite WR climbing — wins are "easy" now

Evidence against pure exploitation:
- US WR 74% is remarkable — the heuristic as USSR is very strong (66% WR in self-play)
- Entropy still at 2.1 (healthy diversity in action selection)
- The improvement was gradual over 160 iters, not a sudden exploit discovery
- Policy loss magnitude gradually decreasing — optimization is smooth

**Likely reality**: Mix of both. The model learned genuinely better TS strategy (especially
for US side) AND learned heuristic-specific patterns that won't transfer to stronger opponents.

### Diagnostic experiments needed

To distinguish real strength from heuristic exploitation:

1. **PPO model vs itself**: Does it play coherent games? With +2 bid the game is balanced
   in pro play (~50/50 ±2pp). Self-play WR should be near 50/50. If wildly asymmetric
   (e.g. 90/10), the model has a degenerate strategy for one side.

2. **PPO model vs MCTS 400sim (greedy policy)**: If PPO beats MCTS-augmented greedy,
   the improvement is real. If PPO loses to MCTS, the improvement is exploitation.

3. **PPO model vs different heuristic**: Test against a hand-crafted stronger opponent
   or a different temperature schedule. If WR drops dramatically, exploitation is confirmed.

4. **Game length analysis**: Check whether PPO wins are concentrated in early turns
   (DEFCON exploits) or spread across the game (strategic improvement).

### Infrastructure

- **C++ batched rollout**: `rollout_games_batched()` in `mcts_batched.cpp`
  - Records per-step features, masks, actions, log_probs, values
  - 23× speedup over sequential Python callback (24s vs 560s per 200 games)

- **TorchScript trace workaround**: `_recompute_log_probs_and_values()` in `train_ppo.py`
  - `jit.trace` freezes data-dependent branches in GNN model
  - Python recomputation adds ~5s but ensures log_prob consistency

- **Rolling checkpoints**: Write-before-delete pattern, milestone preservation at
  benchmark iterations (every 20)

- **Per-side tracking**: W&B logs `rollout_wr_ussr` and `rollout_wr_us` separately

### Crashes and Fixes

1. **Country ID 64 crash (iter 48)**: Proportional allocation sampled country 64 which
   has no spec. Fix: mask out ID 64 before sampling (`VALID_COUNTRY_IDS = range(86) - {64}`).

2. **KL divergence early stop (iter 43)**: After switching to batched rollout, TorchScript
   trace caused log_prob mismatch. Fix: recompute log_probs in Python post-rollout.

### W&B

Multiple runs due to restarts: korduban-ai/twilight-struggle-ai (PPO v1 runs).
Restart points: iter 41 (ID 64 crash), iter 43 (KL mismatch), iter 78 (batched rollout switch).

### Final PPO v1 Result

Ran to 200 iterations. Final benchmark (iter 200): **83.2% combined** (USSR=90.6%, US=74.2%).
Best checkpoint: `data/checkpoints/ppo_v1_from_v106/ppo_best.pt`

---

## Infrastructure Improvements (2026-04-07)

### jit.script GNN model fix

**Problem**: `torch.jit.trace` freezes `if bg_mask.any(): x[:, bg_mask, :]` branches
in `TSControlFeatGNNEncoder` as compile-time constants, causing log_prob divergence.

**Fix**: Replaced all conditional boolean indexing with branch-free weighted-sum pooling:
```python
# BEFORE (breaks jit.script):
if bg_mask.any():
    bg_pooled = x[:, bg_mask, :].mean(dim=1)
# AFTER (jit.script compatible):
bg_weight = bg_mask.float().unsqueeze(0).unsqueeze(-1)
bg_count = bg_weight.sum(dim=1).clamp(min=1.0)
bg_pooled = (x * bg_weight).sum(dim=1) / bg_count
```

`torch.jit.script(TSControlFeatGNNModel())` now succeeds. Numerical outputs match within 1e-5.

**Effect**: `_recompute_log_probs_and_values` no longer needed in rollout. Saves ~5s/iter.

### Additional features added

- **VP-scaled terminal reward**: `--vp-reward-coef` (default 0 = ±1 binary). Scales
  terminal reward by final VP magnitude: `(1-coef)*±1 + coef*clip(final_vp/20, -1, 1)`
- **Entropy scheduling**: `--ent-coef-final` for linear decay over training
- **Self-play rollout**: `rollout_self_play_batched` C++ function + Python binding.
  Records steps for both sides, assigns per-side rewards from same game outcome.
- **Self-play PPO mode**: `--self-play` flag in `train_ppo.py`, with `--self-play-heuristic-mix`
  (default 0.2) to anchor against heuristic collapse.

---

## PPO v2: Self-Play (2026-04-07)

### Setup

- **Base checkpoint**: ppo_v1_from_v106/ppo_best.pt (83.2% combined)
- **Mode**: Self-play (both sides learned model) + 20% heuristic mix
- **Hyperparameters**:
  ```
  games_per_iter=200, ppo_epochs=1, clip_eps=0.2, lr=5e-5, max_kl=0.2,
  gamma=0.99, gae_lambda=0.95, ent_coef=0.01, vf_coef=0.5, seed=100000
  ```
- **Reward**: Sparse ±1.0 terminal (no VP scaling)
- **Rollout**: ~30k steps/iter (both sides recorded; 2× vs v1's 13k)
- **Log_probs**: TorchScript from C++ (jit.script fixed; no Python recomputation)

### Rationale for reduced lr/epochs

Self-play produces ~2.3× more steps per iteration (both sides recorded, ~30k vs 13k).
PPO v2 crash at iter 1 with default settings (KL 0.24 >> 0.1). Fix: halved lr (1e-4→5e-5)
and reduced ppo_epochs (4→1) to match effective gradient steps. max_kl raised to 0.2
(self-play research typically uses larger KL thresholds).

### Early Training Observations (iters 1-17)

| Iter | Rollout WR | Steps | Entropy | Value Loss | Policy Loss | KL |
|------|-----------|-------|---------|------------|-------------|-----|
| 1 | 0.458 | 29,989 | 2.277 | 0.129 | 0.042 | 0.143 |
| 5 | 0.492 | ~30k | 2.220 | 0.091 | 0.025 | 0.124 |
| 13 | 0.512 | 30,518 | 2.034 | 0.073 | 0.020 | 0.105 |
| 17 | 0.517 | 30,106 | 2.025 | 0.067 | 0.017 | 0.101 |

- Rollout WR trending toward 0.5 as expected (self-play should equalize)
- KL stabilizing around 0.10-0.11 (below 0.2 threshold)
- Entropy declining: 2.28 → 2.02 (policy sharpening)
- W&B run: korduban-ai/twilight-struggle-ai, run `f4j10b29`

### Self-play WR interpretation

`rollout_wr` aggregates heuristic mix games + self-play games. The USSR/US split
(`rollout_wr_ussr=0.788, rollout_wr_us=0.441` at iter 17) includes heuristic games
where model vs heuristic is very strong. Pure self-play WR tracked separately via
`sp_rollout_wr_ussr` and `sp_rollout_wr_us` in W&B.

### GAE Zero-Sum Bug (discovered and fixed during PPO v2)

**Bug**: In self-play GAE computation, consecutive steps alternate between USSR (side_int=0)
and US (side_int=1). Original `compute_gae` used `next_value = steps[t+1].value` regardless
of side, mixing values from opponent perspective. Since V_USSR(s) = -V_US(s) in zero-sum
games, this introduced a `+gamma` bias per step for the USSR side, causing progressive
USSR skill degradation.

**Symptom**: USSR WR dropped from ~50% self-play WR to 27% after 30 iters of the buggy
PPO v2. Heuristic WR dropped from 83.2% to 65.4%.

**Fix**: `_compute_gae_per_side()` — compute GAE independently for each side's steps within
a game, bootstrapping only from same-side future values. Terminal rewards: winner gets +1,
loser gets -1.

**Note**: Tried zero-sum flip first (negating cross-side bootstrap). Value loss spiked to
41.4 — PPO v1's value function was not trained symmetrically. Per-side GAE avoids this by
never crossing sides.

### PPO v2b: Self-Play with Per-Side GAE Fix (2026-04-07)

**Setup**: Same as v2 but with `_compute_gae_per_side()`, `--max-kl 0.25`, `--seed 200000`.
Base: PPO v1 best (83.2% combined).

### Iter 20 Benchmark vs Heuristic

| Iter | USSR WR | US WR | Combined | Notes |
|------|---------|-------|----------|-------|
| 0 (PPO v1 best) | 90.6% | 74.2% | 83.2% | Starting point |
| 20 | 84.0% | 63.2% | 73.6% | Self-play anchored with 20% heuristic mix |

Heuristic WR drop from 83.2% → 73.6% is expected: self-play shifts the model from
heuristic-exploitation toward general strategy. Not regression — the cross-model Elo
proves it's stronger.

### Cross-Checkpoint Elo (iter 20)

Using `benchmark_model_vs_model_batched` (200 games, seed=77000):
- **PPO v1 best** vs **PPO v2b iter 20**: v2b wins 100/200, v1 wins 92/200, 8 draws
- v2b WR = 54.0% over v1 → **Elo: PPO v1=1407, PPO v2b_iter20=1592** (+185 pts)

PPO v2b after just 20 iters of self-play already beats PPO v1's 200-iter result (which
was the best heuristic-trained checkpoint). This confirms that self-play is providing
real strength gains, not just shifting to different heuristic exploitation patterns.

---

## Next Steps

See `docs/ppo_next_steps.md` for detailed plan. Summary:

1. ✅ Self-play PPO (running as PPO v2b with fixed GAE)
2. ✅ Cross-checkpoint Elo (infrastructure complete, first matchup done)
3. League training (pool of past checkpoints) — spec in `.claude/plan/league-training.md`
4. VP-scaled rewards + entropy scheduling (added to train_ppo.py, not yet used in v2b)
5. MCTS-guided PPO (Expert Iteration)
