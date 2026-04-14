Q:
YOu're a senior staff SWE experienced in C++. Analyze the C++ part of the twilight struggle repo (ignore cpp/mcts_batched_fast/) for the architecture. Some areas that concern me:  
0. code duplication everywhere
1. tight coupling of engine and policies (heuristic, MCTS, ISMCTS)
2. not easy to plug a different policy
3. data collection requires one binary, benchmarking -- another binary, with reimplemented stuff
4. large single source files
5. something else

suggest architectural changes to make it more maintainable, extendable, observable, and easier to develop. keep in mind possible multi-threading in MCTS.

A:
My read: the code has a **good kernel idea** but the architectural boundaries are not actually enforced. The README describes a clean `Board` / `Move` / `Command` / `PhaseMachine` split and swappable policies, but the implementation currently pulls engine, move generation, and concrete players into one `ts_core` library; `Game` is hard-coded to `Player<TestPolicy>`; and search code reaches straight into `Board` plus `PhaseMachine::step`. That is the main reason the code feels duplicated, tightly coupled, and awkward to extend. ([GitHub][1])

On your specific concerns:

**0. Duplication is everywhere, but the deeper problem is that duplication is structural.**
You have repeated boilerplate in the `Move` hierarchy, including many per-subclass `operator==` implementations that rely on `dynamic_cast`; a large centralized `Command` hierarchy made of many tiny state-change classes; and two separate search stacks (`mcts_policy` and `tsnnmcts`) that each define their own node/controller/policy concepts instead of sharing one search core with pluggable evaluation. That means every new rule, policy, or tool tends to copy shape as well as logic. ([GitHub][2])

**1. Engine and policies are tightly coupled in both build layout and runtime API.**
The build graph already tells the story: `ts_core` includes board/phase/actions/game-state code *and* concrete player implementations. At runtime, `Player` is just a thin template forwarding object, but `Game` itself is fixed to `Player<TestPolicy>` and owns the match loop. The MCTS code directly clones `Board`, mutates hidden hands during determinization, and drives transitions by calling `PhaseMachine::step` itself. So policies are not consumers of a stable engine API; they are peers of engine internals. ([GitHub][3])

**2. It is not actually easy to plug in a different policy today.**
The README says `Game/Player` are policy-based and swappable, but the real top-level seam is not `IPolicy`; it is `Game(Player<TestPolicy>, Player<TestPolicy>, ...)`. A new policy can only participate cleanly if it fits the current `Board + vector<shared_ptr<Move>> + Side -> shared_ptr<Move>` contract, and even then `Game` still needs to be compiled around `TestPolicy`. `TsNnMcts` is also still a partial skeleton: its search loop has TODOs and currently expands the root from priors and returns the max-prior move rather than running full search. ([GitHub][1])

**3. Data collection vs benchmarking is likely duplicating because there is no shared runtime layer.**
Right now the authoritative loop is embedded in `Game::next()`, and the build exposes one big library plus tests. There is no explicit reusable “match runner / self-play / benchmark / dataset collector” layer with shared config, seeding, telemetry, and result sinks. In that setup, any binary that needs slightly different control flow will naturally reimplement orchestration around the engine. ([GitHub][3])

**4. The large files are not just long; they are carrying too many responsibilities.**
`game_logic_legal_moves_generator.cpp` is 692 lines, `card_effect_legal_move_generator.cpp` is 421, `phase_machine.cpp` is 414, `mcts_policy.cpp` is 526, and even `move.hpp` / `command.hpp` centralize broad type hierarchies. That is not catastrophic by itself, but in this repo those files are also architectural choke points, so they amplify merge conflicts, slow comprehension, and make localized change harder than it should be. ([GitHub][4])

**5. The bigger issue I would add is architecture drift and hidden global state.**
`Game` calls `CardEffectLegalMoveGenerator::initializeBuiltinGenerators()` in its constructor, and that generator has explicit one-time global registration plus test-only reset hooks. `Board` also exposes a very wide mutable surface (`getDeck`, `getPlayerHand`, `pushState`, mutable trackers, RNG access), which makes invariants hard to police and makes concurrency rely on convention instead of on interfaces. Separately, the source tree contains a standalone `mcts_policy.cpp`, but `ts_core` does not build it; meanwhile `TsNnMctsController::runSearch` still contains TODOs and placeholder behavior. That is a signal that the intended extension path is already drifting from the actual one. ([GitHub][5])

What I would change:

### 1) Split the project into layers and enforce dependency direction

I would break `ts_core` into at least these libraries:

* `ts_domain`: enums, IDs, card metadata, value objects, result types.
* `ts_engine`: `Board`, transition/reducer logic, legal-action generation, terminal evaluation, observation and cloning APIs.
* `ts_rules`: phase handlers and card-rule registration.
* `ts_policy_api`: a small runtime policy interface plus budget/cancellation/telemetry context.
* `ts_search_core`: generic MCTS/ISMCTS/PUCT primitives, tree stats, worker scheduler.
* `ts_runtime`: match runner, self-play, benchmark, tournament, dataset collection.
* `ts_observe`: trace sinks, replay logs, metrics.

The key rule is: **engine must not depend on concrete policies**, and **search core must not depend on Twilight Struggle internals beyond a narrow game adapter**. That directly addresses the current “one library owns everything” problem. ([GitHub][3])

### 2) Replace the top-level template seam with a runtime policy seam

Do not make `Game` templated or hard-coded to `TestPolicy`. Make the top-level orchestration object a `MatchRunner` that owns an engine instance and two `IPolicy` objects. Keep templates only behind adapters if you want zero-overhead in local implementations.

The policy boundary should look conceptually like this:

* input: observation, legal actions, side to move, budget, telemetry handle
* output: `ActionId`
* optional lifecycle hooks: `on_match_start`, `on_transition`, `on_match_end`

That would also let you finally support lifecycle hooks cleanly; `Game::next()` already has a TODO for calling `Player::onGameEnd`. ([GitHub][6])

### 3) Introduce a canonical `ActionId` and stop passing heavy `Move` objects across the policy boundary

This is the highest-ROI change.

Today `Game::next()` validates a selected move by scanning the legal list and comparing polymorphic `Move` objects via `operator==`. That makes equality, caching, logging, dataset encoding, and cross-policy interoperability harder than necessary. Replace that with a canonical `ActionId` plus optional `ActionDebugInfo`. Policies choose an ID; the engine validates by ID; `Move` can remain an internal lowering artifact if needed. ([GitHub][7])

Benefits:

* no more structural equality boilerplate at the runner boundary
* better logging and replay
* natural keys for MCTS child stats, TT entries, and aggregated root-parallel results
* easier dataset generation and benchmark comparison

### 4) Extract a `Ruleset` object and kill implicit global registration

`initializeBuiltinGenerators()` should not live as a constructor side effect of `Game`. Make rules explicit:

* `TwilightStruggleRuleset rules = make_default_ruleset();`
* engine or runner receives `rules`
* tests can inject trimmed or mocked rulesets

Then split rules by responsibility: phase handlers by phase, card effects by pattern/family, bespoke card logic only where necessary. A lot of the current card code looks like it could be expressed as reusable patterns (place/remove influence, region filters, select-N countries, saturation rules) rather than giant monolithic generators. ([GitHub][5])

### 5) Create a shared runtime for self-play, benchmarking, and data collection

Make binaries thin front ends over one reusable runtime API.

A good shape is:

* `MatchRunner`: one game
* `SeriesRunner`: many games with seeds/config
* `BenchmarkService`: fixed scenario + timing/metrics sink
* `SelfPlayService`: emits traces / training samples
* `TournamentService`: round-robin or Elo

Then collection and benchmarking differ only by policy factories, budgets, and sinks, not by duplicated control flow. This is the missing layer between the engine and binaries. ([GitHub][3])

### 6) Make observability a first-class API, not an afterthought

Add a structured telemetry/event sink that every runner and policy can use. At minimum I would log:

* match id, seed, side, phase, ply
* legal action count and chosen `ActionId`
* policy latency and budget consumption
* MCTS visits, value, prior, UCB/PUCT score for root children
* determinization count for ISMCTS
* command/application traces when debugging
* thread/worker index for parallel search

This also helps tests: instead of asserting on fragile internal state only, you can assert on transition traces and policy decisions. There is already a TODO in `tsnnmcts.cpp` about warning/logging once a logging base exists; build that base now. ([GitHub][8])

### 7) Consolidate search into one reusable search core

`MCTSPolicy` and `TsNnMctsPolicy` should not own separate tree infrastructures. Build one `search_core` with:

* node stats / child stats
* scheduler / budgets / deadlines
* worker orchestration
* telemetry hooks
* pluggable evaluator (`rollout`, `heuristic`, `network`)
* pluggable hidden-info sampler / determinizer

