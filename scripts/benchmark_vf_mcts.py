"""Benchmark value-function MCTS against baselines.

Usage:
    uv run python scripts/benchmark_vf_mcts.py \\
        --checkpoint data/checkpoints/baseline_epoch20.pt \\
        --n-games 20 \\
        --n-sim 5

Compares:
  1. vf_mcts5 (value-function MCTS, n_sim=5) vs random
  2. vf_mcts5 vs heuristic
  3. vf_mcts20 vs heuristic
  4. Prints wall-time per move for profiling
"""
from __future__ import annotations

import argparse
import os
import queue
import random
import sys
import threading
import time
from dataclasses import dataclass
from typing import Optional

sys.path.insert(0, os.path.dirname(__file__))
from collect_learned_vs_heuristic import BarrierBatcher

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "python"))

import torch

from tsrl.engine.game_loop import GameResult, Policy, make_random_policy, play_game
from tsrl.engine.mcts import uct_mcts
from tsrl.policies.learned_policy import (
    _build_action_from_country_logits,
    _build_random_targets,
    _extract_features,
    make_learned_policy,
)
from tsrl.policies.model import TSBaselineModel
from tsrl.policies.minimal_hybrid import make_minimal_hybrid_policy
from tsrl.schemas import ActionEncoding, ActionMode, Side


@dataclass
class BenchmarkResult:
    """Result of a matchup: policy_a vs policy_b.

    policy_a_wins / policy_b_wins track wins by the policy (not by side).
    Games alternate: even games policy_a plays USSR, odd games policy_a plays US.
    """

    name: str  # "vf_mcts5 vs random", etc.
    games: int
    policy_a_wins: int
    policy_b_wins: int
    draws: int
    avg_wall_time_per_move: float  # seconds

    @property
    def a_winrate(self) -> float:
        return self.policy_a_wins / max(1, self.games - self.draws)

    @property
    def b_winrate(self) -> float:
        return self.policy_b_wins / max(1, self.games - self.draws)

    @property
    def draw_rate(self) -> float:
        return self.draws / max(1, self.games)

    def __str__(self) -> str:
        decisive = self.games - self.draws
        a_name, b_name = self.name.split(" vs ", 1) if " vs " in self.name else ("A", "B")
        return (
            f"{self.name:35s} "
            f"  {a_name[:12]:12s} {self.policy_a_wins:3d}/{decisive:3d} ({100*self.a_winrate:5.1f}%)  "
            f"{b_name[:12]:12s} {self.policy_b_wins:3d}/{decisive:3d} ({100*self.b_winrate:5.1f}%)  "
            f"Draw {self.draws:2d}/{self.games}  "
            f"Time {self.avg_wall_time_per_move*1000:.1f}ms/move"
        )


_VF_SIDE: Side = Side.USSR
_VF_OPPONENT_POLICY: Optional[Policy] = None
_THREAD_LOCAL = threading.local()


def _load_model(checkpoint_path: str):
    if not os.path.exists(checkpoint_path):
        raise FileNotFoundError(checkpoint_path)

    checkpoint = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
    state_dict = checkpoint.get("model_state_dict", checkpoint)
    ckpt_args = checkpoint.get("args", {})
    hidden_dim = ckpt_args.get("hidden_dim", 256)
    model = TSBaselineModel(hidden_dim=hidden_dim)
    model.load_state_dict(state_dict, strict=False)
    expected_influence_dim = model.influence_encoder.in_features
    has_strategy_heads = all(
        key in state_dict
        for key in (
            "strategy_heads.weight",
            "strategy_heads.bias",
            "strategy_mixer.weight",
            "strategy_mixer.bias",
        )
    )
    model.eval()
    try:
        model = torch.compile(model, dynamic=True)
    except Exception:
        pass
    return model, has_strategy_heads, expected_influence_dim


