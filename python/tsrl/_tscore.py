from __future__ import annotations

import importlib
import sys
from pathlib import Path
from types import ModuleType

_TSCORE: ModuleType | None = None


def get_tscore() -> ModuleType:
    """Import the native ``tscore`` module, preferring the build-ninja binding."""
    global _TSCORE
    if _TSCORE is not None:
        return _TSCORE

    repo_root = Path(__file__).resolve().parents[2]
    for bindings_path in (
        repo_root / "build-ninja" / "bindings",
        repo_root / "build" / "bindings",
    ):
        bindings_dir = str(bindings_path)
        if any(bindings_path.glob("tscore*.so")):
            if bindings_dir not in sys.path:
                sys.path.insert(0, bindings_dir)
            break

    try:
        _TSCORE = importlib.import_module("tscore")
    except ImportError as exc:
        raise ImportError(
            "tscore bindings are not available. Build them under build-ninja/bindings "
            "or add the bindings directory to PYTHONPATH."
        ) from exc
    return _TSCORE
