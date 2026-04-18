#!/usr/bin/env python3
"""Export an AWR checkpoint to TorchScript and benchmark vs panel models.

Usage:
    uv run python scripts/benchmark_awr_checkpoint.py \
        --checkpoint results/awr_sweep/v2/country_attn_side/awr_best.pt \
        --vs data/checkpoints/scripted_for_elo/v56_scripted.pt \
           results/capacity_test/ppo_ussr_only_v5/ppo_best_scripted.pt \
           results/capacity_test/ppo_us_only_v5/ppo_best_scripted.pt \
        --n-games 100 --pool 32
"""

import argparse
import sys
import tempfile
from pathlib import Path

import torch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "python"))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "build-ninja/bindings"))

import tscore
from tsrl.constants import MODEL_REGISTRY
from tsrl.policies.model import SCALAR_DIM


def export_to_scripted(checkpoint_path: str, out_path: str) -> None:
    ckpt = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
    ckpt_args = ckpt.get("args", {})
    model_type = ckpt_args.get("model_type", "baseline")
    hidden_dim = ckpt_args.get("hidden_dim", 256)
    dropout = ckpt_args.get("dropout", 0.0)

    cls = MODEL_REGISTRY.get(model_type)
    if cls is None:
        raise ValueError(f"Unknown model_type: {model_type}")

    import inspect
    init_params = inspect.signature(cls.__init__).parameters
    kwargs: dict = {"hidden_dim": hidden_dim, "dropout": dropout}
    if "num_strategies" in init_params:
        kwargs["num_strategies"] = ckpt_args.get("num_strategies", 4)

    model = cls(**kwargs)
    sd = ckpt.get("model_state_dict", ckpt)
    model_sd = model.state_dict()
    filtered = {k: v for k, v in sd.items() if k in model_sd and v.shape == model_sd[k].shape}
    model.load_state_dict(filtered, strict=False)
    model.eval()

    try:
        scripted = torch.jit.script(model)
    except Exception:
        example = (
            torch.zeros((1, 172), dtype=torch.float32),
            torch.zeros((1, 448), dtype=torch.float32),
            torch.zeros((1, SCALAR_DIM), dtype=torch.float32),
        )
        scripted = torch.jit.trace(model, example, strict=False)

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    scripted.save(out_path)
    return model_type


def benchmark_vs(scripted_path: str, opponent_path: str, n_games: int, pool: int, seed: int) -> dict:
    # model_a=AWR arch; first half model_a=USSR, second half model_a=US
    results = tscore.benchmark_model_vs_model_batched(
        scripted_path, opponent_path, n_games=n_games * 2, pool_size=pool, seed=seed
    )
    half = len(results) // 2
    ussr_results = results[:half]
    us_results = results[half:]
    ussr_wr = sum(1 for r in ussr_results if r.winner == tscore.Side.USSR) / max(len(ussr_results), 1)
    us_wr = sum(1 for r in us_results if r.winner == tscore.Side.US) / max(len(us_results), 1)
    combined = (ussr_wr + us_wr) / 2
    return {"ussr_wr": ussr_wr, "us_wr": us_wr, "combined": combined}


def benchmark_vs_heuristic(scripted_path: str, n_games: int, pool: int, seed: int) -> dict:
    results_ussr = tscore.benchmark_batched(scripted_path, tscore.Side.USSR, n_games=n_games, pool_size=pool, seed=seed)
    results_us = tscore.benchmark_batched(scripted_path, tscore.Side.US, n_games=n_games, pool_size=pool, seed=seed + 50000)
    ussr_wr = sum(1 for r in results_ussr if r.winner == tscore.Side.USSR) / len(results_ussr)
    us_wr = sum(1 for r in results_us if r.winner == tscore.Side.US) / len(results_us)
    return {"ussr_wr": ussr_wr, "us_wr": us_wr, "combined": (ussr_wr + us_wr) / 2}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--checkpoint", required=True)
    ap.add_argument("--vs", nargs="*", default=[], help="Opponent scripted model paths")
    ap.add_argument("--vs-heuristic", action="store_true", help="Also benchmark vs heuristic")
    ap.add_argument("--n-games", type=int, default=100)
    ap.add_argument("--pool", type=int, default=32)
    ap.add_argument("--seed", type=int, default=70000)
    ap.add_argument("--scripted-out", default=None, help="Where to save scripted .pt (default: temp file)")
    args = ap.parse_args()

    with tempfile.TemporaryDirectory() as tmpdir:
        scripted_path = args.scripted_out or str(Path(tmpdir) / "awr_scripted.pt")
        print(f"Exporting {args.checkpoint} → {scripted_path}")
        model_type = export_to_scripted(args.checkpoint, scripted_path)
        print(f"  model_type: {model_type}")

        if args.vs_heuristic:
            res = benchmark_vs_heuristic(scripted_path, args.n_games, args.pool, args.seed)
            print(f"  vs heuristic:  USSR={res['ussr_wr']:.1%}  US={res['us_wr']:.1%}  combined={res['combined']:.1%}")

        for opp_path in args.vs:
            opp_name = Path(opp_path).stem
            try:
                res = benchmark_vs(scripted_path, opp_path, args.n_games, args.pool, args.seed)
                print(f"  vs {opp_name:30s}:  USSR={res['ussr_wr']:.1%}  US={res['us_wr']:.1%}  combined={res['combined']:.1%}")
            except Exception as e:
                print(f"  vs {opp_name}: ERROR — {e}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
