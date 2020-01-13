import random
def rzut_kostka():
    dice = random.randint(1,6)
    assert type(dice) == int and dice in range(1,7)
    return dice
print(rzut_kostka())