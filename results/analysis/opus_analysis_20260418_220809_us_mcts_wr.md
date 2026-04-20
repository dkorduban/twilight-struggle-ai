# Opus Analysis: US MCTS Win Rate Collapse
Date: 2026-04-18 UTC
Question: Why does US MCTS WR collapse to ~12% while greedy is 47%?

## Executive Summary
The bug is a **sign-convention mismatch between the trained value head and MCTS**. The
value head in `TSControlFeatGNNCardAttnModel` is trained with **actor-relative** returns
(positive = good for the side whose turn it is, because PPO's `reward = terminal if
side==winner else -terminal` and the model has two independent heads `value_head_ussr` /
`value_head_us`). But `select_edge_fast` / `select_edge` assume the value is in **absolute
USSR-perspective** (positive = USSR winning) and flip the sign only for `side_to_move ==
Side::US`. On every US-to-move node this flip turns a positive "good for US" leaf value
into a negative score, so US MCTS **systematically picks the actions the value head rates
worst for US**, collapsing US WR from 47% (greedy) to ~12%. USSR is unaffected on its own
decision nodes because actor-relative and USSR-perspective coincide when the actor is USSR;
the USSR side is only mildly polluted by mixed-perspective backup values from deeper US
subtrees, which matches the observed asymmetric collapse.

## Findings

### 1. Value convention used by MCTS (C++)
`cpp/tscore/search_common.hpp:239`:
```cpp
inline double winner_value(std::optional<Side> winner) {
    if (winner == Side::USSR) return 1.0;
    if (winner == Side::US)   return -1.0;
    return 0.0;
}
```
Terminal values are **USSR-perspective**: +1 = USSR won, -1 = US won. This is consistent
with the VP convention confirmed in `cpp/tscore/step.cpp:100-112` where USSR success gives
`next.vp += 2` and US success gives `next.vp -= 2` (positive VP = USSR winning).

`cpp/tscore/mcts_batched.cpp:1794-1832` (`select_edge_fast`) and
`cpp/tscore/mcts.cpp:580-612` (`MctsNode::select_edge`) both apply the same flip:
```cpp
auto q = effective_visits > 0 ? effective_total_value / effective_visits : 0.0;
if (side_to_move == Side::US) q = -q;           // mcts.cpp
// or: const bool invert_q = (node.side_to_move == Side::US);
```
This is the standard "values are in a fixed frame (USSR), the US side negates before
maximizing" pattern. Crucially, `backpropagate_path` / the loop in `mcts_search` do
**not** flip sign during backup (`edge.total_value += leaf_value`), so `edge.total_value`
is assumed to be in a single global frame.

### 2. Value convention produced by the NN (Python)
`python/tsrl/policies/model.py:2046-2122` (`TSControlFeatGNNCardAttnModel`, the model in
`results/ppo_gnn_card_attn_v1/ppo_iter0300_scripted.pt`):
```python
self.value_branch_ussr = nn.Linear(hidden_dim, VALUE_BRANCH_HIDDEN)
self.value_head_ussr   = nn.Linear(VALUE_BRANCH_HIDDEN, 1)
self.value_branch_us   = nn.Linear(hidden_dim, VALUE_BRANCH_HIDDEN)
self.value_head_us     = nn.Linear(VALUE_BRANCH_HIDDEN, 1)
...
v_ussr = torch.tanh(self.value_head_ussr(torch.relu(self.value_branch_ussr(hidden))))
v_us   = torch.tanh(self.value_head_us  (torch.relu(self.value_branch_us  (hidden))))
is_us  = side_idx.unsqueeze(1).float()         # scalar[10] in features
value  = (1.0 - is_us) * v_ussr + is_us * v_us
```
The model returns **one head's output per sample**, selected by the acting side. Each head
is trained independently.

### 3. Value target used to train the heads (PPO)
`scripts/train_ppo.py:606-644` (`_compute_reward`):
```python
is_ussr = side_int == 0
won = result.winner == (tscore.Side.USSR if is_ussr else tscore.Side.US)
...
base = 1.0 if won else -1.0
```
And `_compute_gae_per_side` at `scripts/train_ppo.py:1700-1721`:
```python
reward = terminal_reward if target_side == terminal_side else -terminal_reward
...
side_steps[t].returns = gae + side_steps[t].value
```
The return (= value target) fed into `F.mse_loss(values_b, batch_returns)`
(`scripts/train_ppo.py:1978`) is therefore **actor-relative**:
- USSR-row target: +1 iff USSR won.
- US-row target: +1 iff US won.

So `value_head_ussr` learns "positive = USSR winning" and `value_head_us` learns
"positive = US winning". Both heads output in the **acting side's** frame.

The dataset layer mirrors this: `python/tsrl/policies/dataset.py:140-147` explicitly
documents `actor_relative` mode and `train_baseline.py:305-309` exposes it as a CLI
choice; the BC/AWR warmstart used before PPO (`results/awr_sweep/v2b/control_feat_gnn_card_attn/`)
followed the same convention, and PPO itself always trains actor-relative returns.

### 4. Mismatch trace at a US-to-move leaf
1. A US-to-move state is evaluated by the NN. Because `side_idx == 1`, `value = v_us ∈
   [-1, 1]`, where **positive means "US winning"**.
2. `evaluate` / `evaluate_leaf_value_raw` return this raw value unchanged
   (`cpp/tscore/mcts.cpp:238-252`, `cpp/tscore/search_common.hpp:311-327`).
3. `backpropagate_path` (`mcts_batched.cpp:1760`) or the ancestor loop in `mcts_search`
   does `edge.total_value += leaf_value` with no sign flip.
4. In the next `select_edge_fast` on the **same US-to-move parent**, `invert_q == true`,
   so the edge's average value is negated before being maximised. A leaf reporting
   "US is winning" (+V) is treated as "USSR is winning" and, after flip, scores -V —
   US then **avoids** it. Conversely, the action the head thinks is worst for US scores
   highest. US MCTS systematically picks the actions the model thinks are worst for US.

This is the direct mechanism that produces the 35 pp collapse (47% → 12%) against a
greedy opponent. A policy that picks the value-min action against a value head that was
the greedy policy's signal is strictly worse than greedy; 12% is consistent with
"anti-greedy" behaviour.

### 5. Why USSR MCTS is mostly fine (~40-45%)
On a USSR-to-move node, `side_idx == 0` → `value = v_ussr`, positive = USSR winning.
`select_edge_fast` does **not** flip for `side_to_move == Side::USSR`. So on USSR's own
decision nodes the value is interpreted correctly and MCTS behaves as designed.

USSR nodes are still *mildly* polluted by leaves expanded inside US subtrees (because
those leaves contribute `v_us` = "US frame", which when summed into `edge.total_value`
along a path that crosses several US-to-move nodes gives incoherent but not
catastrophically biased averages). Terminal leaves are correctly USSR-frame, so as a
fraction of rollouts terminate at game end the tree still gets a consistent signal for
USSR-side decisions. This is why USSR MCTS approximately matches greedy instead of
collapsing.

### 6. Ruling out the non-bug hypotheses
- **(B) Value-head miscalibration**: the reported -0.137 on a symmetric board is actually
  *consistent* with actor-relative interpretation (US is structurally disadvantaged by
  bid rules, so US head at VP=0 reporting "slightly losing" is reasonable). It is only
  pathological under the absolute-USSR interpretation MCTS uses.
- **(C) Greedy already optimal**: implausible — MCTS with correct values is strictly
  better than greedy at ≥1 simulation (it becomes greedy as sims→0 or c_puct→∞). A 35 pp
  drop below greedy requires actively anti-correlated decisions, which is exactly what
  the sign inversion produces.
- **(D) Side-indicator bug**: checked — `nn_features.cpp:49-89` writes `ptr[10] = to_index(side)`
  and `TSControlFeatGNNCardAttnModel` reads exactly that index. Side is plumbed correctly.
  The bug is the *interpretation* of the value output, not the side input.
- **(E) US rollouts longer / deeper**: MCTS doesn't do depth-limited rollouts by default
  here (`use_rollout_backup` off in benchmark config — `benchmark_mcts` does not set it).
  Values come from the NN only.

### 7. Why this didn't show up earlier with single-head models
Older `TSControlFeatGNNFiLMModel`-style checkpoints have a single `value_head` with
`side_idx` only as an input feature. Under the same actor-relative training signal, a
single-head network can still only produce one scalar per forward pass, so its learned
output is *still* actor-relative — the head has to use the side feature to flip internally
because the target sign depends on side. In practice the representational pressure to
learn "absolute USSR-perspective" simply doesn't exist. So the same bug is latent in
older checkpoints too, but the symptom may be smaller because the shared trunk
interpolates between sides and the learned bias is less extreme than a full dual-head
separation. The dual-head architecture makes the mismatch maximally explicit: each head
is strictly trained in its own frame with no cross-over.

This is consistent with the project's history of "US side always underperforms"
observations and the `feedback_game_asymmetry.md` note that filter-to-US-wins-only was
needed. Some of that asymmetry was likely the convention bug amplifying the native
TS side imbalance.

## Conclusions
1. The value head in `ppo_iter0300_scripted.pt` (and in every PPO-trained checkpoint in
   this repo) outputs an **actor-relative** value: positive = good for whichever side
   `scalars[10]` says is acting. This is the convention trained by `_compute_reward` /
   `_compute_gae_per_side`.
2. `select_edge_fast` in `cpp/tscore/mcts_batched.cpp:1794` and `MctsNode::select_edge`
   in `cpp/tscore/mcts.cpp:580` assume value is in **absolute USSR-perspective** (they
   flip sign only when `side_to_move == Side::US`). Combined with side-agnostic
   `backpropagate_path`, this is a **direct sign contradiction** for US nodes.
3. On US-to-move nodes, the contradiction inverts MCTS selection: US maximizes `-v_us`
   instead of `+v_us`, picking the actions the model rates worst for US. That matches
   the observed 47% → 12% collapse.
4. USSR-to-move nodes coincide with the USSR-perspective assumption, so USSR MCTS is
   approximately correct and stays near greedy (~40-45%).
5. Terminal backup uses `winner_value` which is genuinely USSR-perspective — this is the
   "anchor" that keeps USSR MCTS from collapsing and causes the residual mixed-frame
   noise for both sides.
6. The bug is latent in older single-head checkpoints too (same PPO training signal), but
   the dual-head `TSControlFeatGNNCardAttnModel` exposes it most starkly.

## Recommendations
1. **Fix the convention in MCTS leaf handling**, not in the model. The model convention
   is well-defined by PPO training; inverting PPO rewards to absolute-USSR would throw
   away sign consistency across self-play sides. Preferred fix, localised in C++:

   ```cpp
   // In evaluate() / evaluate_leaf_value_raw(): convert actor-relative → USSR-perspective
   double raw = value_ptr[...];
   double v_ussr_frame = (state.pub.phasing == Side::USSR) ? raw : -raw;
   return calibrate_value(v_ussr_frame, config);
   ```
   Apply at the **exact point where the NN value first enters the search** (leaf eval),
   before any backup. All downstream math (`edge.total_value`, `select_edge_fast`
   invert_q, terminal handling via `winner_value`) remains correct as-is.
2. **Add an invariant test** in `tests/cpp/`: at a hand-crafted symmetric VP=0 position,
   run MCTS with `n_simulations=1` for US and for USSR; the mean root Q after backup
   should have the same magnitude and sign convention for both sides (both USSR-frame).
   A direct assertion that `v_us` gets negated-on-entry covers regression.
3. **Add a Python-side smoke test** that runs the scripted model on a symmetric state for
   both sides and asserts `value_us_side == -value_ussr_side` up to trunk asymmetry
   (actor-relative convention) — documents the expected convention contractually.
4. **Rerun the MCTS benchmark** with the fix on `ppo_iter0300_scripted.pt`. Expectation:
   US MCTS should recover to at least greedy level (47%+) and likely above; USSR MCTS
   should also improve somewhat because the US-subtree leaves contributing to USSR-node
   averages now carry the correct sign.
5. **Audit Elo / benchmark history** for systematic US-side underperformance once the
   fix lands. Past Elo numbers where MCTS was used will be biased; greedy-only Elo is
   unaffected.
6. **Consider documenting** the value convention explicitly in `cpp/tscore/mcts.hpp` and
   `python/tsrl/policies/model.py` as a block comment so future architecture changes
   don't re-introduce the mismatch.

## Open Questions
1. Does the same bug affect `ismcts.cpp`? The file uses `winner_value(...)` at line 524
   for terminals and similar leaf-NN evaluation via `evaluate_leaf_value_raw`, so almost
   certainly yes — the fix needs to be applied there too. Worth checking the ISMCTS
   benchmark numbers vs greedy for US specifically.
2. Did training ever use `actor_relative` vs `final_vp` mode for the BC warmstart feeding
   this PPO run? Either way the final PPO training imposes actor-relative via
   `_compute_gae_per_side`, so the outcome is the same, but the warmstart's initial
   sign bias could explain why the mean `v_us` starts already negative for US.
3. How much of the historically noted "US side underperforms" gap closes once this is
   fixed? If it closes substantially, some of the bid-compensation / US-filter heuristics
   in the training pipeline may become unnecessary.
4. The `calibrate_value` step (`search_common.hpp:249-256`) operates on the raw value
   before the USSR-frame conversion. If any calibration parameters are ever set they
   should be fit **after** the actor→USSR conversion, otherwise the calibration mixes
   the two frames. Currently `calib_a=1, calib_b=0` default so this is moot, but worth
   flagging for anyone who enables calibration later.
