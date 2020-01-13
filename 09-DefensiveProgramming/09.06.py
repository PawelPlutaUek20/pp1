a = 5
assert type(a) == int, "Wartość b nie jest liczbą całkowitą"
b = 3
assert type(b) == int, "Wartość b nie jest liczbą całkowitą"
assert b!=0, 'Wartość b równa 0!'
print(f'{a}/{b} = {a/b}')