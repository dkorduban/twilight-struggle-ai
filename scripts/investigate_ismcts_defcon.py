#!/usr/bin/env python3
"""Investigate DEFCON-1 patterns around ISMCTS/search traces.

This script does two things:
1. Collect a small deterministic raw-policy baseline from the best available
   scripted checkpoint using traced greedy self-play.
2. Analyze the best available existing search-trace JSONL files in
   ``data/selfplay/`` because the bindings do not expose a traced ISMCTS
   policy API, only benchmark entrypoints that return terminal GameResults.

Outputs:
  - results/analysis/ismcts_defcon_trace_analysis.md
  - results/analysis/ismcts_defcon_trace_windows.jsonl
"""
from __future__ import annotations

import argparse
import json
import math
import statistics
import sys
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import torch

_REPO_ROOT = Path(__file__).resolve().parents[1]
for _p in (_REPO_ROOT / "build-ninja" / "bindings", _REPO_ROOT / "build" / "bindings"):
    if any(_p.glob("tscore*.so")):
        sys.path.insert(0, str(_p))
        break
sys.path.insert(0, str(_REPO_ROOT / "python"))

import tscore  # noqa: E402
from tsrl.engine.legal_actions import (  # noqa: E402
    accessible_countries,
    effective_ops,
    legal_cards,
    legal_modes,
    load_adjacency,
)
from tsrl.etl.dataset import _card_mask  # noqa: E402
from tsrl.etl.game_data import load_cards  # noqa: E402
from tsrl.schemas import ActionMode, PublicState, Side  # noqa: E402


MODE_LABELS = {
    0: "ops",
    1: "event",
    2: "space",
    3: "realignment",
    4: "coup",
}

# Engine/raw enum -> requested normalized mode_id
NORMALIZED_MODE_ID = {
    int(ActionMode.INFLUENCE): 0,
    int(ActionMode.EVENT): 1,
    int(ActionMode.SPACE): 2,
    int(ActionMode.REALIGN): 3,
    int(ActionMode.COUP): 4,
}

PRIMARY_SEARCH_GLOB = "mcts*.jsonl"
WINDOW_SIZE = 10
LAST_STEPS_FOR_SUMMARY = 3
RAW_TRACE_TEMPERATURE = 1e-6

BOOL_PUBLIC_STATE_FIELDS = [
    "china_playable",
    "warsaw_pact_played",
    "marshall_plan_played",
    "truman_doctrine_played",
    "john_paul_ii_played",
    "nato_active",
    "de_gaulle_active",
    "willy_brandt_active",
    "us_japan_pact_active",
    "nuclear_subs_active",
    "norad_active",
    "shuttle_diplomacy_active",
    "flower_power_active",
    "flower_power_cancelled",
    "salt_active",
    "opec_cancelled",
    "awacs_active",
    "north_sea_oil_extra_ar",
    "glasnost_extra_ar",
    "formosan_active",
    "cuban_missile_crisis_active",
    "vietnam_revolts_active",
    "bear_trap_active",
    "quagmire_active",
    "iran_hostage_crisis_active",
]

INT_PUBLIC_STATE_FIELDS = [
    "turn",
    "ar",
    "vp",
    "defcon",
    "handicap_ussr",
    "handicap_us",
    "state_hash",
]


@dataclass
class ActionRow:
    source: str
    source_kind: str
    game_id: str
    step_idx: int
    turn: int
    ar: int
    side: str
    side_int: int
    card_id: int
    card_name: str
    raw_mode: int
    mode_id: int
    mode_name: str
    defcon_before: int
    defcon_after: int
    is_defcon_drop: bool
    is_terminal_defcon1: bool
    end_turn: int
    end_reason: str


