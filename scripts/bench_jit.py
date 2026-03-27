from __future__ import annotations

import argparse
import gc
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve()
PYTHON_DIR = SCRIPT_PATH.parents[1] / "python"

UV_INSTALL_MESSAGE = (
    "uv is required to run this benchmark.\n"
    "Install uv and rerun. See: https://docs.astral.sh/uv/getting-started/installation/"
)

JIT_SETUP_MESSAGE = (
    "Python 3.14 with JIT is not available through uv.\n"
    "Ensure `uv run --python 3.14 python` resolves to a build where "
    "`sys._jit.is_available()` is true.\n"
    "Example:\n"
    "  uv python install 3.14\n"
    "  uv run --python 3.14 python -c \"from sys import _jit; print(_jit.is_available())\""
)


def _jit_status() -> tuple[bool, bool]:
    try:
        from sys import _jit
    except ImportError:
        return False, False
    return _jit.is_available(), _jit.is_enabled()


def _safe_rate(count: int, seconds: float) -> float:
    if seconds <= 0.0:
        return 0.0
    return count / seconds


def _speedup(baseline: float, candidate: float) -> float:
    if baseline <= 0.0:
        return 0.0
    return candidate / baseline


def _setup_check() -> int:
    jit_available, jit_enabled = _jit_status()

    print(f"Python      : {sys.version}")
    print(f"JIT available: {jit_available}")
    print(f"JIT enabled : {jit_enabled}")
    if jit_available:
        return 0

    print(JIT_SETUP_MESSAGE)
    return 1


def _load_worker_functions():
    sys.path.insert(0, str(PYTHON_DIR))
    from tsrl.engine.game_loop import make_random_policy, play_random_game
    from tsrl.engine.mcts import collect_self_play_game

    make_random_policy()
    return play_random_game, collect_self_play_game


def _benchmark_rollouts(
    play_random_game,
    *,
    n_warmup: int,
    n_bench: int,
    seed: int,
) -> dict[str, object]:
    for i in range(n_warmup):
        play_random_game(seed=seed - i - 1)

    gc.disable()
    try:
        t0 = time.perf_counter_ns()
        n_completed = 0
        for i in range(n_bench):
            play_random_game(seed=seed + i)
            n_completed += 1
        elapsed = (time.perf_counter_ns() - t0) / 1_000_000_000
    finally:
        gc.enable()

    return {
        "n_completed": n_completed,
        "rollout_seconds": elapsed,
        "rollouts_per_second": _safe_rate(n_completed, elapsed),
    }


def _benchmark_mcts(
    collect_self_play_game,
    *,
    n_warmup: int,
    n_bench: int,
    n_sim: int,
    seed: int,
) -> dict[str, object]:
    for i in range(n_warmup):
        collect_self_play_game(n_sim=n_sim, use_uct=True, seed=seed - i - 1)

    gc.disable()
    try:
        t0 = time.perf_counter_ns()
        n_completed = 0
        total_steps = 0
        for i in range(n_bench):
            steps, _ = collect_self_play_game(n_sim=n_sim, use_uct=True, seed=seed + i)
            total_steps += len(steps)
            n_completed += 1
        elapsed = (time.perf_counter_ns() - t0) / 1_000_000_000
    finally:
        gc.enable()

    return {
        "n_sim": n_sim,
        "n_completed": n_completed,
        "total_steps": total_steps,
        "mcts_seconds": elapsed,
        "games_per_second": _safe_rate(n_completed, elapsed),
        "steps_per_second": _safe_rate(total_steps, elapsed),
    }


def _run_worker(args: argparse.Namespace) -> int:
    play_random_game, collect_self_play_game = _load_worker_functions()
    jit_available, jit_enabled = _jit_status()

    result = {
        "mode": args.worker,
        "python_version": sys.version.splitlines()[0],
        "jit_available": jit_available,
        "jit_enabled": jit_enabled,
        "n_warmup": args.n_warmup,
        "n_bench": args.n_bench,
        "mcts": None,
    }
    result.update(
        _benchmark_rollouts(
            play_random_game,
            n_warmup=args.n_warmup,
            n_bench=args.n_bench,
            seed=args.seed,
        )
    )
    if args.with_mcts:
        result["mcts"] = _benchmark_mcts(
            collect_self_play_game,
            n_warmup=args.n_warmup,
            n_bench=args.n_bench,
            n_sim=args.n_sim,
            seed=args.seed,
        )

    print(json.dumps(result, sort_keys=True))
    return 0


def _run_worker_subprocess(mode: str, args: argparse.Namespace) -> dict[str, object]:
    jit_value = "0" if mode == "jit_disabled" else "1"
    cmd = [
        "uv",
        "run",
        "--python",
        "3.14",
        "python",
        str(SCRIPT_PATH),
        "--worker",
        mode,
        "--n-warmup",
        str(args.n_warmup),
        "--n-bench",
        str(args.n_bench),
        "--seed",
        str(args.seed),
    ]
    if args.with_mcts:
        cmd.extend(["--with-mcts", "--n-sim", str(args.n_sim)])

    completed = subprocess.run(
        cmd,
        env={**os.environ, "PYTHON_JIT": jit_value},
        capture_output=True,
        text=True,
        check=True,
    )
    return json.loads(completed.stdout)


def _format_speedup(speedup: float) -> str:
    return f"{speedup:.2f}x"


