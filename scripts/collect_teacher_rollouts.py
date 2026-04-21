#!/usr/bin/env python3
"""Collect TorchScript teacher rollout rows with full policy targets.

The teacher plays both sides across the requested game set, rotating opponents
within each side split.  Rows are recorded only for teacher decisions and are
compatible with scripts/train_baseline.py --teacher-targets.
"""
from __future__ import annotations

import argparse
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
import torch
import torch.nn.functional as F

_ROOT = Path(__file__).resolve().parents[1]
for _path in (_ROOT / "build-ninja" / "bindings", _ROOT / "python", _ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

import tscore  # noqa: E402

CARD_SLOTS = 112
CARD_TARGET_SIZE = 111
COUNTRY_SLOTS = 86
MODE_INFLUENCE = 0
MODE_COUP = 1
MODE_REALIGN = 2
MODE_SPACE = 3
MODE_EVENT = 4
MODE_EVENT_FIRST = 5
FLUSH_ROWS = 10_000

_EFFECT_BOOL_COLS = [
    "bear_trap_active",
    "quagmire_active",
    "cuban_missile_crisis_active",
    "iran_hostage_crisis_active",
    "norad_active",
    "shuttle_diplomacy_active",
    "salt_active",
    "flower_power_active",
    "flower_power_cancelled",
    "vietnam_revolts_active",
    "north_sea_oil_extra_ar",
    "glasnost_extra_ar",
    "nato_active",
    "de_gaulle_active",
    "nuclear_subs_active",
    "formosan_active",
    "awacs_active",
]

_SCHEMA = pa.schema(
    [
        ("game_id", pa.string()),
        ("step_idx", pa.int64()),
        ("turn", pa.int32()),
        ("ar", pa.int32()),
        ("phasing", pa.int32()),
        ("action_kind", pa.int32()),
        ("card_id", pa.int32()),
        ("country_id", pa.int32()),
        ("action_card_id", pa.int32()),
        ("action_mode", pa.int32()),
        ("action_targets", pa.string()),
        ("vp", pa.int32()),
        ("defcon", pa.int32()),
        ("milops_ussr", pa.int32()),
        ("milops_us", pa.int32()),
        ("space_ussr", pa.int32()),
        ("space_us", pa.int32()),
        ("china_held_by", pa.int32()),
        ("china_playable", pa.bool_()),
        ("ussr_influence", pa.list_(pa.int32())),
        ("us_influence", pa.list_(pa.int32())),
        ("discard_mask", pa.list_(pa.float32())),
        ("removed_mask", pa.list_(pa.float32())),
        ("actor_known_in", pa.list_(pa.float32())),
        ("actor_possible", pa.list_(pa.float32())),
        ("actor_hand_size", pa.int32()),
        ("actor_holds_china", pa.bool_()),
        ("winner_side", pa.float32()),
        ("game_result", pa.string()),
        ("final_vp", pa.int32()),
        ("end_turn", pa.int32()),
        ("end_reason", pa.string()),
        ("ops_modifier", pa.list_(pa.int32())),
        *[(col, pa.int8()) for col in _EFFECT_BOOL_COLS],
        ("influence", pa.list_(pa.float32())),
        ("cards", pa.list_(pa.float32())),
        ("scalars", pa.list_(pa.float32())),
        ("card_mask", pa.list_(pa.bool_())),
        ("mode_mask", pa.list_(pa.bool_())),
        ("country_mask", pa.list_(pa.bool_())),
        ("target_card", pa.int32()),
        ("target_mode", pa.int32()),
        ("target_country", pa.int32()),
        ("target_is_card", pa.bool_()),
        ("teacher_card_target", pa.list_(pa.float32())),
        ("teacher_mode_target", pa.list_(pa.float32())),
        ("teacher_value_target", pa.float32()),
        ("has_teacher_target", pa.bool_()),
    ]
)


@dataclass
class ScriptedPolicy:
    name: str
    path: Path
    model: torch.jit.ScriptModule
    device: torch.device
    scalar_dim: int
    card_dim: int
    mode_dim: int


@dataclass
class PolicyForward:
    influence: list[float]
    cards: list[float]
    scalars: list[float]
    card_logits: torch.Tensor
    mode_logits: torch.Tensor
    country_logits: torch.Tensor | None
    value: torch.Tensor


class BatchParquetWriter:
    def __init__(self, out_path: Path) -> None:
        self.out_path = out_path
        self.out_path.parent.mkdir(parents=True, exist_ok=True)
        self._rows: list[dict[str, Any]] = []
        self._writer: pq.ParquetWriter | None = None
        self.rows_written = 0

    def add(self, row: dict[str, Any]) -> None:
        self._rows.append(row)
        if len(self._rows) >= FLUSH_ROWS:
            self.flush()

    def flush(self) -> None:
        if not self._rows:
            return
        table = pa.Table.from_pylist(self._rows, schema=_SCHEMA)
        if self._writer is None:
            self._writer = pq.ParquetWriter(self.out_path, _SCHEMA, compression="snappy")
        self._writer.write_table(table)
        self.rows_written += len(self._rows)
        self._rows.clear()

    def close(self) -> None:
        if self._rows:
            self.flush()
        if self._writer is None:
            self._writer = pq.ParquetWriter(self.out_path, _SCHEMA, compression="snappy")
        self._writer.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Collect teacher softmax targets from TorchScript rollout games."
    )
    parser.add_argument("--teacher", type=Path, required=True, help="TorchScript .pt teacher")
    parser.add_argument("--opponents", nargs="+", required=True, help="Opponent names or __heuristic__")
    parser.add_argument("--games", type=int, default=2000, help="Total games to collect")
    parser.add_argument("--out", type=Path, required=True, help="Output parquet path")
    parser.add_argument("--seed", type=int, default=77777, help="Base RNG seed")
    parser.add_argument(
        "--include-softmax",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Keep teacher card/mode softmax targets (currently always written)",
    )
    parser.add_argument(
        "--include-values",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Write teacher value predictions",
    )
    parser.add_argument("--device", default=None, help="Torch device; default auto")
    parser.add_argument("--epsilon", type=float, default=0.0, help="Teacher epsilon-greedy rate")
    parser.add_argument("--max-steps", type=int, default=3000, help="Safety cap per game")
    parser.add_argument("--verbose", action="store_true", help="Print progress every 100 games")
    return parser.parse_args()


