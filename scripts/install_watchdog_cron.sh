#!/usr/bin/env bash
# Run this once to install the stale training watchdog cron job.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
CRON_CMD="*/15 * * * * cd $PROJECT_DIR && uv run python scripts/check_stale_training.py >> results/stale_training.log 2>&1"

# Add to crontab if not already present
(crontab -l 2>/dev/null | grep -v "check_stale_training"; echo "$CRON_CMD") | crontab -
echo "Installed cron: $CRON_CMD"
crontab -l | grep check_stale_training
