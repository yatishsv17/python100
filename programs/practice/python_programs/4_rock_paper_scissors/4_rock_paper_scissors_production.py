"""
Rock Paper Scissors - Production Version
==========================================

WHAT THIS PROGRAM DOES (Flow):
1. Display welcome banner
2. Prompt user for choice (rock/paper/scissors)
   a. Validate input, re-prompt on invalid
3. Computer randomly selects its choice
4. Determine winner using a win-map dictionary
5. Display both choices with emojis and result
6. Track cumulative score across rounds
7. Ask to play again or show final stats

INPUTS:
- User choice (str): 'rock', 'paper', or 'scissors' (case-insensitive)
- Play again (str): 'yes' or 'no'

OUTPUTS:
- Choices with emojis (console)
- Round result (console)
- Cumulative score tracker (console)
- Final statistics on exit (console)

SIDE EFFECTS:
- None

RULES:
- Rock beats Scissors, Scissors beats Paper, Paper beats Rock
- Same choice = Tie
- Score tracked across multiple rounds

ASSUMPTIONS:
- Computer choice is truly random
- Standard game rules apply

DEPENDENCIES:
- random (standard library)
"""

import random
from typing import Optional

CHOICES = ("rock", "paper", "scissors")
EMOJIS = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}

# Maps each choice to what it beats
WIN_MAP = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock",
}


def get_user_choice() -> str:
    """Prompt for a valid rock/paper/scissors choice.

    Returns:
        Validated choice string.
    """
    options_str = ", ".join(CHOICES)
    while True:
        raw = input(f"Choose {options_str}: ").strip().lower()
        if raw in CHOICES:
            return raw
        print(f"  Invalid choice '{raw}'. Please choose from: {options_str}")


def get_computer_choice() -> str:
    """Randomly select the computer's choice.

    Returns:
        A random choice from CHOICES.
    """
    return random.choice(CHOICES)


def determine_winner(user: str, computer: str) -> str:
    """Determine the round winner.

    Args:
        user: The user's choice.
        computer: The computer's choice.

    Returns:
        'win', 'lose', or 'tie'.
    """
    if user == computer:
        return "tie"
    if WIN_MAP[user] == computer:
        return "win"
    return "lose"


def display_round(user: str, computer: str, result: str, scores: dict) -> None:
    """Display round results.

    Args:
        user: User's choice.
        computer: Computer's choice.
        result: Round result ('win', 'lose', 'tie').
        scores: Current score dictionary.
    """
    print(f"\n  You:      {user} {EMOJIS[user]}")
    print(f"  Computer: {computer} {EMOJIS[computer]}")
    messages = {"win": "You win!", "lose": "Computer wins!", "tie": "It's a tie!"}
    print(f"  Result:   {messages[result]}")
    print(f"  Score:    You {scores['wins']} - {scores['losses']} Computer "
          f"(Ties: {scores['ties']})\n")


def display_final_stats(scores: dict) -> None:
    """Display final game statistics.

    Args:
        scores: Final score dictionary.
    """
    total = scores["wins"] + scores["losses"] + scores["ties"]
    print("\n--- Final Stats ---")
    print(f"  Rounds played: {total}")
    print(f"  Wins:   {scores['wins']}")
    print(f"  Losses: {scores['losses']}")
    print(f"  Ties:   {scores['ties']}")
    if total > 0:
        win_rate = (scores["wins"] / total) * 100
        print(f"  Win rate: {win_rate:.1f}%")
    print("-------------------")


def run() -> None:
    """Main program loop."""
    print("=" * 35)
    print("   Rock Paper Scissors")
    print("=" * 35)
    print()

    scores = {"wins": 0, "losses": 0, "ties": 0}

    while True:
        user = get_user_choice()
        computer = get_computer_choice()
        result = determine_winner(user, computer)

        if result == "win":
            scores["wins"] += 1
        elif result == "lose":
            scores["losses"] += 1
        else:
            scores["ties"] += 1

        display_round(user, computer, result, scores)

        again = input("Play again? (yes/no): ").strip().lower()
        if again != "yes":
            display_final_stats(scores)
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    run()
