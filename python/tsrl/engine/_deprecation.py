"""Shared deprecation warning text for the legacy Python engine."""

from __future__ import annotations

import warnings


def warn_engine_deprecated(module_name: str) -> None:
    """Emit a module-level deprecation warning for the Python engine."""
    warnings.warn(
        f"{module_name} is deprecated. Use the tscore C++ bindings "
        "(PYTHONPATH=build-ninja/bindings) instead. "
        "The Python engine will be removed in a future release.",
        DeprecationWarning,
        stacklevel=2,
    )
