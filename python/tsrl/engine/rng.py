"""PCG64-based RNG factory for cross-language reproducibility.

All game-logic RNG in this repo uses numpy's PCG64 generator (returned by
``np.random.default_rng(seed)``).  PCG64 has a reference C++ implementation
(https://www.pcg-random.org/) that produces bit-identical output for the same
seed, enabling C++ self-play workers to match Python seeds exactly.

Cutover
-------
Generation v28 onwards uses PCG64.  Generations v1–v27 used Python's stdlib
``random.Random`` (MT19937).  **Do not reuse old seeds across the cutover —
the same integer seed produces a completely different sequence under each
generator.**  Old seed values were typically in the range 20 000–50 000;
new seeds should use the same range but be understood as PCG64.

PCG64_EPOCH_GEN marks the first generation trained with PCG64 seeds.

Usage
-----
    from tsrl.engine.rng import make_rng

    rng = make_rng(seed)          # seeded
    rng = make_rng()              # random seed (for ad-hoc use)

API differences vs random.Random
---------------------------------
    random.Random              np.random.Generator (PCG64)
    -----------------------------------------------------------
    rng.randint(a, b)          int(rng.integers(a, b + 1))   # b inclusive
    rng.choice(seq)            rng.choice(seq)                # cast int() for IDs
    rng.random()               rng.random()                   # identical
    rng.shuffle(lst)           rng.shuffle(lst)               # identical
"""

from __future__ import annotations

from ._deprecation import warn_engine_deprecated

warn_engine_deprecated(__name__)

import numpy as np

# First generation trained with PCG64 seeds (v1–v27 used MT19937 / random.Random).
PCG64_EPOCH_GEN: int = 28

# Convenience type alias used in annotations throughout the codebase.
RNG = np.random.Generator


def make_rng(seed: int | None = None) -> np.random.Generator:
    """Return a seeded PCG64 Generator.

    Parameters
    ----------
    seed:
        Integer seed.  Pass ``None`` to get a randomly-seeded generator
        (uses OS entropy — not reproducible).
    """
    return np.random.default_rng(seed)
