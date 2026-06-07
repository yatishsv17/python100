# Caesar Cipher - Python Concepts

## Core Python Concepts Used

### 1. Modulo Operator (`%`)
**Concept:** Wrapping values around a fixed range — essential for circular alphabet shifting.

```python
shift = shift % 26          # Normalize: 28 → 2, 52 → 0
new_index = (index + shift) % 26  # Wrap: 25 + 3 → 2 (Z+3=C)
```

- `a % b` returns the remainder of `a / b`
- Always returns non-negative result when `b > 0`
- Key for circular/wrapping logic

**Modulo use cases in programming:**
```python
# 1. Circular indexing (wrap around)
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
(25 + 3) % 26    # 2 → wraps Z→C

# 2. Check even/odd
n % 2 == 0        # True if even

# 3. Cycle through a sequence
colors = ["red", "green", "blue"]
colors[i % len(colors)]  # Cycles through colors regardless of i

# 4. Every Nth iteration
for i in range(100):
    if i % 10 == 0:
        print(f"Progress: {i}%")

# 5. Clock arithmetic
(14 + 5) % 12    # 7 → 2:00 PM + 5 hours = 7:00 PM
```

**Python modulo with negatives (different from C/Java!):**
```python
# Python: result always has the sign of the divisor
(-3) % 26    # 23  (not -3 like in C!)
(-1) % 5     # 4
7 % -3       # -2

# This is WHY Caesar cipher decryption works:
# Shift -3 with modulo 26 → 23, which is a forward shift of 23
```

**`divmod()` — get quotient and remainder together:**
```python
quotient, remainder = divmod(28, 26)  # (1, 2)
# More efficient than computing // and % separately
```

### 2. String Indexing and `.index()`
**Concept:** Finding character positions in a string.

```python
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
index = ALPHABET.index('c')   # Returns 2
new_char = ALPHABET[5]         # Returns 'f'
```

- `.index(x)` returns the first position of `x`
- Raises `ValueError` if not found
- Strings support bracket indexing: `s[0]`, `s[-1]`

**String indexing reference:**
```python
s = "python"
s[0]      # 'p' — first character
s[-1]     # 'n' — last character
s[1:4]    # 'yth' — slice (start inclusive, end exclusive)
s[:3]     # 'pyt' — first 3 characters
s[3:]     # 'hon' — from index 3 to end
s[::-1]   # 'nohtyp' — reversed string
```

**`.index()` vs `.find()` vs `in`:**
```python
s = "hello world"
s.index("world")   # 6 — raises ValueError if not found
s.find("world")    # 6 — returns -1 if not found
"world" in s        # True — boolean check only

# Safe pattern:
if char in ALPHABET:
    idx = ALPHABET.index(char)  # Safe — we know it exists
```

**`ord()` and `chr()` — alternative to alphabet string lookup:**
```python
# Convert character to number and back
ord('a')         # 97
ord('z')         # 122
chr(97)          # 'a'

# Caesar cipher using ord/chr (alternative approach):
def shift_char(c, shift):
    if c.islower():
        return chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
    if c.isupper():
        return chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
    return c  # Non-alpha unchanged
```

### 3. String Case Methods
**Concept:** Checking and converting character case.

```python
char.isupper()    # True if uppercase
char.islower()    # True if lowercase
char.upper()      # Convert to uppercase
char.lower()      # Convert to lowercase
```

**Preserving original case during cipher:**
```python
was_upper = char.isupper()
shifted = ALPHABET[(ALPHABET.index(char.lower()) + shift) % 26]
result = shifted.upper() if was_upper else shifted
```

**`str.isalpha()` vs `str.isalnum()` vs `str.isascii()`:**

| Method | Returns True for | Example |
|--------|------------------|---------|
| `.isalpha()` | Only letters | `"abc"` ✓, `"abc1"` ✗ |
| `.isdigit()` | Only digits | `"123"` ✓, `"12.3"` ✗ |
| `.isalnum()` | Letters or digits | `"abc123"` ✓, `"abc 123"` ✗ |
| `.isascii()` | ASCII chars (0-127) | `"hello"` ✓, `"héllo"` ✗ |
| `.isprintable()` | Printable chars | `"hello"` ✓, `"hello\n"` ✗ |

