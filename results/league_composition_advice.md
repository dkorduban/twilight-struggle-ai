# League Composition Analysis & Recommendations

## 1. Current Setup Summary

**Opponent sampling** (`sample_league_opponent`):
- 15% heuristic (MinimalHybrid, ~1606 Elo, 395 Elo below frontier)
- 85% uniform among top-5 most recent checkpoints in pool

**Pool mechanics**:
- Checkpoints saved every 20 iterations as `iter_NNNN.pt`
- 200-iteration run produces ~10 checkpoints (iter_0001, iter_0020, ..., iter_0200)
- ONE opponent sampled per iteration; all 200 games face that single opponent

**Observed results** (from `elo_full_ladder.json`):
- v4/v5/v6: ~1800 Elo, essentially tied despite sequential training
- v8-v13 Elo gains per generation: +23, +1, +6, +23, +6
- v11/v12/v13 plateau: only +29 Elo across 3 full 200-iteration generations
- Heuristic at 1606, current frontier at ~2007 (401 Elo gap)

---

## 2. Analysis

### Q1: Is restricting to top-5 most recent a good idea?

**Problem**: At 200 iters with save-every-20, the pool has 10 checkpoints. Top-5 means only iters 120-200 are ever sampled. Early-run checkpoints (iter_0001 through iter_0080) are dead weight — never used. The model only trains against copies of itself from the last 80 iterations, which are likely very similar in style.

**What the literature says**: AlphaZero uses a single most-recent opponent (pure self-play). OpenAI Five / AlphaStar use full league pools with diverse historical agents including "exploiters" that specifically target weaknesses. The key insight from AlphaStar is that historical diversity prevents cyclical strategy forgetting — agent A beats B beats C beats A.

**In this setup**: The top-5 restriction combined with only 10 checkpoints means you're sampling from a narrow band of nearly identical policies. This is closer to pure self-play than league play. The whole point of the league is diversity, and top-5-of-10 defeats that purpose.

**Verdict**: Top-5 restriction is actively harmful. It creates a pseudo-self-play echo chamber that likely explains the v4/v5/v6 plateau (all essentially tied) and the v11/v12/v13 deceleration.

### Q2: Should the heuristic stay at 15%?

**Pros of keeping heuristic**:
- Prevents total policy collapse (proven in pre-PPO v11/v12 incident)
- Provides a fixed reference point that doesn't co-evolve
- Forces the model to maintain basic competence against a qualitatively different play style

**Cons at 15%**:
- Heuristic is 401 Elo below frontier — expected WR is ~92%. Learning signal is weak: nearly every game is a win, gradients push toward "beat the heuristic faster" rather than "play better strategy"
- 15% of training budget (~30 games/iter) spent on near-trivial opponents
- The heuristic is deterministic enough that the model can memorize exploits rather than learn general strategy

**What's needed**: An anchor opponent, but not necessarily the heuristic. The oldest league checkpoint serves the same anti-collapse function while being a much closer skill match. However, the heuristic has a qualitatively different play style (rule-based vs learned), which provides policy diversity that no checkpoint can replicate.

**Verdict**: Reduce heuristic to 5-10%. The anti-collapse insurance is valuable but doesn't need 15%. Replace the freed budget with broader league sampling.

### Q3: One opponent per iteration vs mixing per-game

**Current**: One `sample_league_opponent()` call → 200 games vs same opponent.

**Tradeoffs**:

| Aspect | Per-iteration (current) | Per-game (proposed) |
|--------|------------------------|---------------------|
| Gradient variance | Lower (same opponent = correlated games, but consistent gradient direction) | Higher (mixed opponents = diverse gradients, better expected value) |
| Credit assignment | Clear — model sees what works against THIS opponent | Noisy — hard to attribute wins/losses to strategy vs opponent weakness |
| Echo chamber risk | High — if one opponent sampled 3 iters in a row, model overfits to it | Low — every iteration sees the full opponent distribution |
| Implementation | Current code | Trivial change: call `sample_league_opponent()` inside the game loop |
| Batch efficiency | Current C++ batched rollout expects one opponent_path | Need to group games by opponent, call batched rollout per-group |

**The key issue**: With only 10 opponents in the pool and one sampled per iteration, the model can go 5+ iterations seeing the same opponent (17% chance per iter with top-5 uniform). This creates mini echo chambers within a generation.

