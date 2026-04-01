#!/usr/bin/env python3
"""Small-scale smoke validation for the native C++ runtime.

This deliberately lives under cpp/tools so validation logic can evolve with the
native runtime without depending on the Python research loop. It exercises the
native bindings and collection tooling end-to-end on small seeds.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

import tscore


def check_traced_game(game: tscore.TracedGame) -> None:
    assert game.result.end_turn >= 1
    assert game.result.end_reason
    assert len(game.steps) > 0

    for step in game.steps:
        assert step.turn >= 1
        assert step.ar >= 0
        assert 1 <= step.defcon_before <= 5
        assert 1 <= step.defcon_after <= 5
        assert step.action.card_id > 0
        if step.action.mode in (tscore.ActionMode.Event, tscore.ActionMode.Space):
            assert len(step.action.targets) == 0
        if step.action.mode == tscore.ActionMode.Coup:
            assert len(step.action.targets) == 1
        if step.action.mode == tscore.ActionMode.Realign:
            assert len(step.action.targets) >= 1


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--games", type=int, default=3)
    parser.add_argument("--seed", type=int, default=101)
    parser.add_argument("--model", type=Path, default=None)
    parser.add_argument(
        "--rows-tool",
        type=Path,
        default=Path("build-ninja/cpp/tools/ts_collect_selfplay_rows_jsonl"),
    )
    args = parser.parse_args()

    for offset in range(args.games):
        seed = args.seed + offset
        game = tscore.play_traced_game(
            tscore.PolicyKind.MinimalHybrid,
            tscore.PolicyKind.Random,
            seed,
        )
        check_traced_game(game)

    results = tscore.play_matchup(
        tscore.PolicyKind.MinimalHybrid,
        tscore.PolicyKind.Random,
        args.games,
        args.seed,
    )
    summary = tscore.summarize_results(results)
    assert summary.games == args.games
    assert summary.ussr_wins + summary.us_wins + summary.draws == args.games

    if args.model is not None:
        learned = tscore.play_learned_matchup(
            str(args.model),
            tscore.Side.USSR,
            tscore.PolicyKind.Random,
            1,
            args.seed,
        )
        learned_summary = tscore.summarize_results(learned)
        assert learned_summary.games == 1

    rows_out = Path("/tmp/ts_native_rows_smoke.jsonl")
    subprocess.run(
        [
            str(args.rows_tool),
            "--out",
            str(rows_out),
            "--games",
            "1",
            "--seed",
            str(args.seed),
            "--ussr-policy",
            "minimal_hybrid",
            "--us-policy",
            "random",
        ],
        check=True,
    )
    row = json.loads(rows_out.read_text().splitlines()[0])
    required = {
        "game_id",
        "step_idx",
        "turn",
        "ar",
        "phasing",
        "action_card_id",
        "action_mode",
        "action_targets",
        "winner_side",
        "final_vp",
        "end_turn",
        "end_reason",
        "actor_known_in",
        "lbl_actor_hand",
        "ussr_influence",
        "us_influence",
    }
    assert required.issubset(row)
    assert len(row["actor_known_in"]) == 112
    assert len(row["lbl_actor_hand"]) == 112
    assert len(row["ussr_influence"]) == 86
    assert len(row["us_influence"]) == 86

    print("native smoke ok")


if __name__ == "__main__":
    main()