### 4. List Accumulator Pattern
**Concept:** Building results efficiently with a list and joining at the end.

```python
# Efficient (production) — O(n)
result = []
for char in text:
    result.append(processed_char)
return "".join(result)

# Inefficient (simple) — O(n²)
result = ""
for char in text:
    result += processed_char  # Creates new string each time!
```

- String concatenation (`+=`) creates a new object every time — O(n²)
- List `.append()` + `"".join()` is O(n)

**Why string `+=` is O(n²):**
```python
# Each += creates a NEW string and copies all previous characters:
# Step 1: "" + "a"       → copy 1 char
# Step 2: "a" + "b"      → copy 2 chars
# Step 3: "ab" + "c"     → copy 3 chars
# ...
# Step n:                 → copy n chars
# Total copies: 1 + 2 + 3 + ... + n = n(n+1)/2 = O(n²)
```

**Alternative: list comprehension + join:**
```python
# Even more Pythonic:
result = "".join(
    process_char(c, shift) if c.isalpha() else c
    for c in text
)
```

### 5. Iterating Over Characters in a String
**Concept:** Applying different logic based on character type.

```python
for char in text:
    if char.lower() in ALPHABET:
        # Process alphabetic character
        ...
    else:
        result.append(char)  # Preserve non-alpha (spaces, punctuation)
```

**Strings are iterables in Python:**
```python
# All these work on strings:
for char in "hello":    # Iterate character by character
len("hello")            # 5
"ll" in "hello"         # True (substring check)
list("hello")           # ['h', 'e', 'l', 'l', 'o']
"hello"[2]              # 'l' (indexing)
```

**Processing patterns for character-by-character transformations:**
```python
# Pattern 1: for loop + list accumulator
result = []
for char in text:
    result.append(transform(char))
output = "".join(result)

# Pattern 2: list comprehension
output = "".join([transform(c) for c in text])

# Pattern 3: generator expression
output = "".join(transform(c) for c in text)

# Pattern 4: map()
output = "".join(map(transform, text))
```

### 6. Negative Shift for Decryption (Symmetry)
**Concept:** Using negative shift to reverse the encryption.

```python
if direction == "decrypt":
    shift = -shift
# Now (index + shift) % 26 shifts backward
```

- Negative modulo in Python always returns non-negative: `(-3) % 26 = 23`
- This means decrypt with shift=3 is the same as encrypt with shift=23
- The same function handles both encryption and decryption!

**Cryptographic principle — inverse operations:**
```python
# Encrypt: shift forward by N
# Decrypt: shift forward by (26 - N)  ← same as shifting backward by N
encrypt("hello", 3)    # "khoor"
encrypt("khoor", -3)   # "hello"  (decrypt)
encrypt("khoor", 23)   # "hello"  (same thing — 26-3=23)
```

### 7. Named Constants for Magic Numbers
**Concept:** Replacing raw numbers with descriptive names.

```python
# Bad (magic number)
new_index = (index + shift) % 26

# Good (named constant)
ALPHABET_SIZE = 26
new_index = (index + shift) % ALPHABET_SIZE
```

- Makes code self-documenting
- Single place to change if alphabet changes
- PEP 8: constants in `UPPER_SNAKE_CASE`

---

## Simple vs Production Comparison

| Aspect | Simple | Production |
|--------|--------|------------|
| **String building** | `+=` concatenation (O(n²)) | List + `join()` (O(n)) |
| **Case handling** | Lowercase only | Preserves original case |
| **Non-alpha chars** | May be lost | Preserved (spaces, punctuation) |
| **Input validation** | None | Direction, text, shift all validated |
| **Output** | Single line | Detailed summary with stats |
| **Functions** | One function | Separate input, cipher, display functions |
| **Replay** | Single run | Loop with play-again |
| **Constants** | Hardcoded string | Named constants (`ALPHABET_SIZE`) |

### Why Production is Better
- **Performance:** List accumulator pattern is O(n) vs O(n²) string concatenation
- **Robustness:** Validates all inputs before processing
- **Correctness:** Preserves case and non-alphabetic characters
- **Clarity:** Named constants and functions make code self-documenting
- **Modularity:** `caesar_cipher()` can be imported and used in other programs
- **Symmetry:** Single function handles both encrypt and decrypt via sign flip
