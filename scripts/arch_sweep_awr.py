#!/usr/bin/env python3
"""Architecture sweep using AWR offline evaluation.

Trains multiple MODEL_REGISTRY architectures on the same frozen data
and compares metrics. Much faster than PPO (~2-5 min per arch).

Usage:
    python scripts/arch_sweep_awr.py \
        --data data/awr_eval/awr_panel_v5.parquet \
        --archs country_attn_side country_attn_side_policy baseline \
        --epochs 5 --lr 3e-4 --tau 1.0
"""

import argparse
import sys
import time
from pathlib import Path

import numpy as np
import torch

_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_root / "python"))
sys.path.insert(0, str(_root))

from tsrl.constants import MODEL_REGISTRY


def run_awr_eval(
    data_path: str,
    model_type: str,
    hidden_dim: int = 256,
    checkpoint: str | None = None,
    epochs: int = 5,
    lr: float = 3e-4,
    batch_size: int = 2048,
    tau: float = 1.0,
    vf_coef: float = 0.5,
    val_frac: float = 0.1,
    seed: int = 42,
    device: str = "cuda",
    max_rows: int = 0,
) -> dict:
    """Run AWR evaluation for a single architecture. Returns metrics dict."""
    # Import here to share dataset across calls
    from scripts.train_awr import AWRDataset, eval_epoch, train_epoch

    torch.manual_seed(seed)
    np.random.seed(seed)

    from torch.utils.data import DataLoader, random_split

    dataset = AWRDataset(data_path, max_rows=max_rows)
    val_size = int(len(dataset) * val_frac)
    train_size = len(dataset) - val_size
    train_ds, val_ds = random_split(
        dataset, [train_size, val_size],
        generator=torch.Generator().manual_seed(seed),
    )

    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True,
                              num_workers=0, pin_memory=(device == "cuda"))
    val_loader = DataLoader(val_ds, batch_size=batch_size, shuffle=False,
                            num_workers=0, pin_memory=(device == "cuda"))

    # Create model
    cls = MODEL_REGISTRY[model_type]
    model = cls(hidden_dim=hidden_dim)

    if checkpoint:
        ckpt = torch.load(checkpoint, map_location="cpu", weights_only=True)
        sd = ckpt.get("model_state_dict", ckpt)
        model.load_state_dict(sd, strict=False)
        if hasattr(model, "_init_from_shared"):
            model._init_from_shared()

    model = model.to(device)
    total_params = sum(p.numel() for p in model.parameters())

    optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=1e-4)

    best_val_loss = float("inf")
    best_metrics = {}
    t0 = time.time()

    for epoch in range(epochs):
        train_metrics = train_epoch(model, train_loader, optimizer, device,
                                    tau=tau, vf_coef=vf_coef)
        val_metrics = eval_epoch(model, val_loader, device, tau=tau)

        if val_metrics["val_policy_loss"] < best_val_loss:
            best_val_loss = val_metrics["val_policy_loss"]
            best_metrics = {**train_metrics, **val_metrics}
            best_metrics["best_epoch"] = epoch + 1

    total_time = time.time() - t0

    return {
        "model_type": model_type,
        "hidden_dim": hidden_dim,
        "params": total_params,
        "train_rows": train_size,
        "val_rows": val_size,
        "time_s": total_time,
        **best_metrics,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="AWR architecture sweep")
    parser.add_argument("--data", required=True, help="AWR parquet data path")
    parser.add_argument("--archs", nargs="+", required=True,
                        help="Model types from MODEL_REGISTRY to compare")
    parser.add_argument("--hidden-dims", nargs="+", type=int, default=[256],
                        help="Hidden dimensions to try (crossed with archs)")
    parser.add_argument("--checkpoint", default=None,
                        help="Warm-start checkpoint (applied to all archs)")
    parser.add_argument("--epochs", type=int, default=5, help="Training epochs per arch")
    parser.add_argument("--lr", type=float, default=3e-4, help="Learning rate")
    parser.add_argument("--batch-size", type=int, default=2048, help="Batch size")
    parser.add_argument("--tau", type=float, default=1.0, help="AWR temperature")
    parser.add_argument("--max-rows", type=int, default=0, help="Max rows (0=all)")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--device", default="cuda", help="Device")
    parser.add_argument("--out", default=None, help="Save results JSON to this path")
    args = parser.parse_args()

    if args.device == "cuda" and not torch.cuda.is_available():
        print("CUDA not available, using CPU")
        args.device = "cpu"

    # Build experiment grid
    experiments = []
    for arch in args.archs:
        if arch not in MODEL_REGISTRY:
            print(f"WARNING: {arch} not in MODEL_REGISTRY, skipping")
            continue
        for hdim in args.hidden_dims:
            experiments.append((arch, hdim))

    if not experiments:
        print("ERROR: no valid architectures specified")
        sys.exit(1)

    print(f"=== AWR Architecture Sweep ===")
    print(f"Data: {args.data}")
    print(f"Experiments: {len(experiments)}")
    print(f"Epochs: {args.epochs}, LR: {args.lr}, tau: {args.tau}")
    print()

    results = []
    for i, (arch, hdim) in enumerate(experiments):
        tag = f"{arch}_h{hdim}"
        print(f"[{i+1}/{len(experiments)}] {tag}...", flush=True)

        metrics = run_awr_eval(
            data_path=args.data,
            model_type=arch,
            hidden_dim=hdim,
            checkpoint=args.checkpoint,
            epochs=args.epochs,
            lr=args.lr,
            batch_size=args.batch_size,
            tau=args.tau,
            seed=args.seed,
            device=args.device,
            max_rows=args.max_rows,
        )
        results.append(metrics)

        print(f"  → card={metrics.get('val_card_acc', 0):.3f} "
              f"adv_card={metrics.get('val_adv_card_acc', 0):.3f} "
              f"pl={metrics.get('val_policy_loss', 0):.3f} "
              f"vl={metrics.get('val_value_loss', 0):.3f} "
              f"({metrics['time_s']:.0f}s, {metrics['params']:,} params)")

    # Ranked table
    print(f"\n{'='*80}")
    print(f"{'Architecture':<35} {'Params':>8} {'Card%':>6} {'AdvCard%':>8} "
          f"{'PolicyL':>8} {'ValueL':>7} {'Time':>5}")
    print(f"{'='*80}")

    # Sort by advantage-weighted card accuracy (best metric for play strength proxy)
    ranked = sorted(results, key=lambda r: r.get("val_adv_card_acc", 0), reverse=True)
    for r in ranked:
        tag = f"{r['model_type']}_h{r['hidden_dim']}"
        print(f"{tag:<35} {r['params']:>8,} {r.get('val_card_acc',0):>6.1%} "
              f"{r.get('val_adv_card_acc',0):>8.1%} "
              f"{r.get('val_policy_loss',0):>8.3f} {r.get('val_value_loss',0):>7.4f} "
              f"{r['time_s']:>4.0f}s")

    print(f"{'='*80}")

    # Save results
    if args.out:
        import json
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w") as f:
            json.dump(results, f, indent=2)
        print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
