"""Mine hard positions from self-play Parquet rows.

Scores positions by value-head surprise (|pred - actual|) and uncertainty
(1 - |pred|), then writes the top-K positions as JSONL.

For Parquet inputs, the emitted state payload is partial: it contains the
available public state plus observer card-knowledge fields, but not exact
hands, deck order, or persistent effect flags.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

import numpy as np
import polars as pl
import torch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "python"))

from tsrl.policies.model import TSBaselineModel  # noqa: E402,I001


LIST_COLUMNS = (
    "ussr_influence",
    "us_influence",
    "discard_mask",
    "removed_mask",
    "actor_known_in",
    "actor_known_not_in",
    "actor_possible",
    "opp_known_in",
    "opp_known_not_in",
    "opp_possible",
)

REQUIRED_COLUMNS = (
    "game_id",
    "step_idx",
    "turn",
    "ar",
    "phasing",
    "vp",
    "defcon",
    "milops_ussr",
    "milops_us",
    "space_ussr",
    "space_us",
    "china_held_by",
    "china_playable",
    "actor_hand_size",
    "actor_holds_china",
    "opp_hand_size",
    "opp_holds_china",
    "winner_side",
    "final_vp",
    "end_reason",
    "ussr_influence",
    "us_influence",
    "discard_mask",
    "removed_mask",
    "actor_known_in",
    "actor_known_not_in",
    "actor_possible",
    "opp_known_in",
    "opp_known_not_in",
    "opp_possible",
)

# Columns emitted by the updated C++ collector for full game state.
# When present, mine_hard_positions can emit state_dict_complete=True.
FULL_STATE_COLUMNS = (
    "ussr_hand",
    "us_hand",
    "deck",
    "ussr_holds_china",
    "us_holds_china",
    "warsaw_pact_played",
    "marshall_plan_played",
    "truman_doctrine_played",
    "john_paul_ii_played",
    "nato_active",
    "de_gaulle_active",
    "willy_brandt_active",
    "us_japan_pact_active",
    "nuclear_subs_active",
    "norad_active",
    "shuttle_diplomacy_active",
    "flower_power_active",
    "flower_power_cancelled",
    "salt_active",
    "opec_cancelled",
    "awacs_active",
    "north_sea_oil_extra_ar",
    "glasnost_extra_ar",
    "formosan_active",
    "cuban_missile_crisis_active",
    "vietnam_revolts_active",
    "bear_trap_active",
    "quagmire_active",
    "iran_hostage_crisis_active",
    "handicap_ussr",
    "handicap_us",
    "ops_modifier",
)

MISSING_STATE_KEYS = [
    "warsaw_pact_played",
    "marshall_plan_played",
    "truman_doctrine_played",
    "john_paul_ii_played",
    "nato_active",
    "de_gaulle_active",
    "willy_brandt_active",
    "us_japan_pact_active",
    "nuclear_subs_active",
    "norad_active",
    "shuttle_diplomacy_active",
    "flower_power_active",
    "flower_power_cancelled",
    "salt_active",
    "opec_cancelled",
    "awacs_active",
    "north_sea_oil_extra_ar",
    "glasnost_extra_ar",
    "formosan_active",
    "cuban_missile_crisis_active",
    "vietnam_revolts_active",
    "bear_trap_active",
    "quagmire_active",
    "iran_hostage_crisis_active",
    "handicap_ussr",
    "handicap_us",
    "ops_modifier",
    "ussr_hand",
    "us_hand",
    "deck",
    "ussr_holds_china",
    "us_holds_china",
]


def _lower_priority() -> None:
    try:
        os.nice(10)
    except OSError:
        pass


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--data",
        "--data-dir",
        dest="data",
        required=True,
        help="Parquet file or directory containing Parquet files.",
    )
    parser.add_argument(
        "--checkpoint",
        default=None,
        help="Model checkpoint path. If omitted, inferred from the data path when possible.",
    )
    parser.add_argument("--out", required=True, help="Output JSONL path.")
    parser.add_argument("--top-k", type=int, default=5000, help="Number of rows to write.")
    parser.add_argument("--min-turn", type=int, default=2, help="Inclusive minimum turn filter.")
    parser.add_argument("--max-turn", type=int, default=9, help="Inclusive maximum turn filter.")
    parser.add_argument("--batch-size", type=int, default=512, help="Inference batch size.")
    parser.add_argument(
        "--difficulty-metric",
        choices=("surprise", "uncertainty", "both"),
        default="both",
        help="Ranking metric.",
    )
    parser.add_argument(
        "--device",
        default="auto",
        choices=("auto", "cpu", "cuda"),
        help="Inference device. 'auto' prefers CUDA when available.",
    )
    return parser.parse_args()


def _resolve_device(name: str) -> torch.device:
    if name == "cuda":
        if not torch.cuda.is_available():
            raise RuntimeError("CUDA requested but not available")
        return torch.device("cuda")
    if name == "auto" and torch.cuda.is_available():
        return torch.device("cuda")
    return torch.device("cpu")


def _infer_checkpoint(data_path: Path, checkpoint: str | None) -> Path:
    if checkpoint is not None:
        path = Path(checkpoint)
        if not path.is_file():
            raise FileNotFoundError(path)
        return path

    match = re.search(r"(?:^|[_/])v(\d+)(?:[_./]|$)", str(data_path))
    if match:
        candidate = Path(f"data/checkpoints/retrain_v{match.group(1)}/baseline_best.pt")
        if candidate.is_file():
            return candidate

    raise FileNotFoundError(
        "Could not infer a checkpoint from the data path. Pass --checkpoint explicitly."
    )


def _parquet_paths(data_path: Path) -> list[Path]:
    if data_path.is_file():
        if data_path.suffix != ".parquet":
            raise ValueError(f"Expected a parquet file, got {data_path}")
        return [data_path]
    if data_path.is_dir():
        paths = sorted(data_path.glob("*.parquet"))
        if not paths:
            raise FileNotFoundError(f"No *.parquet files found in {data_path}")
        return paths
    raise FileNotFoundError(data_path)


def _normalize_frame(df: pl.DataFrame) -> pl.DataFrame:
    casts = [
        pl.col(col).cast(pl.List(pl.Int32)).alias(col)
        for col in LIST_COLUMNS
        if col in df.columns
    ]
    return df.with_columns(casts) if casts else df


def load_rows(data_path: Path, min_turn: int | None, max_turn: int | None) -> pl.DataFrame:
    paths = _parquet_paths(data_path)
    # Probe first file for full-state columns; select them if available
    probe_schema = pl.read_parquet_schema(str(paths[0]))
    available_full_state = [c for c in FULL_STATE_COLUMNS if c in probe_schema]
    select_cols = list(REQUIRED_COLUMNS) + available_full_state
    if available_full_state:
        print(f"Full-state columns detected ({len(available_full_state)} fields)")

    scans = []
    for path in paths:
        schema = pl.read_parquet_schema(str(path))
        cols = [c for c in select_cols if c in schema]
        scans.append(pl.scan_parquet(str(path)).select(cols))
    lf = pl.concat(scans, how="vertical_relaxed")
    if min_turn is not None:
        lf = lf.filter(pl.col("turn") >= min_turn)
    if max_turn is not None:
        lf = lf.filter(pl.col("turn") <= max_turn)
    df = lf.collect()
    return _normalize_frame(df)


def load_model(checkpoint_path: Path, device: torch.device) -> TSBaselineModel:
    ckpt = torch.load(checkpoint_path, map_location=device, weights_only=False)
    cfg = ckpt.get("config", {})
    ckpt_args = ckpt.get("args", {})
    hidden_dim = cfg.get("hidden_dim", ckpt_args.get("hidden_dim", 256))
    dropout = cfg.get("dropout", ckpt_args.get("dropout", 0.1))

    model = TSBaselineModel(hidden_dim=hidden_dim, dropout=dropout).to(device)
    state_dict = ckpt.get("model_state_dict", ckpt)
    model.load_state_dict(state_dict, strict=False)
    model.eval()
    return model


def _normalize_influence_features(influence: torch.Tensor, expected_dim: int) -> torch.Tensor:
    actual_dim = int(influence.shape[1])
    if actual_dim == expected_dim:
        return influence
    if actual_dim == expected_dim + 2 and expected_dim % 2 == 0:
        half = actual_dim // 2
        return torch.cat([influence[:, 1:half], influence[:, half + 1 :]], dim=1)
    if actual_dim > expected_dim:
        return influence[:, :expected_dim]
    pad = torch.zeros(
        (influence.shape[0], expected_dim - actual_dim),
        dtype=influence.dtype,
    )
    return torch.cat([influence, pad], dim=1)


def run_inference(
    model: TSBaselineModel,
    df: pl.DataFrame,
    batch_size: int,
    device: torch.device,
) -> np.ndarray:
    n_rows = len(df)
    preds = np.zeros(n_rows, dtype=np.float32)

    ussr = np.array(df["ussr_influence"].to_list(), dtype=np.float32)
    us = np.array(df["us_influence"].to_list(), dtype=np.float32)
    influence = torch.from_numpy(np.concatenate([ussr, us], axis=1))
    influence = _normalize_influence_features(influence, model.influence_encoder.in_features)

    known_in = np.array(df["actor_known_in"].to_list(), dtype=np.uint8)
    possible = np.array(df["actor_possible"].to_list(), dtype=np.uint8)
    discard = np.array(df["discard_mask"].to_list(), dtype=np.uint8)
    removed = np.array(df["removed_mask"].to_list(), dtype=np.uint8)
    cards = torch.from_numpy(np.concatenate([known_in, possible, discard, removed], axis=1))

    scalars = np.stack(
        [
            df["vp"].cast(pl.Float32).to_numpy() / 20.0,
            (df["defcon"].cast(pl.Float32).to_numpy() - 1.0) / 4.0,
            df["milops_ussr"].cast(pl.Float32).to_numpy() / 6.0,
            df["milops_us"].cast(pl.Float32).to_numpy() / 6.0,
            df["space_ussr"].cast(pl.Float32).to_numpy() / 9.0,
            df["space_us"].cast(pl.Float32).to_numpy() / 9.0,
            df["china_held_by"].cast(pl.Float32).to_numpy(),
            df["actor_holds_china"].cast(pl.Float32).to_numpy(),
            df["turn"].cast(pl.Float32).to_numpy() / 10.0,
            df["ar"].cast(pl.Float32).to_numpy() / 8.0,
            df["phasing"].cast(pl.Float32).to_numpy(),
        ],
        axis=1,
    ).astype(np.float32)
    scalars_t = torch.from_numpy(scalars)

    with torch.inference_mode():
        for start in range(0, n_rows, batch_size):
            end = min(start + batch_size, n_rows)
            out = model(
                influence[start:end].to(device),
                cards[start:end].to(device).float(),
                scalars_t[start:end].to(device),
            )
            preds[start:end] = out["value"].squeeze(-1).detach().cpu().numpy()

    return preds


def add_scores(df: pl.DataFrame, preds: np.ndarray, metric: str) -> pl.DataFrame:
    actuals = np.clip(df["final_vp"].cast(pl.Float32).to_numpy() / 20.0, -1.0, 1.0)
    surprise = np.abs(preds - actuals)
    uncertainty = np.clip(1.0 - np.abs(preds), 0.0, 1.0)

    if metric == "surprise":
        difficulty = surprise
    elif metric == "uncertainty":
        difficulty = uncertainty
    else:
        difficulty = surprise + uncertainty

    return df.with_columns(
        pl.Series("value_pred", preds),
        pl.Series("value_target", actuals),
        pl.Series("surprise_score", surprise),
        pl.Series("uncertainty_score", uncertainty),
        pl.Series("difficulty_score", difficulty),
    )


def _ids_from_mask(mask: list[int]) -> list[int]:
    return [idx for idx, present in enumerate(mask) if idx > 0 and present]


def _has_full_state(row: dict[str, object]) -> bool:
    """Check if the row has all fields needed for a complete state_dict."""
    return "ussr_hand" in row and row["ussr_hand"] is not None


def _full_state_dict_from_row(row: dict[str, object]) -> dict[str, object]:
    """Build a complete state_dict from a row with full-state fields."""
    # Boolean flags with defaults (False) for backwards compatibility
    bool_flags = [
        "warsaw_pact_played", "marshall_plan_played", "truman_doctrine_played",
        "john_paul_ii_played", "nato_active", "de_gaulle_active",
        "willy_brandt_active", "us_japan_pact_active", "nuclear_subs_active",
        "norad_active", "shuttle_diplomacy_active", "flower_power_active",
        "flower_power_cancelled", "salt_active", "opec_cancelled",
        "awacs_active", "north_sea_oil_extra_ar", "glasnost_extra_ar",
        "formosan_active", "cuban_missile_crisis_active",
        "vietnam_revolts_active", "bear_trap_active", "quagmire_active",
        "iran_hostage_crisis_active",
    ]
    sd: dict[str, object] = {
        "turn": int(row["turn"]),
        "ar": int(row["ar"]),
        "phasing": int(row["phasing"]),
        "vp": int(row["vp"]),
        "defcon": int(row["defcon"]),
        "milops": [int(row["milops_ussr"]), int(row["milops_us"])],
        "space": [int(row["space_ussr"]), int(row["space_us"])],
        "china_held_by": int(row["china_held_by"]),
        "china_playable": bool(row["china_playable"]),
        "ussr_influence": [int(x) for x in row["ussr_influence"]],
        "us_influence": [int(x) for x in row["us_influence"]],
        "discard": _ids_from_mask(row["discard_mask"]),
        "removed": _ids_from_mask(row["removed_mask"]),
        # Full state fields
        "ussr_hand": [int(x) for x in row["ussr_hand"]],
        "us_hand": [int(x) for x in row["us_hand"]],
        "deck": [int(x) for x in row["deck"]],
        "ussr_holds_china": bool(row["ussr_holds_china"]),
        "us_holds_china": bool(row["us_holds_china"]),
        "handicap_ussr": int(row.get("handicap_ussr", 0)),
        "handicap_us": int(row.get("handicap_us", 0)),
        "ops_modifier": [int(x) for x in row.get("ops_modifier", [0, 0])],
    }
    for flag in bool_flags:
        sd[flag] = bool(row.get(flag, False))
    return sd


def _partial_state_dict_from_row(row: dict[str, object]) -> dict[str, object]:
    """Build a partial state_dict (legacy path for old collector output)."""
    return {
        "turn": int(row["turn"]),
        "ar": int(row["ar"]),
        "phasing": int(row["phasing"]),
        "vp": int(row["vp"]),
        "defcon": int(row["defcon"]),
        "milops": [int(row["milops_ussr"]), int(row["milops_us"])],
        "space": [int(row["space_ussr"]), int(row["space_us"])],
        "china_held_by": int(row["china_held_by"]),
        "china_playable": bool(row["china_playable"]),
        "ussr_influence": [int(x) for x in row["ussr_influence"]],
        "us_influence": [int(x) for x in row["us_influence"]],
        "discard": _ids_from_mask(row["discard_mask"]),
        "removed": _ids_from_mask(row["removed_mask"]),
        "actor_hand_size": int(row["actor_hand_size"]),
        "actor_holds_china": bool(row["actor_holds_china"]),
        "opp_hand_size": int(row["opp_hand_size"]),
        "opp_holds_china": bool(row["opp_holds_china"]),
        "actor_known_in": _ids_from_mask(row["actor_known_in"]),
        "actor_known_not_in": _ids_from_mask(row["actor_known_not_in"]),
        "actor_possible": _ids_from_mask(row["actor_possible"]),
        "opp_known_in": _ids_from_mask(row["opp_known_in"]),
        "opp_known_not_in": _ids_from_mask(row["opp_known_not_in"]),
        "opp_possible": _ids_from_mask(row["opp_possible"]),
        "_partial": True,
        "_missing_keys": MISSING_STATE_KEYS,
    }


def top_k_records(scored: pl.DataFrame, top_k: int) -> list[dict[str, object]]:
    ranked = scored.sort(
        by=["difficulty_score", "game_id", "step_idx"],
        descending=[True, False, False],
    ).head(top_k)

    records: list[dict[str, object]] = []
    n_full = 0
    for row in ranked.iter_rows(named=True):
        full = _has_full_state(row)
        if full:
            n_full += 1
        records.append(
            {
                "game_id": row["game_id"],
                "step_index": int(row["step_idx"]),
                "turn": int(row["turn"]),
                "ar": int(row["ar"]),
                "side": int(row["phasing"]),
                "value_pred": float(row["value_pred"]),
                "value_target": float(row["value_target"]),
                "surprise_score": float(row["surprise_score"]),
                "uncertainty_score": float(row["uncertainty_score"]),
                "difficulty_score": float(row["difficulty_score"]),
                "state_dict_complete": full,
                "state_dict": _full_state_dict_from_row(row) if full else _partial_state_dict_from_row(row),
            }
        )
    if n_full > 0:
        print(f"Full state available for {n_full}/{len(records)} positions (teacher search ready)")
    else:
        print("WARNING: No full-state positions found — teacher search will skip all positions")
    return records


def write_jsonl(records: list[dict[str, object]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, sort_keys=True))
            handle.write("\n")


def print_summary(scored: pl.DataFrame, records: list[dict[str, object]], metric: str) -> None:
    n_total = len(scored)
    print(f"Scanned positions: {n_total:,}")
    print(f"Difficulty metric: {metric}")

    if not records:
        print("No records selected.")
        return

    diffs = np.array([record["difficulty_score"] for record in records], dtype=np.float32)
    turns = Counter(int(record["turn"]) for record in records)
    turn_bits = ", ".join(f"T{turn}={count}" for turn, count in sorted(turns.items()))

    print(f"Selected positions: {len(records):,}")
    print(
        "Top-K difficulty stats: "
        f"mean={diffs.mean():.4f} median={np.median(diffs):.4f} max={diffs.max():.4f}"
    )
    print(f"Top-K turn distribution: {turn_bits}")


def main() -> None:
    _lower_priority()
    args = _parse_args()
    data_path = Path(args.data)
    checkpoint_path = _infer_checkpoint(data_path, args.checkpoint)
    out_path = Path(args.out)
    device = _resolve_device(args.device)

    print(f"Loading rows from {data_path}...")
    df = load_rows(data_path, args.min_turn, args.max_turn)
    if len(df) == 0:
        raise RuntimeError("No rows matched the requested turn filters")

    print(f"Loading checkpoint from {checkpoint_path} on {device}...")
    model = load_model(checkpoint_path, device)

    print(f"Running value inference over {len(df):,} rows...")
    preds = run_inference(model, df, batch_size=args.batch_size, device=device)

    print("Scoring positions...")
    scored = add_scores(df, preds, metric=args.difficulty_metric)
    records = top_k_records(scored, top_k=args.top_k)

    print(f"Writing {len(records):,} records to {out_path}...")
    write_jsonl(records, out_path)
    print_summary(scored, records, args.difficulty_metric)


if __name__ == "__main__":
    main()
