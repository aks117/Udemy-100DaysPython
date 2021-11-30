from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.move_speed = 0.1
        self.speed("slowest")
        self.x_move = 10
        self.y_move = 10

    def move(self, x_sign="+", y_sign="+"):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_paddle()

        x = random.randint(0, 1)

        if x == 0:
            self.bounce_wall()

        self.move_speed = 0.1
