# Opus Analysis: Rollout Results in SQL for Tournament Reuse
Date: 2026-04-12T04:30:00Z
Question: Should rollout game results (games collected during PPO training iterations) be saved into the same SQL database as tournament match results, using a unique ID like (run_id, checkpoint_num)? Should we store checkpoint shas and git sha so rollout games can be reused in candidate tournaments and full ladder tournaments? Or is this a bad idea due to possibly different hyperparams like temperature?

## Executive Summary

Rollout game results should **not** be mixed into the tournament `match_results` table for BayesElo computation. The systematic differences — temperature sampling (rollout_temp=1.0-1.2 vs tournament temperature=0.0), Dirichlet exploration noise, PFSP-sampled mixed opponents vs fixed pairings, and tiny per-pair sample sizes (~5-25 games per opponent per iteration vs 200-400 in tournaments) — would corrupt Elo estimates rather than narrow confidence intervals. However, rollout results are valuable for a **separate purpose**: early regression detection and training diagnostics. The right design is a dedicated `rollout_game_results` table with full hyperparam metadata, queryable for trend analysis but explicitly excluded from the BayesElo pipeline.

## Findings

### What hyperparams differ between rollout games and tournament games?

**Temperature.** This is the most important difference. Tournament games use `temperature=0.0` (greedy argmax), which represents the model's true strength. Rollout games use `rollout_temp` which defaults to 1.0 and is often set to 1.2 for exploration. At T=1.2, the model deliberately takes weaker moves to improve training signal diversity. This systematically depresses win rates. Evidence from the codebase:

- `run_elo_tournament.py` line 295: `temperature=0.0` hard-coded for model-vs-model matches
- `train_ppo.py` line 2485, 2495: panel eval during training also uses `temperature=0.0`
- `train_ppo.py` line 735: rollout collection uses `temperature=rollout_temp` (configurable, default 1.0)
- The corrupted-era models v27-v41 were specifically excluded from Elo because they were trained with T=1.2 + log_prob bugs — temperature sensitivity is a known issue

**Dirichlet exploration noise.** Rollout collection injects Dirichlet noise at the MCTS root (`dir_alpha`, `dir_epsilon` args). Tournament matches do not. This further depresses apparent strength.

**PFSP opponent sampling.** Rollout opponents are sampled from a league pool using UCB-weighted PFSP (Prioritized Fictitious Self-Play). The model deliberately plays more games against harder opponents (low WR → high weight). This means the per-opponent game counts are not balanced pairs: a strong opponent might get 50+ games while a weak one gets 5. Tournament scheduling uses round-robin with equal games per pair.

**Self-play slot.** Rollout includes a `__self__` opponent slot (model vs itself), which produces 50/50 results by definition. Tournament never includes self-play.

**Scripted vs live model.** Rollout uses a freshly exported TorchScript model that changes every iteration. Tournament uses a stable scripted checkpoint from `scripted_for_elo/`. The rollout model at iteration N is slightly different from any saved checkpoint because PPO updates happen between collection and the next save.

**Nash temperature flag.** Rollout collection uses `nash_temperatures=True` (lines 736, 808), while tournament heuristic benchmarks use `nash_temperatures=False` (lines 2543-2544). This affects the heuristic opponent's behavior.

### Can rollout results be used for BayesElo?

**No, not reliably.** Three fundamental problems:

1. **Temperature bias is systematic and non-uniform.** A T=1.2 game is not just "noisier" — it shifts the expected win probability differently depending on the position complexity and the model's policy entropy. Two models A and B might have a true greedy Elo gap of 50, but at T=1.2 the gap could be 30 or 70 depending on their policy sharpness. You cannot correct for this with a simple offset because the bias is model-pair-dependent.

2. **PFSP sampling breaks the pairwise comparison assumption.** BayesElo assumes each game in a (A, B) pair is an independent draw from the same distribution. But in rollout, the "A" player at iteration 10 is different from "A" at iteration 100 — the model has been updated between batches. Aggregating wins across iterations conflates different skill levels into one W/L count.

3. **Per-pair sample sizes are too small.** A typical rollout batch has `games_per_slot` games per opponent (configured via `games-per-iter / (2*league_mix_k)`). With 200 games/iter and k=4, that's ~25 games per slot, split across sides → ~12 games per side per opponent per iteration. BayesElo needs ~100+ games per pair to produce useful CIs. While games accumulate across iterations, the model changes every iteration, so they are not from the same player.

4. **The panel eval already provides clean tournament-equivalent data.** The `_panel_eval_worker` function runs at milestones with `temperature=0.0` and fixed opponents — this is essentially a mini-tournament with proper conditions. These results are already usable for Elo.

### What's the practical benefit?

**Volume.** A 400-iteration run with 200 games/iter produces 80,000 total games. With k=4 league slots + heuristic + self-play, roughly 80,000/6 ≈ 13,000 games per opponent type. But these are spread across 400 different model versions, so per-pair-per-version it's only ~25-33 games.

**Regression detection.** The real value is not Elo precision but trend monitoring. If rollout WR against v14 drops from 65% to 45% over 20 iterations, that signals a regression far earlier than waiting for a milestone tournament. The `rollout_stats` table already captures aggregate WR, but per-opponent breakdown would be more informative.

