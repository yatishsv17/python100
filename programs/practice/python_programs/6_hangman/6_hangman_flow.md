# Hangman - Function Call Flow & Flow Diagram

## Simple Version Call Flow

```
Script Start
  └─> random.choice(WORD_LIST) → word
  └─> Initialize display, lives, guessed_letters
  └─> while lives > 0:
  │     └─> print() word state, lives, guessed
  │     └─> input().lower().strip() → guess
  │     └─> Validate (single alpha, not duplicate)
  │     └─> if guess in word → update display[]
  │     └─> else → lives -= 1, print hangman art
  │     └─> if "_" not in display → print win, break
  └─> else → print game over
Script End
```

## Production Version Call Flow

### Function Call Graph

```
run()
  ├─> display_banner()
  │
  └─> [Game Loop]
        ├─> random.choice(WORD_LIST) → word
        ├─> HangmanGame(word)
        │     └─> __init__: set word, lives, guessed, display
        │
        ├─> [While not game.is_over]
        │     ├─> display_state(game)
        │     │     ├─> game.get_hangman_art() → HANGMAN_STAGES[lives]
        │     │     ├─> game.get_display_str() → " ".join(display)
        │     │     └─> sorted(game.guessed)
        │     │
        │     ├─> input() → raw guess
        │     └─> game.guess(raw)
        │           ├─> Validate (single alpha)
        │           ├─> Check already_guessed (set lookup)
        │           ├─> Add to self.guessed
        │           ├─> Check if letter in self.word
        │           │     ├─> Yes: update self.display[], correct_guesses++
        │           │     └─> No: lives--, incorrect_guesses++
        │           └─> Return result string
        │
        ├─> display_result(game)
        │     └─> Print win/lose, statistics
        │
        └─> input() play again?
```

## Mermaid Flow Diagram

```mermaid
flowchart TD
    A[Start] --> B[Select Random Word]
    B --> C[Initialize HangmanGame]
    C --> D[Display State]
    D --> E[Get Letter Guess]
    E --> F{Valid Letter?}
    F -- No --> G[Show Error]
    G --> D
    F -- Yes --> H{Already Guessed?}
    H -- Yes --> I[Show Duplicate Warning]
    I --> D
    H -- No --> J{Letter in Word?}
    J -- Yes --> K[Reveal Letter Positions]
    J -- No --> L[Decrement Lives]
    K --> M{Word Complete?}
    L --> N{Lives = 0?}
    M -- No --> D
    M -- Yes --> O[Display Win Result]
    N -- No --> D
    N -- Yes --> P[Display Lose Result]
    O --> Q{Play Again?}
    P --> Q
    Q -- Yes --> B
    Q -- No --> R[End]
```

## Class Interaction Diagram

```mermaid
classDiagram
    class HangmanGame {
        -str word
        -int lives
        -set guessed
        -list display
        -int correct_guesses
        -int incorrect_guesses
        +__init__(word)
        +guess(letter) str
        +is_won bool
        +is_lost bool
        +is_over bool
        +get_display_str() str
        +get_hangman_art() str
    }

    class run {
        calls display_banner()
        creates HangmanGame
        calls display_state()
        calls display_result()
    }

    run --> HangmanGame : creates & uses
```
