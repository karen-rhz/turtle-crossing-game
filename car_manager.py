import turtle
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        # super().__init__()
        self.all_turtles = []
        self.speed = 0
        self.move()

    def move(self):
        for item in self.all_turtles:
            item.forward(STARTING_MOVE_DISTANCE)

    def new_car(self):
        # To slow down car creation
        # Only creat a car when getting a 6
        n = random.randint(1, 7)
        if n == 6:
            # Only create a new car every time I get a 6
            new_turtle = Turtle("square")
            new_turtle.shapesize(1, 2)
            new_turtle.color(random.choice(COLORS))
            new_turtle.penup()
            new_turtle.seth(180)
            new_turtle.goto(400, random.randint(-250, 250))
            self.all_turtles.append(new_turtle)

    def speed_up(self):
        self.speed += MOVE_INCREMENT