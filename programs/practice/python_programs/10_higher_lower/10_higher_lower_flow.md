# Higher Lower Game - Function Call Flow & Flow Diagram

## Simple Version Call Flow

```
Script Start
  └─> print() welcome
  └─> for q in range(1, 11):
  │     └─> random.sample(DATA, 2) → a, b
  │     └─> print() item A and B names
  │     └─> input().upper() → guess
  │     └─> Compare followers
  │     └─> print() actual counts, correct/wrong, score
  └─> print() final score and percentage
Script End
```

## Production Version Call Flow

### Function Call Graph

```
run()
  ├─> print() welcome banner
  │
  └─> [Main Loop]
        ├─> play_round()
        │     └─> for q in range(1, TOTAL_QUESTIONS + 1):
        │           ├─> get_two_items()
        │           │     └─> random.sample(DATA, 2)
        │           ├─> print() items with categories
        │           ├─> get_user_choice()
        │           │     └─> input().strip().upper()
        │           │     └─> validate in ("A", "B")
        │           ├─> check_answer(choice, item_a, item_b)
        │           │     └─> Compare followers based on choice
        │           └─> print() results, update score
        │
        ├─> display_final_results(score)
        │     ├─> Calculate percentage
        │     ├─> get_performance_feedback(score, total)
        │     │     └─> Tier lookup based on percentage
        │     └─> print() score, percentage, feedback
        │
        └─> input() play again?
```

## Mermaid Flow Diagram

```mermaid
flowchart TD
    A[Start] --> B[Display Banner]
    B --> C["Question Loop (q = 1 to 10)"]
    C --> D[Pick 2 Random Items]
    D --> E[Display Items A and B]
    E --> F[Get User Choice: A or B]
    F --> G{Valid?}
    G -- No --> F
    G -- Yes --> H[Check Answer]
    H --> I{Correct?}
    I -- Yes --> J[Score + 1]
    I -- No --> K[No score change]
    J --> L[Display Results]
    K --> L
    L --> M{More Questions?}
    M -- Yes --> C
    M -- No --> N[Display Final Results]
    N --> O[Performance Feedback]
    O --> P{Play Again?}
    P -- Yes --> C
    P -- No --> Q[End]
```
