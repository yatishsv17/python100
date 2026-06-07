"""
Quiz Main - Production Version (Entry Point)
===============================================

WHAT THIS PROGRAM DOES (Flow):
1. Import question data from 12_quiz_data
2. Import Question model from 12_quiz_question_model
3. Import QuizBrain from 12_quiz_brain
4. Convert question data dicts → Question objects (question_bank)
5. Create QuizBrain with the question_bank
6. Run quiz loop: while questions remain, present next question
7. Display final score with percentage and performance feedback

INPUTS:
- QUESTION_DATA from 12_quiz_data.py
- User answers during quiz

OUTPUTS:
- Welcome message (console)
- Questions with feedback (console)
- Final score, percentage, performance feedback (console)

SIDE EFFECTS:
- None

RULES:
- Questions processed sequentially
- Final score with performance tier feedback

ASSUMPTIONS:
- All quiz modules are in the same directory
- Question data is properly formatted

DEPENDENCIES:
- 12_quiz_data (QUESTION_DATA)
- 12_quiz_question_model (Question)
- 12_quiz_brain (QuizBrain)
"""

from quiz_data import QUESTION_DATA
from quiz_question_model import Question
from quiz_brain import QuizBrain

# Note: The above imports use short names. If running from a different directory,
# you may need to adjust. Run this file from within the 12_quiz folder:
#   cd 12_quiz && python 12_quiz_main.py
# Or rename imports to match the file naming convention.


def create_question_bank(data: list[dict]) -> list[Question]:
    """Convert raw question data to Question objects.

    Args:
        data: List of dicts with "question" and "answer" keys.

    Returns:
        List of Question objects.
    """
    bank = []
    for item in data:
        q = Question(item["question"], item["answer"])
        bank.append(q)
    return bank


def get_performance_feedback(percentage: float) -> str:
    """Return performance feedback based on quiz percentage.

    Args:
        percentage: Score as a percentage.

    Returns:
        Feedback string.
    """
    if percentage == 100:
        return "Perfect score! Outstanding!"
    if percentage >= 80:
        return "Excellent work!"
    if percentage >= 60:
        return "Good job, keep learning!"
    if percentage >= 40:
        return "Not bad, but there's room for improvement."
    return "Keep studying, you'll do better next time!"


def main() -> None:
    """Main entry point for the quiz application."""
    print("=" * 35)
    print("       Welcome to the Quiz!")
    print("=" * 35)

    question_bank = create_question_bank(QUESTION_DATA)
    quiz = QuizBrain(question_bank)

    print(f"You'll answer {len(question_bank)} questions.\n")

    while quiz.still_has_questions():
        quiz.next_question()

    score, total, percentage = quiz.get_final_score()

    print(f"\n{'=' * 35}")
    print(f"  Final Score: {score}/{total} ({percentage:.0f}%)")
    print(f"  {get_performance_feedback(percentage)}")
    print(f"{'=' * 35}\n")


if __name__ == "__main__":
    main()
