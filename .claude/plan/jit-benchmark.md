# Plan: Python 3.14 JIT Self-Play Rollout Benchmark

## Goal

A standalone script `scripts/bench_jit.py` that:
1. Requires Python 3.14 with JIT compiled in (via uv or custom build)
2. Launches two worker subprocesses — one with `PYTHON_JIT=0`, one with `PYTHON_JIT=1`
3. Measures self-play rollout throughput (rollouts/s) for each mode using `play_random_game()`
4. Prints a comparison table showing speedup ratio

---

## 0. Python 3.14 + JIT Setup

### What the JIT requires

The JIT compiler must be compiled into the Python binary (`--enable-experimental-jit` build flag). The `PYTHON_JIT=1` env var enables it at runtime; `PYTHON_JIT=0` disables it. Both require a JIT-capable build.

JIT detection at runtime via `sys._jit` (Python 3.14+):
```python
from sys import _jit
_jit.is_available()  # JIT compiled in? — use for setup verification
_jit.is_enabled()    # JIT enabled for this process? — use for worker reporting
# Note: _jit.is_active() is a debug-only signal; do not use for verification or reporting.
```

### uv + Python 3.14 (try first)

uv distributes Python from `python-build-standalone` (Astral), not python.org. JIT availability in these builds on Linux/x86_64 is **not guaranteed**. Always verify with `--setup-check` before running.

```bash
# Install Python 3.14
uv python install 3.14

# Verify JIT is compiled in
uv run --python 3.14 scripts/bench_jit.py --setup-check
```

`--setup-check` prints Python version, `_jit.is_available()`, `_jit.is_enabled()`, and exits 0 if JIT is available, 1 if not, with targeted instructions.

### Linux: getting a JIT-capable build (if uv build lacks JIT)

Preferred: use pyenv with the JIT configure flag (avoids downloading third-party install scripts):

```bash
# Install LLVM 21 via apt (required to compile JIT stencils)
sudo apt-get install llvm-21 clang-21

# Install Python 3.14 with JIT via pyenv
PYTHON_CONFIGURE_OPTS='--enable-experimental-jit' pyenv install 3.14.3

# Verify
PYTHON_JIT=1 pyenv exec python3 -c "from sys import _jit; print('JIT:', _jit.is_available(), _jit.is_enabled())"

# Run benchmark using pyenv interpreter
uv run --python $(pyenv which python3) scripts/bench_jit.py
```

Alternative: build CPython from source with the same `--enable-experimental-jit=yes` flag, then `uv run --python /path/to/python3 scripts/bench_jit.py`.

---

## 1. Rollout Hot Path

The measurement target is `play_random_game()` in `python/tsrl/engine/game_loop.py`:

```
play_random_game(seed=N)    ← timed unit of work
  └─ _run_headline_phase() + _run_action_rounds() × 6-7 per turn × 10 turns
       ├─ legal_actions.py   (frozenset ops, dict lookups)
       ├─ step.py            (PublicState copy, influence dict mutation)
       ├─ scoring.py
       └─ events.py / cat_c_events.py
```

This is the pure random-policy game loop using `make_random_policy`. There is no MCTS candidate sampling or state cloning overhead from a search tree.

Since `tscore` C++ bindings are currently a stub, all hot-path time is pure Python.

Two measurement levels:
- **Level 1 (default):** `play_random_game(seed=N)` — random policy both sides, reports rollouts/s
- **Level 2 (`--with-mcts`):** `collect_self_play_game(n_sim=N, use_uct=True)` — MCTS overhead included, reports rollouts/s and steps/s

Level 1 reports rollouts/s only (no steps/s — `play_random_game` does not return a step count).
Level 2 reports both rollouts/s and steps/s from the same `collect_self_play_game` call.

---

## 2. Subprocess Architecture

The benchmark must launch two worker subprocesses with different `PYTHON_JIT` values — the JIT cannot be toggled at runtime.

```
coordinator (runs under any Python, uses uv to target 3.14)
  pre-flight:
    1. shutil.which("uv") — uv installed? if not: exit(1) with install instructions
    2. uv run --python 3.14 -c "from sys import _jit; exit(0 if _jit.is_available() else 1)"
       if fails: exit(1) with setup instructions (point to --setup-check output)

  workers:
    PYTHON_JIT=0  uv run --python 3.14 scripts/bench_jit.py --worker jit_disabled ...
    PYTHON_JIT=1  uv run --python 3.14 scripts/bench_jit.py --worker jit_enabled  ...
    each prints JSON to stdout

coordinator collects JSON, computes speedup, prints table or JSON
```

The coordinator always uses `uv run --python 3.14` (never `sys.executable`) to launch workers. This ensures workers run on 3.14 regardless of which Python the coordinator runs under.

