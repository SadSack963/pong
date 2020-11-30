from turtle import Turtle, Screen
from score import Score

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
NET_NUMBER_OF_LINES = 20
UP = 90


# START
# =====

# Screen object
s = Screen()
s.colormode(255)
s.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
s.bgcolor("black")

# Draw the net
net = Turtle()
net.hideturtle()
net.speed(5)
net.pu()
net.pencolor("white")
net.pensize(4)
net.setposition(0, -SCREEN_HEIGHT / 2)
net.setheading(UP)
line_length = SCREEN_HEIGHT / (NET_NUMBER_OF_LINES * 2 + 1)
while net.ycor() < SCREEN_HEIGHT:
    net.pu()
    net.fd(line_length)
    net.pd()
    net.fd(line_length)

# Create Score objects
player_score = Score((-200, SCREEN_HEIGHT / 2 - 100))
ai_score = Score((200, SCREEN_HEIGHT / 2 - 100))


# Listen for player keys
s.listen()
# s.onkey(up, "Up")
# s.onkey(down, "Down")


s.exitonclick()
