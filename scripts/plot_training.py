"""Parse /tmp/pipeline_vN.log files and plot all training metrics + benchmarks.

Usage
-----
    uv run python scripts/plot_training.py                    # all versions
    uv run python scripts/plot_training.py --versions 22 23 24
    uv run python scripts/plot_training.py --out results/training_curves.png
"""
from __future__ import annotations

import argparse
import glob
import re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Parsing — training epochs
# ---------------------------------------------------------------------------

_KV = re.compile(r"(\w+)=(-?[\d.]+)")

def parse_log(path: str) -> dict[int, dict[str, float]]:
    """Return {epoch: {metric: value}} from a pipeline log file."""
    epochs: dict[int, dict[str, float]] = {}
    with open(path) as fh:
        for line in fh:
            if not line.startswith("Epoch ") or "summary" not in line:
                continue
            m = re.match(r"Epoch (\d+) summary", line)
            if not m:
                continue
            ep = int(m.group(1))
            row: dict[str, float] = {}
            for key, val in _KV.findall(line):
                row[key] = float(val)
            epochs[ep] = row
    return epochs


def load_versions(versions: list[int]) -> dict[int, dict[int, dict[str, float]]]:
    data: dict[int, dict[int, dict[str, float]]] = {}
    for v in versions:
        path = f"/tmp/pipeline_v{v}.log"
        if not Path(path).exists():
            continue
        parsed = parse_log(path)
        if parsed:
            data[v] = parsed
            print(f"  v{v}: {len(parsed)} epochs")
    return data


# ---------------------------------------------------------------------------
# Parsing — benchmarks
# ---------------------------------------------------------------------------

# e.g. "   learned vs heuristic   learned  10/ 60 ( 16.7%)  heuristic ..."
_BENCH_LINE = re.compile(
    r"(learned|vf_mcts\d+)\s+vs\s+(heuristic|random)"
    r".*?\(\s*([\d.]+)%\)"
)

# Fallback: "[timestamp] vN vs heuristic: X%"
_BENCH_SUMMARY = re.compile(r"v(\d+) vs heuristic:\s*([\d.]+)%")


def parse_benchmarks(path: str) -> dict[str, float]:
    """Return {matchup_key: win_pct} using the last occurrence of each matchup."""
    results: dict[str, float] = {}
    with open(path) as fh:
        for line in fh:
            m = _BENCH_LINE.search(line)
            if m:
                agent, opponent, pct = m.group(1), m.group(2), float(m.group(3))
                key = f"{agent}_vs_{opponent}"
                results[key] = pct
    return results


def load_benchmarks(versions: list[int]) -> dict[int, dict[str, float]]:
    benchmarks: dict[int, dict[str, float]] = {}

    # Seed from durable history first (survives /tmp wipe)
    hist_path = Path("results/benchmark_history.json")
    if hist_path.exists():
        import json
        hist = json.loads(hist_path.read_text())
        for key, val in hist.items():
            try:
                v = int(key.lstrip("v"))
                benchmarks[v] = {k: w for k, w in val.items() if w is not None}
            except (ValueError, AttributeError):
                pass

    for v in versions:
        if v in benchmarks:
            continue  # already loaded from durable history
        # Prefer largest standalone benchmark log (500g > 200g > pipeline)
        candidates = [
            f"/tmp/benchmark_v{v}_500g.log",
            f"/tmp/benchmark_v{v}_200g.log",
            f"/tmp/benchmark_v{v}.log",
            f"/tmp/pipeline_v{v}.log",
        ]
        for path in candidates:
            if not Path(path).exists():
                continue
            b = parse_benchmarks(path)
            if b:
                benchmarks[v] = b
                break
    return benchmarks


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------

# Each entry: (title, [(metric_key, prefix, invert)])
# invert=True → plot 1-value (error rate), making log scale useful for near-1 metrics
TRAIN_PANELS = [
    ("Val loss",             [("loss",        "val_",   False)]),
    ("Card error (1-top1)",  [("card_top1",   "val_",   True)]),
    ("Card MRR error",       [("card_mrr",    "val_",   True)]),
    ("Card NLL",             [("card_nll",    "val_",   False)]),
    ("Card conf error",      [("card_conf",   "val_",   True)]),
    ("Value MSE",            [("value_mse",   "val_",   False)]),
    ("Mode error (1-acc)",   [("mode_acc",    "val_",   True)]),
    ("Country error",        [("country_top1","",       True)]),
]

BENCH_MATCHUPS = [
    ("learned_vs_heuristic", "Learned vs Heuristic"),
]

COLORS = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
          "#8c564b", "#e377c2", "#7f7f7f"]
TRAIN_ALPHA = 0.4
MARKER = "o"


def _plot_training(axes, data, versions, color_map):
    for ax_idx, (title, series) in enumerate(TRAIN_PANELS):
        ax = axes[ax_idx]
        ax.set_title(title, fontsize=10, fontweight="bold")
        ax.set_xlabel("Epoch", fontsize=8)
        ax.set_yscale("log")
        ax.grid(True, alpha=0.3, which="both")

        plotted = False
        for v in versions:
            if v not in data:
                continue
            color = color_map[v]
            for metric_key, prefix, invert in series:
                full_key = prefix + metric_key
                xs, ys = [], []
                for ep in sorted(data[v]):
                    row = data[v][ep]
                    if full_key in row:
                        val = row[full_key]
                        xs.append(ep)
                        ys.append(max(1e-6, 1.0 - val) if invert else val)
                if not xs:
                    continue
                ax.plot(xs, ys, color=color, linewidth=1.8, label=f"v{v}")
                plotted = True

        if not plotted:
            ax.text(0.5, 0.5, "No data", transform=ax.transAxes,
                    ha="center", va="center", color="gray", fontsize=9)
        else:
            ax.legend(fontsize=7, loc="best")


