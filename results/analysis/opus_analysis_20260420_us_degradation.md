# Opus Analysis: PPO US Side Degradation
Date: 2026-04-20
Question: Why does US WR drop 25pp within 10 PPO iters and how to fix it?

## Executive Summary

PPO is consistently burning the US side within 10-20 iterations. The combined WR
cap at ~0.40 is not a single-bug failure — it is the compound effect of at least
four reinforcing dynamics in `scripts/train_ppo.py`:

1.  **The `us_win_w = torch.where(returns < 0, 2.0, 1.0)` weighting at lines
    1978 and 2255 does NOT do what the committed memory says it does.** The memory
    `feedback_us_win_value_weighting.md` claims it "upweights US-win positions."
    In reality it upweights **losses on either side**. On the US side, ~85% of
    games are losses (US WR ≈ 0.15), so `us_win_w=2` fires on the majority class
    and drives the value head to learn "US states are losing." On the USSR side
    only ~27% of games are losses, so the same rule is more benign. This is a
    smoking-gun mislabelled implementation that actively *causes* US value
    miscalibration rather than fixing it.

2.  **UPGO (`--upgo=true` in v13/v18/v20) kills policy gradient on the losing
    side asymmetrically.** For a side with 15% WR, the value head quickly learns
    that US positions are bad, so `value > upgo_g` on most US-side steps → the
    US-side policy gradient attenuates toward zero, while USSR gradients remain
    strong. This causes a learning-rate asymmetry between sides that is not
    fixed by per-side advantage normalization (which only centers advantages,
    does not add gradient mass back).

3.  **The PPO rollout step distribution is side-balanced by GAMES but not by
    STEPS.** US-side games terminate early (DEFCON1 / VP20 / europe_control)
    when the model plays poorly; USSR-side games run full length. With US WR
    ≈ 0.15 the actual step counts probably run ~1.5-2:1 USSR:US, so USSR
    dominates each minibatch even before any per-side weighting. (This is not
    verified directly; add `n_steps_ussr` / `n_steps_us` to the log dict to
    confirm in one iter — a one-line fix.)

4.  **The v13 → v20 PFSP pool has not diverged meaningfully, but per-opponent
    side coverage is wildly uneven.** `results/ppo_v20_v13warm/wr_table.json`
    shows `v56_scripted` played 132 USSR games, **0 US games**. `iter_0010`
    played 0 USSR games, 264 US games. Under PFSP `sym+UCB` weighting this is
    expected behavior, but in a 20-iter run the resulting US-side opponent
    distribution is thin and skewed — US updates are dominated by a tiny set of
    opponents. This is a secondary factor, not the primary cause.

The primary causes are (1) and (2). They are cheap to test and fix.

## Findings (with code line references)

### 1. `us_win_w` is semantically wrong (PRIMARY)

`scripts/train_ppo.py:1978` and `:2255`
```python
us_win_w = torch.where(batch_returns < 0, 2.0, 1.0)
value_loss = (us_win_w * (values_b - batch_returns) ** 2).mean()
```

The variable name suggests "US-win weight" but the predicate `returns < 0`
selects ALL losses (any side), not US-win positions. In per-side GAE/return
convention (see `compute_gae` line 1661 and `_compute_gae_per_side` line 1681),
`returns` is negative whenever the actor (of that step) lost. The implementation
upweights losses equally on both sides.

