#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include <algorithm>
#include <cmath>
#include <optional>

#include "game_loop.hpp"
#include "game_state.hpp"
#include "ismcts.hpp"
#include "learned_policy.hpp"
#include "mcts.hpp"
#include "mcts_batched.hpp"
#include "policies.hpp"

namespace py = pybind11;

namespace {

py::list bitset_to_list(const ts::CardSet& cards) {
    py::list out;
    for (int card_id = 1; card_id <= ts::kMaxCardId; ++card_id) {
        if (cards.test(static_cast<size_t>(card_id))) {
            out.append(card_id);
        }
    }
    return out;
}

py::list influence_to_list(const ts::InfluenceBlock& influence) {
    py::list out;
    for (int country_id = 0; country_id <= ts::kMaxCountryId; ++country_id) {
        out.append(influence[static_cast<size_t>(country_id)]);
    }
    return out;
}

py::dict action_to_dict(const ts::ActionEncoding& action) {
    py::dict out;
    out["card_id"] = action.card_id;
    out["mode"] = static_cast<int>(action.mode);
    out["targets"] = action.targets;
    return out;
}

py::dict public_state_to_dict(const ts::PublicState& pub) {
    py::dict out;
    out["turn"] = pub.turn;
    out["ar"] = pub.ar;
    out["phasing"] = static_cast<int>(pub.phasing);
    out["vp"] = pub.vp;
    out["defcon"] = pub.defcon;
    out["milops"] = py::make_tuple(pub.milops[0], pub.milops[1]);
    out["space"] = py::make_tuple(pub.space[0], pub.space[1]);
    out["china_held_by"] = static_cast<int>(pub.china_held_by);
    out["china_playable"] = pub.china_playable;
    out["ussr_influence"] = influence_to_list(pub.influence[ts::to_index(ts::Side::USSR)]);
    out["us_influence"] = influence_to_list(pub.influence[ts::to_index(ts::Side::US)]);
    out["discard"] = bitset_to_list(pub.discard);
    out["removed"] = bitset_to_list(pub.removed);
    out["warsaw_pact_played"] = pub.warsaw_pact_played;
    out["marshall_plan_played"] = pub.marshall_plan_played;
    out["truman_doctrine_played"] = pub.truman_doctrine_played;
    out["john_paul_ii_played"] = pub.john_paul_ii_played;
    out["nato_active"] = pub.nato_active;
    out["de_gaulle_active"] = pub.de_gaulle_active;
    out["willy_brandt_active"] = pub.willy_brandt_active;
    out["us_japan_pact_active"] = pub.us_japan_pact_active;
    out["nuclear_subs_active"] = pub.nuclear_subs_active;
    out["norad_active"] = pub.norad_active;
    out["shuttle_diplomacy_active"] = pub.shuttle_diplomacy_active;
    out["flower_power_active"] = pub.flower_power_active;
    out["flower_power_cancelled"] = pub.flower_power_cancelled;
    out["salt_active"] = pub.salt_active;
    out["opec_cancelled"] = pub.opec_cancelled;
    out["awacs_active"] = pub.awacs_active;
    out["north_sea_oil_extra_ar"] = pub.north_sea_oil_extra_ar;
    out["glasnost_extra_ar"] = pub.glasnost_extra_ar;
    out["formosan_active"] = pub.formosan_active;
    out["cuban_missile_crisis_active"] = pub.cuban_missile_crisis_active;
    out["vietnam_revolts_active"] = pub.vietnam_revolts_active;
    out["bear_trap_active"] = pub.bear_trap_active;
    out["quagmire_active"] = pub.quagmire_active;
    out["iran_hostage_crisis_active"] = pub.iran_hostage_crisis_active;
    out["handicap_ussr"] = pub.handicap_ussr;
    out["handicap_us"] = pub.handicap_us;
    out["ops_modifier"] = py::make_tuple(pub.ops_modifier[0], pub.ops_modifier[1]);
    out["state_hash"] = pub.state_hash;
    return out;
}

// Deserialize a Python dict (produced by cpp_rollout.py serialize_game_state)
// into a C++ GameState for mid-game rollout.
ts::GameState game_state_from_dict(const py::dict& d) {
    ts::GameState gs;

    // --- PublicState ---
    ts::PublicState& pub = gs.pub;
    pub.turn    = d["turn"].cast<int>();
    pub.ar      = d["ar"].cast<int>();
    pub.phasing = static_cast<ts::Side>(d["phasing"].cast<int>());
    pub.vp      = d["vp"].cast<int>();
    pub.defcon  = d["defcon"].cast<int>();

    auto milops = d["milops"].cast<std::vector<int>>();
    pub.milops[0] = milops[0];
    pub.milops[1] = milops[1];

    auto space = d["space"].cast<std::vector<int>>();
    pub.space[0] = space[0];
    pub.space[1] = space[1];

    pub.china_held_by  = static_cast<ts::Side>(d["china_held_by"].cast<int>());
    pub.china_playable = d["china_playable"].cast<bool>();

    // Influence: flat list[int] length 86 (indices 0..85)
    auto ussr_inf = d["ussr_influence"].cast<std::vector<int>>();
    auto us_inf   = d["us_influence"].cast<std::vector<int>>();
    for (int i = 0; i < static_cast<int>(ussr_inf.size()) && i <= ts::kMaxCountryId; ++i) {
        pub.influence[ts::to_index(ts::Side::USSR)][i] = static_cast<int16_t>(ussr_inf[i]);
        pub.influence[ts::to_index(ts::Side::US)][i]   = static_cast<int16_t>(us_inf[i]);
    }

    // Discard / removed as list[int] of card ids
    for (int cid : d["discard"].cast<std::vector<int>>()) {
        pub.discard.set(static_cast<size_t>(cid));
    }
    for (int cid : d["removed"].cast<std::vector<int>>()) {
        pub.removed.set(static_cast<size_t>(cid));
    }

    // Bool effect flags
    pub.warsaw_pact_played          = d["warsaw_pact_played"].cast<bool>();
    pub.marshall_plan_played        = d["marshall_plan_played"].cast<bool>();
    pub.truman_doctrine_played      = d["truman_doctrine_played"].cast<bool>();
    pub.john_paul_ii_played         = d["john_paul_ii_played"].cast<bool>();
    pub.nato_active                 = d["nato_active"].cast<bool>();
    pub.de_gaulle_active            = d["de_gaulle_active"].cast<bool>();
    pub.willy_brandt_active         = d["willy_brandt_active"].cast<bool>();
    pub.us_japan_pact_active        = d["us_japan_pact_active"].cast<bool>();
    pub.nuclear_subs_active         = d["nuclear_subs_active"].cast<bool>();
    pub.norad_active                = d["norad_active"].cast<bool>();
    pub.shuttle_diplomacy_active    = d["shuttle_diplomacy_active"].cast<bool>();
    pub.flower_power_active         = d["flower_power_active"].cast<bool>();
    pub.flower_power_cancelled      = d["flower_power_cancelled"].cast<bool>();
    pub.salt_active                 = d["salt_active"].cast<bool>();
    pub.opec_cancelled              = d["opec_cancelled"].cast<bool>();
    pub.awacs_active                = d["awacs_active"].cast<bool>();
    pub.north_sea_oil_extra_ar      = d["north_sea_oil_extra_ar"].cast<bool>();
    pub.glasnost_extra_ar           = d["glasnost_extra_ar"].cast<bool>();
    pub.formosan_active             = d["formosan_active"].cast<bool>();
    pub.cuban_missile_crisis_active = d["cuban_missile_crisis_active"].cast<bool>();
    pub.vietnam_revolts_active      = d["vietnam_revolts_active"].cast<bool>();
    pub.bear_trap_active            = d["bear_trap_active"].cast<bool>();
    pub.quagmire_active             = d["quagmire_active"].cast<bool>();
    pub.iran_hostage_crisis_active  = d["iran_hostage_crisis_active"].cast<bool>();
    pub.handicap_ussr               = d["handicap_ussr"].cast<int>();
    pub.handicap_us                 = d["handicap_us"].cast<int>();

    auto ops_mod = d["ops_modifier"].cast<std::vector<int>>();
    pub.ops_modifier[0] = ops_mod[0];
    pub.ops_modifier[1] = ops_mod[1];

    // --- Hands ---
    for (int cid : d["ussr_hand"].cast<std::vector<int>>()) {
        gs.hands[ts::to_index(ts::Side::USSR)].set(static_cast<size_t>(cid));
    }
    for (int cid : d["us_hand"].cast<std::vector<int>>()) {
        gs.hands[ts::to_index(ts::Side::US)].set(static_cast<size_t>(cid));
    }

    // --- Deck ---
    gs.deck = d["deck"].cast<std::vector<ts::CardId>>();

    // --- China Card ownership ---
    gs.ussr_holds_china = d["ussr_holds_china"].cast<bool>();
    gs.us_holds_china   = d["us_holds_china"].cast<bool>();

    // Game phase: assume Headline at start of turn
    gs.phase        = ts::GamePhase::Headline;
    gs.current_side = pub.phasing;
    gs.ar_index     = 1;
    gs.ars_taken    = {0, 0};

    return gs;
}

// Run a heuristic (MinimalHybrid vs MinimalHybrid) game from a serialized
// mid-game state dict.  Returns final_vp / 20.0 clamped to [-1, 1] from
// USSR perspective.  Positive = USSR ahead.
double play_from_public_state(const py::dict& state_dict, py::object seed_obj) {
    ts::GameState gs = game_state_from_dict(state_dict);

    std::optional<uint32_t> seed;
    if (!seed_obj.is_none()) {
        seed = seed_obj.cast<uint32_t>();
    }

    const ts::PolicyFn ussr_fn = [](const ts::PublicState& pub, const ts::CardSet& hand, bool holds_china, ts::Pcg64Rng& rng) {
        return ts::choose_action(ts::PolicyKind::MinimalHybrid, pub, hand, holds_china, rng);
    };
    const ts::PolicyFn us_fn = [](const ts::PublicState& pub, const ts::CardSet& hand, bool holds_china, ts::Pcg64Rng& rng) {
        return ts::choose_action(ts::PolicyKind::MinimalHybrid, pub, hand, holds_china, rng);
    };

    const ts::GameResult result = ts::play_game_from_mid_state_fn(std::move(gs), ussr_fn, us_fn, seed);
    const double raw = static_cast<double>(result.final_vp) / 20.0;
    return std::clamp(raw, -1.0, 1.0);
}

#if defined(TS_BUILD_TORCH_RUNTIME)
thread_local std::string cached_model_path;
thread_local std::optional<torch::jit::script::Module> cached_model;

torch::jit::script::Module& get_or_load_model(const std::string& model_path) {
    if (!cached_model.has_value() || cached_model_path != model_path) {
        cached_model = torch::jit::load(model_path);
        cached_model->eval();
        cached_model_path = model_path;
    }
    return *cached_model;
}

py::dict run_mcts_search_from_state(
    const py::dict& state_dict,
    const std::string& model_path,
    int n_sim,
    float c_puct,
    float calib_a,
    float calib_b,
    py::object seed_obj
) {
    if (n_sim <= 0) {
        throw py::value_error("n_sim must be positive");
    }
    if (c_puct <= 0.0f) {
        throw py::value_error("c_puct must be positive");
    }

    ts::GameState gs = game_state_from_dict(state_dict);
    auto& model = get_or_load_model(model_path);

    ts::MctsConfig config;
    config.n_simulations = n_sim;
    config.c_puct = c_puct;
    config.calib_a = calib_a;
    config.calib_b = calib_b;

    ts::Pcg64Rng rng = seed_obj.is_none()
        ? ts::Pcg64Rng()
        : ts::Pcg64Rng(seed_obj.cast<uint64_t>());

    const ts::SearchResult result = ts::mcts_search(gs, model, config, rng);

    py::list edges_out;
    for (const auto& edge : result.root_edges) {
        py::dict edge_out;
        edge_out["card_id"] = edge.action.card_id;
        edge_out["mode"] = static_cast<int>(edge.action.mode);
        edge_out["targets"] = edge.action.targets;
        edge_out["visits"] = edge.visit_count;
        edge_out["mean_value"] = edge.mean_value();
        edge_out["prior"] = edge.prior;
        edges_out.append(std::move(edge_out));
    }

    py::dict out;
    py::object best_action = py::none();
    if (!result.root_edges.empty() && result.best_action.card_id != 0) {
        best_action = action_to_dict(result.best_action);
    }
    out["best_action"] = std::move(best_action);
    out["root_value"] = result.root_value;
    out["total_simulations"] = result.total_simulations;
    out["edges"] = std::move(edges_out);
    return out;
}
#endif

}  // namespace

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
        .def_property_readonly("pub_snapshot", [](const ts::StepTrace& step) {
            return public_state_to_dict(step.pub_snapshot);
        })
        .def_property_readonly("hand_snapshot", [](const ts::StepTrace& step) {
            return bitset_to_list(step.hand_snapshot);
        })
        .def_readonly("action", &ts::StepTrace::action)
        .def_readonly("vp_before", &ts::StepTrace::vp_before)
        .def_readonly("vp_after", &ts::StepTrace::vp_after)
        .def_readonly("defcon_before", &ts::StepTrace::defcon_before)
        .def_readonly("defcon_after", &ts::StepTrace::defcon_after);

    py::class_<ts::TracedGame>(m, "TracedGame")
        .def_readonly("steps", &ts::TracedGame::steps)
        .def_readonly("result", &ts::TracedGame::result);

    m.def(
        "play_game",
        [](ts::PolicyKind ussr_policy, ts::PolicyKind us_policy, py::object seed_obj) {
            std::optional<uint32_t> seed;
            if (!seed_obj.is_none()) {
                seed = seed_obj.cast<uint32_t>();
            }
            return ts::play_game(ussr_policy, us_policy, seed);
        },
        py::arg("ussr_policy"),
        py::arg("us_policy"),
        py::arg("seed") = py::none()
    );
    m.def(
        "play_from_public_state",
        [](const py::dict& state_dict, py::object seed_obj) {
            return play_from_public_state(state_dict, seed_obj);
        },
        py::arg("state_dict"),
        py::arg("seed") = py::none(),
        "Run a MinimalHybrid vs MinimalHybrid heuristic game from a mid-game state dict.\n"
        "Returns final_vp / 20.0 clamped to [-1, 1] (USSR perspective)."
    );
    m.def(
        "play_traced_game",
        [](ts::PolicyKind ussr_policy, ts::PolicyKind us_policy, py::object seed_obj) {
            std::optional<uint32_t> seed;
            if (!seed_obj.is_none()) {
                seed = seed_obj.cast<uint32_t>();
            }
            const ts::PolicyFn ussr_fn = [ussr_policy](const ts::PublicState& pub, const ts::CardSet& hand, bool holds_china, ts::Pcg64Rng& rng) {
                return ts::choose_action(ussr_policy, pub, hand, holds_china, rng);
            };
            const ts::PolicyFn us_fn = [us_policy](const ts::PublicState& pub, const ts::CardSet& hand, bool holds_china, ts::Pcg64Rng& rng) {
                return ts::choose_action(us_policy, pub, hand, holds_china, rng);
            };
            return ts::play_game_traced_fn(ussr_fn, us_fn, seed);
        },
        py::arg("ussr_policy"),
        py::arg("us_policy"),
        py::arg("seed") = py::none()
    );
    m.def(
        "play_traced_game_from_seed_words",
        [](ts::PolicyKind ussr_policy, ts::PolicyKind us_policy, const std::array<uint64_t, 4>& words, py::object seed_obj) {
            std::optional<uint32_t> seed;
            if (!seed_obj.is_none()) {
                seed = seed_obj.cast<uint32_t>();
            }
            const ts::PolicyFn ussr_fn = [ussr_policy](const ts::PublicState& pub, const ts::CardSet& hand, bool holds_china, ts::Pcg64Rng& rng) {
                return ts::choose_action(ussr_policy, pub, hand, holds_china, rng);
            };
            const ts::PolicyFn us_fn = [us_policy](const ts::PublicState& pub, const ts::CardSet& hand, bool holds_china, ts::Pcg64Rng& rng) {
                return ts::choose_action(us_policy, pub, hand, holds_china, rng);
            };
            return ts::play_game_traced_from_seed_words_fn(words, ussr_fn, us_fn, seed);
        },
        py::arg("ussr_policy"),
        py::arg("us_policy"),
        py::arg("words"),
        py::arg("seed") = py::none()
    );
    m.def(
        "play_random_game",
        [](py::object seed_obj) {
            std::optional<uint32_t> seed;
            if (!seed_obj.is_none()) {
                seed = seed_obj.cast<uint32_t>();
            }
            return ts::play_random_game(seed);
        },
        py::arg("seed") = py::none()
    );
    m.def(
        "play_matchup",
        [](ts::PolicyKind ussr_policy, ts::PolicyKind us_policy, int game_count, py::object seed_obj) {
            std::optional<uint32_t> seed;
            if (!seed_obj.is_none()) {
                seed = seed_obj.cast<uint32_t>();
            }
            return ts::play_matchup(ussr_policy, us_policy, game_count, seed);
        },
        py::arg("ussr_policy"),
        py::arg("us_policy"),
        py::arg("game_count"),
        py::arg("seed") = py::none()
    );
    m.def(
        "summarize_results",
        [](const std::vector<ts::GameResult>& results) {
            return ts::summarize_results(results);
        },
        py::arg("results")
    );

    // play_callback_matchup: run games with a Python callable as one side's policy.
    // The callback receives (state_dict, hand_list, holds_china, side_int) and
    // returns an action dict {"card_id": int, "mode": int, "targets": list[int]}
    // or None to skip.
    m.def(
        "play_callback_matchup",
        [](py::function callback, ts::Side learned_side, ts::PolicyKind opponent_policy, int game_count, py::object seed_obj) {
            std::optional<uint32_t> seed;
            if (!seed_obj.is_none()) {
                seed = seed_obj.cast<uint32_t>();
            }
            const ts::PolicyFn callback_fn = [&callback](const ts::PublicState& pub, const ts::CardSet& hand, bool holds_china, ts::Pcg64Rng& /*rng*/) -> std::optional<ts::ActionEncoding> {
                py::gil_scoped_acquire gil;
                py::dict state = public_state_to_dict(pub);
                py::list hand_list = bitset_to_list(hand);
                py::object result = callback(state, hand_list, holds_china, static_cast<int>(pub.phasing));
                if (result.is_none()) {
                    return std::nullopt;
                }
                py::dict action_dict = result.cast<py::dict>();
                ts::ActionEncoding action;
                action.card_id = static_cast<ts::CardId>(action_dict["card_id"].cast<int>());
                action.mode = static_cast<ts::ActionMode>(action_dict["mode"].cast<int>());
                for (auto t : action_dict["targets"].cast<std::vector<int>>()) {
                    action.targets.push_back(static_cast<ts::CountryId>(t));
                }
                return action;
            };
            const ts::PolicyFn opponent_fn = [opponent_policy](const ts::PublicState& pub, const ts::CardSet& hand, bool holds_china, ts::Pcg64Rng& rng) {
                return ts::choose_action(opponent_policy, pub, hand, holds_china, rng);
            };
            // Use atomic setup for bit-identity with batched path:
            // places opening influence in one shot (2 RNG calls) instead of
            // per-point policy callbacks (15+ RNG calls).
            ts::GameLoopConfig config;
            config.use_atomic_setup = true;
            // Release GIL for the game loop; callback re-acquires it as needed.
            py::gil_scoped_release release;
            return learned_side == ts::Side::USSR
                ? ts::play_matchup_fn(callback_fn, opponent_fn, game_count, seed, config)
                : ts::play_matchup_fn(opponent_fn, callback_fn, game_count, seed, config);
        },
        py::arg("callback"),
        py::arg("learned_side"),
        py::arg("opponent_policy"),
        py::arg("game_count"),
        py::arg("seed") = py::none(),
        "Run games where one side uses a Python callback policy.\n"
        "Callback signature: (state_dict, hand_list, holds_china, side_int) -> action_dict or None."
    );

