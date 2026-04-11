# n_steps Drop Investigation: PPO v2b vs v3

## What is n_steps?

`n_steps = len(all_steps)` in `train_ppo.py` line 1615. It counts the total number of **decision-point Step objects** collected during the rollout phase of one PPO iteration. Each `Step` represents one game state where the learning model chose an action (card + mode + country targets). It is logged to W&B at line 1756 and printed at line 1680.

## Observed values

| Run | Config | n_steps range | Average |
|-----|--------|--------------|---------|
| PPO v2b (self-play) | `--self-play --self-play-heuristic-mix 0.2`, 200 games/iter | 28,500 - 30,200 | ~29,500 |
| PPO v3 (league) | `--league`, 200 games/iter | 11,200 - 12,600 | ~11,800 |

**Drop**: ~60%, from ~29.5k to ~11.8k per iteration.

## Root cause: one-sided step recording in league mode

The drop is **entirely explained by a change in which steps are recorded**, not by game length, DEFCON-1 rates, or config changes. Both runs use 200 games per iteration.

### v2b: self-play mode (both sides recorded)

In `collect_rollout_self_play_batched()` (line 651), C++ function `rollout_self_play_batched` records steps for **both sides** (USSR and US) since both use the learning model. For 200 self-play games, this yields ~200 games x ~120 decisions/game = ~24,000 steps from self-play. Then the heuristic mix (20% = 40 games, split 20 USSR + 20 US) adds ~40 x ~140 decisions/game = ~5,600 steps. Total: ~29,500.

### v3: league mode (model_a only)

In `collect_rollout_league_batched()` (line 744), the function calls `rollout_model_vs_model_batched` which explicitly records steps **only for model_a** (the learning model). The C++ comment at line 4309 confirms: "Separate batch buffers: model_a batch (steps recorded) and model_b batch (greedy only)." And line 4423: "model_b batch: greedy_action_from_outputs, no step recording."

For 200 league games with only one side's steps recorded per game: ~200 x ~60 decisions/side/game = ~12,000 steps. This matches perfectly.

Additionally, when the league samples the heuristic (20% of the time), it falls back to `collect_rollout_batched` which also records only one side's steps. So there's no compensating heuristic-mix bonus.

### The math

- v2b self-play: 200 games x 2 sides x ~60 steps/side + 40 heuristic games x ~140 steps = ~29,600
- v3 league: 200 games x 1 side x ~60 steps/side = ~12,000

Ratio: 29,600 / 12,000 = 2.47x, which matches the observed ~2.5x drop.

## Is it declining over training?

**No.** The v3 n_steps is stable throughout training:
- Iter 1-10: 11,703 - 12,559 (avg ~12,050)
- Iter 20-30: 11,438 - 12,020 (avg ~11,750)
- Iter 40-50: 11,232 - 11,635 (avg ~11,450)

There is a very slight downward trend (~5%) which is consistent with the model winning more games before turn 10 (early VP victories = slightly fewer decisions per game). This is not concerning. If it dropped to <8,000 that would indicate DEFCON-1 farming or extreme early-game collapses.

## Is this a problem?

**Partially yes.** The reduced n_steps means:

1. **Less data per iteration**: Each PPO update sees ~60% fewer training examples. With the same `--ppo-epochs` and `--minibatch-size`, the model gets fewer gradient steps per wall-clock hour.

2. **Different data distribution**: Only model_a's decisions are used. In self-play, training on both sides' perspectives provides a natural form of data augmentation and ensures the value function learns from both sides' viewpoints evenly.

3. **Wall clock efficiency**: Rollout time is similar (v2b: ~18-22s, v3: ~16-18s per iter) because the C++ code still simulates both models for all 200 games. But v3 produces ~60% fewer usable training steps for roughly the same compute cost.

**Mitigating factors:**
- The league opponent diversity (heuristic + latest + random historical) provides qualitatively different and arguably higher-quality training signal than pure self-play
- The v3 benchmark results are actually improving (combined WR: 0.871 at iter 20, 0.898 at iter 40) despite fewer steps
- The KL divergence and clip fraction are much lower in v3 (kl=0.008-0.012 vs v2b kl=0.10-0.14), suggesting the model changes are more stable

## Recommendations

1. **Double `--games-per-iter` for league mode**: Use `--games-per-iter 400` to bring n_steps back to ~24k, comparable to v2b. This would roughly double rollout time from ~17s to ~34s per iteration, but the PPO update phase would scale proportionally with data volume. Net wall-clock increase ~50% per iteration.

2. **Alternative: record both sides in model-vs-model**: Modify `rollout_model_vs_model_batched` to optionally record model_b's steps too when model_b is a past checkpoint of the same architecture. This would recover the "both sides" data without extra simulation cost. However, the opponent's decisions come from a stale policy, so their `old_log_prob` values may create importance sampling issues.

3. **Monitor steps/game**: Track `n_steps / n_terminal_games` as a derived metric. A sustained decline there (vs the one-time level shift from the mode change) would be the real warning sign.

4. **No immediate action needed if Elo is improving**: The v3 run appears to be learning effectively despite fewer steps. The quality-over-quantity tradeoff from league diversity may be net positive. Consider doubling games-per-iter only if learning plateaus.

---

## Detailed verification (2026-04-07)

### Q1: Step recording per rollout variant — exact code confirmation

**`rollout_self_play_batched`** (`mcts_batched.cpp:4640`): Uses a single `batch_inputs` buffer and a single `batch_slots` vector. Every decision point for BOTH sides is fed through the model and recorded via `rollout_action_from_outputs` (line 4719). Steps are stored in `steps_by_game[slot->game_index]`. There is no side filter — all decisions produce steps. **Confirmed: records both sides.**

