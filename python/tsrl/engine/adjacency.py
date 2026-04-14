"""
Country adjacency graph for Twilight Struggle.

Loads data/spec/adjacency.csv and provides:
  - Neighbor lookup by country_id
  - Reachability: which countries a player can place influence in / coup / realign

Reachability rules (ITS competitive rules):
  - A player can place influence in a country if:
      (a) it is adjacent to a country where that player already has ≥ 1 influence, OR
      (b) it is adjacent to the player's superpower anchor (USA id=81 / USSR id=82).
  - Coup and realign have the same accessibility requirement.
  - The superpower anchors themselves (id=81, id=82) are NOT valid board targets.
"""
from __future__ import annotations

from ._deprecation import warn_engine_deprecated

warn_engine_deprecated(__name__)

import csv
from functools import lru_cache
from pathlib import Path

from tsrl.schemas import PublicState, Side

# IDs of the superpower anchor nodes (never coup/influence targets).
_USA_ID: int = 81
_USSR_ID: int = 82
_SUPERPOWER_IDS: frozenset[int] = frozenset({_USA_ID, _USSR_ID})

# Default path to adjacency CSV (relative to repo root).
_DEFAULT_CSV = Path(__file__).parents[3] / "data" / "spec" / "adjacency.csv"


def load_adjacency(path: str | Path = _DEFAULT_CSV) -> dict[int, frozenset[int]]:
    """Return adjacency dict: country_id → frozenset of neighbor IDs.

    Reads from data/spec/adjacency.csv.  Comment lines (starting with '#')
    and inline comments (after '#') are ignored.
    """
    neighbors: dict[int, set[int]] = {}
    with open(path, newline="") as f:
        reader = csv.reader(f)
        for raw in reader:
            # Strip inline comments and blank lines.
            row = [cell.split("#")[0].strip() for cell in raw]
            if not row or row[0] == "" or row[0].startswith("#"):
                continue
            if row[0] == "country_a":
                continue  # header
            a, b = int(row[0]), int(row[1])
            neighbors.setdefault(a, set()).add(b)
            neighbors.setdefault(b, set()).add(a)
    return {k: frozenset(v) for k, v in neighbors.items()}


@lru_cache(maxsize=1)
def _default_adjacency() -> dict[int, frozenset[int]]:
    return load_adjacency()


def neighbors(country_id: int, adj: dict[int, frozenset[int]] | None = None) -> frozenset[int]:
    """Return the set of countries adjacent to country_id."""
    g = adj if adj is not None else _default_adjacency()
    return g.get(country_id, frozenset())


def accessible_countries(
    side: Side,
    pub: PublicState,
    adj: dict[int, frozenset[int]] | None = None,
) -> frozenset[int]:
    """Return the set of countries a side can reach for influence placement.

    Reachability rules (TS ITS competitive rules, matching C++ engine):
      1. Own-influence 1-hop: any country where the side has ≥ 1 influence, plus
         every country directly adjacent to such a country (1-hop only — no
         transitive chaining through newly placed influence).
      2. Own superpower anchor (1-hop only): each side gets the direct neighbors
         of their OWN anchor (USSR → {Finland, Poland, Romania, Afghanistan, N.Korea};
         US → {Canada, Cuba, Mexico, Japan, Philippines, S.Korea}).
         The opponent's anchor neighbors are NOT included.

    Superpower anchors themselves (id=81, id=82) are excluded from the result.
    Note: for Coup and Realign accessibility use legal_actions.accessible_countries
    which returns all non-DEFCON-restricted countries instead.
    """
    g = adj if adj is not None else _default_adjacency()

    own_anchor = _USSR_ID if side == Side.USSR else _USA_ID

    visited: set[int] = set()

    # Rule 1: countries with own influence + their direct neighbors (1-hop).
    for (s, cid), inf in pub.influence.items():
        if s == side and inf > 0:
            visited.add(cid)
            for nbr in g.get(cid, frozenset()):
                if nbr not in _SUPERPOWER_IDS:
                    visited.add(nbr)

    # Rule 2: own anchor's direct neighbors only (not opponent's anchor).
    for nbr in g.get(own_anchor, frozenset()):
        if nbr not in _SUPERPOWER_IDS:
            visited.add(nbr)

    return frozenset(visited)
