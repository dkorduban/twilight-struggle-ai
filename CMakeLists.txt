cmake_minimum_required(VERSION 3.21)

project(tscore
    VERSION     0.1.0
    DESCRIPTION "Twilight Struggle AI - exact C++ game engine"
    LANGUAGES   CXX
)

# ---------------------------------------------------------------------------
# Global settings
# ---------------------------------------------------------------------------

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Export compile commands for clangd / tooling.
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

include(GNUInstallDirs)

# Default build type guard (useful when configuring without -DCMAKE_BUILD_TYPE).
if(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
    message(STATUS "No build type specified; defaulting to Release")
    set(CMAKE_BUILD_TYPE Release CACHE STRING "Build type" FORCE)
endif()

# ---------------------------------------------------------------------------
# Optimization flags — applied to the hot-path tscore library and all tools.
# -O3          : full optimization (vs -O2 in RelWithDebInfo)
# -march=native: tune for the build machine's exact ISA (enables AVX2/AVX-512
#                where available — confirmed RTX 3050 host has AVX2)
# -fno-math-errno: safe fast-math subset; lets compiler fold sqrt/log without
#                  errno checks. Avoids -ffast-math which breaks IEEE NaN/Inf
#                  handling that PCG64 and TS scoring rely on.
# ---------------------------------------------------------------------------
add_compile_options(
    $<$<COMPILE_LANGUAGE:CXX>:-O3>
    $<$<COMPILE_LANGUAGE:CXX>:-march=native>
    $<$<COMPILE_LANGUAGE:CXX>:-fno-math-errno>
)

# ---------------------------------------------------------------------------
# Dependencies
# ---------------------------------------------------------------------------

option(TS_BUILD_PYTHON_BINDINGS "Build pybind11 Python extension module" ON)
option(TS_BUILD_TORCH_RUNTIME "Build TorchScript/libtorch learned-policy runtime" ON)

set(TS_PYTHON_EXECUTABLE "" CACHE FILEPATH "Python interpreter for CMake Python/Torch probes")
if(NOT TS_PYTHON_EXECUTABLE)
    if(EXISTS "${CMAKE_SOURCE_DIR}/.venv/bin/python")
        set(TS_PYTHON_EXECUTABLE "${CMAKE_SOURCE_DIR}/.venv/bin/python")
    elseif(EXISTS "$ENV{HOME}/.venv/bin/python")
        set(TS_PYTHON_EXECUTABLE "$ENV{HOME}/.venv/bin/python")
    else()
        find_program(TS_PYTHON_EXECUTABLE NAMES python3 REQUIRED)
    endif()
    set(TS_PYTHON_EXECUTABLE "${TS_PYTHON_EXECUTABLE}" CACHE FILEPATH "Python interpreter for CMake Python/Torch probes" FORCE)
endif()

set(Python3_EXECUTABLE "${TS_PYTHON_EXECUTABLE}" CACHE FILEPATH "Python interpreter for Twilight Struggle builds" FORCE)
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

if(TS_BUILD_PYTHON_BINDINGS)
    find_package(pybind11 CONFIG REQUIRED)
endif()

execute_process(
    COMMAND "${TS_PYTHON_EXECUTABLE}" -c "import numpy.random._generator as g; print(g.__file__)"
    OUTPUT_VARIABLE TS_NUMPY_GENERATOR_SO
    OUTPUT_STRIP_TRAILING_WHITESPACE
    ERROR_QUIET
)
execute_process(
    COMMAND "${TS_PYTHON_EXECUTABLE}" -c "import sysconfig; from pathlib import Path; print(Path(sysconfig.get_config_var('LIBDIR')) / sysconfig.get_config_var('LDLIBRARY'))"
    OUTPUT_VARIABLE TS_PYTHON_SHARED_LIB
    OUTPUT_STRIP_TRAILING_WHITESPACE
    ERROR_QUIET
)

if(TS_BUILD_TORCH_RUNTIME)
    if(NOT DEFINED TS_TORCH_CMAKE_PREFIX)
        execute_process(
            COMMAND "${TS_PYTHON_EXECUTABLE}" -c "import torch; print(torch.utils.cmake_prefix_path)"
            OUTPUT_VARIABLE TS_TORCH_CMAKE_PREFIX
            OUTPUT_STRIP_TRAILING_WHITESPACE
            ERROR_QUIET
        )
    endif()
    if(TS_TORCH_CMAKE_PREFIX)
        list(APPEND CMAKE_PREFIX_PATH "${TS_TORCH_CMAKE_PREFIX}")
    endif()
    if(EXISTS "/usr/local/cuda/bin/nvcc")
        set(ENV{CUDACXX} "/usr/local/cuda/bin/nvcc")
        set(CMAKE_CUDA_COMPILER "/usr/local/cuda/bin/nvcc" CACHE FILEPATH "CUDA compiler for libtorch" FORCE)
        set(CMAKE_CUDA_STANDARD 17 CACHE STRING "CUDA standard for libtorch probes" FORCE)
        set(CMAKE_CUDA_STANDARD_REQUIRED ON CACHE BOOL "Require CUDA standard" FORCE)
    endif()
    find_package(Torch REQUIRED)
endif()

# ---------------------------------------------------------------------------
# Subdirectories
# ---------------------------------------------------------------------------

add_subdirectory(cpp/tscore)
add_subdirectory(cpp/tools)

if(TS_BUILD_PYTHON_BINDINGS)
    add_subdirectory(bindings)
endif()

# ---------------------------------------------------------------------------
# Testing
# ---------------------------------------------------------------------------

include(CTest)
enable_testing()

if(BUILD_TESTING)
    add_subdirectory(tests/cpp)
endif()

# ---------------------------------------------------------------------------
# Install
# ---------------------------------------------------------------------------

install(TARGETS tscore
    EXPORT  tscoreTargets
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

install(EXPORT tscoreTargets
    FILE      tscoreTargets.cmake
    NAMESPACE ts::
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/tscore
)
