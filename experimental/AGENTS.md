# Experimental Subtree Agent Rules

This subtree is controlled by an independent Codex agent for isolated
experiments.

Rules:
- Do not change, stage, or commit any file outside `experimental/`.
- The main Claude agent must not commit changes in `experimental/`.
- Codex owns commits that touch `experimental/`.
- Any commit that touches `experimental/` must include a
  `Co-authored-by:` trailer.
- Keep experiments self-contained, reversible, and documented.
- Nothing in `experimental/` changes production behavior unless it is promoted
  elsewhere by an explicit follow-up task.

