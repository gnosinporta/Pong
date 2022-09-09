from turtle import Turtle

# constants
SHAPE = "circle"
COLOR = "white"
X_MOVEMENT = 3
Y_MOVEMENT = 10
ACCELERATION = 1.1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.penup()
        self.x_cor = X_MOVEMENT
        self.y_cor = Y_MOVEMENT

    def move(self):
        new_x = self.xcor() + self.x_cor
        new_y = self.ycor() + self.y_cor
        self.goto(new_x, new_y)

    def bounce_walls(self):
        self.y_cor *= -1
        self.accelerate()

    def bounce_paddle(self):
        self.x_cor *= -1
        # self.accelerate()

    def accelerate(self):
        self.x_cor *= ACCELERATION
        self.y_cor *= ACCELERATION
