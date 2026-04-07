# Spec: K-Sample Influence Allocation in MCTS

## Goal

Currently each (card, Influence) pair creates exactly **one** MCTS tree edge with a
single deterministic allocation computed by proportional rounding from the NN's country
logits. MCTS never explores alternative influence placements — this is the confirmed
bottleneck (card/mode search gives 0pp improvement, allocation quality is the gap).

This change creates **K diverse influence edges** per (card, Influence) pair, letting
MCTS explore and compare different country allocations. No engine, Python, or binding
changes required — purely in the C++ expand path.

## Files to modify

- `cpp/tscore/mcts_batched.hpp` — add `int influence_samples` to `BatchedMctsConfig`
- `cpp/tscore/mcts_batched.cpp` — rewrite influence edge creation in `expand_from_raw()`
- `cpp/tools/collect_mcts_games_jsonl.cpp` — add `--influence-samples` CLI flag

## Files to reference (read-only)

- `cpp/tscore/mcts_batched.cpp` lines 614-787 — current `expand_from_raw()` function
- `cpp/tscore/mcts_batched.cpp` lines 654-677 — current argmax strategy selection
- `cpp/tscore/mcts_batched.cpp` lines 745-783 — current single proportional allocation
- `cpp/tscore/mcts_batched.hpp` lines 93-123 — `BatchedMctsConfig` struct
- `cpp/tscore/rng.hpp` — `Pcg64Rng` API (`next_u32`, `uniform_int`, `choice_index`)
- `cpp/tscore/types.hpp` lines 97-103 — `ActionEncoding` struct

## Interface contract

### Config additions

In `BatchedMctsConfig` (mcts_batched.hpp), add four fields:
```cpp
float influence_t_strategy = 0.0f;    // Temperature for strategy selection.
                                       // 0 = argmax (current behavior).
                                       // >0 = sample from softmax(logits / T).
float influence_t_country = 0.0f;     // Temperature for country sampling within a strategy.
                                       // 0 = deterministic proportional rounding (current).
                                       // >0 = multinomial sample with p^(1/T) scaling.
bool influence_proportional_first = true;
                                       // When true AND K>1: the first allocation for each
                                       // selected strategy uses deterministic proportional
                                       // rounding regardless of T_country. Subsequent
                                       // allocations from the same strategy use T_country.
                                       // When false: all allocations use T_country directly.
                                       // Ignored when K=1 and T_country=0 (single det. edge).
int influence_samples = 1;            // K: number of influence allocation edges created per
                                       // (card, Influence) during node expansion.
                                       // 1 = single edge (current). >1 = K diverse edges.
                                       // These are EDGES, not simulations — all K edges
                                       // share the n_sim budget via UCB selection.
```

How the knobs compose:
- `T_s=0, T_c=0, K=1`: bit-identical to current (argmax strategy + proportional + 1 edge)
- `T_s>0, T_c=0, K=1`: sample strategy, deterministic proportional from it
- `T_s=0, T_c>0, K=1`: argmax strategy, multinomial country sample at T_c
- `T_s>0, T_c>0, K=1`: sample strategy at T_s, multinomial countries at T_c
- `T_s=0, T_c=0, K>1`: argmax deterministic as edge 0, per-strategy deterministic for
  edges 1..min(K-1, n_strat-1), then T_c=1.0 multinomial for remainder
- `T_s>0, T_c>0, K>1, prop_first=true`: each edge samples a strategy at T_s; first
  edge per strategy is deterministic proportional, rest use T_c multinomial. Deduped.
- `T_s>0, T_c>0, K>1, prop_first=false`: all K edges sampled (strategy at T_s,
  countries at T_c). Deduped.

No "mixture distribution" — each edge uses a single strategy's country distribution.

When all at defaults (`T_s=0, T_c=0, K=1`), behavior must be **bit-identical**
to current code. All existing tests, benchmarks, and self-play must be unaffected.

### CLI flags

