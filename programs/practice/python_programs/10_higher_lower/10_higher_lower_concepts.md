# Higher Lower Game - Python Concepts

## Core Python Concepts Used

### 1. List of Dictionaries (Data Modeling)
**Concept:** Representing structured records as dictionaries in a list.

```python
DATA = [
    {"name": "Instagram", "followers": 500, "category": "Social Media"},
    {"name": "TikTok", "followers": 350, "category": "Social Media"},
]
item = DATA[0]
print(item["name"])       # "Instagram"
print(item["followers"])  # 500
```

- Common pattern for tabular data
- Each dict is a "row", keys are "columns"

**Alternative data modeling approaches:**
```python
# 1. NamedTuple (immutable, lightweight)
from collections import namedtuple
Celebrity = namedtuple("Celebrity", ["name", "followers", "category"])
data = [Celebrity("Instagram", 500, "Social Media")]
data[0].name  # "Instagram" — attribute access

# 2. dataclass (mutable, full-featured)
from dataclasses import dataclass
@dataclass
class Celebrity:
    name: str
    followers: int
    category: str
data = [Celebrity("Instagram", 500, "Social Media")]

# 3. TypedDict (dict with type checking)
from typing import TypedDict
class CelebrityDict(TypedDict):
    name: str
    followers: int
    category: str
```

**When to use which:**

| Approach | Pros | Cons | Best For |
|----------|------|------|----------|
| `dict` | Flexible, no setup | No IDE autocomplete, typo-prone | Quick scripts |
| `namedtuple` | Immutable, lightweight | Can't modify | Read-only records |
| `dataclass` | Type hints, methods, mutable | More code | Production classes |
| `TypedDict` | Dict with types | Dict only | JSON/API data |

### 2. `random.sample()` — Unique Random Selection
**Concept:** Selecting multiple unique random items from a sequence.

```python
import random
a, b = random.sample(DATA, 2)  # Pick 2 unique items
```

| Function | Description | Replacement? |
|----------|-------------|-------------|
| `random.choice(seq)` | Pick 1 random item | N/A |
| `random.sample(seq, k)` | Pick k unique items | **Without** replacement |
| `random.choices(seq, k=k)` | Pick k items | **With** replacement |
| `random.shuffle(seq)` | Shuffle in-place | N/A |

**`sample()` gotchas:**
```python
random.sample([1, 2, 3], k=5)  # ValueError! k > len(sequence)
random.sample(range(100), k=5) # Works — range is a sequence

# Weighted random selection:
random.choices(["A", "B", "C"], weights=[70, 20, 10], k=1)
# A has 70% chance, B 20%, C 10%
```

### 3. Tuple Unpacking from Functions
**Concept:** Assigning multiple values from a tuple in one statement.

```python
item_a, item_b = get_two_items()
# Equivalent to:
# result = get_two_items()
# item_a = result[0]
# item_b = result[1]
```

**Extended unpacking with `*` (star expression):**
```python
first, *middle, last = [1, 2, 3, 4, 5]
# first=1, middle=[2, 3, 4], last=5

head, *tail = [1, 2, 3, 4]
# head=1, tail=[2, 3, 4]

*init, last = [1, 2, 3, 4]
# init=[1, 2, 3], last=4
```

**Nested unpacking:**
```python
(a, b), (c, d) = (1, 2), (3, 4)
# a=1, b=2, c=3, d=4

# Useful with enumerate:
for i, (name, score) in enumerate(zip(names, scores)):
    print(f"{i}: {name} - {score}")
```

### 4. String `.upper()` / `.lower()` for Input Normalization
**Concept:** Converting user input for consistent comparison.

```python
raw = input("Type 'A' or 'B': ").strip().upper()
if raw in ("A", "B"):
    ...
```

**`.upper()` vs `.lower()` — which to use?**
- `.lower()` is more common (PEP 8 names, database keys)
- `.upper()` is better for short option menus ("A", "B")
- `.casefold()` handles international chars: `"straße".casefold()` → `"strasse"`

**`str.casefold()` vs `str.lower()`:**
```python
"HELLO".lower()      # "hello"
"HELLO".casefold()   # "hello"
"Straße".lower()     # "straße" (still has ß)
"Straße".casefold()  # "strasse" (ß → ss — more aggressive)
```

### 5. For Loop with `range()` for Counting
**Concept:** Running a fixed number of iterations with a counter.

```python
for q in range(1, TOTAL_QUESTIONS + 1):  # 1, 2, 3, ..., 10
    print(f"Question {q}/{TOTAL_QUESTIONS}")
```

- `range(start, stop)` excludes `stop`
- `range(1, 11)` gives 1 through 10

**Common off-by-one patterns:**
```python
# 0-indexed (default)
for i in range(10):          # 0, 1, ..., 9

# 1-indexed (for display)
for i in range(1, 11):       # 1, 2, ..., 10

# Countdown
for i in range(10, 0, -1):   # 10, 9, ..., 1

# Using enumerate for both index and count
for i, item in enumerate(items, start=1):
    print(f"Question {i}: {item}")
```

### 6. Percentage Calculation and Formatting
**Concept:** Computing and formatting percentages.

```python
pct = (score / total) * 100
print(f"{pct:.0f}%")   # "80%" (no decimal)
print(f"{pct:.1f}%")   # "80.0%" (one decimal)
```

**Alternative — f-string `%` format spec:**
```python
ratio = 0.8
print(f"{ratio:.0%}")   # "80%" — auto-multiplies by 100!
print(f"{ratio:.1%}")   # "80.0%"
print(f"{ratio:.2%}")   # "80.00%"
# No need to manually multiply by 100
```

**Performance tier pattern (mapping score to feedback):**
```python
def get_tier(pct: float) -> str:
    if pct == 100:
        return "Perfect!"
    elif pct >= 80:
        return "Excellent"
    elif pct >= 60:
        return "Good"
    elif pct >= 40:
        return "Average"
    else:
        return "Keep practicing"
```

---

## Simple vs Production Comparison

| Aspect | Simple | Production |
|--------|--------|------------|
| **Data** | Name + followers | Name + followers + category |
| **Input validation** | Invalid = skip | Re-prompt until valid (A/B) |
| **Feedback** | None | Performance tiers (Perfect/Excellent/etc.) |
| **Replay** | Single round | Multiple rounds with cumulative stats |
| **Code structure** | Linear script | Modular functions |
| **Display** | Basic print | Formatted with section headers |
| **Question count** | Plays until wrong | Fixed question count per round |

### Why Production is Better
- **No skipped questions:** Invalid input is re-prompted, not skipped
- **Richer data:** Category information adds context to comparisons
- **Feedback loop:** Performance tiers motivate improvement
- **Replayability:** Can play multiple rounds without restarting
- **Fair scoring:** Fixed question count gives consistent difficulty
