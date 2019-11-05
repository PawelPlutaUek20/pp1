def sumacyfr(x):
    sum=0
    for i in str(x):
        sum += int(i)
    return sum
suma=0
x=int(input('Podaj liczbe: '))
for i in range(len(str(x))):
    suma+=int(str(x)[i])
if suma==sumacyfr(x):
    print(suma)

