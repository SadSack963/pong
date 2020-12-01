from turtle import Turtle, Screen
from score import Score
from random import randint
from ball import Ball
from bat import Bat
import CONSTANTS as C


def create_screen(screen):
    screen.colormode(255)
    screen.setup(width=C.SCREEN_WIDTH, height=C.SCREEN_HEIGHT)
    screen.bgcolor("black")


def draw_net(net):
    # Draw the net
    net.hideturtle()
    net.speed("fastest")
    net.pu()
    net.pencolor("white")
    net.pensize(4)
    net.setposition(0, -C.HALF_HEIGHT)
    net.setheading(C.UP)
    line_length = C.SCREEN_HEIGHT / (C.NET_NUMBER_OF_LINES * 2 + 1)
    while net.ycor() < C.SCREEN_HEIGHT:
        net.pu()
        net.fd(line_length)
        net.pd()
        net.fd(line_length)


# START
# =====

# Screen object
s = Screen()
create_screen(s)

# Net object
n = Turtle()
draw_net(n)

# Create Score objects
player_score = Score((-200, C.HALF_HEIGHT - 100))
ai_score = Score((200, C.HALF_HEIGHT - 100))

# Create bats
player_bat = Bat((-C.HALF_WIDTH + 50, randint(-C.HALF_HEIGHT, C.HALF_HEIGHT)))
ai_bat = Bat((C.HALF_WIDTH - 50, randint(-C.HALF_HEIGHT, C.HALF_HEIGHT)))

# Create Ball object
ball = Ball((-C.HALF_WIDTH, randint(-C.HALF_HEIGHT, C.HALF_HEIGHT)))
for _ in range(40):
    ball.fd(20)


# Listen for player keys
s.listen()
# s.onkey(up, "Up")
# s.onkey(down, "Down")


# Close the screen once the game has ended and the screen is clicked
s.exitonclick()
