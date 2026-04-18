// Mutable hidden-information game state used by the native live engine.

#pragma once

#include <algorithm>
#include <array>
#include <bitset>
#include <cstring>
#include <random>
#include <span>
#include <stdexcept>
#include <string>
#include <vector>

#include "decision_frame.hpp"
#include "public_state.hpp"
#include "rng.hpp"

namespace ts {

// Fixed-capacity inline deck that eliminates heap allocation on copy.
// Max capacity = kCardSlots (112), more than enough for any game state.
struct InlineDeck {
    static constexpr int kCapacity = kCardSlots;  // 112

    int size_ = 0;
    std::array<CardId, kCapacity> data_;

    InlineDeck() = default;

    // Construct from vector or span.
    explicit InlineDeck(std::span<const CardId> cards)
        : size_(static_cast<int>(cards.size())) {
        std::memcpy(data_.data(), cards.data(), cards.size());
    }

    // Assign from vector.
    InlineDeck& operator=(const std::vector<CardId>& v) {
        size_ = static_cast<int>(v.size());
        std::memcpy(data_.data(), v.data(), v.size());
        return *this;
    }
    InlineDeck& operator=(std::vector<CardId>&& v) {
        return operator=(static_cast<const std::vector<CardId>&>(v));
    }

    // Assign from iterator range.
    template<typename It>
    void assign(It first, It last) {
        size_ = 0;
        for (auto it = first; it != last; ++it) {
            data_[static_cast<size_t>(size_++)] = *it;
        }
    }

    [[nodiscard]] int size() const { return size_; }
    [[nodiscard]] bool empty() const { return size_ == 0; }
    void clear() { size_ = 0; }

    CardId& operator[](size_t i) { return data_[i]; }
    const CardId& operator[](size_t i) const { return data_[i]; }

    CardId& front() { return data_[0]; }
    const CardId& front() const { return data_[0]; }
    CardId& back() { return data_[static_cast<size_t>(size_ - 1)]; }
    const CardId& back() const { return data_[static_cast<size_t>(size_ - 1)]; }

    void push_back(CardId c) {
        if (size_ >= kCapacity) {
            throw std::out_of_range("InlineDeck overflow in push_back: size=" + std::to_string(size_));
        }
        data_[static_cast<size_t>(size_++)] = c;
    }
    void pop_back() { --size_; }

    CardId* begin() { return data_.data(); }
    CardId* end() { return data_.data() + size_; }
    const CardId* begin() const { return data_.data(); }
    const CardId* end() const { return data_.data() + size_; }

    // Erase single element by iterator (shifts left).
    CardId* erase(CardId* pos) {
        auto next = pos + 1;
        std::memmove(pos, next, static_cast<size_t>(end() - next));
        --size_;
        return pos;
    }

    // Erase range [first, last).
    CardId* erase(CardId* first, CardId* last) {
        if (first == last) return first;
        auto tail = static_cast<size_t>(end() - last);
        std::memmove(first, last, tail);
        size_ -= static_cast<int>(last - first);
        return first;
    }

    // Insert range before pos.
    template<typename It>
    void insert(CardId* pos, It first, It last) {
        int count = 0;
        for (auto it = first; it != last; ++it) ++count;
        if (count == 0) return;
        if (size_ + count > kCapacity) {
            throw std::out_of_range("InlineDeck overflow in insert: size=" + std::to_string(size_) + " count=" + std::to_string(count));
        }
        auto offset = static_cast<size_t>(pos - begin());
        // Shift existing elements right.
        std::memmove(data_.data() + offset + count, data_.data() + offset,
                     static_cast<size_t>(size_) - offset);
        int i = static_cast<int>(offset);
        for (auto it = first; it != last; ++it) {
            data_[static_cast<size_t>(i++)] = *it;
        }
        size_ += count;
    }

    // Convert to vector (for logging/snapshots).
    [[nodiscard]] std::vector<CardId> to_vector() const {
        return {begin(), end()};
    }
};

struct GameState {
    PublicState pub;
    std::array<CardSet, 2> hands;
    InlineDeck deck;
    bool ussr_holds_china = true;
    bool us_holds_china = false;
    GamePhase phase = GamePhase::Setup;
    Side current_side = Side::USSR;
    int ar_index = 1;
    std::array<int, 2> ars_taken = {0, 0};
    std::array<CardId, 2> headline_card = {0, 0};
    bool game_over = false;
    std::optional<Side> winner;
    std::vector<DecisionFrame> frame_stack;  // pending sub-decisions
    // Remaining setup-phase influence placements: index 0 = USSR, index 1 = US.
    // Non-zero only while phase == GamePhase::Setup.
    std::array<int, 2> setup_influence_remaining = {kUSSRSetupInfluence, kUSSetupInfluence};
};

// What one player can observe: public board + own hand + opponent hand size.
// The opponent's actual hand is hidden. Used as the root input for ISMCTS.
struct Observation {
    PublicState pub;
    CardSet own_hand;
    bool holds_china = false;
    int opp_hand_size = 0;
    Side acting_side = Side::USSR;
};

// Turn-specific constants and reset helpers used by normal play plus parity
// tools that need exact setup control.
int ars_for_turn(int turn);
int hand_size_for_turn(int turn);
GameState reset_game(std::optional<uint32_t> seed = std::nullopt);
GameState reset_game_from_rng(Pcg64Rng& rng);
GameState reset_game_from_seed_words(std::array<uint64_t, 4> words);
GameState clone_game_state(const GameState& gs);
[[nodiscard]] Observation make_observation(const GameState& gs, Side acting_side);
[[nodiscard]] GameState determinize(const Observation& obs, Pcg64Rng& rng);
void deal_cards(GameState& gs, Side side, Pcg64Rng& rng);
void advance_to_mid_war(GameState& gs, Pcg64Rng& rng);
void advance_to_late_war(GameState& gs, Pcg64Rng& rng);
std::vector<CardId> hand_to_vector(const CardSet& hand);
int hand_count(const CardSet& hand);

}  // namespace ts
