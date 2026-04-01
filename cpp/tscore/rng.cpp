#include "rng.hpp"

#include <Python.h>

#include <algorithm>
#include <dlfcn.h>
#include <mutex>
#include <stdexcept>
#include <unordered_map>

namespace ts {
namespace {

constexpr Uint128 kMask64 = (static_cast<Uint128>(1) << 64) - 1;
constexpr Uint128 kMask128 = ~static_cast<Uint128>(0);
constexpr Uint128 kMultiplier = (static_cast<Uint128>(0x2360ed051fc65da4ULL) << 64) | 0x4385df649fccf645ULL;

Uint128 make_u128(uint64_t hi, uint64_t lo) {
    return (static_cast<Uint128>(hi) << 64) | static_cast<Uint128>(lo);
}

uint64_t rotr64(uint64_t value, uint64_t rot) {
    return std::rotr(value, static_cast<int>(rot & 63U));
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
    return static_cast<Pcg64Rng*>(st)->next_u64();
}

uint32_t bitgen_next_uint32(void* st) {
    return static_cast<Pcg64Rng*>(st)->next_u32();
}

double bitgen_next_double(void* st) {
    constexpr double scale = 1.0 / static_cast<double>(uint64_t{1} << 53);
    return static_cast<double>(static_cast<Pcg64Rng*>(st)->next_u64() >> 11) * scale;
}

uint64_t bitgen_next_raw(void* st) {
    return static_cast<Pcg64Rng*>(st)->next_u64();
}

struct NumpyRandomApi {
    void* python_handle = nullptr;
    void* generator_handle = nullptr;
    RandomIntervalFn random_interval = nullptr;
    RandomBoundedUint64Fn random_bounded_uint64 = nullptr;
    bool loaded = false;
};

NumpyRandomApi& numpy_random_api() {
    static NumpyRandomApi api;
    static std::once_flag once;
    std::call_once(once, [] {
#if defined(TS_PYTHON_SHARED_LIB)
        api.python_handle = dlopen(TS_PYTHON_SHARED_LIB, RTLD_NOW | RTLD_GLOBAL);
#endif
#if defined(TS_NUMPY_GENERATOR_SO)
        api.generator_handle = dlopen(TS_NUMPY_GENERATOR_SO, RTLD_NOW | RTLD_GLOBAL);
        if (api.generator_handle != nullptr) {
            api.random_interval = reinterpret_cast<RandomIntervalFn>(dlsym(api.generator_handle, "random_interval"));
            api.random_bounded_uint64 =
                reinterpret_cast<RandomBoundedUint64Fn>(dlsym(api.generator_handle, "random_bounded_uint64"));
        }
#endif
        api.loaded = api.random_interval != nullptr && api.random_bounded_uint64 != nullptr;
    });
    return api;
}

std::array<uint64_t, 4> seed_sequence_words_from_numpy(uint64_t seed) {
    static std::mutex cache_mutex;
    static std::unordered_map<uint64_t, std::array<uint64_t, 4>> cache;

    {
        std::lock_guard<std::mutex> lock(cache_mutex);
        if (const auto found = cache.find(seed); found != cache.end()) {
            return found->second;
        }
    }

    if (!Py_IsInitialized()) {
        Py_Initialize();
    }

    std::array<uint64_t, 4> words{};
    PyGILState_STATE gil_state = PyGILState_Ensure();

    PyObject* module = PyImport_ImportModule("numpy.random");
    if (module == nullptr) {
        PyGILState_Release(gil_state);
        throw std::runtime_error("failed to import numpy.random for SeedSequence");
    }

    PyObject* seed_sequence_type = PyObject_GetAttrString(module, "SeedSequence");
    Py_DECREF(module);
    if (seed_sequence_type == nullptr) {
        PyGILState_Release(gil_state);
        throw std::runtime_error("failed to load numpy.random.SeedSequence");
    }

    PyObject* seed_arg = PyLong_FromUnsignedLongLong(seed);
    PyObject* seed_sequence = PyObject_CallFunctionObjArgs(seed_sequence_type, seed_arg, nullptr);
    Py_DECREF(seed_arg);
    Py_DECREF(seed_sequence_type);
    if (seed_sequence == nullptr) {
        PyGILState_Release(gil_state);
        throw std::runtime_error("failed to construct SeedSequence");
    }

    PyObject* state_array = PyObject_CallMethod(seed_sequence, "generate_state", "is", 4, "uint64");
    Py_DECREF(seed_sequence);
    if (state_array == nullptr) {
        PyGILState_Release(gil_state);
        throw std::runtime_error("failed to call SeedSequence.generate_state");
    }

    PyObject* state_list = PyObject_CallMethod(state_array, "tolist", nullptr);
    Py_DECREF(state_array);
    if (state_list == nullptr || !PyList_Check(state_list) || PyList_Size(state_list) != 4) {
        Py_XDECREF(state_list);
        PyGILState_Release(gil_state);
        throw std::runtime_error("SeedSequence.generate_state returned unexpected shape");
    }

    for (Py_ssize_t i = 0; i < 4; ++i) {
        PyObject* item = PyList_GetItem(state_list, i);
        words[static_cast<size_t>(i)] = PyLong_AsUnsignedLongLong(item);
        if (PyErr_Occurred()) {
            Py_DECREF(state_list);
            PyGILState_Release(gil_state);
            throw std::runtime_error("failed to read SeedSequence word");
        }
    }
    Py_DECREF(state_list);
    PyGILState_Release(gil_state);

    {
        std::lock_guard<std::mutex> lock(cache_mutex);
        cache.emplace(seed, words);
    }
    return words;
}

Uint128 seeded_state(Uint128 initstate, Uint128 inc) {
    Uint128 state = 0;
    state = state * kMultiplier + inc;
    state += initstate;
    state = state * kMultiplier + inc;
    return state;
}

}  // namespace

Pcg64Rng::Pcg64Rng() {
    std::random_device rd;
    const auto hi = (static_cast<uint64_t>(rd()) << 32) ^ static_cast<uint64_t>(rd());
    const auto lo = (static_cast<uint64_t>(rd()) << 32) ^ static_cast<uint64_t>(rd());
    const auto seq_hi = (static_cast<uint64_t>(rd()) << 32) ^ static_cast<uint64_t>(rd());
    const auto seq_lo = (static_cast<uint64_t>(rd()) << 32) ^ static_cast<uint64_t>(rd());
    *this = from_seed_sequence_words({lo, hi, seq_hi, seq_lo});
}

Pcg64Rng::Pcg64Rng(uint64_t seed) {
    *this = from_seed_sequence_words(seed_sequence_words_from_numpy(seed));
}

Pcg64Rng::Pcg64Rng(Uint128 state, Uint128 inc) : state_(state), inc_(inc) {}

Pcg64Rng Pcg64Rng::from_numpy_state(Uint128 state, Uint128 inc) {
    return Pcg64Rng(state, inc);
}

Pcg64Rng Pcg64Rng::from_seed_sequence_words(std::array<uint64_t, 4> words) {
    const auto initstate = make_u128(words[0], words[1]);
    const auto initseq = make_u128(words[2], words[3]);
    const auto inc = (initseq << 1) | static_cast<Uint128>(1);
    const auto state = seeded_state(initstate, inc);
    return Pcg64Rng(state, inc);
}

uint64_t Pcg64Rng::operator()() {
    return next_u64();
}

uint64_t Pcg64Rng::next_u64() {
    state_ = state_ * kMultiplier + inc_;
    const auto hi = static_cast<uint64_t>(state_ >> 64);
    const auto lo = static_cast<uint64_t>(state_ & kMask64);
    const auto xsl = hi ^ lo;
    return rotr64(xsl, hi >> 58);
}

uint32_t Pcg64Rng::next_u32() {
    if (has_uint32_) {
        has_uint32_ = false;
        return uinteger_;
    }
    const auto value = next_u64();
    uinteger_ = static_cast<uint32_t>(value >> 32);
    has_uint32_ = true;
    return static_cast<uint32_t>(value & 0xffffffffU);
}

uint64_t Pcg64Rng::bounded_u64(uint64_t bound_exclusive) {
    if (bound_exclusive <= 1) {
        return 0;
    }
    const auto threshold = static_cast<uint64_t>(-bound_exclusive) % bound_exclusive;
    while (true) {
        const auto value = next_u64();
        if (value >= threshold) {
            return value % bound_exclusive;
        }
    }
}

uint64_t Pcg64Rng::bounded_interval_inclusive(uint64_t max_inclusive) {
    if (max_inclusive == 0) {
        return 0;
    }
    const auto mask = gen_mask(max_inclusive);
    if (max_inclusive <= std::numeric_limits<uint32_t>::max()) {
        const auto max32 = static_cast<uint32_t>(max_inclusive);
        const auto mask32 = static_cast<uint32_t>(mask);
        auto value = static_cast<uint32_t>(next_u32() & mask32);
        while (value > max32) {
            value = static_cast<uint32_t>(next_u32() & mask32);
        }
        return value;
    }

    auto value = next_u64() & mask;
    while (value > max_inclusive) {
        value = next_u64() & mask;
    }
    return value;
}

uint64_t Pcg64Rng::numpy_interval(uint64_t max_inclusive) {
    auto& api = numpy_random_api();
    if (!api.loaded) {
        return bounded_interval_inclusive(max_inclusive);
    }
    NumpyBitgen bitgen{
        .state = this,
        .next_uint64 = bitgen_next_uint64,
        .next_uint32 = bitgen_next_uint32,
        .next_double = bitgen_next_double,
        .next_raw = bitgen_next_raw,
    };
    return api.random_interval(&bitgen, max_inclusive);
}

uint64_t Pcg64Rng::numpy_bounded_uint64(uint64_t off, uint64_t range) {
    auto& api = numpy_random_api();
    if (!api.loaded) {
        return off + bounded_interval_inclusive(range);
    }
    NumpyBitgen bitgen{
        .state = this,
        .next_uint64 = bitgen_next_uint64,
        .next_uint32 = bitgen_next_uint32,
        .next_double = bitgen_next_double,
        .next_raw = bitgen_next_raw,
    };
    return api.random_bounded_uint64(&bitgen, off, range, gen_mask(range), false);
}

int Pcg64Rng::uniform_int(int low_inclusive, int high_inclusive) {
    return static_cast<int>(numpy_bounded_uint64(
        static_cast<uint64_t>(low_inclusive),
        static_cast<uint64_t>(high_inclusive - low_inclusive)
    ));
}

size_t Pcg64Rng::choice_index(size_t size) {
    if (size <= 1) {
        return 0;
    }
    return static_cast<size_t>(numpy_bounded_uint64(0, size - 1));
}

double Pcg64Rng::random_double() {
    constexpr double scale = 1.0 / static_cast<double>(uint64_t{1} << 53);
    return static_cast<double>(next_u64() >> 11) * scale;
}

bool Pcg64Rng::bernoulli(double p) {
    if (p <= 0.0) {
        return false;
    }
    if (p >= 1.0) {
        return true;
    }
    return random_double() < p;
}

std::array<uint64_t, 2> split_u128(Uint128 value) {
    return {
        static_cast<uint64_t>(value >> 64),
        static_cast<uint64_t>(value & kMask64),
    };
}

}  // namespace ts
