tablica=[15,38,7,23,14]
def wystepuje(liczba,tablica):
    n=0
    print('Liczba:',liczba)
    print('Tablica:',end=' ')
    print(*tablica, sep=' ')
    while n<len(tablica)-1:
        for i in tablica:
            if i == tablica[n]:
                print('jest')
                n+=1
                break
            elif i != tablica[n]:
                n+=1
    else:
        print('nie ma')
liczba=int(input('Podaj liczbe: '))
wystepuje(liczba,tablica)