Then `heuristic MCTS`, `ISMCTS`, and `NN-guided MCTS` become configurations of the same framework, not separate subsystems. That will remove a lot of duplicated search code and make benchmarking/search ablations much easier. ([GitHub][9])

### 8) For multi-threading in MCTS, favor clone-per-worker and root-parallel first

You do **not** need a globally thread-safe `Board` to get good parallel search. Given the current wide mutable surface on `Board`, I would explicitly avoid trying to share engine state across workers. Keep the engine single-thread-friendly and make search parallel by design:

* each worker gets its own engine clone / determinized root state
* each worker gets an explicit worker index and RNG seeded from `(global_seed, worker_index)`
* aggregate root statistics by `ActionId`
* use per-worker arenas / PMR resources for node allocation

This matches the current root-parallel approach better than tree-parallel, and it is easier to reason about with hidden information. Also replace `hash(thread::id) % N` RNG selection with explicit worker indexing for determinism and debuggability. If you later need tree-parallel search, share only compact node stats with atomics; do **not** store mutable `Board` objects in shared nodes. ([GitHub][10])

If I were prioritizing this work, I would do it in this order:

1. Add `ActionId` and a `MatchRunner` while keeping adapters to the current `Move` world.
2. Introduce `IPolicy` and stop hard-coding `Game` to `TestPolicy`.
3. Extract `Ruleset` and remove global card-generator initialization from `Game`.
4. Build shared runtime services for self-play, benchmark, and collection.
5. Merge MCTS / ISMCTS / TsNnMcts onto a common search core.
6. Split `ts_core` into separate libraries and lock in dependency rules.

That gives you the biggest payoff without a big-bang rewrite. The first three steps alone would remove most of the current extensibility pain and set you up for cleaner multi-threaded MCTS later.

[1]: https://github.com/Twilight-Struggle/TSGE "https://github.com/Twilight-Struggle/TSGE"
[2]: https://github.com/Twilight-Struggle/TSGE/blob/main/include/tsge/actions/move.hpp "https://github.com/Twilight-Struggle/TSGE/blob/main/include/tsge/actions/move.hpp"
[3]: https://github.com/Twilight-Struggle/TSGE/blob/main/CMakeLists.txt "https://github.com/Twilight-Struggle/TSGE/blob/main/CMakeLists.txt"
[4]: https://github.com/Twilight-Struggle/TSGE/blob/main/src/core/phase_machine.cpp "https://github.com/Twilight-Struggle/TSGE/blob/main/src/core/phase_machine.cpp"
[5]: https://github.com/Twilight-Struggle/TSGE/blob/main/include/tsge/actions/card_effect_legal_move_generator.hpp "https://github.com/Twilight-Struggle/TSGE/blob/main/include/tsge/actions/card_effect_legal_move_generator.hpp"
[6]: https://github.com/Twilight-Struggle/TSGE/blob/main/include/tsge/core/game.hpp "https://github.com/Twilight-Struggle/TSGE/blob/main/include/tsge/core/game.hpp"
[7]: https://github.com/Twilight-Struggle/TSGE/blob/main/src/core/game.cpp "https://github.com/Twilight-Struggle/TSGE/blob/main/src/core/game.cpp"
[8]: https://github.com/Twilight-Struggle/TSGE/blob/main/src/players/tsnnmcts.cpp "https://github.com/Twilight-Struggle/TSGE/blob/main/src/players/tsnnmcts.cpp"
[9]: https://github.com/Twilight-Struggle/TSGE/blob/main/include/tsge/players/mcts_policy.hpp "https://github.com/Twilight-Struggle/TSGE/blob/main/include/tsge/players/mcts_policy.hpp"
[10]: https://github.com/Twilight-Struggle/TSGE/blob/main/src/players/mcts_policy.cpp "https://github.com/Twilight-Struggle/TSGE/blob/main/src/players/mcts_policy.cpp"

Q:
I still want to keep efficiency gains from MCTS optimizations (see _fast symbols and file names), is it possible to marry to your proposal? Also we have perfect information MCTS and imperfect infirmation heuristic/ISMCTS, how will it play together?

A:
Yes.

I did not inspect the ignored `cpp/mcts_batched_fast/` subtree itself here, so this is about preserving that *class* of optimization rather than auditing that exact implementation. Architecturally, the answer is still yes: you can keep the fast kernels and still clean up the repo. The current tree already points that way. The README explicitly centers `Board::copyForMCTS()` and policy-swappable players; the classic MCTS path already generates determinizations, clones boards, and runs root-parallel threads; and the Zero-style path already has a separate inference-engine seam, even though its current `runSearch()` is still a skeleton that expands root priors and returns the max-prior move. ([GitHub][1])

The trick is to separate **control plane** from **data plane**. The control plane can be clean and runtime-configurable: `MatchRunner`, `PolicyFactory`, `SearchBudget`, `TraceSink`, `ActionId`, common config. The data plane stays specialized: `perfect_mcts_fast`, `ismcts_fast`, `puct_batched_fast`, `heuristic_fast`. I would **not** try to force those into one shared `Node` type or one fully virtualized engine API. In the current hot path, you still have `std::shared_ptr<Move>`, `PhaseMachine::step(const_cast<Board&>(node->getBoard()))`, RNG lookup via hashed `thread::id`, and root-action reconstruction by stringifying card ids and branching on `dynamic_cast`. Those are exactly the kinds of things that should be removed from inner loops, not wrapped in more abstraction. ([GitHub][2])

I would make the fast backends explicit build targets. Right now `src/players` contains `mcts_policy.cpp`, `policies.cpp`, and `tsnnmcts.cpp`, but `ts_core` is built from `tsnnmcts.cpp` and `policies.cpp` rather than `mcts_policy.cpp`. Turning search backends into named libraries would make that divergence intentional instead of accidental. ([GitHub][3])

The clean model is to treat **information regime** as a separate axis from **search algorithm**. I would define three related state forms: `FullState`, `Observation`, and `DeterminizedState`. Perfect-information MCTS/PUCT runs on `FullState`. ISMCTS runs on `Observation + BeliefSampler -> DeterminizedState`. A heuristic policy scores legal `ActionId`s directly from `Observation` or a belief summary, and that same heuristic can also be used as a rollout or leaf evaluator inside either tree.

That maps well to what the code is already doing, but with clearer names. Today `copyForMCTS()` clones the board, masks the opponent hand and deck with `DUMMY`, and hides headline cards as needed; then the current MCTS code immediately mutates those copies to inject sampled opponent hands for determinization. That works, but it overloads one API with two meanings. I would rename the current function to something like `clone_for_viewer()` and add separate `clone_full()` / `materialize_determinization()` APIs. Then perfect-info and imperfect-info search stop sharing an ambiguously named primitive. ([GitHub][4])

The main unifier should be `ActionId`, not `Move*` and not a shared node layout. The current root aggregation already wants a canonical action key, but today it approximates one by building a `move_key` string from the card id plus move-type suffixes and then reconstructing concrete moves with `dynamic_cast`. Replace that with a stable integer `ActionId` and an `ActionCodec` at the engine boundary. Then perfect MCTS, ISMCTS, heuristic policies, telemetry, replay, batching, and dataset collection all speak the same root-action language. ([GitHub][5])

For multithreading, I would use **different parallel models per backend**. Perfect-information fast backends can do tree-parallel search with shared stats, virtual loss, and a TT keyed by full state, or root-parallel if that benchmarks better. Imperfect-information backends should prefer worker-local determinizations and root-level merge only; I would not share one inner tree across different hidden-state samples. That is also the natural evolution of the current code, which already creates per-determinization roots and parallelizes across them. I would also replace hashed `thread::id` RNG selection with an explicit `worker_index` carried in `SearchContext`; it is simpler, deterministic, and easier to debug. ([GitHub][5])

For the batched / NN side, keep a common `InferenceService`, but not a common `TsNnMctsNode`. Both `puct_batched_fast` and `ismcts_fast` can push leaf-eval requests into the same batcher, but their node storage and scheduling should remain specialized. That is especially attractive here because `TsNnMcts` already has an explicit inference-engine interface and config, while its current implementation still stops at root expansion/backup and max-prior selection instead of running full simulations. That means you can grow the batched fast backend behind the evaluator boundary without blocking the rest of the refactor. ([GitHub][6])

The shape I would use is:

