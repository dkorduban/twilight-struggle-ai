# Spec: Restartable Benchmark Runner

## Goal

Replace the current pattern of long-running single-shot `benchmark_batched`/`benchmark_mcts`
calls with a Python wrapper that runs in small batches, emits partial results to a JSON file
after each batch, and can be restarted from where it left off. Supports progress reporting,
graceful interruption, and job resumption.

## Problem

Current benchmark calls are single blocking C++ calls: `tscore.benchmark_batched(model, side, 500, ...)`
takes 40s-5hours depending on sim count, with zero progress visibility. If killed, all work is lost.

## Files to create

- `scripts/bench_resumable.py` — the restartable benchmark runner

## Files to reference (read-only)

- `bindings/tscore_bindings.cpp` lines 542-665 — `benchmark_batched` and `benchmark_mcts` signatures
- `scripts/bench_gpu.py` — existing benchmark script pattern (model loading, result printing)
- `scripts/run_v110_data_sweep.sh` — shows how benchmarks are called from sweep scripts

## Interface

```
uv run python scripts/bench_resumable.py \
    --checkpoint data/checkpoints/v106_cf_gnn_s42/baseline_best_scripted.pt \
    --sides both \
    --n-games 500 \
    --seed 50000 \
    --batch-size 50 \
    --n-sim 0 \
    --pool-size 32 \
    --nash-temperatures \
    --job-dir results/bench_jobs
```

### Arguments

| Arg | Default | Description |
|-----|---------|-------------|
| `--checkpoint` | required | Path to .pt checkpoint (raw or scripted) |
| `--sides` | `both` | `ussr`, `us`, or `both` |
| `--n-games` | 500 | Games per side |
| `--seed` | 50000 | Base seed (US side uses seed + n_games) |
| `--batch-size` | 50 | Games per C++ call (progress granularity) |
| `--n-sim` | 0 | MCTS simulations (0 = greedy) |
| `--pool-size` | 32 | Concurrent game pool |
| `--nash-temperatures` | flag | Use Nash temperature sampling |
| `--job-dir` | `results/bench_jobs` | Directory for job state files |
| `--job-id` | auto | Resume a specific job (default: generate new UUID) |

### Output

On startup, prints:
```
[bench] job_id: a1b2c3d4
[bench] checkpoint: data/checkpoints/v106_cf_gnn_s42/baseline_best_scripted.pt
[bench] config: sides=both n_games=500 seed=50000 n_sim=0 batch_size=50
[bench] progress: 0/1000 games (0 USSR, 0 US)
```

After each batch:
```
[bench] batch 1/10 USSR: 50 games in 4.2s (11.9 g/s) — 32 wins, 15 losses, 3 draws
[bench] progress: 50/1000 games | USSR 64.0% (32/50) | cumulative
```

On completion:
```
[bench] DONE job_id=a1b2c3d4
[bench] USSR: 55.8% (279/500) | US: 14.0% (70/500) | Combined: 34.9%
[bench] Total: 82.3s | Saved to results/bench_jobs/a1b2c3d4.json
```

## Job state file

`results/bench_jobs/{job_id}.json`:

```json
{
    "job_id": "a1b2c3d4",
    "status": "running",
    "checkpoint": "data/checkpoints/v106_cf_gnn_s42/baseline_best_scripted.pt",
    "sides": "both",
    "n_games": 500,
    "seed": 50000,
    "n_sim": 0,
    "pool_size": 32,
    "nash_temperatures": true,
    "batch_size": 50,
    "created_at": "2026-04-05T22:30:00",
    "updated_at": "2026-04-05T22:31:00",
    "tasks": [
        {
            "side": "ussr",
            "seed": 50000,
            "total_games": 500,
            "completed_games": 250,
            "wins": 140,
            "losses": 100,
            "draws": 10,
            "elapsed_s": 41.2,
            "batches_done": 5
        },
        {
            "side": "us",
            "seed": 50500,
            "total_games": 500,
            "completed_games": 0,
            "wins": 0,
            "losses": 0,
            "draws": 0,
            "elapsed_s": 0,
            "batches_done": 0
        }
    ]
}
```

## Algorithm

