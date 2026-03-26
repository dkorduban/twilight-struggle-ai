add_library(tscore STATIC
    public_state.cpp
)

target_include_directories(tscore
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
        $<INSTALL_INTERFACE:include/tscore>
)

target_compile_features(tscore PUBLIC cxx_std_20)

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
    types.hpp
    public_state.hpp
    hand_knowledge.hpp
    DESTINATION include/tscore
)
