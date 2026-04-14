cmake_minimum_required(VERSION 3.21)

project(ts_fast_mcts LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_compile_options(
    $<$<COMPILE_LANGUAGE:CXX>:-O3>
    $<$<COMPILE_LANGUAGE:CXX>:-march=native>
    $<$<COMPILE_LANGUAGE:CXX>:-fno-math-errno>
)

set(TS_REPO_ROOT "${CMAKE_CURRENT_SOURCE_DIR}/../.." CACHE PATH "Twilight Struggle repo root")
set(TS_PREBUILT_TSCORE
    "${TS_REPO_ROOT}/build-ninja/cpp/tscore/libtscore.a"
    CACHE FILEPATH
    "Path to an existing libtscore.a build"
)

if(NOT EXISTS "${TS_PREBUILT_TSCORE}")
    message(FATAL_ERROR "Missing prebuilt tscore archive: ${TS_PREBUILT_TSCORE}")
endif()

set(TS_PYTHON_EXECUTABLE "" CACHE FILEPATH "Python interpreter for Torch discovery")
if(NOT TS_PYTHON_EXECUTABLE)
    if(EXISTS "${TS_REPO_ROOT}/.venv/bin/python")
        set(TS_PYTHON_EXECUTABLE "${TS_REPO_ROOT}/.venv/bin/python")
    else()
        find_program(TS_PYTHON_EXECUTABLE NAMES python3 REQUIRED)
    endif()
    set(TS_PYTHON_EXECUTABLE "${TS_PYTHON_EXECUTABLE}" CACHE FILEPATH "Python interpreter for Torch discovery" FORCE)
endif()

set(Python3_EXECUTABLE "${TS_PYTHON_EXECUTABLE}" CACHE FILEPATH "Python interpreter" FORCE)
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

execute_process(
    COMMAND "${TS_PYTHON_EXECUTABLE}" -c "import torch; print(torch.utils.cmake_prefix_path)"
    OUTPUT_VARIABLE TS_TORCH_CMAKE_PREFIX
    OUTPUT_STRIP_TRAILING_WHITESPACE
)
if(NOT TS_TORCH_CMAKE_PREFIX)
    message(FATAL_ERROR "Unable to detect torch.utils.cmake_prefix_path")
endif()
list(APPEND CMAKE_PREFIX_PATH "${TS_TORCH_CMAKE_PREFIX}")
if(EXISTS "/usr/local/cuda/bin/nvcc")
    set(ENV{CUDACXX} "/usr/local/cuda/bin/nvcc")
    set(CMAKE_CUDA_COMPILER "/usr/local/cuda/bin/nvcc" CACHE FILEPATH "CUDA compiler for libtorch" FORCE)
    set(CMAKE_CUDA_STANDARD 17 CACHE STRING "CUDA standard for libtorch probes" FORCE)
    set(CMAKE_CUDA_STANDARD_REQUIRED ON CACHE BOOL "Require CUDA standard" FORCE)
endif()
find_package(Torch REQUIRED)

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

get_filename_component(TS_TORCH_INSTALL_PREFIX "${Torch_DIR}/../../.." ABSOLUTE)
set(TS_TORCH_LIB_DIR "${TS_TORCH_INSTALL_PREFIX}/lib")

add_executable(ts_fast_mcts_bench
    bench_fast_mcts.cpp
    fast_mcts_batched.cpp
)

target_include_directories(ts_fast_mcts_bench
    PRIVATE
        "${TS_REPO_ROOT}/cpp/tscore"
)

target_compile_definitions(ts_fast_mcts_bench
    PRIVATE
        TS_BUILD_TORCH_RUNTIME=1
        TS_NUMPY_GENERATOR_SO="${TS_NUMPY_GENERATOR_SO}"
        TS_PYTHON_SHARED_LIB="${TS_PYTHON_SHARED_LIB}"
)

separate_arguments(TORCH_CXX_FLAGS_LIST NATIVE_COMMAND "${TORCH_CXX_FLAGS}")
target_compile_options(ts_fast_mcts_bench
    PRIVATE
        ${TORCH_CXX_FLAGS_LIST}
        $<$<CXX_COMPILER_ID:GNU,Clang>:
            -Wall -Wextra -Wpedantic -Werror
            -Wno-unused-parameter
        >
        $<$<CXX_COMPILER_ID:MSVC>:/W4 /WX>
)

target_link_libraries(ts_fast_mcts_bench
    PRIVATE
        "${TS_PREBUILT_TSCORE}"
        "${TORCH_LIBRARIES}"
        Python3::Python
)

set_target_properties(ts_fast_mcts_bench PROPERTIES BUILD_RPATH "${TS_TORCH_LIB_DIR}")
