from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()

        # CREATING TURTLE SHAPE, COLOR AND POSITION
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.color('black')
        self.start()

    def go_up(self):        # moves turtle forward on pressing space
        self.forward(MOVE_DISTANCE)

    def start(self):        # sets the turtles position on starting position
        self.goto(STARTING_POSITION)

    def is_at_finish(self):  # checks of turtle is at finish line and update level
        if (self.ycor() > FINISH_LINE_Y):
            return True
