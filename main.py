from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

scoreboard_r = Scoreboard(40)
scoreboard_l = Scoreboard(-40)
paddle_l = Paddle((-350,0))
paddle_r = Paddle((350,0))
ball = Ball()

screen = Screen()
screen.tracer(0)

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game.")

screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    if ball.xcor() > 380:
        scoreboard_l.increase_score()
        ball.reset()
    elif ball.xcor() < -380:
        scoreboard_r.increase_score()
        ball.reset()




















screen.exitonclick()