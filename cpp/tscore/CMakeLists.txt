# Core native Twilight Struggle library target. This is the hot-path runtime
# that tools and bindings link against.

add_library(tscore STATIC
    adjacency.cpp
    dice.cpp
    game_data.cpp
    game_loop.cpp
    game_state.cpp
    hand_ops.cpp
    legal_actions.cpp
    policies.cpp
    public_state.cpp
    rng.cpp
    rule_queries.cpp
    scoring.cpp
    step.cpp
)

if(TS_BUILD_TORCH_RUNTIME)
    target_sources(tscore PRIVATE learned_policy.cpp ismcts.cpp mcts.cpp mcts_batched.cpp nn_features.cpp)
    target_compile_definitions(tscore PUBLIC TS_BUILD_TORCH_RUNTIME=1)
    separate_arguments(TORCH_CXX_FLAGS_LIST NATIVE_COMMAND "${TORCH_CXX_FLAGS}")
    target_compile_options(tscore PRIVATE ${TORCH_CXX_FLAGS_LIST})
    target_link_libraries(tscore PUBLIC "${TORCH_LIBRARIES}")
endif()

set_target_properties(tscore PROPERTIES POSITION_INDEPENDENT_CODE ON)

target_include_directories(tscore
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
        $<INSTALL_INTERFACE:include/tscore>
    PRIVATE
        ${Python3_INCLUDE_DIRS}
)

target_compile_features(tscore PUBLIC cxx_std_23)

if(TS_NUMPY_GENERATOR_SO)
    target_compile_definitions(tscore PUBLIC TS_NUMPY_GENERATOR_SO="${TS_NUMPY_GENERATOR_SO}")
endif()
if(TS_PYTHON_SHARED_LIB)
    target_compile_definitions(tscore PUBLIC TS_PYTHON_SHARED_LIB="${TS_PYTHON_SHARED_LIB}")
endif()

target_link_libraries(tscore PUBLIC Python3::Python)

# Strict warnings — treated as errors to keep the codebase clean.
target_compile_options(tscore PRIVATE
    $<$<CXX_COMPILER_ID:GNU,Clang>:
        -Wall -Wextra -Wpedantic -Werror
        -Wno-unused-parameter
    >
    $<$<CXX_COMPILER_ID:MSVC>:/W4 /WX>
)

# Install rules (consumed by the root CMakeLists install target).
install(TARGETS tscore
    ARCHIVE DESTINATION lib
    LIBRARY DESTINATION lib
    RUNTIME DESTINATION bin
)
install(FILES
    adjacency.hpp
    dice.hpp
    game_data.hpp
    game_loop.hpp
    game_state.hpp
    legal_actions.hpp
    learned_policy.hpp
    ismcts.hpp
    mcts.hpp
    mcts_batched.hpp
    nn_features.hpp
    policies.hpp
    types.hpp
    public_state.hpp
    rng.hpp
    rule_queries.hpp
    scoring.hpp
    step.hpp
    hand_knowledge.hpp
    DESTINATION include/tscore
)
