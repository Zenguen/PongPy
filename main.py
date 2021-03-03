from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard_l = ScoreBoard((-100, 200))
scoreboard_r = ScoreBoard((100, 200))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    if ball.distance(r_paddle) < 53.9 and ball.xcor() > 320 or ball.distance(l_paddle) < 53.9 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() >= 380:
        scoreboard_l.add_point()
        ball.reset_position()

    if ball.xcor() <= -380:
        scoreboard_r.add_point()
        ball.reset_position()
    screen.update()

screen.exitonclick()
