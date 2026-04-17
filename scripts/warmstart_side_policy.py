#!/usr/bin/env python3
"""Warm-start TSCountryAttnSidePolicyModel from a TSCountryAttnSideModel checkpoint.

Loads the source checkpoint, creates the new model with per-side policy heads,
copies shared weights, then initializes per-side heads from shared ones.

Usage:
    python scripts/warmstart_side_policy.py \
        --src data/checkpoints/ppo_v310_sc_league/ppo_best.pt \
        --dst data/checkpoints/side_policy_warmstart/ppo_best.pt
"""

import argparse
import shutil
from pathlib import Path

import torch

from tsrl.constants import MODEL_REGISTRY


def main() -> None:
    parser = argparse.ArgumentParser(description="Warm-start side-policy model")
    parser.add_argument("--src", required=True, help="Source checkpoint (country_attn_side)")
    parser.add_argument("--dst", required=True, help="Destination checkpoint path")
    parser.add_argument("--hidden-dim", type=int, default=256, help="Hidden dim (default: 256)")
    args = parser.parse_args()

    # Load source checkpoint
    ckpt = torch.load(args.src, map_location="cpu", weights_only=True)
    src_sd = ckpt.get("model_state_dict", ckpt)

    # Create new model
    model = MODEL_REGISTRY["country_attn_side_policy"](hidden_dim=args.hidden_dim)

    # Load shared weights (per-side heads will be missing, which is expected)
    missing, unexpected = model.load_state_dict(src_sd, strict=False)
    side_missing = [k for k in missing if "_ussr" in k or "_us" in k]
    other_missing = [k for k in missing if "_ussr" not in k and "_us" not in k]

    print(f"Loaded {len(src_sd)} keys from {args.src}")
    print(f"Per-side heads missing (expected): {len(side_missing)}")
    if other_missing:
        print(f"WARNING: non-side keys missing: {other_missing}")

    # Initialize per-side heads from shared
    model._init_from_shared()
    print("Copied shared head weights to per-side heads")

    # Build output checkpoint (preserve optimizer state etc. if present)
    out_ckpt = {}
    if isinstance(ckpt, dict):
        for k, v in ckpt.items():
            if k == "model_state_dict":
                continue
            # Skip optimizer state — shapes won't match
            if k in ("optimizer_state_dict",):
                continue
            out_ckpt[k] = v

    out_ckpt["model_state_dict"] = model.state_dict()
    out_ckpt["model_type"] = "country_attn_side_policy"

    # Save
    dst = Path(args.dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    torch.save(out_ckpt, dst)

    total_params = sum(p.numel() for p in model.parameters())
    print(f"\nSaved to {dst}")
    print(f"Model: country_attn_side_policy ({total_params:,} params)")
    print(f"Hidden dim: {args.hidden_dim}")


if __name__ == "__main__":
    main()