```cpp
struct RootContext {
  Side side;
  SearchBudget budget;
  Observation obs;
  std::span<const ActionId> legal_actions;
  TraceSink* trace;
};

using BuiltinPolicy =
    std::variant<HeuristicFast, PerfectMctsFast, IsmctsFast, BatchedPuctFast>;

class PolicyHandle {
 public:
  ActionId choose(const RootContext& ctx) {
    return std::visit([&](auto& p) { return p.choose(ctx); }, impl_);
  }
 private:
  BuiltinPolicy impl_;
};
```

That gives you runtime pluggability at the coarse boundary, but all the real work stays monomorphized inside each backend. One dispatch per move is cheap. A virtual call per node expansion is not.

What I would unify across all backends:

* `ActionId` / `ActionCodec`
* `SearchBudget`
* `SearchContext { worker_index, rng, scratch, trace }`
* `Evaluator` (`rollout`, `heuristic`, `NN`)
* `KnowledgeModel` (`PerfectInfo`, `ObservationOnly`, `DeterminizationSampler`)
* telemetry schema and replay format

What I would *not* unify:

* node layout
* memory arena / node store
* batching strategy
* parallelization model
* transposition-table key space

That is the crucial compromise: **common protocol, specialized kernels**.

Concretely, I would change these first:

* Introduce `ActionId` and an `ActionCodec`.
* Split `copyForMCTS()` into explicit clone/materialization APIs.
* Add `SearchContext{worker_index, rng, scratch, trace}`.
* Extract `Evaluator` and `BeliefSampler`.
* Turn `_fast` paths into explicit backend libraries chosen by a single `PolicyFactory`.

That also fixes your earlier operational issues. One runner binary can benchmark, self-play, or collect data by swapping policy specs and sinks instead of reimplementing orchestration around `Game`. The current top-level loop still wires the constructor to a concrete `Player` type, initializes built-in generators internally, and validates selected moves by comparing full `Move` objects against the legal list. Moving the runner boundary to `ActionId` is the leverage point. ([GitHub][7])

So the short architectural answer is: **yes, absolutely keep the `_fast` implementations**. Just stop treating them as ad hoc branches of the codebase. Make them first-class backends under a stable outer search/runtime API. In this repo, that should preserve the current MCTS-specific speedups and likely improve them, because `ActionId`, explicit clone semantics, worker-local scratch, and backend-specific node stores remove several costs that are currently sitting in the hot path. ([GitHub][2])

A useful next step would be to sketch the actual header layout for `ActionId`, `SearchContext`, `KnowledgeModel`, and the four backend libraries.

[1]: https://github.com/Twilight-Struggle/TSGE "https://github.com/Twilight-Struggle/TSGE"
[2]: https://github.com/Twilight-Struggle/TSGE/raw/refs/heads/main/include/tsge/players/mcts_policy.hpp "https://github.com/Twilight-Struggle/TSGE/raw/refs/heads/main/include/tsge/players/mcts_policy.hpp"
[3]: https://github.com/Twilight-Struggle/TSGE/tree/main/src/players "https://github.com/Twilight-Struggle/TSGE/tree/main/src/players"
[4]: https://raw.githubusercontent.com/Twilight-Struggle/TSGE/refs/heads/main/src/core/board.cpp "https://raw.githubusercontent.com/Twilight-Struggle/TSGE/refs/heads/main/src/core/board.cpp"
[5]: https://github.com/Twilight-Struggle/TSGE/blob/main/src/players/mcts_policy.cpp "https://github.com/Twilight-Struggle/TSGE/blob/main/src/players/mcts_policy.cpp"
[6]: https://raw.githubusercontent.com/Twilight-Struggle/TSGE/refs/heads/main/include/tsge/players/tsnnmcts.hpp "https://raw.githubusercontent.com/Twilight-Struggle/TSGE/refs/heads/main/include/tsge/players/tsnnmcts.hpp"
[7]: https://raw.githubusercontent.com/Twilight-Struggle/TSGE/refs/heads/main/src/core/game.cpp "https://raw.githubusercontent.com/Twilight-Struggle/TSGE/refs/heads/main/src/core/game.cpp"

Q:
How would you rebuild the airplane during flight or migrate to this cleaner architecture while keeping things like working basically gradually? Is it even possible also? How to make sure that the new logic doesn't break anything? I mean, there is a high chance that random generators will be moved around and then it's not a bit exact, and then like kind of how to reason. Or is it possible to refactor and still keep it a bit exact?

A:
Yes, it is possible.

The way to do it without breaking everything is to **separate “changing structure” from “changing behavior”**, and to make the current behavior observable before you touch the architecture.

Right now the repo gives you enough seams to do that: the top-level match loop is centralized in `Game::next()`, `Board::copyForMCTS()` is already the clone seam for search, and CMake already wires a fairly broad unit test suite. At the same time, the current baseline is not set up for strict reproducibility by default: non-test `Game` randomizes player order from `random_device`, `Randomizer` seeds itself from `random_device`, and `copyForMCTS()` uses `Board copy = *this` while leaving the RNG-reset line commented out. Also, `Board` owns a `Randomizer`, but `Deck` stores a `Randomizer&`; by normal C++ copy semantics, I would treat cloned-board RNG binding as risky until copying is made explicit. The existing tests cover things like `copyForMCTS()` hiding behavior and a skeleton `TsNnMctsPolicy` case, but they do not yet define seeded end-to-end trace equivalence. ([GitHub][1])

The key is to decide **what kind of sameness you actually need**.

I would define four levels:

1. **Rules exactness**
   Same legal actions and same resulting board state after applying an action.

2. **Trace exactness**
   For a fixed seed and scripted players, the full match trace is identical step by step.

3. **Search exactness**
   For a fixed seed in a deterministic search mode, the chosen action and root stats match.

4. **Statistical equivalence**
   For fast parallel MCTS/ISMCTS, strength and behavior match distributionally over many seeds, not bit for bit.

That distinction matters because **bit exactness is realistic for the engine and for a deterministic reference search mode**, but it is usually the wrong target for an aggressively parallel shared-tree MCTS. For multi-threaded search, a better target is: deterministic reference backend for CI, fast backend for benchmarks.

The migration I would use is this:

### 1) Freeze the current behavior before reorganizing anything

First PR: no file moves, no abstractions, no algorithm changes.

Add:

* a `SeedConfig` or `MasterSeed`
* a `TraceSink`
* a canonical `StateSnapshot` / `StateHash`
* a “record/replay” RNG debug mode

The important part is that every random draw becomes attributable to a named stream and a counter. Not just “some RNG was used”, but “deck_shuffle stream, draw #17”, “dice stream, draw #42”, “mcts_rollout worker 3, draw #91”.

That gives you a debugging unit: the **first divergence**.

Without this, when behavior changes you just see “the game went differently.” With it, you see:

* state first diverged before RNG usage → logic bug
* RNG counter diverged with same prior state → sequencing bug
* same state but different chosen action → ordering / policy bug
* same engine trace but different MCTS stats → search nondeterminism or intentional search change

### 2) Introduce the new architecture as wrappers around the old code

Do not rewrite the engine first.

Create:

* `LegacyEngineAdapter`
* `LegacyPolicyAdapter`
* `MatchRunner`
* `BenchmarkRunner`
* `SelfPlayRunner`

But have them call the **existing** engine loop and policies underneath.

This is the “airplane during flight” move. The new architecture starts by **hosting the old implementation unchanged**. Once that exists, your data collection and benchmarking binaries can already stop duplicating orchestration, because both can go through the same runner API even before any logic is replaced.

### 3) Add `ActionId` without removing `Move`

Make `ActionId` additive first.

At the boundary:

* engine still produces legacy `Move`s
* an `ActionCodec` assigns stable IDs to the current legal list
* new code consumes IDs
* legacy adapters decode back to `Move`

That gives you a stable comparison surface. Old policy says “I picked this `Move*`”; new policy says “I picked Action 137”; the adapter resolves both to the same canonical action key.

This is also how you avoid hidden behavior changes from move ordering. Once you have `ActionId`, you can sort or at least stabilize externally visible action ordering without rewriting all internals at once.

### 4) Split RNG into explicit streams before moving logic around

This is the most important part for exactness.

Do not let “moving code” implicitly change which RNG gets consumed.

Have separate named streams for at least:

* match setup
* deck shuffle
* dice
* policy tie-breaks
* determinization
* rollout
* Dirichlet / search noise
* one per MCTS worker

The engine should consume **engine streams** only. Search should consume **search streams** only. That way a refactor inside MCTS cannot perturb the live game RNG, and a change in deck handling cannot perturb determinization order.

In your repo, this is especially important because randomness currently lives partly in `Game`, partly in `Randomizer`, and search swaps external RNGs into simulation paths. That is exactly the kind of setup where innocent refactors can change behavior in ways that are hard to reason about. ([GitHub][1])

### 5) Build a lock-step differential harness

This is how you know the new logic is still correct.

