"""JSON-backed match cache keyed by model file content hashes."""

from __future__ import annotations

import hashlib
import json
import logging
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


def file_sha256(path: str | Path, chunk_size: int = 1 << 20) -> str:
    """SHA256 of file contents, truncated to 64 bits for stable cache identity."""
    file_path = Path(path)
    hasher = hashlib.sha256()
    with file_path.open("rb") as handle:
        while chunk := handle.read(chunk_size):
            hasher.update(chunk)
    digest = hasher.hexdigest()[:16]
    logger.debug("match cache key: %s (%s)", digest[:8], file_path.name)
    return digest


def _canonical_hash_pair(
    model_a_path: str | Path,
    model_b_path: str | Path,
) -> tuple[str, str, bool]:
    hash_a = file_sha256(model_a_path)
    hash_b = file_sha256(model_b_path)
    swapped = hash_a > hash_b
    if swapped:
        return hash_b, hash_a, True
    return hash_a, hash_b, False


def _hash_cache_key(hash_a: str, hash_b: str, *, n_games: int, seed: int) -> str:
    return f"{hash_a}:{hash_b}:g{n_games}:s{seed}"


def match_cache_key(
    model_a_path: str | Path,
    model_b_path: str | Path,
    *,
    n_games: int,
    seed: int,
) -> str:
    """Return the canonical hash-based cache key for a matchup."""
    hash_a, hash_b, _ = _canonical_hash_pair(model_a_path, model_b_path)
    key = _hash_cache_key(hash_a, hash_b, n_games=n_games, seed=seed)
    logger.debug("match cache lookup key: %s", key)
    return key


def load_match_cache(path: str | Path) -> dict[str, dict[str, Any]]:
    """Load the JSON cache file, returning an empty cache on missing/invalid files."""
    cache_path = Path(path)
    if not cache_path.exists():
        return {}

    try:
        raw = json.loads(cache_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        logger.warning("ignoring unreadable match cache %s: %s", cache_path, exc)
        return {}

    if not isinstance(raw, dict):
        logger.warning("ignoring non-dict match cache %s", cache_path)
        return {}

    cache: dict[str, dict[str, Any]] = {}
    for key, value in raw.items():
        if isinstance(key, str) and isinstance(value, dict):
            cache[key] = value
    return cache


def save_match_cache(cache: dict[str, dict[str, Any]], path: str | Path) -> None:
    """Persist the match cache as stable, human-readable JSON."""
    cache_path = Path(path)
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(cache, indent=2, sort_keys=True) + "\n")


def _entry_matches_request(entry: dict[str, Any], *, n_games: int, seed: int) -> bool:
    entry_games = entry.get("games", entry.get("n_games"))
    if entry_games is not None and int(entry_games) != n_games:
        return False

    entry_seed = entry.get("seed")
    if entry_seed is not None and int(entry_seed) != seed:
        return False

    return True


def _swap_entry(entry: dict[str, Any]) -> dict[str, Any]:
    swapped = dict(entry)
    if "wins_a" in swapped and "wins_b" in swapped:
        swapped["wins_a"], swapped["wins_b"] = swapped["wins_b"], swapped["wins_a"]
    if "model_a_name" in swapped and "model_b_name" in swapped:
        swapped["model_a_name"], swapped["model_b_name"] = (
            swapped["model_b_name"],
            swapped["model_a_name"],
        )
    if "sha256_a" in swapped and "sha256_b" in swapped:
        swapped["sha256_a"], swapped["sha256_b"] = swapped["sha256_b"], swapped["sha256_a"]
    return swapped


def _legacy_cache_keys(
    model_a_path: str | Path,
    model_b_path: str | Path,
    *,
    n_games: int,
    seed: int,
) -> list[tuple[str, bool]]:
    path_a = Path(model_a_path)
    path_b = Path(model_b_path)
    ordered_candidates = [
        (str(path_a), str(path_b), False),
        (str(path_b), str(path_a), True),
        (path_a.name, path_b.name, False),
        (path_b.name, path_a.name, True),
    ]

    keys: list[tuple[str, bool]] = []
    seen: set[tuple[str, bool]] = set()
    for first, second, swapped in ordered_candidates:
        for key in (
            f"{first}:{second}",
            f"{first}:{second}:g{n_games}",
            f"{first}:{second}:g{n_games}:s{seed}",
        ):
            candidate = (key, swapped)
            if candidate not in seen:
                keys.append(candidate)
                seen.add(candidate)
    return keys


def lookup_match_cache_entry(
    cache: dict[str, dict[str, Any]],
    model_a_path: str | Path,
    model_b_path: str | Path,
    *,
    n_games: int,
    seed: int,
) -> dict[str, Any] | None:
    """Return a cached match entry normalized to the requested model order."""
    hash_a, hash_b, swapped = _canonical_hash_pair(model_a_path, model_b_path)
    key = _hash_cache_key(hash_a, hash_b, n_games=n_games, seed=seed)
    logger.debug("match cache lookup key: %s", key)

    entry = cache.get(key)
    if entry is not None and _entry_matches_request(entry, n_games=n_games, seed=seed):
        return _swap_entry(entry) if swapped else dict(entry)

    for legacy_key, legacy_swapped in _legacy_cache_keys(
        model_a_path,
        model_b_path,
        n_games=n_games,
        seed=seed,
    ):
        legacy_entry = cache.get(legacy_key)
        if legacy_entry is None:
            continue
        if not _entry_matches_request(legacy_entry, n_games=n_games, seed=seed):
            continue
        logger.debug("match cache legacy hit: %s", legacy_key)
        return _swap_entry(legacy_entry) if legacy_swapped else dict(legacy_entry)

    return None


def store_match_cache_entry(
    cache: dict[str, dict[str, Any]],
    model_a_path: str | Path,
    model_b_path: str | Path,
    *,
    n_games: int,
    seed: int,
    wins_a: int,
    wins_b: int,
    draws: int,
    model_a_name: str,
    model_b_name: str,
) -> tuple[str, dict[str, Any]]:
    """Store a match result under the canonical hash-based key."""
    hash_a, hash_b, swapped = _canonical_hash_pair(model_a_path, model_b_path)
    key = _hash_cache_key(hash_a, hash_b, n_games=n_games, seed=seed)
    logger.debug("match cache store key: %s", key)

    stored_entry = {
        "sha256_a": hash_a,
        "sha256_b": hash_b,
        "model_a_name": model_b_name if swapped else model_a_name,
        "model_b_name": model_a_name if swapped else model_b_name,
        "wins_a": wins_b if swapped else wins_a,
        "wins_b": wins_a if swapped else wins_b,
        "draws": draws,
        "games": n_games,
        "seed": seed,
        "timestamp": datetime.now(UTC).isoformat(),
    }
    cache[key] = stored_entry
    return key, dict(stored_entry)
