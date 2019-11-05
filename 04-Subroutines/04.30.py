import random
a=[]
parzyste=[]
nieparzyste=[]
print('Dla 1000 liczb losowych z przedziału <1,50>:')
def procent():
    x=random.randint(1,50)
    return x
for i in range(1000):
    a.append(int(procent()))
for j in a:
    if j%2==0:
        parzyste.append(j)
    else:
        nieparzyste.append(j)
print('Liczby parzyste: {}%'.format((len(parzyste)/10)))
print('Liczby nieparzyste: {}%'.format((len(nieparzyste)/10)))
procent()