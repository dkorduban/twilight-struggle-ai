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
    value_loss   = MSELoss(value_pred, value_target)  # target = winner_side or
                                                     #   final_vp/20
                                                     #   (defcon1/europe_control
                                                     #    always use winner_side)
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

# Make the script runnable both as a standalone file and as a module.
import sys
import time

# W&B is optional: import it lazily so the script still works if it's not installed.
try:
    import wandb as _wandb_module

    _WANDB_AVAILABLE = True
except ImportError:
    _wandb_module = None  # type: ignore[assignment]
    _WANDB_AVAILABLE = False

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, random_split

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "python"))

from tsrl.policies.dataset import TS_SelfPlayDataset
from tsrl.policies.model import (
    TSBaselineModel,
    TSCardEmbedModel,
    TSCountryAttnModel,
    TSCountryEmbedModel,
    TSFullEmbedModel,
)

# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Train the TSBaselineModel on self-play Parquet data.")
    p.add_argument("--data-dir", required=True, help="Directory with *.parquet files")
    p.add_argument("--out-dir", default="checkpoints", help="Directory for checkpoint files")
    p.add_argument("--epochs", type=int, default=20)
    p.add_argument("--batch-size", type=int, default=256)
    p.add_argument("--lr", type=float, default=3e-4)
    p.add_argument(
        "--weight-decay",
        type=float,
        default=0.0,
        help="L2 weight decay for AdamW (default 0 = plain Adam)",
    )
    p.add_argument(
        "--label-smoothing",
        type=float,
        default=0.0,
        help="Label smoothing epsilon for card/mode CE losses (default 0)",
    )
    p.add_argument(
        "--dropout",
        type=float,
        default=0.1,
        help="Dropout probability in trunk (default 0.1)",
    )
    p.add_argument(
        "--hidden-dim",
        type=int,
        default=256,
        help="Trunk hidden dimension (default 256)",
    )
    p.add_argument(
        "--one-cycle",
        action="store_true",
        help="Use OneCycleLR schedule (linear warmup + cosine decay)",
    )
    p.add_argument(
        "--compile",
        action="store_true",
        help="torch.compile the model for faster training (PyTorch 2+)",
    )
    p.add_argument(
        "--amp",
        action="store_true",
        help="Use automatic mixed precision (float16) for faster GPU training",
    )
    p.add_argument(
        "--resume",
        action="store_true",
        help="Resume from latest checkpoint in --out-dir",
    )
    p.add_argument(
        "--init-from",
        default=None,
        help="Warm-start from a checkpoint by loading model weights only.",
    )
    p.add_argument(
        "--patience",
        type=int,
        default=None,
        help="Early stopping: stop if val_loss hasn't improved for N epochs (0 = disabled)",
    )
    p.add_argument(
        "--advantage-weight",
        type=float,
        default=0.0,
        help=(
            "Scale policy losses by (1 + alpha * advantage) where advantage = "
            "value_target - value_pred. 0 = disabled (pure BC). "
            "0.5-1.0 = moderate advantage weighting. Reinforces surprising wins, "
            "downweights predicted losses."
        ),
    )
    p.add_argument("--seed", type=int, default=42)
    p.add_argument(
        "--no-wandb",
        action="store_true",
        help=(
            "Disable Weights & Biases logging even if .wandb-api-key.txt is present. "
            "W&B is auto-enabled when the key file exists and wandb is installed."
        ),
    )
    p.add_argument(
        "--model-type",
        default="baseline",
        choices=["baseline", "card_embed", "country_embed", "full_embed", "country_attn"],
        help="Model architecture variant (default: baseline)",
    )
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
        "--teacher-targets",
        default=None,
        help="Optional teacher target cache path (.parquet/.jsonl) or directory of cache files.",
    )
    p.add_argument(
        "--teacher-weight",
        type=float,
        default=0.5,
        help="Weight of teacher KL loss relative to behavior cloning loss (default 0.5).",
    )
    p.add_argument(
        "--teacher-value-weight",
        type=float,
        default=0.3,
        help="Weight of teacher value MSE inside the teacher loss term (default 0.3).",
    )
    p.add_argument(
        "--value-weight",
        type=float,
        default=1.0,
        help=(
            "Multiplier on value MSE loss relative to card/mode/country losses "
            "(default 1.0). NOTE: increasing this alone does not help if the "
            "value floor is caused by sparse terminal rewards. Use "
            "--value-target final_vp instead."
        ),
    )
    p.add_argument(
        "--value-target",
        default="winner_side",
        choices=["winner_side", "final_vp"],
        help=(
            "Value training target: 'winner_side' (default, {-1,0,+1} terminal "
            "outcome) or 'final_vp' (final_vp/20 clamped to [-1,1], denser "
            "reward signal)."
        ),
    )
    p.add_argument(
        "--bench-after-train",
        type=int,
        default=0,
        help=(
            "Run bench_cpp.sh with this many games after training completes and "
            "log results to W&B. 0 = disabled (default). E.g. --bench-after-train 200."
        ),
    )
    p.add_argument(
        "--bench-seed",
        type=int,
        default=9999,
        help="Seed for benchmark games (default 9999).",
    )
    return p.parse_args(argv)


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


