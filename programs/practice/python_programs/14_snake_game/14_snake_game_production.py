"""
Snake Game - Production Version
=================================

WHAT THIS PROGRAM DOES (Flow):
1. Set up turtle screen (600x600, black background)
2. Create Snake object (manages head + body segments)
3. Create Food object (random position)
4. Create Scoreboard object (score + high score)
5. Bind keyboard events (WASD + arrow keys)
6. Game loop at ~10 FPS:
   a. Snake.move() — shift body segments, move head
   b. Check food collision (distance < 15) → extend snake, reposition food, score++
   c. Check wall collision (|x| > 290 or |y| > 290) → reset game
   d. Check self collision (distance to any body seg < 10) → reset game
7. Track high score across resets

INPUTS:
- W/Up: move up
- S/Down: move down
- A/Left: move left
- D/Right: move right

OUTPUTS:
- Visual game: snake, food, scoreboard (turtle window)
- High score persists across game resets within session

SIDE EFFECTS:
- Opens turtle graphics window
- Keyboard event listeners

RULES:
- Snake grows when eating food
- Wall or self collision resets the game
- High score tracked across resets
- Cannot reverse direction (e.g., can't go down while going up)

ASSUMPTIONS:
- Turtle graphics and keyboard events supported
- 20px grid alignment, 600x600 screen

DEPENDENCIES:
- turtle (standard library)
- time (standard library)
- random (standard library)
"""

import turtle
import time
import random

SCREEN_W = 600
SCREEN_H = 600
GRID_SIZE = 20
BOUNDARY = 290
GAME_SPEED = 0.1


class Scoreboard:
    """Displays and tracks score and high score."""

    def __init__(self) -> None:
        self.score = 0
        self.high_score = 0
        self.writer = turtle.Turtle()
        self.writer.color("white")
        self.writer.penup()
        self.writer.hideturtle()
        self.writer.goto(0, 270)
        self.update()

    def update(self) -> None:
        """Refresh the score display."""
        self.writer.clear()
        self.writer.write(
            f"Score: {self.score}  High Score: {self.high_score}",
            align="center",
            font=("Courier", 16, "normal"),
        )

    def increment(self) -> None:
        """Increment score by 1."""
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.update()

    def reset(self) -> None:
        """Reset score to 0, preserve high score."""
        self.score = 0
        self.update()


class Food:
    """Represents the food item on screen."""

    def __init__(self) -> None:
        self.t = turtle.Turtle()
        self.t.shape("circle")
        self.t.color("red")
        self.t.penup()
        self.t.shapesize(0.5, 0.5)
        self.reposition()

    def reposition(self) -> None:
        """Move food to a random location on the grid."""
        x = random.randint(-BOUNDARY + 10, BOUNDARY - 10)
        y = random.randint(-BOUNDARY + 10, BOUNDARY - 10)
        # Snap to grid
        x = round(x / GRID_SIZE) * GRID_SIZE
        y = round(y / GRID_SIZE) * GRID_SIZE
        self.t.goto(x, y)


class Snake:
    """Manages the snake: head, body, movement, and direction."""

    DIRECTIONS = {
        "up": (0, GRID_SIZE),
        "down": (0, -GRID_SIZE),
        "left": (-GRID_SIZE, 0),
        "right": (GRID_SIZE, 0),
    }
    OPPOSITES = {"up": "down", "down": "up", "left": "right", "right": "left"}

    def __init__(self) -> None:
        self.segments: list[turtle.Turtle] = []
        self.direction = "stop"
        self._create_head()

    def _create_head(self) -> None:
        """Create the head segment."""
        head = turtle.Turtle()
        head.shape("square")
        head.color("white")
        head.penup()
        head.goto(0, 0)
        self.segments.append(head)

    @property
    def head(self) -> turtle.Turtle:
        """Return the head segment."""
        return self.segments[0]

    def set_direction(self, new_dir: str) -> None:
        """Set direction if not reversing.

        Args:
            new_dir: The new direction to set.
        """
        if self.direction != self.OPPOSITES.get(new_dir, ""):
            self.direction = new_dir

    def move(self) -> None:
        """Move all segments: body follows, head moves in direction."""
        if self.direction == "stop":
            return

        # Shift body segments
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)

        # Move head
        dx, dy = self.DIRECTIONS[self.direction]
        self.head.setx(self.head.xcor() + dx)
        self.head.sety(self.head.ycor() + dy)

    def extend(self) -> None:
        """Add a new segment to the snake."""
        seg = turtle.Turtle()
        seg.shape("square")
        seg.color("grey")
        seg.penup()
        self.segments.append(seg)

    def reset(self) -> None:
        """Reset snake to initial state."""
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self._create_head()
        self.direction = "stop"

    def hit_wall(self) -> bool:
        """Check if head is beyond boundary."""
        return (abs(self.head.xcor()) > BOUNDARY or
                abs(self.head.ycor()) > BOUNDARY)

    def hit_self(self) -> bool:
        """Check if head collides with any body segment."""
        for seg in self.segments[1:]:
            if self.head.distance(seg) < 10:
                return True
        return False


def run() -> None:
    """Main game loop."""
    screen = turtle.Screen()
    screen.title("Snake Game")
    screen.bgcolor("black")
    screen.setup(width=SCREEN_W, height=SCREEN_H)
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(lambda: snake.set_direction("up"), "w")
    screen.onkey(lambda: snake.set_direction("down"), "s")
    screen.onkey(lambda: snake.set_direction("left"), "a")
    screen.onkey(lambda: snake.set_direction("right"), "d")
    screen.onkey(lambda: snake.set_direction("up"), "Up")
    screen.onkey(lambda: snake.set_direction("down"), "Down")
    screen.onkey(lambda: snake.set_direction("left"), "Left")
    screen.onkey(lambda: snake.set_direction("right"), "Right")

    while True:
        screen.update()
        time.sleep(GAME_SPEED)

        snake.move()

        # Food collision
        if snake.head.distance(food.t) < 15:
            food.reposition()
            snake.extend()
            scoreboard.increment()

        # Wall collision
        if snake.hit_wall():
            snake.reset()
            scoreboard.reset()

        # Self collision
        if snake.hit_self():
            snake.reset()
            scoreboard.reset()


if __name__ == "__main__":
    run()
