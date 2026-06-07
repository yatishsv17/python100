"""
Pong Game - Production Version
=================================

WHAT THIS PROGRAM DOES (Flow):
1. Set up screen (800x600, black background, manual rendering)
2. Create Paddle objects for Player A (left) and Player B (right)
3. Create Ball object at center with initial velocity
4. Create Scoreboard object
5. Draw center line
6. Bind keyboard events for both players
7. Game loop (~200 FPS):
   a. Ball.move() — update position by velocity
   b. Ball.bounce_walls() — reverse dy on top/bottom collision
   c. Check paddle collisions — reverse dx, increase speed slightly
   d. Check scoring — reset ball, increment score
8. Game runs indefinitely

INPUTS:
- Player A: 'w' (up), 's' (down)
- Player B: Up arrow (up), Down arrow (down)

OUTPUTS:
- Visual game: paddles, ball, center line, scores (turtle window)

SIDE EFFECTS:
- Opens turtle graphics window, keyboard event listeners

RULES:
- Ball bounces off top/bottom walls
- Ball bounces off paddles (speed increases slightly each hit)
- Score when ball passes opponent's side
- Paddles clamped to screen boundaries
- Ball resets to center after scoring

ASSUMPTIONS:
- Two players at same keyboard
- Turtle graphics with keyboard events supported

DEPENDENCIES:
- turtle (standard library)
- time (standard library)
"""

import turtle
import time

SCREEN_W = 800
SCREEN_H = 600
PADDLE_SPEED = 20
BALL_INITIAL_SPEED = 2
BALL_SPEED_INCREMENT = 0.2
MAX_BALL_SPEED = 6
PADDLE_HALF_HEIGHT = 50
BOUNDARY_Y = 290
PADDLE_X = 350
COLLISION_X = 330


class Paddle:
    """A player's paddle.

    Attributes:
        t: The turtle object.
        speed: Movement speed per key press.
    """

    def __init__(self, x: int, color: str = "white") -> None:
        """Create a paddle at the given x position.

        Args:
            x: Horizontal position.
            color: Paddle color.
        """
        self.t = turtle.Turtle()
        self.t.shape("square")
        self.t.color(color)
        self.t.shapesize(stretch_wid=5, stretch_len=1)
        self.t.penup()
        self.t.goto(x, 0)
        self.speed = PADDLE_SPEED

    def move_up(self) -> None:
        """Move paddle up if within bounds."""
        if self.t.ycor() < BOUNDARY_Y - PADDLE_HALF_HEIGHT:
            self.t.sety(self.t.ycor() + self.speed)

    def move_down(self) -> None:
        """Move paddle down if within bounds."""
        if self.t.ycor() > -BOUNDARY_Y + PADDLE_HALF_HEIGHT:
            self.t.sety(self.t.ycor() - self.speed)

    @property
    def y(self) -> float:
        return self.t.ycor()


