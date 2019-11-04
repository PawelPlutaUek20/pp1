import random
a=[]
def rzucKostka():
    print('Wyrzucone oczka:', end=' ')
    for i in range(3):
        x=random.randint(1,6)
        a.append(x)
        print(x, end=' ')
    print('\n',end='')
    print('Suma oczek:', end=' ')
    print(sum(a))
rzucKostka()
