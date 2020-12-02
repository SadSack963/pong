from turtle import Turtle


class GameOver(Turtle):

    def __init__(self):
        super(GameOver, self).__init__()
        self.hideturtle()
        self.pu()
        self.color("red")
        self.setposition(0, 0)
        self.write(f"GAME OVER!", align="center", font=("Comic Sans", 48, "italic"))
