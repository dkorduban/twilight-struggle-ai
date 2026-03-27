"""
Self-play data collector for Twilight Struggle AI.

Collects games using MCTS (UCT or flat MC) and converts each decision point
into a row dict compatible with the replay-based Parquet schema.

Feature columns match python/tsrl/etl/dataset.py exactly.  Self-play adds:
  game_id        str    unique game identifier
  step_idx       int    decision index within the game
  game_result    str    'ussr_win' | 'us_win' | 'draw'
  winner_side    int    +1=USSR, -1=US, 0=draw  (value training target)
  final_vp       int    final VP score at game end
  end_turn       int    turn on which the game ended
  end_reason     str    'vp_threshold' | 'defcon1' | 'turn_limit' | 'europe_control'

Action encoding columns (instead of legacy card_id / country_id / action_kind):
  action_card_id  int   card played
  action_mode     int   ActionMode int value
  action_targets  str   comma-separated country IDs, or empty string

Offline-label columns are populated with known-good values because self-play
provides perfect information:
  lbl_actor_hand          exact hand mask (quality EXACT)
  lbl_step_quality        0  (EXACT)
  lbl_card_quality        per-card quality mask, all 0 for held cards
  lbl_opponent_possible   not computed here; sentinel zeros mask

WARNING: lbl_opponent_possible is a zero mask in self-play rows.  Do not use
it as a training target without filling it from a proper smoother pass.
"""
from __future__ import annotations

import logging

from tsrl.engine.game_loop import GameResult
from tsrl.engine.mcts import SelfPlayStep, collect_self_play_game
from tsrl.etl.dataset import (
    MAX_CARD_ID,
    MAX_COUNTRY_ID,
    _CARD_MASK_LEN,
    _COUNTRY_MASK_LEN,
    _card_mask,
    _influence_array,
)
from tsrl.schemas import PublicState, Side

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Value encoding
# ---------------------------------------------------------------------------

_GAME_RESULT_STR: dict[int | None, str] = {
    Side.USSR: "ussr_win",
    Side.US: "us_win",
    None: "draw",
}

_WINNER_SIDE_INT: dict[int | None, int] = {
    Side.USSR: 1,
    Side.US: -1,
    None: 0,
}


def _encode_result(result: GameResult) -> tuple[str, int]:
    """Return (game_result_str, winner_side_int)."""
    winner = result.winner  # Side enum or None
    return _GAME_RESULT_STR[winner], _WINNER_SIDE_INT[winner]


# ---------------------------------------------------------------------------
# Row builder
# ---------------------------------------------------------------------------


