from __future__ import annotations

import importlib
import sys
from pathlib import Path
from types import ModuleType

_MODULE: ModuleType | None = None


def get_tscore_experimental() -> ModuleType:
    global _MODULE
    if _MODULE is not None:
        return _MODULE

    repo_root = Path(__file__).resolve().parents[2]
    for bindings_path in (
        repo_root / "build-ninja" / "cpp" / "experimental",
        repo_root / "build" / "cpp" / "experimental",
    ):
        bindings_dir = str(bindings_path)
        if any(bindings_path.glob("ts_experimental*.so")):
            if bindings_dir not in sys.path:
                sys.path.insert(0, bindings_dir)
            break

    _MODULE = importlib.import_module("ts_experimental")
    return _MODULE

