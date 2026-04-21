// Run native MCTS search from a serialized state or a fresh deterministic turn.

#include <algorithm>
#include <chrono>
#include <cctype>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <iterator>
#include <optional>
#include <random>
#include <stdexcept>
#include <string>
#include <string_view>
#include <unordered_map>
#include <utility>
#include <variant>
#include <vector>

#include <torch/script.h>

#include "game_data.hpp"
#include "game_loop.hpp"
#include "game_state.hpp"
#include "mcts.hpp"
#include "policies.hpp"
#include "scoring.hpp"
#include "step.hpp"

namespace {

constexpr int kMidWarTurn = 4;
constexpr int kLateWarTurn = 8;
constexpr int kMaxTurns = 10;
constexpr size_t kTopEdgeCount = 10;

class JsonValue {
public:
    using Object = std::unordered_map<std::string, JsonValue>;
    using Array = std::vector<JsonValue>;
    using Storage = std::variant<std::nullptr_t, bool, double, std::string, Array, Object>;

    JsonValue() : value_(nullptr) {}
    explicit JsonValue(std::nullptr_t value) : value_(value) {}
    explicit JsonValue(bool value) : value_(value) {}
    explicit JsonValue(double value) : value_(value) {}
    explicit JsonValue(std::string value) : value_(std::move(value)) {}
    explicit JsonValue(Array value) : value_(std::move(value)) {}
    explicit JsonValue(Object value) : value_(std::move(value)) {}

    [[nodiscard]] bool is_null() const { return std::holds_alternative<std::nullptr_t>(value_); }
    [[nodiscard]] bool is_bool() const { return std::holds_alternative<bool>(value_); }
    [[nodiscard]] bool is_number() const { return std::holds_alternative<double>(value_); }
    [[nodiscard]] bool is_string() const { return std::holds_alternative<std::string>(value_); }
    [[nodiscard]] bool is_array() const { return std::holds_alternative<Array>(value_); }
    [[nodiscard]] bool is_object() const { return std::holds_alternative<Object>(value_); }

    [[nodiscard]] bool as_bool(const char* field_name) const {
        if (!is_bool()) {
            throw std::runtime_error(std::string("expected boolean for field: ") + field_name);
        }
        return std::get<bool>(value_);
    }

    [[nodiscard]] int as_int(const char* field_name) const {
        if (!is_number()) {
            throw std::runtime_error(std::string("expected number for field: ") + field_name);
        }
        return static_cast<int>(std::get<double>(value_));
    }

    [[nodiscard]] const std::string& as_string(const char* field_name) const {
        if (!is_string()) {
            throw std::runtime_error(std::string("expected string for field: ") + field_name);
        }
        return std::get<std::string>(value_);
    }

    [[nodiscard]] const Array& as_array(const char* field_name) const {
        if (!is_array()) {
            throw std::runtime_error(std::string("expected array for field: ") + field_name);
        }
        return std::get<Array>(value_);
    }

    [[nodiscard]] const Object& as_object(const char* field_name) const {
        if (!is_object()) {
            throw std::runtime_error(std::string("expected object for field: ") + field_name);
        }
        return std::get<Object>(value_);
    }

private:
    Storage value_;
};

class JsonParser {
public:
    explicit JsonParser(std::string_view input) : input_(input) {}

    [[nodiscard]] JsonValue parse() {
        auto value = parse_value();
        skip_whitespace();
        if (pos_ != input_.size()) {
            throw std::runtime_error("unexpected trailing JSON content");
        }
        return value;
    }

private:
    [[nodiscard]] JsonValue parse_value() {
        skip_whitespace();
        if (pos_ >= input_.size()) {
            throw std::runtime_error("unexpected end of JSON input");
        }

        const char ch = input_[pos_];
        if (ch == '{') {
            return JsonValue(parse_object());
        }
        if (ch == '[') {
            return JsonValue(parse_array());
        }
        if (ch == '"') {
            return JsonValue(parse_string());
        }
        if (ch == 't') {
            consume_literal("true");
            return JsonValue(true);
        }
        if (ch == 'f') {
            consume_literal("false");
            return JsonValue(false);
        }
        if (ch == 'n') {
            consume_literal("null");
            return JsonValue(nullptr);
        }
        if (ch == '-' || std::isdigit(static_cast<unsigned char>(ch))) {
            return JsonValue(parse_number());
        }

        throw std::runtime_error("unexpected JSON token");
    }

