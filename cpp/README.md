# C++ Port Status

This directory contains the in-progress native port of the Twilight Struggle runtime.

The target is not "some C++ implementation". The target is a fast native clone of the
Python live-play stack that can eventually replace Python in the hot path for:

- benchmark runs
- heuristic vs heuristic play
- learned vs heuristic play
- self-play data collection

ETL is intentionally out of scope for this port.

## Current Scope

Implemented in C++ today:

- live game state and public state handling
- deck construction, dealing, reshuffling, turn loop
- legality generation
- action application
- scoring
- event handling for the current native engine surface
- random and heuristic policy entrypoints
- learned-policy TorchScript runtime
- pybind11 bindings for coarse-grained native execution
- native benchmark / collection / parity-debug tools

Not moved yet:

- replay ETL / dataset ingestion
- exact replacement of every Python validation/test surface
- full semantic parity for all seeded games

## Directory Layout

- `tscore/`: native engine, policies, RNG, scoring, game loop
- `tools/`: native benchmarks, collectors, smokes, parity probes, export helpers

Important files:

- `tscore/game_state.*`: deck, hands, reset, era advancement, dealing
- `tscore/legal_actions.*`: legal move generation and random action sampling
- `tscore/step.*`: action application and event effects
- `tscore/game_loop.*`: headline phase, AR loop, extra ARs, end-of-turn flow, traced play
- `tscore/policies.*`: random policy and native `minimal_hybrid`
- `tscore/learned_policy.*`: TorchScript model loading and action selection
- `tscore/rng.*`: PCG64 state handling plus NumPy-compat helpers used for parity work

## Build Model

Build system:

- CMake
- Ninja

The current build also depends on:

- Python 3 development headers
- NumPy installed in the active Python environment
- pybind11 for bindings
- PyTorch / libtorch if `TS_BUILD_TORCH_RUNTIME=ON`

The native runtime currently uses Python and NumPy in two cold-path / parity-sensitive places:

- integer seed expansion via `numpy.random.SeedSequence(...).generate_state(...)`
- NumPy bounded-integer helpers loaded from the local NumPy extension for RNG-compat paths

This is deliberate. The game loop stays native; the dependency is being used to match the
Python PCG64 seeding and bounded sampling behavior closely enough to drive parity work.

Typical build:

```bash
nice -n 15 cmake -S . -B build-ninja -G Ninja -DTS_BUILD_PYTHON_BINDINGS=ON -DTS_BUILD_TORCH_RUNTIME=ON -DBUILD_TESTING=OFF
nice -n 15 cmake --build build-ninja --target tscore tscore_py -j1
```

## Native Entry Points

Available today:

- native benchmark executable:
  - `build-ninja/cpp/tools/ts_benchmark_matchup`
- native learned-policy matchup:
  - `build-ninja/cpp/tools/ts_learned_matchup`
- native trace collector:
  - `build-ninja/cpp/tools/ts_collect_trace_jsonl`
- native self-play row collector:
  - `build-ninja/cpp/tools/ts_collect_selfplay_rows_jsonl`
- Python bindings module:
  - `build-ninja/bindings/tscore*.so`

Bindings expose coarse-grained play helpers so Python can validate or orchestrate without
driving the full hot loop step-by-step.

## Policies

Native policy surface currently includes:

- `Random`
- `MinimalHybrid`

Learned policy support:

- TorchScript export helper in `tools/export_baseline_to_torchscript.py`
- native TorchScript inference in `tscore/learned_policy.*`

Current intent:

- Python remains the model-authoring / export side
- C++ executes the model for hot-path play and collection

## Validation / Smoke Tooling

Useful tools in `tools/`:

- `event_parity_smoke.cpp`
- `cat_c_smoke.cpp`
- `loop_mechanics_smoke.cpp`
- `smoke_native_runtime.py`
- `compare_initial_setup.py`
- `compare_initial_headline.py`
- `compare_native_python.py`
- `numpy_bounded_probe.cpp`
- `shuffle_stream_probe.cpp`

What these are for:

- setup parity
- headline parity
- event / loop regression checks
- native-vs-Python seeded trace comparison
- isolating RNG mismatches

## Current Parity State

The port is not at 100% seeded parity yet.

What is confirmed working:

- exact initial setup parity from NumPy seed-sequence words
- exact initial deck shuffle parity
- exact post-shuffle d6 stream parity in isolation
- opening headline choice parity on tested seeds
- runtime integer-seed seeding now matches Python `default_rng(seed)` much more closely
- the first-turn Iran coup path now matches again after fixing runtime RNG lifetime and seeding

What is still mismatching:

- full traced seeded games still diverge later
- the raw trace comparer still reports an early mismatch at turn-2 headline because:
  - Python trace collection records headline pick order
  - native trace collection records headline resolution order
- once headline order is normalized away, the first real seed-123 divergence is currently:
  - turn `2`
  - AR `1`
  - USSR card `27`
  - native targets `(21, 25, 76, 79)`
  - Python targets `(22, 25, 76, 79)`

Current best diagnosis:

- the next remaining parity bug is in NumPy-style `choice(..., replace=False)` / subset sampling
  semantics inside matched stochastic event paths
- the currently isolated drift shows up after the turn-1 AR-5 Warsaw Pact event path

## What Changed Recently

Recent parity-focused progress in the current working tree:

- split native reset RNG from native gameplay RNG to match the Python parity flow
- changed native integer seeding to use NumPy `SeedSequence(seed).generate_state(4, "uint64")`
- routed more random sampling through NumPy-compatible bounded helpers
- added `choice_index`, `random_double`, and explicit shuffle helpers in `tscore/rng.*`
- fixed stochastic branch sites that should use discrete choice semantics instead of Bernoulli
- added dedicated probe binaries for:
  - bounded integer behavior
  - shuffle stream behavior

## Known Technical Debt

- exact no-replacement sampling still needs to be matched more tightly
- not every Python event path has been proven seed-identical yet
- the current native parity path depends on local Python/NumPy internals
- the raw parity comparer should eventually normalize headline order before reporting the first mismatch

## Practical Readiness

Good enough today for:

- native architecture work
- throughput benchmarking
- native learned-policy plumbing
- small-scale collection experiments
- targeted parity debugging

Not ready yet for:

- claiming exact seeded equivalence with the Python loop
- replacing Python as the sole source of truth for benchmark/collection correctness

## Recommended Next Steps

1. Fix exact NumPy-compatible no-replacement subset sampling.
2. Update the parity comparer to normalize headline batches before diffing.
3. Re-run seeded parity on a fixed set of seeds such as `123`, `42`, and `120`.
4. Continue moving later stochastic drifts forward until full seeded parity is reached.
