# Opus Analysis: Frame Migration Status, Correctness, and Input Features
Date: 2026-04-19T21:50:00Z
Question: Current status of frame migration correctness and frame input features, and the plan.

## Executive Summary

Frame migration is now effectively complete on the C++ engine side: every card flagged unmigrated in `continuation_plan.json` (32, 43, 45, 47, 52, 68, 78, 84) has a `resume_card_*` handler wired into `resume_card_subframe`, and every previously-dormant FrameKind (`ForcedDiscard`, `CancelChoice`, `NoradInfluence`, `FreeOpsInfluence`, `DeferredOps`) is now pushed from at least one call site — the continuation plan's `dormant_framekinds_to_activate` list is stale. The remaining ones (`SetupPlacement`, `Headline`) are correctly deferred placeholders and should be deleted. The largest remaining correctness gaps are **inherited rules bugs** (cards 7, 16 add-branch, 20, 50, 75 per-country caps and options, plus card 98 LADC which was reimplemented but whose value head was never retrained) and the **complete absence of a frame-context feature channel to the neural network**: `nn_features.cpp` exposes 32 public-state scalars and masks but zero frame metadata — the model cannot see frame kind, source card, step index, budget remaining, parent card, or the legal country/card mask. Every sub-frame decision is answered by reusing the same top-level `(influence, cards, scalars)` tensor, which the engine then legality-masks after the fact. This is the single highest-leverage next correctness/strength lever.

## Findings

### Frame Migration Status

FrameKind enum (from `cpp/tscore/decision_frame.hpp:13-25`):

| FrameKind | Pushed from | Resume functions | Status |
|---|---|---|---|
| `TopLevelAR` (0) | Not pushed — default on `DecisionFrame` | N/A | baseline (not a sub-frame) |
| `SmallChoice` (1) | `push_option_frame` (step.cpp, hand_ops.cpp); used by cards 16, 20, 48, 49, 52, 68, 78, 84, 97, 103, plus `resume_ops_randomly` mode pick | 10+ cards | **ACTIVE** |
| `CountryPick` (2) | `push_country_frame` + `push_typed_country_frame` — used by ~40 migrated cards | ~40 | **ACTIVE** |
| `CardSelect` (3) | `push_card_frame` + `push_typed_card_frame` — used by 5, 10, 46, 52, 68, 78, 84, 88, 95, 98, 101 | 11 | **ACTIVE** |
| `ForcedDiscard` (4) | Pushed from `hand_ops.cpp:1096` (trap resolver) and `game_loop.cpp:1830` (CMC cancel follow-on) | `resume_trap_forced_discard`, `resume_card_43` | **ACTIVE** (now pushed; continuation plan was stale) |
| `CancelChoice` (5) | Pushed from `hand_ops.cpp:1136` (CMC cancel opt-in) | `resume_card_43` | **ACTIVE** (now pushed) |
| `FreeOpsInfluence` (6) | Pushed from `game_loop.cpp:713` (Glasnost follow-on) | `resume_free_ops_influence` | **ACTIVE** (now pushed) |
| `NoradInfluence` (7) | Pushed from `game_loop.cpp:226` (NORAD post-coup) | `resume_norad_influence` | **ACTIVE** (now pushed) |
| `DeferredOps` (8) | Pushed from `hand_ops.cpp:820` + `game_loop.cpp:1382` (`push_deferred_ops_country_frame`) | `resume_deferred_ops` | **ACTIVE** (now pushed) |
| `SetupPlacement` (9) | Never pushed (uses whole-action `PolicyFn`) | None | **DORMANT** — continuation plan says "consider deleting" |
| `Headline` (10) | Never pushed (uses whole-action `PolicyFn`) | None | **DORMANT** — continuation plan says "consider deleting" |

Resume dispatch switch (`resume_card_subframe`, `game_loop.cpp:2896-3036`) handles these source cards:
5, 7, 10, 14, 16, 19, 20, 23, 24, 26, 28, 29, 30, 32, 33, 36, 37, 39, 43, 45, 46, 47, 48, 49, 50, 52, 56, 59, 60, 67, 68, 71, 75, 76, 77, 78, 83, 84, 88, 90, 91, 94, 95, 97, 98, 101, 102, 105. **All of `continuation_plan.json:unmigrated_cards = [32, 43, 45, 47, 52, 68, 78, 84]` have resume handlers today.**

