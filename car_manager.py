from collections.abc import Iterable
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self) -> None:
        self.all_cars = []

    def create_car(self):       # creates car in 1/6 random times of 1ms
        random_choice = random.randint(1, 6)
        if (random_choice == 1):
            # TWEAKING CAR SHAPE, SIZE, COLOR, POSITION
            car = Turtle('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(300, random.randint(-240, 240))
            self.all_cars.append(car)

    def move_cars(self):        # move car 5 distance
        if self.all_cars != []:
            for elements in self.all_cars:
                elements.setheading(180)
                elements.forward(STARTING_MOVE_DISTANCE)
