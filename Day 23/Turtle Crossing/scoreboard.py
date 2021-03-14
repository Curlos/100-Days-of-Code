from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f"Level {self.level}:", align="center",
                   font=("Courier", 20, "normal"))

    def level_up(self):
        self.level += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center",
                   font=("Courier", 20, "normal"))
