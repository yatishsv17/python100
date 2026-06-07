# Password Generator - Function Call Flow & Flow Diagram

## Simple Version Call Flow

```
Script Start
  └─> input() → int() nr_letters
  └─> input() → int() nr_symbols
  └─> input() → int() nr_numbers
  └─> [loop] random.choice(letters) → append to list
  └─> [loop] random.choice(symbols) → append to list
  └─> [loop] random.choice(numbers) → append to list
  └─> random.shuffle(password_list)
  └─> "".join(password_list)
  └─> print() password
Script End
```

## Production Version Call Flow

### Function Call Graph

```
run()
  ├─> print() welcome banner
  │
  ├─> get_non_negative_int("letters") → nr_letters
  │     └─> input().strip() → int() → validate >= 0
  │
  ├─> get_non_negative_int("symbols") → nr_symbols
  ├─> get_non_negative_int("numbers") → nr_numbers
  │
  ├─> Check total > 0
  │
  ├─> generate_password(nr_letters, nr_symbols, nr_numbers)
  │     ├─> secrets.choice(LETTERS) × nr_letters
  │     ├─> secrets.choice(SYMBOLS) × nr_symbols
  │     ├─> secrets.choice(DIGITS) × nr_numbers
  │     └─> Fisher-Yates shuffle with secrets.randbelow()
  │
  ├─> display_result(password, nr_letters, nr_symbols, nr_numbers)
  │     ├─> assess_strength(length, has_letters, has_symbols, has_numbers)
  │     └─> print() password, length, composition, strength
  │
  └─> input() generate another?
        └─> "yes" → loop back
        └─> else → break
```

## Mermaid Flow Diagram

```mermaid
flowchart TD
    A[Start] --> B[Get nr_letters]
    B --> C[Get nr_symbols]
    C --> D[Get nr_numbers]
    D --> E{Total > 0?}
    E -- No --> F[Error: need at least 1 char]
    F --> B
    E -- Yes --> G[Generate Password]
    G --> G1[Pick random letters]
    G1 --> G2[Pick random symbols]
    G2 --> G3[Pick random numbers]
    G3 --> G4[Fisher-Yates Shuffle]
    G4 --> H[Assess Strength]
    H --> I[Display Result]
    I --> J{Generate Another?}
    J -- Yes --> B
    J -- No --> K[End]
```

## Password Generation Detail

```mermaid
flowchart LR
    L["secrets.choice(LETTERS) × N"] --> POOL[Character Pool]
    S["secrets.choice(SYMBOLS) × N"] --> POOL
    D["secrets.choice(DIGITS) × N"] --> POOL
    POOL --> SHUFFLE["Fisher-Yates Shuffle"]
    SHUFFLE --> JOIN["''.join() → password"]
```
