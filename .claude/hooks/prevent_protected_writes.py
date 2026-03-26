#!/usr/bin/env python3
import json, sys
from pathlib import Path

PROTECTED_FRAGMENTS = [
    "/build/", "/dist/", "/out/", "/artifacts/", "/checkpoints/", "/wandb/",
    "/.venv/", "/venv/", "/node_modules/", "/.pytest_cache/", "/.mypy_cache/", "/.ruff_cache/"
]
PROTECTED_NAMES = {".env", ".env.local", ".env.development", ".env.production"}
PROTECTED_SUFFIXES = {".pem", ".key"}

try:
    payload = json.load(sys.stdin)
except Exception:
    sys.exit(0)

inp = payload.get("tool_input") or {}
path = inp.get("file_path") or ""
normalized = path.replace("\\", "/")
p = Path(path)

protected = (
    any(frag in normalized for frag in PROTECTED_FRAGMENTS)
    or p.name in PROTECTED_NAMES
    or p.suffix.lower() in PROTECTED_SUFFIXES
)

if protected:
    reason = f"Protected path write blocked by project policy: {path}"
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason
        }
    }))