If pre-flight fails, exit(1) with clear instructions. There is no single-mode fallback — the entire purpose of this script is the JIT comparison.

---

## 3. Benchmark Structure (worker side)

Following `python/tsrl/policies/benchmark_hybrid_vs_random.py` conventions:

```
Phase 1 — import warmup (untimed)
  sys.path.insert, import tsrl modules, load cards/countries data

Phase 2 — rollout warmup: N_WARMUP (default 5) calls to play_random_game()
  Warms Python internal caches before JIT stencil emission window

Phase 3 — timed batch: gc.disable(), time.perf_counter_ns() bracket
  N_BENCH (default 20) calls to play_random_game(seed=BASE_SEED + i)
  Reports rollouts/s from timed wall-clock window

Seed policy: game i uses seed = BASE_SEED + i (zero-indexed within the timed batch).
Both workers use the same seed schedule so they benchmark identical game sequences.

Phase 4 — optional MCTS (--with-mcts):
  Same warmup+timed structure using collect_self_play_game(n_sim=N_SIM, use_uct=True)
  Reports rollouts/s and steps/s (step count from returned step list)

Output: JSON to stdout
{
  "mode": "jit_enabled",
  "python_version": "3.14.3 (main, ...)",
  "jit_available": true,
  "jit_enabled": true,
  "n_warmup": 5,
  "n_bench": 20,
  "n_completed": 20,          ← actual games finished (== n_bench on success)
  "rollout_seconds": 4.23,
  "rollouts_per_second": 4.73,
  "mcts": null
}

`n_completed` is incremented inside the timed loop after each successful `play_random_game()` call. It must equal `n_bench` for a clean run. The field provides a concrete, assertable observable for tests.
```

---

## 4. C++ Overhead Note

The `tscore` C++ bindings are currently a stub with no exported symbols — all measured time is pure Python. The script notes this in its output.

---

## 5. Output Format

Default text table (matching existing benchmark style):
```
Twilight Struggle self-play rollout JIT benchmark
Python       : 3.14.3 (main, ...) [GCC ...]
Workload     : play_random_game() — random policy, both sides
Note         : C++ engine bindings are a stub; all timing is pure Python.
Warmup games : 5
Timed games  : 20

mode           rollouts/s   speedup
-----------  -----------  --------
JIT disabled        4.73     1.00x
JIT enabled         6.11     1.29x
```

With `--json`: coordinator emits a single JSON object:
```json
{
  "python_version": "3.14.3 ...",
  "jit_disabled": { ...worker JSON for jit_disabled mode... },
  "jit_enabled":  { ...worker JSON for jit_enabled mode... },
  "speedup_rollouts": 1.29
}
```
Top-level keys use the worker mode names (`jit_disabled`, `jit_enabled`) for consistency.

---

## 6. Files to Create

| File | Purpose |
|------|---------|
| `scripts/bench_jit.py` | Main benchmark script |
| `tests/python/test_bench_jit.py` | Tests for worker JSON output + setup-check + coordinator |

No `pyproject.toml` changes. No new dependencies (all stdlib + existing tsrl).

---

## 7. `scripts/bench_jit.py` Structure

```python
"""
Benchmark: Python 3.14 experimental JIT vs no-JIT on TS self-play rollouts.

Usage:
    uv run --python 3.14 scripts/bench_jit.py [OPTIONS]

    # Or with a custom JIT-capable Python:
    uv run --python /path/to/python3 scripts/bench_jit.py [OPTIONS]

Options:
    --n-warmup N     Warmup rollouts per mode (default: 5)
    --n-bench N      Timed rollouts per mode (default: 20)
    --with-mcts      Also benchmark MCTS self-play (slow)
    --n-sim N        MCTS simulations per move when --with-mcts (default: 10)
    --seed N         Base RNG seed (default: 42)
    --json           Emit JSON output instead of text table
    --setup-check    Verify Python 3.14 + JIT availability and exit
    --worker MODE    Internal: run worker (jit_disabled|jit_enabled)

Setup:
    uv python install 3.14
    uv run --python 3.14 scripts/bench_jit.py --setup-check
    # If JIT not available on Linux, see --setup-check output for instructions.
"""

def _print_setup_check() -> int:
    """Check Python 3.14 + JIT; return exit code (0=ok, 1=problem)."""
    # prints version, _jit.is_available(), _jit.is_enabled(), instructions if absent
    ...

def _worker_main(args) -> None:
    """Run benchmark in this process, print JSON to stdout."""
    # 1. detect JIT status via _jit.is_available() / _jit.is_enabled()
    # 2. sys.path.insert(0, ...) — same pattern as scripts/run_mcts_game.py
    # 3. import play_random_game, collect_self_play_game
    # 4. warmup phase (play_random_game)
    # 5. timed batch: gc.disable(), perf_counter_ns(), play_random_game() loop
    # 6. optional MCTS phase: collect_self_play_game(n_sim, use_uct=True)
    # 7. print JSON (jit_available, jit_enabled — no jit_active)
    ...

def _coordinator_main(args) -> None:
    """Pre-flight checks, launch two workers, collect JSON, print result."""
    # 1. shutil.which("uv") — exit(1) if missing
    # 2. probe subprocess: uv run --python 3.14 -c "_jit.is_available()" — exit(1) if fails
    # 3. for mode in [("jit_disabled","0"), ("jit_enabled","1")]:
    #      subprocess.run(["uv","run","--python","3.14",
    #                      str(script_path), "--worker", mode, ...],
    #                     env={**os.environ, "PYTHON_JIT": jit_val}, ...)
    # 4. parse JSON from each; compute speedup
    # 5. print table or JSON
    ...

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    # args: --n-warmup, --n-bench, --with-mcts, --n-sim, --seed, --json, --setup-check, --worker
    args = parser.parse_args()
    if args.setup_check:
        return _print_setup_check()
    if args.worker:
        _worker_main(args)
    else:
        _coordinator_main(args)
    return 0
```

