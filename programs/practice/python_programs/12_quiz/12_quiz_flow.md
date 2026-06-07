# Quiz Game - Function Call Flow & Flow Diagram

## Simple Version Call Flow

```
Script Start
  └─> print() welcome
  └─> for i, q in enumerate(QUESTION_DATA, 1):
  │     └─> print() question number and text
  │     └─> input() → user_answer
  │     └─> Compare .lower() of user vs correct
  │     └─> Update score, print feedback
  └─> print() final score and percentage
Script End
```

## Production Version Call Flow

### Entry Point
```
__main__ guard in 12_quiz_main.py
  └─> main()
```

### Module Import Chain
```
12_quiz_main.py
  ├─> from quiz_data import QUESTION_DATA
  ├─> from quiz_question_model import Question
  └─> from quiz_brain import QuizBrain
```

### Function Call Graph

```
main()
  ├─> print() welcome banner
  │
  ├─> create_question_bank(QUESTION_DATA)
  │     └─> for item in data:
  │           └─> Question(item["question"], item["answer"])
  │                 └─> __init__: self.text, self.answer
  │     └─> return list of Question objects
  │
  ├─> QuizBrain(question_bank)
  │     └─> __init__: question_number=0, score=0, question_list
  │
  ├─> while quiz.still_has_questions():
  │     │   └─> self.question_number < len(self.question_list)
  │     │
  │     └─> quiz.next_question()
  │           ├─> Get current Question from list
  │           ├─> Increment question_number
  │           ├─> print() question text
  │           ├─> input() → user_answer
  │           └─> current.check_answer(user_answer)
  │                 └─> strip().lower() comparison
  │
  ├─> quiz.get_final_score()
  │     └─> return (score, total, percentage)
  │
  └─> get_performance_feedback(percentage)
        └─> Tier lookup → feedback string
```

## Mermaid Flow Diagram

```mermaid
flowchart TD
    A[Start: main] --> B[Import Modules]
    B --> C["create_question_bank(QUESTION_DATA)"]
    C --> D["Create Question objects from dicts"]
    D --> E["QuizBrain(question_bank)"]
    E --> F{still_has_questions?}
    F -- Yes --> G[next_question]
    G --> H[Display Question]
    H --> I[Get User Answer]
    I --> J{check_answer}
    J -- Correct --> K[Score + 1]
    J -- Incorrect --> L[Show Correct Answer]
    K --> M[Show Score]
    L --> M
    M --> F
    F -- No --> N[get_final_score]
    N --> O[get_performance_feedback]
    O --> P[Display Final Results]
    P --> Q[End]
```

## Module Dependency Diagram

```mermaid
graph TD
    MAIN[12_quiz_main.py] --> DATA[12_quiz_data.py]
    MAIN --> MODEL[12_quiz_question_model.py]
    MAIN --> BRAIN[12_quiz_brain.py]
    BRAIN --> MODEL

    subgraph "Data Layer"
        DATA
    end

    subgraph "Model Layer"
        MODEL
    end

    subgraph "Logic Layer"
        BRAIN
    end

    subgraph "Presentation Layer"
        MAIN
    end
```

## Class Interaction Diagram

```mermaid
classDiagram
    class Question {
        +str text
        +str answer
        +check_answer(user_answer) bool
        +__repr__() str
        +__str__() str
    }

    class QuizBrain {
        +int question_number
        +int score
        +list question_list
        +still_has_questions() bool
        +next_question() void
        +get_final_score() tuple
    }

    QuizBrain --> Question : uses list of
    QuizBrain ..> Question : calls check_answer()
```
