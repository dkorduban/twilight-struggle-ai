#!/usr/bin/env python3
import json, re, sys

try:
    payload = json.load(sys.stdin)
except Exception:
    sys.exit(0)

command = ((payload.get("tool_input") or {}).get("command") or "").strip()
lower = command.lower()

patterns = [
    r"(^|\s)sudo\s",
    r"rm\s+-rf\s+/($|\s)",
    r"rm\s+-rf\s+~($|\s)",
    r"\bshutdown\b",
    r"\breboot\b",
    r":\(\)\{:\|:&\};:",
]
exfil_tool = r"\b(curl|wget|scp|sftp|nc|ncat|netcat|rsync|ssh)\b"
secretish = r"(\.env(\.|$)|secrets?/|credentials?|id_rsa|id_ed25519|\.aws/|\.ssh/|gcloud|anthropic)"

reason = None
for pat in patterns:
    if re.search(pat, lower):
        reason = f"Blocked dangerous shell command: {command}"
        break
if reason is None and re.search(exfil_tool, lower) and re.search(secretish, lower):
    reason = f"Blocked possible secret exfiltration command: {command}"

if reason:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason
        }
    }))
