#!/usr/bin/env python3
"""Parse Claude Code session JSONL files and produce a chronological summary."""

import json
import sys
from datetime import datetime
from pathlib import Path


def extract_text(content):
    """Extract text from message content (string or list of blocks)."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, dict):
                if block.get("type") == "text":
                    parts.append(block.get("text", ""))
                elif block.get("type") == "tool_use":
                    parts.append(f"[TOOL:{block.get('name','')}]")
        return " ".join(parts)
    return str(content)


def extract_tool_uses(content):
    """Extract list of (tool_name, input_summary) from content blocks."""
    tools = []
    if not isinstance(content, list):
        return tools
    for block in content:
        if isinstance(block, dict) and block.get("type") == "tool_use":
            name = block.get("name", "")
            inp = block.get("input", {})
            summary = ""
            if name == "mcp__codex__codex":
                prompt = inp.get("prompt", "") or inp.get("instructions", "")
                summary = str(prompt)[:80]
            elif name == "Bash":
                cmd = inp.get("command", "")
                summary = str(cmd)[:80]
            elif name == "Agent":
                prompt = inp.get("prompt", "") or inp.get("instructions", "")
                summary = str(prompt)[:80]
            elif name in ("TaskCreate", "TodoWrite"):
                summary = str(inp)[:80]
            else:
                summary = str(inp)[:60]
            tools.append((name, summary))
    return tools


def is_milestone(text):
    """Check if text contains milestone keywords."""
    text_lower = text.lower()
    keywords = ["passing", "complete", "done", "committed", "fixed", "all tests",
                "✓", "success", "✅", "merged", "implemented", "added", "created"]
    return any(kw in text_lower for kw in keywords)


def fmt_time(ts_str):
    """Format ISO timestamp to HH:MM."""
    try:
        dt = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
        return dt.strftime("%H:%M")
    except Exception:
        return "??:??"


def parse_session(filepath, max_entries=200, label=""):
    """Parse a session JSONL file and return timeline entries."""
    filepath = Path(filepath)
    entries = []
    line_count = 0
    error_count = 0

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            line_count += 1
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                error_count += 1
                continue

            ts = obj.get("timestamp", "")
            msg = obj.get("message", {})
            if not msg:
                # Some records have role/content at top level
                role = obj.get("role")
                content = obj.get("content")
                if role and content:
                    msg = {"role": role, "content": content}

            if not msg:
                continue

            role = msg.get("role", "")
            content = msg.get("content", "")

            if role == "user":
                text = extract_text(content)
                # Skip empty or system-only messages
                text_stripped = text.strip()
                if not text_stripped or len(text_stripped) < 5:
                    continue
                # Skip tool results (they're often huge)
                if isinstance(content, list):
                    non_tool = [b for b in content if isinstance(b, dict) and b.get("type") != "tool_result"]
                    if not non_tool:
                        continue
                    text = extract_text(non_tool)
                entries.append({
                    "ts": ts,
                    "role": "USER",
                    "summary": text[:200].replace("\n", " "),
                    "tools": [],
                    "is_milestone": False,
                })

            elif role == "assistant":
                text = extract_text(content)
                tools = extract_tool_uses(content) if isinstance(content, list) else []

                # Only keep entries with user-facing text or interesting tools
                has_codex = any(t[0] == "mcp__codex__codex" for t in tools)
                has_agent = any(t[0] == "Agent" for t in tools)
                has_task = any(t[0] in ("TaskCreate", "TodoWrite") for t in tools)
                has_bash = any(t[0] == "Bash" for t in tools)
                milestone = is_milestone(text[:500])

                # Add text summary entry
                text_clean = text.strip()[:150].replace("\n", " ")
                if text_clean and len(text_clean) > 10:
                    entries.append({
                        "ts": ts,
                        "role": "ASST",
                        "summary": text_clean,
                        "tools": [],
                        "is_milestone": milestone,
                    })

                # Add tool entries (Codex and Agent are most interesting)
                for tname, tsummary in tools:
                    if tname == "mcp__codex__codex":
                        entries.append({
                            "ts": ts,
                            "role": "CODEX",
                            "summary": tsummary,
                            "tools": [],
                            "is_milestone": False,
                        })
                    elif tname == "Agent":
                        entries.append({
                            "ts": ts,
                            "role": "AGENT",
                            "summary": tsummary,
                            "tools": [],
                            "is_milestone": False,
                        })
                    elif tname in ("TaskCreate", "TodoWrite"):
                        entries.append({
                            "ts": ts,
                            "role": "TASK",
                            "summary": tsummary,
                            "tools": [],
                            "is_milestone": False,
                        })
                    elif tname == "Bash" and (milestone or has_codex):
                        # Only log Bash if it's in a milestone context
                        entries.append({
                            "ts": ts,
                            "role": "BASH",
                            "summary": tsummary,
                            "tools": [],
                            "is_milestone": False,
                        })

    return entries, line_count, error_count


def deduplicate_and_limit(entries, max_entries=200):
    """Remove consecutive duplicates and limit to max_entries, prioritizing key events."""
    # First pass: deduplicate consecutive same-role+summary
    deduped = []
    prev = None
    for e in entries:
        key = (e["role"], e["summary"][:50])
        if key != prev:
            deduped.append(e)
            prev = key

    if len(deduped) <= max_entries:
        return deduped

    # Need to trim: keep all USER, CODEX, AGENT, TASK, milestone ASST
    priority = []
    normal = []
    for e in deduped:
        if e["role"] in ("USER", "CODEX", "AGENT", "TASK") or e["is_milestone"]:
            priority.append(e)
        else:
            normal.append(e)

    if len(priority) >= max_entries:
        return priority[:max_entries]

    # Fill remaining slots with normal entries evenly spaced
    remaining = max_entries - len(priority)
    step = max(1, len(normal) // remaining)
    selected_normal = normal[::step][:remaining]

    combined = sorted(priority + selected_normal, key=lambda e: e["ts"])
    return combined[:max_entries]


def get_duration(entries):
    """Get start and end time strings."""
    ts_list = [e["ts"] for e in entries if e["ts"]]
    if not ts_list:
        return "??:??", "??:??"
    ts_list.sort()
    return fmt_time(ts_list[0]), fmt_time(ts_list[-1])


def print_session(entries, session_id, date_label, line_count, error_count):
    start, end = get_duration(entries)
    print(f"\nSESSION: {session_id} ({date_label})")
    print(f"Duration: {start} to {end}  [{line_count} lines, {error_count} parse errors]")
    print()

    for e in entries:
        time_str = fmt_time(e["ts"])
        role = e["role"]
        summary = e["summary"]
        milestone_marker = " *** MILESTONE ***" if e["is_milestone"] else ""
        print(f"  {time_str}  {role}: {summary}{milestone_marker}")


def extract_open_tasks(entries):
    """Extract potential open tasks from assistant messages."""
    open_tasks = []
    task_keywords = ["todo", "still need", "next step", "pending", "not yet",
                     "future work", "month 2", "will need", "should add",
                     "missing", "open question", "remaining"]
    for e in entries:
        if e["role"] in ("ASST",):
            text = e["summary"].lower()
            for kw in task_keywords:
                if kw in text:
                    open_tasks.append(e["summary"])
                    break
    return open_tasks


def main():
    session_small = "/home/dkord/.claude/projects/-home-dkord-code-twilight-struggle-ai/409c1153-0697-4629-9146-a65326e6695e.jsonl"
    session_large = "/home/dkord/.claude/projects/-home-dkord-code-twilight-struggle-ai/aba177c5-eef2-41a2-af47-b8449cc53b84.jsonl"

    print("Parsing sessions...")
    print("=" * 70)

    # Parse small session first
    print(f"\nParsing {Path(session_small).name}...")
    entries_small, lc_small, ec_small = parse_session(session_small)
    entries_small = deduplicate_and_limit(entries_small, max_entries=100)
    print_session(entries_small, "409c1153", "Mar 27", lc_small, ec_small)

    # Parse large session
    print(f"\nParsing {Path(session_large).name}...")
    entries_large, lc_large, ec_large = parse_session(session_large)
    entries_large = deduplicate_and_limit(entries_large, max_entries=200)
    print_session(entries_large, "aba177c5", "Mar 26-28", lc_large, ec_large)

    # Open tasks
    print("\n" + "=" * 70)
    print("OPEN TASKS (from assistant messages mentioning pending work):")
    all_entries = entries_small + entries_large
    open_tasks = extract_open_tasks(all_entries)
    seen = set()
    for task in open_tasks:
        key = task[:60]
        if key not in seen:
            seen.add(key)
            print(f"- {task}")

    print("\nDone.")


if __name__ == "__main__":
    main()
