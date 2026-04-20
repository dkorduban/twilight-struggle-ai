#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>

#include <algorithm>
#include <cmath>
#include <cstring>
#include <optional>
#include <random>

#include "adjacency.hpp"
#include "game_data.hpp"
#include "game_loop.hpp"
#include "game_state.hpp"
#include "ismcts.hpp"
#include "legal_actions.hpp"
#include "learned_policy.hpp"
#include "mcts.hpp"
#include "mcts_batched.hpp"
#include "policies.hpp"

namespace py = pybind11;

namespace {

enum class BoundStepResult {
    Complete = 0,
    SubframePending = 1,
};

BoundStepResult bind_step_result(const ts::StepResult& result) {
    return result.pushed_subframe ? BoundStepResult::SubframePending : BoundStepResult::Complete;
}

py::list bitset_to_list(const ts::CardSet& cards) {
    py::list out;
    for (int card_id = 1; card_id <= ts::kMaxCardId; ++card_id) {
        if (cards.test(static_cast<size_t>(card_id))) {
            out.append(card_id);
        }
    }
    return out;
}

py::list country_bits_to_list(const std::bitset<ts::kCountrySlots>& countries, int limit) {
    py::list out;
    int emitted = 0;
    for (int country_id = 0; country_id <= ts::kMaxCountryId && emitted < limit; ++country_id) {
        if (countries.test(static_cast<size_t>(country_id))) {
            out.append(country_id);
            ++emitted;
        }
    }
    return out;
}

py::list card_bits_to_list(const ts::CardSet& cards, int limit) {
    py::list out;
    int emitted = 0;
    for (int card_id = 1; card_id <= ts::kMaxCardId && emitted < limit; ++card_id) {
        if (cards.test(static_cast<size_t>(card_id))) {
            out.append(card_id);
            ++emitted;
        }
    }
    return out;
}

py::list decision_frame_cards_to_list(const ts::DecisionFrame& frame) {
    return card_bits_to_list(frame.eligible_cards, static_cast<int>(frame.eligible_n));
}

py::list decision_frame_countries_to_list(const ts::DecisionFrame& frame) {
    return country_bits_to_list(frame.eligible_countries, static_cast<int>(frame.eligible_n));
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

ts::FrameAction make_frame_action(int option_index, int card_id, int country_id) {
    return ts::FrameAction{
        .option_index = option_index,
        .card_id = static_cast<ts::CardId>(card_id),
        .country_id = static_cast<ts::CountryId>(country_id),
    };
}

std::vector<ts::ActionEncoding> current_top_level_actions(const ts::GameState& gs) {
    const auto side = gs.pub.phasing;
    if (!ts::is_player_side(side)) {
        return {};
    }
    const auto holds_china = side == ts::Side::USSR ? gs.ussr_holds_china : gs.us_holds_china;
    return ts::enumerate_actions(gs.hands[ts::to_index(side)], gs.pub, side, holds_china);
}

// Fill in the hidden-state fields that game_state_from_dict requires beyond
// what public_state_to_dict already emits. Used by state-trace bindings so
// ismcts_search_from_state can be called on traced decision points.
void augment_state_dict_with_hidden(
    py::dict& out,
    ts::Side side,
    const ts::CardSet& hand_snapshot,
    const ts::CardSet& opp_hand_snapshot,
    const ts::InlineDeck& deck_snapshot,
    bool ussr_holds_china,
    bool us_holds_china
) {
    const ts::CardSet& ussr_hand = side == ts::Side::USSR ? hand_snapshot : opp_hand_snapshot;
    const ts::CardSet& us_hand   = side == ts::Side::US   ? hand_snapshot : opp_hand_snapshot;
    out["ussr_hand"] = bitset_to_list(ussr_hand);
    out["us_hand"]   = bitset_to_list(us_hand);
    out["deck"] = py::cast(deck_snapshot.to_vector());
    out["ussr_holds_china"] = ussr_holds_china;
    out["us_holds_china"]   = us_holds_china;
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
    out["glasnost_free_ops"] = pub.glasnost_free_ops;
    out["glasnost_extra_ar"] = pub.glasnost_free_ops > 0;
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

py::object get_field(const py::handle& obj, const char* name) {
    if (py::isinstance<py::dict>(obj)) {
        auto d = py::reinterpret_borrow<py::dict>(obj);
        py::str key(name);
        if (d.contains(key)) {
            return d[key];
        }
        return py::none();
    }
    if (py::hasattr(obj, name)) {
        return obj.attr(name);
    }
    return py::none();
}

template <typename T>
T get_field_or(const py::handle& obj, const char* name, T default_value) {
    py::object value = get_field(obj, name);
    if (value.is_none()) {
        return default_value;
    }
    return value.cast<T>();
}

ts::Side side_from_python(const py::handle& obj) {
    return static_cast<ts::Side>(py::cast<int>(obj));
}

ts::ActionMode action_mode_from_python(const py::handle& obj) {
    return static_cast<ts::ActionMode>(py::cast<int>(obj));
}

std::optional<ts::Side> optional_side_from_python(const py::object& obj) {
    if (obj.is_none()) {
        return std::nullopt;
    }
    return side_from_python(obj);
}

std::optional<ts::Region> optional_region_from_python(const py::object& obj) {
    if (obj.is_none()) {
        return std::nullopt;
    }
    return static_cast<ts::Region>(obj.cast<int>());
}

template <size_t N>
void fill_int_array(std::array<int, N>& out, const py::object& value) {
    if (value.is_none()) {
        return;
    }
    const auto values = value.cast<std::vector<int>>();
    for (size_t i = 0; i < std::min(N, values.size()); ++i) {
        out[i] = values[i];
    }
}

void fill_card_set(ts::CardSet& out, const py::object& value) {
    if (value.is_none()) {
        return;
    }
    for (const auto item : value.cast<py::iterable>()) {
        out.set(static_cast<size_t>(item.cast<int>()));
    }
}

ts::CardSet card_set_from_iterable(const py::iterable& cards) {
    ts::CardSet out;
    fill_card_set(out, cards);
    return out;
}

ts::PublicState public_state_from_python(const py::handle& obj) {
    ts::PublicState pub;

    pub.turn = get_field_or<int>(obj, "turn", 0);
    pub.ar = get_field_or<int>(obj, "ar", 0);
    pub.phasing = side_from_python(get_field(obj, "phasing").is_none() ? py::int_(0) : get_field(obj, "phasing"));
    pub.vp = get_field_or<int>(obj, "vp", 0);
    pub.defcon = get_field_or<int>(obj, "defcon", 5);

    fill_int_array(pub.milops, get_field(obj, "milops"));
    fill_int_array(pub.space, get_field(obj, "space"));
    fill_int_array(pub.space_attempts, get_field(obj, "space_attempts"));
    fill_int_array(pub.ops_modifier, get_field(obj, "ops_modifier"));

    pub.china_held_by = side_from_python(
        get_field(obj, "china_held_by").is_none() ? py::int_(0) : get_field(obj, "china_held_by")
    );
    pub.china_playable = get_field_or<bool>(obj, "china_playable", true);

    py::object influence = get_field(obj, "influence");
    if (!influence.is_none() && py::hasattr(influence, "items")) {
        for (const auto item_obj : influence.attr("items")()) {
            py::tuple item = item_obj.cast<py::tuple>();
            py::tuple key = item[0].cast<py::tuple>();
            const auto side = side_from_python(key[0]);
            const auto country_id = key[1].cast<int>();
            pub.influence[ts::to_index(side)][country_id] = static_cast<int16_t>(item[1].cast<int>());
        }
    } else {
        py::object ussr_influence = get_field(obj, "ussr_influence");
        if (!ussr_influence.is_none()) {
            const auto values = ussr_influence.cast<std::vector<int>>();
            for (size_t i = 0; i < values.size() && i <= static_cast<size_t>(ts::kMaxCountryId); ++i) {
                pub.influence[ts::to_index(ts::Side::USSR)][i] = static_cast<int16_t>(values[i]);
            }
        }
        py::object us_influence = get_field(obj, "us_influence");
        if (!us_influence.is_none()) {
            const auto values = us_influence.cast<std::vector<int>>();
            for (size_t i = 0; i < values.size() && i <= static_cast<size_t>(ts::kMaxCountryId); ++i) {
                pub.influence[ts::to_index(ts::Side::US)][i] = static_cast<int16_t>(values[i]);
            }
        }
    }

    fill_card_set(pub.discard, get_field(obj, "discard"));
    fill_card_set(pub.removed, get_field(obj, "removed"));

    pub.space_level4_first = optional_side_from_python(get_field(obj, "space_level4_first"));
    pub.space_level6_first = optional_side_from_python(get_field(obj, "space_level6_first"));
    pub.warsaw_pact_played = get_field_or<bool>(obj, "warsaw_pact_played", false);
    pub.marshall_plan_played = get_field_or<bool>(obj, "marshall_plan_played", false);
    pub.truman_doctrine_played = get_field_or<bool>(obj, "truman_doctrine_played", false);
    pub.john_paul_ii_played = get_field_or<bool>(obj, "john_paul_ii_played", false);
    pub.nato_active = get_field_or<bool>(obj, "nato_active", false);
    pub.de_gaulle_active = get_field_or<bool>(obj, "de_gaulle_active", false);
    pub.willy_brandt_active = get_field_or<bool>(obj, "willy_brandt_active", false);
    pub.us_japan_pact_active = get_field_or<bool>(obj, "us_japan_pact_active", false);
    pub.nuclear_subs_active = get_field_or<bool>(obj, "nuclear_subs_active", false);
    pub.norad_active = get_field_or<bool>(obj, "norad_active", false);
    pub.shuttle_diplomacy_active = get_field_or<bool>(obj, "shuttle_diplomacy_active", false);
    pub.flower_power_active = get_field_or<bool>(obj, "flower_power_active", false);
    pub.flower_power_cancelled = get_field_or<bool>(obj, "flower_power_cancelled", false);
    pub.salt_active = get_field_or<bool>(obj, "salt_active", false);
    pub.opec_cancelled = get_field_or<bool>(obj, "opec_cancelled", false);
    pub.awacs_active = get_field_or<bool>(obj, "awacs_active", false);
    pub.north_sea_oil_extra_ar = get_field_or<bool>(obj, "north_sea_oil_extra_ar", false);
    if (auto glasnost_free_ops = get_field(obj, "glasnost_free_ops"); !glasnost_free_ops.is_none()) {
        pub.glasnost_free_ops = glasnost_free_ops.cast<int>();
    } else if (get_field_or<bool>(obj, "glasnost_extra_ar", false)) {
        pub.glasnost_free_ops = 4;
    }
    pub.formosan_active = get_field_or<bool>(obj, "formosan_active", false);
    pub.cuban_missile_crisis_active = get_field_or<bool>(obj, "cuban_missile_crisis_active", false);
    pub.vietnam_revolts_active = get_field_or<bool>(obj, "vietnam_revolts_active", false);
    pub.bear_trap_active = get_field_or<bool>(obj, "bear_trap_active", false);
    pub.quagmire_active = get_field_or<bool>(obj, "quagmire_active", false);
    pub.iran_hostage_crisis_active = get_field_or<bool>(obj, "iran_hostage_crisis_active", false);
    pub.handicap_ussr = get_field_or<int>(obj, "handicap_ussr", 0);
    pub.handicap_us = get_field_or<int>(obj, "handicap_us", 0);
    pub.chernobyl_blocked_region = optional_region_from_python(get_field(obj, "chernobyl_blocked_region"));
    pub.latam_coup_bonus = optional_side_from_python(get_field(obj, "latam_coup_bonus"));
    pub.state_hash = get_field_or<uint32_t>(obj, "state_hash", 0);

    return pub;
}

py::dict adjacency_to_dict() {
    py::dict out;
    const auto& graph = ts::adjacency();
    for (int country_id = 0; country_id <= ts::kMaxCountryId; ++country_id) {
        if (!ts::has_country_spec(country_id)) {
            continue;
        }
        py::set neighbors;
        for (const auto neighbor : graph[static_cast<size_t>(country_id)]) {
            neighbors.add(neighbor);
        }
        out[py::int_(country_id)] = py::frozenset(neighbors);
    }
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
    if (d.contains("glasnost_free_ops")) {
        pub.glasnost_free_ops = d["glasnost_free_ops"].cast<int>();
    } else if (d.contains("glasnost_extra_ar")) {
        pub.glasnost_free_ops = d["glasnost_extra_ar"].cast<bool>() ? 4 : 0;
    }
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

template <typename T>
py::array_t<T> tensor_to_numpy(const torch::Tensor& tensor) {
    auto contiguous = tensor.detach().cpu().contiguous();
    std::vector<py::ssize_t> shape;
    shape.reserve(static_cast<size_t>(contiguous.dim()));
    for (const auto size : contiguous.sizes()) {
        shape.push_back(static_cast<py::ssize_t>(size));
    }
    py::array_t<T> array(shape);
    std::memcpy(
        array.mutable_data(),
        contiguous.data_ptr<T>(),
        static_cast<size_t>(contiguous.numel()) * sizeof(T)
    );
    return array;
}

py::dict rollout_step_to_dict(const ts::RolloutStep& step) {
    py::dict out;
    out["influence"] = tensor_to_numpy<float>(step.influence);
    out["cards"] = tensor_to_numpy<float>(step.cards);
    out["scalars"] = tensor_to_numpy<float>(step.scalars);
    out["card_mask"] = tensor_to_numpy<bool>(step.card_mask);
    out["mode_mask"] = tensor_to_numpy<bool>(step.mode_mask);
    out["country_mask"] = tensor_to_numpy<bool>(step.country_mask);
    out["card_idx"] = step.card_idx;
    out["mode_idx"] = step.mode_idx;
    out["country_targets"] = step.country_targets;
    out["log_prob"] = step.log_prob;
    out["value"] = step.value;
    out["side_int"] = step.side_int;
    out["game_index"] = step.game_index;
    // Raw game state fields for future re-encoding (added 2026-04-07).
    {
        auto t = torch::tensor(
            std::vector<int16_t>(step.raw_ussr_influence.begin(), step.raw_ussr_influence.end()),
            torch::kInt16);
        out["raw_ussr_influence"] = tensor_to_numpy<int16_t>(t);
    }
    {
        auto t = torch::tensor(
            std::vector<int16_t>(step.raw_us_influence.begin(), step.raw_us_influence.end()),
            torch::kInt16);
        out["raw_us_influence"] = tensor_to_numpy<int16_t>(t);
    }
    out["raw_turn"]   = step.raw_turn;
    out["raw_ar"]     = step.raw_ar;
    out["raw_defcon"] = step.raw_defcon;
    out["raw_vp"]     = step.raw_vp;
    out["raw_milops"] = py::list(py::cast(
        std::vector<int>(step.raw_milops.begin(), step.raw_milops.end())));
    out["raw_space"]  = py::list(py::cast(
        std::vector<int>(step.raw_space.begin(), step.raw_space.end())));
    out["hand_card_ids"] = py::list(py::cast(step.hand_card_ids));
    // SmallChoice event decision fields (Phase 1e).
    out["small_choice_target"] = step.small_choice_target;
    out["small_choice_n_options"] = step.small_choice_n_options;
    out["small_choice_logprob"] = step.small_choice_logprob;
    return out;
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

py::dict run_ismcts_from_state(
    const py::dict& state_dict,
    const std::string& model_path,
    int n_determinizations,
    int n_simulations,
    int max_pending_per_det,
    float c_puct,
    float calib_a,
    float calib_b,
    py::object seed_obj,
    ts::Side acting_side_override
) {
    if (n_determinizations <= 0) {
        throw py::value_error("n_determinizations must be positive");
    }
    if (n_simulations <= 0) {
        throw py::value_error("n_simulations must be positive");
    }

    ts::GameState gs = game_state_from_dict(state_dict);
    auto& model = get_or_load_model(model_path);

    const ts::Side acting_side = (acting_side_override == ts::Side::Neutral)
        ? gs.pub.phasing
        : acting_side_override;
    const ts::Observation obs = ts::make_observation(gs, acting_side);

    ts::IsmctsConfig config;
    config.n_determinizations = n_determinizations;
    config.max_pending_per_det = max_pending_per_det;
    config.mcts_config.n_simulations = n_simulations;
    config.mcts_config.c_puct = c_puct;
    config.mcts_config.calib_a = calib_a;
    config.mcts_config.calib_b = calib_b;

    ts::Pcg64Rng rng = seed_obj.is_none()
        ? ts::Pcg64Rng()
        : ts::Pcg64Rng(seed_obj.cast<uint64_t>());

    const ts::IsmctsResult result = ts::ismcts_search(obs, model, config, rng);

    py::list edges_out;
    for (const auto& edge : result.aggregated_edges) {
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
    if (!result.aggregated_edges.empty() && result.best_action.card_id != 0) {
        best_action = action_to_dict(result.best_action);
    }
    out["best_action"] = std::move(best_action);
    out["root_value"] = result.mean_root_value;
    out["total_determinizations"] = result.total_determinizations;
    out["edges"] = std::move(edges_out);
    return out;
}

// Play one greedy-NN (learned_side) vs heuristic game and emit a list of
// {state, action, turn, ar, phasing} dicts, one per learned-side decision.
// The state dicts are compatible with game_state_from_dict, so callers can
// feed them back into ismcts_search_from_state / mcts_search_from_state to
// interrogate what search would do at each greedy-NN decision point.
std::vector<py::dict> greedy_state_trace(
    const std::string& model_path,
    ts::Side learned_side,
    uint32_t seed
) {
    if (learned_side != ts::Side::USSR && learned_side != ts::Side::US) {
        throw py::value_error("learned_side must be USSR or US");
    }

    ts::TorchScriptPolicy learned(model_path);
    const ts::PolicyFn learned_fn = [&learned](
        const ts::PublicState& pub,
        const ts::CardSet& hand,
        bool holds_china,
        ts::Pcg64Rng& rng
    ) {
        return learned.choose_action(pub, hand, holds_china, rng);
    };
    const ts::PolicyFn heuristic_fn = [](
        const ts::PublicState& pub,
        const ts::CardSet& hand,
        bool holds_china,
        ts::Pcg64Rng& rng
    ) {
        return ts::choose_action(ts::PolicyKind::MinimalHybrid, pub, hand, holds_china, rng);
    };

    ts::GameLoopConfig config;
    config.use_atomic_setup = true;

    ts::TracedGame traced;
    {
        py::gil_scoped_release release;
        traced = learned_side == ts::Side::USSR
            ? ts::play_game_traced_fn(learned_fn, heuristic_fn, seed, config)
            : ts::play_game_traced_fn(heuristic_fn, learned_fn, seed, config);
    }

    std::vector<py::dict> out;
    for (const auto& step : traced.steps) {
        if (step.side != learned_side) {
            continue;
        }
        py::dict state_dict = public_state_to_dict(step.pub_snapshot);
        augment_state_dict_with_hidden(
            state_dict,
            step.side,
            step.hand_snapshot,
            step.opp_hand_snapshot,
            step.deck_snapshot,
            step.ussr_holds_china_snapshot,
            step.us_holds_china_snapshot
        );
        py::dict step_out;
        step_out["state"] = std::move(state_dict);
        step_out["action"] = action_to_dict(step.action);
        step_out["turn"] = step.turn;
        step_out["ar"] = step.ar;
        step_out["phasing"] = static_cast<int>(step.pub_snapshot.phasing);
        out.push_back(std::move(step_out));
    }
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
        .value("Event", ts::ActionMode::Event)
        .value("EventFirst", ts::ActionMode::EventFirst);

    py::enum_<ts::PolicyKind>(m, "PolicyKind")
        .value("Random", ts::PolicyKind::Random)
        .value("MinimalHybrid", ts::PolicyKind::MinimalHybrid);

    py::enum_<ts::FrameKind>(m, "FrameKind")
        .value("TopLevelAR", ts::FrameKind::TopLevelAR)
        .value("SmallChoice", ts::FrameKind::SmallChoice)
        .value("CountryPick", ts::FrameKind::CountryPick)
        .value("CardSelect", ts::FrameKind::CardSelect)
        .value("ForcedDiscard", ts::FrameKind::ForcedDiscard)
        .value("CancelChoice", ts::FrameKind::CancelChoice)
        .value("FreeOpsInfluence", ts::FrameKind::FreeOpsInfluence)
        .value("NoradInfluence", ts::FrameKind::NoradInfluence)
        .value("DeferredOps", ts::FrameKind::DeferredOps)
        .value("SetupPlacement", ts::FrameKind::SetupPlacement)
        .value("Headline", ts::FrameKind::Headline);

    py::enum_<BoundStepResult>(m, "StepResult")
        .value("Complete", BoundStepResult::Complete)
        .value("SubframePending", BoundStepResult::SubframePending);

    py::class_<ts::Pcg64Rng>(m, "Pcg64Rng")
        .def(py::init<>())
        .def(py::init<uint64_t>(), py::arg("seed"));

    py::class_<ts::DecisionFrame>(m, "DecisionFrame")
        .def_property_readonly("kind", [](const ts::DecisionFrame& frame) { return frame.kind; })
        .def_property_readonly("acting_side", [](const ts::DecisionFrame& frame) { return frame.acting_side; })
        .def_property_readonly("source_card", [](const ts::DecisionFrame& frame) {
            return static_cast<int>(frame.source_card);
        })
        .def_property_readonly("step_index", [](const ts::DecisionFrame& frame) {
            return static_cast<int>(frame.step_index);
        })
        .def_property_readonly("total_steps", [](const ts::DecisionFrame& frame) {
            return static_cast<int>(frame.total_steps);
        })
        .def_property_readonly("budget_remaining", [](const ts::DecisionFrame& frame) {
            return static_cast<int>(frame.budget_remaining);
        })
        .def_property_readonly("stack_depth", [](const ts::DecisionFrame& frame) {
            return static_cast<int>(frame.stack_depth);
        })
        .def_property_readonly("parent_card", [](const ts::DecisionFrame& frame) {
            return static_cast<int>(frame.parent_card);
        })
        .def_property_readonly("eligible_n", [](const ts::DecisionFrame& frame) {
            return static_cast<int>(frame.eligible_n);
        })
        .def_property_readonly("eligible_cards", &decision_frame_cards_to_list)
        .def_property_readonly("eligible_countries", &decision_frame_countries_to_list)
        .def_property_readonly("criteria_bits", [](const ts::DecisionFrame& frame) {
            return static_cast<int>(frame.criteria_bits);
        });

    py::class_<ts::FrameAction>(m, "FrameAction")
        .def(
            py::init(&make_frame_action),
            py::arg("option_index") = 0,
            py::arg("card_id") = 0,
            py::arg("country_id") = 0
        )
        .def_readwrite("option_index", &ts::FrameAction::option_index)
        .def_property(
            "card_id",
            [](const ts::FrameAction& action) { return static_cast<int>(action.card_id); },
            [](ts::FrameAction& action, int card_id) { action.card_id = static_cast<ts::CardId>(card_id); }
        )
        .def_property(
            "country_id",
            [](const ts::FrameAction& action) { return static_cast<int>(action.country_id); },
            [](ts::FrameAction& action, int country_id) {
                action.country_id = static_cast<ts::CountryId>(country_id);
            }
        );

    py::class_<ts::GameState>(m, "GameState")
        .def(py::init<>())
        .def_property_readonly("pub", [](const ts::GameState& gs) {
            return public_state_to_dict(gs.pub);
        })
        .def_property_readonly("ussr_hand", [](const ts::GameState& gs) {
            return bitset_to_list(gs.hands[ts::to_index(ts::Side::USSR)]);
        })
        .def_property_readonly("us_hand", [](const ts::GameState& gs) {
            return bitset_to_list(gs.hands[ts::to_index(ts::Side::US)]);
        })
        .def_property_readonly("frame_stack", [](const ts::GameState& gs) {
            return gs.frame_stack;
        })
        .def_readwrite("frame_stack_mode", &ts::GameState::frame_stack_mode)
        .def_readonly("game_over", &ts::GameState::game_over)
        .def_readonly("winner", &ts::GameState::winner);

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

    py::class_<ts::Observation>(m, "Observation")
        .def_property_readonly("pub", [](const ts::Observation& obs) {
            return public_state_to_dict(obs.pub);
        })
        .def_property_readonly("own_hand", [](const ts::Observation& obs) {
            return bitset_to_list(obs.own_hand);
        })
        .def_readonly("holds_china", &ts::Observation::holds_china)
        .def_readonly("opp_hand_size", &ts::Observation::opp_hand_size)
        .def_readonly("acting_side", &ts::Observation::acting_side);

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
    m.def(
        "reset_game",
        [](py::object seed_obj) {
            std::optional<uint32_t> seed;
            if (!seed_obj.is_none()) {
                seed = seed_obj.cast<uint32_t>();
            }
            return ts::reset_game(seed);
        },
        py::arg("seed") = py::none()
    );
    m.def(
        "engine_peek",
        [](const ts::GameState& gs) {
            return ts::engine_peek(gs);
        },
        py::arg("game_state")
    );
    m.def(
        "engine_step_toplevel",
        [](ts::GameState& gs, int action_index, ts::Pcg64Rng& rng) {
            const auto actions = current_top_level_actions(gs);
            if (action_index < 0 || action_index >= static_cast<int>(actions.size())) {
                throw py::index_error("action_index out of range for current top-level legal actions");
            }
            const auto result = ts::engine_step_toplevel(
                gs,
                actions[static_cast<size_t>(action_index)],
                gs.pub.phasing,
                rng
            );
            return bind_step_result(result);
        },
        py::arg("game_state"),
        py::arg("action_index"),
        py::arg("rng")
    );
    m.def(
        "engine_step_subframe",
        [](ts::GameState& gs, const ts::FrameAction& action, ts::Pcg64Rng& rng) {
            return bind_step_result(ts::engine_step_subframe(gs, action, rng));
        },
        py::arg("game_state"),
        py::arg("frame_action"),
        py::arg("rng")
    );
    m.def("ars_for_turn", &ts::ars_for_turn, py::arg("turn"));
    m.def("hand_size_for_turn", &ts::hand_size_for_turn, py::arg("turn"));
    m.def(
        "load_adjacency",
        []() {
            return adjacency_to_dict();
        },
        "Load the canonical country adjacency graph as {country_id: frozenset[int]}."
    );
    m.def(
        "accessible_countries",
        [](py::object side_obj, py::object pub_obj, py::object mode_obj) {
            const auto side = side_from_python(side_obj);
            const auto mode = mode_obj.is_none() ? ts::ActionMode::Influence : action_mode_from_python(mode_obj);
            return ts::accessible_countries(side, public_state_from_python(pub_obj), mode);
        },
        py::arg("side"),
        py::arg("pub"),
        py::arg("mode") = py::none()
    );
    m.def(
        "effective_ops",
        [](int card_id, py::object pub_obj, py::object side_obj) {
            return ts::effective_ops(
                static_cast<ts::CardId>(card_id),
                public_state_from_python(pub_obj),
                side_from_python(side_obj)
            );
        },
        py::arg("card_id"),
        py::arg("pub"),
        py::arg("side")
    );
    m.def(
        "legal_cards",
        [](py::iterable hand, py::object pub_obj, py::object side_obj, bool holds_china) {
            return ts::legal_cards(
                card_set_from_iterable(hand),
                public_state_from_python(pub_obj),
                side_from_python(side_obj),
                holds_china
            );
        },
        py::arg("hand"),
        py::arg("pub"),
        py::arg("side"),
        py::arg("holds_china") = false
    );
    m.def(
        "legal_modes",
        [](int card_id, py::object pub_obj, py::object side_obj) {
            return ts::legal_modes(
                static_cast<ts::CardId>(card_id),
                public_state_from_python(pub_obj),
                side_from_python(side_obj)
            );
        },
        py::arg("card_id"),
        py::arg("pub"),
        py::arg("side")
    );
    m.def(
        "legal_countries",
        [](int card_id, py::object mode_obj, py::object pub_obj, py::object side_obj) {
            return ts::legal_countries(
                static_cast<ts::CardId>(card_id),
                action_mode_from_python(mode_obj),
                public_state_from_python(pub_obj),
                side_from_python(side_obj)
            );
        },
        py::arg("card_id"),
        py::arg("mode"),
        py::arg("pub"),
        py::arg("side")
    );
    m.def(
        "enumerate_actions",
        [](py::iterable hand, py::object pub_obj, py::object side_obj, bool holds_china, int max_influence_targets) {
            return ts::enumerate_actions(
                card_set_from_iterable(hand),
                public_state_from_python(pub_obj),
                side_from_python(side_obj),
                holds_china,
                max_influence_targets
            );
        },
        py::arg("hand"),
        py::arg("pub"),
        py::arg("side"),
        py::arg("holds_china") = false,
        py::arg("max_influence_targets") = 84
    );
    m.def(
        "has_legal_action",
        [](py::iterable hand, py::object pub_obj, py::object side_obj, bool holds_china) {
            return ts::has_legal_action(
                card_set_from_iterable(hand),
                public_state_from_python(pub_obj),
                side_from_python(side_obj),
                holds_china
            );
        },
        py::arg("hand"),
        py::arg("pub"),
        py::arg("side"),
        py::arg("holds_china") = false
    );
    m.def(
        "make_observation",
        [](const py::dict& state_dict, ts::Side side) {
            return ts::make_observation(game_state_from_dict(state_dict), side);
        },
        py::arg("gs"),
        py::arg("side"),
        "Build an Observation (own hand + support mask) for the given side."
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

    // play_dual_callback_matchup: both sides use the same Python callback.
    // Records decisions for BOTH sides per game — doubles dataset rows vs one-sided collection.
    // Same callback signature as play_callback_matchup; side_int tells which side is acting.
    m.def(
        "play_dual_callback_matchup",
        [](py::function callback, int game_count, py::object seed_obj) {
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
            ts::GameLoopConfig config;
            config.use_atomic_setup = true;
            py::gil_scoped_release release;
            return ts::play_matchup_fn(callback_fn, callback_fn, game_count, seed, config);
        },
        py::arg("callback"),
        py::arg("game_count"),
        py::arg("seed") = py::none(),
        "Run games where BOTH sides use the same Python callback — records all decisions.\n"
        "Doubles dataset rows per game vs play_callback_matchup (one-sided).\n"
        "Callback signature: (state_dict, hand_list, holds_china, side_int) -> action_dict or None."
    );

    // play_traced_game_with_callback: run ONE traced game with a Python callback as both sides.
    // Returns a TracedGame (with .steps and .result) suitable for human-readable game replay.
    m.def(
        "play_traced_game_with_callback",
        [](py::function callback, py::object seed_obj) {
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
            py::gil_scoped_release release;
            return ts::play_game_traced_fn(callback_fn, callback_fn, seed);
        },
        py::arg("callback"),
        py::arg("seed") = py::none(),
        "Run ONE game where both sides use the same Python callback; returns TracedGame.\n"
        "Callback signature: (state_dict, hand_list, holds_china, side_int) -> action_dict or None.\n"
        "TracedGame.steps is a list of StepTrace; TracedGame.result is a GameResult."
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
        "ismcts_search_from_state",
        &run_ismcts_from_state,
        py::arg("state_dict"),
        py::arg("model_path"),
        py::arg("n_determinizations") = 4,
        py::arg("n_simulations") = 50,
        py::arg("max_pending_per_det") = 8,
        py::arg("c_puct") = 1.5f,
        py::arg("calib_a") = 1.0f,
        py::arg("calib_b") = 0.0f,
        py::arg("seed") = py::none(),
        py::arg("acting_side") = ts::Side::Neutral,
        "Run ISMCTS from a serialized game state and return aggregated edges "
        "(visits + priors per action). acting_side=Neutral defaults to state.phasing."
    );
    m.def(
        "greedy_state_trace",
        &greedy_state_trace,
        py::arg("model_path"),
        py::arg("learned_side"),
        py::arg("seed"),
        "Play one greedy-NN vs heuristic game; return per-learned-side-decision "
        "dicts {state, action, turn, ar, phasing} where state is compatible with "
        "game_state_from_dict for feeding into ismcts/mcts_search_from_state."
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
        "benchmark_model_vs_model_batched",
        [](const std::string& model_a_path, const std::string& model_b_path,
           int n_games, int pool_size, py::object seed_obj, const std::string& device_str,
           float temperature, bool nash_temperatures) {
            std::optional<uint32_t> seed;
            if (!seed_obj.is_none()) {
                seed = seed_obj.cast<uint32_t>();
            }
            torch::Device device(device_str);
            auto model_a = torch::jit::load(model_a_path, device);
            model_a.eval();
            auto model_b = torch::jit::load(model_b_path, device);
            model_b.eval();
            return ts::benchmark_model_vs_model_batched(
                n_games, model_a, model_b, pool_size,
                seed.value_or(std::random_device{}()), device, temperature, nash_temperatures);
        },
        py::arg("model_a_path"),
        py::arg("model_b_path"),
        py::arg("n_games") = 100,
        py::arg("pool_size") = 64,
        py::arg("seed") = py::none(),
        py::arg("device") = "cpu",
        py::arg("temperature") = 0.0f,
        py::arg("nash_temperatures") = false,
        "Run model-vs-model benchmark using batched greedy (argmax) inference.\n"
        "Half the games assign model_a=USSR, model_b=US; the other half swap.\n"
        "Both models use argmax action selection (temperature=0) by default.\n"
        "Returns list[GameResult] ordered as: first n_games//2 with model_a=USSR,\n"
        "then n_games//2 with model_a=US."
    );
    m.def(
        "rollout_games_batched",
        [](const std::string& model_path, ts::Side learned_side, int n_games, int pool_size,
           py::object seed_obj, const std::string& device_str, float temperature,
           bool nash_temperatures, float dir_alpha, float dir_epsilon) {
            std::optional<uint32_t> seed;
            if (!seed_obj.is_none()) {
                seed = seed_obj.cast<uint32_t>();
            }
            torch::Device device(device_str);
            auto model = torch::jit::load(model_path, device);
            model.eval();
            auto rollout = ts::rollout_games_batched(
                n_games,
                model,
                learned_side,
                pool_size,
                seed.value_or(std::random_device{}()),
                device,
                temperature,
                nash_temperatures,
                dir_alpha,
                dir_epsilon
            );

            py::list steps_out;
            for (const auto& step : rollout.steps) {
                steps_out.append(rollout_step_to_dict(step));
            }
            return py::make_tuple(rollout.results, steps_out, rollout.game_boundaries);
        },
        py::arg("model_path"),
        py::arg("learned_side"),
        py::arg("n_games"),
        py::arg("pool_size") = 32,
        py::arg("seed") = py::none(),
        py::arg("device") = "cpu",
        py::arg("temperature") = 1.0f,
        py::arg("nash_temperatures") = true,
        py::arg("dir_alpha") = 0.0f,
        py::arg("dir_epsilon") = 0.0f,
        "Run batched stochastic rollout for PPO collection.\n"
        "Returns (results, steps, game_boundaries), where steps contains NumPy\n"
        "feature/mask arrays plus sampled action metadata and log-probs.\n"
        "dir_alpha/dir_epsilon: Dirichlet noise at root (0=disabled)."
    );
    m.def(
        "rollout_self_play_batched",
        [](const std::string& model_path, int n_games, int pool_size,
           py::object seed_obj, const std::string& device_str, float temperature,
           bool nash_temperatures) {
            std::optional<uint32_t> seed;
            if (!seed_obj.is_none()) {
                seed = seed_obj.cast<uint32_t>();
            }
            torch::Device device(device_str);
            auto model = torch::jit::load(model_path, device);
            model.eval();
            auto rollout = ts::rollout_self_play_batched(
                n_games,
                model,
                pool_size,
                seed.value_or(std::random_device{}()),
                device,
                temperature,
                nash_temperatures
            );

            py::list steps_out;
            for (const auto& step : rollout.steps) {
                steps_out.append(rollout_step_to_dict(step));
            }
            return py::make_tuple(rollout.results, steps_out, rollout.game_boundaries);
        },
        py::arg("model_path"),
        py::arg("n_games"),
        py::arg("pool_size") = 32,
        py::arg("seed") = py::none(),
        py::arg("device") = "cpu",
        py::arg("temperature") = 1.0f,
        py::arg("nash_temperatures") = true,
        "Run batched stochastic self-play rollout for PPO collection.\n"
        "Returns (results, steps, game_boundaries), where steps contains NumPy\n"
        "feature/mask arrays plus sampled action metadata and log-probs."
    );
    m.def(
        "rollout_model_vs_model_batched",
        [](const std::string& model_a_path, const std::string& model_b_path,
           int n_games, int pool_size, py::object seed_obj,
           const std::string& device_str, float temperature, bool nash_temperatures,
           float dir_alpha, float dir_epsilon, ts::Side learned_side) {
            std::optional<uint32_t> seed;
            if (!seed_obj.is_none()) {
                seed = seed_obj.cast<uint32_t>();
            }
            torch::Device device(device_str);
            auto model_a = torch::jit::load(model_a_path, device);
            model_a.eval();
            auto model_b = torch::jit::load(model_b_path, device);
            model_b.eval();
            ts::RolloutResult rollout;
            {
                // Release GIL so parallel ThreadPoolExecutor calls run truly concurrently.
                py::gil_scoped_release release;
                rollout = ts::rollout_model_vs_model_batched(
                    n_games,
                    model_a,
                    model_b,
                    pool_size,
                    seed.value_or(std::random_device{}()),
                    device,
                    temperature,
                    nash_temperatures,
                    dir_alpha,
                    dir_epsilon,
                    learned_side
                );
            }  // GIL re-acquired here

            py::list steps_out;
            for (const auto& step : rollout.steps) {
                steps_out.append(rollout_step_to_dict(step));
            }
            return py::make_tuple(rollout.results, steps_out, rollout.game_boundaries);
        },
        py::arg("model_a_path"),
        py::arg("model_b_path"),
        py::arg("n_games"),
        py::arg("pool_size") = 32,
        py::arg("seed") = py::none(),
        py::arg("device") = "cpu",
        py::arg("temperature") = 1.0f,
        py::arg("nash_temperatures") = false,
        py::arg("dir_alpha") = 0.0f,
        py::arg("dir_epsilon") = 0.0f,
        py::arg("learned_side") = ts::Side::Neutral,
        "Run model_a (learning model) vs model_b (opponent) batched rollout.\n"
        "learned_side=Neutral (default): alternating sides.\n"
        "learned_side=USSR: all n_games with model_a as USSR.\n"
        "learned_side=US:   all n_games with model_a as US.\n"
        "Steps are recorded ONLY for model_a decisions.\n"
        "Returns (results, steps, game_boundaries).\n"
        "dir_alpha/dir_epsilon: Dirichlet noise at root for model_a (0=disabled)."
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
            config.mcts_config.dir_alpha = 0.0f;
            config.mcts_config.dir_epsilon = 0.0f;
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
        "benchmark_ismcts_vs_model",
        [](const std::string& search_model_path,
           const std::string& opponent_model_path,
           ts::Side search_side,
           int n_games,
           int n_determinizations, int n_simulations,
           py::object seed_obj, int pool_size,
           int max_pending_per_det, const std::string& device_str) {
            std::optional<uint32_t> seed;
            if (!seed_obj.is_none()) {
                seed = seed_obj.cast<uint32_t>();
            }
            torch::Device device(device_str);
            auto search_model = torch::jit::load(search_model_path, device);
            search_model.eval();
            auto opponent_model = torch::jit::load(opponent_model_path, device);
            opponent_model.eval();
            ts::IsmctsConfig config;
            config.n_determinizations = n_determinizations;
            config.max_pending_per_det = max_pending_per_det;
            config.mcts_config.n_simulations = n_simulations;
            config.mcts_config.dir_alpha = 0.0f;
            config.mcts_config.dir_epsilon = 0.0f;
            return ts::play_ismcts_vs_model_pooled(
                n_games,
                search_model,
                opponent_model,
                search_side,
                config,
                pool_size,
                seed.value_or(std::random_device{}()),
                device
            );
        },
        py::arg("search_model_path"),
        py::arg("opponent_model_path"),
        py::arg("search_side"),
        py::arg("n_games"),
        py::arg("n_determinizations") = 16,
        py::arg("n_simulations") = 100,
        py::arg("seed") = py::none(),
        py::arg("pool_size") = 16,
        py::arg("max_pending_per_det") = 4,
        py::arg("device") = "cpu",
        "Run ISMCTS vs raw-policy benchmark.\n"
        "search_side uses information-set MCTS (search_model); opponent uses greedy model inference (opponent_model).\n"
        "Returns list[GameResult]."
    );
    m.def(
        "benchmark_ismcts_vs_model_both_sides",
        [](const std::string& search_model_path,
           const std::string& opponent_model_path,
           int n_games,
           int n_determinizations, int n_simulations,
           py::object seed_obj, int pool_size,
           int max_pending_per_det, const std::string& device_str) {
            std::optional<uint32_t> seed;
            if (!seed_obj.is_none()) {
                seed = seed_obj.cast<uint32_t>();
            }
            torch::Device device(device_str);
            auto search_model = torch::jit::load(search_model_path, device);
            search_model.eval();
            auto opponent_model = torch::jit::load(opponent_model_path, device);
            opponent_model.eval();
            ts::IsmctsConfig config;
            config.n_determinizations = n_determinizations;
            config.max_pending_per_det = max_pending_per_det;
            config.mcts_config.n_simulations = n_simulations;
            config.mcts_config.dir_alpha = 0.0f;
            config.mcts_config.dir_epsilon = 0.0f;

            const uint32_t base_seed = seed.value_or(std::random_device{}());
            const int half = n_games / 2;
            const int remainder = n_games - half;

            auto results_ussr = ts::play_ismcts_vs_model_pooled(
                half, search_model, opponent_model, ts::Side::USSR,
                config, pool_size, base_seed, device);
            auto results_us = ts::play_ismcts_vs_model_pooled(
                remainder, search_model, opponent_model, ts::Side::US,
                config, pool_size, base_seed + static_cast<uint32_t>(half), device);

            results_ussr.insert(results_ussr.end(), results_us.begin(), results_us.end());
            return results_ussr;
        },
        py::arg("search_model_path"),
        py::arg("opponent_model_path"),
        py::arg("n_games"),
        py::arg("n_determinizations") = 16,
        py::arg("n_simulations") = 100,
        py::arg("seed") = py::none(),
        py::arg("pool_size") = 16,
        py::arg("max_pending_per_det") = 4,
        py::arg("device") = "cpu",
        "Run ISMCTS vs raw-policy benchmark on both sides.\n"
        "First n_games/2 games: search plays USSR; remaining: search plays US.\n"
        "Returns list[GameResult]."
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
           bool greedy_nn_opponent, bool nash_temperatures,
           int n_mcts_threads, int torch_intra_threads, int torch_interop_threads,
           int influence_samples, float influence_t_strategy, float influence_t_country,
           bool influence_proportional_first, float min_prior_threshold,
           int top_k_actions, float pw_c, float pw_alpha,
           float prior_t_card, float prior_t_mode, float prior_t_country) {
            torch::Device device(device_str);
            auto model = torch::jit::load(model_path, device);
            model.eval();
            return ts::benchmark_mcts(
                n_games, model, learned_side, n_simulations, pool_size, seed, device,
                greedy_nn_opponent, nash_temperatures,
                n_mcts_threads, torch_intra_threads, torch_interop_threads,
                influence_samples, influence_t_strategy, influence_t_country,
                influence_proportional_first, min_prior_threshold,
                top_k_actions, pw_c, pw_alpha,
                prior_t_card, prior_t_mode, prior_t_country);
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
        py::arg("n_mcts_threads") = 0,
        py::arg("torch_intra_threads") = 0,
        py::arg("torch_interop_threads") = 0,
        py::arg("influence_samples") = 1,
        py::arg("influence_t_strategy") = 0.0f,
        py::arg("influence_t_country") = 0.0f,
        py::arg("influence_proportional_first") = true,
        py::arg("min_prior_threshold") = 0.0f,
        py::arg("top_k_actions") = 0,
        py::arg("pw_c") = 0.0f,
        py::arg("pw_alpha") = 0.5f,
        py::arg("prior_t_card") = 1.0f,
        py::arg("prior_t_mode") = 1.0f,
        py::arg("prior_t_country") = 1.0f,
        "Run MCTS benchmark. Opponent is heuristic (default) or greedy NN.\n"
        "If nash_temperatures=true (default), the heuristic opponent samples\n"
        "per-game temperatures from the Nash mixed strategy.\n"
        "Thread params: 0 = auto. influence_samples: K edges per influence action.\n"
        "min_prior_threshold: drop edges with prior < threshold after expansion.\n"
        "top_k_actions: keep only the top-K edges by prior after expansion.\n"
        "pw_c/pw_alpha: progressive widening controls for active children.\n"
        "prior_t_card/mode/country: per-head temperature for NN logits (T<1=sharper, T>1=flatter).\n"
        "Returns list[GameResult]."
    );
#endif
}