Run legacy and new side by side on the same inputs:

* same initial seed
* same scripted action selections
* same action IDs
* same RNG replay log in strict mode

After each transition, compare canonical state snapshots.

For engine work, the test should stop at the first mismatch and print:

* prior state hash
* action chosen
* next state hash
* legal action diff
* RNG stream/counter diff

This lets you migrate one subsystem at a time:

* first `MatchRunner`
* then action encoding
* then rules registry
* then move generation
* then phase handling
* then policy backends

### 6) Keep two search modes: strict and fast

This is how MCTS fits in cleanly.

Have:

* **strict mode**: deterministic, used in CI and refactoring
* **fast mode**: optimized, multithreaded, used in benchmarks and training

For strict mode, use a design that can actually be deterministic:

* fixed thread count
* fixed worker index to seed mapping
* fixed work partition
* worker-local trees
* deterministic reduction by `ActionId`

Root-parallel search is much easier to make reproducible than shared-tree search. For perfect-information MCTS, that can often be bit exact on the same platform/toolchain. For ISMCTS, it can also be reproducible if determinization schedules are fixed. For shared-tree parallel MCTS with races, atomics, or virtual loss, I would not promise bit exactness.

So the rule should be:

* **engine + strict search must be exact**
* **fast search must be statistically validated**

That is enough to refactor safely without forcing the fastest backend to become artificially rigid.

### 7) Be selective about what you preserve bit-exactly

This is important.

Do not preserve accidental bugs just because they are “current behavior.”

For example, I would not make “whatever happens today with copied `Deck` / `Randomizer` bindings” a compatibility target. I would make the target be the intended semantics:

* same public game trace
* same seeded engine behavior
* independent cloned search state
* search randomness isolated from match randomness

If a legacy quirk is clearly not part of the intended model, fix it deliberately and re-baseline after the fix.

### 8) Use the existing tests as a floor, not the oracle

The repo already runs many unit tests from CMake, including `board_mcts_test`, several `phase_machine_*` suites, move-generation tests, deck tests, and a `tsnnmcts_policy_test`. That is a good starting floor. But the current MCTS-board tests are about hidden-info copying and state preservation, and the TsNnMcts test is only a minimal skeleton. They are not enough to guarantee seeded trace compatibility or search reproducibility. ([GitHub][2])

I would add four new test families before any deeper refactor:

* `seeded_match_trace_test`
* `legacy_vs_v2_lockstep_test`
* `clone_rng_independence_test`
* `strict_mcts_repro_test`

### What “bit exact” is realistic here

My view:

* **Engine refactors**: yes, bit exact is achievable on the same compiler/platform if you freeze RNG streams, action ordering, and tie-breaks.
* **Single-thread or deterministic root-parallel search**: often yes.
* **Fast shared-tree multithreaded MCTS**: generally no, not reliably, and not worth making the architectural center of your refactor.
* **Cross-platform / cross-standard-library exactness**: usually no; aim for semantic exactness instead.

So the right mental model is not “either bit exact everywhere or unsafe.” It is:

* exact where exactness is feasible and valuable
* statistical where parallel search makes exactness brittle
* always differential and traceable so the first divergence is obvious

If I were sequencing the actual work, the first change I would make is: **injectable seeds + RNG stream naming + trace logging**, with zero behavior changes intended. That single step turns the rest of the migration from guesswork into controlled engineering.

[1]: https://raw.githubusercontent.com/Twilight-Struggle/TSGE/refs/heads/main/src/core/game.cpp "https://raw.githubusercontent.com/Twilight-Struggle/TSGE/refs/heads/main/src/core/game.cpp"
[2]: https://raw.githubusercontent.com/Twilight-Struggle/TSGE/refs/heads/main/CMakeLists.txt "https://raw.githubusercontent.com/Twilight-Struggle/TSGE/refs/heads/main/CMakeLists.txt"

Q:
Write down a little bit more detailed APIs that you suggest, and explain how it maps in the pseudocode, very high level, like in the game loop. In very high level MCTS, how it will all work together.

A:
Below is the API shape I would introduce first. It is not a rewrite of the rules engine. It keeps the repo’s intended `Command / Move / Board` split and `PhaseMachine`-driven flow, but hides the current `Game::next()` control loop—`pending` move, `PhaseMachine::step`, `Player::decideMove`, legal-move revalidation—behind a cleaner runtime boundary. `Board::copyForMCTS()` is already the natural seam for a search-facing view, so the first version can be mostly adapters around existing code. ([GitHub][1])

## 1) Core boundary

```cpp
namespace ts {

using ActionId = uint32_t;
using Seed = uint64_t;

struct LegalAction {
  ActionId id;
  std::string_view label;   // debug / logs only
};

class ActionCodec {
public:
  static ActionCodec from_legacy(
      const std::vector<std::shared_ptr<Move>>& legacy_moves);

  std::span<const LegalAction> legal() const { return legal_; }

  // Adapter-only: used while engine still speaks Move internally.
  std::shared_ptr<Move> decode(ActionId id) const;
  const Move& debug_move(ActionId id) const;

private:
  std::vector<LegalAction> legal_;
  std::unordered_map<ActionId, std::shared_ptr<Move>> by_id_;
};

struct Observation {
  Side viewer;
  Board board_view;   // v1: masked Board from copyForMCTS(viewer)
};

struct SearchBudget {
  int max_simulations = 0;
  std::chrono::milliseconds max_time{0};
  int threads = 1;
};

struct PolicyInput {
  const Observation& obs;
  Side actor;
  std::span<const LegalAction> legal;
  SearchBudget budget;
};

struct PolicyOutput {
  ActionId action;
};

struct RootActionStat {
  ActionId action;
  int visits = 0;
  float q = 0.0f;
  float prior = 0.0f;
};

struct SearchResult {
  ActionId chosen;
  std::vector<RootActionStat> root;
};

class TraceSink {
public:
  virtual ~TraceSink() = default;
  virtual void on_decision(Side actor, std::span<const LegalAction>) {}
  virtual void on_choice(Side actor, ActionId) {}
  virtual void on_search_result(const SearchResult&) {}
};

class IPolicy {
public:
  virtual ~IPolicy() = default;
  virtual void on_match_start(Side self, Seed seed) {}
  virtual PolicyOutput choose(const PolicyInput&, class PolicyServices&) = 0;
  virtual void on_match_end(std::optional<Side> winner) {}
};

}  // namespace ts
```

`ActionCodec` is the main compatibility layer. Current APIs still pass `std::shared_ptr<Move>` through `Player::decideMove` and `MCTSExecutor::search`, and `Game::next()` checks legality by comparing the chosen move against each legal move. With `ActionId`, all new runners, policies, logs, and datasets speak a stable id, while the adapter still decodes back to `Move` internally. In v1, `Observation` can literally be a masked `Board` built by `copyForMCTS(viewer)`, which already hides opponent hand, deck contents, and non-visible headline information. ([GitHub][2])

## 2) Engine / runtime API

```cpp
namespace ts {

struct MatchConfig {
  Seed seed = 0;
};

struct MatchResult {
  std::optional<Side> winner;
};

struct MatchState {
  Board board;                                     // v1 legacy state
  ActionCodec last_legal;
  std::optional<std::shared_ptr<Move>> pending;    // adapter-only
};

struct DecisionPoint {
  Side actor = Side::NEUTRAL;
  std::span<const LegalAction> legal;
  std::optional<Side> winner;

  bool terminal() const { return winner.has_value(); }
};

class IGameEngine {
public:
  virtual ~IGameEngine() = default;
  virtual MatchState new_match(const MatchConfig&) const = 0;
  virtual DecisionPoint advance_to_decision(MatchState&) const = 0;
  virtual void submit(MatchState&, ActionId) const = 0;
  virtual Observation observe(const MatchState&, Side viewer) const = 0;
};

class LegacyTsEngineAdapter final : public IGameEngine {
public:
  MatchState new_match(const MatchConfig&) const override;

  DecisionPoint advance_to_decision(MatchState& s) const override {
    auto [legacy_legal, actor, winner] =
        PhaseMachine::step(s.board, std::move(s.pending));
    s.last_legal = ActionCodec::from_legacy(legacy_legal);
    return {.actor = actor, .legal = s.last_legal.legal(), .winner = winner};
  }

  void submit(MatchState& s, ActionId id) const override {
    s.pending = s.last_legal.decode(id);
  }

  Observation observe(const MatchState& s, Side viewer) const override {
    return {.viewer = viewer, .board_view = s.board.copyForMCTS(viewer)};
  }
};

class MatchRunner {
public:
  MatchResult play(const MatchConfig&, IGameEngine&,
                   IPolicy& ussr, IPolicy& usa,
                   TraceSink* trace = nullptr);
};

}  // namespace ts
```

