# Tip Calculator - Python Concepts

## Core Python Concepts Used

### 1. Type Casting (`float()`, `int()`)
**Concept:** Converting strings from `input()` to numeric types.

```python
bill = float(input("Total bill? $"))   # str -> float
tip = int(input("Tip percentage? "))   # str -> int
```

- `float()` handles decimals: `"12.50"` → `12.5`
- `int()` requires whole numbers: `"10"` → `10`, `"10.5"` → ValueError

**All built-in type conversion functions:**

| Function | Converts To | Example | Notes |
|----------|-------------|---------|-------|
| `int(x)` | Integer | `int("42")` → `42` | Truncates floats: `int(3.9)` → `3` |
| `int(x, base)` | Integer from base | `int("ff", 16)` → `255` | Base 2, 8, 16, etc. |
| `float(x)` | Float | `float("3.14")` → `3.14` | Also: `float("inf")`, `float("nan")` |
| `str(x)` | String | `str(42)` → `"42"` | Calls `__str__()` |
| `bool(x)` | Boolean | `bool(0)` → `False` | Falsy: `0`, `""`, `None`, `[]`, `{}` |
| `list(x)` | List | `list("abc")` → `["a","b","c"]` | From any iterable |
| `tuple(x)` | Tuple | `tuple([1,2])` → `(1, 2)` | From any iterable |
| `set(x)` | Set | `set([1,1,2])` → `{1, 2}` | Removes duplicates |

**Truthy and Falsy values (closely related to `bool()`):**
```python
# Falsy values (evaluate to False in boolean context):
bool(0)         # False
bool(0.0)       # False
bool("")        # False
bool(None)      # False
bool([])        # False
bool({})        # False
bool(set())     # False

# Everything else is Truthy:
bool(1)         # True
bool(-1)        # True
bool("hello")   # True
bool([0])       # True (non-empty list, even if contents are falsy)
```

**`int()` truncation vs `round()`:**
```python
int(3.9)     # 3   — truncates toward zero
int(-3.9)    # -3  — truncates toward zero
round(3.9)   # 4   — rounds to nearest
round(-3.5)  # -4  — banker's rounding
```

### 2. Arithmetic Operators
**Concept:** Mathematical operations for bill calculation.

```python
tip_amount = bill * (tip / 100)   # Multiplication and division
total = bill + tip_amount          # Addition
per_person = total / people        # Division (always returns float)
```

**Complete operator reference:**

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `/` | True division | `10 / 3` | `3.333...` (always float) |
| `//` | Floor division | `10 // 3` | `3` (rounds toward -∞) |
| `%` | Modulo (remainder) | `10 % 3` | `1` |
| `**` | Exponentiation | `2 ** 10` | `1024` |

**Floor division gotcha with negatives:**
```python
10 // 3    #  3  (rounds toward -∞)
-10 // 3   # -4  (NOT -3! rounds toward -∞)
10 // -3   # -4
```

**Augmented assignment operators:**
```python
x = 10
x += 5     # x = x + 5  → 15
x -= 3     # x = x - 3  → 12
x *= 2     # x = x * 2  → 24
x /= 4     # x = x / 4  → 6.0
x //= 2    # x = x // 2 → 3.0
x %= 2     # x = x % 2  → 1.0
x **= 3    # x = x ** 3 → 1.0
```

**Operator precedence (highest to lowest):**
1. `**` (exponentiation)
2. `+x`, `-x`, `~x` (unary)
3. `*`, `/`, `//`, `%`
4. `+`, `-`
5. `==`, `!=`, `<`, `>`, `<=`, `>=`, `in`, `not in`, `is`, `is not`
6. `not`
7. `and`
8. `or`

**Underscore in numeric literals (Python 3.6+):**
```python
bill > 10_000    # Same as 10000, more readable
population = 7_900_000_000
hex_color = 0xFF_FF_FF
```

### 3. String Formatting (f-strings) — Numeric Formatting
**Concept:** Embedding expressions and formatting numbers inside strings.

```python
print(f"Each person should pay: ${per_person:.2f}")
```

**Numeric format specifiers:**

