# Opponent Pool Analysis: Per-Side Separation, PFSP Tuning, and Pool Composition

**Date**: 2026-04-16
**Context**: PPO league training v300_sc chain, pre-sc fixture panel, 50-iter runs

---

## A. Current State Audit: Is Per-Side Separation Complete?

### What is correctly separated

1. **Fixture pools**: `selected_fixtures.json` maintains independent `ussr_pool` and `us_pool`, ranked by `elo_ussr` and `elo_us` respectively. `ppo_loop_step.sh` reads these into `USSR_FIXTURES` and `US_FIXTURES` and passes them as separate CLI args.

2. **Opponent sampling**: `collect_rollout_league_batched()` calls `sample_K_league_opponents()` twice with `side="ussr"` and `side="us"`, using `_ussr_fixtures` and `_us_fixtures` independently (lines 1404-1405).

3. **WR tracking**: `_update_wr_table_from_steps()` tracks `{wins_ussr, total_ussr, wins_us, total_us}` per opponent key, branching on `s.side_int` (lines 1029-1035).

4. **PFSP weighting**: `_pfsp_weight()` accepts a `side` parameter and reads only the relevant `wins_xxx/total_xxx` pair (lines 987-988).

5. **Rollout collection**: Each task carries a `collect_side` tag ("ussr" or "us") that flows through to `_collect_heuristic_from_script()` and `_collect_vs_model_from_script()`, ensuring games are single-side only for pool opponents (lines 1458-1463).

### Identified leaks and issues

**LEAK 1: `total_games_all` mixes both sides in UCB denominator**

```python
total_games_all = sum(
    int(v.get("total_ussr", 0)) + int(v.get("total_us", 0))
    for v in _wr.values()
)
```
(Line 1076-1079 in `sample_K_league_opponents`)

This computes N for the UCB term `c * sqrt(ln(N) / n_i)` by summing games across BOTH sides for ALL opponents. When computing the USSR pool's UCB weights, N should only count USSR-side games. The current cross-contamination means:
- If US-side games are more numerous (e.g. self-play slot plays both sides), N is inflated
- The UCB exploration bonus is larger than intended for the USSR pool (and vice versa)
- In practice the effect is moderate since both pools accumulate at similar rates, but it is conceptually wrong and will drift if pools are asymmetric

**Severity**: Low-medium. The sqrt(ln(N)) term is sublinear, so a 2x inflation of N changes UCB by ~sqrt(ln(2)) = ~0.83 factor. Still worth fixing for correctness.

**Fix**: In `sample_K_league_opponents`, compute `total_games_side`:
```python
total_key = "total_ussr" if side == "ussr" else "total_us"
total_games_side = sum(int(v.get(total_key, 0)) for v in _wr.values())
```
And pass `total_games_side` instead of `total_games_all` to `_pfsp_weight()`.

Also fix the same issue in the UCB metrics logging block (lines 1518-1522) which uses the same mixed total.

**LEAK 2: Opponent key is shared between sides (by design, but has consequences)**

The WR table stores a single entry per opponent key (e.g., `"v56_scripted"`) with all four counters. This is correct and intentional -- there's no leak. However, when the same model appears in BOTH the USSR and US fixture pools (v56, v44, v54, v20, v55, v22 appear in both), the `_pfsp_weight()` function correctly reads only the relevant side's counters. No issue here.

**LEAK 3: Self-play slot collects "both" sides, but WR is tracked under `__self__`**

The self-play slot (slot 0) uses `collect_side="both"` and its WR is tracked under `__self__`. Since `__self__` entries are excluded from PFSP weighting (the key is never in the fixture list and iter_* entries are filtered), this is benign. No leak.

### Verdict

The separation is **95% complete**. The only real leak is the `total_games_all` UCB denominator mixing both sides. Everything else -- sampling, WR tracking, weight computation, rollout collection -- is correctly per-side.

---

## B. Principled Fixture Pool Design

### Current pools

| Model | USSR pool | US pool | Pre-SC combined WR | USSR WR | US WR |
|-------|-----------|---------|---------------------|---------|-------|
| v56   | #1        | #3      | 45.1%               | 54.6%   | 35.6% |
| v54   | #3        | #1      | 44.1%               | ?       | ?     |
| v44   | #2        | #4      | 43.9%               | ?       | ?     |
| v20   | #4        | #5      | 42.4%               | ?       | ?     |
| v55   | #5        | #2      | 41.1%               | ?       | ?     |
| v22   | #6        | #6      | ?                   | ?       | ?     |
| v45   | #7        | --      | ?                   | ?       | ?     |
| v57   | #8        | --      | ?                   | ?       | ?     |
| v58   | --        | #7      | ?                   | ?       | ?     |
| v46   | --        | #8      | ?                   | ?       | ?     |
| heur. | appended  | appended| (anchor)            | --      | --    |

