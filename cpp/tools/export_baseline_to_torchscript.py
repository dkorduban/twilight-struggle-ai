#!/usr/bin/env python3
"""Export a Python TSBaselineModel checkpoint to TorchScript for C++ inference.

This stays under `cpp/tools` on purpose: the C++ runtime owns the deployment
artifact contract even if the source checkpoint still comes from Python
training.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import torch

from tsrl.policies.model import TSBaselineModel


def load_model(checkpoint_path: Path) -> TSBaselineModel:
    checkpoint = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
    state_dict = checkpoint.get("model_state_dict", checkpoint)
    ckpt_args = checkpoint.get("args", {})
    hidden_dim = ckpt_args.get("hidden_dim", 256)
    model = TSBaselineModel(hidden_dim=hidden_dim)
    model.load_state_dict(state_dict, strict=False)
    model.eval()
    return model


def export_checkpoint(checkpoint_path: Path, output_path: Path) -> None:
    model = load_model(checkpoint_path)
    try:
        scripted = torch.jit.script(model)
    except Exception:
        example_inputs = (
            torch.zeros((1, 172), dtype=torch.float32),
            torch.zeros((1, 448), dtype=torch.float32),
            torch.zeros((1, 11), dtype=torch.float32),
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
