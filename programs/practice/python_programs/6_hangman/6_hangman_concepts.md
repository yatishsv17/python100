# Hangman - Python Concepts

## Core Python Concepts Used

### 1. Lists as Mutable Sequences
**Concept:** Using lists to track the word display state.

```python
display = ["_"] * len(word)   # Creates ["_", "_", "_", ...]
display[i] = guess             # Reveal letter at position i
"_" not in display             # Check if all letters revealed
```

- `["_"] * n` creates a list of n underscores
- Lists are mutable — elements can be changed in-place
- `in` operator checks membership

**List vs Tuple vs String mutability:**
```python
# List — MUTABLE (can change elements)
display = ["_", "_", "_"]
display[0] = "h"           # OK: ["h", "_", "_"]

# Tuple — IMMUTABLE (cannot change)
t = ("_", "_", "_")
t[0] = "h"                 # TypeError!

# String — IMMUTABLE (cannot change characters)
s = "___"
s[0] = "h"                 # TypeError!
# Must create new string:
s = "h" + s[1:]            # "h__"
```

**List slicing (closely related):**
```python
lst = [0, 1, 2, 3, 4, 5]
lst[1:4]       # [1, 2, 3]         — elements 1 to 3
lst[:3]        # [0, 1, 2]         — first 3
lst[3:]        # [3, 4, 5]         — from index 3 to end
lst[-2:]       # [4, 5]            — last 2
lst[::2]       # [0, 2, 4]         — every 2nd element
lst[::-1]      # [5, 4, 3, 2, 1, 0] — reversed copy

# Slice assignment (mutable only):
lst[1:3] = [10, 20]  # [0, 10, 20, 3, 4, 5]
```

### 2. `enumerate()` Function
**Concept:** Getting both index and value when iterating.

```python
for i, letter in enumerate(word):
    if letter == guess:
        display[i] = letter
```

- Returns (index, value) tuples
- Avoids manual index tracking with `range(len(...))`
- `enumerate(iterable, start=0)` — start can be customized

**`enumerate()` vs manual index tracking:**
```python
# Bad — manual index
i = 0
for letter in word:
    if letter == guess:
        display[i] = letter
    i += 1

# Bad — range(len())
for i in range(len(word)):
    if word[i] == guess:
        display[i] = word[i]

# Good — enumerate() (Pythonic)
for i, letter in enumerate(word):
    if letter == guess:
        display[i] = letter
```

**Custom start index:**
```python
for i, line in enumerate(lines, start=1):
    print(f"Line {i}: {line}")
# Line 1: ..., Line 2: ..., etc.
```

### 3. Sets for Membership Tracking
**Concept:** Using sets for efficient duplicate detection.

```python
guessed: set[str] = set()
guessed.add(letter)
if letter in guessed:  # O(1) lookup
    print("Already guessed!")
```

| Operation | Set | List |
|-----------|-----|------|
| `x in collection` | O(1) average | O(n) |
| `.add(x)` / `.append(x)` | O(1) | O(1) |
| Duplicates | Not allowed | Allowed |
| Order | Unordered (insertion order in 3.7+) | Ordered |

**Set methods reference:**

| Method | Description | Example |
|--------|-------------|---------|
| `.add(x)` | Add element | `s.add("a")` |
| `.remove(x)` | Remove (KeyError if missing) | `s.remove("a")` |
| `.discard(x)` | Remove (no error if missing) | `s.discard("a")` |
| `.pop()` | Remove and return arbitrary element | `s.pop()` |
| `.clear()` | Remove all elements | `s.clear()` |
| `.union(other)` or `\|` | All elements from both | `s1 \| s2` |
| `.intersection(other)` or `&` | Common elements | `s1 & s2` |
| `.difference(other)` or `-` | In s1 but not s2 | `s1 - s2` |
| `.symmetric_difference(other)` or `^` | In one but not both | `s1 ^ s2` |
| `.issubset(other)` | All in other? | `s1 <= s2` |
| `.issuperset(other)` | Contains all of other? | `s1 >= s2` |

**Set comprehension:**
```python
unique_letters = {char.lower() for char in word if char.isalpha()}
# {'p', 'y', 't', 'h', 'o', 'n'}
```

**Creating sets:**
```python
s = set()                    # Empty set (NOT {}, that's an empty dict!)
s = {1, 2, 3}               # Set literal
s = set([1, 1, 2, 2, 3])    # From list: {1, 2, 3}
s = set("hello")             # From string: {'h', 'e', 'l', 'o'}
```

### 4. Classes and OOP (Object-Oriented Programming)
**Concept:** Encapsulating game state and behavior in a class.

```python
class HangmanGame:
    def __init__(self, word: str) -> None:
        self.word = word
        self.lives = 6
        self.guessed = set()

    def guess(self, letter: str) -> str:
        # Process guess and return result
        ...

    @property
    def is_won(self) -> bool:
        return "_" not in self.display
```

- `__init__` initializes instance state
- `self` refers to the current instance
- Methods operate on instance data
- `@property` creates read-only computed attributes

**OOP terminology:**

| Term | Meaning | Example |
|------|---------|---------|
| **Class** | Blueprint/template | `class HangmanGame:` |
| **Instance** | Specific object | `game = HangmanGame("python")` |
| **Attribute** | Data on an instance | `game.word`, `game.lives` |
| **Method** | Function on an instance | `game.guess("a")` |
| **`self`** | Reference to current instance | `self.lives -= 1` |
| **Constructor** | `__init__` method | Called automatically on `HangmanGame(...)` |

