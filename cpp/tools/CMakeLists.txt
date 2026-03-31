add_executable(ts_benchmark_matchup
    benchmark_matchup.cpp
)

target_link_libraries(ts_benchmark_matchup
    PRIVATE
        tscore
)

target_compile_features(ts_benchmark_matchup PRIVATE cxx_std_23)

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
