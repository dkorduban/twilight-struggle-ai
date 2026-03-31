#pragma once

#include <array>
#include <bit>
#include <cstddef>
#include <cstdint>
#include <limits>
#include <random>
#include <span>
#include <vector>

namespace ts {

#if !defined(__SIZEOF_INT128__)
#error "Pcg64Rng requires compiler support for unsigned __int128"
#endif

#if defined(__GNUC__) || defined(__clang__)
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wpedantic"
#endif
using Uint128 = unsigned __int128;
#if defined(__GNUC__) || defined(__clang__)
#pragma GCC diagnostic pop
#endif

class Pcg64Rng {
public:
    Pcg64Rng();
    explicit Pcg64Rng(uint64_t seed);
    Pcg64Rng(Uint128 state, Uint128 inc);

    [[nodiscard]] Uint128 state() const { return state_; }
    [[nodiscard]] Uint128 inc() const { return inc_; }

    [[nodiscard]] uint64_t operator()();
    [[nodiscard]] static constexpr uint64_t min() { return std::numeric_limits<uint64_t>::min(); }
    [[nodiscard]] static constexpr uint64_t max() { return std::numeric_limits<uint64_t>::max(); }

    [[nodiscard]] uint64_t next_u64();
    [[nodiscard]] uint32_t next_u32();
    [[nodiscard]] uint64_t bounded_u64(uint64_t bound_exclusive);
    [[nodiscard]] int uniform_int(int low_inclusive, int high_inclusive);

    static Pcg64Rng from_numpy_state(Uint128 state, Uint128 inc);
    static Pcg64Rng from_seed_sequence_words(std::array<uint64_t, 4> words);

private:
    Uint128 state_ = 0;
    Uint128 inc_ = 0;
    bool has_uint32_ = false;
    uint32_t uinteger_ = 0;
};

template <typename T>
void shuffle_with_rng(std::span<T> values, Pcg64Rng& rng) {
    if (values.size() < 2) {
        return;
    }
    for (size_t i = values.size() - 1; i > 0; --i) {
        const auto j = static_cast<size_t>(rng.bounded_u64(i + 1));
        if (i != j) {
            std::swap(values[i], values[j]);
        }
    }
}

template <typename T>
void shuffle_with_rng(std::vector<T>& values, Pcg64Rng& rng) {
    shuffle_with_rng(std::span<T>(values), rng);
}

[[nodiscard]] std::array<uint64_t, 2> split_u128(Uint128 value);

}  // namespace ts
