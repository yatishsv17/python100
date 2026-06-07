# Tip Calculator - Function Call Flow & Flow Diagram

## Simple Version Call Flow

Linear script — no function calls:

```
Script Start
  └─> print() welcome
  └─> input() → float() bill
  └─> input() → int() tip percentage
  └─> input() → int() number of people
  └─> Calculate tip_amount, total, per_person
  └─> print() result
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
  ├─> print()  (welcome banner)
  │
  ├─> get_bill_amount()
  │     └─> [loop up to MAX_RETRIES]
  │           ├─> input()
  │           ├─> float()  (may raise ValueError)
  │           └─> validation checks
  │
  ├─> get_tip_percentage()
  │     └─> [loop up to MAX_RETRIES]
  │           ├─> input()
  │           ├─> int()  (may raise ValueError)
  │           └─> membership check in VALID_TIP_PERCENTAGES
  │
  ├─> get_number_of_people()
  │     └─> [loop up to MAX_RETRIES]
  │           ├─> input()
  │           ├─> int()  (may raise ValueError)
  │           └─> positive integer check
  │
  ├─> calculate_split(bill, tip_pct, people)
  │     └─> round()  (tip_amount, total, per_person)
  │
  ├─> display_result(bill, tip_pct, people, result)
  │     └─> print()  (formatted breakdown)
  │
  └─> input()  (play again?)
        └─> [if "yes" → loop back]
        └─> [else → break]
```

## Mermaid Flow Diagram

```mermaid
flowchart TD
    A[Start] --> B[Display Welcome Banner]
    B --> C[Get Bill Amount]
    C --> C1{Valid Number > 0?}
    C1 -- No --> C2{Retries Left?}
    C2 -- Yes --> C
    C2 -- No --> EXIT[Exit Program]
    C1 -- Yes --> D[Get Tip Percentage]
    D --> D1{10, 12, or 15?}
    D1 -- No --> D2{Retries Left?}
    D2 -- Yes --> D
    D2 -- No --> EXIT
    D1 -- Yes --> E[Get Number of People]
    E --> E1{Valid Integer > 0?}
    E1 -- No --> E2{Retries Left?}
    E2 -- Yes --> E
    E2 -- No --> EXIT
    E1 -- Yes --> F[Calculate Split]
    F --> G[Display Breakdown]
    G --> H{Play Again?}
    H -- Yes --> C
    H -- No --> I[Goodbye Message]
    I --> J[End]
```

## Calculation Flow Detail

```mermaid
flowchart LR
    B[bill] --> T[tip_amount = bill * tip/100]
    T --> TO[total = bill + tip_amount]
    TO --> PP[per_person = round total/people, 2]
    PP --> R[Return dict]
```
