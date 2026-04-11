#!/usr/bin/env python3
"""Migrate old checkpoints to the current scalar feature dimension.

The scalar feature vector grew from 11 to 32 dims (21 new active-effect booleans).
Models that concatenate region scalars went from 39 (11+28) to 60 (32+28).

Migration strategy: pad scalar_encoder.weight with zeros for the 21 new features.
- Zero weights mean: model perfectly ignores new features → identical outputs on
  states where new features are all zero; graceful degradation when they're non-zero.
- No other weights are affected (bias shape is unchanged, all other layers are fine).

Layout:
  Old 11-dim:  [scalars(11)]                  → new 32-dim:  [scalars(11), zeros(21)]
  Old 39-dim:  [scalars(11), region(28)]       → new 60-dim:  [scalars(11), zeros(21), region(28)]

Usage:
    # Migrate one checkpoint
    uv run python scripts/migrate_scalar_dim.py --input data/checkpoints/v106_cf_gnn_s42/best.pt \\
                                                 --output data/checkpoints/v106_cf_gnn_s42/best_32dim.pt

    # Dry-run (prints what would be done, no writes)
    uv run python scripts/migrate_scalar_dim.py --input data/checkpoints/... --dry-run

    # Batch migrate all 11/39-dim checkpoints found under a directory
    uv run python scripts/migrate_scalar_dim.py --scan data/checkpoints/ --inplace

    # Self-test: verify migration preserves outputs exactly on zero-new-features input
    uv run python scripts/migrate_scalar_dim.py --self-test
"""
from __future__ import annotations

import argparse
import glob
import os
import sys
from pathlib import Path

import torch
import torch.nn as nn

sys.path.insert(0, str(Path(__file__).parent.parent))


# These are the only two valid old-dim configs.
_OLD_SCALAR_DIM = 11
_NEW_SCALAR_DIM = 32
_REGION_DIM = 28
_OLD_SCALAR_WITH_REGION = _OLD_SCALAR_DIM + _REGION_DIM   # 39
_NEW_SCALAR_WITH_REGION = _NEW_SCALAR_DIM + _REGION_DIM   # 60


def _detect_scalar_dim(state_dict: dict) -> int | None:
    """Return input size of scalar_encoder.weight, or None if not found."""
    w = state_dict.get("scalar_encoder.weight")
    if w is None:
        return None
    return int(w.shape[1])


def _migrate_state_dict(state_dict: dict) -> tuple[dict, str]:
    """Pad scalar_encoder.weight if needed. Returns (new_sd, description)."""
    old_dim = _detect_scalar_dim(state_dict)
    if old_dim is None:
        return state_dict, "no scalar_encoder.weight — skipped"

    if old_dim == _NEW_SCALAR_DIM or old_dim == _NEW_SCALAR_WITH_REGION:
        return state_dict, f"already {old_dim}-dim — no migration needed"

    if old_dim not in (_OLD_SCALAR_DIM, _OLD_SCALAR_WITH_REGION):
        return state_dict, f"unexpected scalar dim {old_dim} — skipped (not 11 or 39)"

    w_old = state_dict["scalar_encoder.weight"]  # shape [H, old_dim]
    H = w_old.shape[0]
    zeros = torch.zeros(H, _NEW_SCALAR_DIM - _OLD_SCALAR_DIM, dtype=w_old.dtype)

    if old_dim == _OLD_SCALAR_DIM:
        # Simple: [scalars(11)] → [scalars(11), zeros(21)]
        w_new = torch.cat([w_old, zeros], dim=1)
        desc = f"11→32 dim (no region scalars)"
    else:
        # With region scalars: [scalars(11), region(28)] → [scalars(11), zeros(21), region(28)]
        w_scalar = w_old[:, :_OLD_SCALAR_DIM]   # [H, 11]
        w_region = w_old[:, _OLD_SCALAR_DIM:]   # [H, 28]
        w_new = torch.cat([w_scalar, zeros, w_region], dim=1)
        desc = f"39→60 dim (with region scalars, zeros inserted before region)"

    new_sd = dict(state_dict)
    new_sd["scalar_encoder.weight"] = w_new
    return new_sd, desc


