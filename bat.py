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

    def move(self, distance):
        """Up: positive distance, Down: negative distance"""
        self.fd(distance)

    def detect_ball(self):
        # TODO Detect collision with ball - probably not required ?
        pass

    def detect_wall(self):
        # TODO Detect collision with wall - Stop moving
        pass
