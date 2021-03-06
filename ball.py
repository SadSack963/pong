from turtle import Turtle
from random import randint, choice
import CONSTANTS as C


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.pu()
        self.shape("square")
        self.color("white")
        self.setposition(0, 0)
        self.speed("slow")
        self.setheading(choice([-45, 45, 135, -135]))  # + randint(-10, 10))
        self.speed_multiplier = C.INIT_SPEED_MULTIPLIER

    def move(self):
        # Move ball a fixed distance
        self.fd(C.BALL_SPEED)
        self.detect_wall()

    def detect_bat(self, bat_position):
        # Detect collision with bat
        # If the ball x coordinate is just in front of the bat
        #   and the ball is within 55 of the bat position
        #   then there is a collision.
        # Make the ball bounce.
        if (((self.xcor() <= -C.HALF_WIDTH + 70) and
             (90 < self.heading() < 270)) or
            ((self.xcor() >= C.HALF_WIDTH - 70) and
             (self.heading() < 90 or self.heading() > 270))) and \
                (self.distance(bat_position) < 45):
            self.setheading(180 - self.heading())
            self.speed_multiplier *= 0.95

    def detect_wall(self):
        # Detect collision with wall and reflect the heading
        if self.ycor() >= C.HALF_HEIGHT - 20\
                or self.ycor() <= -C.HALF_HEIGHT + 20:
            self.setheading(-self.heading())

    def detect_edge(self):
        # Detect when ball passes left/right edge of screen
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

    def new_position(self):
        self.setposition(0, randint(int(-C.HALF_HEIGHT * 3 / 4), int(C.HALF_HEIGHT * 3 / 4)))
        self.speed_multiplier = C.INIT_SPEED_MULTIPLIER
