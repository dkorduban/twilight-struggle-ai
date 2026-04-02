"""Run native MCTS teacher search over mined JSONL positions and cache targets.

The input JSONL is expected to contain mined decision points with full
``state_dict`` payloads that can be passed directly to
``tscore.mcts_search_from_state``. The output is a Parquet cache keyed by
``(game_id, step_index)`` with soft teacher targets for the card and mode heads.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
from pathlib import Path
from typing import Any

import polars as pl

CARD_TARGET_SIZE = 111
MODE_TARGET_SIZE = 5
DEFAULT_PROGRESS_INTERVAL = 50

_tscore = None


def _lower_priority() -> None:
    try:
        os.nice(10)
    except OSError:
        pass


def _get_tscore():
    global _tscore
    if _tscore is not None:
        return _tscore

    build_bindings = Path(__file__).resolve().parents[1] / "build-ninja" / "bindings"
    if str(build_bindings) not in sys.path:
        sys.path.insert(0, str(build_bindings))

    import tscore as module

    _tscore = module
    return _tscore


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--positions",
        type=Path,
        required=True,
        help="Mined JSONL file or directory of JSONL files containing full state_dict payloads.",
    )
    parser.add_argument(
        "--model",
        required=True,
        help="TorchScript model path passed through to tscore.mcts_search_from_state.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        required=True,
        help="Output Parquet cache path.",
    )
    parser.add_argument("--n-sim", type=int, default=400, help="MCTS simulations per position.")
    parser.add_argument("--c-puct", type=float, default=1.5, help="PUCT exploration constant.")
    parser.add_argument(
        "--calibration",
        type=Path,
        default=None,
        help="Optional JSON file containing fitted Platt scaling params {a, b}.",
    )
    parser.add_argument("--seed", type=int, default=None, help="Optional base RNG seed.")
    parser.add_argument(
        "--max-positions",
        type=int,
        default=None,
        help="Optional cap after resume filtering.",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help=(
            "Skip keys already present in --out and merge new rows into the existing parquet cache."
        ),
    )
    parser.add_argument(
        "--progress-interval",
        type=int,
        default=DEFAULT_PROGRESS_INTERVAL,
        help="Print a progress line every N processed positions. Use 0 to disable.",
    )
    args = parser.parse_args()
    if args.n_sim <= 0:
        parser.error("--n-sim must be positive")
    if args.c_puct <= 0:
        parser.error("--c-puct must be positive")
    if args.max_positions is not None and args.max_positions < 0:
        parser.error("--max-positions must be non-negative")
    if args.progress_interval < 0:
        parser.error("--progress-interval must be non-negative")
    return args


def _load_calibration(path: Path | None) -> tuple[float, float]:
    if path is None:
        return 1.0, 0.0
    with path.open(encoding="utf-8") as handle:
        payload = json.load(handle)
    return float(payload["a"]), float(payload["b"])


def _jsonl_paths(positions_path: Path) -> list[Path]:
    if positions_path.is_file():
        return [positions_path]
    if positions_path.is_dir():
        paths = sorted(positions_path.glob("*.jsonl"))
        if paths:
            return paths
        raise FileNotFoundError(f"No *.jsonl files found in {positions_path}")
    raise FileNotFoundError(positions_path)


def _position_key(position: dict[str, Any]) -> tuple[str, int]:
    try:
        game_id = str(position["game_id"])
        step_index = int(position["step_index"])
    except KeyError as exc:
        raise KeyError(f"Position is missing required key {exc.args[0]!r}") from exc
    return game_id, step_index


def _validate_position(position: dict[str, Any]) -> None:
    game_id, step_index = _position_key(position)
    state_dict = position.get("state_dict")
    if not isinstance(state_dict, dict):
        raise TypeError(f"{game_id}:{step_index} is missing a dict state_dict payload")
    if position.get("state_dict_complete") is False or state_dict.get("_partial") is True:
        raise ValueError(
            f"{game_id}:{step_index} has a partial state_dict; teacher search "
            "requires full hands, deck, and flags"
        )


def _load_positions(
    positions_path: Path,
    done_keys: set[tuple[str, int]] | None = None,
) -> list[dict[str, Any]]:
    done_keys = done_keys or set()
    positions: list[dict[str, Any]] = []
    seen_keys: set[tuple[str, int]] = set()

    for path in _jsonl_paths(positions_path):
        with path.open(encoding="utf-8") as handle:
            for lineno, line in enumerate(handle, 1):
                text = line.strip()
                if not text:
                    continue
                try:
                    position = json.loads(text)
                except json.JSONDecodeError as exc:
                    raise ValueError(f"Malformed JSON in {path}:{lineno}: {exc}") from exc
                key = _position_key(position)
                if key in seen_keys:
                    raise ValueError(f"Duplicate mined position key {key} encountered in {path}")
                seen_keys.add(key)
                if key in done_keys:
                    continue
                positions.append(position)
    return positions


def build_teacher_targets(edges: list[dict[str, Any]]) -> tuple[list[float], list[float]]:
    total_visits = sum(int(edge["visits"]) for edge in edges)
    if total_visits <= 0:
        raise ValueError("Teacher search result had no root visits")

    teacher_card = [0.0] * CARD_TARGET_SIZE
    teacher_mode = [0.0] * MODE_TARGET_SIZE
    inv_total = 1.0 / float(total_visits)

    for edge in edges:
        card_id = int(edge["card_id"])
        mode = int(edge["mode"])
        if not 1 <= card_id <= CARD_TARGET_SIZE:
            raise ValueError(f"Unexpected card_id {card_id}; expected 1..{CARD_TARGET_SIZE}")
        if not 0 <= mode < MODE_TARGET_SIZE:
            raise ValueError(f"Unexpected mode {mode}; expected 0..{MODE_TARGET_SIZE - 1}")
        prob = int(edge["visits"]) * inv_total
        teacher_card[card_id - 1] += prob
        teacher_mode[mode] += prob

    if not math.isclose(sum(teacher_card), 1.0, rel_tol=1e-6, abs_tol=1e-6):
        raise ValueError("teacher_card_target does not sum to 1.0")
    if not math.isclose(sum(teacher_mode), 1.0, rel_tol=1e-6, abs_tol=1e-6):
        raise ValueError("teacher_mode_target does not sum to 1.0")
    return teacher_card, teacher_mode


def _build_row(
    position: dict[str, Any],
    result: dict[str, Any],
    *,
    n_sim: int,
    c_puct: float,
    elapsed_s: float,
) -> dict[str, Any]:
    teacher_card, teacher_mode = build_teacher_targets(list(result["edges"]))
    game_id, step_index = _position_key(position)
    state_dict = position["state_dict"]
    return {
        "game_id": game_id,
        "step_index": step_index,
        "turn": int(position.get("turn", state_dict["turn"])),
        "ar": int(position.get("ar", state_dict["ar"])),
        "side": int(position.get("side", state_dict.get("phasing", 0))),
        "teacher_n_sim": int(n_sim),
        "teacher_c_puct": float(c_puct),
        "teacher_root_value": float(result["root_value"]),
        "teacher_value_target": float(result["root_value"]),
        "teacher_card_target": [float(x) for x in teacher_card],
        "teacher_mode_target": [float(x) for x in teacher_mode],
        "search_elapsed_s": float(elapsed_s),
    }


def _empty_frame() -> pl.DataFrame:
    return pl.DataFrame(
        schema={
            "game_id": pl.String,
            "step_index": pl.Int64,
            "turn": pl.Int32,
            "ar": pl.Int32,
            "side": pl.Int32,
            "teacher_n_sim": pl.Int32,
            "teacher_c_puct": pl.Float32,
            "teacher_root_value": pl.Float32,
            "teacher_value_target": pl.Float32,
            "teacher_card_target": pl.List(pl.Float32),
            "teacher_mode_target": pl.List(pl.Float32),
            "search_elapsed_s": pl.Float32,
        }
    )


def _rows_to_frame(rows: list[dict[str, Any]]) -> pl.DataFrame:
    if not rows:
        return _empty_frame()

    df = pl.DataFrame(rows)
    return df.with_columns(
        pl.col("step_index").cast(pl.Int64),
        pl.col("turn").cast(pl.Int32),
        pl.col("ar").cast(pl.Int32),
        pl.col("side").cast(pl.Int32),
        pl.col("teacher_n_sim").cast(pl.Int32),
        pl.col("teacher_c_puct").cast(pl.Float32),
        pl.col("teacher_root_value").cast(pl.Float32),
        pl.col("teacher_value_target").cast(pl.Float32),
        pl.col("teacher_card_target").cast(pl.List(pl.Float32)),
        pl.col("teacher_mode_target").cast(pl.List(pl.Float32)),
        pl.col("search_elapsed_s").cast(pl.Float32),
    )


def _done_keys_from_frame(df: pl.DataFrame) -> set[tuple[str, int]]:
    if len(df) == 0:
        return set()
    return {
        (str(row["game_id"]), int(row["step_index"]))
        for row in df.select("game_id", "step_index").iter_rows(named=True)
    }


def _load_existing_cache(out_path: Path) -> pl.DataFrame:
    if not out_path.exists():
        return _empty_frame()
    return pl.read_parquet(str(out_path))


def _write_cache(df: pl.DataFrame, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.sort(["game_id", "step_index"]).write_parquet(str(out_path))


def run_teacher_search(
    positions_path: Path,
    model_path: str,
    out_path: Path,
    *,
    n_sim: int,
    c_puct: float,
    calib_a: float = 1.0,
    calib_b: float = 0.0,
    seed: int | None = None,
    max_positions: int | None = None,
    resume: bool = False,
    progress_interval: int = DEFAULT_PROGRESS_INTERVAL,
) -> int:
    existing_df = _load_existing_cache(out_path) if resume else _empty_frame()
    done_keys = _done_keys_from_frame(existing_df)
    positions = _load_positions(positions_path, done_keys=done_keys)
    if max_positions is not None:
        positions = positions[:max_positions]

    print(
        f"Loaded {len(positions):,} pending positions from {positions_path}"
        + (f" after skipping {len(done_keys):,} cached keys" if resume else "")
    )

    if not positions:
        if resume and len(existing_df) > 0:
            print(f"No new positions to process; cache remains {out_path}")
            return 0
        raise RuntimeError("No positions to process")

    tscore = None
    new_rows: list[dict[str, Any]] = []
    total = len(positions)
    t_start = time.time()

    skipped_partial = 0
    for idx, position in enumerate(positions):
        try:
            _validate_position(position)
        except (TypeError, ValueError) as exc:
            skipped_partial += 1
            if skipped_partial <= 5:
                print(f"[teacher_search] skipping position {idx}: {exc}", flush=True)
            elif skipped_partial == 6:
                print("[teacher_search] (further partial-state skip messages suppressed)", flush=True)
            continue
        if tscore is None:
            tscore = _get_tscore()

        search_seed = None if seed is None else seed + idx
        started = time.time()
        result = tscore.mcts_search_from_state(
            state_dict=position["state_dict"],
            model_path=model_path,
            n_sim=n_sim,
            c_puct=c_puct,
            calib_a=calib_a,
            calib_b=calib_b,
            seed=search_seed,
        )
        elapsed_s = time.time() - started
        new_rows.append(
            _build_row(
                position,
                result,
                n_sim=n_sim,
                c_puct=c_puct,
                elapsed_s=elapsed_s,
            )
        )

        should_log = progress_interval > 0 and (
            (idx + 1) % progress_interval == 0 or (idx + 1) == total
        )
        if should_log:
            total_elapsed = max(time.time() - t_start, 1e-9)
            rate = (idx + 1) / total_elapsed
            remaining = total - (idx + 1)
            eta_s = remaining / rate if rate > 0 else float("inf")
            game_id, step_index = _position_key(position)
            print(
                f"[{idx + 1}/{total}] {game_id}:{step_index} "
                f"root={float(result['root_value']):+.3f} "
                f"elapsed={elapsed_s:.2f}s eta={eta_s:.1f}s"
            )

    if skipped_partial > 0:
        print(f"[teacher_search] skipped {skipped_partial}/{total} positions (partial state_dict)")

    new_df = _rows_to_frame(new_rows)
    merged_df = (
        pl.concat([existing_df, new_df], how="vertical_relaxed")
        if resume and len(existing_df)
        else new_df
    )
    _write_cache(merged_df, out_path)
    print(f"Wrote {len(new_df):,} new rows ({len(merged_df):,} total) to {out_path}")
    return len(new_df)


def main() -> None:
    _lower_priority()
    args = _parse_args()
    calib_a, calib_b = _load_calibration(args.calibration)
    run_teacher_search(
        args.positions,
        args.model,
        args.out,
        n_sim=args.n_sim,
        c_puct=args.c_puct,
        calib_a=calib_a,
        calib_b=calib_b,
        seed=args.seed,
        max_positions=args.max_positions,
        resume=args.resume,
        progress_interval=args.progress_interval,
    )


if __name__ == "__main__":
    main()
