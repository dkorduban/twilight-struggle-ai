#!/usr/bin/env python3
"""Compare Python and native initial setup state for a fixed seed."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

from tsrl.engine.game_state import reset


def python_setup(seed: int) -> dict[str, object]:
    gs = reset(seed=seed)
    return {
        "turn": gs.pub.turn,
        "ussr_hand": sorted(gs.hands[0]),
        "us_hand": sorted(gs.hands[1]),
        "deck_prefix": list(gs.deck[:16]),
        "deck_size": len(gs.deck),
    }


def native_setup(tool: Path, seed: int) -> dict[str, object]:
    out = subprocess.check_output([str(tool), "--seed", str(seed)], text=True)
    return json.loads(out)


def native_setup_from_words(tool: Path, seed: int) -> dict[str, object]:
    from numpy.random import SeedSequence
    import numpy.random._generator as np_generator
    import sysconfig

    words = SeedSequence(seed).generate_state(4, dtype="uint64").tolist()
    python_lib = Path(sysconfig.get_config_var("LIBDIR")) / sysconfig.get_config_var("LDLIBRARY")
    cmd = [
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
    ]
    out = subprocess.check_output(cmd, text=True)
    return json.loads(out)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=123)
    parser.add_argument(
        "--tool",
        type=Path,
        default=Path("build-ninja/cpp/tools/ts_dump_native_setup"),
    )
    parser.add_argument(
        "--mode",
        choices=("native-seed", "pcg64-words"),
        default="native-seed",
    )
    args = parser.parse_args()

    py = python_setup(args.seed)
    native = (
        native_setup(args.tool, args.seed)
        if args.mode == "native-seed"
        else native_setup_from_words(args.tool, args.seed)
    )
    report = {
        "seed": args.seed,
        "mode": args.mode,
        "match": py == native,
        "python": py,
        "native": native,
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