def _normalize_influence_features(
    influence: torch.Tensor,
    expected_dim: int,
) -> torch.Tensor:
    actual_dim = int(influence.shape[1])
    if actual_dim == expected_dim:
        return influence
    if actual_dim == expected_dim + 2 and expected_dim % 2 == 0:
        half = actual_dim // 2
        return torch.cat([influence[:, 1:half], influence[:, half + 1 :]], dim=1)
    if actual_dim > expected_dim:
        return influence[:, :expected_dim]
    pad = torch.zeros(
        (influence.shape[0], expected_dim - actual_dim),
        dtype=influence.dtype,
        device=influence.device,
    )
    return torch.cat([influence, pad], dim=1)


def _get_thread_slot_id() -> int:
    slot_id = getattr(_THREAD_LOCAL, "slot_id", None)
    if slot_id is None:
        raise RuntimeError("thread slot_id not configured")
    return slot_id


def _make_batched_value_fn(
    batcher: BarrierBatcher,
    expected_influence_dim: int,
):
    def _value_fn(gs) -> float:
        pub = gs.pub
        side = pub.phasing
        holds_china = (side == Side.USSR and gs.ussr_holds_china) or (
            side == Side.US and gs.us_holds_china
        )
        hand = gs.hands[side]
        influence, cards, scalars = _extract_features(pub, hand, holds_china, side)
        influence = _normalize_influence_features(influence, expected_influence_dim)
        outputs = batcher.request(_get_thread_slot_id(), influence, cards, scalars)
        return outputs["value"][0, 0].item()

    return _value_fn


def _make_batched_candidate_fn(
    batcher: BarrierBatcher,
    expected_influence_dim: int,
    *,
    n_candidates: int,
    has_strategy_heads: bool,
):
    from tsrl.engine.legal_actions import legal_cards, legal_modes, load_adjacency

    adj = load_adjacency()

    def _candidate_fn(
        gs,
        side: Side,
        holds_china: bool,
        n: int,
        *,
        rng: random.Random | None = None,
    ) -> list[ActionEncoding]:
        hand = gs.hands[side]
        pub = gs.pub
        playable = sorted(legal_cards(hand, pub, side, holds_china=holds_china))
        if not playable:
            return []

        influence, cards, scalars = _extract_features(pub, hand, holds_china, side)
        influence = _normalize_influence_features(influence, expected_influence_dim)
        outputs = batcher.request(_get_thread_slot_id(), influence, cards, scalars)
        card_logits = outputs["card_logits"][0]
        mode_logits = outputs["mode_logits"][0]
        country_logits = outputs.get("country_logits")
        if country_logits is not None:
            country_logits = country_logits[0]
        strategy_logits = outputs.get("strategy_logits")
        if strategy_logits is not None:
            strategy_logits = strategy_logits[0]
        country_strategy_logits = outputs.get("country_strategy_logits")
        if country_strategy_logits is not None:
            country_strategy_logits = country_strategy_logits[0]

        card_probs = torch.softmax(card_logits, dim=0)
        mode_probs = torch.softmax(mode_logits, dim=0)

        scored_pairs: list[tuple[int, ActionMode, float]] = []
        for card_id in playable:
            card_score = float(card_probs[card_id - 1].item())
            modes = sorted(legal_modes(card_id, pub, side, adj=adj), key=int)
            for mode in modes:
                scored_pairs.append((card_id, mode, card_score * float(mode_probs[int(mode)].item())))

        if not scored_pairs:
            return []

        limit = min(n, n_candidates, len(scored_pairs))
        if limit <= 0:
            return []

        scored_pairs.sort(key=lambda item: (-item[2], item[0], int(item[1])))
        selected_pairs = [(card_id, mode) for card_id, mode, _ in scored_pairs[:limit]]

        _rng = rng or random.Random()
        actions: list[ActionEncoding] = []
        for card_id, mode in selected_pairs:
            if mode in (ActionMode.SPACE, ActionMode.EVENT):
                actions.append(ActionEncoding(card_id=card_id, mode=mode, targets=()))
                continue

            action = None
            if has_strategy_heads and country_logits is not None:
                action = _build_action_from_country_logits(
                    card_id,
                    mode,
                    country_logits,
                    pub,
                    side,
                    adj,
                    _rng,
                    strategy_logits=strategy_logits,
                    country_strategy_logits=country_strategy_logits,
                )
            if action is None:
                action = _build_random_targets(card_id, mode, pub, side, adj, _rng)
            if action is not None:
                actions.append(action)
        return actions

    return _candidate_fn


