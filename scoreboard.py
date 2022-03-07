from turtle import Turtle, Screen

screen = Screen()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        screen.tracer(0)
        self.goto(-100, 200)
        self.write(self.l_score, False, "center", ("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, False, "center", ("Courier", 60, "normal"))
        screen.tracer(1)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
