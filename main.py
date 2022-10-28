from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

# Creating the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("PyPong")
screen.tracer(0)

# Creating the paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball((1, 1))
scoreboard = ScoreBoard()
# m_paddle = Paddle((0, 0))

# Making the screen interactive
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# As we used the Tracer method
gameIsOn = True
while gameIsOn:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    if (ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50) and abs(ball.xcor()) > 330:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if ball.ycor() > 288 or ball.ycor() < -288:
        ball.bounce_y()

screen.exitonclick()