In `collect_mcts_games_jsonl.cpp`, add:
- `--influence-t-strategy F` (default 0.0) → `config.influence_t_strategy`
- `--influence-t-country F` (default 0.0) → `config.influence_t_country`
- `--influence-proportional-first` (flag, default true) → `config.influence_proportional_first`
- `--no-influence-proportional-first` (flag) → sets it to false
- `--influence-samples N` (default 1) → `config.influence_samples`

## Algorithm: multi-sample influence expansion

When `influence_samples > 1` and we reach a (card, Influence) edge in `expand_from_raw()`:

### Step 1: Compute per-strategy country distributions

Compute **all n_strategy distributions** (masked softmax per strategy over legal countries):

```cpp
float strategy_logits_buf[kMaxStrategies];
// Copy raw strategy logits
memcpy(strategy_logits_buf, raw.strategy_logits + batch_index * raw.strategy_stride,
       n_strategy * sizeof(float));

// Per-strategy masked country distributions
float country_probs[kMaxStrategies][kMaxCountryLogits];
for (int s = 0; s < n_strategy; ++s) {
    const float* cs_row = raw.country_strategy_logits + batch_index * cs_batch_stride + s * cs_n_countries;
    // Fill with -inf, unmask legal countries, softmax → country_probs[s]
}
```

No mixture distribution needed. Each allocation uses a single strategy's distribution.

### Step 2: Zobrist hash table for dedup

```cpp
// hash of allocation = sum over all placed ops of kZobrist[country_id_of_that_op]
// Since sum is commutative over the multiset of country_ids, this IS order-invariant.
// kZobrist[c] is a random 64-bit constant per country_id c, fixed at compile time or
// initialized from a fixed seed at static init.
```

For a placement [France, France, WGermany]: hash = 2 * kZobrist[France] + kZobrist[WGermany].

### Step 2b: Bootstrap local RNG

```cpp
// Consume exactly 1 u64 from the main game RNG to seed a local RNG.
// All sampling in this expansion uses local_rng.
// Main RNG advances by exactly 1 regardless of K, retries, or collisions.
// This prevents K-sample work from desynchronizing downstream game decisions.
Pcg64Rng local_rng(rng.next_u64());
```

At T_s=0, T_c=0, K=1 the guard skips the new path entirely → main RNG untouched →
bit-identical to current code. When the new path IS entered, main RNG always advances
by exactly 1.

### Step 3: Generate K allocations with dedup