def play_game_with_vf_uct(
    value_fn,
    n_sim: int,
    seed: int,
    candidate_fn=None,
) -> GameResult:
    """Play one game with value-function UCT on one side over the live GameState."""
    from tsrl.engine.game_loop import (
        _MID_WAR_TURN,
        _LATE_WAR_TURN,
        _MAX_TURNS,
        _end_of_turn,
        _run_action_rounds,
        _run_extra_ar,
        _run_headline_phase,
    )
    from tsrl.engine.game_state import (
        _ars_for_turn,
        advance_to_late_war,
        advance_to_mid_war,
        clone_game_state,
        deal_cards,
        reset,
    )
    from tsrl.engine.legal_actions import sample_action

    thread_vf_side = getattr(_THREAD_LOCAL, "vf_side", _VF_SIDE)
    thread_opp_policy = getattr(_THREAD_LOCAL, "opponent_policy", _VF_OPPONENT_POLICY)
    if thread_opp_policy is None:
        raise RuntimeError("opponent policy not configured")

    rng = random.Random(seed)
    gs = reset(seed=rng.randint(0, 2**32))

    def _vf_policy(pub, hand, holds_china):
        side = pub.phasing
        if side != thread_vf_side:
            return thread_opp_policy(pub, hand, holds_china)

        gs_snap = clone_game_state(gs)
        gs_snap.hands[side] = hand
        action = uct_mcts(
            gs_snap, n_sim,
            value_fn=value_fn,
            candidate_fn=candidate_fn,
            rng=rng,
        )
        if action is None:
            action = sample_action(hand, pub, side, holds_china=holds_china, rng=rng)
        return action

    result: Optional[GameResult] = None
    for turn in range(1, _MAX_TURNS + 1):
        gs.pub.turn = turn
        if turn == _MID_WAR_TURN:
            advance_to_mid_war(gs, rng)
        elif turn == _LATE_WAR_TURN:
            advance_to_late_war(gs, rng)

        deal_cards(gs, Side.USSR, rng)
        deal_cards(gs, Side.US, rng)

        result = _run_headline_phase(gs, _vf_policy, _vf_policy, rng)
        if result is not None:
            break

        result = _run_action_rounds(gs, _vf_policy, _vf_policy, rng, _ars_for_turn(turn))
        if result is not None:
            break

        if gs.pub.north_sea_oil_extra_ar:
            gs.pub.north_sea_oil_extra_ar = False
            result = _run_extra_ar(gs, Side.US, _vf_policy, rng)
            if result is not None:
                break

        if gs.pub.glasnost_extra_ar:
            gs.pub.glasnost_extra_ar = False
            result = _run_extra_ar(gs, Side.USSR, _vf_policy, rng)
            if result is not None:
                break

        result = _end_of_turn(gs, rng, turn)
        if result is not None:
            break

    if result is None:
        winner: Optional[Side] = None
        if gs.pub.vp > 0:
            winner = Side.USSR
        elif gs.pub.vp < 0:
            winner = Side.US
        result = GameResult(winner, gs.pub.vp, _MAX_TURNS, "turn_limit")

    return result


