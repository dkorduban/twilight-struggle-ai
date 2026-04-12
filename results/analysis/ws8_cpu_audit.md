# WS8 CPU Saturation Audit
Date: 2026-04-12
Source: v67_sc log (`results/logs/ppo/ppo_v67_sc.log`), `scripts/train_ppo.py` instrumentation

## Per-Iteration Breakdown (v67_sc, 80 iters)

| Phase | Time (s) | % of iter |
|-------|----------|-----------|
| Rollout (game collection) | 17–21s | ~77% |
| PPO update (GPU backprop) | 4.4–5.8s | ~22% |
| Export / scripting / logging | ~1s | ~1% |
| **Normal total** | **~23s** | 100% |

Panel eval iters (every 10 iters, async subprocess launched):
- iter 11: 67.4s total (rollout=61.6s) — 3× slower due to panel contention
- iter 12: 64.1s total (rollout=58.3s)
- iter 13: 42.3s total (rollout=36.9s) — panel winding down
- Panel eval elapsed times: 176s, 561s, 312s, 181s, 207s, 184s, 182s (iters 10–70)

**Run wall-clock:** ~70 normal iters × 23s + ~7 contention iters × 57s = ~2010s ≈ **33–56 min per 80-iter run** (variance from panel eval duration).

## Bottleneck

**Primary: Rollout (game collection) at ~77% of normal iter time.**

The rollout runs Python game simulations with `--rollout-workers 1`. Each iteration plays 200 games (100 per league side mix). At ~17–21s for 200 games, that's ~85–105ms per game — plausible for CPU-side Python overhead calling C++ tscore engine.

**Secondary: Panel eval subprocess CPU core contention (NOT GPU).**

The panel eval worker (`_panel_eval_worker`) already uses `device="cpu"` explicitly — GPU is not the issue. The problem is `pool_size = min(32, half) = 32` parallel game workers in the panel eval subprocess competing with training's rollout for CPU cores. WSL2 typically exposes 6–12 logical cores to the guest. With 32 panel workers and 1 rollout worker fighting for the same CPU pool, rollout takes 3× longer for 2–3 iterations per eval cycle.

Panel eval takes 176–561s (3–9 minutes), overlapping multiple subsequent rollout iterations. Total overhead per 80-iter run: ~7 panel evals × ~40s slowdown each = ~280s extra.

The 561s outlier (iter 20 of v67_sc) suggests occasional panel eval variance — possibly game length distribution or fixture loading cold start.

## Recommendations (by estimated impact)

### 1. Cap panel eval pool_size (HIGH IMPACT, 1-line fix)
Change `pool = min(32, half)` to `pool = min(6, half)` in `_panel_eval_worker` in `scripts/train_ppo.py`. This limits panel eval to 6 parallel workers, leaving CPU headroom for training rollout. Panel eval will run ~5× slower (176s → ~880s) but rollout stays at 17–21s throughout. Net effect on 80-iter run: rollout saves ~280s but panel eval adds ~4900s more wall time. **This trades total wall time for stable training throughput** — only useful if rollout throughput matters more than panel eval latency.

**Better alternative**: reduce panel eval games from 200 to 60 per opponent (total 300 games instead of 1000). This cuts panel eval time by 3× with acceptable variance (~5% WR SE at 30 games/side). Combined with pool=6: eval takes ~175s (same as before) but with 60 games. Change `200` → `60` in the `_panel_proc` args at line 3336.

### 2. Increase rollout workers (MEDIUM IMPACT, check CPU headroom)
`--rollout-workers 1` uses one game worker for training rollout. Increasing to `--rollout-workers 2` during non-panel-eval periods would improve throughput. Requires confirming CPU cores are free (`htop` during a run).

### 3. Reduce panel eval frequency (LOW IMPACT, easy)
Change `--eval-every 10` to `--eval-every 20` in `ppo_loop_step.sh`. Halves panel eval overhead. Tradeoff: HWM tracking misses earlier peaks. Given Opus finding that iter_0010 is usually the HWM, evaluating less frequently is acceptable.

### 4. Pre-script export (NO IMPACT)
Scripted checkpoint export happens every 10 iters. Currently <1s — not a bottleneck.

## Applied Fix

Reduced panel eval games: `200` → `60` per opponent in `train_ppo.py` `_panel_proc` args.
This keeps pool_size=32 (fast parallel eval) but cuts total games 5× for much faster eval cycles.
Expected panel eval time: 176s × (60/200) ≈ 53s — fits within one normal rollout iteration (23s × 2–3 = 46–69s).

## Open Questions

- Does `htop` show 100% on one core during rollout, or spread across multiple?
- What fraction of rollout time is C++ engine vs Python overhead?
- Is the 561s panel eval outlier reproducible or a one-off?
