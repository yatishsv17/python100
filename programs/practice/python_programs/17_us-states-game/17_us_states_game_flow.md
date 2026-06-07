# US States Game - Function Call Flow & Flow Diagram

## Simple Version Call Flow

```
Script Start
  └─> turtle.Screen() + addshape() + shape()
  └─> open(CSV) → csv.DictReader → states dict
  └─> while len(guessed) < 50:
  │     └─> screen.textinput() → answer
  │     └─> if "Exit" → break
  │     └─> if valid state and not guessed → write on map
  └─> Save missing states to CSV
  └─> print() final score
  └─> screen.exitonclick()
Script End
```

## Production Version Call Graph

```
run()
  ├─> Validate CSV_PATH and IMAGE_PATH exist
  │
  ├─> load_states()
  │     └─> csv.DictReader → {name: (x, y)} dict
  │
  ├─> load_high_score()
  │     └─> HIGH_SCORE_PATH.read_text() → int
  │
  ├─> turtle.Screen() setup + addshape + shape
  │
  ├─> time.time() → start_time
  │
  ├─> [Game Loop: while guessed < total]
  │     ├─> screen.textinput() → answer
  │     ├─> if None or "exit" → break
  │     ├─> answer.strip().title() → cleaned
  │     └─> if valid and not guessed:
  │           ├─> guessed.add(cleaned)
  │           └─> write_state_on_map(name, x, y)
  │                 └─> Turtle → hideturtle, penup, goto, write
  │
  ├─> Calculate elapsed time, score, missing
  │
  ├─> save_states_to_learn(missing)
  │     └─> csv.writer → writerow for each state
  │
  ├─> save_high_score(score) if new high
  │     └─> Path.write_text(str(score))
  │
  ├─> print() results summary
  │
  └─> screen.exitonclick()
```

## Mermaid Flow Diagram

```mermaid
flowchart TD
    A[Start] --> B[Validate Files]
    B --> C{Files OK?}
    C -- No --> D[Error Exit]
    C -- Yes --> E[Load States from CSV]
    E --> F[Load High Score]
    F --> G[Setup Map Display]
    G --> H[Start Timer]
    H --> I[Show Text Input Dialog]
    I --> J{Answer?}
    J -- None/Exit --> K[End Game]
    J -- Text --> L[Clean: strip + title]
    L --> M{Valid State?}
    M -- No --> I
    M -- Yes --> N{Already Guessed?}
    N -- Yes --> I
    N -- No --> O[Add to Guessed Set]
    O --> P[Write Name on Map]
    P --> Q{All 50 Guessed?}
    Q -- No --> I
    Q -- Yes --> K
    K --> R[Save States to Learn]
    R --> S[Update High Score]
    S --> T[Display Summary]
    T --> U[Exit on Click]
```
