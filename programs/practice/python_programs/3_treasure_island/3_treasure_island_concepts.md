# Treasure Island - Python Concepts

## Core Python Concepts Used

### 1. Nested If/Elif/Else (Conditional Branching)
**Concept:** Decision trees implemented via nested conditionals.

```python
if choice1 == "left":
    if choice2 == "wait":
        if choice3 == "yellow":
            print("You Win!")
        elif choice3 == "red":
            print("Game Over - fire")
    else:
        print("Game Over - trout")
else:
    print("Game Over - hole")
```

- `if` checks first condition
- `elif` checks additional conditions (only if previous were False)
- `else` catches all remaining cases
- Nesting depth increases with each decision point

**Comparison operators used in conditions:**

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `choice == "left"` |
| `!=` | Not equal to | `choice != "right"` |
| `<` | Less than | `age < 18` |
| `>` | Greater than | `score > 100` |
| `<=` | Less than or equal | `count <= 3` |
| `>=` | Greater than or equal | `total >= 0` |
| `is` | Identity (same object) | `x is None` |
| `is not` | Not same object | `x is not None` |

**`==` vs `is` (common pitfall):**
```python
a = [1, 2, 3]
b = [1, 2, 3]
a == b    # True  (same value)
a is b    # False (different objects in memory)

# Use `is` ONLY for None, True, False:
if x is None:      # Correct
if x == None:      # Works but not Pythonic
```

**Ternary (conditional) expression — alternative to simple if/else:**
```python
result = "win" if choice == "yellow" else "lose"
# Equivalent to:
if choice == "yellow":
    result = "win"
else:
    result = "lose"
```

**Chained comparisons (Python-specific):**
```python
if 1 <= score <= 100:     # Same as: 1 <= score and score <= 100
if "a" < letter < "z":   # Alphabetical range check
```

### 2. String Methods: `.lower()` and `.strip()`
**Concept:** Case-insensitive, whitespace-tolerant input handling.

```python
choice = input("Left or right? ").strip().lower()
# "  LEFT  " → "LEFT" → "left"
```

**Input normalization chain pattern:**
```python
raw = input(prompt)       # User types "  Left  \n"
raw = raw.strip()         # Remove whitespace → "Left"
raw = raw.lower()         # Lowercase → "left"
# Or chained:
cleaned = input(prompt).strip().lower()
```

**Why `.strip()` before `.lower()`?**
- `.strip()` removes whitespace and newlines first
- `.lower()` then normalizes case
- Either order works for these two, but `.strip()` first is conventional

### 3. Multi-line Strings (Triple Quotes)
**Concept:** Strings spanning multiple lines for ASCII art.

```python
print('''
  Line 1
  Line 2
  Line 3
''')
```

- `'''` or `"""` for multi-line strings
- Preserves newlines and indentation
- Common for ASCII art, docstrings, and long text

**Raw strings with `r` prefix (closely related):**
```python
print(r"No \n newline here")  # Prints literal \n
path = r"C:\Users\name\folder"  # No need to escape backslashes
```

**`textwrap.dedent()` for indented multi-line strings:**
```python
import textwrap
msg = textwrap.dedent("""\
    Line 1
    Line 2
    Line 3
""")
# Removes common leading whitespace from all lines
```

**Escape sequences reference:**

| Escape | Meaning | Example |
|--------|---------|---------|
| `\n` | Newline | `"Hello\nWorld"` |
| `\t` | Tab | `"Name\tAge"` |
| `\\` | Literal backslash | `"C:\\Users"` |
| `\'` | Literal single quote | `'It\'s'` |
| `\"` | Literal double quote | `"He said \"hi\""` |
| `\0` | Null character | Used in binary data |

### 4. Data-Driven Design with Nested Dictionaries
**Concept:** Storing game scenarios in structured data instead of nested if/else.

```python
SCENARIOS = {
    "crossroad": {
        "prompt": "Where do you go?",
        "options": ["left", "right"],
        "results": {
            "right": {"outcome": "lose", "message": "Game Over."},
            "left":  {"outcome": "continue", "message": "You continue..."},
        },
    },
}
```

- Separates data from logic
- Easy to add/modify scenarios without changing code
- Nested dictionaries model complex structures

**Accessing nested dictionaries:**
```python
# Direct access (raises KeyError if missing)
msg = SCENARIOS["crossroad"]["results"]["left"]["message"]

# Safe access with .get() chaining
msg = SCENARIOS.get("crossroad", {}).get("results", {}).get("left", {}).get("message", "default")
```

**Data-driven vs hardcoded pattern:**
```python
# Hardcoded (simple version) — hard to modify
if choice == "left":
    if choice2 == "wait":
        print("You survive!")

# Data-driven (production version) — easy to modify
for scene_key in GAME_SEQUENCE:
    scenario = SCENARIOS[scene_key]
    choice = get_choice(scenario)
    result = scenario["results"][choice]
```