def _step_to_row(
    step: SelfPlayStep,
    game_id: str,
    step_idx: int,
) -> dict:
    """Convert one SelfPlayStep to a flat row dict."""
    pub: PublicState = step.pub_snapshot
    side: Side = step.side
    opp: Side = Side.US if side == Side.USSR else Side.USSR

    assert step.game_result is not None, "game_result must be set before row extraction"

    game_result_str, winner_side = _encode_result(step.game_result)

    # Actor hand — perfect info in self-play.
    actor_hand_mask = _card_mask(step.hand)

    # Card quality: EXACT (0) for every held card, UNKNOWN (3) elsewhere.
    cq = [3] * _CARD_MASK_LEN
    for cid in step.hand:
        if 0 < cid < _CARD_MASK_LEN:
            cq[cid] = 0  # LabelQuality.EXACT

    # Influence arrays.
    ussr_inf = _influence_array(pub, Side.USSR)
    us_inf = _influence_array(pub, Side.US)

    # Action fields.
    targets_str = ",".join(str(t) for t in step.action.targets)

    # Known-in-hand from actor perspective: full hand visible in self-play.
    actor_known_in = actor_hand_mask
    # known_not_in: everything not in hand and not possibly drawn is excluded;
    # use discard + removed as hard exclusions.
    actor_known_not_in = _card_mask(pub.discard | pub.removed)
    # possible_hidden: since we have full info, possible == actual hand.
    actor_possible = actor_hand_mask

    # Opponent hand: unknown from actor's perspective (no inference done here).
    # Use zeros for known_in; known_not_in = actor's hand + discard + removed.
    opp_known_in_mask = [0] * _CARD_MASK_LEN
    opp_known_not_in_mask = _card_mask(step.hand | pub.discard | pub.removed)
    opp_possible_mask = [0] * _CARD_MASK_LEN  # not computed

    # Hand size (excluding China Card, id=6).
    actor_hand_size = sum(1 for c in step.hand if c != 6)
    actor_holds_china = step.holds_china

    # Opponent hand size: not tracked in SelfPlayStep; use 0 as sentinel.
    opp_hand_size = 0
    opp_holds_china = not step.holds_china if pub.china_held_by != Side.NEUTRAL else False

    return {
        # --- Identity ---
        "game_id": game_id,
        "step_idx": step_idx,
        # --- Decision context ---
        "turn": pub.turn,
        "ar": pub.ar,
        "phasing": int(side),
        # action_kind is not set for self-play rows (use -1 sentinel).
        "action_kind": -1,
        # Legacy card_id / country_id: use action fields instead (sentinel -1).
        "card_id": step.action.card_id,
        "country_id": step.action.targets[0] if step.action.targets else -1,
        # --- Action encoding ---
        "action_card_id": step.action.card_id,
        "action_mode": int(step.action.mode),
        "action_targets": targets_str,
        # --- Global state ---
        "vp": pub.vp,
        "defcon": pub.defcon,
        "milops_ussr": pub.milops[Side.USSR],
        "milops_us": pub.milops[Side.US],
        "space_ussr": pub.space[Side.USSR],
        "space_us": pub.space[Side.US],
        "china_held_by": int(pub.china_held_by),
        "china_playable": pub.china_playable,
        # --- Influence ---
        "ussr_influence": ussr_inf,
        "us_influence": us_inf,
        # --- Card set masks ---
        "discard_mask": _card_mask(pub.discard),
        "removed_mask": _card_mask(pub.removed),
        # --- Actor hand knowledge ---
        "actor_known_in": actor_known_in,
        "actor_known_not_in": actor_known_not_in,
        "actor_possible": actor_possible,
        "actor_hand_size": actor_hand_size,
        "actor_holds_china": actor_holds_china,
        # --- Opponent hand knowledge ---
        "opp_known_in": opp_known_in_mask,
        "opp_known_not_in": opp_known_not_in_mask,
        "opp_possible": opp_possible_mask,
        "opp_hand_size": opp_hand_size,
        "opp_holds_china": opp_holds_china,
        # --- Offline labels (perfect info in self-play) ---
        "lbl_actor_hand": actor_hand_mask,
        "lbl_step_quality": 0,          # LabelQuality.EXACT
        "lbl_card_quality": cq,
        "lbl_opponent_possible": [0] * _CARD_MASK_LEN,  # not computed; sentinel
        # --- Self-play outcome columns ---
        "game_result": game_result_str,
        "winner_side": winner_side,
        "final_vp": step.game_result.final_vp,
        "end_turn": step.game_result.end_turn,
        "end_reason": step.game_result.end_reason,
    }


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

# Required columns that every self-play row must contain.
REQUIRED_COLUMNS: frozenset[str] = frozenset({
    "game_id",
    "step_idx",
    "turn",
    "ar",
    "phasing",
    "vp",
    "defcon",
    "ussr_influence",
    "us_influence",
    "discard_mask",
    "removed_mask",
    "actor_known_in",
    "actor_hand_size",
    "actor_holds_china",
    "lbl_actor_hand",
    "lbl_step_quality",
    "action_card_id",
    "action_mode",
    "action_targets",
    "game_result",
    "winner_side",
    "final_vp",
    "end_turn",
    "end_reason",
})


def collect_games(
    n_games: int,
    n_sim: int,
    base_seed: int,
    use_uct: bool = True,
) -> list[dict]:
    """Collect n_games self-play games and return a list of row dicts.

    Each row corresponds to one decision point.  Rows from different games
    have unique game_id values.

    Args:
        n_games:    Number of complete games to play.
        n_sim:      MCTS simulations per move.
        base_seed:  Base RNG seed.  Game i uses seed base_seed + i for
                    reproducibility.
        use_uct:    Use UCT (True) or flat Monte Carlo (False).

    Returns:
        List of row dicts, one per decision point across all games.
    """
    all_rows: list[dict] = []

    for game_idx in range(n_games):
        game_seed = base_seed + game_idx
        game_id = f"selfplay_{base_seed}_{game_idx:04d}"

        try:
            steps, result = collect_self_play_game(
                n_sim=n_sim,
                use_uct=use_uct,
                seed=game_seed,
            )
        except Exception as exc:
            log.warning("game %s failed: %s", game_id, exc)
            continue

        for step_idx, step in enumerate(steps):
            try:
                row = _step_to_row(step, game_id, step_idx)
                all_rows.append(row)
            except Exception as exc:
                log.warning("game %s step %d row build failed: %s", game_id, step_idx, exc)

        log.info("game %-30s  steps=%d  result=%s  vp=%d",
                 game_id, len(steps), _GAME_RESULT_STR[result.winner], result.final_vp)

    return all_rows
