import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).parents[2] / "scripts" / "bench_jit.py"


def _jit_available() -> bool:
    if shutil.which("uv") is None:
        return False
    result = subprocess.run(
        [
            "uv",
            "run",
            "--python",
            "3.14",
            "python",
            "-c",
            "from sys import _jit; exit(0 if _jit.is_available() else 1)",
        ],
        capture_output=True,
    )
    return result.returncode == 0


def _run_jit_worker(
    mode: str,
    jit_value: str,
    *extra_args: str,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            "uv",
            "run",
            "--python",
            "3.14",
            "python",
            str(SCRIPT),
            "--worker",
            mode,
            *extra_args,
        ],
        capture_output=True,
        text=True,
        check=True,
        env={**os.environ, "PYTHON_JIT": jit_value},
    )


needs_jit = pytest.mark.skipif(not _jit_available(), reason="uv + Python 3.14 + JIT not available")


@pytest.mark.serial
def test_setup_check_exits_cleanly():
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--setup-check"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode in {0, 1}
    assert "traceback" not in result.stderr.lower()


@pytest.mark.serial
@needs_jit
def test_worker_jit_disabled_json():
    result = _run_jit_worker(
        "jit_disabled",
        "0",
        "--n-warmup",
        "1",
        "--n-bench",
        "2",
        "--seed",
        "0",
    )
    payload = json.loads(result.stdout)
    assert payload["mode"] == "jit_disabled"
    assert payload["rollouts_per_second"] > 0
    assert payload["n_completed"] == 2


@pytest.mark.serial
@needs_jit
def test_worker_jit_enabled_json():
    result = _run_jit_worker(
        "jit_enabled",
        "1",
        "--n-warmup",
        "1",
        "--n-bench",
        "2",
        "--seed",
        "0",
    )
    payload = json.loads(result.stdout)
    assert payload["mode"] == "jit_enabled"
    assert payload["jit_enabled"] is True
    assert payload["n_completed"] == 2


@pytest.mark.serial
@needs_jit
def test_coordinator_json_output():
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--json",
            "--n-warmup",
            "1",
            "--n-bench",
            "2",
            "--seed",
            "0",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)
    assert "jit_disabled" in payload
    assert "jit_enabled" in payload


@pytest.mark.serial
@needs_jit
def test_rollout_count_sanity():
    result = _run_jit_worker(
        "jit_disabled",
        "0",
        "--n-bench",
        "3",
        "--n-warmup",
        "1",
        "--seed",
        "0",
    )
    payload = json.loads(result.stdout)
    assert payload["n_completed"] == 3
