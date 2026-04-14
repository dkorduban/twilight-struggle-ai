#include <catch2/catch_test_macros.hpp>

#if defined(TS_BUILD_TORCH_RUNTIME)

#include <algorithm>
#include <cstdlib>
#include <filesystem>
#include <fstream>
#include <optional>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

#include <torch/script.h>

#include "game_data.hpp"
#include "game_state.hpp"
#include "ismcts.hpp"
#include "legal_actions.hpp"
#include "step.hpp"

using namespace ts;

namespace {

std::string shell_quote(const std::string& value) {
    std::string quoted = "'";
    for (const char ch : value) {
        if (ch == '\'') {
            quoted += "'\\''";
        } else {
            quoted.push_back(ch);
        }
    }
    quoted.push_back('\'');
    return quoted;
}

std::filesystem::path model_cache_dir() {
    const auto dir = std::filesystem::temp_directory_path() / "ts_ismcts_regression";
    std::filesystem::create_directories(dir);
    return dir;
}

std::filesystem::path ensure_stub_model_file(
    const std::string& name,
    int preferred_card_id,
    int preferred_mode
) {
    const auto cache_dir = model_cache_dir();
    const auto script_path = cache_dir / "generate_stub_model.py";
    const auto model_path = cache_dir / (name + ".pt");

    if (std::filesystem::exists(model_path)) {
        return model_path;
    }

    {
        std::ofstream script(script_path);
        if (!script) {
            throw std::runtime_error("failed to open stub-model generator script for writing");
        }
        script << R"PY(import sys
from pathlib import Path

import torch


class StubModel(torch.nn.Module):
    def __init__(self, preferred_card_id: int, preferred_mode: int):
        super().__init__()
        self.preferred_card_id = preferred_card_id
        self.preferred_mode = preferred_mode

    def forward(self, influence: torch.Tensor, cards: torch.Tensor, scalars: torch.Tensor):
        batch = influence.size(0)
        device = influence.device
        dtype = influence.dtype
        card_logits = torch.zeros((batch, 112), device=device, dtype=dtype)
        if self.preferred_card_id > 0:
            card_logits[:, self.preferred_card_id - 1] = 6.0
        mode_logits = torch.zeros((batch, 8), device=device, dtype=dtype)
        if self.preferred_mode >= 0:
            mode_logits[:, self.preferred_mode] = 6.0
        country_logits = torch.zeros((batch, 86), device=device, dtype=dtype)
        value = torch.zeros((batch, 1), device=device, dtype=dtype)
        return {
            "card_logits": card_logits,
            "mode_logits": mode_logits,
            "country_logits": country_logits,
            "value": value,
        }


output_path = Path(sys.argv[1])
preferred_card_id = int(sys.argv[2])
preferred_mode = int(sys.argv[3])
output_path.parent.mkdir(parents=True, exist_ok=True)
module = torch.jit.script(StubModel(preferred_card_id, preferred_mode))
module.save(output_path.as_posix())
)PY";
    }

    const auto python = repo_root() / ".venv" / "bin" / "python";
    if (!std::filesystem::exists(python)) {
        throw std::runtime_error("expected repo-local Python at " + python.string());
    }

    std::ostringstream cmd;
    cmd << shell_quote(python.string()) << ' '
        << shell_quote(script_path.string()) << ' '
        << shell_quote(model_path.string()) << ' '
        << preferred_card_id << ' '
        << preferred_mode;

    if (std::system(cmd.str().c_str()) != 0) {
        throw std::runtime_error("failed to generate TorchScript stub model");
    }
    if (!std::filesystem::exists(model_path)) {
        throw std::runtime_error("TorchScript stub model was not created");
    }
    return model_path;
}

torch::jit::script::Module load_stub_model(
    const std::string& name,
    int preferred_card_id,
    int preferred_mode
) {
    auto module = torch::jit::load(
        ensure_stub_model_file(name, preferred_card_id, preferred_mode).string(),
        torch::kCPU
    );
    module.eval();
    return module;
}