    [[nodiscard]] JsonValue::Object parse_object() {
        expect('{');
        skip_whitespace();

        JsonValue::Object object;
        if (peek('}')) {
            expect('}');
            return object;
        }

        while (true) {
            skip_whitespace();
            const auto key = parse_string();
            skip_whitespace();
            expect(':');
            object.emplace(key, parse_value());
            skip_whitespace();
            if (peek('}')) {
                expect('}');
                break;
            }
            expect(',');
        }

        return object;
    }

    [[nodiscard]] JsonValue::Array parse_array() {
        expect('[');
        skip_whitespace();

        JsonValue::Array array;
        if (peek(']')) {
            expect(']');
            return array;
        }

        while (true) {
            array.push_back(parse_value());
            skip_whitespace();
            if (peek(']')) {
                expect(']');
                break;
            }
            expect(',');
        }

        return array;
    }

    [[nodiscard]] std::string parse_string() {
        expect('"');
        std::string out;
        while (pos_ < input_.size()) {
            const char ch = input_[pos_++];
            if (ch == '"') {
                return out;
            }
            if (ch == '\\') {
                if (pos_ >= input_.size()) {
                    throw std::runtime_error("unterminated JSON escape");
                }
                const char escaped = input_[pos_++];
                switch (escaped) {
                    case '"': out.push_back('"'); break;
                    case '\\': out.push_back('\\'); break;
                    case '/': out.push_back('/'); break;
                    case 'b': out.push_back('\b'); break;
                    case 'f': out.push_back('\f'); break;
                    case 'n': out.push_back('\n'); break;
                    case 'r': out.push_back('\r'); break;
                    case 't': out.push_back('\t'); break;
                    default:
                        throw std::runtime_error("unsupported JSON escape sequence");
                }
                continue;
            }
            out.push_back(ch);
        }
        throw std::runtime_error("unterminated JSON string");
    }

    [[nodiscard]] double parse_number() {
        const size_t start = pos_;
        if (input_[pos_] == '-') {
            ++pos_;
        }
        consume_digits();
        if (pos_ < input_.size() && input_[pos_] == '.') {
            ++pos_;
            consume_digits();
        }
        if (pos_ < input_.size() && (input_[pos_] == 'e' || input_[pos_] == 'E')) {
            ++pos_;
            if (pos_ < input_.size() && (input_[pos_] == '+' || input_[pos_] == '-')) {
                ++pos_;
            }
            consume_digits();
        }
        return std::stod(std::string(input_.substr(start, pos_ - start)));
    }

    void consume_digits() {
        const size_t digit_start = pos_;
        while (pos_ < input_.size() && std::isdigit(static_cast<unsigned char>(input_[pos_]))) {
            ++pos_;
        }
        if (digit_start == pos_) {
            throw std::runtime_error("expected digit in JSON number");
        }
    }

    void consume_literal(std::string_view literal) {
        if (input_.substr(pos_, literal.size()) != literal) {
            throw std::runtime_error("invalid JSON literal");
        }
        pos_ += literal.size();
    }

    void skip_whitespace() {
        while (pos_ < input_.size() && std::isspace(static_cast<unsigned char>(input_[pos_]))) {
            ++pos_;
        }
    }

    [[nodiscard]] bool peek(char ch) const {
        return pos_ < input_.size() && input_[pos_] == ch;
    }

    void expect(char ch) {
        skip_whitespace();
        if (pos_ >= input_.size() || input_[pos_] != ch) {
            throw std::runtime_error(std::string("expected JSON character: ") + ch);
        }
        ++pos_;
    }

