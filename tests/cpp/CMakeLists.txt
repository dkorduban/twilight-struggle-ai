include(FetchContent)

FetchContent_Declare(
    Catch2
    GIT_REPOSITORY https://github.com/catchorg/Catch2.git
    GIT_TAG        v3.5.3
)
FetchContent_MakeAvailable(Catch2)

add_executable(test_tscore
    test_public_state.cpp
)

target_link_libraries(test_tscore
    PRIVATE
        tscore
        Catch2::Catch2WithMain
)

target_compile_features(test_tscore PRIVATE cxx_std_20)

# Register with CTest.
include(Catch)
catch_discover_tests(test_tscore)
