// Benchmark runner for the standalone fast batched MCTS replica.

#include "fast_mcts_batched.hpp"

#if defined(TS_BUILD_TORCH_RUNTIME)

#include <chrono>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <optional>
#include <stdexcept>
#include <string>
#include <string_view>
#include <thread>
#include <vector>

#include <torch/torch.h>

namespace {

constexpr double kExperimentBaselineSimsPerS = 2553.6;
constexpr double kExperimentBaselineSecPerGame = 2.8;

struct CpuTimes {
    uint64_t idle = 0;
    uint64_t total = 0;
};

struct LoadSample {
    double cpu_total_pct = 0.0;
    double loadavg1 = 0.0;
    int logical_cpus = 0;
};

void usage(const char* argv0) {
    std::cerr
        << "usage: " << argv0
        << " [--model scripted.pt] [--games N] [--n-sim N] [--pool-size N]"
        << " [--max-pending N] [--virtual-loss N] [--cache-visit-threshold N]"
        << " [--c-puct F] [--temperature F] [--epsilon-greedy F]"
        << " [--dir-alpha F] [--dir-epsilon F] [--learned-side both|ussr|us]"
        << " [--seed N] [--torch-threads N] [--torch-interop N]"
        << " [--forward-worker] [--load-threshold N] [--load-sample-ms N]"
        << " [--load-wait-s N] [--warmup N] [--repeats N]\n";
}

CpuTimes read_cpu_times() {
    std::ifstream in("/proc/stat");
    if (!in) {
        throw std::runtime_error("failed to read /proc/stat");
    }

    std::string label;
    CpuTimes out;
    uint64_t user = 0, nice = 0, system = 0, idle = 0, iowait = 0, irq = 0, softirq = 0, steal = 0;
    in >> label >> user >> nice >> system >> idle >> iowait >> irq >> softirq >> steal;
    out.idle = idle + iowait;
    out.total = user + nice + system + idle + iowait + irq + softirq + steal;
    return out;
}

double read_loadavg1() {
    std::ifstream in("/proc/loadavg");
    if (!in) {
        return 0.0;
    }
    double load1 = 0.0;
    in >> load1;
    return load1;
}

LoadSample sample_system_load(int sample_ms) {
    const auto start = read_cpu_times();
    std::this_thread::sleep_for(std::chrono::milliseconds(sample_ms));
    const auto end = read_cpu_times();

    const auto idle_delta = static_cast<double>(end.idle - start.idle);
    const auto total_delta = static_cast<double>(end.total - start.total);
    const auto busy_fraction = total_delta > 0.0 ? (1.0 - idle_delta / total_delta) : 0.0;
    const int logical_cpus = std::max(1u, std::thread::hardware_concurrency());

    return LoadSample{
        .cpu_total_pct = busy_fraction * static_cast<double>(logical_cpus) * 100.0,
        .loadavg1 = read_loadavg1(),
        .logical_cpus = logical_cpus,
    };
}

LoadSample wait_for_acceptable_load(double threshold_pct, int sample_ms, double wait_s) {
    for (;;) {
        const auto sample = sample_system_load(sample_ms);
        std::cout << std::fixed << std::setprecision(1)
                  << "[load] cpu_total=" << sample.cpu_total_pct << "% "
                  << "load1=" << sample.loadavg1 << " "
                  << "cpus=" << sample.logical_cpus << "\n";
        if (sample.cpu_total_pct <= threshold_pct) {
            return sample;
        }
        std::cout << "[load] above threshold " << threshold_pct << "%, sleeping for "
                  << wait_s << "s\n";
        std::this_thread::sleep_for(std::chrono::duration<double>(wait_s));
    }
}

}  // namespace

