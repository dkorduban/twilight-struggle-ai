# Opus Analysis: PFSP Weight Design
Date: 2026-04-12 UTC
Question: Optimal combination of symmetric PFSP + additive UCB + 0.5x generation decay

## Executive Summary

The current implementation has the right primitives (symmetric parabola base, additive UCB, 0.5x decay) but two structural issues in `sample_K_league_opponents()`: (1) fixtures collectively receive only 33% of sampling probability after normalization, which is too low for the 3-fixture case where fixtures are the primary diversity source; and (2) the UCB `total_games_all` term sums across both sides, inflating `N` and creating side-contaminated exploration bonuses. The generation decay correctly applies to both wins and totals (preserving WR while reducing confidence), which is the right behavior for non-stationary bandit discounting. The recommended fixes are: raise fixture mass from 0.5x to 1.0x past-self mass (giving fixtures ~50% after normalization), compute `total_games_all` per-side, and add a warm-start floor for fixtures at iter<5.

## Findings

### 1. Fixture Weight Budget Analysis (Question 1)

**Current formula:** `fixture_each[i] = past_total * 0.5 * (w_i / fixture_total)`

Where `past_total = sum(past_self_weights)` after normalization to sum=1.0, so `past_total = 1.0`.

This means total fixture mass = `past_total * 0.5 = 0.5`, and after combining:
- past-self total weight = 1.0
- fixture total weight = 0.5
- After final normalization: past-self gets 1.0/1.5 = 66.7%, fixtures get 0.5/1.5 = 33.3%

**Is 33% the right ratio?**

No, 33% is too low. Here is the reasoning:

