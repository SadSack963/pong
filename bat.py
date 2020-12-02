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

    def move_up(self):
        # TODO Move bat
        self.fd(5)
        s.ontimer(self.move_up, C.REPEAT_RATE)

    def move_down(self):
        # TODO Move bat
        self.bk(20)

    def detect_bat(self):
        # TODO Detect collision with ball ?
        pass

    def detect_wall(self):
        # TODO Detect collision with wall - Stop moving
        pass
