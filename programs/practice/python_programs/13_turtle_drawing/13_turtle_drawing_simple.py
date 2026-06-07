"""
Turtle Drawing - Simple Version
=================================

WHAT THIS PROGRAM DOES (Flow):
1. Show menu of drawing options
2. User selects a drawing (1-6)
3. Execute the chosen drawing:
   1. Dashed Line
   2. Shapes (triangle, square, pentagon, hexagon)
   3. Random Walk
   4. Spirograph
   5. Hirst Dot Painting
   6. Etch-a-Sketch (interactive WASD)
4. Display turtle graphics on canvas

INPUTS:
- Menu choice (int): 1-6
- For Etch-a-Sketch: W/A/S/D keys, C to clear

OUTPUTS:
- Visual turtle graphics on canvas

SIDE EFFECTS:
- Opens a turtle graphics window

RULES:
- Menu choice must be 1-6
- Etch-a-Sketch uses keyboard events

ASSUMPTIONS:
- Turtle module is available
- System supports GUI windows

DEPENDENCIES:
- turtle (standard library)
- random (standard library)
"""

import turtle
import random


def draw_dashed_line():
    t = turtle.Turtle()
    t.speed("fast")
    for _ in range(15):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()


def draw_shapes():
    t = turtle.Turtle()
    t.speed("fast")
    colors = ["red", "blue", "green", "orange", "purple", "brown"]
    for sides in range(3, 9):
        t.color(colors[(sides - 3) % len(colors)])
        angle = 360 / sides
        for _ in range(sides):
            t.forward(100)
            t.right(angle)


def random_walk():
    t = turtle.Turtle()
    t.speed("fastest")
    t.pensize(3)
    colors = ["red", "blue", "green", "yellow", "orange", "purple",
              "cyan", "magenta"]
    directions = [0, 90, 180, 270]
    for _ in range(200):
        t.color(random.choice(colors))
        t.setheading(random.choice(directions))
        t.forward(20)


def draw_spirograph():
    t = turtle.Turtle()
    t.speed("fastest")
    for i in range(72):
        t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        t.circle(100)
        t.left(5)


def hirst_painting():
    t = turtle.Turtle()
    t.speed("fastest")
    t.penup()
    colors = ["red", "blue", "green", "yellow", "orange", "purple",
              "pink", "cyan", "magenta", "brown"]
    t.setheading(225)
    t.forward(250)
    t.setheading(0)

    for row in range(10):
        for col in range(10):
            t.dot(20, random.choice(colors))
            t.forward(50)
        t.setheading(90)
        t.forward(50)
        if row % 2 == 0:
            t.setheading(180)
        else:
            t.setheading(0)


def etch_a_sketch():
    t = turtle.Turtle()
    screen = turtle.Screen()

    def move_forward():
        t.forward(10)

    def move_backward():
        t.backward(10)

    def turn_left():
        t.left(10)

    def turn_right():
        t.right(10)

    def clear_screen():
        t.clear()
        t.penup()
        t.home()
        t.pendown()

    screen.listen()
    screen.onkey(move_forward, "w")
    screen.onkey(move_backward, "s")
    screen.onkey(turn_left, "a")
    screen.onkey(turn_right, "d")
    screen.onkey(clear_screen, "c")

    print("Etch-a-Sketch: W=forward, S=backward, A=left, D=right, C=clear")


print("Turtle Drawing Menu:")
print("1. Dashed Line")
print("2. Shapes")
print("3. Random Walk")
print("4. Spirograph")
print("5. Hirst Dot Painting")
print("6. Etch-a-Sketch")

choice = input("\nChoose (1-6): ")

screen = turtle.Screen()
screen.colormode(255)

if choice == "1":
    draw_dashed_line()
elif choice == "2":
    draw_shapes()
elif choice == "3":
    random_walk()
elif choice == "4":
    draw_spirograph()
elif choice == "5":
    hirst_painting()
elif choice == "6":
    etch_a_sketch()
else:
    print("Invalid choice!")

screen.exitonclick()
