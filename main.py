from turtle import Turtle, Screen
from score import Score
from random import randint
from ball import Ball
from bat import Bat
import gameover
from time import sleep
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


def bat_move_up():
    player_bat.move(C.PLAYER_BAT_SPEED)
    s.ontimer(bat_move_up, 200)


def bat_move_down():
    player_bat.move(-C.PLAYER_BAT_SPEED)
    s.ontimer(bat_move_down, 200)


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

# Listen for screen events
s.listen()

# Screen Events
# The functions player_bat.move_up and player_bat.move_down are not actually called here.
# They are passed to the event handler mainloop() when the "key" is pressed
s.onkey(player_bat.move, "Up")
s.onkey(player_bat.move, "Down")

game_on = True
while game_on:
    if player_score.score == 5:
        print("You Win!")
        game_on = False
        gameover.GameOver()
    elif ai_score.score == 5:
        print("You Lose!")
        game_on = False
        gameover.GameOver()
    else:
        ball.move()
        ai_bat.move(randint(C.AI_BAT_SPEED - 3, C.AI_BAT_SPEED + 3))
        sleep(0.2)

# Close the screen once the game has ended and the screen is clicked
# This binds bye() method to mouse clicks on the Screen.
# Also enters s.mainloop() if “using_IDLE” in the configuration dictionary is False.
s.exitonclick()

# # Or s.done(). Starts the screen event loop - calling Tkinter’s mainloop function.
# # Must be the last statement in a turtle graphics program.
# s.mainloop()