IsmctsConfig make_test_config(
    int n_determinizations,
    int n_simulations,
    bool use_rollout_backup = false
) {
    IsmctsConfig config;
    config.n_determinizations = n_determinizations;
    config.max_pending_per_det = 2;
    config.mcts_config.n_simulations = n_simulations;
    config.mcts_config.dir_alpha = 0.0f;
    config.mcts_config.dir_epsilon = 0.0f;
    config.mcts_config.use_rollout_backup = use_rollout_backup;
    config.mcts_config.value_weight = use_rollout_backup ? 0.0f : 1.0f;
    return config;
}

GameState make_midgame_action_round_state() {
    auto gs = reset_game(42);
    gs.pub.turn = 3;
    gs.pub.ar = 2;
    gs.pub.defcon = 4;
    gs.pub.phasing = Side::USSR;
    gs.pub.china_held_by = Side::US;
    gs.phase = GamePhase::ActionRound;
    gs.current_side = Side::USSR;
    gs.ar_index = 2;
    gs.setup_influence_remaining = {0, 0};
    gs.ussr_holds_china = false;
    gs.us_holds_china = true;
    gs.hands[to_index(Side::USSR)].reset();
    gs.hands[to_index(Side::US)].reset();
    gs.hands[to_index(Side::USSR)].set(7);
    gs.hands[to_index(Side::USSR)].set(9);
    gs.hands[to_index(Side::US)].set(13);
    gs.hands[to_index(Side::US)].set(23);
    gs.hands[to_index(Side::US)].set(25);
    return gs;
}

Observation make_hidden_info_observation() {
    auto gs = reset_game(77);
    gs.pub.turn = 3;
    gs.pub.ar = 2;
    gs.pub.defcon = 4;
    gs.pub.phasing = Side::USSR;
    gs.phase = GamePhase::ActionRound;
    gs.current_side = Side::USSR;
    gs.ar_index = 2;
    gs.setup_influence_remaining = {0, 0};
    return make_observation(gs, Side::USSR);
}

bool same_game_result(const GameResult& lhs, const GameResult& rhs) {
    return lhs.winner == rhs.winner &&
        lhs.final_vp == rhs.final_vp &&
        lhs.end_turn == rhs.end_turn &&
        lhs.end_reason == rhs.end_reason;
}

bool same_game_results(
    const std::vector<GameResult>& lhs,
    const std::vector<GameResult>& rhs
) {
    if (lhs.size() != rhs.size()) {
        return false;
    }
    for (size_t i = 0; i < lhs.size(); ++i) {
        if (!same_game_result(lhs[i], rhs[i])) {
            return false;
        }
    }
    return true;
}

bool same_ismcts_result(const IsmctsResult& lhs, const IsmctsResult& rhs) {
    if (lhs.best_action != rhs.best_action ||
        lhs.total_determinizations != rhs.total_determinizations ||
        lhs.mean_root_value != rhs.mean_root_value ||
        lhs.aggregated_edges.size() != rhs.aggregated_edges.size()) {
        return false;
    }

    for (size_t i = 0; i < lhs.aggregated_edges.size(); ++i) {
        const auto& left = lhs.aggregated_edges[i];
        const auto& right = rhs.aggregated_edges[i];
        if (left.action != right.action ||
            left.prior != right.prior ||
            left.visit_count != right.visit_count ||
            left.total_value != right.total_value) {
            return false;
        }
    }
    return true;
}

}  // namespace

TEST_CASE("play_ismcts_matchup_pooled terminates without tripping the loop guard", "[ismcts][regression][loop_guard]") {
    auto model = load_stub_model("ismcts_event_card9", /*preferred_card_id=*/9, static_cast<int>(ActionMode::Event));
    const auto config = make_test_config(/*n_determinizations=*/2, /*n_simulations=*/1);

    const auto results = play_ismcts_matchup_pooled(
        /*n_games=*/1,
        model,
        Side::USSR,
        config,
        /*pool_size=*/1,
        /*base_seed=*/1234,
        torch::kCPU
    );

    REQUIRE(results.size() == 1);
    CHECK(results.front().end_reason != "loop_guard");
    CHECK(results.front().end_turn >= 1);
    CHECK(results.front().end_turn <= 10);
}

