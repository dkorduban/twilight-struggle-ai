#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

#include "rng.hpp"

namespace {

void shuffle_with_bounded64(std::vector<int>& values, ts::Pcg64Rng& rng) {
    if (values.size() < 2) {
        return;
    }
    for (size_t i = values.size(); i > 1; --i) {
        const auto j = static_cast<size_t>(rng.numpy_bounded_uint64(0, i - 1));
        if (j != i - 1) {
            std::swap(values[i - 1], values[j]);
        }
    }
}

void shuffle_with_native_bounded(std::vector<int>& values, ts::Pcg64Rng& rng) {
    if (values.size() < 2) {
        return;
    }
    for (size_t i = values.size(); i > 1; --i) {
        const auto j = static_cast<size_t>(rng.bounded_u64(i));
        if (j != i - 1) {
            std::swap(values[i - 1], values[j]);
        }
    }
}

}  // namespace

int main(int argc, char** argv) {
    std::array<uint64_t, 4> words{0, 0, 0, 0};
    size_t count = 12;
    size_t rolls = 8;
    std::string method = "interval";

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
        } else if (arg == "--count" && i + 1 < argc) {
            count = static_cast<size_t>(std::stoull(argv[++i]));
        } else if (arg == "--rolls" && i + 1 < argc) {
            rolls = static_cast<size_t>(std::stoull(argv[++i]));
        } else if (arg == "--method" && i + 1 < argc) {
            method = argv[++i];
        }
    }

    auto rng = ts::Pcg64Rng::from_seed_sequence_words(words);
    std::vector<int> values;
    values.reserve(count);
    for (size_t i = 0; i < count; ++i) {
        values.push_back(static_cast<int>(i));
    }

    if (method == "interval") {
        ts::shuffle_with_numpy_rng(values, rng);
    } else if (method == "bounded64") {
        shuffle_with_bounded64(values, rng);
    } else if (method == "native_bounded") {
        shuffle_with_native_bounded(values, rng);
    } else {
        std::cerr << "unknown method\n";
        return 1;
    }

    std::cout << "shuffle=[";
    for (size_t i = 0; i < values.size(); ++i) {
        if (i > 0) {
            std::cout << ",";
        }
        std::cout << values[i];
    }
    std::cout << "]\n";

    std::cout << "next_d6=[";
    for (size_t i = 0; i < rolls; ++i) {
        if (i > 0) {
            std::cout << ",";
        }
        std::cout << rng.numpy_bounded_uint64(1, 5);
    }
    std::cout << "]\n";
    return 0;
}
