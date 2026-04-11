# K-Sample Influence Expansion: Regression Analysis

## Summary

The K=4 influence expansion causes a **~20pp win rate regression** (37.5% -> 17.0% combined)
that does NOT recover with more simulations. The regression has three compounding causes,
ordered by severity:

1. **Slow-path fallback** (primary cause of wall-time blowup, secondary cause of strength loss)
2. **Fundamental tree width vs simulation budget mismatch** (primary cause of strength loss)
3. **Prior dilution of influence edges** (amplifier that compounds cause #2)

There is no single implementation bug. The regression is a predictable consequence of the
architecture: adding K edges to an already-wide tree while keeping simulations constant.

---

## Detailed Findings

### Finding 1: Slow-path fallback (Hypothesis 4 -- CONFIRMED)

When `influence_samples > 1`, `expand_from_raw_fast()` immediately falls back to
`expand_from_raw()`:

```cpp
// mcts_batched.cpp:1534-1539
if (config.influence_samples > 1 ||
    config.influence_t_strategy > 0.0f ||
    config.influence_t_country > 0.0f) {
    return expand_from_raw(state, raw, batch_index, config, rng);
}
```

The slow path uses `collect_card_drafts_cached()` which allocates `std::vector<CountryId>`
for every edge (including the ~460 coup/realign edges that are identical between K=1 and K=4).
The fast path avoids these allocations by using compact boolean flags and direct pointer math.

**Measured impact**: K=4 at 100 sims takes 417s vs K=1 at 50s -- an **8.3x slowdown**.
Since influence edges are only ~4% of total edges, the K-sample computation itself is not
the bottleneck. The heap allocations for the other 96% of edges (coup/realign) in the slow
path dominate.

**This means at equal wall time, K=4 explores ~8x fewer sims.** The 400-sim K=4 result
(1274s) consumed the same wall time as ~2,000 sims at K=1, yet produced only 400 sims of
search quality.

### Finding 2: Tree width vs simulation budget (Hypothesis 1 -- CONFIRMED, dominant)

Profiling shows **~474 edges per node** at K=4. Crucially, K=1 in the slow path would
produce ~470 edges per node (influence is only 4% of edges). The tree is wide regardless
of K, because each (card, coup/realign, country) triple is a separate edge.

With the PUCT formula: `score = Q + c_puct * prior * sqrt(N_parent) / (1 + N_child)`

At 100 sims, only ~21% of edges at the root can be visited even once. At 400 sims,
still only ~84% get a single visit. PUCT degenerates into "follow the prior" when visits
are this sparse -- the Q term (learned value from deeper search) barely contributes.

**The fundamental problem**: with 474 edges, MCTS needs ~2000-5000 sims per node to start
getting meaningful visit counts on second-choice edges. At 100-400 sims, the tree is
essentially one level deep, and search adds almost nothing over raw policy.

This explains why **400 sims does NOT recover the K=4 regression** -- both 100 and 400 sims
are far below the threshold where the wider tree pays off.

### Finding 3: Prior dilution of influence edges (Hypothesis 2 -- partially confirmed)

With K=1: Influence gets prior = `P(card) * P(influence)` as a single concentrated edge.
With K=4: The same total prior mass is split among 4 allocations via density-weighted
normalization: `prior_k = P(card) * P(influence) * density_k / sum(densities)`.

The density computation (`compute_density` -> `multinomial_probability`) is mathematically
correct. There is no bug in the probability calculation. However, the split means each
individual influence edge has a smaller prior, making it less attractive to PUCT compared
to coup/realign edges (which have concentrated priors on individual countries).

At c_puct=1.5, with parent_visits=100:
- K=1 influence edge with prior 0.10: exploration bonus = 1.5 * 0.10 * 10 = **1.50**
- K=4 influence edge with prior 0.025: exploration bonus = 1.5 * 0.025 * 10 = **0.375**

The best influence allocation competes poorly against high-prior coup targets, biasing
search toward military operations. Since influence is often the stronger play (especially
for board control), this degrades strategic quality.

### Finding 4: log_factorial table (Hypothesis 6 -- NOT a bug)

The hardcoded `log_factorial[6]` (max index 5) is sufficient. `effective_ops` returns
`max(1, card.ops + ops_modifier)` where card.ops <= 4 and ops_modifier <= +1 (Brezhnev/
Containment), so max effective ops = 5. The table cannot overflow.

### Finding 5: RNG consumption (Hypothesis 5 -- minimal impact)

The K-sample path creates a local RNG via `Pcg64Rng local_rng(rng.next_u64())`, advancing
the parent RNG by exactly 1 regardless of K. Non-influence code paths advance the RNG
identically between K=1 and K=4. The game trajectory divergence from RNG is minimal and
does not systematically bias toward harder games.

---

## Recommendations

### Option A: Abandon K>1 expansion (recommended for now)

The tree is already too wide (~470 edges per node) for K-sampling to add value at
100-400 sims. Adding more edges to an under-explored tree hurts more than it helps.
The model's policy network already provides a good influence allocation via proportional
rounding; splitting it into K samples just dilutes the prior signal.

**Keep K=1 and invest in reducing tree width instead.**

### Option B: Reduce tree width first, then revisit K>1

The ~470 edges per node are dominated by (card, realign, country) triples -- 61% of edges.
Consider:

1. **Prune low-prior edges**: Drop edges with prior < 0.001 after normalization. Most
   coup/realign targets have near-zero probability from the policy network.
2. **Top-N country pruning**: For coup and realign, keep only the top 5-10 country targets
   per card instead of all legal targets.
3. **Progressive widening**: Start with top-K edges and add more as visit count grows.

If tree width drops to ~50-100 edges, then K=2-4 for influence could work.

### Option C: Fix the slow-path fallback (necessary if pursuing K>1)

Even if K>1 is worth pursuing, the slow-path fallback must be eliminated. The fix:
add K-sample support directly into `expand_from_raw_fast()` so it uses the compact
legal card representation, pre-computed softmax, and zero-allocation edge construction.
This would eliminate the 8x wall-time penalty.

### Option D: PUCT adaptation for split priors

If K>1 is kept, consider adjusting PUCT to account for the fact that K influence edges
jointly represent a single strategic choice. Options:
- Sum priors of all K influence edges for the same card when computing the exploration
  bonus (group PUCT)
- Use a higher c_puct for influence edges specifically
- Weight influence edges by their share of the K-sample set

---

## Conclusion

K>1 influence expansion is not viable at the current simulation budget (100-400 sims) with
the current tree width (~474 edges/node). The regression is not a bug but a fundamental
mismatch between tree width and search depth. The most impactful improvement would be
reducing tree width through edge pruning, which would benefit K=1 search quality as well.