### Seed arithmetic for batching

The C++ `benchmark_batched`/`benchmark_mcts` assigns game `i` the seed `base_seed + i`.
So running 500 games with seed=50000 is equivalent to:
- Batch 0: 50 games, seed=50000
- Batch 1: 50 games, seed=50050
- ...
- Batch 9: 50 games, seed=50450

Each batch produces identical results to the corresponding slice of a single 500-game run.
**This is what makes resumption correct** — we don't need to replay previous batches.

### Startup

1. If `--job-id` provided: load `{job_dir}/{job_id}.json`, validate params match, resume
2. Else: generate UUID, create job file, start fresh
3. Export checkpoint to TorchScript if needed (check if `_scripted.pt` exists)

### Main loop

```python
for task in job["tasks"]:  # ussr, then us
    side = task["side"]
    remaining = task["total_games"] - task["completed_games"]
    current_seed = task["seed"] + task["completed_games"]
    
    while remaining > 0:
        batch = min(batch_size, remaining)
        
        if n_sim == 0:
            results = tscore.benchmark_batched(
                scripted_model, side_enum, batch,
                pool_size=pool_size, seed=current_seed,
                nash_temperatures=nash_temperatures)
        else:
            results = tscore.benchmark_mcts(
                scripted_model, side_enum, batch,
                n_simulations=n_sim, pool_size=pool_size,
                seed=current_seed,
                nash_temperatures=nash_temperatures)
        
        # Count results
        wins = sum(1 for r in results if r.winner == side_enum)
        losses = sum(1 for r in results if r.winner == other_side)
        draws = batch - wins - losses
        
        # Update task state
        task["completed_games"] += batch
        task["wins"] += wins
        task["losses"] += losses
        task["draws"] += draws
        
        # Save checkpoint + print progress
        save_job(job)
        print_progress(job)
        
        remaining -= batch
        current_seed += batch

job["status"] = "done"
save_job(job)
print_summary(job)
```

### Resume

On resume, the loop simply skips already-completed batches because `completed_games`
is already advanced and `current_seed` starts from where we left off. No state beyond
the JSON file is needed.

### TorchScript export

The C++ bindings need a TorchScript model path (string), not a Python model object.
If `--checkpoint` points to a raw `.pt` file (not `*_scripted.pt`), auto-export:

```python
scripted_path = checkpoint.replace(".pt", "_scripted.pt")
if not os.path.exists(scripted_path):
    # Use existing export logic from export_baseline_to_torchscript.py
    subprocess.run(["uv", "run", "python", "cpp/tools/export_baseline_to_torchscript.py",
                     "--checkpoint", checkpoint, "--out", scripted_path], check=True)
```

If checkpoint already ends with `_scripted.pt`, use directly.

## Constraints

- Pure Python script — no C++ or binding changes needed
- Must work with existing `tscore.benchmark_batched` and `tscore.benchmark_mcts` APIs
- Batch seed arithmetic must produce bit-identical results to single-shot runs
- Job file is the only state — no database, no lock files
- `--batch-size` defaults to 50 (good granularity: ~4s for greedy, ~5min for 800sim)
- Print to stdout, not stderr (for easy `tee` and pipe)

## Test plan

1. **Seed correctness**: Run 100 games single-shot (seed=50000) and 2×50 batched
   (seed=50000, seed=50050). Verify identical win counts.
2. **Resume**: Run 100 games with batch=50, kill after batch 1, resume with same job_id.
   Verify final results match a fresh 100-game run.
3. **Both sides**: Run with `--sides both --n-games 10 --batch-size 5`. Verify USSR
   runs first (2 batches), then US (2 batches), progress shows both.
4. **MCTS mode**: Run with `--n-sim 100 --n-games 10 --batch-size 5`. Verify completes.

## Acceptance criteria

- [ ] `--batch-size 50` produces identical aggregate results to single-shot 500 games
- [ ] Resume from job file produces correct final results
- [ ] Progress printed after each batch with cumulative stats
- [ ] Job JSON updated atomically after each batch
- [ ] Works with both `benchmark_batched` (n_sim=0) and `benchmark_mcts` (n_sim>0)
