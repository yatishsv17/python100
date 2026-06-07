# Coffee Machine - Python Concepts

## Core Python Concepts Used

### 1. Nested Dictionaries
**Concept:** Dictionaries containing other dictionaries for structured data.

```python
MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.50,
    },
}
# Access nested values
cost = MENU["espresso"]["cost"]              # 1.50
water_needed = MENU["espresso"]["ingredients"]["water"]  # 50
```

**Accessing deeply nested data safely:**
```python
# Risky — KeyError if any level is missing
value = MENU["latte"]["ingredients"]["milk"]

# Safe — chain .get() with defaults
value = MENU.get("latte", {}).get("ingredients", {}).get("milk", 0)

# Alternative — try/except
try:
    value = MENU["latte"]["ingredients"]["milk"]
except KeyError:
    value = 0
```

**Iterating nested dictionaries:**
```python
for drink_name, details in MENU.items():
    print(f"{drink_name}: ${details['cost']}")
    for ingredient, amount in details["ingredients"].items():
        print(f"  {ingredient}: {amount}")
```

### 2. Dictionary `.get()` with Default
**Concept:** Safely accessing dictionary keys that may not exist.

```python
available = resources.get("milk", 0)
# Returns the value for "milk" if it exists, otherwise 0
# Avoids KeyError unlike resources["milk"]
```

**`.get()` vs `[]` vs `setdefault()` vs `defaultdict`:**
```python
# [] — raises KeyError if missing
d["missing"]                    # KeyError!

# .get() — returns default, doesn't modify dict
d.get("missing", 0)            # 0 (d unchanged)

# .setdefault() — returns default AND adds it to dict
d.setdefault("missing", 0)     # 0 (d now has "missing": 0)

# defaultdict — auto-creates missing keys
from collections import defaultdict
d = defaultdict(int)            # Missing keys default to 0
d["new_key"] += 1               # Works! d = {"new_key": 1}

d = defaultdict(list)           # Missing keys default to []
d["colors"].append("red")       # Works! d = {"colors": ["red"]}
```

### 3. Global Mutable State vs Encapsulation
**Concept:** Managing shared state — the core architectural difference between simple and production.

```python
# Simple: global dict modified by functions (fragile)
resources = {"water": 300}
def make_coffee():
    resources["water"] -= 50  # Modifies global state — any code can break this

# Production: encapsulated in a class (safe)
class CoffeeMachine:
    def __init__(self):
        self.resources = {"water": 300}
    def make_coffee(self):
        self.resources["water"] -= 50  # Only accessible through the object
```

**Why global mutable state is problematic:**
```python
# Problem 1: Any function can modify the global
def reset():
    resources.clear()  # Oops, accidentally cleared everything

# Problem 2: Can't have two machines
# With globals, there's only one "resources" dict
# With classes: machine1 = CoffeeMachine(), machine2 = CoffeeMachine()

# Problem 3: Testing is harder
# Can't test in isolation — global state leaks between tests
```

**The `global` keyword (related):**
```python
count = 0
def increment():
    global count       # Required to modify global from inside function
    count += 1

# Without `global`, Python treats `count` as a local variable
# and raises UnboundLocalError
```

### 4. Classes for State Management
**Concept:** Using a class to bundle related data and behavior.

```python
class CoffeeMachine:
    def __init__(self):
        self.resources = dict(INITIAL_RESOURCES)
        self.money = 0.0
        self.orders_served = 0

    def report(self):
        print(f"Water: {self.resources['water']}ml")

    def make_coffee(self, drink_name):
        # All state access through self
        ...
```

**Instance creation and method calling:**
```python
machine = CoffeeMachine()       # __init__ called automatically
machine.report()                # Call method on instance
machine.make_coffee("espresso") # self = machine in the method

# Can create multiple independent machines:
machine1 = CoffeeMachine()
machine2 = CoffeeMachine()
machine1.make_coffee("latte")   # Only machine1's resources change
```

**`self` explained:**
```python
class CoffeeMachine:
    def report(self):
        print(self.money)

machine = CoffeeMachine()
machine.report()
# Python translates this to: CoffeeMachine.report(machine)
# `self` is just the instance being operated on
```

### 5. Iterating Dictionary Items
**Concept:** Looping over key-value pairs.

