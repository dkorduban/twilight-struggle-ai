---
# Opus Analysis: Breaking the Elo 2110 Plateau — Harder Opponents and League Redesign
Date: 2026-04-11T04:00:00Z
Question: How to break through the Elo ~2110 plateau? Why not use ALL previous versions as opponents? What opponent sampling strategies could provide harder/more useful training signal? Is the current PFSP implementation optimal?

## Executive Summary

The Elo plateau at ~2110 is not primarily a league/opponent problem — it is a **training signal quality problem** exacerbated by league design. The v45 paradox (lowest rollout WR = highest Elo) reveals that training against harder opponents produces better generalization even though it produces worse in-training metrics. The current league is too narrow (3 fixtures + self-play within one run's checkpoints), too shallow (only 80 iterations of self-play history per run), and suffers from a critical structural flaw: **each run starts with an empty league pool**, so early iterations train against fixtures only, and late iterations train in a self-play echo chamber. Adding all available scripted versions (v8-v22, v44-v52) as permanent fixtures would be the single highest-impact change: it transforms the league from a narrow 3-opponent + self-play system into a proper 15+ opponent ladder spanning 200 Elo. The key code change is trivial — add more paths to `--league-fixtures` — but the PFSP weighting needs adjustment to handle a larger, more diverse pool.

## Findings

### 1. The v45 Paradox: Low Rollout WR = High Elo

v45 had the lowest rollout win rate (~0.39-0.44) among v44-v53 but achieved the highest Elo (2108). Later runs (v46-v53) achieved higher rollout WRs (0.45-0.55) but lower Elo. This is the central diagnostic clue.

**Explanation:** v45 inherited its checkpoint from v44/iter0020, which was the best checkpoint from v44's confirmation tournament. This checkpoint was strong because it was trained for only 20 iterations — not enough time to overfit to its league pool. When v45 ran its 80 iterations with PFSP, it faced a diverse pool (fixtures v8/v14/v22 + heuristic + its own evolving checkpoints). The low rollout WR means v45's opponents were hard relative to its current strength — this is exactly the regime where learning is most efficient.

By contrast, v46 onward inherit from the previous run's ppo_best.pt, which is typically iter 10-20 of that run. But each successive run's league pool resets to empty, so iterations 1-10 face only fixtures (easy opponents → high WR, low learning). By the time the pool fills up (iter 20+), the model has already drifted toward exploiting easy opponents. The rollout WR is higher but the training signal is worse.

### 2. The League Pool Resets Every Run — This Is the Core Problem

Looking at the launch script (`ppo_loop_step.sh` line 226-233):

```
if [ -d "$NEXT_DIR" ]; then
  STALE_COUNT=$(ls "${NEXT_DIR}"/iter_*.pt 2>/dev/null | wc -l)
  if [ "$STALE_COUNT" -gt 0 ]; then
    rm -f "${NEXT_DIR}"/iter_*.pt "${NEXT_DIR}"/iter_*_scripted.pt
  fi
fi
```

Each new run (v46, v47, ...) starts in a fresh `NEXT_DIR` with zero `iter_*.pt` files. The `sample_K_league_opponents` function (line 970-976) only searches the run's own league directory for `iter_*.pt`:

```python
for p in sorted(Path(league_dir).glob("iter_*.pt")):
    m = re.search(r"iter_(\d+)\.pt$", str(p))
```

This means:
- **Iteration 1**: Pool = 0 past-self checkpoints. Only fixtures + heuristic available.
- **Iteration 10**: Pool = 1 past-self (iter_0001). Mostly fixtures.
- **Iteration 40**: Pool = 4 past-self checkpoints. Starting to get some self-play signal.
- **Iteration 80**: Pool = 8 past-self checkpoints. Only the last 70 iterations of THIS run.

The model never trains against checkpoints from previous runs (v44, v45, v46...) during rollouts — only during Elo tournaments after each run completes. This is a massive waste of available opponent diversity.

### 3. Available Scripted Checkpoints: A Rich Opponent Pool Going Unused

From the scripted_for_elo directory, 23 usable checkpoints exist:

| Version | Elo | Era | Notes |
|---------|-----|-----|-------|
| v8 | 1913 | BC baseline | Weakest non-heuristic |
| v9 | 1948 | | |
| v10 | 1952 | | |
| v11 | 1977 | | |
| v12 | 2004 | | |
| v13 | 2000 | | |
| v14 | 2015 | Anchor | Mid-ladder |
| v15 | 2053 | | |
| v16 | 2040 | | |
| v17 | 2065 | | |
| v18 | 2058 | | |
| v19 | 2076 | | |
| v20 | 2079 | | |
| v21 | 2088 | | |
| v22 | 2097 | Pre-corruption best | Frontier fixture |
| v27-v41 | 1689-1888 | CORRUPTED | Exclude permanently |
| v44 | 2107 | Post-restart | Near-frontier |
| v45 | 2108 | Current best | Near-frontier |
| v46 | 2108 | | Near-frontier |
| v47 | 2103 | | Near-frontier |
| v48 | 2104 | | Near-frontier |
| v49 | 2089 | | Slight regression |
| v50 | 2074 | | Regression |
| v51 | 2014 | | Major regression |
| v52 | 1996 | | Major regression |

Excluding v27-v41 (corrupted) and heuristic, there are **20 usable scripted opponents** spanning Elo 1913-2108. Currently only 3 are used as fixtures (v8, v14, v22). The rest sit on disk unused during training.

### 4. Why the Current PFSP Implementation Is Suboptimal

**Problem A: Recency vs PFSP conflict.** The weight formula is `recency_w * pfsp_w` where `recency_w = exp(rank / tau)`. With tau=50 and 8 checkpoints (saved every 10 iters in an 80-iter run), the most recent checkpoint gets `exp(8/50) = 1.17x` the oldest — this is mild. But the problem is that ALL 8 past-self checkpoints are from the SAME run, trained from the SAME starting point, and thus very similar in style. PFSP between near-identical opponents adds noise, not signal.

**Problem B: WR table does not persist across runs.** The WR table is stored in `{league_dir}/wr_table.json`. Since each run uses a new `league_dir`, the WR table starts empty. PFSP has no WR data for the first ~20 games against each opponent, defaulting to WR=0.5 (uniform sampling). By the time WR estimates stabilize (iter 30+), the run is nearly half done.

**Problem C: PFSP exponent=1.0 is too mild with a small pool.** With only 4-8 opponents, the difference between WR=0.4 and WR=0.6 opponents is (1-0.4)^1 / (1-0.6)^1 = 0.6/0.4 = 1.5x. The hard opponent gets sampled only 50% more often. With exponent=2.0, it would be 0.36/0.16 = 2.25x. With a small pool, stronger prioritization helps.

**Problem D: Self-slot consumes 25% of games with no external signal.** Slot 0 is always the current model playing itself. With k=4, that is 50 games/iter of pure self-play. These games provide gradient signal only to the extent the model can beat itself — which converges quickly to 50/50. The self-play slot made sense when the pool was empty (v44 era), but now that 20+ external opponents are available, dedicating 25% to self-play is wasteful.

### 5. The Confirmation Tournament Data Reveals Rapid Intra-Run Degradation

From v45's confirmation tournament (80 iterations saved every 20):
```
iter0020: Elo=1933 (WINNER — note: internal Elo, different scale from global)
iter0040: Elo=1925
iter0100: Elo=1845
iter0060: Elo=1839
iter0180: Elo=1840
```

From v50's confirmation tournament (80 iterations saved every 10):
```
iter0010: Elo=2085 (WINNER)
iter0030: Elo=2084
iter0020: Elo=2076
iter0040: Elo=2076
iter0050: Elo=2051
iter0070: Elo=2038
iter0060: Elo=1958 (!)
```

In both cases, the best checkpoint is from the first 10-20 iterations, and the model degrades by 50-130 Elo by the end of the run. This pattern is consistent across v44-v52.

The degradation has a clear cause: the early iterations train against diverse external opponents (fixtures), while later iterations increasingly train against the model's own (degrading) checkpoints. It is a self-reinforcing collapse. The model gets weaker → its saved checkpoints are weaker → it trains against weaker opponents → it gets weaker.

### 6. Why Adding All Previous Versions as Opponents Would Help

**The user's intuition is exactly right.** Adding all available scripted versions as permanent fixtures would:

1. **Provide a stable external signal throughout each run.** Instead of facing only v8/v14/v22 for the first 10 iterations then increasingly facing its own checkpoints, the model would face a ladder of 15-20 opponents at every iteration.

2. **Prevent the self-play echo chamber.** With 20 fixture opponents and k=4 slots (plus self-play in slot 0), at least 2-3 of the 4 opponents per iteration would be external. The model cannot drift into an echo chamber.

3. **Provide a natural difficulty curriculum.** Opponents range from heuristic (~1737) to v45 (~2108). PFSP would automatically focus on opponents near the current model's strength — the ones it wins ~40-60% against. Easy opponents (v8, v9) would get low PFSP weight. Very hard opponents (v45, v46) would get high weight.

4. **Exploit the v45 paradox.** v45 succeeded because it faced hard opponents and had low rollout WR. Adding v44-v52 as fixtures ensures every future run faces frontier-strength opponents throughout training, not just in the first 10 iterations.

5. **The cost is zero.** The games are already being played (200 games/iter). The only change is which opponents are selected, not how many games are played.

### 7. Recommended Opponent Sampling Strategy: Tiered PFSP with Full Historical Pool

The current `sample_K_league_opponents` should be restructured:

**Tier 1 — Frontier fixtures (v44, v45, v46):** The model's primary training opponents. These are near its own strength and provide the strongest gradient signal. PFSP weight should be high.

**Tier 2 — Mid-ladder fixtures (v15-v22):** Strong opponents that the model should beat consistently. If the model starts losing to these, PFSP surfaces them as high-priority.

**Tier 3 — Weak fixtures (v8-v14, heuristic):** Baseline opponents. Should receive low PFSP weight because the model beats them easily. Their main role is preventing catastrophic regression (if the model starts losing to v8, something is seriously wrong).

**Tier 4 — Intra-run self-play (iter_*.pt):** Past checkpoints from the current run. Useful for style diversity but should not dominate.

The current system has no tier structure — all opponents compete in one flat pool with recency weighting that biases toward Tier 4 (intra-run checkpoints).

### 8. The Elo Plateau Is Also Partially a Hyperparameter Problem

Even with optimal opponent selection, the following factors contribute to the plateau:

**a) Entropy is too high for a mature policy.** v44 entropy increased from 4.08 to 4.54 over its run. The model is being pushed toward uniformity. The ent_coef decay from 0.01 to 0.003 (v46+ config) partially addresses this but may not be aggressive enough.