```cpp
std::unordered_set<uint64_t> seen_hashes;
struct InfluenceAllocation {
    ActionEncoding action;  // card_id, mode=Influence, targets=[country_ids...]
    double prior;           // card_prob * mode_prob * multinomial_prob
    uint64_t hash;
};
std::vector<InfluenceAllocation> allocations;
allocations.reserve(influence_samples);

int ops = effective_ops(card_id, state.pub, state.pub.phasing);
float T_s = config.influence_t_strategy;
float T_c = config.influence_t_country;
bool prop_first = config.influence_proportional_first;

// Track which strategies have already produced a proportional allocation
bool strategy_has_proportional[kMaxStrategies] = {};

// Helper: pick a strategy index
auto pick_strategy = [&](Pcg64Rng& local_rng) -> int {
    if (T_s == 0.0f) {
        // argmax
        int best = 0;
        for (int s = 1; s < n_strategy; ++s)
            if (strategy_logits_buf[s] > strategy_logits_buf[best]) best = s;
        return best;
    }
    // Sample from softmax(logits / T_s)
    float temp_logits[kMaxStrategies];
    for (int s = 0; s < n_strategy; ++s) temp_logits[s] = strategy_logits_buf[s] / T_s;
    softmax_inplace(temp_logits, n_strategy);
    return categorical_sample(temp_logits, n_strategy, local_rng);
};

// Helper: generate allocation from a strategy's country distribution
// Returns proportional if (a) T_c=0, or (b) prop_first and this strategy hasn't
// produced its proportional allocation yet.
auto make_allocation = [&](int strat, Pcg64Rng& local_rng) -> AllocationResult {
    bool use_proportional = (T_c == 0.0f) ||
                            (prop_first && !strategy_has_proportional[strat]);
    if (use_proportional) {
        strategy_has_proportional[strat] = true;
        return proportional_allocation(country_probs[strat], cache.influence, ops, n_country);
    }
    return multinomial_sample(country_probs[strat], cache.influence, ops, n_country, T_c, local_rng);
};

// Strategy probabilities (for prior computation — marginalize over all strategies)
float strategy_probs[kMaxStrategies];
memcpy(strategy_probs, strategy_logits_buf, n_strategy * sizeof(float));
softmax_inplace(strategy_probs, n_strategy);

// Helper: compute model density for a placement, marginalizing over strategies
// model_density = sum_s strategy_prob[s] * multinomial_density(placement | country_probs[s])
auto model_density = [&](const std::vector<CountryId>& targets) -> double {
    double density = 0.0;
    for (int s = 0; s < n_strategy; ++s) {
        density += strategy_probs[s] *
            multinomial_probability(targets, country_probs[s], cache.influence, ops, n_country);
    }
    return density;
};

// Helper: add allocation if unique (prior computed later after normalization)
auto try_add = [&](AllocationResult&& ar, int strat) -> bool {
    if (seen_hashes.count(ar.hash)) return false;
    double density = model_density(ar.targets);
    seen_hashes.insert(ar.hash);
    allocations.push_back({
        ActionEncoding{card_id, ActionMode::Influence, std::move(ar.targets)},
        density,  // unnormalized — will be normalized to sum to card_prob*mode_prob
        ar.hash
    });
    return true;
};

// --- All-deterministic fast path (T_s=0, T_c=0, K>1) ---
// Edge 0: argmax strategy, proportional. Edges 1+: per-strategy proportional.
// Remainder: T_c=1.0 multinomial fallback (need randomness).
if (T_s == 0.0f && T_c == 0.0f) {
    // Edge 0: argmax strategy
    int best_s = pick_strategy(local_rng);
    try_add(make_allocation(best_s, local_rng), best_s);

    // Per-strategy deterministic for remaining strategies
    for (int s = 0; s < n_strategy && allocations.size() < influence_samples; ++s) {
        if (s == best_s) continue;
        try_add(make_allocation(s, local_rng), s);
    }

    // Fill remainder with T_c=1.0 multinomial (override T_c temporarily)
    int max_retries = 3 * influence_samples;
    int retries = 0;
    while (allocations.size() < influence_samples && retries++ < max_retries) {
        // Sample strategy uniformly (T_s fallback = 1.0)
        float uniform_logits[kMaxStrategies];
        for (int s = 0; s < n_strategy; ++s) uniform_logits[s] = strategy_logits_buf[s];
        softmax_inplace(uniform_logits, n_strategy);
        int s = categorical_sample(uniform_logits, n_strategy, local_rng);
        auto ar = multinomial_sample(country_probs[s], cache.influence, ops, n_country, 1.0f, local_rng);
        try_add(std::move(ar), s);
    }
}
// --- General path (at least one T > 0) ---
else {
    int max_retries = 3 * influence_samples;
    int retries = 0;
    while (allocations.size() < influence_samples && retries++ < max_retries) {
        int s = pick_strategy(local_rng);
        auto ar = make_allocation(s, local_rng);
        if (!try_add(std::move(ar), s)) continue;
        // On success, retries doesn't increment (only on collision)
        // Actually retries always increments to bound total attempts
    }
}
```

**How `proportional_first` works with K>1:**

Say K=8, T_s=1.0, T_c=1.0, prop_first=true, n_strategy=4:
- Edge 0: sample strategy → say s=2. First time seeing s=2 → proportional allocation.
- Edge 1: sample strategy → say s=0. First time → proportional.
- Edge 2: sample strategy → say s=2 again. Already has proportional → multinomial at T_c.
- Edge 3: sample strategy → say s=1. First time → proportional.
- Edges 4-7: all strategies have their proportional → all use T_c multinomial.

