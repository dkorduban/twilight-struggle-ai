# Opus Analysis: ISMCTS Root-Cause Strategy
Date: 2026-04-18 04:15:56 UTC
Question: Design a root-causing strategy for the ISMCTS investigation. Two symptoms:

SYMPTOM 1 (crash): `free(): invalid pointer` when running `scripts/ismcts_sweep_vs_self.py` at the
final config (`n_det=16, n_sim=100, pool=16, max_pending_per_det=8`) at N=20/side. Crash happens
after the USSR half completes, during the transition to the US half (pool/batch_inputs destruction
or second-half init). Crash is intermittent/scale-dependent: fresh-process single-config at N=10
runs clean (4 variants tested). ASAN-instrumented single-config at N=5 runs for 12+ min (7x
overhead) which makes systematic ASAN testing impractical.

SYMPTOM 2 (search net-negative vs greedy): At `n_det=4, n_sim=50` on same-seed paired games N=50
USSR: greedy NN wins 27/50, ISMCTS wins 5/50. 23 wins flipped to losses, 1 loss rescued. Budget
sweep (50 to 1600 rollouts) shows NO correlation between budget and WR (flat 32-42% combined vs
greedy-self). Post-fix ISMCTS vs heuristic also weak (13% combined) while greedy NN vs heuristic is
51%.

## Executive Summary
Two concrete, code-specific root causes already jump out of the source and explain both symptoms
without further experimentation: (1) a heap use-after-free (UAF) in
`ismcts.cpp:RawBatchOutputs::extract` that is missing the `_storage` tensor fields present in the
identical construct in `mcts_batched.cpp`, and (2) root Dirichlet noise (alpha=0.2, epsilon=0.25)
is unconditionally applied inside every ISMCTS benchmark path because `MctsConfig` defaults are
never zeroed for eval. Strategic priority for *the project* is SYMPTOM 2 (a search that loses more
than greedy is worthless even if it never crashes); debugging priority is SYMPTOM 1 first because
UB can silently taint any measurement taken for SYMPTOM 2. The whole investigation is closable
within a short session: two ~10-line code fixes plus two short reruns of existing scripts.

## Findings

### 1. Both symptoms have a strong primary hypothesis already visible in the code

#### 1.1 SYMPTOM 1 primary: dangling pointers in `RawBatchOutputs::extract` (ismcts.cpp)

`cpp/tscore/ismcts.cpp:553-614` defines `RawBatchOutputs` with raw `const float*` pointers only:

```cpp
struct RawBatchOutputs {
    const float* card_logits = nullptr;
    ...
    static RawBatchOutputs extract(const nn::BatchOutputs& outputs) {
        RawBatchOutputs raw;
        auto cont_card = outputs.card_logits.contiguous();  // LOCAL
        raw.card_logits = cont_card.data_ptr<float>();       // pointer into local
        ...
        return raw;                                          // cont_card destroyed
    }
};
```

Contrast with the identical construct at `cpp/tscore/mcts_batched.cpp:441-510`, which has
`torch::Tensor *_storage` fields for every raw pointer and even documents this:

```cpp
// Storage tensors keep the contiguous data alive across barriers.
torch::Tensor card_logits_storage;
const float* card_logits = nullptr;
...
raw.card_logits_storage = outputs.card_logits.contiguous();
raw.card_logits = raw.card_logits_storage.data_ptr<float>();
```

Why doesn't the ISMCTS version always crash?
- When `outputs.card_logits` is already contiguous, `.contiguous()` returns the same tensor
  (shared storage). `cont_card` holds one refcount; its destruction drops refcount by 1 but the
  caller still holds `outputs`, so storage is kept alive. Raw pointer stays valid.
- When `.contiguous()` has to materialize (non-contiguous tensor, e.g. from certain TorchScript
  graphs, odd reshapes, or `.cpu()` transfer paths that happen to return non-contiguous tensors),
  the new tensor is held only by `cont_card`. When `cont_card` dies at function return, the
  storage is freed. `raw.*_logits` now dangles.

Why it manifests as scale-dependent crash:
- With small batches, glibc often keeps freed chunks on the tcache and reads may return stale but
  benign data; the process doesn't crash.