**b) PPO epochs = 4 may be insufficient.** With 200 games/iter producing ~3000-5000 steps, and minibatch_size=2048, each PPO epoch does 1-2 gradient steps. More epochs (6-8) would extract more learning from each rollout batch, which matters more when rollout games are expensive.

**c) The value function is a bottleneck.** With 300 steps per game and purely terminal reward, the value function must propagate signal through a very long chain. The shared trunk means value gradients interfere with policy features. UPGO helps (already enabled) but is a band-aid.

**d) The US-side asymmetry persists.** US WR is 28-35%, USSR WR is 50%+. The model is almost as weak on US side as it was at v22 era. Targeted improvement here could yield 20-40 Elo.

### 9. What the Research Literature Says About Opponent Diversity

**OpenAI Five (2018):** Used a single past version (latest minus N minutes of training) as opponent. Found that N too small → policy cycling, N too large → stale opponents. The key insight: the opponent should be "close but not identical" in strength.

**AlphaStar (2019):** Full league with 3 agent types. Main agents prioritized opponents via PFSP. The key finding: **without league diversity, main agents converged to a narrow Nash equilibrium of the current population** — exactly what we observe with our intra-run-only self-play.

**Fictitious Self-Play theory (Heinrich & Silver, 2016):** FSP converges to Nash equilibrium when the agent trains against the FULL historical average of past policies. In practice, PFSP approximates this by weighting the historical policies by difficulty. The critical requirement: **the historical pool must be large enough to prevent cycling.**

