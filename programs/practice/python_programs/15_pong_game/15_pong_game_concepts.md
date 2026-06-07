# Pong Game - Python Concepts

## Core Python Concepts Used

### 1. Turtle `shapesize()` for Custom Shapes
**Concept:** Stretching the default 20×20 square to create paddles.

```python
paddle.shapesize(stretch_wid=5, stretch_len=1)
# stretch_wid=5 → 5 × 20 = 100px tall
# stretch_len=1 → 1 × 20 = 20px wide
```

**Turtle shape system:**
```python
# Built-in shapes
t.shape("square")    # 20×20 default
t.shape("circle")    # 20px diameter
t.shape("turtle")    # Turtle icon
t.shape("arrow")     # Arrow pointer
t.shape("triangle")  # Triangle

# shapesize stretches the base shape
t.shapesize(stretch_wid=2, stretch_len=3)
# width: 2 × 20 = 40px,  length: 3 × 20 = 60px
```

### 2. Dynamic Attributes on Turtle Objects
**Concept:** Adding custom attributes to turtle instances at runtime.

```python
ball.dx = 2   # Not a built-in attribute — dynamically added
ball.dy = 2
ball.setx(ball.xcor() + ball.dx)
```

- Python allows adding attributes to objects at runtime
- Works but can be fragile — production version uses a proper class

**How dynamic attributes work in Python:**
```python
class Dog:
    pass

fido = Dog()
fido.name = "Fido"       # Adds attribute at runtime — Python allows this
fido.age = 3              # Another dynamic attribute

# This works because Python objects use __dict__ internally:
print(fido.__dict__)      # {"name": "Fido", "age": 3}
```

**Why proper classes are better:**
```python
# Dynamic attributes — fragile
ball.dx = 2
ball.dX = 3    # Typo! Creates a NEW attribute, no error

# Proper class — catches typos
class Ball:
    def __init__(self):
        self.dx = 2
        self.dy = 2
    # Typos in attribute access → AttributeError
```

**`__slots__` — preventing dynamic attributes:**
```python
class Ball:
    __slots__ = ("dx", "dy", "t")  # Only these attributes allowed
    def __init__(self):
        self.dx = 2
        self.dy = 2

ball = Ball()
ball.speed = 5  # AttributeError! Not in __slots__
# Benefits: faster attribute access, less memory
```

### 3. Absolute Value for Distance Checks
**Concept:** Using `abs()` to check if two objects are within range.

```python
if abs(ball.ycor() - paddle.ycor()) < 50:
    # Ball is within paddle's reach (above OR below center)
```

- `abs(-30)` → `30`
- Simplifies "within range" checks without separate above/below logic

**Pattern: range check with `abs()`:**
```python
# Without abs — need two conditions:
if ball_y - paddle_y < 50 and ball_y - paddle_y > -50:
    ...

# With abs — single clean condition:
if abs(ball_y - paddle_y) < 50:
    ...

# Equivalent using chained comparison:
if -50 < ball_y - paddle_y < 50:
    ...
```

### 4. Velocity-Based Movement (Physics Simulation)
**Concept:** Objects have dx/dy velocity components updated each frame.

```python
class Ball:
    def __init__(self):
        self.dx = 2   # pixels per frame horizontally
        self.dy = 2   # pixels per frame vertically

    def move(self):
        self.t.setx(self.t.xcor() + self.dx)
        self.t.sety(self.t.ycor() + self.dy)
```

- Bouncing = negate the velocity component: `self.dy *= -1`
- Speed increase = increment magnitude: `self.dx += 0.2`

**Bounce physics:**
```python
# Wall bounce (top/bottom): reverse vertical direction
if ball.ycor() > 280 or ball.ycor() < -280:
    ball.dy *= -1   # Flip vertical velocity

# Paddle bounce: reverse horizontal direction
if ball.xcor() > 340 and abs(ball.ycor() - paddle.ycor()) < 50:
    ball.dx *= -1   # Flip horizontal velocity
```