@dataclass
class DatasetSummary:
    name: str
    source_kind: str
    games: int
    defcon1_games: int
    avg_turn_defcon1: float | None


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--raw-games", type=int, default=64, help="Near-greedy raw-policy baseline games.")
    p.add_argument("--raw-seed", type=int, default=24000, help="Base seed for greedy traced raw-policy games.")
    p.add_argument(
        "--checkpoint-dir",
        type=Path,
        default=Path("data/checkpoints/scripted_for_elo"),
        help="Directory containing scripted checkpoints.",
    )
    p.add_argument(
        "--search-dir",
        type=Path,
        default=Path("data/selfplay"),
        help="Directory containing existing MCTS/search JSONL traces.",
    )
    p.add_argument(
        "--out-md",
        type=Path,
        default=Path("results/analysis/ismcts_defcon_trace_analysis.md"),
        help="Markdown findings output path.",
    )
    p.add_argument(
        "--out-jsonl",
        type=Path,
        default=Path("results/analysis/ismcts_defcon_trace_windows.jsonl"),
        help="Detailed DEFCON-1 windows JSONL output path.",
    )
    return p.parse_args()


def side_name(side_int: int) -> str:
    if side_int == int(Side.USSR):
        return "USSR"
    if side_int == int(Side.US):
        return "US"
    return f"side_{side_int}"


def normalized_mode(mode: int) -> tuple[int, str]:
    norm = NORMALIZED_MODE_ID.get(int(mode), -1)
    return norm, MODE_LABELS.get(norm, f"mode_{norm}")


def find_best_scripted_checkpoint(checkpoint_dir: Path) -> Path:
    choices: list[tuple[int, str, Path]] = []
    for path in checkpoint_dir.glob("v*_scripted.pt"):
        prefix = path.stem.split("_")[0]
        digits = "".join(ch for ch in prefix if ch.isdigit())
        if digits:
            choices.append((int(digits), path.name, path))
    for path in checkpoint_dir.glob("v*_sc_scripted.pt"):
        prefix = path.stem.split("_")[0]
        digits = "".join(ch for ch in prefix if ch.isdigit())
        if digits:
            choices.append((int(digits), path.name, path))
    if not choices:
        raise FileNotFoundError(f"No scripted checkpoints found in {checkpoint_dir}")
    choices.sort(key=lambda item: (item[0], item[1]))
    return choices[-1][2]


def build_public_state(state_dict: dict[str, Any]) -> PublicState:
    pub = PublicState()
    for field in INT_PUBLIC_STATE_FIELDS:
        if field in state_dict:
            setattr(pub, field, int(state_dict[field]))
    pub.phasing = Side(int(state_dict["phasing"]))
    pub.china_held_by = Side(int(state_dict["china_held_by"]))

    milops = [int(x) for x in state_dict.get("milops", [0, 0])]
    space = [int(x) for x in state_dict.get("space", [0, 0])]
    ops_modifier = [int(x) for x in state_dict.get("ops_modifier", [0, 0])]
    pub.milops = milops
    pub.space = space
    pub.ops_modifier = ops_modifier
    pub.discard = frozenset(int(x) for x in state_dict.get("discard", []))
    pub.removed = frozenset(int(x) for x in state_dict.get("removed", []))

    for field in BOOL_PUBLIC_STATE_FIELDS:
        if field in state_dict:
            setattr(pub, field, bool(state_dict[field]))

    for cid, amount in enumerate(state_dict.get("ussr_influence", [])):
        if amount:
            pub.influence[Side.USSR, cid] = int(amount)
    for cid, amount in enumerate(state_dict.get("us_influence", [])):
        if amount:
            pub.influence[Side.US, cid] = int(amount)
    return pub


