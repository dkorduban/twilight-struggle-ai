"""
cpp_rollout.py — fast C++ leaf evaluation for MCTS rollouts.

Provides cpp_rollout_value(gs, rng_seed) -> float which serializes a Python
GameState into the dict format expected by tscore.play_from_public_state and
runs a MinimalHybrid vs MinimalHybrid heuristic game to terminal in C++.

Fallback: if tscore is not importable, returns 0.0 with a one-time warning.
"""
from __future__ import annotations

import warnings
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tsrl.engine.game_state import GameState

# ---------------------------------------------------------------------------
# Import tscore (may fail in test / CPU-only environments)
# ---------------------------------------------------------------------------

_tscore = None
_import_warned = False


def _get_tscore():
    global _tscore, _import_warned
    if _tscore is not None:
        return _tscore
    try:
        # Prefer the build-ninja .so (matches the project's preferred build dir).
        import sys

        _build_so = Path(__file__).resolve().parents[3] / "build-ninja" / "bindings"
        if str(_build_so) not in sys.path:
            sys.path.insert(0, str(_build_so))

        import tscore as _mod

        _tscore = _mod
        return _tscore
    except ImportError:
        if not _import_warned:
            warnings.warn(
                "tscore C++ extension not available; cpp_rollout_value will return 0.0. "
                "Build with: cmake --build build-ninja --target tscore_py -j4",
                stacklevel=3,
            )
            _import_warned = True
        return None


# ---------------------------------------------------------------------------
# Serialization
# ---------------------------------------------------------------------------


def _serialize_game_state(gs: "GameState") -> dict:
    """Serialize a Python GameState to the flat dict expected by play_from_public_state."""
    from tsrl.schemas import Side

    pub = gs.pub

    # Influence: flat list[int] index 0..85
    ussr_inf = [0] * 86
    us_inf = [0] * 86
    for (side, cid), val in pub.influence.items():
        if side == Side.USSR:
            ussr_inf[cid] = int(val)
        else:
            us_inf[cid] = int(val)

    # Discard / removed as list[int]
    discard_list = list(pub.discard) if pub.discard else []
    removed_list = list(pub.removed) if pub.removed else []

    return {
        # PublicState scalars
        "turn": int(pub.turn),
        "ar": int(pub.ar),
        "phasing": int(pub.phasing),
        "vp": int(pub.vp),
        "defcon": int(pub.defcon),
        "milops": [int(pub.milops[0]), int(pub.milops[1])],
        "space": [int(pub.space[0]), int(pub.space[1])],
        "china_held_by": int(pub.china_held_by),
        "china_playable": bool(pub.china_playable),
        # Influence arrays
        "ussr_influence": ussr_inf,
        "us_influence": us_inf,
        # Card sets
        "discard": discard_list,
        "removed": removed_list,
        # Effect flags
        "warsaw_pact_played": bool(pub.warsaw_pact_played),
        "marshall_plan_played": bool(pub.marshall_plan_played),
        "truman_doctrine_played": bool(pub.truman_doctrine_played),
        "john_paul_ii_played": bool(pub.john_paul_ii_played),
        "nato_active": bool(pub.nato_active),
        "de_gaulle_active": bool(pub.de_gaulle_active),
        "willy_brandt_active": bool(pub.willy_brandt_active),
        "us_japan_pact_active": bool(pub.us_japan_pact_active),
        "nuclear_subs_active": bool(pub.nuclear_subs_active),
        "norad_active": bool(pub.norad_active),
        "shuttle_diplomacy_active": bool(pub.shuttle_diplomacy_active),
        "flower_power_active": bool(pub.flower_power_active),
        "flower_power_cancelled": bool(pub.flower_power_cancelled),
        "salt_active": bool(pub.salt_active),
        "opec_cancelled": bool(pub.opec_cancelled),
        "awacs_active": bool(pub.awacs_active),
        "north_sea_oil_extra_ar": bool(pub.north_sea_oil_extra_ar),
        "glasnost_extra_ar": bool(pub.glasnost_extra_ar),
        "formosan_active": bool(pub.formosan_active),
        "cuban_missile_crisis_active": bool(pub.cuban_missile_crisis_active),
        "vietnam_revolts_active": bool(pub.vietnam_revolts_active),
        "bear_trap_active": bool(pub.bear_trap_active),
        "quagmire_active": bool(pub.quagmire_active),
        "iran_hostage_crisis_active": bool(pub.iran_hostage_crisis_active),
        "handicap_ussr": int(pub.handicap_ussr),
        "handicap_us": int(pub.handicap_us),
        "ops_modifier": [int(pub.ops_modifier[0]), int(pub.ops_modifier[1])],
        # Hands
        "ussr_hand": sorted(gs.hands[Side.USSR]),
        "us_hand": sorted(gs.hands[Side.US]),
        # Deck
        "deck": list(gs.deck),
        # China Card ownership
        "ussr_holds_china": bool(gs.ussr_holds_china),
        "us_holds_china": bool(gs.us_holds_china),
    }


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def cpp_rollout_value(gs: "GameState", rng_seed: int | None = None) -> float:
    """Run a C++ MinimalHybrid heuristic rollout from gs to terminal.

    Returns a value in [-1, +1] from USSR perspective:
      +1.0 = USSR wins, -1.0 = US wins, 0.0 = draw.

    Falls back to 0.0 (neutral) if the C++ extension is unavailable.

    Args:
        gs:       Current game state (not mutated).
        rng_seed: Optional integer seed for reproducibility.
    """
    tscore = _get_tscore()
    if tscore is None:
        return 0.0

    state_dict = _serialize_game_state(gs)
    return tscore.play_from_public_state(state_dict, rng_seed)
