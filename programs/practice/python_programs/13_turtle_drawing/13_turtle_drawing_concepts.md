# Turtle Drawing - Python Concepts

## Core Python Concepts Used

### 1. Turtle Graphics Module
**Concept:** Built-in module for visual programming and learning.

```python
import turtle
t = turtle.Turtle()
screen = turtle.Screen()

t.forward(100)     # Move forward 100 pixels
t.right(90)        # Turn right 90 degrees
t.circle(50)       # Draw circle with radius 50
t.penup()          # Stop drawing
t.pendown()        # Start drawing
t.color("red")     # Change color
t.speed("fastest") # Set speed: "slowest", "slow", "normal", "fast", "fastest"
t.dot(20, "blue")  # Draw a dot
t.goto(x, y)       # Move to coordinates
t.home()           # Go to origin (0, 0)
t.hideturtle()     # Hide the turtle cursor
```

**Complete turtle method reference:**

| Category | Method | Description |
|----------|--------|-------------|
| **Movement** | `forward(d)` / `fd(d)` | Move forward d pixels |
| | `backward(d)` / `bk(d)` | Move backward d pixels |
| | `right(a)` / `rt(a)` | Turn right a degrees |
| | `left(a)` / `lt(a)` | Turn left a degrees |
| | `goto(x, y)` | Move to coordinates |
| | `home()` | Go to (0, 0), face east |
| | `circle(r, extent)` | Arc of radius r, extent degrees |
| **Pen** | `penup()` / `pu()` | Stop drawing |
| | `pendown()` / `pd()` | Start drawing |
| | `pensize(w)` / `width(w)` | Set line width |
| | `pencolor(c)` | Set pen color |
| **State** | `position()` / `pos()` | Current (x, y) |
| | `heading()` | Current angle |
| | `isdown()` | Is pen drawing? |
| | `xcor()`, `ycor()` | Current x or y |
| **Appearance** | `shape(name)` | `"arrow"`, `"turtle"`, `"circle"`, `"square"` |
| | `hideturtle()` / `ht()` | Hide cursor |
| | `showturtle()` / `st()` | Show cursor |
| **Color** | `color(c)` | Set pen and fill color |
| | `fillcolor(c)` | Set fill color only |
| | `begin_fill()` | Start recording fill area |
| | `end_fill()` | Fill recorded area |

**Color modes:**
```python
# Named colors
t.color("red")

# Hex colors
t.color("#FF5733")

# RGB mode (0.0 to 1.0 default)
t.color(0.5, 0.2, 0.8)

# RGB mode (0 to 255) — must set colormode first
screen.colormode(255)
t.color(128, 51, 204)  # Must be integers when colormode is 255!
```

### 2. Keyboard Event Handling (Event-Driven Programming)
**Concept:** Binding functions to keyboard events.

```python
screen.listen()                    # Start listening for events
screen.onkey(move_forward, "w")    # Bind 'w' key to function
screen.onkey(turn_left, "a")
screen.exitonclick()               # Close on mouse click
```

- `screen.listen()` must be called before `onkey()`
- Functions bound to keys must take no arguments
- Useful for interactive/game applications

**Event-driven vs sequential programming:**
```python
# Sequential: code runs top to bottom, waits for input
name = input("Name: ")  # Program BLOCKS until user types

# Event-driven: program runs, callbacks fire when events occur
screen.onkey(handler, "space")  # Program CONTINUES, handler called later
screen.mainloop()               # Keep listening for events
```

**Mouse events:**
```python
screen.onclick(handler)           # Click anywhere on screen
screen.onscreenclick(handler)     # Same (screen click)
t.onclick(handler)                # Click on turtle only

def handler(x, y):                # Mouse handlers receive x, y coords
    print(f"Clicked at ({x}, {y})")
```

### 3. Closures (Nested Functions)
**Concept:** Functions defined inside other functions that capture variables from the enclosing scope.

```python
def etch_a_sketch(self):
    def move_forward():       # Nested function (closure)
        self.t.forward(10)    # Captures 'self' from enclosing scope
    screen.onkey(move_forward, "w")
```

