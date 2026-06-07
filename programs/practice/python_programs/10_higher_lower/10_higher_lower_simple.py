"""
Higher Lower Game - Simple Version
====================================

WHAT THIS PROGRAM DOES (Flow):
1. Define a data set of items with follower counts
2. Pick two random different items
3. Show both items (A and B) to the user
4. Ask user to guess which has more followers
5. Reveal the answer and update score
6. Repeat for 10 questions
7. Show final score

INPUTS:
- User choice (str): 'A' or 'B' for each comparison

OUTPUTS:
- Item names for comparison (console)
- Actual follower counts after each guess (console)
- Score updates (console)
- Final score with percentage (console)

SIDE EFFECTS:
- None

RULES:
- 10 questions per round
- Choose which item has more followers
- Score is count of correct guesses

ASSUMPTIONS:
- Data items have numeric follower counts
- User understands A/B format

DEPENDENCIES:
- random (standard library)
"""

import random

DATA = [
    {"name": "Instagram", "followers": 500},
    {"name": "Twitter/X", "followers": 400},
    {"name": "TikTok", "followers": 350},
    {"name": "YouTube", "followers": 300},
    {"name": "Facebook", "followers": 250},
    {"name": "Snapchat", "followers": 200},
    {"name": "LinkedIn", "followers": 180},
    {"name": "Pinterest", "followers": 150},
    {"name": "Reddit", "followers": 120},
    {"name": "Twitch", "followers": 100},
    {"name": "Discord", "followers": 90},
    {"name": "WhatsApp", "followers": 80},
    {"name": "Telegram", "followers": 70},
    {"name": "Signal", "followers": 40},
    {"name": "Mastodon", "followers": 10},
]

TOTAL_QUESTIONS = 10

print("Welcome to the Higher Lower Game!")
print("Guess which platform has more followers (in millions).\n")

score = 0

for q in range(1, TOTAL_QUESTIONS + 1):
    a, b = random.sample(DATA, 2)

    print(f"Question {q}/{TOTAL_QUESTIONS}")
    print(f"  A: {a['name']}")
    print(f"  B: {b['name']}")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    if guess not in ("A", "B"):
        print("Invalid choice! Skipping.\n")
        continue

    if guess == "A":
        correct = a["followers"] >= b["followers"]
    else:
        correct = b["followers"] >= a["followers"]

    print(f"  A: {a['name']} = {a['followers']}M followers")
    print(f"  B: {b['name']} = {b['followers']}M followers")

    if correct:
        score += 1
        print(f"  Correct! Score: {score}\n")
    else:
        print(f"  Wrong! Score: {score}\n")

print(f"Final Score: {score}/{TOTAL_QUESTIONS} ({score / TOTAL_QUESTIONS * 100:.0f}%)")
