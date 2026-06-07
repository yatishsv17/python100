"""
Quiz Game - Simple Version (All-in-One)
=========================================

WHAT THIS PROGRAM DOES (Flow):
1. Define a list of question dictionaries (question + answer)
2. Loop through each question:
   a. Display question number and text
   b. Get user answer
   c. Compare answer (case-insensitive)
   d. Show correct/incorrect feedback
   e. Update score
3. Display final score

INPUTS:
- User answers (str): text answers to each question (case-insensitive)

OUTPUTS:
- Question text with number (console)
- Correct/incorrect feedback (console)
- Correct answer if wrong (console)
- Running score (console)
- Final score (console)

SIDE EFFECTS:
- None

RULES:
- 10 questions covering various topics
- Case-insensitive answer matching
- Score tracked throughout

ASSUMPTIONS:
- Questions have definitive text answers
- Simple text matching is sufficient

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

print("Welcome to the Quiz!")
print(f"You'll answer {len(QUESTION_DATA)} questions.\n")

score = 0

for i, q in enumerate(QUESTION_DATA, 1):
    print(f"Q{i}: {q['question']}")
    user_answer = input("Your answer: ").strip()

    if user_answer.lower() == q["answer"].lower():
        score += 1
        print(f"  Correct! Score: {score}/{i}\n")
    else:
        print(f"  Incorrect. The answer was: {q['answer']}")
        print(f"  Score: {score}/{i}\n")

print(f"Final Score: {score}/{len(QUESTION_DATA)}")
percentage = (score / len(QUESTION_DATA)) * 100
print(f"Percentage: {percentage:.0f}%")
