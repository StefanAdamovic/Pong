from turtle import Turtle

DISTANCE = 40
UP = 90


class Pong(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.setposition(position)
        self.shape("square")
        self.setheading(UP)
        self.shapesize(stretch_wid=1, stretch_len=5)

    def up(self):
        self.forward(DISTANCE)

    def down(self):
        self.backward(DISTANCE)
