from __future__ import annotations

import importlib.util
import sys
from functools import lru_cache
from pathlib import Path
from types import ModuleType

REPO_ROOT = Path(__file__).resolve().parents[2]
TRAIN_PPO_PATH = REPO_ROOT / "scripts" / "train_ppo.py"


@lru_cache(maxsize=1)
def load_train_ppo_module() -> ModuleType:
    """Load the live PPO trainer module without modifying it.

    The production PPO entrypoint lives in ``scripts/train_ppo.py`` rather than
    an importable package module. Experiments still need access to its helpers
    such as ``Step``, ``load_model``, ``compute_gae_batch``, and
    ``_export_temp_model``. This loader keeps that dependency one-way:
    experiments can call into the live script, but production code stays
    untouched.
    """
    spec = importlib.util.spec_from_file_location(
        "experimental_train_ppo_live",
        TRAIN_PPO_PATH,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load module from {TRAIN_PPO_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module
