#include "profile.hpp"

#include <array>
#include <atomic>
#include <sstream>

namespace ts::experimental::profile {
namespace {

struct Counter {
    std::atomic<long long> nanos{0};
    std::atomic<long long> calls{0};
};

std::array<Counter, static_cast<size_t>(Slot::Count)> g_counters;
std::atomic<bool> g_enabled{false};

const char* slot_name(Slot slot) {
    switch (slot) {
        case Slot::ChooseSearchAction: return "choose_search_action";
        case Slot::EnumerateActionProposals: return "enumerate_action_proposals";
        case Slot::CandidateActions: return "candidate_actions";
        case Slot::BeamInfluenceActions: return "beam_influence_actions";
        case Slot::PlanActionOnce: return "plan_action_once";
        case Slot::SolveCallbackScript: return "solve_callback_script";
        case Slot::ExactActionValue: return "exact_action_value";
        case Slot::NormalizeToDecisionPoint: return "normalize_to_decision_point";
        case Slot::EvaluateState: return "evaluate_state";
        case Slot::Count: break;
    }
    return "unknown";
}

}  // namespace

void set_enabled(bool enabled_flag) {
    g_enabled.store(enabled_flag);
}

bool enabled() {
    return g_enabled.load();
}

void reset() {
    for (auto& counter : g_counters) {
        counter.nanos.store(0);
        counter.calls.store(0);
    }
}

void add(Slot slot, std::chrono::nanoseconds elapsed) {
    g_counters[static_cast<size_t>(slot)].nanos.fetch_add(elapsed.count(), std::memory_order_relaxed);
}

void increment(Slot slot) {
    g_counters[static_cast<size_t>(slot)].calls.fetch_add(1, std::memory_order_relaxed);
}

std::string report() {
    std::ostringstream out;
    out << "experimental_profile\n";
    for (size_t idx = 0; idx < g_counters.size(); ++idx) {
        const auto slot = static_cast<Slot>(idx);
        const auto nanos = g_counters[idx].nanos.load(std::memory_order_relaxed);
        const auto calls = g_counters[idx].calls.load(std::memory_order_relaxed);
        const double millis = static_cast<double>(nanos) / 1'000'000.0;
        const double avg_millis = calls > 0 ? millis / static_cast<double>(calls) : 0.0;
        out << slot_name(slot)
            << " calls=" << calls
            << " total_ms=" << millis
            << " avg_ms=" << avg_millis
            << '\n';
    }
    return out.str();
}

}  // namespace ts::experimental::profile
