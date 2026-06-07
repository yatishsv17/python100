# Quiz Game - Python Concepts

## Core Python Concepts Used

### 1. Modules and Imports
**Concept:** Splitting code across multiple files and importing them.

```python
# 12_quiz_main.py
from quiz_data import QUESTION_DATA
from quiz_question_model import Question
from quiz_brain import QuizBrain
```

| Import Style | Syntax | Use Case |
|-------------|--------|----------|
| Import module | `import os` | Access via `os.path` |
| Import specific | `from os import path` | Direct access to `path` |
| Import all | `from os import *` | Not recommended (pollutes namespace) |
| Alias | `import numpy as np` | Shorter name for frequent use |

**How Python finds modules (search order):**
1. Current directory
2. `PYTHONPATH` environment variable
3. Standard library
4. Installed packages (`site-packages`)

**`__init__.py` and packages:**
```python
# Directory structure:
# quiz/
#   __init__.py        ← Makes it a package
#   data.py
#   question_model.py
#   brain.py

from quiz.data import QUESTION_DATA
from quiz.question_model import Question
```

**Circular import pitfall:**
```python
# a.py imports from b.py, b.py imports from a.py → ImportError
# Fix: restructure code, use local imports, or merge modules
```

### 2. Classes and Object-Oriented Programming
**Concept:** Defining classes with attributes and methods.

```python
class Question:
    def __init__(self, text: str, answer: str):
        self.text = text       # Instance attribute
        self.answer = answer

    def check_answer(self, user_answer: str) -> bool:
        return user_answer.lower() == self.answer.lower()
```

**OOP Pillars:**
- **Encapsulation:** Data and methods bundled in classes
- **Abstraction:** Hide complexity behind simple interfaces
- **Inheritance:** Extend existing classes
- **Polymorphism:** Same interface, different behavior

**Inheritance example (closely related):**
```python
class MultipleChoiceQuestion(Question):
    def __init__(self, text, answer, choices):
        super().__init__(text, answer)  # Call parent __init__
        self.choices = choices

    def display(self):
        print(self.text)
        for i, choice in enumerate(self.choices, 1):
            print(f"  {i}. {choice}")
```

**`super().__init__()` explained:**
```python
class Child(Parent):
    def __init__(self, extra_arg):
        super().__init__()      # Initialize parent class first
        self.extra = extra_arg  # Then add child-specific attributes
```

**Class with type hints (production pattern):**
```python
class QuizBrain:
    def __init__(self, question_list: list[Question]) -> None:
        self.question_number: int = 0
        self.score: int = 0
        self.question_list: list[Question] = question_list
```

### 3. `__repr__` vs `__str__`
**Concept:** String representations for different audiences.

```python
class Question:
    def __repr__(self):
        return f"Question(text='{self.text[:30]}...', answer='{self.answer}')"

    def __str__(self):
        return self.text

q = Question("What is 2+2?", "4")
repr(q)  # "Question(text='What is 2+2?...', answer='4')" — for developers
str(q)   # "What is 2+2?" — for users
print(q) # Uses __str__ → "What is 2+2?"
```

**When each is called:**

| Context | Method Called | Purpose |
|---------|-------------|---------|
| `print(obj)` | `__str__` | User-friendly output |
| `str(obj)` | `__str__` | Explicit string conversion |
| `f"{obj}"` | `__str__` | f-string interpolation |
| `repr(obj)` | `__repr__` | Developer/debug representation |
| Typing `obj` in REPL | `__repr__` | Interactive inspection |
| `[obj]` in list display | `__repr__` | Container elements always use repr |

**Rule of thumb:**
- `__repr__` should be unambiguous (ideally valid Python to recreate the object)
- `__str__` should be readable (human-friendly)
- If only one is defined, define `__repr__` — it's the fallback for `str()` too

### 4. `enumerate()` with Start Parameter
**Concept:** Counting from a number other than 0.

```python
for i, q in enumerate(QUESTION_DATA, 1):  # Start from 1
    print(f"Q{i}: {q['question']}")
# Q1: What is...
# Q2: What is...
```

**`enumerate()` under the hood:**
```python
# enumerate() yields (index, value) tuples:
list(enumerate(["a", "b", "c"]))          # [(0, 'a'), (1, 'b'), (2, 'c')]
list(enumerate(["a", "b", "c"], start=1)) # [(1, 'a'), (2, 'b'), (3, 'c')]

# It's equivalent to:
def my_enumerate(iterable, start=0):
    n = start
    for item in iterable:
        yield n, item
        n += 1
```

