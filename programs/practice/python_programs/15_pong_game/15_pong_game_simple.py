"""
Pong Game - Simple Version
============================

WHAT THIS PROGRAM DOES (Flow):
1. Set up turtle screen (800x600, black background)
2. Create two paddles (left for Player A, right for Player B)
3. Create ball in center
4. Create scoreboard
5. Game loop:
   a. Move ball continuously
   b. Bounce ball off top/bottom walls
   c. Detect paddle collisions → reverse ball x-direction
   d. Detect scoring (ball passes paddle) → increment score, reset ball
6. Listen for keyboard inputs to move paddles

INPUTS:
- Player A: 'w' (up), 's' (down)
- Player B: Up arrow (up), Down arrow (down)

OUTPUTS:
- Visual game: paddles, ball, scores (turtle window)

SIDE EFFECTS:
- Opens turtle graphics window, keyboard listeners

RULES:
- Ball bounces off top/bottom borders
- Ball bounces off paddles
- Score when ball passes opponent's paddle
- Paddles stay within screen boundaries

ASSUMPTIONS:
- Two players available at same keyboard
- Turtle graphics with keyboard events supported

DEPENDENCIES:
- turtle (standard library)
- time (standard library)
"""

import turtle
import time

# Screen
screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Paddle A (left)
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B (right)
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Score
score_a = 0
score_b = 0
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Player A: {score_a}  Player B: {score_b}",
                    align="center", font=("Courier", 18, "normal"))

# Paddle movement
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        paddle_a.sety(y + 20)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:
        paddle_a.sety(y - 20)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        paddle_b.sety(y + 20)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:
        paddle_b.sety(y - 20)

screen.listen()
screen.onkey(paddle_a_up, "w")
screen.onkey(paddle_a_down, "s")
screen.onkey(paddle_b_up, "Up")
screen.onkey(paddle_b_down, "Down")

# Game loop
while True:
    screen.update()
    time.sleep(0.005)

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top/bottom bounce
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Right side score (Player A scores)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        score_display.clear()
        score_display.write(f"Player A: {score_a}  Player B: {score_b}",
                            align="center", font=("Courier", 18, "normal"))

    # Left side score (Player B scores)
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        score_display.clear()
        score_display.write(f"Player A: {score_a}  Player B: {score_b}",
                            align="center", font=("Courier", 18, "normal"))

    # Paddle B collision
    if (ball.xcor() > 330 and ball.xcor() < 350 and
            abs(ball.ycor() - paddle_b.ycor()) < 50):
        ball.setx(330)
        ball.dx *= -1

    # Paddle A collision
    if (ball.xcor() < -330 and ball.xcor() > -350 and
            abs(ball.ycor() - paddle_a.ycor()) < 50):
        ball.setx(-330)
        ball.dx *= -1
