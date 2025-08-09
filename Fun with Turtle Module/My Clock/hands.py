import turtle

class ClockHand(turtle.Turtle):
    def __init__(self, color="white", length=10, width=0.4, shape="arrow", center_dot=True):
        super().__init__()
        self.shape(shape)
        self.speed(0)
        self.color(color)
        self.penup()
        self.goto(0, 0)
        self.shapesize(stretch_wid=width, stretch_len=length)
        self.center_dot = center_dot
        if self.center_dot:
            self._draw_center_dot()

    def _draw_center_dot(self):
        pivot = turtle.Turtle()
        pivot.hideturtle()
        pivot.penup()
        pivot.goto(0, 0)
        pivot.dot(15, "gold") 

    def update_angle(self, angle):
        self.setheading(90 - angle)
