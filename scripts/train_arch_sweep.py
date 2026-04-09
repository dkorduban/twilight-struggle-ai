#!/usr/bin/env python3
"""Architecture sweep trainer for PPO rollout data.

Reads PPO rollout parquets directly (no BC column format needed) and trains
any model architecture registered in train_baseline.py's _MODEL_REGISTRY.

PPO rollout columns used:
  influence      (172,) float32  — [ussr_inf(86), us_inf(86)]
  cards          (448,) float32  — pre-assembled card feature tensor
  scalars        (32,)  float32  — [game(32)] (effect+region already in)
  card_id        int    — action label (1-indexed card, 0=setup/skip)
  mode_id        int    — mode label
  country_targets list[int] — country target indices
  side_int       int    — 0=USSR, 1=US
  gae_return     float  — value target (GAE return from PPO)
  iteration      int    — used as proxy game_id for train/val split
"""

import argparse
import glob
import os
import sys
import time
from pathlib import Path

import numpy as np
import polars as pl
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset

sys.path.insert(0, str(Path(__file__).parent.parent / "python"))

from tsrl.policies.model import (
    TSControlFeatGNNSideModel,
    TSCountryAttnSideModel,
)

_MODEL_REGISTRY = {
    "control_feat_gnn_side": TSControlFeatGNNSideModel,
    "country_attn_side": TSCountryAttnSideModel,
}

_SCALAR_DIM = 32   # kScalarDim in nn_features.cpp
_INF_DIM    = 172  # 86 * 2
_CARDS_DIM  = 448


class PPORolloutDataset(Dataset):
    """Dataset backed by PPO rollout parquets.

    Skips rows with card_id == 0 (setup/influence placement with no card decision).
    Train/val split by iteration (last val_frac of iterations go to val).
    """

    def __init__(
        self,
        rollout_dirs: list[str],
        split: str = "train",
        val_frac: float = 0.1,
        max_files: int | None = None,
    ):
        assert split in ("train", "val")
        files: list[str] = []
        for d in rollout_dirs:
            files.extend(sorted(glob.glob(os.path.join(d, "rollout_iter_*.parquet"))))
        if not files:
            raise FileNotFoundError(f"No rollout parquets found in {rollout_dirs}")

        # Keep only the most recent N files (highest-quality policy data)
        if max_files is not None and len(files) > max_files:
            files = files[-max_files:]
            print(f"Subsampled to {max_files} most recent files", flush=True)

        # Split by iteration (proxy game split)
        all_iters = sorted({
            int(Path(f).stem.split("_iter_")[1].split(".")[0])
            for f in files
        })
        cutoff = int(len(all_iters) * (1 - val_frac))
        train_iters = set(all_iters[:cutoff])
        val_iters = set(all_iters[cutoff:])
        keep_iters = train_iters if split == "train" else val_iters

        keep_files = [
            f for f in files
            if int(Path(f).stem.split("_iter_")[1].split(".")[0]) in keep_iters
        ]
        print(f"[{split}] {len(keep_files)} files from {len(keep_iters)} iters", flush=True)

        cols = ["influence", "cards", "scalars", "card_id", "mode_id",
                "country_targets", "side_int", "gae_return"]
        frames = []
        for f in keep_files:
            schema = pl.read_parquet_schema(f)
            available = [c for c in cols if c in schema]
            frames.append(pl.read_parquet(f, columns=available))

        df = pl.concat(frames, how="diagonal")
        # Filter setup rows
        df = df.filter(pl.col("card_id") > 0)

        N = len(df)
        print(f"[{split}] {N:,} rows after filtering", flush=True)

        self._influence = torch.from_numpy(
            np.array(df["influence"].to_list(), dtype=np.float32)
        )  # (N, 172)
        self._cards = torch.from_numpy(
            np.array(df["cards"].to_list(), dtype=np.float32)
        )  # (N, 448)
        self._scalars = torch.from_numpy(
            np.array(df["scalars"].to_list(), dtype=np.float32)
        )  # (N, 32)
        self._card_id = torch.tensor(df["card_id"].to_list(), dtype=torch.long) - 1  # 0-indexed
        self._mode_id = torch.tensor(df["mode_id"].to_list(), dtype=torch.long)
        self._side = torch.tensor(df["side_int"].to_list(), dtype=torch.long)
        self._value = torch.tensor(df["gae_return"].to_list(), dtype=torch.float32)

        # Country targets: variable-length → store as padded (N, max_k)
        ct = df["country_targets"].to_list()
        max_k = max((len(x) for x in ct), default=0)
        country_arr = np.full((N, max(max_k, 1)), -1, dtype=np.int64)
        for i, row in enumerate(ct):
            if row:
                country_arr[i, :len(row)] = row
        self._country_targets = torch.from_numpy(country_arr)

    def __len__(self):
        return len(self._influence)

    def __getitem__(self, idx):
        return {
            "influence": self._influence[idx],
            "cards": self._cards[idx],
            "scalars": self._scalars[idx],
            "side": self._side[idx],
            "card_idx": self._card_id[idx],
            "mode_idx": self._mode_id[idx],
            "country_targets": self._country_targets[idx],
            "value": self._value[idx],
        }


