from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.left(90)
        self.color("black")
        self.shape("turtle")
        self.goto_start()

    def move_up(self):
        # new_y = self.ycor() + MOVE_DISTANCE
        # self.goto(0, new_y)
        self.forward(MOVE_DISTANCE)

    def goto_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False