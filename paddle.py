from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.shape("square")
        self.teleport(0, pos)
        self.fillcolor("grey")
        self.shapesize(stretch_len=15, stretch_wid=1)

    def to_right(self):
        right = self.xcor() + 20
        if self.xcor() < 400:
            self.goto(right, self.ycor())

    def to_left(self):
        left = self.xcor() - 20
        if self.xcor() > -400:
            self.goto(left, self.ycor())