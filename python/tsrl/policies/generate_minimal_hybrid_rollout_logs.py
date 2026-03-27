"""Generate detailed self-play rollout logs for minimal_hybrid."""
from __future__ import annotations

import argparse
import copy
import json
import os
import random
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from pathlib import Path

from tsrl.engine.game_loop import (
    _MAX_TURNS,
    GameResult,
    _end_of_turn,
    _run_action_rounds,
    _run_extra_ar,
    _run_headline_phase,
)
from tsrl.engine.game_state import (
    _ars_for_turn,
    advance_to_late_war,
    advance_to_mid_war,
    deal_cards,
    reset,
)
from tsrl.etl.game_data import load_cards, load_countries
from tsrl.policies.minimal_hybrid import (
    DEFAULT_MINIMAL_HYBRID_PARAMS,
    DecisionAnalysis,
    MinimalHybridParams,
    analyze_minimal_hybrid_decision,
    make_minimal_hybrid_policy,
)
from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Side

_CARDS = load_cards()
_COUNTRIES = load_countries()


@dataclass
class TraceStep:
    step_idx: int
    turn: int
    ar: int
    side: str
    holds_china: bool
    hand: list[dict[str, object]]
    flags: list[str]
    public_state: dict[str, object]
    legal_action_count: int
    chosen_action: dict[str, object] | None
    top_actions: list[dict[str, object]]
    post_public_state: dict[str, object] | None = None
    action_effects: dict[str, object] | None = None


def _snapshot_pub(pub: PublicState) -> PublicState:
    cloned = copy.copy(pub)
    cloned.milops = list(pub.milops)
    cloned.space = list(pub.space)
    cloned.space_attempts = list(pub.space_attempts)
    cloned.ops_modifier = list(pub.ops_modifier)
    cloned.influence = dict(pub.influence)
    return cloned


def _card_summary(card_id: int) -> dict[str, object]:
    card = _CARDS[card_id]
    return {
        "card_id": card_id,
        "name": card.name,
        "ops": card.ops,
        "side": Side(card.side).name if not isinstance(card.side, Side) else card.side.name,
        "is_scoring": card.is_scoring,
        "starred": card.starred,
    }


def _action_summary(action: ActionEncoding | None) -> dict[str, object] | None:
    if action is None:
        return None
    return {
        "card": _card_summary(action.card_id),
        "mode": action.mode.name,
        "targets": [
            {
                "country_id": cid,
                "name": _COUNTRIES[cid].name,
            }
            for cid in action.targets
        ],
    }


def _breakdown_summary(analysis: DecisionAnalysis) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for item in analysis.ranked_actions:
        rows.append(
            {
                "action": _action_summary(item.action),
                "total_score": round(item.total_score, 4),
                "mode_prior": round(item.mode_prior, 4),
                "mode_detail": round(item.mode_detail, 4),
                "event_score": round(item.event_score, 4),
                "card_bias": round(item.card_bias, 4),
                "ops_penalty": round(item.ops_penalty, 4),
                "headline_adjustment": round(item.headline_adjustment, 4),
                "notes": list(item.notes),
            }
        )
    return rows


def _hand_summary(hand: frozenset[int]) -> list[dict[str, object]]:
    return [_card_summary(card_id) for card_id in sorted(hand)]


def _public_state_summary(pub: PublicState) -> dict[str, object]:
    influence_rows: list[dict[str, object]] = []
    seen = {
        country_id
        for (_side, country_id), amount in pub.influence.items()
        if amount > 0
    }
    for country_id in sorted(seen):
        ussr = pub.influence.get((Side.USSR, country_id), 0)
        us = pub.influence.get((Side.US, country_id), 0)
        if ussr == 0 and us == 0:
            continue
        influence_rows.append(
            {
                "country_id": country_id,
                "name": _COUNTRIES[country_id].name,
                "ussr": ussr,
                "us": us,
                "battleground": _COUNTRIES[country_id].is_battleground,
                "region": _COUNTRIES[country_id].region.name,
            }
        )
    return {
        "turn": pub.turn,
        "ar": pub.ar,
        "phasing": pub.phasing.name,
        "vp": pub.vp,
        "defcon": pub.defcon,
        "milops": {"USSR": pub.milops[0], "US": pub.milops[1]},
        "space": {"USSR": pub.space[0], "US": pub.space[1]},
        "china_held_by": pub.china_held_by.name,
        "china_playable": pub.china_playable,
        "influence": influence_rows,
    }


