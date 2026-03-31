"""Step 4: Evaluate checkpoint on a different version's data.

Loads parquet files and runs forward pass to measure card_top1, card_mrr, NLL.
Useful for detecting distribution shift between model versions.

Usage:
    uv run python scripts/diag_cross_eval.py \
        --checkpoint data/checkpoints/retrain_v24/baseline_best.pt \
        --data-dir data/combined_v23 \
        --label "v24 ckpt on v23 data"
"""
from __future__ import annotations
import argparse, sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "python"))

import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader

from tsrl.policies.dataset import TS_SelfPlayDataset
from tsrl.policies.model import TSBaselineModel


def evaluate(ckpt_path: str, data_dir: str, label: str, batch_size: int = 4096) -> None:
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)
    model = TSBaselineModel(
        hidden_dim=ckpt.get("args", {}).get("hidden_dim", 256),
        dropout=0.0,
    ).to(device)
    model.load_state_dict(ckpt["model_state_dict"])
    model.eval()
    print(f"Loaded: {ckpt_path}  (epoch {ckpt.get('epoch')})")

    ds = TS_SelfPlayDataset(data_dir, value_target_mode="winner_side")
    loader = DataLoader(ds, batch_size=batch_size, shuffle=False, num_workers=0)

    total_top1 = total_mrr = total_nll = total_vmse = n = 0.0
    t0 = time.time()
    with torch.no_grad():
        for batch in loader:
            inf  = batch["influence"].to(device)
            cards = batch["cards"].to(device)
            scal = batch["scalars"].to(device)
            ct   = batch["card_target"].to(device)
            vt   = batch["value_target"].to(device)

            out = model(inf, cards, scal)
            logits = out["card_logits"]
            probs  = F.softmax(logits, dim=1)

            top1  = (logits.argmax(dim=1) == ct).float().sum().item()
            nll   = F.cross_entropy(logits, ct, reduction="sum").item()
            ranks = (logits.argsort(dim=1, descending=True) == ct.unsqueeze(1)).int().argmax(dim=1) + 1
            mrr   = (1.0 / ranks.float()).sum().item()
            vmse  = ((out["value"].squeeze(1) - vt.squeeze(1)) ** 2).sum().item()

            b = ct.shape[0]
            total_top1 += top1
            total_mrr  += mrr
            total_nll  += nll
            total_vmse += vmse
            n += b

    print(f"\n{'='*60}")
    print(f"  {label}")
    print(f"  data: {data_dir}  ({int(n):,} rows)")
    print(f"  card_top1 : {total_top1/n:.4f}  ({100*total_top1/n:.2f}%)")
    print(f"  card_mrr  : {total_mrr/n:.4f}")
    print(f"  card_nll  : {total_nll/n:.4f}")
    print(f"  value_mse : {total_vmse/n:.4f}")
    print(f"  elapsed   : {time.time()-t0:.1f}s")
    print(f"{'='*60}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--checkpoint", required=True)
    ap.add_argument("--data-dir",   required=True)
    ap.add_argument("--label",      default="eval")
    ap.add_argument("--batch-size", type=int, default=4096)
    args = ap.parse_args()
    evaluate(args.checkpoint, args.data_dir, args.label, args.batch_size)


if __name__ == "__main__":
    main()
