#include "callback_script.hpp"

#include <algorithm>
#include <chrono>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <sstream>
#include <stdexcept>

#include "evaluator.hpp"
#include "game_data.hpp"
#include "logging.hpp"
#include "profile.hpp"

namespace ts::experimental {
namespace {

constexpr double kSlowSolveLogMs = 100.0;

struct CaptureStop final : std::exception {
    const char* what() const noexcept override { return "capture_stop"; }
};

const char* decision_kind_name(DecisionKind kind) {
    switch (kind) {
        case DecisionKind::SmallChoice: return "small_choice";
        case DecisionKind::CountrySelect: return "country_select";
        case DecisionKind::CardSelect: return "card_select";
    }
    return "unknown";
}

bool slow_callback_logging_enabled() {
    static const bool enabled = [] {
        const char* value = std::getenv("TS_EXP_LOG_SLOW_CALLBACKS");
        return value != nullptr && value[0] != '\0' && value[0] != '0';
    }();
    return enabled;
}

int map_script_decision_to_index(const ScriptDecision& script, const EventDecision& decision) {
    if (script.kind == DecisionKind::SmallChoice) {
        return std::clamp(script.chosen_index, 0, std::max(0, decision.n_options - 1));
    }
    for (int idx = 0; idx < decision.n_options; ++idx) {
        if (decision.eligible_ids[idx] == script.chosen_id) {
            return idx;
        }
    }
    return std::clamp(script.chosen_index, 0, std::max(0, decision.n_options - 1));
}

ScriptDecision make_script_decision(const EventDecision& decision, int option_index) {
    ScriptDecision out;
    out.source_card = decision.source_card;
    out.kind = decision.kind;
    out.acting_side = decision.acting_side;
    out.chosen_index = option_index;
    if (decision.kind == DecisionKind::SmallChoice) {
        out.chosen_id = option_index;
    } else {
        out.chosen_id = decision.eligible_ids[option_index];
    }
    return out;
}

struct ReplayScriptCallback {
    const std::vector<ScriptDecision>& script;
    size_t cursor = 0;

    int operator()(const PublicState&, const EventDecision& decision) {
        if (cursor >= script.size()) {
            return 0;
        }
        const auto& item = script[cursor++];
        return map_script_decision_to_index(item, decision);
    }
};

struct CaptureFirstDecisionCallback {
    const std::vector<ScriptDecision>& prefix;
    size_t cursor = 0;
    PublicState captured_pub{};
    EventDecision captured{};
    bool has_captured = false;

