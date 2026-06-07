"""
Higher Lower Game - Production Version
========================================

WHAT THIS PROGRAM DOES (Flow):
1. Display welcome banner with rules
2. For each of 10 questions:
   a. Pick two random distinct items from the data set
   b. Display item A and item B names
   c. Prompt user for 'A' or 'B' (validated)
   d. Compare follower counts
   e. Reveal actual counts and whether guess was correct
   f. Update score
3. After 10 questions:
   a. Show final score and percentage
   b. Provide performance feedback
   c. Offer to play again

INPUTS:
- User choice (str): 'A' or 'B' per question (case-insensitive)
- Play again (str): 'yes' or 'no'

OUTPUTS:
- Comparison items per question (console)
- Actual follower counts after each guess (console)
- Running score (console)
- Final score, percentage, performance feedback (console)

SIDE EFFECTS:
- None

RULES:
- 10 questions per round
- Correct guess = +1 point
- Performance tiers: Perfect, Excellent, Good, Average, Needs Practice

ASSUMPTIONS:
- Data has valid numeric follower values
- User understands A/B choice format

DEPENDENCIES:
- random (standard library)
"""

import random


DATA = [
    {"name": "Instagram", "followers": 500, "category": "Social Media"},
    {"name": "Twitter/X", "followers": 400, "category": "Social Media"},
    {"name": "TikTok", "followers": 350, "category": "Social Media"},
    {"name": "YouTube", "followers": 300, "category": "Video Platform"},
    {"name": "Facebook", "followers": 250, "category": "Social Media"},
    {"name": "Snapchat", "followers": 200, "category": "Social Media"},
    {"name": "LinkedIn", "followers": 180, "category": "Professional"},
    {"name": "Pinterest", "followers": 150, "category": "Social Media"},
    {"name": "Reddit", "followers": 120, "category": "Forum"},
    {"name": "Twitch", "followers": 100, "category": "Streaming"},
    {"name": "Discord", "followers": 90, "category": "Communication"},
    {"name": "WhatsApp", "followers": 80, "category": "Messaging"},
    {"name": "Telegram", "followers": 70, "category": "Messaging"},
    {"name": "Signal", "followers": 40, "category": "Messaging"},
    {"name": "Mastodon", "followers": 10, "category": "Social Media"},
]

TOTAL_QUESTIONS = 10


def get_two_items() -> tuple[dict, dict]:
    """Pick two random distinct items from DATA.

    Returns:
        Tuple of two different item dictionaries.
    """
    return tuple(random.sample(DATA, 2))


def get_user_choice() -> str:
    """Prompt for a valid A or B choice.

    Returns:
        'A' or 'B'.
    """
    while True:
        raw = input("  Who has more followers? Type 'A' or 'B': ").strip().upper()
        if raw in ("A", "B"):
            return raw
        print("  Invalid choice. Please type 'A' or 'B'.")


def check_answer(choice: str, item_a: dict, item_b: dict) -> bool:
    """Check if the user's choice is correct.

    Args:
        choice: 'A' or 'B'.
        item_a: First item dictionary.
        item_b: Second item dictionary.

    Returns:
        True if the chosen item has more or equal followers.
    """
    if choice == "A":
        return item_a["followers"] >= item_b["followers"]
    return item_b["followers"] >= item_a["followers"]


def get_performance_feedback(score: int, total: int) -> str:
    """Get performance feedback based on score percentage.

    Args:
        score: Number of correct answers.
        total: Total number of questions.

    Returns:
        Feedback string.
    """
    pct = (score / total) * 100
    if pct == 100:
        return "Perfect! You're a social media expert!"
    if pct >= 80:
        return "Excellent! You really know your platforms!"
    if pct >= 60:
        return "Good job! You know quite a bit."
    if pct >= 40:
        return "Average. Keep learning!"
    return "Needs practice. Try again!"


def play_round() -> int:
    """Play one round of 10 questions.

    Returns:
        The score for this round.
    """
    score = 0

    for q in range(1, TOTAL_QUESTIONS + 1):
        item_a, item_b = get_two_items()

        print(f"\n--- Question {q}/{TOTAL_QUESTIONS} ---")
        print(f"  A: {item_a['name']} ({item_a['category']})")
        print(f"  B: {item_b['name']} ({item_b['category']})")

        choice = get_user_choice()
        correct = check_answer(choice, item_a, item_b)

        print(f"\n  A: {item_a['name']} = {item_a['followers']}M followers")
        print(f"  B: {item_b['name']} = {item_b['followers']}M followers")

        if correct:
            score += 1
            print(f"  Correct! Score: {score}/{q}")
        else:
            print(f"  Wrong! Score: {score}/{q}")

    return score


def display_final_results(score: int) -> None:
    """Display final round results.

    Args:
        score: Total correct answers.
    """
    pct = (score / TOTAL_QUESTIONS) * 100
    feedback = get_performance_feedback(score, TOTAL_QUESTIONS)

    print(f"\n{'=' * 35}")
    print(f"  Final Score: {score}/{TOTAL_QUESTIONS} ({pct:.0f}%)")
    print(f"  {feedback}")
    print(f"{'=' * 35}\n")


def run() -> None:
    """Main program loop."""
    print("=" * 40)
    print("     Higher Lower Game")
    print("  Guess which has more followers!")
    print("=" * 40)

    while True:
        score = play_round()
        display_final_results(score)

        again = input("Play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    run()
