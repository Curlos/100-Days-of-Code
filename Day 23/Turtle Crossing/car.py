from turtle import Turtle
import random


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.speed = random.randrange(3, 10)
        self.penup()
        self.setheading(180)
        self.randomColor()
        self.goToRandomPos()

    def randomColor(self):
        r = random.random()
        g = random.random()
        b = random.random()
        self.color((r, g, b))

    def goToRandomPos(self):
        newY = random.randrange(-250, 300)
        self.goto(300, newY)

    def drive(self):
        self.forward(self.speed)
