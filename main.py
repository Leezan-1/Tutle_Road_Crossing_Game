# FILE IMPORTS
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# SETTING UP THE SCREEN
screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

# CREATING INSTANCES OF PLAYER. CARS_MANAGER AND SCOREBOARD
player = Player()
levels = Scoreboard()
cars = CarManager()

# CONTROL FOR PLAYER'S TURTLE
screen.onkeypress(player.go_up, "space")


game_is_on = True
while game_is_on:

    time.sleep(levels.level_speed)      # speed for game
    screen.update()

    # CREATES MOVING CARS IN SCREEN
    cars.create_car()
    cars.move_cars()

    # NEW LEVEL FOR THE PLAYER
    if (player.is_at_finish()):
        player.start()
        levels.next_level()

    # if cars.all_cars != []:
    for moving_cars in cars.all_cars:
        if moving_cars.distance(player) < 20:
            game_is_on = False
            levels.game_over()

        if moving_cars.xcor() < -450:
            moving_cars.hideturtle()
            cars.all_cars.remove(moving_cars)


screen.update()
screen.exitonclick()
