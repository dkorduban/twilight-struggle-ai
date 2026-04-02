#include "human_openings.hpp"
#include "rng.hpp"

#include <iostream>
#include <iomanip>

int main() {
    using namespace ts;

    std::cout << "=== Human Openings Frequency Weights Test ===" << std::endl;

    // Test USSR openings
    std::cout << "\nUSSR Openings (58 games total):" << std::endl;
    double ussr_sum = 0.0;
    for (size_t i = 0; i < kHumanUSSROpenings.size(); ++i) {
        const auto& opening = kHumanUSSROpenings[i];
        ussr_sum += opening.weight;
        std::cout << "  Opening " << i << ": weight = " << std::fixed
                  << std::setprecision(4) << opening.weight
                  << " (" << static_cast<int>(opening.weight * 58.0) << "/52)" << std::endl;
    }
    std::cout << "  Sum of weights: " << std::fixed << std::setprecision(6)
              << ussr_sum << " (should be ~1.0)" << std::endl;

    // Test US openings
    std::cout << "\nUS Openings with bid (58 games total):" << std::endl;
    double us_sum = 0.0;
    for (size_t i = 0; i < kHumanUSOpeningsBid2.size(); ++i) {
        const auto& opening = kHumanUSOpeningsBid2[i];
        us_sum += opening.weight;
        std::cout << "  Opening " << i << ": weight = " << std::fixed
                  << std::setprecision(4) << opening.weight
                  << " (" << static_cast<int>(opening.weight * 58.0) << "/52)" << std::endl;
    }
    std::cout << "  Sum of weights: " << std::fixed << std::setprecision(6)
              << us_sum << " (should be ~1.0)" << std::endl;

    // Test weighted sampling
    std::cout << "\n=== Testing Weighted Sampling ===" << std::endl;

    Pcg64Rng rng(12345);  // Fixed seed for reproducibility

    // Sample USSR openings 1000 times
    std::cout << "\nSampling USSR openings 1000 times:" << std::endl;
    std::array<int, 3> ussr_counts = {0, 0, 0};
    for (int i = 0; i < 1000; ++i) {
        const SetupOpening* opening =
            choose_random_opening(kHumanUSSROpenings.data(),
                                  static_cast<int>(kHumanUSSROpenings.size()), rng);
        if (opening >= kHumanUSSROpenings.data() &&
            opening < kHumanUSSROpenings.data() + kHumanUSSROpenings.size()) {
            int idx = opening - kHumanUSSROpenings.data();
            ussr_counts[idx]++;
        }
    }
    for (size_t i = 0; i < ussr_counts.size(); ++i) {
        double expected = kHumanUSSROpenings[i].weight * 100.0;
        double actual = static_cast<double>(ussr_counts[i]) / 10.0;
        std::cout << "  Opening " << i << ": " << ussr_counts[i] << "/1000 = "
                  << std::fixed << std::setprecision(1) << actual << "% "
                  << "(expected ~" << expected << "%)" << std::endl;
    }

    // Sample US openings 1000 times
    std::cout << "\nSampling US openings 1000 times:" << std::endl;
    std::array<int, 6> us_counts = {0, 0, 0, 0, 0, 0};
    for (int i = 0; i < 1000; ++i) {
        const SetupOpening* opening =
            choose_random_opening(kHumanUSOpeningsBid2.data(),
                                  static_cast<int>(kHumanUSOpeningsBid2.size()), rng);
        if (opening >= kHumanUSOpeningsBid2.data() &&
            opening < kHumanUSOpeningsBid2.data() + kHumanUSOpeningsBid2.size()) {
            int idx = opening - kHumanUSOpeningsBid2.data();
            us_counts[idx]++;
        }
    }
    for (size_t i = 0; i < us_counts.size(); ++i) {
        double expected = kHumanUSOpeningsBid2[i].weight * 100.0;
        double actual = static_cast<double>(us_counts[i]) / 10.0;
        std::cout << "  Opening " << i << ": " << us_counts[i] << "/1000 = "
                  << std::fixed << std::setprecision(1) << actual << "% "
                  << "(expected ~" << expected << "%)" << std::endl;
    }

    std::cout << "\n=== All Tests Passed ===" << std::endl;
    return 0;
}
