# Band Name Generator - Python Concepts

## Core Python Concepts Used

### 1. String Concatenation & f-Strings
**Concept:** Combining strings using `+` operator vs formatted string literals.

**Simple version** uses basic concatenation:
```python
band_name = city + " " + pet
print(f"Your band name could be: {band_name}")
```

**Production version** uses `str.format()` with templates:
```python
BAND_NAME_STYLES = {
    "Classic": "The {city} {pet}",
}
name = template.format(city=city, pet=pet)
```

**All 4 ways to format strings in Python:**

| Method | Syntax | Example | When to Use |
|--------|--------|---------|-------------|
| **Concatenation** | `"a" + "b"` | `city + " " + pet` | Quick one-offs, very simple joins |
| **%-formatting** | `"Hello %s" % name` | `"Score: %d" % 10` | Legacy code (Python 2 style) |
| **`str.format()`** | `"Hi {name}".format(name=x)` | `template.format(city=city)` | Reusable templates with named placeholders |
| **f-strings** (3.6+) | `f"Hi {name}"` | `f"Band: {band_name}"` | Most readable for inline expressions |

**f-string advanced features:**
```python
name = "alice"
f"{name!r}"           # repr: "'alice'"
f"{name!s}"           # str:  "alice"
f"{name:>20}"         # Right-align in 20-char field
f"{name:^20}"         # Center-align in 20-char field
f"{3.14159:.2f}"      # Float precision: "3.14"
f"{1000000:,}"        # Thousands separator: "1,000,000"
f"{255:#x}"           # Hex with prefix: "0xff"
f"{'yes' if True else 'no'}"  # Inline ternary
```

**Closely related:** `str.join()` is preferred when concatenating many strings:
```python
parts = ["The", city, pet]
" ".join(parts)  # More efficient than repeated +
```

### 2. `input()` Function
**Concept:** Reading user input from the console. `input()` always returns a string.

```python
city = input("What's the name of the city you grew up in?\n")
```

**Key details:**
- Always returns `str`, even if user types a number
- Blocks execution until user presses Enter
- `\n` in the prompt pushes the cursor to the next line
- `input()` strips the trailing newline automatically
- Raises `EOFError` if input stream is closed (e.g., piped input ends)
- Raises `KeyboardInterrupt` on Ctrl+C

**Common pattern — converting input types:**
```python
age = int(input("Age: "))           # May raise ValueError
price = float(input("Price: "))     # May raise ValueError
```

**Safe conversion pattern:**
```python
try:
    age = int(input("Age: "))
except ValueError:
    print("That's not a valid number!")
```

### 3. String Methods
**Concept:** Built-in string methods for validation and transformation.

| Method | Purpose | Example | Return Type |
|--------|---------|---------|-------------|
| `.strip()` | Remove leading/trailing whitespace | `"  hello  ".strip()` → `"hello"` | `str` |
| `.lstrip()` | Remove leading whitespace only | `"  hello  ".lstrip()` → `"hello  "` | `str` |
| `.rstrip()` | Remove trailing whitespace only | `"  hello  ".rstrip()` → `"  hello"` | `str` |
| `.title()` | Title-case each word | `"new york".title()` → `"New York"` | `str` |
| `.capitalize()` | Capitalize first char only | `"new york".capitalize()` → `"New york"` | `str` |
| `.upper()` | Uppercase entire string | `"hello".upper()` → `"HELLO"` | `str` |
| `.lower()` | Lowercase entire string | `"YES".lower()` → `"yes"` | `str` |
| `.swapcase()` | Swap upper/lower case | `"Hello".swapcase()` → `"hELLO"` | `str` |
| `.isalpha()` | Check if all chars are alphabetic | `"Hello".isalpha()` → `True` | `bool` |
| `.isdigit()` | Check if all chars are digits | `"123".isdigit()` → `True` | `bool` |
| `.isalnum()` | Check if all chars are alphanumeric | `"abc123".isalnum()` → `True` | `bool` |
| `.isspace()` | Check if all chars are whitespace | `"  ".isspace()` → `True` | `bool` |
| `.startswith()` | Check prefix | `"hello".startswith("he")` → `True` | `bool` |
| `.endswith()` | Check suffix | `"hello.py".endswith(".py")` → `True` | `bool` |
| `.find()` | Find index of substring (-1 if missing) | `"hello".find("ll")` → `2` | `int` |
| `.index()` | Find index (raises ValueError if missing) | `"hello".index("ll")` → `2` | `int` |
| `.count()` | Count occurrences | `"banana".count("a")` → `3` | `int` |
| `.replace()` | Replace substring | `"a b".replace(" ", "")` → `"ab"` | `str` |
| `.split()` | Split into list | `"a,b,c".split(",")` → `["a","b","c"]` | `list` |
| `.join()` | Join iterable with separator | `"-".join(["a","b"])` → `"a-b"` | `str` |
| `.zfill()` | Pad with zeros on the left | `"42".zfill(5)` → `"00042"` | `str` |
| `.center()` | Center in field | `"hi".center(10, "-")` → `"----hi----"` | `str` |
| `.ljust()` | Left-justify in field | `"hi".ljust(10, ".")` → `"hi........"` | `str` |
| `.rjust()` | Right-justify in field | `"hi".rjust(10, ".")` → `"........hi"` | `str` |

