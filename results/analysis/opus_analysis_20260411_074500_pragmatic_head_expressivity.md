# Opus Analysis: Pragmatic Head Plan vs Expressivity Gaps
Date: 2026-04-11T07:45:00Z
Question: Does the pragmatic-head.md plan adequately address the expressivity limitations identified in the unimplemented mechanics analysis? Should we proceed as-is, modify, or take a different approach?

## Executive Summary

The pragmatic-head plan (from `head-architecture.md`) is an excellent architectural blueprint that fully addresses the expressivity limitations identified in the unimplemented mechanics analysis. However, it is a *destination*, not an *implementation plan* -- it requires a typed decision-node engine (`card -> use -> scope -> typed-args`) that does not yet exist in the C++ core, which currently resolves all event decisions randomly. The plan should be adopted as the target architecture, but the implementation path needs to be staged: first add policy-driven decision nodes to the engine (the real bottleneck), then swap the model heads. The head swap alone is the easy part; the engine refactor is where the effort lives.

## Findings

### What the unimplemented-mechanics analysis identified

The April 11 analysis (results/opus_analysis_20260411_020000_unimplemented_mechanics.md) found:

1. **~50-60 cards use random resolution** where rules call for player choice. This is the single largest gap.
2. **Pattern 1** (~45 cards): random target selection instead of policy-driven country choice on events like Socialist Governments, COMECON, Marshall Plan, De-Stalinization, Voice of America, Pershing II.
3. **Pattern 2** (~8 cards): random option selection instead of policy-driven binary/small choice on events like Warsaw Pact (add vs remove), Olympic Games (boycott vs participate), Summit (DEFCON direction), How I Learned (DEFCON level).
4. **Pattern 3** (~6 cards): ops applied randomly instead of through policy (CIA Created, UN Intervention, Grain Sales, ABM Treaty).
5. **Pattern 4** (~3 cards): missing interactive mechanics entirely (CMC removal, How I Learned DEFCON setting, Star Wars pile bug).

The implicit architecture conclusion is: the current model has **card_head + mode_head + K=4 MoS country_head + value_head**, which cannot represent event-specific decisions at all. The country head produces a single distribution over countries, used only for main-AR influence/coup/realign. Events that need country selection, binary choices, card selection from discard pile, region selection, or multi-step allocation are all handled randomly by the engine.

### What the pragmatic-head plan proposes

The plan in `pragmatic-head.md` (sourced from a ChatGPT conversation, now at repo root) proposes exactly **4 head families**:

1. **CardHead** -- choose one card from a masked candidate set. Covers AR hand choice, headline, discards, SALT/Star Wars recovery, Aldrich Ames, Missile Envy ties, UN Intervention pairing.

2. **SmallChoiceHead** -- one masked head for all finite small choices. Covers use choice (event/ops/space), opponent-event timing, China/Vietnam scope, Olympics boycott, Summit/HISL DEFCON, Chernobyl region, Wargames invoke, Warsaw Pact branch, war target choices.

3. **CountryAllocHead(score[c,k])** -- per-country per-threshold allocation head decoded by constrained DP. Covers influence placement, influence removal, choose-N-countries events, single-country targets (coup, Brush War, Truman Doctrine, Junta follow-up, Ortega coup).

4. **CardSubsetHead** -- subset selection for Ask Not-style "discard any subset" events.

Plus a **resolution-frame context** system: each engine decision node carries `source_card_id`, `step_id`, `decision_kind`, `phase`, visible card set, legal masks, caps, cost curves, budget, and other constraints.

### Gap-by-gap coverage assessment

| Expressivity Gap | Addressed? | How |
|---|---|---|
| Pattern 1: random country targets on events (~45 cards) | YES | CountryAllocHead with event-specific masks, caps, budgets |
| Pattern 2: random binary/small choices (~8 cards) | YES | SmallChoiceHead with legal mask |
| Pattern 3: random ops application (~6 cards) | YES | SmallChoiceHead for mode, then CountryAllocHead for placement |
| Pattern 4: missing mechanics (CMC, HISL, Star Wars) | PARTIAL | SmallChoiceHead covers HISL DEFCON choice; CMC removal needs engine work; Star Wars covered by CardHead on correct pile |
| Ops modifiers (+1/-1 from Containment, Brezhnev, Vietnam, China) | YES | `scope` as SmallChoice factor + `effective_ops` as DP budget |
| Stacking (multiple points in one country) | YES | score[c,k] with k>1 naturally represents stacking |
| Per-country caps (e.g. "max +2 per country in Europe") | YES | cap[c] parameter in DP decoder |
| Variable-cost placement (2 ops in enemy-controlled) | YES | cost_curve[c][k] in DP decoder |
| Realignment (repeated single-target, may re-target same country) | YES | Modeled as repeated CountryAllocHead(total=1) continuation nodes |
| De-Stalinization (remove then place) | YES | Two sequential allocation nodes |
| Bear Trap/Quagmire card selection | YES | CardHead with hand mask |
| China/Vietnam region-restricted bonus | YES | scope as SmallChoice or parallel scoring |

