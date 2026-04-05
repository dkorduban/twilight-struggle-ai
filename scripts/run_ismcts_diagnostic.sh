#!/bin/bash
# ISMCTS diagnostic benchmark: measures search uplift on USSR and US sides.
# Runs 100 games/side at 8 determinizations × 400 simulations.
# Estimated runtime: ~5-11 hours on CPU (depends on game length).
#
# Usage: nice -n 19 bash scripts/run_ismcts_diagnostic.sh
set -e
cd "$(dirname "$0")/.."

MODEL="${MODEL:-data/checkpoints/v99_saturation_1x_95ep/baseline_best_scripted.pt}"
N_GAMES="${N_GAMES:-100}"
N_DET="${N_DET:-8}"
N_SIM="${N_SIM:-400}"
RESULTS_FILE="results/ismcts_diagnostic.txt"

echo "[ismcts] Model: $MODEL"
echo "[ismcts] Config: ${N_DET}det × ${N_SIM}sims, ${N_GAMES} games/side"
echo "[ismcts] Results → $RESULTS_FILE"
echo "[ismcts] Started: $(date '+%Y-%m-%d %H:%M:%S')"

PYTHONPATH=build-ninja/bindings nice -n 19 uv run python -c "
import tscore, math, time, sys

model = '$MODEL'
n_games = $N_GAMES
n_det = $N_DET
n_sim = $N_SIM

print(f'[ismcts] Running USSR side ({n_games} games)...')
t0 = time.time()
ussr_results = tscore.benchmark_ismcts(model, tscore.Side.USSR, n_games,
    n_determinizations=n_det, n_simulations=n_sim, seed=42)
ussr_elapsed = time.time() - t0
ussr_wins = sum(1 for r in ussr_results if r.winner == tscore.Side.USSR)
ussr_pct = ussr_wins / n_games * 100
se_u = math.sqrt(ussr_pct/100*(1-ussr_pct/100)/n_games)*100
print(f'[ismcts] USSR done in {ussr_elapsed/60:.1f}min: {ussr_pct:.1f}% ±{se_u:.1f}')

print(f'[ismcts] Running US side ({n_games} games)...')
t0 = time.time()
us_results = tscore.benchmark_ismcts(model, tscore.Side.US, n_games,
    n_determinizations=n_det, n_simulations=n_sim, seed=4200)
us_elapsed = time.time() - t0
us_wins = sum(1 for r in us_results if r.winner == tscore.Side.US)
us_pct = us_wins / n_games * 100
se_s = math.sqrt(us_pct/100*(1-us_pct/100)/n_games)*100

comb = (ussr_wins + us_wins) / (n_games * 2) * 100
se_c = math.sqrt((ussr_pct/100*(1-ussr_pct/100) + us_pct/100*(1-us_pct/100))/(4*n_games))*100

print()
print(f'=== ISMCTS {n_det}det×{n_sim}sims ({n_games} games/side) ===')
print(f'USSR: {ussr_pct:.1f}% ±{se_u:.1f}  (raw policy baseline: 46.2%)')
print(f'US:   {us_pct:.1f}% ±{se_s:.1f}  (raw policy baseline: 13.0%)')
print(f'Combined: {comb:.1f}% ±{se_c:.1f}  (raw policy baseline: 29.5%)')
print(f'Total time: {(ussr_elapsed+us_elapsed)/60:.1f}min')
print(f'Per game: {(ussr_elapsed+us_elapsed)/(n_games*2):.1f}s')
" 2>&1 | tee "$RESULTS_FILE"

echo "[ismcts] Finished: $(date '+%Y-%m-%d %H:%M:%S')"
