# Opus Analysis: PFSP Symmetric UCB Decay Formula Design
Date: 2026-04-12
Question: Design PFSP formula combining symmetric WR weights (bias toward 0.5) + UCB + 0.5/generation decay

## Executive Summary

The current PFSP weight `(1 - WR) + c * sqrt(ln(N)/n_i)` is asymmetric -- it biases toward hard opponents (low WR), which is correct for AlphaStar's exploiter league but wrong for our curated fixture pool where we want maximum learning signal near WR=0.5. The recommended replacement is **Option E with parabolic symmetric base**: `weight = 4*WR*(1-WR) * (1 + c * sqrt(ln(N)/n_i))`, with `c=1.5` (unchanged) and WR decay reduced from 0.7x to 0.5x per generation. This peaks at WR=0.5, symmetrically drops to 0 at extremes, and the multiplicative UCB structure ensures under-explored opponents get boosted proportionally rather than additively (which would overwhelm the symmetric signal for small fixture pools). The 0.5x decay is appropriate because our 30-iteration runs produce meaningful policy shifts that make old WR data unreliable.

## Findings

### 1. Current Implementation Analysis

The current `_pfsp_weight()` at line 929 of `scripts/train_ppo.py`:

```python
exploitation = 1.0 - wr
exploration = pfsp_exponent * math.sqrt(math.log(total_games_all) / total)
return max(0.01, exploitation + exploration)
```

**Key properties:**
- At WR=0.0 (always lose): weight = 1.0 + UCB  (maximum base)
- At WR=0.5 (even match): weight = 0.5 + UCB  (medium base)
- At WR=1.0 (always win): weight = 0.0 + UCB  (minimum base, only UCB keeps it alive)

This creates a strong pull toward opponents we lose to. In AlphaStar's full league with exploiters and main agents, this makes sense because exploiters exist to find weaknesses. In our 4-fixture curated pool (v22, v44, v45, v55), this is suboptimal: if the model beats v22 easily (WR~0.8), v22 correctly gets deprioritized. But if v55 is too hard (WR~0.2), v55 gets maximum weight -- training on games we consistently lose does not produce useful gradients (the model gets no positive reward signal to reinforce).

### 2. Symmetric Base Function Candidates

#### Option A: Parabola `f(WR) = 4 * WR * (1 - WR)`

| WR   | f(WR) | Notes                     |
|------|-------|---------------------------|
| 0.00 | 0.000 | Impossible opponent → 0   |
| 0.20 | 0.640 | Very hard → moderate      |
| 0.35 | 0.910 | Challenging → high        |
| 0.50 | 1.000 | Sweet spot → maximum      |
| 0.65 | 0.910 | Easy-ish → high           |
| 0.80 | 0.640 | Easy → moderate           |
| 1.00 | 0.000 | Trivial → 0              |

**Pros:** Smooth, differentiable, simple. The factor of 4 normalizes the peak to 1.0. Drops off gently -- WR=0.3 and WR=0.7 both still get 84% of peak weight, which is reasonable since these are still useful matchups.

**Cons:** Zero at extremes means a completely-lost fixture gets literally zero weight (before UCB). But the `max(0.01, ...)` floor handles this, and the UCB term will rescue under-explored opponents.

#### Option B: Tent function `f(WR) = 1 - |2*WR - 1|`

| WR   | f(WR) | Notes                     |
|------|-------|---------------------------|
| 0.00 | 0.000 | Same as parabola at extremes |
| 0.20 | 0.400 | Steeper drop than parabola |
| 0.35 | 0.700 |                           |
| 0.50 | 1.000 | Peak                      |
| 0.65 | 0.700 |                           |
| 0.80 | 0.400 |                           |
| 1.00 | 0.000 |                           |

**Pros:** Linear, easy to reason about. Same peak and zeros as parabola.

