from turtle import Turtle

ALIGMENT = "center"
FONT = ("Arial", 28, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("black")
        self.hideturtle()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def positions(self, x, y):
        self.setposition(x, y)