**Class vs Instance attributes:**
```python
class Dog:
    species = "Canis familiaris"  # Class attribute (shared by all)

    def __init__(self, name):
        self.name = name          # Instance attribute (unique per object)

fido = Dog("Fido")
rex = Dog("Rex")
fido.species     # "Canis familiaris" (shared)
fido.name        # "Fido" (unique)
rex.name         # "Rex" (unique)
```

**Common dunder (magic) methods:**
```python
class MyClass:
    def __init__(self):     # Constructor
    def __str__(self):      # str(obj), print(obj)
    def __repr__(self):     # repr(obj), debugging display
    def __len__(self):      # len(obj)
    def __eq__(self, other): # obj == other
    def __lt__(self, other): # obj < other
    def __contains__(self, item): # item in obj
    def __getitem__(self, key):   # obj[key]
```

### 5. `@property` Decorator
**Concept:** Making methods behave like attributes.

```python
@property
def is_won(self) -> bool:
    return "_" not in self.display

# Usage: game.is_won (not game.is_won())
```

- Accessed without parentheses
- Computed on each access (not cached)
- Useful for derived state

**Property with getter, setter, and deleter:**
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        """Getter — computed on access."""
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Setter — convert and store."""
        self._celsius = (value - 32) * 5/9

    @fahrenheit.deleter
    def fahrenheit(self):
        """Deleter — reset."""
        self._celsius = 0

t = Temperature(100)
t.fahrenheit        # 212.0 (getter)
t.fahrenheit = 32   # sets _celsius to 0.0 (setter)
```

**When to use `@property` vs regular methods:**
- Use `@property` for **derived state** (computed from existing attributes)
- Use methods for **actions** that do work or have side effects
- `game.is_won` ← property (reads state)
- `game.guess("a")` ← method (changes state)

### 6. While Loop with Multiple Exit Conditions
**Concept:** Game loop that checks win/lose on each iteration.

```python
while not game.is_over:       # Loop until game ends
    display_state(game)
    raw = input("Guess: ")
    result = game.guess(raw)
```

**`while...else` clause (used in simple version):**
```python
while lives > 0:
    # ... game logic ...
    if "_" not in display:
        print("You win!")
        break
else:
    print("Game Over!")  # Only runs if lives reached 0 (no break)
```

**Nested loop pattern (outer=replay, inner=game):**
```python
while True:                    # Outer: replay loop
    game = HangmanGame(word)
    while not game.is_over:    # Inner: game loop
        # Play one turn
        pass
    # Game over — show results
    if input("Again?") != "yes":
        break
```

### 7. `sorted()` vs `.sort()`
**Concept:** Sorting with and without mutation.

```python
sorted_guessed = sorted(game.guessed)  # Sort set into NEW list
```

| Function | Mutates? | Returns | Works On |
|----------|----------|---------|----------|
| `sorted(iterable)` | No | New list | Any iterable (set, tuple, dict, etc.) |
| `list.sort()` | Yes | `None` | Lists only |

**Sorting with key functions:**
```python
sorted(["banana", "Apple", "cherry"], key=str.lower)
# ['Apple', 'banana', 'cherry'] — case-insensitive sort

sorted(words, key=len)               # Sort by length
sorted(words, key=len, reverse=True) # Longest first

# Lambda as key:
students = [("Alice", 95), ("Bob", 87), ("Charlie", 92)]
sorted(students, key=lambda s: s[1], reverse=True)
# [('Alice', 95), ('Charlie', 92), ('Bob', 87)]
```

### 8. String Return Values as Status Codes
**Concept:** Using strings to communicate action results.

```python
def guess(self, letter: str) -> str:
    if letter in self.guessed:
        return "already_guessed"
    if letter in self.word:
        return "correct"
    return "incorrect"
```

**Alternatives to string status codes:**

| Approach | Pros | Cons |
|----------|------|------|
| String returns | Simple, readable | Typo-prone, no IDE autocomplete |
| Enum | Type-safe, IDE-friendly | More boilerplate |
| Boolean | Simple for 2 states | Can't represent 3+ states |
| Exception | For errors only | Overuse is bad practice |

**Enum approach (better for production):**
```python
from enum import Enum, auto
class GuessResult(Enum):
    CORRECT = auto()
    INCORRECT = auto()
    ALREADY_GUESSED = auto()
    INVALID = auto()
```

---

## Simple vs Production Comparison

| Aspect | Simple | Production |
|--------|--------|------------|
| **Data structure** | List for guessed letters | Set (O(1) lookup) |
| **Architecture** | Procedural script | OOP with `HangmanGame` class |
| **State management** | Global variables | Encapsulated in class instance |
| **Properties** | Manual checks | `@property` decorators (`is_won`, `is_lost`, `is_over`) |
| **Statistics** | None | Correct/incorrect guess counts |
| **Replay** | No | Yes, with play-again loop |
| **Word list** | 10 words | 15 words |
| **Display** | Basic text | ASCII art hangman stages |
| **Input validation** | Minimal | Single alpha char, duplicate check |

### Why Production is Better
- **Encapsulation:** All game state lives in one object — no global variables
- **Efficiency:** Set-based duplicate detection is O(1) vs O(n) with lists
- **Clean API:** `game.is_won`, `game.is_lost` read like English
- **Testability:** Can create `HangmanGame` objects and test methods independently
- **Separation of concerns:** Game logic (class) separated from display logic (functions)
- **Reusable:** `HangmanGame` class can be imported and used in a GUI or web app
