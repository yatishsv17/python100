# Rock Paper Scissors - Python Concepts

## Core Python Concepts Used

### 1. `random` Module
**Concept:** Generating random selections for the computer player.

```python
import random
computer_choice = random.choice(["rock", "paper", "scissors"])
```

**Key `random` module functions:**

| Function | Description | Example |
|----------|-------------|---------|
| `random.choice(seq)` | Random element from sequence | `random.choice(["a","b","c"])` |
| `random.randint(a, b)` | Random integer in [a, b] inclusive | `random.randint(1, 6)` |
| `random.random()` | Random float in [0.0, 1.0) | `random.random()` → `0.7312...` |
| `random.uniform(a, b)` | Random float in [a, b] | `random.uniform(1.5, 9.5)` |
| `random.shuffle(lst)` | Shuffle list in-place | `random.shuffle(deck)` |
| `random.sample(seq, k)` | k unique random elements | `random.sample(range(100), 5)` |
| `random.choices(seq, k=n)` | k random with replacement | `random.choices("abc", k=10)` |
| `random.seed(n)` | Set seed for reproducibility | `random.seed(42)` |

**`random.choice()` vs `random.choices()` vs `random.sample()`:**
```python
items = [1, 2, 3, 4, 5]

random.choice(items)          # One item: 3
random.choices(items, k=3)    # 3 items, WITH replacement: [2, 2, 5]
random.sample(items, k=3)     # 3 items, WITHOUT replacement: [4, 1, 3]
```

**Closely related — `secrets` module for cryptographic randomness:**
```python
import secrets
secrets.choice(items)          # Cryptographically secure choice
secrets.token_hex(16)          # Random hex string: "a3f9c8..."
secrets.randbelow(100)         # Secure random int in [0, 100)
```

### 2. Logical Operators (`and`, `or`, `not`)
**Concept:** Combining multiple conditions.

```python
if (user == "rock" and computer == "scissors") or \
   (user == "scissors" and computer == "paper") or \
   (user == "paper" and computer == "rock"):
    print("You win!")
```

| Operator | Description | Short-circuit | Returns |
|----------|-------------|---------------|---------|
| `and` | Both must be True | Stops if left is False | Last evaluated operand |
| `or` | At least one True | Stops if left is True | Last evaluated operand |
| `not` | Negates boolean | N/A | `True` or `False` |

**Short-circuit evaluation in detail:**
```python
# `and` returns the first falsy value, or the last value if all truthy
0 and 5        # 0 (first falsy)
"" and "hello" # "" (first falsy)
3 and 5        # 5 (all truthy → last value)

# `or` returns the first truthy value, or the last value if all falsy
0 or 5         # 5 (first truthy)
"" or "hello"  # "hello" (first truthy)
0 or "" or []  # [] (all falsy → last value)

# Practical use — default values
name = user_input or "Anonymous"  # Use "Anonymous" if input is empty/falsy
```

**Line continuation with `\` and parentheses:**
```python
# Backslash continuation (fragile — no trailing whitespace allowed)
if condition1 and \
   condition2:

# Parentheses continuation (preferred)
if (condition1 and
    condition2 and
    condition3):
```

### 3. Dictionary as a Lookup Map (Strategy Pattern)
**Concept:** Using dictionaries to replace complex if/elif chains.

```python
WIN_MAP = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

if WIN_MAP[user] == computer:
    result = "win"
```

- Cleaner than multiple `if`/`elif` conditions
- O(1) lookup time vs O(n) for chained conditions
- Easy to extend with new rules

**Why dictionaries beat if/elif chains:**
```python
# Bad: O(n) chain, hard to maintain
if user == "rock" and computer == "scissors":
    print("Win")
elif user == "scissors" and computer == "paper":
    print("Win")
elif user == "paper" and computer == "rock":
    print("Win")
# ... more conditions

# Good: O(1) lookup, one-line check
if WIN_MAP[user] == computer:
    print("Win")
