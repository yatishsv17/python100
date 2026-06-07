"""
Number Guessing Game - Simple Version
=======================================

WHAT THIS PROGRAM DOES (Flow):
1. Generate a random number between 1 and 100
2. Ask user to choose difficulty (easy=10 attempts, hard=5)
3. Loop: ask user for a guess
4. If guess is correct → win
5. If guess is too high/low → give hint, decrement attempts
6. If attempts run out → lose, reveal number

INPUTS:
- Difficulty (str): 'easy' or 'hard'
- Number guesses (int): 1 to 100

OUTPUTS:
- Hints: "Too high" or "Too low" (console)
- Remaining attempts (console)
- Win/lose message (console)

SIDE EFFECTS:
- None

RULES:
- Secret number: 1-100 inclusive
- Easy: 10 attempts, Hard: 5 attempts

ASSUMPTIONS:
- User enters valid integers
- Binary search is optimal strategy

DEPENDENCIES:
- random (standard library)
"""

import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.\n")

secret = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

while attempts > 0:
    print(f"\nYou have {attempts} attempts remaining.")
    guess = int(input("Make a guess: "))

    if guess == secret:
        print(f"You got it! The answer was {secret}.")
        break
    elif guess < secret:
        print("Too low.")
    else:
        print("Too high.")

    attempts -= 1

    if attempts == 0:
        print(f"\nYou've run out of guesses. The number was {secret}.")