TEST_CASE("ismcts determinization remains isolated across pooled searches", "[ismcts][regression][cloning]") {
    SECTION("pooled matchup stays stable as pending determinization width changes") {
        auto model = load_stub_model("ismcts_uniform", /*preferred_card_id=*/0, /*preferred_mode=*/-1);
        auto serial_config = make_test_config(/*n_determinizations=*/2, /*n_simulations=*/2, /*use_rollout_backup=*/true);
        serial_config.max_pending_per_det = 1;
        auto parallel_config = serial_config;
        parallel_config.max_pending_per_det = 2;

        const auto pooled_serial = play_ismcts_matchup_pooled(
            /*n_games=*/1,
            model,
            Side::USSR,
            serial_config,
            /*pool_size=*/1,
            /*base_seed=*/5151,
            torch::kCPU
        );
        const auto pooled_parallel = play_ismcts_matchup_pooled(
            /*n_games=*/1,
            model,
            Side::USSR,
            parallel_config,
            /*pool_size=*/1,
            /*base_seed=*/5151,
            torch::kCPU
        );
        const auto pooled_parallel_repeat = play_ismcts_matchup_pooled(
            /*n_games=*/1,
            model,
            Side::USSR,
            parallel_config,
            /*pool_size=*/1,
            /*base_seed=*/5151,
            torch::kCPU
        );

        REQUIRE(same_game_results(pooled_serial, pooled_parallel));
        REQUIRE(same_game_results(pooled_parallel, pooled_parallel_repeat));
    }

    SECTION("ismcts_search is deterministic for the same seed and changes across seeds") {
        auto model = load_stub_model("ismcts_uniform", /*preferred_card_id=*/0, /*preferred_mode=*/-1);
        const auto config = make_test_config(/*n_determinizations=*/4, /*n_simulations=*/3, /*use_rollout_backup=*/true);
        const auto obs = make_hidden_info_observation();

        Pcg64Rng rng_a(2024);
        Pcg64Rng rng_b(2024);
        Pcg64Rng rng_c(2025);

        const auto result_a = ismcts_search(obs, model, config, rng_a);
        const auto result_b = ismcts_search(obs, model, config, rng_b);
        const auto result_c = ismcts_search(obs, model, config, rng_c);

        REQUIRE(same_ismcts_result(result_a, result_b));
        REQUIRE_FALSE(same_ismcts_result(result_a, result_c));
    }
}

TEST_CASE("ismcts_search returns a legal midgame action across action rounds", "[ismcts][regression][action_rounds]") {
    auto model = load_stub_model("ismcts_event_card9", /*preferred_card_id=*/9, static_cast<int>(ActionMode::Event));
    const auto config = make_test_config(/*n_determinizations=*/4, /*n_simulations=*/20);
    const auto gs = make_midgame_action_round_state();
    const auto obs = make_observation(gs, Side::USSR);

    Pcg64Rng search_rng(4242);
    const auto result = ismcts_search(obs, model, config, search_rng);

    REQUIRE(result.best_action.card_id != 0);
    const auto legal = enumerate_actions(
        gs.hands[to_index(Side::USSR)],
        gs.pub,
        Side::USSR,
        gs.ussr_holds_china
    );
    REQUIRE(std::find(legal.begin(), legal.end(), result.best_action) != legal.end());

    Pcg64Rng apply_rng(7);
    const auto [next_pub, over, winner] = apply_action(gs.pub, result.best_action, Side::USSR, apply_rng);
    (void)over;
    (void)winner;
    CHECK(next_pub.defcon != 1);
}

#else

TEST_CASE("ISMCTS regression coverage requires torch runtime", "[ismcts][regression]") {
    SUCCEED("TS_BUILD_TORCH_RUNTIME is disabled");
}

#endif
