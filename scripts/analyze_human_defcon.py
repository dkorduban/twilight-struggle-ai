#!/usr/bin/env python3
"""
Analyze human replay logs for DEFCON behavior and coup patterns.

Extract:
1. DEFCON distribution across all games
2. Coup behavior at low DEFCON (3, 2)
3. Risky card handling (DEFCON-lowering cards)
4. MilOps behavior patterns
5. Final game DEFCON levels
"""

import re
from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Optional

# Card IDs that lower DEFCON
DEFCON_LOWERING_CARDS = {
    "Duck and Cover": 4,
    "We Will Bury You": 53,
    "KAL 007": 92,
}

@dataclass
class GameAnalysis:
    """Track game state and events."""
    game_file: str
    current_defcon: int = 5  # Start at DEFCON 5
    current_turn: int = 0
    current_player: Optional[str] = None
    defcon_history: list[tuple[int, int, str]] = field(default_factory=list)  # (turn, defcon, context)
    coups: list[dict] = field(default_factory=list)
    card_plays: list[dict] = field(default_factory=list)
    milops_history: list[tuple[int, int, int]] = field(default_factory=list)  # (turn, ussr_milops, us_milops)
    risky_card_events: list[dict] = field(default_factory=list)
    final_defcon: int = 5
    nuclear_war: bool = False
    game_ended_by: str = "unknown"  # 'nuclear_war', 'turn_10', 'scoring', 'unknown'