```python
for item, amount in ingredients.items():
    self.resources[item] -= amount

for coin_name, value in COIN_VALUES.items():
    total += count * value
```

**Three ways to iterate a dictionary:**
```python
d = {"water": 300, "milk": 200, "coffee": 100}

# Keys only (default)
for key in d:
    print(key)                # "water", "milk", "coffee"

# Values only
for val in d.values():
    print(val)                # 300, 200, 100

# Key-value pairs
for key, val in d.items():
    print(f"{key}: {val}")    # "water: 300", etc.
```

**Dictionary views are dynamic:**
```python
keys = d.keys()       # View object, NOT a list
d["sugar"] = 50       # Modify dict
print(keys)           # dict_keys(["water", "milk", "coffee", "sugar"])
# The view reflects changes to the dict!

# To get a static copy:
keys_list = list(d.keys())
```

### 6. `dict()` Constructor for Copying
**Concept:** Creating an independent copy of a dictionary.

```python
self.resources = dict(INITIAL_RESOURCES)
# Creates a shallow copy — changes to self.resources won't affect INITIAL_RESOURCES
```

**Shallow vs Deep copy:**
```python
import copy

# Shallow copy — copies top-level keys, shares nested objects
original = {"a": [1, 2, 3], "b": 4}
shallow = dict(original)      # or original.copy()
shallow["a"].append(4)        # Modifies BOTH — shared reference!
# original["a"] is now [1, 2, 3, 4]

# Deep copy — recursively copies all nested objects
deep = copy.deepcopy(original)
deep["a"].append(5)           # Only modifies deep copy
# original["a"] unchanged
```

**When to use which:**

| Method | Syntax | Nested? | Use |
|--------|--------|---------|-----|
| `dict(d)` | `dict(original)` | Shallow | Flat dicts |
| `d.copy()` | `original.copy()` | Shallow | Flat dicts |
| `{**d}` | `{**original}` | Shallow | Merging dicts |
| `copy.deepcopy(d)` | `deepcopy(original)` | Deep | Nested dicts/lists |

### 7. Floating Point Precision and `round()`
**Concept:** Handling currency calculations with floating-point precision.

```python
total = quarters * 0.25 + dimes * 0.10  # May have precision issues
total = round(total, 2)                  # Round to 2 decimal places
change = round(payment - cost, 2)
```

- `0.1 + 0.2 == 0.30000000000000004` (floating-point imprecision)
- `round()` mitigates this for display purposes

**Why floats are imprecise:**
```python
# Floats use binary (base 2) — some decimals can't be represented exactly
0.1 + 0.2 == 0.3           # False!
0.1 + 0.2                   # 0.30000000000000004

# Think of it like 1/3 in decimal: 0.333333... never terminates
# 0.1 in binary: 0.000110011001100... never terminates
```

**`decimal.Decimal` for precise money:**
```python
from decimal import Decimal
price = Decimal("1.50")
payment = Decimal("2.00")
change = payment - price       # Decimal('0.50') — exact!

# Always use string to create Decimal:
Decimal("0.1") + Decimal("0.2") == Decimal("0.3")  # True!
Decimal(0.1) + Decimal(0.2)  # Still imprecise — float already rounded
```

---

## Simple vs Production Comparison

| Aspect | Simple | Production |
|--------|--------|------------|
| **State management** | Global dict (fragile) | `CoffeeMachine` class (encapsulated) |
| **Coin validation** | None — crashes on bad input | Validates non-negative integers |
| **Order tracking** | None | `orders_served` counter |
| **Shutdown** | Silent exit | Summary statistics report |
| **Resource check** | Prints which resource is short | Shows amounts needed vs available |
| **Code structure** | Functions + global state | OOP with methods |
| **Multiple instances** | Impossible (one global state) | Multiple machines possible |

### Why Production is Better
- **Encapsulation:** All state is in the `CoffeeMachine` object — no globals
- **Robustness:** Coin input validated (no crashes on non-integer)
- **Observability:** Order tracking and shutdown summary
- **Testability:** Can create multiple machines, test independently
- **Extensibility:** Adding new drinks = add to MENU dict
- **Reusable:** Class can be imported into a GUI or web application
