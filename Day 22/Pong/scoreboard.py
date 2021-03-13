from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.playerOneScore = 0
        self.playerTwoScore = 0
        self.setpos(0, 440)
        self.hideturtle()
        self.color("white")
        self.updateScoreboard()

    def updateScoreboard(self):
        self.write(f"{self.playerOneScore}      {self.playerTwoScore}", move=False,
                   align=ALIGNMENT, font=FONT)

    def gameOver(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False,
                   align=ALIGNMENT, font=FONT)

    def incrementScore(self, player):
        if player == 'playerOne':
            self.playerOneScore += 1
        else:
            self.playerTwoScore += 1
        self.clear()
        self.updateScoreboard()
