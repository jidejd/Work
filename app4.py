import random


members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second


lucky = Dice()
print(lucky.roll())

