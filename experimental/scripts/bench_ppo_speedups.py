#!/usr/bin/env python3
from __future__ import annotations

import argparse
import contextlib
import io
import json
import sys
import time
from collections.abc import Callable
from dataclasses import asdict, dataclass
from pathlib import Path

import torch

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


@dataclass
class BenchResult:
    name: str
    seconds: float
    steps: int
    games: int

    @property
    def games_per_sec(self) -> float:
        return self.games / self.seconds if self.seconds > 0 else 0.0

    @property
    def steps_per_sec(self) -> float:
        return self.steps / self.seconds if self.seconds > 0 else 0.0


def _device_synchronize(device: str) -> None:
    """Make timing include pending CUDA work when training runs on GPU."""
    if device.startswith("cuda") and torch.cuda.is_available():
        torch.cuda.synchronize()


def _time_call(device: str, fn: Callable[[], list | dict]) -> tuple[float, list | dict]:
    """Time one callable with optional CUDA synchronization around it."""
    _device_synchronize(device)
    t0 = time.perf_counter()
    result = fn()
    _device_synchronize(device)
    return time.perf_counter() - t0, result


def _rollout_bench(
    name: str,
    device: str,
    games: int,
    fn: Callable[[], list],
) -> BenchResult:
    seconds, steps = _time_call(device, fn)
    return BenchResult(name=name, seconds=seconds, steps=len(steps), games=games)


def _update_bench(
    name: str,
    device: str,
    fn: Callable[[], dict],
    n_steps: int,
) -> BenchResult:
    seconds, _ = _time_call(device, fn)
    return BenchResult(name=name, seconds=seconds, steps=n_steps, games=0)


def _try_rollout_bench(
    results: list[BenchResult],
    name: str,
    device: str,
    games: int,
    fn: Callable[[], list],
) -> None:
    """Record rollout timing without aborting the full benchmark on one failure."""
    try:
        results.append(_rollout_bench(name, device, games, fn))
    except Exception as exc:
        print(f"- {name}: skipped ({exc})")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Benchmark experimental PPO speedups")
    parser.add_argument(
        "--checkpoint",
        default="data/checkpoints/retrain_v68/baseline_best.pt",
        help="Checkpoint to load",
    )
    parser.add_argument("--device", default="cuda", help="Training/update device")
    parser.add_argument("--games", type=int, default=64, help="Games per rollout benchmark")
    parser.add_argument("--pool-size", type=int, default=64, help="Rollout batch pool size")
    parser.add_argument("--seed", type=int, default=99000, help="Base RNG seed")
    parser.add_argument("--rollout-workers", type=int, nargs="*", default=[2, 4])
    parser.add_argument("--rollout-thread-options", type=int, nargs="*", default=[1])
    parser.add_argument("--ppo-epochs", type=int, default=2)
    parser.add_argument("--minibatch-size", type=int, default=2048)
    parser.add_argument("--lr", type=float, default=1e-4)
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    return parser.parse_args()


