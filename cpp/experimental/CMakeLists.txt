add_library(ts_experimental_core STATIC
    callback_script.cpp
    evaluator.cpp
    planner.cpp
    profile.cpp
    search.cpp
    runner.cpp
)

set_target_properties(ts_experimental_core PROPERTIES POSITION_INDEPENDENT_CODE ON)
set_target_properties(ts_experimental_core PROPERTIES INTERPROCEDURAL_OPTIMIZATION TRUE)

target_include_directories(ts_experimental_core
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
)

target_link_libraries(ts_experimental_core PUBLIC tscore)
target_compile_features(ts_experimental_core PUBLIC cxx_std_23)

target_compile_options(ts_experimental_core PRIVATE
    $<$<CXX_COMPILER_ID:GNU,Clang>:
        -Wall -Wextra -Wpedantic -Werror
        -Wno-unused-parameter
        -O3
        -march=native
    >
    $<$<CXX_COMPILER_ID:MSVC>:/W4 /WX>
)

if(TS_BUILD_PYTHON_BINDINGS)
    pybind11_add_module(ts_experimental_py pybind_module.cpp)
    target_link_libraries(ts_experimental_py PRIVATE ts_experimental_core)
    set_target_properties(ts_experimental_py PROPERTIES OUTPUT_NAME ts_experimental)
    target_compile_features(ts_experimental_py PRIVATE cxx_std_23)
endif()

add_executable(ts_experimental_selfplay tools/heuristic_selfplay.cpp)
target_link_libraries(ts_experimental_selfplay PRIVATE ts_experimental_core)
target_compile_features(ts_experimental_selfplay PRIVATE cxx_std_23)
set_target_properties(ts_experimental_selfplay PROPERTIES INTERPROCEDURAL_OPTIMIZATION TRUE)

add_executable(ts_experimental_matchup tools/heuristic_matchup.cpp)
target_link_libraries(ts_experimental_matchup PRIVATE ts_experimental_core)
target_compile_features(ts_experimental_matchup PRIVATE cxx_std_23)
set_target_properties(ts_experimental_matchup PROPERTIES INTERPROCEDURAL_OPTIMIZATION TRUE)

add_executable(ts_experimental_spsa tools/heuristic_spsa.cpp)
target_link_libraries(ts_experimental_spsa PRIVATE ts_experimental_core)
target_compile_features(ts_experimental_spsa PRIVATE cxx_std_23)
set_target_properties(ts_experimental_spsa PROPERTIES INTERPROCEDURAL_OPTIMIZATION TRUE)

if(TS_BUILD_PYTHON_BINDINGS)
    set_target_properties(ts_experimental_py PROPERTIES INTERPROCEDURAL_OPTIMIZATION TRUE)
endif()