**Per-game mixing is strictly better for gradient quality**: PPO already batches steps from all 200 games into minibatches — the gradient is already a mixture. But if all 200 games are against one opponent, the "mixture" is monoculture. Per-game mixing makes the minibatch gradient a true mixture over opponent strategies.

**Implementation concern**: The C++ `rollout_model_vs_model_batched` takes a single `model_b_path`. Per-game mixing requires either (a) grouping games by sampled opponent and making multiple batched calls, or (b) modifying C++ to accept per-game opponent paths.

**Verdict**: Switch to per-game sampling. Implementation: sample N opponents for N games, group by opponent, call `rollout_model_vs_model_batched` once per group. Heuristic games go through `collect_rollout_batched` as now. Overhead: one extra TorchScript load per unique opponent per iteration (negligible — already loading one).

### Q4: Is save-every-20 too sparse?

**Current density**: 10 checkpoints in 200 iters. At top-5, only 5 distinct opponents.

**Comparison**: AlphaZero effectively has a new opponent every iteration (latest self). OpenAI Five saves every ~few minutes of wall time. In this setup, 20 iterations = ~20 minutes wall time at 24s/rollout + PPO update. Saving every 10 or every 5 would be 20 or 40 checkpoints — much better coverage.

**Disk cost**: Each checkpoint is a TorchScript model, ~2-4MB. 40 checkpoints = ~160MB per generation. Negligible.

**Quality benefit**: Denser pool means:
- More diverse opponents (captures intermediate strategies during training)
- Better granularity for league sampling
- Smoother Elo progression within a generation

**Verdict**: Save every 10 iterations (20 checkpoints per generation). This doubles pool density at negligible cost. Every-5 (40 checkpoints) is also fine but offers diminishing returns over every-10.

### Q5: Should sampling be prioritized by strength/recency?

**Uniform-among-recent** (current) concentrates mass on near-frontier opponents. This maximizes learning signal per game (strongest opponents push hardest) but reduces diversity.

**Literature**: AlphaStar's "Prioritized Fictitious Self-Play" (PFSP) samples opponents proportional to how much the agent loses to them — not by recency or Elo. This targets the agent's weaknesses automatically. Full PFSP requires tracking win rates against each pool member, which is more infrastructure.

**Simpler alternative — decayed uniform**: Sample with probability proportional to `decay^(rank_from_newest)`. With decay=0.7 and 20 checkpoints:
- Newest 5: ~60% of mass
- Middle 10: ~35% of mass
- Oldest 5: ~5% of mass

This preserves frontier focus while still occasionally sampling old opponents.

**Even simpler — uniform over full pool**: Given the echo chamber diagnosis, the marginal value of diversity outweighs the marginal value of harder opponents. Uniform over all checkpoints is the simplest fix and directly addresses the current problem.

**Verdict**: Start with uniform over the full pool (simplest, maximum diversity). If that works, consider PFSP later. The current plateau is a diversity problem, not a difficulty problem.

---

## 3. Recommended Configuration

```python
def sample_league_opponent(league_dir: str) -> Optional[str]:
    """Sample an opponent from the league pool.
    
    Distribution:
    - 10% heuristic (anti-collapse anchor)
    - 90% uniform over ALL checkpoints in pool (not just top-5)
    
    Called per-game, not per-iteration.
    """
    import random
    pts = sorted(Path(league_dir).glob("iter_*.pt"))
    if not pts:
        return None  # empty pool -> heuristic
    r = random.random()
    if r < 0.10:
        return None  # 10%: heuristic anchor
    return str(random.choice(pts))  # 90%: uniform over FULL pool
```

**League save interval**: `--league-save-every 10` (20 checkpoints per 200-iter run)

**Per-game sampling**: Modify `collect_rollout_league_batched` to sample per-game:

```python
def collect_rollout_league_batched(model, league_dir, n_games, ...):
    # Sample one opponent per game
    opponents = [sample_league_opponent(league_dir) for _ in range(n_games)]
    
    # Group by opponent for batched execution
    groups = defaultdict(list)
    for i, opp in enumerate(opponents):
        groups[opp].append(i)
    
    all_steps = []
    for opp_path, game_indices in groups.items():
        n = len(game_indices)
        if opp_path is None:
            # Heuristic games
            steps = collect_rollout_batched(model, n, ...)
        else:
            # Model-vs-model games
            steps = rollout_model_vs_model_batched(model, opp_path, n, ...)
        all_steps.extend(steps)
    return all_steps
```

