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
    value_loss   = MSELoss(value_pred, value_target)  # target = winner_side or final_vp/20
                                                     #   (defcon1/europe_control always use winner_side)
    total        = card_loss + mode_loss + country_loss + value_weight * value_loss

    With --advantage-weight alpha > 0 (train only):
        advantage_i  = value_target_i - value_pred_i.detach()   # residual, game-level signal
        w_i          = clamp(1 + alpha * advantage_i, 0.1, 2.0) # always positive
        policy_loss  = mean(w_i * (card_loss_i + mode_loss_i + country_loss_i))

    Design notes
    ~~~~~~~~~~~~
    This is inspired by AWR / AWAC (offline advantage-weighted regression) but
    uses a **clamped linear** weight rather than the canonical exponential form
    exp(A/tau).  Key choices and their rationale:

    * value_pred is **detached**: advantage is a reweighting signal only; it
      must not create a competing gradient path back through the value head.

    * clamp(0.1, 2.0) keeps weights **strictly positive** — gradients are
      never reversed and bad-outcome games still contribute (at 10x reduced
      weight) rather than being discarded entirely.  Standard nonneg AWR
      (w = max(0, A)) would discard the ~86 % of games where the model is
      currently losing, wasting most of the training data.

    * Linear rather than exponential: avoids the temperature hyperparameter τ
      and keeps the weight range interpretable.  The downside vs. exp() is
      that a single very-high-advantage game can saturate at 2× rather than
      pulling harder — acceptable for a game-level signal with α=0.5.

    * value_target here is final_vp (signed VP margin / 20, ≈ –1 … +1), so
      the advantage is on a consistent scale across games.

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
    p.add_argument("--weight-decay", type=float, default=0.0,
                   help="L2 weight decay for AdamW (default 0 = plain Adam)")
    p.add_argument("--label-smoothing", type=float, default=0.0,
                   help="Label smoothing epsilon for card/mode CE losses (default 0)")
    p.add_argument("--dropout", type=float, default=0.1,
                   help="Dropout probability in trunk (default 0.1)")
    p.add_argument(
        "--hidden-dim",
        type=int,
        default=256,
        help="Trunk hidden dimension (default 256)",
    )
    p.add_argument("--one-cycle", action="store_true",
                   help="Use OneCycleLR schedule (linear warmup + cosine decay)")
    p.add_argument("--compile", action="store_true",
                   help="torch.compile the model for faster training (PyTorch 2+)")
    p.add_argument("--amp", action="store_true",
                   help="Use automatic mixed precision (float16) for faster GPU training")
    p.add_argument("--resume", action="store_true",
                   help="Resume from latest checkpoint in --out-dir")
    p.add_argument("--patience", type=int, default=0,
                   help="Early stopping: stop if val_loss hasn't improved for N epochs (0 = disabled)")
    p.add_argument("--advantage-weight", type=float, default=0.0,
                   help="Scale policy losses by (1 + alpha * advantage) where advantage = value_target - value_pred. "
                        "0 = disabled (pure BC). 0.5-1.0 = moderate advantage weighting. "
                        "Reinforces surprising wins, downweights predicted losses.")
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
    p.add_argument(
        "--pin-memory",
        action="store_true",
        help="Enable pin_memory in DataLoader for faster CPU->GPU transfers (default off)",
    )
    p.add_argument(
        "--value-weight",
        type=float,
        default=1.0,
        help="Multiplier on value MSE loss relative to card/mode/country losses (default 1.0)."
             " NOTE: increasing this alone does not help if the value floor is caused by sparse"
             " terminal rewards. Use --value-target final_vp instead.",
    )
    p.add_argument(
        "--value-target",
        default="winner_side",
        choices=["winner_side", "final_vp"],
        help="Value training target: 'winner_side' (default, {-1,0,+1} terminal outcome) or"
             " 'final_vp' (final_vp/20 clamped to [-1,1], denser reward signal).",
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
    label_smoothing: float = 0.0,
    scheduler=None,
    value_weight: float = 1.0,
    scaler: "torch.cuda.amp.GradScaler | None" = None,
    advantage_weight: float = 0.0,
) -> dict[str, float]:
    """Run one full pass over ``loader``.

    If ``optimizer`` is None the pass is evaluation-only (no backward).
    Returns a dict of mean metrics over the epoch.
    """
    is_train = optimizer is not None
    model.train(is_train)

    use_adv = advantage_weight > 0.0 and is_train
    _reduction = "none" if use_adv else "mean"
    ce_loss_fn = nn.CrossEntropyLoss(label_smoothing=label_smoothing, reduction=_reduction)
    # ignore_index=-1 skips rows where action_mode is unknown (human-log rows
    # where the play mode cannot be inferred from the PLAY event alone).
    mode_ce_loss_fn = nn.CrossEntropyLoss(ignore_index=-1, label_smoothing=label_smoothing,
                                          reduction=_reduction)
    mse_loss_fn = nn.MSELoss()

    total_loss = 0.0
    total_card_loss = 0.0
    total_mode_loss = 0.0
    total_country_loss = 0.0
    total_value_loss = 0.0
    total_card_acc = 0.0
    total_card_mrr = 0.0
    total_card_nll = 0.0
    total_card_conf = 0.0
    total_mode_acc = 0.0
    total_country_ce = 0.0
    total_country_top1 = 0.0
    total_value_mse = 0.0
    n_batches = 0

    t0 = time.time()

    use_amp = scaler is not None and device.type == "cuda"
    ctx = torch.no_grad() if not is_train else torch.enable_grad()
    with ctx:
        for batch_idx, batch in enumerate(loader):
            influence = batch["influence"].to(device, non_blocking=True)
            cards = batch["cards"].to(device, non_blocking=True).float()
            scalars = batch["scalars"].to(device, non_blocking=True)
            card_target = batch["card_target"].to(device, non_blocking=True)
            mode_target = batch["mode_target"].to(device, non_blocking=True)
            country_ops_target = batch["country_ops_target"].to(device, non_blocking=True)
            value_target = batch["value_target"].to(device, non_blocking=True)

            with torch.autocast(device_type=device.type, enabled=use_amp):
                outputs = model(influence, cards, scalars)
                card_logits = outputs["card_logits"]
                mode_logits = outputs["mode_logits"]
                country_logits = outputs["country_logits"]
                country_strategy_logits = outputs["country_strategy_logits"]
                strategy_logits = outputs["strategy_logits"]
                value_pred = outputs["value"]

                card_loss_raw = ce_loss_fn(card_logits, card_target)
                mode_loss_raw = mode_ce_loss_fn(mode_logits, mode_target)
                value_loss = mse_loss_fn(value_pred, value_target)

                # Advantage-weighted regression (AWR-inspired, linear form).
                # advantage = value_target - value_pred  (positive = better than expected)
                # w = clamp(1 + alpha * advantage, 0.1, 2.0)
                #   - always positive: never inverts gradients (contrast with raw signed weights)
                #   - keeps losing games at w≈0.1 rather than discarding (contrast with max(0,A))
                #   - value_pred detached: advantage is a reweighting signal only,
                #     not a gradient path back through the value head
                #   - train only: val loss uses uniform weights for comparability
                if use_adv:
                    adv = (value_target - value_pred.detach()).squeeze(-1)
                    w = (1.0 + advantage_weight * adv).clamp(0.1, 2.0)
                    card_loss = (card_loss_raw * w).mean()
                    # mode has ignore_index=-1; mask those out before weighting
                    mode_mask = (mode_target != -1).float()
                    mode_loss = ((mode_loss_raw * w) * mode_mask).sum() / mode_mask.sum().clamp(min=1)
                else:
                    card_loss = card_loss_raw
                    mode_loss = mode_loss_raw

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
                    country_loss_per = -(
                        ops_prob * torch.log(mixture_probs + 1e-8)
                    ).sum(dim=1)
                    if use_adv:
                        w_c = w[country_ops_mask]
                        country_loss = (country_loss_per * w_c).mean()
                    else:
                        country_loss = country_loss_per.mean()
                    country_top1 = (
                        country_logits[country_ops_mask].argmax(dim=1)
                        == country_ops_target[country_ops_mask].argmax(dim=1)
                    ).float().mean().item()
                else:
                    country_loss = torch.tensor(0.0, device=device)

                loss = card_loss + mode_loss + country_loss + value_weight * value_loss

            if is_train:
                optimizer.zero_grad()
                if scaler is not None:
                    scaler.scale(loss).backward()
                    scaler.step(optimizer)
                    scaler.update()
                else:
                    loss.backward()
                    optimizer.step()
                if scheduler is not None:
                    scheduler.step()

            # --- card MRR, NLL, confidence ---
            with torch.no_grad():
                sorted_idx = card_logits.argsort(dim=1, descending=True)  # (B, 112)
                ct = card_target.unsqueeze(1)                              # (B, 1)
                ranks = (sorted_idx == ct).int().argmax(dim=1) + 1        # (B,) 1-indexed
                card_mrr_val  = (1.0 / ranks.float()).mean().item()
                probs = torch.softmax(card_logits, dim=1)
                card_nll_val  = torch.nn.functional.cross_entropy(card_logits, card_target, reduction='mean').item()
                card_conf_val = probs.max(dim=1).values.mean().item()

            # --- accumulate metrics ---
            total_loss += loss.item()
            total_card_loss += card_loss.item()
            total_mode_loss += mode_loss.item()
            total_country_loss += country_loss.item()
            total_value_loss += value_loss.item()
            total_card_acc += accuracy(card_logits, card_target)
            total_card_mrr  += card_mrr_val
            total_card_nll  += card_nll_val
            total_card_conf += card_conf_val
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
        "card_top1": total_card_acc  / n_batches,
        "card_mrr":  total_card_mrr  / n_batches,
        "card_nll":  total_card_nll  / n_batches,
        "card_conf": total_card_conf / n_batches,
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
    full_dataset = TS_SelfPlayDataset(args.data_dir, value_target_mode=args.value_target)
    n_total = len(full_dataset)
    n_val = max(1, int(n_total * args.val_fraction))
    n_train = n_total - n_val
    print(f"Dataset: {n_total} steps  (train={n_train}, val={n_val})")

    generator = torch.Generator().manual_seed(args.seed)
    train_ds, val_ds = random_split(full_dataset, [n_train, n_val], generator=generator)

    # Use 'forkserver' (or 'spawn') to avoid Polars/OpenMP thread-pool corruption
    # after fork. Polars uses internal Rayon/BLAS thread pools that deadlock in
    # forked child processes. 'forkserver' spawns a clean server process instead.
    mp_ctx = "forkserver" if args.num_workers > 0 else None
    # TS_SelfPlayDataset implements __getitems__ for vectorised batch indexing.
    # The dataset returns a pre-batched dict, so collate_fn must be a pass-through.
    _passthrough_collate = TS_SelfPlayDataset.passthrough_collate
    train_loader = DataLoader(
        train_ds,
        batch_size=args.batch_size,
        shuffle=True,
        num_workers=args.num_workers,
        generator=generator,
        drop_last=False,
        persistent_workers=(args.num_workers > 0),
        pin_memory=args.pin_memory,
        multiprocessing_context=mp_ctx,
        collate_fn=_passthrough_collate,
    )
    val_loader = DataLoader(
        val_ds,
        batch_size=args.batch_size,
        shuffle=False,
        num_workers=args.num_workers,
        drop_last=False,
        persistent_workers=(args.num_workers > 0),
        pin_memory=args.pin_memory,
        multiprocessing_context=mp_ctx,
        collate_fn=_passthrough_collate,
    )

    # ---- model ----
    model = TSBaselineModel(dropout=args.dropout, hidden_dim=args.hidden_dim).to(device)
    n_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"Model parameters: {n_params:,}")
    if args.compile:
        model = torch.compile(model)
        print("Model compiled with torch.compile")

    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    scheduler = None
    if args.one_cycle:
        scheduler = torch.optim.lr_scheduler.OneCycleLR(
            optimizer,
            max_lr=args.lr,
            epochs=args.epochs,
            steps_per_epoch=len(train_loader),
        )

    # ---- checkpoint directory ----
    os.makedirs(args.out_dir, exist_ok=True)

    # ---- resume from latest checkpoint if requested ----
    best_val_loss = float("inf")
    start_epoch = 1
    best_ckpt_path = os.path.join(args.out_dir, "baseline_best.pt")

    if args.resume:
        import glob as _glob
        epoch_ckpts = sorted(
            _glob.glob(os.path.join(args.out_dir, "baseline_epoch*.pt")),
            key=lambda p: int(os.path.basename(p).replace("baseline_epoch", "").replace(".pt", "")),
        )
        if epoch_ckpts:
            latest = epoch_ckpts[-1]
            print(f"Resuming from {latest}")
            ckpt = torch.load(latest, map_location=device, weights_only=False)
            model.load_state_dict(ckpt["model_state_dict"])
            optimizer.load_state_dict(ckpt["optimizer_state_dict"])
            if scheduler is not None and "scheduler_state_dict" in ckpt:
                scheduler.load_state_dict(ckpt["scheduler_state_dict"])
            start_epoch = ckpt["epoch"] + 1
            best_val_loss = ckpt.get("val_metrics", {}).get("loss", float("inf"))
            print(f"Resumed at epoch {start_epoch}, best_val_loss={best_val_loss:.4f}")
        else:
            print("--resume specified but no checkpoints found; starting fresh")

    # ---- AMP scaler ----
    scaler = torch.cuda.amp.GradScaler() if (getattr(args, "amp", False) and device.type == "cuda") else None
    if scaler is not None:
        print("AMP enabled (float16 autocast + GradScaler)")

    # ---- early stopping state ----
    epochs_no_improve = 0

    # ---- training loop ----
    for epoch in range(start_epoch, args.epochs + 1):
        t_epoch = time.time()
        print(f"\n=== Epoch {epoch}/{args.epochs} ===")

        train_metrics = run_epoch(
            model, train_loader, optimizer, device, args.log_interval, f"train e{epoch}",
            label_smoothing=args.label_smoothing,
            scheduler=scheduler,
            value_weight=args.value_weight,
            scaler=scaler,
            advantage_weight=getattr(args, "advantage_weight", 0.0),
        )
        val_metrics = run_epoch(
            model, val_loader, None, device, args.log_interval, f"val   e{epoch}",
            label_smoothing=args.label_smoothing,
            value_weight=args.value_weight,
        )

        elapsed = time.time() - t_epoch
        val_loss = val_metrics.get("loss", float("nan"))
        is_best = val_loss < best_val_loss
        if is_best:
            best_val_loss = val_loss
            epochs_no_improve = 0
        else:
            epochs_no_improve += 1

        print(
            f"Epoch {epoch} summary"
            + ("  [adv-weighted]" if getattr(args, "advantage_weight", 0.0) > 0 else "")
            + f"  train_loss={train_metrics.get('loss', float('nan')):.4f}"
            f"  train_card_top1={train_metrics.get('card_top1', float('nan')):.3f}"
            f"  train_card_mrr={train_metrics.get('card_mrr', float('nan')):.3f}"
            f"  train_mode_acc={train_metrics.get('mode_acc', float('nan')):.3f}"
            f"  train_country_ce={train_metrics.get('country_ce', float('nan')):.4f}"
            f"  val_loss={val_loss:.4f}"
            f"  val_card_top1={val_metrics.get('card_top1', float('nan')):.3f}"
            f"  val_card_mrr={val_metrics.get('card_mrr', float('nan')):.3f}"
            f"  val_card_nll={val_metrics.get('card_nll', float('nan')):.4f}"
            f"  val_card_conf={val_metrics.get('card_conf', float('nan')):.3f}"
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
            "scheduler_state_dict": scheduler.state_dict() if scheduler is not None else None,
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

        # ---- early stopping ----
        if args.patience > 0 and epochs_no_improve >= args.patience:
            print(f"\nEarly stopping at epoch {epoch}: no improvement for {epochs_no_improve} epochs.")
            break

    print(f"\nTraining complete. Best val_loss={best_val_loss:.4f} -> {best_ckpt_path}")


if __name__ == "__main__":
    main()
