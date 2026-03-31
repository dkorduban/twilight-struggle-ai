#include "rng.hpp"

#include <algorithm>

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
    const auto seq = std::array<uint64_t, 4>{seed, 0, seed ^ 0x9e3779b97f4a7c15ULL, 0};
    *this = from_seed_sequence_words(seq);
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

int Pcg64Rng::uniform_int(int low_inclusive, int high_inclusive) {
    const auto width = static_cast<uint64_t>(high_inclusive - low_inclusive + 1);
    return low_inclusive + static_cast<int>(bounded_u64(width));
}

std::array<uint64_t, 2> split_u128(Uint128 value) {
    return {
        static_cast<uint64_t>(value >> 64),
        static_cast<uint64_t>(value & kMask64),
    };
}

}  // namespace ts
