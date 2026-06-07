# Mail Merge - Python Concepts

## Core Python Concepts Used

### 1. File I/O with `open()` and Context Managers
**Concept:** Reading and writing files safely using `with` statements.

```python
# Reading
with open("template.txt", "r") as f:
    content = f.read()     # Read entire file
    # or
    lines = f.readlines()  # Read as list of lines

# Writing
with open("output.txt", "w") as f:
    f.write(content)
```

| Mode | Description | Creates? | Truncates? |
|------|-------------|----------|------------|
| `"r"` | Read (default) | No | No |
| `"w"` | Write (overwrites) | Yes | Yes |
| `"a"` | Append | Yes | No |
| `"x"` | Exclusive create | Yes (fails if exists) | N/A |
| `"r+"` | Read and write | No | No |
| `"rb"` / `"wb"` | Binary read/write | Same as above | Same |

- `with` ensures the file is closed even if an exception occurs
- `f.read()` → entire file as string
- `f.readlines()` → list of lines (includes `\n`)
- `f.readline()` → single line

**Context manager protocol (`with` statement):**
```python
# with statement is equivalent to:
f = open("file.txt")
try:
    content = f.read()
finally:
    f.close()    # Always closes, even on exception

# with is cleaner:
with open("file.txt") as f:
    content = f.read()
# f is automatically closed here
```

**Writing methods:**
```python
with open("output.txt", "w") as f:
    f.write("Hello\n")              # Write string
    f.writelines(["a\n", "b\n"])    # Write list of strings (no auto \n)
    print("Hello", file=f)          # print() can write to files too
```

**Iterating over file lines (memory-efficient):**
```python
# Reads entire file into memory (bad for large files):
lines = f.readlines()

# Iterates line by line (memory-efficient):
with open("large_file.txt") as f:
    for line in f:          # f is an iterator — reads one line at a time
        process(line.strip())
```

### 2. `pathlib.Path` vs `os.path`
**Concept:** Modern path handling with `pathlib` (Python 3.4+).

```python
# os.path (simple version)
import os
path = os.path.join(dir, "file.txt")
os.makedirs(dir, exist_ok=True)
exists = os.path.exists(path)

# pathlib (production version)
from pathlib import Path
path = Path(dir) / "file.txt"
path.parent.mkdir(parents=True, exist_ok=True)
exists = path.exists()
content = path.read_text(encoding="utf-8")
path.write_text(content, encoding="utf-8")
```

| Feature | `os.path` | `pathlib.Path` |
|---------|-----------|----------------|
| Join paths | `os.path.join(a, b)` | `Path(a) / b` |
| Read file | `open(p).read()` | `p.read_text()` |
| Write file | `open(p, 'w').write()` | `p.write_text()` |
| Check exists | `os.path.exists(p)` | `p.exists()` |
| Get parent | `os.path.dirname(p)` | `p.parent` |
| Get filename | `os.path.basename(p)` | `p.name` |
| Get extension | `os.path.splitext(p)[1]` | `p.suffix` |
| List dir | `os.listdir(p)` | `p.iterdir()` |
| Glob pattern | `glob.glob("*.txt")` | `p.glob("*.txt")` |

**`pathlib.Path` useful properties:**
```python
p = Path("/home/user/docs/letter.txt")
p.name       # "letter.txt"
p.stem       # "letter"  (name without extension)
p.suffix     # ".txt"
p.parent     # Path("/home/user/docs")
p.parts      # ('/', 'home', 'user', 'docs', 'letter.txt')
p.is_file()  # True if file exists
p.is_dir()   # True if directory exists
```

### 3. String `.replace()` Method
**Concept:** Replacing placeholders in templates.

```python
template = "Dear [name], welcome!"
letter = template.replace("[name]", "Alice")
# "Dear Alice, welcome!"
```

- Returns a new string (strings are immutable)
- Replaces ALL occurrences by default
- Case-sensitive

**`.replace()` with count limit:**
```python
s = "aaa"
s.replace("a", "b")      # "bbb" — all occurrences
s.replace("a", "b", 1)   # "baa" — only first occurrence
```

**Alternative templating approaches:**
```python
# 1. str.replace() — simple placeholder swap
template.replace("[name]", name)

# 2. f-strings — inline expressions
f"Dear {name}, welcome!"

# 3. str.format() — positional/named
"Dear {}, welcome!".format(name)
"Dear {name}, welcome!".format(name="Alice")

# 4. string.Template — safe substitution
from string import Template
t = Template("Dear $name, welcome!")
t.substitute(name="Alice")       # "Dear Alice, welcome!"
t.safe_substitute(name="Alice")  # Won't error on missing keys

# 5. Jinja2 — production templating engine
# "Dear {{ name }}, welcome!"
```

