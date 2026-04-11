#!/usr/bin/env python3
"""Compute pairwise JSD matrix across all scripted models in scripted_for_elo/.

Efficiently caches each model's output distributions once (N forward passes),
then computes all N*(N-1)/2 pairwise JSD values from cached tensors.

Tracks all 3 heads separately: card_jsd, mode_jsd, country_jsd.
Combined distance = 0.5*card + 0.3*country + 0.2*mode (weighted by entropy).

Output: results/elo/jsd_matrix.json
"""
from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path

import torch
import polars as pl

CARD_SLOTS = 111
MODE_SLOTS = 5
COUNTRY_SLOTS = 86
COUNTRY_HEAD_MODE_IDS = frozenset({0, 2, 3})

# Weights for combined distance metric
W_CARD = 0.5
W_COUNTRY = 0.3
W_MODE = 0.2


def _masked_probs(logits: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
    """Softmax with masking (for card/mode heads)."""
    masked = torch.where(mask, logits, torch.full_like(logits, -1e9))
    probs = torch.softmax(masked, dim=1)
    probs = probs * mask.float()
    probs = probs / probs.sum(dim=1, keepdim=True).clamp(min=1e-10)
    return probs


def _renorm_probs(probs: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
    """Renormalize (for country head which outputs mixture-of-softmaxes)."""
    probs = probs * mask.float()
    probs = probs / probs.sum(dim=1, keepdim=True).clamp(min=1e-10)
    return probs


def _pairwise_jsd(p: torch.Tensor, q: torch.Tensor, mask: torch.Tensor) -> float:
    """Mean JSD(P||Q) over rows. Both p, q are already normalized probabilities."""
    valid = mask.any(dim=1)
    if not valid.any():
        return float("nan")
    p = p[valid]
    q = q[valid]
    mix = 0.5 * (p + q)
    safe_p = p.clamp(min=1e-10)
    safe_q = q.clamp(min=1e-10)
    safe_mix = mix.clamp(min=1e-10)
    kl_pm = (p * (safe_p.log() - safe_mix.log())).sum(dim=1)
    kl_qm = (q * (safe_q.log() - safe_mix.log())).sum(dim=1)
    jsd = (0.5 * (kl_pm + kl_qm) / math.log(2.0)).clamp(0.0, 1.0)
    return float(jsd.mean().item())


def _forward_model(
    model: torch.nn.Module,
    influence: torch.Tensor,
    cards: torch.Tensor,
    scalars: torch.Tensor,
) -> dict[str, torch.Tensor]:
    """Forward pass with scalar dimension adaptation."""
    scalar_encoder = getattr(model, "scalar_encoder", None)
    expected_scalars = scalars.shape[1]
    if scalar_encoder is not None and hasattr(scalar_encoder, "in_features"):
        expected_scalars = int(scalar_encoder.in_features)

    if scalars.shape[1] < expected_scalars:
        pad = torch.zeros(
            (scalars.shape[0], expected_scalars - scalars.shape[1]),
            dtype=scalars.dtype, device=scalars.device,
        )
        model_scalars = torch.cat([scalars, pad], dim=1)
    else:
        model_scalars = scalars[:, :expected_scalars]

    return model(influence, cards, model_scalars)


def cache_model_distributions(
    model: torch.nn.Module,
    influence: torch.Tensor,
    cards: torch.Tensor,
    scalars: torch.Tensor,
    card_mask: torch.Tensor,
    mode_mask: torch.Tensor,
    country_mask: torch.Tensor,
    mode_id: torch.Tensor,
    device: torch.device,
    batch_size: int = 256,
) -> dict[str, torch.Tensor]:
    """Run model forward on entire probe set, return normalized probability distributions.

    Returns:
        dict with keys: card_probs (N, 111), mode_probs (N, 5), country_probs (N, 86)
        All country positions use probs even when mode doesn't use country head
        (country_active mask applied during pairwise JSD).
    """
    n = influence.shape[0]
    all_card_probs = torch.zeros(n, CARD_SLOTS)
    all_mode_probs = torch.zeros(n, MODE_SLOTS)
    all_country_probs = torch.zeros(n, COUNTRY_SLOTS)

    model.eval()
    with torch.no_grad():
        for start in range(0, n, batch_size):
            end = min(start + batch_size, n)
            out = _forward_model(
                model,
                influence[start:end].to(device),
                cards[start:end].to(device),
                scalars[start:end].to(device),
            )
            cm = card_mask[start:end].to(device)
            mm = mode_mask[start:end].to(device)
            km = country_mask[start:end].to(device)

            all_card_probs[start:end] = _masked_probs(out["card_logits"], cm).cpu()
            all_mode_probs[start:end] = _masked_probs(out["mode_logits"], mm).cpu()
            # country head returns mixture-of-softmaxes probabilities, not logits
            all_country_probs[start:end] = _renorm_probs(out["country_logits"], km).cpu()

    return {
        "card_probs": all_card_probs,
        "mode_probs": all_mode_probs,
        "country_probs": all_country_probs,
    }


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Compute pairwise JSD matrix across scripted models")
    p.add_argument("--model-dir", default="data/checkpoints/scripted_for_elo",
                   help="Directory containing *_scripted.pt files")
    p.add_argument("--probe-set", default="data/probe_positions.parquet")
    p.add_argument("--out", default="results/elo/jsd_matrix.json")
    p.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    p.add_argument("--batch-size", type=int, default=256)
    p.add_argument("--include", nargs="*", help="Only include these model names (e.g. v8 v14 v22)")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    device = torch.device(args.device)

    # Load probe set
    probe_path = Path(args.probe_set)
    print(f"Loading probe set: {probe_path}")
    df = pl.read_parquet(probe_path)
    n = len(df)
    print(f"  {n} positions")

    influence = torch.tensor(df["influence"].to_list(), dtype=torch.float32)
    cards = torch.tensor(df["cards"].to_list(), dtype=torch.float32)
    scalars = torch.tensor(df["scalars"].to_list(), dtype=torch.float32)
    mode_id = torch.tensor(df["mode_id"].to_list(), dtype=torch.int64)

    if "card_mask" in df.columns:
        card_mask = torch.tensor(df["card_mask"].to_list(), dtype=torch.bool)
    else:
        card_mask = torch.ones((n, CARD_SLOTS), dtype=torch.bool)

    if "mode_mask" in df.columns:
        mode_mask = torch.tensor(df["mode_mask"].to_list(), dtype=torch.bool)
    else:
        mode_mask = torch.ones((n, MODE_SLOTS), dtype=torch.bool)

    valid_country = torch.ones(COUNTRY_SLOTS, dtype=torch.bool)
    valid_country[64] = False  # slot 64 unused
    country_mask = valid_country.unsqueeze(0).expand(n, -1).clone()

    # country_active: positions where country head is used
    country_active_ids = torch.tensor(sorted(COUNTRY_HEAD_MODE_IDS), dtype=torch.int64)
    country_active = torch.isin(mode_id, country_active_ids)  # (N,) bool

    # Discover models
    model_dir = Path(args.model_dir)
    model_paths = sorted(model_dir.glob("*_scripted.pt"))
    if args.include:
        include_set = set(args.include)
        model_paths = [p for p in model_paths if p.stem.replace("_scripted", "") in include_set]
    if not model_paths:
        raise FileNotFoundError(f"No *_scripted.pt files in {model_dir}")

    models: dict[str, Path] = {p.stem.replace("_scripted", ""): p for p in model_paths}
    names = sorted(models.keys())
    print(f"\nFound {len(names)} models: {names}")

    # Step 1: Cache distributions for each model
    print("\n--- Phase 1: forward passes ---")
    cached: dict[str, dict[str, torch.Tensor]] = {}
    for i, name in enumerate(names):
        t0 = time.time()
        try:
            model = torch.jit.load(str(models[name]), map_location=device)
        except Exception as e:
            print(f"  [{i+1}/{len(names)}] {name}: LOAD FAILED: {e}")
            continue
        dists = cache_model_distributions(
            model, influence, cards, scalars,
            card_mask, mode_mask, country_mask, mode_id,
            device, args.batch_size,
        )
        cached[name] = dists
        elapsed = time.time() - t0
        print(f"  [{i+1}/{len(names)}] {name}: {elapsed:.1f}s")

    loaded_names = sorted(cached.keys())
    print(f"\nSuccessfully cached {len(loaded_names)}/{len(names)} models")

    # Step 2: Pairwise JSD
    print("\n--- Phase 2: pairwise JSD ---")
    matrix: dict[str, dict[str, dict[str, float]]] = {}
    n_pairs = len(loaded_names) * (len(loaded_names) - 1) // 2
    pair_idx = 0

    for i, name_a in enumerate(loaded_names):
        matrix[name_a] = {}
        for j, name_b in enumerate(loaded_names):
            if i == j:
                matrix[name_a][name_b] = {
                    "card_jsd": 0.0, "mode_jsd": 0.0, "country_jsd": 0.0, "combined": 0.0
                }
                continue
            if j < i:
                # Copy symmetric entry
                entry = matrix[name_b][name_a]
                matrix[name_a][name_b] = entry
                continue

            pair_idx += 1
            da = cached[name_a]
            db = cached[name_b]

            card_jsd = _pairwise_jsd(da["card_probs"], db["card_probs"], card_mask)
            mode_jsd = _pairwise_jsd(da["mode_probs"], db["mode_probs"], mode_mask)

            # Country JSD: only over positions where country head is active
            ca_mask = country_mask[country_active]
            country_jsd = _pairwise_jsd(
                da["country_probs"][country_active],
                db["country_probs"][country_active],
                ca_mask,
            )

            combined = W_CARD * card_jsd + W_MODE * mode_jsd + W_COUNTRY * (
                country_jsd if not math.isnan(country_jsd) else 0.0
            )

            entry = {
                "card_jsd": round(card_jsd, 6),
                "mode_jsd": round(mode_jsd, 6),
                "country_jsd": round(country_jsd, 6) if not math.isnan(country_jsd) else None,
                "combined": round(combined, 6),
            }
            matrix[name_a][name_b] = entry

            if pair_idx % 50 == 0 or pair_idx == n_pairs:
                print(f"  [{pair_idx}/{n_pairs}] {name_a} vs {name_b}: "
                      f"card={card_jsd:.4f} mode={mode_jsd:.4f} "
                      f"country={country_jsd:.4f} combined={combined:.4f}")

    # Save
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    result = {
        "models": loaded_names,
        "probe_set": str(probe_path),
        "n_positions": n,
        "weights": {"card": W_CARD, "mode": W_MODE, "country": W_COUNTRY},
        "matrix": matrix,
    }
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nSaved JSD matrix ({len(loaded_names)}×{len(loaded_names)}) to {out_path}")

    # Quick summary: most/least similar pairs
    pairs = []
    for i, a in enumerate(loaded_names):
        for j, b in enumerate(loaded_names):
            if j <= i:
                continue
            pairs.append((matrix[a][b]["combined"], a, b))
    pairs.sort()
    print("\nTop-5 most similar pairs (combined JSD):")
    for d, a, b in pairs[:5]:
        print(f"  {a} vs {b}: {d:.4f}")
    print("Top-5 most different pairs:")
    for d, a, b in pairs[-5:][::-1]:
        print(f"  {a} vs {b}: {d:.4f}")


if __name__ == "__main__":
    main()
