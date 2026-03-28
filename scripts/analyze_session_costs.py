#!/usr/bin/env python3
"""
Analyze Claude Code session transcripts for token usage and cost breakdown.
Streams JSONL files line by line to handle large files efficiently.
"""
import json
import sys
from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Optional

# Pricing per million tokens
PRICING = {
    "sonnet": {
        "input": 3.0,
        "output": 15.0,
        "cache_read": 0.30,
        "cache_creation": 3.75,
    },
    "haiku": {
        "input": 0.80,
        "output": 4.0,
        "cache_read": 0.08,
        "cache_creation": 1.0,
    },
}

SESSION_FILES = {
    "aba177c5": ("aba177c5-eef2-41a2-af47-b8449cc53b84.jsonl", "Mar 28, 45MB"),
    "409c1153": ("409c1153-0697-4629-9146-a65326e6695e.jsonl", "Mar 27, 893KB"),
    "fd6e2044": ("fd6e2044-8fab-49f7-9ef8-fb7c1d022f86.jsonl", "Mar 27, 95KB"),
    "2ca85944": ("2ca85944-5e4f-4d17-b3e2-f41687c30d2d.jsonl", "Mar 27, 6KB"),
}

BASE_DIR = Path("/home/dkord/.claude/projects/-home-dkord-code-twilight-struggle-ai")


@dataclass
class TurnStats:
    turns: int = 0
    input_tok: int = 0
    output_tok: int = 0
    cache_read: int = 0
    cache_creation: int = 0
    cost_usd: float = 0.0
    direct_cost_usd: float = 0.0  # from costUSD field


@dataclass
class SessionStats:
    session_id: str
    label: str
    total: TurnStats = field(default_factory=TurnStats)
    by_type: dict = field(default_factory=lambda: defaultdict(TurnStats))
    codex_skill_invocations: list = field(default_factory=list)
    codex_tasks: list = field(default_factory=list)
    direct_cost_total: float = 0.0
    model_counts: dict = field(default_factory=lambda: defaultdict(int))


def get_model_tier(model: Optional[str]) -> str:
    if not model:
        return "sonnet"
    model_lower = model.lower()
    if "haiku" in model_lower:
        return "haiku"
    return "sonnet"


def compute_cost(usage: dict, model_tier: str) -> float:
    pricing = PRICING[model_tier]
    cost = 0.0
    cost += usage.get("input_tokens", 0) * pricing["input"] / 1_000_000
    cost += usage.get("output_tokens", 0) * pricing["output"] / 1_000_000
    cost += usage.get("cache_read_input_tokens", 0) * pricing["cache_read"] / 1_000_000
    cost += usage.get("cache_creation_input_tokens", 0) * pricing["cache_creation"] / 1_000_000
    return cost


def add_usage_to_stats(stats: TurnStats, usage: dict, model_tier: str):
    stats.turns += 1
    stats.input_tok += usage.get("input_tokens", 0)
    stats.output_tok += usage.get("output_tokens", 0)
    stats.cache_read += usage.get("cache_read_input_tokens", 0)
    stats.cache_creation += usage.get("cache_creation_input_tokens", 0)
    stats.cost_usd += compute_cost(usage, model_tier)


def classify_turn(tool_names: list[str]) -> list[str]:
    """Return list of invocation type labels for a turn (can be multiple)."""
    types = []
    if "mcp__codex__codex" in tool_names:
        types.append("codex_call")
    if "mcp__codex__codex-reply" in tool_names:
        types.append("codex_reply")
    if "Skill" in tool_names:
        types.append("skill_invocation")
    if "Agent" in tool_names:
        types.append("agent_subagent")
    if "TaskCreate" in tool_names:
        types.append("task_create_bg")
    if not types:
        types.append("main_agent")
    return types