### 4. Regular Expressions (`re` module)
**Concept:** Pattern matching and string transformation.

```python
import re
safe_name = re.sub(r"[^\w\s-]", "", name).strip()
# Keeps word chars (\w = a-z, 0-9, _), whitespace (\s), hyphens (-)
# Removes everything else
```

**Common `re` functions:**

| Function | Description | Example |
|----------|-------------|---------|
| `re.sub(pattern, repl, string)` | Replace matches | `re.sub(r"\d+", "X", "a1b2")` → `"aXbX"` |
| `re.search(pattern, string)` | Find first match | Returns `Match` or `None` |
| `re.match(pattern, string)` | Match at start only | Returns `Match` or `None` |
| `re.findall(pattern, string)` | All matches as list | `re.findall(r"\d+", "a1b2")` → `["1", "2"]` |
| `re.split(pattern, string)` | Split by pattern | `re.split(r"[,;]", "a,b;c")` → `["a","b","c"]` |

**Common regex patterns:**
```python
r"\d"       # Digit [0-9]
r"\w"       # Word char [a-zA-Z0-9_]
r"\s"       # Whitespace [ \t\n\r]
r"[^\w]"    # NOT a word char (negate with ^)
r"[a-z]+"   # One or more lowercase letters
r".*"       # Any characters (greedy)
r".*?"      # Any characters (non-greedy/lazy)
```

**Raw strings (`r"..."`) for regex:**
```python
# Without raw string: \n means newline
re.sub("\n", " ", text)    # Replaces actual newlines

# With raw string: \n is literal backslash + n
re.sub(r"\n", " ", text)   # Same — but clearer intent
re.sub(r"\d+", "", text)   # Without r: \d is not a valid escape → warning
```

### 5. List Comprehension for Filtering
**Concept:** Counting valid items concisely.

```python
count = len([n for n in names if n.strip()])
```

**Filtering patterns:**
```python
# List comprehension with filter
valid_names = [n.strip() for n in names if n.strip()]

# filter() built-in
valid_names = list(filter(str.strip, names))

# Walrus operator (:=) to avoid double .strip() (Python 3.8+)
valid_names = [stripped for n in names if (stripped := n.strip())]
```

### 6. `__file__` for Script-Relative Paths
**Concept:** Locating files relative to the script, not the current working directory.

```python
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# or
SCRIPT_DIR = Path(__file__).parent.resolve()
```

**Why this matters:**
```python
# Problem: relative paths depend on WHERE you run the script from
# Running from /home/user: open("data/names.txt") → /home/user/data/names.txt
# Running from /tmp:       open("data/names.txt") → /tmp/data/names.txt ← WRONG!

# Solution: use __file__ to get script's own directory
SCRIPT_DIR = Path(__file__).parent.resolve()
names_path = SCRIPT_DIR / "data" / "names.txt"  # Always correct
```

**`__file__` vs `__name__`:**
```python
__file__  # Path to this script: "/home/user/project/main.py"
__name__  # Module name: "__main__" if run directly, "main" if imported
```

---

## Simple vs Production Comparison

| Aspect | Simple | Production |
|--------|--------|------------|
| **Path handling** | `os.path` strings | `pathlib.Path` objects |
| **File reading** | `open()` + `with` | `path.read_text()` |
| **Validation** | None | File exists, placeholder present |
| **Name cleaning** | Basic `.strip()` | Regex sanitization for filesystem |
| **Error handling** | None — crashes | `try/except` for write errors |
| **Statistics** | Basic count | Created, skipped, errors breakdown |
| **Encoding** | Default (platform-dependent) | Explicit UTF-8 |
| **Templating** | `str.replace()` | `str.replace()` with validation |

### Why Production is Better
- **Safety:** Validates files exist before processing
- **Robustness:** Regex sanitization prevents filesystem errors from special characters
- **Observability:** Detailed statistics on created/skipped/errors
- **Encoding:** Explicit UTF-8 prevents cross-platform encoding issues
- **Modern API:** `pathlib` is more readable and Pythonic than `os.path`
- **Portable:** `__file__`-based paths work regardless of working directory
