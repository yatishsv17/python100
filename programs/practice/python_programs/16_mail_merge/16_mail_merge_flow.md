# Mail Merge - Function Call Flow & Flow Diagram

## Simple Version Call Flow

```
Script Start
  └─> os.makedirs(OUTPUT_DIR, exist_ok=True)
  └─> open(TEMPLATE_PATH) → template string
  └─> open(NAMES_PATH) → names list
  └─> for each name:
  │     └─> name.strip()
  │     └─> template.replace("[name]", name)
  │     └─> open(output_path, "w") → write letter
  │     └─> print() progress
  └─> print() summary count
Script End
```

## Production Version Call Graph

```
run()
  ├─> print() welcome banner
  │
  ├─> validate_files()
  │     ├─> TEMPLATE_PATH.exists()
  │     └─> NAMES_PATH.exists()
  │
  ├─> read_template()
  │     ├─> TEMPLATE_PATH.read_text(encoding="utf-8")
  │     └─> Check PLACEHOLDER in text
  │
  ├─> read_names()
  │     ├─> NAMES_PATH.read_text(encoding="utf-8")
  │     └─> splitlines() → strip() → filter empty
  │
  ├─> generate_letters(template, names)
  │     ├─> OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
  │     └─> for each name:
  │           ├─> sanitize_filename(name)
  │           │     └─> re.sub(r"[^\w\s-]", "", name)
  │           ├─> template.replace(PLACEHOLDER, name)
  │           └─> output_path.write_text(letter)
  │                 └─> try/except OSError
  │
  └─> print() summary stats
```

## Mermaid Flow Diagram

```mermaid
flowchart TD
    A[Start] --> B[Validate Files Exist]
    B --> C{Both exist?}
    C -- No --> D[Error and Exit]
    C -- Yes --> E[Read Template]
    E --> F{Contains placeholder?}
    F -- No --> G[Error and Exit]
    F -- Yes --> H[Read Names]
    H --> I{Names found?}
    I -- No --> J[Error: No names]
    I -- Yes --> K[Create Output Directory]
    K --> L[For Each Name]
    L --> M[Sanitize Filename]
    M --> N{Valid name?}
    N -- No --> O[Skip, increment skipped]
    N -- Yes --> P[Replace placeholder]
    P --> Q[Write Output File]
    Q --> R{Write OK?}
    R -- No --> S[Log error, increment errors]
    R -- Yes --> T[Increment created]
    O --> U{More names?}
    S --> U
    T --> U
    U -- Yes --> L
    U -- No --> V[Display Summary]
    V --> W[End]
```

## Data Flow

```mermaid
flowchart LR
    TPL["template.txt<br/>'Dear [name]...'"] --> MERGE["replace([name], name)"]
    NAMES["names.txt<br/>Aang<br/>Zuko<br/>..."] --> MERGE
    MERGE --> OUT1["for_Aang.txt"]
    MERGE --> OUT2["for_Zuko.txt"]
    MERGE --> OUT3["for_....txt"]
```