def _side(side_int: int):
    return tscore.Side.USSR if int(side_int) == int(tscore.Side.USSR) else tscore.Side.US


def _card_mask(card_ids: list[int] | set[int] | frozenset[int]) -> list[float]:
    mask = [0.0] * CARD_SLOTS
    for cid in card_ids:
        cid_i = int(cid)
        if 0 < cid_i < CARD_SLOTS:
            mask[cid_i] = 1.0
    return mask


def _feature_lists(
    state: dict[str, Any],
    hand: list[int],
    holds_china: bool,
    side_int: int,
) -> tuple[list[float], list[float], list[float]]:
    influence = [float(x) for x in state["ussr_influence"]] + [
        float(x) for x in state["us_influence"]
    ]
    hand_mask = _card_mask(hand)
    cards = hand_mask + hand_mask + _card_mask(state["discard"]) + _card_mask(state["removed"])
    ops_modifier = state.get("ops_modifier", (0, 0))
    base_scalars = [
        float(state["vp"]) / 20.0,
        (float(state["defcon"]) - 1.0) / 4.0,
        float(state["milops"][0]) / 6.0,
        float(state["milops"][1]) / 6.0,
        float(state["space"][0]) / 9.0,
        float(state["space"][1]) / 9.0,
        float(state["china_held_by"]),
        float(holds_china),
        float(state["turn"]) / 10.0,
        float(state["ar"]) / 8.0,
        float(side_int),
        float(bool(state.get("bear_trap_active", False))),
        float(bool(state.get("quagmire_active", False))),
        float(bool(state.get("cuban_missile_crisis_active", False))),
        float(bool(state.get("iran_hostage_crisis_active", False))),
        float(bool(state.get("norad_active", False))),
        float(bool(state.get("shuttle_diplomacy_active", False))),
        float(bool(state.get("salt_active", False))),
        float(bool(state.get("flower_power_active", False))),
        float(bool(state.get("flower_power_cancelled", False))),
        float(bool(state.get("vietnam_revolts_active", False))),
        float(bool(state.get("north_sea_oil_extra_ar", False))),
        float(state.get("glasnost_free_ops", 0)) / 4.0,
        float(bool(state.get("nato_active", False))),
        float(bool(state.get("de_gaulle_active", False))),
        float(bool(state.get("nuclear_subs_active", False))),
        float(bool(state.get("formosan_active", False))),
        float(bool(state.get("awacs_active", False))),
        0.0,
        0.0,
        float(ops_modifier[0]) / 3.0,
        float(ops_modifier[1]) / 3.0,
    ]
    frame_context = [0.0] * 8
    frame_context[-1] = 1.0
    return influence, cards, base_scalars + frame_context


