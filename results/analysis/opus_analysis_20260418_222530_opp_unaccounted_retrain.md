# Opus Analysis: opp_unaccounted Retrain Decision

Date: 2026-04-18 UTC
Question: Should we retrain from scratch after the `opp_unaccounted` encoding change (commit c749ae0, Task #61)?

## Executive Summary

**Recommended path: Option D (keep `opp_unaccounted`, collect fresh data, AWR warmstart, run v2 PPO).**

The encoding change is genuinely useful: it replaces 112 zero-information duplicate bits with a real signal about cards the opponent could still hold. The cost of a full retrain is bounded (~2h data collection + ~6h AWR + ~15 PPO iters ≈ 8–12h wall clock to re-reach ~45–47% WR) and is on the critical path anyway because the stated next task in `results/continuation_plan.json` is "v2 PPO chain with best arch from gated comparison (use opp_unaccounted encoding, fresh data collect needed)".

Option C (hot-patching old weights) is **not viable** in any meaningful sense:

- The production architecture `TSControlFeatGNNCardAttnModel` uses `self.card_encoder = nn.Linear(CARD_DIM=448, CARD_HIDDEN)`. That is one dense projection where every output neuron depends on every one of the 448 input bits. The old weights on columns `[112:224]` learned to sum two identical mask bits per card (`actor_known_in[c]` + `actor_possible[c]` are the same vector in self-play). Zeroing those columns removes half of the learned per-card signal — it does not "gracefully degrade."
- The `CardEmbedEncoder` variant (used only by some legacy DeepSet models) is slightly more structured (a shared `card_proj` plus four pooled concat slots), but its `out_proj` is also a fully connected `Linear(4*D, CARD_HIDDEN)` that has co-adapted the pool-1 channel with the other three. You could initialize a hot-patched pool-1 from the pool-0 weights (since the old data has `actor_possible == actor_known_in`), but that only recovers the *old* (garbage) semantics; it does not learn the new `opp_unaccounted` meaning, and the first layer after it is still miscalibrated.
- Option B (revert) preserves 47% but loses the feature improvement, and the commit history shows we will have to re-do this anyway before any fresh v2 chain. Doing the breakage twice is strictly worse than doing it once.

## Findings

### F1. The encoding change is real and breaking

From `cpp/tscore/nn_features.cpp` lines 34–47 (commit c749ae0):

```
[0..111]   actor_known_in (unchanged)
[112..223] opp_unaccounted   ← NEW: !hand && !discard && !removed
[224..335] discard           (unchanged)
[336..447] removed           (unchanged)
```

Previously `[112..223]` was a second copy of `actor_known_in`. In self-play (the only regime this code runs in) `actor_possible == hand`, so the slot was literally a duplicate.

The commit message explicitly states: *"Breaking change: existing checkpoints are incompatible with the new feature layout."* The empirical drop from 47% → ~6% WR confirms the model's learned weights on those 112 columns are now applied to a very different distribution (average density of `opp_unaccounted` per state is much higher than `hand`, which has ≤9 bits set).

### F2. The production architecture fully entangles the 448 card bits

In `TSControlFeatGNNCardAttnModel.forward` (model.py:2070):

```python
h_card = torch.relu(self.card_encoder(cards))   # Linear(448, CARD_HIDDEN)
```

There is no per-slot sub-encoder. The learned weight matrix `W ∈ R^{CARD_HIDDEN × 448}` has columns `W[:, 112:224]` that were fitted under the assumption those bits mirror `W[:, 0:112]`. In practice the learned combined linear operator is approximately `(W[:, :112] + W[:, 112:224]) · hand`, and the split between those two column blocks is arbitrary (any rotation would give equivalent behaviour during training).

This means:
- Zeroing `W[:, 112:224]` halves (on average) the hand signal.
- Remapping `W[:, 112:224]` via any lossless identity transform produces the *old* semantics, not the new one.
- There is no clean orthogonal subspace we can preserve while the opp_unaccounted signal is learned; the new feature's weights have to be learned *inside* the same dense layer that already holds entangled per-card channels for hand / discard / removed.

### F3. The cross-attention is unaffected — but it's not enough on its own

`TSControlFeatGNNCardAttnModel` pulls hand mask only from `cards[:, :NUM_CARDS]` (model.py:2091) for its attention pooling. That 0–112 slice is *unchanged* by Task #61. So the card-to-country cross-attention pathway still sees correct hand semantics.

However, the trunk concatenates `h_card` (the broken 448→CARD_HIDDEN output) with `h_cross`, and residual-adds them. When `h_card` has been corrupted by the encoding swap, the model's overall behaviour still collapses — cross-attention alone cannot rescue the value and mode heads that sit on top of the trunk.

### F4. The AWR comparison currently running is still scientifically valid for architecture ranking

`compare_gnn_card_attn_gated.sh` (PID 501141) trains both arms on OLD parquet (duplicate actor hand in `[112:224]`). Since both arms see identical inputs, `val_adv_card_acc` is a valid head-to-head between gated vs parent. Its *benchmark WRs* are invalid because benchmark uses the new binary, so the input distribution at inference differs from training. The plan already notes this; proceed to read `val_adv` only.

### F5. Checkpoint inventory: the sunk cost is moderate, not catastrophic

- `results/ppo_gnn_card_attn_v1/`: 30+ iterations (iter0010..iter0300 plus 10 retry rounds), ~2.3 MB each, ~6h of GPU compute. `ppo_best.pt` is at 47% combined WR.
- `data/checkpoints/scripted_for_elo/`: the long v8..v319 ladder (hundreds of scripted checkpoints from earlier PPO chains and BC). These are all frozen for Elo ranking purposes. With Task #61 live, their *benchmark numbers against the new binary* are meaningless, but their *relative* Elo history (computed before Task #61) is still accurate and still a useful reference point.
- Best pre-sc baseline v56 (48.5% combined, 45.1% @ N=500) was the high-water mark for months. Losing its benchmark comparability is a real cost; but v56's *strength* is preserved — we can keep it as a frozen reference by always running it through the legacy binary or by always benchmarking against the new binary with a new peak.

### F6. Option B (revert) is deceptively expensive

Reverting restores 47% today but:
- The next-task list explicitly plans to collect fresh data with the new encoding and run v2 PPO. Reverting means re-applying the change later and paying the retrain cost anyway.
- Reverting *now* commits us to a flag-day migration later with whichever checkpoints are current then — throwing away more work, not less.
- The MCTS sign-fix and any other search-side improvements can be tested with the *current* code post-retrain; they do not depend on keeping old checkpoints alive.

### F7. Is `opp_unaccounted` worth a full retrain on its own merits?

Probably marginal, but not zero:
- In a 112-card deck with ~9 cards in hand, ~X in discard, ~Y removed, `opp_unaccounted` has roughly 60–90 bits on. The information content is "which high-value threats could still be in opp's hand." That is exactly the feature a strong player uses to anticipate scoring/coup threats.
- Empirical claim in the commit message ("actual threat-awareness signal") is plausible but untested. We do not have an ablation with vs. without.
- However, the retrain is not being paid *only* for this feature — it's paid for the whole v2 chain, which also includes the gated/attn architecture winner, `val_calib_coef` in both update loops, and any self-play data improvements. `opp_unaccounted` is one of several coupled changes that all require a fresh parquet anyway.

### F8. ROI comparison

| Option | Eng time to 47% | Feature value kept | Follow-up tax | Risk |
|---|---|---|---|---|
| A Fresh retrain (AWR + PPO) | ~8–12h | opp_unaccounted + new arch | none | low (well-trodden path) |
| B Revert + keep old models | 0h | none (must redo later) | pay retrain cost later | medium (flag-day later) |
| C Hot-patch weights | unknown, likely > A | unclear; degraded start | full retrain likely still needed | high (ad-hoc surgery, no prior art in this repo) |
| D Keep change, accept breakage, move fast | ~8–12h | opp_unaccounted + new arch | none | low |

Options A and D are functionally the same plan; the difference is framing. D is the right framing: the new encoding is *now the definition of the feature*, and old checkpoints are legacy.

## Conclusions

1. **Hot-patching old weights (Option C) is not viable.** The production `TSControlFeatGNNCardAttnModel` uses a single `Linear(448, CARD_HIDDEN)` that fully mixes `[112:224]` with the other three mask blocks. Columns of that matrix cannot be surgically replaced without re-learning the next layer, which is equivalent to fine-tuning the whole model — at which point you are retraining.

2. **Cross-attention is *not* broken by the encoding change.** `TSControlFeatGNNCardAttnModel` reads the hand mask from `cards[:, :112]`, which is unchanged. The breakage is localized to `self.card_encoder(cards)`. This means old checkpoints could in principle be *fine-tuned* cheaply with the first layer reset — but the complete retrain is already cheap, so there is no ROI gap worth chasing.

3. **`opp_unaccounted` is a real but modest feature improvement.** It replaces a truly zero-information duplicate with a plausibly useful threat-awareness signal. The absolute gain is untested and could be ≤1–2 pp WR, but the cost is amortized across the v2 retrain that we need anyway.

4. **Option B (revert) is strictly worse than Option D** under the stated roadmap. We would have to re-apply Task #61 before v2 PPO anyway, so reverting only delays the same work while freezing us on the old encoding for interim experiments.

5. **The AWR comparison currently running (gated vs parent) is still meaningful.** Both arms use old-encoding data; their `val_adv_card_acc` delta is valid for architecture choice. Benchmark WRs in that run are garbage and should be discarded. The continuation plan already flags this.

6. **v56's "48.5% combined" milestone is a historical number from the old encoding.** It should not be used as an absolute anchor for new-encoding runs. We should expect the v2 peak to temporarily dip below 48.5% and re-establish a new baseline. This is book-keeping, not a regression.

## Recommendations

1. **Commit to Option D.** Do not revert Task #61. Treat old checkpoints (ppo_gnn_card_attn_v1 iter010..iter300, v2..v319_sc) as legacy-encoding artifacts — keep them for historical Elo plotting but do not try to resurrect them.

2. **Let the running AWR comparison finish and read `val_adv_card_acc` only.** Pick the winning architecture (gated vs parent) from that signal. Ignore its benchmark numbers. This is already the stated plan in `continuation_plan.json`.

3. **Execute the planned v2 chain.** Collect fresh parquet with new encoding (Task #64), AWR warmstart with the winning architecture, then 15+ PPO iterations. Expected cost ~8–12h wall clock. Target: reach or beat the old 47% combined WR on the new encoding within 15–30 PPO iterations.

4. **Preserve one legacy-compatible binary path for historical benchmarks.** Optional but cheap: tag the commit *before* c749ae0 so that re-running v56-era benchmarks against historical data is possible without reverting main. This protects Elo continuity across the encoding change.

5. **Mark v2 as a new Elo reference point.** Reset the benchmark baseline to "best v2 model vs heuristic" once one run clears ~45%. Do not compare new-encoding WRs to old-encoding WRs numerically; only compare within-encoding.

6. **Run a small post-hoc ablation on the feature itself.** After v2 stabilizes, train one arm with `opp_unaccounted` zeroed at runtime (mimicking the old behaviour) for 10 PPO iters on the new-encoding codepath. Gives us a clean measurement of the feature's actual contribution. This is ~1–2h and retroactively justifies the breaking change.

## Open Questions

- **Expected magnitude of `opp_unaccounted`.** We have no ablation yet. Could be 0–3 pp combined WR. Worth the post-hoc measurement in Recommendation 6.
- **Does the current dataset collector emit the new encoding?** Need to confirm `python/tsrl/selfplay/collector.py` (which still sets `actor_possible = actor_hand_mask`) was updated, or if the new parquet will need a second change to actually carry `opp_unaccounted` rather than duplicating hand. If the collector path feeds into training via AWR, the new encoding must be produced *in parquet* too — otherwise the AWR warmstart still trains on duplicated bits and only inference sees the new signal.
- **Interaction with frame-stack migration (Slices 3–7).** If the frame stack lands before v2 PPO finishes, the retrain may need to roll again. Worth deciding Option A vs B on frame stack *before* paying the v2 retrain cost, or at least acknowledging sequence risk.
- **Whether ISMCTS's value-head bias (closed investigation 2026-04-17) is affected.** The determinization-bias fix is orthogonal to encoding, but the new `opp_unaccounted` feature *is* directly about hidden-information state, and could interact with determinization-aware value-head training in future work.
