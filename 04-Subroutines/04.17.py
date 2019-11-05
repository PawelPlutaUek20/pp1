import random
def rzucKostka():
    x = random.randint(1,6)
    return x
a=[]
print('Wyrzucone oczka:', end=' ')
for i in range(3):
    a.append(int(rzucKostka()))
print(*a, sep=' ')
print('Suma oczek:', end=' ')
print(sum(a))


