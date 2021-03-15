from turtle import Turtle


class State(Turtle):
    def __init__(self, stateName, color, x, y):
        super().__init__()
        self.hideturtle()
        self.color(color)
        self.penup()
        self.goto(x, y)
        self.write(f"{stateName}", font=("Verdana",
                                         10, "normal"))