That adapter is the whole “rebuild in flight” trick. `advance_to_decision()` is just the existing `PhaseMachine::step(board, pending)` call plus encoding the returned legal `Move`s; `submit()` is the inverse decode; `observe()` reuses `copyForMCTS(viewer)`. So phase handling, legal move generation, command application, and most existing tests do not need to move first. The repo also already builds one `ts_core` library and runs a broad unit-test suite over it, which makes this kind of wrapper-first refactor practical. ([GitHub][3])

## 3) Game-loop mapping

Current flow, conceptually:

```cpp
pending = null;
while (true) {
  auto [legal, actor, winner] = PhaseMachine::step(board, std::move(pending));

  if (legal.empty() && actor == Side::NEUTRAL) {
    break;
  }

  do {
    pending = players[actor].decideMove(board, legal, actor);
  } while (!is_legal(pending, legal));
}
```

Proposed outer loop:

```cpp
MatchResult MatchRunner::play(...) {
  MatchState state = engine.new_match(cfg);

  std::array<IPolicy*, 2> policies = {&ussr, &usa};

  ussr.on_match_start(Side::USSR, cfg.seed);
  usa.on_match_start(Side::USA, cfg.seed);

  while (true) {
    DecisionPoint dp = engine.advance_to_decision(state);
    if (dp.terminal()) {
      ussr.on_match_end(dp.winner);
      usa.on_match_end(dp.winner);
      return {.winner = dp.winner};
    }

    Observation obs = engine.observe(state, dp.actor);
    PolicyInput in{obs, dp.actor, dp.legal, budget_for(dp.actor)};

    if (trace) trace->on_decision(dp.actor, dp.legal);

    PolicyOutput out = policies[static_cast<int>(dp.actor)]->choose(in, services_);

    if (trace) trace->on_choice(dp.actor, out.action);

    engine.submit(state, out.action);
  }
}
```

The important point is that `MatchRunner` no longer knows what a `Move` is, does not call `PhaseMachine::step` directly, and does not care whether the policy is heuristic, classic MCTS, ISMCTS, or NN-guided. Only the legacy adapter knows how to talk to the existing engine internals. That maps directly to the current `Game::next()` / `PhaseMachine::step()` / `Player::decideMove()` structure. ([GitHub][2])

## 4) Search-facing API

```cpp
namespace ts {

// v1 migration: search state is still just Board.
// Later, each fast backend may use a smaller internal state type.
using SearchState = Board;

struct RngBundle {
  Seed master_seed = 0;
  // named streams later: engine, determinization, rollout, per-worker...
};

struct SearchContext {
  int worker_index = 0;
  TraceSink* trace = nullptr;
  RngBundle* rngs = nullptr;
  // backend-owned scratch arena / cancellation token can live here too
};

class ISearchGame {
public:
  virtual ~ISearchGame() = default;

  virtual std::vector<LegalAction> legal_actions(
      const SearchState&, Side& actor) const = 0;

  virtual void apply(SearchState&, ActionId, SearchContext&) const = 0;

  virtual bool terminal(const SearchState&) const = 0;
  virtual float terminal_value(const SearchState&, Side root_side) const = 0;
};

class IKnowledgeModel {
public:
  virtual ~IKnowledgeModel() = default;

  // disclosed_full_state is only set for perfect-info / cheating backends.
  virtual SearchState make_root(const MatchState* disclosed_full_state,
                                const Observation& obs,
                                Side actor,
                                SearchContext&) const = 0;
};

struct EvalOutput {
  std::vector<float> priors;   // same order as legal actions
  float value = 0.0f;          // root-side view
};

class IEvaluator {
public:
  virtual ~IEvaluator() = default;

  virtual EvalOutput evaluate(const SearchState&,
                              std::span<const LegalAction> legal,
                              Side actor,
                              SearchContext&) = 0;
};

struct PolicyServices {
  const MatchState* disclosed_full_state = nullptr; // null for honest imperfect-info policies
  ISearchGame& game;
  IKnowledgeModel& knowledge;
  IEvaluator& evaluator;
  TraceSink* trace = nullptr;
  RngBundle* rngs = nullptr;
};

class ISearchBackend {
public:
  virtual ~ISearchBackend() = default;
  virtual SearchResult run(const PolicyInput&, PolicyServices&) = 0;
};

class MctsPolicy final : public IPolicy {
public:
  explicit MctsPolicy(std::unique_ptr<ISearchBackend> backend)
      : backend_(std::move(backend)) {}

  PolicyOutput choose(const PolicyInput& in, PolicyServices& svc) override {
    return {.action = backend_->run(in, svc).chosen};
  }

private:
  std::unique_ptr<ISearchBackend> backend_;
};

}  // namespace ts
```

This is where the families separate cleanly. `IKnowledgeModel` is the information-regime axis: perfect-information backends clone a disclosed full state, while ISMCTS backends sample a determinization from an observation. `IEvaluator` is the value/prior axis: rollout, heuristic, or NN. The outer `ISearchBackend` API stays the same, but each fast backend keeps its own node layout, allocator, TT, batching strategy, and parallelization model. That fits the current repo well: classic MCTS already has `Node(Board, last_move, current_side, DeterminizedState)` plus per-thread RNGs and determinization generation, and the NN path already exposes `TsNnMctsInferenceEngine::evaluate(board, legal_moves, side) -> policy + value`, which is almost exactly the `IEvaluator` contract. ([GitHub][4])

## 5) Very high-level MCTS pseudocode

```cpp
SearchResult Backend::run(const PolicyInput& root, PolicyServices& svc) {
  RootAccumulator acc(root.legal);   // keyed by ActionId

  parallel_for (int worker = 0; worker < root.budget.threads; ++worker) {
    SearchContext ctx = make_worker_context(worker, svc);
    FastWorkerTree tree(ctx);   // backend-specific fast node store

    while (!budget_exhausted(root.budget, ctx)) {
      SearchState s =
          svc.knowledge.make_root(svc.disclosed_full_state, root.obs, root.actor, ctx);

      Path path = tree.select(s, svc.game, root.actor, ctx);

      float value;
      if (svc.game.terminal(s)) {
        value = svc.game.terminal_value(s, root.actor);
      } else {
        Side actor;
        auto legal = svc.game.legal_actions(s, actor);

        EvalOutput eval = svc.evaluator.evaluate(s, legal, actor, ctx);

        tree.expand(path.leaf, legal, eval.priors);
        value = eval.value;
      }

      tree.backup(path, value);
    }

    acc.merge(tree.root_stats());  // merge by ActionId
  }

  SearchResult out = acc.finalize_best_by_visits();
  if (svc.trace) svc.trace->on_search_result(out);
  return out;
}
```

That same outer loop supports the three main regimes:

`PerfectMctsFast`

```cpp
knowledge = PerfectKnowledgeModel{};    // make_root = clone full state
evaluator = RolloutEvaluator{};         // or heuristic evaluator
backend   = PerfectMctsFastBackend{};   // tree/root parallel, TT if you want
```

`IsmctsFast`

```cpp
knowledge = DeterminizedKnowledgeModel{/* belief sampler */};
evaluator = RolloutEvaluator{};         // or heuristic evaluator
backend   = IsmctsFastBackend{};        // usually root-parallel / worker-local trees
```

`BatchedPuctFast`

```cpp
knowledge = PerfectKnowledgeModel{} or DeterminizedKnowledgeModel{};
evaluator = BatchedNnEvaluator{/* wraps inference engine / batcher */};
backend   = PuctBatchedFastBackend{};
```

For the NN path, the only extra piece is that `BatchedNnEvaluator::evaluate()` does not immediately compute priors/value itself. It serializes the leaf state plus legal actions, queues the request into an inference batcher, and later returns the batch result in legal-action order. That lines up naturally with the current `TsNnMctsInferenceEngine` contract. ([GitHub][5])

## 6) How the current repo maps to this

Conceptually, the mapping is:

* `Game::next()` → `MatchRunner::play()`
* `PhaseMachine::step(board, pending)` → `LegacyTsEngineAdapter::advance_to_decision()`
* `Player::decideMove(board, legalMoves, side)` → `IPolicy::choose(PolicyInput, PolicyServices)`
* `std::vector<std::shared_ptr<Move>>` → `ActionCodec + ActionId`
* `Board::copyForMCTS(viewer)` → `Observation`
* `MCTSExecutor` → `ISearchBackend`
* `TsNnMctsInferenceEngine` → `IEvaluator`

That is why this can be incremental. The outer architecture gets cleaned up first, but the hot code and the rules code can stay where they are until you choose to replace them. The only hard requirement is that all backend root stats, telemetry, replay, and runner boundaries speak `ActionId` instead of raw `Move*`. ([GitHub][2])

