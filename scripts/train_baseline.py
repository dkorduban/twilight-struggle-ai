"""Offline imitation-learning training loop for the TSBaselineModel.

Usage
-----
    uv run python scripts/train_baseline.py \\
        --data-dir data/selfplay \\
        --out-dir checkpoints \\
        --epochs 20 \\
        --batch-size 256 \\
        --lr 3e-4 \\
        --seed 42

Losses
------
    card_loss    = CrossEntropyLoss(card_logits, card_target)
    mode_loss    = CrossEntropyLoss(mode_logits, mode_target)
    country_loss = Ops-weighted log-mixture CE(country_strategy_logits,
                                               strategy_logits,
                                               country_ops_target)
    value_loss   = MSELoss(value_pred, value_target)
    total        = card_loss + mode_loss + country_loss + value_loss

Checkpoints are saved to <out-dir>/baseline_epoch{N}.pt after each epoch.
"""

from __future__ import annotations

import argparse
import os
import random
import time

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, random_split

# Make the script runnable both as a standalone file and as a module.
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "python"))

from tsrl.policies.dataset import TS_SelfPlayDataset
from tsrl.policies.model import TSBaselineModel


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Train the TSBaselineModel on self-play Parquet data."
    )
    p.add_argument("--data-dir", required=True, help="Directory with *.parquet files")
    p.add_argument("--out-dir", default="checkpoints", help="Directory for checkpoint files")
    p.add_argument("--epochs", type=int, default=20)
    p.add_argument("--batch-size", type=int, default=256)
    p.add_argument("--lr", type=float, default=3e-4)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument(
        "--val-fraction",
        type=float,
        default=0.1,
        help="Fraction of data to hold out for validation (default 0.1)",
    )
    p.add_argument(
        "--log-interval",
        type=int,
        default=100,
        help="Log metrics every N batches (default 100)",
    )
    p.add_argument(
        "--num-workers",
        type=int,
        default=0,
        help="DataLoader worker processes (default 0 = main process)",
    )
    return p.parse_args()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def set_seed(seed: int) -> None:
    random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def make_device() -> torch.device:
    if torch.cuda.is_available():
        return torch.device("cuda")
    return torch.device("cpu")


def accuracy(
    logits: torch.Tensor,
    targets: torch.Tensor,
    ignore_index: int = -100,
) -> float:
    """Top-1 accuracy as a Python float, skipping ignore_index targets."""
    mask = targets != ignore_index
    if not mask.any():
        return float("nan")
    preds = logits.argmax(dim=-1)
    return (preds[mask] == targets[mask]).float().mean().item()


# ---------------------------------------------------------------------------
# Training epoch / eval epoch
# ---------------------------------------------------------------------------


