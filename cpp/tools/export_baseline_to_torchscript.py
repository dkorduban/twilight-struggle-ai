#!/usr/bin/env python3
"""Export a Python TSBaselineModel checkpoint to TorchScript for C++ inference.

This stays under `cpp/tools` on purpose: the C++ runtime owns the deployment
artifact contract even if the source checkpoint still comes from Python
training. The exported module is the handoff point between Python training and
native hot-path inference.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import torch

from tsrl.policies.model import (
    SCALAR_DIM,
    TSBaselineModel,
    TSCardEmbedModel,
    TSControlFeatGNNModel,
    TSControlFeatGNNSideModel,
    TSControlFeatModel,
    TSCountryAttnModel,
    TSCountryAttnSideModel,
    TSCountryEmbedModel,
    TSDirectCountryModel,
    TSFullEmbedModel,
    TSMarginalValueModel,
)

_MODEL_REGISTRY = {
    "baseline": TSBaselineModel,
    "card_embed": TSCardEmbedModel,
    "country_embed": TSCountryEmbedModel,
    "full_embed": TSFullEmbedModel,
    "country_attn": TSCountryAttnModel,
    "country_attn_side": TSCountryAttnSideModel,
    "direct_country": TSDirectCountryModel,
    "marginal_value": TSMarginalValueModel,
    "control_feat": TSControlFeatModel,
    "control_feat_gnn": TSControlFeatGNNModel,
    "control_feat_gnn_side": TSControlFeatGNNSideModel,
}


def load_model(checkpoint_path: Path) -> tuple[torch.nn.Module, int]:
    """Load model from checkpoint. Returns (model, scalar_dim) for export tracing."""
    checkpoint = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
    state_dict = checkpoint.get("model_state_dict", checkpoint)
    ckpt_args = checkpoint.get("args", {})
    hidden_dim = ckpt_args.get("hidden_dim", 256)
    model_type = ckpt_args.get("model_type", "baseline")
    dropout = ckpt_args.get("dropout", 0.1)
    num_strategies = ckpt_args.get("num_strategies", 4)
    cls = _MODEL_REGISTRY.get(model_type, TSBaselineModel)
    import inspect
    init_params = inspect.signature(cls.__init__).parameters
    kwargs: dict = {"hidden_dim": hidden_dim, "dropout": dropout}
    if "num_strategies" in init_params:
        kwargs["num_strategies"] = num_strategies
    model = cls(**kwargs)
    # Detect actual scalar_dim from checkpoint weights BEFORE loading
    scalar_w = state_dict.get("scalar_encoder.weight")
    ckpt_scalar_dim: int = int(scalar_w.shape[1]) if scalar_w is not None else SCALAR_DIM
    # Filter state_dict to only keys with matching shapes (skip size-mismatched heads)
    model_sd = model.state_dict()
    filtered_sd = {
        k: v for k, v in state_dict.items()
        if k in model_sd and v.shape == model_sd[k].shape
    }
    model.load_state_dict(filtered_sd, strict=False)
    model.eval()
    return model, ckpt_scalar_dim


def export_checkpoint(checkpoint_path: Path, output_path: Path) -> None:
    model, ckpt_scalar_dim = load_model(checkpoint_path)
    try:
        scripted = torch.jit.script(model)
    except Exception:
        example_inputs = (
            torch.zeros((1, 172), dtype=torch.float32),
            torch.zeros((1, 448), dtype=torch.float32),
            torch.zeros((1, SCALAR_DIM), dtype=torch.float32),  # C++ sends SCALAR_DIM; models with region_encoder extend internally
        )
        scripted = torch.jit.trace(model, example_inputs, strict=False)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    scripted.save(str(output_path))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", type=Path, required=True, help="Input .pt checkpoint")
    parser.add_argument("--out", type=Path, required=True, help="Output TorchScript .pt file")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    export_checkpoint(args.checkpoint, args.out)
    print(f"exported {args.checkpoint} -> {args.out}")


if __name__ == "__main__":
    main()
