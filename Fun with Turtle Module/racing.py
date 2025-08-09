from turtle import Turtle, Screen, Terminator
import random
import time

screen = Screen()
screen.setup(width=1000, height=800)
is_race_on = False
T_colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

while True:
    user_bet = screen.textinput(
    title="Make a bet",
    prompt="Pick a turtle!\nAvailable colours:\n" + "\n".join(T_colours)
)


    if user_bet in T_colours:
        break


if user_bet:
    countdown_turtle = Turtle()
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    countdown_turtle.color("black")
    countdown_turtle.goto(0, 0)
    countdown_turtle.write("Get Ready!", align="center", font=("Arial", 36, "bold"))
    time.sleep(1)
    for num in ["3", "2", "1", "GO!"]:
        countdown_turtle.clear()
        countdown_turtle.write(num, align="center", font=("Arial", 48, "bold"))
        time.sleep(1)
    countdown_turtle.clear()

    is_race_on = True
y_pos = [0, 100, -100, 200, -200, 300, -300]
all_turtles = []


def pick_colour(turtle):
    colour = random.choice(T_colours)
    turtle.color(colour)
    T_colours.remove(colour)


"""Shorter way"""
for index in range(0, 7):

    Turtle_obj = Turtle(shape="turtle")
    Turtle_obj.speed("fastest")
    pick_colour(Turtle_obj)
    Turtle_obj.penup()
    Turtle_obj.goto(x=-480, y=y_pos[index])
    all_turtles.append(Turtle_obj)

announce_turtle = Turtle()
announce_turtle.hideturtle()
announce_turtle.penup()
announce_turtle.color("black")
announce_turtle.goto(0, -100)

while is_race_on:
    for turt in all_turtles:
        if turt.xcor() > 480:
            is_race_on = False
            winner = turt.pencolor()
            if winner == user_bet:
                announce_turtle.write(
                    f"You won!, {winner} turtle is the winner!",
                    align="center",
                    font=("Arial", 32, "bold"),
                )
            else:
                announce_turtle.write(
                    f"You lost, {winner} turtle won the race.",
                    align="center",
                    font=("Arial", 32, "bold"),
                )
        turt.fd(random.randint(0, 10))

time.sleep(2)
screen.bye()

# screen.exitonclick()