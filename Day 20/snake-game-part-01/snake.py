from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]

    def createSnake(self):
        for i in range(3):
            segment = Turtle()
            segment.shape("square")
            segment.color("white")

            if i > 0:
                segment.penup()
                prevSegmentPosX = self.segments[i - 1].position()[0]
                prevSegmentPosY = self.segments[i - 1].position()[1]
                # Each turtle is a square of 20x20 so to move one to the left, move it by 20 px
                segment.setpos(prevSegmentPosX -
                               MOVE_DISTANCE, prevSegmentPosY)
            self.segments.append(segment)

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
