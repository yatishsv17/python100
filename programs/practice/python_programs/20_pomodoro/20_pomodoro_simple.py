"""
Pomodoro Timer - Simple Version
==================================

WHAT THIS PROGRAM DOES (Flow):
1. Create tkinter window with tomato image, timer text, and buttons
2. Start button begins the Pomodoro cycle:
   a. Work session (25 min) → title turns green
   b. Short break (5 min) → title turns pink
   c. After 4 work sessions → long break (30 min) → title turns red
3. Timer counts down and updates display every second
4. Checkmarks added after each completed work session
5. Reset button clears everything

INPUTS:
- Start button click: begins timer
- Reset button click: resets timer and checkmarks
- Image file: tomato.png (in same directory)

OUTPUTS:
- Countdown timer on tomato image (MM:SS format, GUI)
- Title label color-coded by session type (GUI)
- Checkmarks for completed work sessions (GUI)

SIDE EFFECTS:
- Opens tkinter GUI window
- Uses after() for non-blocking timer

RULES:
- Work: 25 min, Short break: 5 min, Long break: 30 min
- Checkmarks after each work session (up to 4)
- Only start/reset (no pause)

ASSUMPTIONS:
- tkinter available
- tomato.png exists in same directory
- PIL for image loading (fallback to PhotoImage for .png)

DEPENDENCIES:
- tkinter (standard library)
- os (standard library)
"""

import tkinter as tk
import os
import math

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(SCRIPT_DIR, "tomato.png")

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

reps = 0
timer = None


def reset_timer():
    global reps, timer
    if timer is not None:
        window.after_cancel(timer)
    reps = 0
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        title_label.config(text="Work", fg=GREEN)


def count_down(count):
    global timer
    minutes = math.floor(count / 60)
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # Add checkmark after work session
        if reps % 2 == 0:
            marks = "✔" * (reps // 2)
            check_label.config(text=marks)


# Window
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Title
title_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW,
                        font=("Courier", 36, "bold"))
title_label.grid(row=0, column=1)

# Canvas with tomato image
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
try:
    from PIL import Image, ImageTk
    img = Image.open(IMAGE_PATH)
    img = img.resize((200, 224))
    tomato_img = ImageTk.PhotoImage(img)
except ImportError:
    tomato_img = tk.PhotoImage(file=IMAGE_PATH)

canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00",
                                 fill="white", font=("Courier", 28, "bold"))
canvas.grid(row=1, column=1)

# Buttons
start_button = tk.Button(text="Start", command=start_timer,
                          highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = tk.Button(text="Reset", command=reset_timer,
                          highlightthickness=0)
reset_button.grid(row=2, column=2)

# Check marks
check_label = tk.Label(fg=GREEN, bg=YELLOW, font=("Courier", 16))
check_label.grid(row=3, column=1)

window.mainloop()