#if defined(TS_BUILD_TORCH_RUNTIME)
    m.def(
        "play_learned_matchup",
        [](const std::string& model_path, ts::Side learned_side, ts::PolicyKind opponent_policy, int game_count, py::object seed_obj) {
            std::optional<uint32_t> seed;
            if (!seed_obj.is_none()) {
                seed = seed_obj.cast<uint32_t>();
            }
            ts::GameLoopConfig config;
            config.use_atomic_setup = true;  // bid+2 baked into kHumanUSOpeningsBid2
            ts::TorchScriptPolicy learned(model_path);
            const ts::PolicyFn learned_fn = [&learned](const ts::PublicState& pub, const ts::CardSet& hand, bool holds_china, ts::Pcg64Rng& rng) {
                return learned.choose_action(pub, hand, holds_china, rng);
            };
            const ts::PolicyFn opponent_fn = [opponent_policy](const ts::PublicState& pub, const ts::CardSet& hand, bool holds_china, ts::Pcg64Rng& rng) {
                return ts::choose_action(opponent_policy, pub, hand, holds_china, rng);
            };
            return learned_side == ts::Side::USSR
                ? ts::play_matchup_fn(learned_fn, opponent_fn, game_count, seed, config)
                : ts::play_matchup_fn(opponent_fn, learned_fn, game_count, seed, config);
        },
        py::arg("model_path"),
        py::arg("learned_side"),
        py::arg("opponent_policy"),
        py::arg("game_count"),
        py::arg("seed") = py::none()
    );
    m.def(
        "mcts_search_from_state",
        &run_mcts_search_from_state,
        py::arg("state_dict"),
        py::arg("model_path"),
        py::arg("n_sim") = 200,
        py::arg("c_puct") = 1.5f,
        py::arg("calib_a") = 1.0f,
        py::arg("calib_b") = 0.0f,
        py::arg("seed") = py::none(),
        "Run native PUCT MCTS from a serialized game state and return root search statistics."
    );
    m.def(
        "search_from_public_state",
        &run_mcts_search_from_state,
        py::arg("state_dict"),
        py::arg("model_path"),
        py::arg("n_sim") = 200,
        py::arg("c_puct") = 1.5f,
        py::arg("calib_a") = 1.0f,
        py::arg("calib_b") = 0.0f,
        py::arg("seed") = py::none(),
        "Alias for mcts_search_from_state that runs native PUCT MCTS from a serialized game state."
    );
    m.def(
        "benchmark_batched",
        [](const std::string& model_path, ts::Side learned_side, int n_games, int pool_size, py::object seed_obj, const std::string& device_str, bool greedy_opponent, float temperature, bool nash_temperatures) {
            std::optional<uint32_t> seed;
            if (!seed_obj.is_none()) {
                seed = seed_obj.cast<uint32_t>();
            }
            torch::Device device(device_str);
            auto model = torch::jit::load(model_path, device);
            model.eval();
            return ts::benchmark_games_batched(
                n_games, model, learned_side, pool_size,
                seed.value_or(std::random_device{}()), device, greedy_opponent, temperature, nash_temperatures);
        },
        py::arg("model_path"),
        py::arg("learned_side"),
        py::arg("n_games"),
        py::arg("pool_size") = 32,
        py::arg("seed") = py::none(),
        py::arg("device") = "cpu",
        py::arg("greedy_opponent") = false,
        py::arg("temperature") = 0.0f,
        py::arg("nash_temperatures") = true,
        "Run batched greedy benchmark: learned side uses argmax (T=0) or softmax\n"
        "sampling (T>0). Opponent uses heuristic (default) or greedy NN.\n"
        "If nash_temperatures=true (default), the heuristic opponent samples\n"
        "per-game temperatures from the Nash mixed strategy (matching training data).\n"
        "Returns list[GameResult]."
    );
    m.def(
        "benchmark_ismcts",
        [](const std::string& model_path, ts::Side learned_side, int n_games,
           int n_determinizations, int n_simulations, py::object seed_obj, int pool_size,
           int max_pending_per_det, const std::string& device_str) {
            std::optional<uint32_t> seed;
            if (!seed_obj.is_none()) {
                seed = seed_obj.cast<uint32_t>();
            }
            torch::Device device(device_str);
            auto model = torch::jit::load(model_path, device);
            model.eval();
            ts::IsmctsConfig config;
            config.n_determinizations = n_determinizations;
            config.max_pending_per_det = max_pending_per_det;
            config.mcts_config.n_simulations = n_simulations;
            return ts::play_ismcts_matchup_pooled(
                n_games,
                model,
                learned_side,
                config,
                pool_size,
                seed.value_or(std::random_device{}()),
                device
            );
        },
        py::arg("model_path"),
        py::arg("learned_side"),
        py::arg("n_games"),
        py::arg("n_determinizations") = 8,
        py::arg("n_simulations") = 50,
        py::arg("seed") = py::none(),
        py::arg("pool_size") = 4,
        py::arg("max_pending_per_det") = 8,
        py::arg("device") = "cpu",
        "Run ISMCTS benchmark: learned side uses information-set MCTS,\n"
        "opponent uses heuristic. Returns list[GameResult].\n"
        "n_determinizations: parallel determinization count (default 8).\n"
        "n_simulations: MCTS simulations per determinization (default 50).\n"
        "pool_size: concurrent games batched together (default 4).\n"
        "max_pending_per_det: concurrent leaves per determinization via virtual loss (default 8).\n"
        "device: 'cpu' or 'cuda' for GPU inference."
    );
    m.def(
        "benchmark_mcts_vs_greedy",
        [](const std::string& model_path, ts::Side learned_side, int n_games,
           int n_simulations, int pool_size, uint32_t seed, const std::string& device_str) {
            torch::Device device(device_str);
            auto model = torch::jit::load(model_path, device);
            model.eval();
            return ts::benchmark_mcts_vs_greedy(
                n_games, model, learned_side, n_simulations, pool_size, seed, device);
        },
        py::arg("model_path"),
        py::arg("learned_side"),
        py::arg("n_games"),
        py::arg("n_simulations") = 400,
        py::arg("pool_size") = 32,
        py::arg("seed") = 42000,
        py::arg("device") = "cpu",
        "Run MCTS (learned side) vs greedy NN (opponent, same model) benchmark.\n"
        "Returns list[GameResult]."
    );
    m.def(
        "benchmark_mcts",
        [](const std::string& model_path, ts::Side learned_side, int n_games,
           int n_simulations, int pool_size, uint32_t seed, const std::string& device_str,
           bool greedy_nn_opponent, bool nash_temperatures) {
            torch::Device device(device_str);
            auto model = torch::jit::load(model_path, device);
            model.eval();
            return ts::benchmark_mcts(
                n_games, model, learned_side, n_simulations, pool_size, seed, device,
                greedy_nn_opponent, nash_temperatures);
        },
        py::arg("model_path"),
        py::arg("learned_side"),
        py::arg("n_games"),
        py::arg("n_simulations") = 400,
        py::arg("pool_size") = 32,
        py::arg("seed") = 42000,
        py::arg("device") = "cpu",
        py::arg("greedy_nn_opponent") = false,
        py::arg("nash_temperatures") = true,
        "Run MCTS benchmark. Opponent is heuristic (default) or greedy NN.\n"
        "If nash_temperatures=true (default), the heuristic opponent samples\n"
        "per-game temperatures from the Nash mixed strategy.\n"
        "Returns list[GameResult]."
    );
#endif
}
