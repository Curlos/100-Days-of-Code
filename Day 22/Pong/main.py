from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from random import randrange
import time

PLAYER_ONE_STARTING_POS = [(-900, 40), (-900, 20),
                           (-900, 0), (-900, -20), (-900, -40)]

PLAYER_TWO_STARTING_POS = [(900, 40), (900, 20),
                           (900, 0), (900, -20), (900, -40)]

screen = Screen()
screen.setup(width=1920, height=1080)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

playerOne = Paddle(PLAYER_ONE_STARTING_POS, 50)
playerTwo = Paddle(PLAYER_TWO_STARTING_POS, 30)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(playerOne.up, "Up")
screen.onkey(playerOne.down, "Down")

gameIsOn = True
AI_UP = True
AI_DOWN = False
BALL_UP = True
BALL_DOWN = False
BALL_RIGHT = False
BALL_LEFT = True

while gameIsOn:
    screen.update()

    if playerOne.distance(ball) < 15:
        BALL_UP = True
        BALL_RIGHT = True
        BALL_DOWN = False
        BALL_LEFT = False
    elif playerTwo.distance(ball) < 15:
        BALL_DOWN = True
        BALL_LEFT = True
        BALL_UP = False
        BALL_RIGHT = False

    if ball.xcor() >= (screen.window_width() // 2) or ball.xcor() < (-1 * screen.window_width() // 2):
        ball.penup()
        ball.setpos(0, 0)
        randomNum = randrange(10)
        print(randomNum)
        if randomNum > 5:
            BALL_UP = True
            BALL_RIGHT = True
            BALL_DOWN = False
            BALL_LEFT = False
        else:
            BALL_UP = True
            BALL_LEFT = True
            BALL_DOWN = False
            BALL_RIGHT = False
        time.sleep(0.1)

    else:
        if playerTwo.tail.ycor() <= -520:
            playerTwo.up()
            AI_UP = True
            AI_DOWN = False
        elif playerTwo.head.ycor() >= 520:
            playerTwo.down()
            AI_DOWN = True
            AI_UP = False
        else:
            if AI_UP:
                playerTwo.up()
            else:
                playerTwo.down()

        if ball.ycor() <= -520:
            if ball.xcor() < 0:
                BALL_LEFT = True
                BALL_RIGHT = False
                ball.moveUpLeft()
            elif ball.xcor() > 0:
                BALL_RIGHT = True
                BALL_LEFT = False
                ball.moveUpRight()
            BALL_UP = True
            BALL_DOWN = False
        elif ball.ycor() >= 520:
            if ball.xcor() < 0:
                BALL_LEFT = True
                BALL_RIGHT = False
                ball.moveDownRight()
            elif ball.xcor() > 0:
                BALL_RIGHT = True
                BALL_LEFT = False
                ball.moveDownLeft()
            BALL_DOWN = True
            BALL_UP = False
        else:
            if BALL_UP:
                if BALL_LEFT:
                    print('left boi')
                    ball.moveUpLeft()
                else:
                    ball.moveUpRight()
            else:
                if BALL_LEFT:
                    ball.moveDownLeft()
                else:
                    ball.moveDownRight()


screen.exitonclick()
