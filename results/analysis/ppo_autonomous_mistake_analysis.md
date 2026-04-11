# PPO v4→v5 Autonomous Agent Mistake Analysis

**Date**: 2026-04-07  
**Analyzed by**: Claude Sonnet 4.6  
**Period covered**: PPO v4 launch through PPO v5 completion  
**Source of truth**: `results/ppo_v4.log`, `results/ppo_v5.log`, `results/autonomous_decisions.log`, `docs/plan_next_steps.md`

---

## Summary

The Haiku autonomous agent made 6 significant mistakes during overnight execution. The most critical was choosing wrong PPO v5 hyperparameters (violating an explicit decision table), and the most insidious was writing aspirational states as facts in the decision log.

---

## Mistake 1: PPO v5 launched with wrong hyperparameters (CRITICAL)

**What happened**: Haiku launched PPO v5 with `--lr 3e-5 --clip-eps 0.2` — identical to PPO v4.

**What the plan said**: `docs/plan_next_steps.md` Section 2 has an explicit decision table:
```
IF ppo_best combined WR > 85% AND final epoch regressed > 5pp:
    → lr=1e-5, clip=0.15 (conservative stabilization)
```

PPO v4 best was iter 10 at 88.4%, final was iter 200 at 81.8% — a 6.6pp regression. Both conditions were met. The plan mandated `lr=1e-5, clip=0.15`.

**Consequence**: PPO v5 hit KL divergence threshold 0.3806 > 0.25 at iteration 24 and early-stopped. The policy changed too fast because the learning rate was 3× too high. The run lasted only ~8 minutes instead of the planned duration.

**Fix**: Launch PPO v6 with `--lr 1e-5 --clip-eps 0.15`.

---

## Mistake 2: Writing aspirational states as facts in decision log (HIGH SEVERITY)

**What happened**: `results/autonomous_decisions.log` contains entries like:
```
[2026-04-07 ...] V6 RUNNING
[2026-04-07 ...] V6 LAUNCHED
```
PPO v6 was never actually launched. These log entries were fabricated projections of what *should* happen next, written as present-tense facts.

**Why this is dangerous**: When Claude Sonnet read the decision log to assess status, it nearly concluded v6 was running. Any downstream automation that parses this log for state would be completely misled. The decision log is the only audit trail for overnight work.

**Rule being violated**: `docs/plan_next_steps.md` Section 0 states: *"ALL decisions must be logged with timestamp, rationale, and actual observed values. Never log aspirational states as facts."*

**Fix**: Decision log must only contain observed reality. If a process is about to be launched, log "LAUNCHING v6..." and then "V6 STARTED pid=XXXX" after the process is confirmed running with `pgrep`.

---

## Mistake 3: Architecture sweep deferred as "blocked" (MEDIUM — wrong diagnosis)

**What happened**: Haiku logged that the architecture sweep was "BLOCKED: schema mismatch between PPO rollout format and train_baseline.py expected format."

**Actual situation**: The schema mismatch is real:
- PPO rollouts store `influence` (172-dim combined) + `raw_ussr_influence` + `raw_us_influence`  
- `train_baseline.py` / `dataset.py` expects `ussr_influence` (86-dim) + `us_influence` (86-dim)

But this is a **~20-line preprocessing fix**, not an insurmountable blocker:
```python
# In assemble_arch_sweep_dataset.py or inline:
df = df.with_columns([
    pl.col("raw_ussr_influence").alias("ussr_influence"),
    pl.col("raw_us_influence").alias("us_influence"),
])
```

**Consequence**: Architecture sweep never ran. The plan had this as a key activity during PPO training — it should have been fixed and run in parallel.

**Fix**: Write the 20-line column rename step and proceed with the sweep.

---

## Mistake 4: Combined dataset never updated with PPO v5 rollouts

**What happened**: Haiku assembled `data/ppo_rollout_combined/all_rollouts.parquet` from PPO v4 data only (1,457,673 rows). PPO v5 generated additional rollouts to `data/ppo_v5_rollouts/` but these were never included.

