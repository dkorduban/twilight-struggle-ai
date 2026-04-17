"""Lightweight event log for surfacing game events (dice rolls, card effects) to the CLI.

Usage in engine code:
    from tsrl.engine.event_log import log_event
    log_event("Roll: 4 + 2 ops - 2×3 stability = 0 → coup fails")

Usage in CLI:
    from tsrl.engine.event_log import drain_events
    for msg in drain_events():
        print(f"  {msg}")
"""
from __future__ import annotations

_log: list[str] = []


def log_event(msg: str) -> None:
    """Append a human-readable event message."""
    _log.append(msg)


def drain_events() -> list[str]:
    """Return and clear all logged events."""
    events = list(_log)
    _log.clear()
    return events