- With large batches (`pool=16 * n_det=16 * max_pending=8 = 2048` slots, avg_batch 1187 observed),
  output tensors are large, heap allocator churn is heavy, and once a freed tensor block is handed
  to a new allocation its pointer now aliases a chunk with different glibc metadata. First `free`
  on that chunk later trips `free(): invalid pointer` — exactly the observed signature.
- The crash hits at the USSR → US boundary because that's when the per-call `pool`, `batch_inputs`,
  and `batch_entries` objects are destroyed (`play_ismcts_vs_model_pooled` returns in
  `benchmark_ismcts_vs_model_both_sides`, bindings/tscore_bindings.cpp:1309-1314), which runs
  destructors on all the pending node subtrees and any leftover raw-pointer-consuming structures.

Evidence fits every observed property of the crash: scale-dependent, intermittent, survivable in
short runs, manifests during destruction.

#### 1.2 SYMPTOM 2 primary: root Dirichlet noise is on during evaluation

`cpp/tscore/mcts.hpp:44-54`:
```cpp
struct MctsConfig {
    int n_simulations = 200;
    float c_puct = 1.5f;
    float dir_alpha = 0.2f;
    float dir_epsilon = 0.25f;
    ...
};
```

`cpp/tscore/ismcts.hpp:17-21`:
```cpp
struct IsmctsConfig {
    int n_determinizations = 8;
    int max_pending_per_det = 8;
    MctsConfig mcts_config;    // default-initialized => noise ON
};
```

The three benchmark bindings (`benchmark_ismcts`, `benchmark_ismcts_vs_model`,
`benchmark_ismcts_vs_model_both_sides`, bindings/tscore_bindings.cpp:1194-1331) set
`n_determinizations`, `max_pending_per_det`, and `n_simulations`, and do not zero the Dirichlet
parameters. `play_ismcts_vs_model_pooled` calls `apply_root_dirichlet_noise(*det.root, ...)`
unconditionally for each determinization (ismcts.cpp:2246, 2296).

At epsilon=0.25, the root prior is mixed as `0.75*prior + 0.25*Dirichlet`. With 4-16
determinizations, noise is resampled independently per-det, so inter-det aggregation does not
average out noise (each det explores a different noise realisation; argmax-by-visits is dominated
by whichever noisy prior + value draw wins). At 50-200 sims per det, the visit count distribution
is dominated by priors, priors are 25% Dirichlet. Result: search argmax is close to "sample from
(0.75 * NN prior + 0.25 * Dirichlet)". Greedy argmax sees 0% noise. Directly explains why search
flips 23/50 wins to losses: 25% of the time, picks a noise-boosted non-argmax action.

#### 1.3 Why the budget sweep is flat (what neither primary hypothesis fully explains)

Dirichlet noise should average out as sims per det grow. The sweep at n_det=4 goes from 25 → 100
sims/det (100 → 400 total rollouts) and WR is flat 32-42%. That plateau is the most informative
unresolved signal: it says search has a **second** mechanism hurting it, OR the value-head feedback
in determinized states is so biased that even a clean search converges to a bad edge.

Three candidates:

**(a) UAF contamination.** The same UAF lives in the ISMCTS path. For longer runs the dangling
pointer sometimes returns post-free data that changes actual leaf values fed into PUCT; visit
trajectories then diverge on noise. This would explain both symptoms and the flatness
simultaneously: fixing the UAF would not just stop crashes, it would make higher budgets actually
correlate with stronger play.

**(b) Opponent-model mismatch.** Tree rollouts sample opponent moves from the NN policy. Against a
heuristic opponent, the fictional NN opponent is systematically overaggressive in some modes
(e.g. DEFCON brinksmanship, or different coup/realign priors). FINDINGS.md already discusses this.
But it cannot explain flat-vs-self since the opponent *is* NN-greedy there.

**(c) Value-head miscalibration on determinized states.** The NN value head was trained on true
public+own-hand states. ISMCTS feeds it full determinized states which include hallucinated
opponent hands. If the value head's error on hallucinated hands is biased rather than zero-mean,
search will consistently over- or under-weight particular subtrees and not converge.

(a) and (c) are symmetric across sides, (b) is asymmetric; the vs-self flatness argues for (a) or
(c). (a) and (b) are the two cheapest to probe.

