"""
check_value_calibration.py — Value head calibration analysis.

Loads a checkpoint and validation positions, runs inference, then reports:
  - Reliability diagram (ASCII)
  - ECE and Brier score
  - Stratified by data source (vs_heuristic vs selfplay) and game stage

Usage:
    uv run python scripts/check_value_calibration.py [--checkpoint PATH] [--data-dir DIR]
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

import numpy as np
import polars as pl
import torch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "python"))
from tsrl.policies.model import TSBaselineModel


def load_checkpoint(ckpt_path: str) -> TSBaselineModel:
    ckpt = torch.load(ckpt_path, map_location="cpu", weights_only=False)
    cfg = ckpt.get("config", {})
    model = TSBaselineModel(
        hidden_dim=cfg.get("hidden_dim", 256),
        dropout=cfg.get("dropout", 0.1),
    )
    sd = ckpt.get("model_state_dict", ckpt)
    model.load_state_dict(sd, strict=False)
    model.eval()
    return model


def run_inference(model: TSBaselineModel, df: pl.DataFrame, batch_size: int = 4096) -> np.ndarray:
    """Return value predictions (N,) for all rows in df."""
    N = len(df)
    preds = np.zeros(N, dtype=np.float32)

    # Build tensors
    ussr = np.array(df["ussr_influence"].to_list(), dtype=np.float32)
    us   = np.array(df["us_influence"].to_list(),   dtype=np.float32)
    influence = torch.from_numpy(np.concatenate([ussr, us], axis=1))  # (N,172)

    known_in = np.array(df["actor_known_in"].to_list(),  dtype=np.uint8)
    possible = np.array(df["actor_possible"].to_list(),  dtype=np.uint8)
    discard  = np.array(df["discard_mask"].to_list(),    dtype=np.uint8)
    removed  = np.array(df["removed_mask"].to_list(),    dtype=np.uint8)
    cards = torch.from_numpy(np.concatenate([known_in, possible, discard, removed], axis=1))

    scalars = np.stack([
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
    ], axis=1).astype(np.float32)
    scalars_t = torch.from_numpy(scalars)

    with torch.no_grad():
        for start in range(0, N, batch_size):
            end = min(start + batch_size, N)
            out = model(
                influence[start:end],
                cards[start:end].float(),
                scalars_t[start:end],
            )
            # model returns a dict; value is (B, 1) tanh output
            val = out["value"].squeeze(-1).numpy()
            preds[start:end] = val

    return preds


def calibration_report(preds: np.ndarray, actuals: np.ndarray, label: str, n_bins: int = 10) -> dict:
    bins = np.linspace(-1.0, 1.0, n_bins + 1)
    bin_indices = np.digitize(preds, bins) - 1
    bin_indices = np.clip(bin_indices, 0, n_bins - 1)

    results = []
    for i in range(n_bins):
        mask = bin_indices == i
        n = mask.sum()
        if n == 0:
            results.append({"bin": i, "n": 0, "pred_mean": None, "actual_mean": None})
            continue
        results.append({
            "bin": i,
            "n": int(n),
            "pred_mean": float(preds[mask].mean()),
            "actual_mean": float(actuals[mask].mean()),
        })

    total = len(preds)
    ece = sum(
        r["n"] / total * abs(r["pred_mean"] - r["actual_mean"])
        for r in results if r["n"] > 0
    )
    brier = float(np.mean((preds - actuals) ** 2))
    bias = float(np.mean(preds - actuals))

    # ASCII reliability diagram
    print(f"\n{'='*60}")
    print(f"  {label}  (N={total:,})")
    print(f"  ECE={ece:.4f}  Brier={brier:.4f}  Bias={bias:+.4f}")
    print(f"{'='*60}")
    print(f"  {'Bin':>14}  {'N':>6}  {'Pred':>6}  {'Actual':>6}  {'Diff':>6}  Chart")
    print(f"  {'-'*14}  {'-'*6}  {'-'*6}  {'-'*6}  {'-'*6}  {'-'*30}")
    for r in results:
        if r["n"] == 0:
            continue
        lo = bins[r["bin"]]
        hi = bins[r["bin"] + 1]
        diff = r["pred_mean"] - r["actual_mean"]
        bar_pred   = int((r["pred_mean"]   + 1) / 2 * 28)
        bar_actual = int((r["actual_mean"] + 1) / 2 * 28)
        chart = ['.'] * 30
        if 0 <= bar_actual < 30:
            chart[bar_actual] = 'A'
        if 0 <= bar_pred < 30:
            chart[bar_pred] = 'P' if chart[bar_pred] == '.' else 'X'
        print(f"  [{lo:+.1f},{hi:+.1f})  {r['n']:>6}  {r['pred_mean']:>+.3f}  {r['actual_mean']:>+.3f}  {diff:>+.3f}  {''.join(chart)}")

    return {"label": label, "n": total, "ece": ece, "brier": brier, "bias": bias, "bins": results}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", default=None, help="Path to .pt checkpoint (auto-detected if omitted)")
    parser.add_argument("--data-dir", default=None, help="Combined data dir (auto-detected if omitted)")
    parser.add_argument("--val-frac", type=float, default=0.1, help="Fraction of games for validation")
    parser.add_argument("--out", default=None, help="Output JSON path (auto-named if omitted)")
    args = parser.parse_args()

    # Auto-detect checkpoint
    if args.checkpoint is None:
        hist = json.load(open("results/benchmark_history.json"))
        best_gen = max(hist.keys(), key=lambda k: hist[k]["learned_vs_heuristic"])
        args.checkpoint = f"data/checkpoints/retrain_{best_gen}/baseline_best.pt"
        print(f"Auto-selected checkpoint: {args.checkpoint} (win%={hist[best_gen]['learned_vs_heuristic']})")

    gen = Path(args.checkpoint).parts[-2].replace("retrain_", "")

    if args.data_dir is None:
        # Use the combined dir for this gen, falling back to the next one
        for candidate in [f"data/combined_v{gen}", f"data/combined_v{int(gen[1:])+1}"]:
            if os.path.isdir(candidate) and list(Path(candidate).glob("*.parquet")):
                args.data_dir = candidate
                break
        print(f"Auto-selected data dir: {args.data_dir}")

    if args.out is None:
        args.out = f"results/value_calibration_{gen}.json"

    import glob as _glob
    paths = sorted(_glob.glob(os.path.join(args.data_dir, "*.parquet")))
    print(f"Found {len(paths)} parquet files — scanning game_ids (lightweight pass)...")

    # Pass 1: collect all game_ids cheaply (one column only per file)
    all_gids_sorted: list[str] = []
    for p in paths:
        gids = pl.read_parquet(p, columns=["game_id"])["game_id"].unique().sort().to_list()
        all_gids_sorted.extend(gids)
    all_gids_sorted = sorted(set(all_gids_sorted))
    n_val = max(1, int(len(all_gids_sorted) * args.val_frac))
    val_gids = set(all_gids_sorted[-n_val:])
    print(f"Total games: {len(all_gids_sorted):,}  Val games: {len(val_gids):,}")

    # Normalize list column schemas
    _LIST_COLS = ["ussr_influence","us_influence","discard_mask","removed_mask",
                  "actor_known_in","actor_known_not_in","actor_possible",
                  "opp_known_in","opp_known_not_in","opp_possible",
                  "lbl_actor_hand","lbl_card_quality","lbl_opponent_possible"]
    def _norm(f: pl.DataFrame) -> pl.DataFrame:
        casts = [pl.col(c).cast(pl.List(pl.Int32)).alias(c) for c in _LIST_COLS if c in f.columns]
        return f.with_columns(casts) if casts else f

    # Pass 2: load only val rows per file (keeps peak RSS ~= one file at a time)
    val_frames: list[pl.DataFrame] = []
    canonical: list[str] | None = None
    for p in paths:
        f = pl.read_parquet(p)
        if canonical is None:
            canonical = f.columns
        f = _norm(f.select(canonical)).filter(pl.col("game_id").is_in(val_gids))
        if len(f) == 0:
            continue
        tag = "selfplay" if "selfplay" in Path(p).name else "vs_heuristic"
        f = f.with_columns(pl.lit(tag).alias("_source"))
        val_frames.append(f)

    df_val = pl.concat(val_frames)
    print(f"Val rows loaded: {len(df_val):,}")

    # Load model and run inference
    print(f"Loading model from {args.checkpoint}...")
    model = load_checkpoint(args.checkpoint)
    print("Running inference...")
    preds = run_inference(model, df_val)

    # Replicate the training value target: final_vp / 20, clamped to [-1, 1]
    actuals = (df_val["final_vp"].cast(pl.Float32) / 20.0).clip(-1.0, 1.0).to_numpy()
    sources = df_val["_source"].to_list()
    turns   = df_val["turn"].to_numpy()

    all_results = []

    # Overall
    all_results.append(calibration_report(preds, actuals, f"Overall ({gen})"))

    # By source
    for src in ["vs_heuristic", "selfplay"]:
        mask = np.array([s == src for s in sources])
        if mask.sum() > 100:
            all_results.append(calibration_report(preds[mask], actuals[mask], f"Source: {src}"))

    # By game stage
    for stage, (lo, hi) in [("early (T1-3)", (1,3)), ("mid (T4-7)", (4,7)), ("late (T8-10)", (8,10))]:
        mask = (turns >= lo) & (turns <= hi)
        if mask.sum() > 100:
            all_results.append(calibration_report(preds[mask], actuals[mask], f"Stage: {stage}"))

    # Save
    Path("results").mkdir(exist_ok=True)
    with open(args.out, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResults saved to {args.out}")


if __name__ == "__main__":
    main()
