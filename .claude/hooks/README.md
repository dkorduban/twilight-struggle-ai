# Project hooks

- `prevent_dangerous_bash.py`: blocks obviously destructive shell commands and obvious secret-exfiltration shells.
- `prevent_protected_writes.py`: blocks edits/writes into secrets and generated-artifact paths.
- `run-targeted-checks.py`: async, best-effort quick checks after edits/writes.
- `log_config_change.py`: reminds Claude to re-check config after settings or skills change.

Design goals:
- no external dependencies like `jq`
- deterministic and cheap enough for a Pro-plan workflow
- keep noisy checks out of the main transcript unless they matter