def run_epoch(
    model: TSBaselineModel,
    loader: DataLoader,
    optimizer: torch.optim.Optimizer | None,
    device: torch.device,
    log_interval: int,
    epoch_label: str,
) -> dict[str, float]:
    """Run one full pass over ``loader``.

    If ``optimizer`` is None the pass is evaluation-only (no backward).
    Returns a dict of mean metrics over the epoch.
    """
    is_train = optimizer is not None
    model.train(is_train)

    ce_loss_fn = nn.CrossEntropyLoss()
    # ignore_index=-1 skips rows where action_mode is unknown (human-log rows
    # where the play mode cannot be inferred from the PLAY event alone).
    mode_ce_loss_fn = nn.CrossEntropyLoss(ignore_index=-1)
    mse_loss_fn = nn.MSELoss()

    total_loss = 0.0
    total_card_loss = 0.0
    total_mode_loss = 0.0
    total_country_loss = 0.0
    total_value_loss = 0.0
    total_card_acc = 0.0
    total_mode_acc = 0.0
    total_country_ce = 0.0
    total_country_top1 = 0.0
    total_value_mse = 0.0
    n_batches = 0

    t0 = time.time()

    ctx = torch.no_grad() if not is_train else torch.enable_grad()
    with ctx:
        for batch_idx, batch in enumerate(loader):
            influence = batch["influence"].to(device)
            cards = batch["cards"].to(device)
            scalars = batch["scalars"].to(device)
            card_target = batch["card_target"].to(device)
            mode_target = batch["mode_target"].to(device)
            country_ops_target = batch["country_ops_target"].to(device)
            value_target = batch["value_target"].to(device)

            outputs = model(influence, cards, scalars)
            card_logits = outputs["card_logits"]
            mode_logits = outputs["mode_logits"]
            country_logits = outputs["country_logits"]
            country_strategy_logits = outputs["country_strategy_logits"]
            strategy_logits = outputs["strategy_logits"]
            value_pred = outputs["value"]

            card_loss = ce_loss_fn(card_logits, card_target)
            mode_loss = mode_ce_loss_fn(mode_logits, mode_target)
            value_loss = mse_loss_fn(value_pred, value_target)

            # Country loss: only on rows with at least one country op target.
            country_ops_mask = country_ops_target.sum(dim=1) > 0
            country_top1 = 0.0
            if country_ops_mask.any():
                ops_t = country_ops_target[country_ops_mask]
                ops_prob = ops_t / ops_t.sum(dim=1, keepdim=True)
                mixing = torch.softmax(strategy_logits[country_ops_mask], dim=1)
                strategy_probs = torch.softmax(
                    country_strategy_logits[country_ops_mask], dim=2
                )
                mixture_probs = (mixing.unsqueeze(2) * strategy_probs).sum(dim=1)
                country_loss = -(
                    ops_prob * torch.log(mixture_probs + 1e-8)
                ).sum(dim=1).mean()
                country_top1 = (
                    country_logits[country_ops_mask].argmax(dim=1)
                    == country_ops_target[country_ops_mask].argmax(dim=1)
                ).float().mean().item()
            else:
                country_loss = torch.tensor(0.0, device=device)

            loss = card_loss + mode_loss + country_loss + value_loss

            if is_train:
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

            # --- accumulate metrics ---
            total_loss += loss.item()
            total_card_loss += card_loss.item()
            total_mode_loss += mode_loss.item()
            total_country_loss += country_loss.item()
            total_value_loss += value_loss.item()
            total_card_acc += accuracy(card_logits, card_target)
            total_mode_acc += accuracy(mode_logits, mode_target, ignore_index=-1)
            total_country_ce += country_loss.item()
            total_country_top1 += country_top1
            total_value_mse += value_loss.item()
            n_batches += 1

            if (batch_idx + 1) % log_interval == 0:
                elapsed = time.time() - t0
                print(
                    f"  [{epoch_label} batch {batch_idx + 1:4d}]"
                    f"  loss={loss.item():.4f}"
                    f"  card_loss={card_loss.item():.4f}"
                    f"  mode_loss={mode_loss.item():.4f}"
                    f"  country_loss={country_loss.item():.4f}"
                    f"  country_ce={country_loss.item():.4f}"
                    f"  value_mse={value_loss.item():.4f}"
                    f"  card_top1={accuracy(card_logits, card_target):.3f}"
                    f"  mode_acc={accuracy(mode_logits, mode_target, ignore_index=-1):.3f}"
                    f"  country_top1={country_top1:.3f}"
                    f"  elapsed={elapsed:.1f}s"
                )

    if n_batches == 0:
        return {}

    return {
        "loss": total_loss / n_batches,
        "card_loss": total_card_loss / n_batches,
        "mode_loss": total_mode_loss / n_batches,
        "country_loss": total_country_loss / n_batches,
        "value_loss": total_value_loss / n_batches,
        "card_top1": total_card_acc / n_batches,
        "mode_acc": total_mode_acc / n_batches,
        "country_ce": total_country_ce / n_batches,
        "country_top1": total_country_top1 / n_batches,
        "value_mse": total_value_mse / n_batches,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    import sys
    # Force unbuffered stdout so logs appear immediately when redirected to a file.
    sys.stdout.reconfigure(line_buffering=True)

    args = parse_args()
    set_seed(args.seed)
    device = make_device()

    print(f"Device: {device}")
    print(f"Data dir: {args.data_dir}")
    print(f"Output dir: {args.out_dir}")

    # ---- dataset ----
    full_dataset = TS_SelfPlayDataset(args.data_dir)
    n_total = len(full_dataset)
    n_val = max(1, int(n_total * args.val_fraction))
    n_train = n_total - n_val
    print(f"Dataset: {n_total} steps  (train={n_train}, val={n_val})")

    generator = torch.Generator().manual_seed(args.seed)
    train_ds, val_ds = random_split(full_dataset, [n_train, n_val], generator=generator)

    train_loader = DataLoader(
        train_ds,
        batch_size=args.batch_size,
        shuffle=True,
        num_workers=args.num_workers,
        generator=generator,
        drop_last=False,
        persistent_workers=(args.num_workers > 0),  # avoids per-epoch worker restart
    )
    val_loader = DataLoader(
        val_ds,
        batch_size=args.batch_size,
        shuffle=False,
        num_workers=args.num_workers,
        drop_last=False,
        persistent_workers=(args.num_workers > 0),
    )

    # ---- model ----
    model = TSBaselineModel().to(device)
    n_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"Model parameters: {n_params:,}")

    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr)

    # ---- checkpoint directory ----
    os.makedirs(args.out_dir, exist_ok=True)

    # ---- training loop ----
    best_val_loss = float("inf")
    best_ckpt_path = os.path.join(args.out_dir, "baseline_best.pt")

    for epoch in range(1, args.epochs + 1):
        t_epoch = time.time()
        print(f"\n=== Epoch {epoch}/{args.epochs} ===")

        train_metrics = run_epoch(
            model, train_loader, optimizer, device, args.log_interval, f"train e{epoch}"
        )
        val_metrics = run_epoch(
            model, val_loader, None, device, args.log_interval, f"val   e{epoch}"
        )

        elapsed = time.time() - t_epoch
        val_loss = val_metrics.get("loss", float("nan"))
        is_best = val_loss < best_val_loss
        if is_best:
            best_val_loss = val_loss

        print(
            f"Epoch {epoch} summary"
            f"  train_loss={train_metrics.get('loss', float('nan')):.4f}"
            f"  train_card_top1={train_metrics.get('card_top1', float('nan')):.3f}"
            f"  train_mode_acc={train_metrics.get('mode_acc', float('nan')):.3f}"
            f"  train_country_ce={train_metrics.get('country_ce', float('nan')):.4f}"
            f"  val_loss={val_loss:.4f}"
            f"  val_card_top1={val_metrics.get('card_top1', float('nan')):.3f}"
            f"  val_mode_acc={val_metrics.get('mode_acc', float('nan')):.3f}"
            f"  val_country_ce={val_metrics.get('country_ce', float('nan')):.4f}"
            f"  country_top1={val_metrics.get('country_top1', float('nan')):.3f}"
            f"  val_value_mse={val_metrics.get('value_mse', float('nan')):.4f}"
            f"  elapsed={elapsed:.1f}s"
            + ("  [BEST]" if is_best else "")
        )

        ckpt_payload = {
            "epoch": epoch,
            "model_state_dict": model.state_dict(),
            "optimizer_state_dict": optimizer.state_dict(),
            "train_metrics": train_metrics,
            "val_metrics": val_metrics,
            "args": vars(args),
            "seed": args.seed,
        }

        # ---- per-epoch checkpoint ----
        ckpt_path = os.path.join(args.out_dir, f"baseline_epoch{epoch}.pt")
        torch.save(ckpt_payload, ckpt_path)
        print(f"Saved checkpoint: {ckpt_path}")

        # ---- best-val checkpoint ----
        if is_best:
            torch.save(ckpt_payload, best_ckpt_path)
            print(f"Saved best checkpoint: {best_ckpt_path}  (val_loss={val_loss:.4f})")

    print(f"\nTraining complete. Best val_loss={best_val_loss:.4f} -> {best_ckpt_path}")


if __name__ == "__main__":
    main()
