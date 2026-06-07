"""
Rock Paper Scissors - Simple Version
======================================

WHAT THIS PROGRAM DOES (Flow):
1. Ask user to choose rock, paper, or scissors
2. Computer randomly picks rock, paper, or scissors
3. Compare choices and determine winner
4. Print result

INPUTS:
- User choice (str): 'rock', 'paper', or 'scissors'

OUTPUTS:
- User's choice and computer's choice (console)
- Game result: win, lose, or tie (console)

SIDE EFFECTS:
- None

RULES:
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
- Same choice = Tie

ASSUMPTIONS:
- Single round per execution
- Computer choice is random

DEPENDENCIES:
- random (standard library)
"""

import random

choices = ["rock", "paper", "scissors"]
emojis = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}

user_choice = input("Choose rock, paper, or scissors: ").lower()

if user_choice not in choices:
    print("Invalid choice! Please choose rock, paper, or scissors.")
else:
    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice} {emojis[user_choice]}")
    print(f"Computer chose: {computer_choice} {emojis[computer_choice]}\n")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        print("You win!")
    else:
        print("Computer wins!")