Non-card resume functions: `resume_trap_forced_discard`, `resume_norad_influence`, `resume_free_ops_influence`, `resume_deferred_ops`, `resume_ops_randomly` (cards 32/52/68 shared helper covering the SmallChoice mode pick and downstream CountryPicks for Influence/Coup/Realign).

`frame_stack_mode` bail-out guards: 29 hits in `hand_ops.cpp`, 78 in `step.cpp`, 7 in `game_loop.cpp` (total 119 across 5 files), i.e. the guard is universally threaded.

Parity harness status per continuation plan: GREEN — 79/79 tests pass as of 2026-04-19.

### Rules Correctness Remaining Issues

Cross-referencing the 2026-04-19 rules audit with the current `resume_card_*` surface:

**Card 32 — Grain Sales to Soviets (Lone Gunman variant)** (hand_ops.cpp:325, resume_card_32 at game_loop.cpp:2111)
- What the card does: US draws 1 random card from USSR hand; US may play the card as event OR as ops (via `apply_ops_randomly_impl`); then returns the card to USSR, discards it from US hand.
- Current: CardSelect for which USSR card to target (the "draw" is player-selected, NOT random — rules bug), then if in frame mode either `apply_frame_ops_impl` (frame-aware ops) or `apply_ops_randomly_impl` fallback. The draw should be **random** per rules (this mirrors the card-95 Terrorism rules bug which was fixed Tier-2).
- Correct implementation: draw one card via RNG from USSR hand-minus-China-minus-scoring; then give US a choice of (event | ops | return). The policy should not choose which card to "pull".
- Status: **partial** (migrated structure, but mechanic is player-selected rather than random; not a frame-migration issue — it's a pre-existing rules bug).

**Card 43 — Cuban Missile Crisis cancel resolver** (resume_card_43 at game_loop.cpp:1824)
- What it does: Owner of CMC may opt to cancel the effect by discarding a card with ops ≥ 2 from hand.
- Current: CancelChoice (SmallChoice, 2 options: opt-in / skip) then on opt-in pushes ForcedDiscard over ops≥2 hand cards.
- Correct: matches rules. **Fully migrated.**

**Cards 45 / 47 — Quagmire / Bear Trap forced discard** (resume_trap_forced_discard at game_loop.cpp:1803)
- What they do: Phasing trap-holder must discard a card with ops ≥ 2 (not scoring) each AR; if d6 roll ≤ 4 the trap clears.
- Current: ForcedDiscard frame with eligible=ops≥2-non-scoring hand; commit discards the card, rolls the die, clears flag on success (bear_trap_active or quagmire_active based on `source_card`).
- Correct: matches rules. **Fully migrated.**

**Card 52 — Junta (Influence + free coup/realign)** (hand_ops.cpp:422, resume_card_52 at game_loop.cpp:1934)
- What it does: USSR: place 2 infl in one Central/South America country; then free coup OR realignment.
- Current: CardSelect for a hand card (Junta proxy)? Actually `hand_ops.cpp:422` handles Junta's hand draw+opponent-card variant; the coup country pick is part of the shared resume_ops_randomly path when nested ops fire. The Junta-as-event path also migrates via step.cpp (resume_card_50 actually handles the place + coup; see rules audit §Card 50).
- Rules audit flagged: lacks realignment option, forces coup. Pre-existing; not introduced by frame migration.
- Status: **migrated but rules-incomplete** (realign branch missing).

**Card 68 — Lone Gunman** (hand_ops.cpp:501, resume_card_68 at game_loop.cpp:1728)
- What it does: Similar to card 32 — reveal US hand; USSR may use 1 US card as ops (via `apply_ops_randomly_impl`).
- Current: CardSelect over US hand, then `apply_frame_ops_impl` (via resume_ops_randomly for SmallChoice mode + CountryPick frames). **Now fully frame-aware** (no silent `apply_ops_randomly_impl` fall-through in frame mode, per the hand_ops.cpp:350 guard).
- Correct: matches rules shape. **Fully migrated**; any bug is in the shared resume_ops_randomly helper (e.g. mode-pick as SmallChoice over {Infl, Infl, Coup, Realign} where the two Influence slots appear to be a redundancy — worth re-auditing but orthogonal).

**Card 78 — Ask Not What Your Country…** (hand_ops.cpp:550, resume_card_78 at game_loop.cpp:2302)
- What it does: US chooses 0..up-to-4 cards in hand to discard; draws replacements.
- Current: SmallChoice (count 0..N), then N sequential CardSelects with running `eligible_cards` exclusion; after completion, draws count cards via `draw_one_frame`.
- Correct: matches rules shape. **Fully migrated.** Minor: the count semantics include 0 (code uses `std::clamp(action.option_index, 0, ...)` and short-circuits to `finish_frame_event` when 0).

**Card 84 — ABC Africa? / Alliance for Progress? (Our Man in Tehran)** (hand_ops.cpp:619, resume_card_84 at game_loop.cpp:2363)
- What it does: Draw top N cards, US keeps a chosen subset, rest are discarded.
- Current: SmallChoice (keep-count 0..N), then keep-count CardSelects among drawn cards with running exclusion; non-selected drawn cards discarded.
- Correct: matches rules shape. **Fully migrated.**

**Summary**: Of the continuation-plan "unmigrated_cards" list:
- Fully migrated & rules-matching: 43, 45, 47, 68, 78, 84
- Fully migrated but rules-incomplete (pre-existing): 32 (should be random draw, not player-selected), 52 (missing realignment branch)

The **bigger remaining correctness surface** is the unrelated Tier-3 deferred fixes plus several pre-existing bugs not yet on any tier (all audited on 2026-04-19):
- Card 7 Socialist Governments: per-country cap enforced as ≤1 via pool-erasure instead of the ≤2 rule.
- Card 16 Warsaw Pact add-5 branch: Tier-2 added 2-per-country cap; audit confirms it landed.
- Card 20 Olympic Games boycott: frozen accessibility pool + no double-cost for opponent control + missing +2 phasing-player die bonus.
- Card 30 Decolonization: Tier-1 fix landed (distinct-country enforcement).
- Card 33 De-Stalinization: Tier-1 fix landed (phase 1 remove, phase 2 place, 2-per-country cap).
- Card 50 Junta: missing realignment option, forced coup.
- Card 60 ABM Treaty: Tier-2 "correct accessibility" landed but original audit flagged (a) wrong VP reward, (b) wrong placement count (2 vs 4). Verify fix went all the way.
- Card 75 Voice of America: Tier-3, forced 1-per-country instead of up-to-2.
- Card 77 Ussuri River Skirmish: Tier-1 fix landed (Asia-only pool + 2-per-country cap).
- Card 95 Terrorism: Tier-2 landed (random discard).
- Card 98 Latin American Debt Crisis: Tier-1 reimplemented from scratch; behavior change is the largest — policy's value head was never retrained post-fix and event-play frequency on this card should be treated as a diagnostic (per `opus_analysis_20260419_083500_rules_fix_plan.md`).

**Paired-engine A/B to quantify all Tier-1+2 fixes was specified and skipped** (per `opus_analysis_20260419_210000_engine_fix_model_history.md` conclusion #4). This remains the single most useful unblocked correctness measurement.

### Frame Input Features: What the Model Sees

`cpp/tscore/nn_features.cpp` (`fill_scalars`, `fill_cards`, `fill_influence_array`) defines the **entire** input surface to the neural net:

**Influence tensor** (B, 172) — 86 countries × 2 sides of raw influence counts (0..N), unnormalized.

**Cards tensor** (B, 448) — 4 × 112 binary masks: (actor_hand, actor_hand duplicated, discard, removed). Note: the "actor_hand" appears twice; second slot is intended for an observation of opponent known-in-hand but currently repeats actor hand.

**Scalars tensor** (B, 32):
- [0] vp/20
- [1] (defcon-1)/4
- [2] milops USSR /6
- [3] milops US /6
- [4] space USSR /9
- [5] space US /9
- [6] china_held_by (side index)
- [7] holds_china (bool)
- [8] turn/10
- [9] ar/8
- [10] acting_side index
- [11-27] 17 active-effect flags (bear_trap, quagmire, CMC, Iran-hostage, NORAD, shuttle, SALT, flower_power, flower_power_cancelled, vietnam, north_sea, glasnost_free_ops/4, nato, de_gaulle, nuclear_subs, formosan, awacs)
- [28-29] chernobyl region active + index/6
- [30-31] ops_modifier per side /3

**What the model DOES NOT see:**
- **FrameKind** — model cannot distinguish a top-level AR decision from a Decolonization step 2 CountryPick, a CMC ForcedDiscard, or a NORAD placement. All sub-frames reuse the top-level scalar tensor unchanged.
- **source_card** on the current frame — model has no feature telling it "we are resolving card 33 step 3" vs "top-level AR". The only proxy is the active-effect flags for long-lived cards (bear_trap, quagmire, vietnam, etc.), which only cover 17 of 110 cards and only when effects are latched.
- **step_index / total_steps** — multi-step sequences (Decolonization 4 picks, Marshall 7 picks, De-Stal 8 picks) are invisible; the model produces the same logits on step 0 as on step 6 for the same post-commit state.
- **budget_remaining** — for `FreeOpsInfluence` (Glasnost) and `DeferredOps` the budget can be 1-4; model cannot see it. For top-level ops it's recoverable from the chosen card's ops + flags, but for sub-frames there's no such anchor.
- **parent_card** — for `resolve_frame_selected_event` nested events (e.g., card 88 Star Wars fires a card from discard, which may itself push sub-frames), the model has no feature telling it which card spawned the current frame.
- **eligible_countries / eligible_cards masks** — the legal mask on the current frame is used post-hoc to zero out illegal action logits in `learned_policy.cpp`; it is **not fed into the encoder**. The model makes its logit prediction without knowing which country/card subset is legal, then legality is masked afterward.
- **criteria_bits** — e.g., De-Stalinization src-country carried on dst frame, Warsaw Pact add/remove mode flag. Invisible.
- **Head routing** — the model has a single `country_logits`, single `card_logits`, single `mode_logits`, single `small_choice_logits` head. There is no per-frame-kind head; the orchestration layer picks which head to consume based on the frame kind, but the model itself doesn't know which head will be read.

**Net**: the Python inference layer (`learned_policy.cpp`, `learned_policy.py`) receives a frame reference from the engine but translates it into a flat `(influence, cards, scalars)` tensor that is frame-agnostic. The frame-aware information lives **only** outside the model: in the legality mask applied after the logits are produced, and in the head-selection logic.

### Gaps and Problems

1. **Frame context is not an input feature.** The most important mismatch. The model must guess based on public state which sub-frame it's in — for example, on a Decolonization step 3 the only signal is that 3 Africa/SEAsia countries gained +1 USSR infl since the event fired. If the post-commit state happens to look like a natural game state, the model cannot tell whether this is a CountryPick for Decolonization step 3, for Marshall Plan step 6, for COMECON step 2, or for the top-level ops placement. The legality mask disambiguates eligibility but does not inform the encoder; the logits are produced blind and then filtered.

2. **No head-routing conditioning.** The model emits `card_logits`, `mode_logits`, `country_logits`, `small_choice_logits` unconditionally every forward pass; the choice of which is "live" is made externally by frame kind. A model that knew the frame kind could specialize feature extraction.

3. **Continuation plan is stale.** `unmigrated_cards = [32, 43, 45, 47, 52, 68, 78, 84]` is no longer accurate — all eight have resume handlers. Likewise `dormant_framekinds_to_activate = [ForcedDiscard, CancelChoice, NoradInfluence, FreeOpsInfluence, DeferredOps]` — all are active. Only `SetupPlacement` and `Headline` remain dormant (and are candidates for deletion).

4. **The apply_ops_randomly_impl silent divergence is NOT fully closed.** Per `hand_ops.cpp:340-354`, card 32 calls `apply_frame_ops_impl` only when `gs.frame_stack_mode && policy_cb == nullptr`; otherwise it falls back to `apply_ops_randomly_impl` (which uses policy_cb if available, else RNG). This is the correct dual-path but means the two paths must produce semantically-equivalent traces — something the parity harness is supposed to prove at 79/79. Status is green but this is the single thinnest part of the migration.

5. **Paired A/B never ran.** The post-Tier-1+2 ΔWR on frozen panel checkpoints was never measured. The best available evidence is circumstantial (post-fix panel combined WR = 41-45% with ~0.55/0.35 USSR/US asymmetry), but the `strength-cost-of-fixes` and the policy's behavior on card 98 LADC post-fix remain quantitatively unknown.

6. **Python bindings still do not expose the frame API.** Per the 20260419 migration-plan audit §4, `bindings/tscore_bindings.cpp` has zero references to `engine_peek`, `engine_step_subframe`, `engine_step_toplevel`, `frame_stack`, or `DecisionFrame`. The frame API is currently C++-only. This blocks any future MCTS / self-play / play-server consumer from driving the frame path from Python.

7. **Pre-existing rules bugs still unfixed.** Cards 7 (no 2-per-country stacking), 20 (three bugs), 50 (no realign), 60 (verify Tier-2 covered all three sub-bugs), 75 (forced 1-per-country), 32 (should be random draw). These are not frame-migration issues but they hurt ground-truth strength.

## Conclusions

1. **Frame migration is effectively complete** — every card flagged unmigrated in the continuation plan has a resume handler, every dormant FrameKind except the two whole-action kinds (SetupPlacement, Headline) is actively pushed, and the parity harness is green at 79/79. The continuation plan's migration status fields are stale and should be updated to reflect the current state.

2. **The remaining correctness surface is rules bugs, not migration gaps.** Tier-3 deferred cards (75, 50) and a handful of pre-existing bugs (7, 20, 32-as-random, 60 sub-bugs) are the only known rules issues. Frame-migration-specific regressions are zero.

3. **The neural network receives no frame context.** The 32-scalar + card-mask + influence-array feature bundle is entirely top-level; the model sees no frame kind, source card, step index, budget, parent card, or eligibility mask. This is the single highest-value gap and applies to every multi-step card and every non-top-level resolver.

4. **Head routing is external and unconditioned.** The model produces all heads every call, and the frame-kind-to-head mapping lives in `learned_policy`. A frame-aware encoder could specialize this internally.

5. **The paired-engine A/B that would quantify Tier-1+2 WR impact was never run.** This is the best-defined unblocked correctness-strength measurement available.

6. **The 1.35M-row BC corpus on the buggy engine is partially contaminated** and still in use (the v56 BC baseline + awr_v4_bc_diverse parquet descend from it). A post-fix BC corpus on the fixed engine would be the clean foundation for a re-blessed training chain.

7. **Python bindings for the frame API do not exist.** This blocks any Python-driven consumer of the frame path (MCTS extension, play-server, external analysis).

## Recommendations

Prioritized. Effort estimates in engineer-hours.

1. **Add a frame-context feature channel to `nn_features.cpp`** — **highest leverage**. Append ~16-24 scalars plus two masks to the feature bundle, populated when `engine_peek` returns a non-empty frame:
   - frame_kind onehot (8-11 dims; one per active FrameKind)
   - source_card id / 112 (scalar)
   - parent_card id / 112 (scalar)
   - step_index / max_steps (scalar; max_steps known from engine)
   - total_steps / max_steps (scalar)
   - budget_remaining / max_budget (scalar; max_budget=4 for Glasnost/DeferredOps, else 0)
   - criteria_bits low 8 bits as scalar
   - stack_depth / max_depth (scalar)
   - Two boolean masks (111 cards, 86 countries) for `eligible_cards` and `eligible_countries` — these already exist in the frame.
   This is a one-commit change to C++ `fill_scalars` + Python `SCALAR_DIM` bump + BC/PPO retraining. **Effort: 4-8h engineer + 1-2 training cycles**. All existing scripted checkpoints become incompatible (same pattern as the 21-dim→32-dim bump in PPO v3).

2. **Run the paired-engine A/B on Tier-1+2 fixes.** Build two engine binaries (`d8b8934^` and HEAD), benchmark v20/v44/v54/v55/v56/gnn_card_attn_v1/current best under identical seeds, vs random + heuristic, 500 games/side. Quantify ΔWR and per-card event-play rate changes. **Effort: 2-4h**. Without this, the strength claim "engine fixes help evaluation fairness" is qualitative.

3. **Update `continuation_plan.json`** to reflect: `unmigrated_cards: []`, move all five previously-dormant kinds out of the activate list, move `SetupPlacement` and `Headline` into `dormant_framekinds_confirm_delete`. **Effort: 10min**.

4. **Delete `SetupPlacement` and `Headline` from the FrameKind enum** (or keep and wire them if there's a concrete whole-action-frame consumer). Current status is dead weight. **Effort: 30min to delete, 4-6h to wire if kept.**

5. **Fix the pre-existing rules bugs as Tier-3.5 (batched):** card 32 random draw (not player-selected), card 50 realign branch, card 7 per-country 2-cap, card 20 accessibility refresh + opponent-control cost + +2 die bonus, card 75 per-country 2-cap. Each touches both `step.cpp` (or `hand_ops.cpp`) AND `resume_card_*` atomically to keep parity green. **Effort: 8-14h total**, with paired A/B gate after.

6. **Expose the frame API to Python bindings** (`bindings/tscore_bindings.cpp`). Add `engine_peek`, `engine_step_toplevel`, `engine_step_subframe`, `DecisionFrame` read-only properties, `FrameAction` writable, `StepResult`. **Effort: 4-6h**, unblocks any Python-side MCTS / play-server / online-play consumer.

7. **Add head-routing conditioning to the model.** Once the frame-kind onehot feature lands, inject a FiLM-style conditioning layer into the existing GNN / attention models, gating the per-head outputs on frame kind. **Effort: 6-10h**, part of an architecture experiment cycle. Expected gain: better per-frame-kind logit sharpness; measured via val_adv_card_acc / val_adv_country_acc on a frame-annotated dataset.

8. **Collect a fresh BC corpus on the fixed engine** with the new frame-feature channel active. Replace `data/awr_eval/v4_bc_diverse_v1/` (which descends from the buggy-engine 1.35M-row corpus) with a clean-engine rollout set using v56 BC + ppo_ussr_only_v5 + ppo_us_only_v5 + gnn_card_attn_v1 as the data-generating models. **Effort: 4-6h compute**.

9. **Gate the next PPO chain restart on frame-features landing.** If recommendation #1 ships, the resulting checkpoint line is not interchangeable with v20..v310_sc (all 32-scalar); treat this as a generational break and freeze a new Elo anchor on the frame-feature engine (`v14_e3`).

## Open Questions

1. Should the frame-feature tensor be appended to `scalars` (increasing SCALAR_DIM to ~50-55) or emitted as a separate encoder input (e.g., `frame_context`)? Appending is simpler; separate input allows dedicated encoder and conditional gating.

2. The `eligible_cards` / `eligible_countries` masks are already computed by the engine and used for legality after-the-fact. Passing them INTO the encoder is a ~197-bit addition. Is there measurable gain from encoder awareness of legality vs. post-hoc masking? Worth an ablation.

3. For nested events (card 88 Star Wars firing a card from discard), should `parent_card` be surfaced as an additional scalar/onehot, or should the frame `source_card` field already capture it (it currently does)? Confirm by tracing a Star Wars play under frame_stack_mode.

4. Is the `apply_ops_randomly_impl` mode pick (SmallChoice over 4 = {Infl, Infl, Coup, Realign}) correctly defined? The two Infl slots look like a redundancy; if intentional (e.g., to bias mode distribution in the RNG path), it should be documented.

5. How does the current paired A/B gap interact with the "fresh Elo anchor" recommendation? If Tier-1+2 ΔWR turns out to be <2pp per checkpoint, the old Elo ladder could possibly be retained; if >5pp, it must be reset. The A/B resolves this.

6. Should `SetupPlacement` and `Headline` be wired as their own `engine_step_setup_card` / `engine_step_headline_card` entry points, or removed? Wiring them enables a fully-frame-driven whole-game observation stream (useful for MCTS and online play); removal simplifies the enum. Decision should precede recommendation #4.

7. The continuation plan's `apply_ops_randomly_impl_silent_divergence` note says Slice E was meant to close the parity gap on cards 32/52/68. Per the current code, Slice E has landed (resume_ops_randomly exists, frame_stack_mode guards are in place). Confirm this in the next parity-harness run.
