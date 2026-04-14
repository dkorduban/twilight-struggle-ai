// Benchmark runner for the standalone fast batched MCTS replica.

#include "fast_mcts_batched.hpp"

#if defined(TS_BUILD_TORCH_RUNTIME)

#include <atomic>
#include <chrono>
#include <cstdint>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <memory>
#include <optional>
#include <stdexcept>
#include <string>
#include <string_view>
#include <thread>
#include <vector>

#include <sched.h>
#include <sys/wait.h>
#include <unistd.h>

#include <torch/torch.h>

namespace {

constexpr double kWorkingBaselineSimsPerS = 8174.7;
constexpr double kGoalMultiple = 3.0;

struct CpuTimes {
    uint64_t idle = 0;
    uint64_t total = 0;
};

struct LoadSample {
    double cpu_total_pct = 0.0;
    double loadavg1 = 0.0;
    int logical_cpus = 0;
};

std::optional<uint64_t> read_max_cpu_mhz_x1000() {
    std::ifstream in("/proc/cpuinfo");
    if (!in) {
        return std::nullopt;
    }

    std::string line;
    uint64_t best = 0;
    while (std::getline(in, line)) {
        constexpr std::string_view kPrefix = "cpu MHz";
        if (!line.starts_with(kPrefix)) {
            continue;
        }
        const auto colon = line.find(':');
        if (colon == std::string::npos) {
            continue;
        }
        try {
            const auto mhz = std::stod(line.substr(colon + 1));
            if (mhz > 0.0) {
                const auto mhz_x1000 = static_cast<uint64_t>(mhz * 1000.0);
                best = std::max(best, mhz_x1000);
            }
        } catch (const std::exception&) {
        }
    }

    if (best == 0) {
        return std::nullopt;
    }
    return best;
}

void usage(const char* argv0) {
    std::cerr
        << "usage: " << argv0
        << " [--model scripted.pt] [--games N] [--n-sim N] [--pool-size N]"
        << " [--max-pending N] [--virtual-loss N] [--cache-visit-threshold N]"
        << " [--c-puct F] [--temperature F] [--epsilon-greedy F]"
        << " [--dir-alpha F] [--dir-epsilon F] [--learned-side both|ussr|us]"
        << " [--seed N] [--mcts-workers N] [--torch-threads N] [--torch-interop N]"
        << " [--influence-samples N] [--influence-t-strategy F] [--influence-t-country F]"
        << " [--influence-proportional-first 0|1]"
        << " [--pin-workers] [--worker-core-span N]"
        << " [--forward-worker] [--load-threshold N] [--load-sample-ms N]"
        << " [--load-wait-s N] [--warmup N] [--repeats N]"
        << " [--baseline-sims F] [--target-multiple F]\n";
}

int split_even(int total, int parts, int index) {
    const int base = total / parts;
    const int remainder = total % parts;
    return base + (index < remainder ? 1 : 0);
}

std::vector<int> build_worker_cpu_set(int worker_index, int worker_count, int logical_cpus, int core_span) {
    if (worker_index < 0 || worker_count <= 0 || logical_cpus <= 0 || core_span <= 0) {
        return {};
    }

    const int span = std::min(core_span, logical_cpus);
    const int start = (worker_index * logical_cpus) / worker_count;
    std::vector<int> cpus;
    cpus.reserve(static_cast<size_t>(span));
    for (int offset = 0; offset < span; ++offset) {
        const int cpu = (start + offset) % logical_cpus;
        if (std::find(cpus.begin(), cpus.end(), cpu) == cpus.end()) {
            cpus.push_back(cpu);
        }
    }
    return cpus;
}

void pin_current_process_or_throw(const std::vector<int>& cpus) {
    if (cpus.empty()) {
        return;
    }

    cpu_set_t mask;
    CPU_ZERO(&mask);
    for (const int cpu : cpus) {
        CPU_SET(cpu, &mask);
    }
    if (::sched_setaffinity(0, sizeof(mask), &mask) != 0) {
        throw std::runtime_error("sched_setaffinity failed");
    }
}

ts::fastmcts::BenchResult merge_worker_results(
    const std::vector<ts::fastmcts::BenchResult>& workers,
    int n_games,
    int pool_size,
    int n_simulations,
    double elapsed_s
) {
    ts::fastmcts::BenchResult merged;
    merged.n_games = n_games;
    merged.pool_size = pool_size;
    merged.n_simulations = n_simulations;
    merged.elapsed_s = elapsed_s;

    for (const auto& worker : workers) {
        merged.total_simulations += worker.total_simulations;
        merged.mcts_decisions += worker.mcts_decisions;
        merged.n_batches += worker.n_batches;
        merged.total_batch_items += worker.total_batch_items;
        merged.wins += worker.wins;
        merged.losses += worker.losses;
        merged.draws += worker.draws;
        merged.t_advance += worker.t_advance;
        merged.t_select += worker.t_select;
        merged.t_nn += worker.t_nn;
        merged.t_expand += worker.t_expand;
        merged.t_commit += worker.t_commit;
    }

    merged.sims_per_s = elapsed_s > 0.0 ? static_cast<double>(merged.total_simulations) / elapsed_s : 0.0;
    merged.avg_batch = merged.n_batches > 0
        ? static_cast<double>(merged.total_batch_items) / static_cast<double>(merged.n_batches)
        : 0.0;
    return merged;
}

struct WorkerPipeMessage {
    int ok = 0;
    ts::fastmcts::BenchResult result{};
    char error[256] = {};
};

void write_all_or_throw(int fd, const void* buffer, size_t size) {
    const auto* bytes = static_cast<const char*>(buffer);
    size_t written = 0;
    while (written < size) {
        const auto rc = ::write(fd, bytes + written, size - written);
        if (rc <= 0) {
            throw std::runtime_error("failed to write worker pipe");
        }
        written += static_cast<size_t>(rc);
    }
}

void read_all_or_throw(int fd, void* buffer, size_t size) {
    auto* bytes = static_cast<char*>(buffer);
    size_t read_total = 0;
    while (read_total < size) {
        const auto rc = ::read(fd, bytes + read_total, size - read_total);
        if (rc <= 0) {
            throw std::runtime_error("failed to read worker pipe");
        }
        read_total += static_cast<size_t>(rc);
    }
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
        int mcts_workers = 1;
        int torch_threads = 1;
        int torch_interop = 1;
        int influence_samples = 1;
        float influence_t_strategy = 0.0f;
        float influence_t_country = 0.0f;
        bool influence_proportional_first = true;
        bool pin_workers = false;
        int worker_core_span = 0;
        bool forward_worker = false;
        double load_threshold = 1000.0;
        int load_sample_ms = 250;
        double load_wait_s = 5.0;
        int warmup = 1;
        int repeats = 1;
        double baseline_sims = kWorkingBaselineSimsPerS;
        double target_multiple = kGoalMultiple;
        int child_output_fd = -1;
        int worker_index = -1;
        int worker_total = 1;

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
            } else if (arg == "--mcts-workers") {
                mcts_workers = std::stoi(std::string(require_value("--mcts-workers")));
            } else if (arg == "--torch-threads") {
                torch_threads = std::stoi(std::string(require_value("--torch-threads")));
            } else if (arg == "--torch-interop") {
                torch_interop = std::stoi(std::string(require_value("--torch-interop")));
            } else if (arg == "--influence-samples") {
                influence_samples = std::stoi(std::string(require_value("--influence-samples")));
            } else if (arg == "--influence-t-strategy") {
                influence_t_strategy = std::stof(std::string(require_value("--influence-t-strategy")));
            } else if (arg == "--influence-t-country") {
                influence_t_country = std::stof(std::string(require_value("--influence-t-country")));
            } else if (arg == "--influence-proportional-first") {
                influence_proportional_first = std::stoi(std::string(require_value("--influence-proportional-first"))) != 0;
            } else if (arg == "--pin-workers") {
                pin_workers = true;
            } else if (arg == "--worker-core-span") {
                worker_core_span = std::stoi(std::string(require_value("--worker-core-span")));
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
            } else if (arg == "--baseline-sims") {
                baseline_sims = std::stod(std::string(require_value("--baseline-sims")));
            } else if (arg == "--target-multiple") {
                target_multiple = std::stod(std::string(require_value("--target-multiple")));
            } else if (arg == "--child-output-fd") {
                child_output_fd = std::stoi(std::string(require_value("--child-output-fd")));
            } else if (arg == "--worker-index") {
                worker_index = std::stoi(std::string(require_value("--worker-index")));
            } else if (arg == "--worker-total") {
                worker_total = std::stoi(std::string(require_value("--worker-total")));
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
            mcts_workers <= 0 || influence_samples <= 0 ||
            worker_core_span < 0 || worker_total <= 0 ||
            warmup < 0 || repeats <= 0 || load_sample_ms <= 0 || load_wait_s < 0.0 || load_threshold <= 0.0 ||
            baseline_sims <= 0.0 || target_multiple <= 0.0) {
            throw std::invalid_argument("invalid non-positive argument");
        }
        if (worker_index >= worker_total) {
            throw std::invalid_argument("worker-index must be less than worker-total");
        }

