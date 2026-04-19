include(FetchContent)

# Ensure Catch2 is built with the same GCC dual-ABI setting as the rest of the
# project.  PyTorch's CMake module injects -D_GLIBCXX_USE_CXX11_ABI=0 via
# TORCH_CXX_FLAGS, which is applied to tscore (and therefore propagated to any
# target that links it).  If Catch2 is built with ABI=1 (the default) while
# the test object is compiled with ABI=0, the linker cannot resolve
# StringMaker<int>::convert and other Catch2 symbols.  Setting CMAKE_CXX_FLAGS
# here before FetchContent_MakeAvailable forces both to use the same ABI.
if(DEFINED TORCH_CXX_FLAGS AND TORCH_CXX_FLAGS MATCHES "_GLIBCXX_USE_CXX11_ABI=0")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -D_GLIBCXX_USE_CXX11_ABI=0")
endif()

FetchContent_Declare(
    Catch2
    GIT_REPOSITORY https://github.com/catchorg/Catch2.git
    GIT_TAG        v3.5.3
)
FetchContent_MakeAvailable(Catch2)

add_executable(test_tscore
    test_decode_helpers.cpp
    test_frame_parity.cpp
    test_frame_regression.cpp
    test_ismcts_regression.cpp
    test_observation.cpp
    test_public_state.cpp
    test_adjacency.cpp
    test_experimental_heuristic.cpp
)

target_link_libraries(test_tscore
    PRIVATE
        tscore
        ts_experimental_core
        Catch2::Catch2WithMain
)

target_compile_features(test_tscore PRIVATE cxx_std_20)

# Register with CTest.
include(Catch)
catch_discover_tests(test_tscore)