The short version is: one shared outer protocol, multiple specialized inner kernels. That gives you a clean game loop and clean policy plumbing without giving up `_fast`-style backends.

[1]: https://github.com/Twilight-Struggle/TSGE "https://github.com/Twilight-Struggle/TSGE"
[2]: https://raw.githubusercontent.com/Twilight-Struggle/TSGE/main/src/core/game.cpp "https://raw.githubusercontent.com/Twilight-Struggle/TSGE/main/src/core/game.cpp"
[3]: https://raw.githubusercontent.com/Twilight-Struggle/TSGE/main/include/tsge/core/phase_machine.hpp "https://raw.githubusercontent.com/Twilight-Struggle/TSGE/main/include/tsge/core/phase_machine.hpp"
[4]: https://raw.githubusercontent.com/Twilight-Struggle/TSGE/main/include/tsge/players/mcts_policy.hpp "https://raw.githubusercontent.com/Twilight-Struggle/TSGE/main/include/tsge/players/mcts_policy.hpp"
[5]: https://raw.githubusercontent.com/Twilight-Struggle/TSGE/main/include/tsge/players/tsnnmcts.hpp "https://raw.githubusercontent.com/Twilight-Struggle/TSGE/main/include/tsge/players/tsnnmcts.hpp"

Q:
What's actionid then? Actions are complex (influence placement subset, etc). Also what's the point to have a unordered map? 

I'm worried about calling virtual functions or other overhead in hot loop

A:
I would actually rename it.

`ActionId` sounds like a globally meaningful semantic encoding. What I really mean is closer to **`ActionRef`** or **`LegalActionRef`**: a cheap handle to one already-generated legal action. That matters because your current `Move` objects are not simple scalars. They already carry rich payloads like `std::map<CountryEnum,int>` for influence placement/removal and `targetCountry + history + remainingOps + flags` for realignment requests, and equality is currently structural/polymorphic through `Move::operator==`. ([GitHub][1])

So I would split the concept into two layers.

```cpp
struct ActionRef {
  uint32_t epoch;   // which decision point created it
  uint16_t slot;    // index in that decision point's legal-action table
};

enum class ActionKind : uint8_t {
  PlaceInfluence,
  RemoveInfluence,
  Coup,
  Realignment,
  EventChoice,
  Pass,
  Discard,
  HeadlineSelect,
  // ...
};

struct ActionMeta {
  ActionKind kind;
  CardEnum card;
  Side side;
  uint32_t payload_index;   // index into a per-kind payload array
};
```

And then the payloads live elsewhere:

```cpp
struct PlaceInfluencePayload {
  SmallVector<std::pair<CountryEnum, uint8_t>, 4> deltas; // sorted
};

struct RemoveInfluencePayload {
  SmallVector<std::pair<CountryEnum, uint8_t>, 4> deltas; // sorted
};

struct CoupPayload {
  CountryEnum target;
};

struct RealignmentPayload {
  CountryEnum target;
  SmallVector<CountryEnum, 8> history;
  uint8_t remaining_ops;
  AdditionalOpsType flags;
};

class ActionList {
public:
  uint32_t epoch() const noexcept { return epoch_; }
  std::span<const ActionMeta> meta() const noexcept { return meta_; }

  const PlaceInfluencePayload& place(uint32_t i) const noexcept;
  const RemoveInfluencePayload& remove(uint32_t i) const noexcept;
  const CoupPayload& coup(uint32_t i) const noexcept;
  const RealignmentPayload& realign(uint32_t i) const noexcept;

private:
  uint32_t epoch_ = 0;
  std::pmr::vector<ActionMeta> meta_;
  std::pmr::vector<PlaceInfluencePayload> place_;
  std::pmr::vector<RemoveInfluencePayload> remove_;
  std::pmr::vector<CoupPayload> coup_;
  std::pmr::vector<RealignmentPayload> realign_;
};
```

That handles arbitrarily complex actions because the integer is **not** the action itself. It is just a slot into an `ActionList` that already owns the real payload. Influence subsets, remove-all subsets, realignment history, event choices—all fine. The only requirement is that payload construction be canonical, for example sorting country/count pairs once during generation.

For logs, replay, and datasets, I would keep a separate durable representation:

```cpp
struct ActionRecord {
  ActionKind kind;
  CardEnum card;
  Side side;
  std::vector<std::pair<CountryEnum,uint8_t>> deltas;
  std::vector<CountryEnum> history;
  CountryEnum target = CountryEnum::DUMMY;
  uint8_t remaining_ops = 0;
  AdditionalOpsType flags = AdditionalOpsType::NONE;
};
```

So:

* `ActionRef` = execution/search handle, local and cheap
* `ActionRecord` = persistent semantic description, slower but durable

That is the important correction.

On the `unordered_map`: I would **not** keep it in the real design.

In my earlier sketch it was just an adapter convenience. For this repo, dense indexing is better almost everywhere. The current MCTS code already pays for something much worse: `MCTSExecutor::selectBestMove()` aggregates root stats in an `std::unordered_map<std::string, std::pair<int,double>>`, builds a string key from the move/card, uses `dynamic_cast` to distinguish move types, and then reconstructs the winning move by repeating the same kind of type checks. At the game loop level, `Game::next()` also validates a chosen move by scanning the legal list and comparing full polymorphic `Move`s via `operator==`. ([GitHub][2])

So the real structure I would use is:

```cpp
struct RootStats {
  std::vector<int> visits;      // indexed by root slot
  std::vector<float> value_sum; // indexed by root slot
};
```

No hash map. No string key. No `dynamic_cast` to identify the root action.

At a decision point, the engine generates one canonical `ActionList`:

```cpp
DecisionPoint dp = engine.advance_to_decision(state);
// dp.actions is the ActionList for this state
```

A policy sees only:

```cpp
struct LegalActionView {
  ActionRef ref;
  ActionKind kind;
  CardEnum card;
  // optional tiny debug fields
};
```

And it returns one `ActionRef`. The engine checks only:

```cpp
bool valid = (ref.epoch == dp.actions.epoch()) &&
             (ref.slot < dp.actions.meta().size());
```

That replaces the current full structural equality loop.

For the legacy migration, you do not need an `unordered_map` either. Keep the old `Move` objects side by side with the new action table:

```cpp
class LegacyActionList {
public:
  ActionList actions;
  std::pmr::vector<std::shared_ptr<Move>> legacy_moves; // same slot order
};
```

Then:

```cpp
void submit(const LegacyActionList& list, ActionRef ref) {
  pending_ = list.legacy_moves[ref.slot];
}
```

That gives you the new API immediately, while the old engine still consumes `Move`. Again: no hash table.

On virtuals and hot-loop overhead: I agree with the concern, and I would not put virtual dispatch inside the tree search core.

The repo today already uses a mix of static and dynamic mechanisms: `Player` is a template wrapper over a policy type, but `Game` is concretely wired around `Player<TestPolicy>`, while the `Move` hierarchy is virtual and `Game::next()`/MCTS both lean on those polymorphic moves. ([GitHub][3])

What I want is:

* one indirect dispatch at the **turn boundary** is acceptable
* zero virtual dispatch in **selection / expansion / backup**
* zero `shared_ptr<Move>` stored in tree nodes
* zero `unordered_map`/string keying in root merge

So I would structure it like this:

```cpp
struct ChildEdge {
  uint16_t action_slot;   // slot in this node's ActionList
  float prior;
  float value_sum;
  int visits;
  NodeId child;
};
```

And the backend stays concrete:

```cpp
template<class SearchGame, class Evaluator, class KnowledgeModel>
class PerfectMctsFastBackend {
public:
  SearchResult run(const PolicyInput& root, SearchGame& game,
                   Evaluator& eval, KnowledgeModel& know,
                   SearchContext& ctx);
};
```

or, if you want runtime pluggability without virtual calls in the hot path:

```cpp
using BuiltinPolicy =
  std::variant<HeuristicFast, PerfectMctsFast, IsmctsFast, BatchedPuctFast>;

ActionRef choose(const PolicyInput& in) {
  return std::visit([&](auto& p) { return p.choose(in); }, impl_);
}
```

That `std::visit` happens once per move, not once per node. The inner loops are still monomorphized.

The high-level flow becomes:

```cpp
while (!terminal) {
  DecisionPoint dp = engine.advance_to_decision(state); // builds ActionList once

  Observation obs = engine.observe(state, dp.actor);

  ActionRef chosen = policy.choose({
    .obs = obs,
    .actor = dp.actor,
    .actions = dp.actions.view(),
    .budget = budget,
  });

  engine.submit(state, chosen); // O(1) slot lookup
}
```

