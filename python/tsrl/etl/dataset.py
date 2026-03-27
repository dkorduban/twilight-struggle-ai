"""
Parquet dataset builder for Twilight Struggle replay logs.

Pipeline per game:
  parse_replay → resolve_names → reduce_game + smooth_game → emit rows

One row = one decision point (PLAY / HEADLINE / SPACE_RACE event) in a game.

Offline label fields (prefixed ``lbl_``) must NEVER be used in online inference,
self-play, or evaluation.  They are targets for supervised training only.

Usage::

    from tsrl.etl.dataset import build_dataset
    build_dataset(
        log_dir="data/raw_logs",
        out_dir="data/parquet",
    )
"""
from __future__ import annotations

import hashlib
import logging
import warnings
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

import polars as pl

from tsrl.etl.game_data import load_cards, load_countries
from tsrl.etl.parser import ParseResult, parse_replay
from tsrl.etl.reducer import reduce_game
from tsrl.etl.resolver import resolve_names
from tsrl.etl.smoother import OfflineLabels, smooth_game
from tsrl.schemas import (
    EventKind,
    HandKnowledge,
    OfflineLabels,
    PublicState,
    ReplayEvent,
    Side,
)

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Dimension constants
# ---------------------------------------------------------------------------

# Cards are IDs 1..MAX_CARD_ID.  Index 0 is unused (sentinel).
MAX_CARD_ID: int = 111
# Countries are IDs 0..MAX_COUNTRY_ID.
MAX_COUNTRY_ID: int = 83

_CARD_MASK_LEN: int = MAX_CARD_ID + 1        # length 112; index 0 unused
_COUNTRY_MASK_LEN: int = MAX_COUNTRY_ID + 1  # length 84

# Decision point EventKinds that produce training rows.
# SPACE_RACE is a result event (card advancement), not a decision —
# the PLAY event for the same AR already captures the decision.
_DECISION_KINDS: frozenset[EventKind] = frozenset({
    EventKind.PLAY,
    EventKind.HEADLINE,
})


# ---------------------------------------------------------------------------
# Feature helpers
# ---------------------------------------------------------------------------


def _card_mask(card_ids: frozenset[int]) -> list[int]:
    """Binary mask of length _CARD_MASK_LEN; 1 at each present card ID."""
    mask = [0] * _CARD_MASK_LEN
    for cid in card_ids:
        if 0 < cid < _CARD_MASK_LEN:
            mask[cid] = 1
    return mask


def _influence_array(pub: PublicState, side: Side) -> list[int]:
    """Influence values for one side, indexed by country_id (len=_COUNTRY_MASK_LEN)."""
    arr = [0] * _COUNTRY_MASK_LEN
    for (s, cid), val in pub.influence.items():
        if s == side and 0 <= cid < _COUNTRY_MASK_LEN:
            arr[cid] = val
    return arr


def _game_id(path: Path) -> str:
    """Stable game identifier: SHA-1 of file content (first 12 hex chars)."""
    digest = hashlib.sha1(path.read_bytes()).hexdigest()
    return digest[:12]


# ---------------------------------------------------------------------------
# Row building
# ---------------------------------------------------------------------------


@dataclass
class _Row:
    """One training row (one decision point)."""
    # Identity
    game_id: str
    step_idx: int
    # Decision context
    turn: int
    ar: int
    phasing: int          # Side int value (0=USSR, 1=US)
    action_kind: int      # EventKind int value
    card_id: int          # -1 if unknown
    country_id: int       # -1 if not applicable
    # Global state
    vp: int
    defcon: int
    milops_ussr: int
    milops_us: int
    space_ussr: int
    space_us: int
    china_held_by: int    # Side int value
    china_playable: bool
    # Influence (flat arrays; len = _COUNTRY_MASK_LEN)
    ussr_influence: list[int]
    us_influence: list[int]
    # Card set masks (len = _CARD_MASK_LEN)
    discard_mask: list[int]
    removed_mask: list[int]
    # Actor hand knowledge (causal, online-safe)
    actor_known_in: list[int]
    actor_known_not_in: list[int]
    actor_possible: list[int]
    actor_hand_size: int
    actor_holds_china: bool
    # Opponent hand knowledge (from actor's observer perspective)
    opp_known_in: list[int]
    opp_known_not_in: list[int]
    opp_possible: list[int]
    opp_hand_size: int
    opp_holds_china: bool
    # Offline labels — TRAINING TARGETS ONLY, never use in online inference
    lbl_actor_hand: list[int]
    lbl_step_quality: int
    lbl_card_quality: list[int]
    lbl_opponent_possible: list[int]