        const int logical_cpus = std::max(1u, std::thread::hardware_concurrency());
        const int effective_core_span = std::max(1, worker_core_span > 0 ? worker_core_span : torch_threads);
        if (pin_workers && worker_index >= 0) {
            const auto pinned_cpus = build_worker_cpu_set(worker_index, worker_total, logical_cpus, effective_core_span);
            pin_current_process_or_throw(pinned_cpus);
        }

        at::set_num_threads(torch_threads);
        at::set_num_interop_threads(torch_interop);
        std::unique_ptr<torch::jit::script::Module> single_worker_model;
        if (mcts_workers == 1) {
            single_worker_model = std::make_unique<torch::jit::script::Module>(torch::jit::load(model_path, torch::kCPU));
            single_worker_model->eval();
        }

        ts::fastmcts::BenchConfig config;
        config.mcts.n_simulations = n_sim;
        config.mcts.c_puct = c_puct;
        config.mcts.dir_alpha = dir_alpha;
        config.mcts.dir_epsilon = dir_epsilon;
        config.pool_size = pool_size;
        config.max_pending = max_pending;
        config.virtual_loss_weight = virtual_loss;
        config.cache_visit_threshold = cache_visit_threshold;
        config.influence_samples = influence_samples;
        config.influence_t_strategy = influence_t_strategy;
        config.influence_t_country = influence_t_country;
        config.influence_proportional_first = influence_proportional_first;
        config.temperature = temperature;
        config.epsilon_greedy = epsilon_greedy;
        config.learned_side = learned_side;
        config.use_forward_worker = forward_worker;