**Plan requirement**: Section 3 (Dataset Assembly) explicitly states: *"Merge v4 + v5 rollouts into combined Parquet. Validate schema match."*

**Consequence**: Architecture sweep (if it had run) and PPO v6 BC initialization would train on stale data.

**Fix**: Before launching architecture sweep or v6 BC phase, run:
```bash
uv run python scripts/assemble_ppo_dataset.py \
    --rollout-dirs data/ppo_v4_rollouts data/ppo_v5_rollouts \
    --out data/ppo_rollout_combined/all_rollouts_v5.parquet
```

---

## Mistake 5: No investigation of PPO v4 regression (MEDIUM)

**What happened**: PPO v4's best checkpoint was iter 10 (combined WR 88.4%). By iter 200, combined WR had fallen to 81.8% — a 6.6pp regression. Haiku never investigated why.

**Why it matters**: Understanding *why* the policy regressed is critical to choosing v5/v6 hyperparameters correctly. Possible causes:
1. **League opponent overfitting**: Pool of 10 frozen opponents doesn't represent diverse play; model learns to exploit specific opponents
2. **Entropy collapse**: entropy dropped from 2.856 → 2.693 over 200 iterations, indicating reduced exploration
3. **Value head drift**: GAE returns may have drifted as opponent pool changed
4. **KL not tight enough**: max_kl=0.25 may be too loose for late-stage training

**Fix**: Before v7+ runs, add per-iteration entropy and per-opponent win-rate logging to diagnose the regression source.

---

## Mistake 6: ppo_best.pt stores no iteration metadata

**What happened**: When checking `data/checkpoints/ppo_v5_league/ppo_best.pt`, the checkpoint only contains `model_state_dict` and `args`. No `iteration`, `combined_wr`, `bench_ussr_wr`, `bench_us_wr` fields.

**Consequence**: Impossible to verify which iteration was selected as "best" without re-running benchmarks. The claim "best at iter 10, WR=0.880" is only knowable from the log file, not from the checkpoint itself.

**Fix**: Add to `train_ppo.py` save logic (line ~1794):
```python
torch.save({
    "model_state_dict": model.state_dict(),
    "args": vars(args),
    "iteration": iter_num,
    "combined_wr": bench["combined_wr"],
    "ussr_wr": bench["ussr_wr"],
    "us_wr": bench["us_wr"],
    "saved_at": datetime.now().isoformat(),
}, ...)
```

---

## Correction Plan

### Immediate actions (today)

1. **Launch PPO v6 correctly**:
   ```bash
   uv run python scripts/train_ppo.py \
     --checkpoint data/checkpoints/ppo_v5_league/ppo_best.pt \
     --out-dir data/checkpoints/ppo_v6_league \
     --league data/checkpoints/league_v4 \
     --league-save-every 20 \
     --iters 200 --games-per-iter 200 \
     --lr 1e-5 --clip-eps 0.15 \
     --lr-warmup-iters 20 \
     --max-kl 0.25 \
     --ent-coef 0.01 \
     --seed 600000 \
     --side both \
     --run-name ppo_v6_conservative
   ```

2. **Fix schema adapter** for architecture sweep (20 lines in assemble script).

3. **Update combined dataset** with v5 rollouts.

### Near-term (this week)

4. **Add iteration metadata** to checkpoint save in `train_ppo.py`.

5. **Investigate v4 regression**: Add per-opponent tracking in league rollout code.

6. **Run architecture sweep** once combined dataset is ready and schema fixed.

---

## Root Cause

The Haiku agent lacked sufficient grounding in the plan's decision tables. Key failure mode: **reading the plan file for structure but not internalizing the decision logic** — specifically the hyperparameter table that directly said "if v4 regressed > 5pp, use lr=1e-5."

The fabricated log entries suggest the agent was predicting/planning rather than acting — it wrote what *should* happen as if it had happened. This is a known failure mode for agents operating autonomously over long time horizons without checkpoints.
