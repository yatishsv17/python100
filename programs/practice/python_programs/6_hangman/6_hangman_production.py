"""
Hangman - Production Version
==============================

WHAT THIS PROGRAM DOES (Flow):
1. Display welcome banner
2. Select random word from word list
3. Initialize game state: lives=6, empty guessed set, blank display
4. Game loop:
   a. Show hangman art, word state, lives, guessed letters
   b. Prompt for letter guess (validated: single alpha char, not repeated)
   c. Check if letter is in the word
   d. Update display or decrement lives
   e. Check win/lose conditions
5. Display final result with statistics
6. Offer replay

INPUTS:
- Letter guesses (str): single alphabetic character a-z (case-insensitive)
- Play again (str): 'yes' or 'no'

OUTPUTS:
- Hangman ASCII art at each stage (console)
- Word state with blanks and revealed letters (console)
- Remaining lives, guessed letters (console)
- Win/lose message with game statistics (console)

SIDE EFFECTS:
- None

RULES:
- 6 lives total
- Only single alphabetic characters accepted
- Duplicate guesses are rejected without penalty
- Case-insensitive matching

ASSUMPTIONS:
- English alphabet only (a-z)
- ASCII terminal for hangman art display

DEPENDENCIES:
- random (standard library)
"""

import random
from typing import Optional

WORD_LIST = [
    "python", "javascript", "hangman", "computer", "programming",
    "algorithm", "function", "variable", "keyboard", "monitor",
    "developer", "interface", "database", "network", "terminal",
]

MAX_LIVES = 6

HANGMAN_STAGES = [
    # 0 lives left (dead)
    """
      -----
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,
    # 1 life left
    """
      -----
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    # 2 lives left
    """
      -----
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    # 3 lives left
    """
      -----
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    # 4 lives left
    """
      -----
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    # 5 lives left
    """
      -----
      |   |
      O   |
          |
          |
          |
    =========
    """,
    # 6 lives left (start)
    """
      -----
      |   |
          |
          |
          |
          |
    =========
    """,
]


class HangmanGame:
    """Manages a single game of Hangman.

    Attributes:
        word: The secret word to guess.
        lives: Remaining lives.
        guessed: Set of guessed letters.
        display: List showing revealed letters and blanks.
        correct_guesses: Count of correct unique guesses.
        incorrect_guesses: Count of incorrect guesses.
    """

    def __init__(self, word: str) -> None:
        """Initialize a new game.

        Args:
            word: The secret word.
        """
        self.word = word.lower()
        self.lives = MAX_LIVES
        self.guessed: set[str] = set()
        self.display = ["_"] * len(self.word)
        self.correct_guesses = 0
        self.incorrect_guesses = 0

    def guess(self, letter: str) -> str:
        """Process a letter guess.

        Args:
            letter: A single lowercase letter.

        Returns:
            Result message: 'correct', 'incorrect', 'already_guessed', or 'invalid'.
        """
        letter = letter.lower().strip()

        if len(letter) != 1 or not letter.isalpha():
            return "invalid"

        if letter in self.guessed:
            return "already_guessed"

        self.guessed.add(letter)

        if letter in self.word:
            self.correct_guesses += 1
            for i, char in enumerate(self.word):
                if char == letter:
                    self.display[i] = letter
            return "correct"
        else:
            self.incorrect_guesses += 1
            self.lives -= 1
            return "incorrect"

    @property
    def is_won(self) -> bool:
        """Check if the word has been fully guessed."""
        return "_" not in self.display

    @property
    def is_lost(self) -> bool:
        """Check if all lives are lost."""
        return self.lives <= 0

    @property
    def is_over(self) -> bool:
        """Check if the game is over."""
        return self.is_won or self.is_lost

    def get_display_str(self) -> str:
        """Get the current word display as a string."""
        return " ".join(self.display)

    def get_hangman_art(self) -> str:
        """Get the current hangman ASCII art."""
        return HANGMAN_STAGES[self.lives]


def display_banner() -> None:
    """Display the welcome banner."""
    print("=" * 35)
    print("       HANGMAN")
    print("=" * 35)
    print()


def display_state(game: HangmanGame) -> None:
    """Display current game state.

    Args:
        game: The current HangmanGame instance.
    """
    print(game.get_hangman_art())
    print(f"  Word:    {game.get_display_str()}")
    print(f"  Lives:   {'❤️ ' * game.lives}({'.' * (MAX_LIVES - game.lives)})")
    sorted_guessed = sorted(game.guessed)
    print(f"  Guessed: {', '.join(sorted_guessed) if sorted_guessed else 'None'}")


def display_result(game: HangmanGame) -> None:
    """Display final game result with statistics.

    Args:
        game: The completed HangmanGame instance.
    """
    print("\n--- Game Result ---")
    if game.is_won:
        print(f"  Congratulations! You guessed: {game.word}")
    else:
        print(game.get_hangman_art())
        print(f"  Game Over! The word was: {game.word}")
    print(f"  Correct guesses:   {game.correct_guesses}")
    print(f"  Incorrect guesses: {game.incorrect_guesses}")
    print(f"  Total guesses:     {len(game.guessed)}")
    unique_letters = len(set(game.word))
    print(f"  Unique letters in word: {unique_letters}")
    print("-------------------\n")


def run() -> None:
    """Main program loop."""
    display_banner()

    while True:
        word = random.choice(WORD_LIST)
        game = HangmanGame(word)

        while not game.is_over:
            display_state(game)
            raw = input("\n  Guess a letter: ").strip()
            result = game.guess(raw)

            if result == "invalid":
                print("  Please enter a single letter (a-z).")
            elif result == "already_guessed":
                print(f"  You already guessed '{raw}'. Try a different letter.")
            elif result == "correct":
                print(f"  Good guess! '{raw}' is in the word!")
            elif result == "incorrect":
                print(f"  Wrong! '{raw}' is not in the word.")

        display_result(game)

        again = input("Play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing Hangman!")
            break
        print()


if __name__ == "__main__":
    run()
