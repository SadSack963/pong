from turtle import Turtle
from random import randint, random, choice
import CONSTANTS as C


class Bat(Turtle):
    def __init__(self, position):
        super(Bat, self).__init__()
        self.pu()
        self.setheading(C.UP)
        self.shape("square")
        self.resizemode("user")
        self.shapesize(stretch_len=4)
        self.color("white")
        self.setposition(position)
        self.speed(4)
        self.stop_moving = False

    def move(self, distance):
        """Up: positive distance, Down: negative distance"""
        # First move the bat
        if not self.stop_moving:
            self.fd(distance)
        # Then detect (near) collision with top or bottom of screen
        self.detect_wall()

    def detect_wall(self):
        # Detect collision with wall - Stop moving the bat
        if self.ycor() >= C.HALF_HEIGHT - C.BAT_OFFSET \
                or self.ycor() <= -C.HALF_HEIGHT + C.BAT_OFFSET :
            self.stop_moving = True
