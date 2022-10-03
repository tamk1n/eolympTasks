from random import randint

class Dice:

    def __init__(self, sides):
        self.sides = sides

    def roll_dice(self):
        for x in range(0,10):
            side = randint(1,self.sides)
            print(side)

my_game = Dice(5)

my_game.roll_dice()
