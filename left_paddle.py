from turtle import Turtle
STARTING_POSITION = [(-380, 20), (-380, 0), (-380, -20)]
X_POS = -380
MOVE_DISTANCE = 20
SIZE = 40
UP = 90
DOWN = 270


class LeftPaddle:

    def __init__(self):
        self.segments = []
        self.create_paddle()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def create_paddle(self):
        for position in STARTING_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.pensize(SIZE)
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def up(self):
        self.head.setheading(UP)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(X_POS, new_y)
        self.head.forward(MOVE_DISTANCE)

    def down(self):
        self.tail.setheading(DOWN)
        for seg_num in range(0, len(self.segments)-1, 1):
            new_y = self.segments[seg_num+1].ycor()
            self.segments[seg_num].goto(X_POS, new_y)
        self.tail.forward(MOVE_DISTANCE)
