"""Pre-training smoke test: run N games to verify model loads and doesn't crash."""
from pathlib import Path
from typing import Tuple


def run_smoke_test(model_path: Path, n_games: int = 10) -> Tuple[bool, str]:
    """Run n_games using tscore.benchmark_batched. Returns (ok, message)."""
    try:
        import tscore
        results = tscore.benchmark_batched(
            str(model_path),
            str(model_path),
            n_games,
            pool_size=4,
        )
        completed = len(results)
        if completed < n_games:
            return False, f"Only {completed}/{n_games} games completed"
        return True, f"Smoke test passed: {completed} games completed"
    except Exception as e:
        return False, f"Smoke test failed: {e}"
