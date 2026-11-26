from turtle import Screen
from ball import Ball
from paddle import Paddle
from wall import Brick
from scoreboard import Scoreboard
import time

screen = Screen()

WIDTH = 800
HEIGHT = 500
WALL_MAX = 390
WALL_MIN = -390
WALL_STEP = 40
lives = 3

screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Breakout game")
screen.tracer(0)
screen.listen()


ball = Ball()
paddle = Paddle(-230)

yellow_wall_bricks = [Brick("yellow", (xpos, 130)) for xpos in range(WALL_MIN, WALL_MAX, WALL_STEP)]
red_wall_bricks = [Brick("red", (xpos, 100)) for xpos in range(WALL_MIN, WALL_MAX, WALL_STEP)]
green_wall_bricks = [Brick("green", (xpos, 160)) for xpos in range(WALL_MIN, WALL_MAX, WALL_STEP)]
scoreboard = Scoreboard()

# Functionality
screen.onkeypress(paddle.to_right, "Right")
screen.onkeypress(paddle.to_left, "Left")

play = True
while play:
    screen.update()
    ball.move()
    time.sleep(ball.mv_speed)

    # Bouncing against left or right sides
    if ball.xcor() < -390.0 or ball.xcor() > 390.0:
        ball.bounce_side()

    # Bouncing against upper side
    if ball.ycor() > 230:
        ball.bounce_side(upper=True)

    # Bouncing against the paddle
    if ball.ycor() < -210 and ball.distance(paddle) < 50:
        ball.bounce_paddle()

    # Bouncing again walls and gaining points
    for brick in red_wall_bricks:
        if ball.distance(brick) < 15:
            scoreboard.up_score("red")
            red_wall_bricks.remove(brick)
            brick.hideturtle()
            ball.bounce_wall()

    for brick in yellow_wall_bricks:
        if ball.distance(brick) < 15:
            scoreboard.up_score("yellow")
            yellow_wall_bricks.remove(brick)
            brick.hideturtle()
            ball.bounce_wall()

    for brick in green_wall_bricks:
        if ball.distance(brick) < 15:
            scoreboard.up_score("green")
            green_wall_bricks.remove(brick)
            brick.hideturtle()
            ball.bounce_wall()

    # Beyond the paddle
    if ball.ycor() < -230:
        ball.reset_home()
        # Update lives
        scoreboard.down_life()

        if scoreboard.lives == 0:
            play = False
            # score boad game over
            scoreboard.game_over()
        

    # destroy all walls
    if len(yellow_wall_bricks) == 0 and len(red_wall_bricks) == 0 and len(green_wall_bricks) == 0:
        play = False
        # scoreboad: Win
        scoreboard.win()


screen.mainloop()