def run_matchup(
    name: str,
    policy_a: Policy,
    policy_b: Policy,
    n_games: int,
    seed: int,
    *,
    vf_value_fn=None,
    vf_n_sim: int = 0,
    vf_candidate_fn=None,
    pool_size: int = 32,
) -> BenchmarkResult:
    """Play n_games between policy_a and policy_b, alternating sides.

    policy_a plays USSR on even games and US on odd games.
    Wins are tracked by policy (not side) so results are unbiased by TS's side asymmetry.
    """
    a_wins = b_wins = draws = 0
    total_time = 0.0
    move_count = 0

    if vf_value_fn is None:
        for game_idx in range(n_games):
            a_is_ussr = (game_idx % 2 == 0)
            if a_is_ussr:
                ussr_pol, us_pol = policy_a, policy_b
            else:
                ussr_pol, us_pol = policy_b, policy_a

            t0 = time.time()
            result = play_game(ussr_pol, us_pol, seed=seed + game_idx)
            t1 = time.time()
            total_time += t1 - t0

            a_side = Side.USSR if a_is_ussr else Side.US
            if result.winner is None:
                draws += 1
            elif result.winner == a_side:
                a_wins += 1
            else:
                b_wins += 1

            move_count += 100  # rough estimate

            if (game_idx + 1) % 5 == 0 or game_idx == 0:
                elapsed = t1 - t0
                print(
                    f"  [{name}] game {game_idx+1}/{n_games}"
                    f"  a_wins={a_wins} b_wins={b_wins} draws={draws}"
                    f"  game_time={elapsed:.1f}s"
                )
    else:
        model, has_strategy_heads, expected_influence_dim = vf_value_fn
        active_slots = min(pool_size, n_games)
        device = next(model.parameters()).device
        batcher = BarrierBatcher(model, n_slots=active_slots, device=device)
        batcher.set_active_slots(active_slots)
        batched_value_fn = _make_batched_value_fn(batcher, expected_influence_dim)
        batched_candidate_fn = None
        if vf_candidate_fn is not None:
            batched_candidate_fn = _make_batched_candidate_fn(
                batcher,
                expected_influence_dim,
                n_candidates=vf_candidate_fn,
                has_strategy_heads=has_strategy_heads,
            )

        results_q: queue.Queue[tuple[int, GameResult, float]] = queue.Queue()
        counter_lock = threading.Lock()
        next_game_idx = [0]

        def _worker(slot_id: int) -> None:
            _THREAD_LOCAL.slot_id = slot_id
            try:
                while True:
                    with counter_lock:
                        if next_game_idx[0] >= n_games:
                            return
                        game_idx = next_game_idx[0]
                        next_game_idx[0] += 1

                    a_is_ussr = (game_idx % 2 == 0)
                    if a_is_ussr:
                        ussr_pol, us_pol = policy_a, policy_b
                    else:
                        ussr_pol, us_pol = policy_b, policy_a

                    global _VF_SIDE, _VF_OPPONENT_POLICY
                    _VF_SIDE = Side.USSR if a_is_ussr else Side.US
                    _VF_OPPONENT_POLICY = us_pol if _VF_SIDE == Side.USSR else ussr_pol
                    _THREAD_LOCAL.vf_side = _VF_SIDE
                    _THREAD_LOCAL.opponent_policy = _VF_OPPONENT_POLICY

                    t0 = time.time()
                    result = play_game_with_vf_uct(
                        batched_value_fn,
                        vf_n_sim,
                        seed + game_idx,
                        candidate_fn=batched_candidate_fn,
                    )
                    results_q.put((game_idx, result, time.time() - t0))
            finally:
                batcher.deactivate_slot(slot_id)

        threads = [
            threading.Thread(target=_worker, args=(slot_id,), daemon=True)
            for slot_id in range(active_slots)
        ]
        for thread in threads:
            thread.start()
        try:
            completed = 0
            while completed < n_games:
                game_idx, result, elapsed = results_q.get()
                completed += 1
                total_time += elapsed

                a_is_ussr = (game_idx % 2 == 0)
                a_side = Side.USSR if a_is_ussr else Side.US
                if result.winner is None:
                    draws += 1
                elif result.winner == a_side:
                    a_wins += 1
                else:
                    b_wins += 1

                move_count += 100  # rough estimate

                if (completed % 5 == 0) or game_idx == 0:
                    print(
                        f"  [{name}] game {completed}/{n_games}"
                        f"  a_wins={a_wins} b_wins={b_wins} draws={draws}"
                        f"  game_time={elapsed:.1f}s"
                    )
        finally:
            for thread in threads:
                thread.join()

    avg_time = total_time / max(1, move_count)
    return BenchmarkResult(
        name=name,
        games=n_games,
        policy_a_wins=a_wins,
        policy_b_wins=b_wins,
        draws=draws,
        avg_wall_time_per_move=avg_time,
    )


