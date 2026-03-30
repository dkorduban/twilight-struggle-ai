"""Modal-backed training experiment runner for TSBaselineModel.

Runs full training on a cloud T4 GPU (~5-10 min per 60-epoch run).
Data and checkpoints persist in a Modal Volume between runs.

Usage
-----
# One-time: push training data to the Modal volume
    modal volume create ts-experiments
    modal volume put ts-experiments data/combined_v21/filtered_v20.parquet /data/filtered_v20.parquet

# Run a full experiment (streams output, saves results/modal_<tag>.json locally)
    uv run modal run scripts/modal_train.py
    uv run modal run scripts/modal_train.py --hidden-dim 512 --tag big512
    uv run modal run scripts/modal_train.py --n-blocks 3 --tag depth3

# List saved results
    ls results/modal_*.json | xargs -I{} python3 -c "import json,sys; d=json.load(open('{}'));
        print(d['tag'], 'vvmse=', d.get('val_value_mse'), 'card=', d.get('val_card_top1'))"

# Download a checkpoint
    modal volume get ts-experiments checkpoints/<tag>/baseline_best.pt data/checkpoints/modal_<tag>.pt
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import modal

# ---------------------------------------------------------------------------
# Image — PyTorch (CUDA 12.4) + training deps + local code baked in
# Image is rebuilt only when code or deps change (content-hashed by Modal).
# ---------------------------------------------------------------------------

_repo_root = Path(__file__).parent.parent

image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install(
        "torch",
        extra_index_url="https://download.pytorch.org/whl/cu124",
    )
    .pip_install(
        "polars>=0.20",
        "pyarrow>=14",
        "pydantic>=2.0",
        "numpy>=1.26",
    )
    # Bake in local code — Modal caches this layer by content hash.
    .add_local_dir(str(_repo_root / "python"), remote_path="/root/python")
    .add_local_dir(str(_repo_root / "scripts"), remote_path="/root/scripts")
)

# ---------------------------------------------------------------------------
# Persistent volume — /vol/data for parquets, /vol/checkpoints for ckpts
# ---------------------------------------------------------------------------

volume = modal.Volume.from_name("ts-experiments", create_if_missing=True)
VMOUNT = "/vol"

app = modal.App("ts-train")


# ---------------------------------------------------------------------------
# Training function
# ---------------------------------------------------------------------------

@app.function(
    image=image,
    gpu="T4",
    cpu=4,         # 4 vCPUs: 1 main + 2 dataloader workers + headroom
    volumes={VMOUNT: volume},
    timeout=7200,
    env={"PYTHONPATH": "/root/python"},
)
def train(
    hidden_dim: int = 256,
    n_blocks: int = 2,
    epochs: int = 60,
    batch_size: int = 2048,
    lr: float = 1.2e-3,
    weight_decay: float = 1e-4,
    dropout: float = 0.1,
    label_smoothing: float = 0.05,
    value_target: str = "final_vp",
    data_filename: str = "filtered_v20.parquet",
    tag: str = "exp",
) -> dict:
    import os, subprocess, torch

    data_file = f"{VMOUNT}/data/{data_filename}"
    out_dir   = f"{VMOUNT}/checkpoints/{tag}"

    if not os.path.exists(data_file):
        raise FileNotFoundError(
            f"{data_file} not found on volume. "
            f"Upload: modal volume put ts-experiments <local.parquet> /data/{data_filename}"
        )

    os.makedirs(out_dir, exist_ok=True)

    cmd = [
        sys.executable, "/root/scripts/train_baseline.py",
        "--data-dir", os.path.dirname(data_file),
        "--out-dir", out_dir,
        "--epochs",          str(epochs),
        "--batch-size",      str(batch_size),
        "--lr",              str(lr),
        "--weight-decay",    str(weight_decay),
        "--dropout",         str(dropout),
        "--label-smoothing", str(label_smoothing),
        "--value-target",    value_target,
        "--hidden-dim",      str(hidden_dim),
        "--num-workers",     "2",  # Modal has no OOM risk unlike WSL
        "--one-cycle",
    ]
    print(f"[modal] tag={tag}  hidden_dim={hidden_dim}  n_blocks={n_blocks}  "
          f"epochs={epochs}  batch_size={batch_size}\n", flush=True)
    subprocess.run(cmd, check=False)

    # Always write results JSON to volume so they survive detached runs.
    import json as _json
    metrics = _read_metrics(out_dir, tag)
    results_path = f"{VMOUNT}/results/{tag}.json"
    os.makedirs(os.path.dirname(results_path), exist_ok=True)
    with open(results_path, "w") as fh:
        _json.dump(metrics, fh, indent=2)

    volume.commit()
    return metrics


def _read_metrics(out_dir: str, tag: str) -> dict:
    import os, torch
    best = f"{out_dir}/baseline_best.pt"
    if not os.path.exists(best):
        return {"tag": tag, "error": "no checkpoint"}
    ckpt = torch.load(best, map_location="cpu", weights_only=False)
    vm = ckpt.get("val_metrics", {})
    return {
        "tag":             tag,
        "epoch":           ckpt.get("epoch"),
        "val_loss":        vm.get("loss"),
        "val_card_top1":   vm.get("card_top1"),
        "val_mode_acc":    vm.get("mode_acc"),
        "val_value_mse":   vm.get("value_mse"),
        "val_country_top1": vm.get("country_top1"),
        "checkpoint_path": f"checkpoints/{tag}/baseline_best.pt",
    }


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

@app.function(image=image, volumes={VMOUNT: volume})
def fetch_results_from_volume(tag: str) -> str | None:
    """Read the results JSON for `tag` from the volume; return None if missing."""
    import json as _json, os
    path = f"{VMOUNT}/results/{tag}.json"
    if not os.path.exists(path):
        return None
    return open(path).read()


def _fetch_results(tag: str) -> None:
    """Download results for `tag` from volume and save locally."""
    raw = fetch_results_from_volume.remote(tag)
    if raw is None:
        print(f"No results yet for tag={tag!r}. Job may still be running.")
        print(f"  Check: https://modal.com/apps/")
        return
    metrics = json.loads(raw)
    Path("results").mkdir(exist_ok=True)
    out = Path(f"results/modal_{tag}.json")
    out.write_text(json.dumps(metrics, indent=2))
    print(f"Results for {tag}:")
    print(f"  val_value_mse : {metrics.get('val_value_mse')}")
    print(f"  val_card_top1 : {metrics.get('val_card_top1')}")
    print(f"  val_loss      : {metrics.get('val_loss')}")
    print(f"  epoch         : {metrics.get('epoch')}")
    print(f"  saved to      : {out}")


# ---------------------------------------------------------------------------
# Local entrypoint
# ---------------------------------------------------------------------------

@app.local_entrypoint()
def main(
    hidden_dim: int = 256,
    n_blocks: int = 2,
    epochs: int = 60,
    batch_size: int = 2048,
    lr: float = 1.2e-3,
    weight_decay: float = 1e-4,
    dropout: float = 0.1,
    label_smoothing: float = 0.05,
    value_target: str = "final_vp",
    data_filename: str = "filtered_v20.parquet",
    tag: str = "",
    # Set to fetch + print results already saved to volume (no new training run)
    fetch: str = "",
):
    # ── Fetch mode: download results already on the volume ──────────────────
    if fetch:
        _fetch_results(fetch)
        return

    if not tag:
        tag = f"h{hidden_dim}_b{n_blocks}_e{epochs}"

    print(f"\nSubmitting: tag={tag}  hidden_dim={hidden_dim}  n_blocks={n_blocks}  "
          f"epochs={epochs}  batch_size={batch_size}  lr={lr}", flush=True)

    t0 = time.time()
    metrics = train.remote(
        hidden_dim=hidden_dim, n_blocks=n_blocks, epochs=epochs,
        batch_size=batch_size, lr=lr, weight_decay=weight_decay,
        dropout=dropout, label_smoothing=label_smoothing,
        value_target=value_target, data_filename=data_filename, tag=tag,
    )
    elapsed = time.time() - t0

    metrics.update({"elapsed_s": round(elapsed, 1), "hyperparams": {
        "hidden_dim": hidden_dim, "n_blocks": n_blocks, "epochs": epochs,
        "batch_size": batch_size, "lr": lr, "weight_decay": weight_decay,
        "dropout": dropout, "label_smoothing": label_smoothing,
        "value_target": value_target,
    }})

    Path("results").mkdir(exist_ok=True)
    out = Path(f"results/modal_{tag}.json")
    out.write_text(json.dumps(metrics, indent=2))

    print(f"\n{'='*52}")
    print(f"Done in {elapsed:.0f}s  ({elapsed/60:.1f} min)")
    print(f"  val_value_mse : {metrics.get('val_value_mse', 'N/A')}")
    print(f"  val_card_top1 : {metrics.get('val_card_top1', 'N/A')}")
    print(f"  val_loss      : {metrics.get('val_loss', 'N/A')}")
    print(f"  results       : {out}")
    print(f"  checkpoint    : modal volume get ts-experiments {metrics.get('checkpoint_path','')}")
