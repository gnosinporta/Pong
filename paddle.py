from turtle import Turtle

# constants
STRETCH_WID = 5
STRETCH_LEN = 1
SHAPE = "square"
COLOR = "white"


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.shapesize(stretch_wid = STRETCH_WID, stretch_len = STRETCH_LEN)
        self.penup()
        self.goto(position)