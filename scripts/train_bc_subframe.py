#!/usr/bin/env python3
"""Train the mixed AR/sub-frame BC baseline."""

from __future__ import annotations

import argparse
import json
import os
import random
import sys
import time
from pathlib import Path

import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader, Subset, random_split

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "python"))

from tsrl.policies.dataset import (
    NUM_TARGET_HEADS,
    TARGET_HEAD_AR,
    TARGET_HEAD_CARD_PICK,
    TARGET_HEAD_COUNTRY_PICK,
    TARGET_HEAD_HEADLINE,
    TARGET_HEAD_SMALL_CHOICE,
    TS_SelfPlayDataset,
)
from tsrl.policies.model import TSCountryAttnSubframeModel


DEFAULT_WARMSTART = "results/ppo_v32_continue/ppo_best.pt"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", required=True, help="Parquet file or directory of *.parquet")
    parser.add_argument("--out-dir", default="results/bc_subframe_v1")
    parser.add_argument("--epochs", type=int, default=30)
    parser.add_argument("--batch-size", type=int, default=1024)
    parser.add_argument("--lr", type=float, default=1e-4)
    parser.add_argument("--weight-decay", type=float, default=1e-4)
    parser.add_argument("--label-smoothing", type=float, default=0.05)
    parser.add_argument("--dropout", type=float, default=0.1)
    parser.add_argument("--hidden-dim", type=int, default=256)
    parser.add_argument("--value-weight", type=float, default=0.5)
    parser.add_argument("--val-fraction", type=float, default=0.1)
    parser.add_argument("--seed", type=int, default=20260421)
    parser.add_argument("--num-workers", type=int, default=0)
    parser.add_argument("--pin-memory", action="store_true")
    parser.add_argument("--log-interval", type=int, default=100)
    parser.add_argument("--random-split", action="store_true")
    parser.add_argument("--no-bf16", action="store_true")
    parser.add_argument(
        "--warmstart",
        nargs="?",
        const=DEFAULT_WARMSTART,
        default=None,
        help=f"Warm-start model weights; default path when passed without value: {DEFAULT_WARMSTART}",
    )
    parser.add_argument("--init-from", default=None, help="Alias for --warmstart PATH")
    return parser.parse_args()


def set_seed(seed: int) -> None:
    random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def make_device() -> torch.device:
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def _zero(device: torch.device) -> torch.Tensor:
    return torch.zeros((), device=device)


