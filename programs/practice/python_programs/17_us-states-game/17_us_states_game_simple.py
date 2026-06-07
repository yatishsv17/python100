"""
US States Game - Simple Version
==================================

WHAT THIS PROGRAM DOES (Flow):
1. Load blank US map image as turtle screen background
2. Read state data (name, x, y) from CSV file
3. Loop: ask user to guess a state name
4. If correct → write state name at correct coordinates on map
5. If user types "Exit" → end game, save unguessed states to CSV
6. Show final score

INPUTS:
- State names via turtle textinput dialog (case-insensitive)
- CSV file: 50_states.csv (state, x, y columns)
- Image file: blank_states_img.gif

OUTPUTS:
- Visual US map with guessed state names displayed (turtle window)
- states_to_learn.csv: CSV of states not guessed (file)
- Final score (console)

SIDE EFFECTS:
- Opens turtle graphics window
- Reads CSV file
- Writes states_to_learn.csv to disk

RULES:
- Must match one of the 50 US states
- Case-insensitive with title case conversion
- Game ends when all 50 guessed or user types "Exit"

ASSUMPTIONS:
- CSV and image files in same directory as script
- Turtle graphics available

DEPENDENCIES:
- turtle (standard library)
- csv (standard library)
- os (standard library)
"""

import turtle
import csv
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(SCRIPT_DIR, "50_states.csv")
IMAGE_PATH = os.path.join(SCRIPT_DIR, "blank_states_img.gif")

screen = turtle.Screen()
screen.title("US States Game")
screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)

# Read state data
states = {}
with open(CSV_PATH, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        states[row["state"].strip().title()] = (int(row["x"]), int(row["y"]))

guessed = []
total = len(states)

while len(guessed) < total:
    answer = screen.textinput(
        title=f"{len(guessed)}/{total} States Correct",
        prompt="What's another state's name?"
    )

    if answer is None or answer.strip().title() == "Exit":
        break

    answer = answer.strip().title()

    if answer in states and answer not in guessed:
        guessed.append(answer)
        x, y = states[answer]
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(x, y)
        writer.write(answer, align="center", font=("Arial", 8, "normal"))

# Save states to learn
missing = [s for s in states if s not in guessed]
if missing:
    output_path = os.path.join(SCRIPT_DIR, "states_to_learn.csv")
    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["state"])
        for state in missing:
            writer.writerow([state])

print(f"\nFinal Score: {len(guessed)}/{total}")
if missing:
    print(f"States to learn: {len(missing)}")
    print(f"Saved to states_to_learn.csv")

screen.exitonclick()
