# Snakefile — experiment pipeline for training, exporting, and benchmarking models.
#
# Usage:
#   uv run snakemake -j4 --resources gpu=1 bench=1   # run all experiments
#   uv run snakemake -j1                              # fully sequential (safe)
#   uv run snakemake results/bench/v99_nash_c_95ep_s42.txt  # single experiment
#   uv run snakemake -n                               # dry run
#
# Resource constraints:
#   gpu=1  — at most 1 training job at a time (GPU memory)
#   bench=1 — at most 1 benchmark at a time (CPU/RAM bound)
#   Training and benchmarking CAN overlap (different resources).

import os
import yaml

# ---------------------------------------------------------------------------
# Load experiment definitions from experiments.yaml
# ---------------------------------------------------------------------------
with open("experiments.yaml") as _f:
    _cfg = yaml.safe_load(_f)

_defaults = _cfg["defaults"]
_bench = _cfg["benchmark"]

# name → (data_dir, seed)
EXPERIMENTS = {
    name: (exp["data_dir"], exp["seed"])
    for name, exp in _cfg["experiments"].items()
}

# Common training hyperparams derived from defaults
TRAIN_ARGS = (
    f"--epochs {_defaults['epochs']} "
    f"--batch-size {_defaults['batch_size']} "
    f"--lr {_defaults['lr']} "
    f"--weight-decay {_defaults['weight_decay']} "
    f"--label-smoothing {_defaults['label_smoothing']} "
    f"{'--one-cycle ' if _defaults['one_cycle'] else ''}"
    f"--hidden-dim {_defaults['hidden_dim']} "
    f"--value-target {_defaults['value_target']} "
    f"--patience {_defaults['patience']} "
    f"{'--deterministic-split' if _defaults['deterministic_split'] else ''}"
).strip()

BENCH_GAMES = _bench["games_per_side"]
BENCH_POOL = _bench["pool_size"]
BENCH_SEED = _bench["seed"]

# ---------------------------------------------------------------------------
# Default target: all benchmarks
# ---------------------------------------------------------------------------
rule all:
    input:
        expand("results/bench/{name}.txt", name=EXPERIMENTS.keys())

# ---------------------------------------------------------------------------
# Step 1: Train → checkpoint
# ---------------------------------------------------------------------------
rule train:
    output:
        ckpt="data/checkpoints/{name}/baseline_best.pt"
    params:
        data_dir=lambda wc: EXPERIMENTS[wc.name][0],
        seed=lambda wc: EXPERIMENTS[wc.name][1],
        train_args=TRAIN_ARGS
    resources:
        gpu=1
    log:
        "results/logs/{name}_train.log"
    shell:
        """
        uv run python scripts/train_baseline.py \
            --data-dir {params.data_dir} \
            --out-dir data/checkpoints/{wildcards.name} \
            --seed {params.seed} \
            {params.train_args} \
            2>&1 | tee {log}
        """

# ---------------------------------------------------------------------------
# Step 2: Export to TorchScript
# ---------------------------------------------------------------------------
rule export:
    input:
        ckpt="data/checkpoints/{name}/baseline_best.pt"
    output:
        scripted="data/checkpoints/{name}/baseline_best_scripted.pt"
    log:
        "results/logs/{name}_export.log"
    shell:
        """
        uv run python cpp/tools/export_baseline_to_torchscript.py \
            --checkpoint {input.ckpt} \
            --out {output.scripted} \
            2>&1 | tee {log}
        """

