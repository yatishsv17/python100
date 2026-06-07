"""
Pomodoro Timer - Production Version
======================================

WHAT THIS PROGRAM DOES (Flow):
1. Create PomodoroApp with tkinter window, tomato image, timer, buttons
2. Start button initiates the Pomodoro cycle:
   a. Work session (25 min) — title "Work" in green
   b. Short break (5 min) — title "Break" in pink
   c. After 4 work sessions: long break (30 min) — title "Long Break" in red
3. Timer counts down using window.after() (non-blocking)
4. Checkmarks (up to 4) appear after each completed work session
5. Reset button cancels timer and clears all state
6. Console logs session transitions
7. Start button disabled during active timer, re-enabled on reset

INPUTS:
- Start button click: begins Pomodoro cycle
- Reset button click: resets timer, checkmarks, and state
- tomato.png: image file in same directory

OUTPUTS:
- Countdown timer overlaid on tomato image (MM:SS format, GUI)
- Title label color-coded by session type (GUI)
- Green checkmarks for completed work sessions (GUI)
- Console logs for session transitions

SIDE EFFECTS:
- Opens tkinter GUI window
- Uses after() for async timer callbacks
- Console output for session logging

RULES:
- Work: 25 min, Short break: 5 min, Long break: 30 min (after 4 work sessions)
- Checkmarks shown after each work session completion
- No pause — only start/reset
- Start disabled while timer active

ASSUMPTIONS:
- tkinter available
- tomato.png in same directory
- PIL installed for image handling (fallback to PhotoImage)

DEPENDENCIES:
- tkinter (standard library)
- math (standard library)
- pathlib (standard library)
"""

import tkinter as tk
import math
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.resolve()
IMAGE_PATH = SCRIPT_DIR / "tomato.png"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = "white"


class PomodoroApp:
    """Pomodoro timer GUI application.

    Attributes:
        window: The tkinter root window.
        reps: Current repetition count (odd=work, even=break).
        timer_id: The after() callback ID for cancellation.
    """

    def __init__(self) -> None:
        """Initialize the Pomodoro app."""
        self.reps: int = 0
        self.timer_id = None

        self.window = tk.Tk()
        self.window.title("Pomodoro Timer")
        self.window.config(padx=100, pady=50, bg=YELLOW)
        self.window.resizable(False, False)

        self._load_image()
        self._build_widgets()

    def _load_image(self) -> None:
        """Load the tomato image."""
        try:
            from PIL import Image, ImageTk
            img = Image.open(str(IMAGE_PATH))
            img = img.resize((200, 224))
            self.tomato_img = ImageTk.PhotoImage(img)
        except (ImportError, FileNotFoundError):
            try:
                self.tomato_img = tk.PhotoImage(file=str(IMAGE_PATH))
            except tk.TclError:
                self.tomato_img = None

    def _build_widgets(self) -> None:
        """Create and layout all GUI widgets."""
        # Title
        self.title_label = tk.Label(
            self.window, text="Timer", fg=GREEN, bg=YELLOW,
            font=("Courier", 36, "bold"),
        )
        self.title_label.grid(row=0, column=1)

        # Canvas with tomato
        self.canvas = tk.Canvas(
            self.window, width=200, height=224,
            bg=YELLOW, highlightthickness=0,
        )
        if self.tomato_img:
            self.canvas.create_image(100, 112, image=self.tomato_img)
        self.timer_text = self.canvas.create_text(
            100, 130, text="00:00", fill=WHITE,
            font=("Courier", 28, "bold"),
        )
        self.canvas.grid(row=1, column=1)

        # Buttons
        self.start_button = tk.Button(
            self.window, text="Start", command=self.start_timer,
            highlightthickness=0, font=("Arial", 12),
        )
        self.start_button.grid(row=2, column=0)

        self.reset_button = tk.Button(
            self.window, text="Reset", command=self.reset_timer,
            highlightthickness=0, font=("Arial", 12),
        )
        self.reset_button.grid(row=2, column=2)

        # Checkmarks
        self.check_label = tk.Label(
            self.window, fg=GREEN, bg=YELLOW, font=("Courier", 16),
        )
        self.check_label.grid(row=3, column=1)

    def start_timer(self) -> None:
        """Start the next Pomodoro session."""
        self.start_button.config(state="disabled")
        self.reps += 1

        if self.reps % 8 == 0:
            seconds = LONG_BREAK_MIN * 60
            self.title_label.config(text="Long Break", fg=RED)
            print(f"  [Pomodoro] Long break started ({LONG_BREAK_MIN} min)")
        elif self.reps % 2 == 0:
            seconds = SHORT_BREAK_MIN * 60
            self.title_label.config(text="Break", fg=PINK)
            print(f"  [Pomodoro] Short break started ({SHORT_BREAK_MIN} min)")
        else:
            seconds = WORK_MIN * 60
            self.title_label.config(text="Work", fg=GREEN)
            work_num = (self.reps + 1) // 2
            print(f"  [Pomodoro] Work session {work_num} started ({WORK_MIN} min)")

        self._count_down(seconds)

    def _count_down(self, count: int) -> None:
        """Recursive countdown using after().

        Args:
            count: Remaining seconds.
        """
        minutes = math.floor(count / 60)
        seconds = count % 60
        self.canvas.itemconfig(self.timer_text, text=f"{minutes:02d}:{seconds:02d}")

        if count > 0:
            self.timer_id = self.window.after(1000, self._count_down, count - 1)
        else:
            # Session complete — auto-start next
            self.start_timer()
            # Add checkmark after work session (when entering break)
            if self.reps % 2 == 0:
                work_sessions = self.reps // 2
                marks = "✔" * min(work_sessions, 4)
                self.check_label.config(text=marks)
                print(f"  [Pomodoro] Work sessions completed: {work_sessions}")

    def reset_timer(self) -> None:
        """Reset all timer state."""
        if self.timer_id is not None:
            self.window.after_cancel(self.timer_id)
            self.timer_id = None
        self.reps = 0
        self.title_label.config(text="Timer", fg=GREEN)
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.check_label.config(text="")
        self.start_button.config(state="normal")
        print("  [Pomodoro] Timer reset.")

    def run(self) -> None:
        """Start the tkinter main loop."""
        self.window.mainloop()


if __name__ == "__main__":
    app = PomodoroApp()
    app.run()