def resolve_training_args(args: argparse.Namespace) -> argparse.Namespace:
    if args.patience is None:
        args.patience = 8 if args.init_from else 0
    return args


def make_scheduler(
    args: argparse.Namespace,
    optimizer: torch.optim.Optimizer,
    steps_per_epoch: int,
) -> tuple[torch.optim.lr_scheduler.LRScheduler | None, bool]:
    if args.one_cycle:
        return (
            torch.optim.lr_scheduler.OneCycleLR(
                optimizer,
                max_lr=args.lr,
                epochs=args.epochs,
                steps_per_epoch=steps_per_epoch,
            ),
            True,
        )
    return None, False


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
    scaler: torch.cuda.amp.GradScaler | None = None,
    advantage_weight: float = 0.0,
    teacher_weight: float = 0.0,
    teacher_value_weight: float = 0.3,
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
    mode_ce_loss_fn = nn.CrossEntropyLoss(
        ignore_index=-1, label_smoothing=label_smoothing, reduction=_reduction
    )
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
    total_teacher_kl_card = 0.0
    total_teacher_kl_mode = 0.0
    total_teacher_value_mse = 0.0
    total_teacher_rows = 0
    total_rows = 0
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
            batch_size = card_target.shape[0]
            teacher_coverage_batch = 0.0
            teacher_kl_card = torch.tensor(0.0, device=device)
            teacher_kl_mode = torch.tensor(0.0, device=device)
            teacher_value_loss = torch.tensor(0.0, device=device)

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
                    mode_loss = ((mode_loss_raw * w) * mode_mask).sum() / mode_mask.sum().clamp(
                        min=1
                    )
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
                    strategy_probs = torch.softmax(country_strategy_logits[country_ops_mask], dim=2)
                    mixture_probs = (mixing.unsqueeze(2) * strategy_probs).sum(dim=1)
                    country_loss_per = -(ops_prob * torch.log(mixture_probs + 1e-8)).sum(dim=1)
                    if use_adv:
                        w_c = w[country_ops_mask]
                        country_loss = (country_loss_per * w_c).mean()
                    else:
                        country_loss = country_loss_per.mean()
                    country_top1 = (
                        (
                            country_logits[country_ops_mask].argmax(dim=1)
                            == country_ops_target[country_ops_mask].argmax(dim=1)
                        )
                        .float()
                        .mean()
                        .item()
                    )
                else:
                    country_loss = torch.tensor(0.0, device=device)

                loss = card_loss + mode_loss + country_loss + value_weight * value_loss

                use_teacher = is_train and teacher_weight > 0.0 and "has_teacher_target" in batch
                if use_teacher:
                    has_teacher = batch["has_teacher_target"].to(device, non_blocking=True).bool()
                    teacher_rows = int(has_teacher.sum().item())
                    teacher_coverage_batch = teacher_rows / max(batch_size, 1)
                    if teacher_rows > 0:
                        t_card = batch["teacher_card_target"].to(device, non_blocking=True)
                        t_mode = batch["teacher_mode_target"].to(device, non_blocking=True)
                        t_value = batch["teacher_value_target"].to(device, non_blocking=True)
                        teacher_kl_card = F.kl_div(
                            F.log_softmax(card_logits[has_teacher], dim=1),
                            t_card[has_teacher],
                            reduction="batchmean",
                        )
                        teacher_kl_mode = F.kl_div(
                            F.log_softmax(mode_logits[has_teacher], dim=1),
                            t_mode[has_teacher],
                            reduction="batchmean",
                        )
                        teacher_value_loss = mse_loss_fn(
                            value_pred[has_teacher], t_value[has_teacher]
                        )
                        teacher_loss = (
                            teacher_kl_card
                            + teacher_kl_mode
                            + teacher_value_weight * teacher_value_loss
                        )
                        loss = loss + teacher_weight * teacher_loss
                        total_teacher_rows += teacher_rows

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
                ct = card_target.unsqueeze(1)  # (B, 1)
                ranks = (sorted_idx == ct).int().argmax(dim=1) + 1  # (B,) 1-indexed
                card_mrr_val = (1.0 / ranks.float()).mean().item()
                probs = torch.softmax(card_logits, dim=1)
                card_nll_val = torch.nn.functional.cross_entropy(
                    card_logits,
                    card_target,
                    reduction="mean",
                ).item()
                card_conf_val = probs.max(dim=1).values.mean().item()

            # --- accumulate metrics ---
            total_loss += loss.item()
            total_card_loss += card_loss.item()
            total_mode_loss += mode_loss.item()
            total_country_loss += country_loss.item()
            total_value_loss += value_loss.item()
            total_card_acc += accuracy(card_logits, card_target)
            total_card_mrr += card_mrr_val
            total_card_nll += card_nll_val
            total_card_conf += card_conf_val
            total_mode_acc += accuracy(mode_logits, mode_target, ignore_index=-1)
            total_country_ce += country_loss.item()
            total_country_top1 += country_top1
            total_value_mse += value_loss.item()
            total_teacher_kl_card += teacher_kl_card.item()
            total_teacher_kl_mode += teacher_kl_mode.item()
            total_teacher_value_mse += teacher_value_loss.item()
            total_rows += batch_size
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
                    f"  teacher_coverage={teacher_coverage_batch:.3f}"
                    f"  teacher_kl_card={teacher_kl_card.item():.4f}"
                    f"  teacher_kl_mode={teacher_kl_mode.item():.4f}"
                    f"  teacher_value_mse={teacher_value_loss.item():.4f}"
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
        "card_mrr": total_card_mrr / n_batches,
        "card_nll": total_card_nll / n_batches,
        "card_conf": total_card_conf / n_batches,
        "mode_acc": total_mode_acc / n_batches,
        "country_ce": total_country_ce / n_batches,
        "country_top1": total_country_top1 / n_batches,
        "value_mse": total_value_mse / n_batches,
        "teacher_kl_card": total_teacher_kl_card / n_batches,
        "teacher_kl_mode": total_teacher_kl_mode / n_batches,
        "teacher_value_mse": total_teacher_value_mse / n_batches,
        "teacher_coverage": (total_teacher_rows / total_rows) if total_rows > 0 else 0.0,
    }