def _plot_benchmarks(axes, benchmarks, versions, color_map):
    """One panel per matchup — line chart over versions."""
    for ax_idx, (key, title) in enumerate(BENCH_MATCHUPS):
        ax = axes[ax_idx]
        ax.set_title(title, fontsize=10, fontweight="bold")
        ax.set_xlabel("Version", fontsize=8)
        ax.set_ylabel("Win %", fontsize=8)
        ax.set_ylim(0, 105)
        ax.axhline(50, color="gray", linewidth=0.8, linestyle=":", alpha=0.6)
        ax.grid(True, alpha=0.3)

        xs = [v for v in versions if v in benchmarks and key in benchmarks[v]]
        ys = [benchmarks[v][key] for v in xs]

        if not xs:
            ax.text(0.5, 0.5, "No data", transform=ax.transAxes,
                    ha="center", va="center", color="gray", fontsize=9)
            continue

        ax.plot(xs, ys, color="#333333", linewidth=1.8, marker=MARKER,
                markersize=7, zorder=3)
        for x, y, v in zip(xs, ys, xs):
            ax.scatter([x], [y], color=color_map.get(v, "#333333"), s=60, zorder=4)
            ax.annotate(f"{y:.1f}%", (x, y), textcoords="offset points",
                        xytext=(0, 7), ha="center", fontsize=8)

        ax.set_xticks(xs)
        ax.set_xticklabels([f"v{v}" for v in xs], fontsize=8)


def plot(data, benchmarks, versions, out: str) -> None:
    n_train = len(TRAIN_PANELS)
    n_bench = len(BENCH_MATCHUPS)
    ncols = 4

    train_rows = (n_train + ncols - 1) // ncols
    bench_rows = (n_bench + ncols - 1) // ncols
    total_rows = train_rows + bench_rows + 1  # +1 for section label spacing

    fig = plt.figure(figsize=(ncols * 5, total_rows * 3.8))

    color_map = {v: COLORS[i % len(COLORS)] for i, v in enumerate(versions)}

    # --- Training section ---
    fig.text(0.01, 1 - 0.04, "Training metrics (per epoch)", fontsize=12,
             fontweight="bold", va="top")
    train_axes = [
        fig.add_subplot(total_rows, ncols, i + 1)
        for i in range(n_train)
    ]
    _plot_training(train_axes, data, versions, color_map)
    for i in range(n_train, train_rows * ncols):
        fig.add_subplot(total_rows, ncols, i + 1).set_visible(False)

    # --- Benchmark section ---
    bench_start = train_rows * ncols + ncols  # skip one row for label
    fig.text(0.01, 1 - (train_rows + 1) / total_rows - 0.01,
             "Benchmark results (per version)", fontsize=12, fontweight="bold", va="top")
    bench_axes = [
        fig.add_subplot(total_rows, ncols, bench_start + i + 1)
        for i in range(n_bench)
    ]
    _plot_benchmarks(bench_axes, benchmarks, versions, color_map)
    for i in range(n_bench, bench_rows * ncols):
        fig.add_subplot(total_rows, ncols, bench_start + i + 1).set_visible(False)

    fig.suptitle("Twilight Struggle AI — Training & Benchmark history", fontsize=14,
                 fontweight="bold", y=1.02)
    fig.tight_layout(rect=[0, 0, 1, 1])
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=150, bbox_inches="tight")
    print(f"Saved: {out}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--versions", nargs="+", type=int, default=None)
    ap.add_argument("--min-version", type=int, default=21,
                    help="Skip versions older than this (default: 21)")
    ap.add_argument("--out", default="results/training_curves.png")
    args = ap.parse_args()

    if args.versions:
        versions = args.versions
    else:
        seen = set()
        # Primary: /tmp pipeline logs (have epoch-level training metrics)
        for p in glob.glob("/tmp/pipeline_v*.log"):
            m = re.search(r"v(\d+)", p)
            if m and "launch" not in p:
                seen.add(int(m.group(1)))
        # Fallback: checkpoint dirs (survive /tmp wipe, but no training metrics)
        for p in glob.glob("data/checkpoints/retrain_v*/baseline_best.pt"):
            m = re.search(r"retrain_v(\d+)/", p)
            if m and "_" not in p.split("retrain_v")[1].split("/")[0]:
                seen.add(int(m.group(1)))
        # Fallback: durable benchmark history
        hist_path = Path("results/benchmark_history.json")
        if hist_path.exists():
            import json
            for key in json.loads(hist_path.read_text()):
                try:
                    seen.add(int(key.lstrip("v")))
                except ValueError:
                    pass
        versions = sorted(v for v in seen if v >= args.min_version)
        print(f"Found versions (>= v{args.min_version}): {versions}")

    print("Loading training data...")
    data = load_versions(versions)
    print("Loading benchmarks...")
    benchmarks = load_benchmarks(versions)
    for v, b in benchmarks.items():
        print(f"  v{v}: {b}")

    if not data and not benchmarks:
        print("No data found.")
        return

    plot(data, benchmarks, versions, args.out)


if __name__ == "__main__":
    main()