### What the plan gets right

1. **Correct factorization**: `card -> use -> scope -> typed-args` matches the TS rules structure much better than the current `card -> mode -> single-country-distribution`.

2. **Minimal head count**: 4 families covering all known TS decision types is elegant and sufficient. No over-engineering.

3. **DP decoder for allocation**: The `score[c,k]` formulation with bounded-knapsack DP is the right approach for influence placement. It handles ops modifiers, per-country caps, cost curves, and stacking in a single parallel forward pass. This directly resolves the K=4 MoS limitation where the model cannot represent "put all 4 ops in one country."

4. **Resolution-frame context**: The generic frame (`source_card_id`, `step_id`, `decision_kind`, `phase`, masks, caps, budget) is the correct abstraction. It avoids hardcoded booleans and makes the same head reusable across dozens of events.

5. **Chance nodes stay in engine**: Correct -- dice rolls and forced random draws should not be policy decisions.

6. **Realignment as repeated continuation**: Correctly identifies that realignment cannot be a single DP allocation because you see each roll before choosing the next target.

### What the plan is missing or gets wrong

1. **No implementation path from current state**: The plan describes the target architecture but not how to get there from the current codebase. The C++ engine (`step.cpp`, `game_loop.cpp`) currently has no concept of "typed decision nodes" -- events are resolved inline with random sampling. Adding decision-node yield points to the engine is a substantial refactor (estimated 2-4 weeks for the ~50 cards that need it).

2. **No staging strategy**: The plan implies all 4 heads arrive together. In practice, the highest-ROI path is:
   - Stage 1: Add SmallChoiceHead for the ~8 binary/option events (biggest strength-per-effort)
   - Stage 2: Upgrade CountryAllocHead from MoS to score[c,k]+DP for main-AR placement
   - Stage 3: Extend CountryAllocHead to event-driven country selections (~45 cards)
   - Stage 4: Add CardSubsetHead (only needed for Ask Not)

3. **Throughput impact of DP decoder is unclear**: The plan claims "one heavy trunk pass + one tiny DP" but does not quantify. The bounded knapsack DP over 86 countries with budget up to 5 and T_MAX=4 is O(86 * 5 * 4) = ~1700 operations per sample. This is indeed tiny relative to the trunk, but needs verification in the batched PPO/MCTS context where thousands of states are evaluated per second.

4. **Training signal for score[c,k]**: The plan does not address how to train the allocation head. The current self-play engine resolves all events randomly, so there are no training labels for event-specific country choices. Before the allocation head can learn good event decisions, the engine must produce policy-driven events AND those events must be included in the training data. This is a chicken-and-egg problem: you need the head to make good decisions, but you need good decisions to train the head.

5. **Backward compatibility with existing checkpoints**: The plan proposes a fundamentally different output interface. All existing checkpoints, the PPO pipeline, MCTS candidate generation, and the benchmark harness assume `card_logits + mode_logits + country_logits + value`. The migration needs careful handling.

6. **CardSubsetHead complexity**: The plan lists this as a separate head family but Ask Not is the only card that needs it. The cost of implementing and maintaining a separate head for one card is questionable -- a simpler approach might be to model Ask Not as repeated CardHead calls with a STOP token.

7. **The TSMarginalValueModel already exists**: The codebase already has a `TSMarginalValueModel` (model.py line 913) that predicts `delta[c,t]` marginal values -- this is literally the `score[c,k]` head the plan recommends. It outputs `marginal_logits: (B, 86, T_MAX)` with `T_MAX=4`. The plan does not acknowledge this existing prototype. The gap is not "we need to build score[c,k]" but rather "we need to add DP decoding on top of the existing marginal head AND connect it to policy-driven event resolution."

### Risk assessment

| Risk | Severity | Mitigation |
|---|---|---|
| Engine refactor scope creep | HIGH | Stage the typed-node engine changes by card priority, not all-at-once |
| Training data chicken-and-egg | MEDIUM | Use MCTS-generated labels from positions where events need decisions |
| Throughput regression from DP decoding | LOW | DP is O(N*B*T) which is tiny; profile before worrying |
| Breaking existing PPO/MCTS pipeline | MEDIUM | Maintain backward-compat output keys; add new keys alongside |
| Overengineering CardSubsetHead for one card | LOW | Defer or use repeated CardHead |

## Conclusions

