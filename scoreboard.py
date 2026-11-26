from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.pencolor("white")
        self.penup()
        self.hideturtle()     
        self.score = 0
        self.lives = 4
        self.up_scoreboard()

    def up_scoreboard(self):
        self.clear()
        self.goto(-395, 220)
        if self.color() != "white":
            self.color("white")
            
        self.write(f"Score: {self.score}", align="left", font=("Courier", 16, "bold"))

        self.goto(395, 220)
        if self.lives <= 1:
            self.pencolor("red")
            self.write(f"Lives: {self.lives}", align="right", font=("Courier", 16, "normal"))
        else:
            self.write(f"Lives: {self.lives}", align="right", font=("Courier", 16, "normal"))

    def down_life(self):
        self.lives -= 1
        self.up_scoreboard()

    def up_score(self, wall):
        if wall == "red":
            self.score += 1
        elif wall == "yellow":
            self.score += 10
        elif wall == "green":
            self.score += 100

        self.up_scoreboard()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))

    def win(self):
        self.home()
        self.write("YOU WIN", align="center", font=("Courier", 24, "normal"))