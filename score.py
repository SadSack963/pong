from turtle import Turtle


class Score(Turtle):
    def __init__(self, position):
        super(Score, self).__init__()  # Call the Turtle initializer
        self.hideturtle()
        self.pu()
        self.color("white")
        self.setposition(position)
        self.score = -1
        self.update()

    def update(self):
        self.score += 1
        self.clear()
        # TODO Try drawing block font with turtle? - or using picture of numbers?
        self.write(f"{self.score}", align="center", font=("Arial", 50, "normal"))