1. **The pragmatic-head plan correctly identifies all four expressivity gaps** in the current architecture and proposes sound solutions for each. The `score[c,k]` allocation head with DP decoding directly fixes the K=4 MoS limitations around stacking, ops modifiers, and per-country caps.

2. **The plan is architecturally correct but implementation-incomplete.** It describes the neural head design well but does not address the prerequisite engine changes needed to emit typed decision nodes. Without engine-side policy callbacks, the new heads have nothing to predict.

3. **The existing TSMarginalValueModel is already 70% of the allocation head** the plan recommends. It predicts `delta[c,t]` for `t=1..4`. The remaining work is: (a) add DP decoding at inference time, (b) switch training loss from per-threshold BCE to proper allocation-level cross-entropy, and (c) connect to policy-driven event resolution in the engine.

4. **SmallChoiceHead is the highest-ROI addition** because it unlocks ~8 binary/option events that are currently random, and it requires only a small engine change (expose the choice as a policy callback instead of `rng()`) plus a tiny Linear head.

5. **The engine refactor is the real bottleneck**, not the head design. Adding typed decision nodes to `step.cpp` and `game_loop.cpp` for ~50 cards is estimated at 2-4 weeks of focused C++ work.

6. **The plan should be adopted as the target architecture** with a staged implementation path that prioritizes: SmallChoice events first, then allocation-head upgrade for main-AR, then event-driven allocations.

7. **CardSubsetHead should be deferred** -- Ask Not can be handled as repeated CardHead with STOP, or even left random for now given its low frequency.

## Recommendations

1. **Adopt the pragmatic-head plan as the target architecture**, but add a phased implementation roadmap:
   - **Phase 1 (1-2 days)**: Add SmallChoiceHead (Linear(hidden, max_choices)) to the model. Add engine callbacks for the 8 highest-impact binary/option events (Olympic Games, Warsaw Pact, Summit, HISL, Chernobyl, war target choices). This is the fastest path to measurable Elo gain.
   - **Phase 2 (3-5 days)**: Upgrade the existing TSMarginalValueModel with DP decoding at inference time. Replace the largest-remainder proportional allocation in `_build_action_from_country_logits()` with proper bounded-knapsack DP. This improves main-AR influence placement quality without engine changes.
   - **Phase 3 (2-4 weeks)**: Add typed decision-node yield points to the C++ engine for the ~45 event-driven country selection cards. Train the CountryAllocHead on event-specific labels.
   - **Phase 4 (low priority)**: CardSubsetHead for Ask Not; full resolution-frame context embedding.

2. **Start Phase 1 immediately** -- it is cheap (one new Linear head, ~8 engine callbacks) and directly addresses the Pattern 2 expressivity gap that the analysis highlighted.

3. **Benchmark TSMarginalValueModel with DP decoding** against the current K=4 MoS country head on the existing PPO pipeline before committing to Phase 2. The marginal model prototype already exists; the comparison is straightforward.

4. **Do not attempt the full engine refactor (Phase 3) until Phases 1-2 are validated.** The engine refactor is the highest-risk, highest-effort component and should only proceed after confirming that policy-driven event decisions actually improve Elo.

5. **Maintain backward-compatible output keys** throughout all phases. Add new keys (`small_choice_logits`, `alloc_marginals`, etc.) alongside existing ones so the PPO pipeline, MCTS, and benchmarks continue working.

## Open Questions

1. **What is the current Elo cost of random event resolution?** Without a measurement, we cannot prioritize the engine refactor against other Month-3 work (ISMCTS, parallel MCTS, exploration noise). A rough estimate could come from running a tournament where one agent uses a perfect-information oracle for event decisions.

2. **Should the DP decoder run on GPU or CPU?** The bounded knapsack DP is inherently sequential across countries but parallelizable across batch samples. A CPU implementation might be simpler; a custom CUDA kernel would be faster for large batches in PPO/MCTS.

3. **How does the resolution-frame context interact with the trunk?** The plan suggests conditioning the allocation head on `source_card_id`, `step_id`, `effective_ops`, etc. This context could be: (a) concatenated to the trunk hidden state, (b) used as a separate conditioning embedding, or (c) encoded via a small cross-attention layer. The choice affects both expressivity and throughput.

4. **Is the TSMarginalValueModel prototype trained and evaluated anywhere?** If there are existing training runs, their results would inform whether the score[c,k] formulation learns well in practice.

5. **How will typed decision nodes interact with MCTS?** Currently MCTS operates at the action-round level (card+mode+targets as one atomic action). If event resolution becomes multi-step (SmallChoice then CountryAlloc then another SmallChoice), each step becomes a separate MCTS node, which could explode the tree. The plan acknowledges this for realignment but does not address the general case.
