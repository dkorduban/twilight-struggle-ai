from __future__ import annotations

import random
from copy import copy
from dataclasses import dataclass, field
from typing import Callable, Generator, Optional

from tsrl.engine.game_loop import DecisionRequest, GameResult, _run_game_gen
from tsrl.engine.game_state import GameState
from tsrl.engine.mcts import SelfPlayStep
from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Side

__all__ = ["run_games_vectorized"]


@dataclass
class Slot:
    game_idx: int
    gs: GameState
    gen: Generator[DecisionRequest, Optional[ActionEncoding], GameResult]
    req: DecisionRequest
    steps: list[SelfPlayStep] = field(default_factory=list)
    learned_side: Side = Side.USSR
    pending_step: Optional[SelfPlayStep] = None


def _snapshot_pub(pub: PublicState) -> PublicState:
    snap = copy(pub)
    snap.milops = list(pub.milops)
    snap.space = list(pub.space)
    snap.space_attempts = list(pub.space_attempts)
    snap.ops_modifier = list(pub.ops_modifier)
    snap.influence = pub.influence.copy()
    return snap


def _record_action(slot: Slot, action: ActionEncoding) -> None:
    recorded_action = action
    if slot.req.pub.ar == 0:
        recorded_action = ActionEncoding(
            card_id=action.card_id,
            mode=ActionMode.EVENT,
            targets=(),
        )
    step = SelfPlayStep(
        pub_snapshot=_snapshot_pub(slot.req.pub),
        side=slot.req.side,
        hand=slot.req.hand,
        holds_china=slot.req.holds_china,
        action=recorded_action,
    )
    slot.steps.append(step)
    slot.pending_step = step


def _finalize_slot(
    slot: Slot,
    result: GameResult,
    results: list[GameResult | None],
    on_game_done: Callable[[int, list[SelfPlayStep], GameResult], None] | None,
) -> None:
    if slot.pending_step is not None:
        slot.pending_step.post_pub = _snapshot_pub(slot.gs.pub)
        slot.pending_step = None
    for step in slot.steps:
        step.game_result = result
    results[slot.game_idx] = result
    if on_game_done is not None:
        on_game_done(slot.game_idx, slot.steps, result)


def _advance_slot(
    slot: Slot,
    action: ActionEncoding,
    results: list[GameResult | None],
    on_game_done: Callable[[int, list[SelfPlayStep], GameResult], None] | None,
) -> bool:
    _record_action(slot, action)
    try:
        slot.req = slot.gen.send(action)
    except StopIteration as exc:
        _finalize_slot(slot, exc.value, results, on_game_done)
        return True

    if slot.pending_step is not None:
        slot.pending_step.post_pub = _snapshot_pub(slot.gs.pub)
        slot.pending_step = None
    return False


def run_games_vectorized(
    n_games: int,
    make_game_fn: Callable[[], GameState],
    learned_side_fn: Callable[[int], Side],
    learned_infer_fn: Callable[
        [list[DecisionRequest], list[GameState]], list[ActionEncoding]
    ],
    heuristic_fn: Callable[[DecisionRequest], ActionEncoding],
    seed_base: int = 0,
    max_turns: int = 10,
    on_game_done: Callable[[int, list[SelfPlayStep], GameResult], None] | None = None,
) -> list[GameResult]:
    """Run n_games concurrently, batching all learned-side decisions.

    learned_infer_fn receives both the list of DecisionRequests AND the
    corresponding list of live GameState objects so that callers needing the
    full state (e.g. MCTS) can use it directly without a separate lookup.
    """
    results: list[GameResult | None] = [None] * n_games
    active_slots: list[Slot] = []

    for game_idx in range(n_games):
        gs = make_game_fn()
        rng = random.Random(seed_base + game_idx)
        gen = _run_game_gen(gs, rng, max_turns)
        try:
            req = next(gen)
        except StopIteration as exc:
            results[game_idx] = exc.value
            if on_game_done is not None:
                on_game_done(game_idx, [], exc.value)
            continue
        active_slots.append(
            Slot(
                game_idx=game_idx,
                gs=gs,
                gen=gen,
                req=req,
                learned_side=learned_side_fn(game_idx),
            )
        )

    while active_slots:
        still_active: list[Slot] = []
        for slot in active_slots:
            finished = False
            while slot.req.side != slot.learned_side:
                action = heuristic_fn(slot.req)
                finished = _advance_slot(slot, action, results, on_game_done)
                if finished:
                    break
            if not finished:
                still_active.append(slot)
        active_slots = still_active
        if not active_slots:
            break

        requests = [slot.req for slot in active_slots]
        game_states = [slot.gs for slot in active_slots]
        actions = learned_infer_fn(requests, game_states)
        if len(actions) != len(active_slots):
            raise ValueError(
                f"learned_infer_fn returned {len(actions)} actions for "
                f"{len(active_slots)} requests"
            )

        next_active: list[Slot] = []
        for slot, action in zip(active_slots, actions):
            if not _advance_slot(slot, action, results, on_game_done):
                next_active.append(slot)
        active_slots = next_active

    return [result for result in results if result is not None]
