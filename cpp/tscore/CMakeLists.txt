add_library(tscore STATIC
    adjacency.cpp
    dice.cpp
    game_data.cpp
    game_loop.cpp
    game_state.cpp
    legal_actions.cpp
    policies.cpp
    public_state.cpp
    scoring.cpp
    step.cpp
)

set_target_properties(tscore PROPERTIES POSITION_INDEPENDENT_CODE ON)

target_include_directories(tscore
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
        $<INSTALL_INTERFACE:include/tscore>
)

target_compile_features(tscore PUBLIC cxx_std_23)

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
    policies.hpp
    types.hpp
    public_state.hpp
    scoring.hpp
    step.hpp
    hand_knowledge.hpp
    DESTINATION include/tscore
)
