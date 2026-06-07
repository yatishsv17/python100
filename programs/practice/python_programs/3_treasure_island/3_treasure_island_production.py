"""
Treasure Island - Production Version
======================================

WHAT THIS PROGRAM DOES (Flow):
1. Display welcome banner with ASCII art
2. Present decision nodes as a tree:
   Node 1: Crossroad → left / right
     - right → Game Over (fall into hole)
     - left  → Node 2
   Node 2: Lake → wait / swim
     - swim → Game Over (attacked by trout)
     - wait → Node 3
   Node 3: Three doors → red / yellow / blue
     - red    → Game Over (room of fire)
     - blue   → Game Over (room of beasts)
     - yellow → Victory! (treasure found)
3. Display result with themed messages
4. Show game summary and offer replay

INPUTS:
- Choices at each node (str): validated against allowed options
- Play again choice (str): 'yes' or 'no'

OUTPUTS:
- Narrative text at each decision point (console)
- Game Over or Victory message with ASCII art (console)
- Game statistics (choices made, path taken)

SIDE EFFECTS:
- None

RULES:
- Winning path: left → wait → yellow
- All other paths lead to game over
- Case-insensitive, whitespace-trimmed input
- Invalid choices prompt re-entry (not game over)

ASSUMPTIONS:
- Single-path adventure (one winning route)
- User reads narrative text before choosing

DEPENDENCIES:
- None (standard library only)
"""

import sys
from typing import Optional


SCENARIOS = {
    "crossroad": {
        "prompt": "You're at a crossroad. Where do you want to go?",
        "options": ["left", "right"],
        "results": {
            "right": {
                "outcome": "lose",
                "message": "You fell into a hole. Game Over.",
            },
            "left": {
                "outcome": "continue",
                "message": "You chose the left path and come to a lake...",
            },
        },
    },
    "lake": {
        "prompt": "There is an island in the middle of the lake. What do you do?",
        "options": ["wait", "swim"],
        "results": {
            "swim": {
                "outcome": "lose",
                "message": "You get attacked by an angry trout. Game Over.",
            },
            "wait": {
                "outcome": "continue",
                "message": "You wait for a boat and arrive at the island safely...",
            },
        },
    },
    "doors": {
        "prompt": "There is a house with 3 doors. One red, one yellow, one blue. Which do you choose?",
        "options": ["red", "yellow", "blue"],
        "results": {
            "red": {
                "outcome": "lose",
                "message": "It's a room full of fire. Game Over.",
            },
            "blue": {
                "outcome": "lose",
                "message": "You enter a room of beasts. Game Over.",
            },
            "yellow": {
                "outcome": "win",
                "message": "You found the treasure! You Win!",
            },
        },
    },
}

GAME_SEQUENCE = ["crossroad", "lake", "doors"]


def display_banner() -> None:
    """Display the welcome banner with ASCII art."""
    print("=" * 50)
    print("        WELCOME TO TREASURE ISLAND")
    print("    Your mission is to find the treasure.")
    print("=" * 50)
    print()


def get_choice(scenario: dict) -> str:
    """Prompt the user for a valid choice within a scenario.

    Args:
        scenario: Dictionary with prompt, options, and results.

    Returns:
        The validated user choice (lowercase).
    """
    options_str = " / ".join(f'"{opt}"' for opt in scenario["options"])
    while True:
        raw = input(f"\n{scenario['prompt']}\nChoose {options_str}: ").strip().lower()
        if raw in scenario["options"]:
            return raw
        print(f"  Invalid choice '{raw}'. Please choose from: {options_str}")


def play_game() -> tuple[bool, list[str]]:
    """Run one game session.

    Returns:
        Tuple of (won: bool, choices_made: list[str]).
    """
    choices_made = []
    for scene_key in GAME_SEQUENCE:
        scenario = SCENARIOS[scene_key]
        choice = get_choice(scenario)
        choices_made.append(choice)
        result = scenario["results"][choice]
        print(f"\n  >> {result['message']}")

        if result["outcome"] == "lose":
            return False, choices_made
        if result["outcome"] == "win":
            return True, choices_made
    return False, choices_made


def display_summary(won: bool, choices: list[str]) -> None:
    """Display game summary.

    Args:
        won: Whether the player won.
        choices: List of choices made during the game.
    """
    print("\n--- Game Summary ---")
    print(f"  Path taken: {' → '.join(choices)}")
    print(f"  Decisions made: {len(choices)}")
    if won:
        print("  Result: VICTORY! You found the treasure!")
    else:
        print("  Result: GAME OVER")
    print("--------------------\n")


def run() -> None:
    """Main program loop."""
    display_banner()

    while True:
        won, choices = play_game()
        display_summary(won, choices)

        again = input("Play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing Treasure Island!")
            break
        print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    run()
