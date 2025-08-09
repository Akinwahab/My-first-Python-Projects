from turtle import Turtle
import math

class ClockFace(Turtle):
    def __init__(self, radius=300):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.pensize(3)
        self.color("white")
        self.radius = radius

        self._draw_main_circle(radius)
        self._draw_hour_marks(radius - 50)
        self._draw_flourishes(radius - 20)

    def _draw_main_circle(self, radius):
        self.penup()
        self.goto(0, -radius)
        self.pendown()
        self.circle(radius)

    def _draw_hour_marks(self, radius):
        roman_nums = ["XII", "I", "II", "III", "IV", "V",
                      "VI", "VII", "VIII", "IX", "X", "XI"]
        self.penup()
        for i in range(12):
            angle = i * 30
            x = radius * math.sin(math.radians(angle))
            y = radius * math.cos(math.radians(angle))
            self.goto(x, y - 10)
            self.write(roman_nums[i], align="center",
                       font=("Times New Roman", 20, "bold"))

    def _draw_flourishes(self, radius):
        self.pensize(2)
        self.pencolor("gold")
        for i in range(12):
            angle = i * 30
            self.penup()
            self.goto(0, 0)
            self.setheading(90 - angle)
            self.forward(radius)
            self.pendown()
            self.circle(8, 180)  # small arc
        self.pensize(3)
        self.pencolor("white")
