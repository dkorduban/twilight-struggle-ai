# CountryAlloc Frame Redesign: Cost / Benefit Analysis

Date: 2026-04-19
Context: mid-migration evaluation of a proposal (inspired by `long-prompts/pragmatic-head.md`) to collapse the current ~4 active FrameKinds into 4 head families (CardHead, SmallChoiceHead, CountryAllocHead(score[c,k]), CardSubsetHead), with Realignment staying sequential.

---

## Executive Summary

The proposal is directionally correct about **model heads** and materially wrong about framing it as a **FrameAction schema change**. Engine decision granularity (how many nodes the frame stack produces per card) and model head factorization (score[c,k] vs per-step categorical) are *separable*: the C++ DP decoder (`cpp/tscore/dp_decoder.hpp::knapsack_alloc`) and Python (`python/tsrl/policies/dp_decoder.py::bounded_knapsack_dp`) already implement bounded-knapsack allocation and are used for top-level ops influence today. You can adopt a CountryAllocHead on the model side *without* touching `FrameAction`, `DecisionFrame`, or the C++ sub-policy contract. The proposed schema-level redesign is a cross-cutting change mid-migration (violates CLAUDE.md layer-local principle), its branching-factor and credit-assignment arguments are theoretical (MCTS/ISMCTS do not consume the frame API yet, per `cpp/tscore/mcts*.cpp` and `cpp/tscore/ismcts.cpp`), and the remaining ~12 unmigrated cards are mostly single-pick / option-count / non-alloc patterns that get little benefit from a multiset node. Recommendation: finish the sequential migration, then promote CountryAllocHead in the model for multi-step country runs; defer any `FrameAction` schema change until there is concrete PPO/MCTS evidence.

---

## Findings

### Q1. End-to-end workability per-card

The proposal's "single CountryAlloc node" pattern is clean on paper but fragments as soon as you look at real cards:

- **Decolonization (card 30)**: clean fit. Place 4 influence across Africa/SEAsia, cap 1 per country, cost 1 each. One CountryAlloc node with budget=4, legal={Af ∪ SEAsia}, cap=1 works.
- **Marshall Plan (23), Warsaw Pact (16), Willy Brandt**: clean fit. Fixed budget, fixed region, cap 1 per country. Single CountryAlloc node.
- **De-Stalinization (33)**: must be two nodes linked by `required_total`, as the proposal itself admits. Removal constraints (only US-owned, up to 2 per country) differ from placement constraints (non-US-controlled, cap 2 per country). The "one allocation head" story breaks here. Current impl uses a 2N-step CountryPick loop which already threads src id via `criteria_bits`.
- **Realignment cards (Junta/Ortega 94, 52, 102, 105, …)**: must remain sequential. Each roll can retarget based on new DEFCON / adjacency. Proposal acknowledges this. Same node count as today.
- **Coup cards**: single pick, no alloc benefit. SmallChoice or CountryPick-of-1 is identical information content.
- **Grain Sales (32), Junta (52), Lone Gunman (68)**: these go through `apply_ops_randomly_impl` in `cpp/tscore/hand_ops.cpp:673`. They *first* need a mode-selection node (Influence vs Coup vs Realign), then either CountryAlloc (if Influence) or per-country sequential (if Coup/Realign). That is exactly what the top-level AR already does. Again, this doesn't require a schema change — it requires wiring these cards through the existing frame push helpers.
- **Cards 24, 43, 45, 47, 78, 83, 84, 90, 91, 97 (Chernobyl), 102**: mostly SmallChoice / CardSelect / single-region-designate / forced-discard patterns. Not allocation-shaped; CountryAlloc is irrelevant.
- **Star Wars (88), Summit (48), Ask Not**: card-pool interactions. CardSubset or SmallChoice fit; CountryAlloc is inapplicable.

**Bottom line**: CountryAlloc is a genuine fit for roughly **5-7 cards** (30, 23, 16, Willy Brandt, 34 TT, Decol-like patterns). The rest either need sequential resolution anyway (realign, De-Stal, coup continuation) or are single-pick/small-choice shapes that don't benefit.

### Q2. Engine-side cost

The proposed schema change touches:

