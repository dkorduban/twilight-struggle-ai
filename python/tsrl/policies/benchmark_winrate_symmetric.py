"""Symmetric win-rate benchmark scaffold for policy-vs-policy evaluation."""
from __future__ import annotations

import argparse
import importlib.util
import sys
from collections.abc import Sequence
from pathlib import Path

from tsrl.engine.game_loop import Policy, play_game
from tsrl.schemas import Side


def _load_policy(path: str) -> Policy:
    module_path = Path(path).resolve()
    module_name = f"_benchmark_policy_{module_path.stem}_{abs(hash(module_path))}"
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Failed to load policy module from {module_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    if hasattr(module, "choose_minimal_hybrid"):
        return module.choose_minimal_hybrid
    if hasattr(module, "make_minimal_hybrid_policy"):
        return module.make_minimal_hybrid_policy()
    raise AttributeError(f"{module_path} does not expose a supported policy callable")


def benchmark_symmetric_winrate(
    policy_v1: Policy,
    policy_v2: Policy,
    num_games: int = 100,
    seed_base: int = 20260500,
) -> dict[str, float | int]:
    """Benchmark paired games with swapped sides for two policies."""
    v1_points = 0.0
    v2_points = 0.0
    draws = 0

    for game_idx in range(num_games):
        seed = seed_base + game_idx
        for ussr_policy, us_policy, v1_is_ussr in (
            (policy_v1, policy_v2, True),
            (policy_v2, policy_v1, False),
        ):
            result = play_game(ussr_policy, us_policy, seed=seed)
            if result.winner is None:
                draws += 1
                v1_points += 0.5
                v2_points += 0.5
                continue
            if (result.winner == Side.USSR) == v1_is_ussr:
                v1_points += 1.0
            else:
                v2_points += 1.0

    total_games = num_games * 2
    return {
        "num_games": num_games,
        "total_games": total_games,
        "draws": draws,
        "v1_points": v1_points,
        "v2_points": v2_points,
        "v1_win_rate": (100.0 * v1_points / total_games) if total_games else 0.0,
        "v2_win_rate": (100.0 * v2_points / total_games) if total_games else 0.0,
    }


def build_arg_parser() -> argparse.ArgumentParser:
    """Return the CLI parser for the symmetric win-rate benchmark."""
    parser = argparse.ArgumentParser(
        description="Benchmark paired Twilight Struggle games for two policies.",
    )
    parser.add_argument(
        "--num-games",
        type=int,
        default=100,
        help="Number of paired seeds to evaluate before swapping sides.",
    )
    parser.add_argument(
        "--seed-base",
        type=int,
        default=20260500,
        help="Base seed used to derive deterministic paired game seeds.",
    )
    parser.add_argument("--old-policy", required=True, help="Path to the baseline policy module.")
    parser.add_argument("--new-policy", required=True, help="Path to the candidate policy module.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Parse CLI arguments and run the symmetric win-rate benchmark."""
    args = build_arg_parser().parse_args(argv)
    result = benchmark_symmetric_winrate(
        _load_policy(args.old_policy),
        _load_policy(args.new_policy),
        num_games=args.num_games,
        seed_base=args.seed_base,
    )
    print(
        "oldWR={old:.1f}% newWR={new:.1f}% delta={delta:+.1f}% draws={draws}/{total}".format(
            old=result["v1_win_rate"],
            new=result["v2_win_rate"],
            delta=result["v2_win_rate"] - result["v1_win_rate"],
            draws=result["draws"],
            total=result["total_games"],
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
