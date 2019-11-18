import math
x = 3.7
y = 4
sqrtX = f'%.2f'%math.sqrt(x)
powXY = f'%.2f'%math.pow(x,y)
sqrtYX = f'%.2f'%math.pow(x,(1/y))
poleY = f'%.2f'%(math.pi*y**2)
factorialY = math.factorial(y)
floorX = math.floor(x)

print(f'Pierwiastek kwadratowy z {x} wynosi {sqrtX}')
print(f'{x} do potegi {y} wynosi {powXY}')
print(f'Pierwiastek {y}-tego stopnia z {x} wynosi {sqrtYX}')
print(f'Pole koła o promieniu {y} wynosi {poleY}')
print(f'Silnia {y} wynosi {factorialY}')
print(f'Największą możliwą liczbę całkowitą, mniejszą bądź równą {x} wynosi {floorX}')