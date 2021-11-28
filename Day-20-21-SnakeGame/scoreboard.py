from turtle import Turtle

SCORE_ALIGN = "center"
SCORE_FONT = ("ariel", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.goto(-10, 270)
        self.display_score()

    def score_up(self):
        self.score += 1

    def display_score(self):
        self.clear()
        self.write(arg=f"SCORE : {self.score}", move=False,align=SCORE_ALIGN,font=SCORE_FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER!", move=False, align=SCORE_ALIGN, font=SCORE_FONT)