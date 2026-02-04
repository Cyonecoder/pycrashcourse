from random import randint


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        """rolling the dice"""
        print(randint(1, self.sides))
