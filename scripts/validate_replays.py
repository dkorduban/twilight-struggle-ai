#!/usr/bin/env python3
"""Run replay validation and write JSON/Markdown triage reports."""

import argparse
import json
import sys
from collections import Counter
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

from tsrl.etl.validator import validate_log_dir

DEFAULT_KINDS = (
    "SCORING_VP_MISMATCH,TARGET_ILLEGAL,"
    "RESHUFFLE_EMPTY_DISCARD,HEADLINE_ORDER_MISMATCH"
)
DEFAULT_VIOLATIONS_JSONL = Path("results/validator_violations.jsonl")


def serialize_violation(game_name: str, result, violation) -> dict:
    data = asdict(violation)
    data["kind"] = violation.kind.value
    data["phasing"] = violation.phasing.value
    data["game"] = game_name
    data["game_id"] = result.game_id
    return data


def _write_scoring_violation_jsonl(log_dir: Path, results: dict, out: Path) -> int:
    from tsrl.engine.scoring import apply_scoring_card
    from tsrl.etl.game_data import load_cards, load_countries
    from tsrl.etl.parser import parse_replay
    from tsrl.etl.reducer import reduce_game
    from tsrl.etl.resolver import resolve_names
    from tsrl.schemas import EventKind, PublicState, Region, Side

    cards = load_cards()
    countries = load_countries()
    all_card_ids = frozenset(cid for cid in cards if cid != 6)
    card_regions = {
        1: Region.ASIA,
        2: Region.EUROPE,
        3: Region.MIDDLE_EAST,
        40: Region.CENTRAL_AMERICA,
        41: Region.SOUTHEAST_ASIA,
        80: Region.AFRICA,
        82: Region.SOUTH_AMERICA,
    }
    stop_kinds = {
        EventKind.PLAY,
        EventKind.ACTION_ROUND_START,
        EventKind.HEADLINE_PHASE_START,
        EventKind.TURN_END,
        EventKind.HEADLINE,
    }

    def other_side(side: Side) -> Side:
        return Side.US if side == Side.USSR else Side.USSR

    def controls(side: Side, cid: int, pub: PublicState) -> bool:
        spec = countries[cid]
        if spec.stability <= 0:
            return False
        own = pub.influence.get((side, cid), 0)
        opp = pub.influence.get((other_side(side), cid), 0)
        return own >= opp + spec.stability

    def region_ids_for(card_id: int) -> list[int]:
        region = card_regions[card_id]
        regions = (Region.ASIA, Region.SOUTHEAST_ASIA) if card_id == 1 else (region,)
        return [
            cid for cid, spec in sorted(countries.items())
            if spec.region in regions and spec.stability > 0
        ]

    def region_snapshot(card_id: int, pub: PublicState) -> dict:
        ids = region_ids_for(card_id)
        battleground_ids = [
            cid for cid in ids
            if countries[cid].is_battleground or (cid == 85 and pub.formosan_active)
        ]
        total_bgs = len(battleground_ids)

        def counts(side: Side) -> tuple[int, int, int]:
            bgs = sum(1 for cid in battleground_ids if controls(side, cid, pub))
            non_bgs = sum(
                1 for cid in ids
                if cid not in battleground_ids and controls(side, cid, pub)
            )
            return bgs, non_bgs, bgs + non_bgs

        def tier(own: tuple[int, int, int], opp: tuple[int, int, int]) -> str:
            bgs, non_bgs, total = own
            opp_bgs, _, opp_total = opp
            if total_bgs > 0 and bgs == total_bgs and total > opp_total:
                return "Control"
            if total > opp_total and bgs > opp_bgs and bgs >= 1 and non_bgs >= 1:
                return "Domination"
            if total >= 1:
                return "Presence"
            return "None"

        us_counts = counts(Side.US)
        ussr_counts = counts(Side.USSR)
        us_tier = tier(us_counts, ussr_counts)
        ussr_tier = tier(ussr_counts, us_counts)
        return {
            "ussr_influence_by_country": {
                countries[cid].name: pub.influence.get((Side.USSR, cid), 0) for cid in ids
            },
            "us_influence_by_country": {
                countries[cid].name: pub.influence.get((Side.US, cid), 0) for cid in ids
            },
            "control_us": [countries[cid].name for cid in ids if controls(Side.US, cid, pub)],
            "control_ussr": [countries[cid].name for cid in ids if controls(Side.USSR, cid, pub)],
            "presence_us": us_counts[2] > 0,
            "presence_ussr": ussr_counts[2] > 0,
            "domination_us": us_tier == "Domination",
            "domination_ussr": ussr_tier == "Domination",
            "battlegrounds_controlled_us": [
                countries[cid].name for cid in battleground_ids if controls(Side.US, cid, pub)
            ],
            "battlegrounds_controlled_ussr": [
                countries[cid].name for cid in battleground_ids if controls(Side.USSR, cid, pub)
            ],
            "tier_us": us_tier,
            "tier_ussr": ussr_tier,
        }

    lines: list[str] = []
    for game_name, validation_result in sorted(results.items()):
        path = log_dir / game_name
        if not path.exists():
            continue
        parsed = parse_replay(path.read_text())
        resolved = resolve_names(parsed.events, cards, countries, warn_unresolved=False)
        states = reduce_game(resolved, all_card_ids, check_invariants=False)

        for i, ev in enumerate(resolved):
            spec = cards.get(ev.card_id) if ev.card_id is not None else None
            if ev.kind != EventKind.PLAY or spec is None or not spec.is_scoring:
                continue
            if ev.card_id not in card_regions:
                continue

            pub_before = states[i - 1][0] if i > 0 else PublicState()
            engine_vp = apply_scoring_card(ev.card_id, pub_before).vp_delta
            logged_vp = 0
            for next_ev in resolved[i + 1:]:
                if next_ev.kind in stop_kinds:
                    break
                if next_ev.kind == EventKind.VP_CHANGE and next_ev.amount is not None:
                    logged_vp += next_ev.amount
            if logged_vp == engine_vp:
                continue

            row = {
                "kind": "SCORING_VP_MISMATCH",
                "game": game_name,
                "game_id": validation_result.game_id,
                "turn": ev.turn,
                "side": ev.phasing.name,
                "card_id": ev.card_id,
                "card_name": spec.name,
                "region": card_regions[ev.card_id].name.title().replace("_", " "),
                "expected_vp": logged_vp,
                "actual_vp": engine_vp,
                "delta": engine_vp - logged_vp,
            }
            row.update(region_snapshot(ev.card_id, pub_before))
            lines.append(json.dumps(row, sort_keys=True))

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + ("\n" if lines else ""))
    return len(lines)


