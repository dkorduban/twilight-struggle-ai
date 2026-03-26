#!/usr/bin/env python3
import json, subprocess, sys
from pathlib import Path


def run(cmd, timeout=20):
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return proc.returncode, (proc.stdout + proc.stderr).strip()
    except Exception as e:
        return 99, str(e)


def emit(msg):
    print(json.dumps({"systemMessage": msg}))

try:
    payload = json.load(sys.stdin)
except Exception:
    sys.exit(0)

file_path = ((payload.get("tool_input") or {}).get("file_path"))
if not file_path:
    sys.exit(0)

p = Path(file_path)
suffix = p.suffix.lower()

if suffix == ".py":
    code, out = run([sys.executable, "-m", "py_compile", str(p)], timeout=15)
    emit(f"Quick check {'passed' if code == 0 else 'failed'} for {p}: {out[:1200] if out else 'python -m py_compile'}")
    sys.exit(0)

if suffix == ".json":
    try:
        with open(p, "r", encoding="utf-8") as f:
            json.load(f)
        emit(f"Quick check passed: JSON parsed successfully for {p}")
    except Exception as e:
        emit(f"Quick check failed for {p}: {e}")
    sys.exit(0)

if suffix == ".sh":
    code, out = run(["bash", "-n", str(p)], timeout=15)
    emit(f"Quick check {'passed' if code == 0 else 'failed'} for {p}: {out[:1200] if out else 'bash -n'}")
    sys.exit(0)

cpp_like = suffix in {".c", ".cc", ".cpp", ".cxx", ".h", ".hh", ".hpp", ".hxx"} or p.name == "CMakeLists.txt"
if cpp_like:
    build_dir = Path("build")
    if (build_dir / "CTestTestfile.cmake").exists() or (build_dir / "DartConfiguration.tcl").exists():
        code, out = run(["ctest", "--test-dir", "build", "-L", "smoke", "--output-on-failure"], timeout=90)
        emit(f"Smoke checks {'passed' if code == 0 else 'failed'} after editing {p}: {out[:1600] if out else 'ctest -L smoke'}")
    else:
        emit(f"C++/CMake file edited ({p}). No build/ smoke config detected; run your normal engine smoke target.")
