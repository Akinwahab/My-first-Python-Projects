from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball= Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Bounce off paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 350) or \
       (ball.distance(l_paddle) < 50 and ball.xcor() < -350):
        ball.bounce_x()
    #detect if ball out 
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()
    elif ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()
    
screen.exitonclick()