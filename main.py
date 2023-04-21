import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()

# Making the turtle move when pressing Up key
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Creating moving obstacles
    cars.new_car()
    cars.move()
    scoreboard.update_score()

    # Checking level up when at the other end of the screen
    if player.level_up():
        player.starting_position()
        cars.speed_up()
        scoreboard.plus_one_score()

    # Checking if the player is hit by one of the random cars
    for turtle in cars.all_turtles:
        if player.distance(turtle) < 20:
            scoreboard.game_over()
            game_is_on = False

scoreboard.game_over()

screen.exitonclick()