# ---------------------------------------------------------------------------
# W&B helpers
# ---------------------------------------------------------------------------

_WANDB_API_KEY_FILE = os.path.join(os.path.dirname(__file__), "..", ".wandb-api-key.txt")
_WANDB_ENTITY = "korduban-ai"
_WANDB_PROJECT = "twilight-struggle-ai"


def _infer_run_name(args: argparse.Namespace) -> str:
    """Derive a short, human-readable run name from CLI args.

    Format: v{N}_{warm|cold}
      - version N is parsed from the last path component of --out-dir that
        looks like a version token (e.g. 'combined_v45_vsh_filtered' -> 'v45').
        Falls back to the raw basename if no vN token is found.
      - warm/cold distinguishes --init-from (warm start) from scratch (cold).
    """
    import re

    # Try to find a vN token anywhere in the out-dir path.
    version = "unknown"
    for part in reversed(os.path.normpath(args.out_dir).split(os.sep)):
        m = re.search(r"v(\d+)", part)
        if m:
            version = f"v{m.group(1)}"
            break
    else:
        # Use the last non-empty path component as a fallback.
        version = os.path.basename(os.path.normpath(args.out_dir)) or "run"

    warm_cold = "warm" if getattr(args, "init_from", None) else "cold"
    return f"{version}_{warm_cold}"


