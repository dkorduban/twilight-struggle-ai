#!/usr/bin/env python3
"""AWR (Advantage-Weighted Regression) training for fast architecture comparison.

Trains any MODEL_REGISTRY architecture on frozen rollout parquet data with
advantage-weighted policy loss + value regression. Much faster than PPO
(~2 min per architecture) with comparable signal for ranking architectures.

Usage:
    # Quick architecture comparison
    python scripts/train_awr.py \
        --data data/awr_eval/awr_initial.parquet \
        --model-type country_attn_side \
        --checkpoint data/checkpoints/ppo_v309_sc_league/ppo_best.pt \
        --epochs 5 --lr 3e-4

    # Compare two architectures
    python scripts/train_awr.py --data data/awr_eval/awr_initial.parquet \
        --model-type country_attn_side --tag baseline
    python scripts/train_awr.py --data data/awr_eval/awr_initial.parquet \
        --model-type country_attn_side_policy --tag side_policy
"""

import argparse
import sys
import time
from pathlib import Path

import numpy as np
import pyarrow.parquet as pq
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset, random_split

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "python"))

from tsrl.constants import MODEL_REGISTRY

# Match model.py constants
NUM_PLAYABLE_CARDS = 111
NUM_MODES = 6
NUM_COUNTRIES = 86


# ---------------------------------------------------------------------------
# Dataset
# ---------------------------------------------------------------------------

class AWRDataset(Dataset):
    """Parquet-backed dataset for AWR training."""

    def __init__(self, parquet_path: str, max_rows: int = 0) -> None:
        t = pq.read_table(parquet_path)
        if max_rows > 0 and len(t) > max_rows:
            indices = np.random.choice(len(t), max_rows, replace=False)
            t = t.take(indices)

        N = len(t)
        print(f"  Loaded {N:,} rows from {parquet_path}")

        # Features: convert fixed-size list columns to contiguous float32
        self.influence = torch.from_numpy(
            np.stack(t.column("influence").to_pylist()).astype(np.float32)
        )
        self.cards = torch.from_numpy(
            np.stack(t.column("cards").to_pylist()).astype(np.float32)
        )
        self.scalars = torch.from_numpy(
            np.stack(t.column("scalars").to_pylist()).astype(np.float32)
        )

        # Masks
        self.card_mask = torch.from_numpy(
            np.stack(t.column("card_mask").to_pylist()).astype(bool)
        )
        self.mode_mask = torch.from_numpy(
            np.stack(t.column("mode_mask").to_pylist()).astype(bool)
        )
        self.country_mask = torch.from_numpy(
            np.stack(t.column("country_mask").to_pylist()).astype(bool)
        )

        # Targets
        self.card_idx = torch.from_numpy(t.column("card_idx").to_numpy().astype(np.int64))
        self.mode_idx = torch.from_numpy(t.column("mode_idx").to_numpy().astype(np.int64))

        # Country targets: variable-length, store as padded tensor + length
        country_lists = t.column("country_targets").to_pylist()
        max_targets = max(len(ct) for ct in country_lists) if country_lists else 1
        max_targets = max(max_targets, 1)
        ct_padded = np.zeros((N, max_targets), dtype=np.int64)
        ct_lengths = np.zeros(N, dtype=np.int64)
        for i, ct in enumerate(country_lists):
            ct_lengths[i] = len(ct)
            for j, c in enumerate(ct):
                ct_padded[i, j] = c
        self.country_targets = torch.from_numpy(ct_padded)
        self.country_lengths = torch.from_numpy(ct_lengths)

        # Values and advantages
        advantage_raw = t.column("advantage").to_numpy().astype(np.float32)

        # Per-model advantage normalization: normalize within each model's data
        # so that weaker models (with noisier value heads) don't dominate the weights
        if "model_name" in t.schema.names:
            model_names = t.column("model_name").to_pylist()
            unique_models = set(model_names)
            model_names_arr = np.array(model_names)
            advantage_normed = advantage_raw.copy()
            for m in unique_models:
                mask = model_names_arr == m
                vals = advantage_raw[mask]
                mu, sigma = vals.mean(), vals.std()
                advantage_normed[mask] = (vals - mu) / (sigma + 1e-8)
            advantage_raw = advantage_normed
            print(f"  Per-model advantage normalization: {len(unique_models)} models")

        self.advantage = torch.from_numpy(advantage_raw)
        self.returns = torch.from_numpy(t.column("returns").to_numpy().astype(np.float32))
        self.value = torch.from_numpy(t.column("value").to_numpy().astype(np.float32))
        self.side_int = torch.from_numpy(t.column("side_int").to_numpy().astype(np.int64))

        # Metadata for stratified analysis
        self.turn = torch.from_numpy(t.column("turn").to_numpy().astype(np.int64))

    def __len__(self) -> int:
        return len(self.card_idx)

    def __getitem__(self, idx: int) -> dict:
        return {
            "influence": self.influence[idx],
            "cards": self.cards[idx],
            "scalars": self.scalars[idx],
            "card_mask": self.card_mask[idx],
            "mode_mask": self.mode_mask[idx],
            "country_mask": self.country_mask[idx],
            "card_idx": self.card_idx[idx],
            "mode_idx": self.mode_idx[idx],
            "country_targets": self.country_targets[idx],
            "country_lengths": self.country_lengths[idx],
            "advantage": self.advantage[idx],
            "returns": self.returns[idx],
            "side_int": self.side_int[idx],
            "turn": self.turn[idx],
        }