**Augmented assignment operators (used for velocity):**

| Operator | Equivalent | Example |
|----------|-----------|---------|
| `x += 2` | `x = x + 2` | Increment |
| `x -= 1` | `x = x - 1` | Decrement |
| `x *= -1` | `x = x * -1` | Negate (bounce) |
| `x /= 2` | `x = x / 2` | Halve |

### 5. Boundary Clamping
**Concept:** Preventing objects from going off-screen.

```python
def move_up(self):
    if self.t.ycor() < BOUNDARY_Y - PADDLE_HALF_HEIGHT:
        self.t.sety(self.t.ycor() + self.speed)
```

- Check position before moving
- Prevents paddles from leaving the visible area

**Clamping patterns:**
```python
# Pattern 1: Check before move (used here)
if new_y < max_y:
    paddle.sety(new_y)

# Pattern 2: Move then clamp
paddle.sety(new_y)
if paddle.ycor() > max_y:
    paddle.sety(max_y)

# Pattern 3: Using min/max for clamping
new_y = max(min_y, min(max_y, new_y))
paddle.sety(new_y)

# Python doesn't have a built-in clamp, but you can make one:
def clamp(value, minimum, maximum):
    return max(minimum, min(maximum, value))
```

### 6. Frame-Rate Control with `time.sleep()`
**Concept:** Using sleep intervals for consistent game speed.

```python
while True:
    screen.update()
    time.sleep(0.005)  # ~200 FPS
```

- Lower sleep = faster game, higher = slower
- `screen.tracer(0)` + `screen.update()` = manual frame control

**`time` module functions:**

| Function | Description | Example |
|----------|-------------|---------|
| `time.sleep(s)` | Pause for s seconds | `time.sleep(0.1)` |
| `time.time()` | Current time (epoch seconds) | `1700000000.123` |
| `time.perf_counter()` | High-precision timer | Benchmarking |
| `time.monotonic()` | Monotonic clock (never goes back) | Timeouts |

**Measuring frame time:**
```python
import time
start = time.perf_counter()
# ... game logic ...
elapsed = time.perf_counter() - start
sleep_time = max(0, TARGET_FRAME_TIME - elapsed)
time.sleep(sleep_time)
```

### 7. Named Constants for Game Configuration
**Concept:** Extracting magic numbers into descriptive constants.

```python
BALL_INITIAL_SPEED = 2
BALL_SPEED_INCREMENT = 0.2
MAX_BALL_SPEED = 6
PADDLE_HALF_HEIGHT = 50
```

**Benefits of named constants:**
- Self-documenting — `MAX_BALL_SPEED` vs `6`
- Single point of change — update one constant, affects all uses
- Prevents typo-bugs — IDE autocompletes constant names
- Easy tuning — all game parameters visible at file top

---

## Simple vs Production Comparison

| Aspect | Simple | Production |
|--------|--------|------------|
| **Architecture** | Procedural globals | OOP (Paddle, Ball, Scoreboard) |
| **Ball speed** | Constant throughout | Increases on paddle hit (capped at max) |
| **Center line** | None | Dashed center line drawn |
| **Constants** | Magic numbers inline | Named constants at top |
| **Collision** | Inline coordinate checks | `hits_paddle()` method |
| **Score update** | Duplicated code | `point_a()` / `point_b()` methods |
| **Paddle bounds** | Hardcoded values | Uses `BOUNDARY_Y - PADDLE_HALF_HEIGHT` |
| **Ball attributes** | Dynamic on turtle obj | Proper class with defined attributes |

### Why Production is Better
- **Progressive difficulty:** Ball speeds up on each paddle hit (capped at max)
- **Clean OOP:** Each game entity is a self-contained class
- **No duplication:** Scoring and display updates are single methods
- **Visual polish:** Center line, proper boundary calculations
- **Configurable:** Change constants to adjust game feel
- **Type safety:** Proper classes prevent attribute typo bugs