**Cons:** Non-differentiable at WR=0.5 (kink). Drops off faster than the parabola -- at WR=0.3, weight is only 0.6 vs parabola's 0.84. This is arguably too aggressive at discounting useful-but-uneven matchups. With only 4 fixtures, we want a gentler rolloff.

#### Option C: Gaussian `f(WR) = exp(-k * (WR - 0.5)^2)`

With k=8 (standard choice for WR in [0,1]):

| WR   | f(WR)  | Notes                        |
|------|--------|------------------------------|
| 0.00 | 0.135  | Non-zero floor (unlike A/B)  |
| 0.20 | 0.449  |                              |
| 0.35 | 0.835  |                              |
| 0.50 | 1.000  | Peak                         |
| 0.65 | 0.835  |                              |
| 0.80 | 0.449  |                              |
| 1.00 | 0.135  |                              |

**Pros:** Smooth, tunable width via k. Non-zero at extremes, so even dominated matchups retain some weight. Well-understood.

**Cons:** Extra hyperparameter (k). For k=8, the floor at WR=0 is 0.135 -- not zero, which might be a feature or a bug. More complex than the parabola for no clear benefit given our 4-fixture pool.

**Verdict on base function: Option A (parabola) wins.** It is the simplest, has the right shape, the gentlest rolloff among the zero-at-extremes options, and the `max(0.01, ...)` floor plus UCB handles the zero-extremes issue. The Gaussian's extra knob (k) is not needed for 4 fixtures.

### 3. UCB Combination: Additive vs Multiplicative

#### Option D: Additive `weight = symmetric(WR) + c * sqrt(ln(N)/n_i)`

At WR=1.0 (always win, n_i=50, N=500):
- symmetric = 4*1*0 = 0.0
- UCB = 1.5 * sqrt(ln(500)/50) = 1.5 * sqrt(6.21/50) = 1.5 * 0.352 = 0.53
- weight = 0.53

At WR=0.5 (even match, n_i=50, N=500):
- symmetric = 4*0.5*0.5 = 1.0
- UCB = 0.53
- weight = 1.53

At WR=0.5 (even match, n_i=200, N=500):
- symmetric = 1.0
- UCB = 1.5 * sqrt(6.21/200) = 1.5 * 0.176 = 0.26
- weight = 1.26

**Problem:** With only 4 fixtures and ~200 total games per generation, the UCB term is large relative to the symmetric base. For an under-explored opponent (n_i=10, N=500), UCB = 1.5 * sqrt(6.21/10) = 1.18. This means an under-explored WR=1.0 opponent (fully beaten) would have weight 0+1.18 = 1.18, which is HIGHER than a well-explored WR=0.5 opponent (1.0+0.26 = 1.26). The additive UCB overwhelms the symmetric signal when the fixture pool is small.

#### Option E: Multiplicative `weight = symmetric(WR) * (1 + c * sqrt(ln(N)/n_i))`

At WR=1.0 (always win, n_i=50, N=500):
- symmetric = 0.0
- multiplier = 1 + 0.53 = 1.53
- weight = 0.0 * 1.53 = 0.0 → floor 0.01

At WR=0.5 (even match, n_i=50, N=500):
- symmetric = 1.0
- weight = 1.0 * 1.53 = 1.53

At WR=0.5 (even match, n_i=200, N=500):
- weight = 1.0 * 1.26 = 1.26

At WR=0.3 (hard, n_i=10, N=500):
- symmetric = 4*0.3*0.7 = 0.84
- UCB multiplier = 1 + 1.5*sqrt(6.21/10) = 1 + 1.18 = 2.18
- weight = 0.84 * 2.18 = 1.83

**This is the right behavior:** an under-explored hard opponent gets strongly boosted (1.83), a well-explored even opponent gets moderate weight (1.26), and a fully-beaten opponent stays near zero regardless of exploration. The multiplicative structure preserves the symmetric signal's zeros while allowing UCB to boost interesting matchups that need more data.

