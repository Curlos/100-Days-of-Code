from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.readHighScore() or 0 
        self.setpos(0, 270)
        self.hideturtle()
        self.color("white")
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False,
                   align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.updateScoreboard()

    def incrementScore(self):
        self.score += 1
        self.updateScoreboard()

    def readHighScore(self):
        with open("high_score.txt", mode="r") as file:
            return int(file.read())
