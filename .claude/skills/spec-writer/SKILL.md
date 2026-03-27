---
name: spec-writer
description: "Explore codebase with Haiku, synthesize a tight machine-readable implementation spec. Output feeds directly into /feature-coder or /tdd-fixer — no plan-audit loop. Triggers on: /spec-writer, write a spec, spec out this feature, spec before coding."
---

# Spec-Writer — Haiku Explores, Sonnet Specifies

Produces a `.claude/plan/<name>.md` spec ready for `/feature-coder` or `/tdd-fixer`.
**No Codex audit loop. No Plan agent.** Haiku does discovery; this session synthesizes.

## Input

Task description as the argument. Optionally: an existing rough notes file.

## Happy-path Claude cost: low

Phase 1 (Haiku Explore subagent) does all file reading. This session only synthesizes.
Target: ≤ 5 main-session turns on the happy path.

## Tool Requirements

- `Task` — Haiku Explore subagent for discovery
- `Read`, `Glob`, `Grep` — fallback lookups only
- `Write` — save spec file

## Execution

### Phase 1: Discovery (Haiku Explore subagent)

Launch a Task agent (subagent_type: "Explore", model: "haiku") with:

```
Explore the codebase to answer these questions for the task: "{task description}"

1. Which existing files are most relevant? (list paths + 1-line purpose)
2. What test file conventions exist? (naming, fixture patterns, imports)
3. What interfaces/types/schemas does the new code need to conform to?
4. Are there similar existing implementations to follow as a pattern?
5. What are the exact file paths that need to be created or modified?

Return structured answers only. No prose. No implementation.
```

### Phase 2: Spec Synthesis (this session)

Using the Explore output, write `.claude/plan/<feature-name>.md` with this structure:

```markdown
# Spec: <feature name>

## Goal
One paragraph. What this does and why.

## Files to create
- `path/to/new_file.py` — purpose

## Files to modify
- `path/to/existing.py` — what changes and why

## Interfaces / signatures
Exact function signatures, class definitions, schema fields.
Copy from existing patterns where applicable.

## Test cases (required)
List as bullet points:
- test_<name>: <what it asserts> — <setup required>
- test_<name>_edge_case: <edge condition>
(minimum 3, cover happy path + 1 error path + 1 edge case)

## Acceptance criteria
- [ ] All listed test cases pass
- [ ] No regressions: `uv run pytest tests/python/ -q` green
- [ ] Follows existing code conventions (no new deps, no style changes)

## Constraints
Any project-specific rules (e.g. "no in-place frozenset mutation", "use _vp_delta not pub.vp +=")
```

### Phase 3: Deliver

Print:
```
Spec saved to `.claude/plan/<feature-name>.md`

To implement:  /feature-coder .claude/plan/<feature-name>.md
To TDD:        /tdd-fixer .claude/plan/<feature-name>.md
```

Stop. Do not implement.
