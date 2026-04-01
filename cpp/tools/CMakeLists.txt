# Native helper binaries used for benchmarking, collection, and parity work.
# These intentionally stay small and single-purpose so they can be composed in
# shell/Python workflows without pulling the full Python engine into the hot
# path.

add_executable(ts_benchmark_matchup
    benchmark_matchup.cpp
)

target_link_libraries(ts_benchmark_matchup
    PRIVATE
        tscore
)

target_compile_features(ts_benchmark_matchup PRIVATE cxx_std_23)

add_executable(ts_dump_native_setup
    dump_native_setup.cpp
)

target_link_libraries(ts_dump_native_setup
    PRIVATE
        tscore
)

target_compile_features(ts_dump_native_setup PRIVATE cxx_std_23)

add_executable(ts_pcg64_smoke
    pcg64_smoke.cpp
)

target_link_libraries(ts_pcg64_smoke
    PRIVATE
        tscore
)

target_compile_features(ts_pcg64_smoke PRIVATE cxx_std_23)

add_executable(ts_initial_headline_choice
    initial_headline_choice.cpp
)

target_link_libraries(ts_initial_headline_choice
    PRIVATE
        tscore
)

target_compile_features(ts_initial_headline_choice PRIVATE cxx_std_23)

add_executable(ts_numpy_bounded_probe
    numpy_bounded_probe.cpp
)

target_link_libraries(ts_numpy_bounded_probe
    PRIVATE
        tscore
)

target_compile_features(ts_numpy_bounded_probe PRIVATE cxx_std_23)

add_executable(ts_shuffle_stream_probe
    shuffle_stream_probe.cpp
)

target_link_libraries(ts_shuffle_stream_probe
    PRIVATE
        tscore
)

target_compile_features(ts_shuffle_stream_probe PRIVATE cxx_std_23)

if(TS_BUILD_TORCH_RUNTIME)
    add_executable(ts_learned_matchup
        learned_matchup.cpp
    )

    target_link_libraries(ts_learned_matchup
        PRIVATE
            tscore
    )

    target_compile_features(ts_learned_matchup PRIVATE cxx_std_23)
endif()

add_executable(ts_collect_trace_jsonl
    collect_trace_jsonl.cpp
)

target_link_libraries(ts_collect_trace_jsonl
    PRIVATE
        tscore
)

target_compile_features(ts_collect_trace_jsonl PRIVATE cxx_std_23)

add_executable(ts_collect_selfplay_rows_jsonl
    collect_selfplay_rows_jsonl.cpp
)

target_link_libraries(ts_collect_selfplay_rows_jsonl
    PRIVATE
        tscore
)

target_compile_features(ts_collect_selfplay_rows_jsonl PRIVATE cxx_std_23)

add_executable(ts_event_parity_smoke
    event_parity_smoke.cpp
)

target_link_libraries(ts_event_parity_smoke
    PRIVATE
        tscore
)

target_compile_features(ts_event_parity_smoke PRIVATE cxx_std_23)

if(BUILD_TESTING)
    add_test(NAME ts_event_parity_smoke COMMAND ts_event_parity_smoke)
endif()

add_executable(ts_cat_c_smoke
    cat_c_smoke.cpp
)

target_link_libraries(ts_cat_c_smoke
    PRIVATE
        tscore
)

target_compile_features(ts_cat_c_smoke PRIVATE cxx_std_23)

if(BUILD_TESTING)
    add_test(NAME ts_cat_c_smoke COMMAND ts_cat_c_smoke)
endif()

add_executable(ts_loop_mechanics_smoke
    loop_mechanics_smoke.cpp
)

target_link_libraries(ts_loop_mechanics_smoke
    PRIVATE
        tscore
)

target_compile_features(ts_loop_mechanics_smoke PRIVATE cxx_std_23)

if(BUILD_TESTING)
    add_test(NAME ts_loop_mechanics_smoke COMMAND ts_loop_mechanics_smoke)
endif()

add_custom_target(ts_native_smokes
    COMMAND ts_event_parity_smoke
    COMMAND ts_cat_c_smoke
    COMMAND ts_loop_mechanics_smoke
    DEPENDS
        ts_event_parity_smoke
        ts_cat_c_smoke
        ts_loop_mechanics_smoke
    USES_TERMINAL
)

if(TS_BUILD_PYTHON_BINDINGS)
    add_custom_target(ts_native_validation
        COMMAND ${CMAKE_COMMAND} -E env
            PYTHONPATH=${PROJECT_SOURCE_DIR}/python:$<TARGET_FILE_DIR:tscore_py>
            python3
            ${PROJECT_SOURCE_DIR}/cpp/tools/smoke_native_runtime.py
            --games 2
            --seed 101
            --rows-tool $<TARGET_FILE:ts_collect_selfplay_rows_jsonl>
        DEPENDS
            ts_native_smokes
            tscore_py
            ts_collect_selfplay_rows_jsonl
        USES_TERMINAL
    )
endif()
