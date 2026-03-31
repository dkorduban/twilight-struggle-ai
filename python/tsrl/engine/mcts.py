"""
Monte Carlo Tree Search (UCT) for Twilight Struggle.

Three implementations:

  flat_mcts(gs, n_sim, rng) → ActionEncoding
    For each legal action at the root, run n_sim//n_actions rollouts.
    Fast, simple, suitable as an initial baseline over random policy.

  uct_mcts(gs, n_sim, rng, c) → ActionEncoding
    Full UCT with UCB1 selection, expansion, rollout/value, backpropagation.
    Single-tree. Supports an optional batch_value_fn that defers all leaf
    evaluations to one call after all simulations complete (keeps the
    batch_value_fn interface for callers that already construct it).

  interleaved_uct_mcts(game_states, n_sim, batch_value_fn) → list[ActionEncoding]
    Run N UCT trees in lockstep, sharing one batched value function call per
    round.  Each round: every tree does one select+expand step, all leaf
    states are evaluated together, every tree backpropagates.  UCB1 is
    correct (stats updated before each round's selection) and the GPU batch
    size equals N (number of parallel positions) rather than 1.

All use perfect-information rollouts (both hands visible), appropriate for
self-play training data generation.

Value convention: +1.0 = USSR wins, -1.0 = US wins, 0.0 = draw.
All UCB1 statistics are stored from USSR's perspective for consistency.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Callable, Optional

import numpy as np

from tsrl.engine.rng import RNG, make_rng

from tsrl.engine.game_loop import GameResult, Policy, make_random_policy, play_from_state
from tsrl.engine.game_state import GameState, clone_game_state
from tsrl.engine.legal_actions import sample_action
from tsrl.engine.step import apply_action
from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Side

# ---------------------------------------------------------------------------
# Value helpers
# ---------------------------------------------------------------------------


def _result_value(result: GameResult) -> float:
    """Convert GameResult to a scalar value in [-1, +1].

    +1.0 = USSR wins, -1.0 = US wins, 0.0 = draw / DEFCON mutual destruction.
    """
    if result.winner == Side.USSR:
        return 1.0
    if result.winner == Side.US:
        return -1.0
    return 0.0


def _from_side(value: float, side: Side) -> float:
    """Flip value sign when side is US (all stats stored from USSR perspective)."""
    return value if side == Side.USSR else -value


# ---------------------------------------------------------------------------
# Flat Monte Carlo
# ---------------------------------------------------------------------------


def flat_mcts(
    gs: GameState,
    n_sim: int,
    *,
    rollout_policy: Optional[Policy] = None,
    candidate_fn=None,
    rng: Optional[RNG] = None,
) -> Optional[ActionEncoding]:
    """Run flat Monte Carlo and return the action with the highest mean value.

    For each legal action at the root:
      1. Apply the action to a clone of gs.
      2. Roll out to completion using rollout_policy (default: random).
      3. Track mean result value.

    The action with the highest value from the phasing player's perspective
    is returned.

    Returns None if the player has no legal actions.
    """
    _rng = rng or make_rng()
    side = gs.pub.phasing
    holds_china = (side == Side.USSR and gs.ussr_holds_china) or \
                  (side == Side.US and gs.us_holds_china)

    _rollout = rollout_policy or make_random_policy(_rng)

    # Sample a set of distinct legal actions to evaluate.
    if candidate_fn is not None:
        candidates = candidate_fn(gs, side, holds_china, n_sim, rng=_rng)
    else:
        candidates = _sample_candidates(gs, side, holds_china, n_sim, _rng)
    if not candidates:
        return None

    n_per_action = max(1, n_sim // len(candidates))

    best_action: Optional[ActionEncoding] = None
    best_value = float("-inf")

    for action in candidates:
        total = 0.0
        for _ in range(n_per_action):
            sim = clone_game_state(gs)
            _apply_action_to_gs(sim, action, side, _rng)
            result = play_from_state(sim, _rollout, _rollout, rng=_rng)
            total += _from_side(_result_value(result), side)
        mean = total / n_per_action
        if mean > best_value:
            best_value = mean
            best_action = action

    return best_action


# ---------------------------------------------------------------------------
# UCT
# ---------------------------------------------------------------------------


@dataclass
class _Node:
    """UCT tree node."""
    visits: int = 0
    total_value: float = 0.0   # cumulative value (USSR perspective)
    children: dict[ActionEncoding, "_Node"] = field(default_factory=dict)
    untried: list[ActionEncoding] = field(default_factory=list)
    is_terminal: bool = False
    terminal_value: float = 0.0

    @property
    def mean_value(self) -> float:
        return self.total_value / self.visits if self.visits > 0 else 0.0

    def ucb1(self, parent_visits: int, c: float, side: Side) -> float:
        if self.visits == 0:
            return float("inf")
        exploitation = _from_side(self.mean_value, side)
        exploration = c * math.sqrt(math.log(parent_visits) / self.visits)
        return exploitation + exploration


def uct_mcts(
    gs: GameState,
    n_sim: int,
    *,
    c: float = 1.41,
    rollout_policy: Optional[Policy] = None,
    candidate_fn=None,
    value_fn: Optional[Callable[[GameState], float]] = None,
    batch_value_fn: Optional[Callable[[list[GameState]], list[float]]] = None,
    rng: Optional[RNG] = None,
) -> Optional[ActionEncoding]:
    """Run UCT (Upper Confidence Trees) and return the most-visited root action.

    Args:
        gs:             Current game state (not mutated).
        n_sim:          Number of UCT simulations to run.
        c:              UCB1 exploration constant (sqrt(2) ≈ 1.41).
        rollout_policy: Policy for rollouts from leaf nodes (default: random).
        value_fn:       Optional value function for leaf evaluation. If provided,
                        replaces rollout. Takes GameState, returns value in [-1, +1]
                        from USSR perspective.
        batch_value_fn: Optional batched leaf evaluator. When provided, collects
                        the leaf GameState for each simulation and evaluates them
                        in one call after tree traversal/expansion.
        rng:            RNG for sampling.

    Returns the action with the highest visit count at the root.
    Returns None if no legal actions exist.
    """
    _rng = rng or make_rng()
    side = gs.pub.phasing
    holds_china = (side == Side.USSR and gs.ussr_holds_china) or \
                  (side == Side.US and gs.us_holds_china)

    _rollout = rollout_policy or make_random_policy(_rng)

    # Build root node with initial legal action list.
    root = _Node()
    if candidate_fn is not None:
        root.untried = candidate_fn(gs, side, holds_china, max(n_sim, 50), rng=_rng)
    else:
        root.untried = _sample_candidates(gs, side, holds_china, max(n_sim, 50), _rng)
    if not root.untried:
        return None

    pending_paths: list[list[tuple[_Node, ActionEncoding, Side]]] = []
    pending_terminal_values: list[float | None] = []
    pending_leaf_states: list[GameState] = []

    for _ in range(n_sim):
        sim = clone_game_state(gs)
        node = root
        path: list[tuple[_Node, ActionEncoding, Side]] = []
        sim_side = side

        # --- Selection ---
        while node.untried == [] and node.children and not node.is_terminal:
            action, node = _ucb1_select(node, sim_side, c)
            _apply_action_to_gs(sim, action, sim_side, _rng)
            sim_side = _next_side(sim_side)
            path.append((node, action, sim_side))

        # --- Expansion ---
        if node.untried and not node.is_terminal:
            action = _rng.choice(node.untried)
            node.untried = [a for a in node.untried if a != action]
            _apply_action_to_gs(sim, action, sim_side, _rng)
            child = _Node()
            next_side = _next_side(sim_side)
            next_holds_china = _holds_china(sim, next_side)
            if candidate_fn is not None:
                child.untried = candidate_fn(
                    sim, next_side, next_holds_china, max(n_sim // 4, 20), rng=_rng
                )
            else:
                child.untried = _sample_candidates(
                    sim, next_side, next_holds_china, max(n_sim // 4, 20), _rng
                )
            node.children[action] = child
            node = child
            sim_side = next_side
            path.append((node, action, sim_side))

        pending_paths.append(path)
        if node.is_terminal:
            pending_terminal_values.append(node.terminal_value)
        else:
            pending_terminal_values.append(None)
            pending_leaf_states.append(sim)

    leaf_values: list[float] = []
    if pending_leaf_states:
        if batch_value_fn is not None:
            leaf_values = batch_value_fn(pending_leaf_states)
            if len(leaf_values) != len(pending_leaf_states):
                raise ValueError("batch_value_fn returned wrong number of values")
        elif value_fn is not None:
            leaf_values = [value_fn(sim) for sim in pending_leaf_states]
        else:
            leaf_values = [
                _result_value(play_from_state(sim, _rollout, _rollout, rng=_rng))
                for sim in pending_leaf_states
            ]

    leaf_idx = 0
    for path, terminal_value in zip(pending_paths, pending_terminal_values, strict=True):
        if terminal_value is not None:
            value = terminal_value
        else:
            value = leaf_values[leaf_idx]
            leaf_idx += 1

        # --- Backpropagation ---
        root.visits += 1
        root.total_value += value
        for child_node, _, _ in path:
            child_node.visits += 1
            child_node.total_value += value

    if not root.children:
        # No simulations reached expansion; return any candidate.
        return root.untried[0] if root.untried else None

    # Return most-visited child.
    best = max(root.children.items(), key=lambda kv: kv[1].visits)
    return best[0]


# ---------------------------------------------------------------------------
# Interleaved UCT — N trees share one batched value call per round
# ---------------------------------------------------------------------------


def interleaved_uct_mcts(
    game_states: list[GameState],
    n_sim: int,
    batch_value_fn: Callable[[list[GameState]], list[float]],
    *,
    c: float = 1.41,
    candidate_fn=None,
    rng: Optional[RNG] = None,
) -> list[Optional[ActionEncoding]]:
    """Run N UCT trees interleaved, sharing one batched value call per round.

    For each of n_sim rounds:
      1. Every tree does one select+expand step on a clone of its game state,
         producing a leaf GameState.
      2. All non-terminal leaf states are evaluated together in one
         batch_value_fn call (batch size = N).
      3. Every tree backpropagates its leaf value.

    UCB1 is correct: each round's selection uses stats from all prior rounds.
    Batch size per value call = len(game_states), independent of n_sim.

    Args:
        game_states:    N positions to search.  Not mutated.
        n_sim:          Simulations per tree (= number of rounds).
        batch_value_fn: fn(list[GameState]) -> list[float] in [-1,+1] (USSR
                        perspective).  Called once per round with up to N states.
        c:              UCB1 exploration constant.
        candidate_fn:   Optional fn(gs, side, holds_china, n, rng) ->
                        list[ActionEncoding].  Defaults to random sampling.
        rng:            Master RNG; each tree gets a derived independent RNG so
                        results are deterministic regardless of N.

    Returns:
        list[ActionEncoding | None] — best action for each input position.
        None if that position has no legal actions.
    """
    if not game_states:
        return []

    _rng = rng or make_rng()
    N = len(game_states)

    # Derive an independent RNG per tree so simulation order doesn't matter.
    tree_rngs = [make_rng(int(_rng.integers(0, 2**32))) for _ in range(N)]

    # Compute root side / china for each tree.
    sides: list[Side] = []
    for gs in game_states:
        sides.append(gs.pub.phasing)

    # Initialise root nodes and candidate lists.
    roots: list[_Node] = []
    for i, (gs, side) in enumerate(zip(game_states, sides)):
        root = _Node()
        holds_china = _holds_china(gs, side)
        if candidate_fn is not None:
            root.untried = candidate_fn(
                gs, side, holds_china, max(n_sim, 50), rng=tree_rngs[i]
            )
        else:
            root.untried = _sample_candidates(
                gs, side, holds_china, max(n_sim, 50), tree_rngs[i]
            )
        roots.append(root)

    # ── Main loop: one simulation step per tree per round ─────────────────────
    for _ in range(n_sim):
        leaf_states: list[GameState] = []
        # For each tree: (root, path, is_terminal, terminal_value)
        backprop: list[tuple[_Node, list[tuple[_Node, ActionEncoding, Side]], bool, float]] = []

        for i, (gs, side, root, trng) in enumerate(
            zip(game_states, sides, roots, tree_rngs)
        ):
            sim = clone_game_state(gs)
            node = root
            path: list[tuple[_Node, ActionEncoding, Side]] = []
            sim_side = side

            # Selection
            while node.untried == [] and node.children and not node.is_terminal:
                action, node = _ucb1_select(node, sim_side, c)
                _apply_action_to_gs(sim, action, sim_side, trng)
                sim_side = _next_side(sim_side)
                path.append((node, action, sim_side))

            # Expansion
            if node.untried and not node.is_terminal:
                action = trng.choice(node.untried)
                node.untried = [a for a in node.untried if a != action]
                _apply_action_to_gs(sim, action, sim_side, trng)
                child = _Node()
                next_side = _next_side(sim_side)
                next_holds_china = _holds_china(sim, next_side)
                if candidate_fn is not None:
                    child.untried = candidate_fn(
                        sim, next_side, next_holds_china,
                        max(n_sim // 4, 20), rng=trng,
                    )
                else:
                    child.untried = _sample_candidates(
                        sim, next_side, next_holds_china, max(n_sim // 4, 20), trng
                    )
                node.children[action] = child
                node = child
                sim_side = next_side
                path.append((node, action, sim_side))

            if node.is_terminal:
                backprop.append((root, path, True, node.terminal_value))
            else:
                backprop.append((root, path, False, 0.0))
                leaf_states.append(sim)

        # Batch-evaluate all non-terminal leaves in one call.
        leaf_values = batch_value_fn(leaf_states) if leaf_states else []

        # Backpropagate — stats are live for the next round's UCB1 selection.
        leaf_iter = iter(leaf_values)
        for root, path, is_terminal, terminal_value in backprop:
            value = terminal_value if is_terminal else next(leaf_iter)
            root.visits += 1
            root.total_value += value
            for child_node, _, _ in path:
                child_node.visits += 1
                child_node.total_value += value

    # Return most-visited child action for each tree.
    results: list[Optional[ActionEncoding]] = []
    for root in roots:
        if not root.children:
            results.append(root.untried[0] if root.untried else None)
        else:
            best = max(root.children.items(), key=lambda kv: kv[1].visits)
            results.append(best[0])
    return results


# ---------------------------------------------------------------------------
# Self-play data collection
# ---------------------------------------------------------------------------


@dataclass
class SelfPlayStep:
    """One decision point from a self-play game."""
    pub_snapshot: PublicState      # public state before the action
    side: Side                     # acting player
    hand: frozenset[int]           # actor's actual hand
    holds_china: bool
    action: ActionEncoding         # action taken
    game_result: Optional[GameResult] = None   # filled in after game ends
    post_pub: Optional[PublicState] = None     # public state after the action (for rich logging)


def collect_self_play_game(
    n_sim: int = 50,
    *,
    use_uct: bool = True,
    c: float = 1.41,
    seed: Optional[int] = None,
) -> tuple[list[SelfPlayStep], GameResult]:
    """Play one complete game with MCTS policies and collect training steps.

    Returns (steps, result) where steps is one entry per decision point
    and result is the final game outcome.

    Args:
        n_sim:    MCTS simulations per move.
        use_uct:  Use UCT (True) or flat Monte Carlo (False).
        c:        UCB1 exploration constant (UCT only).
        seed:     RNG seed for reproducibility.
    """
    import copy
    _rng = make_rng(seed)

    from tsrl.engine.game_loop import (
        GameResult, _MID_WAR_TURN, _LATE_WAR_TURN, _MAX_TURNS,
        _run_headline_phase, _run_action_rounds, _end_of_turn,
    )
    from tsrl.engine.game_state import (
        reset, deal_cards, _ars_for_turn, advance_to_mid_war, advance_to_late_war,
    )

    # The game loop runs HERE so that _mcts_policy's closure over `gs` always
    # refers to the live, continuously-updated game state.  Using play_game()
    # would create a second `gs` in its own scope, leaving this `gs` stale and
    # causing MCTS to sample candidates against wrong state (e.g. stale DEFCON).
    gs = reset(seed=int(_rng.integers(0, 2**32)))
    steps: list[SelfPlayStep] = []
    # Holds the most recently appended step so we can fill post_pub retroactively.
    # When the policy is called for action N+1, gs.pub already reflects the result
    # of action N, so we set step[N].post_pub = gs.pub at that point.
    _pending: list[Optional[SelfPlayStep]] = [None]

    def _snapshot_pub(p: PublicState) -> PublicState:
        """Shallow copy with mutable containers deep-copied."""
        c2 = copy.copy(p)
        c2.milops = list(p.milops)
        c2.space = list(p.space)
        c2.space_attempts = list(p.space_attempts)
        c2.ops_modifier = list(p.ops_modifier)
        c2.influence = p.influence.copy()
        return c2

    # Build MCTS policy that records decisions.
    def _mcts_policy(pub: PublicState, hand: frozenset[int], holds_china: bool):
        # Retroactively fill post_pub for the previous step now that gs.pub is updated.
        if _pending[0] is not None:
            _pending[0].post_pub = _snapshot_pub(gs.pub)
            _pending[0] = None

        _side = pub.phasing
        # Clone the live gs so MCTS rollouts don't mutate it.
        _gs_snap = clone_game_state(gs)
        _gs_snap.hands[_side] = hand

        if use_uct:
            action = uct_mcts(_gs_snap, n_sim, c=c, rng=_rng)
        else:
            action = flat_mcts(_gs_snap, n_sim, rng=_rng)

        if action is None:
            action = sample_action(hand, pub, _side, holds_china=holds_china, rng=_rng)

        if action is not None:
            # During headline phase (ar == 0), game_loop forces the played card
            # to EVENT mode with no targets.  Record the mode-forced action so
            # training labels match what was actually applied.
            recorded_action = action
            if pub.ar == 0:
                recorded_action = ActionEncoding(
                    card_id=action.card_id,
                    mode=ActionMode.EVENT,
                    targets=(),
                )
            step = SelfPlayStep(
                pub_snapshot=copy.copy(pub),
                side=_side,
                hand=hand,
                holds_china=holds_china,
                action=recorded_action,
            )
            steps.append(step)
            _pending[0] = step
        return action

    # Run our own game loop (mirrors play_game logic) so `gs` stays in scope.
    result: Optional[GameResult] = None
    for turn in range(1, _MAX_TURNS + 1):
        gs.pub.turn = turn
        if turn == _MID_WAR_TURN:
            advance_to_mid_war(gs, _rng)
        elif turn == _LATE_WAR_TURN:
            advance_to_late_war(gs, _rng)
        deal_cards(gs, Side.USSR, _rng)
        deal_cards(gs, Side.US, _rng)
        result = _run_headline_phase(gs, _mcts_policy, _mcts_policy, _rng)
        if result is not None:
            break
        result = _run_action_rounds(gs, _mcts_policy, _mcts_policy, _rng, _ars_for_turn(turn))
        if result is not None:
            break
        result = _end_of_turn(gs, _rng, turn)
        if result is not None:
            break

    if result is None:
        winner: Optional[Side] = None
        if gs.pub.vp > 0:
            winner = Side.USSR
        elif gs.pub.vp < 0:
            winner = Side.US
        result = GameResult(winner, gs.pub.vp, _MAX_TURNS, "turn_limit")

    # Fill post_pub for the last step (never got a follow-up policy call).
    if _pending[0] is not None:
        _pending[0].post_pub = _snapshot_pub(gs.pub)

    # Annotate all steps with the game result.
    for step in steps:
        step.game_result = result

    return steps, result


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _sample_candidates(
    gs: GameState,
    side: Side,
    holds_china: bool,
    n: int,
    rng: RNG,
) -> list[ActionEncoding]:
    """Sample up to n distinct legal actions via factorized sampling."""
    hand = gs.hands[side]
    seen: set[ActionEncoding] = set()
    actions: list[ActionEncoding] = []
    max_attempts = n * 5
    for _ in range(max_attempts):
        if len(actions) >= n:
            break
        a = sample_action(hand, gs.pub, side, holds_china=holds_china, rng=rng)
        if a is not None and a not in seen:
            seen.add(a)
            actions.append(a)
    return actions


def _top_heuristic_candidates(
    gs: GameState,
    side: Side,
    holds_china: bool,
    n: int,
    *,
    temperature: float = 0.0,
    rng: Optional[RNG] = None,
) -> list[ActionEncoding]:
    """Return the top-n actions ranked by the MinimalHybrid heuristic.

    Uses _scored_candidate_actions from minimal_hybrid to score all plausible
    candidates. With temperature=0, returns the n best actions
    deterministically; with temperature>0, samples up to n actions without
    replacement from a softmax over heuristic scores.
    """
    from tsrl.policies.minimal_hybrid import (
        _make_decision_context,
        _scored_candidate_actions,
        _action_sort_key,
        DEFAULT_MINIMAL_HYBRID_PARAMS,
    )

    hand = gs.hands[side]
    context = _make_decision_context(gs.pub, side, DEFAULT_MINIMAL_HYBRID_PARAMS)
    scored = _scored_candidate_actions(hand, holds_china, context)

    def _key(item: tuple[ActionEncoding, float | None]) -> tuple[float, int, int, int, tuple[int, ...]]:
        action, score = item
        return _action_sort_key(action, score if score is not None else 0.0)

    scored.sort(key=_key)
    if len(scored) <= n or temperature <= 0.0:
        return [action for action, _ in scored[:n]]

    _rng = rng or make_rng()
    remaining: list[tuple[ActionEncoding, float]] = [
        (action, -_key((action, score))[0]) for action, score in scored
    ]
    sampled: list[ActionEncoding] = []

    for _ in range(min(n, len(remaining))):
        max_logit = max(logit for _, logit in remaining)
        weights = [
            math.exp((logit - max_logit) / temperature)
            for _, logit in remaining
        ]
        target = _rng.random() * sum(weights)
        cumulative = 0.0
        for idx, ((action, _), weight) in enumerate(zip(remaining, weights)):
            cumulative += weight
            if target <= cumulative or idx == len(remaining) - 1:
                sampled.append(action)
                remaining.pop(idx)
                break

    return sampled


def _apply_action_to_gs(
    gs: GameState,
    action: ActionEncoding,
    side: Side,
    rng: RNG,
) -> None:
    """Apply action to gs in-place, updating pub and hands."""
    if action.card_id in gs.hands[side]:
        gs.hands[side] = gs.hands[side] - {action.card_id}
    new_pub, _over, _winner = apply_action(gs.pub, action, side, rng=rng)
    gs.pub = new_pub
    # Sync China Card ownership.
    gs.ussr_holds_china = (gs.pub.china_held_by == Side.USSR)
    gs.us_holds_china = (gs.pub.china_held_by == Side.US)


def _next_side(side: Side) -> Side:
    return Side.US if side == Side.USSR else Side.USSR


def _holds_china(gs: GameState, side: Side) -> bool:
    return (side == Side.USSR and gs.ussr_holds_china) or \
           (side == Side.US and gs.us_holds_china)


def _ucb1_select(
    node: _Node,
    side: Side,
    c: float,
) -> tuple[ActionEncoding, "_Node"]:
    """Select the child with the highest UCB1 score."""
    best_score = float("-inf")
    best_action: Optional[ActionEncoding] = None
    best_child: Optional[_Node] = None
    for action, child in node.children.items():
        score = child.ucb1(node.visits, c, side)
        if score > best_score:
            best_score = score
            best_action = action
            best_child = child
    return best_action, best_child
