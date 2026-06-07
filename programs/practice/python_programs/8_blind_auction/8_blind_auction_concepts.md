# Blind Auction - Python Concepts

## Core Python Concepts Used

### 1. Dictionaries for Data Storage
**Concept:** Mapping bidder names to bid amounts.

```python
bids = {}
bids["Alice"] = 150.0    # Add/update
bids["Bob"] = 200.0
print(bids["Alice"])      # Access → 150.0
```

**Complete dictionary operations:**

| Method | Description | Example |
|--------|-------------|---------|
| `d[key] = value` | Set/update | `bids["Alice"] = 100` |
| `d[key]` | Get value (KeyError if missing) | `bids["Alice"]` → `100` |
| `d.get(key, default)` | Safe get (no error) | `bids.get("Zoe", 0)` → `0` |
| `d.keys()` | All keys (view) | `dict_keys(["Alice", "Bob"])` |
| `d.values()` | All values (view) | `dict_values([100, 200])` |
| `d.items()` | Key-value pairs (view) | `[("Alice", 100), ...]` |
| `key in d` | Membership check (keys) | `"Alice" in bids` → `True` |
| `d.pop(key, default)` | Remove and return | `bids.pop("Alice", 0)` |
| `d.setdefault(key, val)` | Get or set if missing | `d.setdefault("k", [])` |
| `d.update(other)` | Merge another dict | `d.update({"Eve": 300})` |
| `d \| other` | Merge (Python 3.9+) | `d1 \| d2` (new dict) |
| `del d[key]` | Delete key | `del bids["Alice"]` |
| `d.clear()` | Remove all | `bids.clear()` |

**`d[key]` vs `d.get(key)` — when to use which:**
```python
# d[key] — when key MUST exist (raises KeyError if not)
price = prices["apple"]  # Error if "apple" not in prices

# d.get(key) — when key might be missing
price = prices.get("apple", 0.0)  # Returns 0.0 if missing

# d.setdefault(key, default) — get or initialize
groups = {}
groups.setdefault("team_a", []).append("Alice")
groups.setdefault("team_a", []).append("Bob")
# groups = {"team_a": ["Alice", "Bob"]}
```

**Dictionary comprehension:**
```python
# Filter bids above 100
high_bids = {name: bid for name, bid in bids.items() if bid > 100}

# Invert a dictionary (swap keys and values)
inverted = {v: k for k, v in bids.items()}

# Create dict from two lists
names = ["Alice", "Bob"]
amounts = [150, 200]
bids = dict(zip(names, amounts))  # {"Alice": 150, "Bob": 200}
```

**Dictionary ordering (Python 3.7+):**
- Dictionaries maintain **insertion order**
- Before Python 3.7, dictionaries were unordered
- Use `collections.OrderedDict` only if you need `move_to_end()` or equality based on order

### 2. `max()` with `key` Parameter
**Concept:** Finding the dictionary key with the highest value.

```python
winner = max(bids, key=bids.get)
# Iterates over keys, uses bids.get to compare values
# Returns the key with the maximum value
```

- `max(iterable)` returns the largest element
- `key=func` applies `func` to each element for comparison
- `min()` works the same way for minimum

**How `key=` works step by step:**
```python
bids = {"Alice": 150, "Bob": 200, "Charlie": 175}

# max(bids) without key → compares keys alphabetically: "Charlie"
# max(bids, key=bids.get) → compares bids.get("Alice"), bids.get("Bob"), ...
#   = compares 150, 200, 175 → max is 200 → returns "Bob"
```

**Common `key=` patterns:**
```python
max(words, key=len)                    # Longest word
max(students, key=lambda s: s["gpa"])  # Highest GPA
min(files, key=os.path.getsize)        # Smallest file
sorted(items, key=str.lower)           # Case-insensitive sort
```

**`max()` with empty iterable (edge case):**
```python
max([])                        # ValueError: max() arg is an empty sequence
max([], default=0)             # 0 — safe with default parameter
max(bids, key=bids.get) if bids else None  # Guard with ternary
```

### 3. `os` Module — System Interaction
**Concept:** Running shell commands and detecting the operating system.

```python
import os
os.system("cls" if os.name == "nt" else "clear")
```

- `os.name` returns `"nt"` on Windows, `"posix"` on Linux/Mac
- `cls` clears Windows terminal; `clear` clears Unix terminal

**Key `os` module functions:**

| Function | Description | Example |
|----------|-------------|---------|
| `os.name` | OS identifier | `"nt"` or `"posix"` |
| `os.system(cmd)` | Run shell command | `os.system("ls")` |
| `os.getcwd()` | Current directory | `"/home/user/project"` |
| `os.path.exists(p)` | File/dir exists? | `os.path.exists("data.csv")` |
| `os.path.join(a, b)` | Join paths safely | `os.path.join("data", "file.txt")` |
| `os.listdir(path)` | List directory contents | `os.listdir(".")` |
| `os.makedirs(path)` | Create nested dirs | `os.makedirs("a/b/c")` |
| `os.environ` | Environment variables | `os.environ["HOME"]` |
| `os.getenv(key)` | Safe env var get | `os.getenv("API_KEY", "")` |

**`subprocess` vs `os.system()` (modern alternative):**
```python
# os.system — simple, returns exit code only
os.system("echo hello")

# subprocess — more control, captures output
import subprocess
result = subprocess.run(["echo", "hello"], capture_output=True, text=True)
print(result.stdout)  # "hello\n"
```