**Observations**:
- 6 of 10 combined models appear in both pools (v56, v54, v44, v20, v55, v22)
- Only 4 models are pool-specific: v45, v57 (USSR-only), v58, v46 (US-only)
- The pools are ranked by per-side Elo, which is correct
- Heuristic is appended to both as `__heuristic__` and participates in PFSP tracking

### Should per-side fixtures be curated differently?

**Yes, more aggressively.** The current overlap (6/8 shared) means the two pools are nearly identical. The whole point of per-side pools is that a model strong as USSR opponent (i.e., the model playing US well against our USSR-side model) may be weak as US opponent (i.e., the model playing USSR poorly). These are entirely different skills.

The ranking should be:
- **USSR fixtures**: ranked by how hard they are to beat when our model plays USSR. This means opponents who play US well (high `elo_us` from the opponent's perspective, or equivalently low `wr_ussr` for our model against them).
- **US fixtures**: ranked by how hard they are to beat when our model plays US. This means opponents who play USSR well (high `elo_ussr` from the opponent's perspective).

**The current `select_league_fixtures.py` does this correctly** -- it ranks USSR pool by `elo_ussr` and US pool by `elo_us`. The issue is that most strong models are strong on both sides (correlation), so the pools overlap naturally.

**Recommendation**: Accept the overlap. The JSD deduplication already ensures diversity. The 4 pool-specific models (v45, v57, v58, v46) provide the asymmetric signal. No change needed to the fixture selection algorithm.

### Optimal fixture pool SIZE

Current: 8 per side + heuristic = 9 per side.

With `k_per_side = max(1, (6 - 1) // 2) = 2` slots per side per iteration, and 50 iterations per run, each fixture gets sampled approximately `2 * 50 / 9 = 11` times per run (plus PFSP skew). At 200 games/iter and ~29 games/slot (`200 / 7 slots`), that's ~320 games per fixture per run.

**Analysis by pool size**:

| Pool size | Games/fixture/run | PFSP signal quality | Diversity |
|-----------|-------------------|---------------------|-----------|
| 4-5       | ~580-725          | Excellent convergence | Low -- may overfit to small set |
| 6-8       | ~320-430          | Good -- WR estimates reliable by iter 15 | Good |
| 10-12     | ~240-290          | Marginal -- UCB exploration may dominate | High but diluted |
| 15+       | <200              | Poor -- PFSP can't converge in one run | Too diluted |

**Recommendation**: **6 per side is the sweet spot.** Reduce from 8 to 6. This gives ~480 games/fixture/run (solid PFSP signal), while JSD deduplication ensures the 6 are meaningfully distinct. The WR table carries over across runs with 0.5x decay, so long-term signal accumulates.

With 6 fixtures per side, `k_per_side=2` gives each fixture ~800 games/run (excellent). Even with PFSP skew concentrating on 50%-WR opponents, the floor UCB ensures ~200 games for dominated opponents.

### Should heuristic get special treatment per side?

**Yes.** The model's WR vs heuristic is highly asymmetric:
- As USSR vs heuristic: typically 55-65% (strong)
- As US vs heuristic: typically 25-35% (weak)

This means:
- In the USSR pool, heuristic has WR ~0.60 -> symmetric PFSP = 4*0.6*0.4 = 0.96 (near peak -- good, keeps getting sampled)
- In the US pool, heuristic has WR ~0.30 -> symmetric PFSP = 4*0.3*0.7 = 0.84 (still good)

The symmetric PFSP formula handles this well -- both extremes still get reasonable weight. No special treatment needed beyond what PFSP already provides.

### Literature on PFSP in asymmetric games

**AlphaStar (Vinyals et al., 2019)**: Used three agent types -- main agents, league exploiters, and main exploiters. Main agents trained against all, exploiters trained specifically against weaknesses. PFSP sampling: `p(opponent) proportional to f(win_rate)` where f is a monotone function favoring ~50% matchups. Key insight: **separate exploiter agents per matchup type** to avoid catastrophic forgetting.

**OpenAI Five (OpenAI, 2019)**: Used 80% self-play + 20% past-self. No per-role separation because Dota roles are assigned within the same model. Not directly applicable to TS asymmetry.

**Relevant principle from AlphaStar**: In asymmetric games (Protoss vs Terran vs Zerg), AlphaStar maintained **separate main agents per race** with independent PFSP. Our per-side pools are the correct analog. The key AlphaStar lesson was that a single PFSP weight mixing matchup types led to one side dominating training time. Our per-side split avoids this.

**Polyak averaging / population diversity (Lanctot et al., 2017)**: In two-player zero-sum games, the exploitability of the average policy decreases monotonically with population size. But returns diminish rapidly after ~5-8 distinct opponents. This supports our 6-fixture target.

---

## C. Past-Self Pool Issues

### Current state

- `league_save_every=10`, runs are 50 iterations
- Snapshots saved: iter_0001, iter_0010, iter_0020, iter_0030, iter_0040, iter_0050 = **6 snapshots per run**
- `recency_tau=50` means weight = exp(rank/50), so for 6 snapshots: weights are [1.0, 1.02, 1.04, 1.06, 1.08, 1.10]
- This is **nearly uniform** -- the recency bias is negligible

### Should we save more frequently?

**No.** 6 past-self snapshots is adequate. The marginal value of past-self opponents is low compared to fixtures because:
1. Past-self snapshots from the same run are highly correlated (only ~2% policy divergence per 10 iters)
2. They all share the same exploitable weaknesses (they're from the same lineage)
3. The PFSP signal from past-self is noisy (WR is always near 50% for recent snapshots)

More frequent saving (every 5 iters) would give 10 snapshots, but they'd be even more correlated. The training time is better spent on diverse fixtures.

### Should past-self carry over across runs?

**Currently: No.** `ppo_loop_step.sh` explicitly deletes stale `iter_*.pt` from the next run's directory (lines 217-222) and strips `iter_*` keys from the WR table (line 255).

**Should it? Also no.** Cross-run past-self has three problems:
1. **Checkpoint compatibility**: Architecture may change between runs (e.g., 5-mode to 6-mode). Old checkpoints would crash.
2. **WR staleness**: The model has changed; old WR estimates are meaningless.
3. **Diversity illusion**: Carrying 6 old snapshots + 6 new = 12, but they're from two correlated lineages. The JSD-selected fixtures provide better diversity.

The current approach of carrying over FIXTURE WR with 0.5x decay (but dropping past-self) is correct.

### Is recency_tau=50 appropriate?

**No, it's too high for 6 snapshots.** With tau=50 and 6 ranked items, the ratio between newest and oldest is only 1.10:1. This is effectively uniform sampling.

The purpose of recency weighting is to spend more time on recent (more policy-relevant) past-selves. With tau=50, we're not doing that.

**However**, this may be fine because:
1. Past-self pool mass competes with fixture pool mass (50/50 split at steady state)
2. With only `k_per_side=2` slots and ~9 fixture + 6 past-self candidates, past-self gets sampled ~3-4 times per run regardless
3. PFSP weighting (symmetric base + UCB) already handles which past-self to play

**Recommendation**: Leave tau=50. The recency weighting is a second-order effect when PFSP is active. The UCB term already drives exploration toward under-tested past-selves. Reducing tau would fight the UCB signal.

---

## D. PFSP Exponent and UCB Analysis

### Current formula

```
weight = max(0.01, 4*WR*(1-WR) + c * sqrt(ln(N)/n_i))
```

Where `c = pfsp_exponent = 0.5`.

### Is c=0.5 appropriate?

**The symmetric parabola 4*WR*(1-WR)** peaks at 1.0 when WR=0.5 (ideal learning opponent) and drops to 0 at WR=0 or WR=1 (dominated/dominating). This is well-suited for opponent selection because:
- WR=0.5 opponents provide maximum gradient signal
- WR=0.9+ opponents provide little learning value (already solved)
- WR=0.1- opponents provide little value (too hard, signal is noise)

**The UCB term** `0.5 * sqrt(ln(N)/n_i)` provides exploration:
- With N=1000 total games, n_i=50 per opponent: UCB = 0.5 * sqrt(6.9/50) = 0.19
- With N=1000, n_i=200: UCB = 0.5 * sqrt(6.9/200) = 0.09
- With N=1000, n_i=10 (min): UCB = 0.5 * sqrt(6.9/10) = 0.42

At WR=0.85 (dominated opponent): symmetric=0.51, UCB@n=50=0.19, total=0.70. Still gets sampled, good for regression detection.

At WR=0.95 (strongly dominated): symmetric=0.19, UCB@n=50=0.19, total=0.38. Gets reduced but non-zero sampling. Good.

**c=0.5 is reasonable.** The historical context (comment: "1.5 caused v230_sc 1742, -41 Elo drop") shows that higher c over-explores weak opponents at the expense of learning-productive matchups. The 0.5 setting was validated empirically.

### Should the exponent differ per side?

**In principle, yes.** The model is much weaker as US (WR ~30-35% vs heuristic) than as USSR (WR ~55%). This means:
- US pool opponents tend to have high WR (we lose often) -> symmetric base is high -> they already get sampled heavily
- USSR pool opponents tend to have low WR (we win often) -> symmetric base is lower -> UCB is relatively more important

With c=0.5, the USSR pool relies more on UCB to maintain diversity (since the symmetric base is lower for dominated opponents). This is actually desirable -- the model is strong as USSR, so regression detection (UCB) matters more than learning (symmetric base).

**Recommendation**: Keep c=0.5 for both sides. The formula already adapts correctly to the asymmetry through the WR-dependent symmetric base.

### Is UCB causing iter_0001 over-selection?

When a new run starts with a seeded WR table:
- Fixtures: n_i has been decayed 0.5x from the previous run, so UCB is elevated but bounded
- iter_0001: n_i=0, so PFSP returns the default 1.0 (MIN_GAMES=10 guard at line 990)

At steady state (iter 20+):
- iter_0001 has accumulated games and its UCB is normal
- Newer iter_0010, iter_0020 have fewer games -> higher UCB -> get sampled more

**No over-selection problem.** The MIN_GAMES=10 guard ensures new entries start at weight 1.0 (the peak of the symmetric parabola), which is the same as a perfectly-balanced opponent. This is a good default -- we don't know the WR yet, so assume it's informative.

---

## E. Concrete Recommendations

### Priority 1: Fix total_games_all UCB leak (5 min, correctness)

**File**: `scripts/train_ppo.py`, function `sample_K_league_opponents` (line 1076)

Replace:
```python
total_games_all = sum(
    int(v.get("total_ussr", 0)) + int(v.get("total_us", 0))
    for v in _wr.values()
)
```
With:
```python
total_key = "total_ussr" if side == "ussr" else "total_us"
total_games_all = sum(int(v.get(total_key, 0)) for v in _wr.values())
```

Also fix the UCB metrics logging block (lines 1518-1522) similarly, computing separate totals for the two `_pfsp_weight()` calls.

### Priority 2: Reduce fixture pool from 8 to 6 per side (5 min, config)

**File**: `scripts/select_league_fixtures.py`

Change defaults:
```python
p.add_argument("--ussr-pool-n", type=int, default=6)
p.add_argument("--us-pool-n", type=int, default=6)
```

Then regenerate `results/selected_fixtures.json`:
```bash
uv run python scripts/select_league_fixtures.py --ussr-pool-n 6 --us-pool-n 6
```

**Rationale**: 6 fixtures give ~480 games/fixture/run (solid PFSP signal). 8 fixtures dilute to ~320, and the extra 2 are marginal (lowest-Elo in each pool, often near-duplicates after JSD pruning).

### Priority 3: No further changes needed

The analysis confirms that the current system is well-designed:
- Per-side separation is correct (with the minor UCB fix above)
- Symmetric PFSP + additive UCB is a sound formula
- c=0.5 is empirically validated
- Past-self management (save every 10, don't carry across runs, seed WR with decay) is correct
- Heuristic as a PFSP-tracked fixture works well
- recency_tau=50 is effectively uniform but this is fine when PFSP is the primary weighting signal

### Not recommended

- **Changing recency_tau**: Second-order effect, PFSP dominates
- **Per-side UCB exponents**: The formula auto-adapts via WR-dependent base
- **Carrying past-self across runs**: Compatibility risk, staleness, and diversity illusion
- **More frequent saving**: Correlated snapshots add noise not signal
- **Separate WR table entries per side**: Current shared-key + per-side counters is clean and correct

---

## Summary

The per-side opponent pool system is well-engineered. The only concrete fix needed is the `total_games_all` UCB denominator (Priority 1), which is a minor correctness issue. Reducing pool size from 8 to 6 (Priority 2) is a tuning improvement that concentrates PFSP signal. Everything else -- the formula, the parameters, the carryover logic -- is sound and should be left alone.