### 5. List Comprehension vs Loop
**Concept:** Concise way to build lists.

```python
# Loop approach (used in production for clarity)
bank = []
for item in data:
    bank.append(Question(item["question"], item["answer"]))

# List comprehension (equivalent, more concise)
bank = [Question(item["question"], item["answer"]) for item in data]
```

**List comprehension anatomy:**
```python
[expression for item in iterable if condition]
#    ↑              ↑                  ↑
# what to add   loop variable    optional filter

# Examples:
squares = [x**2 for x in range(10)]           # [0, 1, 4, 9, ...]
evens = [x for x in range(20) if x % 2 == 0]  # [0, 2, 4, 6, ...]
upper = [s.upper() for s in words]              # Uppercase all words
```

**Related comprehension types:**
```python
# Dict comprehension
{k: v for k, v in items}

# Set comprehension
{x for x in items}

# Generator expression (lazy — doesn't build list in memory)
sum(x**2 for x in range(1000000))  # Memory-efficient
```

**When NOT to use list comprehension:**
```python
# Too complex — use a loop instead
# Bad:
result = [transform(x) for x in data if validate(x) and x.type == "A" for y in x.children]

# Good: use a loop for readability when logic is complex
result = []
for x in data:
    if validate(x) and x.type == "A":
        for y in x.children:
            result.append(transform(x))
```

### 6. Separation of Concerns (SoC)
**Concept:** Each module has a single responsibility.

| Module | Responsibility |
|--------|---------------|
| `quiz_data.py` | Store question data |
| `quiz_question_model.py` | Define Question class |
| `quiz_brain.py` | Manage quiz logic and state |
| `quiz_main.py` | Orchestrate the quiz flow |

**Benefits of SoC:**
```
quiz_data.py           ← Change data without touching logic
quiz_question_model.py ← Change model without touching data
quiz_brain.py          ← Change scoring without touching model
quiz_main.py           ← Change flow without touching anything else
```

**Closely related — MVC pattern:**

| Layer | Responsibility | Quiz Equivalent |
|-------|---------------|-----------------|
| **Model** | Data + business logic | `Question`, `QuizBrain` |
| **View** | Display/UI | `print()` statements |
| **Controller** | User input + flow | `quiz_main.py` |

### 7. Object Composition (Has-A Relationship)
**Concept:** One class uses another class as a component.

```python
class QuizBrain:
    def __init__(self, question_list: list[Question]):
        self.question_list = question_list  # QuizBrain HAS Questions
        self.question_number = 0
        self.score = 0
```

**Composition vs Inheritance:**
```python
# Inheritance (IS-A): "A dog IS an animal"
class Dog(Animal):
    pass

# Composition (HAS-A): "A quiz HAS questions"
class QuizBrain:
    def __init__(self, questions: list[Question]):
        self.questions = questions  # Component
```

- **Prefer composition over inheritance** (general OOP guideline)
- Composition is more flexible — components can be swapped at runtime
- Inheritance creates tight coupling between parent and child

---

## Simple vs Production Comparison

| Aspect | Simple | Production |
|--------|--------|------------|
| **Files** | 1 file (all-in-one) | 4 files (data, model, brain, main) |
| **Structure** | Procedural script | OOP with classes |
| **Data** | Embedded in script | Separate data module |
| **Validation** | Basic string compare | `check_answer()` method with strip/lower |
| **Extensibility** | Must edit single file | Add questions to data, swap brain logic |
| **Testability** | Can't test parts | Each class testable independently |
| **Reusability** | None | Question and QuizBrain reusable |
| **Representations** | None | `__repr__` and `__str__` for debugging |

### Why Production is Better
- **Separation of Concerns:** Each file has one job — easier to understand and modify
- **Reusability:** `Question` and `QuizBrain` classes can be used in other quiz apps
- **Testability:** Each class can be unit-tested in isolation
- **Scalability:** Adding 100 more questions only changes the data file
- **Maintainability:** Bug in scoring? Only fix `QuizBrain`. Bug in data? Only fix data module
- **Debuggability:** `__repr__` provides clear object inspection during development