def _mask_logits_with_fallback(logits: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
    legal = mask.to(device=logits.device, dtype=torch.bool)
    if legal.shape[-1] > logits.shape[-1]:
        legal = legal[..., : logits.shape[-1]]
    if legal.shape[-1] != logits.shape[-1]:
        raise ValueError(f"mask width {legal.shape[-1]} != logits width {logits.shape[-1]}")
    has_legal = legal.any(dim=1, keepdim=True)
    legal = torch.where(has_legal, legal, torch.ones_like(legal))
    return logits.masked_fill(~legal, torch.finfo(logits.dtype).min)


def _mask_small_choice_logits(logits: torch.Tensor, eligible_n: torch.Tensor) -> torch.Tensor:
    n = eligible_n.to(device=logits.device, dtype=torch.long).clamp(min=1, max=logits.shape[1])
    idx = torch.arange(logits.shape[1], device=logits.device).unsqueeze(0)
    legal = idx < n.unsqueeze(1)
    return logits.masked_fill(~legal, torch.finfo(logits.dtype).min)


def _country_mixture_loss(
    outputs: dict[str, torch.Tensor],
    country_ops_target: torch.Tensor,
    mask: torch.Tensor,
) -> tuple[torch.Tensor, float]:
    if not mask.any():
        return _zero(country_ops_target.device), float("nan")
    ops_t = country_ops_target[mask]
    ops_prob = ops_t / ops_t.sum(dim=1, keepdim=True).clamp_min(1.0)
    mixing = torch.softmax(outputs["strategy_logits"][mask], dim=1)
    strategy_probs = torch.softmax(outputs["country_strategy_logits"][mask], dim=2)
    mixture_probs = (mixing.unsqueeze(2) * strategy_probs).sum(dim=1)
    loss = -(ops_prob * torch.log(mixture_probs + 1e-8)).sum(dim=1).mean()
    top1 = (
        outputs["country_logits"][mask].argmax(dim=1) == country_ops_target[mask].argmax(dim=1)
    ).float().mean().item()
    return loss, top1


def _subframe_loss(
    outputs: dict[str, torch.Tensor],
    batch: dict[str, torch.Tensor],
    target_head: torch.Tensor,
    head_weights: torch.Tensor,
    label_smoothing: float,
) -> torch.Tensor:
    device = target_head.device
    total = _zero(device)

    small_mask = target_head == TARGET_HEAD_SMALL_CHOICE
    if small_mask.any():
        logits = _mask_small_choice_logits(
            outputs["small_choice_logits"][small_mask],
            batch["eligible_n"][small_mask],
        )
        target = batch["chosen_option_index"][small_mask].long().clamp(0, logits.shape[1] - 1)
        loss = F.cross_entropy(logits, target, reduction="none", label_smoothing=label_smoothing)
        total = total + head_weights[TARGET_HEAD_SMALL_CHOICE] * loss.mean()

    country_mask = target_head == TARGET_HEAD_COUNTRY_PICK
    if country_mask.any():
        logits = _mask_logits_with_fallback(
            outputs["country_pick_logits"][country_mask],
            batch["eligible_countries_mask"][country_mask],
        )
        target = batch["chosen_country"][country_mask].long().clamp(0, logits.shape[1] - 1)
        loss = F.cross_entropy(logits, target, reduction="none", label_smoothing=label_smoothing)
        total = total + head_weights[TARGET_HEAD_COUNTRY_PICK] * loss.mean()

    card_mask = target_head == TARGET_HEAD_CARD_PICK
    if card_mask.any():
        logits = _mask_logits_with_fallback(
            outputs["card_logits"][card_mask],
            batch["eligible_cards_mask"][card_mask],
        )
        target = (batch["chosen_card"][card_mask].long() - 1).clamp(0, logits.shape[1] - 1)
        loss = F.cross_entropy(logits, target, reduction="none", label_smoothing=label_smoothing)
        total = total + head_weights[TARGET_HEAD_CARD_PICK] * loss.mean()

    headline_mask = target_head == TARGET_HEAD_HEADLINE
    if headline_mask.any():
        card_logits = _mask_logits_with_fallback(
            outputs["card_logits"][headline_mask],
            batch["eligible_cards_mask"][headline_mask],
        )
        card_target = (batch["chosen_card"][headline_mask].long() - 1).clamp(
            0,
            card_logits.shape[1] - 1,
        )
        card_loss = F.cross_entropy(
            card_logits,
            card_target,
            reduction="none",
            label_smoothing=label_smoothing,
        ).mean()
        event_target = torch.full(
            (int(headline_mask.sum().item()),),
            4,
            device=device,
            dtype=torch.long,
        )
        mode_loss = F.cross_entropy(
            outputs["mode_logits"][headline_mask],
            event_target,
            reduction="none",
            label_smoothing=label_smoothing,
        ).mean()
        total = total + head_weights[TARGET_HEAD_HEADLINE] * (card_loss + mode_loss)

    return total


def run_epoch(
    model: TSCountryAttnSubframeModel,
    loader: DataLoader,
    optimizer: torch.optim.Optimizer | None,
    scheduler: torch.optim.lr_scheduler.LRScheduler | None,
    device: torch.device,
    head_weights: torch.Tensor,
    args: argparse.Namespace,
    epoch_label: str,
) -> dict[str, float]:
    is_train = optimizer is not None
    model.train(is_train)
    totals = {
        "loss": 0.0,
        "ar_loss": 0.0,
        "sub_loss": 0.0,
        "value_loss": 0.0,
        "country_top1": 0.0,
    }
    card_correct = 0
    card_count = 0
    batches = 0
    t0 = time.time()
    autocast_enabled = not args.no_bf16 and device.type == "cuda"

    ctx = torch.enable_grad() if is_train else torch.no_grad()
    with ctx:
        for batch_idx, raw_batch in enumerate(loader):
            batch = {
                k: v.to(device, non_blocking=True) if torch.is_tensor(v) else v
                for k, v in raw_batch.items()
            }
            influence = batch["influence"]
            cards = batch["cards"].float()
            scalars = batch["scalars"]
            card_target = batch["card_target"].long()
            mode_target = batch["mode_target"].long()
            country_ops_target = batch["country_ops_target"]
            value_target = batch["value_target"]
            target_head = batch["target_head"].long()

            with torch.autocast(
                device_type=device.type,
                dtype=torch.bfloat16,
                enabled=autocast_enabled,
            ):
                outputs = model(influence, cards, scalars)
                ar_mask = target_head == TARGET_HEAD_AR
                card_loss = _zero(device)
                mode_loss = _zero(device)
                country_loss = _zero(device)
                value_loss = _zero(device)
                country_top1 = float("nan")

                if ar_mask.any():
                    card_loss = F.cross_entropy(
                        outputs["card_logits"][ar_mask],
                        card_target[ar_mask],
                        label_smoothing=args.label_smoothing,
                    )
                    mode_valid = ar_mask & (mode_target >= 0)
                    if mode_valid.any():
                        mode_loss = F.cross_entropy(
                            outputs["mode_logits"][mode_valid],
                            mode_target[mode_valid],
                            label_smoothing=args.label_smoothing,
                        )
                    country_mask = ar_mask & (country_ops_target.sum(dim=1) > 0)
                    country_loss, country_top1 = _country_mixture_loss(
                        outputs,
                        country_ops_target,
                        country_mask,
                    )
                    value_loss = F.mse_loss(outputs["value"][ar_mask], value_target[ar_mask])

                sub_loss = _subframe_loss(
                    outputs,
                    batch,
                    target_head,
                    head_weights,
                    args.label_smoothing,
                )
                ar_loss = card_loss + mode_loss + country_loss
                loss = ar_loss + sub_loss + args.value_weight * value_loss

            if is_train:
                optimizer.zero_grad(set_to_none=True)
                loss.backward()
                optimizer.step()
                if scheduler is not None:
                    scheduler.step()

            with torch.no_grad():
                if ar_mask.any():
                    preds = outputs["card_logits"][ar_mask].argmax(dim=1)
                    card_correct += int((preds == card_target[ar_mask]).sum().item())
                    card_count += int(ar_mask.sum().item())

            totals["loss"] += float(loss.item())
            totals["ar_loss"] += float(ar_loss.item())
            totals["sub_loss"] += float(sub_loss.item())
            totals["value_loss"] += float(value_loss.item())
            if country_top1 == country_top1:
                totals["country_top1"] += country_top1
            batches += 1

            if is_train and (batch_idx + 1) % args.log_interval == 0:
                elapsed = time.time() - t0
                card_top1 = card_correct / max(1, card_count)
                print(
                    f"  [{epoch_label} batch {batch_idx + 1:4d}]"
                    f" loss={loss.item():.4f}"
                    f" ar={ar_loss.item():.4f}"
                    f" sub={sub_loss.item():.4f}"
                    f" value={value_loss.item():.4f}"
                    f" card_top1={card_top1:.3f}"
                    f" elapsed={elapsed:.1f}s",
                    flush=True,
                )

    if batches == 0:
        return {}
    metrics = {k: v / batches for k, v in totals.items()}
    metrics["card_top1"] = card_correct / max(1, card_count)
    return metrics


def main() -> None:
    sys.stdout.reconfigure(line_buffering=True)
    args = parse_args()
    args.model_type = "country_attn_subframe"
    set_seed(args.seed)
    device = make_device()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "args.json").write_text(json.dumps(vars(args), indent=2, sort_keys=True))

    print(f"Device: {device}")
    print(f"Data: {args.data_dir}")
    print(f"Out: {args.out_dir}")
    if not args.no_bf16 and device.type == "cuda":
        print("bf16 autocast enabled")

    dataset = TS_SelfPlayDataset(args.data_dir)
    n_total = len(dataset)
    n_val = max(1, int(n_total * args.val_fraction))
    n_train = n_total - n_val
    generator = torch.Generator().manual_seed(args.seed)
    if not args.random_split and dataset._game_ids is not None:
        train_idx, val_idx = dataset.deterministic_split(args.val_fraction)
        train_ds = Subset(dataset, train_idx)
        val_ds = Subset(dataset, val_idx)
    else:
        train_ds, val_ds = random_split(dataset, [n_train, n_val], generator=generator)
    print(f"Dataset: {n_total:,} rows train={len(train_ds):,} val={len(val_ds):,}")
    print(f"Head weights: {dataset.head_weights.tolist()}")

    collate = TS_SelfPlayDataset.passthrough_collate
    mp_ctx = "forkserver" if args.num_workers > 0 else None
    train_loader = DataLoader(
        train_ds,
        batch_size=args.batch_size,
        shuffle=True,
        generator=generator,
        num_workers=args.num_workers,
        persistent_workers=args.num_workers > 0,
        pin_memory=args.pin_memory,
        multiprocessing_context=mp_ctx,
        collate_fn=collate,
    )
    val_loader = DataLoader(
        val_ds,
        batch_size=args.batch_size,
        shuffle=False,
        num_workers=args.num_workers,
        persistent_workers=args.num_workers > 0,
        pin_memory=args.pin_memory,
        multiprocessing_context=mp_ctx,
        collate_fn=collate,
    )

    model = TSCountryAttnSubframeModel(
        dropout=args.dropout,
        hidden_dim=args.hidden_dim,
    ).to(device)
    warmstart = args.init_from or args.warmstart
    if warmstart:
        ckpt = torch.load(warmstart, map_location=device, weights_only=False)
        state_dict = ckpt.get("model_state_dict", ckpt)
        incompatible = model.load_state_dict(state_dict, strict=False)
        print(
            f"Warm-started from {warmstart};"
            f" missing={len(incompatible.missing_keys)} unexpected={len(incompatible.unexpected_keys)}"
        )

    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=args.lr,
        weight_decay=args.weight_decay,
    )
    scheduler = torch.optim.lr_scheduler.OneCycleLR(
        optimizer,
        max_lr=args.lr,
        epochs=args.epochs,
        steps_per_epoch=max(1, len(train_loader)),
    )
    head_weights = dataset.head_weights.to(device)
    if head_weights.numel() != NUM_TARGET_HEADS:
        raise RuntimeError(f"expected {NUM_TARGET_HEADS} head weights, got {head_weights.numel()}")

    best_val_loss = float("inf")
    best_path = out_dir / "baseline_best.pt"
    for epoch in range(1, args.epochs + 1):
        print(f"\n=== Epoch {epoch}/{args.epochs} ===")
        start = time.time()
        train_metrics = run_epoch(
            model,
            train_loader,
            optimizer,
            scheduler,
            device,
            head_weights,
            args,
            f"train e{epoch}",
        )
        val_metrics = run_epoch(
            model,
            val_loader,
            None,
            None,
            device,
            head_weights,
            args,
            f"val e{epoch}",
        )
        val_loss = val_metrics.get("loss", float("inf"))
        is_best = val_loss < best_val_loss
        if is_best:
            best_val_loss = val_loss

        ckpt_payload = {
            "epoch": epoch,
            "model_state_dict": model.state_dict(),
            "optimizer_state_dict": optimizer.state_dict(),
            "scheduler_state_dict": scheduler.state_dict(),
            "train_metrics": train_metrics,
            "val_metrics": val_metrics,
            "args": vars(args),
            "seed": args.seed,
        }
        epoch_path = out_dir / f"baseline_epoch{epoch}.pt"
        torch.save(ckpt_payload, epoch_path)
        if is_best:
            torch.save(ckpt_payload, best_path)

        elapsed = time.time() - start
        print(
            f"Epoch {epoch} summary"
            f" train_loss={train_metrics.get('loss', float('nan')):.4f}"
            f" val_loss={val_loss:.4f}"
            f" val_card_top1={val_metrics.get('card_top1', float('nan')):.3f}"
            f" elapsed={elapsed:.1f}s"
            + (" [BEST]" if is_best else ""),
            flush=True,
        )

    print(f"Training complete. Best val_loss={best_val_loss:.4f} -> {best_path}")


if __name__ == "__main__":
    main()
