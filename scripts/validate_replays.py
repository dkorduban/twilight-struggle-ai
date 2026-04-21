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


def serialize_violation(game_name: str, result, violation) -> dict:
    data = asdict(violation)
    data["kind"] = violation.kind.value
    data["phasing"] = violation.phasing.value
    data["game"] = game_name
    data["game_id"] = result.game_id
    return data


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
    return 1 if report["summary"]["parse_failures"] else 0


if __name__ == "__main__":
    sys.exit(main())