def _adapt_scalars(scalars: list[float], scalar_dim: int) -> list[float]:
    if len(scalars) == scalar_dim:
        return scalars
    if scalar_dim == 32 and len(scalars) == 40:
        return scalars[:32]
    if scalar_dim == 11:
        return scalars[:11]
    if len(scalars) > scalar_dim:
        return scalars[:scalar_dim]
    return scalars + [0.0] * (scalar_dim - len(scalars))


def _probe_policy_shape(
    model: torch.jit.ScriptModule,
    device: torch.device,
) -> tuple[int, int, int]:
    for scalar_dim in (40, 32, 11):
        try:
            with torch.no_grad():
                out = model(
                    torch.zeros((1, 172), dtype=torch.float32, device=device),
                    torch.zeros((1, 448), dtype=torch.float32, device=device),
                    torch.zeros((1, scalar_dim), dtype=torch.float32, device=device),
                )
            return (
                scalar_dim,
                int(out["card_logits"].shape[-1]),
                int(out["mode_logits"].shape[-1]),
            )
        except Exception:
            continue
    raise RuntimeError("could not infer TorchScript input/output shapes")


def load_scripted_policy(name: str, path: Path, device: torch.device) -> ScriptedPolicy:
    if not path.exists():
        raise FileNotFoundError(path)
    model = torch.jit.load(str(path), map_location=device)
    model.eval()
    model.to(device)
    scalar_dim, card_dim, mode_dim = _probe_policy_shape(model, device)
    return ScriptedPolicy(
        name=name,
        path=path,
        model=model,
        device=device,
        scalar_dim=scalar_dim,
        card_dim=card_dim,
        mode_dim=mode_dim,
    )


def _forward_policy(
    policy: ScriptedPolicy,
    state: dict[str, Any],
    hand: list[int],
    holds_china: bool,
    side_int: int,
) -> PolicyForward:
    influence, cards, scalars_40 = _feature_lists(state, hand, holds_china, side_int)
    model_scalars = _adapt_scalars(scalars_40, policy.scalar_dim)
    with torch.no_grad():
        out = policy.model(
            torch.tensor([influence], dtype=torch.float32, device=policy.device),
            torch.tensor([cards], dtype=torch.float32, device=policy.device),
            torch.tensor([model_scalars], dtype=torch.float32, device=policy.device),
        )

    country_logits = out.get("country_logits")
    if country_logits is not None:
        country_logits = country_logits[0].detach().cpu()
    strategy_logits = out.get("strategy_logits")
    country_strategy_logits = out.get("country_strategy_logits")
    if strategy_logits is not None and country_strategy_logits is not None:
        strategy_idx = int(strategy_logits[0].argmax().item())
        country_logits = country_strategy_logits[0, strategy_idx].detach().cpu()

    return PolicyForward(
        influence=influence,
        cards=cards,
        scalars=scalars_40,
        card_logits=out["card_logits"][0],
        mode_logits=out["mode_logits"][0],
        country_logits=country_logits,
        value=out["value"].reshape(-1)[0],
    )


def _legal_card_mask(
    hand: list[int],
    state: dict[str, Any],
    side_obj: Any,
    holds_china: bool,
    card_dim: int,
) -> torch.Tensor:
    mask = torch.zeros(card_dim, dtype=torch.bool)
    for cid in tscore.legal_cards(hand, state, side_obj, holds_china):
        idx = int(cid) - 1
        if 0 <= idx < card_dim:
            mask[idx] = True
    return mask


