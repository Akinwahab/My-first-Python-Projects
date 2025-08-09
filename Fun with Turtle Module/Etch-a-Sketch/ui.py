from turtle import Turtle

class WelcomeScreen:
    def __init__(self, screen):
        self.screen = screen
        self.writer = Turtle(visible=False)
        self.writer.penup()
        self.writer.goto(0, 100)
        self.writer.color("blue")
        self.screen.bgcolor("white")
        
    def show(self):
        self.writer.clear()
        instructions = [
            "Welcome to Etch-A-Sketch!",
            "",
            "Controls:",
            "W = Move Forward",
            "S = Move Backward",
            "A = Turn Left",
            "D = Turn Right",
            "P = Toggle Pen Up/Down",
            "C = Clear with Shake",
            "R = Random Pen Color",
            "E/Q = Increase/Decrease Pen Size",
            "1/2/3 = Draw Circle/Square/Star",
            "B = Random Background Color",
            "",
            "Press Enter to Start Drawing"
        ]
        for i, line in enumerate(instructions):
            self.writer.goto(0, 100 - i * 25)
            self.writer.write(line, align="center", font=("Arial", 16, "normal"))

    def wait_for_start(self, start_callback):
        def on_enter():
            self.writer.clear()
            self.writer.hideturtle()
            start_callback()
        self.screen.onkey(on_enter, "Return")
        self.screen.listen()

class InfoPanel:
    def __init__(self, screen):
        self.screen = screen
        self.writer = Turtle(visible=False)
        self.writer.penup()
        self.writer.goto(-screen.window_width()//2 + 10, screen.window_height()//2 - 100)
        self.writer.color("black")
        self.writer.hideturtle()

    def show(self):
        lines = [
            "Controls:",
            "W = Forward",
            "S = Backward",
            "A = Left",
            "D = Right",
            "P = Pen Up/Down",
            "C = Clear",
            "R = Pen Color",
            "E/Q = Pen Size + / -",
            "1/2/3 = Shapes",
            "B = Background"
        ]
        self.writer.clear()
        for i, line in enumerate(lines):
            self.writer.goto(-self.screen.window_width()//2 + 10, self.screen.window_height()//2 - 30 - i * 20)
            self.writer.write(line, font=("Arial", 10, "normal"))
