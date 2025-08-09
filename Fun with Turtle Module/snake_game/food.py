import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.speed("fastest")
        self.color("blue")
        self.refresh()
    def refresh(self):
        random_x=random.randint(-270,270)
        random_y=random.randint(-270, 270)
        self.goto(random_x, random_y)