### 2. Priority argument: which symptom first

**User-value priority:** SYMPTOM 2. A benchmark search that's worse than greedy at 1600 rollouts is
strictly negative — it costs 4x time for worse play. Even if we ship a crash fix, nobody would want
to run the search.

**Debug-order priority:** SYMPTOM 1 first, *but fixes* should land together in a single PR.
Reason: the UAF is undefined behavior. Any measurement of search quality taken while UAF is live
cannot be trusted — memory at those pointers may contain either correct post-`.contiguous()` data
(when the tensor was already contiguous) or arbitrary garbage. SYMPTOM 2's observed numbers may
change after the UAF fix. You must fix UAF *before* re-measuring search quality.

Practical consequence: fix UAF first (cheap, ~10 lines), re-run the same SYMPTOM-2 diagnostics,
*then* decide how much of SYMPTOM 2 remains.

### 3. Enumerated root causes with cheap probes

#### SYMPTOM 1 (crash), ranked by prior probability

1. **UAF in `RawBatchOutputs::extract` (ismcts.cpp:553-614)** — ~85% prior.
   *Probe:* Mirror the `_storage` Tensor pattern from `mcts_batched.cpp:441-510` into
   `ismcts.cpp`. Rebuild with `nice -n 15 cmake --build build-ninja -j4`. Rerun the original
   crasher config `scripts/ismcts_sweep_vs_self.py` (N=20/side, n_det=16, n_sim=100, pool=16).
   No ASAN needed. Pass = fixed.

2. **Raw-pointer lifetime bug elsewhere on the hot path** — ~10%. `BatchEntry` stores raw
   `IsmctsGameSlot*` and `DeterminizationSlot*`. The `pool` vector is sized once at start and
   never resized (ismcts.cpp:2190), and `slot.dets` is reserve()'d then filled without subsequent
   grow (ismcts.cpp:1707-1723). But if *any* path mutates `pool` or `slot.dets` between
   `queue_batch_item` (which pushes `BatchEntry{.det = &det, ...}`) and batch processing, the
   pointer is stale. `commit_selected_action` calls `reset_search(slot)` which does
   `slot.dets.clear()`. If any codepath reaches `commit_selected_action` inside the same outer
   iteration as `batch_entries` still containing entries, dangling.
   *Probe:* Add a debug assertion at the top of the batch-processing block:
   `assert(batch_entries.empty() || all slots have search_active && dets.size() == n_det)` — or
   simpler, temporarily sanity-check that no `dets.clear()` happens between `batch_entries` push
   and batch processing within one while-loop iteration. Run existing crash repro. Low effort.

3. **TorchScript `.cpu()` move returning non-contiguous tensor** — a special case of (1) but worth
   calling out since it's the trigger condition. *Probe:* already subsumed by the (1) fix.

4. **Double-free in GameState clone / MctsNode tree destruction at pool reuse** — ~3%. `pool`
   slots are reused by overwriting `slot = IsmctsGameSlot{}` in `initialize_game_slot`
   (ismcts.cpp:1018). That invokes the destructor on the prior slot's dets/trees; if any tree
   contains aliased child pointers we'd see double-free. The vector-of-unique_ptr pattern makes
   this unlikely but not impossible.
   *Probe:* After (1) fix, if the crash persists, run with `-DMALLOC_CHECK_=2` in env — cheap
   glibc malloc checking, far lighter than ASAN. Typically 1.2-1.5x overhead.

5. **TorchScript internal pool / thread-local state leaking across calls at scale** — ~2%. The
   crash at the USSR→US boundary coincides with the second `torch::jit::load` call. *Probe:*
   Load both models once at binding level (refactor
   `benchmark_ismcts_vs_model_both_sides` to load once). If crash disappears, blame TorchScript.
   Diagnostic only — cheap to do, ~20 lines.

#### SYMPTOM 2 (search net-negative), ranked by prior probability

1. **Root Dirichlet noise on during eval** — ~70% prior for a large chunk of the gap.
   *Probe:* Either (a) add `dir_alpha`/`dir_epsilon` kwargs to the three ISMCTS bindings,
   defaulting to 0.0, or (b) temporarily hardcode in `play_ismcts_vs_model_pooled` /
   `play_ismcts_matchup_pooled` with a local `IsmctsConfig` copy that zeros both. Rebuild. Rerun
   `scripts/ismcts_policy_agreement.py` (N=50 USSR). If 10% → e.g. 35-50% that's most of the bug.
   ~3 min runtime.