def main() -> None:
    from experimental.ppo.live import load_train_ppo_module
    from experimental.ppo.rollout import (
        ParallelRolloutConfig,
        SelfPlayRolloutExecutor,
        collect_rollout_self_play_single,
    )
    from experimental.ppo.update import pack_steps, ppo_update_packed

    args = parse_args()
    if args.device.startswith("cuda") and not torch.cuda.is_available():
        raise RuntimeError("CUDA requested but not available")

    train_ppo = load_train_ppo_module()

    base_model, _, _ = train_ppo.load_model(args.checkpoint, device=args.device)
    rollout_results: list[BenchResult] = []

    def baseline_rollout() -> list:
        # This is the production-style collector path and serves as the control.
        return train_ppo.collect_rollout_self_play_batched(
            base_model,
            n_games=args.games,
            base_seed=args.seed,
            device=args.device,
        )

    _try_rollout_bench(
        rollout_results,
        "baseline_self_play_cpu",
        "cpu",
        args.games,
        baseline_rollout,
    )

    _try_rollout_bench(
        rollout_results,
        "single_process_cpu",
        "cpu",
        args.games,
        lambda: collect_rollout_self_play_single(
            base_model,
            n_games=args.games,
            base_seed=args.seed,
            rollout_device="cpu",
            pool_size=args.pool_size,
        ),
    )

    if torch.cuda.is_available():
        _try_rollout_bench(
            rollout_results,
            "single_process_cuda",
            "cpu",
            args.games,
            lambda: collect_rollout_self_play_single(
                base_model,
                n_games=args.games,
                base_seed=args.seed,
                rollout_device="cuda",
                pool_size=args.pool_size,
            ),
        )

    for workers in args.rollout_workers:
        for torch_threads in args.rollout_thread_options:
            name = f"parallel_cpu_w{workers}_t{torch_threads}"
            with SelfPlayRolloutExecutor(
                ParallelRolloutConfig(
                    workers=workers,
                    rollout_device="cpu",
                    pool_size=args.pool_size,
                    torch_threads=torch_threads,
                )
            ) as executor:
                _try_rollout_bench(
                    rollout_results,
                    name,
                    "cpu",
                    args.games,
                    lambda executor=executor: executor.collect(
                        base_model,
                        n_games=args.games,
                        base_seed=args.seed,
                    ),
                )

    step_source = collect_rollout_self_play_single(
        base_model,
        n_games=args.games,
        base_seed=args.seed + 1000,
        rollout_device="cpu",
        pool_size=args.pool_size,
    )
    # Reuse the live GAE implementation so only the update mechanics differ.
    train_ppo.compute_gae_batch(step_source)
    packed_steps = pack_steps(step_source)

    baseline_model, _, _ = train_ppo.load_model(args.checkpoint, device=args.device)
    packed_model, _, _ = train_ppo.load_model(args.checkpoint, device=args.device)
    baseline_optimizer = torch.optim.Adam(baseline_model.parameters(), lr=args.lr)
    packed_optimizer = torch.optim.Adam(packed_model.parameters(), lr=args.lr)

    with contextlib.redirect_stdout(io.StringIO()):
        baseline_update_result = _update_bench(
            "baseline_ppo_update",
            args.device,
            lambda: train_ppo.ppo_update(
                step_source,
                baseline_model,
                baseline_optimizer,
                device=args.device,
                ppo_epochs=args.ppo_epochs,
                minibatch_size=args.minibatch_size,
            ),
            len(step_source),
        )

    if not rollout_results:
        raise RuntimeError("No rollout benchmark succeeded")

    packed_update_result = _update_bench(
        "packed_ppo_update",
        args.device,
        lambda: ppo_update_packed(
            packed_steps,
            packed_model,
            packed_optimizer,
            device=args.device,
            ppo_epochs=args.ppo_epochs,
            minibatch_size=args.minibatch_size,
        ),
        len(step_source),
    )

    rollout_summary = [
        {
            **asdict(result),
            "games_per_sec": result.games_per_sec,
            "steps_per_sec": result.steps_per_sec,
        }
        for result in rollout_results
    ]
    update_summary = [
        {
            **asdict(result),
            "steps_per_sec": result.steps_per_sec,
        }
        for result in (baseline_update_result, packed_update_result)
    ]

    best_rollout = max(rollout_results, key=lambda result: result.games_per_sec)
    baseline_rollout_result = next(
        result for result in rollout_results if result.name == "baseline_self_play_cpu"
    )
    speedup_vs_baseline_rollout = (
        best_rollout.games_per_sec / baseline_rollout_result.games_per_sec
        if baseline_rollout_result.games_per_sec > 0 else 0.0
    )
    update_speedup = (
        packed_update_result.steps_per_sec / baseline_update_result.steps_per_sec
        if baseline_update_result.steps_per_sec > 0 else 0.0
    )
    # This is an iteration-level estimate, not a full end-to-end trainer claim.
    combined_baseline_seconds = baseline_rollout_result.seconds + baseline_update_result.seconds
    combined_experimental_seconds = best_rollout.seconds + packed_update_result.seconds
    combined_speedup = (
        combined_baseline_seconds / combined_experimental_seconds
        if combined_experimental_seconds > 0 else 0.0
    )

    payload = {
        "checkpoint": args.checkpoint,
        "games": args.games,
        "pool_size": args.pool_size,
        "device": args.device,
        "rollout_results": rollout_summary,
        "update_results": update_summary,
        "best_rollout": best_rollout.name,
        "rollout_speedup_vs_baseline": speedup_vs_baseline_rollout,
        "update_speedup_vs_baseline": update_speedup,
        "combined_baseline_seconds": combined_baseline_seconds,
        "combined_experimental_seconds": combined_experimental_seconds,
        "combined_speedup_vs_baseline": combined_speedup,
    }

    if args.json:
        print(json.dumps(payload, indent=2))
        return

    print("Rollout benchmarks")
    for item in rollout_summary:
        print(
            f"- {item['name']}: {item['seconds']:.3f}s, "
            f"{item['games_per_sec']:.2f} games/s, {item['steps']} steps"
        )

    print("\nPPO update benchmarks")
    for item in update_summary:
        print(
            f"- {item['name']}: {item['seconds']:.3f}s, "
            f"{item['steps_per_sec']:.2f} steps/s"
        )

    print("\nSummary")
    print(
        f"- Best rollout: {best_rollout.name} "
        f"({speedup_vs_baseline_rollout:.2f}x vs baseline_self_play_cpu)"
    )
    print(f"- Packed PPO update speedup: {update_speedup:.2f}x")
    print(f"- Estimated combined rollout+update speedup: {combined_speedup:.2f}x")


if __name__ == "__main__":
    main()
