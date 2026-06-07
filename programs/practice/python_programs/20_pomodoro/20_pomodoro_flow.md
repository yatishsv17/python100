# Pomodoro Timer - Function Call Flow & Flow Diagram

## Production Version Call Graph

```
__main__
  └─> PomodoroApp()
        └─> __init__
              ├─> _load_image()
              │     └─> PIL.Image.open() → ImageTk.PhotoImage()
              │     └─> [fallback] tk.PhotoImage()
              └─> _build_widgets()
                    ├─> title_label (Timer, green)
                    ├─> canvas (tomato image + timer text)
                    ├─> start_button → start_timer
                    ├─> reset_button → reset_timer
                    └─> check_label (checkmarks)

  └─> app.run()
        └─> window.mainloop()

[Event: Start Click]
  └─> start_timer()
        ├─> start_button.config(state="disabled")
        ├─> reps += 1
        ├─> Determine session type (work/short break/long break)
        ├─> title_label.config(text, fg)
        └─> _count_down(seconds)
              ├─> Calculate minutes:seconds
              ├─> canvas.itemconfig(timer_text)
              ├─> if count > 0: window.after(1000, _count_down, count-1)
              └─> if count == 0:
                    ├─> start_timer()  [auto-start next session]
                    └─> if entering break: update checkmarks

[Event: Reset Click]
  └─> reset_timer()
        ├─> window.after_cancel(timer_id)
        ├─> reps = 0
        ├─> title_label.config(text="Timer")
        ├─> canvas.itemconfig(timer_text, text="00:00")
        ├─> check_label.config(text="")
        └─> start_button.config(state="normal")
```

## Mermaid Pomodoro Cycle

```mermaid
flowchart TD
    A[Start] --> B[Work 25 min]
    B --> C[Short Break 5 min]
    C --> D[Work 25 min]
    D --> E[Short Break 5 min]
    E --> F[Work 25 min]
    F --> G[Short Break 5 min]
    G --> H[Work 25 min]
    H --> I[Long Break 30 min]
    I --> A
```

## Timer Countdown Flow

```mermaid
flowchart TD
    S[start_timer] --> T[Determine session type]
    T --> U["_count_down(seconds)"]
    U --> V{count > 0?}
    V -- Yes --> W["Update display: MM:SS"]
    W --> X["window.after(1000, _count_down, count-1)"]
    X --> U
    V -- No --> Y[Session Complete]
    Y --> Z[Auto-start next session]
    Z --> S
```

## Class Structure

```mermaid
classDiagram
    class PomodoroApp {
        -int reps
        -timer_id
        -Tk window
        -Label title_label
        -Canvas canvas
        -Button start_button
        -Button reset_button
        -Label check_label
        +__init__()
        -_load_image()
        -_build_widgets()
        +start_timer()
        -_count_down(count)
        +reset_timer()
        +run()
    }
```
