# Snake Game - Python Concepts

## Core Python Concepts Used

### 1. Game Loop Pattern
**Concept:** Continuously updating game state at a fixed interval.

```python
while True:
    screen.update()    # Render frame
    time.sleep(0.1)    # ~10 FPS
    snake.move()       # Update state
    # Check collisions...
```

- `screen.tracer(0)` disables auto-rendering (manual control)
- `screen.update()` manually renders one frame
- `time.sleep()` controls game speed (frames per second)

**Game loop anatomy:**
```python
# 1. Setup phase (runs once)
screen = turtle.Screen()
screen.tracer(0)         # Disable auto-refresh
snake = Snake()
food = Food()

# 2. Game loop (runs every frame)
game_running = True
while game_running:
    screen.update()      # RENDER: draw current state
    time.sleep(0.1)      # WAIT: control frame rate
    snake.move()         # UPDATE: advance game state
    check_collisions()   # LOGIC: detect events
```

**Frame rate and `time.sleep()`:**
```python
import time
time.sleep(0.1)    # 100ms delay → ~10 FPS
time.sleep(0.05)   # 50ms delay → ~20 FPS (faster game)
time.sleep(0.2)    # 200ms delay → ~5 FPS (slower game)

# Dynamic speed (increase over time):
delay = 0.1
delay = max(0.03, delay - 0.005)  # Get faster but cap at 30+ FPS
```

### 2. Coordinate-Based Movement
**Concept:** Moving objects by changing x/y coordinates on a grid.

```python
DIRECTIONS = {
    "up":    (0, 20),     # y increases
    "down":  (0, -20),    # y decreases
    "left":  (-20, 0),    # x decreases
    "right": (20, 0),     # x increases
}
dx, dy = DIRECTIONS[self.direction]
head.setx(head.xcor() + dx)
head.sety(head.ycor() + dy)
```