def analyze_session(session_id: str, filename: str, label: str) -> SessionStats:
    path = BASE_DIR / filename
    stats = SessionStats(session_id=session_id, label=label)

    line_count = 0
    parse_errors = 0

    # Track skill invocations to detect codex-dispatch pattern
    pending_skill_calls = []  # skill tool calls we've seen
    in_codex_dispatch = False
    codex_dispatch_count = 0
    current_skill_name = None

    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            line_count += 1

            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                parse_errors += 1
                continue

            # Collect direct costUSD fields
            if "costUSD" in obj:
                stats.direct_cost_total += float(obj["costUSD"])

            msg_type = obj.get("type", "")

            # Look at assistant messages for usage and tool calls
            if msg_type == "assistant":
                message = obj.get("message", obj)
                usage = message.get("usage", {})
                model = message.get("model", obj.get("model", ""))
                model_tier = get_model_tier(model)

                if model:
                    stats.model_counts[model] += 1

                # Extract tool calls from content
                content = message.get("content", [])
                tool_names = []
                tool_inputs = {}

                if isinstance(content, list):
                    for block in content:
                        if isinstance(block, dict) and block.get("type") == "tool_use":
                            tool_name = block.get("name", "")
                            tool_names.append(tool_name)
                            tool_inputs[tool_name] = block.get("input", {})

                # Detect Skill tool calls for codex-dispatch
                if "Skill" in tool_inputs:
                    skill_input = tool_inputs["Skill"]
                    skill_name = skill_input.get("skill", "") if isinstance(skill_input, dict) else ""
                    current_skill_name = skill_name
                    if "codex" in skill_name.lower() or "dispatch" in skill_name.lower():
                        in_codex_dispatch = True
                        stats.codex_skill_invocations.append({
                            "skill": skill_name,
                            "args": skill_input.get("args", "") if isinstance(skill_input, dict) else "",
                        })

                # Detect codex calls to extract task descriptions
                if "mcp__codex__codex" in tool_inputs:
                    codex_input = tool_inputs["mcp__codex__codex"]
                    if isinstance(codex_input, dict):
                        task_desc = codex_input.get("prompt", codex_input.get("task", str(codex_input)[:200]))
                        stats.codex_tasks.append({
                            "task": task_desc[:300],
                            "from_dispatch": in_codex_dispatch,
                        })

                # Only count usage if present
                if usage and (usage.get("input_tokens", 0) or usage.get("output_tokens", 0)):
                    types = classify_turn(tool_names)

                    # Add to total
                    add_usage_to_stats(stats.total, usage, model_tier)

                    # Add to each type bucket
                    for t in types:
                        # For haiku model, override type label
                        if model_tier == "haiku" and t == "main_agent":
                            t = "haiku_subagent"
                        elif model_tier == "haiku":
                            t = f"haiku_{t}"
                        add_usage_to_stats(stats.by_type[t], usage, model_tier)

    stats._line_count = line_count
    stats._parse_errors = parse_errors
    return stats


def fmt_tok(n: int) -> str:
    if n >= 1_000_000:
        return f"{n/1_000_000:.2f}M"
    elif n >= 1_000:
        return f"{n/1_000:.1f}K"
    return str(n)


def fmt_cost(c: float) -> str:
    return f"${c:.4f}"


