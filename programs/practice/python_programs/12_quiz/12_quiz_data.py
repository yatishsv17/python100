"""
Quiz Data Module - Production Version
=======================================

WHAT THIS PROGRAM DOES:
Provides the quiz question data as a list of dictionaries.
Each dictionary has a "question" key and an "answer" key.
This module is imported by 12_quiz_main.py.

INPUTS:
- None (data module)

OUTPUTS:
- QUESTION_DATA: List of dicts with "question" and "answer" keys

RULES:
- Each dict must have "question" and "answer" keys
- Fixed set of 10 questions
- Single correct answer per question, text-based

ASSUMPTIONS:
- Questions are factual with definitive answers
- Answers are unambiguous

DEPENDENCIES:
- None
"""

QUESTION_DATA = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What planet is known as the Red Planet?", "answer": "Mars"},
    {"question": "What is the largest ocean on Earth?", "answer": "Pacific"},
    {"question": "Who wrote 'Romeo and Juliet'?", "answer": "Shakespeare"},
    {"question": "What is the chemical symbol for water?", "answer": "H2O"},
    {"question": "How many continents are there?", "answer": "7"},
    {"question": "What is the speed of light in km/s (approx)?", "answer": "300000"},
    {"question": "What language is primarily spoken in Brazil?", "answer": "Portuguese"},
    {"question": "What is the largest mammal?", "answer": "Blue Whale"},
]