The memory rationale ("self-play data is ~70/30 USSR-wins/US-wins → value head
undertrained on US-wins") would require weighting by `side_int==1` AND
`returns>0`, or alternatively by `side_int==1` unconditionally. Neither is
implemented. What *is* implemented amplifies the overrepresented
"US-plays-and-loses" class, pushing the value head's mean on US states further
negative.

A stronger-pessimism value head on the US side makes policy updates on US
states less discriminating (advantages compressed around large negative means),
and under UPGO (see §2) directly silences gradient flow.

### 2. UPGO silently zeros US-side policy gradient

`scripts/train_ppo.py:1791`
```python
def _apply_upgo_to_segment(seg: list[Step], gamma: float) -> None:
    T = len(seg); upgo_g = 0.0
    for t in reversed(range(T)):
        r = seg[t].reward
        v_next = seg[t + 1].value if t + 1 < T else 0.0
        upgo_g = r + gamma * max(v_next, upgo_g)
        seg[t].advantage = upgo_g - seg[t].value
```

UPGO `advantage = G_upgo - value`, where `G_upgo = r + γ·max(v_next, G_upgo_{t+1})`.
On a lost trajectory (r=-1 at terminal, 0 elsewhere), `G_upgo` collapses to the
per-step bootstrap and advantage is ≤ 0 on most steps. Per-side advantage
normalization in `pack_steps` (line 2103-2109) centers these, but the residual
variance is much smaller on the US side (because most steps have similar
pessimistic returns). Combined with PPO ratio clipping, this produces very low
effective gradient magnitude on US-side steps.

v13 (best run, 0.427 combined) was also `upgo=true`, so UPGO alone is not the
trigger. The trigger is the **interaction**: as soon as US WR drops below
~0.30, UPGO starts preferentially silencing US updates, which makes US WR drop
further → runaway feedback loop confirmed by the evidence (v20 US WR:
0.38→0.124 in 10 iters).

### 3. Step count imbalance per side (unverified but very likely)

`scripts/train_ppo.py:3506-3509`
```python
ussr_done = [s for s in terminal_steps if s.side_int == 0]
us_done = [s for s in terminal_steps if s.side_int == 1]
```

Win rate is tracked, step counts per side are NOT logged. Per-side advantage
normalization (line 2103-2109) and per-side GAE handle game boundaries, but
the minibatch sampler (line 2182 `perm = torch.randperm(num_steps)`) draws
uniformly from the combined flat pool. If USSR produces 2x as many steps as
US per iter, USSR state coverage is 2x higher. Single-line diagnostic:
```python
log_dict["n_steps_ussr"] = sum(1 for s in all_steps if s.side_int == 0)
log_dict["n_steps_us"]   = sum(1 for s in all_steps if s.side_int == 1)
```

### 4. Rollout pool composition (secondary)

`results/ppo_v20_v13warm/wr_table.json`:
```
v56_scripted: total_ussr=132 total_us=0        ← PFSP never picked v56 for US pool
v55_scripted: total_ussr=66  total_us=132
v44_scripted: total_ussr=264 total_us=264
iter_0010:    total_ussr=0   total_us=264      ← self-snapshot only on US
heuristic:    total_ussr=198 total_us=66       ← 3:1 heuristic imbalance
```

This is PFSP + heuristic_floor=0.2 working as designed: US-pool is pulled
toward opponents the US model currently loses to (self-snapshots, v44), while
USSR-pool pulls toward opponents the USSR model struggles with (heuristic,
v56). Net effect: heuristic signal for USSR is 3x stronger than for US. US
side is trained against a thin, biased pool.

With only 10-20 training iterations, small sample means the US pool has very
high variance in composition. This alone wouldn't cause a 25pp drop in 10
iters, but it amplifies the other effects.

### 5. Rollout structure: self-slot gives balanced games, pool slots don't

`scripts/train_ppo.py:1536-1547`. Task allocation for v20 (mix_k=4, self_slot=True):
- `k_per_side = max(1, (4-1)//2) = 1`
- `total_slots = 1 + 1*2 = 3`
- `games_per_slot = 200//3 = 66`
- Self-slot: 66 games "both" (alternating → 33 USSR + 33 US via
  `rollout_model_vs_model_batched(learned_side=Neutral)`, see
  `cpp/tscore/mcts_batched.cpp:4109-4113`)
- USSR-pool: 66 USSR-only games
- US-pool: 66 US-only games
- Per iter: 99 USSR games, 99 US games

Game counts ARE balanced. Step counts likely are NOT (§3).

### 6. v20 args retained full-run config — not a "gentle fine-tune"

`results/ppo_v20_v13warm/ppo_args.json`:
- `lr=5e-5` constant, `clip_eps=0.12`, `ppo_epochs=4`, `target_kl=0.015`
- `ema_decay=0.995` — 10 iters ≈ 5% EMA influence
- `reset_optimizer: false` (GOOD — preserves Adam moments from v13)

LR and clip are conservative but 4 PPO epochs on 200 games per iter is still
enough churn to reshape policy. On a model at 0.427, even small gradient bias
toward USSR (§1+§2) compounds fast.

### 7. The "good" v13 iter20 checkpoint is a lucky peak, not a stable attractor

From memory (`project_ppo_seed_investigation.md`) and `autonomous_decisions.log`:
- v13 (seed=42000) peaked at iter20 = 0.427, had US WR ~0.38 at that point
- Subsequent iters drifted: "all v56-warmstart runs give 0.30-0.41 peak"
- v18 seed sweep: 0.372 / 0.383 / 0.407 — high variance, never reproduces 0.427
- v19 same seed as v18_33333 got 0.339 (PFSP stochasticity)

This is consistent with US-side learning being *noise-driven* rather than
signal-driven: the gradient on US states is so attenuated that whether US WR
improves or degrades in a given iter is dominated by sampling variance. The
"good" v13 iter20 is where the noise happened to align favorably — there is
no mechanism pulling the model back to that state.

## Root Cause

**The value head learns that US states are losing states, and UPGO turns that
pessimism into silenced policy gradient on the US side. The faulty `us_win_w`
weighting accelerates the value head's US-side pessimism. Per-side advantage
normalization cannot rescue this because normalization divides by σ — it does
not restore gradient *magnitude* to match the USSR side's signal.**

The PFSP pool imbalance (§4) and step count imbalance (§3) are contributing
factors but not the primary driver. The primary drivers are the interaction
of `us_win_w` semantics + UPGO + low US WR.

## Concrete Fix Recommendations (ranked by expected impact)

### P0 — Fix `us_win_w` semantics or remove it (IMMEDIATE, 5-line change)

**Option A (safest): remove the weighting entirely.** Revert both lines to
`value_loss = F.mse_loss(values_b, batch_returns)`. The memory claim that it
fixes US value calibration does not match the code.

**Option B (intent-preserving): weight by side-win state.** If the memory's
actual goal is to upweight US-win states:
```python
# in pack_steps, carry side_int into PackedSteps
side_ints_b = packed.side_ints.index_select(0, idx)
is_us_win = (side_ints_b == 1) & (returns > 0)
us_win_w = torch.where(is_us_win, 2.0, 1.0)
value_loss = (us_win_w * (values - returns) ** 2).mean()
```

**Option C (recommended first pass): weight by US side regardless of win/loss.**
```python
us_side_w = torch.where(side_ints_b == 1, 2.0, 1.0)
```

Test: warmstart from v13 iter20, 20 iters, measure US WR trajectory.
Expected: US WR stops dropping within 5 iters, may recover some.

### P1 — Disable UPGO for US-side runs (IMMEDIATE, 1-arg change)

In `apply_upgo_advantages`, skip UPGO on the side that is behind:
```python
if len(sides) > 1:
    # In mixed-side segments, only apply UPGO to the leading side
    # to preserve raw GAE gradient on the lagging side.
    ussr_wr = ...  # from last iter's rollout_wr_ussr
    us_wr   = ...
    for target_side in [0, 1]:
        side_steps = [s for s in seg if s.side_int == target_side]
        if (target_side == 1 and us_wr < 0.30) or (target_side == 0 and ussr_wr < 0.30):
            continue  # keep GAE advantage
        _apply_upgo_to_segment(side_steps, gamma)
```

Faster alternative: launch one control run with `--upgo=false` from v13 iter20
warmstart, 20 iters. If US WR survives, UPGO is confirmed as primary
amplifier.

### P2 — Oversample US-side steps in PPO minibatch (10-line change)

In `ppo_update_packed`, instead of a uniform random permutation, stratified
sampling by side:
```python
us_idx  = (packed.side_ints == 1).nonzero(as_tuple=True)[0]
ussr_idx = (packed.side_ints == 0).nonzero(as_tuple=True)[0]
# Match: each minibatch has 50/50 US/USSR by resampling US
n_mb = max(len(us_idx), len(ussr_idx)) * 2
perm_us   = us_idx[torch.randint(0, len(us_idx), (n_mb//2,), device=device)]
perm_ussr = ussr_idx[torch.randint(0, len(ussr_idx), (n_mb//2,), device=device)]
perm = torch.cat([perm_us, perm_ussr])[torch.randperm(n_mb, device=device)]
```

Gives the US side 50% of the gradient mass per minibatch, matching game-count
balance.

### P3 — Launch separate `--side us` and `--side ussr` rollout + update passes

The user's question #4. This is a structural fix that cleanly decouples the
sides. Two options:

**P3a: Sequential.** Each iter does a USSR-only 100-game rollout + update,
then a US-only 100-game rollout + update. Separate optimizer param groups?
No — shared model, shared optimizer, but two update passes per iter.

**P3b: Alternating epochs.** `--side ussr` for 10 iters, then `--side us` for
10 iters, alternating. Preserves existing code path (already supported by
the `args.side` flag).

P3 is a heavier change than P0/P1/P2. Try them first.

### P4 — Force per-opponent side balance in PFSP pool

In `sample_K_league_opponents`, after selection, check that every opponent
seen has at least `min_per_side=10` games on BOTH sides before letting PFSP
weight-down in favor of "hardest" matchups. Cheapest hack: during iter < 20,
override selection to be uniform over fixtures.

Expected impact: lower variance across runs, not a direct fix for US
degradation.

### P5 — Add diagnostic logging (NOW, 2-line change)

To validate §3 and attribute future regressions:
```python
log_dict["n_steps_ussr"]  = sum(1 for s in all_steps if s.side_int == 0)
log_dict["n_steps_us"]    = sum(1 for s in all_steps if s.side_int == 1)
log_dict["returns_ussr_mean"] = np.mean([s.returns for s in all_steps if s.side_int == 0])
log_dict["returns_us_mean"]   = np.mean([s.returns for s in all_steps if s.side_int == 1])
log_dict["values_ussr_mean"]  = np.mean([s.value  for s in all_steps if s.side_int == 0])
log_dict["values_us_mean"]    = np.mean([s.value  for s in all_steps if s.side_int == 1])
```

Should be added before running P0/P1/P2/P3 experiments so the trajectory is
legible in W&B.

### Suggested experiment sequence (to validate causal ordering)

1. **Control run (confirm current behavior):** v13 iter20 warmstart, identical
   args, 20 iters → should reproduce ~0.33 combined.
2. **P0 only:** remove `us_win_w` → measure US WR drop rate.
3. **P1 only:** `--upgo=false` → measure US WR drop rate.
4. **P0 + P1:** both → if US WR stable, conclusive.
5. **P2 (stratified minibatch):** only if P0+P1 insufficient.
6. **P3 (per-side separate passes):** only as a last resort.

Each run takes ~7 min (20 iters @ 20s/iter + benchmark). Five runs = 35 min
wall clock. Extremely cheap to validate.

## Open Questions

1.  **Is US-side game length actually shorter?** The §3 claim depends on this.
    One log line adds certainty. If USSR:US step ratio is ≤1.2, step
    imbalance is not a driver and P2 won't help much.

2.  **Does the v13 checkpoint have a calibrated US value head, or was it
    already drifting?** Quick check: run v13 iter20 scripted model on 200
    US-side positions and compare mean predicted value vs mean actual outcome.
    If mean value is already more negative than mean return, the v13 starting
    point is compromised and no warmstart from it will be stable.

3.  **Is `reset_optimizer=false` + UPGO + Adam preserving bad USSR-side
    gradient moments?** v13 had `reset_optimizer=true`, v20 has `false`. Adam
    momentum from v13's USSR-dominant updates may be still biasing v20
    gradients toward USSR-favored directions.

4.  **Would `vf_coef` below 0.5 help?** Currently 0.5. If US value head
    overconfidence is the issue, lowering vf_coef → 0.1 reduces value
    gradient's pull on shared features. Very cheap to test.

5.  **Is the self-slot's "both" mode causing interference?** Self-play
    gradients on both sides share the same 66 games. In a game where the model
    (as USSR) crushes itself (as US), the USSR-side steps get positive
    advantage and US-side steps get negative advantage on the same shared
    features. Over many such games, the policy learns "state X is good for
    USSR" but the representation is tied to the same state X for US. This is
    the standard self-play symmetry issue. Worth checking whether the
    `self-slot` should be ussr-only and us-only (two slots instead of one
    two-sided slot).
