from turtle import Turtle
import time


class Ball(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(pos)
        self.x_move = 2
        self.y_move = 2
        self.move_speed = 0.01

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        time.sleep(1)
        self.move_speed = 0.01
        self.goto(0, 0)
        self.bounce_x()
