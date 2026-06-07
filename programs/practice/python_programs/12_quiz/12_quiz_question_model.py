"""
Quiz Question Model - Production Version
==========================================

WHAT THIS PROGRAM DOES:
Defines the Question class representing a single quiz question
with its text and correct answer. Provides methods to check answers.

INPUTS:
- question_text (str): The question string
- correct_answer (str): The correct answer string
- user_answer (str): The user's answer for validation

OUTPUTS:
- Boolean result of answer checking (True/False)
- String representation of the question

SIDE EFFECTS:
- None (pure data class)

RULES:
- Case-insensitive matching
- Whitespace stripped from answers
- Empty answers are rejected (return False)

ASSUMPTIONS:
- Text-based answers only
- Case-insensitive matching is appropriate

DEPENDENCIES:
- None
"""


class Question:
    """Represents a single quiz question.

    Attributes:
        text: The question text.
        answer: The correct answer.
    """

    def __init__(self, text: str, answer: str) -> None:
        """Initialize a Question.

        Args:
            text: The question text.
            answer: The correct answer.
        """
        self.text = text
        self.answer = answer

    def check_answer(self, user_answer: str) -> bool:
        """Check if the user's answer is correct.

        Args:
            user_answer: The answer provided by the user.

        Returns:
            True if the answer matches (case-insensitive, stripped).
        """
        if not user_answer or not user_answer.strip():
            return False
        return user_answer.strip().lower() == self.answer.strip().lower()

    def __repr__(self) -> str:
        """Return a developer-friendly string representation."""
        return f"Question(text='{self.text[:30]}...', answer='{self.answer}')"

    def __str__(self) -> str:
        """Return the question text."""
        return self.text