def _enumerate_actions(
    hand: list[int],
    state: dict[str, Any],
    side_obj: Any,
    holds_china: bool,
) -> list[Any]:
    return list(tscore.enumerate_actions(hand, state, side_obj, holds_china))


def _mode_mask_from_actions(actions: list[Any], mode_dim: int) -> torch.Tensor:
    mask = torch.zeros(mode_dim, dtype=torch.bool)
    for action in actions:
        mode_idx = int(action.mode)
        if 0 <= mode_idx < mode_dim:
            mask[mode_idx] = True
    return mask


def _choose_index(
    logits: torch.Tensor,
    mask: torch.Tensor,
    rng: np.random.Generator,
    epsilon: float,
) -> int:
    legal = torch.nonzero(mask, as_tuple=False).flatten().cpu().numpy()
    if legal.size == 0:
        raise ValueError("empty legal mask")
    if epsilon > 0.0 and float(rng.random()) < epsilon:
        return int(rng.choice(legal))
    masked = logits.detach().cpu().masked_fill(~mask, -1.0e9)
    return int(masked.argmax().item())


def _softmax_target(logits: torch.Tensor, mask: torch.Tensor) -> list[float]:
    masked = logits.masked_fill(~mask.to(logits.device), -1.0e9)
    probs = F.softmax(masked, dim=-1).detach().cpu().numpy().astype(np.float32)
    return probs.tolist()


def _country_score(country_logits: torch.Tensor | None, country_id: int) -> float:
    if country_logits is None:
        return 0.0
    if 0 <= country_id < int(country_logits.numel()):
        return float(country_logits[country_id].item())
    return float("-inf")


def _action_score(action: Any, country_logits: torch.Tensor | None) -> tuple[float, int, tuple[int, ...]]:
    targets = tuple(int(t) for t in action.targets)
    if not targets:
        return (0.0, 0, targets)
    score = sum(_country_score(country_logits, target) for target in targets)
    return (float(score), -len(targets), tuple(-target for target in targets))


def _action_dict(action: Any) -> dict[str, Any]:
    return {
        "card_id": int(action.card_id),
        "mode": int(action.mode),
        "targets": [int(target) for target in action.targets],
    }


def _select_action(
    policy: ScriptedPolicy,
    forward: PolicyForward,
    state: dict[str, Any],
    hand: list[int],
    holds_china: bool,
    side_int: int,
    rng: np.random.Generator,
    epsilon: float,
) -> tuple[dict[str, Any] | None, torch.Tensor, torch.Tensor, torch.Tensor]:
    side_obj = _side(side_int)
    card_mask = _legal_card_mask(hand, state, side_obj, holds_china, policy.card_dim)
    if not bool(card_mask.any()):
        actions = _enumerate_actions(hand, state, side_obj, holds_china)
        if not actions:
            return None, card_mask, torch.zeros(policy.mode_dim, dtype=torch.bool), torch.zeros(
                COUNTRY_SLOTS, dtype=torch.bool
            )
        action = sorted(actions, key=lambda a: (int(a.card_id), int(a.mode), tuple(a.targets)))[0]
        mode_mask = _mode_mask_from_actions(actions, policy.mode_dim)
        country_mask = _country_mask_for_actions(actions)
        return _action_dict(action), card_mask, mode_mask, country_mask

    card_idx = _choose_index(forward.card_logits, card_mask, rng, epsilon)
    card_id = card_idx + 1
    card_actions = _enumerate_actions([card_id], state, side_obj, holds_china)
    if not card_actions:
        card_actions = [
            action
            for action in _enumerate_actions(hand, state, side_obj, holds_china)
            if int(action.card_id) == card_id
        ]
    if not card_actions:
        return None, card_mask, torch.zeros(policy.mode_dim, dtype=torch.bool), torch.zeros(
            COUNTRY_SLOTS, dtype=torch.bool
        )

    mode_mask = _mode_mask_from_actions(card_actions, policy.mode_dim)
    if bool(mode_mask.any()):
        mode_idx = _choose_index(forward.mode_logits, mode_mask, rng, epsilon)
    else:
        mode_idx = int(card_actions[0].mode)

    candidate_actions = [action for action in card_actions if int(action.mode) == mode_idx]
    if not candidate_actions:
        candidate_actions = card_actions
        mode_idx = int(candidate_actions[0].mode)

    country_mask = _country_mask_for_actions(candidate_actions)
    action = max(
        candidate_actions,
        key=lambda a: (_action_score(a, forward.country_logits), -int(a.card_id), -int(a.mode)),
    )
    return _action_dict(action), card_mask, mode_mask, country_mask


