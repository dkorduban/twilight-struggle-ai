  ---
  Manual Experiment Guide — Twilight Struggle AI

  Prerequisites

  Build the C++ engine

  cd /home/dkord/code/twilight-struggle-ai
  cmake -S . -B build-ninja -G Ninja -DCMAKE_BUILD_TYPE=RelWithDebInfo
  nice -n 15 cmake --build build-ninja -j4   # always nice -n 15, avoids OOM on 17G swap
  Produces build-ninja/bindings/tscore.cpython-312-x86_64-linux-gnu.so. All Python code imports this.

  W&B login

  The API key lives in .wandb-api-key.txt (project root). train_ppo.py reads it automatically when --wandb is passed — no manual wandb login needed. If you want to log in interactively anyway:
  uv run wandb login   # paste key from .wandb-api-key.txt
  Project: twilight-struggle-ai, entity: korduban-ai. Runs appear at https://wandb.ai/korduban-ai/twilight-struggle-ai.

  Export a model for C++ inference

  The C++ engine only accepts TorchScript (.pt saved with torch.jit.save). Plain ppo_best.pt checkpoints are training-only.
  uv run python cpp/tools/export_baseline_to_torchscript.py \
      --checkpoint data/checkpoints/ppo_v267_sc_league/ppo_best.pt \
      --out data/checkpoints/scripted_for_elo/v267_sc_scripted.pt
  This script auto-detects the actual scalar dim from the checkpoint weights and traces with the right shapes — unlike the hardcoded trace in _export_torchscript_model. Always use this script for
  Elo/benchmark exports.

  ---
  Running a PPO training run manually

  The full command ppo_loop_step.sh would generate is:

  uv run python scripts/train_ppo.py \
      --checkpoint data/checkpoints/ppo_v267_sc_league/ppo_best.pt \
      --out-dir data/checkpoints/ppo_v292_sc_league \
      --n-iterations 30 \
      --games-per-iter 200 \
      --lr 5e-5 \
      --clip-eps 0.12 \
      --ent-coef 0.01 \
      --ent-coef-final 0.003 \
      --global-ent-decay-start 0 \
      --global-ent-decay-end 300 \
      --max-kl 0.03 \
      --reset-optimizer \
      --league data/checkpoints/ppo_v292_sc_league \
      --league-save-every 10 \
      --league-mix-k 6 \
      --ussr-league-fixtures \
          data/checkpoints/scripted_for_elo/v267_sc_scripted.pt \
          data/checkpoints/scripted_for_elo/v266_sc_scripted.pt \
          data/checkpoints/scripted_for_elo/v265_sc_scripted.pt \
          __heuristic__ \
      --us-league-fixtures \
          data/checkpoints/scripted_for_elo/v267_sc_scripted.pt \
          data/checkpoints/scripted_for_elo/v263_sc_scripted.pt \
          __heuristic__ \
      --league-fixtures \
          data/checkpoints/scripted_for_elo/v267_sc_scripted.pt \
          __heuristic__ \
      --league-recency-tau 50 \
      --league-fixture-fadeout 999 \
      --pfsp-exponent 0.5 \
      --eval-every 10 \
      --rollout-workers 1 \
      --device cuda \
      --wandb \
      --wandb-run-name ppo_v292_sc \
      --upgo \
      --skip-smoke-test \
      >> results/logs/ppo/ppo_v292_sc.log 2>&1

  Key flags explained

  ┌──────────────────────────────────────────────┬─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
  │                     Flag                     │                                                                    What it does                                                                     │
  ├──────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ --checkpoint                                 │ Resume from this .pt file. Must be ppo_best.pt or ppo_final.pt — never *_scripted.pt (scripted files crash on torch.load).                          │
  ├──────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ --reset-optimizer                            │ Start fresh Adam state. Required when switching checkpoint source (different model, architecture change). Omit to continue training from same run.  │
  ├──────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ --out-dir                                    │ All iter checkpoints, ppo_final.pt, ppo_running_best.pt, wr_table.json go here.                                                                     │
  ├──────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ --n-iterations 30                            │ 30 × 200 = 6000 games per run. About 25-35 minutes on RTX 3050.                                                                                     │
  ├──────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ --games-per-iter 200                         │ Games collected per PPO iteration. More = more stable but slower.                                                                                   │
  ├──────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ --league                                     │ Directory of past-self checkpoints for PFSP opponent sampling. Same as --out-dir.                                                                   │
  ├──────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ --league-save-every 10                       │ Save iter_NNNN.pt to the league pool every 10 iters (+ always at iter 1).                                                                           │
  ├──────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ --league-mix-k 6                             │ Use 6 opponent slots total (1 self + 2 USSR fixtures + 2 US fixtures + 1 heuristic each side).                                                      │
  ├──────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ --ussr-league-fixtures /                     │ Per-side fixture pools. Use __heuristic__ for heuristic opponent.                                                                                   │
  │ --us-league-fixtures                         │                                                                                                                                                     │
  ├──────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ --league-fixture-fadeout 999                 │ Fixtures never fade (999 > max iterations).                                                                                                         │
  ├──────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ --pfsp-exponent 0.5                          │ UCB exploration constant for PFSP opponent selection. 0.5 = current calibrated value.                                                               │
  ├──────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ --ent-coef 0.01 / --ent-coef-final 0.003     │ Entropy regularization: starts at 0.01, decays to 0.003 over global-ent-decay-end - global-ent-decay-start global iterations.                       │
  ├──────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ --global-ent-decay-start/end                 │ Chained run: set start to total iterations done so far so decay is continuous across restarts.                                                      │
  ├──────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ --max-kl 0.03                                │ Abort PPO update if KL divergence > 0.03. Prevents catastrophic policy collapse.                                                                    │
  ├──────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ --upgo                                       │ UPGO (Upgoing Policy Update): uses MC returns as advantage when they exceed GAE. Empirically helpful.                                               │
  ├──────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ --skip-smoke-test                            │ Skip 10-game pre-training benchmark. Required when restarting from a checkpoint with a different C++ binary version (scripted sibling would be      │
  │                                              │ stale).                                                                                                                                             │
  ├──────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ --eval-every 10                              │ Run panel evaluation at iters 10, 20, 30. Requires --eval-panel paths.                                                                              │
  ├──────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ --probe-set / --probe-every                  │ JSD probe evaluation (skip if data/probe_positions.parquet doesn't exist — training handles gracefully).                                            │
  └──────────────────────────────────────────────┴─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

  What train_ppo.py does internally

  1. Load checkpoint → extract model weights into Python PyTorch model
  2. Smoke test (unless --skip-smoke-test) → 10 C++ benchmark games to verify model works
  3. Iteration loop for N iterations:
    - Save current model to league pool as iter_NNNN.pt (TorchScript via torch.jit.script → fallback to torch.jit.trace)
    - Select opponents via PFSP: weight = (1 - WR_side)^pfsp + UCB bonus; higher PFSP = more games against weak-spot opponents
    - Collect 200 games via C++ rollout_model_vs_model_batched in threads (self + k fixtures per side)
    - PPO update: clip ratio = 0.12, max KL = 0.03, 4 PPO epochs, minibatch 256
    - Log metrics to W&B: card_loss, mode_loss, country_loss, value_loss, entropy, clip_frac, explained_variance, rollout WR per opponent
    - Every 10 iters: panel eval + post_train_confirm.sh --incremental for Elo placement
    - Track running best checkpoint (by combined WR vs panel)
  4. Save ppo_final.pt → watcher sees this and auto-launches next run via ppo_loop_step.sh

  Checkpoint files produced

  data/checkpoints/ppo_v292_sc_league/
  ├── iter_0001.pt            # TorchScript — league pool member (auto-loaded by C++ as opponent)
  ├── iter_0010.pt            # milestone iter (kept even with rolling deletion)
  ├── iter_0020.pt
  ├── iter_0030.pt
  ├── ppo_running_best.pt     # standard torch.save checkpoint — best combined WR so far
  ├── ppo_best.pt             # symlink/copy of ppo_running_best.pt
  ├── ppo_best_scripted.pt    # TorchScript export of ppo_best.pt (for Elo ladder)
  ├── ppo_final.pt            # final iter checkpoint (triggers watcher)
  ├── wr_table.json           # per-opponent win-rate history for PFSP
  ├── snakemake_train_config.yaml
  ├── ppo_args.json
  └── wandb_run_id.txt

  CRITICAL: iter_*.pt files in the league pool are TorchScript models (saved with torch.jit.save). ppo_best.pt / ppo_final.pt are standard PyTorch checkpoints (saved with torch.save). Never pass
  *_scripted.pt as --checkpoint — it will crash with AttributeError: 'RecursiveScriptModule' object has no attribute 'get'.

  ---
  Running via the automated chain (ppo_loop_step.sh)

  ppo_loop_step.sh wraps snakemake and sets up the watcher:

  bash scripts/ppo_loop_step.sh v291_sc v292_sc

  - Reads results/checkpoint_override_v292_sc.txt if it exists (overrides the default checkpoint)
  - Reads results/selected_fixtures.json for the fixture pool
  - Writes data/checkpoints/ppo_v292_sc_league/snakemake_train_config.yaml
  - Runs uv run snakemake --snakefile Snakefile.ppo --config train_config=<yaml> ppo_train_dynamic
  - Launches a watcher process in background — when ppo_final.pt appears, auto-runs next iteration
  - Launches post_train_confirm.sh --incremental in background for Elo placement after training

  To create a checkpoint override (e.g. restart from a peak):
  echo "data/checkpoints/ppo_v267_sc_league/ppo_best.pt" > results/checkpoint_override_v292_sc.txt

  ---
  Benchmarking a model

  # Export to TorchScript first
  uv run python cpp/tools/export_baseline_to_torchscript.py \
      --checkpoint data/checkpoints/ppo_v267_sc_league/ppo_best.pt \
      --out /tmp/v267_test_scripted.pt

  # Run benchmark
  PYTHONPATH=build-ninja/bindings uv run python -c "
  import tscore
  m_path = '/tmp/v267_test_scripted.pt'
  r_ussr = tscore.benchmark_batched(m_path, tscore.Side.USSR, 500, pool_size=32, seed=50000, nash_temperatures=True)
  r_us   = tscore.benchmark_batched(m_path, tscore.Side.US,   500, pool_size=32, seed=50500, nash_temperatures=True)
  ussr_wr = sum(1 for r in r_ussr if r.winner == tscore.Side.USSR) / 500
  us_wr   = sum(1 for r in r_us   if r.winner == tscore.Side.US)   / 500
  print(f'USSR WR: {ussr_wr:.1%}  US WR: {us_wr:.1%}  Combined: {(ussr_wr+us_wr)/2:.1%}')
  "

  Note: benchmark_batched takes model_path: str (path to scripted model), NOT a model object. Canonical seeds: USSR=50000, US=50500.

  ---
  Elo placement

  # Incremental (fast, ~5 minutes — use after every training run)
  bash scripts/post_train_confirm.sh data/checkpoints/ppo_v292_sc_league --incremental

  # Dry-run to preview what it will do
  bash scripts/post_train_confirm.sh data/checkpoints/ppo_v292_sc_league --dry-run

  # Full ladder rebuild (100+ matches, >1 hour — manual only)
  bash scripts/post_train_confirm.sh data/checkpoints/ppo_v292_sc_league --full

  Writes results to results/elo/elo_full_ladder.json. Current all-time peak: v267_sc = 1938 Elo.

  ---
  Running the C++ tests

  ctest --test-dir build-ninja --output-on-failure   # all 51 tests
  ctest --test-dir build-ninja --output-on-failure -R mcts  # just MCTS tests

  ---
  Known issues / gotchas

  1. _export_torchscript_model in train_ppo.py uses hardcoded SCALAR_DIM=32 for the trace fallback, but v267_sc and later models have scalar_encoder expecting 74 inputs. If torch.jit.script fails, the
  trace fallback fails too, and warn_only=True means no error is raised — it silently doesn't write the file. Always use cpp/tools/export_baseline_to_torchscript.py for manual exports (it detects the
  real dim).
  2. benchmark_batched signature changed — now takes model_path: str, not a model object. Old code patterns tscore.benchmark_batched(model, side, n) crash with TypeError.
  3. rollout_model_vs_model_batched also takes model_a_path: str, model_b_path: str — both must be paths to TorchScript files.
  4. League pool iter_*.pt files are TorchScript (saved by _export_torchscript_model). If that export fails silently, the C++ will crash when loading the opponent.
  5. results/autonomous_decisions.log is the audit trail for all automated actions. Check it first when diagnosing why a run failed.
  
  ---
  Running Evaluations, Tournaments, and Head-to-Head Matches

  Quick sanity: does my model beat heuristic?

  PYTHONPATH=build-ninja/bindings uv run python -c "
  import tscore
  # model_path must be a *_scripted.pt file
  m = 'data/checkpoints/scripted_for_elo/v267_sc_scripted.pt'
  r_ussr = tscore.benchmark_batched(m, tscore.Side.USSR, 200, pool_size=32, seed=50000, nash_temperatures=True)
  r_us   = tscore.benchmark_batched(m, tscore.Side.US,   200, pool_size=32, seed=50500, nash_temperatures=True)
  ussr_wr = sum(1 for r in r_ussr if r.winner == tscore.Side.USSR) / 200
  us_wr   = sum(1 for r in r_us   if r.winner == tscore.Side.US)   / 200
  print(f'USSR WR: {ussr_wr:.1%}  US WR: {us_wr:.1%}  Combined: {(ussr_wr+us_wr)/2:.1%}')
  "

  Canonical eval seeds: USSR = 50000, US = 50500. Always use these for comparable numbers. nash_temperatures=True makes the heuristic opponent use its actual mixed strategy (matches training
  distribution).

  Heuristic ceiling: ~83% USSR WR, ~17% US WR combined (~50%). Anything above 50% combined means you're beating heuristic on both sides. v267_sc: 1938 Elo (see ladder section for context).

  ---
  Head-to-head: model A vs model B

  The C++ binding rollout_model_vs_model_batched runs N games, both sides, and returns step data + results. Both models must be TorchScript:

  PYTHONPATH=build-ninja/bindings uv run python -c "
  import tscore, sys

  model_a = 'data/checkpoints/scripted_for_elo/v267_sc_scripted.pt'
  model_b = 'data/checkpoints/scripted_for_elo/v266_sc_scripted.pt'
  n = 200  # must be even; half each side

  results, steps, boundaries = tscore.rollout_model_vs_model_batched(
      model_a_path=model_a,
      model_b_path=model_b,
      n_games=n,
      pool_size=32,
      seed=1000,
      device='cpu',
      temperature=0.0,         # 0=greedy, 1.0=sampling
      nash_temperatures=False,
      learned_side=tscore.Side.Neutral,  # alternating sides
  )

  wins_a = sum(1 for i, r in enumerate(results) if r.winner == (tscore.Side.USSR if i < n//2 else tscore.Side.US))
  print(f'model_a wins: {wins_a}/{n} = {wins_a/n:.1%}')
  # For quick win count when model_a always plays USSR:
  # results, _, _ = tscore.rollout_model_vs_model_batched(..., learned_side=tscore.Side.USSR)
  # wins = sum(1 for r in results if r.winner == tscore.Side.USSR)
  "

  For a simpler head-to-head with just win counts, post_train_confirm.sh and run_elo_tournament.py handle this automatically.

  ---
  Elo tournament: place one new model vs the ladder

  This is the standard post-training flow. Three steps:

  Step 1: Candidate tournament — find the best checkpoint within a run

  uv run python scripts/ppo_confirm_best.py \
      --run-dir data/checkpoints/ppo_v292_sc_league \
      --fixtures \
          "v209_sc:data/checkpoints/scripted_for_elo/v209_sc_scripted.pt" \
          "v217_sc:data/checkpoints/scripted_for_elo/v217_sc_scripted.pt" \
          "v232_sc:data/checkpoints/scripted_for_elo/v232_sc_scripted.pt" \
          "v228_sc:data/checkpoints/scripted_for_elo/v228_sc_scripted.pt" \
          "v227_sc:data/checkpoints/scripted_for_elo/v227_sc_scripted.pt" \
      --n-top 8 \
      --n-games 150 \
      --anchor v209_sc --anchor-elo 1875 \
      --script-dir data/checkpoints/scripted_for_elo \
      2>&1 | tee results/logs/elo/confirm_v292_sc.log

  This reads panel_eval_history.json from the run directory, picks the top-8 checkpoints by panel WR, runs round-robin among them, and copies the winner to ppo_best.pt / ppo_best_scripted.pt.

  Step 2: Incremental Elo placement — place ppo_best against ladder

  bash scripts/post_train_confirm.sh \
      data/checkpoints/ppo_v292_sc_league \
      --incremental \
      2>&1 | tee results/logs/elo/elo_v292_sc_update.log

  What --incremental does:
  1. Panel (5 models × 150 games each) → already cached from Step 1, plays 0 new games
  2. 3 diverse opponents (bottom-quartile, median, top of 6-mode ladder) × 200 games each
  3. Fits BayesElo on all results, writes only v292_sc's rating to results/elo/elo_full_ladder.json
  4. Prints: Done. v292_sc: elo=XXXX elo_ussr=XXXX elo_us=XXXX

  Step 3: Verify

  python3 -c "
  import json
  d = json.load(open('results/elo/elo_full_ladder.json'))
  r = d['ratings'].get('v292_sc', {})
  print(f'v292_sc: elo={r.get(\"elo\",\"?\")} ussr={r.get(\"elo_ussr\",\"?\")} us={r.get(\"elo_us\",\"?\")}')
  # Top 6-mode models for context:
  import re
  sc = [(n,i) for n,i in d['ratings'].items() if re.match(r'v(\d+)_sc$',n) and int(re.match(r'v(\d+)_sc$',n).group(1))>=205]
  sc.sort(key=lambda x: x[1].get('elo',0), reverse=True)
  for name,info in sc[:5]:
      print(f'  {name}: {info.get(\"elo\",0):.0f}')
  "

  ---
  Full ladder rebuild (manual only, never automated)

  Only needed after major changes (new model era, anchor recalibration). Takes >1 hour.

  bash scripts/post_train_confirm.sh data/checkpoints/ppo_v292_sc_league --full
  # OR directly:
  uv run python scripts/run_elo_tournament.py \
      --models \
          heuristic \
          v209_sc:data/checkpoints/scripted_for_elo/v209_sc_scripted.pt \
          v217_sc:data/checkpoints/scripted_for_elo/v217_sc_scripted.pt \
          ... \
          v292_sc:data/checkpoints/ppo_v292_sc_league/ppo_best_scripted.pt \
      --games 400 \
      --anchor v209_sc --anchor-elo 1875 \
      --schedule round_robin \
      --resume-from results/elo/elo_full_ladder.json \
      --out results/elo/elo_full_ladder.json \
      --mode full

  ---
  Querying the match cache (SQLite)

  All match results (paired games) are stored in results/metadata.sqlite3:

  # Recent matches
  sqlite3 results/metadata.sqlite3 "
  SELECT model_a, model_b, wins_a, wins_b, n_games, run_at
  FROM match_cache
  ORDER BY run_at DESC LIMIT 20;
  "

  # Head-to-head between two specific models
  sqlite3 results/metadata.sqlite3 "
  SELECT model_a, model_b, wins_a, wins_b, n_games
  FROM match_cache
  WHERE (model_a='v267_sc' AND model_b='v268_sc')
     OR (model_a='v268_sc' AND model_b='v267_sc');
  "

  # All matches involving v267_sc
  sqlite3 results/metadata.sqlite3 "
  SELECT model_a, model_b, wins_a, wins_b, n_games FROM match_cache
  WHERE model_a='v267_sc' OR model_b='v267_sc'
  ORDER BY run_at DESC;
  "

  run_elo_tournament.py checks this cache before playing any pair — if a pair already has ≥ --games results, it skips that matchup entirely. This means replaying a tournament is cheap as long as the
  models haven't changed.

  ---
  Viewing the Elo ladder

  python3 -c "
  import json, re
  d = json.load(open('results/elo/elo_full_ladder.json'))
  r = d['ratings']

  # All 6-mode _sc models (v205_sc+), sorted by Elo
  sc = [(n, i) for n, i in r.items()
        if re.match(r'v(\d+)_sc$', n) and int(re.match(r'v(\d+)_sc$', n).group(1)) >= 205]
  sc.sort(key=lambda x: x[1].get('elo', 0), reverse=True)
  for name, info in sc[:20]:
      e  = info.get('elo', 0)
      eu = info.get('elo_ussr', 0)
      es = info.get('elo_us', 0)
      print(f'{name:15s}  elo={e:.0f}  ussr={eu:.0f}  us={es:.0f}')
  "

  Current anchors (do not change without Opus analysis):
  - Anchor: v209_sc = 1875 Elo (6-mode era baseline)
  - All-time peak: v267_sc = 1938

  ---
  Tracing a single game (debugging)

  run_traced_game.py runs one game and prints every action with card/mode/country:

  PYTHONPATH=build-ninja/bindings uv run python scripts/run_traced_game.py \
      --model data/checkpoints/scripted_for_elo/v267_sc_scripted.pt \
      --seed 42 \
      --temperature 0.0    # 0=greedy, 1.0=sample

  To trace a heuristic game (no model needed):
  PYTHONPATH=build-ninja/bindings uv run python scripts/run_traced_game.py --heuristic --seed 42

  ---
  Selecting league fixtures for a new training run

  The select_league_fixtures.py script picks a diverse fixture pool using Elo ranking + JSD deduplication (JSD = Jensen-Shannon divergence between policy distributions — high JSD means different
  playstyle):

  # First, build a JSD matrix (requires scripted models of all candidates)
  # results/analysis/jsd_matrix.json — built by compute_jsd_matrix.py

  uv run python scripts/select_league_fixtures.py \
      --elo-ladder results/elo/elo_full_ladder.json \
      --model-dir data/checkpoints/scripted_for_elo \
      --ussr-pool-n 8 \
      --us-pool-n 8 \
      --min-elo 1800 \
      --add-heuristic \
      --show-analysis

  Output is written to results/selected_fixtures.json and is read automatically by ppo_loop_step.sh. If this file doesn't exist, ppo_loop_step.sh falls back to the hardcoded v262–v267 pool.

  ---
  W&B: viewing training metrics

  Go to https://wandb.ai/korduban-ai/twilight-struggle-ai. Key metrics per run:

  ┌──────────────────────────────────────┬──────────────────────────────────────────────────────────────────────────────┐
  │                Metric                │                                What it means                                 │
  ├──────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────────┤
  │ rollout_wr                           │ Combined win rate vs all opponents this iteration (primary real-time signal) │
  ├──────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────────┤
  │ wr/{opponent}                        │ Per-opponent WR — low values = PFSP will up-weight this opponent             │
  ├──────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────────┤
  │ card_loss / mode_loss / country_loss │ Action head policy losses                                                    │
  ├──────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────────┤
  │ value_loss                           │ Value function MSE                                                           │
  ├──────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────────┤
  │ entropy                              │ Policy entropy — watch for collapse (drops near 0)                           │
  ├──────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────────┤
  │ clip_frac                            │ Fraction of PPO steps clipped — >0.3 means too-large updates                 │
  ├──────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────────┤
  │ explained_variance                   │ Value function quality — >0.5 is good                                        │
  ├──────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────────┤
  │ kl_early_stop                        │ 1 if KL exceeded --max-kl and PPO update was aborted                         │
  ├──────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────────┤
  │ panel_wr_combined                    │ Combined WR vs fixed panel (runs every 10 iters)                             │
  ├──────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────────┤
  │ jsd_prev                             │ Jensen-Shannon divergence vs previous checkpoint (when probe active)         │
  └──────────────────────────────────────┴──────────────────────────────────────────────────────────────────────────────┘