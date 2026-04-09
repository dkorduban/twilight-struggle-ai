# PPO Speedup Findings

This document records what was tested in `experimental/`, what the code does,
and what the benchmark results mean.

## Objective

The goal was to identify practical ways to speed up PPO iteration time without
modifying production code.

The current production PPO path in [`scripts/train_ppo.py`](/home/dkord/code/twilight-struggle-ai/scripts/train_ppo.py)
has two dominant pieces of work:

1. Rollout collection
2. PPO update on the collected steps

Earlier code reading showed two likely bottlenecks:

- Rollout collection uses a single Python process calling a native C++ batched
  collector. The collector itself runs a single scheduling loop, so overall CPU
  utilization can stay low even on a 20-vCPU machine.
- PPO update rebuilds minibatch tensors from Python objects on every epoch and
  every minibatch. That creates a large amount of repeated `torch.cat`,
  `torch.stack`, Python list slicing, and device transfer work.

## Experimental variants

Everything here stays inside `experimental/` and reuses the live trainer as a
reference implementation.

### 1. Baseline rollout

This is the current production-style self-play collector from
`scripts/train_ppo.py`, used as the comparison point:

- one Python process
- native `tscore.rollout_self_play_batched`
- rollout inference hardcoded to CPU in the live trainer

### 2. Single-process rollout with configurable inference device

Implemented in [`experimental/ppo/rollout.py`](/home/dkord/code/twilight-struggle-ai/experimental/ppo/rollout.py):

- still one Python process
- still one native collector call
- unlike production, can choose `rollout_device="cpu"` or `"cuda"`

This isolates whether the rollout inference device is the main bottleneck.

### 3. Process-sharded rollout

Also implemented in [`experimental/ppo/rollout.py`](/home/dkord/code/twilight-struggle-ai/experimental/ppo/rollout.py):

- export the model once to TorchScript
- split `n_games` across multiple worker processes
- each worker runs its own `tscore.rollout_self_play_batched`
- worker results are converted back into `Step` objects in the parent

This targets the actual underutilization problem: the single-process path does
not keep many CPU cores busy for long enough.

### 4. Packed PPO update

Implemented in [`experimental/ppo/update.py`](/home/dkord/code/twilight-struggle-ai/experimental/ppo/update.py):

- pack all rollout steps once into dense tensors
- move the packed tensors to device once
- during PPO epochs, minibatches are selected with `index_select`
- avoid rebuilding masks, indices, and padded country targets every minibatch

This targets Python overhead and repeated tensor assembly in the update loop.

## Benchmark driver

The benchmark entrypoint is
[`experimental/scripts/bench_ppo_speedups.py`](/home/dkord/code/twilight-struggle-ai/experimental/scripts/bench_ppo_speedups.py).

What it does:

1. Load a checkpoint using the live `load_model` helper.
2. Measure several rollout variants.
3. Collect one rollout batch for PPO update benchmarking.
4. Compute GAE using the live helper.
5. Compare:
   - live `ppo_update`
   - experimental `ppo_update_packed`
6. Report per-component speedups and a simple combined iteration estimate:
   `best_rollout_time + packed_update_time` versus
   `baseline_rollout_time + baseline_update_time`.

This is not a full alternate trainer. It is a component benchmark focused on
iteration throughput.

## Results

Two runs were collected.

### Shakeout run

Command:

```bash
uv run python experimental/scripts/bench_ppo_speedups.py \
  --games 16 \
  --ppo-epochs 1 \
  --minibatch-size 512 \
  --rollout-workers 2 4 \
  --rollout-thread-options 1 2 \
  --json
```

This run was mainly for validation. It showed:

- packed PPO update was already much faster than baseline
- rollout variants were noisy at 16 games
- CUDA rollout did not look promising on this setup

The 16-game run should not be treated as the final throughput conclusion.

### Main run

Command:

```bash
uv run python experimental/scripts/bench_ppo_speedups.py \
  --games 200 \
  --ppo-epochs 2 \
  --minibatch-size 2048 \
  --rollout-workers 2 4 \
  --rollout-thread-options 1 2 \
  --json
```

Results:

| Variant | Seconds | Games/s | Steps/s |
|---|---:|---:|---:|
| `baseline_self_play_cpu` | 15.61 | 12.81 | 1800.25 |
| `single_process_cpu` | 15.39 | 13.00 | 1850.15 |
| `single_process_cuda` | 18.19 | 11.00 | 1536.35 |
| `parallel_cpu_w2_t1` | 10.97 | 18.24 | 2595.73 |
| `parallel_cpu_w2_t2` | 10.51 | 19.03 | 2716.44 |
| `parallel_cpu_w4_t1` | 7.70 | 25.99 | 3746.04 |
| `parallel_cpu_w4_t2` | 8.70 | 23.00 | 3161.18 |

