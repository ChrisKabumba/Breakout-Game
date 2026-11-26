from turtle import Turtle

class Brick(Turtle):
    def __init__(self, color: str, position: tuple, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.color(color, color)
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=2)
        self.up()
        self.goto(position)