def migrate_checkpoint(input_path: Path, output_path: Path, dry_run: bool = False) -> str:
    """Load, migrate, save. Returns a one-line status string."""
    raw = torch.load(input_path, map_location="cpu", weights_only=False)

    if isinstance(raw, dict):
        state_dict = raw.get("model_state_dict", raw)
        new_sd, desc = _migrate_state_dict(state_dict)
        if not dry_run and new_sd is not state_dict:
            new_ckpt = dict(raw)
            if "model_state_dict" in raw:
                new_ckpt["model_state_dict"] = new_sd
            else:
                new_ckpt = new_sd
            # Update stored args so future load_model() uses correct dim
            if "args" in new_ckpt and isinstance(new_ckpt["args"], dict):
                new_ckpt["args"] = dict(new_ckpt["args"])
                new_ckpt["args"]["scalar_dim"] = _NEW_SCALAR_DIM
            output_path.parent.mkdir(parents=True, exist_ok=True)
            # Write to temp file then rename — atomic on Linux, safe to interrupt
            tmp = output_path.with_suffix(".pt.migrating")
            torch.save(new_ckpt, tmp)
            tmp.rename(output_path)
    else:
        desc = "TorchScript archive — cannot migrate state_dict directly"

    action = "[DRY RUN]" if dry_run else "written" if output_path != input_path else "in-place"
    return f"{input_path.name}: {desc} → {action}"


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------