PPO update:

| Variant | Seconds | Steps/s |
|---|---:|---:|
| `baseline_ppo_update` | 6.36 | 4438.73 |
| `packed_ppo_update` | 0.53 | 53136.18 |

Derived speedups:

- Best rollout variant: `parallel_cpu_w4_t1`
- Rollout speedup vs baseline rollout: `2.03x`
- Packed update speedup vs baseline update: `11.97x`
- Estimated combined rollout + update speedup: `2.67x`

## Packed Update Exactness

After the speed benchmark, the next question was whether
`ppo_update_packed()` is merely close to the live `ppo_update()` or whether it
is actually performing the same update.

To test that, an exactness checker was added in
[`experimental/scripts/check_packed_update_equivalence.py`](/home/dkord/code/twilight-struggle-ai/experimental/scripts/check_packed_update_equivalence.py).

What it does:

1. Collect one rollout batch.
2. Run live `compute_gae_batch`.
3. Load two identical model/optimizer pairs from the same checkpoint.
4. Seed Torch identically before each updater call.
5. Run:
   - live `ppo_update`
   - experimental `ppo_update_packed`
6. Compare:
   - returned metrics
   - full model `state_dict()`
   - full optimizer tensor state

One extra detail matters here: the live updater samples minibatch permutations
on CPU. The packed updater now exposes an experimental `perm_device` knob so
the equivalence test can force the packed path to use the same CPU-side
permutation stream.

### CPU exactness check

Command:

```bash
uv run python experimental/scripts/check_packed_update_equivalence.py \
  --device cpu \
  --games 32 \
  --ppo-epochs 2 \
  --minibatch-size 1024 \
  --json
```

Results:

- steps: `4615`
- model parameter max abs diff: `0.0`
- optimizer tensor-state max abs diff: `0.0`
- metric max abs diff: `1.12e-9`

The only non-zero metric difference was `approx_kl`, at the `1e-9` level.

### CUDA exactness check

Command:

```bash
uv run python experimental/scripts/check_packed_update_equivalence.py \
  --device cuda \
  --games 32 \
  --ppo-epochs 2 \
  --minibatch-size 1024 \
  --json
```

Results:

- steps: `4505`
- model parameter max abs diff: `0.0`
- optimizer tensor-state max abs diff: `0.0`
- metric max abs diff: `6.33e-9`

Again, the only non-zero metric difference was `approx_kl`, and it remained in
the low `1e-9` range.

### Interpretation

For the actual training update, packed and non-packed are equivalent in the
meaningful sense established here:

- same post-update parameters
- same post-update optimizer state
- same losses and PPO statistics up to tiny floating-point reporting noise

The remaining `approx_kl` delta is expected because the two implementations use
slightly different but mathematically equivalent formulas:

- live updater: `((r - 1) - log(r + 1e-10))`
- packed updater: `((r - 1) - (new_log_probs - old_log_probs))`

Since `r = exp(new_log_probs - old_log_probs)`, both expressions represent the
same quantity, but the final floating-point rounding path is not identical.

## Interpretation

### What worked

#### Process-level rollout sharding

This was the main rollout win.

The best configuration on this machine was:

- `4` worker processes
- `1` Torch thread per worker
- CPU inference

That is consistent with the earlier code-reading hypothesis:

- the native collector is not a highly parallel scheduler
- one process does not saturate the machine
- multiple independent collectors scale better than “more threads in one process”

#### Packed PPO update

This is the clearest single win in the whole experiment.

The baseline update loop repeatedly reconstructs minibatches from Python
objects. The packed path pays the assembly cost once, then uses dense tensors
for all PPO epochs. On the 200-game run this reduced update time from `6.36s`
to `0.53s`.

The equivalence check above also matters operationally: this speedup did not
change the learned update in any meaningful way. On both CPU and CUDA, the
experimental packed update produced identical model and optimizer states to the
live updater when fed the same minibatch order.

### What did not work

#### CUDA rollout inference

On this host, `single_process_cuda` was slower than CPU rollout.

That suggests rollout is not dominated by the model forward pass alone. The
native collector still has substantial CPU-side game stepping, decision logic,
and step-materialization overhead. Moving the policy forward pass to CUDA does
not compensate for that at this problem size.