# ---------------------------------------------------------------------------
# Step 3a: Benchmark one side (checkpointed — each side saved independently)
# ---------------------------------------------------------------------------
rule bench_side:
    input:
        scripted="data/checkpoints/{name}/baseline_best_scripted.pt"
    output:
        result="results/bench/{name}_{side}.json"
    params:
        n=BENCH_GAMES,
        pool=BENCH_POOL,
        seed=lambda wc: BENCH_SEED if wc.side == "ussr" else BENCH_SEED + BENCH_GAMES
    resources:
        bench=1
    log:
        "results/logs/{name}_bench_{side}.log"
    shell:
        """
        PYTHONPATH=build-ninja/bindings uv run python -c "
import tscore, json, tempfile, os
n = {params.n}
side = tscore.Side.USSR if '{wildcards.side}' == 'ussr' else tscore.Side.US
results = tscore.benchmark_batched('{input.scripted}', side, n, pool_size={params.pool}, seed={params.seed})
wins = sum(1 for r in results if r.winner == side)
data = {{'side': '{wildcards.side}', 'wins': wins, 'games': n, 'pct': wins/n*100}}
# Atomic write: temp file then rename (no partial files on kill)
fd, tmp = tempfile.mkstemp(dir=os.path.dirname('{output.result}'), suffix='.tmp')
with os.fdopen(fd, 'w') as f:
    json.dump(data, f)
os.rename(tmp, '{output.result}')
pct = wins/n*100
print('{wildcards.name} {wildcards.side}: {{wins}}/{{n}} = {{pct:.1f}}%'.format(wins=wins, n=n, pct=pct))
" 2>&1 | tee {log}
        """

# ---------------------------------------------------------------------------
# Step 3b: Merge both sides into final result
# ---------------------------------------------------------------------------
rule bench_merge:
    input:
        ussr="results/bench/{name}_ussr.json",
        us="results/bench/{name}_us.json"
    output:
        result="results/bench/{name}.txt"
    run:
        import json, math
        ussr = json.load(open(input.ussr))
        us = json.load(open(input.us))
        n = ussr["games"]
        up, sp = ussr["pct"], us["pct"]
        cp = (ussr["wins"] + us["wins"]) / (2 * n) * 100
        use = math.sqrt(up/100*(1-up/100)/n)*100
        sse = math.sqrt(sp/100*(1-sp/100)/n)*100
        cse = math.sqrt((up/100*(1-up/100)+sp/100*(1-sp/100))/(4*n))*100
        line = f'{wildcards.name} | USSR {up:.1f}% +/-{use:.1f} | US {sp:.1f}% +/-{sse:.1f} | Combined {cp:.1f}% +/-{cse:.1f}'
        print(line)
        with open(output.result, 'w') as f:
            f.write(line + '\n')

# ---------------------------------------------------------------------------
# Convenience: prepare symlink data dirs for single-file experiments
# ---------------------------------------------------------------------------
rule setup_data_dirs:
    output:
        touch("data/nash_c_only/.ready"),
        touch("data/nash_b_only/.ready")
    shell:
        """
        mkdir -p data/nash_c_only data/nash_b_only
        ln -sf "$(pwd)/data/combined_v99_clean/heuristic_nash_c.parquet" data/nash_c_only/heuristic_nash_c.parquet
        ln -sf "$(pwd)/data/combined_v99_clean/heuristic_nash_b.parquet" data/nash_b_only/heuristic_nash_b.parquet
        """

# ---------------------------------------------------------------------------
# Summary: print all benchmark results
# ---------------------------------------------------------------------------
rule summary:
    input:
        expand("results/bench/{name}.txt", name=EXPERIMENTS.keys())
    shell:
        """
        echo "=== Benchmark Results ==="
        cat {input}
        echo ""
        echo "=== Reference Baselines ==="
        echo "v99_saturation_1x_95ep (nash_b, s42) | USSR 46.2% +/-1.1 | US 13.0% +/-0.8 | Combined 29.5% +/-0.7"
        echo "v99_saturation_2x_47ep (nash_b+c, s42) | USSR 42.1% +/-1.1 | US 11.6% +/-0.7 | Combined 26.9% +/-0.7"
        echo "v99_baseline_2x95ep (nash_b+c, s42) | USSR 36.0% +/-1.1 | US 9.0% +/-0.6 | Combined 22.5% +/-0.6"
        """
