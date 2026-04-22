# Task #128 Arrow C++ Linkage Blocker

## Requested change

Add `--format jsonl|parquet` to `cpp/tools/collect_selfplay_rows_jsonl.cpp` and write Parquet directly with Apache Arrow C++ while preserving the `scripts/jsonl_to_parquet.py` schema.

## Blocker

Arrow C++ is not already linked or discoverable by this CMake build, and adding it is not a minimal local linkage change in this checkout.

Findings:

- `CMakeLists.txt` and `cpp/tools/CMakeLists.txt` do not call `find_package(Arrow)` or `find_package(Parquet)`.
- There is no top-level `vcpkg.json` in this checkout.
- `pkg-config --list-all` has no Arrow or Parquet package entries.
- No `ArrowConfig.cmake`, `arrow-config.cmake`, `ParquetConfig.cmake`, or `parquet-config.cmake` was found under `build-ninja`, `.venv`, `/usr`, `/usr/local`, or `/opt`.
- The only Arrow distribution found is the Python `pyarrow` wheel in `.venv`.

The `pyarrow` wheel is not a safe drop-in C++ link target for this collector:

- `pyarrow.get_cmake_dir()` returns `None`.
- The wheel has headers and versioned shared libraries under `.venv/lib/python3.12/site-packages/pyarrow`, but no CMake package metadata.
- The existing collector compile command includes `-D_GLIBCXX_USE_CXX11_ABI=0` via the Torch runtime path.
- `pyarrow`'s `libarrow.so.2300` exports C++11 ABI symbols such as `arrow::Status::ToString[abi:cxx11]` and `arrow::field(std::__cxx11::basic_string<...>)`.

Linking this collector directly against the wheel libraries would require resolving ABI/toolchain compatibility and manual Arrow/Parquet library wiring. That is larger than the bounded "minimal linkage" requested for this task.

## Safest local assumption

Keep JSONL behavior unchanged and defer direct Parquet output until the project has a repo-owned Arrow C++ dependency path that matches the collector's toolchain and ABI.

## Human / Claude decision needed

Please decide one of:

1. Add a project-managed Arrow C++ dependency with CMake targets and matching libstdc++ ABI for the existing Torch-enabled native tools.
2. Split direct Parquet collection into a non-Torch native target that can use a separate Arrow ABI, with an explicit decision about learned-model support.
3. Keep the current JSONL collector plus `scripts/jsonl_to_parquet.py` conversion path.

Files needing that decision:

- `CMakeLists.txt`
- `cpp/tools/CMakeLists.txt`
- `cpp/tools/collect_selfplay_rows_jsonl.cpp`