def _self_test() -> None:
    """Verify that migration preserves forward-pass outputs exactly on zero-new-features input."""
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from tsrl.policies.model import TSControlFeatGNNModel, TSBaselineModel, SCALAR_DIM, CARD_DIM, INFLUENCE_DIM

    print("=== Migration self-test ===")
    failures = []

    # --- Test 1: TSBaselineModel (11 → 32) ---
    print("\n[1] TSBaselineModel 11→32 ...")
    # Build an 11-dim variant of TSBaselineModel by patching its scalar_encoder
    model_old = TSBaselineModel(hidden_dim=64)
    # Shrink scalar_encoder to 11 inputs (simulate old checkpoint)
    old_in = 11
    w_old = torch.randn(model_old.scalar_encoder.weight.shape[0], old_in)
    b_old = model_old.scalar_encoder.bias.data.clone()
    model_old.scalar_encoder = nn.Linear(old_in, model_old.scalar_encoder.weight.shape[0])
    model_old.scalar_encoder.weight.data.copy_(w_old)
    model_old.scalar_encoder.bias.data.copy_(b_old)
    model_old.eval()

    # Build old-style state_dict
    sd_old = model_old.state_dict()
    assert sd_old["scalar_encoder.weight"].shape[1] == 11

    # Migrate
    sd_new, desc = _migrate_state_dict(sd_old)
    assert sd_new["scalar_encoder.weight"].shape[1] == 32, f"Expected 32, got {sd_new['scalar_encoder.weight'].shape[1]}"
    print(f"  Migration desc: {desc}")

    # Load into new model
    model_new = TSBaselineModel(hidden_dim=64)
    model_new.load_state_dict(sd_new, strict=False)
    model_new.eval()

    # Run with zeros in positions 11:32 (new features = 0)
    inf = torch.randn(2, INFLUENCE_DIM)
    cards = torch.randn(2, CARD_DIM)
    scalars_old = torch.randn(2, 11)
    scalars_new = torch.zeros(2, 32)
    scalars_new[:, :11] = scalars_old

    with torch.no_grad():
        out_old = model_old(inf, cards, scalars_old)
        out_new = model_new(inf, cards, scalars_new)

    for k in out_old:
        eq = torch.equal(out_old[k], out_new[k])
        diff = (out_old[k] - out_new[k]).abs().max().item()
        if not eq and diff > 1e-5:
            failures.append(f"TSBaselineModel {k}: max_diff={diff:.2e} FAIL")
            print(f"  FAIL {k}: max_diff={diff:.2e}")
        else:
            status = "bit-exact" if eq else f"close (max_diff={diff:.2e})"
            print(f"  OK {k}: {status}")

    # --- Test 2: TSControlFeatGNNModel (39 → 60) ---
    print("\n[2] TSControlFeatGNNModel 39→60 ...")
    model_old2 = TSControlFeatGNNModel(hidden_dim=64)
    # Shrink scalar_encoder from 60 to 39
    old_in2 = 39
    w_old2 = torch.randn(model_old2.scalar_encoder.weight.shape[0], old_in2)
    b_old2 = model_old2.scalar_encoder.bias.data.clone()
    model_old2.scalar_encoder = nn.Linear(old_in2, model_old2.scalar_encoder.weight.shape[0])
    model_old2.scalar_encoder.weight.data.copy_(w_old2)
    model_old2.scalar_encoder.bias.data.copy_(b_old2)
    model_old2.eval()

    sd_old2 = model_old2.state_dict()
    assert sd_old2["scalar_encoder.weight"].shape[1] == 39

    sd_new2, desc2 = _migrate_state_dict(sd_old2)
    assert sd_new2["scalar_encoder.weight"].shape[1] == 60, f"Expected 60, got {sd_new2['scalar_encoder.weight'].shape[1]}"
    print(f"  Migration desc: {desc2}")

    model_new2 = TSControlFeatGNNModel(hidden_dim=64)
    model_new2.load_state_dict(sd_new2, strict=False)
    model_new2.eval()

    # region_scalars are positions [11:39] in old layout, [32:60] in new layout
    # Simulate: create scalars_old with 11 scalar values, then model appends region(28)
    # In practice, the model's forward() does: scalars_extended = cat([scalars, region_scalars])
    # So we test: old model with scalars(11)+region(28) = same as new model with scalars(32, zeros in 11:32)+region(28)
    # BUT the model appends region internally. We control scalars (11 or 32 dims), model appends region(28).
    scalars_11 = torch.randn(2, 11)
    scalars_32 = torch.zeros(2, 32)
    scalars_32[:, :11] = scalars_11  # positions 11:32 = zero (new features)

    with torch.no_grad():
        out_old2 = model_old2(inf, cards, scalars_11)
        out_new2 = model_new2(inf, cards, scalars_32)

    for k in out_old2:
        eq = torch.equal(out_old2[k], out_new2[k])
        diff = (out_old2[k] - out_new2[k]).abs().max().item()
        if not eq and diff > 1e-5:
            failures.append(f"TSControlFeatGNNModel {k}: max_diff={diff:.2e} FAIL")
            print(f"  FAIL {k}: max_diff={diff:.2e}")
        else:
            status = "bit-exact" if eq else f"close (max_diff={diff:.2e})"
            print(f"  OK {k}: {status}")

    # --- Summary ---
    print()
    if failures:
        print(f"FAILED: {len(failures)} checks")
        for f in failures:
            print(f"  {f}")
        sys.exit(1)
    else:
        print("All migration correctness checks PASSED.")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--input", type=Path, help="Single checkpoint to migrate")
    p.add_argument("--output", type=Path, help="Output path (default: <input>.migrated.pt)")
    p.add_argument("--inplace", action="store_true", help="Overwrite the input file (use with --scan)")
    p.add_argument("--scan", type=Path, help="Directory to scan for old-dim checkpoints (batch mode)")
    p.add_argument("--dry-run", action="store_true", help="Print what would happen, do nothing")
    p.add_argument("--self-test", action="store_true", help="Run correctness self-test and exit")
    args = p.parse_args()

    if args.self_test:
        _self_test()
        return

    if args.scan:
        pts = sorted(glob.glob(str(args.scan / "**" / "*.pt"), recursive=True))
        print(f"Scanning {len(pts)} checkpoints under {args.scan}...")
        counts = {"migrated": 0, "skipped": 0, "error": 0}
        for f in pts:
            path = Path(f)
            try:
                out = path if args.inplace else path.with_suffix(".migrated.pt")
                status = migrate_checkpoint(path, out, dry_run=args.dry_run)
                if "no migration" in status or "already" in status or "skipped" in status or "TorchScript" in status:
                    counts["skipped"] += 1
                else:
                    counts["migrated"] += 1
                    print(f"  {status}")
            except Exception as e:
                counts["error"] += 1
                print(f"  ERROR {path.name}: {e}")
        print(f"\nDone: {counts['migrated']} migrated, {counts['skipped']} skipped, {counts['error']} errors")
        return

    if args.input:
        out = args.output or args.input.with_suffix(".migrated.pt")
        status = migrate_checkpoint(args.input, out, dry_run=args.dry_run)
        print(status)
        return

    p.print_help()


if __name__ == "__main__":
    main()
