from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.seth(90)
        self.starting_position()

    def move(self):
        self.forward(10)

    def level_up(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def starting_position(self):
        self.goto(STARTING_POSITION)