2. **Flat-vs-budget residual: UAF polluting leaf values** — ~40% of *remaining* gap after (1).
   Dirichlet noise averages out with sims; the flatness past 400 rollouts is the fingerprint of
   something non-averaging. UAF returning garbage floats to `evaluate_leaf_value_raw` is exactly
   such a mechanism.
   *Probe:* Already tested by the SYMPTOM-1 fix. After (1.1)+(1.2) fixes, rerun the budget sweep
   at (2,25), (4,50), (4,100), (8,100). If WR now monotonically improves (or at least ceases to
   be flat) then UAF was a significant SYMPTOM-2 driver.

3. **Opponent-model mismatch (tree assumes NN-greedy)** — ~70% of vs-heuristic gap but ~0% of
   vs-self gap. Already discussed in FINDINGS.md section "Remaining gap".
   *Probe:* Compare (post-fix) vs-self WR at high budget to (post-fix) vs-heuristic WR at the
   same budget. If vs-self converges to ~50% and vs-heuristic plateaus below 40%, structural
   mismatch confirmed. Already have `benchmark_ismcts` and `benchmark_ismcts_vs_model_both_sides`
   for this.

4. **Visit-argmax at low visit counts picks prior-argmax rather than value-argmax** — ~20%.
   With small budget per determinization (50-100 sims spread over O(20-40) root edges), many
   edges get 1-3 visits. `aggregated_edge_better` picks by visit count, breaking ties by prior.
   An edge with high prior and bad value may still win on visits alone before value propagates.
   *Probe:* Modify `aggregate_result` to emit top-5 (action, visits, mean_value, prior) per
   decision into a debug log. Pick 10 root positions at random. Manually compare to NN-argmax.
   Cheap because you already have the data structures.

5. **Value-head miscalibration on determinized full states** — ~15%. Requires more work to probe
   (needs an offline experiment comparing value-head output on true vs determinized hands), so
   defer unless (1)-(4) don't close the gap.

6. **Incorrect Dirichlet alpha for this action-space fanout** — ~5%. alpha=0.2 is AlphaZero's
   default for Go's ~200-action fanout. TS has more like 20-50 legal actions at a typical root.
   A smaller alpha would be more appropriate, but this is a tuning detail that only matters if
   (1) is rejected rather than removed; if noise is off during eval, this is moot.

### 4. Execution order

**Step 0 (0 min):** Read this document and FINDINGS.md. Decide on two-commit or single-commit
strategy for the fixes. Recommend single commit: both fixes are small, both are "always wrong"
rather than "tuning", both block re-measuring the same diagnostic.

**Step 1 (10 min): UAF fix.** Edit `cpp/tscore/ismcts.cpp:553-614` to mirror the `_storage`
Tensor field pattern from `cpp/tscore/mcts_batched.cpp:441-510`. Build:
```
nice -n 15 cmake --build build-ninja -j4
```
Smoke-test with existing unit tests:
```
uv run pytest tests/python/test_ismcts.py -n 0
ctest --test-dir build-ninja --output-on-failure -R ismcts
```

**Step 2 (3 min): Crash repro.** Rerun the original crasher:
```
uv run python scripts/ismcts_sweep_vs_self.py 2>&1 | tee results/ismcts_fix/sweep_vs_self_post_uaf.txt
```
Success: all 6 rows complete including (16, 100) row. Takes ~18 min on this hardware based on the
prior run going up to n_det=8/n_sim=100 at 452s.

**Step 3 (5 min): Dirichlet fix.** Add `dir_alpha: float = 0.0, dir_epsilon: float = 0.0`
kwargs to the three ISMCTS bindings (`bindings/tscore_bindings.cpp:1194-1331`). Write them into
`config.mcts_config.dir_alpha` / `dir_epsilon`. Rebuild.

