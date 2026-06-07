# Caesar Cipher - Function Call Flow & Flow Diagram

## Simple Version Call Flow

```
Script Start
  └─> input() → direction
  └─> input() → text
  └─> input() → int() → shift
  └─> shift % 26
  └─> caesar(text, shift, direction)
  │     └─> if decrypt: shift *= -1
  │     └─> for each char:
  │           ├─> if alpha: index → shift → new_index → new_char
  │           └─> else: preserve char
  └─> print() result
Script End
```

## Production Version Call Flow

### Function Call Graph

```
run()
  ├─> print() welcome banner
  │
  ├─> get_direction()
  │     └─> input().strip().lower()
  │     └─> validate in ("encrypt", "decrypt")
  │
  ├─> get_text()
  │     └─> input().strip()
  │     └─> validate non-empty
  │
  ├─> get_shift()
  │     └─> input().strip() → int()
  │     └─> validate >= 0
  │
  ├─> caesar_cipher(text, shift, direction)
  │     ├─> shift % ALPHABET_SIZE
  │     ├─> if decrypt: shift = -shift
  │     └─> for each char:
  │           ├─> char.lower() in ALPHABET?
  │           │     ├─> ALPHABET.index(char.lower())
  │           │     ├─> (index + shift) % ALPHABET_SIZE
  │           │     └─> ALPHABET[new_index]
  │           └─> else: append unchanged
  │
  ├─> display_result(direction, original, result, shift)
  │     └─> print() operation, shift, texts, char count
  │
  └─> input() process another?
```

## Mermaid Flow Diagram

```mermaid
flowchart TD
    A[Start] --> B[Get Direction]
    B --> C[Get Text Message]
    C --> D[Get Shift Number]
    D --> E[Normalize Shift: shift % 26]
    E --> F{Direction?}
    F -- encrypt --> G[Keep shift positive]
    F -- decrypt --> H[Negate shift]
    G --> I[Process Characters]
    H --> I
    I --> J{Next Character}
    J --> K{Is Alphabetic?}
    K -- Yes --> L[Find index in ALPHABET]
    L --> M["new_index = (index + shift) % 26"]
    M --> N[Get new character, preserve case]
    N --> O[Append to result]
    K -- No --> P[Append unchanged]
    P --> O
    O --> Q{More characters?}
    Q -- Yes --> J
    Q -- No --> R[Display Result]
    R --> S{Process Another?}
    S -- Yes --> B
    S -- No --> T[End]
```

## Character Shifting Detail

```mermaid
flowchart LR
    C[char 'H'] --> LOW["lower() → 'h'"]
    LOW --> IDX["index('h') → 7"]
    IDX --> SHIFT["(7 + 3) % 26 → 10"]
    SHIFT --> NEW["ALPHABET[10] → 'k'"]
    NEW --> CASE["isupper? → 'K'"]
```
