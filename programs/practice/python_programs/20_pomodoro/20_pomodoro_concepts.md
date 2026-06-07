# Pomodoro Timer - Python Concepts

## Core Python Concepts Used

### 1. `window.after()` — Non-Blocking Timer
**Concept:** Scheduling a function call after a delay without blocking the GUI.

```python
timer_id = window.after(1000, count_down, count - 1)
# Calls count_down(count - 1) after 1000ms (1 second)
```

- Returns an ID that can be used with `after_cancel()`
- Does NOT block — GUI remains responsive
- Recursive usage creates a countdown effect

**Why not `time.sleep()`?**
```python
# BAD — freezes GUI completely:
import time
time.sleep(1)   # Blocks thread → window stops responding to events

# GOOD — schedules callback, returns immediately:
window.after(1000, my_function)  # GUI stays responsive
```

**Recursive countdown pattern:**
```python
def count_down(count):
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
    if count > 0:
        window.after(1000, count_down, count - 1)  # Schedule next tick
    else:
        on_timer_complete()  # Timer finished
```

**`after()` vs `after_idle()`:**
```python
window.after(1000, func)      # Call func after 1000ms delay
window.after(0, func)         # Call func as soon as possible (next event loop)
window.after_idle(func)       # Call func when no other events are pending
```

### 2. `window.after_cancel()` — Cancelling Scheduled Callbacks
**Concept:** Stopping a scheduled `after()` call.

```python
if self.timer_id is not None:
    window.after_cancel(self.timer_id)
    self.timer_id = None
```

**Why track the timer ID?**
```python
# after() returns an ID — save it to cancel later
self.timer_id = window.after(1000, self.count_down, count - 1)

# Cancel when user clicks Reset:
window.after_cancel(self.timer_id)

# Always set to None after cancelling to avoid stale references:
self.timer_id = None
```

### 3. Canvas Widget for Overlaying Text on Images
**Concept:** Drawing text over an image using Canvas.

```python
canvas = tk.Canvas(width=200, height=224)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white")

# Update text later:
canvas.itemconfig(timer_text, text="24:59")
```

- `create_image()` places an image at coordinates
- `create_text()` places text at coordinates
- `itemconfig()` updates existing canvas items by ID

**Canvas coordinate system:**
```python
# (0, 0) is the top-left corner
# x increases rightward, y increases downward
canvas.create_image(100, 112, image=img)  # Center of image at (100, 112)
canvas.create_text(100, 130, text="25:00", font=("Courier", 28, "bold"))
```

**Canvas vs Label for dynamic content:**
- Use **Canvas** when you need layers (text over image, shapes)
- Use **Label** for simple text or image display

### 4. PIL (Pillow) for Image Handling
**Concept:** Loading and resizing images for tkinter.

```python
from PIL import Image, ImageTk
img = Image.open("tomato.png")
img = img.resize((200, 224))
photo = ImageTk.PhotoImage(img)
```

- tkinter's native `PhotoImage` only supports GIF/PGM/PPM
- PIL/Pillow adds PNG, JPEG, etc. support

**Fallback pattern (try PIL, then native):**
```python
try:
    from PIL import Image, ImageTk
    img = Image.open("tomato.png").resize((200, 224))
    photo = ImageTk.PhotoImage(img)
except ImportError:
    photo = tk.PhotoImage(file="tomato.gif")  # Native: GIF only
```

**Common Pillow gotcha — garbage collection:**
```python
# BUG: image disappears after function returns
def load_image():
    photo = ImageTk.PhotoImage(img)
    label.config(image=photo)
    # photo goes out of scope → garbage collected → image vanishes!

# FIX: keep a reference
def load_image():
    photo = ImageTk.PhotoImage(img)
    label.config(image=photo)
    label.image = photo  # Keep reference alive!
```

### 5. `math.floor()` and Time Formatting
**Concept:** Extracting minutes and seconds from total seconds.

```python
import math
count = 1530  # seconds
minutes = math.floor(count / 60)  # 25
seconds = count % 60               # 30
text = f"{minutes:02d}:{seconds:02d}"  # "25:30"
```

- `:02d` pads with zeros to 2 digits: `5` → `"05"`

**`math.floor()` vs `//` vs `int()`:**
```python
math.floor(7.9)    # 7   — always rounds toward negative infinity
7.9 // 1           # 7.0 — floor division (returns float if float input)
int(7.9)           # 7   — truncates toward zero

# Difference with negatives:
math.floor(-2.3)   # -3  (toward -∞)
int(-2.3)          # -2  (toward 0)
-7 // 2            # -4  (toward -∞)
```

**f-string format specifiers for numbers:**
```python
f"{5:02d}"     # "05"  — zero-padded, 2 digits
f"{5:03d}"     # "005" — zero-padded, 3 digits
f"{5:>5d}"     # "    5" — right-aligned in 5 chars
f"{3.14:.2f}"  # "3.14" — 2 decimal places
f"{0.8:.0%}"   # "80%"  — percentage format
```

### 6. Global vs Instance State
**Concept:** Managing mutable state across function calls.

```python
# Simple (global — fragile)
reps = 0
timer = None
def start_timer():
    global reps, timer
    reps += 1

# Production (instance — safe)
class PomodoroApp:
    def __init__(self):
        self.reps = 0
        self.timer_id = None
    def start_timer(self):
        self.reps += 1
```

**Why `global` is problematic for GUI apps:**
```python
# Problem 1: Multiple windows share the same global state
# If two PomodoroApp windows run, they'd fight over `reps`

# Problem 2: Reset is error-prone
# Must remember to reset EVERY global variable — easy to miss one

# Problem 3: Testing requires resetting all globals between tests
```

### 7. Button State Management
**Concept:** Enabling/disabling buttons to prevent double-clicks.

```python
self.start_button.config(state="disabled")  # Can't click (greyed out)
self.start_button.config(state="normal")    # Can click (active)
```

**Button states:**

| State | Appearance | Clickable? |
|-------|-----------|------------|
| `"normal"` | Normal colors | Yes |
| `"disabled"` | Greyed out | No |
| `"active"` | Highlighted (during click) | Yes |

**Pattern: disable during processing, re-enable after:**
```python
def start_timer(self):
    self.start_button.config(state="disabled")
    # ... start countdown ...

def on_timer_complete(self):
    self.start_button.config(state="normal")
```

---

## Simple vs Production Comparison

| Aspect | Simple | Production |
|--------|--------|------------|
| **Architecture** | Procedural + globals | OOP (`PomodoroApp` class) |
| **Global state** | `global reps, timer` | Instance attributes |
| **Start button** | Always clickable (double-start bug) | Disabled during active timer |
| **Image loading** | Try PIL, fallback | Try PIL, fallback + error handling |
| **Console logging** | None | Session transitions logged |
| **Window config** | Resizable | Non-resizable, styled buttons |
| **Timer cancel** | May leave orphan callbacks | Properly tracks and cancels ID |

### Why Production is Better
- **No globals:** All state encapsulated in `PomodoroApp`
- **Button safety:** Can't accidentally double-start the timer
- **Logging:** Console logs help debug session transitions
- **Robustness:** Graceful image loading with multiple fallbacks
- **Clean reset:** Timer ID tracking prevents orphaned callbacks
