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
    message(STATUS "No build type specified; defaulting to RelWithDebInfo")
    set(CMAKE_BUILD_TYPE RelWithDebInfo CACHE STRING "Build type" FORCE)
endif()

# ---------------------------------------------------------------------------
# Dependencies
# ---------------------------------------------------------------------------

option(TS_BUILD_PYTHON_BINDINGS "Build pybind11 Python extension module" ON)

if(TS_BUILD_PYTHON_BINDINGS)
    find_package(pybind11 CONFIG REQUIRED)
endif()

# ---------------------------------------------------------------------------
# Subdirectories
# ---------------------------------------------------------------------------

add_subdirectory(cpp/tscore)

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
