from dice import Dice


my_dice = Dice()
print("6 sided dice ")
for d in range(10):
    my_dice.roll_dice()
my_dice10 = Dice(10)
print("10 sided dice ")

for d2 in range(10):
    my_dice10.roll_dice()
my_dice20 = Dice(20)
print("20 sided dice ")

for d3 in range(20):
    my_dice20.roll_dice()
