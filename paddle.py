from turtle import Turtle

# constants
STRETCH_WID = 5
STRETCH_LEN = 1
SHAPE = "square"
COLOR = "white"
UP_DOWN_MARGINS = 240
MOVEMENT = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.shapesize(stretch_wid=STRETCH_WID, stretch_len=STRETCH_LEN)
        self.penup()
        self.goto(position)

    # these functions control the movement of the paddle
    def go_up(self):
        if self.ycor() < UP_DOWN_MARGINS:
            new_y = self.ycor() + MOVEMENT
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -UP_DOWN_MARGINS:
            new_y = self.ycor() - MOVEMENT
            self.goto(self.xcor(), new_y)