**Step 4 (3 min): SYMPTOM-2 re-measurement with both fixes live.**
```
uv run python scripts/ismcts_policy_agreement.py 2>&1 | tee results/ismcts_fix/policy_agreement_post_fix.txt
```
Expect: ISMCTS USSR WR climbs from 10% materially; net-win-flip goes from -22 toward 0 or better.
If it hits ≥40%, primary bug of SYMPTOM 2 is also identified.

**Step 5 (~25 min): Budget sweep with both fixes.**
```
uv run python scripts/ismcts_sweep_vs_self.py 2>&1 | tee results/ismcts_fix/sweep_vs_self_post_fix.txt
```
Expect: monotonic or at least ceiling-approaching WR as budget grows. If still flat, open the
"value-head miscalibration on determinized states" branch — that's a bigger investigation.

**Step 6 (5 min): vs-heuristic re-measurement.**
```
uv run python scripts/ismcts_validate.py 2>&1 | tee results/ismcts_fix/validate_n50_post_fix.txt
```
This is the honesty check: if vs-self is now healthy but vs-heuristic is still 13%-ish, the
opponent-model-mismatch hypothesis is confirmed and the remaining gap is out of scope for a pure
fix. If vs-heuristic also climbs close to the 51% greedy ceiling, even better.

**Step 7: Commit, update FINDINGS.md, close tasks.**

### 5. Dead-ends to avoid

1. **ASAN on a 40-game crasher.** 7x overhead × ~450s = ~52 min per run, and scale-dependent heap
   reuse often evades ASAN's quarantine list. Already explicitly deprioritized in FINDINGS.
   Skip entirely in favor of the source-diff comparison.

2. **Valgrind on the same.** Even slower than ASAN (10-30x). Same issue.

3. **Searching for more hypotheses via more runs before fixing what you already have.** The UAF
   and Dirichlet findings are source-grounded (not log-grounded). Additional sweeps while UAF is
   live produce untrustworthy numbers. Diminishing returns.

4. **"Train a better value head for determinized states"** or other offline architectural rework.
   Out of scope for Month 3. Only revisit if both fixes leave a major gap.

5. **Tuning n_det / n_sim / c_puct / pool_size without fixing the two bugs first.** You'd just be
   tuning noise superposition on top of broken memory and degraded priors.

6. **Rewriting the ISMCTS outer loop for thread-safety or determinism.** No evidence these are
   broken; the symptoms are fully explained by the two known bugs.

7. **Chasing "intermittent crash" as if it's nondeterministic.** Given the source diff, it's
   deterministic UB whose observable effect depends on allocator state — which is effectively
   random from the caller's perspective but fully explainable once the UAF is gone.

### 6. Success criteria

Close the investigation when **all three** hold:

1. **Crash gone.** Original crasher config (`n_det=16, n_sim=100, pool=16, max_pending=8`, N=20/
   side) completes without error in a fresh process. Optionally verify at N=40 or N=60 for extra
   confidence.

2. **Search is net-positive vs self.** ISMCTS vs greedy-self combined WR ≥ 50% at *some* budget
   ≥ 400 rollouts. "≥ 50%" = search is at least breakeven vs pure greedy of the same model.
   Bonus if monotonic budget scaling is restored.

3. **vs-heuristic gap is explained.** Either ISMCTS vs heuristic combined WR comes within 10pp of
   the 51% greedy ceiling (fixed), OR FINDINGS.md is updated to cite this as confirmed structural
   opponent-model mismatch with the three mitigations listed and the issue is explicitly out of
   scope for this fix pass.

If (1) and (3) hold but (2) plateaus below 50%, do NOT declare victory. That's the
value-head-on-determinized-states branch opening up and the investigation needs to continue there
instead of getting prematurely closed.

## Conclusions

1. The observed crash (SYMPTOM 1) has a strong, source-visible root cause: `RawBatchOutputs` in
   `cpp/tscore/ismcts.cpp:553-614` stores raw `float*` pointers without keeping the underlying
   contiguous Tensors alive. The sibling implementation in `cpp/tscore/mcts_batched.cpp:441-510`
   does exactly this correctly (`_storage` Tensor fields). This is a 10-line fix by transplant.