**How closures work:**
```python
def make_multiplier(n):
    def multiply(x):
        return x * n       # 'n' is captured from enclosing scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
double(5)   # 10
triple(5)   # 15
```

**Closures vs lambda:**
```python
# Closure (named)
def go_up():
    snake.set_direction("up")
screen.onkey(go_up, "w")

# Lambda (anonymous — equivalent)
screen.onkey(lambda: snake.set_direction("up"), "w")
```

### 4. First-Class Functions and Dispatch Pattern
**Concept:** Functions are objects — they can be stored in variables, lists, and dicts.

```python
from typing import Callable

actions: dict[int, Callable] = {
    1: drawer.draw_dashed_line,
    2: drawer.draw_shapes,
}
actions[choice]()  # Call the function mapped to the choice
```

**First-class functions explained:**
```python
def greet(name):
    return f"Hello {name}"

# Store in variable
fn = greet
fn("Alice")          # "Hello Alice"

# Pass as argument
def apply(func, arg):
    return func(arg)
apply(greet, "Bob")  # "Hello Bob"

# Store in list
funcs = [str.upper, str.lower, str.title]
[f("hello world") for f in funcs]
# ["HELLO WORLD", "hello world", "Hello World"]
```

**Dispatch pattern vs if/elif:**
```python
# Bad — long if/elif chain
if choice == 1:
    draw_dashed_line()
elif choice == 2:
    draw_shapes()
elif choice == 3:
    draw_random_walk()

# Good — dictionary dispatch
actions = {1: draw_dashed_line, 2: draw_shapes, 3: draw_random_walk}
if choice in actions:
    actions[choice]()
```

### 5. Random Colors
**Concept:** Generating random RGB colors.

```python
# Using integer RGB (0-255) — requires colormode(255)
screen.colormode(255)
t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Using named colors from a list
t.color(random.choice(["red", "blue", "green", "purple"]))
```

**Common pitfall — `colormode(255)` and floats:**
```python
screen.colormode(255)
# WRONG: random.random() returns float (0.0 to 1.0) — TypeError!
t.color(random.random(), random.random(), random.random())

# CORRECT: Use randint for integer mode
t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
```

**Helper function for random colors:**
```python
def random_color() -> tuple[int, int, int]:
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

t.color(random_color())
```

### 6. Geometry in Code
**Concept:** Using math for shapes and patterns.

```python
# Regular polygon: exterior angle = 360 / sides
for sides in range(3, 9):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(100)
        t.right(angle)

# Spirograph: rotate slightly after each circle
for _ in range(72):
    t.circle(100)
    t.left(5)      # 360/72 = 5 degrees
```

**Key geometry formulas:**
```python
# Exterior angle of regular polygon = 360 / n
# Interior angle = 180 - exterior = 180 - (360/n)
# Triangle: 360/3 = 120° exterior
# Square: 360/4 = 90° exterior
# Hexagon: 360/6 = 60° exterior

# Circle from tiny steps:
for _ in range(360):
    t.forward(1)
    t.right(1)
```

**Nested loops for patterns:**
```python
# Draw multiple polygons (triangle through octagon)
for sides in range(3, 9):        # Outer: which shape
    for _ in range(sides):       # Inner: draw that shape
        t.forward(100)
        t.right(360 / sides)
```

---

## Simple vs Production Comparison

| Aspect | Simple | Production |
|--------|--------|------------|
| **Structure** | Functions + if/elif | Class (`TurtleDrawer`) + dict dispatch |
| **Screen setup** | Default settings | Configured title, size, colormode |
| **Input validation** | None | Validated int 1-6 with retry |
| **Canvas reset** | No | `reset()` method between drawings |
| **Parameters** | Hardcoded | Configurable (steps, rows, cols) |
| **Completion feedback** | None | Console messages after each drawing |
| **Color handling** | May mix float/int | Consistent colormode with correct types |

### Why Production is Better
- **OOP:** `TurtleDrawer` class manages screen/turtle lifecycle cleanly
- **Dispatch pattern:** Dictionary of callables replaces if/elif chain
- **Configurable:** Parameters like `steps`, `rows`, `cols` allow customization
- **Reusable:** Class can be imported and used programmatically
- **Safe colors:** Consistent colormode prevents TypeError with RGB values