def _setup_wandb(args: argparse.Namespace) -> bool:
    """Initialise W&B if available and not disabled.

    Returns True if W&B is active for this run, False otherwise.
    """
    if getattr(args, "no_wandb", False):
        return False
    if not _WANDB_AVAILABLE:
        print("W&B not installed; skipping W&B logging.")
        return False

    key_path = os.path.abspath(_WANDB_API_KEY_FILE)
    if not os.path.exists(key_path):
        print(f"W&B key file not found at {key_path}; skipping W&B logging.")
        return False

    with open(key_path) as fh:
        api_key = fh.read().strip()
    if not api_key:
        print("W&B key file is empty; skipping W&B logging.")
        return False

    os.environ["WANDB_API_KEY"] = api_key

    run_name = _infer_run_name(args)
    _wandb_module.init(
        entity=_WANDB_ENTITY,
        project=_WANDB_PROJECT,
        name=run_name,
        config=vars(args),
        resume="allow",
    )
    print(f"W&B run initialised: {_WANDB_ENTITY}/{_WANDB_PROJECT}/{run_name}")
    return True


def _wandb_log_epoch(
    epoch: int,
    train_metrics: dict[str, float],
    val_metrics: dict[str, float],
    current_lr: float,
    is_best: bool,
) -> None:
    """Log per-epoch metrics to W&B."""
    payload: dict[str, object] = {"epoch": epoch, "lr": current_lr}
    for k, v in train_metrics.items():
        payload[f"train_{k}"] = v
    for k, v in val_metrics.items():
        payload[f"val_{k}"] = v
    if is_best:
        payload["best_val_loss"] = val_metrics.get("loss", float("nan"))
    _wandb_module.log(payload, step=epoch)


def _wandb_log_dataset_qa(data_dir: str, n_total: int, n_train: int, n_val: int) -> None:
    """Log dataset composition and QA stats to W&B config/summary."""
    import glob as _glob
    import re

    import pyarrow.parquet as pq

    files = sorted(_glob.glob(os.path.join(data_dir, "*.parquet")))
    file_stats = []
    total_rows = 0
    composition = {"anchor": 0, "vsh": 0, "selfplay": 0, "us_side": 0, "other": 0}

    for f in files:
        fname = os.path.basename(f)
        real_path = os.path.realpath(f)
        try:
            pf = pq.ParquetFile(real_path)
            nrows = pf.metadata.num_rows
            ncols = pf.metadata.num_columns
        except Exception:
            nrows = 0
            ncols = 0
        total_rows += nrows

        # Classify by filename pattern
        if "anchor" in fname or fname.startswith("heuristic_"):
            composition["anchor"] += nrows
        elif "us_vs_heuristic" in fname or "us_side" in fname:
            composition["us_side"] += nrows
        elif "selfplay" in fname or "_vs_" in fname.replace("vs_heuristic", ""):
            # selfplay files have _vs_ but not vs_heuristic
            if "vs_heuristic" in fname or "vsh" in fname:
                composition["vsh"] += nrows
            else:
                composition["selfplay"] += nrows
        elif "vsh" in fname or "vs_heuristic" in fname:
            composition["vsh"] += nrows
        else:
            composition["other"] += nrows

        # Extract version
        m = re.search(r"v(\d+)", fname)
        version = int(m.group(1)) if m else None
        file_stats.append({"file": fname, "rows": nrows, "cols": ncols, "version": version})

    # Log to wandb
    summary = {
        "dataset/total_rows": total_rows,
        "dataset/n_files": len(files),
        "dataset/n_train": n_train,
        "dataset/n_val": n_val,
    }
    for k, v in composition.items():
        summary[f"dataset/composition_{k}"] = v
        if total_rows > 0:
            summary[f"dataset/pct_{k}"] = round(100.0 * v / total_rows, 1)

    # Version range
    versions = [s["version"] for s in file_stats if s["version"] is not None]
    if versions:
        summary["dataset/min_version"] = min(versions)
        summary["dataset/max_version"] = max(versions)

    _wandb_module.config.update(summary, allow_val_change=True)
    print(f"[wandb] Dataset QA: {total_rows:,} rows, {len(files)} files, "
          f"composition: { {k: v for k, v in composition.items() if v > 0} }")


