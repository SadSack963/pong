from turtle import Turtle, Screen
from random import randint, choice
from score import Score
from random import randint
from ball import Ball
from bat import Bat
import gameover
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


# TODO Find a way to get a held key to repeat.
#  s.ontimer() doesn't work - it doesn't allow anything else to happen!
def player_bat_up():
    if not player_bat.stop_up:
        player_bat.move(C.PLAYER_BAT_SPEED)
    # s.ontimer(player_bat_up, 200)


def player_bat_down():
    if not player_bat.stop_down:
        player_bat.move(-C.PLAYER_BAT_SPEED)
    # s.ontimer(player_bat_down, 200)


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
player_bat = Bat((-C.HALF_WIDTH + 40, randint(-C.HALF_HEIGHT, C.HALF_HEIGHT)))
ai_bat = Bat((C.HALF_WIDTH - 40, randint(-C.HALF_HEIGHT, C.HALF_HEIGHT)))

# Create Ball object
ball = Ball()

# Listen for screen events
s.listen()

# Screen Events
# The functions player_bat.move_up and player_bat.move_down are not actually called here.
# They are passed to the event handler mainloop() when the "key" is pressed
s.onkey(player_bat_up, "Up")
s.onkey(player_bat_down, "Down")


# MAIN GAME LOOP
# ==============

game_on = True
ai_direction = 0  # direction of AI bat movement
new_ai_direction = 0
ai_speed = 0
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
        ball.detect_bat(player_bat.pos())
        ball.detect_bat(ai_bat.pos())
        if ball.detect_edge() == 1:
            # Player wins
            player_score.update()
            # Reposition ball with new heading
            ball.setposition(0, 0)
            ball.setheading(choice([-45, 45, 135, -135]) + randint(-10, 10))
        elif ball.detect_edge() == 2:
            # AI wins
            ai_score.update()
            # Reposition ball with new heading
            ball.setposition(0, 0)
            ball.setheading(choice([-45, 45, 135, -135]) + randint(-10, 10))
        else:
            # If the bat direction has changed, then get a new random AI bat speed
            if new_ai_direction != ai_direction:
                ai_direction = new_ai_direction
                ai_speed = randint(C.AI_BAT_SPEED, C.AI_BAT_SPEED + 8)
            if ball.ycor() - ai_bat.ycor() > 10:
                new_ai_direction = 1
            elif ball.ycor() - ai_bat.ycor() < -10:
                new_ai_direction = -1
            else:
                new_ai_direction = 0
            ai_bat.move(new_ai_direction * ai_speed)


# Close the screen once the game has ended and the screen is clicked
# This binds bye() method to mouse clicks on the Screen.
# Also enters s.mainloop() if “using_IDLE” in the configuration dictionary is False.
s.exitonclick()

# # Or s.done(). Starts the screen event loop - calling Tkinter’s mainloop function.
# # Must be the last statement in a turtle graphics program.
# s.mainloop()
