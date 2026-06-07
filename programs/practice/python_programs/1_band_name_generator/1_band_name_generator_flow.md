# Band Name Generator - Function Call Flow & Flow Diagram

## Simple Version Call Flow

The simple version is a linear script with no function calls:

```
Script Start
  └─> print() welcome message
  └─> input() city name
  └─> input() pet name
  └─> String concatenation
  └─> print() band name
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
  │     └─> print()  (welcome message)
  │
  ├─> get_valid_input("city prompt", "City name")
  │     └─> [loop up to MAX_RETRIES]
  │           ├─> input()
  │           └─> validate_input(raw_text, "City name")
  │                 ├─> str.strip()
  │                 ├─> str.replace().isalpha()
  │                 └─> str.title()  (if valid)
  │
  ├─> get_valid_input("pet prompt", "Pet name")
  │     └─> [same as above]
  │
  ├─> generate_band_names(city, pet)
  │     └─> [loop over BAND_NAME_STYLES.items()]
  │           └─> str.format(city=city, pet=pet)
  │
  ├─> print()  (display results)
  │
  └─> input()  (play again?)
        └─> [if "yes" → loop back to get_valid_input]
        └─> [if not "yes" → break, print goodbye]
```

## Mermaid Flow Diagram

```mermaid
flowchart TD
    A[Start] --> B[Display Welcome Banner]
    B --> C[Prompt for City Name]
    C --> D{Valid Input?}
    D -- No --> E{Retries Left?}
    E -- Yes --> C
    E -- No --> F[Exit with Error]
    D -- Yes --> G[Prompt for Pet Name]
    G --> H{Valid Input?}
    H -- No --> I{Retries Left?}
    I -- Yes --> G
    I -- No --> F
    H -- Yes --> J[Generate Band Names]
    J --> K[Display All Styles]
    K --> L{Play Again?}
    L -- Yes --> C
    L -- No --> M[Print Goodbye]
    M --> N[End]
```

## Validation Flow Detail

```mermaid
flowchart TD
    V1[Receive raw input] --> V2[Strip whitespace]
    V2 --> V3{Is empty?}
    V3 -- Yes --> V7[Return None + error msg]
    V3 -- No --> V4{Length >= 2?}
    V4 -- No --> V7
    V4 -- Yes --> V5{All alphabetic?}
    V5 -- No --> V7
    V5 -- Yes --> V6[Return title-cased string]
```
