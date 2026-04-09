from __future__ import annotations

import math
import os
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import torch

from experimental.ppo.live import load_train_ppo_module


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _ensure_repo_on_path() -> None:
    """Make live Python and native bindings importable in child processes."""
    import sys

    repo_root = _repo_root()
    py_dir = repo_root / "python"
    build_candidates = (
        repo_root / "build" / "bindings",
        repo_root / "build-ninja" / "bindings",
    )
    for candidate in build_candidates:
        candidate_str = str(candidate)
        if candidate.exists() and candidate_str not in sys.path:
            sys.path.insert(0, candidate_str)
            break
    py_dir_str = str(py_dir)
    if py_dir_str not in sys.path:
        sys.path.insert(0, py_dir_str)


def _step_from_rollout_dict(step_dict: dict[str, Any]) -> Any:
    """Convert a native rollout record into the live ``Step`` dataclass.

    The prototype deliberately reuses the production ``Step`` type so the
    experimental update path can be compared against the live PPO update with
    identical step objects.
    """
    train_ppo = load_train_ppo_module()
    country_mask = torch.from_numpy(step_dict["country_mask"])
    return train_ppo.Step(
        influence=torch.from_numpy(step_dict["influence"]).unsqueeze(0),
        cards=torch.from_numpy(step_dict["cards"]).unsqueeze(0),
        scalars=torch.from_numpy(step_dict["scalars"]).unsqueeze(0),
        card_mask=torch.from_numpy(step_dict["card_mask"]),
        mode_mask=torch.from_numpy(step_dict["mode_mask"]),
        country_mask=country_mask if bool(country_mask.any()) else None,
        card_idx=step_dict["card_idx"],
        mode_idx=step_dict["mode_idx"],
        country_targets=list(step_dict["country_targets"]),
        old_log_prob=float(step_dict["log_prob"]),
        value=float(step_dict["value"]),
        side_int=int(step_dict["side_int"]),
        raw_ussr_influence=step_dict["raw_ussr_influence"].tolist()
        if "raw_ussr_influence" in step_dict else None,
        raw_us_influence=step_dict["raw_us_influence"].tolist()
        if "raw_us_influence" in step_dict else None,
        raw_turn=int(step_dict["raw_turn"]) if "raw_turn" in step_dict else None,
        raw_ar=int(step_dict["raw_ar"]) if "raw_ar" in step_dict else None,
        raw_defcon=int(step_dict["raw_defcon"]) if "raw_defcon" in step_dict else None,
        raw_vp=int(step_dict["raw_vp"]) if "raw_vp" in step_dict else None,
        raw_milops=list(step_dict["raw_milops"]) if "raw_milops" in step_dict else None,
        raw_space=list(step_dict["raw_space"]) if "raw_space" in step_dict else None,
        hand_card_ids=list(step_dict["hand_card_ids"]) if "hand_card_ids" in step_dict else None,
    )


def _annotate_terminal_rewards(
    results: list[Any],
    steps: list[Any],
    boundaries: list[int],
    vp_reward_coef: float,
) -> list[Any]:
    """Apply terminal reward/done flags using the live reward helper."""
    train_ppo = load_train_ppo_module()
    for i, result in enumerate(results):
        start = boundaries[i]
        end = boundaries[i + 1] if i + 1 < len(boundaries) else len(steps)
        if start >= end:
            continue
        last = steps[end - 1]
        last.reward = train_ppo._compute_reward(result, last.side_int, vp_reward_coef)
        last.done = True
    return steps


def collect_rollout_self_play_single(
    model: torch.nn.Module,
    n_games: int,
    base_seed: int,
    rollout_device: str,
    pool_size: int,
    vp_reward_coef: float = 0.0,
) -> list[Any]:
    """Single-process self-play rollout with selectable inference device.

    This mirrors the production self-play collector but exposes the native
    rollout ``device`` argument so the experiment can answer whether moving the
    policy forward pass to CUDA materially improves end-to-end rollout speed.
    """
    train_ppo = load_train_ppo_module()
    _ensure_repo_on_path()
    import tscore

    script_path = train_ppo._export_temp_model(model)
    try:
        results, raw_steps, boundaries = tscore.rollout_self_play_batched(
            model_path=script_path,
            n_games=n_games,
            pool_size=min(n_games, pool_size),
            seed=base_seed,
            device=rollout_device,
            temperature=1.0,
            nash_temperatures=True,
        )
    finally:
        try:
            os.remove(script_path)
        except OSError:
            pass
    steps = [_step_from_rollout_dict(step) for step in raw_steps]
    return _annotate_terminal_rewards(results, steps, boundaries, vp_reward_coef)


