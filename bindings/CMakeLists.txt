pybind11_add_module(tscore_py tscore_bindings.cpp)

# Link against the static engine library.
target_link_libraries(tscore_py PRIVATE tscore)

# The output name must match the module name declared in PYBIND11_MODULE.
set_target_properties(tscore_py PROPERTIES OUTPUT_NAME tscore)

target_compile_features(tscore_py PRIVATE cxx_std_20)

install(TARGETS tscore_py
    LIBRARY DESTINATION ${Python_SITEARCH}
)
