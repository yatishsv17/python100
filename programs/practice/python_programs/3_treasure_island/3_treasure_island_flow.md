# Treasure Island - Function Call Flow & Flow Diagram

## Simple Version Call Flow

Linear nested-if script:

```
Script Start
  └─> print() ASCII art + welcome
  └─> input().lower() → choice1
  └─> if "left":
  │     └─> input().lower() → choice2
  │     └─> if "wait":
  │           └─> input().lower() → choice3
  │           └─> if "yellow" → Win
  │           └─> elif "red" → Lose
  │           └─> elif "blue" → Lose
  │           └─> else → Lose
  │     └─> else → Lose (swim)
  └─> else → Lose (right)
Script End
```

## Production Version Call Flow

### Entry Point
```
__main__ guard
  └─> run()
```

### Function Call Graph

```
run()
  ├─> display_banner()
  │     └─> print()
  │
  ├─> play_game()
  │     └─> [for each scene_key in GAME_SEQUENCE]
  │           ├─> get_choice(scenario)
  │           │     └─> input().strip().lower()
  │           │     └─> [validate against scenario["options"]]
  │           └─> Check result["outcome"]
  │                 ├─> "lose" → return (False, choices)
  │                 ├─> "win"  → return (True, choices)
  │                 └─> "continue" → next iteration
  │
  ├─> display_summary(won, choices)
  │     └─> print() path, decisions, result
  │
  └─> input() play again?
        └─> "yes" → loop back to play_game()
        └─> else  → break
```

## Mermaid Game Flow Diagram

```mermaid
flowchart TD
    A[Start Game] --> B[Crossroad: Left or Right?]
    B -- right --> C[Game Over: Fell into hole]
    B -- left --> D[Lake: Wait or Swim?]
    D -- swim --> E[Game Over: Attacked by trout]
    D -- wait --> F[Doors: Red, Yellow, or Blue?]
    F -- red --> G[Game Over: Room of fire]
    F -- blue --> H[Game Over: Room of beasts]
    F -- yellow --> I[Victory: Treasure found!]

    C --> J{Play Again?}
    E --> J
    G --> J
    H --> J
    I --> J
    J -- yes --> A
    J -- no --> K[End]
```

## Production Code Flow

```mermaid
flowchart TD
    START[run] --> BANNER[display_banner]
    BANNER --> LOOP[Game Loop]
    LOOP --> PG[play_game]
    PG --> SCENE["For each scene in GAME_SEQUENCE"]
    SCENE --> GC["get_choice(scenario)"]
    GC --> VALID{Valid choice?}
    VALID -- No --> GC
    VALID -- Yes --> CHECK{Outcome?}
    CHECK -- lose --> RET_L["Return (False, choices)"]
    CHECK -- win --> RET_W["Return (True, choices)"]
    CHECK -- continue --> SCENE
    RET_L --> SUMMARY[display_summary]
    RET_W --> SUMMARY
    SUMMARY --> AGAIN{Play again?}
    AGAIN -- yes --> LOOP
    AGAIN -- no --> END[End]
```