**Opposite direction prevention (snake can't reverse):**
```python
OPPOSITES = {"up": "down", "down": "up", "left": "right", "right": "left"}

def set_direction(self, new_dir: str) -> None:
    if new_dir != OPPOSITES.get(self.direction):
        self.direction = new_dir
    # Ignores invalid direction changes (can't go backward)
```

**Grid snapping (aligning to grid):**
```python
GRID_SIZE = 20

def snap_to_grid(x: float) -> int:
    """Snap a coordinate to the nearest grid position."""
    return round(x / GRID_SIZE) * GRID_SIZE

# Food always appears on grid-aligned positions:
x = random.randrange(-280, 280, GRID_SIZE)  # -280, -260, ..., 260
y = random.randrange(-280, 280, GRID_SIZE)
```

### 3. Collision Detection
**Concept:** Using distance-based checks for object interaction.

```python
# Food collision (within 15 pixels)
if head.distance(food) < 15:
    # Eat food

# Wall collision (boundary check)
if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
    # Hit wall

# Self collision
for seg in segments[1:]:
    if head.distance(seg) < 10:
        # Hit self
```

**Types of collision detection:**

| Method | How It Works | Use Case |
|--------|-------------|----------|
| **Distance-based** | `a.distance(b) < threshold` | Circle/point collision |
| **Bounding box** | Check x/y overlap of rectangles | Grid-based games |
| **Pixel-perfect** | Check actual pixel overlap | Complex shapes |
| **Boundary** | Compare coord to wall limits | Wall collision |

**`turtle.distance()` — Euclidean distance:**
```python
# distance = sqrt((x2-x1)² + (y2-y1)²)
head.distance(food)    # Returns float — distance in pixels
head.distance(0, 0)    # Distance from origin

# Why < 15 and not == 0?
# Objects move in steps (20px). They may never be at exact same position.
# Threshold accounts for "close enough" to overlap.
```

### 4. `@property` Decorator
**Concept:** Clean access to derived attributes without calling a method.

```python
@property
def head(self) -> turtle.Turtle:
    return self.segments[0]

# Usage: snake.head (not snake.head())
```

**Why use `@property` here?**
- `snake.head` reads naturally — it's a noun, not an action
- The head is always `segments[0]` — no need to store separately
- If implementation changes (e.g., different data structure), callers don't change

### 5. Lambda Functions for Event Binding
**Concept:** Creating inline functions for keyboard event handlers.

```python
screen.onkey(lambda: snake.set_direction("up"), "w")
# Equivalent to:
# def go_up(): snake.set_direction("up")
# screen.onkey(go_up, "w")
```

**Why lambdas work well for event binding:**
```python
# Without lambda: need 4 separate named functions
def go_up():    snake.set_direction("up")
def go_down():  snake.set_direction("down")
def go_left():  snake.set_direction("left")
def go_right(): snake.set_direction("right")

# With lambda: 4 inline one-liners
for key, direction in [("w", "up"), ("s", "down"), ("a", "left"), ("d", "right")]:
    screen.onkey(lambda d=direction: snake.set_direction(d), key)
```

**Lambda closure gotcha — default argument trick:**
```python
# BUG: All lambdas share the same `direction` variable
for key, direction in bindings:
    screen.onkey(lambda: snake.set_direction(direction), key)
    # All keys will use the LAST value of `direction`!

# FIX: Use default argument to capture current value
for key, direction in bindings:
    screen.onkey(lambda d=direction: snake.set_direction(d), key)
    # Each lambda captures its own copy of `direction`
```

### 6. Segment Following Algorithm
**Concept:** Each body segment moves to the previous segment's position.

```python
# From tail to head (reverse iteration)
for i in range(len(segments) - 1, 0, -1):
    x = segments[i - 1].xcor()
    y = segments[i - 1].ycor()
    segments[i].goto(x, y)
# Then move head in current direction
```

**Why iterate in reverse?**
```python
# Forward iteration would overwrite positions before they're read:
# seg[0] → seg[1] → seg[2]
# Moving seg[1] to seg[0]'s position BEFORE seg[2] reads seg[1]'s old position
# = Bug! All segments stack on head.

# Reverse iteration preserves the chain:
# seg[2] ← seg[1] ← seg[0]
# seg[2] reads seg[1]'s position first, THEN seg[1] reads seg[0]'s position
```

### 7. Multiple Classes for Game Objects (Composition)
**Concept:** Separating game entities into dedicated classes.

| Class | Responsibility | State |
|-------|---------------|-------|
| `Snake` | Movement, direction, segments | `segments`, `direction` |
| `Food` | Random positioning | `position` |
| `Scoreboard` | Display, score tracking | `score`, `high_score` |

**How they interact (composition):**
```python
# Main game orchestrates the objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Each object is independent but the game loop connects them:
if snake.head.distance(food) < 15:  # Snake interacts with Food
    food.refresh()                   # Food repositions
    snake.extend()                   # Snake grows
    scoreboard.increase_score()      # Scoreboard updates
```

---

## Simple vs Production Comparison

| Aspect | Simple | Production |
|--------|--------|------------|
| **Architecture** | Procedural with globals | OOP (Snake, Food, Scoreboard) |
| **Direction logic** | Separate functions per direction | `set_direction()` with opposites map |
| **High score** | None | Tracked across resets |
| **Constants** | Magic numbers (290, 20, 15) | Named constants (`GRID_SIZE`, `BOUNDARY`) |
| **Grid alignment** | No snapping | Food snaps to grid via `randrange` |
| **Collision** | Inline checks | Methods `hit_wall()`, `hit_self()` |
| **Reset** | Duplicated code | `snake.reset()`, `scoreboard.reset()` |
| **Speed** | Fixed | Can increase dynamically |

### Why Production is Better
- **No code duplication:** Reset logic lives in one place per class
- **High score:** Motivates players across multiple rounds
- **Grid alignment:** Food appears at consistent positions
- **Maintainability:** Each class can be modified independently
- **Testability:** Can test Snake movement and collision in isolation
- **Extensibility:** Easy to add power-ups, obstacles, or new game modes
