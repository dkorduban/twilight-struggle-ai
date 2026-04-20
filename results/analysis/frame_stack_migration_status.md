# Frame Stack Migration — Status (2026-04-18)

## What's done (Slices 1+2)

**Slice 1** — New types + dead infrastructure (4 commits, cherry-picked to main):
- `cpp/tscore/decision_frame.hpp`: `FrameKind`, `DecisionFrame`, `FrameAction`, `StepResult`, `SubframePolicyFn`
- `GameState.frame_stack: std::vector<DecisionFrame>` (member exists, never written/read yet)
- `engine_peek(gs)`, `engine_step_toplevel(...)`, `engine_step_subframe(...)` declared + implemented

**Slice 2** — Adapter bridge (1 commit, main):
- `event_decision_to_frame(EventDecision → DecisionFrame)` converter
- `frame_action_to_index(FrameAction → int)` converter
- `engine_step_toplevel` now creates a `PolicyCallbackFn` adapter from `sub_policy` and passes it to `apply_action_live`

**Status**: WRs preserved (USSR 0.57 / US 0.36), 54/54 C++ tests pass.

## What's NOT done

The adapter approach is **synchronous** — `sub_policy` is called inside `apply_action_live` before control returns to the caller. This means:

- `frame_stack` is never pushed to or popped from — it's dead code
- The caller cannot "pause and resume" between sub-decisions
- **The user's stated goal** ("user step may be 2 policy calls sequential; all that sub ar state must be encoded and presented to model") is NOT achieved

To achieve real push/pop semantics, ~148 callback sites in `step.cpp` and `hand_ops.cpp` must be converted to:
1. Push a `DecisionFrame` to `gs.frame_stack`
2. Return from the handler (yield)
3. Caller calls `engine_step_subframe(gs, action, rng)` to apply the sub-choice and resume

## Cost estimate for remaining slices

| Slice | Description | Effort | Risk |
|-------|-------------|--------|------|
| 3 | Convert ~60 event handlers in step.cpp to push frames | 3-5 days | High (WR regression risk per card) |
| 4 | Convert hand_ops.cpp (NORAD, Glasnost, CMC) | 1-2 days | Medium |
| 5 | Update observation features to encode frame_stack | 1 day | Low |
| 6 | Update dataset schema / MCTS alignment | 1 day | Medium |
| 7 | Delete PolicyCallbackFn + EventDecision + policy_callback.hpp | 0.5 day | Low (cleanup) |

**Total: ~7-10 days**, with Slice 3 being the critical path and regression risk.

## Decision needed

Option A: **Current adapter is enough**
- `engine_step_toplevel(gs, action, side, rng, sub_policy)` is the clean public API
- Internal `PolicyCallbackFn` is an implementation detail hidden from callers
- Sub-choices are driven by `sub_policy` synchronously (works for training/MCTS)
- Skip Slices 3-7 until there's concrete demand

Option B: **Push through to real frame_stack**
- 2-policy-call-sequential semantics become possible
- Enables cleaner model conditioning on sub-AR state
- Required for the "encoded sub-AR state presented to model" use case
- Authorize Slices 3-7 explicitly; plan 1-2 week timeline

## Recommendation

If the goal is having the policy model decide sub-choices with full game state context, Option A (adapter) already achieves this — `sub_policy(gs, frame)` is called with the current `GameState` and the `DecisionFrame` describing the choice. The only missing piece vs. Option B is that control doesn't return to the Python caller between sub-decisions within one AR.

If you need per-sub-decision batching (e.g., gather all NORAD country picks across a batch of games simultaneously), Option B is needed.
