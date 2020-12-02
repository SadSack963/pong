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
        self.speed("slow")
        self.setheading(choice([-45, 45]) + randint(-10, 10))

    def move(self):
        # Move ball
        self.fd(C.BALL_SPEED)
        self.detect_wall()

    def detect_bat(self):
        # TODO Detect collision with bat
        pass

    def detect_wall(self):
        # Detect collision with wall
        if self.ycor() >= C.HALF_HEIGHT\
                or self.ycor() <= -C.HALF_HEIGHT:
            self.setheading(-self.heading())

    def detect_edge(self):
        # TODO Detect when ball passes left/right edge of screen
        pass