**Summary of changes from current**:

| Parameter | Current | Recommended |
|-----------|---------|-------------|
| Heuristic % | 15% | 10% |
| Pool subset | Top-5 most recent | Full pool |
| Sampling granularity | Per-iteration (1 opponent, 200 games) | Per-game |
| Save interval | Every 20 iters (10 checkpoints) | Every 10 iters (20 checkpoints) |
| Sampling distribution | Uniform among top-5 | Uniform over full pool |

---

## 4. What to Try First (Priority Order)

### Priority 1: Full-pool uniform sampling (high impact, 5-minute change)

Change `recent = pts[-5:]` to `recent = pts` in `sample_league_opponent`. This is the single highest-impact change: it immediately doubles or triples the effective opponent diversity. The top-5 restriction is the most likely cause of the v11-v13 plateau.

**Expected effect**: Break the echo chamber. Each iteration's gradient now reflects a broader range of opponent strategies. Should see resumed Elo growth within 1-2 generations.

### Priority 2: Per-game sampling (medium impact, 30-minute change)

Modify `collect_rollout_league_batched` to sample per-game and group into batched calls. This eliminates the "all 200 games against one random opponent" problem that introduces high variance between iterations.

**Expected effect**: Smoother training curves, more consistent Elo gains per generation. Less iteration-to-iteration variance in rollout WR.

### Priority 3: Denser checkpointing (low impact, 1-minute change)

Change `--league-save-every` from 20 to 10. More checkpoints in the pool = finer-grained historical coverage.

**Expected effect**: Marginal improvement in diversity. Most valuable in combination with full-pool sampling (Priority 1).

### Priority 4: Reduce heuristic to 10% (low impact, 1-minute change)

Change `0.15` to `0.10` in `sample_league_opponent`. Frees 5% of training budget from a 401-Elo-below opponent.

**Expected effect**: Small. The heuristic games are nearly free wins that don't contribute much gradient signal. Reducing from 15% to 10% is minor but directionally correct.

### Not recommended yet

- **PFSP / win-rate-based sampling**: Requires tracking per-opponent win rates across iterations. Good idea but premature — uniform-over-full-pool should be tried first.
- **Eliminating heuristic entirely**: The pre-PPO collapse incident makes this risky. Keep at least 5-10% as insurance.
- **Sampling by Elo distance**: Adds complexity with unclear benefit. The pool is small enough (10-20 checkpoints) that uniform sampling gives adequate coverage.

---

## 5. Quantitative Expectations

**Current state**: v11/v12/v13 gained 29 Elo over 3 generations (600 iterations). That's ~5 Elo per 100 iterations — near zero.

**After Priority 1+2**: With full-pool diversity and per-game mixing, a reasonable target is 15-30 Elo per generation (back to the v8->v9 rate of +23 Elo/gen). If gains don't resume within 2 generations, the bottleneck is elsewhere (architecture, reward shaping, exploration noise).

**Diagnostic**: Track the average Elo of sampled opponents per iteration. Currently this clusters tightly around the frontier. After changes, it should spread across the pool range (~1800-2000 Elo). If the model still plateaus against diverse opponents, the problem is capacity or exploration, not opponent diversity.

---

## 6. Follow-up: Cross-run opponents and mini-batch mixing

### Question 1: Should we include prior-generation checkpoints (v1-v13) as permanent league fixtures?

#### Available assets

We have 13 final checkpoints (`data/checkpoints/ppo_v*/ppo_final.pt`) and 10 pre-exported TorchScript models (`data/checkpoints/scripted_for_elo/v*_scripted.pt` for v4-v13). The full Elo ladder from round-robin evaluation:

| Model | Elo | Gap to frontier (v13) |
|-------|-----|-----------------------|
| v13 | 2007 | 0 |
| v12 | 2001 | -6 |
| v11 | 1978 | -29 |
| v10 | 1972 | -35 |
| v9 | 1971 | -36 |
| v8 | 1948 | -59 |
| v7 | 1837 | -170 |
| v4-v6 | ~1800 | ~-205 |
| heuristic | 1606 | -401 |

