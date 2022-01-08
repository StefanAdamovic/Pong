from turtle import Turtle, Screen
from scoreboard import Scoreboard
from pong import Pong
from ball import Ball
import time


# Screen made
screen = Screen()
screen.setup(width=1000, height=800)
screen.title("PONG")
screen.tracer(0)

# Scoreboard for right player
scoreboard_1 = Scoreboard()
scoreboard_1.positions(200, 350)
scoreboard_1.update_score()

# Scoreboard for left player
scoreboard_2 = Scoreboard()
scoreboard_2.positions(-200, 350)
scoreboard_2.update_score()

# Middle line on screen
middle_line = Turtle()
middle_line.hideturtle()
middle_line.penup()
middle_line.speed("fastest")
middle_line.setposition(0, 440)
middle_line.setheading(270)
middle_line.width(3)

# Drawing middle line on screen
for x in range(17):
    middle_line.forward(25)
    middle_line.penup()
    middle_line.forward(25)
    middle_line.pendown()

# Positions for right pong
first_pos = (470, 0)

# Positions for left pong
second_pos = (-470, 0)

# Right pong
right_pong = Pong(first_pos)

# Left pong
left_pong = Pong(second_pos)

# Controls for pongs
screen.listen()
screen.onkey(right_pong.up, "Up")
screen.onkey(right_pong.down, "Down")
screen.onkey(left_pong.up, "w")
screen.onkey(left_pong.down, "s")

# Ball
ball = Ball()

# Game mechanic
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Collision with wall
    if ball.ycor() > 380 or ball.ycor() < - 380:
        ball.bounce_y()

    # Collision with pongs
    if ball.distance(right_pong) < 50 and ball.xcor() > 440 or ball.distance(left_pong) < 50 and ball.xcor() < -440:
        ball.bounce_x()






    # Detect scores
    if ball.xcor() > 500:
        scoreboard_2.increase_score()
        ball.reset_position()
    elif ball.xcor() < -500:
        scoreboard_1.increase_score()
        ball.reset_position()





    # Right pong vertical move limit
    if right_pong.ycor() > 345:
        right_pong.sety(345)
    elif right_pong.ycor() < -345:
        right_pong.sety(-345)

    # Left pong vertical move limit
    if left_pong.ycor() > 345:
        left_pong.sety(345)
    elif left_pong.ycor() < -345:
        left_pong.sety(-345)


screen.exitonclick()
