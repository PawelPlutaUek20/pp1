tablica=[4,3,7,1,3]
def suma(tablica):
    print('Tablica:',end=' ')
    print(*tablica, sep=' ')
    print('Suma wartości:', end=' ')
    print(sum(tablica))
suma(tablica)
    