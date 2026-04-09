# Experimental Subtree Ownership

This subtree is delegated to an independent Codex experiment agent.

Rules for the main Claude/control-plane agent:
- Do not commit changes inside `experimental/`.
- Do not move code from `experimental/` into production paths without an
  explicit handoff and review.
- Treat this subtree as a sandbox for isolated benchmarks and prototypes.
- Do not request or apply edits outside `experimental/` as part of work rooted
  here.