        if (child_output_fd >= 0) {
            WorkerPipeMessage message;
            try {
                torch::jit::script::Module model = torch::jit::load(model_path, torch::kCPU);
                model.eval();
                message.ok = 1;
                message.result = ts::fastmcts::benchmark_mcts_fast(
                    games,
                    model,
                    config,
                    seed,
                    torch::kCPU
                );
            } catch (const std::exception& ex) {
                message.ok = 0;
                std::strncpy(message.error, ex.what(), sizeof(message.error) - 1);
                message.error[sizeof(message.error) - 1] = '\0';
            }
            write_all_or_throw(child_output_fd, &message, sizeof(message));
            ::close(child_output_fd);
            return message.ok ? 0 : 1;
        }

        std::cout << std::fixed << std::setprecision(3)
                  << "[config] model=" << model_path
                  << " games=" << games
                  << " n_sim=" << n_sim
                  << " pool=" << pool_size
                  << " max_pending=" << max_pending
                  << " mcts_workers=" << mcts_workers
                  << " torch_threads=" << torch_threads
                  << " torch_interop=" << torch_interop
                  << " influence_samples=" << influence_samples
                  << " influence_t_strategy=" << influence_t_strategy
                  << " influence_t_country=" << influence_t_country
                  << " influence_proportional_first=" << (influence_proportional_first ? 1 : 0)
                  << " pin_workers=" << (pin_workers ? 1 : 0)
                  << " worker_core_span=" << effective_core_span
                  << " forward_worker=" << (forward_worker ? 1 : 0)
                  << " learned_side=" << (learned_side == ts::Side::USSR ? "ussr" : learned_side == ts::Side::US ? "us" : "both")
                  << " warmup=" << warmup
                  << " repeats=" << repeats
                  << " baseline_sims_per_s=" << baseline_sims
                  << " target_multiple=" << target_multiple
                  << " target_sims_per_s=" << (baseline_sims * target_multiple)
                  << "\n";

