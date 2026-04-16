#pragma once

#include <chrono>
#include <cstdint>
#include <string>

namespace ts::experimental::profile {

enum class Slot : uint8_t {
    ChooseSearchAction = 0,
    EnumerateActionProposals = 1,
    CandidateActions = 2,
    BeamInfluenceActions = 3,
    PlanActionOnce = 4,
    SolveCallbackScript = 5,
    ExactActionValue = 6,
    NormalizeToDecisionPoint = 7,
    EvaluateState = 8,
    Count = 9,
};

void set_enabled(bool enabled);
bool enabled();
void reset();
void add(Slot slot, std::chrono::nanoseconds elapsed);
void increment(Slot slot);
std::string report();

class ScopedTimer {
public:
    explicit ScopedTimer(Slot slot)
        : slot_(slot), start_(std::chrono::steady_clock::now()), active_(enabled()) {}

    ~ScopedTimer() {
        if (!active_) {
            return;
        }
        add(slot_, std::chrono::steady_clock::now() - start_);
        increment(slot_);
    }

private:
    Slot slot_;
    std::chrono::steady_clock::time_point start_;
    bool active_ = false;
};

}  // namespace ts::experimental::profile
