#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "game_loop.hpp"
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

    m.def("play_game", &ts::play_game, py::arg("ussr_policy"), py::arg("us_policy"), py::arg("seed") = py::none());
    m.def("play_random_game", &ts::play_random_game, py::arg("seed") = py::none());
    m.def("play_matchup", &ts::play_matchup, py::arg("ussr_policy"), py::arg("us_policy"), py::arg("game_count"), py::arg("seed") = py::none());
}