Our pool of 20 scripted historical opponents satisfies this requirement. Using only 3 fixtures does not.

### 10. Implementation Plan: Adding All Versions as Fixtures

The code change is minimal. In `ppo_loop_step.sh`, the fixture list is hardcoded:

```bash
WEAKEST_FIXTURE="data/checkpoints/scripted_for_elo/v8_scripted.pt"
MID_FIXTURE="data/checkpoints/scripted_for_elo/v14_scripted.pt"
FRONTIER_FIXTURE="data/checkpoints/scripted_for_elo/v22_scripted.pt"
```

**Option A — Add all as fixtures directly:**
```bash
FIXTURES=""
for scripted in data/checkpoints/scripted_for_elo/v*_scripted.pt; do
  ver=$(basename "$scripted" | sed 's/v\([0-9]*\)_scripted.pt/\1/')
  # Skip corrupted era
  if echo "27 28 29 30 31 32 33 34 35 36 37 38 39 40 41" | grep -qw "$ver"; then continue; fi
  FIXTURES="$FIXTURES $scripted"
done
```

Then pass all to `--league-fixtures $FIXTURES __heuristic__`.

**Concern:** With 20 fixtures and k=4 slots (slot 0 = self), only 3 slots are available for opponent selection per iteration. Each iteration, 3 of 20+ opponents are sampled. Over 80 iterations, the model sees each fixture ~12 times. This is sufficient for PFSP WR estimates (10-game minimum) but the training signal from any individual fixture is thin.

