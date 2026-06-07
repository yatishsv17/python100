# Number Guessing Game - Python Concepts

## Core Python Concepts Used

### 1. `random.randint()`
**Concept:** Generating a random integer within an inclusive range.

```python
import random
secret = random.randint(1, 100)  # Both endpoints included
```

| Function | Range | Example |
|----------|-------|---------|
| `random.randint(a, b)` | [a, b] inclusive | `randint(1, 6)` → 1-6 |
| `random.randrange(a, b)` | [a, b) exclusive end | `randrange(1, 7)` → 1-6 |
| `random.random()` | [0.0, 1.0) | `random()` → 0.7231... |

**`randint` vs `randrange` — subtle difference:**
```python
random.randint(1, 6)      # 1, 2, 3, 4, 5, or 6 (inclusive both ends)
random.randrange(1, 7)    # 1, 2, 3, 4, 5, or 6 (exclusive end — like range())
random.randrange(0, 100, 5)  # Random multiple of 5: 0, 5, 10, ..., 95

# Simulating a die:
die = random.randint(1, 6)   # Most readable for dice
```

### 2. Dictionary Mapping for Configuration
**Concept:** Using a dict to map difficulty names to values.

```python
DIFFICULTY_MAP = {"easy": 10, "hard": 5}
attempts = DIFFICULTY_MAP[difficulty]
```

- Cleaner than if/elif chains
- Easy to add new difficulties
- Acts as a configuration table

**Configuration dict pattern:**
```python
# Bad — hardcoded if/elif
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

# Good — data-driven configuration
DIFFICULTY_MAP = {"easy": 10, "medium": 7, "hard": 5}
attempts = DIFFICULTY_MAP[difficulty]
# Adding "extreme" = just one dict entry: "extreme": 3
```

**Closely related — `enum.Enum` for configuration:**
```python
from enum import Enum

class Difficulty(Enum):
    EASY = 10
    MEDIUM = 7
    HARD = 5

attempts = Difficulty["EASY"].value  # 10
# Type-safe, IDE autocomplete, prevents typos
```

### 3. Sets for Tracking Unique Guesses
**Concept:** Using sets to prevent duplicate guesses.

```python
guessed: set[int] = set()
guessed.add(guess)
if guess in guessed:  # O(1) lookup
    print("Already guessed!")
```

**Why sets and not lists for tracking?**
```python
# List: O(n) lookup — checks every element
if guess in guessed_list:    # Slow for large lists

# Set: O(1) lookup — hash-based, constant time
if guess in guessed_set:     # Fast regardless of size
```

**Set operations useful for game analysis:**
```python
all_numbers = set(range(1, 101))    # {1, 2, ..., 100}
guessed = {5, 23, 67, 42}
remaining = all_numbers - guessed   # Numbers not yet guessed
print(f"{len(remaining)} numbers left")
```

### 4. Lambda Functions
**Concept:** Anonymous functions used as sort/filter keys.

```python
closest = min(history, key=lambda g: abs(g - secret))
# Finds the guess closest to the secret number
```

- `lambda args: expression` — anonymous single-expression function
- `abs()` returns the absolute value
- `key` parameter tells `min()` what to compare

**Lambda vs `def` — when to use which:**
```python
# Lambda: short, throwaway, single expression
sorted(words, key=lambda w: len(w))
filter(lambda x: x > 0, numbers)

# def: complex, reusable, multiple statements
def closest_to_secret(guess):
    """Distance from secret number."""
    return abs(guess - secret)
min(history, key=closest_to_secret)
```

**Lambda limitations:**
```python
# Lambdas can ONLY contain a single expression:
lambda x: x * 2              # OK — expression
lambda x: print(x)           # OK — print is an expression
lambda x: x if x > 0 else 0  # OK — ternary is an expression

# These CANNOT be lambdas:
# Multiple statements, loops, try/except, assignments
```

**Common lambda patterns:**
```python
sorted(items, key=lambda x: x["age"])           # Sort by dict key
sorted(items, key=lambda x: (x["age"], x["name"]))  # Multi-key sort
max(items, key=lambda x: x.score)               # Max by attribute
filter(lambda x: x % 2 == 0, range(10))         # Even numbers
map(lambda x: x ** 2, range(5))                  # Squares
```

### 5. Tuple Return Values with Type Hints
**Concept:** Returning multiple related values from a function.

```python
def play_game() -> tuple[bool, int, list[int]]:
    return won, secret, history

won, secret, history = play_game()  # Unpack
```

**Type hint for tuple return values:**
```python
# Fixed-length tuple (each position has a type)
def func() -> tuple[bool, int, list[int]]:
    return True, 42, [1, 2, 3]

# Variable-length tuple of same type
def get_primes() -> tuple[int, ...]:
    return (2, 3, 5, 7, 11)
```

### 6. While Loop with Decrementing Counter
**Concept:** Counting down attempts in a loop.

```python
while attempts > 0:
    # ... get guess, check ...
    attempts -= 1
```

- Decrement after processing each guess
- Loop exits naturally when counter reaches 0

**Alternative loop patterns for guessing games:**
```python
# Pattern 1: Decrementing counter (used here)
while attempts > 0:
    guess = get_guess()
    attempts -= 1

# Pattern 2: for loop with range
for attempt in range(max_attempts):
    guess = get_guess()
    remaining = max_attempts - attempt - 1

# Pattern 3: Incrementing counter
guesses = 0
while guesses < max_guesses:
    guess = get_guess()
    guesses += 1
```

### 7. `abs()` — Absolute Value
**Concept:** Computing distance regardless of direction.

```python
distance = abs(guess - secret)
# abs(50 - 42) = 8
# abs(42 - 50) = 8  (same result regardless of order)
```

**Common uses of `abs()`:**
```python
abs(-5)           # 5
abs(5)            # 5
abs(3.14)         # 3.14
abs(-3 + 4j)      # 5.0 (complex number magnitude)

# Finding closest value:
closest = min(candidates, key=lambda x: abs(x - target))

# Check if two values are "close enough":
if abs(a - b) < 0.001:
    print("Approximately equal")
```

**Closely related — `math.isclose()` for float comparison:**
```python
import math
math.isclose(0.1 + 0.2, 0.3)  # True (handles float imprecision)
```

---

## Simple vs Production Comparison

| Aspect | Simple | Production |
|--------|--------|------------|
| **Input validation** | None — crashes on bad input | Validates int, range, duplicates |
| **Duplicate guesses** | Allowed (wastes attempts) | Rejected without penalty |
| **Statistics** | None | Guess count, history, closest guess |
| **Configuration** | Hardcoded if/else | `DIFFICULTY_MAP` dictionary |
| **Replay** | No | Yes, with play-again loop |
| **Constants** | Magic numbers | Named constants (`RANGE_MIN`, etc.) |
| **Hints** | Basic higher/lower | Higher/lower + distance feedback |

### Why Production is Better
- **No wasted turns:** Duplicate guesses don't cost attempts
- **Richer feedback:** History and closest-guess analysis help learning
- **Extensibility:** Adding "medium" difficulty = one line in `DIFFICULTY_MAP`
- **Robustness:** Won't crash on non-integer input
- **Analysis:** Post-game statistics show guess progression and distance
