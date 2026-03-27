"""
Game data loader: cards, countries, adjacency.

Loads from data/spec/ CSV files.  Results are cached after first load.
All functions return plain dataclasses / dicts — no Polars dependency at this layer.
"""
from __future__ import annotations

import csv
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from tsrl.schemas import Era, Region, Side


# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

_REPO_ROOT = Path(__file__).parents[3]  # .../twilight-struggle-ai/
_SPEC_DIR = _REPO_ROOT / "data" / "spec"


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class CardSpec:
    card_id: int
    name: str
    side: Side
    ops: int       # 0 for scoring cards
    era: Era
    starred: bool  # event fires once then removed
    is_scoring: bool
    # True if this card cannot be held past end of its era (scoring cards)
    must_be_played_by_era_end: bool


@dataclass(frozen=True)
class CountrySpec:
    country_id: int
    name: str
    region: Region
    stability: int
    is_battleground: bool
    us_start: int    # starting US influence
    ussr_start: int  # starting USSR influence


# ---------------------------------------------------------------------------
# Loaders
# ---------------------------------------------------------------------------


def _parse_bool(s: str) -> bool:
    return s.strip().lower() in ("true", "1", "yes")


def _parse_side(s: str) -> Side:
    s = s.strip().upper()
    if s == "USSR":
        return Side.USSR
    if s == "US":
        return Side.US
    return Side.NEUTRAL


def _parse_era(s: str) -> Era:
    s = s.strip().lower()
    if s == "early":
        return Era.EARLY
    if s == "mid":
        return Era.MID
    return Era.LATE


def _parse_region(s: str) -> Region:
    mapping = {
        "europe": Region.EUROPE,
        "asia": Region.ASIA,
        "middleeast": Region.MIDDLE_EAST,
        "centralamerica": Region.CENTRAL_AMERICA,
        "southamerica": Region.SOUTH_AMERICA,
        "africa": Region.AFRICA,
        "southeastasia": Region.SOUTHEAST_ASIA,
    }
    return mapping.get(s.strip().lower().replace("_", "").replace("/", ""), Region.EUROPE)


@lru_cache(maxsize=1)
def load_cards(spec_dir: Path = _SPEC_DIR) -> dict[int, CardSpec]:
    """Load cards.csv → {card_id: CardSpec}.

    Skips comment lines (starting with #) and the header row.
    """
    path = spec_dir / "cards.csv"
    cards: dict[int, CardSpec] = {}
    with path.open(newline="") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            # Skip header
            if line.lower().startswith("card_id"):
                continue
            # Strip inline comments
            line = line.split("#")[0].strip()
            if not line:
                continue
            row = [c.strip() for c in line.split(",")]
            if len(row) < 7:
                continue  # malformed row
            try:
                card_id = int(row[0])
                name = row[1]
                side = _parse_side(row[2])
                ops = int(row[3])
                era = _parse_era(row[4])
                starred = _parse_bool(row[5])
                is_scoring = _parse_bool(row[6])
                must_play = _parse_bool(row[7]) if len(row) > 7 else is_scoring
            except (ValueError, IndexError):
                continue
            cards[card_id] = CardSpec(
                card_id=card_id,
                name=name,
                side=side,
                ops=ops,
                era=era,
                starred=starred,
                is_scoring=is_scoring,
                must_be_played_by_era_end=must_play,
            )
    return cards


@lru_cache(maxsize=1)
def load_countries(spec_dir: Path = _SPEC_DIR) -> dict[int, CountrySpec]:
    """Load countries.csv → {country_id: CountrySpec}."""
    path = spec_dir / "countries.csv"
    countries: dict[int, CountrySpec] = {}
    with path.open(newline="") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if line.lower().startswith("country_id"):
                continue
            line = line.split("#")[0].strip()
            if not line:
                continue
            row = [c.strip() for c in line.split(",")]
            if len(row) < 7:
                continue
            try:
                country_id = int(row[0])
                name = row[1]
                region = _parse_region(row[2])
                stability = int(row[3])
                is_bg = _parse_bool(row[4])
                us_start = int(row[5])
                ussr_start = int(row[6])
            except (ValueError, IndexError):
                continue
            countries[country_id] = CountrySpec(
                country_id=country_id,
                name=name,
                region=region,
                stability=stability,
                is_battleground=is_bg,
                us_start=us_start,
                ussr_start=ussr_start,
            )
    return countries


@lru_cache(maxsize=1)
def load_adjacency(spec_dir: Path = _SPEC_DIR) -> frozenset[tuple[int, int]]:
    """Load adjacency.csv → frozenset of (a, b) pairs with a < b."""
    path = spec_dir / "adjacency.csv"
    if not path.exists():
        return frozenset()
    edges: set[tuple[int, int]] = set()
    with path.open(newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row or row[0].startswith("#"):
                continue
            if row[0].strip().lower() == "country_id_a":
                continue
            try:
                # Strip inline comments from each cell before parsing.
                a = int(row[0].split("#")[0].strip())
                b = int(row[1].split("#")[0].strip())
                edges.add((min(a, b), max(a, b)))
            except (ValueError, IndexError):
                continue
    return frozenset(edges)


# ---------------------------------------------------------------------------
# Convenience helpers
# ---------------------------------------------------------------------------


def fixed_starting_influence(
    spec_dir: Path = _SPEC_DIR,
) -> dict[tuple[Side, int], int]:
    """Return the implicit fixed starting influence for every country.

    TSEspionage logs only record the BIDDING/optional setup placements —
    they never emit PLACE_INFLUENCE events for the standard fixed starting
    influence defined by the rulebook (e.g. US=5 in UK, USSR=4 in Poland).
    Callers that need the TRUE influence at the start of a game should
    add this dict as a baseline on top of whatever the event-based reducer
    has produced.

    Returns {(Side.USSR|Side.US, country_id): influence}.
    """
    countries = load_countries(spec_dir)
    result: dict[tuple[Side, int], int] = {}
    for cid, spec in countries.items():
        if spec.ussr_start > 0:
            result[(Side.USSR, cid)] = spec.ussr_start
        if spec.us_start > 0:
            result[(Side.US, cid)] = spec.us_start
    return result


def card_name_index(spec_dir: Path = _SPEC_DIR) -> dict[str, int]:
    """Return {canonical_name_lower: card_id} for fuzzy name matching."""
    return {spec.name.lower(): cid for cid, spec in load_cards(spec_dir).items()}


def country_name_index(spec_dir: Path = _SPEC_DIR) -> dict[str, int]:
    """Return {canonical_name_lower: country_id}."""
    return {spec.name.lower(): cid for cid, spec in load_countries(spec_dir).items()}


def initial_influence() -> dict[tuple[int, int], int]:
    """Return {(Side, country_id): influence} for the standard start position."""
    result: dict[tuple[int, int], int] = {}
    for cid, c in load_countries().items():
        if c.us_start:
            result[(Side.US, cid)] = c.us_start
        if c.ussr_start:
            result[(Side.USSR, cid)] = c.ussr_start
    return result