**`rollout_model_vs_model_batched`** (`mcts_batched.cpp:4272`): Maintains two separate batch buffers: `batch_a` (model_a, steps recorded) and `batch_b` (model_b, greedy only). Line 4309 comment: "Separate batch buffers: model_a batch (steps recorded) and model_b batch (greedy only)." Line 4423 comment: "model_b batch: greedy_action_from_outputs, no step recording." The `a_acts` flag (line 4355) routes each decision to the correct batch based on game_index and side. **Confirmed: records model_a only.**

**`rollout_games_batched`** (`mcts_batched.cpp:4469`): Used for model-vs-heuristic. Line 4536: `if (decision_side == learned_side)` — only the learned side's decisions are batched through the model and recorded. The other side is played by `choose_minimal_hybrid_sampled` (heuristic) with no step recording. **Confirmed: records learned_side only.**

### Q2: games-per-iter in v2b vs v3

Both use the argparse default of `--games-per-iter 200` (`train_ppo.py:1448`). No PPO experiment configs exist in `experiments.yaml` (which only has BC training configs). The prior investigation statement "Both runs use 200 games per iteration" is correct.

However, v2b **additionally** generates heuristic mix games:
- `n_heur = max(1, int(200 * 0.2)) = 40` extra heuristic games (line 1594)
- These are split: 20 as USSR + 20 as US via `collect_rollout_batched` (lines 1595-1602)
- Total games simulated in v2b: 200 (self-play) + 40 (heuristic) = **240 games**

V3 league always uses exactly 200 games (the opponent is sampled once per iteration, line 758).

### Q3: Average steps per side per game — back-calculated from observations

**v3 league** (clean single-variable):
- 11,800 steps / 200 games / 1 side = **59.0 steps/side/game**

**v2b self-play** — solving the equation:
- Let S = avg steps/side in self-play, H = avg steps/side in heuristic games
- v2b total: `200 × 2S + 40 × H = 29,500`
- If H ≈ 59 (same as v3 league games): `400S + 2,360 = 29,500` → `S = 67.85`
- **Self-play games average ~68 steps/side**, heuristic games average ~59 steps/side

**Comparison with TS game theory:**
A full 10-turn TS game has 1 headline + 6 AR (turns 1-3) + 7 AR (turns 4-10) = 1 + 18 + 49 = **68 decisions/side**. The self-play figure of ~68 is consistent with games going nearly to completion. The league/heuristic figure of ~59 indicates games ending ~1.3 turns earlier on average (decisive VP victories or DEFCON-1 losses cutting games short against a weaker/mismatched opponent).

### Q4: Why 2.5× not 2× — corrected explanation

The prior investigation's formula was approximately right but used the wrong steps/game for heuristic games ("~140 decisions/game" is incorrect — `collect_rollout_batched` records only one side, so it's ~59, not ~140).

The **correct math** accounting for both factors:

| Factor | v2b self-play | v3 league |
|--------|--------------|-----------|
| Games simulated | 200 SP + 40 heuristic = 240 | 200 |
| Sides recorded per game | 2 (SP) / 1 (heuristic) | 1 |
| Avg steps/side | ~68 (SP) / ~59 (heuristic) | ~59 |
| Total steps | 200×2×68 + 40×59 = **29,560** | 200×1×59 = **11,800** |
| **Ratio** | | **2.50×** |

Three factors compound to produce the 2.5× ratio (not just the 2× from one-vs-two-sided recording):

1. **Two-sided vs one-sided recording** (2.0× base): Self-play records both sides; league records only model_a. This is the dominant factor.

2. **Longer games in self-play** (~68 vs ~59 steps/side, 1.15× multiplier): Self-play between two equal-strength models with temperature=1.0 exploration produces games that run closer to the full 10 turns. League games against a past checkpoint or heuristic are more decisive (earlier VP auto-wins, more DEFCON-1 losses), shortening games by ~1.3 turns on average.

3. **Extra heuristic mix games in v2b** (240 vs 200 effective games, but only 40 extra games × 59 steps = 2,360 extra steps, a ~8% boost): v2b generates 40 additional heuristic-mix games on top of the 200 self-play games. v3 league has no such bonus — the 20% heuristic sampling in `sample_league_opponent` replaces model games rather than adding to them.

Combined: 2.0 × 1.15 × 1.08 ≈ **2.48×**, matching the observed 2.50× ratio.

### Q5: n_steps stability in v3

The prior investigation's data is confirmed: n_steps is stable at ~11,800 with a slight downward drift (~5% over 50 iterations). This is expected because:

- When the league samples a model opponent (80%): `rollout_model_vs_model_batched` with 200 games × 1 side × ~59 steps ≈ 11,800
- When the league samples the heuristic (20%): `collect_rollout_batched` called twice (100 USSR + 100 US) × 1 side × ~59 steps ≈ 11,800

Both paths produce approximately the same n_steps, explaining the stability. The slight downward trend is consistent with the learning model winning more decisively over time (fewer turns per game → fewer decisions per side).

### Summary of corrections to prior investigation

The original conclusion was directionally correct: the drop is primarily due to one-sided vs two-sided step recording. But the prior math had errors:

1. **Wrong**: "40 heuristic games x ~140 decisions/game = ~5,600 steps" — `collect_rollout_batched` records one side, not both. Correct: 40 × ~59 = ~2,360 steps.
2. **Missing**: The game-length asymmetry between self-play (~68 steps/side) and model-vs-opponent (~59 steps/side) was not identified. This 15% difference is a meaningful secondary factor.
3. **Missing**: The extra 40 heuristic-mix games in v2b (240 total vs 200 in v3) were noted but their contribution wasn't quantified correctly.

The corrected decomposition: 2.0× (recording) × 1.15× (game length) × 1.08× (extra games) = 2.50×.