def _country_mask_for_actions(actions: list[Any]) -> torch.Tensor:
    mask = torch.zeros(COUNTRY_SLOTS, dtype=torch.bool)
    for action in actions:
        for target in action.targets:
            target_i = int(target)
            if 0 <= target_i < COUNTRY_SLOTS:
                mask[target_i] = True
    return mask


def _winner_side_value(result: Any) -> float:
    if result.winner == tscore.Side.USSR:
        return 1.0
    if result.winner == tscore.Side.US:
        return -1.0
    return 0.0


def _game_result_str(result: Any) -> str:
    if result.winner == tscore.Side.USSR:
        return "ussr_win"
    if result.winner == tscore.Side.US:
        return "us_win"
    return "draw"


def _teacher_won(result: Any, teacher_side: Any) -> bool:
    return bool(result.winner == teacher_side)


def _row_from_decision(
    game_id: str,
    step_idx: int,
    state: dict[str, Any],
    hand: list[int],
    holds_china: bool,
    side_int: int,
    action: dict[str, Any],
    forward: PolicyForward,
    card_mask: torch.Tensor,
    mode_mask: torch.Tensor,
    country_mask: torch.Tensor,
    teacher_card_target: list[float],
    teacher_mode_target: list[float],
    teacher_value_target: float,
) -> dict[str, Any]:
    action_targets = [int(t) for t in action["targets"]]
    hand_set = set(int(cid) for cid in hand)
    discard = set(int(cid) for cid in state["discard"])
    removed = set(int(cid) for cid in state["removed"])
    target_country = action_targets[0] if action_targets else -1
    return {
        "game_id": game_id,
        "step_idx": step_idx,
        "turn": int(state["turn"]),
        "ar": int(state["ar"]),
        "phasing": int(side_int),
        "action_kind": -1,
        "card_id": int(action["card_id"]),
        "country_id": target_country,
        "action_card_id": int(action["card_id"]),
        "action_mode": int(action["mode"]),
        "action_targets": ",".join(str(t) for t in action_targets),
        "vp": int(state["vp"]),
        "defcon": int(state["defcon"]),
        "milops_ussr": int(state["milops"][0]),
        "milops_us": int(state["milops"][1]),
        "space_ussr": int(state["space"][0]),
        "space_us": int(state["space"][1]),
        "china_held_by": int(state["china_held_by"]),
        "china_playable": bool(state.get("china_playable", False)),
        "ussr_influence": [int(x) for x in state["ussr_influence"]],
        "us_influence": [int(x) for x in state["us_influence"]],
        "discard_mask": _card_mask(discard),
        "removed_mask": _card_mask(removed),
        "actor_known_in": _card_mask(hand_set),
        "actor_possible": _card_mask(hand_set),
        "actor_hand_size": sum(1 for cid in hand_set if cid != 6),
        "actor_holds_china": bool(holds_china),
        "winner_side": 0.0,
        "game_result": "",
        "final_vp": 0,
        "end_turn": 0,
        "end_reason": "",
        "ops_modifier": [int(x) for x in state.get("ops_modifier", (0, 0))],
        **{col: int(bool(state.get(col, False))) for col in _EFFECT_BOOL_COLS},
        "influence": forward.influence,
        "cards": forward.cards,
        "scalars": forward.scalars,
        "card_mask": [bool(x) for x in card_mask.tolist()],
        "mode_mask": [bool(x) for x in mode_mask.tolist()],
        "country_mask": [bool(x) for x in country_mask.tolist()],
        "target_card": int(action["card_id"]) - 1,
        "target_mode": int(action["mode"]),
        "target_country": target_country,
        "target_is_card": int(action["card_id"]) > 0,
        "teacher_card_target": teacher_card_target,
        "teacher_mode_target": teacher_mode_target,
        "teacher_value_target": teacher_value_target,
        "has_teacher_target": True,
    }