Key observations from the round-robin match data:
- v8 vs v13: v8 wins 36.5% — still competitive, not trivial
- v7 vs v13: v7 wins 17.5% — weaker but not a washout
- v4 vs v13: v4 wins 23.0% — comparable to v7, still produces meaningful games
- heuristic vs v13: wins 21.5% — only slightly lower than v4-v7 range

This is surprisingly flat. Even v4 (200 Elo below frontier) wins nearly 1 in 4. The Elo gaps translate to much closer win rates than a chess-like model would predict, likely because TS has high variance (card draw, DEFCON incidents, scoring timing). This means even "weak" cross-run opponents still produce non-trivial games with real gradient signal.

#### Analysis

**Arguments for including cross-run opponents:**

1. **Genuinely different play styles.** v4/v5/v6 were trained in different data regimes and developed different strategic tendencies. Within-run checkpoints (iter_020 through iter_200) are minor variations of the same policy. Cross-run opponents provide qualitatively different opposition — the kind that prevents rock-paper-scissors cycling.

2. **Much wider Elo spread.** Current within-run pool spans maybe ~50 Elo (early vs late checkpoints of one generation). Cross-run pool spans 200+ Elo. Wider spread = more diverse difficulty levels = better curriculum.

3. **Directly addresses the v11-v13 echo chamber.** The plateau diagnosis in sections 2-3 above identified narrowness of the opponent pool as the likely cause. Cross-run opponents are the single most effective way to broaden the pool without changing the training procedure.

4. **Free — no extra compute.** These checkpoints already exist. The TorchScript versions are already exported and benchmarked.

5. **Win rates are still informative.** Even v4 wins 23% against v13. These are not heuristic-level blowouts — they produce games where the learner must actually play well to win, and where it sometimes loses and receives useful negative gradient signal.

**Arguments against:**

1. **Risk of wasting budget on easy games.** If v14 is substantially stronger than v13, then v4-v6 become ~80%+ expected WR — approaching heuristic territory. But we already keep the heuristic at 10%, so the incremental waste from a few v4/v5 games is small.

2. **Stale strategies might not transfer.** Old generations may have exploitable habits that the learner memorizes instead of learning general play. However, the same argument applies to within-run checkpoints, and the diversity benefit likely outweighs this.

3. **Pool management complexity.** More checkpoints to track. Mitigated by using the pre-exported `scripted_for_elo/` directory that already exists.

#### Recommendation: Yes, include cross-run opponents. Use Elo-spaced selection, not all of them.

**Which ones to include:**

Do not include all 13. Many are near-duplicates in Elo (v4/v5/v6 within 11 Elo, v9/v10/v11 within 8 Elo). Instead, select representatives spaced ~50-100 Elo apart to maximize diversity per slot:

| Fixture | Elo | Role |
|---------|-----|------|
| heuristic | 1606 | Anti-collapse anchor (existing) |
| v4_scripted | 1807 | Early-gen representative |
| v8_scripted | 1948 | Mid-gen representative |
| v12_scripted | 2001 | Near-frontier representative |

This gives 4 permanent fixtures spanning 400 Elo. As v14+ trains and the frontier moves, v12 stays as a "recent past" fixture and older ones naturally become easier sparring partners — a built-in curriculum.

**Sampling weights for permanent fixtures:**

```
Permanent fixtures (20% total):
  heuristic:    5%    (anti-collapse, qualitatively different)
  v4_scripted:  3%    (early-gen diversity)
  v8_scripted:  5%    (mid-gen, still competitive)
  v12_scripted: 7%    (near-frontier, hardest fixture)

Current-run pool (80%):
  uniform over all within-run checkpoints
```

The 80/20 split ensures that the learning agent primarily trains against its own generation (for frontier-pushing gradient signal) while still facing diverse historical opponents often enough to prevent strategy cycling.

**After each generation completes:** Consider adding the new final checkpoint as a permanent fixture if it is 50+ Elo above the nearest existing fixture. Drop the lowest-Elo non-heuristic fixture if the pool grows beyond 6 permanent entries.

**Implementation:**

```python
# Permanent cross-run fixtures (paths to pre-exported TorchScript models)
PERMANENT_FIXTURES = {
    "heuristic": None,  # sentinel for heuristic path
    "v4": "data/checkpoints/scripted_for_elo/v4_scripted.pt",
    "v8": "data/checkpoints/scripted_for_elo/v8_scripted.pt",
    "v12": "data/checkpoints/scripted_for_elo/v12_scripted.pt",
}
FIXTURE_WEIGHTS = {
    "heuristic": 0.05,
    "v4": 0.03,
    "v8": 0.05,
    "v12": 0.07,
}
# Remaining 80% goes to uniform over current-run pool
```

