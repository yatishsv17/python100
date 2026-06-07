# US States Game - Python Concepts

## Core Python Concepts Used

### 1. CSV File Reading with `csv.DictReader`
**Concept:** Reading CSV files into dictionaries with column headers as keys.

```python
import csv
with open("50_states.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["state"], row["x"], row["y"])
        # Each row is an OrderedDict: {"state": "Alabama", "x": "139", "y": "-77"}
```

| CSV Reader | Returns | Use |
|------------|---------|-----|
| `csv.reader(f)` | Lists of strings per row | Simple, no headers |
| `csv.DictReader(f)` | Dicts with header keys | Named column access |
| `csv.writer(f)` | Write lists as CSV rows | Output data |
| `csv.DictWriter(f, fieldnames)` | Write dicts as CSV rows | Named column output |

**`csv.reader` vs `csv.DictReader`:**
```python
# csv.reader — access by index
reader = csv.reader(f)
for row in reader:
    print(row[0], row[1])     # By position — fragile if columns change

# csv.DictReader — access by name
reader = csv.DictReader(f)
for row in reader:
    print(row["state"], row["x"])  # By name — resilient to column reorder
```

**CSV gotchas:**
```python
# All values are STRINGS — must convert explicitly
x = int(row["x"])              # String → int
y = float(row["y"])            # String → float

# Handle missing values
value = row.get("optional_col", "")  # Default if column missing
```

### 2. Turtle `textinput()` Dialog
**Concept:** GUI input dialog instead of console `input()`.

```python
answer = screen.textinput(title="Game Title", prompt="Enter a state:")
# Returns string or None (if cancelled)
```

- Returns `None` if user clicks Cancel or closes dialog
- Always check for `None` before processing

**Turtle dialog functions:**
```python
# Text input (returns str or None)
name = screen.textinput("Title", "Enter name:")

# Numeric input (returns float or None)
age = screen.numinput("Title", "Enter age:", default=0, minval=0, maxval=120)
```

**Safe handling of `None` return:**
```python
answer = screen.textinput("Game", "Enter a state:")
if answer is None:
    break                      # User cancelled — exit game
answer = answer.strip().title()  # Normalize: "  new york  " → "New York"
```

### 3. Turtle `addshape()` and Background Images
**Concept:** Loading custom images as turtle shapes or screen backgrounds.

```python
screen.addshape("map.gif")    # Register the image
turtle.shape("map.gif")       # Set as current shape
```

- Only supports `.gif` format natively
- Image becomes the turtle's shape (displayed at turtle position)

**Alternative — `bgpic()` for backgrounds:**
```python
screen.bgpic("map.gif")       # Set background image directly
# Difference: bgpic is a static background, addshape moves with turtle
```

### 4. Writing Text on Canvas
**Concept:** Placing text at specific coordinates using turtle.

```python
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.goto(x, y)
writer.write("Alabama", align="center", font=("Arial", 8, "normal"))
```

**`turtle.write()` parameters:**
```python
t.write(
    "text",
    move=False,           # Whether turtle moves to end of text
    align="center",       # "left", "center", or "right"
    font=("Arial", 12, "bold")  # (family, size, style)
)
# style: "normal", "bold", "italic", "bold italic"
```

### 5. Sets for Efficient Membership Tracking
**Concept:** Tracking guessed states with O(1) lookups.

```python
guessed: set[str] = set()
guessed.add("Alabama")
if "Alabama" in guessed:   # O(1)
    print("Already guessed!")
```

**List vs Set lookup performance:**
```python
# 50 states — difference is tiny
# 1,000,000 items — difference is huge:
# List: O(n) — checks each element sequentially
# Set:  O(1) — hash-based, constant time

import timeit
big_list = list(range(1_000_000))
big_set = set(range(1_000_000))
# "999999 in big_list" → ~30ms
# "999999 in big_set"  → ~0.05ms (600× faster!)
```

**Set operations for game analysis:**
```python
all_states = set(states_data.keys())
guessed = {"Alabama", "Alaska", "Arizona"}
missing = all_states - guessed          # States not yet guessed
pct = len(guessed) / len(all_states) * 100
```

### 6. CSV Writing
**Concept:** Saving structured data to CSV files.

```python
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["state"])           # Header row
    for state in missing:
        writer.writerow([state])         # Data rows
```

- `newline=""` prevents double newlines on Windows
- `.writerow()` for single rows, `.writerows()` for multiple

**Why `newline=""`?**
```python
# Without newline="": Windows adds \r\n, csv adds \n → double newlines
# With newline="":    csv module handles line endings correctly

# writerow vs writerows:
writer.writerow(["a", "b"])              # Single row: a,b
writer.writerows([["a", "b"], ["c", "d"]])  # Multiple rows at once
```

**`csv.DictWriter` for named columns:**
```python
with open("output.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["state", "x", "y"])
    writer.writeheader()                # Writes header row
    writer.writerow({"state": "Alabama", "x": 139, "y": -77})
```

### 7. `time.time()` for Elapsed Time
**Concept:** Measuring how long something takes.

```python
import time
start = time.time()
# ... do work ...
elapsed = time.time() - start
print(f"Took {elapsed:.0f} seconds")
```

**Formatting elapsed time:**
```python
elapsed = 185  # seconds
minutes, seconds = divmod(elapsed, 60)
print(f"{int(minutes)}m {int(seconds)}s")  # "3m 5s"

# Or using timedelta for automatic formatting:
from datetime import timedelta
print(str(timedelta(seconds=elapsed)))  # "0:03:05"
```

---

## Simple vs Production Comparison

| Aspect | Simple | Production |
|--------|--------|------------|
| **Data structure** | Dict (states) + List (guessed) | Dict (states) + Set (guessed) |
| **File validation** | None — crashes on missing files | Checks CSV and image exist |
| **High score** | None | Persisted to file |
| **Timing** | None | Tracks elapsed game time |
| **Output** | Basic score print | Full statistics summary |
| **Path handling** | `os.path` | `pathlib.Path` |
| **States to learn** | Unsorted list | Sorted alphabetically in CSV |
| **Input handling** | No None check | Handles Cancel/None gracefully |

### Why Production is Better
- **Persistence:** High scores saved across sessions
- **Performance:** Set-based lookup is O(1) vs list O(n)
- **Validation:** Won't crash if files are missing
- **Statistics:** Time tracking and percentage display
- **Sorted output:** `states_to_learn.csv` is alphabetically sorted
- **Learning tool:** Missing states CSV helps study what was missed