    std::string_view input_;
    size_t pos_ = 0;
};

const JsonValue& require_field(const JsonValue::Object& object, const char* field_name) {
    const auto it = object.find(field_name);
    if (it == object.end()) {
        throw std::runtime_error(std::string("missing required field: ") + field_name);
    }
    return it->second;
}

std::vector<int> read_int_array(const JsonValue::Object& object, const char* field_name) {
    const auto& values = require_field(object, field_name).as_array(field_name);
    std::vector<int> out;
    out.reserve(values.size());
    for (const auto& value : values) {
        out.push_back(value.as_int(field_name));
    }
    return out;
}

ts::CardSet read_card_set(const JsonValue::Object& object, const char* field_name) {
    ts::CardSet cards;
    for (const int card_id : read_int_array(object, field_name)) {
        if (card_id < 0 || card_id > ts::kMaxCardId) {
            throw std::runtime_error(std::string("card id out of range in field: ") + field_name);
        }
        cards.set(static_cast<size_t>(card_id));
    }
    return cards;
}

ts::GameState game_state_from_json_object(const JsonValue::Object& object) {
    ts::GameState gs;
    ts::PublicState& pub = gs.pub;

    pub.turn = require_field(object, "turn").as_int("turn");
    pub.ar = require_field(object, "ar").as_int("ar");
    pub.phasing = static_cast<ts::Side>(require_field(object, "phasing").as_int("phasing"));
    pub.vp = require_field(object, "vp").as_int("vp");
    pub.defcon = require_field(object, "defcon").as_int("defcon");

    const auto milops = read_int_array(object, "milops");
    if (milops.size() != 2) {
        throw std::runtime_error("milops must contain exactly 2 integers");
    }
    pub.milops[0] = milops[0];
    pub.milops[1] = milops[1];

    const auto space = read_int_array(object, "space");
    if (space.size() != 2) {
        throw std::runtime_error("space must contain exactly 2 integers");
    }
    pub.space[0] = space[0];
    pub.space[1] = space[1];

    pub.china_held_by = static_cast<ts::Side>(require_field(object, "china_held_by").as_int("china_held_by"));
    pub.china_playable = require_field(object, "china_playable").as_bool("china_playable");

    const auto ussr_influence = read_int_array(object, "ussr_influence");
    const auto us_influence = read_int_array(object, "us_influence");
    if (ussr_influence.size() != ts::kCountrySlots || us_influence.size() != ts::kCountrySlots) {
        throw std::runtime_error("influence arrays must have length 86");
    }
    for (int country_id = 0; country_id <= ts::kMaxCountryId; ++country_id) {
        pub.influence[ts::to_index(ts::Side::USSR)][country_id] = static_cast<int16_t>(ussr_influence[static_cast<size_t>(country_id)]);
        pub.influence[ts::to_index(ts::Side::US)][country_id] = static_cast<int16_t>(us_influence[static_cast<size_t>(country_id)]);
    }

    pub.discard = read_card_set(object, "discard");
    pub.removed = read_card_set(object, "removed");

    pub.warsaw_pact_played = require_field(object, "warsaw_pact_played").as_bool("warsaw_pact_played");
    pub.marshall_plan_played = require_field(object, "marshall_plan_played").as_bool("marshall_plan_played");
    pub.truman_doctrine_played = require_field(object, "truman_doctrine_played").as_bool("truman_doctrine_played");
    pub.john_paul_ii_played = require_field(object, "john_paul_ii_played").as_bool("john_paul_ii_played");
    pub.nato_active = require_field(object, "nato_active").as_bool("nato_active");
    pub.de_gaulle_active = require_field(object, "de_gaulle_active").as_bool("de_gaulle_active");
    pub.willy_brandt_active = require_field(object, "willy_brandt_active").as_bool("willy_brandt_active");
    pub.us_japan_pact_active = require_field(object, "us_japan_pact_active").as_bool("us_japan_pact_active");
    pub.nuclear_subs_active = require_field(object, "nuclear_subs_active").as_bool("nuclear_subs_active");
    pub.norad_active = require_field(object, "norad_active").as_bool("norad_active");
    pub.shuttle_diplomacy_active = require_field(object, "shuttle_diplomacy_active").as_bool("shuttle_diplomacy_active");
    pub.flower_power_active = require_field(object, "flower_power_active").as_bool("flower_power_active");
    pub.flower_power_cancelled = require_field(object, "flower_power_cancelled").as_bool("flower_power_cancelled");
    pub.salt_active = require_field(object, "salt_active").as_bool("salt_active");
    pub.opec_cancelled = require_field(object, "opec_cancelled").as_bool("opec_cancelled");
    pub.awacs_active = require_field(object, "awacs_active").as_bool("awacs_active");
    pub.north_sea_oil_extra_ar = require_field(object, "north_sea_oil_extra_ar").as_bool("north_sea_oil_extra_ar");
    if (const auto it = object.find("glasnost_free_ops"); it != object.end()) {
        pub.glasnost_free_ops = it->second.as_int("glasnost_free_ops");
    } else {
        pub.glasnost_free_ops = require_field(object, "glasnost_extra_ar").as_bool("glasnost_extra_ar") ? 4 : 0;
    }
    pub.formosan_active = require_field(object, "formosan_active").as_bool("formosan_active");
    pub.cuban_missile_crisis_active = require_field(object, "cuban_missile_crisis_active").as_bool("cuban_missile_crisis_active");
    pub.vietnam_revolts_active = require_field(object, "vietnam_revolts_active").as_bool("vietnam_revolts_active");
    pub.bear_trap_active = require_field(object, "bear_trap_active").as_bool("bear_trap_active");
    pub.quagmire_active = require_field(object, "quagmire_active").as_bool("quagmire_active");
    pub.iran_hostage_crisis_active = require_field(object, "iran_hostage_crisis_active").as_bool("iran_hostage_crisis_active");
    pub.handicap_ussr = require_field(object, "handicap_ussr").as_int("handicap_ussr");
    pub.handicap_us = require_field(object, "handicap_us").as_int("handicap_us");

    const auto ops_modifier = read_int_array(object, "ops_modifier");
    if (ops_modifier.size() != 2) {
        throw std::runtime_error("ops_modifier must contain exactly 2 integers");
    }
    pub.ops_modifier[0] = ops_modifier[0];
    pub.ops_modifier[1] = ops_modifier[1];

    gs.hands[ts::to_index(ts::Side::USSR)] = read_card_set(object, "ussr_hand");
    gs.hands[ts::to_index(ts::Side::US)] = read_card_set(object, "us_hand");

    for (const int card_id : read_int_array(object, "deck")) {
        if (card_id < 0 || card_id > ts::kMaxCardId) {
            throw std::runtime_error("card id out of range in deck");
        }
        gs.deck.push_back(static_cast<ts::CardId>(card_id));
    }

    gs.ussr_holds_china = require_field(object, "ussr_holds_china").as_bool("ussr_holds_china");
    gs.us_holds_china = require_field(object, "us_holds_china").as_bool("us_holds_china");
    gs.phase = ts::GamePhase::Headline;
    gs.current_side = pub.phasing;
    gs.ar_index = 1;
    gs.ars_taken = {0, 0};
    return gs;
}

std::string read_text_file(const std::string& path) {
    std::ifstream input(path);
    if (!input) {
        throw std::runtime_error("failed to open file: " + path);
    }
    return std::string(
        std::istreambuf_iterator<char>(input),
        std::istreambuf_iterator<char>()
    );
}

ts::GameState load_state_json(const std::string& path) {
    const auto parsed = JsonParser(read_text_file(path)).parse();
    const auto& root = parsed.as_object("root");
    const auto state_it = root.find("state_dict");
    if (state_it != root.end()) {
        return game_state_from_json_object(state_it->second.as_object("state_dict"));
    }
    return game_state_from_json_object(root);
}

ts::PolicyFn minimal_hybrid_policy() {
    return [](const ts::PublicState& pub, const ts::CardSet& hand, bool holds_china, ts::Pcg64Rng& rng) {
        return ts::choose_action(ts::PolicyKind::MinimalHybrid, pub, hand, holds_china, rng);
    };
}

std::optional<ts::GameResult> end_of_turn_cleanup(ts::GameState& gs, int turn) {
    gs.phase = ts::GamePhase::Cleanup;

    const auto defcon = gs.pub.defcon;
    for (const auto side : {ts::Side::USSR, ts::Side::US}) {
        const auto shortfall = std::max(0, defcon - gs.pub.milops[ts::to_index(side)]);
        if (shortfall == 0) {
            continue;
        }
        if (side == ts::Side::USSR) {
            gs.pub.vp -= shortfall;
        } else {
            gs.pub.vp += shortfall;
        }
    }

    auto [over, winner] = ts::check_vp_win(gs.pub);
    if (over) {
        return ts::GameResult{
            .winner = winner,
            .final_vp = gs.pub.vp,
            .end_turn = gs.pub.turn,
            .end_reason = "vp",
        };
    }

    gs.pub.defcon = std::min(5, gs.pub.defcon + 1);
    gs.pub.milops = {0, 0};
    gs.pub.space_attempts = {0, 0};
    gs.pub.ops_modifier = {0, 0};
    gs.pub.vietnam_revolts_active = false;
    gs.pub.yuri_samantha_active = false;
    gs.pub.north_sea_oil_extra_ar = false;
    gs.pub.glasnost_free_ops = 0;
    gs.pub.chernobyl_blocked_region.reset();
    gs.pub.latam_coup_bonus.reset();

    for (const auto side : {ts::Side::USSR, ts::Side::US}) {
        for (int card_id = 1; card_id <= ts::kMaxCardId; ++card_id) {
            if (gs.hands[ts::to_index(side)].test(card_id) &&
                ts::card_spec(static_cast<ts::CardId>(card_id)).is_scoring) {
                return ts::GameResult{
                    .winner = ts::other_side(side),
                    .final_vp = gs.pub.vp,
                    .end_turn = gs.pub.turn,
                    .end_reason = "scoring_card_held",
                };
            }
        }
    }

    if (turn == kMaxTurns) {
        auto final = ts::apply_final_scoring(gs.pub);
        gs.pub.vp += final.vp_delta;
        if (final.game_over) {
            return ts::GameResult{
                .winner = final.winner,
                .final_vp = gs.pub.vp,
                .end_turn = turn,
                .end_reason = "europe_control",
            };
        }
    }

    for (const auto side : {ts::Side::USSR, ts::Side::US}) {
        for (int card_id = 1; card_id <= ts::kMaxCardId; ++card_id) {
            if (gs.hands[ts::to_index(side)].test(card_id)) {
                gs.pub.discard.set(card_id);
            }
        }
        gs.hands[ts::to_index(side)].reset();
    }

    return std::nullopt;
}

ts::GameState fresh_state_for_turn(int target_turn, std::optional<uint32_t> seed) {
    if (target_turn < 1 || target_turn > kMaxTurns) {
        throw std::runtime_error("turn must be between 1 and 10");
    }

    auto gs = ts::reset_game(seed);
    ts::Pcg64Rng rng(seed.has_value() ? ts::Pcg64Rng(*seed) : ts::Pcg64Rng(std::random_device{}()));
    const auto policy = minimal_hybrid_policy();

    for (int turn = 1; turn <= target_turn; ++turn) {
        gs.pub.turn = turn;
        if (turn == kMidWarTurn) {
            ts::advance_to_mid_war(gs, rng);
        } else if (turn == kLateWarTurn) {
            ts::advance_to_late_war(gs, rng);
        }
        ts::deal_cards(gs, ts::Side::USSR, rng);
        ts::deal_cards(gs, ts::Side::US, rng);

        if (turn == target_turn) {
            gs.phase = ts::GamePhase::Headline;
            gs.current_side = ts::Side::USSR;
            gs.pub.phasing = ts::Side::USSR;
            gs.pub.ar = 0;
            gs.ar_index = 1;
            gs.ars_taken = {0, 0};
            return gs;
        }

        if (auto result = ts::run_headline_phase_live(gs, policy, policy, rng, nullptr); result.has_value()) {
            throw std::runtime_error(
                "game ended before requested turn " + std::to_string(target_turn) +
                " during headline phase of turn " + std::to_string(turn)
            );
        }
        if (auto result = ts::run_action_rounds_live(gs, policy, policy, rng, ts::ars_for_turn(turn), nullptr); result.has_value()) {
            throw std::runtime_error(
                "game ended before requested turn " + std::to_string(target_turn) +
                " during action rounds of turn " + std::to_string(turn)
            );
        }
        if (gs.pub.north_sea_oil_extra_ar) {
            gs.pub.north_sea_oil_extra_ar = false;
            if (auto result = ts::run_extra_action_round_live(gs, ts::Side::US, policy, rng, nullptr); result.has_value()) {
                throw std::runtime_error(
                    "game ended before requested turn " + std::to_string(target_turn) +
                    " during extra US action round of turn " + std::to_string(turn)
                );
            }
        }
        if (gs.pub.glasnost_free_ops > 0) {
            ts::resolve_glasnost_free_ops_live(gs.pub, rng);
        }
        if (auto result = end_of_turn_cleanup(gs, turn); result.has_value()) {
            throw std::runtime_error(
                "game ended before requested turn " + std::to_string(target_turn) +
                " during cleanup of turn " + std::to_string(turn)
            );
        }
    }

    return gs;
}

void write_action_json(std::ostream& out, const ts::ActionEncoding& action) {
    out << "{\"card_id\":" << static_cast<int>(action.card_id)
        << ",\"mode\":" << static_cast<int>(action.mode)
        << ",\"targets\":[";
    for (size_t i = 0; i < action.targets.size(); ++i) {
        if (i > 0) {
            out << ",";
        }
        out << static_cast<int>(action.targets[i]);
    }
    out << "]}";
}

void usage(const char* argv0) {
    std::cerr
        << "usage: " << argv0
        << " --model <path.pt>"
        << " [--n-sim <int>]"
        << " [--c-puct <float>]"
        << " [--seed <uint32>]"
        << " [--state-json <path>]"
        << " [--turn <int>]\n";
}

}  // namespace

