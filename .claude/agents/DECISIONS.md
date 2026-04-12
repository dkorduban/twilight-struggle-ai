# Agent Decisions Log

## 2026-04-12 — Remove bg-codex-analyzer

**Removed:** `.claude/agents/bg-codex-analyzer.md`

**Why:**

`bg-codex-analyzer` had no `mcpServers:` in its YAML frontmatter, which means
`mcp__codex__codex` was never registered in its tool list. The body instructions
said "use Codex for complex scripts > 40 lines" — but this was dead code. The
agent always did the work itself using Read/Grep/Glob/Bash, hitting its 25-turn
ceiling before finishing non-trivial tasks.

Concrete failure: ISMCTS engine validity audit (2026-04-12) — the agent spent all
25 turns reading C++ files and died before writing `result.md`. Redispatching to a
general-purpose Sonnet agent (which inherits MCP tools from the parent session)
completed the same audit with `result.md` written and 3 engine bugs identified.

**Pattern that works instead:**

Use a general-purpose Sonnet agent with `mcp__codex__codex` available (inherited
from parent session). Instruct it to delegate to Codex for any non-trivial analysis
or code generation. This has no turn ceiling on Codex's side and produces committed
output files.

    Agent(
        subagent_type="general-purpose",
        model="sonnet",
        run_in_background=True,
        prompt="Call mcp__codex__codex to [task]..."
    )

**Reference commit:** see `git log --oneline | grep bg-codex-analyzer`
