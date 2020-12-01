from turtle import Turtle, Screen
from score import Score

# Constants
# =========

# Screen setup
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
NET_NUMBER_OF_LINES = 20
# Turtle headings
UP = 90
DOWN = -90
LEFT = 180
RIGHT = 0


def create_screen(screen):
    screen.colormode(255)
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")


def draw_net(net):
    # Draw the net
    net.hideturtle()
    net.speed("fastest")
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


# START
# =====

# Screen object
s = Screen()
create_screen(s)

# Net object
n = Turtle()
draw_net(n)

# Create Score objects
player_score = Score((-200, SCREEN_HEIGHT / 2 - 100))
ai_score = Score((200, SCREEN_HEIGHT / 2 - 100))




# Listen for player keys
s.listen()
# s.onkey(up, "Up")
# s.onkey(down, "Down")



# Close the screen once the game has ended and the screen is clicked
s.exitonclick()
