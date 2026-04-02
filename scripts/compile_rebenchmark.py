"""Compile rebenchmark results into corrected benchmark_history.json and summary.

Usage:
    uv run python scripts/compile_rebenchmark.py
"""

import json
from pathlib import Path


def main() -> None:
    results_dir = Path("results")
    old_history_path = results_dir / "benchmark_history_pre_defcon_fix.json"
    new_history_path = results_dir / "benchmark_history.json"
    summary_path = results_dir / "rebenchmark_summary.md"

    # Load old history
    old_history = {}
    if old_history_path.exists():
        old_history = json.loads(old_history_path.read_text())

    # Collect rebenchmark results
    new_results: dict[str, dict] = {}
    for f in sorted(results_dir.glob("rebench_v*.json")):
        data = json.loads(f.read_text())
        # Extract version from filename
        version = f.stem.replace("rebench_", "")  # e.g., "v23"
        new_results[version] = data

    if not new_results:
        print("No rebenchmark results found!")
        return

    # Build corrected benchmark_history.json
    corrected_history: dict[str, dict] = {}
    for version, data in sorted(new_results.items(), key=lambda x: _version_sort_key(x[0])):
        corrected_history[version] = {"learned_vs_heuristic": data["learned_win_pct"]}

    new_history_path.write_text(json.dumps(corrected_history, indent=2) + "\n")
    print(f"Wrote corrected history to {new_history_path} ({len(corrected_history)} versions)")

    # Build summary markdown
    lines = [
        "# Rebenchmark Summary: DEFCON-Fixed Heuristic",
        "",
        "All checkpoints rebenchmarked against the current (DEFCON-fixed) heuristic.",
        "- Games per version: 500",
        "- Seed: 9999",
        "- Learned side: USSR",
        "",
        "## Old vs New Win Rates",
        "",
        "| Version | Old Win% | New Win% | Delta |",
        "|---------|----------|----------|-------|",
    ]

    for version in sorted(corrected_history.keys(), key=_version_sort_key):
        new_pct = corrected_history[version]["learned_vs_heuristic"]
        old_pct = old_history.get(version, {}).get("learned_vs_heuristic")
        if old_pct is not None:
            delta = new_pct - old_pct
            delta_str = f"{delta:+.1f}%"
        else:
            old_pct_str = "N/A"
            delta_str = "N/A"
        old_pct_str = f"{old_pct:.1f}%" if old_pct is not None else "N/A"
        lines.append(f"| {version} | {old_pct_str} | {new_pct:.1f}% | {delta_str} |")

    # Summary stats
    deltas = []
    for version in corrected_history:
        old_pct = old_history.get(version, {}).get("learned_vs_heuristic")
        new_pct = corrected_history[version]["learned_vs_heuristic"]
        if old_pct is not None:
            deltas.append(new_pct - old_pct)

    if deltas:
        avg_delta = sum(deltas) / len(deltas)
        min_delta = min(deltas)
        max_delta = max(deltas)
        lines.extend([
            "",
            "## Summary Statistics",
            "",
            f"- Versions compared: {len(deltas)}",
            f"- Average delta: {avg_delta:+.1f}%",
            f"- Min delta: {min_delta:+.1f}%",
            f"- Max delta: {max_delta:+.1f}%",
            f"- Best new win%: {max(v['learned_vs_heuristic'] for v in corrected_history.values()):.1f}%",
            f"- Worst new win%: {min(v['learned_vs_heuristic'] for v in corrected_history.values()):.1f}%",
        ])

    lines.append("")
    summary_path.write_text("\n".join(lines))
    print(f"Wrote summary to {summary_path}")


def _version_sort_key(v: str) -> int:
    """Sort v23, v24, ... numerically."""
    import re
    m = re.search(r"(\d+)", v)
    return int(m.group(1)) if m else 0


if __name__ == "__main__":
    main()
