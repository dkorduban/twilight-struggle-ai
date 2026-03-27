---
name: rules-batcher
description: "Batch 5-20 rules/card questions into one Haiku agent call that reads PDF + docs once and answers all. Replaces per-question rules-lawyer calls. Triggers on: /rules-batcher, batch rules questions, look up these cards, verify these rules."
---

# Rules-Batcher — One Haiku Agent Answers Many Questions

**Cost model: one Haiku subagent reads all sources once, answers everything.**
Never spawn one agent per question. Max 20 questions per invocation.

## Input

Questions as the argument, one per line. Or a file path containing questions.
Questions can be:
- Card rule clarifications: "Card 47 Bear Trap: does the escape roll consume the card?"
- Rules edge cases: "Can USSR coup a BG country at DEFCON 2 if it triggers nuclear war?"
- Implementation checks: "Does Formosan Resolution grant +1 to Taiwan stability or just BG status?"
- Scoring questions: "Does adjacency bonus apply to non-BG countries adjacent to superpowers?"

Max 20 questions. For more, call this skill twice.

## Tool Requirements

- `Task` — one Haiku subagent (all sources + all questions)
- `Write` (optional) — save answers to file

## Execution

### Step 1: Collect questions (Claude, 1 turn)

Parse the input into a numbered list of questions.

### Step 2: Haiku batch agent

Launch a Task agent (subagent_type: "rules-lawyer", model: "haiku") with:

```
You are a Twilight Struggle rules expert. Answer each numbered question using ONLY
the sources listed below. For each answer:
- Quote the exact relevant rule text (with section number if available)
- State VERIFIED if from a source below, UNVERIFIED if from memory only
- Flag CONFLICT if sources disagree
- Flag OPEN if the sources do not cover the question

SOURCES (read in this order, stop when question is answered):
1. docs/TS_Rules_Deluxe.pdf — official rules (use pypdf to read)
2. docs/event_scope.md — implementation scope decisions
3. data/spec/cards.csv — card stats (ops, era, side, starred)
4. python/tsrl/engine/events.py — current implementation (for "how is X implemented")
5. python/tsrl/engine/cat_c_events.py — hand-interaction card implementations

QUESTIONS:
{numbered question list}

Return a structured answer for each question:

## Q{N}: {question text}
**Answer:** {answer}
**Source:** {source name + section/line}
**Status:** VERIFIED | UNVERIFIED | CONFLICT | OPEN
```

### Step 3: Format and deliver (Claude, 1 turn)

Present the answers. Flag any CONFLICT or OPEN items prominently.

If any OPEN items exist, note them as candidates for `docs/project_open_rules_questions.md`.

Optionally save to `.claude/rules-answers/<timestamp>.md` if more than 5 questions.