class Ball:
    """The game ball with velocity and collision logic.

    Attributes:
        t: The turtle object.
        dx: Horizontal velocity.
        dy: Vertical velocity.
    """

    def __init__(self) -> None:
        """Create ball at center."""
        self.t = turtle.Turtle()
        self.t.shape("square")
        self.t.color("white")
        self.t.penup()
        self.dx = BALL_INITIAL_SPEED
        self.dy = BALL_INITIAL_SPEED

    def move(self) -> None:
        """Update ball position."""
        self.t.setx(self.t.xcor() + self.dx)
        self.t.sety(self.t.ycor() + self.dy)

    def bounce_walls(self) -> None:
        """Bounce off top and bottom walls."""
        if self.t.ycor() > BOUNDARY_Y:
            self.t.sety(BOUNDARY_Y)
            self.dy *= -1
        elif self.t.ycor() < -BOUNDARY_Y:
            self.t.sety(-BOUNDARY_Y)
            self.dy *= -1

    def bounce_paddle(self, paddle_side: str) -> None:
        """Bounce off a paddle and slightly increase speed.

        Args:
            paddle_side: 'left' or 'right'.
        """
        self.dx *= -1
        # Slight speed increase
        if abs(self.dx) < MAX_BALL_SPEED:
            self.dx += BALL_SPEED_INCREMENT if self.dx > 0 else -BALL_SPEED_INCREMENT
        # Set ball x to avoid repeated collision
        if paddle_side == "right":
            self.t.setx(COLLISION_X)
        else:
            self.t.setx(-COLLISION_X)

    def reset(self) -> None:
        """Reset ball to center and reverse direction."""
        self.t.goto(0, 0)
        self.dx = BALL_INITIAL_SPEED if self.dx < 0 else -BALL_INITIAL_SPEED
        self.dy = BALL_INITIAL_SPEED

    def hits_paddle(self, paddle: Paddle, side: str) -> bool:
        """Check if ball collides with a paddle.

        Args:
            paddle: The Paddle object.
            side: 'left' or 'right'.

        Returns:
            True if collision detected.
        """
        bx = self.t.xcor()
        if side == "right" and bx > COLLISION_X and bx < PADDLE_X:
            if abs(self.t.ycor() - paddle.y) < PADDLE_HALF_HEIGHT:
                return True
        elif side == "left" and bx < -COLLISION_X and bx > -PADDLE_X:
            if abs(self.t.ycor() - paddle.y) < PADDLE_HALF_HEIGHT:
                return True
        return False

    def past_right(self) -> bool:
        """Check if ball passed right boundary."""
        return self.t.xcor() > PADDLE_X + 40

    def past_left(self) -> bool:
        """Check if ball passed left boundary."""
        return self.t.xcor() < -PADDLE_X - 40


class Scoreboard:
    """Displays scores for both players."""

    def __init__(self) -> None:
        self.score_a = 0
        self.score_b = 0
        self.writer = turtle.Turtle()
        self.writer.color("white")
        self.writer.penup()
        self.writer.hideturtle()
        self.writer.goto(0, 260)
        self.update()

    def update(self) -> None:
        """Refresh score display."""
        self.writer.clear()
        self.writer.write(
            f"Player A: {self.score_a}    Player B: {self.score_b}",
            align="center",
            font=("Courier", 18, "normal"),
        )

    def point_a(self) -> None:
        """Award point to Player A."""
        self.score_a += 1
        self.update()

    def point_b(self) -> None:
        """Award point to Player B."""
        self.score_b += 1
        self.update()


def draw_center_line(screen: turtle.Screen) -> None:
    """Draw a dashed center line.

    Args:
        screen: The turtle Screen object.
    """
    line = turtle.Turtle()
    line.color("white")
    line.penup()
    line.hideturtle()
    line.goto(0, 300)
    line.setheading(270)
    for _ in range(30):
        line.pendown()
        line.forward(10)
        line.penup()
        line.forward(10)


def run() -> None:
    """Main game loop."""
    screen = turtle.Screen()
    screen.title("Pong Game")
    screen.bgcolor("black")
    screen.setup(width=SCREEN_W, height=SCREEN_H)
    screen.tracer(0)

    paddle_a = Paddle(-PADDLE_X)
    paddle_b = Paddle(PADDLE_X)
    ball = Ball()
    scoreboard = Scoreboard()
    draw_center_line(screen)

    screen.listen()
    screen.onkey(paddle_a.move_up, "w")
    screen.onkey(paddle_a.move_down, "s")
    screen.onkey(paddle_b.move_up, "Up")
    screen.onkey(paddle_b.move_down, "Down")

    while True:
        screen.update()
        time.sleep(0.005)

        ball.move()
        ball.bounce_walls()

        # Paddle collisions
        if ball.hits_paddle(paddle_b, "right"):
            ball.bounce_paddle("right")
        if ball.hits_paddle(paddle_a, "left"):
            ball.bounce_paddle("left")

        # Scoring
        if ball.past_right():
            scoreboard.point_a()
            ball.reset()
        if ball.past_left():
            scoreboard.point_b()
            ball.reset()


if __name__ == "__main__":
    run()
