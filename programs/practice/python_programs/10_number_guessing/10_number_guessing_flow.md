# Number Guessing Game - Function Call Flow & Flow Diagram

## Simple Version Call Flow

```
Script Start
  └─> print() welcome
  └─> random.randint(1, 100) → secret
  └─> input().lower() → difficulty
  └─> Set attempts (10 or 5)
  └─> while attempts > 0:
  │     └─> print() attempts remaining
  │     └─> input() → int() → guess
  │     └─> if guess == secret → win, break
  │     └─> elif guess < secret → "Too low"
  │     └─> else → "Too high"
  │     └─> attempts -= 1
  │     └─> if attempts == 0 → lose
Script End
```

## Production Version Call Flow

### Function Call Graph

```
run()
  ├─> print() welcome banner
  │
  └─> [Main Loop]
        ├─> play_game()
        │     ├─> random.randint(RANGE_MIN, RANGE_MAX) → secret
        │     ├─> get_difficulty()
        │     │     └─> input().strip().lower()
        │     │     └─> DIFFICULTY_MAP[raw] → attempts
        │     │
        │     └─> [While attempts > 0]
        │           ├─> get_guess(guessed)
        │           │     └─> input() → int()
        │           │     └─> Validate range and duplicates
        │           ├─> guessed.add(guess)
        │           ├─> history.append(guess)
        │           └─> Compare: ==, <, >
        │                 ├─> correct → return (True, secret, history)
        │                 └─> hint + attempts -= 1
        │
        ├─> display_result(won, secret, history)
        │     ├─> Print win/lose message
        │     ├─> Print guess count and history
        │     └─> min(history, key=lambda ...) → closest guess
        │
        └─> input() play again?
```

## Mermaid Flow Diagram

```mermaid
flowchart TD
    A[Start] --> B[Generate Secret Number]
    B --> C[Get Difficulty]
    C --> D[Set Attempts]
    D --> E{Attempts > 0?}
    E -- No --> F[Display Lose Result]
    E -- Yes --> G[Get Guess]
    G --> H{Valid?}
    H -- No --> G
    H -- Yes --> I{Already Guessed?}
    I -- Yes --> G
    I -- No --> J{Guess == Secret?}
    J -- Yes --> K[Display Win Result]
    J -- No --> L{Guess < Secret?}
    L -- Yes --> M[Hint: Too Low]
    L -- No --> N[Hint: Too High]
    M --> O[Decrement Attempts]
    N --> O
    O --> E
    K --> P{Play Again?}
    F --> P
    P -- Yes --> B
    P -- No --> Q[End]
```