1. `cpp/tscore/decision_frame.hpp`: new frame kind + new `FrameAction` variant (`country_alloc: vector<pair<CountryId,int>>`) — breaks struct POD assumptions the current `resume_card_N` functions rely on.
2. `cpp/tscore/game_loop.cpp`: every `push_country_frame` callsite needs to decide "am I the leaf or am I a step in an alloc?", and `resume_card_subframe` (switch at ~line 1732) needs a new branch per card that uses alloc. Each `resume_card_N` (at least 30, 23, 33, 16, Willy Brandt, 34) needs rewriting to consume an alloc action instead of iterating `step_index`.
3. `cpp/tscore/step.cpp`: the `choose_country` callback shape would have to accept a whole allocation in `frame_stack_mode`, not a single id. That's a callback-signature change, not a local edit.
4. `cpp/tscore/hand_ops.cpp::apply_ops_randomly_impl` (line 673): either stays sequential (current behavior) and is fine, or needs to gain an alloc-shape emission, doubling the branching complexity of ops-modifier threading (China Card Asia-only, Vietnam Revolts SEAsia-only).
5. `bindings/tscore_bindings.cpp`: does not expose the frame API at all today. Adding alloc variants here is net-new bindings work that wouldn't exist if schema stayed flat.
6. Legality: today `eligible_countries` is an id list. An alloc action needs `(legal, cap, cost, budget, required_total)` carried on the frame. That's not a big change, but every callsite has to populate and respect it.

**Scope-threading is where this bites**: China Card Asia-only and Vietnam Revolts SEAsia-only constraints are currently layered on top of per-step country eligibility. With a CountryAlloc node the constraint has to be baked into `legal` at *frame construction*, which crosses the current "criteria_bits is a small scalar" boundary. Workable but invasive.

**Estimate**: ~1200-1800 LOC across C++ (frame struct, game_loop pushers, step callbacks, ~6 resume_card_N rewrites, legality plumbing) plus ~300-500 LOC Python (action encoding, legal-action mask shape, dataset action column, policy target format). This is comparable to the *remaining* migration effort and happens *on top* of it.

### Q3. Action encoding changes (Python-side)

Today `python/tsrl/policies/learned_policy.py` encodes sub-policy outputs as scalar indices (option_index | card_id | country_id). Adding CountryAlloc means:

