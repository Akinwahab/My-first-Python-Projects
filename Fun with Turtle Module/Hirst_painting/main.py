"""import turtle
t=turtle.Turtle()
turtle.colormode(255)
import random
import colorgram


def colour_extractor(img):
    rgb_colour=[]
    colours=colorgram.extract(img, 40)
    for colour in colours:
        r=colour.rgb.r
        g=colour.rgb.g
        b=colour.rgb.b
        if (r and g and b)>230:
            continue
        else:
            rgb=(r,g,b)
            rgb_colour.append(rgb)
    return rgb_colour
rgb_colour=colour_extractor("hirst.jpeg")
t.penup()
t.goto(-300, 300)
t.pendown()
for i in range(20):
    for _ in range(20):
        t.pendown()
        t.dot(20, random.choice(rgb_colour))
        t.penup()
        t.fd(20)
    if i%2 == 0:
        t.rt(90)
        t.fd(20)
        t.rt(90)
    else:
        t.lt(90)
        t.fd(20)
        t.lt(90)

        
screen=turtle.Screen()
screen.exitonclick()"""
import turtle
import random
import colorgram

# Extract colors
def colour_extractor(img):
    rgb_colour = []
    colours = colorgram.extract(img, 40)
    for colour in colours:
        r, g, b = colour.rgb.r, colour.rgb.g, colour.rgb.b
        if r > 230 and g > 230 and b > 230:
            continue
        rgb_colour.append((r, g, b))
    return rgb_colour

# Setup
t = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
t.hideturtle()
t.penup()
t.speed("fastest")

# Get colors
rgb_colour = colour_extractor("hirst.jpeg")

# Dot grid setup
num_dots = 20
spacing = 30  # space between dots

start_x = -spacing * num_dots // 2
start_y = spacing * num_dots // 2

# Draw grid
for row in range(num_dots):
    for col in range(num_dots):
        x = start_x + col * spacing
        y = start_y - row * spacing
        t.goto(x, y)
        t.dot(20, random.choice(rgb_colour))

screen.exitonclick()