**Verdict: Option E (multiplicative) is correct for a small fixture pool.** Additive UCB would make exploration override the WR signal, defeating the purpose of symmetric weighting.

### 4. WR Decay: 0.7x vs 0.5x per Generation

Current: `DECAY = 0.7` in `ppo_loop_step.sh` line 221.

The decay multiplies both wins and totals by the factor, preserving the WR ratio but shrinking the effective sample size. This increases the UCB exploration bonus for stale matchups.

| After N gens | 0.7x retention | 0.5x retention |
|-------------|----------------|----------------|
| 1           | 0.700          | 0.500          |
| 2           | 0.490          | 0.250          |
| 3           | 0.343          | 0.125          |
| 5           | 0.168          | 0.031          |

For a fixture with 200 games:
- After 3 gens at 0.7x: 69 effective games (still > MIN_GAMES=10, WR data dominates)
- After 3 gens at 0.5x: 25 effective games (barely above MIN_GAMES, UCB starts dominating)
- After 5 gens at 0.5x: 6 effective games (below MIN_GAMES → uniform weight)

**Analysis:** With 0.5x decay and 200 games/gen, a fixture that hasn't been played for 5 generations drops below MIN_GAMES=10 and gets reset to uniform (weight=1.0). This is aggressive but arguably correct -- after 5 PPO runs (150 iterations), the model has changed enough that old WR data is truly stale.

**Risk:** With the current 4-fixture pool and 30 iters/run, fixtures are played frequently enough that staleness is unlikely within 2-3 generations. The faster decay means that after a breakthrough (e.g., suddenly winning 80% against a previously 50% opponent), the old data washes out in ~2 generations instead of ~4. This is desirable for tracking rapid improvement.

**Where to change:** The decay is applied in `ppo_loop_step.sh` lines 221, not in `train_ppo.py`. The decay is a between-generation operation, so it stays in the shell script. No change needed in `train_ppo.py` for the decay itself.

### 5. Impact on Current 4-Fixture Pool

Approximate current WR estimates (from selected_fixtures.json context):

| Fixture   | Side pool | Approx WR | Current weight (1-WR) | New symmetric weight (4*WR*(1-WR)) | Ratio change |
|-----------|-----------|-----------|----------------------|--------------------------------------|--------------|
| v22       | USSR      | ~0.80     | 0.20                 | 0.64                                 | 3.2x more    |
| v45       | USSR      | ~0.50     | 0.50                 | 1.00                                 | 2.0x more    |
| v44       | US        | ~0.45     | 0.55                 | 0.99                                 | 1.8x more    |
| v55       | US        | ~0.50     | 0.50                 | 1.00                                 | 2.0x more    |
| heuristic | both      | ~0.85     | 0.15                 | 0.51                                 | 3.4x more    |

The symmetric formula dramatically changes the relative weighting:

**Current (asymmetric):**
- USSR pool: v45 gets 2.5x the weight of v22 (0.50 vs 0.20). v22 is starved.
- US pool: v44 gets 1.1x the weight of v55 (0.55 vs 0.50). Nearly equal.

**New (symmetric):**
- USSR pool: v45 gets 1.56x the weight of v22 (1.00 vs 0.64). v22 gets much more play.
- US pool: v44 and v55 are nearly identical (0.99 vs 1.00).

The biggest change is for v22 (WR~0.80, "easy" opponent). Under the current formula, v22 gets only 20% base weight -- it is almost ignored. Under the symmetric formula, v22 gets 64% base weight, ensuring the model still gets practice against weaker opponents it has already beaten. This prevents forgetting basic competencies.

For heuristic (WR~0.85): current weight 0.15, new weight 0.51 -- 3.4x increase. This is significant but heuristic is injected separately via `heuristic_pct=0.15`, so the PFSP weight only affects its share of the fixture mass, not the direct heuristic injection.

### 6. Edge Cases and Floor Behavior

When `n_i < MIN_GAMES=10`: weight = 1.0 (unchanged, uniform exploration until we have data).

