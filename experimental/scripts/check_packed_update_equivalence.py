#!/usr/bin/env python3
from __future__ import annotations

import argparse
import contextlib
import io
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import torch

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


@dataclass
class DiffSummary:
    max_abs: float
    max_rel: float
    worst_key: str | None


def _compare_named_tensors(
    left: dict[str, torch.Tensor],
    right: dict[str, torch.Tensor],
) -> DiffSummary:
    max_abs = 0.0
    max_rel = 0.0
    worst_key: str | None = None
    for key, left_tensor in left.items():
        right_tensor = right[key]
        abs_diff = (left_tensor - right_tensor).abs()
        local_abs = float(abs_diff.max().item()) if abs_diff.numel() else 0.0
        denom = torch.maximum(left_tensor.abs(), right_tensor.abs()).clamp_min(1e-12)
        rel_diff = abs_diff / denom
        local_rel = float(rel_diff.max().item()) if rel_diff.numel() else 0.0
        if local_abs > max_abs:
            max_abs = local_abs
            max_rel = local_rel
            worst_key = key
    return DiffSummary(max_abs=max_abs, max_rel=max_rel, worst_key=worst_key)


def _state_dict_cpu(module: torch.nn.Module) -> dict[str, torch.Tensor]:
    return {key: value.detach().cpu().clone() for key, value in module.state_dict().items()}


def _optimizer_state_cpu(optimizer: torch.optim.Optimizer) -> dict[str, torch.Tensor]:
    result: dict[str, torch.Tensor] = {}
    for state_idx, state in optimizer.state_dict()["state"].items():
        for key, value in state.items():
            if torch.is_tensor(value):
                result[f"{state_idx}:{key}"] = value.detach().cpu().clone()
    return result


def _metrics_diff(left: dict[str, float], right: dict[str, float]) -> DiffSummary:
    max_abs = 0.0
    max_rel = 0.0
    worst_key: str | None = None
    for key, left_value in left.items():
        right_value = right[key]
        abs_diff = abs(left_value - right_value)
        denom = max(abs(left_value), abs(right_value), 1e-12)
        rel_diff = abs_diff / denom
        if abs_diff > max_abs:
            max_abs = abs_diff
            max_rel = rel_diff
            worst_key = key
    return DiffSummary(max_abs=max_abs, max_rel=max_rel, worst_key=worst_key)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check packed PPO update equivalence")
    parser.add_argument(
        "--checkpoint",
        default="data/checkpoints/retrain_v68/baseline_best.pt",
        help="Checkpoint to load",
    )
    parser.add_argument("--device", default="cpu", help="Execution device for the update")
    parser.add_argument("--games", type=int, default=32, help="Games for rollout collection")
    parser.add_argument("--pool-size", type=int, default=64, help="Rollout pool size")
    parser.add_argument("--seed", type=int, default=99000, help="Base seed")
    parser.add_argument("--ppo-epochs", type=int, default=2)
    parser.add_argument("--minibatch-size", type=int, default=1024)
    parser.add_argument("--lr", type=float, default=1e-4)
    parser.add_argument("--atol", type=float, default=1e-6)
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def main() -> None:
    from experimental.ppo.live import load_train_ppo_module
    from experimental.ppo.rollout import collect_rollout_self_play_single
    from experimental.ppo.update import pack_steps, ppo_update_packed

    args = parse_args()
    if args.device.startswith("cuda") and not torch.cuda.is_available():
        raise RuntimeError("CUDA requested but not available")

    train_ppo = load_train_ppo_module()

    rollout_model, _, _ = train_ppo.load_model(args.checkpoint, device=args.device)
    steps = collect_rollout_self_play_single(
        rollout_model,
        n_games=args.games,
        base_seed=args.seed,
        rollout_device="cpu",
        pool_size=args.pool_size,
    )
    train_ppo.compute_gae_batch(steps)
    packed_steps = pack_steps(steps)

    baseline_model, _, _ = train_ppo.load_model(args.checkpoint, device=args.device)
    packed_model, _, _ = train_ppo.load_model(args.checkpoint, device=args.device)
    baseline_optimizer = torch.optim.Adam(baseline_model.parameters(), lr=args.lr)
    packed_optimizer = torch.optim.Adam(packed_model.parameters(), lr=args.lr)

    torch.manual_seed(args.seed + 12345)
    with contextlib.redirect_stdout(io.StringIO()):
        baseline_metrics = train_ppo.ppo_update(
            steps,
            baseline_model,
            baseline_optimizer,
            device=args.device,
            ppo_epochs=args.ppo_epochs,
            minibatch_size=args.minibatch_size,
        )

    torch.manual_seed(args.seed + 12345)
    packed_metrics = ppo_update_packed(
        packed_steps,
        packed_model,
        packed_optimizer,
        device=args.device,
        ppo_epochs=args.ppo_epochs,
        minibatch_size=args.minibatch_size,
        perm_device="cpu",
    )

    metric_diff = _metrics_diff(baseline_metrics, packed_metrics)
    param_diff = _compare_named_tensors(
        _state_dict_cpu(baseline_model),
        _state_dict_cpu(packed_model),
    )
    opt_diff = _compare_named_tensors(
        _optimizer_state_cpu(baseline_optimizer),
        _optimizer_state_cpu(packed_optimizer),
    )

    exact_metrics = metric_diff.max_abs == 0.0
    exact_params = param_diff.max_abs == 0.0
    exact_optim = opt_diff.max_abs == 0.0
    within_tol = (
        metric_diff.max_abs <= args.atol
        and param_diff.max_abs <= args.atol
        and opt_diff.max_abs <= args.atol
    )

    payload: dict[str, Any] = {
        "checkpoint": args.checkpoint,
        "device": args.device,
        "games": args.games,
        "steps": len(steps),
        "ppo_epochs": args.ppo_epochs,
        "minibatch_size": args.minibatch_size,
        "baseline_metrics": baseline_metrics,
        "packed_metrics": packed_metrics,
        "metric_diff": asdict(metric_diff),
        "param_diff": asdict(param_diff),
        "optimizer_diff": asdict(opt_diff),
        "exact_metrics": exact_metrics,
        "exact_params": exact_params,
        "exact_optimizer": exact_optim,
        "within_tolerance": within_tol,
        "atol": args.atol,
    }

    if args.json:
        print(json.dumps(payload, indent=2))
        return

    print(f"steps={len(steps)} device={args.device}")
    print(
        f"metrics exact={exact_metrics} "
        f"max_abs={metric_diff.max_abs:.3e} key={metric_diff.worst_key}"
    )
    print(
        f"params exact={exact_params} "
        f"max_abs={param_diff.max_abs:.3e} key={param_diff.worst_key}"
    )
    print(
        f"optimizer exact={exact_optim} "
        f"max_abs={opt_diff.max_abs:.3e} key={opt_diff.worst_key}"
    )
    print(f"within tolerance ({args.atol:g}) = {within_tol}")

    if not within_tol:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
