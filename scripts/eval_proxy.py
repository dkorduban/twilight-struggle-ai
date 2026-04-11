#!/usr/bin/env python3
"""Phase 5 proxy eval: evaluate a checkpoint on the proxy eval set in <3s.

Reports: card_top1, card_top3, mode_acc, country_top1, val_loss.
Runs in ~1-2s on GPU, ~3-5s on CPU.

Usage:
    uv run python scripts/eval_proxy.py data/checkpoints/phase4/gnn_side_s42_05M/baseline_best.pt
    uv run python scripts/eval_proxy.py <ckpt1.pt> <ckpt2.pt>  # compare multiple
"""

import argparse
import os
import sys
import time

import torch
import torch.nn.functional as F

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

_PROXY_EVAL_PATH = "data/proxy_eval_v3.parquet"


def load_proxy_dataset(path: str, device: str):
    """Load proxy eval parquet and return tensors ready for forward pass."""
    from python.tsrl.policies.dataset import TS_SelfPlayDataset

    class _SingleDirDataset(TS_SelfPlayDataset):
        def __init__(self, parquet_path, value_target_mode="final_vp"):
            import glob, time as t
            import polars as pl
            from python.tsrl.policies.dataset import _NEEDED_COLS, _EFFECT_BOOL_COLS, SCALAR_DIM

            df = pl.read_parquet(parquet_path)
            self._build(df, value_target_mode)

        def _build(self, df, value_target_mode):
            import polars as pl
            import numpy as np
            from python.tsrl.policies.dataset import (
                _NEEDED_COLS, _EFFECT_BOOL_COLS, NUM_COUNTRIES, SCALAR_DIM,
            )

            # Build tensors matching TS_SelfPlayDataset format
            self._influence = []
            self._cards = []
            self._scalars = []
            self._card_targets = []
            self._mode_targets = []
            self._country_targets = []
            self._value_targets = []

            # Use the dataset class properly
            import tempfile, shutil
            tmpdir = tempfile.mkdtemp()
            try:
                df.write_parquet(os.path.join(tmpdir, "proxy.parquet"))
                parent = TS_SelfPlayDataset.__new__(TS_SelfPlayDataset)
                TS_SelfPlayDataset.__init__(parent, tmpdir, value_target_mode)
                self._parent = parent
                self._n = len(parent)
            finally:
                shutil.rmtree(tmpdir)

        def __len__(self):
            return self._parent._n if hasattr(self, '_parent') else 0

        def __getitem__(self, idx):
            return self._parent[idx]

    ds = _SingleDirDataset(path)
    return ds


