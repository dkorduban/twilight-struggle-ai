# Opus Analysis: ent_coef Decay — W&B vs Code Analysis
Date: 2026-04-10T22:21:11Z
Question: W&B shows ent_coef decayed, but code analysis says decay never fires. Who is right?

## Executive Summary

**Both the previous analysis and W&B are partially correct — they describe different code paths that existed at different times.** The contradiction arises from a code change on 2026-04-09 (commit c055d32) that replaced a per-run linear decay with a global-iteration-based schedule. The previous analysis examined only the current (global) code path and concluded decay never fires because `total_iters` is missing from v22's checkpoint (global_iter_offset=0, max global_iter=200 < decay_start=400). However, runs v9-v22 used the **original** per-run linear decay code that always decays within each run regardless of global offset. Runs v27+ use the new global schedule, and whether decay fires depends on the accumulated `total_iters` in the checkpoint chain.

Current state (v38-v44 era): `total_iters` was **reset** at v38 (=160) due to a lineage restart. The v38-v41 chain has total_iters in the 160-380 range, meaning decay is just beginning to fire in the last ~60 iterations of v40/v41 runs. The full 0.03→0.005 decay will not complete until ~total_iters=2000, which at 200 iters/run means ~8 more runs from the v38 restart point.

## Findings

### The Decay Code Path (Re-examined)

There have been **two distinct implementations**:

**Version 1 (commit 8d79f55, 2026-04-07): Per-run linear decay**
```python
# Decays from ent_coef → ent_coef_final over the N iterations of THIS run
t_frac = (iteration - 1) / max(1, args.n_iterations - 1)
current_ent_coef = args.ent_coef + t_frac * (args.ent_coef_final - args.ent_coef)
```
This ALWAYS decays within each run. Used by v5-v22.

**Version 2 (commit c055d32, 2026-04-09): Global iteration schedule**
```python
# Decays based on cumulative iterations across ALL chained runs
global_iter = global_iter_offset + iteration  # offset loaded from checkpoint
if global_iter <= args.global_ent_decay_start:  # default 400
    current_ent_coef = args.ent_coef            # flat at initial value
elif global_iter >= args.global_ent_decay_end:   # default 2000
    current_ent_coef = args.ent_coef_final       # flat at final value
else:
    # linear interpolation between start and end
```
Whether this fires depends entirely on `total_iters` stored in the source checkpoint.

### What is Actually Logged to W&B

Line 2896: `log_dict["ent_coef"] = current_ent_coef` — logs the actual coefficient used each iteration. The W&B sparklines faithfully reflect the true value used in training.

### Evidence from Log Files

| Run   | Code version | total_iters in source ckpt | global_iter range | Decay behavior | W&B sparkline |
|-------|-------------|---------------------------|-------------------|----------------|---------------|
| v9-v10 | Per-run | N/A | N/A | Always decays 0.05→0.01 | Decaying ████→▁▁▁▁ |
| v12-v22 | Per-run | N/A | N/A | Always decays 0.03→0.005 | Decaying ████→▁▁▁▁ |
| v24-v26 | Global | 0→600 | 1-200, 201-400, 401-600 | v24-v25 flat, v26 starts decaying | Mixed |
| v27 | Global | 0 (from v22, no total_iters) | 1-200 | Flat at 0.03 (all ≤400) | Flat ▁▁▁▁▁▁ |
| v28-v37 | Global | 399→2399 | Passes through 400-2000 zone | Progressive decay across runs | Varies by run |
| v37 | Global | 2399 (source) | 2400-2599 | Flat at 0.005 (past decay_end) | Flat ▁▁▁▁▁▁ |
| v38 | Global | 160 (RESET — new lineage) | 161-360 | Flat at 0.03 (all ≤400) | Flat ▁▁▁▁▁▁ |
| v39 | Global | 260 | 261-460 | Flat iters 1-139, decaying iters 140-200 | Mostly flat, slight decay at end |
| v40 | Global | 320 | 321-520 | Flat iters 1-79, decaying iters 80-200 | Late decay ████▅▄▃▂▁ |
| v41 | Global | 380 | 381-580 | Flat iters 1-19, decaying iters 20-200 | Early decay █▇▆▅▄▃▂▁ |

### The v38 Reset

v38's checkpoint has total_iters=160 despite being late in the chain. This happened because v38 was launched from a checkpoint where ppo_best.pt was saved at iter 160 (best combined WR peaked early). The total_iters counter accurately reflects the best iteration, not the final iteration.

### Reconciliation

The previous analysis was **correct about the current code** but **wrong about why W&B showed decay**:
- It assumed W&B decay came from the global schedule → wrong for v9-v22 (those used per-run decay)
- It correctly identified that v22's checkpoint lacks total_iters → true
- It concluded "decay never fires" → only true for runs loading from v22 directly (e.g., v27)
- For v28+ in the v27 chain, total_iters accumulates correctly and decay does fire

## Conclusions

1. **The previous analysis was wrong.** W&B correctly shows decay. For v9-v22, the OLD per-run linear decay code always fired. For v27+, the global schedule fires when total_iters passes 400.

2. **The v38 lineage reset is the real problem.** When v38 started from a checkpoint with total_iters=160, the decay schedule effectively restarted. The current chain (v38→v41) has total_iters=380, meaning decay has only just begun to fire (starting mid-run in v40).

3. **Decay is happening, but slowly.** With 200 iters per run and a decay window of 400-2000 (1600 iters wide), the full 0.03→0.005 schedule takes 8 runs from the decay start. Since v38 reset to 160, it takes ~9 more runs from v38 to complete the decay.

4. **The current ent_coef at v41's end is ~0.028** (global_iter≈380+200=580, decay_frac=(580-400)/1600=0.1125, ent=0.03+0.1125*(0.005-0.03)=0.027). The agent is still exploring at nearly the initial rate.

## Recommendations

1. **If faster decay is desired**: Pass `--global-ent-decay-start 0 --global-ent-decay-end 400` on the next launch to complete the decay within 2 runs. Or pass `--global-ent-decay-start 380 --global-ent-decay-end 780` to start decaying immediately and finish in 2 runs.

2. **If the current slow decay is intentional**: No action needed. The schedule will reach ent_coef_final=0.005 around v46-v47 at the current pace.

3. **To prevent future resets**: The `ppo_best.pt` checkpoint already stores `total_iters`, but a lineage restart (loading a different base checkpoint) naturally resets it. Consider adding a `--global-iter-offset-override` CLI flag to manually set the offset when restarting from a checkpoint that lacks or has stale total_iters.

## Open Questions

1. Was the v38 reset intentional or accidental? The total_iters dropped from 2399 (v37) to 160 (v38), which dramatically delayed the entropy decay schedule.

2. Is the slow entropy decay (estimated completion at v46-v47) desirable, or should it be accelerated? High entropy (0.03→0.028 currently) means the policy is still exploring heavily, which may explain plateau behavior.

3. The per-run decay (v9-v22) trained every run with full 0.03→0.005 decay. The global schedule means early runs after a reset train with nearly constant high entropy. Which approach produces stronger policies? This is an empirical question worth tracking.
