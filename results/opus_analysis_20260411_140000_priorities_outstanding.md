# Opus Analysis: Outstanding Work and Priorities
Date: 2026-04-11T14:00:00Z
Question: Summarize outstanding work and priorities given the latest progress.

## Executive Summary

v55 remains the strongest model at Elo 2124, with the v44-v55 generation cluster forming an Elo plateau at ~2100-2124. The v64 (bc_wide384, h=384) experiment definitively failed -- peaking at Elo 1661, a massive 463 points below v55. v65 (v55 + SmallChoiceHead, h=256) is running PPO at iter 49/80 with rollout WR ~0.45, which is concerning as it is below the ~0.50 self-play equilibrium. Today's main infrastructure wins are the full 50-model JSD matrix, the `select_league_fixtures.py` script, two-pool PFSP with per-side UCB, and Phase 1 SmallChoiceHead completion. The project is at a critical juncture: architecture improvements (Pragmatic Heads Phases 2-4) are the identified bottleneck, but the only running experiment (v65) is not yet showing strength gains from the SmallChoiceHead addition.

## Findings

### What was just completed (today, 2026-04-11)

1. **Phase 1 SmallChoiceHead**: Fully implemented and marked complete. Engine PolicyCallback interface wired through `game_loop.cpp` for 8+ event decisions (Warsaw Pact, Summit, How I Learned, Olympic Games, Chernobyl, war targets, Wargames). SmallChoiceHead added to model classes. CountrySelect callbacks also wired.

2. **JSD matrix for 50 models**: `scripts/compute_jsd_matrix.py` computed full pairwise JSD (card/mode/country/combined) across 50 scripted models. Output at `results/jsd_matrix.json`. Key findings:
   - Most similar pair: v39 vs v40 (combined JSD = 0.0022) -- adjacent PPO generations are nearly identical
   - Most different pair: v55_sc vs v57 (combined JSD = 0.5026) -- v55_sc (SmallChoice variant) is the most behaviorally distinct model
   - Consecutive generations (v31-v41) have JSD < 0.005 -- massive redundancy in league fixtures

3. **`select_league_fixtures.py`**: Pareto-front seeding + greedy max-min JSD diversification. Written but not yet integrated into `ppo_loop_step.sh`.

4. **Two-pool PFSP**: Per-side (USSR/US) opponent pools with UCB-style weight selection. Single-side vs-model collection implemented.

5. **v64 declared failure**: bc_wide384 completed 80 PPO iters. Elo chain tournament shows best checkpoint (i80) at Elo 1661, compared to v55 at 2124. Width increase (256->384) with fresh BC init was catastrophically worse than continuing from v55 lineage.

6. **Bipartite Elo refit**: MM solver for bipartite (per-side) Elo fitting added, improving rating accuracy for asymmetric game.

### Currently running

- **v65 PPO** (PID 363233): iter 49/80, ~60% complete. Starting from v55 checkpoint with SmallChoiceHead. Uses 8 league fixtures (v8, v9, v14, v22, v44, v46, v55, v61) + heuristic. Rollout WR ~0.40-0.48, entropy 3.85-3.94 (healthy). Running on CUDA (RTX 3050). ETA: ~20 more minutes at ~38s/iter.
  - **Warning sign**: Rollout WR is trending below 0.50, and the PFSP pools show WR_us consistently at 0.33-0.42 against self-play checkpoints. This suggests US-side play may be a weak point.

### Key experimental result: v64 failure

The v64 experiment tested whether a wider model (h=384 vs h=256) initialized from behavior cloning could match v55 after PPO. Results are decisive:

| Checkpoint | Elo    | vs v55 |
|-----------|--------|--------|
| bc384_bc (BC init) | 1333 | -791 |
| v64_i10 | 1496 | -628 |
| v64_i40 | 1538 | -586 |
| v64_i80 (best) | 1661 | -463 |

**Root cause**: v55 benefited from 55+ PPO generations of progressive self-play refinement. Restarting from scratch with a wider model throws away all that accumulated learning. The 128 extra hidden units cannot compensate for ~500 Elo of PPO refinement.

**Lesson**: Future architecture experiments must use checkpoint surgery (loading compatible weights from v55), not fresh BC initialization. The v65 approach (starting from v55 checkpoint) is correct.

### State of infrastructure (JSD, fixture pruning, PFSP)

**JSD infrastructure**: Complete and production-ready.
- `ProbeEvaluator` with 996 frozen positions
- Full 50x50 matrix computed (~3 min on RTX 3050)
- Weighted combined metric (card=0.5, mode=0.2, country=0.3)
- Ready for integration into PPO loop

**Fixture pruning**: Script written, not yet deployed. The JSD data reveals that ~15 of the 34 Elo-tournament models (v29-v41 cluster) are essentially identical (pairwise JSD < 0.01). Pruning to ~14 diverse fixtures would double per-fixture training signal.

**PFSP**: Two-pool per-side opponent selection is live. v65 is the first run using it. The per-side WR tracking shows clear asymmetry: models consistently score higher as USSR than US, confirming the known game asymmetry.

**Elo ladder**: 34 models rated via round-robin (400 games/match). v55 at 2124 is the clear leader. The v44-v56 cluster at 2099-2108 forms a plateau. Below v17 (Elo 2063), there is a gradual decline to heuristic at 1751.

## Conclusions

1. **v55 (Elo 2124) remains the best model** and is the correct base for all future experiments. The 463-Elo gap to v64 proves that lineage continuity matters more than architectural width for PPO-trained models.

