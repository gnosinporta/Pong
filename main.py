from turtle import Screen
from paddle import Paddle
from ball import Ball

# constants
BGCOLOR = "black"
WIDTH = 800
HEIGHT = 610
TITLE = "Pong"
R_POSITION = (350, 0)
L_POSITION = (-350, 0)

# creation of the screen
screen = Screen()
screen.bgcolor(BGCOLOR)
screen.setup(width=WIDTH, height=HEIGHT)
screen.title(TITLE)

# the screen is turned off
screen.tracer(0)

# creation of the paddles and the ball
r_paddle = Paddle(R_POSITION)
l_paddle = Paddle(L_POSITION)
ball = Ball()

# reading of the keyboard input
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# game loop
game_is_on = True
while game_is_on:
    screen.update()  # now screen.tracer(0) means something

screen.exitonclick()
