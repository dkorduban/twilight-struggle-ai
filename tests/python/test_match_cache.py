from __future__ import annotations

from pathlib import Path

from tsrl.eval.match_cache import (
    file_sha256,
    lookup_match_cache_entry,
    match_cache_key,
)


def _write_bytes(path: Path, payload: bytes) -> Path:
    path.write_bytes(payload)
    return path


def test_identical_files_get_same_match_cache_key(tmp_path: Path) -> None:
    model_a = _write_bytes(tmp_path / "model_a.pt", b"same checkpoint bytes")
    model_b = _write_bytes(tmp_path / "model_b.pt", b"same checkpoint bytes")
    opponent = _write_bytes(tmp_path / "opponent.pt", b"opponent bytes")

    assert match_cache_key(model_a, opponent, n_games=200, seed=17) == match_cache_key(
        model_b,
        opponent,
        n_games=200,
        seed=17,
    )


def test_different_files_get_different_hashes(tmp_path: Path) -> None:
    model_a = _write_bytes(tmp_path / "model_a.pt", b"checkpoint A")
    model_b = _write_bytes(tmp_path / "model_b.pt", b"checkpoint B")

    assert file_sha256(model_a) != file_sha256(model_b)


def test_renaming_file_preserves_match_cache_key(tmp_path: Path) -> None:
    model_path = _write_bytes(tmp_path / "model.pt", b"rename stable")
    opponent = _write_bytes(tmp_path / "opponent.pt", b"opponent bytes")

    key_before = match_cache_key(model_path, opponent, n_games=100, seed=9)
    renamed_path = model_path.rename(tmp_path / "renamed_model.pt")
    key_after = match_cache_key(renamed_path, opponent, n_games=100, seed=9)

    assert key_before == key_after


def test_lookup_reads_legacy_filename_keys(tmp_path: Path) -> None:
    model_a = _write_bytes(tmp_path / "model_a.pt", b"legacy A")
    model_b = _write_bytes(tmp_path / "model_b.pt", b"legacy B")
    cache = {
        "model_a.pt:model_b.pt": {
            "wins_a": 7,
            "wins_b": 3,
            "games": 10,
            "seed": 123,
        }
    }

    forward = lookup_match_cache_entry(cache, model_a, model_b, n_games=10, seed=123)
    reverse = lookup_match_cache_entry(cache, model_b, model_a, n_games=10, seed=123)

    assert forward == {"wins_a": 7, "wins_b": 3, "games": 10, "seed": 123}
    assert reverse == {"wins_a": 3, "wins_b": 7, "games": 10, "seed": 123}