**Mitigation:** Increase k from 4 to 6 or 8. With 200 games/iter and k=6, each opponent gets ~33 games/iter. This costs nothing except slightly more diverse (less focused) training batches. The games_per_opp would drop from 50 to 33, but the total training steps remain the same.

**Option B — Persistent league pool across runs (better long-term):**
Instead of resetting the league directory each run, maintain a persistent `data/checkpoints/league_pool/` directory that accumulates checkpoints across all runs. `sample_K_league_opponents` would read from this persistent pool plus the current run's `iter_*.pt` files.

This is more invasive but eliminates the pool-reset problem entirely.

### 11. The WR Table Should Be Global, Not Per-Run

Currently, each run creates a fresh `wr_table.json` in its own league directory. A global WR table at `data/checkpoints/league_wr_table.json` that persists across runs would:

1. Give PFSP immediate WR estimates for all fixture opponents from the very first iteration.
2. Allow the system to track long-term trends (is the model getting better or worse against v22 over successive runs?).
3. Reduce the "cold start" problem where PFSP defaults to uniform (WR=0.5) for the first 10-20 games against each opponent.

Implementation: In `ppo_loop_step.sh`, pass `--wr-table-path data/checkpoints/league_wr_table.json` instead of letting the code default to `{league_dir}/wr_table.json`. The WR tracking already writes to a single file — just make it a shared one.

## Conclusions

1. **The Elo plateau is caused by a training signal problem, not a model capacity problem.** The model peaks in the first 10-20 iterations of each run when it faces diverse external opponents, then degrades as it increasingly trains against its own near-identical checkpoints.

2. **The league pool resetting every run is the single biggest structural flaw.** Each run starts with zero historical opponents and must rebuild its pool from scratch. By the time the pool is diverse enough, the model has already begun to overfit.

3. **The user's suggestion to add all previous versions as opponents is correct and should be implemented immediately.** There are 20 usable scripted checkpoints (v8-v22 excluding corrupted, v44-v52) spanning 200 Elo. Currently only 3 are used as fixtures. Adding all of them transforms the league from a narrow system into a proper opponent ladder.

4. **The v45 paradox (low rollout WR = high Elo) confirms the theory.** Training against hard opponents that you lose to produces better generalization than training against easy opponents that you beat. PFSP should be pushing the model toward harder opponents more aggressively.

5. **PFSP exponent should increase from 1.0 to at least 2.0 given the small pool size.** With 20 opponents, linear PFSP barely distinguishes easy from hard. Quadratic PFSP provides meaningful concentration on the hardest opponents.

6. **The self-play slot (25% of all games) is wasteful when 20+ external opponents are available.** Consider reducing it to 1 of k=6 slots (17%) or removing it entirely now that frontier-strength opponents (v44-v46) exist in the fixture pool.

7. **The WR table should persist across runs.** Currently PFSP has no memory between runs, spending the first 20-30 iterations of each run with uninformed uniform sampling. A global WR table gives PFSP warm-start data from the first iteration.

8. **Even with optimal opponents, auxiliary fixes are needed:** lower entropy coefficient faster, add more PPO epochs per iteration, and investigate the US-side weakness as a separate Elo lever.

9. **The current within-run degradation pattern (peak at iter 10-20, lose 50-130 Elo by iter 80) suggests the runs should be shortened further or early-stopped more aggressively.** Alternatively, fixing the opponent pool issue may extend the useful training window because the model would face external signal throughout.

10. **The degradation from v49 onward (2089 → 2074 → 2014 → 1996) shows compounding regression across runs.** Each run's ppo_best.pt is the starting point for the next run; if it is itself slightly degraded, the next run starts from a weaker base. The lineage from v45 → v52 has lost ~110 Elo. **Urgently reset the next run's checkpoint to v45's ppo_best.pt, not v52's.**

