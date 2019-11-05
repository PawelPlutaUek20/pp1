tablica=[4,3,7,1,3]
def suma(tablica):
    sum=0
    print('Tablica:',end=' ')
    print(*tablica, sep=' ')
    for i in tablica:
        sum+=i
    return sum
print('Suma wartosci:',suma(tablica))