def _decision_flags(
    pub: PublicState,
    hand: frozenset[int],
    holds_china: bool,
    action: ActionEncoding | None,
) -> list[str]:
    flags: list[str] = []
    other_side = Side.US if pub.phasing == Side.USSR else Side.USSR
    if any(_CARDS[card_id].is_scoring for card_id in hand):
        flags.append("scoring_in_hand")
    if holds_china:
        flags.append("holds_china")
    milops_short = max(0, pub.turn - pub.milops[int(pub.phasing)])
    if milops_short > 0:
        flags.append(f"milops_shortfall:{milops_short}")
    if pub.space[int(pub.phasing)] < pub.space[int(other_side)]:
        flags.append("behind_on_space")
    if action is not None:
        card = _CARDS[action.card_id]
        if action.mode != ActionMode.EVENT and card.side not in (pub.phasing, Side.NEUTRAL):
            flags.append("offside_ops_play")
        if action.mode.name == "SPACE":
            flags.append("space_play")
    return flags


def _diff_states(before: PublicState, after: PublicState) -> dict[str, object]:
    influence_changes: list[dict[str, object]] = []
    country_ids = {
        country_id
        for _side, country_id in before.influence.keys() | after.influence.keys()
    }
    for country_id in sorted(country_ids):
        before_ussr = before.influence.get((Side.USSR, country_id), 0)
        before_us = before.influence.get((Side.US, country_id), 0)
        after_ussr = after.influence.get((Side.USSR, country_id), 0)
        after_us = after.influence.get((Side.US, country_id), 0)
        if before_ussr == after_ussr and before_us == after_us:
            continue
        influence_changes.append(
            {
                "country_id": country_id,
                "name": _COUNTRIES[country_id].name,
                "ussr": [before_ussr, after_ussr],
                "us": [before_us, after_us],
            }
        )
    return {
        "vp_delta": after.vp - before.vp,
        "defcon_delta": after.defcon - before.defcon,
        "milops_delta": {
            "USSR": after.milops[0] - before.milops[0],
            "US": after.milops[1] - before.milops[1],
        },
        "space_delta": {
            "USSR": after.space[0] - before.space[0],
            "US": after.space[1] - before.space[1],
        },
        "china_held_by": [before.china_held_by.name, after.china_held_by.name],
        "china_playable": [before.china_playable, after.china_playable],
        "influence_changes": influence_changes,
    }


