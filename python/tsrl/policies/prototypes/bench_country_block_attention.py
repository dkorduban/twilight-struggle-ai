"""CUDA benchmark for dense vs masked vs block country attention prototypes."""

from __future__ import annotations

import argparse
import statistics
import time

import torch

from tsrl.policies.prototypes.country_block_attention import (
    INFLUENCE_DIM,
    BlockRegionNeighborCountryAttnEncoder,
    DenseCountryAttnPrototype,
    MaskedRegionNeighborCountryAttnEncoder,
    build_region_neighbor_metadata,
)


def _synchronize(device: str) -> None:
    if device == "cuda":
        torch.cuda.synchronize()


def _make_influence(batch_size: int, device: str) -> torch.Tensor:
    return torch.randn(batch_size, INFLUENCE_DIM, device=device)


def _bench_forward(
    model: torch.nn.Module,
    *,
    batch_size: int,
    device: str,
    warmup: int,
    iters: int,
    repeats: int,
) -> float:
    samples = []
    model = model.to(device).eval()
    with torch.no_grad():
        for _ in range(repeats):
            influence = _make_influence(batch_size, device)
            for _ in range(warmup):
                model(influence)
            _synchronize(device)
            t0 = time.perf_counter()
            for _ in range(iters):
                model(influence)
            _synchronize(device)
            samples.append((time.perf_counter() - t0) / iters)
    return statistics.median(samples)


def _bench_forward_backward(
    model: torch.nn.Module,
    *,
    batch_size: int,
    device: str,
    warmup: int,
    iters: int,
    repeats: int,
) -> float:
    samples = []
    model = model.to(device).train()
    for _ in range(repeats):
        influence = _make_influence(batch_size, device)
        for _ in range(warmup):
            for param in model.parameters():
                param.grad = None
            out = model(influence)
            out.float().square().mean().backward()
        _synchronize(device)
        t0 = time.perf_counter()
        for _ in range(iters):
            for param in model.parameters():
                param.grad = None
            out = model(influence)
            out.float().square().mean().backward()
        _synchronize(device)
        samples.append((time.perf_counter() - t0) / iters)
    return statistics.median(samples)


def main() -> None:
    parser = argparse.ArgumentParser(description="Benchmark country-attention prototypes")
    parser.add_argument("--device", default="cuda", choices=["cpu", "cuda"])
    parser.add_argument("--batch-sizes", type=int, nargs="+", default=[256, 1024, 4096])
    parser.add_argument("--warmup-fw", type=int, default=10)
    parser.add_argument("--iters-fw", type=int, default=50)
    parser.add_argument("--warmup-bw", type=int, default=5)
    parser.add_argument("--iters-bw", type=int, default=20)
    parser.add_argument("--repeats", type=int, default=3)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    if args.device == "cuda" and not torch.cuda.is_available():
        raise SystemExit("CUDA requested but not available")

    torch.manual_seed(args.seed)
    metadata = build_region_neighbor_metadata()
    print(
        "region-neighbor pairs:",
        f"{metadata.sparse_pairs}/{metadata.dense_pairs}",
        f"({metadata.dense_pairs / metadata.sparse_pairs:.2f}x fewer than dense)",
    )

    models: list[tuple[str, torch.nn.Module]] = [
        ("dense", DenseCountryAttnPrototype()),
        ("masked_dense", MaskedRegionNeighborCountryAttnEncoder()),
        ("block", BlockRegionNeighborCountryAttnEncoder()),
    ]

    print(f"device: {args.device}")
    for batch_size in args.batch_sizes:
        print(f"\nbatch_size={batch_size}")
        fw_times: dict[str, float] = {}
        bw_times: dict[str, float] = {}
        for name, model in models:
            fw = _bench_forward(
                model,
                batch_size=batch_size,
                device=args.device,
                warmup=args.warmup_fw,
                iters=args.iters_fw,
                repeats=args.repeats,
            )
            bw = _bench_forward_backward(
                model,
                batch_size=batch_size,
                device=args.device,
                warmup=args.warmup_bw,
                iters=args.iters_bw,
                repeats=args.repeats,
            )
            fw_times[name] = fw
            bw_times[name] = bw
            print(
                f"  {name:12s} forward={fw * 1000:8.3f} ms"
                f"  fwd+bwd={bw * 1000:8.3f} ms"
            )

        dense_fw = fw_times["dense"]
        dense_bw = bw_times["dense"]
        print("  relative to dense:")
        for name in ("masked_dense", "block"):
            print(
                f"    {name:12s} forward={fw_times[name] / dense_fw:6.2f}x"
                f"  fwd+bwd={bw_times[name] / dense_bw:6.2f}x"
            )


if __name__ == "__main__":
    main()