**The `wr_table.json` already stores cumulative per-opponent WR.** The existing `_update_wr_table_from_steps` function tracks `{wins_ussr, total_ussr, wins_us, total_us}` per opponent key. This is not per-iteration though — it's cumulative across the entire run, which conflates early-iteration and late-iteration results.

### Schema implications

If we do add rollout game tracking (recommended for diagnostics, not for Elo):

**Recommended: a separate `rollout_game_results` table, not reusing `match_results`.**

```sql
CREATE TABLE IF NOT EXISTS rollout_game_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id TEXT NOT NULL,           -- e.g. "ppo_v66_sc_league"
    checkpoint_name TEXT NOT NULL,  -- e.g. "ppo_iter0100"
    iter_num INTEGER NOT NULL,
    opponent TEXT NOT NULL,         -- e.g. "v14_scripted", "heuristic", "__self__"
    side TEXT NOT NULL,             -- "ussr" or "us"
    wins INTEGER NOT NULL,
    losses INTEGER NOT NULL,
    n_games INTEGER NOT NULL,
    rollout_temp REAL,
    dir_alpha REAL,
    dir_epsilon REAL,
    nash_temperatures INTEGER,     -- 0/1 boolean
    git_sha TEXT,
    checkpoint_hash TEXT,
    logged_at TEXT NOT NULL
);
```

**Unique ID scheme.** `(run_id, iter_num, opponent, side)` is a natural composite key. No need for a hash-based ID — the run directory name plus iteration number is already unique and human-readable.

**The `matchup_aggregates` view needs no changes** because it only queries `match_results`. A separate `rollout_opponent_trends` view could aggregate rollout data for dashboards.

**Filtering.** The key architectural decision is: **do not put rollout rows into `match_results`** at all. This avoids any risk of them leaking into BayesElo computation. If they were in the same table, every consumer would need to remember to filter by `source_type = 'tournament'`, and one forgotten filter would silently corrupt ratings.

## Conclusions

1. **Do not merge rollout results into `match_results`.** The temperature, exploration noise, PFSP sampling, and per-iteration model drift make rollout games fundamentally incomparable to tournament games. Mixing them would corrupt BayesElo estimates.

2. **The panel eval during training already produces tournament-quality data** (temperature=0.0, fixed opponents, deterministic seeds). If you want more Elo signal during training, increase panel eval frequency rather than trying to reuse rollout games.

3. **Rollout results are valuable for regression detection and training diagnostics.** A dedicated `rollout_game_results` table with per-opponent, per-iteration, per-side granularity would be more useful than the current aggregate `rollout_stats`.

4. **Store hyperparam metadata (rollout_temp, dir_alpha, dir_epsilon, nash_temperatures) on every rollout row** so that future analysis can filter or adjust for known biases.

5. **Store git_sha and checkpoint_hash on rollout rows** — not for Elo reuse, but for reproducibility and debugging. If a regression appears, you want to know exactly which code and weights produced those results.

6. **The `matchup_aggregates` view should remain tournament-only.** No schema changes needed for the existing Elo pipeline.

## Recommendations

1. **Create a `rollout_game_results` table** (schema above) in `checkpoint_db.py`. Add a `log_rollout_game_results()` function alongside the existing `log_rollout_wr()`.

2. **Add per-opponent logging to the league collection loop** in `train_ppo.py`. The data is already available in `_update_wr_table_from_steps` — just also write it to SQL.

3. **If you want tighter Elo CIs during training, increase panel eval frequency** (currently at milestones). Consider running panel eval every 10-20 iterations instead of only at save milestones. Panel eval uses temperature=0.0 and is directly comparable to tournament results.

4. **Consider making panel eval results loggable to `match_results`** with a distinct `tournament_id` prefix like `"panel_eval_{run_id}_iter{N}"`. Since panel eval already uses tournament-compatible settings (T=0.0, fixed seeds, equal games per side), these results *could* legitimately contribute to BayesElo — though the per-opponent sample size (typically 100-200 games) is smaller than full tournament games (400).

5. **Do not invest in a correction factor** to "adjust" rollout results to approximate greedy play. The relationship between T=1.2 WR and T=0.0 WR is model-pair-specific and would require calibration data that is more expensive to collect than just running more panel evals.

## Open Questions

1. **Panel eval as mini-tournament.** Panel eval results during training (`_panel_eval_worker`) already use T=0.0 and fixed opponents. Are these currently logged anywhere in SQL? If not, logging them as proper match_results with a "panel_eval" tournament_id would be the easiest way to get more Elo signal without any methodology risk.

2. **wr_table.json persistence across runs.** The WR table is cumulative within a run but lost between runs. Should it be migrated to SQL for cross-run analysis? This is separate from the Elo question but related to diagnostic value.

3. **Nash temperature inconsistency.** Rollout uses `nash_temperatures=True` while panel eval/tournament benchmarks use `nash_temperatures=False` for heuristic matches. This means rollout WR vs heuristic is not directly comparable to tournament WR vs heuristic even at the same temperature. Should this be standardized?