---

### Question 2: Mini-batch opponent mixing (sample 4-8 opponents per iteration)

#### The proposal

Instead of sampling one opponent for all 200 games (current) or sampling per-game (full per-game mixing from section 3), an intermediate approach: sample K opponents (e.g., 4) at the start of each iteration, run 200/K games against each, concatenate and shuffle all steps, then do one PPO update.

Concretely for K=4, 200 games: sample 4 opponents, run 50 games vs each (4 separate batched C++ calls), shuffle all resulting steps together, PPO update on the shuffled batch.

#### Analysis

**Does this give meaningfully smoother gradient signal vs single-opponent-per-iter?**

Yes, substantially. The core problem with single-opponent-per-iter is that the gradient direction is determined entirely by which opponent was drawn. If opponent A is drawn for 3 iterations in a row (17% chance with 5 opponents), the model's updates are correlated across those iterations. With K=4, each iteration's gradient is a mixture over 4 opponent strategies. This reduces between-iteration variance by roughly a factor of K (variance of a mean of K independent samples = variance/K).

Quantitatively: with K=1, the expected variance in per-iteration gradient direction is proportional to the variance across opponent types. With K=4, it drops to ~25% of that. The PPO update sees a more representative sample of the opponent distribution every single iteration, rather than seeing a noisy single sample.

This is especially valuable early in a generation when the within-run pool is small (1-3 checkpoints) — the permanent fixtures provide immediate diversity from iteration 1.

**Is the batching still efficient?**

Yes. The overhead structure:

| Component | K=1 (current) | K=4 (proposed) |
|-----------|---------------|----------------|
| TorchScript model loads | 1 opponent | 4 opponents |
| C++ batched rollout calls | 1 x 200 games | 4 x 50 games |
| Model export (learning agent) | 1 | 1 (same model for all calls) |
| Total game count | 200 | 200 |

The key question is whether 4 calls of 50 games each is slower than 1 call of 200 games. Looking at the current `rollout_model_vs_model_batched` call: it uses `pool_size=min(n_games, 64)`. So:
- 1 x 200 games with pool_size=64: 64 games run in parallel, 4 waves
- 4 x 50 games with pool_size=50: 50 games run in parallel, 1 wave each, 4 sequential calls

The per-game compute is identical. The overhead is TorchScript loading (one extra load per unique opponent) and call dispatch. TorchScript loads are ~100-500ms each; with 4 opponents, that is an extra ~1-2 seconds per iteration vs a rollout that takes ~24 seconds. Overhead: **~5-8%, negligible.**

If the 4 opponents include some games routed to `collect_rollout_batched` (heuristic), those use a different code path but the same total game count. No efficiency loss.

**Any issues with importance sampling / old_log_prob correctness?**

**No.** This is a critical point that makes mini-batch mixing safe. PPO's importance sampling ratio is `pi_new(a|s) / pi_old(a|s)`, where `pi_old` is the policy that *generated* the action — i.e., the learning agent's policy at rollout time. The opponent's identity does not appear in the importance weight. The `old_log_prob` recorded in each step is the learning agent's own log probability of the action it took, regardless of who the opponent was.

Mixing steps from different opponents is exactly like mixing steps from different games (which PPO already does). The opponent affects the *state distribution* (which states the learner visits), but not the importance weight. Shuffling steps from different opponents before the PPO update is mathematically identical to what would happen if all 200 games happened to visit those states by chance against a single opponent.

One subtlety: the *value function baseline* should ideally condition on opponent strength (stronger opponents = lower expected return from the same state). But in practice, with a small Elo range (within-run checkpoints differ by ~50 Elo), this effect is minor. With cross-run fixtures spanning 400 Elo, the value function will see higher variance in returns from similar states. This could slightly increase GAE variance, but the diversity benefit should dominate. If it becomes a problem, a simple fix is to add an "opponent strength" scalar to the observation (e.g., normalized Elo of the opponent), but this is premature optimization.

**Is there a sweet spot for K?**

