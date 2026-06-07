"""
Hangman - Simple Version
=========================

WHAT THIS PROGRAM DOES (Flow):
1. Randomly select a word from a predefined list
2. Show blanks for each letter in the word
3. Ask user to guess a letter
4. If correct → reveal letter position(s)
5. If incorrect → lose a life, draw hangman
6. Repeat until word is guessed (win) or lives = 0 (lose)

INPUTS:
- Letter guesses (str): single alphabetic character (a-z)

OUTPUTS:
- Current word state with blanks and revealed letters (console)
- Hangman ASCII art stages (console)
- Remaining lives count (console)
- Win/lose message (console)

SIDE EFFECTS:
- None

RULES:
- 6 lives total
- Guess one letter at a time
- Case-insensitive

ASSUMPTIONS:
- English alphabet only (a-z)
- Single word per game

DEPENDENCIES:
- random (standard library)
"""

import random

WORD_LIST = [
    "python", "javascript", "hangman", "computer", "programming",
    "algorithm", "function", "variable", "keyboard", "monitor"
]

HANGMAN_STAGES = [
    """
      -----
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
          |
          |
          |
    =========
    """,
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

word = random.choice(WORD_LIST)
lives = 6
guessed_letters = []
display = ["_"] * len(word)

print("Welcome to Hangman!")
print(HANGMAN_STAGES[lives])

while lives > 0:
    print(f"\nWord: {' '.join(display)}")
    print(f"Lives: {lives}")
    print(f"Guessed: {', '.join(guessed_letters)}")

    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try again.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(f"Good guess! '{guess}' is in the word.")
        for i, letter in enumerate(word):
            if letter == guess:
                display[i] = guess
    else:
        lives -= 1
        print(f"Wrong! '{guess}' is not in the word.")
        print(HANGMAN_STAGES[lives])

    if "_" not in display:
        print(f"\nCongratulations! You guessed the word: {word}")
        break
else:
    print(f"\nGame Over! The word was: {word}")