And MCTS root merge becomes:

```cpp
RootStats agg(num_root_actions);

for (worker : workers) {
  WorkerTree tree = run_worker(root_action_list, ...);

  for (const ChildEdge& e : tree.root_edges()) {
    agg.visits[e.action_slot] += e.visits;
    agg.value_sum[e.action_slot] += e.value_sum;
  }
}

best_slot = argmax(agg.visits);
return ActionRef{root_epoch, best_slot};
```

That is the main point: for complex Twilight Struggle actions, the fast design is **not** “encode the whole action into an integer.” The fast design is “mint a dense slot for a fully materialized action record, then keep using that dense slot everywhere inside the engine and search.”

So the short answers are:

* `ActionId` should really be `ActionRef`: a local handle, not a semantic compression.
* Complex actions live in sidecar payload storage; the handle just points at them.
* The `unordered_map` was adapter scaffolding, not something I would keep.
* In the real design, hot paths use dense vectors and `slot` indices.
* Virtuals stay at coarse boundaries only; the search kernel remains concrete and inlinable.

If you want, I can write the next level down: an exact `DecisionPoint` / `ActionListBuilder` / `LegacyEngineAdapter` header set that shows how this fits into the current `PhaseMachine::step(board, pending)` flow.

[1]: https://github.com/Twilight-Struggle/TSGE/blob/main/include/tsge/actions/move.hpp "TSGE/include/tsge/actions/move.hpp at main · Twilight-Struggle/TSGE · GitHub"
[2]: https://github.com/Twilight-Struggle/TSGE/blob/main/src/players/mcts_policy.cpp "TSGE/src/players/mcts_policy.cpp at main · Twilight-Struggle/TSGE · GitHub"
[3]: https://github.com/Twilight-Struggle/TSGE/blob/main/include/tsge/players/player.hpp "TSGE/include/tsge/players/player.hpp at main · Twilight-Struggle/TSGE · GitHub"

Q:
How do I build a certain action?

A:
Mostly, you **do not let policy code build arbitrary executable actions**.

The engine should build the full legal action set for the current decision point, and the policy should only choose one handle from that set. That is already how the repo behaves today in spirit: `PhaseMachine::step(...)` returns the legal moves, `Game::next()` asks the player to choose one, and then legality is rechecked by comparing the returned move against the legal list. The current move hierarchy already carries rich payloads like influence maps, coup targets, and realignment state, so the cleaner architecture should preserve that “engine builds, policy selects” model rather than forcing policies to construct actions from scratch. ([GitHub][1])

The concrete API I would use is this.

```cpp
struct ActionRef {
  uint32_t epoch;   // decision-point id
  uint16_t slot;    // index into that decision point's ActionList
};

enum class ActionKind : uint8_t {
  PlaceInfluence,
  RemoveInfluence,
  RemoveAllInfluence,
  Coup,
  SpaceRace,
  Realignment,
  RealignmentRequest,
  EventChoice,
  Pass,
  Discard,
  HeadlineSelect,
};

enum class ActionOrigin : uint8_t {
  ActionOps,       // card played for ops
  Event,           // event-generated effect
  InternalRequest, // internal multi-step continuation
};

struct CountryDelta {
  CountryEnum country;
  uint8_t amount;
};

struct ActionMeta {
  ActionKind kind;
  ActionOrigin origin;
  CardEnum card;
  Side side;
  uint32_t payload_index;
};
```

Then store the real payload separately.

```cpp
struct InfluencePayload {
  SmallVector<CountryDelta, 4> deltas; // sorted, merged
};

struct CountryPayload {
  CountryEnum target;
};

struct RealignmentRequestPayload {
  CountryEnum target;
  SmallVector<CountryEnum, 8> history;
  uint8_t remaining_ops;
  AdditionalOpsType flags;
};

class ActionList {
public:
  uint32_t epoch() const noexcept { return epoch_; }
  std::span<const ActionMeta> meta() const noexcept { return meta_; }

  const InfluencePayload& influence(uint32_t i) const noexcept { return influence_[i]; }
  const CountryPayload& country(uint32_t i) const noexcept { return country_[i]; }
  const RealignmentRequestPayload& realignment_request(uint32_t i) const noexcept {
    return realignment_request_[i];
  }

private:
  uint32_t epoch_ = 0;
  std::pmr::vector<ActionMeta> meta_;
  std::pmr::vector<InfluencePayload> influence_;
  std::pmr::vector<CountryPayload> country_;
  std::pmr::vector<RealignmentRequestPayload> realignment_request_;
};
```

And the thing that “builds a certain action” is the builder:

```cpp
class ActionListBuilder {
public:
  explicit ActionListBuilder(uint32_t epoch, std::pmr::memory_resource* mr);

  ActionRef pass(Side side);
  ActionRef discard(CardEnum card, Side side);
  ActionRef headline(CardEnum card, Side side);

  ActionRef place_influence(CardEnum card,
                            Side side,
                            std::span<const CountryDelta> deltas,
                            ActionOrigin origin);

  ActionRef remove_influence(CardEnum card,
                             Side side,
                             std::span<const CountryDelta> deltas,
                             ActionOrigin origin);

  ActionRef remove_all_influence(CardEnum card,
                                 Side side,
                                 std::span<const CountryEnum> countries,
                                 ActionOrigin origin);

  ActionRef coup(CardEnum card, Side side, CountryEnum target);
  ActionRef space_race(CardEnum card, Side side);
  ActionRef realignment(CardEnum card, Side side, CountryEnum target);

  ActionRef realignment_request(CardEnum card,
                                Side side,
                                CountryEnum target,
                                std::span<const CountryEnum> history,
                                uint8_t remaining_ops,
                                AdditionalOpsType flags);

  ActionRef event_choice(CardEnum card, Side side, bool should_trigger_event);

  ActionList finish();

private:
  ActionList out_;
};
```

## What “build a certain action” means in practice

In the current repo, you have concrete move types like `ActionPlaceInfluenceMove`, `EventPlaceInfluenceMove`, `ActionCoupMove`, `ActionRealigmentMove`, `RealignmentRequestMove`, `ActionEventMove`, `PassMove`, `DiscardMove`, `HeadlineCardSelectMove`, `EventRemoveInfluenceMove`, and `EventRemoveAllInfluenceMove`, each with payload in its constructor and later lowered via `toCommand(...)`. The builder above is just the non-polymorphic replacement for those constructors. ([GitHub][1])

So the mapping is roughly:

```cpp
// today
legal.push_back(std::make_shared<ActionPlaceInfluenceMove>(card, side, targetCountries));

// proposed
builder.place_influence(card, side, deltas, ActionOrigin::ActionOps);
```

```cpp
// today
legal.push_back(std::make_shared<EventPlaceInfluenceMove>(card, side, targetCountries));

// proposed
builder.place_influence(card, side, deltas, ActionOrigin::Event);
```

```cpp
// today
legal.push_back(std::make_shared<RealignmentRequestMove>(
    card, side, target, history, remainingOps, flags));

// proposed
builder.realignment_request(card, side, target, history, remainingOps, flags);
```

That is the whole idea: same semantics, cheaper representation.

## Example: building an influence-placement action

This is how I would implement one builder method.

```cpp
ActionRef ActionListBuilder::place_influence(CardEnum card,
                                             Side side,
                                             std::span<const CountryDelta> deltas,
                                             ActionOrigin origin) {
  auto canon = canonicalize_deltas(deltas);   // sort by country, merge duplicates, drop zeros

  uint32_t payload_index = static_cast<uint32_t>(out_.influence_.size());
  out_.influence_.push_back(InfluencePayload{to_small_vector(canon)});

  uint16_t slot = static_cast<uint16_t>(out_.meta_.size());
  out_.meta_.push_back(ActionMeta{
      .kind = ActionKind::PlaceInfluence,
      .origin = origin,
      .card = card,
      .side = side,
      .payload_index = payload_index,
  });

  return ActionRef{out_.epoch_, slot};
}
```

Why canonicalize?

Because then these two descriptions become identical:

```cpp
{{France, 1}, {Italy, 2}}
{{Italy, 2}, {France, 1}}
```

That gives you stable equality, stable replay, stable dataset rows, and stable matching from tests or UI.

## Example: building a realignment-request action

This corresponds directly to the current `RealignmentRequestMove`, which stores `targetCountry`, `realignmentHistory`, `remainingOps`, and `appliedAdditionalOps`. ([GitHub][1])

