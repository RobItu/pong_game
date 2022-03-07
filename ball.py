from turtle import Turtle, Screen
screen = Screen()

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 1.0
        self.speed(self.move_speed)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed += 0.2
        self.speed(self.move_speed)
        print(self.speed())

    def refresh(self):
        self.move_speed = 1.0
        self.speed(self.move_speed)
        screen.tracer(0)
        self.goto(0, 0)
        screen.tracer(1)
        self.x_move *= -1
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

