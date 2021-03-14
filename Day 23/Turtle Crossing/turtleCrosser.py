from turtle import Turtle


class TurtleCrosser(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(0, -270)

    def move(self):
        newX = self.xcor()
        newY = self.ycor() + 10
        self.goto(newX, newY)

    def refresh(self):
        self.goto(0, -270)
