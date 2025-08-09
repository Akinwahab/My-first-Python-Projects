from turtle import Turtle
ALLIGMENT = "center"
FONT = ("Courrier", 20, "italic")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALLIGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALLIGMENT, font=("Arial", 24, "normal"))