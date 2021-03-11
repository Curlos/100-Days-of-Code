from turtle import Turtle, Screen
from random import randrange

screen = Screen()

turtles = []
colors = ["purple", "blue", "green", "yellow",
          "orange", "red", "black"]


def get_in_start_pos():
    for i, color in enumerate(colors):
        newTurtle = Turtle()
        newTurtle.color(color)
        newTurtle.shape("turtle")
        newTurtle.penup()
        turtles.append(newTurtle)

        # First turtle (the purple one) will be set to the top left position
        if i == 0:
            newTurtle.goto((screen.window_width() // 2) * -1 + 20,
                           screen.window_height() // 4)
        # Each following turtle will be 80 pixels below the previous turtle
        else:
            newTurtle.goto(turtles[i - 1].pos()[0],
                           turtles[i - 1].pos()[1] - 80)


def start_race():
    finished = False

    while finished != True:
        for turtle in turtles:
            # If the turtle reaches the end of the x-axis (positive), then it reached the finish line so end the program
            if turtle.pos()[0] >= screen.window_width() // 2:
                finished = True
                winner = turtle.color()[0]

                if bet == winner:
                    print(
                        f"You won. The {winner} turtle has won the race!")
                else:
                    print(
                        f"You lose. The {winner} turtle has won the race!")
                screen.bye()
                break
            else:
                turtle.penup()
                turtle.forward(randrange(50))


bet = screen.textinput(
    "Make your bet", "Who will win the race? Enter a colour:")
get_in_start_pos()
start_race()
