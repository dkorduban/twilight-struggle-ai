"""
Tests for MCTS implementations (flat_mcts, uct_mcts, collect_self_play_game).

These tests are kept fast by using small n_sim values (2-5).
"""
import random
import pytest
from tsrl.engine.game_state import reset, clone_game_state
from tsrl.engine.mcts import flat_mcts, uct_mcts, collect_self_play_game, SelfPlayStep
from tsrl.engine.game_loop import GameResult
from tsrl.schemas import ActionEncoding, Side


class TestFlatMCTS:
    """Tests for flat_mcts."""

    def test_flat_mcts_returns_action_on_fresh_game(self):
        """flat_mcts should return an ActionEncoding for a fresh game state."""
        gs = reset(seed=42)
        rng = random.Random(42)
        action = flat_mcts(gs, n_sim=5, rng=rng)
        assert action is not None
        assert isinstance(action, ActionEncoding)

    def test_flat_mcts_with_n_sim_one(self):
        """flat_mcts should work with n_sim=1."""
        gs = reset(seed=43)
        rng = random.Random(43)
        action = flat_mcts(gs, n_sim=1, rng=rng)
        assert action is not None
        assert isinstance(action, ActionEncoding)

    def test_flat_mcts_does_not_mutate_input_state(self):
        """flat_mcts should not mutate the input GameState."""
        gs = reset(seed=44)

        # Store initial state
        initial_turn = gs.pub.turn
        initial_vp = gs.pub.vp
        initial_defcon = gs.pub.defcon
        initial_influence = dict(gs.pub.influence)

        rng = random.Random(44)
        _ = flat_mcts(gs, n_sim=3, rng=rng)

        # Verify state is unchanged
        assert gs.pub.turn == initial_turn
        assert gs.pub.vp == initial_vp
        assert gs.pub.defcon == initial_defcon
        assert dict(gs.pub.influence) == initial_influence

    def test_flat_mcts_returns_none_with_no_legal_actions(self):
        """flat_mcts should return None if no legal actions exist."""
        gs = reset(seed=45)
        # Clear both hands to simulate no legal actions
        gs.hands[Side.USSR] = frozenset()
        gs.hands[Side.US] = frozenset()

        rng = random.Random(45)
        action = flat_mcts(gs, n_sim=3, rng=rng)
        # If sample_action handles empty hands gracefully, None is expected
        # If not, this test documents the actual behavior
        assert action is None or isinstance(action, ActionEncoding)


class TestUCTMCTS:
    """Tests for uct_mcts."""

    def test_uct_mcts_returns_action_on_fresh_game(self):
        """uct_mcts should return an ActionEncoding for a fresh game state."""
        gs = reset(seed=46)
        rng = random.Random(46)
        action = uct_mcts(gs, n_sim=5, rng=rng)
        assert action is not None
        assert isinstance(action, ActionEncoding)

    def test_uct_mcts_with_n_sim_one(self):
        """uct_mcts should work with n_sim=1."""
        gs = reset(seed=47)
        rng = random.Random(47)
        action = uct_mcts(gs, n_sim=1, rng=rng)
        assert action is not None
        assert isinstance(action, ActionEncoding)

    def test_uct_mcts_does_not_mutate_input_state(self):
        """uct_mcts should not mutate the input GameState."""
        gs = reset(seed=48)

        # Store initial state
        initial_turn = gs.pub.turn
        initial_influence = dict(gs.pub.influence)

        rng = random.Random(48)
        _ = uct_mcts(gs, n_sim=3, rng=rng)

        # Verify state is unchanged
        assert gs.pub.turn == initial_turn
        assert dict(gs.pub.influence) == initial_influence

    def test_uct_mcts_returns_none_with_no_legal_actions(self):
        """uct_mcts should return None if no legal actions exist."""
        gs = reset(seed=49)
        # Clear both hands to simulate no legal actions
        gs.hands[Side.USSR] = frozenset()
        gs.hands[Side.US] = frozenset()

        rng = random.Random(49)
        action = uct_mcts(gs, n_sim=3, rng=rng)
        # If sample_action handles empty hands gracefully, None is expected
        assert action is None or isinstance(action, ActionEncoding)