# ---------------------------------------------------------------------------
# AWR Loss
# ---------------------------------------------------------------------------

def compute_masked_log_prob(
    card_logits: torch.Tensor,   # (B, 111)
    mode_logits: torch.Tensor,   # (B, 6)
    country_logits: torch.Tensor,  # (B, 86) — already probabilities from mixture
    card_mask: torch.Tensor,     # (B, 111)
    mode_mask: torch.Tensor,     # (B, 6)
    country_mask: torch.Tensor,  # (B, 86)
    card_idx: torch.Tensor,      # (B,)
    mode_idx: torch.Tensor,      # (B,)
    country_targets: torch.Tensor,  # (B, max_T)
    country_lengths: torch.Tensor,  # (B,)
) -> torch.Tensor:
    """Compute log probability of the taken action under masked policy."""
    B = card_logits.shape[0]

    # Card log-prob
    masked_card = card_logits.clone()
    masked_card[~card_mask] = -1e9
    card_lp = F.log_softmax(masked_card, dim=-1)
    card_log_prob = card_lp.gather(1, card_idx.unsqueeze(1)).squeeze(1)

    # Mode log-prob (handle 5-mode vs 6-mode compat)
    M = mode_logits.shape[1]
    if mode_mask.shape[1] < M:
        pad = torch.zeros(B, M - mode_mask.shape[1], dtype=torch.bool, device=mode_mask.device)
        mode_mask = torch.cat([mode_mask, pad], dim=1)
    masked_mode = mode_logits.clone()
    masked_mode[~mode_mask] = -1e9
    mode_lp = F.log_softmax(masked_mode, dim=-1)
    mode_log_prob = mode_lp.gather(1, mode_idx.unsqueeze(1)).squeeze(1)

    # Country log-prob (country_logits are already probabilities from mixture model)
    # Apply mask and renormalize
    masked_country = country_logits.clone()
    masked_country[~country_mask] = 0.0
    masked_country = masked_country / (masked_country.sum(dim=-1, keepdim=True) + 1e-10)
    country_lp = torch.log(masked_country + 1e-10)

    # Average log-probs over country targets (macro-action weighting)
    # Dividing by K prevents multi-point placements from dominating the loss
    max_T = country_targets.shape[1]
    country_log_prob = torch.zeros(B, device=card_logits.device)
    for t in range(max_T):
        active = country_lengths > t
        if not active.any():
            break
        targets_t = country_targets[:, t].clamp(0, NUM_COUNTRIES - 1)
        lp_t = country_lp.gather(1, targets_t.unsqueeze(1)).squeeze(1)
        country_log_prob = country_log_prob + lp_t * active.float()
    country_log_prob = country_log_prob / country_lengths.clamp(min=1).float()

    return card_log_prob + mode_log_prob + country_log_prob


