from turtle import Turtle

# Extended ASCII code 178 = ▓ The blocks are dithered
digits_178 = [
    '''
    ▓▓▓
    ▓ ▓
    ▓ ▓
    ▓ ▓
    ▓▓▓
    ''',
    '''
     ▓
    ▓▓
     ▓
     ▓
    ▓▓▓
    ''',
    '''
     ▓ 
    ▓ ▓
      ▓
     ▓ 
    ▓▓▓
    ''',
    '''
    ▓▓▓
      ▓
    ▓▓▓
      ▓
    ▓▓▓
    ''',
    '''
    ▓ ▓
    ▓ ▓
    ▓▓▓
      ▓
      ▓
    ''',
    '''
    ▓▓▓
    ▓
    ▓▓▓
      ▓
    ▓▓▓
    ''',
    '''
    ▓▓▓
    ▓  
    ▓▓▓
    ▓ ▓
    ▓▓▓
    ''',
    '''
    ▓▓▓
      ▓
      ▓
      ▓
      ▓
    ''',
    '''
    ▓▓▓
    ▓ ▓
    ▓▓▓
    ▓ ▓
    ▓▓▓
    ''',
    '''
    ▓▓▓
    ▓ ▓
    ▓▓▓
      ▓
      ▓
    ''',
]


# Extended ASCII code 219 = █ The blocks are solid
digits_219 = [
    '''
    ███
    █ █
    █ █
    █ █
    ███
    ''',
    '''
     █
    ██
     █
     █
    ███
    ''',
    '''
     █ 
    █ █
      █
     █ 
    ███
    ''',
    '''
    ███
      █
    ███
      █
    ███
    ''',
    '''
    █ █
    █ █
    ███
      █
      █
    ''',
    '''
    ███
    █
    ███
      █
    ███
    ''',
    '''
    ███
    █  
    ███
    █ █
    ███
    ''',
    '''
    ███
      █
      █
      █
      █
    ''',
    '''
    ███
    █ █
    ███
    █ █
    ███
    ''',
    '''
    ███
    █ █
    ███
      █
      █
    ''',
]


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

        # Using normal font...
        # self.write(f"{self.score}", align="center", font=("Arial", 50, "normal"))

        # Using ASCII ART...
        self.write(digits_219[self.score], align="center", font=("Courier New", 8, "normal"))
