from turtle import Turtle

# Extended ASCII code 178 = ▓
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


# Extended ASCII code 219 = █
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
        # TODO Try drawing block font with turtle?
        #  Or find and embed appropriate font (how? ASCII Art?),
        #  or using picture of numbers?
        self.write(f"{self.score}", align="center", font=("Arial", 50, "normal"))