def main() -> int:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--log-dir", default="data/raw_logs")
    parser.add_argument(
        "--out",
        type=Path,
        default=Path(f"results/analysis/validate_replays_{stamp}.json"),
    )
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--filter-kind", default=DEFAULT_KINDS)
    parser.add_argument(
        "--violations-jsonl",
        type=Path,
        default=DEFAULT_VIOLATIONS_JSONL,
        help="Write detailed SCORING_VP_MISMATCH rows to this JSONL path.",
    )
    parser.add_argument("--no-violations-jsonl", action="store_true")
    args = parser.parse_args()

    raw_results = validate_log_dir(args.log_dir)
    results = {k: v for k, v in raw_results.items() if k.startswith("tsreplayer_")} or raw_results
    kinds = {part.strip() for part in args.filter_kind.split(",") if part.strip()}
    violations = [
        serialize_violation(game_name, result, violation)
        for game_name, result in results.items()
        for violation in result.violations
        if violation.kind.value in kinds
    ]
    report = {
        "summary": {
            "games": len(results),
            "decisions": sum(result.total_decisions for result in results.values()),
            "parse_failures": sum(result.total_decisions == 0 for result in results.values()),
            "violations_total": len(violations),
            "violations_by_kind": dict(sorted(Counter(v["kind"] for v in violations).items())),
        },
        "violations": violations,
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    jsonl_count = 0
    if not args.no_violations_jsonl:
        jsonl_count = _write_scoring_violation_jsonl(
            Path(args.log_dir),
            results,
            args.violations_jsonl,
        )
    md_path = args.out.with_suffix(".md")
    summary = report["summary"]
    lines = [
        "# Replay Validation Triage",
        "",
        f"- Games: {summary['games']}",
        f"- Decisions: {summary['decisions']}",
        f"- Parse failures: {summary['parse_failures']}",
        f"- Violations total: {summary['violations_total']}",
        f"- Included kinds: {', '.join(sorted(kinds))}",
        "",
        "## Violations by kind",
        "",
    ]
    lines += [f"- {kind}: {count}" for kind, count in summary["violations_by_kind"].items()]
    lines += [
        "",
        "## Top-5 root causes",
        "",
        "| Rank | Kind | Card ID | Count |",
        "|---:|---|---:|---:|",
    ]
    top = Counter((v["kind"], v["card_id"]) for v in violations).most_common(5)
    for rank, ((kind, card_id), count) in enumerate(top, 1):
        lines.append(f"| {rank} | {kind} | {card_id or ''} | {count} |")
    md_path.write_text("\n".join(lines) + "\n")

    if args.verbose:
        print(json.dumps(report["summary"], indent=2, sort_keys=True))
        print(f"Wrote {args.out}")
        print(f"Wrote {md_path}")
        if not args.no_violations_jsonl:
            print(f"Wrote {args.violations_jsonl} ({jsonl_count} rows)")
    return 1 if report["summary"]["parse_failures"] else 0


if __name__ == "__main__":
    sys.exit(main())
