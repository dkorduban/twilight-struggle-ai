---
name: codex-mcp
description: How to use OpenAI Codex via MCP tools for code generation, plan review, and collaborative implementation loops. Use when calling Codex for implementation, review, or any cross-model collaboration.
---

# Codex MCP Usage Guide

## Tools

| Tool | Purpose |
|------|---------|
| `mcp__codex__codex` | Start a new Codex session. Returns a threadId + response. |
| `mcp__codex__codex-reply` | Continue an existing session using threadId. |

## Session Management

Codex sessions are **stateful** via threadId. Always:
1. Save the `threadId` from the first `mcp__codex__codex` call
2. Use `mcp__codex__codex-reply` with that threadId for all follow-ups
3. Never start a new session when continuing the same task — context carries forward

## Key Parameters

### sandbox
| Mode | When to Use |
|------|-------------|
| `read-only` | Plan review, code audit, Q&A — Codex reads but cannot write files |
| `workspace-write` | Implementation — Codex writes files in the project directory |

### approval-policy
| Policy | When to Use |
|--------|-------------|
| `never` | **Background agents** (no UI → hangs forever on approval prompt). Also review-only tasks. |
| `on-failure` | **Foreground** implementation — auto-approve commands, intervene on errors |
| `on-request` | Avoid in background — same hang risk as interactive approval |

### developer-instructions
Inject a persona or constraints into Codex without polluting the main prompt.
Always include: `"Be concise. Do not include your reasoning process in the response. Only output the result."`

## Resume Loop Pattern (CRITICAL)

Codex frequently returns control after partial progress (reading files, making a few edits).
**The caller must resume via `codex-reply` until Codex reports completion.**

### Pattern for background agents (bg-codex-implementer)
```
1. Call mcp__codex__codex with full task prompt → get threadId + partial response
2. While response does not indicate completion:
   a. Call mcp__codex__codex-reply(threadId, "continue") 
   b. Check if Codex says "done", "complete", "all changes made", etc.
3. Write result to .codex_tasks/<task_id>/result.md
```

### Pattern for foreground (main agent)
```
1. Call mcp__codex__codex → get threadId
2. If Codex returned partial work, call mcp__codex__codex-reply(threadId, "continue implementing")
3. Repeat until done (cap at 5 iterations)
```

### Delegation pattern (background Codex via subagent)

**Use a general-purpose Sonnet agent** (not a custom Haiku agent) to dispatch to Codex:
```
Agent(model: "sonnet", isolation: "worktree", run_in_background: true,
      prompt: "You are a Codex dispatcher. Call mcp__codex__codex early
               with approval-policy='never', sandbox='workspace-write'.
               Resume with mcp__codex__codex-reply until done. Codex does
               the heavy implementation — you may read files or check output
               lightly when needed, but don't implement code yourself.
               <full task prompt>")
```

**Why Sonnet?** General-purpose subagents inherit MCP tools from the parent session.
Custom agent types (bg-codex-implementer, codex-only, policy-opt-codex-haiku) with
`mcpServers:` in YAML frontmatter do NOT get MCP tools registered by the runtime.
Confirmed: 0/5 Haiku custom agents succeeded, Sonnet general-purpose agents work reliably.

## Prompting Best Practices

1. **Termination signals**: Ask Codex to reply "APPROVED" or "CHANGES NEEDED" — gives clear loop control
2. **Feedback verbatim**: When sending review feedback via codex-reply, quote specific issues exactly. Do not summarize.
3. **Concise responses**: Always instruct Codex to be concise via developer-instructions to save tokens
4. **Max iterations**: Always enforce a hard cap (default: 5) on review loops

## stderr Suppression

The MCP server config uses `2>/dev/null` at the process level.
Individual tool calls do NOT need stderr suppression — MCP returns structured JSON-RPC responses only.

See reference.md for detailed examples and patterns.
