import warnings

warnings.warn(
    "tsrl.engine is deprecated. Use the tscore C++ bindings "
    "(PYTHONPATH=build-ninja/bindings) instead. "
    "The Python engine will be removed in a future release.",
    DeprecationWarning,
    stacklevel=2,
)