---

## 8. `tests/python/test_bench_jit.py`

Five tests, all marked `@pytest.mark.serial` (subprocess-based, ~2–10s each).

Tests 1, 2, 4, 5 invoke the script via `uv run --python 3.14 python scripts/bench_jit.py ...`.
These four are individually decorated with a `@pytest.mark.skipif` guard (not module-level, so test 3 is unaffected):

```python
import shutil, subprocess, sys, pytest

def _jit_available() -> bool:
    if shutil.which("uv") is None:
        return False
    r = subprocess.run(
        ["uv", "run", "--python", "3.14", "python", "-c",
         "from sys import _jit; exit(0 if _jit.is_available() else 1)"],
        capture_output=True,
    )
    return r.returncode == 0

needs_jit = pytest.mark.skipif(not _jit_available(), reason="uv + Python 3.14 + JIT not available")
```

Tests:

1. **jit_disabled worker produces valid JSON** (`@needs_jit`) — invoke `uv run --python 3.14 python scripts/bench_jit.py --worker jit_disabled --n-warmup 1 --n-bench 2 --seed 0` with env `PYTHON_JIT=0`; assert JSON parseable, `mode == "jit_disabled"`, `rollouts_per_second > 0`, `n_completed == 2`.
2. **jit_enabled worker produces valid JSON** (`@needs_jit`) — same with `--worker jit_enabled` and env `PYTHON_JIT=1`; assert `mode == "jit_enabled"`, `rollouts_per_second > 0`, `n_completed == 2`, `jit_enabled == True`.
3. **`--setup-check` exits 0 or 1 without crashing** (no skipif — runs on any Python) — invoke `sys.executable scripts/bench_jit.py --setup-check`; assert returncode in {0, 1}, no traceback in stderr.
4. **`--json` coordinator produces parseable JSON** (`@needs_jit`) — invoke `uv run --python 3.14 python scripts/bench_jit.py --json --n-warmup 1 --n-bench 2`; assert returncode 0, output parses as JSON with keys `"jit_disabled"` and `"jit_enabled"` (matching worker mode names).
5. **Rollout count sanity** (`@needs_jit`) — invoke jit_disabled worker with `--n-bench 3`; assert `n_completed == 3` (verifies no silent game-loop exits).

---

## 9. Implementation Sequence

1. Create `scripts/bench_jit.py` — `_print_setup_check`, `_worker_main`, `_coordinator_main`, `main`
2. Create `tests/python/test_bench_jit.py` — five tests
3. Manually verify: `uv run --python 3.14 scripts/bench_jit.py --setup-check`
4. Run: `uv run ruff check scripts/bench_jit.py && uv run pytest tests/python/test_bench_jit.py -n 0`

No pyproject.toml changes. No new dependencies.

---

## Critical Files

- `scripts/bench_jit.py` — to create
- `tests/python/test_bench_jit.py` — to create
- `python/tsrl/engine/game_loop.py` — `play_random_game()` — the Level 1 measurement target
- `python/tsrl/engine/mcts.py` — `collect_self_play_game()` — Level 2 (--with-mcts)
- `python/tsrl/policies/benchmark_hybrid_vs_random.py` — idiom reference: warmup, `gc.disable()`, `perf_counter_ns()`, table format
- `scripts/run_mcts_game.py` — `sys.path.insert` pattern to copy