def compute_country_loss(logits: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
    """Cross-entropy over country targets, averaged over non-(-1) targets."""
    # logits: (B, n_countries), targets: (B, K) with -1 padding
    valid = targets >= 0  # (B, K)
    if not valid.any():
        return torch.tensor(0.0, device=logits.device)
    loss = 0.0
    count = 0
    for k in range(targets.shape[1]):
        t = targets[:, k]
        mask = t >= 0
        if mask.any():
            loss = loss + nn.functional.cross_entropy(logits[mask], t[mask], reduction="sum")
            count += mask.sum().item()
    return loss / max(count, 1)


def run_epoch(model, loader, optimizer, device, train: bool):
    model.train(train)
    total_card = total_mode = total_val = total_country = 0.0
    total_card_top1 = 0
    n = 0

    for batch in loader:
        inf = batch["influence"].to(device)
        cards = batch["cards"].to(device)
        scalars = batch["scalars"].to(device)
        side = batch["side"].to(device)
        card_idx = batch["card_idx"].to(device)
        mode_idx = batch["mode_idx"].to(device)
        country_targets = batch["country_targets"].to(device)
        value_tgt = batch["value"].to(device)

        B = inf.shape[0]
        # Models extract side from scalars[:, 10] internally; no mask args needed
        out = model(inf, cards, scalars)
        card_logits = out["card_logits"]    # (B, 110)
        mode_logits = out["mode_logits"]    # (B, 5)
        country_logits = out.get("country_logits")  # (B, 86) or None
        value_pred = out.get("value")       # (B,) or None

        card_loss = nn.functional.cross_entropy(card_logits, card_idx)
        mode_loss = nn.functional.cross_entropy(mode_logits, mode_idx)
        country_loss = (
            compute_country_loss(country_logits, country_targets)
            if country_logits is not None else torch.tensor(0.0)
        )
        val_loss = (
            nn.functional.mse_loss(value_pred.squeeze(-1), value_tgt)
            if value_pred is not None else torch.tensor(0.0)
        )
        loss = card_loss + mode_loss + country_loss + 0.5 * val_loss

        if train:
            optimizer.zero_grad()
            loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()

        total_card += card_loss.item() * B
        total_mode += mode_loss.item() * B
        total_country += country_loss.item() * B
        total_val += val_loss.item() * B
        total_card_top1 += (card_logits.argmax(1) == card_idx).sum().item()
        n += B

    return {
        "card_loss": total_card / n,
        "mode_loss": total_mode / n,
        "country_loss": total_country / n,
        "val_loss": total_val / n,
        "card_top1": total_card_top1 / n,
        "n": n,
    }


def main():
    p = argparse.ArgumentParser(description="Architecture sweep on PPO rollout data")
    p.add_argument("--rollout-dirs", nargs="+", required=True)
    p.add_argument("--out-dir", required=True)
    p.add_argument("--model-type", choices=list(_MODEL_REGISTRY), required=True)
    p.add_argument("--hidden-dim", type=int, default=256)
    p.add_argument("--epochs", type=int, default=20)
    p.add_argument("--batch-size", type=int, default=2048)
    p.add_argument("--lr", type=float, default=1e-3)
    p.add_argument("--val-frac", type=float, default=0.1)
    p.add_argument("--max-files", type=int, default=None,
                   help="Use only the N most recent rollout files (avoids OOM on large datasets)")
    p.add_argument("--device", default="cuda")
    p.add_argument("--seed", type=int, default=42)
    args = p.parse_args()

    torch.manual_seed(args.seed)
    device = torch.device(args.device if torch.cuda.is_available() else "cpu")
    os.makedirs(args.out_dir, exist_ok=True)

    print(f"Loading datasets from {args.rollout_dirs} ...", flush=True)
    train_ds = PPORolloutDataset(args.rollout_dirs, split="train", val_frac=args.val_frac,
                                max_files=args.max_files)
    val_ds = PPORolloutDataset(args.rollout_dirs, split="val", val_frac=args.val_frac,
                               max_files=args.max_files)

    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True,
                              num_workers=2, pin_memory=True)
    val_loader = DataLoader(val_ds, batch_size=args.batch_size, shuffle=False,
                            num_workers=2, pin_memory=True)

    model_cls = _MODEL_REGISTRY[args.model_type]
    model = model_cls(hidden_dim=args.hidden_dim).to(device)
    n_params = sum(p.numel() for p in model.parameters())
    print(f"Model: {args.model_type}, params={n_params:,}", flush=True)

    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)

    best_val_top1 = 0.0
    log_path = os.path.join(args.out_dir, "sweep_log.txt")
    with open(log_path, "w") as f:
        f.write(f"model={args.model_type} hidden={args.hidden_dim} lr={args.lr}\n")
        f.write("epoch\ttrain_card_top1\tval_card_top1\tval_card_loss\tval_val_loss\n")

    for epoch in range(1, args.epochs + 1):
        t0 = time.time()
        train_m = run_epoch(model, train_loader, optimizer, device, train=True)
        val_m = run_epoch(model, val_loader, optimizer, device, train=False)
        scheduler.step()

        if val_m["card_top1"] > best_val_top1:
            best_val_top1 = val_m["card_top1"]
            torch.save({"model_state_dict": model.state_dict(), "args": vars(args),
                        "epoch": epoch, "val_card_top1": best_val_top1},
                       os.path.join(args.out_dir, "best.pt"))

        print(
            f"[epoch {epoch:02d}/{args.epochs}] "
            f"train_top1={train_m['card_top1']:.3f} "
            f"val_top1={val_m['card_top1']:.3f} "
            f"val_card_loss={val_m['card_loss']:.4f} "
            f"val_val_loss={val_m['val_loss']:.4f} "
            f"t={time.time()-t0:.1f}s",
            flush=True,
        )
        with open(log_path, "a") as f:
            f.write(f"{epoch}\t{train_m['card_top1']:.4f}\t{val_m['card_top1']:.4f}\t"
                    f"{val_m['card_loss']:.4f}\t{val_m['val_loss']:.4f}\n")

    print(f"\nBest val card_top1: {best_val_top1:.4f}", flush=True)
    print(f"Checkpoint: {args.out_dir}/best.pt", flush=True)


if __name__ == "__main__":
    main()