**Important:** Strings are **immutable** in Python — every method returns a **new** string.

**Chaining string methods:**
```python
cleaned = raw_input.strip().lower().replace("  ", " ")
```

### 4. Functions with Type Hints
**Concept:** Defining reusable blocks of code with parameter and return type annotations.

```python
from typing import Optional

def validate_input(text: str, field_name: str) -> Optional[str]:
    """Docstring explaining the function."""
    cleaned = text.strip()
    if not cleaned:
        return None
    return cleaned.title()
```

- `Optional[str]` means the return type is either `str` or `None`
- Type hints don't enforce types at runtime but aid readability and IDE support

**Common type hints:**
```python
from typing import Optional, Union, Any

def greet(name: str) -> str:             # Takes str, returns str
def add(a: int, b: int = 0) -> int:     # Default parameter
def find(items: list[str]) -> Optional[str]:  # May return None
def process(data: Union[str, int]) -> Any:    # Multiple types
def log(msg: str) -> None:              # Returns nothing
```

**Python 3.10+ union syntax:**
```python
def find(x: str | None) -> str | int:    # Replaces Optional and Union
```

**Closely related — docstring styles:**
```python
# Google style (used in this project)
def func(arg1: str, arg2: int) -> bool:
    """Summary line.

    Args:
        arg1: Description of arg1.
        arg2: Description of arg2.

    Returns:
        Description of return value.

    Raises:
        ValueError: If arg2 is negative.
    """
```

### 5. Dictionaries
**Concept:** Key-value data structures for mapping style names to templates.

```python
BAND_NAME_STYLES = {
    "Classic": "The {city} {pet}",
    "Reversed": "The {pet} {city}",
}
for style, template in BAND_NAME_STYLES.items():
    print(style, template)
```

**Dictionary methods reference:**

| Method | Description | Example |
|--------|-------------|---------|
| `d[key]` | Get value (raises `KeyError` if missing) | `d["Classic"]` |
| `d.get(key, default)` | Get value with fallback | `d.get("Unknown", "N/A")` |
| `d[key] = value` | Set/update a key | `d["New"] = "template"` |
| `d.pop(key, default)` | Remove and return value | `d.pop("Classic", None)` |
| `d.setdefault(key, val)` | Get or insert default | `d.setdefault("X", "default")` |
| `d.update(other)` | Merge another dict | `d.update({"K": "V"})` |
| `d.items()` | Key-value pairs | `for k, v in d.items()` |
| `d.keys()` | All keys | `list(d.keys())` |
| `d.values()` | All values | `list(d.values())` |
| `key in d` | Membership check | `"Classic" in d` → `True` |
| `len(d)` | Number of entries | `len(d)` → `2` |
| `del d[key]` | Delete entry | `del d["Classic"]` |

**Dictionary comprehension:**
```python
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Filtering
evens = {k: v for k, v in squares.items() if v % 2 == 0}
# {0: 0, 2: 4, 4: 16}

# Swapping keys and values
inverted = {v: k for k, v in {"a": 1, "b": 2}.items()}
# {1: "a", 2: "b"}
```

**Closely related — `dict()` constructor:**
```python
d = dict(name="Alice", age=30)        # From keyword args
d = dict([("name", "Alice")])         # From list of tuples
d = dict.fromkeys(["a", "b"], 0)      # {"a": 0, "b": 0}
```

### 6. While Loop with Break
**Concept:** Repeating the program until the user decides to stop.

```python
while True:
    # ... game logic ...
    again = input("Generate another? (yes/no): ").strip().lower()
    if again != "yes":
        break
```

**Loop control statements:**

| Statement | Effect |
|-----------|--------|
| `break` | Exit the loop immediately |
| `continue` | Skip to the next iteration |
| `pass` | Do nothing (placeholder) |

