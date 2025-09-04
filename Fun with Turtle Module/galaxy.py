"""
import turtle
t=turtle.Turtle()
s=turtle.Screen()
colors=["red","blue","green","yellow","orange","purple","Magenta","cyan"]
s.bgcolor("black")
s.title("Galaxy Drawing")
s.setup(width=800, height=600)
turtle.speed("fastest")
for i in range(360):
    t.pencolor(colors[i%8])
    t.width(i/100 + 1)
    t.forward(i)
    t.right(59)
    turtle.hideturtle()
"""
import turtle
import colorsys

# Setup
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
s.title("Galaxy Drawing")
s.setup(width=800, height=800)
t.speed(0)  # fastest

# Generate smooth gradient colors using HSV
num_colors = 360
colors = []
for i in range(num_colors):
    hue = i / num_colors
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)  # full saturation, full brightness
    colors.append((r, g, b))

turtle.colormode(1.0)  # RGB values between 0 and 1

# Draw spiral
for i in range(360):
    t.pencolor(colors[i % num_colors])
    t.width(i / 50 + 1)  # gradually thicker
    t.forward(i)
    t.right(59)

t.hideturtle()
s.mainloop()
