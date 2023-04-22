from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 70, "bold")


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.update()

    def update(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def count(self):
        self.clear()
        self.score += 1
        self.update()