## Recommendations

### Immediate (before next run launch)

1. **Reset the lineage to v45.** Create `results/checkpoint_override_v54.txt` containing the path to v45's ppo_best.pt. The v49-v52 regression is compounding and must be interrupted.

2. **Add all usable scripted versions as fixtures.** Replace the 3-fixture list with all of: v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v44, v45, v46, v47, v48, heuristic. This is 21 opponents. Exclude v49-v52 (regressed) and v27-v41 (corrupted).

3. **Increase league-mix-k from 4 to 6.** With 20+ fixture opponents, k=4 is too few to sample the pool effectively. k=6 gives 5 non-self slots, each getting ~33 games. Total games remain 200.

4. **Make the WR table path persistent across runs.** Use a global path like `data/checkpoints/league_wr_table.json`. Pass it via `--wr-table-path` in `ppo_loop_step.sh`.

### Short-term (for next 2-3 runs)

5. **Increase pfsp-exponent to 2.0.** Concentrates training on the hardest opponents in the pool. With 20+ opponents, linear PFSP is too diffuse.

6. **Remove the self-play slot (--no-league-self-slot).** True self-play is now redundant because the fixture pool contains near-identical-strength opponents (v44-v46). The model gets more signal from playing v45 (a fixed policy it might find weaknesses in) than from playing a copy of itself (which changes every iteration).

7. **Increase PPO epochs from 4 to 6.** Extract more learning from each rollout batch. With k=6 and 200 games, each opponent contributes only ~33 games. More gradient steps per batch compensates.

8. **Reduce entropy coefficient decay range to 0.008 → 0.002.** The current 0.01 → 0.003 may still be too high for a policy at Elo 2108. The model needs to sharpen, not explore.

### Medium-term (after validating the above)

9. **Implement persistent league pool across runs (Option B from Finding 10).** Instead of fixtures, maintain a single league_pool directory that accumulates checkpoints from all runs. This eliminates the pool-reset problem and the need to manually curate the fixture list.

10. **Add a "hard opponent" meta-slot.** One of the k slots should always be the single opponent with the lowest WR (highest PFSP weight), regardless of other sampling logic. This ensures the model always faces its worst matchup every iteration.

11. **Investigate US-side weakness as a targeted intervention.** The US WR of 28-35% vs frontier opponents is a ~20 Elo drag. Consider: asymmetric training (more US games), US-specific value head, or US-weighted entropy bonus.

12. **Consider adding v49-v52 back as fixtures once the model surpasses Elo 2120.** These regressed checkpoints represent different policy "styles" that might expose novel weaknesses. But they should not be added now while the model is still at the same Elo range — they would dominate PFSP with misleadingly high weights.

## Open Questions

1. **Does the C++ rollout support more than 6-8 concurrent opponents efficiently?** With k=6 and n_workers=1, the games run sequentially in 6 batches. With n_workers>1, they can parallelize. What is the GPU memory impact of k=6 vs k=4?

2. **Should regressed checkpoints (v49-v52) be used as fixtures?** They are weaker than the starting checkpoint but represent distinct policy styles. PFSP would give them low weight (model wins easily), but they might occasionally surface exploitable patterns. Verdict: probably not now, revisit later.

3. **What is the optimal k for a 20-opponent pool?** k=6 means 5 external opponents per iteration, each getting 33 games. k=8 means 7 external opponents, each getting 25 games. Is 25 games enough for meaningful gradient signal? Probably yes — each game produces ~30-50 steps, so 25 games = 750-1250 steps per opponent, which is a decent minibatch.

4. **Should the WR table use windowed or cumulative estimates?** Windowed (last N games) tracks the model's current strength better but has higher variance. Cumulative is more stable but may be stale if the model has improved. A compromise: exponential moving average with decay=0.95 per iteration.

5. **Would MCTS-guided rollouts break the plateau independently of league redesign?** Even 25-50 MCTS simulations per decision would generate higher-quality policy targets. This is likely the single biggest remaining Elo lever after league redesign, but requires C++ implementation work.

6. **Is the v45 → v52 regression purely from the league pool issue, or are there other contributing factors?** The entropy coefficient schedule (identical across v45-v52) and the compounding checkpoint degradation are likely the main factors. But the ent_coef 0.01→0.003 schedule might be decaying too aggressively within each 80-iter run, causing late-run policy collapse. This should be monitored.
---
