###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
"""import colorgram

colors = colorgram.extract('image.jpg', 84)
rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))
"""
from random import choice
from turtle import Turtle, Screen

rgb_colors = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105,
                                                                                                                                                                                                                                                             74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209), (227, 173, 177), (68, 63, 58), (111, 140, 142), (255, 194, 0), (178, 196, 202)]
turtle = Turtle()
screen = Screen()
TURTLE_SIZE_X = 40
TURTLE_SIZE_Y = 40
screen.colormode(255)
turtle.penup()
turtle.hideturtle()
turtle.goto(TURTLE_SIZE_X/2 - screen.window_width()/2,
            screen.window_height()/2 - TURTLE_SIZE_Y/2)
turtle.showturtle()

print(screen.window_width(), screen.window_height())


def draw_dots(TURTLE_SIZE_Y):
    for _ in range(16):
        for _ in range(20):
            random_color = choice(rgb_colors)
            turtle.dot(20, random_color)
            turtle.up()
            turtle.forward(50)

        turtle.hideturtle()
        TURTLE_SIZE_Y += 100
        turtle.goto(TURTLE_SIZE_X/2 - screen.window_width()/2,
                    screen.window_height()/2 - TURTLE_SIZE_Y/2)
        turtle.showturtle()


draw_dots(TURTLE_SIZE_Y)

screen.exitonclick()