When WR is exactly 0 or 1: symmetric base = 0, multiplicative UCB gives 0 * anything = 0, floor catches it at 0.01. This is correct -- if we truly always win or always lose, the matchup is uninformative, and only the floor keeps it minimally alive for occasional re-testing.

When `total_games_all = 0` (first iteration): UCB term = 0, formula degrades to `symmetric(WR)` only. But this only happens after MIN_GAMES games exist in the table, so `total_games_all` will be at least `MIN_GAMES` by then.

### 7. Interaction with Past-Self Pool

Past-self opponents use the same `_pfsp_weight()` function, multiplied by recency weight `exp(rank / tau)`. The symmetric formula applies equally -- recent past selves near 50% WR get boosted, while very old selves that are now easy get deprioritized. This is correct: training against yourself from 100 iterations ago (who you now beat 90% of the time) is not useful. The symmetric formula handles this naturally.

## Conclusions

1. **Option A (parabola) for the symmetric base** is the best choice: `4 * WR * (1-WR)` is simple, smooth, peaks at 1.0 at WR=0.5, and drops symmetrically to 0 at the extremes.

2. **Option E (multiplicative UCB)** is correct for our small fixture pool: `symmetric(WR) * (1 + c * sqrt(ln(N)/n_i))`. Additive UCB (Option D) would overwhelm the symmetric signal when N is small.

3. **The 0.5x decay is appropriate.** With 200 games/gen and 30 iters/run, the faster decay ensures stale WR data washes out in ~2 generations, tracking rapid improvement. The risk of over-decay is mitigated by the MIN_GAMES=10 floor (below which weight resets to uniform 1.0).

4. **The decay change belongs in `ppo_loop_step.sh` only** (line 221, change `DECAY = 0.7` to `DECAY = 0.5`). No change needed in `train_ppo.py` for the decay.

5. **The biggest practical impact** is on v22 (WR~0.80): its weight increases from 0.20 to 0.64 (3.2x), ensuring the model maintains competence against weaker opponents rather than forgetting them.

6. **No new CLI arguments are needed.** The `--pfsp-exponent` arg (currently `c=1.5`) continues to control the UCB coefficient. The help text should be updated to describe the symmetric formula. The decay change is purely in the shell script.

7. **The parabola + multiplicative UCB + 0.5x decay combination** is strictly better than the current asymmetric formula for our use case (curated fixture pool, not exploiter league).

## Recommendations

### 1. Replace `_pfsp_weight()` in `scripts/train_ppo.py`

Drop-in replacement (lines 929-961):

```python
def _pfsp_weight(
    opponent_key: str,
    wr_table: dict[str, dict],
    pfsp_exponent: float,
    total_games_all: int = 0,
    side: str = "ussr",
) -> float:
    """Symmetric UCB-based opponent selection weight for one side.

    Uses symmetric PFSP: weight = 4*WR*(1-WR) * (1 + c * sqrt(ln(N)/n_i))
    where c = pfsp_exponent, N = total games across all opponents, n_i = games vs this one.
    - Opponents near WR=0.5 get maximum base weight (learning sweet spot).
    - Too-easy (WR→1) and too-hard (WR→0) opponents get low base weight (symmetric).
    - Under-explored opponents (low n_i) get multiplicative UCB boost.
    - The multiplicative structure preserves the symmetric signal's zeros.

    side: "ussr" → use USSR WR   "us" → use US WR
    Always call with an explicit side; the two pools use this independently.
    """
    wr_info = wr_table.get(opponent_key, {})
    MIN_GAMES = 10

    wins_key, total_key = ("wins_ussr", "total_ussr") if side == "ussr" else ("wins_us", "total_us")
    wins = int(wr_info.get(wins_key, 0))
    total = int(wr_info.get(total_key, 0))
    if total < MIN_GAMES:
        return 1.0
    wr = wins / total

    # Symmetric base: parabola peaking at 1.0 when WR=0.5, zero at extremes
    symmetric = 4.0 * wr * (1.0 - wr)

    # Multiplicative UCB exploration bonus
    if total_games_all > 0 and total > 0:
        ucb = pfsp_exponent * math.sqrt(math.log(total_games_all) / total)
    else:
        ucb = 0.0

    return max(0.01, symmetric * (1.0 + ucb))
```

