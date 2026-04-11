"""Pre-training smoke test: run N games to verify model loads and doesn't crash."""
from pathlib import Path
from typing import Tuple


def run_smoke_test(model_path: Path, n_games: int = 10) -> Tuple[bool, str]:
    """Run n_games using tscore.benchmark_batched. Returns (ok, message).

    benchmark_batched requires a TorchScript (.pt) model.  If model_path is a
    plain checkpoint (.pt without _scripted suffix), look for the _scripted.pt
    sibling produced by export_checkpoint().
    """
    try:
        import tscore

        # Prefer the scripted (TorchScript) variant if available.
        scripted_path = model_path.parent / (model_path.stem + "_scripted.pt")
        load_path = scripted_path if scripted_path.exists() else model_path

        results = tscore.benchmark_batched(
            str(load_path),
            tscore.Side.USSR,
            n_games,
            pool_size=4,
        )
        completed = len(results)
        if completed < n_games:
            return False, f"Only {completed}/{n_games} games completed"
        return True, f"Smoke test passed: {completed} games completed"
    except Exception as e:
        return False, f"Smoke test failed: {e}"
