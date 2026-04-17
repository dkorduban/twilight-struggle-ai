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
    crr_filter: bool = False,
    preloaded_dataset=None,
    train_indices=None,
    val_indices=None,
) -> dict:
    """Run AWR evaluation for a single architecture. Returns metrics dict.

    If preloaded_dataset is provided (along with train_indices/val_indices),
    skip dataset loading — just create DataLoaders and run.
    """
    # Import here to share dataset across calls
    from scripts.train_awr import AWRDataset, eval_epoch, train_epoch

    torch.manual_seed(seed)
    np.random.seed(seed)

    from torch.utils.data import DataLoader, Subset, random_split

    if preloaded_dataset is not None and train_indices is not None and val_indices is not None:
        # Reshuffle train indices with this seed for reproducibility across seeds
        rng = np.random.default_rng(seed)
        train_idx = rng.permutation(train_indices).tolist()
        val_idx = val_indices.tolist() if hasattr(val_indices, 'tolist') else list(val_indices)
        train_ds = Subset(preloaded_dataset, train_idx)
        val_ds = Subset(preloaded_dataset, val_idx)
    else:
        dataset = AWRDataset(data_path, max_rows=max_rows)
        val_size_n = int(len(dataset) * val_frac)
        train_size_n = len(dataset) - val_size_n
        train_ds, val_ds = random_split(
            dataset, [train_size_n, val_size_n],
            generator=torch.Generator().manual_seed(seed),
        )
    train_size = len(train_ds)
    val_size = len(val_ds)

    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True,
                              num_workers=2, pin_memory=(device == "cuda"),
                              persistent_workers=True)
    val_loader = DataLoader(val_ds, batch_size=batch_size, shuffle=False,
                            num_workers=1, pin_memory=(device == "cuda"),
                            persistent_workers=True)

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
                                    tau=tau, vf_coef=vf_coef, crr_filter=crr_filter)
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
    # Multi-tau support: sweep over multiple temperatures, tau=1e6 approximates uniform BC
    parser.add_argument("--taus", nargs="+", type=float, default=[1.0],
                        help="AWR temperatures to sweep (default [1.0]; use 0.5 1.0 2.0 1e6 for full sweep)")
    parser.add_argument("--tau", type=float, default=None,
                        help="Single AWR temperature (deprecated, use --taus)")
    parser.add_argument("--seeds", nargs="+", type=int, default=[42],
                        help="Random seeds (results averaged across seeds)")
    parser.add_argument("--crr-filter", action="store_true",
                        help="CRR-lite: train only on positive-advantage examples")
    parser.add_argument("--max-rows", type=int, default=0, help="Max rows (0=all)")
    parser.add_argument("--device", default="cuda", help="Device")
    parser.add_argument("--out", default=None, help="Save results JSON to this path")
    args = parser.parse_args()

    # Backward compat: --tau overrides --taus
    if args.tau is not None:
        args.taus = [args.tau]

    if args.device == "cuda" and not torch.cuda.is_available():
        print("CUDA not available, using CPU")
        args.device = "cpu"

    # Build experiment grid: arch × hidden_dim × tau × seed
    base_experiments = []
    for arch in args.archs:
        if arch not in MODEL_REGISTRY:
            print(f"WARNING: {arch} not in MODEL_REGISTRY, skipping")
            continue
        for hdim in args.hidden_dims:
            base_experiments.append((arch, hdim))

    if not base_experiments:
        print("ERROR: no valid architectures specified")
        sys.exit(1)

    total_runs = len(base_experiments) * len(args.taus) * len(args.seeds)
    crr_label = " [CRR-lite]" if args.crr_filter else ""
    print(f"=== AWR Architecture Sweep{crr_label} ===")
    print(f"Data: {args.data}")
    print(f"Archs×dims: {len(base_experiments)}, Taus: {args.taus}, Seeds: {args.seeds}")
    print(f"Total runs: {total_runs}")
    print(f"Epochs: {args.epochs}, LR: {args.lr}")
    print()

    # Pre-load dataset once — avoids re-reading parquet for each experiment
    # (1.27M rows takes 3-5 min to parse; 108x loading = hours of overhead)
    from scripts.train_awr import AWRDataset
    print("Loading dataset (once for all experiments)...")
    t0_load = time.time()
    full_dataset = AWRDataset(args.data, max_rows=args.max_rows)
    val_size = int(len(full_dataset) * 0.1)  # 10% val split
    train_size = len(full_dataset) - val_size
    # Use seed 42 for the canonical train/val split (all seeds see same split)
    rng = np.random.default_rng(42)
    all_idx = rng.permutation(len(full_dataset))
    val_indices = all_idx[:val_size]
    train_indices = all_idx[val_size:]
    print(f"  Loaded in {time.time()-t0_load:.1f}s — train={train_size:,} val={val_size:,}")
    print()

    all_results = []
    run_idx = 0
    for arch, hdim in base_experiments:
        for tau in args.taus:
            seed_metrics = []
            for seed in args.seeds:
                run_idx += 1
                tag = f"{arch}_h{hdim}_tau{tau}_s{seed}"
                print(f"[{run_idx}/{total_runs}] {tag}...", flush=True)

                metrics = run_awr_eval(
                    data_path=args.data,
                    model_type=arch,
                    hidden_dim=hdim,
                    checkpoint=args.checkpoint,
                    epochs=args.epochs,
                    lr=args.lr,
                    batch_size=args.batch_size,
                    tau=tau,
                    seed=seed,
                    device=args.device,
                    max_rows=args.max_rows,
                    crr_filter=args.crr_filter,
                    preloaded_dataset=full_dataset,
                    train_indices=train_indices,
                    val_indices=val_indices,
                )
                metrics["tau"] = tau
                metrics["seed"] = seed
                seed_metrics.append(metrics)
                all_results.append(metrics)

                print(f"  → card={metrics.get('val_card_acc', 0):.3f} "
                      f"adv_card={metrics.get('val_adv_card_acc', 0):.3f} "
                      f"pl={metrics.get('val_policy_loss', 0):.3f} "
                      f"({metrics['time_s']:.0f}s)")

            # Aggregate across seeds for this arch×tau
            if len(seed_metrics) > 1:
                avg_adv = np.mean([m.get("val_adv_card_acc", 0) for m in seed_metrics])
                std_adv = np.std([m.get("val_adv_card_acc", 0) for m in seed_metrics])
                print(f"  → {arch}_h{hdim} tau={tau}: adv_card={avg_adv:.3f} ± {std_adv:.3f}")

    # Aggregate per arch×dim×tau: mean across seeds
    from collections import defaultdict
    agg = defaultdict(list)
    for r in all_results:
        key = (r["model_type"], r["hidden_dim"], r.get("tau", 1.0))
        agg[key].append(r)

    agg_results = []
    for key, runs in agg.items():
        arch, hdim, tau = key
        entry = {
            "model_type": arch,
            "hidden_dim": hdim,
            "tau": tau,
            "params": runs[0]["params"],
            "n_seeds": len(runs),
        }
        for metric in ["val_adv_card_acc", "val_card_acc", "val_policy_loss", "val_value_loss", "time_s"]:
            vals = [r.get(metric, 0) for r in runs]
            entry[metric] = float(np.mean(vals))
            entry[f"{metric}_std"] = float(np.std(vals))
        agg_results.append(entry)

    # Ranked table (sorted by val_adv_card_acc across taus within each arch)
    print(f"\n{'='*90}")
    print(f"{'Architecture':<35} {'tau':>6} {'Seeds':>5} {'Card%':>6} {'AdvCard%':>9} {'AdvCard±':>8} {'PolicyL':>8}")
    print(f"{'='*90}")

    ranked = sorted(agg_results, key=lambda r: r.get("val_adv_card_acc", 0), reverse=True)
    for r in ranked:
        tag = f"{r['model_type']}_h{r['hidden_dim']}"
        tau_str = f"{r['tau']:.3g}"
        print(f"{tag:<35} {tau_str:>6} {r['n_seeds']:>5} {r.get('val_card_acc',0):>6.1%} "
              f"{r.get('val_adv_card_acc',0):>9.1%} "
              f"±{r.get('val_adv_card_acc_std',0):>6.3f} "
              f"{r.get('val_policy_loss',0):>8.3f}")

    print(f"{'='*90}")
    print(f"\nTop-3 by val_adv_card_acc:")
    for r in ranked[:3]:
        tag = f"{r['model_type']}_h{r['hidden_dim']}_tau{r['tau']:.3g}"
        print(f"  {tag}: {r.get('val_adv_card_acc',0):.3%}")

    # Save results
    if args.out:
        import json
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w") as f:
            json.dump({"runs": all_results, "aggregated": agg_results}, f, indent=2)
        print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