def _finish_game_rows(rows: list[dict[str, Any]], result: Any) -> None:
    winner_side = _winner_side_value(result)
    game_result = _game_result_str(result)
    final_vp = int(getattr(result, "final_vp", 0))
    end_turn = int(getattr(result, "end_turn", 0))
    end_reason = str(getattr(result, "end_reason", ""))
    for row in rows:
        row["winner_side"] = winner_side
        row["game_result"] = game_result
        row["final_vp"] = final_vp
        row["end_turn"] = end_turn
        row["end_reason"] = end_reason


def _resolve_opponent_path(name: str) -> Path:
    path = Path(name)
    if path.suffix == ".pt" or path.exists():
        return path
    return _ROOT / "data" / "checkpoints" / "scripted_for_elo" / f"{name}_scripted.pt"


def collect_one_game(
    *,
    writer: BatchParquetWriter,
    teacher: ScriptedPolicy,
    opponent: ScriptedPolicy | None,
    opponent_name: str,
    teacher_side: Any,
    game_idx: int,
    seed: int,
    epsilon: float,
    include_values: bool,
    max_steps: int,
) -> tuple[Any, int]:
    game_rows: list[dict[str, Any]] = []
    game_id = f"teacher_{teacher.name}_g{game_idx:06d}_s{seed}"
    rng = np.random.default_rng(seed)
    callback_count = 0

    def callback(state: dict[str, Any], hand: list[int], holds_china: bool, side_int: int):
        nonlocal callback_count
        callback_count += 1
        if callback_count > max_steps:
            raise RuntimeError(f"game {game_id} exceeded --max-steps={max_steps}")

        acting_side = _side(side_int)
        is_teacher = acting_side == teacher_side
        policy = teacher if is_teacher else opponent
        if policy is None:
            return None

        forward = _forward_policy(policy, state, hand, holds_china, side_int)
        action, card_mask, mode_mask, country_mask = _select_action(
            policy,
            forward,
            state,
            hand,
            holds_china,
            side_int,
            rng,
            epsilon if is_teacher else 0.0,
        )
        if action is None:
            return None

        if is_teacher:
            teacher_card_target = _softmax_target(forward.card_logits, card_mask)
            teacher_mode_target = _softmax_target(forward.mode_logits, mode_mask)
            teacher_value_target = float(forward.value.item()) if include_values else 0.0
            row = _row_from_decision(
                game_id=game_id,
                step_idx=len(game_rows),
                state=state,
                hand=hand,
                holds_china=holds_china,
                side_int=side_int,
                action=action,
                forward=forward,
                card_mask=card_mask,
                mode_mask=mode_mask,
                country_mask=country_mask,
                teacher_card_target=teacher_card_target,
                teacher_mode_target=teacher_mode_target,
                teacher_value_target=teacher_value_target,
            )
            game_rows.append(row)
        return action

    if opponent is None:
        results = tscore.play_callback_matchup(
            callback,
            teacher_side,
            tscore.PolicyKind.MinimalHybrid,
            1,
            seed=seed,
        )
    else:
        results = tscore.play_dual_callback_matchup(callback, game_count=1, seed=seed)
    result = results[0]
    _finish_game_rows(game_rows, result)
    for row in game_rows:
        writer.add(row)
    return result, len(game_rows)