| Spec | Meaning | Example | Result |
|------|---------|---------|--------|
| `:.2f` | 2 decimal places | `f"{3.14159:.2f}"` | `"3.14"` |
| `:.0f` | No decimals | `f"{3.7:.0f}"` | `"4"` |
| `:,` | Thousands separator | `f"{1234567:,}"` | `"1,234,567"` |
| `:,.2f` | Thousands + 2 decimals | `f"{1234.5:,.2f}"` | `"1,234.50"` |
| `:.2%` | Percentage | `f"{0.15:.2%}"` | `"15.00%"` |
| `:.1%` | Percentage 1 decimal | `f"{0.156:.1%}"` | `"15.6%"` |
| `:>10.2f` | Right-align + decimals | `f"{3.14:>10.2f}"` | `"      3.14"` |
| `:010.2f` | Zero-padded | `f"{3.14:010.2f}"` | `0000003.14` |
| `:+.2f` | Force sign | `f"{3.14:+.2f}"` | `"+3.14"` |
| `:e` | Scientific notation | `f"{0.00123:e}"` | `"1.230000e-03"` |
| `:.2e` | Scientific 2 decimals | `f"{0.00123:.2e}"` | `"1.23e-03"` |

**Closely related — currency formatting with `locale`:**
```python
import locale
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
locale.currency(1234.56, grouping=True)  # "$1,234.56"
```

### 4. Try/Except for Error Handling
**Concept:** Catching exceptions to prevent crashes on invalid input.

```python
try:
    bill = float(raw)
except ValueError:
    print(f"Error: '{raw}' is not a valid number.")
```

**Full try/except/else/finally syntax:**
```python
try:
    result = risky_operation()
except ValueError as e:
    print(f"Value error: {e}")
except (TypeError, KeyError) as e:
    print(f"Type or key error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    # Runs ONLY if no exception was raised
    print(f"Success: {result}")
finally:
    # ALWAYS runs, even if an exception was raised
    cleanup()
```

**Common built-in exceptions hierarchy:**
```
BaseException
 ├── SystemExit                  # sys.exit()
 ├── KeyboardInterrupt           # Ctrl+C
 └── Exception
      ├── ValueError             # Invalid value (e.g., float("abc"))
      ├── TypeError              # Wrong type (e.g., "a" + 1)
      ├── KeyError               # Missing dict key
      ├── IndexError             # List index out of range
      ├── AttributeError         # Missing attribute
      ├── FileNotFoundError      # File doesn't exist
      ├── ZeroDivisionError      # Division by zero
      ├── NameError              # Undefined variable
      ├── ImportError             # Failed import
      │    └── ModuleNotFoundError
      ├── OSError                # OS-level error
      │    ├── FileExistsError
      │    ├── PermissionError
      │    └── IsADirectoryError
      ├── RuntimeError           # Generic runtime error
      │    └── RecursionError    # Max recursion depth exceeded
      └── StopIteration          # Iterator exhausted
```

**Raising exceptions:**
```python
raise ValueError("Bill cannot be negative")
raise TypeError(f"Expected float, got {type(bill).__name__}")
```

**`continue` in try/except loops (pattern used in this program):**
```python
for attempt in range(MAX_RETRIES):
    try:
        bill = float(input("Bill? "))
    except ValueError:
        print("Invalid!")
        continue   # Skip to next iteration — retry
    return bill    # Success — exit function
return None        # All retries exhausted
```

### 5. Tuples for Immutable Collections
**Concept:** Fixed collections used for valid options.

```python
VALID_TIP_PERCENTAGES = (10, 12, 15)
if tip not in VALID_TIP_PERCENTAGES:
    print("Invalid tip")
```