def evaluate_checkpoint(ckpt_path: str, proxy_path: str, device: str = "cuda") -> dict:
    """Evaluate checkpoint on proxy eval set. Returns metrics dict."""
    if not torch.cuda.is_available():
        device = "cpu"

    # Load model
    from python.tsrl.policies.model import (
        TSBaselineModel, TSControlFeatGNNModel, TSControlFeatGNNSideModel,
        TSCountryAttnModel, TSCountryAttnSideModel,
    )
    import python.tsrl.policies.model as model_module

    MODEL_REGISTRY = {
        "baseline": TSBaselineModel,
        "control_feat_gnn": TSControlFeatGNNModel,
        "control_feat_gnn_side": TSControlFeatGNNSideModel,
        "country_attn": TSCountryAttnModel,
        "country_attn_side": TSCountryAttnSideModel,
    }

    ckpt = torch.load(ckpt_path, map_location="cpu", weights_only=False)
    if isinstance(ckpt, dict):
        state_dict = ckpt.get("model_state_dict", ckpt)
        args_d = ckpt.get("args", {})
        hidden_dim = args_d.get("hidden_dim", 256)
        model_type = args_d.get("model_type", "control_feat_gnn_side")
        dropout = args_d.get("dropout", 0.1)

        # Detect scalar dim
        _REGION_DIM = 28
        detected_scalar_dim = 32
        for k, v in state_dict.items():
            if "scalar_encoder" in k and "weight" in k and len(v.shape) == 2:
                raw = v.shape[1]
                detected_scalar_dim = raw - _REGION_DIM if raw > _REGION_DIM else raw
                break
        orig_dim = model_module.SCALAR_DIM
        model_module.SCALAR_DIM = detected_scalar_dim
        cls = MODEL_REGISTRY.get(model_type, TSControlFeatGNNSideModel)
        model = cls(hidden_dim=hidden_dim, dropout=dropout)
        model.load_state_dict(state_dict, strict=False)
        model_module.SCALAR_DIM = orig_dim
    else:
        raise ValueError(f"Expected dict checkpoint, got {type(ckpt)}")

    model.eval().to(device)

    # Load proxy dataset
    from python.tsrl.policies.dataset import TS_SelfPlayDataset
    import tempfile, shutil, polars as pl

    df = pl.read_parquet(proxy_path)
    tmpdir = tempfile.mkdtemp()
    try:
        df.write_parquet(os.path.join(tmpdir, "proxy.parquet"))
        ds = TS_SelfPlayDataset(tmpdir, value_target_mode="final_vp")
    finally:
        shutil.rmtree(tmpdir)

    from torch.utils.data import DataLoader
    # TS_SelfPlayDataset has __getitems__ (PyTorch 2.0+ batch indexing) which returns
    # a dict of stacked tensors directly. Use identity collate_fn to pass it through.
    loader = DataLoader(ds, batch_size=512, shuffle=False, num_workers=0,
                        collate_fn=lambda x: x)

    total_card_top1 = 0.0
    total_card_top3 = 0.0
    total_mode_acc = 0.0
    total_country_top1 = 0.0
    total_val_loss = 0.0
    total_n = 0

    t0 = time.time()
    with torch.no_grad():
        for batch in loader:
            # Batch is a dict of stacked tensors (default PyTorch collation of dict samples)
            n = batch["influence"].shape[0]
            influence = batch["influence"].float().to(device)
            cards = batch["cards"].float().to(device)  # stored as uint8, cast to float
            scalars = batch["scalars"].float().to(device)
            card_target = batch["card_target"].long().to(device)
            mode_target = batch["mode_target"].long().to(device)
            country_target = batch["country_ops_target"].float().to(device)

            out = model(influence, cards, scalars)
            card_logits = out["card_logits"]
            mode_logits = out["mode_logits"]

            # Card metrics
            preds = card_logits.argmax(dim=1)
            total_card_top1 += (preds == card_target).sum().item()
            top3 = card_logits.topk(3, dim=1).indices
            total_card_top3 += (top3 == card_target.unsqueeze(1)).any(dim=1).sum().item()

            # Mode accuracy
            mode_preds = mode_logits.argmax(dim=1)
            total_mode_acc += (mode_preds == mode_target).sum().item()

            # Country top1
            if "country_logits" in out:
                country_logits = out["country_logits"]
                country_pred = country_logits.argmax(dim=1)
                country_true = country_target.argmax(dim=1)
                total_country_top1 += (country_pred == country_true).sum().item()

            # Loss
            card_loss = F.cross_entropy(card_logits, card_target, label_smoothing=0.05)
            mode_loss = F.cross_entropy(mode_logits, mode_target, label_smoothing=0.05)
            val_loss = card_loss + 0.5 * mode_loss
            total_val_loss += val_loss.item() * n
            total_n += n

    elapsed = time.time() - t0
    n = total_n
    return {
        "card_top1": total_card_top1 / n,
        "card_top3": total_card_top3 / n,
        "mode_acc": total_mode_acc / n,
        "country_top1": total_country_top1 / n if total_country_top1 > 0 else None,
        "val_loss": total_val_loss / n,
        "n_states": n,
        "elapsed_s": elapsed,
        "ckpt": os.path.basename(ckpt_path),
    }


def main():
    p = argparse.ArgumentParser(description="Evaluate checkpoint(s) on proxy eval set.")
    p.add_argument("checkpoints", nargs="+", help="Checkpoint .pt files to evaluate")
    p.add_argument("--proxy", default=_PROXY_EVAL_PATH, help="Proxy eval parquet path")
    p.add_argument("--device", default="cuda", help="Device (cuda or cpu)")
    args = p.parse_args()

    results = []
    for ckpt_path in args.checkpoints:
        if not os.path.exists(ckpt_path):
            print(f"Warning: {ckpt_path} not found, skipping")
            continue
        try:
            m = evaluate_checkpoint(ckpt_path, args.proxy, args.device)
            results.append(m)
            c = m["country_top1"]
            print(
                f"{m['ckpt']:40s}  card_top1={m['card_top1']:.3f}  card_top3={m['card_top3']:.3f}"
                f"  mode_acc={m['mode_acc']:.3f}"
                + (f"  country_top1={c:.3f}" if c is not None else "")
                + f"  val_loss={m['val_loss']:.4f}  [{m['elapsed_s']:.1f}s, {m['n_states']} states]"
            )
        except Exception as e:
            print(f"Error evaluating {ckpt_path}: {e}")
            import traceback; traceback.print_exc()

    if len(results) > 1:
        print("\n=== Ranking by card_top1 ===")
        for r in sorted(results, key=lambda x: -x["card_top1"]):
            print(f"  {r['card_top1']:.3f}  {r['ckpt']}")


if __name__ == "__main__":
    main()
