"""
Fetch a raw Twilight Struggle log from ts-replayer.fly.dev.

Usage:
    uv run python scripts/fetch_tsreplayer_log.py <game_id> [--out-dir data/raw_logs]

The site embeds game data as an inline JSON array in the page HTML.
Each array element has a `text` field containing the multi-line log text
for that turn/AR. This script concatenates those fields in order.

Exit 0: log written to <out_dir>/tsreplayer_<game_id>.txt
Exit 1: could not extract log (instructions printed to stderr)
"""

import argparse
import json
import re
import sys
from pathlib import Path


_REPLAY_URL = "https://ts-replayer.fly.dev/replay/{game_id}/"

# The JSON array is embedded in a <script id="all-turns" type="application/json"> tag.
_ARRAY_PATTERN = re.compile(
    r'<script[^>]+id=["\']all-turns["\'][^>]*>(.*?)</script>', re.DOTALL
)


def fetch_log(game_id: int) -> str:
    """Fetch and return concatenated log text for a game."""
    try:
        import urllib.request
        url = _REPLAY_URL.format(game_id=game_id)
        req = urllib.request.Request(url, headers={"User-Agent": "ts-log-fetcher/1.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            html = resp.read().decode("utf-8", errors="replace")
    except Exception as exc:
        raise RuntimeError(f"HTTP fetch failed: {exc}") from exc

    m = _ARRAY_PATTERN.search(html)
    if not m:
        raise RuntimeError(
            "Could not find inline JSON array in page HTML. "
            "The site structure may have changed."
        )

    try:
        turns = json.loads(m.group(1))
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"JSON parse failed: {exc}") from exc

    if not isinstance(turns, list) or not turns:
        raise RuntimeError("Parsed JSON is not a non-empty list.")

    parts = []
    for entry in turns:
        text = entry.get("text", "")
        if text:
            parts.append(text.strip())

    if not parts:
        raise RuntimeError("No `text` fields found in JSON entries.")

    return "\n\n".join(parts) + "\n"


def print_manual_instructions(game_id: int) -> None:
    url = _REPLAY_URL.format(game_id=game_id)
    print(
        f"\nAutomatic extraction failed for game {game_id}.\n"
        f"To extract manually:\n"
        f"  1. Open {url} in a browser.\n"
        f"  2. Open DevTools → Console and paste:\n\n"
        "// Block 1: extract inline JSON array\n"
        "(function() {\n"
        "  const scripts = document.querySelectorAll('script');\n"
        "  const style = document.querySelector('style');\n"
        "  if (style && style.nextSibling) {\n"
        "    const raw = style.nextSibling.textContent || '';\n"
        "    const m = raw.match(/^\\s*(\\[.*\\])\\s*$/s);\n"
        "    if (m) {\n"
        "      const turns = JSON.parse(m[1]);\n"
        "      window.__TS_FULL_LOG__ = turns.map(t => t.text || '').filter(Boolean).join('\\n\\n');\n"
        "      console.log('Log extracted, ' + turns.length + ' turns. Run: copy(window.__TS_FULL_LOG__)');\n"
        "    } else { console.log('Pattern not found'); }\n"
        "  } else { console.log('No style/sibling found'); }\n"
        "})();\n\n"
        "  3. Then run: copy(window.__TS_FULL_LOG__)\n"
        f"  4. Paste clipboard into data/raw_logs/tsreplayer_{game_id}.txt\n",
        file=sys.stderr,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("game_id", type=int, help="Numeric game ID from ts-replayer.fly.dev")
    parser.add_argument(
        "--out-dir",
        default="data/raw_logs",
        help="Directory to write the log file (default: data/raw_logs)",
    )
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"tsreplayer_{args.game_id}.txt"

    try:
        log_text = fetch_log(args.game_id)
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        print_manual_instructions(args.game_id)
        sys.exit(1)

    out_path.write_text(log_text, encoding="utf-8")
    print(f"Wrote {len(log_text)} bytes to {out_path}")


if __name__ == "__main__":
    main()
