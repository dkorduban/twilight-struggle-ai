"""
fit_value_calibration.py — Fit Platt scaling for the value head on the validation split.

Usage:
    uv run python scripts/fit_value_calibration.py \
        --data-dir data/combined_v47_vsh_filtered \
        --checkpoint checkpoints/v47/best.pt \
        --out calibration_params.json \
        [--n-bins 20]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import torch
import torch.nn.functional as F

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from check_value_calibration import (
    apply_platt_scaling,
    autodetect_checkpoint,
    autodetect_data_dir,
    calibration_report,
    default_output_path,
    infer_generation_from_checkpoint,
    load_checkpoint,
    load_validation_frame,
    run_inference,
    value_targets,
)


def fit_platt(v_raw, v_target, max_iter: int = 100) -> tuple[float, float]:
    raw_t = torch.as_tensor(v_raw, dtype=torch.float32)
    target_t = torch.as_tensor((v_target + 1.0) / 2.0, dtype=torch.float32)

    a = torch.nn.Parameter(torch.tensor(1.0, dtype=torch.float32))
    b = torch.nn.Parameter(torch.tensor(0.0, dtype=torch.float32))
    optimizer = torch.optim.LBFGS(
        [a, b],
        lr=0.5,
        max_iter=max_iter,
        tolerance_grad=1e-9,
        tolerance_change=1e-9,
        line_search_fn="strong_wolfe",
    )

    def closure():
        optimizer.zero_grad()
        logits = a * raw_t + b
        loss = F.binary_cross_entropy_with_logits(logits, target_t)
        loss.backward()
        return loss

    optimizer.step(closure)
    return float(a.detach().item()), float(b.detach().item())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--checkpoint", default=None, help="Path to .pt checkpoint (auto-detected if omitted)"
    )
    parser.add_argument(
        "--data-dir", default=None, help="Combined data dir (auto-detected if omitted)"
    )
    parser.add_argument(
        "--val-frac", type=float, default=0.1, help="Fraction of games for validation"
    )
    parser.add_argument("--out", default=None, help="Output JSON path")
    parser.add_argument("--n-bins", type=int, default=20, help="ECE bin count")
    args = parser.parse_args()

    if args.checkpoint is None:
        args.checkpoint = autodetect_checkpoint()
    generation = infer_generation_from_checkpoint(args.checkpoint)

    if args.data_dir is None:
        args.data_dir = autodetect_data_dir(generation)
    if args.out is None:
        args.out = default_output_path(generation, suffix="value_calibration_params")

    df_val = load_validation_frame(args.data_dir, args.val_frac)
    print(f"Loading model from {args.checkpoint}...")
    model = load_checkpoint(args.checkpoint)
    print("Running inference...")
    raw_preds = run_inference(model, df_val)
    actuals = value_targets(df_val)

    print("Fitting Platt scaling...")
    a, b = fit_platt(raw_preds, actuals)
    calibrated_preds = apply_platt_scaling(raw_preds, a, b)

    before = calibration_report(raw_preds, actuals, "Before calibration", n_bins=args.n_bins)
    after = calibration_report(calibrated_preds, actuals, "After calibration", n_bins=args.n_bins)

    payload = {
        "method": "platt",
        "a": a,
        "b": b,
        "ece_before": before["ece"],
        "ece_after": after["ece"],
        "source": Path(args.data_dir).name,
        "n_samples": int(len(actuals)),
    }

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
    print(f"\nWrote calibration params to {out_path}")


if __name__ == "__main__":
    main()