def _build_row(
    game_id: str,
    step_idx: int,
    event: ReplayEvent,
    pub: PublicState,
    ussr_hand: HandKnowledge,
    us_hand: HandKnowledge,
    label: OfflineLabels,
) -> _Row:
    """Assemble one training row from state + label at a decision point."""
    actor = event.phasing
    opp = Side.US if actor == Side.USSR else Side.USSR
    actor_hand = ussr_hand if actor == Side.USSR else us_hand
    opp_hand = us_hand if actor == Side.USSR else ussr_hand

    # Card quality array (per-card quality tag, default=UNKNOWN=3)
    cq = [3] * _CARD_MASK_LEN
    for cid, q in label.card_quality.items():
        if 0 < cid < _CARD_MASK_LEN:
            cq[cid] = int(q)

    return _Row(
        game_id=game_id,
        step_idx=step_idx,
        turn=event.turn,
        ar=event.ar,
        phasing=int(actor),
        action_kind=int(event.kind),
        card_id=event.card_id if event.card_id is not None else -1,
        country_id=event.country_id if event.country_id is not None else -1,
        vp=pub.vp,
        defcon=pub.defcon,
        milops_ussr=pub.milops[Side.USSR],
        milops_us=pub.milops[Side.US],
        space_ussr=pub.space[Side.USSR],
        space_us=pub.space[Side.US],
        china_held_by=int(pub.china_held_by),
        china_playable=pub.china_playable,
        ussr_influence=_influence_array(pub, Side.USSR),
        us_influence=_influence_array(pub, Side.US),
        discard_mask=_card_mask(pub.discard),
        removed_mask=_card_mask(pub.removed),
        actor_known_in=_card_mask(actor_hand.known_in_hand),
        actor_known_not_in=_card_mask(actor_hand.known_not_in_hand),
        actor_possible=_card_mask(actor_hand.possible_hidden),
        actor_hand_size=actor_hand.hand_size,
        actor_holds_china=actor_hand.holds_china,
        opp_known_in=_card_mask(opp_hand.known_in_hand),
        opp_known_not_in=_card_mask(opp_hand.known_not_in_hand),
        opp_possible=_card_mask(opp_hand.possible_hidden),
        opp_hand_size=opp_hand.hand_size,
        opp_holds_china=opp_hand.holds_china,
        lbl_actor_hand=_card_mask(label.actor_hand),
        lbl_step_quality=int(label.step_quality),
        lbl_card_quality=cq,
        lbl_opponent_possible=_card_mask(label.opponent_possible),
    )


# ---------------------------------------------------------------------------
# Per-game processing
# ---------------------------------------------------------------------------


def process_game(
    text: str,
    game_id: str,
    all_card_ids: frozenset[int],
) -> list[_Row]:
    """Parse, resolve, reduce, and smooth one game; return training rows.

    Returns an empty list if the game cannot be parsed or produces no decisions.
    Suppresses resolver warnings (unknown names are expected for unseen card variants).
    """
    result: ParseResult = parse_replay(text)
    if not result.events:
        log.warning("game %s: no events after parsing", game_id)
        return []

    cards = load_cards()
    countries = load_countries()

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        resolved = resolve_names(result.events, cards, countries, warn_unresolved=False)

    # Align events: only decision-point events get a label; others don't.
    # We need (event, pub, hand) at the same index.
    try:
        states = reduce_game(resolved, all_card_ids, check_invariants=False)
    except Exception as exc:
        log.warning("game %s: reduce_game failed: %s", game_id, exc)
        return []

    try:
        labels = smooth_game(resolved, all_card_ids)
    except Exception as exc:
        log.warning("game %s: smooth_game failed: %s", game_id, exc)
        return []

    # Build a mapping from (turn, ar, phasing) → OfflineLabels.
    # smooth_game returns one label per decision event, in replay order.
    decision_events = [
        (i, ev) for i, ev in enumerate(resolved) if ev.kind in _DECISION_KINDS
    ]
    if len(decision_events) != len(labels):
        log.warning(
            "game %s: decision count mismatch (%d events vs %d labels); skipping",
            game_id, len(decision_events), len(labels),
        )
        return []

    rows: list[_Row] = []
    for step_idx, (ev_idx, event) in enumerate(decision_events):
        pub, ussr_hand, us_hand = states[ev_idx]
        label = labels[step_idx]
        rows.append(
            _build_row(game_id, step_idx, event, pub, ussr_hand, us_hand, label)
        )

    return rows


