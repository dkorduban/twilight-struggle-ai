#!/usr/bin/env python3
"""Compare Python and native opening headline choices on exact-matched setup."""

from __future__ import annotations

import argparse
import json
import subprocess
import sysconfig
from pathlib import Path

import numpy.random._generator as np_generator
from numpy.random import SeedSequence

from tsrl.engine.game_state import reset
from tsrl.policies.minimal_hybrid import choose_minimal_hybrid


def python_headline(seed: int) -> dict[str, int]:
    gs = reset(seed=seed)
    pub = gs.pub
    pub.phasing = 0
    ussr = choose_minimal_hybrid(pub, gs.hands[0], False)
    pub.phasing = 1
    us = choose_minimal_hybrid(pub, gs.hands[1], False)
    return {
        "ussr_card": int(ussr.card_id) if ussr is not None else -1,
        "ussr_mode": int(ussr.mode) if ussr is not None else -1,
        "us_card": int(us.card_id) if us is not None else -1,
        "us_mode": int(us.mode) if us is not None else -1,
    }


def native_headline(tool: Path, seed: int) -> dict[str, int]:
    words = SeedSequence(seed).generate_state(4, dtype="uint64").tolist()
    python_lib = Path(sysconfig.get_config_var("LIBDIR")) / sysconfig.get_config_var("LDLIBRARY")
    out = subprocess.check_output(
        [
            str(tool),
            "--word0",
            str(words[0]),
            "--word1",
            str(words[1]),
            "--word2",
            str(words[2]),
            "--word3",
            str(words[3]),
            "--numpy-generator-so",
            str(Path(np_generator.__file__)),
            "--python-lib",
            str(python_lib),
        ],
        text=True,
    )
    return json.loads(out)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=123)
    parser.add_argument(
        "--tool",
        type=Path,
        default=Path("build-ninja/cpp/tools/ts_initial_headline_choice"),
    )
    args = parser.parse_args()

    py = python_headline(args.seed)
    native = native_headline(args.tool, args.seed)
    print(json.dumps({"seed": args.seed, "match": py == native, "python": py, "native": native}, indent=2))


if __name__ == "__main__":
    main()