### 2. Update CLI help text for `--pfsp-exponent`

In the argparse block (line 2742):

```python
p.add_argument("--pfsp-exponent", type=float, default=1.0,
               help="UCB exploration coefficient c for symmetric PFSP. "
                    "weight = 4*WR*(1-WR) * (1 + c*sqrt(ln(N)/n_i)). "
                    "Higher c = more exploration of under-sampled opponents.")
```

### 3. Change decay in `ppo_loop_step.sh`

Line 221: change `DECAY = 0.7` to `DECAY = 0.5`.
Lines 234, 236: update log messages from "0.7x" to "0.5x".

### 4. Update docstring in `sample_K_league_opponents()`

Line 1017: change the comment from `(1-WR_side) + c*sqrt(ln(N)/n_i)` to `4*WR*(1-WR) * (1 + c*sqrt(ln(N)/n_i))`.

### 5. Deployment recommendation

Deploy with v79_sc+ (the next self-play continuation). No rollback risk -- the formula change only affects opponent sampling weights, not the PPO algorithm itself. If the model suddenly stops improving, the most likely cause is that 0.5x decay is too aggressive; in that case, revert to 0.6x as a compromise before going back to 0.7x.

### 6. Monitoring

Track these W&B metrics to verify the formula change is working:
- `ucb/v22_weight_ussr` should increase from ~0.2 to ~0.6-0.8
- `ucb/v55_weight_us` should stay near ~1.0-1.5
- Fixture selection frequency should become more uniform across the 4 fixtures
- If any fixture drops below 5% selection rate after 10 iterations, the symmetric formula may be too aggressive -- consider raising the floor from 0.01 to 0.05

## Open Questions

1. **Should MIN_GAMES be raised from 10 to 20?** With 0.5x decay, a fixture with 25 effective games (just above the threshold) has a very noisy WR estimate. Raising MIN_GAMES to 20 would keep fixtures in uniform-exploration mode longer, reducing noise but slowing convergence.

2. **Should the floor be 0.01 or higher?** With multiplicative UCB and symmetric base, opponents at WR=0.0 or WR=1.0 get floor weight 0.01. For a 4-fixture pool, this means they get ~1% selection probability even without UCB. This seems fine, but if fixtures are never played at all, raising to 0.05 would ensure occasional re-testing.

3. **Should the parabola exponent be tunable?** Instead of `4*WR*(1-WR)`, we could use `(4*WR*(1-WR))^p` where p>1 sharpens the peak at 0.5 and p<1 flattens it. For now, p=1 (linear parabola) is the simplest and recommended choice. If the model trains too much on near-50% opponents and neglects moderately uneven matchups (WR~0.3 or ~0.7), consider p=0.5 to flatten the curve.

4. **Interaction with heuristic_pct:** The heuristic opponent is injected with a separate 15% probability via `heuristic_pct` in `sample_K_league_opponents()`. The PFSP weight only affects its share within the fixture mass allocation. If heuristic WR is ~0.85, its symmetric weight is 0.51 -- still gets reasonable fixture mass. This dual pathway (direct injection + fixture PFSP) seems fine but could be simplified in the future.

5. **Should the decay be configurable via CLI?** Currently it is hardcoded in the shell script. Adding `--pfsp-wr-decay` to `train_ppo.py` would make it easier to experiment, but the decay is a between-generation operation that runs before `train_ppo.py` starts, so the shell script is the right place. A compromise: make it a variable at the top of `ppo_loop_step.sh` (e.g., `WR_DECAY=0.5`) rather than buried inline.