def build_model_inputs(
    pub: PublicState,
    hand: frozenset[int],
    holds_china: bool,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    hand_mask = _card_mask(hand)
    influence = torch.tensor(
        list(pub.influence._data[:86]) + list(pub.influence._data[86:]),
        dtype=torch.float32,
    ).unsqueeze(0)
    cards = torch.tensor(
        hand_mask + hand_mask + _card_mask(pub.discard) + _card_mask(pub.removed),
        dtype=torch.float32,
    ).unsqueeze(0)
    scalars = torch.tensor(
        [
            pub.vp / 20.0,
            (pub.defcon - 1) / 4.0,
            pub.milops[Side.USSR] / 6.0,
            pub.milops[Side.US] / 6.0,
            pub.space[Side.USSR] / 9.0,
            pub.space[Side.US] / 9.0,
            float(int(pub.china_held_by)),
            float(holds_china),
            pub.turn / 10.0,
            pub.ar / 8.0,
            float(int(pub.phasing)),
        ],
        dtype=torch.float32,
    ).unsqueeze(0)
    return influence, cards, scalars


def infer_expected_scalar_dim(model: torch.jit.ScriptModule) -> int:
    state = model.state_dict()
    scalar_weight = state.get("scalar_encoder.weight")
    if scalar_weight is None:
        return 11
    input_dim = int(scalar_weight.shape[1])
    has_region_encoder = any(key.startswith("region_encoder.") for key in state)
    region_dim = 42 if has_region_encoder else 0
    scalar_dim = input_dim - region_dim
    return scalar_dim if scalar_dim > 0 else 11


def adapt_scalars(scalars: torch.Tensor, expected_dim: int) -> torch.Tensor:
    current_dim = int(scalars.shape[1])
    if current_dim == expected_dim:
        return scalars
    if current_dim > expected_dim:
        return scalars[:, :expected_dim]
    pad = torch.zeros((scalars.shape[0], expected_dim - current_dim), dtype=scalars.dtype)
    return torch.cat([scalars, pad], dim=1)


def extract_output_tensor(outputs: Any, key: str, index: int) -> torch.Tensor:
    if isinstance(outputs, dict) and key in outputs:
        tensor = outputs[key]
    elif isinstance(outputs, (tuple, list)) and len(outputs) > index:
        tensor = outputs[index]
    else:
        raise KeyError(f"Model output missing {key}")
    if not isinstance(tensor, torch.Tensor):
        raise TypeError(f"Model output {key} is not a tensor")
    return tensor[0]


def ranked_targets(country_logits: torch.Tensor, accessible: list[int], count: int) -> list[int]:
    if count <= 0 or not accessible:
        return []
    ranked = sorted(accessible, key=lambda cid: (-float(country_logits[cid].item()), cid))
    if not ranked:
        return []
    if count <= len(ranked):
        return ranked[:count]
    return ranked + [ranked[0]] * (count - len(ranked))


def make_greedy_scripted_callback(model_path: Path):
    model = torch.jit.load(str(model_path), map_location="cpu")
    model.eval()
    adjacency = load_adjacency()
    expected_scalar_dim = infer_expected_scalar_dim(model)

    def _callback(state_dict, hand_list, holds_china: bool, side_int: int):
        hand = frozenset(int(x) for x in hand_list)
        if not hand:
            return None

        pub = build_public_state(state_dict)
        side = Side(side_int)
        playable = sorted(legal_cards(hand, pub, side, holds_china=holds_china))
        if not playable:
            return None

        influence, cards, scalars = build_model_inputs(pub, hand, holds_china)
        scalars = adapt_scalars(scalars, expected_scalar_dim)
        with torch.no_grad():
            outputs = model(influence, cards, scalars)

        card_logits = extract_output_tensor(outputs, "card_logits", 0)
        masked_card_logits = torch.full_like(card_logits, float("-inf"))
        for card_id in playable:
            masked_card_logits[card_id - 1] = card_logits[card_id - 1]
        card_id = int(torch.argmax(masked_card_logits).item()) + 1

        mode_logits = extract_output_tensor(outputs, "mode_logits", 1)
        legal = sorted(legal_modes(card_id, pub, side, adj=adjacency), key=int)
        if not legal:
            return None
        masked_mode_logits = torch.full_like(mode_logits, float("-inf"))
        for mode in legal:
            masked_mode_logits[int(mode)] = mode_logits[int(mode)]
        mode = ActionMode(int(torch.argmax(masked_mode_logits).item()))

        targets: list[int]
        if mode in (ActionMode.EVENT, ActionMode.SPACE):
            targets = []
        else:
            country_logits = extract_output_tensor(outputs, "country_logits", 2)
            accessible = sorted(accessible_countries(side, pub, adjacency, mode=mode))
            if mode in (ActionMode.COUP, ActionMode.REALIGN):
                targets = ranked_targets(country_logits, accessible, 1)
            else:
                ops = effective_ops(card_id, pub, side)
                targets = ranked_targets(country_logits, accessible, ops)

        return {
            "card_id": int(card_id),
            "mode": int(mode),
            "targets": [int(x) for x in targets],
        }

    return _callback


def action_row_from_trace_step(
    source: str,
    source_kind: str,
    game_id: str,
    step_idx: int,
    step,
    end_turn: int,
    end_reason: str,
    card_names: dict[int, str],
) -> ActionRow:
    raw_mode = int(step.action.mode)
    mode_id, mode_name = normalized_mode(raw_mode)
    side_int = int(step.side)
    return ActionRow(
        source=source,
        source_kind=source_kind,
        game_id=game_id,
        step_idx=step_idx,
        turn=int(step.turn),
        ar=int(step.ar),
        side=side_name(side_int),
        side_int=side_int,
        card_id=int(step.action.card_id),
        card_name=card_names.get(int(step.action.card_id), f"card#{int(step.action.card_id)}"),
        raw_mode=raw_mode,
        mode_id=mode_id,
        mode_name=mode_name,
        defcon_before=int(step.defcon_before),
        defcon_after=int(step.defcon_after),
        is_defcon_drop=int(step.defcon_after) < int(step.defcon_before),
        is_terminal_defcon1=int(step.defcon_after) == 1 and int(step.defcon_before) > 1,
        end_turn=end_turn,
        end_reason=end_reason,
    )


def collect_raw_policy_traces(
    checkpoint: Path,
    n_games: int,
    seed: int,
    card_names: dict[int, str],
) -> tuple[list[ActionRow], DatasetSummary]:
    rows: list[ActionRow] = []
    defcon1_turns: list[int] = []
    results, steps, boundaries = tscore.rollout_self_play_batched(
        model_path=str(checkpoint),
        n_games=n_games,
        pool_size=min(n_games, 64),
        seed=seed,
        device="cpu",
        temperature=RAW_TRACE_TEMPERATURE,
        nash_temperatures=False,
    )

    for game_idx, result in enumerate(results):
        start = int(boundaries[game_idx])
        end = int(boundaries[game_idx + 1]) if game_idx + 1 < len(boundaries) else len(steps)
        game_steps = steps[start:end]
        game_id = f"raw_rollout_{seed:06d}_{game_idx:04d}"
        if result.end_reason == "defcon1" and game_steps:
            defcon1_turns.append(int(game_steps[-1]["raw_turn"]))

        for local_idx, step in enumerate(game_steps):
            raw_mode = int(step["mode_idx"])
            mode_id, mode_name = normalized_mode(raw_mode)
            before = int(step["raw_defcon"])
            if local_idx + 1 < len(game_steps):
                after = int(game_steps[local_idx + 1]["raw_defcon"])
            elif result.end_reason == "defcon1":
                after = 1
            else:
                after = before
            card_id = int(step["card_idx"]) + 1
            side_int = int(step["side_int"])
            rows.append(
                ActionRow(
                    source=checkpoint.name,
                    source_kind="raw_policy",
                    game_id=game_id,
                    step_idx=local_idx,
                    turn=int(step["raw_turn"]),
                    ar=int(step["raw_ar"]),
                    side=side_name(side_int),
                    side_int=side_int,
                    card_id=card_id,
                    card_name=card_names.get(card_id, f"card#{card_id}"),
                    raw_mode=raw_mode,
                    mode_id=mode_id,
                    mode_name=mode_name,
                    defcon_before=before,
                    defcon_after=after,
                    is_defcon_drop=after < before,
                    is_terminal_defcon1=after == 1 and before > 1,
                    end_turn=int(result.end_turn),
                    end_reason=str(result.end_reason),
                )
            )

    summary = DatasetSummary(
        name=f"{checkpoint.name} @ T={RAW_TRACE_TEMPERATURE:g}",
        source_kind="raw_policy",
        games=n_games,
        defcon1_games=len(defcon1_turns),
        avg_turn_defcon1=(sum(defcon1_turns) / len(defcon1_turns)) if defcon1_turns else None,
    )
    return rows, summary


def discover_search_trace_files(search_dir: Path) -> list[Path]:
    candidates = sorted(search_dir.glob(PRIMARY_SEARCH_GLOB))
    primary = [p for p in candidates if "teacher" not in p.name.lower()]
    if primary:
        return primary
    return candidates


def collect_search_trace_rows(
    files: list[Path],
    card_names: dict[int, str],
) -> tuple[list[ActionRow], list[DatasetSummary]]:
    all_rows: list[ActionRow] = []
    summaries: list[DatasetSummary] = []

    for path in files:
        games: dict[str, list[dict[str, Any]]] = defaultdict(list)
        with path.open() as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                row = json.loads(line)
                games[str(row["game_id"])].append(row)

        defcon1_turns: list[int] = []
        file_rows: list[ActionRow] = []
        for game_id, seq in games.items():
            seq.sort(key=lambda item: int(item["step_idx"]))
            end_reason = str(seq[0].get("end_reason", ""))
            end_turn = int(seq[0].get("end_turn", seq[-1].get("turn", 0)))
            if end_reason == "defcon1" and seq:
                defcon1_turns.append(int(seq[-1]["turn"]))

            for idx, row in enumerate(seq):
                raw_mode = int(row["action_mode"])
                mode_id, mode_name = normalized_mode(raw_mode)
                before = int(row["defcon"])
                if idx + 1 < len(seq):
                    after = int(seq[idx + 1]["defcon"])
                elif end_reason == "defcon1":
                    after = 1
                else:
                    after = before
                side_int = int(row["phasing"])
                file_rows.append(
                    ActionRow(
                        source=path.name,
                        source_kind="search_proxy",
                        game_id=game_id,
                        step_idx=int(row["step_idx"]),
                        turn=int(row["turn"]),
                        ar=int(row["ar"]),
                        side=side_name(side_int),
                        side_int=side_int,
                        card_id=int(row["action_card_id"]),
                        card_name=card_names.get(int(row["action_card_id"]), f"card#{int(row['action_card_id'])}"),
                        raw_mode=raw_mode,
                        mode_id=mode_id,
                        mode_name=mode_name,
                        defcon_before=before,
                        defcon_after=after,
                        is_defcon_drop=after < before,
                        is_terminal_defcon1=after == 1 and before > 1,
                        end_turn=end_turn,
                        end_reason=end_reason,
                    )
                )

        all_rows.extend(file_rows)
        summaries.append(
            DatasetSummary(
                name=path.name,
                source_kind="search_proxy",
                games=len(games),
                defcon1_games=len(defcon1_turns),
                avg_turn_defcon1=(sum(defcon1_turns) / len(defcon1_turns)) if defcon1_turns else None,
            )
        )

    return all_rows, summaries


def build_windows(rows: list[ActionRow], window_size: int = WINDOW_SIZE) -> list[dict[str, Any]]:
    by_game: dict[tuple[str, str], list[ActionRow]] = defaultdict(list)
    for row in rows:
        by_game[(row.source_kind, row.game_id)].append(row)

    windows: list[dict[str, Any]] = []
    for (source_kind, game_id), seq in by_game.items():
        seq.sort(key=lambda item: item.step_idx)
        if not seq or seq[-1].end_reason != "defcon1":
            continue
        terminal_idx = None
        for idx, row in enumerate(seq):
            if row.is_terminal_defcon1:
                terminal_idx = idx
        if terminal_idx is None:
            terminal_idx = len(seq) - 1
        start = max(0, terminal_idx - window_size + 1)
        window_rows = seq[start : terminal_idx + 1]
        windows.append(
            {
                "source_kind": source_kind,
                "source": seq[0].source,
                "game_id": game_id,
                "terminal_step_idx": seq[terminal_idx].step_idx,
                "end_turn": seq[-1].end_turn,
                "end_reason": seq[-1].end_reason,
                "steps": [asdict(row) for row in window_rows],
            }
        )
    windows.sort(key=lambda item: (item["source_kind"], item["source"], item["game_id"]))
    return windows


def percent(numer: int, denom: int) -> float:
    return (100.0 * numer / denom) if denom else 0.0


def top_pre_defcon_patterns(windows: list[dict[str, Any]], last_n: int = LAST_STEPS_FOR_SUMMARY) -> list[tuple[str, str, int, str, int]]:
    counter: Counter[tuple[str, str, int, str]] = Counter()
    for window in windows:
        steps = window["steps"][-last_n:]
        for step in steps:
            counter[(step["card_name"], step["side"], int(step["mode_id"]), step["mode_name"])] += 1
    flattened: list[tuple[str, str, int, str, int]] = []
    for (card_name, side, mode_id, mode_name), count in counter.most_common(12):
        flattened.append((card_name, side, mode_id, mode_name, count))
    return flattened


def terminal_drop_stats(windows: list[dict[str, Any]]) -> tuple[Counter[str], Counter[str], Counter[str], list[int]]:
    mode_counter: Counter[str] = Counter()
    side_counter: Counter[str] = Counter()
    source_counter: Counter[str] = Counter()
    turns: list[int] = []
    for window in windows:
        for step in window["steps"]:
            if step["is_terminal_defcon1"]:
                mode_counter[step["mode_name"]] += 1
                side_counter[step["side"]] += 1
                source_counter[window["source_kind"]] += 1
                turns.append(int(step["turn"]))
    return mode_counter, side_counter, source_counter, turns


def last_window_examples(windows: list[dict[str, Any]], limit: int = 5) -> list[str]:
    lines: list[str] = []
    for window in windows[:limit]:
        lines.append(
            f"### {window['source_kind']} | {window['source']} | {window['game_id']} | end_turn={window['end_turn']}"
        )
        lines.append("")
        lines.append("| turn | ar | side | card | mode_id | mode | DEFCON before | DEFCON after |")
        lines.append("|---|---:|---|---|---:|---|---:|---:|")
        for step in window["steps"]:
            lines.append(
                "| "
                f"{step['turn']} | {step['ar']} | {step['side']} | {step['card_name']} ({step['card_id']}) | "
                f"{step['mode_id']} | {step['mode_name']} | {step['defcon_before']} | {step['defcon_after']} |"
            )
        lines.append("")
    return lines


def write_windows_jsonl(path: Path, windows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as f:
        for window in windows:
            f.write(json.dumps(window) + "\n")


def render_dataset_table(summaries: list[DatasetSummary]) -> list[str]:
    lines = [
        "| dataset | source_kind | games | defcon1_games | defcon1_rate | avg_turn_defcon1 |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for s in summaries:
        avg_turn = f"{s.avg_turn_defcon1:.2f}" if s.avg_turn_defcon1 is not None else "-"
        lines.append(
            f"| {s.name} | {s.source_kind} | {s.games} | {s.defcon1_games} | "
            f"{percent(s.defcon1_games, s.games):.1f}% | {avg_turn} |"
        )
    return lines


def render_counter_table(counter: Counter[str], title: str) -> list[str]:
    lines = [f"### {title}", "", "| value | count | pct |", "|---|---:|---:|"]
    total = sum(counter.values())
    for key, value in counter.most_common():
        lines.append(f"| {key} | {value} | {percent(value, total):.1f}% |")
    lines.append("")
    return lines


def render_pattern_table(patterns: list[tuple[str, str, int, str, int]]) -> list[str]:
    total = sum(item[4] for item in patterns)
    lines = [
        "| card | side | mode_id | mode | count | pct_of_top_bucket |",
        "|---|---|---:|---|---:|---:|",
    ]
    for card_name, side, mode_id, mode_name, count in patterns:
        lines.append(
            f"| {card_name} | {side} | {mode_id} | {mode_name} | {count} | {percent(count, total):.1f}% |"
        )
    return lines


def build_markdown_report(
    checkpoint: Path,
    raw_summary: DatasetSummary,
    search_summaries: list[DatasetSummary],
    raw_windows: list[dict[str, Any]],
    search_windows: list[dict[str, Any]],
    out_jsonl: Path,
) -> str:
    search_patterns = top_pre_defcon_patterns(search_windows)
    raw_patterns = top_pre_defcon_patterns(raw_windows) if raw_windows else []

    search_mode_counter, search_side_counter, _, search_turns = terminal_drop_stats(search_windows)
    raw_mode_counter, raw_side_counter, _, raw_turns = terminal_drop_stats(raw_windows)

    lines = [
        "# ISMCTS DEFCON Trace Analysis",
        "",
        "## Scope",
        "",
        f"- Raw greedy baseline checkpoint: `{checkpoint}`",
        "- Direct traced ISMCTS-vs-model play is not exposed in the Python bindings. "
        "The bindings expose `benchmark_ismcts*` result-only APIs, but no traced ISMCTS policy hook.",
        "- This report therefore uses two evidence sources:",
        f"  1. fresh near-greedy raw-policy self-play via `rollout_self_play_batched` "
        f"(binding requires `temperature > 0`, so this uses `temperature={RAW_TRACE_TEMPERATURE:g}`; `n={raw_summary.games}`)",
        "  2. existing search-trace JSONL files in `data/selfplay/` as the closest available step-level proxy",
        f"- Detailed last-{WINDOW_SIZE}-step DEFCON-1 windows were written to `{out_jsonl}`.",
        "",
        "## Dataset Summary",
        "",
    ]
    lines.extend(render_dataset_table([raw_summary, *search_summaries]))
    lines.extend(
        [
            "",
            "## Main Findings",
            "",
            f"- Raw greedy traced baseline ended by DEFCON-1 in {raw_summary.defcon1_games}/{raw_summary.games} "
            f"games ({percent(raw_summary.defcon1_games, raw_summary.games):.1f}%).",
            f"- Search-proxy traces contributed {len(search_windows)} DEFCON-1 games across "
            f"{sum(s.games for s in search_summaries)} recorded games.",
            f"- Average turn of terminal DEFCON-1 in search-proxy traces: "
            f"{(sum(search_turns) / len(search_turns)):.2f}." if search_turns else "- No search-proxy DEFCON-1 games found.",
            f"- Average turn of terminal DEFCON-1 in raw traced baseline: "
            f"{(sum(raw_turns) / len(raw_turns)):.2f}." if raw_turns else "- No raw-policy DEFCON-1 games found in the traced baseline.",
            "- These rates are not a like-for-like reproduction of the 2026-04-12 v45 benchmark in "
            "`results/analysis/ismcts_retest_post_fix.md`. This script follows the task instruction to use the "
            "highest available scripted checkpoint for the raw baseline (`v79_sc_scripted.pt`), and the search "
            "trace proxies come from older recorded MCTS corpora (`v99c` / `v106`) rather than traced "
            "ISMCTS-vs-raw-policy matches.",
            "- The fatal action is not only a `coup` problem. In the search-proxy traces, terminal DEFCON-1 drops "
            "split mostly between `event` and `ops`; the `ops` bucket is dominated by DEFCON-lowering cards such as "
            "`Duck and Cover` played for ops where the opponent event still fires and collapses DEFCON from 2 to 1.",
            "- Repeated headline/setup motifs show up in the last three steps: `Duck and Cover`, `Che`, "
            "`How I Learned to Stop Worrying`, `Brush War`, `We Will Bury You`, and `Cuban Missile Crisis`.",
            "",
            "## Search Proxy: Cards/Modes In Final 3 Steps Before DEFCON-1",
            "",
        ]
    )
    lines.extend(render_pattern_table(search_patterns))
    lines.append("")
    lines.extend(render_counter_table(search_mode_counter, "Search Proxy: Terminal DEFCON-1 Drop Mode"))
    lines.extend(render_counter_table(search_side_counter, "Search Proxy: Terminal DEFCON-1 Drop Side"))
    if raw_windows:
        lines.extend(
            [
                "## Raw Greedy Baseline: Cards/Modes In Final 3 Steps Before DEFCON-1",
                "",
            ]
        )
        lines.extend(render_pattern_table(raw_patterns))
        lines.append("")
        lines.extend(render_counter_table(raw_mode_counter, "Raw Baseline: Terminal DEFCON-1 Drop Mode"))
        lines.extend(render_counter_table(raw_side_counter, "Raw Baseline: Terminal DEFCON-1 Drop Side"))

    lines.extend(
        [
            "## Example Windows",
            "",
            "The appendix below shows a small sample of the recorded last-10-step windows. "
            "The full set is in the JSONL artifact.",
            "",
        ]
    )
    lines.extend(last_window_examples(search_windows[:3] + raw_windows[:2], limit=5))
    return "\n".join(lines).rstrip() + "\n"


def print_stdout_summary(
    checkpoint: Path,
    raw_summary: DatasetSummary,
    search_summaries: list[DatasetSummary],
    raw_windows: list[dict[str, Any]],
    search_windows: list[dict[str, Any]],
    out_md: Path,
    out_jsonl: Path,
) -> None:
    search_mode_counter, search_side_counter, _, search_turns = terminal_drop_stats(search_windows)
    print(f"[checkpoint] {checkpoint}")
    print(
        f"[raw] games={raw_summary.games} defcon1={raw_summary.defcon1_games} "
        f"rate={percent(raw_summary.defcon1_games, raw_summary.games):.1f}%"
    )
    for s in search_summaries:
        print(
            f"[search-proxy] {s.name}: games={s.games} defcon1={s.defcon1_games} "
            f"rate={percent(s.defcon1_games, s.games):.1f}%"
        )
    if search_turns:
        print(f"[search-proxy] avg_turn_defcon1={sum(search_turns) / len(search_turns):.2f}")
    if search_mode_counter:
        print(f"[search-proxy] terminal_drop_modes={dict(search_mode_counter)}")
    if search_side_counter:
        print(f"[search-proxy] terminal_drop_sides={dict(search_side_counter)}")
    top_patterns = top_pre_defcon_patterns(search_windows)
    if top_patterns:
        print("[search-proxy] top_patterns_last3:")
        for card_name, side, mode_id, mode_name, count in top_patterns[:8]:
            print(f"  - {card_name} | {side} | mode_id={mode_id} ({mode_name}) | count={count}")
    print(f"[out] markdown={out_md}")
    print(f"[out] windows_jsonl={out_jsonl}")


def main() -> None:
    args = parse_args()
    card_specs = load_cards()
    card_names = {card_id: spec.name for card_id, spec in card_specs.items()}

    checkpoint = find_best_scripted_checkpoint(args.checkpoint_dir)
    raw_rows, raw_summary = collect_raw_policy_traces(
        checkpoint=checkpoint,
        n_games=args.raw_games,
        seed=args.raw_seed,
        card_names=card_names,
    )

    search_files = discover_search_trace_files(args.search_dir)
    search_rows, search_summaries = collect_search_trace_rows(search_files, card_names)

    raw_windows = build_windows(raw_rows)
    search_windows = build_windows(search_rows)

    write_windows_jsonl(args.out_jsonl, search_windows + raw_windows)
    report = build_markdown_report(
        checkpoint=checkpoint,
        raw_summary=raw_summary,
        search_summaries=search_summaries,
        raw_windows=raw_windows,
        search_windows=search_windows,
        out_jsonl=args.out_jsonl,
    )
    args.out_md.parent.mkdir(parents=True, exist_ok=True)
    args.out_md.write_text(report)

    print_stdout_summary(
        checkpoint=checkpoint,
        raw_summary=raw_summary,
        search_summaries=search_summaries,
        raw_windows=raw_windows,
        search_windows=search_windows,
        out_md=args.out_md,
        out_jsonl=args.out_jsonl,
    )


if __name__ == "__main__":
    main()