def _wandb_log_bench_results(bench_json_path: str) -> None:
    """Log benchmark results from bench_cpp.sh output JSON to W&B summary."""
    import json

    if not os.path.exists(bench_json_path):
        print(f"[wandb] Bench results not found at {bench_json_path}")
        return

    with open(bench_json_path) as f:
        results = json.load(f)

    bench_metrics = {
        "bench/win_pct": results.get("learned_win_pct", 0.0),
        "bench/learned_wins": results.get("learned_wins", 0),
        "bench/heuristic_wins": results.get("heuristic_wins", 0),
        "bench/decisive_games": results.get("decisive_games", 0),
        "bench/draws": results.get("draws", 0),
        "bench/n_games": results.get("n_games", 0),
        "bench/elapsed_seconds": results.get("elapsed_seconds", 0),
    }

    # Side-specific stats
    sides = results.get("sides", {})
    for side_name, side_data in sides.items():
        if side_data.get("games", 0) > 0:
            side_decisive = side_data.get("decisive_games", 0)
            side_wins = side_data.get("learned_wins", 0)
            bench_metrics[f"bench/{side_name}_wins"] = side_wins
            bench_metrics[f"bench/{side_name}_games"] = side_data.get("games", 0)
            if side_decisive > 0:
                bench_metrics[f"bench/{side_name}_win_pct"] = round(
                    100.0 * side_wins / side_decisive, 1
                )

    for k, v in bench_metrics.items():
        _wandb_module.summary[k] = v
    _wandb_module.log(bench_metrics)
    print(f"[wandb] Logged bench results: win_pct={results.get('learned_win_pct', 0.0)}%")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    import sys

    # Force unbuffered stdout so logs appear immediately when redirected to a file.
    sys.stdout.reconfigure(line_buffering=True)

    args = resolve_training_args(parse_args())
    set_seed(args.seed)
    device = make_device()

    wandb_active = _setup_wandb(args)

    # ---- provenance tracking ----
    try:
        from tsrl.provenance import capture_provenance, log_provenance_wandb, save_provenance

        prov = capture_provenance(
            input_files=[f"{args.data_dir}/*.parquet"],
            binaries=["build-ninja/cpp/tools/ts_collect_selfplay_rows_jsonl"],
            extra={"args": vars(args)},
        )
        save_provenance(prov, os.path.join(args.out_dir, "provenance.json"))
        if wandb_active:
            log_provenance_wandb(prov)
        print(f"[provenance] git={prov['git_sha'][:8]} dirty={prov['git_dirty']} "
              f"inputs={prov['input_file_count']} files")
    except Exception as e:
        print(f"[provenance] Skipped (non-fatal): {e}")

    print(f"Device: {device}")
    print(f"Data dir: {args.data_dir}")
    print(f"Output dir: {args.out_dir}")

    # ---- dataset ----
    full_dataset = TS_SelfPlayDataset(
        args.data_dir,
        value_target_mode=args.value_target,
        teacher_targets_path=args.teacher_targets,
    )
    n_total = len(full_dataset)
    n_val = max(1, int(n_total * args.val_fraction))
    n_train = n_total - n_val
    print(f"Dataset: {n_total} steps  (train={n_train}, val={n_val})")
    if wandb_active:
        _wandb_log_dataset_qa(args.data_dir, n_total, n_train, n_val)
    if args.teacher_targets:
        print(
            "Teacher targets:"
            f" {args.teacher_targets}  teacher_weight={args.teacher_weight}"
            f"  teacher_value_weight={args.teacher_value_weight}"
        )

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
    _MODEL_REGISTRY = {
        "baseline": TSBaselineModel,
        "card_embed": TSCardEmbedModel,
        "country_embed": TSCountryEmbedModel,
        "full_embed": TSFullEmbedModel,
        "country_attn": TSCountryAttnModel,
    }
    model = _MODEL_REGISTRY[args.model_type](
        dropout=args.dropout,
        hidden_dim=args.hidden_dim,
    ).to(device)
    n_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"Model parameters: {n_params:,}")
    if args.compile:
        model = torch.compile(model)
        print("Model compiled with torch.compile")

    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=args.lr,
        weight_decay=args.weight_decay,
    )
    scheduler, scheduler_step_per_batch = make_scheduler(args, optimizer, len(train_loader))

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
    elif args.init_from:
        print(f"Warm-starting from {args.init_from}, lr={args.lr}, scheduler={'one-cycle' if args.one_cycle else 'none'}")
        ckpt = torch.load(args.init_from, map_location=device, weights_only=False)
        model.load_state_dict(ckpt["model_state_dict"], strict=False)

    # ---- AMP scaler ----
    scaler = (
        torch.cuda.amp.GradScaler()
        if (getattr(args, "amp", False) and device.type == "cuda")
        else None
    )
    if scaler is not None:
        print("AMP enabled (float16 autocast + GradScaler)")

    # ---- early stopping state ----
    epochs_no_improve = 0

    # ---- training loop ----
    for epoch in range(start_epoch, args.epochs + 1):
        t_epoch = time.time()
        print(f"\n=== Epoch {epoch}/{args.epochs} ===")

        train_metrics = run_epoch(
            model,
            train_loader,
            optimizer,
            device,
            args.log_interval,
            f"train e{epoch}",
            label_smoothing=args.label_smoothing,
            scheduler=scheduler if scheduler_step_per_batch else None,
            value_weight=args.value_weight,
            scaler=scaler,
            advantage_weight=getattr(args, "advantage_weight", 0.0),
            teacher_weight=args.teacher_weight if args.teacher_targets else 0.0,
            teacher_value_weight=args.teacher_value_weight,
        )
        val_metrics = run_epoch(
            model,
            val_loader,
            None,
            device,
            args.log_interval,
            f"val   e{epoch}",
            label_smoothing=args.label_smoothing,
            value_weight=args.value_weight,
        )

        elapsed = time.time() - t_epoch
        if scheduler is not None and not scheduler_step_per_batch:
            scheduler.step()
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
            f"  train_teacher_coverage={train_metrics.get('teacher_coverage', 0.0):.3f}"
            f"  train_teacher_kl_card={train_metrics.get('teacher_kl_card', 0.0):.4f}"
            f"  train_teacher_kl_mode={train_metrics.get('teacher_kl_mode', 0.0):.4f}"
            f"  val_loss={val_loss:.4f}"
            f"  val_card_top1={val_metrics.get('card_top1', float('nan')):.3f}"
            f"  val_card_mrr={val_metrics.get('card_mrr', float('nan')):.3f}"
            f"  val_card_nll={val_metrics.get('card_nll', float('nan')):.4f}"
            f"  val_card_conf={val_metrics.get('card_conf', float('nan')):.3f}"
            f"  val_mode_acc={val_metrics.get('mode_acc', float('nan')):.3f}"
            f"  val_country_ce={val_metrics.get('country_ce', float('nan')):.4f}"
            f"  country_top1={val_metrics.get('country_top1', float('nan')):.3f}"
            f"  val_value_mse={val_metrics.get('value_mse', float('nan')):.4f}"
            f"  elapsed={elapsed:.1f}s" + ("  [BEST]" if is_best else "")
        )

        # ---- W&B per-epoch logging ----
        if wandb_active:
            current_lr = optimizer.param_groups[0]["lr"]
            _wandb_log_epoch(epoch, train_metrics, val_metrics, current_lr, is_best)

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
            print(
                f"\nEarly stopping at epoch {epoch}: no improvement for {epochs_no_improve} epochs."
            )
            break

    print(f"\nTraining complete. Best val_loss={best_val_loss:.4f} -> {best_ckpt_path}")

    # ---- post-training benchmark ----
    bench_json = None
    if args.bench_after_train > 0 and os.path.exists(best_ckpt_path):
        bench_json = os.path.join(args.out_dir, "bench_results.json")
        bench_cmd = (
            f"bash scripts/bench_cpp.sh"
            f" --checkpoint {best_ckpt_path}"
            f" --n-games {args.bench_after_train}"
            f" --seed {args.bench_seed}"
            f" --out {bench_json}"
        )
        print(f"\n[bench] Running post-training benchmark: {bench_cmd}")
        import subprocess
        bench_result = subprocess.run(bench_cmd, shell=True, capture_output=True, text=True)
        print(bench_result.stdout)
        if bench_result.returncode != 0:
            print(f"[bench] WARNING: benchmark failed (rc={bench_result.returncode})")
            if bench_result.stderr:
                print(bench_result.stderr[-500:])
            bench_json = None

    # ---- W&B run summary and finish ----
    if wandb_active:
        _wandb_module.summary["best_val_loss"] = best_val_loss
        _wandb_module.summary["best_epoch"] = (
            # Recover best epoch from the best checkpoint if it was saved.
            torch.load(best_ckpt_path, map_location="cpu", weights_only=False).get("epoch", -1)
            if os.path.exists(best_ckpt_path)
            else -1
        )
        if bench_json and os.path.exists(bench_json):
            _wandb_log_bench_results(bench_json)
        _wandb_module.finish()


if __name__ == "__main__":
    main()
