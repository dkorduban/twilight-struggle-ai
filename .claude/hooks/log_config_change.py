#!/usr/bin/env python3
import json, sys
from pathlib import Path

try:
    payload = json.load(sys.stdin)
except Exception:
    sys.exit(0)

source = payload.get("source", "unknown")
file_path = payload.get("file_path", "")
print(json.dumps({
    "systemMessage": f"Claude Code config changed ({source}): {file_path}. Re-check permissions, hooks, and local overrides before continuing."
}))
