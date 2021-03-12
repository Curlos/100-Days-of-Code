from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.setpos(0, 270)
        self.hideturtle()
        self.color("white")
        self.updateScoreboard()

    def updateScoreboard(self):
        self.write(f"Score: {self.score}", move=False,
                   align=ALIGNMENT, font=FONT)

    def gameOver(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False,
                   align=ALIGNMENT, font=FONT)

    def incrementScore(self):
        self.score += 1
        self.clear()
        self.updateScoreboard()
