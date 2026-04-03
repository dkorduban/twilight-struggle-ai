"""Reproducibility provenance tracking.

Captures git state, file fingerprints, and binary hashes at the start of any
training run, benchmark, or data collection. Designed to be called from scripts
and optionally published to W&B.

Usage::

    from tsrl.provenance import capture_provenance, log_provenance_wandb

    prov = capture_provenance(
        input_files=["data/combined_v87/*.parquet"],
        binaries=["build-ninja/cpp/tools/ts_collect_selfplay_rows_jsonl"],
    )
    # prov is a dict with git_sha, git_dirty, git_diff_summary, file_fingerprints, etc.

    # Optionally log to wandb:
    log_provenance_wandb(prov)

    # Or save to JSON alongside output:
    save_provenance(prov, "data/checkpoints/retrain_v87/provenance.json")
"""

from __future__ import annotations

import hashlib
import html as _html
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _run_git(*args: str) -> str:
    """Run a git command and return stripped stdout, or '' on failure."""
    try:
        result = subprocess.run(
            ["git", *args],
            capture_output=True,
            text=True,
            timeout=10,
        )
        return result.stdout.strip()
    except Exception:
        return ""


def _file_sha256(path: Path) -> str:
    """Compute SHA-256 of a file. Returns '' if file doesn't exist."""
    if not path.exists():
        return ""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _file_fingerprint(path: Path) -> dict[str, Any]:
    """Return size + SHA-256 for a single file."""
    if not path.exists():
        return {"path": str(path), "exists": False}
    return {
        "path": str(path),
        "exists": True,
        "size_bytes": path.stat().st_size,
        "sha256": _file_sha256(path),
    }


def _resolve_globs(patterns: list[str]) -> list[Path]:
    """Expand glob patterns to concrete file paths."""
    result: list[Path] = []
    for pattern in patterns:
        p = Path(pattern)
        if "*" in pattern or "?" in pattern:
            # Glob pattern — resolve relative to cwd
            parts = pattern.split("/")
            # Find the first part with a glob character
            base = Path(".")
            glob_part = pattern
            for i, part in enumerate(parts):
                if "*" in part or "?" in part:
                    base = Path("/".join(parts[:i])) if i > 0 else Path(".")
                    glob_part = "/".join(parts[i:])
                    break
            result.extend(sorted(base.glob(glob_part)))
        elif p.is_dir():
            result.extend(sorted(p.glob("**/*")))
        elif p.exists():
            result.append(p)
    return result


def capture_provenance(
    input_files: list[str] | None = None,
    binaries: list[str] | None = None,
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Capture full reproducibility provenance.

    Parameters
    ----------
    input_files
        Glob patterns or paths to input data files. Each file gets a SHA-256
        fingerprint recorded.
    binaries
        Paths to compiled binaries (C++ tools, .so files). Each gets
        fingerprinted.
    extra
        Any additional metadata to include (e.g., CLI args, config).

    Returns
    -------
    dict
        Provenance record with git state, file fingerprints, timestamps.
    """
    prov: dict[str, Any] = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "git_sha": _run_git("rev-parse", "HEAD"),
        "git_branch": _run_git("rev-parse", "--abbrev-ref", "HEAD"),
        "git_dirty": _run_git("status", "--porcelain") != "",
    }

    # Git diff: stat summary + full unified diff
    diff_stat = _run_git("diff", "--stat")
    if diff_stat:
        prov["git_diff_summary"] = diff_stat.split("\n")[-1].strip()
        prov["git_dirty_files"] = _run_git("diff", "--name-only").split("\n")
        prov["git_diff"] = _run_git("diff", "HEAD")  # full unified diff
    else:
        prov["git_diff_summary"] = ""
        prov["git_dirty_files"] = []
        prov["git_diff"] = ""

    # Input file fingerprints
    if input_files:
        resolved = _resolve_globs(input_files)
        prov["input_files"] = [_file_fingerprint(p) for p in resolved]
        prov["input_file_count"] = len(resolved)
        prov["input_total_bytes"] = sum(
            fp["size_bytes"] for fp in prov["input_files"] if fp.get("exists")
        )
    else:
        prov["input_files"] = []
        prov["input_file_count"] = 0
        prov["input_total_bytes"] = 0

    # Binary fingerprints
    if binaries:
        resolved_bins = _resolve_globs(binaries)
        prov["binaries"] = [_file_fingerprint(p) for p in resolved_bins]
    else:
        prov["binaries"] = []

    # Extra metadata
    if extra:
        prov["extra"] = extra

    return prov


def save_provenance(prov: dict[str, Any], path: str | Path) -> None:
    """Save provenance record to a JSON file."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(prov, indent=2, default=str) + "\n")


def _diff_to_html(diff_text: str) -> str:
    """Convert a unified diff to syntax-highlighted HTML."""
    if not diff_text:
        return "<pre><em>No uncommitted changes.</em></pre>"
    lines = []
    for line in diff_text.split("\n"):
        escaped = _html.escape(line)
        if line.startswith("+++") or line.startswith("---"):
            lines.append(f'<span style="font-weight:bold">{escaped}</span>')
        elif line.startswith("+"):
            lines.append(f'<span style="color:#22863a;background:#f0fff4">{escaped}</span>')
        elif line.startswith("-"):
            lines.append(f'<span style="color:#b31d28;background:#ffeef0">{escaped}</span>')
        elif line.startswith("@@"):
            lines.append(f'<span style="color:#005cc5">{escaped}</span>')
        elif line.startswith("diff ") or line.startswith("index "):
            lines.append(f'<span style="color:#6a737d">{escaped}</span>')
        else:
            lines.append(escaped)
    body = "\n".join(lines)
    return (
        '<html><body><pre style="font-family:monospace;font-size:12px;'
        f'line-height:1.4;white-space:pre-wrap">{body}</pre></body></html>'
    )


def log_provenance_wandb(prov: dict[str, Any]) -> None:
    """Log provenance to the active W&B run's config."""
    try:
        import wandb

        if wandb.run is None:
            return

        # Flatten for wandb config
        wandb.config.update(
            {
                "provenance/git_sha": prov.get("git_sha", ""),
                "provenance/git_branch": prov.get("git_branch", ""),
                "provenance/git_dirty": prov.get("git_dirty", False),
                "provenance/git_diff_summary": prov.get("git_diff_summary", ""),
                "provenance/input_file_count": prov.get("input_file_count", 0),
                "provenance/input_total_bytes": prov.get("input_total_bytes", 0),
                "provenance/timestamp": prov.get("timestamp", ""),
            },
            allow_val_change=True,
        )

        # Log git diff as rich HTML — visible in the run's Media tab
        diff_text = prov.get("git_diff", "")
        wandb.log({"git_diff": wandb.Html(_diff_to_html(diff_text))}, step=0)

        # Log full provenance as an artifact for detailed inspection
        artifact = wandb.Artifact(
            name=f"provenance-{prov.get('git_sha', 'unknown')[:8]}",
            type="provenance",
        )
        import tempfile

        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False
        ) as f:
            json.dump(prov, f, indent=2, default=str)
            f.flush()
            artifact.add_file(f.name, name="provenance.json")
        wandb.log_artifact(artifact)
    except Exception as e:
        print(f"[provenance] W&B logging failed (non-fatal): {e}")