With mix_k=6, the slot allocation is:
- 1 self-play slot (both sides) → dedicated, not sampled from pool
- k_per_side = max(1, (6-1)//2) = 2 per side
- Total: 1 self + 2 USSR pool + 2 US pool = 5 slots

Each side's pool has 2 sampled slots. Within each pool, fixtures get only 33% of the sampling probability. So in expectation:
- Self-play: 1 slot (fixed)
- Per-side pool fixtures: 2 * 0.333 = 0.67 expected fixture slots per side
- Per-side pool past-self: 2 * 0.667 = 1.33 expected past-self slots per side
- Total fixture slots: ~1.33 out of 5 = 26.7%
- Total past-self slots: ~2.67 out of 5 = 53.3%
- Self-play: 1 out of 5 = 20%

With only 3 fixtures (e.g., bc_wide384, v55, heuristic), the fixture diversity is the primary source of policy diversity that prevents self-play collapse. Giving fixtures only 27% of training games is insufficient. Past-self opponents tend to be very similar to the current model (especially recent ones with high recency weight), so they provide less gradient diversity than fixtures.

**Recommendation:** Change the multiplier from 0.5 to 1.0:

```python
fixture_each = [past_total * 1.0 * (w / fixture_total) for w in fixture_pfsp_weights]
```

This gives fixtures 50% of sampling probability (after normalization: 1.0/2.0 = 50%), resulting in:
- Per-side pool fixtures: 2 * 0.5 = 1.0 expected fixture slot per side
- Total fixture slots: ~2 out of 5 = 40%
- Total past-self: ~2 out of 5 = 40%
- Self-play: 1 out of 5 = 20%

This is a more balanced allocation. The heuristic_pct=0.15 fallback also adds extra heuristic games on top (15% chance per non-self slot), further ensuring fixture exposure.

**Alternative: make the multiplier configurable.** Add a `--fixture-weight-ratio` CLI argument (default 1.0) to allow tuning without code changes.

### 2. Generation Decay: Both Wins and Totals (Question 2)

**Current implementation** (in `ppo_loop_step.sh`):
```python
DECAY = 0.5
out[key] = {
    'wins_ussr': int(round(val.get('wins_ussr', 0) * DECAY)),
    'total_ussr': int(round(val.get('total_ussr', 0) * DECAY)),
    ...
}
```

This decays both wins and totals by 0.5x, preserving the win rate (since `(w*d)/(t*d) = w/t`) while halving the effective sample size.

**This is correct.** The reasoning:

1. **Preserving WR is right.** The WR against a fixture (e.g., heuristic) reflects the model's actual strength at that moment. Even though the model has changed, the WR estimate is still our best prior for that matchup. If the model improved, it will quickly push WR higher in new games; if it regressed, WR will drop. Starting from the last known WR is better than starting from scratch.

2. **Reducing sample size is right.** The UCB term `c * sqrt(ln(N)/n_i)` increases as `n_i` shrinks, meaning stale matchups get re-explored. With 0.5x decay:
   - 200 games → 100 after 1 gen → 50 after 2 → 25 after 3 → 12 after 4 → 6 after 5
   - At n=6, the MIN_GAMES=10 threshold triggers → opponent reverts to uniform weight (1.0)
   - This means after 5 generations of not playing an opponent, we completely forget its WR and start fresh — this is appropriate for a rapidly evolving policy.

3. **Decaying only totals (not wins) would be wrong.** If we kept `wins=100` but decayed `total=200→100`, the apparent WR would jump from 50% to 100%. This would massively distort the symmetric PFSP weight.

4. **Decaying only wins (not totals) would also be wrong.** It would deflate WR toward 0, making everything look like a hard opponent.

**One subtlety:** The `int(round(...))` introduces a small bias. For example, wins=11, total=20, WR=0.55. After decay: wins=round(5.5)=6, total=round(10)=10, WR=0.60. The rounding errors compound but are bounded: with 0.5x decay, the maximum rounding error per generation is ±0.5/n, which is negligible for n>10 and gets swamped by new game data within a few iterations.

### 3. Past-Self vs Fixture Weight Ratio (Question 3)

As analyzed in section 1, the 0.5x multiplier gives fixtures only 33% of pool probability. The key insight is:

**Past-self opponents cluster near 50% WR** (because they are recent versions of the same model). This means their symmetric PFSP weight is near maximum (1.0), and their recency weight further concentrates on the most recent checkpoints. The net effect is that most past-self sampling goes to the 2-3 most recent checkpoints, which are nearly identical to the current model.

Training against near-copies of yourself provides weak gradient signal compared to diverse fixtures (heuristic, bc_wide384, strong historical checkpoints). The literature on self-play collapse in this project (documented in `project_policy_collapse.md`) confirms this: v11/v12 regressed due to echo-chamber self-play.

**Recommended ratio:** 1.0x (fixtures get equal mass to past-self pool). This can be raised to 1.5x or 2.0x if collapse symptoms reappear.

### 4. UCB N Term: Cross-Side Contamination (Question 4)

**Current implementation:**
```python
total_games_all = sum(
    int(v.get("total_ussr", 0)) + int(v.get("total_us", 0))
    for v in _wr.values()
)
```

This sums USSR and US games across ALL opponents. Then in `_pfsp_weight()`:
```python
ucb = pfsp_exponent * math.sqrt(math.log(total_games_all) / total)
```
where `total` is the per-side game count (e.g., `total_ussr` for the USSR pool).

**Problem:** `N = total_games_all` includes games from the other side, inflating the UCB exploration bonus.

Example: After 100 iterations, suppose:
- heuristic: total_ussr=300, total_us=300 → total_games_all includes both
- v55: total_ussr=50, total_us=200

When computing the USSR pool weight for v55:
- N = sum of all games across all opponents and both sides ≈ 1200
- n_i = total_ussr for v55 = 50
- UCB = 1.5 * sqrt(ln(1200)/50) = 1.5 * sqrt(7.09/50) = 1.5 * 0.377 = 0.56

If we used per-side N:
- N_ussr = sum of total_ussr across all opponents ≈ 500
- UCB = 1.5 * sqrt(ln(500)/50) = 1.5 * sqrt(6.21/50) = 1.5 * 0.352 = 0.53

**The difference is small** (0.56 vs 0.53) because N appears inside a logarithm. The UCB term scales as `sqrt(ln(N))`, so doubling N only increases the UCB by `sqrt(ln(2)/n_i)` ≈ 0.12 for n_i=50. This is a second-order effect.

**However, it is still conceptually wrong.** The UCB exploration bonus should measure "how under-explored is this opponent relative to others in the same pool." Cross-side contamination means an opponent that is well-explored as US but under-explored as USSR gets a slightly inflated UCB bonus when evaluated for the USSR pool.

**Recommendation:** Compute `total_games_all` per-side. This is a small code change:

```python
# In sample_K_league_opponents():
total_key_for_side = "total_ussr" if side == "ussr" else "total_us"
total_games_all = sum(int(v.get(total_key_for_side, 0)) for v in _wr.values())
```

The practical impact is small, but it eliminates a conceptual leak and makes the formula cleaner. Worth doing when touching this code.

### 5. Bootstrap Bias at Early Iterations (Question 5)

**Scenario:** At iter=1, the league directory is empty or has only 1 checkpoint (iter_0010.pt with n=0 games from the current run, but possibly carried-over data from the previous run's wr_table.json).

**Current behavior:**
- `past_self_paths` has 1 entry (iter_0010.pt)
- `past_self_weights` = [recency * pfsp_w]
- If iter_0010 has no WR data (n=0): pfsp_w = 1.0 (below MIN_GAMES)
- If fixtures have carried-over data (n>10): pfsp_w comes from the formula

After the 0.5x decay, a fixture with 200 games becomes 100 games. Its WR is preserved, so if WR=0.5:
- symmetric = 4*0.5*0.5 = 1.0
- UCB = 1.5 * sqrt(ln(100)/100) = 1.5 * sqrt(4.6/100) = 1.5 * 0.214 = 0.32
- pfsp_w = 1.0 + 0.32 = 1.32

Meanwhile, the single past-self checkpoint has pfsp_w = 1.0.

**Mass allocation:**
- past_total = 1.0 (normalized past_self_weights)
- fixture_each = 1.0 * 0.5 * (w_i / fixture_total) → total fixture mass = 0.5
- After normalization: past-self = 66.7%, fixtures = 33.3%

So the single past-self checkpoint gets 66.7% of sampling probability. This is the bootstrap bias: at early iterations, the model plays mostly against itself (one checkpoint) rather than diverse fixtures.

**This is problematic.** The single past-self checkpoint IS the current model (or very close to it). Playing against yourself at iter=1 provides minimal gradient diversity. The fixtures (heuristic, bc_wide384, etc.) are the only source of diversity.

**Recommended fix:** Add a fixture floor for early iterations:

```python
# At early iterations, boost fixture weight to avoid self-play domination
fixture_mass_multiplier = 1.0  # base (up from 0.5)
if current_iter < 5 and active_fixtures:
    # At iter 0-4, give fixtures 2x weight to ensure diversity
    fixture_mass_multiplier = 2.0

fixture_each = [
    past_total * fixture_mass_multiplier * (w / fixture_total)
    for w in fixture_pfsp_weights
] if active_fixtures else []
```

With multiplier=2.0 at early iters: fixture mass = 2.0, past-self = 1.0, fixtures get 66.7% — exactly inverting the current bias. After iter>=5, the multiplier drops to 1.0 (50/50 split) and the model has enough past-self diversity to train effectively.

Alternatively, a simpler approach: ensure the WR table is always warm-started from the previous run (which `ppo_loop_step.sh` already does). The real problem is when launching manually without seeding the WR table — the comment at line 203-210 already warns about this. The fix should be both: (a) always seed the WR table AND (b) boost fixture weight at early iters as a safety net.

### 6. Additive vs Multiplicative UCB Revisited

The earlier analysis (`opus_analysis_20260412_173000_pfsp_symmetric_ucb_decay.md`) recommended multiplicative UCB. The code now uses additive UCB with a comment explaining the rejection:

> Multiplicative UCB was rejected: near-zero symmetric base at WR→1 kills the exploration bonus, preventing re-testing of weak opponents.

**This is the right call.** The argument for multiplicative UCB assumed that WR extremes should remain at zero weight. But in practice, regression detection is critical: if the model suddenly starts losing to a previously-beaten opponent, we need to detect this quickly. With multiplicative UCB, an opponent at WR=0.95 has symmetric base = 4*0.95*0.05 = 0.19, and the UCB multiplier would need to be >5x to bring this above 1.0 — requiring extremely low n_i. With additive UCB, the same opponent gets 0.19 + UCB, where even a moderate UCB of 0.5 brings the total to 0.69, ensuring regular re-testing.

**The additive UCB is correct for this use case.** The concern about additive UCB overwhelming the symmetric signal (raised in the earlier analysis) is valid for very small N, but with 200 games/iteration and 30 iterations/run, N grows quickly and the UCB term shrinks proportionally.

Quantitative check with c=1.5 after 10 iterations (N ≈ 2000 total games, n_i ≈ 200 per fixture):
- UCB = 1.5 * sqrt(ln(2000)/200) = 1.5 * sqrt(7.6/200) = 1.5 * 0.195 = 0.29
- Symmetric at WR=0.5: 1.0 + 0.29 = 1.29 (UCB is 22% of total — acceptable)
- Symmetric at WR=0.8: 0.64 + 0.29 = 0.93 (UCB is 31% — still fine)
- Symmetric at WR=0.95: 0.19 + 0.29 = 0.48 (UCB dominates — this is the desired regression detection behavior)

### 7. Interaction of All Three Components

Let's trace through a concrete scenario at steady state (iter=15, after several generations):

**Setup:**
- Past-self pool: 15 checkpoints (iter_0010 through iter_0150), recency_tau=50
- Fixtures: heuristic (WR_ussr=0.85, n=150), bc_wide384 (WR_ussr=0.55, n=80), v55 (WR_ussr=0.45, n=120)
- N_ussr ≈ 800 (all USSR games)

**Past-self weights (recency * pfsp):**
- Most recent (rank=14): recency = exp(14/50) = 1.32, pfsp ≈ 1.0 (near-50% WR) → 1.32
- 5th from end (rank=10): recency = exp(10/50) = 1.22, pfsp ≈ 0.90 → 1.10
- Oldest (rank=0): recency = exp(0/50) = 1.0, pfsp ≈ 0.50 (model probably beats it easily) → 0.50
- After normalization, recent checkpoints dominate (as intended)

**Fixture PFSP weights:**
- heuristic: symmetric = 4*0.85*0.15 = 0.51, UCB = 1.5*sqrt(ln(800)/150) = 1.5*0.211 = 0.32 → 0.83
- bc_wide384: symmetric = 4*0.55*0.45 = 0.99, UCB = 1.5*sqrt(ln(800)/80) = 1.5*0.289 = 0.43 → 1.42
- v55: symmetric = 4*0.45*0.55 = 0.99, UCB = 1.5*sqrt(ln(800)/120) = 1.5*0.236 = 0.35 → 1.34

**Fixture allocation (with proposed 1.0x multiplier):**
- fixture_total = 0.83 + 1.42 + 1.34 = 3.59
- heuristic gets: 1.0 * 0.83/3.59 = 0.231 of fixture mass
- bc_wide384 gets: 1.0 * 1.42/3.59 = 0.396 of fixture mass
- v55 gets: 1.0 * 1.34/3.59 = 0.373 of fixture mass

**After normalization (past_total=1.0, fixture_total=1.0):**
- Past-self: 50% total probability
- Fixtures: 50% total probability, distributed as heuristic=11.6%, bc_wide384=19.8%, v55=18.7%

This is a well-balanced allocation: bc_wide384 gets the most fixture weight (closest to WR=0.5, under-explored), v55 is close behind (also near 50% but slightly more explored), and heuristic gets least (far from WR=0.5 but still present for regression detection).

### 8. The heuristic_pct Bypass

There is a subtle interaction: `heuristic_pct=0.15` applies a 15% chance per non-self slot to force heuristic selection, **bypassing** the PFSP weighting entirely:

```python
if not combined_pool or random.random() < heuristic_pct:
    opponents.append(None)  # heuristic
```

This means the effective fixture allocation is:
- 15% of slots → heuristic (forced, regardless of PFSP)
- 85% of slots → sampled from PFSP-weighted pool (which includes heuristic as a fixture)

If heuristic is both a fixture AND in the heuristic_pct bypass, it gets double-dipped:
- Direct: 15% of each slot
- Via fixture pool: 85% * (heuristic's share of fixture mass) ≈ 85% * 11.6% * 50% ≈ 4.9%
- Total: ~20% per slot

This is probably fine — heuristic is a strong anchor opponent — but the double pathway is confusing. If heuristic is in the fixture pool, the `heuristic_pct` bypass could be reduced to 5% or removed entirely, letting PFSP handle the allocation.

## Conclusions

1. **The additive UCB formula `4*WR*(1-WR) + c*sqrt(ln(N)/n_i)` is correct.** Additive UCB ensures regression detection by keeping dominated opponents above zero weight, which multiplicative UCB fails to do.

2. **The fixture mass multiplier should be raised from 0.5 to 1.0.** The current 33% fixture share is too low; fixtures are the primary source of policy diversity and 50% is a better balance. This is the single highest-impact fix.

3. **Decaying both wins and totals by 0.5x is correct.** This preserves the WR estimate (our best prior) while reducing confidence, causing the UCB term to increase for stale matchups. Decaying only one of the two would distort the WR.

4. **The UCB `total_games_all` should be computed per-side, not cross-side.** The current cross-side sum inflates N and creates a conceptual leak, though the practical impact is small (~5% change in UCB values due to the logarithm).

5. **A fixture weight boost at early iterations (iter<5) is needed.** Without it, a single past-self checkpoint monopolizes 67% of sampling at iter=1. Setting `fixture_mass_multiplier=2.0` for iter<5 inverts this bias, ensuring diversity during the critical warm-up phase.

6. **The pfsp_exponent=1.5 is well-calibrated.** At steady state (N~2000, n_i~200), the UCB term is ~0.29 — about 22% of the WR=0.5 base weight. This provides meaningful exploration without overwhelming the symmetric signal.

7. **The 0.5x per-generation decay rate is appropriate.** It causes a fixture with 200 games to fall below MIN_GAMES=10 after 5 generations (~150 iterations), triggering a full reset to uniform weight. This matches the timescale of significant policy change.

8. **The heuristic_pct bypass double-dips heuristic selection** when heuristic is also in the fixture pool. Consider reducing heuristic_pct to 0.05 or 0.0 when `__heuristic__` is an explicit fixture, relying on PFSP to handle allocation.

## Recommendations

### Priority 1: Raise fixture mass multiplier (high impact, 1-line change)
```python
# Line 1070-1073 in sample_K_league_opponents():
fixture_each = [
    past_total * 1.0 * (w / fixture_total)  # was 0.5
    for w in fixture_pfsp_weights
] if active_fixtures else []
```

### Priority 2: Per-side total_games_all (conceptual correctness, 3-line change)
```python
# Line 1041-1044 in sample_K_league_opponents():
total_key_for_side = "total_ussr" if side == "ussr" else "total_us"
total_games_all = sum(
    int(v.get(total_key_for_side, 0)) for v in _wr.values()
)
```

### Priority 3: Early-iteration fixture boost (bootstrap safety, 5-line change)
```python
# After line 1064:
fixture_mass_multiplier = 1.0
if current_iter < 5 and len(past_self_paths) <= 2 and active_fixtures:
    fixture_mass_multiplier = 2.0

fixture_each = [
    past_total * fixture_mass_multiplier * (w / fixture_total)
    for w in fixture_pfsp_weights
] if active_fixtures else []
```

### Priority 4: Make fixture mass ratio configurable (future-proofing)
Add `--fixture-weight-ratio` CLI argument (default 1.0), passed through to `sample_K_league_opponents()`.

### Priority 5: Reduce heuristic_pct when heuristic is a fixture
When `__heuristic__` is in the fixture list, the bypass `heuristic_pct` should be reduced to 0.05 or 0.0 to avoid double-dipping. This could be auto-detected:
```python
effective_heuristic_pct = 0.05 if HEURISTIC_FIXTURE in fixtures else heuristic_pct
```

## Open Questions

1. **Should the fixture mass ratio adapt to the number of fixtures?** With 3 fixtures, 1.0x gives 50/50 split. With 10 fixtures, 1.0x might over-allocate to fixtures. A formula like `min(1.0, 0.33 * len(active_fixtures))` would scale linearly, capping at 1.0 for 3+ fixtures.

2. **Should MIN_GAMES be side-specific?** Currently MIN_GAMES=10 applies per-side. After 0.5x decay, a fixture with 25 games per side becomes 12 — barely above threshold. The formula will produce a noisy WR estimate. Consider raising to MIN_GAMES=15 or 20.

3. **Should the past-self pool be thinned?** With 150+ past checkpoints and recency_tau=50, checkpoints older than ~100 iterations have negligible recency weight (<0.13x the most recent). These occupy pool slots without being selected. Pruning to the most recent 50 checkpoints would reduce noise.

4. **Should the UCB c value decay over time?** As the WR table accumulates more data, the exploration bonus becomes less important. A decaying c (e.g., c = 1.5 / sqrt(generation)) would shift from exploration toward exploitation over the training run. However, the generation decay on n_i already accomplishes something similar (shrinking n_i increases UCB naturally for stale matchups).

5. **Is the `max(0.01, ...)` floor sufficient?** With additive UCB and c=1.5, the floor is rarely hit (UCB alone exceeds 0.01 unless n_i > 10^9). The floor mainly matters when total_games_all=0 and WR is at an extreme. Consider whether 0.01 or 0.05 is better for the edge case.