### 4. While Loop — Flag Variable vs `break`
**Concept:** Controlling loop execution with different patterns.

```python
# Pattern 1: Flag variable (simple version)
continue_bidding = True
while continue_bidding:
    # ... process bid ...
    if more != "yes":
        continue_bidding = False

# Pattern 2: while True + break (production — cleaner)
while True:
    # ... process bid ...
    if more != "yes":
        break
```

**Loop control statements:**

| Statement | Effect | Use |
|-----------|--------|-----|
| `break` | Exit loop immediately | Stop on condition |
| `continue` | Skip to next iteration | Skip invalid items |
| `return` | Exit function (and loop) | Return result early |
| `pass` | Do nothing (placeholder) | Empty loop body |

**`for...else` and `while...else` (Python-specific):**
```python
for name in bidders:
    if name == target:
        print("Found!")
        break
else:
    # Only runs if loop completed WITHOUT break
    print("Not found!")
```

### 5. Built-in Aggregate Functions
**Concept:** Computing statistics from collections.

```python
amounts = list(bids.values())
max(amounts)               # Highest bid
min(amounts)               # Lowest bid
sum(amounts) / len(amounts) # Average bid
len(bids)                  # Number of bidders
```

**Complete list of built-in aggregate/sequence functions:**

| Function | Description | Example |
|----------|-------------|---------|
| `max(iterable)` | Largest element | `max([3, 1, 4])` → `4` |
| `min(iterable)` | Smallest element | `min([3, 1, 4])` → `1` |
| `sum(iterable)` | Total | `sum([1, 2, 3])` → `6` |
| `len(collection)` | Count of elements | `len([1, 2, 3])` → `3` |
| `sorted(iterable)` | New sorted list | `sorted([3, 1, 4])` → `[1, 3, 4]` |
| `reversed(seq)` | Reverse iterator | `list(reversed([1, 2]))` → `[2, 1]` |
| `any(iterable)` | True if any truthy | `any([0, 0, 1])` → `True` |
| `all(iterable)` | True if all truthy | `all([1, 1, 0])` → `False` |
| `enumerate(it)` | Index + value pairs | `list(enumerate("ab"))` → `[(0,"a"),(1,"b")]` |
| `zip(a, b)` | Pair elements | `list(zip([1,2],["a","b"]))` → `[(1,"a"),(2,"b")]` |
| `map(fn, it)` | Apply fn to each | `list(map(str, [1,2]))` → `["1","2"]` |
| `filter(fn, it)` | Keep where fn is True | `list(filter(bool, [0,1,2]))` → `[1,2]` |

**Closely related — `statistics` module:**
```python
import statistics
data = [150, 200, 175, 180]
statistics.mean(data)      # 176.25
statistics.median(data)    # 177.5
statistics.stdev(data)     # 20.96...
statistics.mode([1,1,2,3]) # 1
```

### 6. Type Hints for Complex Types
**Concept:** Annotating dictionary types for clarity and IDE support.

```python
bids: dict[str, float] = {}

def find_winner(bids: dict[str, float]) -> tuple[str, float]:
    ...
```

**Type hint syntax evolution:**
```python
# Python 3.9+: built-in generics (lowercase)
x: dict[str, float] = {}
y: list[int] = [1, 2, 3]
z: tuple[str, int] = ("Alice", 95)

# Python 3.5-3.8: typing module (uppercase)
from typing import Dict, List, Tuple, Optional
x: Dict[str, float] = {}
y: List[int] = [1, 2, 3]
z: Tuple[str, int] = ("Alice", 95)
w: Optional[str] = None  # str | None
```

**Common type hints:**

| Hint | Meaning | Example |
|------|---------|---------|
| `int`, `str`, `float`, `bool` | Primitives | `age: int = 25` |
| `list[int]` | List of ints | `scores: list[int] = []` |
| `dict[str, float]` | String→float dict | `bids: dict[str, float]` |
| `tuple[str, int]` | Fixed-length tuple | `pair: tuple[str, int]` |
| `Optional[str]` | `str` or `None` | `name: Optional[str] = None` |
| `str \| None` | Union (3.10+) | `name: str \| None = None` |
| `Callable[[int], str]` | Function type | `fn: Callable[[int], str]` |
| `Any` | Any type | `data: Any` |

**Type hints are NOT enforced at runtime:**
```python
x: int = "hello"  # No error! Python ignores hints at runtime
# Use mypy or pyright for static type checking:
# $ mypy my_program.py
```

---

## Simple vs Production Comparison

| Aspect | Simple | Production |
|--------|--------|------------|
| **Input validation** | None — crashes on bad input | Name and bid validated with retries |
| **Duplicate names** | Silent overwrite | Warning before overwrite |
| **Statistics** | Winner only | Full stats: count, range, average |
| **Empty auction** | Crashes (`max()` on empty) | Handled gracefully with guard |
| **Code structure** | Linear script | Functions with single responsibility |
| **Screen clearing** | Inline `os.system` | Wrapped in `clear_screen()` |
| **Type safety** | No hints | Full `dict[str, float]` annotations |

### Why Production is Better
- **Safety:** Handles edge cases (empty bids, invalid input, duplicate names)
- **Transparency:** Full auction statistics help bidders understand context
- **Maintainability:** Modular functions can be tested and reused independently
- **User experience:** Warnings for overwrites prevent accidental data loss
- **Robustness:** Validates every input before storing it
