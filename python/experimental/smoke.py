from __future__ import annotations

import importlib.util
from pathlib import Path


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    here = Path(__file__).resolve().parent
    native = _load_module("ts_exp_native", here / "tscore_experimental.py")
    trace = native.get_tscore_experimental().play_selfplay_game(seed=12345, config={})
    print(trace["result"])
    print(len(trace["steps"]))
    print(trace["steps"][:5])


if __name__ == "__main__":
    main()
