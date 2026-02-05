from dice import Dice
import random
import string

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

ticket = "z"
x = True
counter = 0
while x:
    t = tuple(
        tuple(k for k in range(1, 11)) | tuple(random.sample(string.ascii_letters, 4))
    )
    print(t)

    e1 = random.sample(t, 4)
    print(f"Any element corresponding to {", ".join(map(str,e1))} wins")
    counter += 1
    if ticket in t:
        print(f"it took {counter} attempts to win")
        x = False
