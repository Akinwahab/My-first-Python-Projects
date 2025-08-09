from turtle import Turtle, Screen
import random

class EtchASketch(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.shape("turtle")
        self.speed("fastest")
        self.pen_size = 2
        self.pensize(self.pen_size)
        self.screen = screen
        self.bind_keys()
        self.screen.colormode(1)

    # Movement
    def forward_move(self):
        self.fd(10)

    def backward_move(self):
        self.bk(10)

    def turn_right(self):
        self.rt(15)

    def turn_left(self):
        self.lt(15)

    # Pen control
    def toggle_pen(self):
        if self.isdown():
            self.penup()
        else:
            self.pendown()

    # Clear screen
    def clear_screen(self):
        self.penup()
        for _ in range(50):
            self.setheading(random.randint(0, 360))
            self.fd(100)
        self.home()
        self.clear()
        self.pendown()

    def random_color(self):
        r = random.random()
        g = random.random()
        b = random.random()
        self.pencolor(r, g, b)#

    def increase_size(self):
        self.pen_size += 1
        self.pensize(self.pen_size)

    def decrease_size(self):
        if self.pen_size > 1:
            self.pen_size -= 1
            self.pensize(self.pen_size)

    def random_bg(self):
        r = random.random()
        g = random.random()
        b = random.random()
        self.screen.bgcolor(r, g, b)
        
    def draw_circle(self):
        self.circle(50)

    def draw_square(self):
        for _ in range(4):
            self.fd(50)
            self.rt(90)

    def draw_star(self):
        for _ in range(5):
            self.fd(100)
            self.rt(144)

    # Bind keys
    def bind_keys(self):
        self.screen.listen()
        self.screen.onkey(self.forward_move, "w")
        self.screen.onkey(self.backward_move, "s")
        self.screen.onkey(self.turn_right, "d")
        self.screen.onkey(self.turn_left, "a")
        self.screen.onkey(self.toggle_pen, "p")
        self.screen.onkey(self.clear_screen, "c")
        self.screen.onkey(self.random_color, "r")
        self.screen.onkey(self.increase_size, "e")
        self.screen.onkey(self.decrease_size, "q")
        self.screen.onkey(self.draw_circle, "1")
        self.screen.onkey(self.draw_square, "2")
        self.screen.onkey(self.draw_star, "3")
        self.screen.onkey(self.random_bg, "b")