        std::vector<ts::fastmcts::BenchResult> measured;
        measured.reserve(static_cast<size_t>(repeats));

        for (int run = 0; run < warmup + repeats; ++run) {
            const bool is_warmup = run < warmup;
            const auto load_before = wait_for_acceptable_load(load_threshold, load_sample_ms, load_wait_s);
            const auto mhz_before = read_max_cpu_mhz_x1000();
            std::atomic<bool> stop_freq_sampler = false;
            std::atomic<uint64_t> max_run_mhz_x1000 = mhz_before.value_or(0);
            std::thread freq_sampler([&] {
                while (!stop_freq_sampler.load(std::memory_order_relaxed)) {
                    if (const auto mhz = read_max_cpu_mhz_x1000(); mhz.has_value()) {
                        auto current = max_run_mhz_x1000.load(std::memory_order_relaxed);
                        while (current < *mhz &&
                               !max_run_mhz_x1000.compare_exchange_weak(
                                   current,
                                   *mhz,
                                   std::memory_order_relaxed,
                                   std::memory_order_relaxed
                               )) {
                        }
                    }
                    std::this_thread::sleep_for(std::chrono::milliseconds(200));
                }
            });
            ts::fastmcts::BenchResult result;
            try {
                if (mcts_workers == 1) {
                    result = ts::fastmcts::benchmark_mcts_fast(
                        games,
                        *single_worker_model,
                        config,
                        seed + static_cast<uint32_t>(run * 100000U),
                        torch::kCPU
                    );
                } else {
                struct WorkerProc {
                    pid_t pid = -1;
                    int result_fd = -1;
                };

                std::vector<WorkerProc> workers;
                workers.reserve(static_cast<size_t>(mcts_workers));
                for (int worker = 0; worker < mcts_workers; ++worker) {
                    const int worker_games = split_even(games, mcts_workers, worker);
                    const int worker_pool = std::max(1, split_even(pool_size, mcts_workers, worker));
                    if (worker_games <= 0) {
                        continue;
                    }

                    int result_pipe[2];
                    if (::pipe(result_pipe) != 0) {
                        throw std::runtime_error("failed to create worker result pipe");
                    }

                    const auto pid = ::fork();
                    if (pid < 0) {
                        throw std::runtime_error("failed to fork worker");
                    }
                    if (pid == 0) {
                        ::close(result_pipe[0]);
                        std::vector<std::string> child_args_storage = {
                            argv[0],
                            "--model", model_path,
                            "--games", std::to_string(worker_games),
                            "--n-sim", std::to_string(n_sim),
                            "--pool-size", std::to_string(worker_pool),
                            "--max-pending", std::to_string(max_pending),
                            "--virtual-loss", std::to_string(virtual_loss),
                            "--cache-visit-threshold", std::to_string(cache_visit_threshold),
                            "--c-puct", std::to_string(c_puct),
                            "--temperature", std::to_string(temperature),
                            "--epsilon-greedy", std::to_string(epsilon_greedy),
                            "--dir-alpha", std::to_string(dir_alpha),
                            "--dir-epsilon", std::to_string(dir_epsilon),
                            "--seed", std::to_string(seed + static_cast<uint32_t>(run * 100000U + worker * 1000U)),
                            "--mcts-workers", "1",
                            "--torch-threads", std::to_string(torch_threads),
                            "--torch-interop", std::to_string(torch_interop),
                            "--influence-samples", std::to_string(influence_samples),
                            "--influence-t-strategy", std::to_string(influence_t_strategy),
                            "--influence-t-country", std::to_string(influence_t_country),
                            "--influence-proportional-first", influence_proportional_first ? "1" : "0",
                            "--warmup", "0",
                            "--repeats", "1",
                            "--worker-index", std::to_string(worker),
                            "--worker-total", std::to_string(mcts_workers),
                            "--worker-core-span", std::to_string(effective_core_span),
                            "--child-output-fd", std::to_string(result_pipe[1]),
                        };
                        if (pin_workers) {
                            child_args_storage.push_back("--pin-workers");
                        }
                        if (forward_worker) {
                            child_args_storage.push_back("--forward-worker");
                        }
                        if (learned_side == ts::Side::USSR) {
                            child_args_storage.push_back("--learned-side");
                            child_args_storage.push_back("ussr");
                        } else if (learned_side == ts::Side::US) {
                            child_args_storage.push_back("--learned-side");
                            child_args_storage.push_back("us");
                        }

                        std::vector<char*> child_argv;
                        child_argv.reserve(child_args_storage.size() + 1);
                        for (auto& value : child_args_storage) {
                            child_argv.push_back(value.data());
                        }
                        child_argv.push_back(nullptr);
                        ::execvp(child_argv[0], child_argv.data());
                        _exit(127);
                    }

                    ::close(result_pipe[1]);
                    workers.push_back(WorkerProc{
                        .pid = pid,
                        .result_fd = result_pipe[0],
                    });
                }

                std::vector<ts::fastmcts::BenchResult> worker_results;
                worker_results.reserve(workers.size());
                double max_elapsed_s = 0.0;
                for (const auto& worker : workers) {
                    WorkerPipeMessage message;
                    read_all_or_throw(worker.result_fd, &message, sizeof(message));
                    ::close(worker.result_fd);
                    if (message.ok == 0) {
                        throw std::runtime_error(std::string("worker failed: ") + message.error);
                    }
                    worker_results.push_back(message.result);
                    max_elapsed_s = std::max(max_elapsed_s, message.result.elapsed_s);
                }

                for (const auto& worker : workers) {
                    int status = 0;
                    (void)::waitpid(worker.pid, &status, 0);
                }

                result = merge_worker_results(worker_results, games, pool_size, n_sim, max_elapsed_s);
            }
            } catch (...) {
                stop_freq_sampler.store(true, std::memory_order_relaxed);
                freq_sampler.join();
                throw;
            }
            stop_freq_sampler.store(true, std::memory_order_relaxed);
            freq_sampler.join();
            const auto load_after = sample_system_load(load_sample_ms);
            const auto mhz_after = read_max_cpu_mhz_x1000();

            std::cout << std::fixed << std::setprecision(1)
                      << "[" << (is_warmup ? "warmup" : "run") << " " << (run + 1) << "/" << (warmup + repeats) << "] "
                      << "pre_load=" << load_before.cpu_total_pct << "% "
                      << "post_load=" << load_after.cpu_total_pct << "% "
                      << "pre_max_mhz=" << (mhz_before.has_value() ? static_cast<double>(*mhz_before) / 1000.0 : 0.0) << " "
                      << "run_max_mhz=" << static_cast<double>(max_run_mhz_x1000.load(std::memory_order_relaxed)) / 1000.0 << " "
                      << "post_max_mhz=" << (mhz_after.has_value() ? static_cast<double>(*mhz_after) / 1000.0 : 0.0) << " "
                      << "elapsed=" << result.elapsed_s << "s "
                      << "sims=" << result.total_simulations << " "
                      << "baseline_sims_per_s=" << baseline_sims << " "
                      << "current_sims_per_s=" << result.sims_per_s << " "
                      << "speedup=" << (result.sims_per_s / baseline_sims) << "x "
                      << "target_sims_per_s=" << (baseline_sims * target_multiple) << " "
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
                  << " baseline_sims_per_s=" << baseline_sims
                  << " mean_current_sims_per_s=" << mean_sims_per_s
                  << " best_current_sims_per_s=" << best_sims_per_s
                  << " mean_speedup=" << (mean_sims_per_s / baseline_sims) << "x"
                  << " best_speedup=" << (best_sims_per_s / baseline_sims) << "x"
                  << " target_sims_per_s=" << (baseline_sims * target_multiple)
                  << " mean_elapsed=" << mean_elapsed << "s\n";
        return 0;
    } catch (const std::exception& ex) {
        std::cerr << "error: " << ex.what() << "\n";
        return 1;
    }
}

#endif
