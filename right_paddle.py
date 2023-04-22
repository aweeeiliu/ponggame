from turtle import Turtle

STARTING_POSITION = (350, 0)
WIDTH = 20
HEIGHT = 100
X_POS = 350


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.turtlesize(stretch_wid=WIDTH, stretch_len=HEIGHT)
        self.color("white")
        self.penup()
        self.goto(STARTING_POSITION)