def _format_rollout_table(jit_disabled: dict[str, object], jit_enabled: dict[str, object]) -> str:
    disabled_rate = float(jit_disabled["rollouts_per_second"])
    enabled_rate = float(jit_enabled["rollouts_per_second"])
    enabled_speedup = _speedup(disabled_rate, enabled_rate)

    lines = [
        f"{'mode':<12}  {'rollouts/s':>11}  {'speedup':>8}",
        f"{'-' * 12}  {'-' * 11}  {'-' * 8}",
        f"{'JIT disabled':<12}  {disabled_rate:>11.2f}  {_format_speedup(1.0):>8}",
        f"{'JIT enabled':<12}  {enabled_rate:>11.2f}  {_format_speedup(enabled_speedup):>8}",
    ]
    return "\n".join(lines)


def _format_mcts_table(jit_disabled: dict[str, object], jit_enabled: dict[str, object]) -> str:
    disabled_mcts = jit_disabled["mcts"]
    enabled_mcts = jit_enabled["mcts"]
    if not isinstance(disabled_mcts, dict) or not isinstance(enabled_mcts, dict):
        return ""

    disabled_rate = float(disabled_mcts["games_per_second"])
    enabled_rate = float(enabled_mcts["games_per_second"])
    enabled_speedup = _speedup(disabled_rate, enabled_rate)

    lines = [
        "",
        "MCTS workload : collect_self_play_game() - UCT",
        f"MCTS sims     : {disabled_mcts['n_sim']}",
        "",
        f"{'mode':<12}  {'games/s':>9}  {'steps/s':>9}  {'speedup':>8}",
        f"{'-' * 12}  {'-' * 9}  {'-' * 9}  {'-' * 8}",
        (
            f"{'JIT disabled':<12}  "
            f"{float(disabled_mcts['games_per_second']):>9.2f}  "
            f"{float(disabled_mcts['steps_per_second']):>9.2f}  "
            f"{_format_speedup(1.0):>8}"
        ),
        (
            f"{'JIT enabled':<12}  "
            f"{float(enabled_mcts['games_per_second']):>9.2f}  "
            f"{float(enabled_mcts['steps_per_second']):>9.2f}  "
            f"{_format_speedup(enabled_speedup):>8}"
        ),
    ]
    return "\n".join(lines)


def _run_coordinator(args: argparse.Namespace) -> int:
    if shutil.which("uv") is None:
        print(UV_INSTALL_MESSAGE, file=sys.stderr)
        return 1

    preflight = subprocess.run(
        [
            "uv",
            "run",
            "--python",
            "3.14",
            "python",
            "-c",
            "from sys import _jit; exit(0 if _jit.is_available() else 1)",
        ],
        capture_output=True,
    )
    if preflight.returncode != 0:
        print(JIT_SETUP_MESSAGE, file=sys.stderr)
        return 1

    try:
        jit_disabled = _run_worker_subprocess("jit_disabled", args)
        jit_enabled = _run_worker_subprocess("jit_enabled", args)
    except subprocess.CalledProcessError as exc:
        print(f"Worker benchmark failed: {exc}", file=sys.stderr)
        if exc.stderr:
            print(exc.stderr, file=sys.stderr)
        return 1
    except json.JSONDecodeError as exc:
        print(f"Worker returned invalid JSON: {exc}", file=sys.stderr)
        return 1

    speedup_rollouts = _speedup(
        float(jit_disabled["rollouts_per_second"]),
        float(jit_enabled["rollouts_per_second"]),
    )
    if args.json:
        print(
            json.dumps(
                {
                    "python_version": jit_disabled["python_version"],
                    "jit_disabled": jit_disabled,
                    "jit_enabled": jit_enabled,
                    "speedup_rollouts": speedup_rollouts,
                },
                sort_keys=True,
            )
        )
        return 0

    lines = [
        "Twilight Struggle self-play rollout JIT benchmark",
        f"Python       : {jit_disabled['python_version']}",
        "Workload     : play_random_game() - random policy, both sides",
        "Note         : C++ engine bindings are a stub; all timing is pure Python.",
        f"Warmup games : {args.n_warmup}",
        f"Timed games  : {args.n_bench}",
        "",
        _format_rollout_table(jit_disabled, jit_enabled),
    ]
    mcts_table = _format_mcts_table(jit_disabled, jit_enabled)
    if mcts_table:
        lines.append(mcts_table)
    print("\n".join(lines))
    return 0


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n-warmup", type=int, default=5, help="Warmup games per worker")
    parser.add_argument("--n-bench", type=int, default=20, help="Timed games per worker")
    parser.add_argument("--with-mcts", action="store_true", help="Also benchmark UCT self-play")
    parser.add_argument("--n-sim", type=int, default=10, help="MCTS simulations per move")
    parser.add_argument("--seed", type=int, default=42, help="Base RNG seed")
    parser.add_argument("--json", action="store_true", help="Emit JSON from the coordinator")
    parser.add_argument("--setup-check", action="store_true", help="Verify Python 3.14 JIT setup")
    parser.add_argument(
        "--worker",
        choices=("jit_disabled", "jit_enabled"),
        help=argparse.SUPPRESS,
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    if args.setup_check:
        return _setup_check()
    if args.worker is not None:
        return _run_worker(args)
    return _run_coordinator(args)


if __name__ == "__main__":
    sys.exit(main())
