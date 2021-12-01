from turtle import Turtle

SCORE_ALIGN = "center"
SCORE_FONT = ("ariel", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as data:
            hs = data.read()
            self.high_score = int(hs)
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.goto(-10, 270)
        self.display_score()

    def score_up(self):
        self.score += 1

    def display_score(self):
        self.clear()
        self.write(arg=f"SCORE : {self.score}\tHigh Score : {self.high_score}", move=False,align=SCORE_ALIGN,font=SCORE_FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg=f"GAME OVER!", move=False, align=SCORE_ALIGN, font=SCORE_FONT)
    #

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as hs:
                hs.write(f"{self.high_score}")

        self.score = 0
        self.display_score()