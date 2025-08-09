from turtle import Turtle

class DigitalDisplay(Turtle):
    THEMES = {
        "vintage": ["#FFD700", "#DAA520", "#FFEC8B"],
        "neon": ["#00FF88", "#00FF00", "#CCFFCC"],
        "digital": ["#FFB84D", "#FF8000", "#FFD1A3"],
        "futuristic": ["#80DFFF", "#00BFFF", "#E6F7FF"]
    }

    def __init__(self, y_offset=-50, theme="neon"):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, y_offset)
        self.theme = theme if theme in self.THEMES else "neon"

    def draw_glow_text(self, text):
        self.clear()
        glow_colors = self.THEMES[self.theme]
        offsets = [(-2, -2), (2, 2), (0, 0)]
        
        for color, offset in zip(glow_colors, offsets):
            self.goto(offset[0], self.ycor() + offset[1])
            self.color(color)
            self.write(text, align="center", font=("Courier", 36, "bold"))

