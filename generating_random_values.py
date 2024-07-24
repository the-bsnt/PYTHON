import random

for i in range(3):
    print(random.random())
    print(random.randint(20, 40))

members = ["hari", "dipesh", "prabesh", "mazil"]
for i in range(4):
    print(random.choice(members))


def roll_the_dice():
    print(random.randint(0, 6))


for i in range(6):
    roll_the_dice()