**`while` with `else` (uncommon but useful):**
```python
attempts = 3
while attempts > 0:
    if success:
        break
    attempts -= 1
else:
    # Runs ONLY if the loop completed without break
    print("All attempts exhausted!")
```

**Closely related — `for` loop with `else`:**
```python
for item in collection:
    if item == target:
        break
else:
    print("Target not found in collection")
```

### 7. Constants (Module-Level Variables)
**Concept:** Using UPPER_CASE names for values that shouldn't change.

```python
MAX_RETRIES = 3
BAND_NAME_STYLES = { ... }
```

Python doesn't enforce immutability, but the naming convention signals intent.

**Python naming conventions (PEP 8):**

| Style | Usage | Example |
|-------|-------|---------|
| `UPPER_SNAKE_CASE` | Constants | `MAX_RETRIES = 3` |
| `lower_snake_case` | Variables, functions | `band_name`, `get_input()` |
| `PascalCase` | Classes | `class BandGenerator:` |
| `_single_leading` | "Private" (convention) | `_helper()`, `self._data` |
| `__double_leading` | Name mangling (class-internal) | `self.__secret` |
| `__dunder__` | Magic/special methods | `__init__`, `__str__` |

### 8. `if __name__ == "__main__":`
**Concept:** Entry point guard that ensures `run()` only executes when the script is run directly, not when imported.

```python
if __name__ == "__main__":
    run()
```

**How it works:**
- When a script is **run directly**: `__name__` is set to `"__main__"`
- When a script is **imported**: `__name__` is set to the module name (e.g., `"band_generator"`)

**Why it matters:**
```python
# Without guard: importing the module runs all top-level code
import band_generator  # This would trigger input() prompts!

# With guard: only functions/classes are available when imported
from band_generator import generate_band_names  # Safe import
```

### 9. `sys.exit()` — Program Termination
**Concept:** Explicitly ending the program with a status code.

```python
import sys
sys.exit(0)   # Success (default)
sys.exit(1)   # Failure / error
sys.exit("Error message")  # Prints message to stderr, exits with code 1
```

- Exit code `0` = success, any non-zero = failure
- Used by shell scripts and CI/CD pipelines to detect failures
- Raises `SystemExit` exception (can be caught with `try/except`)

### 10. Tuple Unpacking in Loops
**Concept:** Destructuring tuples directly in `for` loop variables.

```python
band_names = [("Classic", "The NYC Buddy"), ("Modern", "NYC & The Buddys")]

for style, name in band_names:
    print(f"  [{style:>10}]  {name}")
```

- Works with any iterable of fixed-length sequences
- Number of variables must match tuple length (or use `*` for remainder)

```python
first, *rest = [1, 2, 3, 4]   # first=1, rest=[2, 3, 4]
first, *mid, last = [1, 2, 3, 4]  # first=1, mid=[2, 3], last=4
```

### 11. String Alignment with f-string Format Spec
**Concept:** Right-aligning text in formatted output.

```python
f"  [{style:>10}]  {name}"
# style="Classic" → "  [   Classic]  The NYC Buddy"
```

| Spec | Meaning | Example |
|------|---------|---------|
| `>10` | Right-align in 10-char field | `"   Classic"` |
| `<10` | Left-align in 10-char field | `"Classic   "` |
| `^10` | Center in 10-char field | `" Classic  "` |
| `>10s` | Right-align string (explicit) | Same as `>10` |

---

## Simple vs Production Comparison

| Aspect | Simple | Production |
|--------|--------|------------|
| **Input validation** | None | Alphabetic check, length check, retry logic |
| **Band name styles** | 1 format | 4 different styles via dictionary templates |
| **Error handling** | Crashes on bad input | Graceful retries with informative messages |
| **Code structure** | Linear script (no functions) | Functions with type hints and docstrings |
| **Reusability** | Not importable | `if __name__` guard, modular functions |
| **Documentation** | Minimal | Full Google-style docstrings on every function |
| **Replay** | Single run | Loop with play-again option |
| **User experience** | Basic prompt | Banner, formatted output, clear errors |
| **Exit handling** | Implicit | `sys.exit(1)` on unrecoverable errors |
| **String formatting** | `+` concatenation + f-string | `str.format()` with named templates |

### Why Production is Better
- **Robustness:** Handles edge cases (empty input, special characters, too-short names)
- **Maintainability:** Each function has a single responsibility, making changes easy
- **Testability:** Functions can be unit-tested independently (`validate_input("", "city")` → `None`)
- **Extensibility:** Adding new band name styles only requires editing the dictionary
- **User experience:** Formatted output, retry logic, and a play-again loop
- **Importability:** Other modules can `from band_name_generator import generate_band_names`