def awr_loss(
    log_probs: torch.Tensor,
    advantages: torch.Tensor,
    tau: float = 1.0,
    clip_weight: float = 20.0,
) -> tuple[torch.Tensor, torch.Tensor]:
    """AWR policy loss: advantage-weighted negative log-likelihood.

    Returns (loss, mean_weight) for logging.
    """
    # Exponential advantage weighting
    weights = torch.exp(advantages / tau)
    weights = weights.clamp(max=clip_weight)
    weights = weights / (weights.mean() + 1e-8)  # normalize

    loss = -(weights * log_probs).mean()
    return loss, weights.mean()


# ---------------------------------------------------------------------------
# Training loop
# ---------------------------------------------------------------------------

def train_epoch(
    model: nn.Module,
    loader: DataLoader,
    optimizer: torch.optim.Optimizer,
    device: str,
    tau: float = 1.0,
    vf_coef: float = 0.5,
    crr_filter: bool = False,
) -> dict[str, float]:
    """One epoch of AWR training. Returns metrics dict."""
    model.train()
    total_policy_loss = 0.0
    total_value_loss = 0.0
    total_card_correct = 0
    total_mode_correct = 0
    total_weighted_card_correct = 0.0
    total_weight = 0.0
    n_batches = 0
    n_samples = 0

    for batch in loader:
        inf = batch["influence"].to(device)
        cards = batch["cards"].to(device)
        scalars = batch["scalars"].to(device)
        card_mask = batch["card_mask"].to(device)
        mode_mask = batch["mode_mask"].to(device)
        country_mask = batch["country_mask"].to(device)
        card_idx = batch["card_idx"].to(device)
        mode_idx = batch["mode_idx"].to(device)
        country_targets = batch["country_targets"].to(device)
        country_lengths = batch["country_lengths"].to(device)
        advantages = batch["advantage"].to(device)
        returns = batch["returns"].to(device)

        # CRR-lite: filter to positive-advantage examples only
        if crr_filter:
            pos_mask = advantages > 0
            if pos_mask.sum() < 2:
                continue
            inf = inf[pos_mask]
            cards = cards[pos_mask]
            scalars = scalars[pos_mask]
            card_mask = card_mask[pos_mask]
            mode_mask = mode_mask[pos_mask]
            country_mask = country_mask[pos_mask]
            card_idx = card_idx[pos_mask]
            mode_idx = mode_idx[pos_mask]
            country_targets = country_targets[pos_mask]
            country_lengths = country_lengths[pos_mask]
            advantages = advantages[pos_mask]
            returns = returns[pos_mask]

        outputs = model(inf, cards, scalars)
        card_logits = outputs["card_logits"]
        mode_logits = outputs["mode_logits"]
        country_logits = outputs.get("country_logits", torch.zeros(inf.shape[0], NUM_COUNTRIES, device=device))
        value = outputs["value"].squeeze(-1)

        # AWR policy loss
        log_probs = compute_masked_log_prob(
            card_logits, mode_logits, country_logits,
            card_mask, mode_mask, country_mask,
            card_idx, mode_idx, country_targets, country_lengths,
        )
        policy_loss, mean_weight = awr_loss(log_probs, advantages, tau=tau)

        # Value loss on GAE returns
        value_loss = F.mse_loss(value, returns)

        loss = policy_loss + vf_coef * value_loss

        optimizer.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 0.5)
        optimizer.step()

        # Accuracy metrics
        B = card_logits.shape[0]
        masked_card = card_logits.clone()
        masked_card[~card_mask] = -1e9
        card_pred = masked_card.argmax(dim=-1)
        card_correct = (card_pred == card_idx).sum().item()

        _mm = mode_mask
        if _mm.shape[1] < mode_logits.shape[1]:
            _mm = torch.cat([_mm, torch.zeros(B, mode_logits.shape[1] - _mm.shape[1], dtype=torch.bool, device=_mm.device)], dim=1)
        masked_mode = mode_logits.clone()
        masked_mode[~_mm] = -1e9
        mode_pred = masked_mode.argmax(dim=-1)
        mode_correct = (mode_pred == mode_idx).sum().item()

        # Advantage-weighted accuracy (how well does model predict GOOD actions?)
        pos_adv = advantages > 0
        if pos_adv.any():
            pos_card_correct = ((card_pred == card_idx) & pos_adv).float().sum().item()
            total_weighted_card_correct += pos_card_correct
            total_weight += pos_adv.float().sum().item()

        total_policy_loss += policy_loss.item() * B
        total_value_loss += value_loss.item() * B
        total_card_correct += card_correct
        total_mode_correct += mode_correct
        n_batches += 1
        n_samples += B

    return {
        "policy_loss": total_policy_loss / n_samples,
        "value_loss": total_value_loss / n_samples,
        "card_acc": total_card_correct / n_samples,
        "mode_acc": total_mode_correct / n_samples,
        "adv_card_acc": total_weighted_card_correct / max(total_weight, 1),
    }


