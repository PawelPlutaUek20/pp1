import math
class Point():
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'P({self.x},{self.y})'
    def __eq__(self, other):
        if isinstance(other, Point):
            if other.x == self.x and other.y == self.y:
                print("odległość pomiędzy nimi wynosi 0")
            else:
                print(f"odległość pomiędzy nimi wynosi {math.sqrt((other.x-self.x)**2+(other.y-self.y)**2)}")