This gives up to n_strategy "best guess" anchors plus K-n_strategy exploratory samples.

### Prior computation for UCB

Every edge needs a prior for PUCT/UCB selection. Each placement's model density
marginalizes over ALL strategies (not just the one that generated it):

```
model_density_k = sum_s  strategy_prob[s] * multinomial_density(placement_k | country_probs[s])
```

where:
- `strategy_prob[s]` = softmax(strategy_logits)[s] — learned mixing weight
- `multinomial_density(...)` = `ops! / prod(count_i!) * prod(p_i^count_i)`

The K densities only cover a subset of all possible placements, so they won't sum
to 1. Normalize across the K edges:

```
placement_prior_k = model_density_k / sum_j(model_density_j)   // sums to 1 across K edges
edge_prior_k = card_prob * mode_prob * placement_prior_k
```

This ensures:
- The K influence edges' priors sum to exactly `card_prob * mode_prob`
- High-density placements get proportionally more prior (PUCT explores them first)
- The formula is uniform for ALL allocations — proportional, per-strategy, or sampled

Note: `multinomial_density` always uses the RAW (unscaled) `country_probs[s]`, not
temperature-distorted ones. Temperature affects which placements are *generated*,
not how they're *evaluated*.

### Step 4: Normalize priors and add edges to tree

```cpp
// Normalize: K densities → sum to 1, then scale by card_prob * mode_prob
double density_sum = 0.0;
for (auto& alloc : allocations) density_sum += alloc.prior;

double influence_total_prior = card_prob * mode_prob;
for (auto& alloc : allocations) {
    double normalized_prior = (density_sum > 0.0)
        ? influence_total_prior * alloc.prior / density_sum
        : influence_total_prior / allocations.size();  // fallback: uniform

    node->edges.push_back(MctsEdge{
        .action = ActionEncoding{card_id, ActionMode::Influence, {}},
        .prior = static_cast<float>(normalized_prior),
    });
    node->children.emplace_back(nullptr);
    node->applied_actions.push_back(std::move(alloc.action));
    total_prior += normalized_prior;
}
```

Note: the `edge.action` stays with empty targets (consistent with current behavior for
matching visit-count aggregation). The resolved targets are in `applied_actions` (used
when actually stepping the game state in the tree).

## Helper functions to add

All should be `inline` or `static` functions in the anonymous namespace in `mcts_batched.cpp`.

### `proportional_allocation`

Extract the existing lines 754-779 into a function:

```cpp
struct AllocationResult {
    std::vector<CountryId> targets;
    uint64_t hash;
};

AllocationResult proportional_allocation(
    const float* probs,          // softmaxed country probs, length n_country
    const std::vector<CountryId>& accessible,  // legal influence countries
    int ops,
    int n_country
);
```

Same logic as current: multiply probs by ops, floor, distribute remainder by largest
fractional part. Compute hash as `sum of count[i] * kZobrist[country_id_i]`.

Build targets as current: for each country with count > 0, push `count` copies of
country_id. **Sort targets by country_id** for canonical ordering.

### `multinomial_sample`

```cpp
AllocationResult multinomial_sample(
    const float* probs,            // softmaxed country probs for ONE strategy
    const std::vector<CountryId>& accessible,
    int ops,
    int n_country,
    float temperature,             // >0; raises probs to 1/T then renormalizes
    Pcg64Rng& rng
);
```

For each of `ops` points, sample a country from the temperature-scaled distribution:
- Scale: `scaled_prob[c] = pow(probs[c], 1.0/T)` for accessible countries, renormalize
- Build CDF over accessible countries
- For each op: draw `u = rng.next_u32() / 2^32`, binary search CDF for country
- Accumulate counts per country, build targets + hash

Note: T=1.0 uses the raw softmax distribution. T<1 sharpens (more greedy). T>1 flattens.

**Important**: the `multinomial_probability` helper always uses the RAW (unscaled)
country_probs for density computation — temperature only affects the sampling process,
not the prior. The prior should reflect "how likely is this placement under the model's
learned distribution?", not "how likely is it under the temperature-distorted distribution?".