    int operator()(const PublicState& pub, const EventDecision& decision) {
        if (cursor < prefix.size()) {
            return map_script_decision_to_index(prefix[cursor++], decision);
        }
        captured_pub = pub;
        captured = decision;
        has_captured = true;
        throw CaptureStop{};
    }
};

double country_priority(const PublicState& pub, Side side, CountryId cid) {
    const auto& spec = country_spec(cid);
    const double region_weight = [&]() {
        switch (spec.region) {
            case Region::Europe: return 1.35;
            case Region::Asia: return 1.2;
            case Region::MiddleEast: return 1.15;
            case Region::SouthAmerica: return 1.0;
            case Region::CentralAmerica: return 0.95;
            case Region::Africa: return 0.9;
            case Region::SoutheastAsia: return 1.0;
        }
        return 1.0;
    }();
    const auto own = static_cast<double>(pub.influence_of(side, cid));
    const auto opp = static_cast<double>(pub.influence_of(other_side(side), cid));
    const auto stability = static_cast<double>(spec.stability);
    double score = region_weight * (spec.is_battleground ? 1.6 : 1.0);
    score *= 1.0 + 0.08 * (own - opp) - 0.12 * ((opp + stability) - own);
    return score;
}

double card_priority(const PublicState&, Side side, CardId card_id) {
    const auto& spec = card_spec(card_id);
    double score = static_cast<double>(spec.ops);
    if (spec.is_scoring) {
        score += 3.0;
    }
    if (spec.side == side) {
        score += 1.5;
    } else if (spec.side == other_side(side)) {
        score -= 1.0;
    } else {
        score += 0.4;
    }
    if (spec.starred) {
        score += 0.2;
    }
    return score;
}

std::vector<int> shortlist_options(const PublicState& pub, const EventDecision& decision) {
    std::vector<int> options;
    options.reserve(static_cast<size_t>(decision.n_options));
    for (int idx = 0; idx < decision.n_options; ++idx) {
        options.push_back(idx);
    }
    if (decision.n_options <= 4 || decision.kind == DecisionKind::SmallChoice) {
        return options;
    }

    std::vector<std::pair<double, int>> scored;
    scored.reserve(options.size());
    for (const auto idx : options) {
        double score = 0.0;
        if (decision.kind == DecisionKind::CountrySelect) {
            score = country_priority(pub, decision.acting_side, static_cast<CountryId>(decision.eligible_ids[idx]));
        } else {
            score = card_priority(pub, decision.acting_side, static_cast<CardId>(decision.eligible_ids[idx]));
        }
        scored.push_back({score, idx});
    }
    std::sort(scored.begin(), scored.end(), [](const auto& lhs, const auto& rhs) {
        return lhs.first > rhs.first;
    });

    std::vector<int> shortlisted;
    const int top_keep = std::min(3, static_cast<int>(scored.size()));
    for (int i = 0; i < top_keep; ++i) {
        shortlisted.push_back(scored[static_cast<size_t>(i)].second);
    }
    for (int i = static_cast<int>(scored.size()) - 1; i >= 0 && static_cast<int>(shortlisted.size()) < 4; --i) {
        const auto option = scored[static_cast<size_t>(i)].second;
        if (std::find(shortlisted.begin(), shortlisted.end(), option) == shortlisted.end()) {
            shortlisted.push_back(option);
        }
    }
    std::sort(shortlisted.begin(), shortlisted.end());
    return shortlisted;
}

double evaluate_finished_resolution(
    const GameState& gs,
    const ResolutionOutcome& outcome,
    Side evaluation_side,
    const HeuristicConfig& config
) {
    if (outcome.over) {
        return evaluate_terminal_for_side(outcome.winner, evaluation_side, config);
    }
    return evaluate_state_for_side(gs, evaluation_side, config);
}

struct SolveResult {
    double score = 0.0;
    CallbackScript script;
};

struct SolveStats {
    int nodes = 0;
    int leaves = 0;
    int max_depth = 0;
    int root_options = 0;
    DecisionKind root_kind = DecisionKind::SmallChoice;
    bool root_captured = false;
};

SolveResult solve_with_prefix(
    const GameState& root_state,
    Side root_side,
    const ResolutionFn& resolution_fn,
    const Pcg64Rng& root_rng,
    Side evaluation_side,
    const HeuristicConfig& config,
    const CallbackScript& prefix,
    SolveStats& stats
) {
    ++stats.nodes;
    stats.max_depth = std::max(stats.max_depth, static_cast<int>(prefix.decisions.size()));
    GameState gs = root_state;
    auto rng = root_rng;
    CaptureFirstDecisionCallback callback{.prefix = prefix.decisions};
    ResolutionOutcome outcome;
    try {
        const PolicyCallbackFn cb = [&callback](const PublicState& pub, const EventDecision& decision) {
            return callback(pub, decision);
        };
        outcome = resolution_fn(gs, rng, &cb);
    } catch (const CaptureStop&) {
    }

    if (!callback.has_captured) {
        ++stats.leaves;
        return SolveResult{
            .score = evaluate_finished_resolution(gs, outcome, evaluation_side, config),
            .script = prefix,
        };
    }

    if (prefix.decisions.empty() && !stats.root_captured) {
        stats.root_captured = true;
        stats.root_options = callback.captured.n_options;
        stats.root_kind = callback.captured.kind;
    }

    const bool maximizing = callback.captured.acting_side == evaluation_side;
    SolveResult best;
    best.score = maximizing ? -std::numeric_limits<double>::infinity() : std::numeric_limits<double>::infinity();
    const auto options = shortlist_options(callback.captured_pub, callback.captured);
    for (const auto option : options) {
        auto next_prefix = prefix;
        next_prefix.decisions.push_back(make_script_decision(callback.captured, option));
        auto candidate = solve_with_prefix(
            root_state,
            root_side,
            resolution_fn,
            root_rng,
            evaluation_side,
            config,
            next_prefix,
            stats
        );
        const bool better = maximizing ? candidate.score > best.score : candidate.score < best.score;
        if (better) {
            best = std::move(candidate);
        }
    }
    return best;
}

}  // namespace

CallbackScript solve_callback_script(
    const GameState& root_state,
    Side root_side,
    const ResolutionFn& resolution_fn,
    Pcg64Rng root_rng,
    Side evaluation_side,
    const HeuristicConfig& config,
    std::string_view label
) {
    const profile::ScopedTimer timer(profile::Slot::SolveCallbackScript);
    const auto start = std::chrono::steady_clock::now();
    SolveStats stats;
    const auto solved = solve_with_prefix(root_state, root_side, resolution_fn, root_rng, evaluation_side, config, {}, stats);
    const auto elapsed_ms = std::chrono::duration<double, std::milli>(std::chrono::steady_clock::now() - start).count();
    if (slow_callback_logging_enabled() && elapsed_ms >= kSlowSolveLogMs) {
        std::ostringstream line;
        line << logging::prefix(__FILE__, __LINE__)
             << "slow_callback_solve"
             << " label=\"" << label << "\""
             << " elapsed_ms=" << elapsed_ms
             << " nodes=" << stats.nodes
             << " leaves=" << stats.leaves
             << " max_depth=" << stats.max_depth
             << " root_options=" << stats.root_options
             << " root_kind=" << decision_kind_name(stats.root_kind)
             << " chosen_depth=" << solved.script.decisions.size();
        std::cerr << line.str() << std::endl;
    }
    return solved.script;
}

PolicyCallbackFn make_replay_callback(const CallbackScript& script) {
    return [state = ReplayScriptCallback{.script = script.decisions}](const PublicState& pub, const EventDecision& decision) mutable {
        return state(pub, decision);
    };
}

}  // namespace ts::experimental
