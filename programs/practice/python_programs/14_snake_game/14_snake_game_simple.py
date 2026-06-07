"""
Snake Game - Simple Version
==============================

WHAT THIS PROGRAM DOES (Flow):
1. Set up turtle screen with black background
2. Create snake (list of square segments)
3. Create food at random position
4. Create scoreboard
5. Game loop:
   a. Move snake forward
   b. Check for food collision → grow snake, move food, increment score
   c. Check for wall collision → reset
   d. Check for tail collision → reset
6. Listen for WASD/arrow key inputs to change direction

INPUTS:
- W/Up: move up
- S/Down: move down
- A/Left: move left
- D/Right: move right

OUTPUTS:
- Visual game display with snake, food, score (turtle window)

SIDE EFFECTS:
- Opens a turtle graphics window, listens for keyboard events

RULES:
- Snake grows when eating food
- Game resets on wall or self collision
- Score resets on death

ASSUMPTIONS:
- Turtle module available with keyboard support
- Simple collision detection sufficient

DEPENDENCIES:
- turtle (standard library)
- time (standard library)
- random (standard library)
"""

import turtle
import time
import random

# Screen setup
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Snake
segments = []
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"
segments.append(head)

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.5, 0.5)
food.goto(random.randint(-280, 280), random.randint(-280, 280))

# Score
score = 0
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 270)
score_display.write(f"Score: {score}", align="center", font=("Courier", 18, "normal"))


def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    x, y = head.xcor(), head.ycor()
    if head.direction == "up":
        head.sety(y + 20)
    elif head.direction == "down":
        head.sety(y - 20)
    elif head.direction == "left":
        head.setx(x - 20)
    elif head.direction == "right":
        head.setx(x + 20)


screen.listen()
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_left, "a")
screen.onkey(go_right, "d")
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

while True:
    screen.update()
    time.sleep(0.1)

    if head.direction == "stop":
        continue

    # Move body segments (from tail to head)
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    move()

    # Food collision
    if head.distance(food) < 15:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))
        new_seg = turtle.Turtle()
        new_seg.shape("square")
        new_seg.color("grey")
        new_seg.penup()
        segments.append(new_seg)
        score += 1
        score_display.clear()
        score_display.write(f"Score: {score}", align="center",
                            font=("Courier", 18, "normal"))

    # Wall collision
    if (head.xcor() > 290 or head.xcor() < -290 or
            head.ycor() > 290 or head.ycor() < -290):
        head.goto(0, 0)
        head.direction = "stop"
        for seg in segments[1:]:
            seg.goto(1000, 1000)
        segments.clear()
        segments.append(head)
        score = 0
        score_display.clear()
        score_display.write(f"Score: {score}", align="center",
                            font=("Courier", 18, "normal"))

    # Tail collision
    for seg in segments[1:]:
        if head.distance(seg) < 10:
            head.goto(0, 0)
            head.direction = "stop"
            for s in segments[1:]:
                s.goto(1000, 1000)
            segments.clear()
            segments.append(head)
            score = 0
            score_display.clear()
            score_display.write(f"Score: {score}", align="center",
                                font=("Courier", 18, "normal"))
            break
