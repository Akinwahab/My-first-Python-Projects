FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard:
    def __init__(self):
        self.level = 1
        self.scoreboard = Turtle()
        self.scoreboard.penup()
        self.scoreboard.hideturtle()
        self.scoreboard.goto(0, 260)
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.scoreboard.clear()
        self.scoreboard.write(f"Level: {self.level}", align="center", font=FONT)
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()#
    def game_over(self):
        self.scoreboard.goto(0, 0)
        self.scoreboard.write("GAME OVER", align="center", font=FONT)