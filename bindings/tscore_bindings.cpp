#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "game_loop.hpp"
#include "learned_policy.hpp"
#include "policies.hpp"

namespace py = pybind11;

PYBIND11_MODULE(tscore, m) {
    m.doc() = "Twilight Struggle exact game engine (C++ core)";

    py::enum_<ts::Side>(m, "Side")
        .value("USSR", ts::Side::USSR)
        .value("US", ts::Side::US)
        .value("Neutral", ts::Side::Neutral);

    py::enum_<ts::ActionMode>(m, "ActionMode")
        .value("Influence", ts::ActionMode::Influence)
        .value("Coup", ts::ActionMode::Coup)
        .value("Realign", ts::ActionMode::Realign)
        .value("Space", ts::ActionMode::Space)
        .value("Event", ts::ActionMode::Event);

    py::enum_<ts::PolicyKind>(m, "PolicyKind")
        .value("Random", ts::PolicyKind::Random)
        .value("MinimalHybrid", ts::PolicyKind::MinimalHybrid);

    py::class_<ts::GameResult>(m, "GameResult")
        .def_readonly("winner", &ts::GameResult::winner)
        .def_readonly("final_vp", &ts::GameResult::final_vp)
        .def_readonly("end_turn", &ts::GameResult::end_turn)
        .def_readonly("end_reason", &ts::GameResult::end_reason);

    py::class_<ts::MatchSummary>(m, "MatchSummary")
        .def_readonly("games", &ts::MatchSummary::games)
        .def_readonly("ussr_wins", &ts::MatchSummary::ussr_wins)
        .def_readonly("us_wins", &ts::MatchSummary::us_wins)
        .def_readonly("draws", &ts::MatchSummary::draws)
        .def_readonly("defcon1", &ts::MatchSummary::defcon1)
        .def_readonly("turn_limit", &ts::MatchSummary::turn_limit)
        .def_readonly("scoring_card_held", &ts::MatchSummary::scoring_card_held)
        .def_readonly("vp_threshold", &ts::MatchSummary::vp_threshold)
        .def_readonly("avg_turn", &ts::MatchSummary::avg_turn)
        .def_readonly("avg_final_vp", &ts::MatchSummary::avg_final_vp);

    py::class_<ts::ActionEncoding>(m, "ActionEncoding")
        .def_readonly("card_id", &ts::ActionEncoding::card_id)
        .def_readonly("mode", &ts::ActionEncoding::mode)
        .def_readonly("targets", &ts::ActionEncoding::targets);

    py::class_<ts::StepTrace>(m, "StepTrace")
        .def_readonly("turn", &ts::StepTrace::turn)
        .def_readonly("ar", &ts::StepTrace::ar)
        .def_readonly("side", &ts::StepTrace::side)
        .def_readonly("holds_china", &ts::StepTrace::holds_china)
        .def_readonly("action", &ts::StepTrace::action)
        .def_readonly("vp_before", &ts::StepTrace::vp_before)
        .def_readonly("vp_after", &ts::StepTrace::vp_after)
        .def_readonly("defcon_before", &ts::StepTrace::defcon_before)
        .def_readonly("defcon_after", &ts::StepTrace::defcon_after);

    py::class_<ts::TracedGame>(m, "TracedGame")
        .def_readonly("steps", &ts::TracedGame::steps)
        .def_readonly("result", &ts::TracedGame::result);

    m.def("play_game", &ts::play_game, py::arg("ussr_policy"), py::arg("us_policy"), py::arg("seed") = py::none());
    m.def(
        "play_traced_game",
        [](ts::PolicyKind ussr_policy, ts::PolicyKind us_policy, py::object seed_obj) {
            std::optional<uint32_t> seed;
            if (!seed_obj.is_none()) {
                seed = seed_obj.cast<uint32_t>();
            }
            const ts::PolicyFn ussr_fn = [ussr_policy](const ts::PublicState& pub, const ts::CardSet& hand, bool holds_china, std::mt19937& rng) {
                return ts::choose_action(ussr_policy, pub, hand, holds_china, rng);
            };
            const ts::PolicyFn us_fn = [us_policy](const ts::PublicState& pub, const ts::CardSet& hand, bool holds_china, std::mt19937& rng) {
                return ts::choose_action(us_policy, pub, hand, holds_china, rng);
            };
            return ts::play_game_traced_fn(ussr_fn, us_fn, seed);
        },
        py::arg("ussr_policy"),
        py::arg("us_policy"),
        py::arg("seed") = py::none()
    );
    m.def("play_random_game", &ts::play_random_game, py::arg("seed") = py::none());
    m.def("play_matchup", &ts::play_matchup, py::arg("ussr_policy"), py::arg("us_policy"), py::arg("game_count"), py::arg("seed") = py::none());
    m.def(
        "summarize_results",
        [](const std::vector<ts::GameResult>& results) {
            return ts::summarize_results(results);
        },
        py::arg("results")
    );

#if defined(TS_BUILD_TORCH_RUNTIME)
    m.def(
        "play_learned_matchup",
        [](const std::string& model_path, ts::Side learned_side, ts::PolicyKind opponent_policy, int game_count, py::object seed_obj) {
            std::optional<uint32_t> seed;
            if (!seed_obj.is_none()) {
                seed = seed_obj.cast<uint32_t>();
            }
            ts::TorchScriptPolicy learned(model_path);
            const ts::PolicyFn learned_fn = [&learned](const ts::PublicState& pub, const ts::CardSet& hand, bool holds_china, std::mt19937& rng) {
                return learned.choose_action(pub, hand, holds_china, rng);
            };
            const ts::PolicyFn opponent_fn = [opponent_policy](const ts::PublicState& pub, const ts::CardSet& hand, bool holds_china, std::mt19937& rng) {
                return ts::choose_action(opponent_policy, pub, hand, holds_china, rng);
            };
            return learned_side == ts::Side::USSR
                ? ts::play_matchup_fn(learned_fn, opponent_fn, game_count, seed)
                : ts::play_matchup_fn(opponent_fn, learned_fn, game_count, seed);
        },
        py::arg("model_path"),
        py::arg("learned_side"),
        py::arg("opponent_policy"),
        py::arg("game_count"),
        py::arg("seed") = py::none()
    );
#endif
}