def main():
    import sys as _sys
    _sys.stdout.reconfigure(line_buffering=True)

    p = argparse.ArgumentParser(
        description="Benchmark value-function MCTS against baselines."
    )
    p.add_argument(
        "--checkpoint",
        required=True,
        help="Path to learned policy checkpoint (.pt)",
    )
    p.add_argument("--n-games", type=int, default=20, help="Games per matchup")
    p.add_argument("--n-sim", type=int, default=5, help="MCTS simulations per move")
    p.add_argument("--seed", type=int, default=42, help="RNG seed")
    p.add_argument(
        "--pool-size", type=int, default=32,
        help="Concurrent game threads / inference slots (default: 32)"
    )
    p.add_argument(
        "--n-candidates", type=int, default=0,
        help="If >0, use model candidate fn with this many candidates (model-guided MCTS)"
    )
    args = p.parse_args()

    if not os.path.exists(args.checkpoint):
        print(f"ERROR: checkpoint not found: {args.checkpoint}")
        sys.exit(1)

    print(f"Loading checkpoint: {args.checkpoint}")
    print(f"Games per matchup: {args.n_games}")
    print(f"MCTS simulations: {args.n_sim}\n")

    # Make policies
    random_pol = make_random_policy(random.Random(args.seed))
    heuristic_pol = make_minimal_hybrid_policy()

    try:
        value_fn = _load_model(args.checkpoint)
        print(f"✓ Value function loaded")
    except Exception as e:
        print(f"ERROR loading value function: {e}")
        sys.exit(1)

    candidate_fn = None
    if args.n_candidates > 0:
        try:
            candidate_fn = args.n_candidates
            print(f"✓ Model candidate fn loaded (n_candidates={args.n_candidates})")
        except Exception as e:
            print(f"ERROR loading candidate fn: {e}")
            sys.exit(1)
    print()

    # Run benchmarks
    print("=" * 120)
    print(f"BENCHMARK RESULTS (n_games={args.n_games}, n_sim={args.n_sim})")
    print("=" * 120)

    results = []

    # 1. Random vs Random (baseline)
    print("\n1. Baseline: random vs random")
    r = run_matchup("random vs random", random_pol, random_pol, args.n_games, args.seed)
    results.append(r)
    print(f"   {r}")

    # 2. Heuristic vs Random
    print("\n2. Heuristic vs random")
    r = run_matchup(
        "heuristic vs random", heuristic_pol, random_pol, args.n_games, args.seed + 100
    )
    results.append(r)
    print(f"   {r}")

    # 3. vf_mcts vs random
    n_sim = args.n_sim
    tag = f"vf_mcts{n_sim}"
    print(f"\n3. {tag} vs random")
    r = run_matchup(
        f"{tag} vs random",
        random_pol,
        random_pol,
        args.n_games,
        args.seed + 200,
        vf_value_fn=value_fn,
        vf_n_sim=n_sim,
        vf_candidate_fn=candidate_fn,
        pool_size=args.pool_size,
    )
    results.append(r)
    print(f"   {r}")

    # 4. vf_mcts vs heuristic
    print(f"\n4. {tag} vs heuristic")
    r = run_matchup(
        f"{tag} vs heuristic",
        heuristic_pol,
        heuristic_pol,
        args.n_games,
        args.seed + 300,
        vf_value_fn=value_fn,
        vf_n_sim=n_sim,
        vf_candidate_fn=candidate_fn,
        pool_size=args.pool_size,
    )
    results.append(r)
    print(f"   {r}")

    # 5. learned policy (no MCTS) vs heuristic — direct policy comparison
    if candidate_fn is not None:
        print(f"\n5. learned_policy(USSR) vs heuristic")
        learned_ussr = make_learned_policy(args.checkpoint, Side.USSR)
        learned_us = make_learned_policy(args.checkpoint, Side.US)
        r = run_matchup(
            "learned vs heuristic",
            learned_ussr,
            heuristic_pol,
            args.n_games,
            args.seed + 400,
        )
        results.append(r)
        print(f"   {r}")


if __name__ == "__main__":
    main()