int main(int argc, char** argv) {
    try {
        std::optional<std::string> model_path;
        std::optional<std::string> state_json_path;
        std::optional<uint32_t> seed;
        int n_simulations = 200;
        float c_puct = 1.5f;
        int turn = 1;

        for (int i = 1; i < argc; ++i) {
            const std::string_view arg = argv[i];
            auto require_value = [&](const char* flag) -> std::string_view {
                if (i + 1 >= argc) {
                    throw std::runtime_error(std::string("missing value for ") + flag);
                }
                return argv[++i];
            };

            if (arg == "--model") {
                model_path = std::string(require_value("--model"));
            } else if (arg == "--n-sim") {
                n_simulations = std::stoi(std::string(require_value("--n-sim")));
            } else if (arg == "--c-puct") {
                c_puct = std::stof(std::string(require_value("--c-puct")));
            } else if (arg == "--seed") {
                seed = static_cast<uint32_t>(std::stoul(std::string(require_value("--seed"))));
            } else if (arg == "--state-json") {
                state_json_path = std::string(require_value("--state-json"));
            } else if (arg == "--turn") {
                turn = std::stoi(std::string(require_value("--turn")));
            } else if (arg == "--help" || arg == "-h") {
                usage(argv[0]);
                return 0;
            } else {
                usage(argv[0]);
                throw std::runtime_error(std::string("unknown argument: ") + std::string(arg));
            }
        }

        if (!model_path.has_value()) {
            usage(argv[0]);
            throw std::runtime_error("--model is required");
        }
        if (n_simulations <= 0) {
            throw std::runtime_error("--n-sim must be positive");
        }
        if (c_puct <= 0.0f) {
            throw std::runtime_error("--c-puct must be positive");
        }
        if (state_json_path.has_value() && turn != 1) {
            throw std::runtime_error("--turn cannot be combined with --state-json");
        }

        const ts::GameState state = state_json_path.has_value()
            ? load_state_json(*state_json_path)
            : fresh_state_for_turn(turn, seed);

        torch::jit::script::Module model = torch::jit::load(*model_path);
        model.eval();

        ts::MctsConfig config;
        config.n_simulations = n_simulations;
        config.c_puct = c_puct;

        ts::Pcg64Rng rng(seed.has_value() ? ts::Pcg64Rng(*seed) : ts::Pcg64Rng());
        const auto started = std::chrono::steady_clock::now();
        const ts::SearchResult result = ts::mcts_search(state, model, config, rng);
        const auto elapsed = std::chrono::duration<double>(std::chrono::steady_clock::now() - started).count();

        auto edges = result.root_edges;
        std::stable_sort(edges.begin(), edges.end(), [](const ts::MctsEdge& lhs, const ts::MctsEdge& rhs) {
            if (lhs.visit_count != rhs.visit_count) {
                return lhs.visit_count > rhs.visit_count;
            }
            if (lhs.mean_value() != rhs.mean_value()) {
                return lhs.mean_value() > rhs.mean_value();
            }
            return lhs.prior > rhs.prior;
        });
        if (edges.size() > kTopEdgeCount) {
            edges.resize(kTopEdgeCount);
        }

        std::cout << "{";
        std::cout << "\"best_action\":";
        if (result.root_edges.empty() || result.best_action.card_id == 0) {
            std::cout << "null";
        } else {
            write_action_json(std::cout, result.best_action);
        }
        std::cout << ",\"root_value\":" << result.root_value;
        std::cout << ",\"total_simulations\":" << result.total_simulations;
        std::cout << ",\"elapsed_seconds\":" << elapsed;
        std::cout << ",\"edges\":[";
        for (size_t i = 0; i < edges.size(); ++i) {
            if (i > 0) {
                std::cout << ",";
            }
            std::cout << "{\"action\":";
            write_action_json(std::cout, edges[i].action);
            std::cout << ",\"visits\":" << edges[i].visit_count
                << ",\"mean_value\":" << edges[i].mean_value()
                << ",\"prior\":" << edges[i].prior
                << "}";
        }
        std::cout << "]}\n";
        return 0;
    } catch (const std::exception& ex) {
        std::cerr << "error: " << ex.what() << "\n";
        return 1;
    }
}