#### More Torch threads per rollout worker

`parallel_cpu_w4_t2` was slower than `parallel_cpu_w4_t1`.

That is a sign of oversubscription:

- too many worker processes times too many intra-op threads
- extra contention instead of useful parallel work

On this machine, more small workers beat fewer fatter workers.

## Code walkthrough

## `experimental/ppo/live.py`

Purpose:

- load the live PPO trainer module by path
- reuse its helpers without importing production code as a package dependency

Why this exists:

- production trainer lives in `scripts/`
- experiments need access to `Step`, `load_model`, `compute_gae_batch`,
  `_export_temp_model`, and `ppo_update`
- this file provides that bridge without changing production code

## `experimental/ppo/rollout.py`

Purpose:

- prototype rollout collection variants

Key pieces:

- `_ensure_repo_on_path()`
  - makes sure worker processes can import `tscore` and the Python package
- `_step_from_rollout_dict()`
  - converts native rollout dicts into live `Step` dataclass instances
- `collect_rollout_self_play_single()`
  - one-process collector with configurable rollout device
- `_collect_rollout_self_play_worker()`
  - worker entrypoint for process-sharded rollout
  - computes terminal reward and `done` inside the worker so the payload that
    crosses process boundaries stays plain Python/numpy data
- `SelfPlayRolloutExecutor`
  - keeps a persistent process pool alive
  - exports the model once per benchmark call
  - shards games across workers and reassembles the resulting steps

Important implementation details:

- `spawn` multiprocessing is used for safety with Torch and native bindings
- worker-local `torch.set_num_threads()` lets us test whether more intra-op
  threading inside each worker helps
- sharded rollout uses separate seeds per worker shard to avoid identical games

## `experimental/ppo/update.py`

Purpose:

- prototype a low-overhead PPO update path

Key pieces:

- `PackedSteps`
  - one container holding every tensor needed by PPO update
- `pack_steps()`
  - performs one-time packing
  - normalizes advantages per side
  - pads variable-length country targets into a dense matrix
- `ppo_update_packed()`
  - moves the packed batch to device once
  - uses `index_select` to form minibatches
  - keeps the same overall PPO objective shape as the live trainer
  - exposes `perm_device` so the exactness checker can force the same CPU-side
    minibatch permutations as the live updater

Important implementation details:

- this is still the same broad PPO math as the live trainer
- the gain comes mostly from eliminating repeated Python and tensor assembly
- memory use is higher because the full packed rollout batch is resident on
  device during the update

## `experimental/scripts/bench_ppo_speedups.py`

Purpose:

- run the rollout and update benchmarks

Flow:

1. load checkpoint
2. benchmark rollout variants
3. collect a step batch for update benchmarking
4. run GAE
5. benchmark baseline update and packed update
6. report individual and combined speedups

Notable design choices:

- baseline update stdout is silenced because the live trainer prints diagnostics
- rollout variants are wrapped in `_try_rollout_bench()` so one failure does not
  kill the whole benchmark
- combined speedup is only an estimate for one PPO iteration shape, not a claim
  about full training runs over many iterations

## `experimental/scripts/check_packed_update_equivalence.py`

Purpose:

- verify that the packed updater is not just faster, but effectively the same
  update as the live trainer

Flow:

1. collect one rollout batch
2. compute GAE with the live helper
3. load two identical model/optimizer pairs
4. seed Torch identically before each updater
5. compare metrics, model state, and optimizer state

What to look at:

- `param_diff.max_abs`
- `optimizer_diff.max_abs`
- `metric_diff.max_abs`

In the current experiments, parameter and optimizer diffs were exactly `0.0` on
both CPU and CUDA.

## Practical recommendation

If these ideas were promoted later, the best first production candidate is:

1. process-sharded CPU rollout with around `4` workers and `1` Torch thread each
2. packed PPO update

That combination gave the best measured improvement here.

I would not prioritize CUDA rollout inference based on these results.

## Caveats

- These numbers are from component benchmarks, not a full promoted trainer.
- Only the self-play rollout path was benchmarked directly.
- The packed update keeps the full rollout batch on device, which may need more
  careful memory management at larger scales.
- Sharded rollout returns steps to the parent process, so very large step
  volumes may start paying noticeable IPC and deserialization cost.
- The exactness check forces the packed path to use CPU-side minibatch
  permutations to match the live updater. If the packed path uses device-local
  `randperm` in normal operation, exact step-for-step comparison is no longer
  expected even though the algorithm is still the same.
