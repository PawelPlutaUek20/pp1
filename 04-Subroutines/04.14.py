tablica=[15,38,7,23,14]
def wystepuje(liczba,tablica):
    n=0
    print('Liczba:',liczba)
    print('Tablica:',end=' ')
    print(*tablica, sep=' ')
    for i in tablica:
        if i==liczba:
            print('Rezultat: Podana liczba występuje w tablicy')
            break
    else:
        print('Rezultat: Podana liczba nie występuje w tablicy')
liczba=23
wystepuje(liczba,tablica)
