"""
US States Game - Production Version
======================================

WHAT THIS PROGRAM DOES (Flow):
1. Validate required files exist (CSV, image)
2. Load state data from CSV into dictionary {name: (x, y)}
3. Load blank US map as turtle screen background
4. Load high score from file (if exists)
5. Game loop:
   a. Show textinput dialog with current score in title
   b. Validate answer: must be a real state, not already guessed
   c. If correct → write state name on map at coordinates
   d. If "Exit" → end game
6. On exit:
   a. Calculate final stats (score, percentage, time)
   b. Save unguessed states to states_to_learn.csv
   c. Update high score if beaten
   d. Display final summary

INPUTS:
- State names via turtle textinput (case-insensitive)
- 50_states.csv: state data with x, y coordinates
- blank_states_img.gif: blank US map image

OUTPUTS:
- Visual map with guessed states (turtle window)
- states_to_learn.csv: unguessed states (file)
- high_score.txt: best score (file)
- Final statistics (console)

SIDE EFFECTS:
- Opens turtle graphics window
- Reads/writes CSV and text files

RULES:
- Case-insensitive matching with title case
- Duplicate guesses silently ignored
- High score tracked across sessions

ASSUMPTIONS:
- CSV and image in same directory as script
- Turtle graphics and textinput available

DEPENDENCIES:
- turtle (standard library)
- csv (standard library)
- time (standard library)
- pathlib (standard library)
"""

import turtle
import csv
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.resolve()
CSV_PATH = SCRIPT_DIR / "50_states.csv"
IMAGE_PATH = SCRIPT_DIR / "blank_states_img.gif"
OUTPUT_PATH = SCRIPT_DIR / "states_to_learn.csv"
HIGH_SCORE_PATH = SCRIPT_DIR / "high_score.txt"


def load_states() -> dict[str, tuple[int, int]]:
    """Load state data from CSV.

    Returns:
        Dictionary mapping state names to (x, y) coordinate tuples.
    """
    states = {}
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["state"].strip().title()
            x, y = int(row["x"]), int(row["y"])
            states[name] = (x, y)
    return states


def load_high_score() -> int:
    """Load the high score from file.

    Returns:
        The high score, or 0 if file doesn't exist.
    """
    if HIGH_SCORE_PATH.exists():
        try:
            return int(HIGH_SCORE_PATH.read_text().strip())
        except (ValueError, OSError):
            pass
    return 0


def save_high_score(score: int) -> None:
    """Save a new high score.

    Args:
        score: The score to save.
    """
    HIGH_SCORE_PATH.write_text(str(score), encoding="utf-8")


def save_states_to_learn(missing: list[str]) -> None:
    """Save unguessed states to CSV.

    Args:
        missing: List of unguessed state names.
    """
    with open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["state"])
        for state in sorted(missing):
            writer.writerow([state])


def write_state_on_map(name: str, x: int, y: int) -> None:
    """Write a state name on the map at given coordinates.

    Args:
        name: State name to display.
        x: X coordinate.
        y: Y coordinate.
    """
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto(x, y)
    writer.write(name, align="center", font=("Arial", 7, "bold"))


def run() -> None:
    """Main game loop."""
    if not CSV_PATH.exists() or not IMAGE_PATH.exists():
        print("Error: Required files (50_states.csv, blank_states_img.gif) not found.")
        return

    states = load_states()
    total = len(states)
    high_score = load_high_score()

    screen = turtle.Screen()
    screen.title("US States Game")
    image_str = str(IMAGE_PATH)
    screen.addshape(image_str)
    turtle.shape(image_str)

    guessed: set[str] = set()
    start_time = time.time()

    while len(guessed) < total:
        hs_text = f" | High Score: {high_score}" if high_score > 0 else ""
        answer = screen.textinput(
            title=f"{len(guessed)}/{total} States{hs_text}",
            prompt="What's another state's name? (type 'Exit' to quit)"
        )

        if answer is None or answer.strip().lower() == "exit":
            break

        cleaned = answer.strip().title()

        if cleaned in states and cleaned not in guessed:
            guessed.add(cleaned)
            x, y = states[cleaned]
            write_state_on_map(cleaned, x, y)

    elapsed = time.time() - start_time
    score = len(guessed)
    missing = [s for s in states if s not in guessed]

    # Save outputs
    if missing:
        save_states_to_learn(missing)

    if score > high_score:
        save_high_score(score)
        print(f"  New high score: {score}!")

    # Display summary
    print(f"\n{'=' * 35}")
    print(f"  US States Game - Results")
    print(f"{'=' * 35}")
    print(f"  States guessed: {score}/{total} ({score/total*100:.0f}%)")
    print(f"  States to learn: {len(missing)}")
    print(f"  Time: {elapsed:.0f} seconds")
    print(f"  High score: {max(score, high_score)}")
    if missing:
        print(f"  Saved to: {OUTPUT_PATH.name}")
    print(f"{'=' * 35}\n")

    screen.exitonclick()


if __name__ == "__main__":
    run()