- Tuples are immutable (can't be changed after creation)
- Use `in` to check membership
- Slightly faster than lists for membership checks

**Tuple vs List vs Set comparison:**

| Feature | Tuple `()` | List `[]` | Set `{}` |
|---------|-----------|-----------|----------|
| **Mutable** | No | Yes | Yes |
| **Ordered** | Yes | Yes | No |
| **Duplicates** | Allowed | Allowed | No |
| **Indexable** | Yes `t[0]` | Yes `l[0]` | No |
| **Hashable** | Yes (can be dict key) | No | No |
| **`in` check** | O(n) | O(n) | O(1) |
| **Use case** | Fixed data, dict keys | Mutable sequences | Membership tests |

**Tuple creation gotchas:**
```python
t = (1, 2, 3)       # Tuple with 3 elements
t = (1,)             # Single-element tuple (comma required!)
t = (1)              # NOT a tuple — this is just int 1
t = ()               # Empty tuple
t = tuple([1, 2])    # From list
t = 1, 2, 3         # Implicit tuple (no parentheses needed)
```

**Named tuples (closely related):**
```python
from collections import namedtuple
Result = namedtuple("Result", ["tip_amount", "total", "per_person"])
r = Result(15.0, 115.0, 57.5)
print(r.tip_amount)  # 15.0 — accessed by name, not index
```

### 6. Dictionary Return Values
**Concept:** Returning structured data from functions.

```python
def calculate_split(bill, tip_pct, people) -> dict:
    return {
        "tip_amount": round(tip_amount, 2),
        "total": round(total, 2),
        "per_person": per_person,
    }
```

- Dictionaries provide named access to results
- More readable than returning multiple values or tuples

**Alternative patterns for returning structured data:**
```python
# 1. Tuple (positional — fragile if order changes)
def calc() -> tuple[float, float, float]:
    return tip_amount, total, per_person
tip, total, pp = calc()

# 2. Dictionary (named — used in this program)
def calc() -> dict:
    return {"tip_amount": 15.0, "total": 115.0}
result = calc()
result["tip_amount"]

# 3. NamedTuple (named + immutable)
from typing import NamedTuple
class BillResult(NamedTuple):
    tip_amount: float
    total: float
    per_person: float

# 4. Dataclass (named + mutable + methods)
from dataclasses import dataclass
@dataclass
class BillResult:
    tip_amount: float
    total: float
    per_person: float
```

### 7. `round()` Function
**Concept:** Rounding numbers to a specified number of decimal places.

```python
per_person = round(total / people, 2)  # Round to 2 decimal places
```

- `round(3.14159, 2)` → `3.14`
- `round(3.5)` → `4` (banker's rounding in Python 3)

**Banker's rounding explained:**
```python
round(0.5)   # 0  (rounds to nearest even)
round(1.5)   # 2  (rounds to nearest even)
round(2.5)   # 2  (rounds to nearest even)
round(3.5)   # 4  (rounds to nearest even)
```

This reduces cumulative rounding bias in financial calculations.

**For precise financial math, use `decimal` module:**
```python
from decimal import Decimal, ROUND_HALF_UP
price = Decimal("10.055")
price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)  # Decimal('10.06')
```

**Why `float` arithmetic can be surprising:**
```python
0.1 + 0.2          # 0.30000000000000004 (IEEE 754 floating point)
round(0.1 + 0.2, 1)  # 0.3 (round fixes display)
```

### 8. `not in` Membership Test
**Concept:** Checking whether a value is absent from a collection.

```python
if tip not in VALID_TIP_PERCENTAGES:
    print("Invalid tip")
```

**All membership operators:**

| Operator | Meaning | Example |
|----------|---------|---------|
| `in` | Is present | `10 in (10, 12, 15)` → `True` |
| `not in` | Is absent | `20 not in (10, 12, 15)` → `True` |

Works with: `list`, `tuple`, `set`, `dict` (checks keys), `str` (substring check):
```python
"ll" in "hello"      # True (substring search)
"x" not in "hello"   # True
"key" in {"key": 1}  # True (checks keys, not values)
```

### 9. Generator Expression in `str.join()`
**Concept:** Lazily generating values for string joining.

```python
options = ", ".join(str(p) for p in VALID_TIP_PERCENTAGES)
# "10, 12, 15"
```

**Generator expression vs list comprehension:**
```python
# List comprehension — builds entire list in memory
[str(p) for p in range(1000000)]

# Generator expression — produces values one at a time (lazy)
(str(p) for p in range(1000000))
```

- Generators use less memory for large iterables
- When passed as the only argument to a function, outer parentheses are optional:
  ```python
  ", ".join(str(p) for p in items)  # Parentheses of join() suffice
  sum(x**2 for x in range(10))     # Same pattern
  ```

---

## Simple vs Production Comparison

| Aspect | Simple | Production |
|--------|--------|------------|
| **Input validation** | None — crashes on bad input | Try/except with retry loop |
| **Error messages** | None | Clear, descriptive error messages per field |
| **Warnings** | None | Warns on unusual values ($10K+ bill, 20+ people) |
| **Output** | Single line result | Full breakdown table with labels |
| **Code structure** | Linear script, no functions | Separate function per validation step |
| **Replay** | Single run | Loop with play-again option |
| **Type safety** | No type hints | Full `Optional[float]`, `Optional[int]` annotations |
| **Rounding** | f-string display only | `round()` on actual values before returning |
| **Data return** | Inline calculation | Dictionary with named fields |

### Why Production is Better
- **Reliability:** Won't crash on non-numeric input; retries gracefully
- **Transparency:** Shows complete breakdown (bill, tip amount, total, per person)
- **Reusability:** `calculate_split()` can be imported and unit-tested independently
- **Usability:** Warnings help catch typos (e.g., $100000 instead of $100)
- **Precision:** `round()` ensures actual values are rounded, not just display
- **Maintainability:** Each function handles one concern (SRP — Single Responsibility Principle)