# ---------------------------------------------------------------------------
# Dataset building
# ---------------------------------------------------------------------------


def _rows_to_dataframe(rows: list[_Row]) -> pl.DataFrame:
    """Convert a list of _Row objects to a Polars DataFrame."""
    if not rows:
        return pl.DataFrame()

    data: dict[str, list] = {f: [] for f in _Row.__dataclass_fields__}
    for row in rows:
        for f in _Row.__dataclass_fields__:
            data[f].append(getattr(row, f))
    return pl.DataFrame(data)


def build_dataset(
    log_dir: str | Path = "data/raw_logs",
    out_dir: str | Path = "data/parquet",
    *,
    val_fraction: float = 0.15,
    test_fraction: float = 0.15,
    seed: int = 42,
) -> dict[str, int]:
    """Process all replay logs and write train/val/test Parquet files.

    Split is by game (not by row) to avoid leakage.

    Args:
        log_dir: Directory containing ``*.txt`` replay log files.
        out_dir: Output directory for Parquet files.
        val_fraction: Fraction of games to reserve for validation.
        test_fraction: Fraction of games to reserve for test.
        seed: RNG seed for reproducible splits.

    Returns:
        Dict with counts: ``{"train": N, "val": N, "test": N, "total": N}``.
    """
    import random

    log_dir = Path(log_dir)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    cards = load_cards()
    # China Card (id=6) is NOT in the draw deck.
    all_card_ids = frozenset(cid for cid in cards if cid != 6)

    log_files = sorted(log_dir.glob("*.txt"))
    if not log_files:
        log.warning("No .txt files found in %s", log_dir)
        return {"train": 0, "val": 0, "test": 0, "total": 0}

    # Assign each file to a split deterministically.
    rng = random.Random(seed)
    shuffled = list(log_files)
    rng.shuffle(shuffled)

    n = len(shuffled)
    n_test = max(1, round(n * test_fraction)) if n >= 3 else 0
    n_val = max(1, round(n * val_fraction)) if n >= 3 else 0
    # Clamp so we always have at least 1 training game if possible.
    n_val = min(n_val, n - n_test - 1) if n > n_test + 1 else 0
    n_train = n - n_val - n_test

    split_map: dict[str, str] = {}
    for i, f in enumerate(shuffled):
        if i < n_train:
            split_map[f.name] = "train"
        elif i < n_train + n_val:
            split_map[f.name] = "val"
        else:
            split_map[f.name] = "test"

    split_rows: dict[str, list[_Row]] = {"train": [], "val": [], "test": []}

    for log_file in log_files:
        text = log_file.read_text()
        gid = _game_id(log_file)
        rows = process_game(text, gid, all_card_ids)
        split = split_map[log_file.name]
        split_rows[split].extend(rows)
        log.info("%-35s → %-5s  %d rows", log_file.name, split, len(rows))

    counts: dict[str, int] = {}
    for split, rows in split_rows.items():
        df = _rows_to_dataframe(rows)
        out_path = out_dir / f"{split}.parquet"
        if not df.is_empty():
            df.write_parquet(out_path)
        counts[split] = len(rows)

    counts["total"] = sum(counts.values())
    return counts
