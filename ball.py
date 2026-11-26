from turtle import Turtle

class Ball(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.shape("circle")
        pen = {
            'pensize': 5, 
            'pencolor': 'white', 
            'pendown': False, 
            'fillcolor': 'white', 
        }
        self.pen(pen)
        self.teleport(0, -175)
        self.x_move = 10
        self.y_move = 10
        self.mv_speed = 0.09

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_wall(self):
        self.y_move *= -1
        self.x_move *= 0.9

    def bounce_paddle(self):
        self.y_move *= -1 
        self.mv_speed *= 0.9

    def bounce_side(self, upper=False):
        if upper:
            self.y_move *= -1
        else:
            self.x_move *= -1

    def reset_home(self):
        self.teleport(self.xcor(), -175)
        self.mv_speed = 0.05
        self.bounce_paddle()