### `categorical_sample`

```cpp
int categorical_sample(const float* probs, int n, Pcg64Rng& rng);
```

Sample from a discrete distribution (used for strategy selection at T>0).
Draw `u = rng.next_u32() / 2^32`, scan CDF, return index.

### `multinomial_probability`

```cpp
double multinomial_probability(
    const std::vector<CountryId>& targets,  // the allocation (repeated country_ids)
    const float* strategy_probs,            // softmaxed country distribution for the
                                            // strategy that generated this allocation
    const std::vector<CountryId>& accessible,
    int ops,
    int n_country
);
```

Compute: `ops! / prod(count_i!) * prod(p_i ^ count_i)` where `count_i` is number of ops
in country i and `p_i` is `strategy_probs[country_id_i]` (re-normalized over accessible).

Use log-space to avoid overflow: `exp(log_factorial(ops) - sum(log_factorial(count_i)) + sum(count_i * log(p_i)))`.

Pre-compute small factorials (max ops = 5, so max factorial = 120). Or just use a
lookup table.

### Zobrist table

```cpp
static const std::array<uint64_t, 86> kInfluenceZobrist = []() {
    std::array<uint64_t, 86> table{};
    // Use a fixed seed unrelated to game RNG
    Pcg64Rng zobrist_rng(0xDEADBEEF42ULL);
    for (int i = 0; i < 86; ++i) {
        table[i] = zobrist_rng.next_u64();
    }
    return table;
}();
```

Hash of allocation = `sum over each op placed: kInfluenceZobrist[country_id]`.
For country c receiving n ops: contributes `n * kInfluenceZobrist[c]`.

## When influence_samples == 1 AND influence_temperature == 0

Skip all the above. Use the existing code path exactly (argmax strategy, proportional
allocation, single edge). This ensures bit-identical behavior and zero overhead for
existing users.

When K=1 but any T>0: use the new path to generate 1 allocation (no dedup needed).

Guard:
```cpp
if (edge.mode == ActionMode::Influence && country_logits_ptr != nullptr && !cache.influence.empty()) {
    if (config.influence_samples > 1 || config.influence_t_strategy > 0.0f || config.influence_t_country > 0.0f) {
        // K-sample / temperature path (new code)
    } else {
        // existing single-allocation path (unchanged, bit-identical)
    }
}
```

## Edge count impact

With K=8 and ~8 playable cards, each having an Influence mode: up to 64 additional edges
per expansion. Current coup/realign already produce 30-50 edges per card. Total node fan-out
goes from ~100-200 to ~150-250. Manageable.

## Constraints

- **No engine changes.** `ActionEncoding`, `GameState`, stepping — all unchanged.
- **No Python changes.** Model, dataset, training, bindings — all unchanged.
- **No binding changes** unless the user adds `--influence-samples` to Python benchmark later.
- **Backward compatible.** All defaults (`T_s=0, T_c=0, K=1`) = bit-identical to current.
- **Deterministic** given the same `Pcg64Rng` state. The new path bootstraps a local
  RNG from exactly 1 `rng.next_u64()` call, so main RNG advances by exactly 1
  regardless of K or retry count. At defaults (T_s=0, T_c=0, K=1) the new path is
  never entered → main RNG untouched → bit-identical.
- Do NOT add influence config to the `benchmark_mcts` Python binding or the
  `benchmark_batched` binding — we will add that separately if the feature works.
  Only wire it through `collect_mcts_games_jsonl.cpp` CLI.

## Test plan

### Unit tests (add to `tests/cpp/test_mcts.cpp` or new `test_influence_samples.cpp`)

**T1. Zobrist hash correctness**
- Verify `hash([A, A, B]) == hash([B, A, A]) == hash([A, B, A])` (order-invariant)
- Verify `hash([A, A, B]) != hash([A, B, B])` (different multisets differ)
- Verify `hash([A]) != hash([B])` for A ≠ B
- Verify `hash([A, A]) == 2 * kZobrist[A]`

