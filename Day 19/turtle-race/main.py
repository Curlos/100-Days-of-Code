from turtle import Turtle, Screen
from random import randrange

purple = Turtle()
blue = Turtle()
green = Turtle()
yellow = Turtle()
orange = Turtle()
red = Turtle()

screen = Screen()

turtles = [purple, blue, green, yellow, orange, red]
turtle_names = ["purple", "blue", "green", "yellow", "orange", "red"]


def get_in_start_pos():
    for i, turtle in enumerate(turtles):
        turtle.color(turtle_names[i])
        turtle.shape("turtle")
        turtle.penup()

        # First turtle (the purple one) will be set to the top left position
        if i == 0:
            turtle.goto((screen.window_width() // 2) * -1 + 20,
                        screen.window_height() // 4)
        # Each following turtle will be 80 pixels below the previous turtle
        else:
            turtle.goto(turtles[i - 1].pos()[0], turtles[i - 1].pos()[1] - 80)

        turtle.pendown()


def start_race():
    finished = False

    while finished != True:
        for turtle in turtles:
            # If the turtle reaches the end of the x-axis (positive)
            if turtle.pos()[0] >= screen.window_width() // 2:
                finished = True
                winner = turtle.color()[0]

                if bet == winner:
                    print(
                        f"You won. The {turtle.color()[0]} turtle has won the race!")
                else:
                    print(
                        f"You lose. The {turtle.color()[0]} turtle has won the race!")
                screen.bye()
                break
            else:
                turtle.penup()
                turtle.forward(randrange(50))


def get_mouse_click_coor(x, y):
    print(x, y)


screen.onscreenclick(get_mouse_click_coor)
bet = screen.textinput(
    "Make your bet", "Who will win the race? Enter a colour:")
get_in_start_pos()
start_race()
