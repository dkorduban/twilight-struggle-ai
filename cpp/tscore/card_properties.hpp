#pragma once
// Canonical DEFCON-lowering card set.
// A card "lowers DEFCON" if playing it as ops at DEFCON <= 2 can cause
// DEFCON to drop to 1, ending the game immediately.
//
// Keep this in sync with scripts/train_ppo.py (DEFCON_LOWERING_CARDS).
// Duplicates existed in: mcts.cpp, ismcts.cpp, mcts_batched.cpp,
//   learned_policy.cpp, policies.cpp — all should #include this header.
#include <algorithm>
#include <array>

namespace tscore {

// Cards whose event or ops can lower DEFCON by 1 or more.
// At DEFCON <= 2, these cards should not be chosen for ops that include coups
// on battleground countries.
//
// Card notes:
//   4   Duck and Cover (US): lowers DEFCON
//   20  Olympic Games (Neutral): DEFCON drops on boycott
//   48  Summit (Neutral): can lower DEFCON
//   49  How I Learned to Stop Worrying (USSR): sets DEFCON directly
//   50  Junta (Neutral): free coup in Central/South America
//   52  Missile Envy (Neutral): calls apply_ops_randomly -> can coup BG
//   53  We Will Bury You (USSR): lowers DEFCON
//   68  Grain Sales to Soviets (US): calls apply_ops_randomly -> can coup BG
//   83  Che (USSR): free coup in Latin America / Africa
//   92  Soviets Shoot Down KAL 007 (US): lowers DEFCON by 1, -2 VP
constexpr std::array<int, 10> kDefconLoweringCards = {
    4, 20, 48, 49, 50, 52, 53, 68, 83, 92,
};

// Returns true if card_id is in kDefconLoweringCards.
inline bool is_defcon_lowering(int card_id) {
    return std::find(kDefconLoweringCards.begin(),
                     kDefconLoweringCards.end(),
                     card_id) != kDefconLoweringCards.end();
}

} // namespace tscore