**T2. Proportional allocation determinism**
- Given fixed country_probs and ops=3, call `proportional_allocation` twice
- Verify identical targets and hash both times

**T3. Multinomial probability correctness**
- Hand-compute multinomial density for a simple case: 2 countries, 3 ops,
  probs = [0.7, 0.3], allocation = [A, A, B]
- Expected: `3! / (2! * 1!) * 0.7^2 * 0.3^1 = 3 * 0.49 * 0.3 = 0.441`
- Verify `multinomial_probability` returns 0.441 ± 1e-6

**T4. Multinomial probability sums to 1**
- For 2 countries and ops=3, enumerate all 4 possible allocations:
  [A,A,A], [A,A,B], [A,B,B], [B,B,B]
- Verify their multinomial probabilities sum to 1.0 ± 1e-6

**T5. Prior normalization**
- Run K-sample expansion on a synthetic node with known card_prob and mode_prob
- Verify sum of K influence edge priors == card_prob * mode_prob ± 1e-6

**T6. Dedup correctness**
- Set K=100 with very peaked distribution (one country has prob 0.99)
- Most samples should collide → actual edges << 100
- Verify no duplicate hashes in the output

**T7. Proportional-first flag**
- With prop_first=true, K=8, T_s=1.0, T_c=1.0:
  - For each strategy that appears, verify its first allocation matches
    `proportional_allocation(country_probs[s], ...)` exactly
  - Verify subsequent allocations from same strategy differ (with high prob)
- With prop_first=false: no such guarantee

**T8. All allocations are legal**
- For every allocation generated, verify:
  - len(targets) == ops
  - All target country_ids are in cache.influence (legal countries)

### Integration tests

**T9. Bit-identical at defaults**
- Run `benchmark_batched` (default config, influence_samples=1) with fixed seed
- Compare game-by-game winners against a golden reference (captured before the change)
- Must be identical

**T10. K=8 smoke test**
- Run `ts_collect_mcts_games_jsonl --model <path> --games 10 --n-sim 50
  --influence-samples 8 --influence-t-strategy 1.0 --influence-t-country 1.0
  --out /tmp/test_k8.jsonl`
- Must complete without crash or assertion failure
- Output JSONL must be valid (parseable, all games complete)

**T11. Determinism with K>1**
- Run the same collection command twice with same seed
- Verify byte-identical output (same local_rng seed → same allocations)

**T12. Temperature effects (statistical)**
- Run 100 expansions with T_c=0.01 (near-deterministic): verify >90% of allocations
  match proportional allocation
- Run 100 expansions with T_c=100.0 (near-uniform): verify country distribution
  has entropy > 90% of maximum entropy
- Run with T_s=0: verify all allocations use argmax strategy
- Run with T_s=100.0: verify all 4 strategies appear (with high prob over 100 trials)

**T13. Edge count distribution**
- Run 50 games with K=8, count influence edges per expansion
- Report min/median/max. Expect median > 4 (most positions have enough legal
  countries to generate diverse allocations)

### RNG isolation test

**T14. Main RNG unaffected by K**
- Run a game with K=1 (new path not entered). Record main RNG state after expansion.
- Run same game with K=8. Record main RNG state after the SAME expansion.
- Main RNG should have advanced by exactly 1 more u64 in the K=8 case
  (the bootstrap call), regardless of how many samples/retries happened.

## Acceptance criteria

- [ ] T1-T8 unit tests pass
- [ ] T9: bit-identical at defaults (golden reference match)
- [ ] T10: K=8 smoke test completes without errors
- [ ] T11: deterministic output with same seed
- [ ] T12: temperature effects are directionally correct
- [ ] T14: main RNG isolation verified
- [ ] All existing tests: `ctest --test-dir build-ninja --output-on-failure` green
- [ ] CLI flags `--influence-t-strategy`, `--influence-t-country`,
  `--influence-samples`, `--[no-]influence-proportional-first` added to
  `collect_mcts_games_jsonl`
- [ ] Existing benchmarks/bindings unaffected (default values)
