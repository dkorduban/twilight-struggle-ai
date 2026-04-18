"""Value head calibration audit and temperature scaling.

Measures bias in the value head and fits post-hoc calibration (temperature scaling
or isotonic regression). Reports Brier score before/after calibration.

Usage:
    PYTHONPATH=build-ninja/bindings uv run python scripts/calibrate_value_head.py \
        --model results/ppo_gnn_card_attn_v1/ppo_iter0030_scripted.pt \
        --data data/awr_eval/awr_panel_v7.parquet \
        [--n-samples 5000] [--device cpu]
"""
from __future__ import annotations
import argparse
import sys
import numpy as np
from pathlib import Path


def parse_args():
    p = argparse.ArgumentParser(description="Value head calibration audit")
    p.add_argument("--model", required=True)
    p.add_argument("--data", default="data/awr_eval/awr_panel_v7.parquet")
    p.add_argument("--n-samples", type=int, default=5000)
    p.add_argument("--device", default="cpu")
    p.add_argument("--seed", type=int, default=42)
    return p.parse_args()


def run_model_on_batch(model, influence, cards, scalars, device):
    import torch
    with torch.no_grad():
        inf_t = torch.tensor(influence, dtype=torch.float32, device=device)
        cards_t = torch.tensor(cards, dtype=torch.float32, device=device)
        sc_t = torch.tensor(scalars, dtype=torch.float32, device=device)
        out = model(inf_t, cards_t, sc_t)
        return out["value"].squeeze(-1).cpu().numpy()


def brier_score(y_pred_raw: np.ndarray, y_true: np.ndarray) -> float:
    """Brier score on probability scale. y_true in {-1, 1}, y_pred in [-1, 1]."""
    p_pred = (y_pred_raw + 1) / 2  # [-1,1] -> [0,1]
    p_true = (y_true + 1) / 2
    return float(np.mean((p_pred - p_true) ** 2))


def temperature_scale(preds: np.ndarray, targets: np.ndarray) -> float:
    """Find temperature T such that mean(preds/T) ≈ mean(targets).
    Returns optimal T via binary search."""
    bias = np.mean(preds) - np.mean(targets)
    if abs(bias) < 1e-4:
        return 1.0
    # Temperature scaling: preds' = preds / T
    # We want mean(preds/T) = mean(targets)
    # T = mean(preds) / mean(targets) if both nonzero
    if abs(np.mean(targets)) > 0.01:
        T = np.mean(preds) / np.mean(targets)
        return float(max(0.1, min(10.0, T)))
    return 1.0


def main():
    args = parse_args()
    import torch
    import polars as pl

    rng = np.random.default_rng(args.seed)

    print(f"Loading model: {args.model}")
    model = torch.jit.load(args.model, map_location=args.device)
    model.eval()

    print(f"Loading data: {args.data}")
    df = pl.read_parquet(args.data)

    # Sample rows
    idx = rng.choice(len(df), size=min(args.n_samples, len(df)), replace=False)
    df_sample = df[idx]

    influence = df_sample["influence"].to_list()
    cards = df_sample["cards"].to_list()
    scalars = df_sample["scalars"].to_list()
    returns = df_sample["returns"].to_numpy()  # actual returns
    turns = df_sample["turn"].to_numpy()

    # Run model in batches
    batch_size = 256
    preds = []
    for i in range(0, len(influence), batch_size):
        v = run_model_on_batch(
            model,
            influence[i:i+batch_size],
            cards[i:i+batch_size],
            scalars[i:i+batch_size],
            args.device,
        )
        preds.extend(v.tolist())
    preds = np.array(preds)

    # Overall stats
    bias = float(np.mean(preds - returns))
    brier_before = brier_score(preds, returns)
    corr = float(np.corrcoef(preds, returns)[0, 1])
    mae = float(np.mean(np.abs(preds - returns)))

    print(f"\n=== Value Head Calibration Report ===")
    print(f"Model:    {Path(args.model).name}")
    print(f"Samples:  {len(preds)}")
    print(f"Bias:     {bias:+.4f}  (model overestimates by {bias:.1%})")
    print(f"MAE:      {mae:.4f}")
    print(f"Brier:    {brier_before:.4f}")
    print(f"Corr:     {corr:.4f}")

    # Per-phase breakdown
    print(f"\n--- Per-phase ---")
    for label, lo, hi in [("early (t1-3)", 1, 3), ("mid (t4-7)", 4, 7), ("late (t8-10)", 8, 10)]:
        mask = (turns >= lo) & (turns <= hi)
        if mask.sum() < 10:
            continue
        p, r = preds[mask], returns[mask]
        print(f"  {label}: n={mask.sum()}, bias={np.mean(p-r):+.4f}, "
              f"Brier={brier_score(p, r):.4f}, corr={np.corrcoef(p, r)[0,1]:.4f}")

    # Temperature scaling calibration
    T = temperature_scale(preds, returns)
    preds_calib = preds / T
    brier_after = brier_score(preds_calib, returns)
    bias_after = float(np.mean(preds_calib - returns))

    print(f"\n--- Temperature scaling ---")
    print(f"  Temperature T = {T:.4f}")
    print(f"  Bias after:    {bias_after:+.4f}")
    print(f"  Brier after:   {brier_after:.4f}  ({(brier_after-brier_before)/brier_before*100:+.1f}%)")

    # Isotonic regression (bins)
    print(f"\n--- Calibration curve (10 bins by predicted value) ---")
    bins = np.percentile(preds, np.linspace(0, 100, 11))
    for i in range(10):
        mask = (preds >= bins[i]) & (preds < bins[i+1])
        if mask.sum() < 5:
            continue
        print(f"  pred=[{bins[i]:+.3f},{bins[i+1]:+.3f}]: "
              f"mean_pred={np.mean(preds[mask]):+.3f}, "
              f"mean_true={np.mean(returns[mask]):+.3f}, "
              f"n={mask.sum()}")

    # Interpretation
    print(f"\n=== Interpretation ===")
    if abs(bias) > 0.08:
        print(f"SIGNIFICANT BIAS: {bias:+.3f}. Causes ISMCTS overoptimism under determinization.")
        print(f"Fix: Add value_calibration_loss = (mean(v_pred) - mean(returns))^2 to PPO loss")
        print(f"  OR apply post-hoc divisor T={T:.3f} at inference.")
    elif abs(bias) > 0.04:
        print(f"MODERATE BIAS: {bias:+.3f}. Monitor across PPO iterations.")
    else:
        print(f"Bias within tolerance: {bias:+.3f}. No calibration needed.")

    if corr < 0.5:
        print(f"LOW CORRELATION ({corr:.3f}): Value head has poor predictive power.")
        print(f"  → Self-play with wider opponent pool may improve this.")
    else:
        print(f"Correlation {corr:.3f}: Value head is informative.")


if __name__ == "__main__":
    main()