def _collect_rollout_self_play_worker(
    model_path: str,
    n_games: int,
    base_seed: int,
    rollout_device: str,
    pool_size: int,
    torch_threads: int | None,
    vp_reward_coef: float,
) -> list[dict[str, Any]]:
    """Worker-side rollout shard for process-parallel experiments.

    Reward annotation happens inside the worker because ``tscore.GameResult`` is
    not process-pickleable. By converting each step to a plain dict and writing
    ``reward``/``done`` here, the parent process only receives plain Python /
    NumPy payloads.
    """
    _ensure_repo_on_path()
    train_ppo = load_train_ppo_module()
    if torch_threads is not None:
        torch.set_num_threads(torch_threads)
        if hasattr(torch, "set_num_interop_threads"):
            try:
                torch.set_num_interop_threads(1)
            except RuntimeError:
                pass
    import tscore

    results, raw_steps, boundaries = tscore.rollout_self_play_batched(
        model_path=model_path,
        n_games=n_games,
        pool_size=min(n_games, pool_size),
        seed=base_seed,
        device=rollout_device,
        temperature=1.0,
        nash_temperatures=True,
    )
    steps = [dict(step) for step in raw_steps]
    for i, result in enumerate(results):
        start = boundaries[i]
        end = boundaries[i + 1] if i + 1 < len(boundaries) else len(steps)
        if start >= end:
            continue
        last = steps[end - 1]
        last["reward"] = train_ppo._compute_reward(
            result,
            int(last["side_int"]),
            vp_reward_coef,
        )
        last["done"] = True
    return steps


@dataclass
class ParallelRolloutConfig:
    """Configuration for a process-sharded self-play rollout collector."""
    workers: int
    rollout_device: str
    pool_size: int
    torch_threads: int | None = None


class SelfPlayRolloutExecutor:
    """Persistent process pool for sharded self-play rollout collection.

    The live PPO path uses one Python process. This executor tests the simpler
    alternative to native scheduler refactoring: run several independent native
    collectors in parallel and merge the resulting steps in Python.
    """

    def __init__(self, config: ParallelRolloutConfig) -> None:
        if config.workers < 1:
            raise ValueError("workers must be >= 1")
        self.config = config
        self._pool = ProcessPoolExecutor(
            max_workers=config.workers,
            mp_context=torch.multiprocessing.get_context("spawn"),
        )

    def close(self) -> None:
        self._pool.shutdown(wait=True, cancel_futures=False)

    def __enter__(self) -> SelfPlayRolloutExecutor:
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

    def collect(
        self,
        model: torch.nn.Module,
        n_games: int,
        base_seed: int,
        vp_reward_coef: float = 0.0,
    ) -> list[Any]:
        """Export once, shard games across workers, and rebuild live Step objects."""
        train_ppo = load_train_ppo_module()
        script_path = train_ppo._export_temp_model(model)
        try:
            # Use an even split with the first few workers taking the remainder.
            per_worker = [n_games // self.config.workers] * self.config.workers
            for i in range(n_games % self.config.workers):
                per_worker[i] += 1
            futures = []
            seed = base_seed
            for shard_games in per_worker:
                if shard_games <= 0:
                    continue
                # Keep each worker's local pool smaller than the global pool so
                # process-level parallelism, not one giant local batch, is the
                # thing being measured.
                shard_pool = min(
                    shard_games,
                    max(1, math.ceil(self.config.pool_size / self.config.workers)),
                )
                futures.append(
                    self._pool.submit(
                        _collect_rollout_self_play_worker,
                        script_path,
                        shard_games,
                        seed,
                        self.config.rollout_device,
                        shard_pool,
                        self.config.torch_threads,
                        vp_reward_coef,
                    )
                )
                seed += shard_games

            all_steps: list[Any] = []
            for future in futures:
                raw_steps = future.result()
                steps = [_step_from_rollout_dict(step) for step in raw_steps]
                # Reward/done were written into plain dict payloads in the worker.
                for step_obj, step_dict in zip(steps, raw_steps, strict=True):
                    step_obj.reward = float(step_dict.get("reward", 0.0))
                    step_obj.done = bool(step_dict.get("done", False))
                all_steps.extend(steps)
            return all_steps
        finally:
            try:
                os.remove(script_path)
            except OSError:
                pass