| K | Games/opponent | Gradient diversity | Overhead | Notes |
|---|---------------|-------------------|----------|-------|
| 1 | 200 | Minimal (current) | 0 | Status quo |
| 2 | 100 | 2x reduction in variance | ~4% | Minimal improvement |
| 4 | 50 | 4x reduction in variance | ~8% | Sweet spot |
| 8 | 25 | 8x reduction in variance | ~16% | Diminishing returns; 25 games per opponent is getting thin for stable WR estimates |
| 200 | 1 | Maximum | ~50%+ | Per-game; requires per-game grouping; heavy overhead from many small batches |

**K=4 is the sweet spot.** Reasoning:
- 50 games per opponent is enough for reasonable gradient signal from each (~7% WR standard error)
- 4 opponents give substantial diversity without excessive overhead
- With 4 permanent fixtures + current-run pool, K=4 naturally maps to "1-2 fixtures + 2-3 current-run opponents" per iteration
- Going to K=8 cuts games-per-opponent to 25 (noisy per-opponent signal) and adds overhead with diminishing diversity gains

Note: K=4 does **not** mean "always exactly 4 distinct opponents." The sampling procedure should be: draw 4 opponent samples from the distribution (including fixtures). If two draws hit the same opponent, merge those into one larger batch. On average with a pool of ~20+4 opponents, collisions are rare.

**Implementation complexity vs benefit:**

This is simpler than full per-game mixing (from section 3). The implementation:

```python
def collect_rollout_league_batched(
    model, league_dir, n_games, base_seed, device, vp_reward_coef=0.0,
    n_opponents=4,
):
    """Collect rollouts against K opponents, shuffle steps."""
    games_per_opp = n_games // n_opponents
    remainder = n_games % n_opponents

    # Sample K opponents
    opponents = [sample_league_opponent(league_dir) for _ in range(n_opponents)]

    # Group by opponent to batch efficiently
    groups = defaultdict(int)
    for i, opp in enumerate(opponents):
        extra = 1 if i < remainder else 0
        groups[opp] = groups.get(opp, 0) + games_per_opp + extra

    all_steps = []
    seed_offset = 0
    for opp_path, n in groups.items():
        if opp_path is None:
            steps = collect_heuristic_rollout(model, n, base_seed + seed_offset, ...)
        else:
            steps = collect_model_vs_model_rollout(model, opp_path, n, base_seed + seed_offset, ...)
        all_steps.extend(steps)
        seed_offset += n

    random.shuffle(all_steps)  # Mix opponents before PPO update
    return all_steps
```

Complexity: ~20 lines changed in one function. No C++ changes. No new dependencies. The grouping logic handles collisions (two draws hitting the same opponent) automatically by merging their game counts.

#### Recommendation: Yes, implement K=4 mini-batch mixing.

This is the right intermediate step between single-opponent (current) and full per-game mixing (complex). It captures most of the diversity benefit (~4x variance reduction) with minimal overhead (~8%) and trivial implementation complexity.

**Combined recommendation with cross-run fixtures:**

With K=4 opponents per iteration and the sampling distribution from Question 1:
- ~20% of draws hit permanent fixtures (heuristic + v4 + v8 + v12)
- ~80% of draws hit current-run pool checkpoints
- On a typical iteration: expect ~1 fixture opponent + ~3 current-run opponents
- All 4 batches run sequentially (50 games each), steps shuffled, one PPO update

This gives the learner frontier-pushing signal from current-run opponents while maintaining diversity through historical fixtures — exactly the combination needed to break the echo chamber.

---

### Summary of combined recommendations

| Change | Impact | Effort | Priority |
|--------|--------|--------|----------|
| Add 3 permanent cross-run fixtures (v4, v8, v12) | High — 400 Elo diversity span | 10 min (config change) | P1 |
| K=4 mini-batch opponent mixing | High — 4x gradient variance reduction | 30 min (one function rewrite) | P1 |
| Reduce heuristic to 5% (now part of fixture budget) | Low | 1 min | P2 |
| Full-pool uniform for current-run checkpoints | Medium (from original analysis) | 5 min | P1 |

**Implementation order:** Do all four together in one PR — they are complementary and the combined effect is greater than the sum. The cross-run fixtures provide diversity across generations; K=4 mixing ensures each iteration actually samples that diversity; full-pool uniform prevents echo chambers within the current generation.