```cpp
ActionRef ActionListBuilder::realignment_request(CardEnum card,
                                                 Side side,
                                                 CountryEnum target,
                                                 std::span<const CountryEnum> history,
                                                 uint8_t remaining_ops,
                                                 AdditionalOpsType flags) {
  uint32_t payload_index = static_cast<uint32_t>(out_.realignment_request_.size());
  out_.realignment_request_.push_back(RealignmentRequestPayload{
      .target = target,
      .history = to_small_vector(history),
      .remaining_ops = remaining_ops,
      .flags = flags,
  });

  uint16_t slot = static_cast<uint16_t>(out_.meta_.size());
  out_.meta_.push_back(ActionMeta{
      .kind = ActionKind::RealignmentRequest,
      .origin = ActionOrigin::InternalRequest,
      .card = card,
      .side = side,
      .payload_index = payload_index,
  });

  return ActionRef{out_.epoch_, slot};
}
```

## Where this happens in the game loop

At a decision point, the engine builds the legal actions once.

```cpp
DecisionPoint Engine::advance_to_decision(MatchState& s) {
  auto [legacy_legal, actor, winner] = PhaseMachine::step(s.board, std::move(s.pending));

  ActionListBuilder b(next_epoch(), arena_);
  s.legacy_moves.clear();

  for (const auto& m : legacy_legal) {
    // adapter layer for migration
    ActionRef ref = encode_legacy_move(*m, b);
    s.legacy_moves.push_back(m); // same slot order
  }

  s.actions = b.finish();
  return {.actor = actor, .actions = s.actions.view(), .winner = winner};
}
```

Then the policy only picks a slot:

```cpp
ActionRef choice = policy.choose(obs, actions_view, budget);
```

Then the engine applies it:

```cpp
void Engine::submit(MatchState& s, ActionRef ref) {
  assert(ref.epoch == s.actions.epoch());
  assert(ref.slot < s.actions.meta().size());

  // migration path
  s.pending = s.legacy_moves[ref.slot];
}
```

That last part is important. During migration, you do **not** need to rewrite action application immediately. Since `Game::next()` currently expects a pending `Move` chosen from the legal list, the first version can just keep a parallel `legacy_moves[slot]` vector and decode by slot. That preserves existing behavior while you clean up the outer architecture. ([GitHub][2])

## If you really want to ask for “this exact semantic action”

That is a different API.

For tests, UI, replay, or dataset rehydration, you may want to say: “give me the legal action that means place 1 in France and 2 in Italy.” In that case, do **not** construct an executable action directly. Build an `ActionSpec` and resolve it against the current legal list.

```cpp
struct ActionSpec {
  ActionKind kind;
  ActionOrigin origin;
  CardEnum card;
  Side side;
  std::variant<
      InfluencePayload,
      CountryPayload,
      RealignmentRequestPayload,
      bool // for event_choice
  > payload;
};

std::optional<ActionRef> resolve_legal(const ActionList& legal,
                                       const ActionSpec& wanted);
```

Example:

```cpp
ActionSpec spec{
  .kind = ActionKind::PlaceInfluence,
  .origin = ActionOrigin::ActionOps,
  .card = CardEnum::NATO,
  .side = Side::USA,
  .payload = InfluencePayload{{{CountryEnum::FRANCE, 1},
                               {CountryEnum::ITALY, 2}}}
};

auto ref = resolve_legal(actions, spec);
```

That is how a human-facing or test-facing layer should work. It avoids bypassing legality.

## Why this does not add hot-loop overhead

The builder runs only when generating the legal list. That is already when the engine is doing the expensive logic. The policy and search kernels then operate on dense `slot` indices and typed payload arrays.

So in the hot path you get:

* no `shared_ptr<Move>` in tree nodes
* no `dynamic_cast` for root-action identity
* no `unordered_map<string, ...>` for root merging
* no virtual `Move::operator==` for legality checking

Instead you get:

```cpp
const ActionMeta& m = actions.meta()[slot];

switch (m.kind) {
  case ActionKind::PlaceInfluence: {
    const auto& p = actions.influence(m.payload_index);
    // apply or lower
    break;
  }
  case ActionKind::Coup: {
    const auto& p = actions.country(m.payload_index);
    break;
  }
  // ...
}
```

That is dense, branchy, but cheap.

## The short answer

The answer is:

1. The **engine** builds actions while generating legal moves.
2. A policy usually does **not** build actions; it picks an `ActionRef`.
3. If some external layer wants a semantic action, it builds an `ActionSpec` and resolves it against the legal list.
4. During migration, `ActionRef.slot` can simply point to the same slot in a parallel `legacy_moves` array, so you keep current behavior intact while changing the outer API. That matches the current design, where legal moves are produced centrally and the chosen move is validated by membership in that legal set. ([GitHub][1])

The next useful step is to write the exact `encode_legacy_move(*m, builder)` function for the current move subclasses one by one.

[1]: https://raw.githubusercontent.com/Twilight-Struggle/TSGE/refs/heads/main/include/tsge/actions/move.hpp "raw.githubusercontent.com"
[2]: https://raw.githubusercontent.com/Twilight-Struggle/TSGE/refs/heads/main/src/core/game.cpp "raw.githubusercontent.com"

---

## Engine / Game-Loop / Policy / Search Decoupling — Task Sequence

**Status:** In progress. Phases 1-2 partially done via decode_helpers.hpp + search_common.hpp.
**Goal:** `game_loop.cpp` becomes a pure turn scheduler; engine transitions live in `step.cpp`; search backends share semantic helpers; `Observation` is the read-only policy/search boundary.

---

### Task A: Unify NN decode path (PARTIAL — decode_helpers.hpp exists)

- **A1** — Move all masked card/mode/country/value decode logic out of `mcts_batched.cpp` into `decode_helpers.hpp` (the "exact mirror" comment is the target)
- **A2** — Make `TorchScriptPolicy::choose_action` in `learned_policy.cpp` a thin wrapper over the same helpers
- **A3** — Delete the mirrored copy in `mcts_batched.cpp`; run fixed-seed trace comparison to confirm parity
- **Done when:** `mcts_batched.cpp` greedy decode path calls helpers from `decode_helpers.hpp`, no semantic duplication

### Task B: Extract shared search-support layer (PARTIAL — search_common.hpp exists)

- **B1** — Identify all duplicated semantic helpers across `mcts.cpp`, `ismcts.cpp`, `mcts_batched.cpp`: `apply_tree_action`, `rollout_value`, `evaluate_leaf_value_raw`, `AccessibleCache`, card-draft / legal-card collection, country-logit resolution
- **B2** — Move each into `search_common.hpp` (or a `.cpp` if non-trivial) with unit tests
- **B3** — Replace each call site in the three search files; do NOT unify node structs, edge storage, batching strategy, or pool management
- **Done when:** DEFCON safety, accessible-country masking, and decode semantics have one implementation referenced by all three search backends

### Task C: Push Observation as the read-only search/policy boundary

- **C1** — Add observation-shaped input overloads to legality/feature helpers that currently take `(PublicState, CardSet, bool)`
- **C2** — Make batched feature filling (`nn_features.cpp`) accept `Observation` directly
- **C3** — Convert ISMCTS root code to derive everything it needs from `Observation`; restrict full-`GameState` access to determinization only
- **C4** — Keep `PolicyFn(const PublicState&, const CardSet&, bool, Pcg64Rng&)` as a stable adapter at the boundary — do NOT change its signature yet
- **Done when:** read-only search paths take `Observation`; full-state reach-through is deliberate and commented, not the default

### Task D: Move hand-dependent event logic out of game_loop.cpp

- **D1** — Identify all rule logic in `game_loop.cpp` that belongs in the engine: `apply_hand_event`, `apply_action_with_hands`, `apply_ops_randomly_impl`, extra-AR / NORAD / Glasnost mutation
- **D2** — Add fixed-seed trace tests for each (headline, Cat-C, extra AR, Glasnost, Missile Envy) before touching code
- **D3** — Move `apply_hand_event` into `step.cpp` (or a new `step_hand.cpp`); replace call site in `game_loop.cpp` with the engine call
- **D4** — Move `apply_ops_randomly_impl` (and its policy-callback successor) behind the same boundary
- **D5** — `game_loop.cpp` becomes: phase scheduling + tracing + turn cleanup only
- **Done when:** `game_loop.cpp` contains no rule execution; all state mutation goes through `step.cpp`

### Task E: Decide fate of cpp/mcts_batched_fast/

- **E1** — After A–D are done, evaluate: archive as experimental, or rebase on shared helpers from B
- **Defer** until live `tscore` path is clean — do not refactor in parallel

---

**Sequencing rule:** A → B → C → D → E. Don't mix correctness gap fixes (GAP-NNN) with structural cleanup in the same patch.

**Fixed-seed trace tests required before D:** headline, Cat-C events, extra AR, batched greedy decode.
