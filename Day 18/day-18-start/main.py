from turtle import Turtle, Screen
from random import random, choice, randint

tim = Turtle()
tim.shape("turtle")
tim.color("red")


def random_color():
    r = random()
    g = random()
    b = random()

    return (r, g, b)

# Challenge 1 - Draw a Square


def draw_square():
    for _ in range(4):
        tim.forward(100)
        tim.left(90)

# Challenge 2 - Draw a Dashed Line


def draw_dashed_line():
    for _ in range(15):
        tim.forward(10)
        tim.up()
        tim.forward(10)
        tim.down()

# Challenge 3 - Drawing Different Shapes


def draw_shape(forward, degrees, sides):
    r = random()
    g = random()
    b = random()
    tim.pencolor(r, g, b)

    for _ in range(sides):
        tim.forward(forward)
        tim.right(degrees)


def draw_diff_shapes():
    for i in range(3, 10):
        draw_shape(100, 360/i, i)

# Challenge 4 - Generate a Random Walk


def draw_random_walk():
    tim.pensize(15)
    tim.speed(0)
    for i in range(200):
        tim.pencolor(random_color())
        tim.setheading(choice([0, 90, 180, 270]))
        tim.forward(30)

# Challenge 5 - Draw a Spiriograph


def draw_spiriograph(sizeOfGap):
    tim.speed(0)

    for _ in range(int(360 / sizeOfGap)):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + sizeOfGap)


draw_spiriograph(5)

screen = Screen()
screen.exitonclick()
