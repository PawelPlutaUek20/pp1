import math
x = 3.7
y = 4
sqrtX = math.sqrt(x)
powXY = math.pow(x,y)
sqrtXY = math.pow(x,(1/y))
area = math.pi*math.pow(y,2)
fact = math.factorial(y)
floor = math.floor(x)

print(f'Pierwiastek kwadratowy z {x} wynosi {sqrtX}\n')
print(f'{x} do potęgi {y} wynosi {powXY}\n')
print(f'Pierwiastek {y}-tego stopnia z {x} wynosi {sqrtXY}\n')
print(f'Pole koła o promieniu {y} wynosi {area}\n')
print(f'Silnia {y} wynosi {fact}\n')
print(f'Największa możliwa liczba całkowita, mniejszą bądź równą {x} wynosi {floor}')