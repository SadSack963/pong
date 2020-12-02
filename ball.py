from turtle import Turtle
from random import randint, choice
import CONSTANTS as C


class Ball(Turtle):
    def __init__(self, position):
        super(Ball, self).__init__()
        self.pu()
        self.shape("square")
        self.color("white")
        self.setposition(position)
        self.speed(3)
        self.setheading(choice([-45, 45]) + randint(-10, 10))

    def move(self):
        # TODO Move ball
        self.fd(20)

        pass

    def detect_bat(self):
        # TODO Detect collision with bat
        pass

    def detect_wall(self):
        # TODO Detect collision with wall
        pass

    def detect_edge(self):
        # TODO Detect when ball passes left/right edge of screen
        pass
