#include <cstdlib>
#include <iostream>
#include <string>

#include "rng.hpp"

namespace {

[[noreturn]] void fail(const std::string& message) {
    std::cerr << "pcg64 smoke failed: " << message << '\n';
    std::exit(1);
}

void require(bool condition, const std::string& message) {
    if (!condition) {
        fail(message);
    }
}

}  // namespace

int main() {
    const ts::Uint128 state =
        (static_cast<ts::Uint128>(8677865484071468644ULL) << 64) |
        static_cast<ts::Uint128>(6624233139883375437ULL);
    const ts::Uint128 inc =
        (static_cast<ts::Uint128>(958784030336496442ULL) << 64) |
        static_cast<ts::Uint128>(2800060049131543611ULL);

    auto rng = ts::Pcg64Rng::from_numpy_state(state, inc);
    require(rng.next_u64() == 12587170189557361101ULL, "first raw output should match local NumPy PCG64 observation");
    require(rng.next_u64() == 992822559630912803ULL, "second raw output should match local NumPy PCG64 observation");

    const auto seeded = ts::Pcg64Rng::from_seed_sequence_words({
        12770025807176811766ULL,
        11695957281888622767ULL,
        9702764052023024029ULL,
        1400030024565771805ULL,
    });
    require(seeded.state() == state, "seed-sequence word seeding should reconstruct the observed NumPy state");
    require(seeded.inc() == inc, "seed-sequence word seeding should reconstruct the observed NumPy increment");

    std::cout << "pcg64 smoke ok\n";
    return 0;
}