def _render_markdown(
    *,
    seed: int,
    result: GameResult,
    steps: list[TraceStep],
) -> str:
    lines = [
        "# minimal_hybrid detailed rollout log",
        "",
        f"- seed: `{seed}`",
        f"- winner: `{result.winner.name if result.winner is not None else 'DRAW'}`",
        f"- final_vp: `{result.final_vp}`",
        f"- end_turn: `{result.end_turn}`",
        f"- end_reason: `{result.end_reason}`",
        "",
    ]
    for step in steps:
        chosen = step.chosen_action
        chosen_text = "pass"
        hand_text = ", ".join(
            f"{card['name']}[{card['card_id']}]"
            for card in step.hand
        )
        state_text = (
            f"VP {step.public_state['vp']}, "
            f"DEFCON {step.public_state['defcon']}, "
            f"MilOps U{step.public_state['milops']['USSR']}/"
            f"A{step.public_state['milops']['US']}, "
            f"Space U{step.public_state['space']['USSR']}/"
            f"A{step.public_state['space']['US']}, "
            f"China {step.public_state['china_held_by']} "
            f"({'up' if step.public_state['china_playable'] else 'down'})"
        )
        if chosen is not None:
            chosen_text = (
                f"{chosen['card']['name']} [{chosen['card']['card_id']}] "
                f"as {chosen['mode']}"
            )
        lines.extend(
            [
                f"## Step {step.step_idx}: T{step.turn} AR{step.ar} {step.side}",
                "",
                f"- chosen: `{chosen_text}`",
                f"- flags: `{', '.join(step.flags) if step.flags else 'none'}`",
                f"- hand: `{hand_text}`",
                f"- state: `{state_text}`",
                "",
                "| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |",
                "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
            ]
        )
        for idx, row in enumerate(step.top_actions, start=1):
            action = row["action"]
            target_text = ", ".join(target["name"] for target in action["targets"])
            if target_text:
                action_text = f"{action['card']['name']} {action['mode']} {target_text}"
            else:
                action_text = f"{action['card']['name']} {action['mode']}"
            lines.append(
                f"| {idx} | {action_text} | {row['total_score']:.2f} | {row['mode_prior']:.2f} "
                f"| {row['mode_detail']:.2f} | {row['event_score']:.2f} | {row['card_bias']:.2f} "
                f"| {row['ops_penalty']:.2f} | {row['headline_adjustment']:.2f} "
                f"| {', '.join(row['notes']) if row['notes'] else ''} |"
            )
        if step.action_effects is not None:
            lines.extend(
                [
                    "",
                    (
                        f"- effects: `VP {step.action_effects['vp_delta']:+}, "
                        f"DEFCON {step.action_effects['defcon_delta']:+}, "
                        f"MilOps U{step.action_effects['milops_delta']['USSR']:+}/"
                        f"A{step.action_effects['milops_delta']['US']:+}`"
                    ),
                ]
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _generate_one_game(
    *,
    seed: int,
    params: MinimalHybridParams,
    top_n: int,
) -> tuple[list[TraceStep], GameResult]:
    rng = random.Random(seed)
    gs = reset(seed=rng.randint(0, 2**32))
    steps: list[TraceStep] = []
    pending: list[TraceStep | None] = [None]
    step_idx = 0
    traced_policy = make_minimal_hybrid_policy(params)

    def _trace_policy(pub: PublicState, hand: frozenset[int], holds_china: bool):
        nonlocal step_idx
        if pending[0] is not None:
            pending[0].post_public_state = _public_state_summary(gs.pub)
            pending[0].action_effects = _diff_states(
                _restore_pub(pending[0].public_state),
                gs.pub,
            )
            pending[0] = None

        analysis = analyze_minimal_hybrid_decision(
            pub,
            hand,
            holds_china,
            params=params,
            top_n=top_n,
        )
        action = analysis.chosen_action
        if action is None:
            return traced_policy(pub, hand, holds_china)

        step_idx += 1
        step = TraceStep(
            step_idx=step_idx,
            turn=pub.turn,
            ar=pub.ar,
            side=pub.phasing.name,
            holds_china=holds_china,
            hand=_hand_summary(hand),
            flags=_decision_flags(pub, hand, holds_china, action),
            public_state=_public_state_summary(_snapshot_pub(pub)),
            legal_action_count=analysis.legal_action_count,
            chosen_action=_action_summary(action),
            top_actions=_breakdown_summary(analysis),
        )
        steps.append(step)
        pending[0] = step
        return action

    result: GameResult | None = None
    for turn in range(1, _MAX_TURNS + 1):
        gs.pub.turn = turn
        if turn == 4:
            advance_to_mid_war(gs, rng)
        elif turn == 8:
            advance_to_late_war(gs, rng)

        deal_cards(gs, Side.USSR, rng)
        deal_cards(gs, Side.US, rng)

        result = _run_headline_phase(gs, _trace_policy, _trace_policy, rng)
        if result is not None:
            break

        result = _run_action_rounds(gs, _trace_policy, _trace_policy, rng, _ars_for_turn(turn))
        if result is not None:
            break

        if gs.pub.north_sea_oil_extra_ar:
            gs.pub.north_sea_oil_extra_ar = False
            result = _run_extra_ar(gs, Side.US, _trace_policy, rng)
            if result is not None:
                break

        if gs.pub.glasnost_extra_ar:
            gs.pub.glasnost_extra_ar = False
            result = _run_extra_ar(gs, Side.USSR, _trace_policy, rng)
            if result is not None:
                break

        result = _end_of_turn(gs, rng, turn)
        if result is not None:
            break

    if result is None:
        winner = None
        if gs.pub.vp > 0:
            winner = Side.USSR
        elif gs.pub.vp < 0:
            winner = Side.US
        result = GameResult(
            winner=winner,
            final_vp=gs.pub.vp,
            end_turn=_MAX_TURNS,
            end_reason="turn_limit",
        )

    if pending[0] is not None:
        pending[0].post_public_state = _public_state_summary(gs.pub)
        pending[0].action_effects = _diff_states(
            _restore_pub(pending[0].public_state),
            gs.pub,
        )

    return steps, result


def _generate_game_artifacts(
    task: tuple[int, int, int, MinimalHybridParams],
) -> tuple[int, dict[str, object], str, dict[str, object]]:
    game_idx, seed, top_n, params = task
    steps, result = _generate_one_game(
        seed=seed,
        params=params,
        top_n=top_n,
    )
    payload = {
        "seed": seed,
        "result": {
            "winner": result.winner.name if result.winner is not None else None,
            "final_vp": result.final_vp,
            "end_turn": result.end_turn,
            "end_reason": result.end_reason,
        },
        "steps": [asdict(step) for step in steps],
    }
    summary_row = {
        "game": game_idx + 1,
        "seed": seed,
        "winner": payload["result"]["winner"],
        "final_vp": result.final_vp,
        "end_turn": result.end_turn,
        "end_reason": result.end_reason,
        "steps": len(steps),
    }
    markdown = _render_markdown(seed=seed, result=result, steps=steps)
    return game_idx, payload, markdown, summary_row


def _restore_pub(payload: dict[str, object]) -> PublicState:
    pub = PublicState()
    pub.turn = int(payload["turn"])
    pub.ar = int(payload["ar"])
    pub.phasing = Side[payload["phasing"]]
    pub.vp = int(payload["vp"])
    pub.defcon = int(payload["defcon"])
    pub.milops = [int(payload["milops"]["USSR"]), int(payload["milops"]["US"])]
    pub.space = [int(payload["space"]["USSR"]), int(payload["space"]["US"])]
    pub.china_held_by = Side[payload["china_held_by"]]
    pub.china_playable = bool(payload["china_playable"])
    for row in payload["influence"]:
        pub.influence[(Side.USSR, int(row["country_id"]))] = int(row["ussr"])
        pub.influence[(Side.US, int(row["country_id"]))] = int(row["us"])
    return pub


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--games", type=int, default=5)
    parser.add_argument("--seed-start", type=int, default=20260401)
    parser.add_argument("--top-n", type=int, default=5)
    parser.add_argument(
        "--workers",
        type=int,
        default=max(1, (os.cpu_count() or 1) // 2),
    )
    parser.add_argument(
        "--out-dir",
        default=(
            "python/tsrl/policies/rollout_logs/"
            f"{time.strftime('%Y%m%d_%H%M%S', time.localtime())}"
        ),
    )
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    summary_rows: list[dict[str, object]] = []
    tasks = [
        (game_idx, args.seed_start + game_idx, args.top_n, DEFAULT_MINIMAL_HYBRID_PARAMS)
        for game_idx in range(args.games)
    ]

    results: list[tuple[int, dict[str, object], str, dict[str, object]]] = []
    if args.workers <= 1:
        results = [_generate_game_artifacts(task) for task in tasks]
    else:
        with ProcessPoolExecutor(max_workers=args.workers) as pool:
            future_map = {
                pool.submit(_generate_game_artifacts, task): task[0]
                for task in tasks
            }
            for completed, future in enumerate(as_completed(future_map), start=1):
                result = future.result()
                results.append(result)
                print(f"completed {completed}/{len(tasks)}", flush=True)

    for game_idx, payload, markdown, summary_row in sorted(results, key=lambda item: item[0]):
        json_path = out_dir / f"game_{game_idx + 1:02d}.json"
        md_path = out_dir / f"game_{game_idx + 1:02d}.md"
        json_path.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        md_path.write_text(
            markdown,
            encoding="utf-8",
        )
        summary_rows.append(summary_row)

    (out_dir / "summary.json").write_text(
        json.dumps({"games": summary_rows}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(out_dir)


if __name__ == "__main__":
    main()
