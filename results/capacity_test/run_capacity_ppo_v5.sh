#!/bin/bash
set -e

# Capacity test v5: Clean panel-only training (no self-play inflation).
#
# Fixes from Opus analysis of v4:
#   1. --no-league-self-slot: 100% panel opponents, no self-play inflation
#   2. --league-save-every 999: no snapshots added to pool
#   3. --lr-schedule constant: no cosine decay (v4 froze by iter 50)
#   4. rollout_wr_panel logged separately in W&B for clean signal
#   5. Baseline benchmark of v56 run FIRST for before/after comparison

V56_CKPT="data/checkpoints/ppo_v56_league/ppo_best_6mode.pt"

# Panel pool: 5 models + heuristic (same as v4 for comparability)
PANEL_FIX="data/checkpoints/scripted_for_elo/v56_scripted.pt data/checkpoints/scripted_for_elo/v54_scripted.pt data/checkpoints/scripted_for_elo/v44_scripted.pt data/checkpoints/scripted_for_elo/v20_scripted.pt data/checkpoints/scripted_for_elo/v55_scripted.pt __heuristic__"

mkdir -p results/capacity_test/ppo_ussr_only_v5 results/capacity_test/ppo_us_only_v5

# ── Step 0: Baseline benchmark of v56 (both sides, vs heuristic + panel) ─
# This provides the "before" numbers that v4 was missing.
echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Running v56 baseline benchmark (vs heuristic + panel models)"

PYTHONPATH=build-ninja/bindings uv run python -c "
import tscore

V56 = 'data/checkpoints/scripted_for_elo/v56_scripted.pt'

# v56 vs heuristic (primary benchmark, per-side)
print('=== v56 vs heuristic ===')
for side_name, side in [('ussr', tscore.Side.USSR), ('us', tscore.Side.US)]:
    results = tscore.benchmark_batched(V56, side, 1000, seed=50000)
    wins = sum(1 for r in results if r.winner == side)
    wr = wins / len(results)
    print(f'  {side_name}: {wins}/{len(results)} = {wr:.3f}')

# v56 vs each panel model (same opponents as training, 400 games each = 200/side)
panel_models = {
    'v20': 'data/checkpoints/scripted_for_elo/v20_scripted.pt',
    'v44': 'data/checkpoints/scripted_for_elo/v44_scripted.pt',
    'v54': 'data/checkpoints/scripted_for_elo/v54_scripted.pt',
    'v55': 'data/checkpoints/scripted_for_elo/v55_scripted.pt',
    'v56': 'data/checkpoints/scripted_for_elo/v56_scripted.pt',
}
print('=== v56 vs panel models (400 games each, split by side) ===')
for opp_name, opp_path in panel_models.items():
    results = tscore.benchmark_model_vs_model_batched(V56, opp_path, n_games=400, seed=50000)
    # First half: v56=USSR, second half: v56=US
    half = len(results) // 2
    ussr_wins = sum(1 for r in results[:half] if r.winner == tscore.Side.USSR)
    us_wins = sum(1 for r in results[half:] if r.winner == tscore.Side.US)
    print(f'  vs {opp_name}: ussr={ussr_wins}/{half}={ussr_wins/max(1,half):.3f}  us={us_wins}/{half}={us_wins/max(1,half):.3f}')
" | tee results/capacity_test/v56_baseline_benchmark.txt

echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Baseline complete. Starting USSR-only v5."

# ── Step 1: USSR-only PPO, panel opponents only ──────────────────────────
PYTHONPATH=build-ninja/bindings nice -n 10 uv run python scripts/train_ppo.py \
  --checkpoint "$V56_CKPT" \
  --out-dir results/capacity_test/ppo_ussr_only_v5 \
  --side ussr \
  --n-iterations 50 \
  --games-per-iter 200 \
  --lr 5e-5 --clip-eps 0.12 \
  --lr-schedule constant \
  --ent-coef 0.01 --ent-coef-final 0.003 \
  --global-ent-decay-start 0 --global-ent-decay-end 300 \
  --max-kl 0.03 \
  --ema-decay 0.995 \
  --upgo \
  --reset-optimizer \
  --league results/capacity_test/ppo_ussr_only_v5 \
  --no-league-self-slot \
  --league-save-every 999 \
  --league-mix-k 6 \
  --league-fixtures $PANEL_FIX \
  --league-fixture-fadeout 999 \
  --pfsp-exponent 0.5 \
  --heuristic-floor 0.15 \
  --device cuda \
  --wandb \
  --wandb-run-name capacity_ussr_only_v5 \
  --skip-smoke-test

echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] USSR-only v5 done. Starting US-only v5."

# ── Step 2: US-only PPO, panel opponents only ────────────────────────────
PYTHONPATH=build-ninja/bindings nice -n 10 uv run python scripts/train_ppo.py \
  --checkpoint "$V56_CKPT" \
  --out-dir results/capacity_test/ppo_us_only_v5 \
  --side us \
  --n-iterations 50 \
  --games-per-iter 200 \
  --lr 5e-5 --clip-eps 0.12 \
  --lr-schedule constant \
  --ent-coef 0.01 --ent-coef-final 0.003 \
  --global-ent-decay-start 0 --global-ent-decay-end 300 \
  --max-kl 0.03 \
  --ema-decay 0.995 \
  --upgo \
  --reset-optimizer \
  --league results/capacity_test/ppo_us_only_v5 \
  --no-league-self-slot \
  --league-save-every 999 \
  --league-mix-k 6 \
  --league-fixtures $PANEL_FIX \
  --league-fixture-fadeout 999 \
  --pfsp-exponent 0.5 \
  --heuristic-floor 0.15 \
  --device cuda \
  --wandb \
  --wandb-run-name capacity_us_only_v5 \
  --skip-smoke-test

echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Both v5 runs complete."

# ── Step 3: Post-training benchmark of best checkpoints ──────────────────
echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Running post-training benchmarks..."

PYTHONPATH=build-ninja/bindings uv run python -c "
import tscore, os
from tsrl.policies.minimal_hybrid import load_model, export_torchscript

V56 = 'data/checkpoints/scripted_for_elo/v56_scripted.pt'
panel_models = {
    'v20': 'data/checkpoints/scripted_for_elo/v20_scripted.pt',
    'v44': 'data/checkpoints/scripted_for_elo/v44_scripted.pt',
    'v54': 'data/checkpoints/scripted_for_elo/v54_scripted.pt',
    'v55': 'data/checkpoints/scripted_for_elo/v55_scripted.pt',
    'v56': 'data/checkpoints/scripted_for_elo/v56_scripted.pt',
}

def bench_checkpoint(ckpt_dir, target_side_name, target_side):
    best = os.path.join(ckpt_dir, 'ppo_best.pt')
    if not os.path.exists(best):
        print(f'  {ckpt_dir}: no ppo_best.pt found')
        return
    # Export to TorchScript for benchmarking
    model_raw = load_model(best, device='cpu')
    ts_path = best.replace('.pt', '_scripted.pt')
    export_torchscript(model_raw, ts_path)

    # vs heuristic (primary)
    results = tscore.benchmark_batched(ts_path, target_side, 1000, seed=50000)
    wins = sum(1 for r in results if r.winner == target_side)
    print(f'  vs heuristic as {target_side_name}: {wins}/{len(results)} = {wins/len(results):.3f}')

    # vs each panel model
    for opp_name, opp_path in panel_models.items():
        results = tscore.benchmark_model_vs_model_batched(ts_path, opp_path, n_games=400, seed=50000)
        half = len(results) // 2
        if target_side_name == 'ussr':
            w = sum(1 for r in results[:half] if r.winner == tscore.Side.USSR)
            print(f'  vs {opp_name} as ussr: {w}/{half} = {w/max(1,half):.3f}')
        else:
            w = sum(1 for r in results[half:] if r.winner == tscore.Side.US)
            print(f'  vs {opp_name} as us: {w}/{half} = {w/max(1,half):.3f}')

print('=== USSR-only v5 checkpoint ===')
bench_checkpoint('results/capacity_test/ppo_ussr_only_v5', 'ussr', tscore.Side.USSR)
print('=== US-only v5 checkpoint ===')
bench_checkpoint('results/capacity_test/ppo_us_only_v5', 'us', tscore.Side.US)
" | tee -a results/capacity_test/v5_post_benchmark.txt

echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] All capacity test v5 steps complete."
echo "Compare v56_baseline_benchmark.txt vs v5_post_benchmark.txt for capacity delta."
