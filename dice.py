from random import randint

class Dice:

    def _init__(self, sides):
        self.sides = sides
        sides = 6

    def roll_dice(self):
        for x in range(0,6):
            side = randint(1,6)
            print(side)

my_game = Dice()

my_game.roll_dice()