def main() -> None:
    args = parse_args()
    if args.games < 0:
        raise ValueError("--games must be non-negative")
    if not args.opponents:
        raise ValueError("--opponents must not be empty")
    if args.epsilon < 0.0 or args.epsilon > 1.0:
        raise ValueError("--epsilon must be in [0, 1]")
    if args.max_steps <= 0:
        raise ValueError("--max-steps must be positive")

    device = torch.device(
        args.device if args.device is not None else ("cuda" if torch.cuda.is_available() else "cpu")
    )
    torch.manual_seed(args.seed)
    if device.type == "cuda":
        torch.cuda.manual_seed_all(args.seed)
    np.random.seed(args.seed)

    teacher = load_scripted_policy("teacher", args.teacher, device)
    if teacher.card_dim != CARD_TARGET_SIZE:
        raise ValueError(f"teacher card head has dim={teacher.card_dim}; expected {CARD_TARGET_SIZE}")
    print(
        f"[collect_teacher_rollouts] teacher={args.teacher} "
        f"scalar_dim={teacher.scalar_dim} card_dim={teacher.card_dim} mode_dim={teacher.mode_dim} "
        f"device={device}",
        flush=True,
    )

    opponents: dict[str, ScriptedPolicy | None] = {}
    for name in args.opponents:
        if name == "__heuristic__":
            opponents[name] = None
            continue
        opp_path = _resolve_opponent_path(name)
        opponents[name] = load_scripted_policy(name, opp_path, device)
        opp = opponents[name]
        assert opp is not None
        print(
            f"[collect_teacher_rollouts] opponent={name} path={opp.path} "
            f"scalar_dim={opp.scalar_dim} card_dim={opp.card_dim} mode_dim={opp.mode_dim}",
            flush=True,
        )

    writer = BatchParquetWriter(args.out)
    half = args.games // 2
    side_counts = {tscore.Side.USSR: 0, tscore.Side.US: 0}
    side_wins = {tscore.Side.USSR: 0, tscore.Side.US: 0}
    opponent_counts: Counter[str] = Counter()
    opponent_rows: Counter[str] = Counter()
    opponent_wins: Counter[str] = Counter()
    result_counts: Counter[str] = Counter()
    started = time.time()

    try:
        for game_idx in range(args.games):
            if game_idx < half:
                teacher_side = tscore.Side.USSR
                half_idx = game_idx
            else:
                teacher_side = tscore.Side.US
                half_idx = game_idx - half
            opponent_name = args.opponents[half_idx % len(args.opponents)]
            opponent = opponents[opponent_name]
            seed = args.seed + game_idx
            result, rows = collect_one_game(
                writer=writer,
                teacher=teacher,
                opponent=opponent,
                opponent_name=opponent_name,
                teacher_side=teacher_side,
                game_idx=game_idx,
                seed=seed,
                epsilon=args.epsilon,
                include_values=args.include_values,
                max_steps=args.max_steps,
            )
            side_counts[teacher_side] += 1
            opponent_counts[opponent_name] += 1
            opponent_rows[opponent_name] += rows
            result_counts[_game_result_str(result)] += 1
            if _teacher_won(result, teacher_side):
                side_wins[teacher_side] += 1
                opponent_wins[opponent_name] += 1
            if args.verbose and (game_idx + 1) % 100 == 0:
                elapsed = time.time() - started
                print(
                    f"[collect_teacher_rollouts] game {game_idx + 1}/{args.games} "
                    f"rows={writer.rows_written + len(writer._rows):,} "
                    f"{(game_idx + 1) / max(elapsed, 1e-9):.2f} games/s",
                    flush=True,
                )
    finally:
        writer.close()

    total_rows = writer.rows_written
    ussr_games = side_counts[tscore.Side.USSR]
    us_games = side_counts[tscore.Side.US]
    ussr_wr = side_wins[tscore.Side.USSR] / ussr_games if ussr_games else 0.0
    us_wr = side_wins[tscore.Side.US] / us_games if us_games else 0.0
    print(f"[collect_teacher_rollouts] wrote {total_rows:,} rows -> {args.out}", flush=True)
    print(
        f"[collect_teacher_rollouts] games={args.games} "
        f"teacher_USSR={side_wins[tscore.Side.USSR]}/{ussr_games} ({ussr_wr:.3f}) "
        f"teacher_US={side_wins[tscore.Side.US]}/{us_games} ({us_wr:.3f})",
        flush=True,
    )
    print(f"[collect_teacher_rollouts] results={dict(result_counts)}", flush=True)
    for name in args.opponents:
        games = opponent_counts[name]
        rows = opponent_rows[name]
        wins = opponent_wins[name]
        wr = wins / games if games else 0.0
        print(
            f"[collect_teacher_rollouts] opponent={name} games={games} rows={rows} "
            f"teacher_wins={wins} teacher_wr={wr:.3f}",
            flush=True,
        )


if __name__ == "__main__":
    main()