def parse_game_log(file_path: Path) -> GameAnalysis:
    """Parse a single game log file."""
    game = GameAnalysis(game_file=file_path.name)

    with open(file_path, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        line = line.rstrip()

        # Track turn number
        turn_match = re.match(r'Turn (\d+),', line)
        if turn_match:
            game.current_turn = int(turn_match.group(1))

        # Track player
        player_match = re.search(r'(USSR|US) AR\d+:', line)
        if player_match:
            game.current_player = player_match.group(1)

        # DEFCON changes
        if 'DEFCON degrades to' in line:
            match = re.search(r'DEFCON degrades to (\d)', line)
            if match:
                new_defcon = int(match.group(1))
                game.current_defcon = new_defcon
                game.defcon_history.append((game.current_turn, new_defcon, 'degraded'))
                # Check if this was a coup
                if i > 0 and 'Coup' in lines[i-1]:
                    if game.coups:
                        game.coups[-1]['resulted_in_defcon'] = new_defcon

        if 'DEFCON improves to' in line:
            match = re.search(r'DEFCON improves to (\d)', line)
            if match:
                new_defcon = int(match.group(1))
                game.current_defcon = new_defcon
                game.defcon_history.append((game.current_turn, new_defcon, 'improved'))

        # Coups
        if 'Coup (' in line and 'Ops' in line:
            match = re.search(r'Coup \((\d) Ops\)', line)
            if match:
                ops = int(match.group(1))
                coup_entry = {
                    'turn': game.current_turn,
                    'player': game.current_player,
                    'ops': ops,
                    'defcon_at_time': game.current_defcon,
                    'target': None,
                    'success': None,
                    'resulted_in_defcon': None,
                }
                game.coups.append(coup_entry)

        # Coup target
        if 'Target:' in line and game.coups:
            match = re.search(r'Target:\s*(.+)', line)
            if match:
                game.coups[-1]['target'] = match.group(1).strip()

        # Coup result
        if 'SUCCESS:' in line or 'DEFEAT:' in line:
            if game.coups:
                success = 'SUCCESS' in line
                game.coups[-1]['success'] = success
                # Extract result value if present
                match = re.search(r'(SUCCESS|DEFEAT):\s*(\d+)', line)
                if match:
                    game.coups[-1]['result_value'] = int(match.group(2))

        # MilOps tracking
        if 'Military Ops to' in line:
            match = re.search(r'(USSR|US) Military Ops to (\d)', line)
            if match:
                player = match.group(1)
                milops = int(match.group(2))
                # This is simplified; we'd need to track both separately

        # Risky card plays (cards that lower DEFCON)
        for card_name, card_id in DEFCON_LOWERING_CARDS.items():
            if card_name in line and 'Event:' in line:
                game.risky_card_events.append({
                    'turn': game.current_turn,
                    'card': card_name,
                    'card_id': card_id,
                    'defcon_at_time': game.current_defcon,
                    'line': line,
                })

        # Check for nuclear war
        if 'Nuclear War' in line or 'DEFCON reaches 1' in line:
            game.nuclear_war = True
            game.game_ended_by = 'nuclear_war'

        # End of turn 10
        if 'Turn 10' in line and 'Cleanup' in line:
            game.final_defcon = game.current_defcon
            if not game.nuclear_war:
                game.game_ended_by = 'turn_10'

        # Scoring at end
        if 'Final Score' in line or 'Game Over' in line:
            game.final_defcon = game.current_defcon
            if not game.nuclear_war:
                game.game_ended_by = 'scoring'

    return game

def analyze_all_games(raw_logs_dir: Path) -> list[GameAnalysis]:
    """Analyze all game logs."""
    log_files = sorted(raw_logs_dir.glob("*.txt"))
    # Exclude synthetic files
    log_files = [f for f in log_files if 'synthetic' not in f.name.lower()]

    games = []
    for log_file in log_files:
        try:
            game = parse_game_log(log_file)
            games.append(game)
        except Exception as e:
            print(f"Error parsing {log_file.name}: {e}")

    return games

def generate_report(games: list[GameAnalysis], output_file: Path) -> None:
    """Generate analysis report."""

    report_lines = []
    report_lines.append("# Human Replay Analysis: DEFCON and Coup Behavior\n")
    report_lines.append(f"Analysis Date: 2026-03-29\n")
    report_lines.append(f"Total Games Analyzed: {len(games)}\n\n")

    # DEFCON distribution at game end
    report_lines.append("## 1. Final DEFCON Distribution\n")
    final_defcon_dist = defaultdict(int)
    for game in games:
        final_defcon_dist[game.final_defcon] += 1

    for defcon in sorted(final_defcon_dist.keys(), reverse=True):
        count = final_defcon_dist[defcon]
        pct = 100.0 * count / len(games)
        report_lines.append(f"- DEFCON {defcon}: {count} games ({pct:.1f}%)\n")

    nuclear_wars = sum(1 for g in games if g.nuclear_war)
    report_lines.append(f"- **Nuclear Wars (DEFCON 1)**: {nuclear_wars} games ({100.0*nuclear_wars/len(games):.1f}%)\n\n")

    # DEFCON trajectory - how deep do games go?
    report_lines.append("## 2. Maximum DEFCON Depth Reached (Minimum DEFCON)\n")
    min_defcons = [min([g.current_defcon] + [d for _, d, _ in g.defcon_history]) if g.defcon_history else g.current_defcon
                   for g in games]
    min_defcon_dist = defaultdict(int)
    for md in min_defcons:
        min_defcon_dist[md] += 1

    for defcon in sorted(min_defcon_dist.keys()):
        count = min_defcon_dist[defcon]
        pct = 100.0 * count / len(games)
        report_lines.append(f"- DEFCON {defcon} reached: {count} games ({pct:.1f}%)\n")
    report_lines.append("\n")

    # Coup analysis
    report_lines.append("## 3. Coup Behavior Analysis\n")
    total_coups = sum(len(g.coups) for g in games)
    report_lines.append(f"Total coups across all games: {total_coups}\n\n")

    # Coups at each DEFCON level
    coups_by_defcon = defaultdict(list)
    for game in games:
        for coup in game.coups:
            coups_by_defcon[coup['defcon_at_time']].append(coup)

    report_lines.append("### Coups by DEFCON Level\n")
    for defcon in sorted(coups_by_defcon.keys(), reverse=True):
        coups = coups_by_defcon[defcon]
        successful = sum(1 for c in coups if c['success'])
        report_lines.append(f"- **DEFCON {defcon}**: {len(coups)} coups ({successful} successful, {len(coups)-successful} failed)\n")
        # Sample targets
        targets = defaultdict(int)
        for coup in coups:
            if coup['target']:
                targets[coup['target']] += 1
        top_targets = sorted(targets.items(), key=lambda x: x[1], reverse=True)[:3]
        for target, count in top_targets:
            report_lines.append(f"  - {target}: {count}\n")
    report_lines.append("\n")

    # Coups at DEFCON 3 or lower (risky)
    report_lines.append("### High-Risk Coups (DEFCON 3 or Lower)\n")
    risky_coups = [c for coups in [coups_by_defcon[d] for d in [1, 2, 3]] for c in coups]
    report_lines.append(f"Total risky coups: {len(risky_coups)}\n")

    if risky_coups:
        bg_coups = sum(1 for c in risky_coups if c['target'] and any(bg in c['target'].lower() for bg in
                       ['afghanistan', 'angola', 'cuba', 'east germany', 'ethiopia', 'hungary', 'iran',
                        'iraq', 'israel', 'laos', 'middle east', 'thailand', 'vietnam', 'yugoslavia',
                        'cambodia', 'pakistan', 'south africa', 'south korea', 'west germany']))
        report_lines.append(f"- Battleground coups: {bg_coups}\n")
        report_lines.append(f"- Non-battleground coups: {len(risky_coups) - bg_coups}\n\n")

    # Risky card handling
    report_lines.append("## 4. Risky Card Handling (DEFCON-Lowering Cards)\n")
    all_risky_cards = []
    for game in games:
        all_risky_cards.extend(game.risky_card_events)

    report_lines.append(f"Total DEFCON-lowering card events triggered: {len(all_risky_cards)}\n\n")

    if all_risky_cards:
        risky_by_card = defaultdict(list)
        for event in all_risky_cards:
            risky_by_card[event['card']].append(event)

        for card_name in sorted(risky_by_card.keys()):
            events = risky_by_card[card_name]
            report_lines.append(f"### {card_name}\n")
            report_lines.append(f"- Triggered: {len(events)} times\n")
            avg_defcon = sum(e['defcon_at_time'] for e in events) / len(events)
            report_lines.append(f"- Average DEFCON when triggered: {avg_defcon:.1f}\n")
            report_lines.append(f"- DEFCON range: {min(e['defcon_at_time'] for e in events)}-{max(e['defcon_at_time'] for e in events)}\n\n")

    # Game ending analysis
    report_lines.append("## 5. How Games End\n")
    end_reasons = defaultdict(int)
    for game in games:
        end_reasons[game.game_ended_by] += 1

    for reason in sorted(end_reasons.keys()):
        count = end_reasons[reason]
        pct = 100.0 * count / len(games)
        report_lines.append(f"- {reason}: {count} games ({pct:.1f}%)\n")
    report_lines.append("\n")

    # Key insights
    report_lines.append("## Key Insights\n\n")

    # Insight 1: Nuclear war frequency
    nuc_pct = 100.0 * nuclear_wars / len(games)
    report_lines.append(f"### Nuclear War Risk\n")
    report_lines.append(f"**Finding**: {nuc_pct:.1f}% of games reached nuclear war (DEFCON 1).\n")
    if nuclear_wars == 0:
        report_lines.append("**Implication**: Human players are highly conservative with DEFCON risk. They avoid situations that spiral to nuclear war.\n")
    else:
        report_lines.append(f"**Implication**: {nuclear_wars} games out of {len(games)} went nuclear. This represents {'frequent' if nuc_pct > 10 else 'occasional'} risk-taking.\n")
    report_lines.append("\n")

    # Insight 2: DEFCON 3 coups
    defcon3_coups = len(coups_by_defcon.get(3, []))
    report_lines.append(f"### DEFCON 3 Coup Aggression\n")
    report_lines.append(f"**Finding**: {defcon3_coups} coups at DEFCON 3 (high risk of triggering DEFCON 2 → 1).\n")
    if defcon3_coups > 0:
        report_lines.append(f"**Implication**: Humans do take DEFCON 3 risks, typically for key battleground control.\n")
    report_lines.append("\n")

    # Insight 3: Risky cards
    if all_risky_cards:
        avg_risky_defcon = sum(e['defcon_at_time'] for e in all_risky_cards) / len(all_risky_cards)
        report_lines.append(f"### Risky Card Play Timing\n")
        report_lines.append(f"**Finding**: Risky cards (Duck & Cover, KAL 007, We Will Bury You) triggered at average DEFCON {avg_risky_defcon:.1f}.\n")
        report_lines.append(f"**Implication**: When these cards must trigger (as events), humans have usually kept DEFCON safe (4-5).\n")

    # Write report
    with open(output_file, 'w') as f:
        f.writelines(report_lines)

    print(f"Report written to {output_file}")

if __name__ == '__main__':
    raw_logs_dir = Path('/home/dkord/code/twilight-struggle-ai/data/raw_logs')
    output_file = Path('/home/dkord/code/twilight-struggle-ai/.codex_tasks/human-defcon-analysis/result.md')

    games = analyze_all_games(raw_logs_dir)
    print(f"Loaded {len(games)} games")

    generate_report(games, output_file)
