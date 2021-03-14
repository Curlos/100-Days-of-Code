from turtle import Screen, Turtle
from turtleCrosser import TurtleCrosser
from traffic import Traffic
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

turtle = TurtleCrosser()
traffic = Traffic(turtle)
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.move, "Up")

gameIsOn = True
while gameIsOn:
    time.sleep(0.1)
    screen.update()
    drive = traffic.driveCars()

    # If a car has crashed and killed our turtle
    if drive == "crash":
        gameIsOn = False
        scoreboard.game_over()

    # If turtle reaches finish line
    if turtle.ycor() > 280:
        scoreboard.level_up()
        turtle.refresh()
        traffic.increase_speed()

screen.exitonclick()