**Why data-driven is better:**
- Adding a new scenario = adding a dictionary entry (no code changes)
- Game logic function doesn't need to know the specific scenarios
- Scenarios could be loaded from JSON/YAML files for even more flexibility

### 5. Tuple Unpacking (Multiple Return Values)
**Concept:** Receiving multiple return values from a function.

```python
def play_game() -> tuple[bool, list[str]]:
    return won, choices_made

won, choices = play_game()
```

**How Python returns multiple values:**
```python
# Python actually returns a single tuple, then unpacks it:
def get_pair():
    return 1, 2        # Returns tuple (1, 2)

a, b = get_pair()      # Unpacks the tuple
result = get_pair()    # result = (1, 2) — tuple object
```

**Swap variables using tuple unpacking:**
```python
a, b = b, a    # Swaps without a temp variable
```

**Ignoring values with `_`:**
```python
_, choices = play_game()   # Ignore the won flag
first, *_, last = [1, 2, 3, 4, 5]   # first=1, last=5, ignore middle
```

### 6. For Loop over a Sequence
**Concept:** Iterating over the game sequence.

```python
GAME_SEQUENCE = ["crossroad", "lake", "doors"]
for scene_key in GAME_SEQUENCE:
    scenario = SCENARIOS[scene_key]
```

**`for` loop patterns:**
```python
# Over a list
for item in [1, 2, 3]:
    print(item)

# With index using enumerate()
for i, item in enumerate(["a", "b", "c"]):
    print(f"{i}: {item}")   # 0: a, 1: b, 2: c

# Over a dictionary
for key in my_dict:                  # Keys only
for key, value in my_dict.items():   # Key-value pairs
for value in my_dict.values():       # Values only

# Over a range
for i in range(5):           # 0, 1, 2, 3, 4
for i in range(2, 10):       # 2, 3, ..., 9
for i in range(0, 10, 2):   # 0, 2, 4, 6, 8

# Over a string
for char in "hello":   # h, e, l, l, o

# Over two lists simultaneously with zip()
names = ["Alice", "Bob"]
scores = [95, 87]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

### 7. String Joining
**Concept:** Combining list elements into a single string.

```python
path = " → ".join(choices)  # ["left", "wait", "yellow"] → "left → wait → yellow"
```

**`join()` vs `+` concatenation:**
```python
# join() — efficient for multiple strings (O(n))
words = ["hello", "world", "python"]
" ".join(words)      # "hello world python"

# + concatenation — inefficient for many strings (O(n²))
result = ""
for word in words:
    result += word + " "  # Creates new string each iteration
```

**Common `join()` patterns:**
```python
", ".join(["a", "b", "c"])      # "a, b, c"
"\n".join(lines)                 # Multi-line string from list
"".join(chars)                   # Merge chars: ["h","i"] → "hi"
" / ".join(f'"{opt}"' for opt in options)  # '"left" / "right"'
```

### 8. Infinite Loop with Validation (`while True`)
**Concept:** Repeatedly prompting until valid input is received.

```python
while True:
    raw = input("Choose: ").strip().lower()
    if raw in scenario["options"]:
        return raw
    print(f"Invalid choice '{raw}'.")
```

- `while True` creates an infinite loop
- `return` or `break` exits the loop
- Ensures the function ALWAYS returns a valid value
- Pattern name: **input validation loop** or **prompt-until-valid**

---

## Simple vs Production Comparison

| Aspect | Simple | Production |
|--------|--------|------------|
| **Structure** | Nested if/elif/else (hardcoded) | Data-driven with SCENARIOS dict |
| **Invalid input** | Falls to else (game over) | Re-prompts until valid choice given |
| **Replay** | No | Yes, with play-again loop |
| **Extensibility** | Must rewrite nested ifs | Add entry to SCENARIOS dict |
| **Summary** | None | Shows path taken and decision count |
| **Code length** | Short but rigid | Longer but flexible and modular |
| **Maintainability** | Hard to modify (change logic) | Easy — change data, not code |
| **Input handling** | Basic `.lower()` | `.strip().lower()` with validation |

### Why Production is Better
- **Robustness:** Invalid inputs don't cause game over — the user is re-prompted
- **Data-driven:** Adding new scenarios requires editing data, not logic
- **Replayability:** Players can try again without restarting the script
- **Transparency:** Game summary shows the path taken for learning
- **Testability:** `play_game()` returns structured results that can be tested
- **Separation of concerns:** Data (SCENARIOS) is separate from logic (`play_game()`)
- **Portable:** SCENARIOS could be loaded from a JSON file for easy editing