def print_report(all_stats: list[SessionStats]):
    print("SESSION ANALYSIS")
    print("=" * 80)
    print()

    print("Sessions analyzed:")
    for s in all_stats:
        lines = getattr(s, "_line_count", 0)
        errs = getattr(s, "_parse_errors", 0)
        print(f"  {s.session_id[:8]} ({s.label}): {lines:,} lines, {errs} parse errors")
    print()

    # Per-session totals
    print("PER-SESSION TOTALS:")
    print(f"  {'Session':<12} {'Turns':>6} {'Input':>10} {'Output':>10} {'CacheRd':>10} {'CacheCr':>10} {'Est Cost':>10} {'Direct$':>10}")
    print("  " + "-" * 90)
    grand = TurnStats()
    for s in all_stats:
        t = s.total
        grand.turns += t.turns
        grand.input_tok += t.input_tok
        grand.output_tok += t.output_tok
        grand.cache_read += t.cache_read
        grand.cache_creation += t.cache_creation
        grand.cost_usd += t.cost_usd
        print(f"  {s.session_id[:8]:<12} {t.turns:>6} {fmt_tok(t.input_tok):>10} {fmt_tok(t.output_tok):>10} {fmt_tok(t.cache_read):>10} {fmt_tok(t.cache_creation):>10} {fmt_cost(t.cost_usd):>10} {fmt_cost(s.direct_cost_total):>10}")
    print("  " + "-" * 90)
    print(f"  {'TOTAL':<12} {grand.turns:>6} {fmt_tok(grand.input_tok):>10} {fmt_tok(grand.output_tok):>10} {fmt_tok(grand.cache_read):>10} {fmt_tok(grand.cache_creation):>10} {fmt_cost(grand.cost_usd):>10}")
    print()

    # Model breakdown per session
    print("MODEL USAGE PER SESSION:")
    for s in all_stats:
        if s.model_counts:
            print(f"  {s.session_id[:8]}:")
            for model, count in sorted(s.model_counts.items(), key=lambda x: -x[1]):
                print(f"    {model}: {count} turns")
    print()

    # Aggregate by type across all sessions
    print("BY INVOCATION TYPE (across all sessions):")
    type_totals: dict[str, TurnStats] = defaultdict(TurnStats)
    for s in all_stats:
        for t, ts in s.by_type.items():
            agg = type_totals[t]
            agg.turns += ts.turns
            agg.input_tok += ts.input_tok
            agg.output_tok += ts.output_tok
            agg.cache_read += ts.cache_read
            agg.cache_creation += ts.cache_creation
            agg.cost_usd += ts.cost_usd

    blocking_map = {
        "main_agent": "yes",
        "codex_call": "yes (waits for Codex)",
        "codex_reply": "yes (polling/result)",
        "skill_invocation": "yes",
        "agent_subagent": "yes (by default)",
        "task_create_bg": "no (background)",
        "haiku_subagent": "yes",
        "haiku_skill_invocation": "yes",
        "haiku_codex_call": "yes",
        "haiku_agent_subagent": "yes",
    }

    print(f"  {'Type':<28} {'Turns':>6} {'Input':>10} {'Output':>10} {'Est Cost':>10} {'Blocking?'}")
    print("  " + "-" * 80)
    for t, ts in sorted(type_totals.items(), key=lambda x: -x[1].cost_usd):
        blocking = blocking_map.get(t, "unknown")
        print(f"  {t:<28} {ts.turns:>6} {fmt_tok(ts.input_tok):>10} {fmt_tok(ts.output_tok):>10} {fmt_cost(ts.cost_usd):>10}  {blocking}")
    print()

    # Codex skill usage
    print("CODEX SKILL USAGE:")
    total_skill_invocations = sum(len(s.codex_skill_invocations) for s in all_stats)
    total_codex_calls = sum(len(s.codex_tasks) for s in all_stats)
    print(f"  Total Skill tool calls (codex-related): {total_skill_invocations}")
    print(f"  Total mcp__codex__codex tool calls: {total_codex_calls}")
    print()

    for s in all_stats:
        if s.codex_skill_invocations:
            print(f"  Session {s.session_id[:8]} skill invocations:")
            for inv in s.codex_skill_invocations:
                args_preview = (inv['args'] or '')[:120].replace('\n', ' ')
                print(f"    skill={inv['skill']} | args: {args_preview}")
        if s.codex_tasks:
            print(f"  Session {s.session_id[:8]} Codex tasks ({len(s.codex_tasks)} total):")
            for i, task in enumerate(s.codex_tasks[:10], 1):
                task_preview = (task['task'] or '')[:150].replace('\n', ' ')
                dispatch_flag = "[via dispatch]" if task['from_dispatch'] else ""
                print(f"    {i}. {dispatch_flag} {task_preview}")
            if len(s.codex_tasks) > 10:
                print(f"    ... and {len(s.codex_tasks)-10} more")
    print()

    print("COST ESTIMATION NOTES:")
    print("  Sonnet 4.6: $3/MTok input, $15/MTok output, $0.30/MTok cache_read, $3.75/MTok cache_creation")
    print("  Haiku 4.5:  $0.80/MTok input, $4/MTok output, $0.08/MTok cache_read, $1/MTok cache_creation")
    print()
    print("BLOCKING vs BACKGROUND NOTES:")
    print("  mcp__codex__codex calls: BLOCKING — main agent waits for Codex to finish before continuing")
    print("  mcp__codex__codex-reply: BLOCKING — used to poll/fetch Codex result")
    print("  Agent tool calls: BLOCKING by default unless run_in_background=true")
    print("  TaskCreate: BACKGROUND — runs as background process, main agent does not wait")
    print("  Skill tool calls: BLOCKING — skill loads and runs synchronously in main context")
    print()
    print("IMPORTANT CAVEAT:")
    print("  Token usage in these JSONL files reflects the MAIN AGENT's turns only.")
    print("  Subagent (Agent tool) token usage is NOT captured in the parent session JSONL.")
    print("  Codex (mcp__codex__codex) token usage is also NOT captured here — only the")
    print("  orchestrating Sonnet turn that called Codex is counted.")
    print("  The actual total cost is therefore HIGHER than the estimated totals above.")


def main():
    all_stats = []
    for session_id, (filename, label) in SESSION_FILES.items():
        path = BASE_DIR / filename
        if not path.exists():
            print(f"WARNING: {path} not found, skipping", file=sys.stderr)
            continue
        print(f"Analyzing {session_id[:8]} ({label})...", file=sys.stderr)
        s = analyze_session(session_id, filename, label)
        all_stats.append(s)
        print(f"  Done: {s._line_count:,} lines, {s.total.turns} assistant turns", file=sys.stderr)

    print_report(all_stats)


if __name__ == "__main__":
    main()
