"""
Name-to-ID resolver pass.

After parse_replay() produces events with card_name/country_name strings,
this module resolves those names to integer IDs using the canonical lookup
tables from data/spec/cards.csv and data/spec/countries.csv.

Design:
  - All lookups are case-insensitive after normalization.
  - Starred-event suffix (*) is stripped before matching: "Marshall Plan*" → "Marshall Plan".
  - Unresolved names are logged as warnings but do NOT raise exceptions — the event
    keeps card_id=None / country_id=None so downstream code handles gracefully.
  - The resolver is deterministic: same input → same output.

Usage::

    from tsrl.etl.parser import parse_replay
    from tsrl.etl.resolver import resolve_names
    from tsrl.etl.game_data import load_cards, load_countries

    result = parse_replay(text)
    cards = load_cards()
    countries = load_countries()
    resolved = resolve_names(result.events, cards, countries)
"""
from __future__ import annotations

import re
import warnings
from dataclasses import replace
from typing import Sequence

from tsrl.etl.game_data import CardSpec, CountrySpec
from tsrl.schemas import EventKind, ReplayEvent

# ---------------------------------------------------------------------------
# Name normalization
# ---------------------------------------------------------------------------

_STAR_RE = re.compile(r"\*$")
_QUOTE_RE = re.compile(r'^"(.*)"$')


def _norm_card(name: str) -> str:
    """Normalize a card name for lookup.

    - Strips trailing '*' (starred event marker).
    - Strips surrounding double-quotes (e.g. '"Lone Gunman"' → 'Lone Gunman').
    - Replaces hyphens with spaces (e.g. 'KAL-007' → 'KAL 007').
    - Lowercases and strips whitespace.
    """
    name = _STAR_RE.sub("", name).strip()
    if m := _QUOTE_RE.match(name):
        name = m.group(1)
    name = name.replace("-", " ")
    return name.strip().lower()


def _norm_country(name: str) -> str:
    """Normalize a country name for lookup (lowercase, strip)."""
    return name.strip().lower()


# ---------------------------------------------------------------------------
# Log-name aliases
# ---------------------------------------------------------------------------
# TSEspionage/ACTS logs sometimes use different names than the canonical CSV.
# Maps normalized-log-name → card_id (bypasses index lookup for known mismatches).
_CARD_ALIASES: dict[str, int] = {
    # Log uses "The China Card"; CSV has "China Card"
    "the china card": 6,
    # Log uses "Mideast Scoring"; CSV has "Middle East Scoring"
    "mideast scoring": 3,
    # Log uses "The Voice of America"; CSV has "Voice of America"
    "the voice of america": 75,
    # Log uses abbreviated quoted titles; CSV has full names
    'ask not what your country...': 78,   # "Ask Not What Your Country Can Do For You"
    'one small step...': 81,              # "One Small Step"
    # "We Will Bury You" — norm matches after quote-strip; alias for safety
    'we will bury you': 53,
}

# Maps normalized country name → country_id for log-name variants.
_COUNTRY_ALIASES: dict[str, int] = {
    # Board space is "Congo/Zaire"; logs use either component name
    "zaire": 60,
    "congo": 60,
    # Indonesia and Malaysia are separate countries in the TSEspionage mod (id=76 and id=84).
    # Aliases handle the case where the log uses individual names.
    "indonesia": 76,
    "malaysia": 84,
}


# ---------------------------------------------------------------------------
# Index builders
# ---------------------------------------------------------------------------


def _build_card_index(cards: dict[int, CardSpec]) -> dict[str, int]:
    """Map normalized card name → card_id (includes log-name aliases)."""
    idx: dict[str, int] = {}
    for cid, spec in cards.items():
        key = _norm_card(spec.name)
        idx[key] = cid
    # Overlay aliases; aliases win over any CSV name that happens to collide.
    idx.update(_CARD_ALIASES)
    return idx


def _build_country_index(countries: dict[int, CountrySpec]) -> dict[str, int]:
    """Map normalized country name → country_id (includes log-name aliases)."""
    idx: dict[str, int] = {}
    for cid, spec in countries.items():
        key = _norm_country(spec.name)
        idx[key] = cid
    idx.update(_COUNTRY_ALIASES)
    return idx


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def build_indexes(
    cards: dict[int, CardSpec],
    countries: dict[int, CountrySpec],
) -> tuple[dict[str, int], dict[str, int]]:
    """Return (card_name_index, country_name_index) for use with resolve_names."""
    return _build_card_index(cards), _build_country_index(countries)


def resolve_names(
    events: Sequence[ReplayEvent],
    cards: dict[int, CardSpec],
    countries: dict[int, CountrySpec],
    *,
    warn_unresolved: bool = True,
) -> list[ReplayEvent]:
    """Resolve card_name / country_name strings to integer IDs.

    Args:
        events: Events from parse_replay() (card_id / country_id may be None).
        cards: Card spec dict from game_data.load_cards().
        countries: Country spec dict from game_data.load_countries().
        warn_unresolved: If True, emit a UserWarning for each unresolved name.

    Returns:
        New list of ReplayEvents with card_id / country_id filled in where
        possible.  Events with no name strings are returned unchanged.
    """
    card_idx, country_idx = build_indexes(cards, countries)
    resolved: list[ReplayEvent] = []
    for ev in events:
        resolved.append(
            _resolve_event(ev, card_idx, country_idx, warn_unresolved=warn_unresolved)
        )
    return resolved


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _resolve_event(
    ev: ReplayEvent,
    card_idx: dict[str, int],
    country_idx: dict[str, int],
    *,
    warn_unresolved: bool,
) -> ReplayEvent:
    """Resolve names for a single event, returning a new frozen ReplayEvent."""
    updates: dict = {}

    # ── Card resolution ───────────────────────────────────────────────────────
    if ev.card_name is not None and ev.card_id is None:
        cid = _lookup_card(ev.card_name, card_idx)
        if cid is not None:
            updates["card_id"] = cid
        elif warn_unresolved:
            warnings.warn(
                f"Unresolved card name {ev.card_name!r} at line {ev.line_number} "
                f"(kind={ev.kind.name})",
                UserWarning,
                stacklevel=2,
            )

    # ── Country resolution ────────────────────────────────────────────────────
    if ev.country_name is not None and ev.country_id is None:
        cid = _lookup_country(ev.country_name, country_idx)
        if cid is not None:
            updates["country_id"] = cid
        elif warn_unresolved:
            warnings.warn(
                f"Unresolved country name {ev.country_name!r} at line {ev.line_number} "
                f"(kind={ev.kind.name})",
                UserWarning,
                stacklevel=2,
            )

    if updates:
        return replace(ev, **updates)
    return ev


def _lookup_card(name: str, idx: dict[str, int]) -> int | None:
    """Look up a card by name (case-insensitive, star-stripped)."""
    return idx.get(_norm_card(name))


def _lookup_country(name: str, idx: dict[str, int]) -> int | None:
    """Look up a country by name (case-insensitive)."""
    return idx.get(_norm_country(name))