```

**Extending the game — "Rock Paper Scissors Lizard Spock":**
```python
WIN_MAP = {
    "rock": ["scissors", "lizard"],      # Rock beats scissors and lizard
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["paper", "spock"],
    "spock": ["rock", "scissors"],
}
if computer in WIN_MAP[user]:
    result = "win"
```

**Dictionary for dispatch (mapping actions to messages):**
```python
messages = {"win": "You win!", "lose": "Computer wins!", "tie": "It's a tie!"}
print(messages[result])  # No if/elif needed
```

### 4. Tuple vs List for Constants
**Concept:** Using tuples for immutable sequences.

```python
CHOICES = ("rock", "paper", "scissors")  # Tuple - immutable
choices = ["rock", "paper", "scissors"]  # List - mutable
```

- Tuples use less memory
- Signal "this won't change"
- Can be used as dictionary keys (lists cannot)

**Memory comparison:**
```python
import sys
sys.getsizeof(("a", "b", "c"))    # 72 bytes (tuple)
sys.getsizeof(["a", "b", "c"])    # 88 bytes (list)
# Lists need extra space for potential growth
```

### 5. Score Tracking with Dictionary
**Concept:** Using a mutable dictionary to track state across rounds.

```python
scores = {"wins": 0, "losses": 0, "ties": 0}
scores["wins"] += 1
```

**Alternative: `collections.Counter` for tallying:**
```python
from collections import Counter
results = Counter()
results["win"] += 1
results["win"] += 1
results["lose"] += 1
print(results)            # Counter({'win': 2, 'lose': 1})
print(results.most_common(1))  # [('win', 2)]
```

**Alternative: `collections.defaultdict` for auto-initialization:**
```python
from collections import defaultdict
scores = defaultdict(int)    # Missing keys default to 0
scores["wins"] += 1          # No KeyError even on first access
```

### 6. Percentage Calculation and Display
**Concept:** Computing and formatting statistics.

```python
total = scores["wins"] + scores["losses"] + scores["ties"]
if total > 0:
    win_rate = (scores["wins"] / total) * 100
    print(f"Win rate: {win_rate:.1f}%")
```

**Guard against division by zero:**
```python
# Pattern 1: Check before dividing
if total > 0:
    rate = wins / total

# Pattern 2: Try/except
try:
    rate = wins / total
except ZeroDivisionError:
    rate = 0.0

# Pattern 3: Ternary
rate = wins / total if total > 0 else 0.0
```

### 7. Emoji/Unicode in Python Strings
**Concept:** Using Unicode characters directly in Python strings.

```python
EMOJIS = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
print(f"You chose: rock {EMOJIS['rock']}")
```

- Python 3 strings are Unicode by default (UTF-8)
- Emojis are valid string characters
- Use `\u` for Unicode escape: `"\u2764"` → `"❤"`
- Use `\U` for extended: `"\U0001F600"` → `"😀"`
- `ord("A")` → `65`, `chr(65)` → `"A"`

---

## Simple vs Production Comparison

| Aspect | Simple | Production |
|--------|--------|------------|
| **Winner logic** | Chained `if/elif` with `and`/`or` | Dictionary lookup (`WIN_MAP`) |
| **Rounds** | Single round | Multiple rounds with score tracking |
| **Invalid input** | Prints error, exits | Re-prompts until valid (`while True`) |
| **Statistics** | None | Win rate, total rounds, final summary |
| **Code structure** | Linear script | Functions with single responsibility |
| **Extensibility** | Hard to add options | Add to `WIN_MAP` and `CHOICES` |
| **Display** | Plain text | Emojis and aligned output |
| **Separation** | Logic mixed with I/O | `determine_winner()` is pure logic |

### Why Production is Better
- **Scalability:** Adding "lizard" and "spock" only requires updating constants
- **Score tracking:** Multi-round play with cumulative statistics
- **Clean logic:** `WIN_MAP` dictionary eliminates complex boolean chains
- **User experience:** Re-prompting on invalid input, final stats summary
- **Testability:** `determine_winner("rock", "scissors")` → `"win"` (pure function)
- **Separation of concerns:** Game logic, I/O, and display are in separate functions
