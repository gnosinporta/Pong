from turtle import Turtle

COLOR = "white"
ALIGN = "center"
FONT = ("Courier", 60, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def r_point(self):
        self.r_score += 1
        self.update()

    def l_point(self):
        self.l_score += 1
        self.update()
