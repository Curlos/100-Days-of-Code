from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, STARTING_POSITIONS, MOVE_DISTANCE):
        super().__init__()
        self.segments = []
        self.createPaddle(STARTING_POSITIONS)
        self.head = self.segments[0]
        self.tail = self.segments[-1]
        self.MOVE_DISTANCE = MOVE_DISTANCE

    def createPaddle(self, positions):
        for position in positions:
            self.addSegment(position)
            print(f'creating segment at position: {position}')

    def addSegment(self, position):
        newSegment = Turtle("square")
        newSegment.color("white")
        newSegment.penup()
        newSegment.goto(position)
        newSegment.speed(0)
        self.segments.append(newSegment)

    def moveUp(self):
        for segNum in range(len(self.segments) - 1, 0, -1):
            self.segments[segNum].penup()
            newX = self.segments[segNum - 1].xcor()
            newY = self.segments[segNum - 1].ycor()
            newY = (newY + (self.MOVE_DISTANCE - 20))
            self.segments[segNum].setpos(newX, newY)
        self.head.forward(self.MOVE_DISTANCE)

    def moveDown(self):
        for segNum in range(len(self.segments) - 1):
            self.segments[segNum].penup()
            newX = self.segments[segNum + 1].xcor()
            newY = self.segments[segNum + 1].ycor()
            newY = (newY - (self.MOVE_DISTANCE - 20))
            self.segments[segNum].setpos(newX, newY)
        self.tail.forward(self.MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)
        self.moveUp()

    def down(self):
        self.tail.setheading(270)
        self.moveDown()