2. The observed search-quality regression (SYMPTOM 2) has a strong, source-visible root cause:
   `IsmctsConfig::mcts_config` default-initializes to `MctsConfig{ dir_alpha=0.2, dir_epsilon=
   0.25 }`, and none of the three ISMCTS benchmark bindings zero these for eval. Root Dirichlet
   noise is active during every ISMCTS benchmark. This is ~10 lines of binding kwargs plus
   defaults.

3. Project-impact priority is SYMPTOM 2 (a losing search is unshippable); debug-order priority is
   SYMPTOM 1 because UB can silently distort SYMPTOM-2 measurements. Both fixes are cheap enough
   to land together.

4. The flat-WR-across-budget observation is the most important residual signal. It's not
   explained by Dirichlet alone (noise averages out). It IS consistent with UAF contaminating
   leaf values; if it persists after both fixes, promote the "value-head miscalibration on
   determinized states" hypothesis.

5. ASAN/valgrind on the full crasher is not worth the time given the source-grounded hypothesis.
   Skip.

## Recommendations

1. **Land both fixes in one commit.** Mirror `_storage` Tensor fields from `mcts_batched.cpp` into
   `ismcts.cpp:RawBatchOutputs`; add `dir_alpha`/`dir_epsilon` kwargs (default 0.0) to
   `benchmark_ismcts`, `benchmark_ismcts_vs_model`, `benchmark_ismcts_vs_model_both_sides`.
   Rebuild.

2. **Rerun, in order, with both fixes live:**
   - `scripts/ismcts_sweep_vs_self.py` (crash + budget scaling check).
   - `scripts/ismcts_policy_agreement.py` (net search value check).
   - `scripts/ismcts_validate.py` (vs-heuristic check).
   Save all outputs under `results/ismcts_fix/*_post_fix.txt`.

3. **Update `results/ismcts_fix/FINDINGS.md`** with the two new root causes, the post-fix numbers,
   and whichever of the three success criteria each result satisfies.

4. **If the budget sweep is still flat after both fixes,** open a separate investigation on
   value-head behavior under determinization. Probe: evaluate `v55_scripted.pt`'s value head at
   ~100 true-hand states vs. the same public state with 10 hallucinated determinizations each;
   measure value variance across determinizations and bias vs true-hand value. If bias is large,
   that's the remaining lever and it needs a training-side fix (e.g. train on determinized
   observations, or use MC rollouts with heuristic policy at leaves to side-step the value head).

5. **If vs-heuristic stays weak while vs-self recovers,** do not chase it further in this pass.
   FINDINGS.md already documents it as structural opponent-model mismatch. Punt to a follow-up
   task explicitly labeled "ISMCTS cross-policy evaluation," and list the three mitigations already
   noted (heuristic opponent-in-tree, heuristic-rollout leaf value, online opponent-type
   detection).

6. **Do not touch** ASAN, valgrind, c_puct tuning, or ISMCTS outer-loop rewrites on this task.

## Open Questions

1. Will fixing the UAF alone change the SYMPTOM-2 numbers measurably (i.e. was any fraction of the
   -22 net-flip attributable to garbage floats in leaf values), or will Dirichlet removal carry
   the entire delta? Cannot tell without running.

2. After both fixes, is budget scaling monotonic or does a plateau remain? This is the key open
   question: the answer selects whether we close the investigation (monotonic → close) or open
   the value-head-on-determinized-states branch (plateau → continue).

3. Is there a path where `.contiguous()` *on a GPU-to-CPU-transferred tensor* can return a
   non-contiguous result? The spec says `.cpu()` returns the same layout, so most outputs are
   contiguous and the UAF is silent. The crash is occurring on CPU-only runs according to the
   script, so the non-contiguity must come from the TorchScript graph itself (e.g. permute or
   transpose in head post-processing). Worth a short look at the TorchScript model export to see
   if a `permute(...)` or `view(...)` step produces non-contiguous outputs.

4. Does any other benchmark path (MCTS vs greedy, dual-model Elo) also carry Dirichlet noise at
   eval? Worth grep'ing the bindings to make sure this isn't silently inflating variance across
   the entire eval suite.

5. If the vs-heuristic gap is structural, at what budget (if any) does the full-heuristic-in-tree
   mitigation (FINDINGS Option 1) close the gap to greedy? This is Month-3 scope only if ISMCTS is
   to be deployed against non-NN opponents.
