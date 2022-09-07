from turtle import Screen
from paddle import Paddle

# constants
BGCOLOR = "black"
WIDTH = 800
HEIGHT = 600
TITLE = "Pong"
R_POSITION = (350, 0)
L_POSITION = (-350, 0)

# creation of the screen
screen = Screen()
screen.bgcolor(BGCOLOR)
screen.setup(width = WIDTH, height = HEIGHT)
screen.title(TITLE)

# the screen is turned off
screen.tracer(0)

# creation of the paddles
r_paddle = Paddle(R_POSITION)
l_paddle = Paddle(L_POSITION)


# game loop
game_is_on = True
while game_is_on:
    screen.update() # the screen updates

screen.exitonclick()