2. **v65 is the critical experiment to watch.** It tests whether SmallChoiceHead (Phase 1 Pragmatic Heads) can break the v44-v55 Elo plateau when trained from the v55 checkpoint. Results will be available within ~30 minutes.

3. **The JSD matrix reveals massive redundancy in the fixture pool.** Consecutive PPO generations (v29-v41) have JSD < 0.005. The current 34-model league is wasting ~40% of training games on near-identical opponents.

4. **Fixture pruning is ready to deploy but has not been.** Running `select_league_fixtures.py` and integrating it into `ppo_loop_step.sh` would immediately improve training efficiency for the next PPO generation.

5. **Phase 1 (SmallChoiceHead) is complete; Phases 2-4 are the main remaining architecture work.** Phase 2 (CountryAllocHead with DP decoding) is the highest-leverage remaining change, as country allocation is the most frequent decision in the game. The bounded-knapsack DP decoder is already implemented.

6. **The v44-v55 Elo plateau at ~2100 is real and persistent.** 11 PPO generations (v44-v55) gained only ~18 Elo points. This confirms the architecture-is-the-bottleneck hypothesis. Incremental PPO runs without architecture changes will not break through.

7. **Per-side Elo reveals US-side weakness as a systematic pattern.** Across all strong models, US Elo is 50-100 points below USSR Elo. This matches the known game asymmetry but suggests US-side training may benefit from focused attention.

## Recommendations

1. **Wait for v65 to complete, then benchmark immediately.** Run the Elo chain tournament against v55 and the standard panel. If v65 > v55, the SmallChoiceHead is validated and should become the new base for all subsequent training. If v65 <= v55, investigate whether the head is being used (check that engine callbacks are triggering during rollout).
   - **How**: `tail -f results/ppo_v65_v55sc.log` to monitor; then run Elo tournament script.

2. **Deploy fixture pruning for the next PPO generation.** Run `select_league_fixtures.py` to select ~14 diverse fixtures and use that list in the next `ppo_loop_step.sh` call. This is zero-risk and immediately improves training efficiency.
   - **How**: `uv run python scripts/select_league_fixtures.py --jsd-matrix results/jsd_matrix.json --elo-ladder results/elo_full_ladder.json --target-n 14 --checkpoint-dir data/checkpoints/scripted_for_elo`

3. **Begin Phase 2 (CountryAllocHead) implementation.** This is the highest-leverage architecture change remaining. The DP decoder is already implemented (`ba781a3`). The main work is:
   - Wiring the `score[c, k]` output through the engine's country allocation path
   - Training with the new head (may need self-play data with country allocation labels)
   - **Why**: Country allocation is the most frequent decision; the current K=4 MoS head cannot represent stacking or variable-cost placement.

4. **Do NOT restart from BC for any future experiment.** The v64 result proves this is a dead end. All future architecture experiments must use checkpoint surgery from v55 (or whatever the current best is). Add compatible layers with zero-init or small random init so the initial policy matches v55 exactly.

5. **Investigate v55_sc behavioral divergence.** The JSD matrix shows v55_sc (SmallChoice variant) is the most behaviorally distinct model (combined JSD 0.49-0.50 vs most others). Understand whether this divergence comes from the SmallChoiceHead actually making different event decisions, or from training instability. This signal directly informs whether Phase 1 is adding value.
   - **How**: Compare v55_sc card_jsd vs v55 specifically; check if the divergence is concentrated in card/mode (existing heads) or in the new SmallChoice outputs.

6. **Add v65 to the JSD matrix after training completes.** Incremental cost is ~5 seconds. This tracks whether the SmallChoiceHead creates meaningful behavioral diversity vs v55.
   - **How**: `uv run python scripts/compute_jsd_matrix.py --incremental --new-model data/checkpoints/ppo_v65_v55sc_league/ppo_best.pt`

7. **Consider focused US-side training or asymmetric hyperparameters.** The consistent 50-100 Elo US deficit suggests the symmetric PPO setup under-serves US play. Options: higher US learning rate, US-side data augmentation, or US-focused fixture selection. Lower priority than Phases 2-3 but worth prototyping.

## Open Questions

1. **Is v65's below-0.50 rollout WR a problem?** At iter 49, rollout WR is 0.39-0.48. This could be normal early-training noise (the model is still learning to use the SmallChoiceHead), or it could signal that the head is interfering with existing card/mode decisions. Need to see final benchmark.

2. **How should Phase 2 training data work?** The CountryAllocHead needs labeled country allocation sequences. Current self-play logs capture the final allocation but not the marginal-value-at-each-step signal needed for DP training. Options: (a) train from final allocation supervision, (b) add per-step marginal value labels to rollout data, (c) learn from PPO reward signal only.

3. **Should the JSD-based fixture pruning use a different weighting for the SmallChoice era?** Current weights are card=0.5, mode=0.2, country=0.3. If SmallChoice decisions become a significant fraction of policy behavior, a SmallChoice JSD component should be added.

4. **What is the ceiling for the current observation space?** The 32-dim scalar features + 172-dim influence features may be missing information that human experts use (e.g., exact discard pile contents, specific active effects beyond the boolean flags). Before investing heavily in Phases 3-4, it may be worth auditing what information the model can and cannot see.

5. **Is the v55 plateau a local optimum or a representation ceiling?** If SmallChoiceHead + CountryAllocHead do not break through ~2124 Elo, the bottleneck may shift to the trunk architecture (GNN vs Transformer, deeper networks) or to the training methodology (MCTS integration, population-based training).
---