int main(int argc, char** argv) {
    try {
        std::string model_path = "data/checkpoints/v99_cf_1x95_s7/baseline_best_scripted.pt";
        int games = 32;
        int n_sim = 50;
        int pool_size = 32;
        int max_pending = 8;
        int virtual_loss = 3;
        int cache_visit_threshold = 0;
        float c_puct = 1.5f;
        float temperature = 1.0f;
        float epsilon_greedy = 0.0f;
        float dir_alpha = 0.3f;
        float dir_epsilon = 0.25f;
        std::optional<ts::Side> learned_side = std::nullopt;
        uint32_t seed = 12345U;
        int torch_threads = 1;
        int torch_interop = 1;
        bool forward_worker = false;
        double load_threshold = 1000.0;
        int load_sample_ms = 250;
        double load_wait_s = 5.0;
        int warmup = 1;
        int repeats = 1;

        for (int i = 1; i < argc; ++i) {
            const std::string_view arg = argv[i];
            auto require_value = [&](const char* flag) -> std::string_view {
                if (i + 1 >= argc) {
                    throw std::invalid_argument(std::string("missing value for ") + flag);
                }
                return argv[++i];
            };

            if (arg == "--model") {
                model_path = std::string(require_value("--model"));
            } else if (arg == "--games") {
                games = std::stoi(std::string(require_value("--games")));
            } else if (arg == "--n-sim") {
                n_sim = std::stoi(std::string(require_value("--n-sim")));
            } else if (arg == "--pool-size") {
                pool_size = std::stoi(std::string(require_value("--pool-size")));
            } else if (arg == "--max-pending") {
                max_pending = std::stoi(std::string(require_value("--max-pending")));
            } else if (arg == "--virtual-loss") {
                virtual_loss = std::stoi(std::string(require_value("--virtual-loss")));
            } else if (arg == "--cache-visit-threshold") {
                cache_visit_threshold = std::stoi(std::string(require_value("--cache-visit-threshold")));
            } else if (arg == "--c-puct") {
                c_puct = std::stof(std::string(require_value("--c-puct")));
            } else if (arg == "--temperature") {
                temperature = std::stof(std::string(require_value("--temperature")));
            } else if (arg == "--epsilon-greedy") {
                epsilon_greedy = std::stof(std::string(require_value("--epsilon-greedy")));
            } else if (arg == "--dir-alpha") {
                dir_alpha = std::stof(std::string(require_value("--dir-alpha")));
            } else if (arg == "--dir-epsilon") {
                dir_epsilon = std::stof(std::string(require_value("--dir-epsilon")));
            } else if (arg == "--learned-side") {
                const auto value = std::string(require_value("--learned-side"));
                if (value == "both") {
                    learned_side.reset();
                } else if (value == "ussr" || value == "USSR") {
                    learned_side = ts::Side::USSR;
                } else if (value == "us" || value == "US") {
                    learned_side = ts::Side::US;
                } else {
                    throw std::invalid_argument("--learned-side must be both|ussr|us");
                }
            } else if (arg == "--seed") {
                seed = static_cast<uint32_t>(std::stoul(std::string(require_value("--seed"))));
            } else if (arg == "--torch-threads") {
                torch_threads = std::stoi(std::string(require_value("--torch-threads")));
            } else if (arg == "--torch-interop") {
                torch_interop = std::stoi(std::string(require_value("--torch-interop")));
            } else if (arg == "--forward-worker") {
                forward_worker = true;
            } else if (arg == "--load-threshold") {
                load_threshold = std::stod(std::string(require_value("--load-threshold")));
            } else if (arg == "--load-sample-ms") {
                load_sample_ms = std::stoi(std::string(require_value("--load-sample-ms")));
            } else if (arg == "--load-wait-s") {
                load_wait_s = std::stod(std::string(require_value("--load-wait-s")));
            } else if (arg == "--warmup") {
                warmup = std::stoi(std::string(require_value("--warmup")));
            } else if (arg == "--repeats") {
                repeats = std::stoi(std::string(require_value("--repeats")));
            } else if (arg == "--help" || arg == "-h") {
                usage(argv[0]);
                return 0;
            } else {
                usage(argv[0]);
                throw std::runtime_error("unknown argument: " + std::string(arg));
            }
        }

        if (games <= 0 || n_sim < 0 || pool_size <= 0 || max_pending <= 0 || virtual_loss <= 0 ||
            cache_visit_threshold < 0 || torch_threads <= 0 || torch_interop <= 0 ||
            warmup < 0 || repeats <= 0 || load_sample_ms <= 0 || load_wait_s < 0.0 || load_threshold <= 0.0) {
            throw std::invalid_argument("invalid non-positive argument");
        }

        at::set_num_threads(torch_threads);
        at::set_num_interop_threads(torch_interop);

        torch::jit::script::Module model = torch::jit::load(model_path, torch::kCPU);
        model.eval();

        ts::fastmcts::BenchConfig config;
        config.mcts.n_simulations = n_sim;
        config.mcts.c_puct = c_puct;
        config.mcts.dir_alpha = dir_alpha;
        config.mcts.dir_epsilon = dir_epsilon;
        config.pool_size = pool_size;
        config.max_pending = max_pending;
        config.virtual_loss_weight = virtual_loss;
        config.cache_visit_threshold = cache_visit_threshold;
        config.temperature = temperature;
        config.epsilon_greedy = epsilon_greedy;
        config.learned_side = learned_side;
        config.use_forward_worker = forward_worker;

        std::cout << std::fixed << std::setprecision(3)
                  << "[config] model=" << model_path
                  << " games=" << games
                  << " n_sim=" << n_sim
                  << " pool=" << pool_size
                  << " max_pending=" << max_pending
                  << " torch_threads=" << torch_threads
                  << " torch_interop=" << torch_interop
                  << " forward_worker=" << (forward_worker ? 1 : 0)
                  << " learned_side=" << (learned_side == ts::Side::USSR ? "ussr" : learned_side == ts::Side::US ? "us" : "both")
                  << " warmup=" << warmup
                  << " repeats=" << repeats
                  << " baseline_sims_per_s=" << kExperimentBaselineSimsPerS
                  << " baseline_s_per_game=" << kExperimentBaselineSecPerGame
                  << "\n";

        std::vector<ts::fastmcts::BenchResult> measured;
        measured.reserve(static_cast<size_t>(repeats));

        for (int run = 0; run < warmup + repeats; ++run) {
            const bool is_warmup = run < warmup;
            const auto load_before = wait_for_acceptable_load(load_threshold, load_sample_ms, load_wait_s);
            const auto result = ts::fastmcts::benchmark_mcts_fast(
                games,
                model,
                config,
                seed + static_cast<uint32_t>(run * 100000U),
                torch::kCPU
            );
            const auto load_after = sample_system_load(load_sample_ms);

            std::cout << std::fixed << std::setprecision(1)
                      << "[" << (is_warmup ? "warmup" : "run") << " " << (run + 1) << "/" << (warmup + repeats) << "] "
                      << "pre_load=" << load_before.cpu_total_pct << "% "
                      << "post_load=" << load_after.cpu_total_pct << "% "
                      << "elapsed=" << result.elapsed_s << "s "
                      << "sims=" << result.total_simulations << " "
                      << "baseline_sims_per_s=" << kExperimentBaselineSimsPerS << " "
                      << "current_sims_per_s=" << result.sims_per_s << " "
                      << "speedup=" << (result.sims_per_s / kExperimentBaselineSimsPerS) << "x "
                      << "decisions=" << result.mcts_decisions << " "
                      << "avg_batch=" << result.avg_batch << "\n";
            std::cout << std::fixed << std::setprecision(3)
                      << "[" << (is_warmup ? "warmup" : "run") << " " << (run + 1) << "/" << (warmup + repeats) << "] "
                      << "advance=" << result.t_advance << "s "
                      << "select=" << result.t_select << "s "
                      << "nn=" << result.t_nn << "s "
                      << "expand=" << result.t_expand << "s "
                      << "commit=" << result.t_commit << "s "
                      << "wins=" << result.wins << " "
                      << "losses=" << result.losses << " "
                      << "draws=" << result.draws << "\n";

            if (!is_warmup) {
                measured.push_back(result);
            }
        }

        double best_sims_per_s = 0.0;
        double mean_sims_per_s = 0.0;
        double mean_elapsed = 0.0;
        for (const auto& result : measured) {
            best_sims_per_s = std::max(best_sims_per_s, result.sims_per_s);
            mean_sims_per_s += result.sims_per_s;
            mean_elapsed += result.elapsed_s;
        }
        mean_sims_per_s /= static_cast<double>(measured.size());
        mean_elapsed /= static_cast<double>(measured.size());

        std::cout << std::fixed << std::setprecision(1)
                  << "[summary] repeats=" << measured.size()
                  << " baseline_sims_per_s=" << kExperimentBaselineSimsPerS
                  << " mean_current_sims_per_s=" << mean_sims_per_s
                  << " best_current_sims_per_s=" << best_sims_per_s
                  << " mean_speedup=" << (mean_sims_per_s / kExperimentBaselineSimsPerS) << "x"
                  << " best_speedup=" << (best_sims_per_s / kExperimentBaselineSimsPerS) << "x"
                  << " mean_elapsed=" << mean_elapsed << "s\n";
        return 0;
    } catch (const std::exception& ex) {
        std::cerr << "error: " << ex.what() << "\n";
        return 1;
    }
}

#endif