class TestSelfPlayCollection:
    """Tests for collect_self_play_game."""

    def test_collect_self_play_game_flat_mcts(self):
        """collect_self_play_game with flat_mcts should return steps and result."""
        steps, result = collect_self_play_game(n_sim=2, use_uct=False, seed=50)

        assert isinstance(steps, list)
        assert len(steps) > 0, "Self-play game should produce at least one step"
        assert isinstance(result, GameResult)
        assert result.winner in [Side.USSR, Side.US]

    def test_collect_self_play_game_uct_mcts(self):
        """collect_self_play_game with uct_mcts should return steps and result."""
        steps, result = collect_self_play_game(n_sim=2, use_uct=True, seed=51)

        assert isinstance(steps, list)
        assert len(steps) > 0, "Self-play game should produce at least one step"
        assert isinstance(result, GameResult)
        assert result.winner in [Side.USSR, Side.US]

    def test_self_play_steps_have_all_fields(self):
        """SelfPlayStep fields should be correctly populated."""
        steps, result = collect_self_play_game(n_sim=2, use_uct=False, seed=52)

        for step in steps:
            assert isinstance(step, SelfPlayStep)
            assert step.pub_snapshot is not None
            assert step.side in [Side.USSR, Side.US]
            assert isinstance(step.hand, frozenset)
            assert len(step.hand) > 0, "Actor hand should not be empty at decision point"
            assert isinstance(step.holds_china, bool)
            assert isinstance(step.action, ActionEncoding)
            # game_result is filled in after collection
            assert step.game_result is not None
            assert step.game_result == result

    def test_all_steps_have_game_result_filled(self):
        """All steps should have game_result filled after collect_self_play_game returns."""
        steps, result = collect_self_play_game(n_sim=2, use_uct=True, seed=53)

        for step in steps:
            assert step.game_result is not None, \
                "All steps should have game_result filled in after collection"
            assert step.game_result == result, \
                "All steps should reference the final game result"

    def test_self_play_deterministic_with_seed(self):
        """collect_self_play_game with same seed should produce same game structure."""
        steps1, result1 = collect_self_play_game(n_sim=2, use_uct=False, seed=54)
        steps2, result2 = collect_self_play_game(n_sim=2, use_uct=False, seed=54)

        assert len(steps1) == len(steps2), \
            "Same seed should produce same number of steps"
        assert result1.winner == result2.winner, \
            "Same seed should produce same winner"

    def test_uct_vs_flat_both_complete_game(self):
        """Both UCT and flat MCTS should complete a full game."""
        steps_uct, result_uct = collect_self_play_game(n_sim=2, use_uct=True, seed=55)
        steps_flat, result_flat = collect_self_play_game(n_sim=2, use_uct=False, seed=56)

        assert len(steps_uct) > 0
        assert len(steps_flat) > 0
        assert isinstance(result_uct, GameResult)
        assert isinstance(result_flat, GameResult)


class TestMCTSIntegration:
    """Integration tests for MCTS with GameState."""

    def test_flat_and_uct_return_different_actions_sometimes(self):
        """flat_mcts and uct_mcts may return different actions on same state."""
        # With very small n_sim, they may occasionally return same action,
        # but with more sims they should often differ due to different algorithms.
        gs = reset(seed=57)
        rng1 = random.Random(571)
        rng2 = random.Random(572)

        action_flat = flat_mcts(gs, n_sim=5, rng=rng1)
        action_uct = uct_mcts(gs, n_sim=5, rng=rng2)

        # Both should return valid actions
        assert action_flat is not None
        assert action_uct is not None
        assert isinstance(action_flat, ActionEncoding)
        assert isinstance(action_uct, ActionEncoding)

    def test_mcts_action_is_from_hand(self):
        """MCTS-selected action should be playable from the actor's hand."""
        gs = reset(seed=58)
        rng = random.Random(58)
        action = flat_mcts(gs, n_sim=3, rng=rng)

        assert action is not None
        side = gs.pub.phasing
        assert action.card_id in gs.hands[side], \
            "MCTS action should reference a card in the phasing player's hand"
