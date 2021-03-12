from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def createSnake(self):
        for position in STARTING_POSITIONS:
            self.addSegment(position)

    def addSegment(self, position):
        newSegment = Turtle("square")
        newSegment.color("white")
        newSegment.penup()
        newSegment.goto(position)
        self.segments.append(newSegment)

    def extend(self):
        newPosX = self.segments[-1].pos()[0]
        newPosY = self.segments[-1].pos()[1]
        self.addSegment((newPosX, newPosY))

    def move(self):
        for segNum in range(len(self.segments) - 1, 0, -1):
            # This goes in reverse and the logic is that the current element will go to the position where the previous one was originally at
            # So if the first segment moves 20px to the right (from (0, 0) to (20,0)) then, the second segment will move from ((-20, 0) to (0,0) the first segments original position)
            self.segments[segNum].penup()
            newX = self.segments[segNum - 1].xcor()
            newY = self.segments[segNum - 1].ycor()
            self.segments[segNum].goto(newX, newY)
        self.segments[0].penup()
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
