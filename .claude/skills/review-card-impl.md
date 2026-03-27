# review-card-impl

Review Twilight Struggle card event handler implementations for correctness.

## Usage

```
/review-card-impl <card_id> [card_id] [card_id]
```

**Maximum 3 cards per invocation.** For larger batches, call this skill multiple times.

Examples:
- `/review-card-impl 47` — review Bear Trap
- `/review-card-impl 32 78 84` — review 3 Cat C cards

## Two modes

### Review mode (default)
Read the handler, ground the official text, check for bugs, produce a structured report. Do not edit files.

### Fix mode (`/review-card-impl --fix <card_id> ...`)
After review produces a bug report, re-invoke with `--fix` to delegate bounded fixes to codex-implementer. Only invoke fix mode when bugs are confirmed and patches are fully specified in the review output.

---

## Review procedure (per card)

### Step 1 — Locate the handler

Search in order:
1. `python/tsrl/engine/cat_c_events.py` (Cat C hand-interaction cards)
2. `python/tsrl/engine/events.py` (all other cards)

Find the exact function and note its line number. If the handler delegates logic to another file (e.g., Quagmire/Bear Trap delegate to `game_loop._resolve_trap_ar`), **read that file too** before forming any opinion.

### Step 2 — Ground the official card text

Check in this order:
1. `docs/event_scope.md` — if the card is documented there, quote it verbatim
2. `data/spec/cards.csv` — verify ops, era, side, starred fields
3. Known GMT Deluxe Edition text from memory — **only if steps 1-2 leave gaps, and only if you are confident**. If uncertain, write `[UNVERIFIED]` next to the text.

**Do not invent card text.** If you cannot verify, say so explicitly and flag it as an open question.

### Step 3 — Check the implementation

Verify:
- Correct side, amount, region per card text
- Correct starred-card handling (→ `removed`, not `discard`)
- Guard conditions present (e.g., "only if US controls X", "only if ahead in Space Race")
- VP grants are conditional where the card text requires it
- Persistent-flag set/clear scope is correct
- No spurious filters (e.g., ops >= N when card text has no such restriction)
- Cross-file logic: if the handler sets a flag and delegates to game_loop, read game_loop too

### Step 4 — Produce the report

For each card:

```
### Card N — Name
**Official text:** "..." [UNVERIFIED if not from docs/]
**Handler:** `_event_foo` / `file.py:line`
**Status:** correct | BUGS FOUND | VERIFY (open question)
**Bugs:**
- Bug description
  Old code (file.py:line): `exact line(s)`
  Proposed fix: `exact replacement`
**Ambiguities:** none | description → add to project_open_rules_questions.md
```

**Quote the exact lines for every bug.** Do not describe bugs without showing the code.

---

## Fix mode procedure

When invoked with `--fix`:

1. Take the bug report from the review pass as input (must be in the format above).
2. For each bug, construct a tight codex-implementer task packet:
   - `Allowed files`: only the one file containing the bug
   - `Goal`: paste exact old code and exact new code
   - `Execution rules`: read file first; re-read modified lines after each edit to confirm change landed; do not modify any parameter not mentioned in the goal
   - `Acceptance checks`: `uv run pytest tests/python/ -q` must pass; show last 5 lines of output
3. Send **one bug at a time** to codex-implementer when bugs are in different files. Batch only when bugs are in the same function.
4. After codex returns, verify the edit actually landed by reading the modified lines before declaring success.

---

## Constraints

- Max 3 cards per review invocation. For larger batches, use multiple calls.
- Review-only by default. Never edit files in review mode.
- Do not re-implement cards not yet in the registry.
- Do not refactor unrelated code.
- Cat C cards: also verify `gs.hands` mutations use frozenset operations (no in-place mutation).
- Cards that delegate to game_loop (45 Quagmire, 47 Bear Trap): read game_loop too before reporting bugs on the flag-setter.
