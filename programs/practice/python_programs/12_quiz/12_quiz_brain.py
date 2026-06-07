"""
Quiz Brain - Production Version
=================================

WHAT THIS PROGRAM DOES:
Manages quiz logic, question flow, scoring, and state tracking.
Provides a clean interface for administering quizzes.

INPUTS:
- question_list: List of Question objects
- User answers: Text answers to each question

OUTPUTS:
- Question text with number (console)
- Feedback for each answer (console)
- Score tracking (console)
- Final score with percentage (console)

SIDE EFFECTS:
- Modifies internal state (question_number, score)

RULES:
- Case-insensitive answer checking (delegated to Question.check_answer)
- Progress tracking with question numbers
- Empty answers rejected

ASSUMPTIONS:
- Question list contains valid Question objects

DEPENDENCIES:
- 12_quiz_question_model (Question class)
"""


class QuizBrain:
    """Manages quiz state and progression.

    Attributes:
        question_number: Current question index (0-based).
        score: Number of correct answers.
        question_list: List of Question objects.
    """

    def __init__(self, question_list: list) -> None:
        """Initialize the QuizBrain.

        Args:
            question_list: List of Question objects.
        """
        self.question_number: int = 0
        self.score: int = 0
        self.question_list = question_list

    def still_has_questions(self) -> bool:
        """Check if there are more questions to answer.

        Returns:
            True if questions remain.
        """
        return self.question_number < len(self.question_list)

    def next_question(self) -> None:
        """Present the next question and process the answer."""
        current = self.question_list[self.question_number]
        self.question_number += 1

        print(f"\nQ{self.question_number}/{len(self.question_list)}: {current.text}")
        user_answer = input("  Your answer: ").strip()

        if not user_answer:
            print("  Empty answer — marked incorrect.")
            print(f"  Correct answer: {current.answer}")
        elif current.check_answer(user_answer):
            self.score += 1
            print(f"  Correct! Score: {self.score}/{self.question_number}")
        else:
            print(f"  Incorrect. The answer was: {current.answer}")
            print(f"  Score: {self.score}/{self.question_number}")

    def get_final_score(self) -> tuple[int, int, float]:
        """Get the final score details.

        Returns:
            Tuple of (score, total, percentage).
        """
        total = len(self.question_list)
        percentage = (self.score / total) * 100 if total > 0 else 0
        return self.score, total, percentage
