"""
Number Guessing Game - Production Version
===========================================

WHAT THIS PROGRAM DOES (Flow):
1. Display welcome banner with rules
2. Prompt for difficulty: easy (10 attempts) or hard (5 attempts)
3. Generate random secret number between 1 and 100
4. Game loop:
   a. Show remaining attempts
   b. Prompt for guess (validated: integer 1-100, not already guessed)
   c. Compare guess to secret
   d. Provide hint: too high / too low / correct
   e. Track guess history
5. On win/lose:
   a. Display result
   b. Show statistics (guesses made, guess history)
   c. Offer replay

INPUTS:
- Difficulty (str): 'easy' or 'hard' (case-insensitive)
- Guesses (int): 1-100
- Play again (str): 'yes' or 'no'

OUTPUTS:
- Hints after each guess (console)
- Remaining attempts (console)
- Guess history (console)
- Win/lose message with statistics (console)

SIDE EFFECTS:
- None

RULES:
- Secret number: 1-100 inclusive
- Easy: 10 attempts, Hard: 5 attempts
- Duplicate guesses rejected without penalty

ASSUMPTIONS:
- User understands number range
- Binary search is optimal strategy

DEPENDENCIES:
- random (standard library)
"""

import random

RANGE_MIN = 1
RANGE_MAX = 100
DIFFICULTY_MAP = {"easy": 10, "hard": 5}


def get_difficulty() -> int:
    """Prompt for difficulty and return the number of attempts.

    Returns:
        Number of attempts based on chosen difficulty.
    """
    options = ", ".join(DIFFICULTY_MAP.keys())
    while True:
        raw = input(f"Choose a difficulty ({options}): ").strip().lower()
        if raw in DIFFICULTY_MAP:
            print(f"  You chose {raw}. You have {DIFFICULTY_MAP[raw]} attempts.\n")
            return DIFFICULTY_MAP[raw]
        print(f"  Invalid choice. Please type {options}.")


def get_guess(guessed: set[int]) -> int:
    """Prompt for a valid guess.

    Args:
        guessed: Set of previously guessed numbers.

    Returns:
        A valid integer between RANGE_MIN and RANGE_MAX.
    """
    while True:
        raw = input("Make a guess: ").strip()
        try:
            guess = int(raw)
        except ValueError:
            print(f"  Error: '{raw}' is not a valid integer.")
            continue
        if guess < RANGE_MIN or guess > RANGE_MAX:
            print(f"  Error: Guess must be between {RANGE_MIN} and {RANGE_MAX}.")
            continue
        if guess in guessed:
            print(f"  You already guessed {guess}. Try a different number.")
            continue
        return guess


def play_game() -> tuple[bool, int, list[int]]:
    """Play one game session.

    Returns:
        Tuple of (won: bool, secret: int, guess_history: list[int]).
    """
    secret = random.randint(RANGE_MIN, RANGE_MAX)
    attempts = get_difficulty()
    guessed: set[int] = set()
    history: list[int] = []

    while attempts > 0:
        print(f"  Attempts remaining: {attempts}")
        guess = get_guess(guessed)
        guessed.add(guess)
        history.append(guess)

        if guess == secret:
            return True, secret, history
        elif guess < secret:
            print("  Too low.\n")
        else:
            print("  Too high.\n")

        attempts -= 1

    return False, secret, history


def display_result(won: bool, secret: int, history: list[int]) -> None:
    """Display game result and statistics.

    Args:
        won: Whether the player won.
        secret: The secret number.
        history: List of guesses in order.
    """
    print(f"\n{'=' * 35}")
    if won:
        print(f"  You got it! The answer was {secret}.")
        print(f"  Guesses needed: {len(history)}")
    else:
        print(f"  You ran out of guesses.")
        print(f"  The number was {secret}.")

    print(f"  Guess history: {history}")

    if len(history) >= 2:
        closest = min(history, key=lambda g: abs(g - secret))
        print(f"  Closest guess: {closest}")
    print(f"{'=' * 35}\n")


def run() -> None:
    """Main program loop."""
    print("=" * 40)
    print("     Number Guessing Game")
    print(f"  I'm thinking of a number {RANGE_MIN}-{RANGE_MAX}")
    print("=" * 40)
    print()

    while True:
        won, secret, history = play_game()
        display_result(won, secret, history)

        again = input("Play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing!")
            break
        print()


if __name__ == "__main__":
    run()