- The action column in the offline dataset becomes variable-shape (a vector of (country_id, amount) pairs) or an encoded 86-slot allocation vector. Schema change.
- PPO / BC action target format changes. The card-head / mode-head / strategy-head / value-head layout is stable; adding an alloc head is fine, but the *training loop* must switch between "categorical per-country step" and "DP-decoded alloc" based on frame kind, which is new branching in `policies/model.py`.
- The pybind11 surface (which, per `bindings/tscore_bindings.cpp`, doesn't expose frame API today) would need to expose alloc shapes when we *do* surface frames to Python for MCTS.

**Key point**: the CountryAllocHead on the model already conceptually exists — `learned_policy.py` lines ~120-155 call `bounded_knapsack_dp` for top-level INFLUENCE mode today. Extending that pattern to mid-card multi-step country runs is a model-side upgrade, not an action-encoding upheaval. The upheaval only materializes if you also change the engine's action *shape*.

### Q4. Exactness trade-offs

- **Sequential is strictly more expressive** than a multiset allocation. Per-step conditioning on partial allocation lets the policy respond to "opponent revealed X via headline mid-card" or "adjacency realign chain opportunity emerged after first placement." A single alloc node collapses this.
- For cards with independent placements (Decol, Marshall, Warsaw), sequential and alloc are equivalent in information; alloc is *not* less expressive.
- For De-Stalinization the proposal keeps two nodes, so exactness is preserved — but the "collapse to one node" narrative is already halfway undone.
- For ops-randomly cards (32, 52, 68) the mode-conditional alloc shape is genuinely different from sequential: once you commit to Coup mode at step 1, the remaining country choice is sequential anyway. Net: no exactness loss, but no expressiveness gain either.

**No correctness hazard** introduced by alloc for the cards that fit. But the *motivation* ("branching factor") is the weakest part: per-step legality masks already prune to legal countries, and PPO scales in `log N` of branching under masking. MCTS branching is only an issue if MCTS ever visits these nodes — which it doesn't today (see Q8).

### Q5. Ops modifiers / scope threading

Today, `criteria_bits` on the frame carries a small scalar (e.g. src country_id for De-Stal). Ops modifiers (Asia-only under China Card, SEAsia-only under Vietnam Revolts, cap-2 under Red Scare/Purge) are applied to per-step country eligibility at `push_country_frame` time via the active effects bitset in `GameState`.

Under CountryAlloc the scope must be materialized into the `legal` mask of the alloc frame *once*, at push time. That is a **stricter** contract: if an effect *changes mid-alloc* (e.g. a triggered effect fires between placements), the alloc node cannot respond. This is not a common case in TS, but it is not zero — effects like "if you place in a battleground, X triggers" become impossible to model cleanly inside an alloc node.

**Counter-point**: current engine also doesn't handle mid-alloc state mutation for those cards; it resolves all placements and then applies triggered effects. So the gap is not widened — but it is *frozen in*, which is worse than a layer that could be extended later.

### Q6. Model / head implications

This is the strongest part of the proposal, and it's the part that does NOT require a schema change:

- CountryAllocHead as score[c,k] + DP decoder: **already exists** in the codebase (`dp_decoder.py::bounded_knapsack_dp`, used by top-level ops). Promoting it for mid-card multi-step runs is a training-time change.
- Gradient flow is cleaner through DP-with-straight-through-estimator than through a multinomial chain at long horizons. This is a real benefit for Decol-style 4-step sequences.
- CardSubsetHead for Ask Not / Summit is a clean new head, independent of any FrameKind refactor.
- SmallChoiceHead already exists (`small_choice_head`, SMALL_CHOICE_MAX=8).

**So the model-side win is real and can be captured without touching the engine's frame schema.**

### Q7. Migration path for the ~35 already-migrated cards

The migrated cards (per `opus_analysis_20260419_060610_frame_migration_plan.md`) include resume_card_14, 30, 33, 34, 37, 39, and ~30 others — each has a `resume_card_N` function that consumes `FrameAction{option_index, card_id, country_id}` and advances `step_index`. A CountryAlloc variant changes the FrameAction from scalar to "scalar OR vector-of-pairs," which is a tagged union. Every existing `resume_card_N` must either:

(a) stay on the old scalar path (wasted opportunity and now you have two code paths), or
(b) be rewritten to consume the alloc action (work we already paid for, redone).

**There is no cheap way to migrate in place.** The CLAUDE.md principle "Keep changes small, layer-local, and reversible" is violated by either option. And the ~12 cards not yet migrated are not the ones that benefit from alloc.

### Q8. Training / MCTS implications

- **PPO**: today's sequential approach works and is training stably. The "credit assignment is hard across 4 steps" concern is theoretical for Decol-depth sequences; no measured PPO signal says the current approach is the bottleneck. The real bottlenecks per current experiment notes are value-head miscalibration and exploration noise — not frame depth.
- **MCTS / ISMCTS**: grepped `cpp/tscore/mcts.cpp`, `mcts_batched.cpp`, `ismcts.cpp` — none reference `engine_step_toplevel`, `engine_peek`, `FrameAction`, or `frame_stack`. They operate on flat top-level actions. So the "MCTS branching factor" argument for CountryAlloc is **hypothetical**: MCTS doesn't currently expand sub-frame nodes, and the planned parallel MCTS work (Month 3 priority #6) doesn't require it. When/if MCTS is extended to sub-frames, `score[c,k] + DP` at the model head can still be used for action proposals without the engine emitting alloc actions.
- **Training throughput**: per `feedback_training_throughput.md`, short iterations and high rollout WR are the metrics that matter. A frame-schema refactor will pause throughput for weeks. That's the opposite of the Month 3 direction.

### Q9. Concrete recommendation

**Do not do the proposed FrameAction schema redesign.** Finish the current sequential migration and adopt CountryAllocHead on the model side as a separate, decoupled change. Evidence:

1. The score[c,k] + DP infrastructure already exists in the codebase, on both C++ and Python, and is working in production for top-level ops. Extending it to mid-card alloc is model-side work, not schema work.
2. The remaining ~12 unmigrated cards are dominated by single-pick / option-count / card-subset / trap patterns — not allocation patterns. CountryAlloc would not simplify them.
3. Sequential resolution is strictly required for realignment (all realign cards), De-Stalinization (two-node), and any effect that mutates state mid-card. The proposal acknowledges this. So the "collapse to one node" win applies to a small slice.
4. Month 3 priorities per CLAUDE.md are ISMCTS + exploration noise, Elo / league, architecture eval, parallel MCTS, online play, benchmark report. Frame redesign is not on that list.
5. CLAUDE.md explicitly says: "do not mix parser, engine, dataset, and trainer changes in one pass." The proposed change mixes C++ frame struct, Python action encoding, dataset schema, policy target format, and (future) MCTS action rep. Textbook cross-cutting.
6. Bindings don't expose the frame API yet; any downstream MCTS/Python consumer will see whatever schema exists *when we bind it*. That is the correct time to revisit schema.
7. Migration cost estimate (1200-1800 LOC C++, 300-500 LOC Python) ≈ finishing the remaining migration all over again, on top of finishing it once. We pay roughly 2x.

---

## Conclusions

1. **Engine decision granularity and model head factorization are separable.** The proposal conflates them. CountryAlloc on the model side does not require a CountryAlloc frame kind on the engine side.
2. **The CountryAlloc model head already exists in practice** (`dp_decoder.py::bounded_knapsack_dp` used for top-level ops). The sophisticated piece of the proposal is already infrastructure we own.
3. **The proposed FrameAction schema change is a cross-cutting mid-migration refactor** touching C++ frame struct, game_loop pushers, step callbacks, resume_card_N for ~6 migrated cards, Python action encoding, dataset schema, and policy target format. It violates layer-local / reversibility principles in CLAUDE.md.
4. **MCTS branching-factor arguments are hypothetical today.** MCTS/ISMCTS do not consume the frame API (verified via grep of `mcts.cpp`, `mcts_batched.cpp`, `ismcts.cpp`). The benefit materializes only if and when sub-frame MCTS ships, at which point the decision can be revisited against real data.
5. **Only ~5-7 cards genuinely fit CountryAlloc.** Decol, Marshall, Warsaw Pact, Willy Brandt, Truman/TT-type placement. The rest of the remaining ~12 unmigrated cards are non-alloc patterns (SmallChoice, CardSelect, single-region-designate, forced-discard, card-pool).
6. **Realignment and De-Stalinization must stay sequential** per rules. The proposal acknowledges this, which shrinks the "collapse nodes" win further than the prose suggests.
7. **Migration cost ≈ doing the remaining migration twice.** ~1200-1800 LOC C++ + ~300-500 LOC Python, on top of finishing the current migration sequentially.
8. **Month 3 priorities (ISMCTS, Elo, parallel MCTS, architecture eval, online play, benchmark report) get pushed by weeks** if frame redesign lands mid-month.

---

## Recommendations

1. **Finish the current sequential frame migration** for the remaining ~12 cards (24, 32, 39, 43, 45, 47, 52, 68, 78, 83, 84, 90, 91, 97, 102, 105). Keep `FrameAction` as the current scalar variant `{option_index, card_id, country_id}`. No schema change.
2. **Adopt a CountryAllocHead in the model, independently of frame schema.** Extend `bounded_knapsack_dp` usage in `learned_policy.py` to score multi-step country sequences for cards 30 / 23 / 16 / Willy Brandt / TT at training time. The engine continues to emit sequential country picks; the policy continues to return per-step country ids to the frame stack; the *model* uses score[c,k] + DP internally for its proposal distribution. This is a PPO target-shaping change at most.
3. **Add a CardSubsetHead for Ask Not / Summit / Star Wars card-pool cards.** Independent of frame kind. Small, isolated, reversible.
4. **Wire `apply_ops_randomly_impl` (cards 32/52/68) through frame push helpers** as part of finishing the migration. This closes the policy_cb vs frame_stack behavior mismatch without any schema change.
5. **Defer any FrameAction schema redesign until MCTS consumes the frame API and produces measured branching-factor or credit-assignment signal.** At that point, evaluate against real numbers (PPO return, MCTS sim/sec, value calibration) and the migration can be scoped to the cards that empirically hurt.
6. **Do not re-open migrated cards.** Do not touch the 35 existing `resume_card_N` functions for a schema they already work with.
7. **When binding the frame API to Python (eventually, for MCTS)**, surface the current scalar FrameAction shape. If CountryAlloc is needed then, introduce it additively at the binding layer and preserve the scalar path.
8. **Track model-side alloc gains separately** via offline dataset BC + small PPO ablation. If CountryAllocHead shows no measured gain on the 5-7 cards that fit, the whole debate is moot — which we won't know until we run it.

---

## Open Questions

1. Does `bounded_knapsack_dp` with straight-through estimator produce measurably better PPO advantage on Decol-length sequences vs the current per-step multinomial chain? (Run ablation on `results/capacity_test/` rig.)
2. How often does a triggered effect fire mid-card in `apply_ops_randomly_impl` under current behavior? If truly never, the CountryAlloc "frozen eligibility" objection (Q5) is cosmetic. If sometimes, it's a hard blocker.
3. When MCTS eventually consumes the frame API, will it want alloc actions or per-step actions for tree expansion? This is the right time to decide schema, not now.
4. Is there a way to ship CountryAllocHead behind a feature flag so we can A/B it without committing to a policy target format change? (Likely yes via per-frame head routing in `policies/model.py`.)
5. How much of pragmatic-head.md's win comes from CountryAlloc vs from CardSubsetHead + SmallChoiceHead + score[c,k] in general? If the alloc piece is a small fraction, the decision is even clearer.