@torch.no_grad()
def eval_epoch(
    model: nn.Module,
    loader: DataLoader,
    device: str,
    tau: float = 1.0,
) -> dict[str, float]:
    """Evaluate AWR metrics without gradient updates."""
    model.eval()
    total_policy_loss = 0.0
    total_value_loss = 0.0
    total_card_correct = 0
    total_mode_correct = 0
    total_weighted_card_correct = 0.0
    total_weight = 0.0
    n_samples = 0

    # Per-turn-bucket metrics
    buckets = {"early": (1, 3), "mid": (4, 7), "late": (8, 10)}
    bucket_correct = {k: 0 for k in buckets}
    bucket_total = {k: 0 for k in buckets}

    for batch in loader:
        inf = batch["influence"].to(device)
        cards = batch["cards"].to(device)
        scalars = batch["scalars"].to(device)
        card_mask = batch["card_mask"].to(device)
        mode_mask = batch["mode_mask"].to(device)
        country_mask = batch["country_mask"].to(device)
        card_idx = batch["card_idx"].to(device)
        mode_idx = batch["mode_idx"].to(device)
        country_targets = batch["country_targets"].to(device)
        country_lengths = batch["country_lengths"].to(device)
        advantages = batch["advantage"].to(device)
        returns = batch["returns"].to(device)
        turns = batch["turn"]

        outputs = model(inf, cards, scalars)
        card_logits = outputs["card_logits"]
        mode_logits = outputs["mode_logits"]
        country_logits = outputs.get("country_logits", torch.zeros(inf.shape[0], NUM_COUNTRIES, device=device))
        value = outputs["value"].squeeze(-1)

        log_probs = compute_masked_log_prob(
            card_logits, mode_logits, country_logits,
            card_mask, mode_mask, country_mask,
            card_idx, mode_idx, country_targets, country_lengths,
        )
        policy_loss, _ = awr_loss(log_probs, advantages, tau=tau)
        value_loss = F.mse_loss(value, returns)

        B = card_logits.shape[0]
        masked_card = card_logits.clone()
        masked_card[~card_mask] = -1e9
        card_pred = masked_card.argmax(dim=-1)
        card_correct = (card_pred == card_idx)

        _mm = mode_mask
        if _mm.shape[1] < mode_logits.shape[1]:
            _mm = torch.cat([_mm, torch.zeros(B, mode_logits.shape[1] - _mm.shape[1], dtype=torch.bool, device=_mm.device)], dim=1)
        masked_mode = mode_logits.clone()
        masked_mode[~_mm] = -1e9
        mode_pred = masked_mode.argmax(dim=-1)

        pos_adv = advantages > 0
        if pos_adv.any():
            total_weighted_card_correct += (card_correct & pos_adv).float().sum().item()
            total_weight += pos_adv.float().sum().item()

        total_policy_loss += policy_loss.item() * B
        total_value_loss += value_loss.item() * B
        total_card_correct += card_correct.sum().item()
        total_mode_correct += (mode_pred == mode_idx).sum().item()
        n_samples += B

        # Per-turn accuracy
        for bname, (t_lo, t_hi) in buckets.items():
            mask = (turns >= t_lo) & (turns <= t_hi)
            if mask.any():
                bucket_correct[bname] += card_correct[mask].sum().item()
                bucket_total[bname] += mask.sum().item()

    metrics = {
        "val_policy_loss": total_policy_loss / n_samples,
        "val_value_loss": total_value_loss / n_samples,
        "val_card_acc": total_card_correct / n_samples,
        "val_mode_acc": total_mode_correct / n_samples,
        "val_adv_card_acc": total_weighted_card_correct / max(total_weight, 1),
    }
    for bname in buckets:
        if bucket_total[bname] > 0:
            metrics[f"val_card_acc_{bname}"] = bucket_correct[bname] / bucket_total[bname]
    return metrics


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="AWR architecture evaluation")
    parser.add_argument("--data", required=True, help="AWR parquet data path")
    parser.add_argument("--model-type", default="country_attn_side", help="Model type from MODEL_REGISTRY")
    parser.add_argument("--checkpoint", default=None, help="Warm-start checkpoint (optional)")
    parser.add_argument("--hidden-dim", type=int, default=256, help="Hidden dimension")
    parser.add_argument("--epochs", type=int, default=5, help="Training epochs")
    parser.add_argument("--lr", type=float, default=3e-4, help="Learning rate")
    parser.add_argument("--batch-size", type=int, default=2048, help="Batch size")
    parser.add_argument("--tau", type=float, default=1.0, help="AWR temperature (lower = more aggressive weighting)")
    parser.add_argument("--vf-coef", type=float, default=0.5, help="Value function loss coefficient")
    parser.add_argument("--val-frac", type=float, default=0.1, help="Validation fraction")
    parser.add_argument("--max-rows", type=int, default=0, help="Max training rows (0=all)")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--device", default="cuda", help="Device")
    parser.add_argument("--tag", default=None, help="Experiment tag for logging")
    parser.add_argument("--out-dir", default=None, help="Save checkpoint to this directory")
    parser.add_argument("--wandb", action="store_true", help="Log to W&B")
    parser.add_argument("--wandb-project", default="twilight-struggle-ai", help="W&B project")
    parser.add_argument("--crr-filter", action="store_true",
                        help="CRR-lite: train only on positive-advantage examples")
    args = parser.parse_args()

    torch.manual_seed(args.seed)
    np.random.seed(args.seed)

    device = args.device
    if device == "cuda" and not torch.cuda.is_available():
        print("CUDA not available, using CPU")
        device = "cpu"

    tag = args.tag or f"{args.model_type}_h{args.hidden_dim}"
    print(f"=== AWR Eval: {tag} ===")
    print(f"  model: {args.model_type}, hidden_dim={args.hidden_dim}")
    print(f"  data: {args.data}")
    print(f"  epochs: {args.epochs}, lr: {args.lr}, tau: {args.tau}")
    print()

    # Load data
    dataset = AWRDataset(args.data, max_rows=args.max_rows)
    val_size = int(len(dataset) * args.val_frac)
    train_size = len(dataset) - val_size
    train_ds, val_ds = random_split(dataset, [train_size, val_size],
                                    generator=torch.Generator().manual_seed(args.seed))

    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True,
                              num_workers=0, pin_memory=(device == "cuda"))
    val_loader = DataLoader(val_ds, batch_size=args.batch_size, shuffle=False,
                            num_workers=0, pin_memory=(device == "cuda"))

    print(f"  train: {train_size:,} rows, val: {val_size:,} rows")

    # Create model
    cls = MODEL_REGISTRY[args.model_type]
    model = cls(hidden_dim=args.hidden_dim)

    # Warm-start from checkpoint if provided
    if args.checkpoint:
        ckpt = torch.load(args.checkpoint, map_location="cpu", weights_only=True)
        sd = ckpt.get("model_state_dict", ckpt)
        missing, unexpected = model.load_state_dict(sd, strict=False)
        if missing:
            print(f"  warm-start: {len(missing)} missing keys (expected for arch changes)")
        # Init per-side heads if applicable
        if hasattr(model, "_init_from_shared"):
            model._init_from_shared()
            print("  initialized per-side heads from shared")

    model = model.to(device)
    total_params = sum(p.numel() for p in model.parameters())
    print(f"  params: {total_params:,}")

    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=1e-4)

    # W&B
    wandb_run = None
    if args.wandb:
        try:
            import wandb
            wandb_run = wandb.init(
                project=args.wandb_project,
                name=f"awr_{tag}",
                config=vars(args),
            )
        except Exception as e:
            print(f"  W&B init failed: {e}")

    # Training loop
    t0 = time.time()
    best_val_loss = float("inf")
    best_metrics = {}

    for epoch in range(args.epochs):
        t_ep = time.time()
        train_metrics = train_epoch(model, train_loader, optimizer, device,
                                    tau=args.tau, vf_coef=args.vf_coef,
                                    crr_filter=args.crr_filter)
        val_metrics = eval_epoch(model, val_loader, device, tau=args.tau)

        elapsed = time.time() - t_ep
        combined = {**train_metrics, **val_metrics}

        print(f"  epoch {epoch+1}/{args.epochs}: "
              f"pl={train_metrics['policy_loss']:.4f} vl={train_metrics['value_loss']:.4f} "
              f"card={train_metrics['card_acc']:.3f} mode={train_metrics['mode_acc']:.3f} "
              f"adv_card={train_metrics['adv_card_acc']:.3f} | "
              f"val_pl={val_metrics['val_policy_loss']:.4f} val_card={val_metrics['val_card_acc']:.3f} "
              f"val_adv={val_metrics['val_adv_card_acc']:.3f} "
              f"({elapsed:.1f}s)")

        if wandb_run:
            wandb_run.log({f"awr/{k}": v for k, v in combined.items()}, step=epoch)

        if val_metrics["val_policy_loss"] < best_val_loss:
            best_val_loss = val_metrics["val_policy_loss"]
            best_metrics = combined.copy()
            best_metrics["best_epoch"] = epoch + 1

            if args.out_dir:
                out_path = Path(args.out_dir) / "awr_best.pt"
                out_path.parent.mkdir(parents=True, exist_ok=True)
                torch.save({
                    "model_state_dict": model.state_dict(),
                    "model_type": args.model_type,
                    "args": vars(args),
                    "metrics": best_metrics,
                }, out_path)

    total_time = time.time() - t0

    # Summary
    print(f"\n{'='*60}")
    print(f"AWR Results: {tag}")
    print(f"{'='*60}")
    print(f"  model: {args.model_type} ({total_params:,} params)")
    print(f"  best epoch: {best_metrics.get('best_epoch', '?')}")
    print(f"  train card_acc: {best_metrics.get('card_acc', 0):.4f}")
    print(f"  train adv_card_acc: {best_metrics.get('adv_card_acc', 0):.4f}")
    print(f"  val card_acc: {best_metrics.get('val_card_acc', 0):.4f}")
    print(f"  val adv_card_acc: {best_metrics.get('val_adv_card_acc', 0):.4f}")
    print(f"  val policy_loss: {best_metrics.get('val_policy_loss', 0):.4f}")
    print(f"  val value_loss: {best_metrics.get('val_value_loss', 0):.4f}")
    for bname in ["early", "mid", "late"]:
        key = f"val_card_acc_{bname}"
        if key in best_metrics:
            print(f"  val card_acc_{bname}: {best_metrics[key]:.4f}")
    print(f"  total time: {total_time:.1f}s ({total_time/60:.1f} min)")
    print(f"{'='*60}")

    if wandb_run:
        wandb_run.finish()


if __name__ == "__main__":
    main()
