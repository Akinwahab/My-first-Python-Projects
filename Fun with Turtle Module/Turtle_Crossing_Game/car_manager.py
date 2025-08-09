import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
STARTING_SPAWN_RATE = 6 
SPAWN_RATE_INCREMENT = 1 

class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.spawn_rate = STARTING_SPAWN_RATE  # smaller = spawns faster
        self.loop_counter = 0


    def create_car(self):
        car = Turtle("square")
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.goto(300, random.randint(-250, 250))
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars[:]:  # iterate over copy for safe removal
            car.setx(car.xcor() - self.move_distance)
            if car.xcor() < -320:
                self.cars.remove(car)
        self.loop_counter += 1
        if self.loop_counter >= self.spawn_rate:
            self.create_car()
            self.loop_counter = 0

    def increase_difficulty(self):
        self.move_distance += MOVE_INCREMENT
        if self.spawn_rate > 1:  # Prevent instant spam
            self.spawn_rate -= SPAWN_RATE_INCREMENT

