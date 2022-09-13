from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

from scoreboard import Scoreboard

# constants
BGCOLOR = "black"
WIDTH = 800
HEIGHT = 620
TITLE = "Pong"
PADDLE_MARGINS = 350
R_POSITION = (PADDLE_MARGINS, 0)
L_POSITION = (-PADDLE_MARGINS, 0)
BOUNCE_MARGINS = 280
TIME_SLEEP = 0.05
PAD_BAL_IMPACT = 60
P_B_ADJUST = 20

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
scoreboard = Scoreboard()

# reading of the keyboard input
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# goal function
def goal():
    ball.reset()
    l_paddle.reset()
    r_paddle.reset()

 
# game loop
game_is_on = True
while game_is_on:
    screen.update()  # now screen.tracer(0) means something
    time.sleep(TIME_SLEEP)
    ball.move()

    # detecting ball collision with upper and lower walls
    if ball.ycor() > BOUNCE_MARGINS or ball.ycor() < -BOUNCE_MARGINS:
        ball.bounce_walls()
        r_paddle.accelerate_movement()
        l_paddle.accelerate_movement()

    # detecting collision with paddles
    if (ball.xcor() >= PADDLE_MARGINS - P_B_ADJUST and ball.distance(r_paddle) < PAD_BAL_IMPACT) or (
            ball.xcor() <= -PADDLE_MARGINS + P_B_ADJUST and ball.distance(l_paddle) < PAD_BAL_IMPACT):
        ball.bounce_paddle()

    # detecting goal in the R
    if ball.xcor() > PADDLE_MARGINS + P_B_ADJUST:
        goal()
        scoreboard.l_point()

    # detecting goal in the L
    if ball.xcor() < -PADDLE_MARGINS - P_B_ADJUST:
        goal()
        scoreboard.r_point()


screen.exitonclick()
