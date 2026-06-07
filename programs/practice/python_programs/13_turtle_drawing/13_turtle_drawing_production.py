"""
Turtle Drawing - Production Version
======================================

WHAT THIS PROGRAM DOES (Flow):
1. Display welcome banner and menu
2. Validate user menu choice (1-6)
3. Set up turtle screen with appropriate settings
4. Execute chosen drawing:
   1. Dashed Line - alternating pen up/down
   2. Shapes - polygons from triangle to octagon
   3. Random Walk - random directions with colors
   4. Spirograph - overlapping circles with rotation
   5. Hirst Dot Painting - grid of colored dots
   6. Etch-a-Sketch - interactive keyboard-controlled drawing
5. Display completion message
6. Wait for click to close

INPUTS:
- Menu choice (int): 1-6
- Etch-a-Sketch: W/A/S/D keys for movement, C to clear

OUTPUTS:
- Visual turtle graphics on canvas window
- Menu and completion messages (console)

SIDE EFFECTS:
- Opens a turtle graphics window
- Listens for keyboard events (Etch-a-Sketch mode)

RULES:
- Menu choice must be 1-6
- Each drawing resets the canvas
- Etch-a-Sketch uses keyboard events

ASSUMPTIONS:
- Turtle module available and functional
- System supports GUI windows
- Fixed parameters are sufficient

DEPENDENCIES:
- turtle (standard library)
- random (standard library)
"""

import turtle
import random
from typing import Callable


class TurtleDrawer:
    """Manages turtle drawing operations.

    Attributes:
        screen: The turtle Screen object.
        t: The Turtle object for drawing.
    """

    def __init__(self) -> None:
        """Initialize screen and turtle."""
        self.screen = turtle.Screen()
        self.screen.title("Turtle Drawing")
        self.screen.setup(width=800, height=600)
        self.t = turtle.Turtle()

    def reset(self) -> None:
        """Reset turtle to default state."""
        self.t.clear()
        self.t.penup()
        self.t.home()
        self.t.pendown()
        self.t.pensize(1)
        self.t.speed("fast")
        self.t.color("black")

    def draw_dashed_line(self) -> None:
        """Draw a dashed line across the screen."""
        self.reset()
        self.t.speed("fast")
        for _ in range(20):
            self.t.forward(10)
            self.t.penup()
            self.t.forward(10)
            self.t.pendown()
        print("  Dashed line complete.")

    def draw_shapes(self) -> None:
        """Draw polygons from triangle to octagon."""
        self.reset()
        self.t.speed("fast")
        colors = ["red", "blue", "green", "orange", "purple",
                  "brown", "cyan", "magenta"]
        for sides in range(3, 11):
            self.t.color(colors[(sides - 3) % len(colors)])
            angle = 360 / sides
            for _ in range(sides):
                self.t.forward(100)
                self.t.right(angle)
        print("  Shapes complete.")

    def random_walk(self, steps: int = 200) -> None:
        """Draw a random walk with colored segments.

        Args:
            steps: Number of steps to take.
        """
        self.reset()
        self.t.speed("fastest")
        self.t.pensize(3)
        colors = ["red", "blue", "green", "yellow", "orange",
                  "purple", "cyan", "magenta"]
        directions = [0, 90, 180, 270]
        for _ in range(steps):
            self.t.color(random.choice(colors))
            self.t.setheading(random.choice(directions))
            self.t.forward(20)
        print(f"  Random walk complete ({steps} steps).")

    def draw_spirograph(self, circles: int = 72) -> None:
        """Draw a spirograph pattern.

        Args:
            circles: Number of circles to draw.
        """
        self.reset()
        self.t.speed("fastest")
        gap = 360 / circles
        for _ in range(circles):
            self.t.color(random.random(), random.random(), random.random())
            self.t.circle(100)
            self.t.left(gap)
        print(f"  Spirograph complete ({circles} circles).")

    def hirst_painting(self, rows: int = 10, cols: int = 10,
                       dot_size: int = 20, spacing: int = 50) -> None:
        """Draw a Hirst-style dot painting.

        Args:
            rows: Number of rows.
            cols: Number of columns.
            dot_size: Diameter of each dot.
            spacing: Space between dots.
        """
        self.reset()
        self.t.speed("fastest")
        self.t.hideturtle()
        colors = ["red", "blue", "green", "yellow", "orange",
                  "purple", "pink", "cyan", "magenta", "brown"]

        start_x = -(cols * spacing) / 2
        start_y = -(rows * spacing) / 2
        self.t.penup()

        for row in range(rows):
            for col in range(cols):
                x = start_x + col * spacing
                y = start_y + row * spacing
                self.t.goto(x, y)
                self.t.dot(dot_size, random.choice(colors))
        print(f"  Hirst painting complete ({rows}x{cols} dots).")

    def etch_a_sketch(self) -> None:
        """Start interactive Etch-a-Sketch mode."""
        self.reset()
        self.t.speed("fastest")

        def move_forward():
            self.t.forward(10)

        def move_backward():
            self.t.backward(10)

        def turn_left():
            self.t.left(10)

        def turn_right():
            self.t.right(10)

        def clear_canvas():
            self.reset()

        self.screen.listen()
        self.screen.onkey(move_forward, "w")
        self.screen.onkey(move_backward, "s")
        self.screen.onkey(turn_left, "a")
        self.screen.onkey(turn_right, "d")
        self.screen.onkey(clear_canvas, "c")

        print("  Etch-a-Sketch: W=fwd, S=back, A=left, D=right, C=clear")
        print("  Click the window to exit.")

    def finish(self) -> None:
        """Wait for click to close the window."""
        self.screen.exitonclick()


def get_menu_choice() -> int:
    """Display menu and get valid choice.

    Returns:
        Integer 1-6.
    """
    print("\n=== Turtle Drawing Menu ===")
    print("  1. Dashed Line")
    print("  2. Shapes (triangle to octagon)")
    print("  3. Random Walk")
    print("  4. Spirograph")
    print("  5. Hirst Dot Painting")
    print("  6. Etch-a-Sketch (interactive)")
    print("===========================\n")

    while True:
        raw = input("Choose (1-6): ").strip()
        try:
            choice = int(raw)
        except ValueError:
            print(f"  Error: '{raw}' is not a number.")
            continue
        if 1 <= choice <= 6:
            return choice
        print("  Error: Choose between 1 and 6.")


def run() -> None:
    """Main program entry."""
    choice = get_menu_choice()

    drawer = TurtleDrawer()

    actions: dict[int, Callable] = {
        1: drawer.draw_dashed_line,
        2: drawer.draw_shapes,
        3: drawer.random_walk,
        4: drawer.draw_spirograph,
        5: drawer.hirst_painting,
        6: drawer.etch_a_sketch,
    }

    actions[choice]()
    drawer.finish()


if __name__ == "__main__":
    run()
