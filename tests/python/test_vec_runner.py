from __future__ import annotations

from tsrl.engine.game_state import reset
from tsrl.engine.game_loop import GameResult
from tsrl.engine.legal_actions import enumerate_actions, sample_action
from tsrl.engine.mcts import SelfPlayStep
from tsrl.engine.vec_runner import run_games_vectorized
from tsrl.schemas import ActionEncoding, ActionMode, Side


def _pick_ranked_action(req, *, reverse: bool) -> ActionEncoding:
    actions = enumerate_actions(
        req.hand,
        req.pub,
        req.side,
        holds_china=req.holds_china,
        max_influence_targets=6,
    )
    ranked = sorted(actions, key=lambda a: (a.card_id, int(a.mode), a.targets))
    action = ranked[-1] if reverse else ranked[0]
    if req.pub.ar == 0:
        return ActionEncoding(card_id=action.card_id, mode=ActionMode.EVENT, targets=())
    return action


def test_run_games_vectorized_basic():
    done: list[tuple[int, list[SelfPlayStep], GameResult]] = []

    def learned_infer_fn(reqs, game_states):
        return [
            sample_action(
                req.hand,
                req.pub,
                req.side,
                holds_china=req.holds_china,
            )
            for req in reqs
        ]

    def heuristic_fn(req):
        return sample_action(
            req.hand,
            req.pub,
            req.side,
            holds_china=req.holds_china,
        )

    results = run_games_vectorized(
        n_games=4,
        make_game_fn=lambda: reset(seed=123),
        learned_side_fn=lambda game_idx: Side.USSR if game_idx % 2 == 0 else Side.US,
        learned_infer_fn=learned_infer_fn,
        heuristic_fn=heuristic_fn,
        seed_base=11,
        max_turns=1,
        on_game_done=lambda game_idx, steps, result: done.append((game_idx, steps, result)),
    )

    assert len(results) == 4
    assert len(done) == 4
    for result in results:
        assert isinstance(result, GameResult)
    for game_idx, steps, result in done:
        assert isinstance(game_idx, int)
        assert all(step.game_result == result for step in steps)


def test_run_games_vectorized_uses_expected_learned_side():
    done: dict[int, list[SelfPlayStep]] = {}

    results = run_games_vectorized(
        n_games=4,
        make_game_fn=lambda: reset(seed=456),
        learned_side_fn=lambda game_idx: Side.USSR if game_idx % 2 == 0 else Side.US,
        learned_infer_fn=lambda reqs, _gs: [_pick_ranked_action(req, reverse=True) for req in reqs],
        heuristic_fn=lambda req: _pick_ranked_action(req, reverse=False),
        seed_base=21,
        max_turns=1,
        on_game_done=lambda game_idx, steps, result: done.setdefault(game_idx, steps),
    )

    assert len(results) == 4
    assert set(done) == {0, 1, 2, 3}
    for game_idx, steps in done.items():
        learned_side = Side.USSR if game_idx % 2 == 0 else Side.US
        heuristic_side = Side.US if learned_side == Side.USSR else Side.USSR
        learned_actions = [
            _pick_ranked_action(
                type(
                    "Req",
                    (),
                    {
                        "hand": step.hand,
                        "pub": step.pub_snapshot,
                        "side": step.side,
                        "holds_china": step.holds_china,
                    },
                )(),
                reverse=True,
            )
            for step in steps
            if step.side == learned_side
        ]
        heuristic_actions = [
            _pick_ranked_action(
                type(
                    "Req",
                    (),
                    {
                        "hand": step.hand,
                        "pub": step.pub_snapshot,
                        "side": step.side,
                        "holds_china": step.holds_china,
                    },
                )(),
                reverse=False,
            )
            for step in steps
            if step.side == heuristic_side
        ]
        assert learned_actions, f"game {game_idx} never reached learned side"
        assert heuristic_actions, f"game {game_idx} never reached heuristic side"
        assert all(
            step.action == expected
            for step, expected in zip(
                [step for step in steps if step.side == learned_side],
                learned_actions,
            )
        )
        assert all(
            step.action == expected
            for step, expected in zip(
                [step for step in steps if step.side == heuristic_side],
                heuristic_actions,
            )
        )


def test_run_games_vectorized_batches_learned_inference():
    call_count = 0

    def learned_infer_fn(reqs, game_states):
        nonlocal call_count
        call_count += 1
        return [_pick_ranked_action(req, reverse=True) for req in reqs]

    results = run_games_vectorized(
        n_games=4,
        make_game_fn=lambda: reset(seed=789),
        learned_side_fn=lambda game_idx: Side.USSR if game_idx % 2 == 0 else Side.US,
        learned_infer_fn=learned_infer_fn,
        heuristic_fn=lambda req: _pick_ranked_action(req, reverse=False),
        seed_base=31,
        max_turns=1,
    )

    assert len(results) == 4
    assert call_count > 0
