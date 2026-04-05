// Collect full-game self-play rows using wavefront-batched native MCTS.

#include <cstdint>
#include <fstream>
#include <iostream>
#include <optional>
#include <stdexcept>
#include <string_view>

#include <torch/script.h>

#include "mcts_batched.hpp"

namespace {

void usage(const char* argv0) {
    std::cerr
        << "usage: " << argv0
        << " --model scripted.pt --out rows.jsonl [--games N] [--n-sim N]"
        << " [--pool-size N] [--max-pending N] [--c-puct F] [--seed N] [--virtual-loss N]"
        << " [--temperature F] [--dir-alpha F] [--dir-epsilon F]"
        << " [--epsilon-greedy F] [--learned-side ussr|us]"
        << " [--heuristic-teacher-mode] [--game-id-prefix PREFIX]\n";
}

}  // namespace

int main(int argc, char** argv) {
    try {
        std::optional<std::string> model_path;
        std::optional<std::string> out_path;
        int game_count = 10;
        int n_simulations = 200;
        int pool_size = 32;
        int max_pending = 8;
        int virtual_loss = 3;
        float c_puct = 1.5f;
        float temperature = 0.0f;
        float dir_alpha = -1.0f;   // <0 means use MctsConfig default
        float dir_epsilon = -1.0f; // <0 means use MctsConfig default
        float epsilon_greedy = 0.0f;
        std::optional<ts::Side> learned_side;
        std::optional<uint32_t> seed = 12345U;
        bool heuristic_teacher_mode = false;
        std::optional<std::string> game_id_prefix;

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
            } else if (arg == "--out") {
                out_path = std::string(require_value("--out"));
            } else if (arg == "--games") {
                game_count = std::stoi(std::string(require_value("--games")));
            } else if (arg == "--n-sim") {
                n_simulations = std::stoi(std::string(require_value("--n-sim")));
            } else if (arg == "--pool-size") {
                pool_size = std::stoi(std::string(require_value("--pool-size")));
            } else if (arg == "--max-pending") {
                max_pending = std::stoi(std::string(require_value("--max-pending")));
            } else if (arg == "--c-puct") {
                c_puct = std::stof(std::string(require_value("--c-puct")));
            } else if (arg == "--seed") {
                seed = static_cast<uint32_t>(std::stoul(std::string(require_value("--seed"))));
            } else if (arg == "--virtual-loss") {
                virtual_loss = std::stoi(std::string(require_value("--virtual-loss")));
            } else if (arg == "--temperature") {
                temperature = std::stof(std::string(require_value("--temperature")));
            } else if (arg == "--dir-alpha") {
                dir_alpha = std::stof(std::string(require_value("--dir-alpha")));
            } else if (arg == "--dir-epsilon") {
                dir_epsilon = std::stof(std::string(require_value("--dir-epsilon")));
            } else if (arg == "--epsilon-greedy") {
                epsilon_greedy = std::stof(std::string(require_value("--epsilon-greedy")));
            } else if (arg == "--learned-side") {
                const auto val = std::string(require_value("--learned-side"));
                if (val == "ussr" || val == "USSR") {
                    learned_side = ts::Side::USSR;
                } else if (val == "us" || val == "US") {
                    learned_side = ts::Side::US;
                } else {
                    throw std::invalid_argument("--learned-side must be 'ussr' or 'us'");
                }
            } else if (arg == "--heuristic-teacher-mode") {
                heuristic_teacher_mode = true;
            } else if (arg == "--game-id-prefix") {
                game_id_prefix = std::string(require_value("--game-id-prefix"));
            } else if (arg == "--help" || arg == "-h") {
                usage(argv[0]);
                return 0;
            } else {
                usage(argv[0]);
                throw std::runtime_error(std::string("unknown argument: ") + std::string(arg));
            }
        }

        if (!model_path.has_value() || !out_path.has_value()) {
            usage(argv[0]);
            throw std::runtime_error("--model and --out are required");
        }
        if (game_count <= 0) {
            throw std::runtime_error("--games must be positive");
        }
        if (n_simulations < 0) {
            throw std::runtime_error("--n-sim must be non-negative");
        }
        if (pool_size <= 0) {
            throw std::runtime_error("--pool-size must be positive");
        }
        if (max_pending <= 0) {
            throw std::runtime_error("--max-pending must be positive");
        }
        if (c_puct <= 0.0f) {
            throw std::runtime_error("--c-puct must be positive");
        }
        if (virtual_loss <= 0) {
            throw std::runtime_error("--virtual-loss must be positive");
        }
        if (temperature < 0.0f) {
            throw std::runtime_error("--temperature must be non-negative");
        }

        torch::jit::script::Module model = torch::jit::load(*model_path);
        model.eval();

        std::ofstream out(*out_path);
        if (!out) {
            throw std::runtime_error("failed to open output file");
        }

        ts::BatchedMctsConfig config;
        config.mcts.n_simulations = n_simulations;
        config.mcts.c_puct = c_puct;
        if (dir_alpha >= 0.0f) config.mcts.dir_alpha = dir_alpha;
        if (dir_epsilon >= 0.0f) config.mcts.dir_epsilon = dir_epsilon;
        config.pool_size = pool_size;
        config.max_pending = max_pending;
        config.virtual_loss_weight = virtual_loss;
        config.temperature = temperature;
        config.epsilon_greedy = epsilon_greedy;
        config.learned_side = learned_side;
        config.heuristic_teacher_mode = heuristic_teacher_mode;
        // Default game_id_prefix to "selfplay" in heuristic_teacher_mode so produced
        // game_ids match existing heuristic dataset rows for teacher target joining.
        if (game_id_prefix.has_value()) {
            config.game_id_prefix = *game_id_prefix;
        } else if (heuristic_teacher_mode) {
            config.game_id_prefix = "selfplay";
        }

        ts::collect_games_batched(game_count, model, config, seed.value_or(12345U), out);
        return 0;
    } catch (const std::exception& ex) {
        std::cerr << "error: " << ex.what() << "\n";
        return 1;
    }
}
