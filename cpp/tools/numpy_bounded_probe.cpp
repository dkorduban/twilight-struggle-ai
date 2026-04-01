// Probe NumPy's bounded-integer helpers directly against the native PCG64
// wrapper to isolate RNG-compatibility bugs.

#include <array>
#include <cstdint>
#include <cstdlib>
#include <dlfcn.h>
#include <iostream>
#include <optional>
#include <string>

#include "rng.hpp"

namespace {

// Mirror NumPy's bitgen callback shape so the probe can call its exported C
// helpers without routing through Python-level Generator objects.
struct NumpyBitgen {
    void* state;
    uint64_t (*next_uint64)(void* st);
    uint32_t (*next_uint32)(void* st);
    double (*next_double)(void* st);
    uint64_t (*next_raw)(void* st);
};

using RandomIntervalFn = uint64_t (*)(NumpyBitgen*, uint64_t);
using RandomBoundedUint64Fn = uint64_t (*)(NumpyBitgen*, uint64_t, uint64_t, uint64_t, bool);

uint64_t bitgen_next_uint64(void* st) {
    return static_cast<ts::Pcg64Rng*>(st)->next_u64();
}

uint32_t bitgen_next_uint32(void* st) {
    return static_cast<ts::Pcg64Rng*>(st)->next_u32();
}

double bitgen_next_double(void* st) {
    constexpr double scale = 1.0 / static_cast<double>(uint64_t{1} << 53);
    return static_cast<double>(static_cast<ts::Pcg64Rng*>(st)->next_u64() >> 11) * scale;
}

uint64_t bitgen_next_raw(void* st) {
    return static_cast<ts::Pcg64Rng*>(st)->next_u64();
}

uint64_t gen_mask(uint64_t max_val) {
    uint64_t mask = max_val;
    mask |= mask >> 1;
    mask |= mask >> 2;
    mask |= mask >> 4;
    mask |= mask >> 8;
    mask |= mask >> 16;
    mask |= mask >> 32;
    return mask;
}

[[noreturn]] void fail(const std::string& message) {
    std::cerr << message << '\n';
    std::exit(1);
}

}  // namespace

int main(int argc, char** argv) {
    std::array<uint64_t, 4> words{0, 0, 0, 0};
    std::string numpy_generator_so;
    std::optional<std::string> python_lib;
    std::string method = "interval";
    int count = 10;
    uint64_t off = 1;
    uint64_t range = 5;
    bool use_masked = false;

    for (int i = 1; i < argc; ++i) {
        const std::string arg = argv[i];
        if (arg == "--word0" && i + 1 < argc) {
            words[0] = std::stoull(argv[++i]);
        } else if (arg == "--word1" && i + 1 < argc) {
            words[1] = std::stoull(argv[++i]);
        } else if (arg == "--word2" && i + 1 < argc) {
            words[2] = std::stoull(argv[++i]);
        } else if (arg == "--word3" && i + 1 < argc) {
            words[3] = std::stoull(argv[++i]);
        } else if (arg == "--numpy-generator-so" && i + 1 < argc) {
            numpy_generator_so = argv[++i];
        } else if (arg == "--python-lib" && i + 1 < argc) {
            python_lib = argv[++i];
        } else if (arg == "--method" && i + 1 < argc) {
            method = argv[++i];
        } else if (arg == "--count" && i + 1 < argc) {
            count = std::stoi(argv[++i]);
        } else if (arg == "--off" && i + 1 < argc) {
            off = std::stoull(argv[++i]);
        } else if (arg == "--range" && i + 1 < argc) {
            range = std::stoull(argv[++i]);
        } else if (arg == "--use-masked") {
            use_masked = true;
        }
    }

    if (numpy_generator_so.empty()) {
        fail("missing --numpy-generator-so");
    }
    if (python_lib.has_value()) {
        void* py = dlopen(python_lib->c_str(), RTLD_NOW | RTLD_GLOBAL);
        if (py == nullptr) {
            fail(std::string("failed to dlopen libpython: ") + dlerror());
        }
    }

    void* handle = dlopen(numpy_generator_so.c_str(), RTLD_NOW | RTLD_GLOBAL);
    if (handle == nullptr) {
        fail(std::string("failed to dlopen numpy generator: ") + dlerror());
    }

    auto* random_interval = reinterpret_cast<RandomIntervalFn>(dlsym(handle, "random_interval"));
    auto* random_bounded_uint64 =
        reinterpret_cast<RandomBoundedUint64Fn>(dlsym(handle, "random_bounded_uint64"));
    if (random_interval == nullptr || random_bounded_uint64 == nullptr) {
        fail("failed to resolve NumPy bounded integer symbols");
    }

    auto rng = ts::Pcg64Rng::from_seed_sequence_words(words);
    NumpyBitgen bitgen{
        .state = &rng,
        .next_uint64 = bitgen_next_uint64,
        .next_uint32 = bitgen_next_uint32,
        .next_double = bitgen_next_double,
        .next_raw = bitgen_next_raw,
    };

    std::cout << "[";
    for (int i = 0; i < count; ++i) {
        uint64_t value = 0;
        if (method == "interval") {
            value = random_interval(&bitgen, range);
        } else if (method == "bounded64") {
            value = random_bounded_uint64(&bitgen, off, range, gen_mask(range), use_masked);
        } else if (method == "native_interval") {
            value = rng.bounded_interval_inclusive(range);
        } else {
            fail("unknown --method");
        }
        if (i > 0) {
            std::cout << ",";
        }
        std::cout << value;
    }
    std::cout << "]\n";
    dlclose(handle);
    return 0;
}
