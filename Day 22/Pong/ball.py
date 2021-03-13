from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")

    def moveUpRight(self):
        self.penup()
        self.setheading(90)
        self.forward(10)
        self.setheading(0)
        self.forward(10)

    def moveUpLeft(self):
        self.penup()
        self.setheading(90)
        self.forward(10)
        self.setheading(180)
        self.forward(10)

    def moveDownLeft(self):
        self.penup()
        self.setheading(270)
        self.forward(10)
        self.setheading(180)
        self.forward(10)

    def moveDownRight(self):
        self.penup()
        self.setheading(270)
        self.forward(10)
        self.setheading(0)
        self.forward(10)
