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
        # Move ball a fixed distance
        self.fd(C.BALL_SPEED)
        self.detect_wall()

    def detect_bat(self):
        # TODO Detect collision with bat
        pass

    def detect_wall(self):
        # Detect collision with wall and reflect the heading
        if self.ycor() >= C.HALF_HEIGHT\
                or self.ycor() <= -C.HALF_HEIGHT:
            self.setheading(-self.heading())
        # TEMPORARY - Confine ball to screen
        if self.xcor() >= C.HALF_WIDTH\
                or self.xcor() <= -C.HALF_WIDTH:
            self.setheading(180-self.heading())

    def detect_edge(self):
        # TODO Detect when ball passes left/right edge of screen
        """Return 0 if ball still in play
        Return 1 if Player wins the point
        Return 2 if AI wins the point"""
        if self.xcor() >= C.HALF_WIDTH:
            # Player wins - increase player score
            return 1
        elif self.xcor() <= -C.HALF_WIDTH:
            # AI wins - increase AI score
            return 2
        else:
            return 0