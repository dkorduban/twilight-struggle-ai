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
    """Return the set of countries a side can reach for ops (influence/coup/realign).

    Reachability rules (matching the TSEspionage digital game):
      1. Superpower anchor adjacency (1-hop only): any country adjacent to EITHER
         superpower (USA id=81 or USSR id=82) is always accessible for both sides.
         This lets USSR place in Cuba (adj USA) and US place in Finland (adj USSR)
         from game start, without requiring existing influence.
      2. Own-influence BFS (full depth): any country reachable via a connected path
         through the adjacency graph starting from countries where the side has ≥ 1
         influence is accessible — regardless of whether intermediate countries have
         influence.  This matches the digital game's chaining model: the path to a
         country via existing influence is sufficient; you do NOT need to spend ops
         on intermediate countries first.

    Superpower anchors themselves (id=81, id=82) are excluded from the result.
    """
    from collections import deque
    g = adj if adj is not None else _default_adjacency()

    own_influence: set[int] = {
        cid for (s, cid), inf in pub.influence.items()
        if s == side and inf > 0
    }

    # Rule 1: 1-hop from superpower anchors (both anchors for both players).
    superpower_nbrs: set[int] = {
        nbr
        for sp in _SUPERPOWER_IDS
        for nbr in g.get(sp, frozenset())
        if nbr not in _SUPERPOWER_IDS
    }

    # Rule 2: full BFS from own-influence network.
    visited: set[int] = set(own_influence)
    q: deque[int] = deque(own_influence)
    while q:
        node = q.popleft()
        for nbr in g.get(node, frozenset()):
            if nbr not in _SUPERPOWER_IDS and nbr not in visited:
                visited.add(nbr)
                q.append(nbr)

    return frozenset(visited | superpower_nbrs)
