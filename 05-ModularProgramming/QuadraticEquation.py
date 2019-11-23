# odczytaj współczynniki z klawiatury, zwraca tablicę współczynników
def czytajWspolczynniki():
    global a,b,c
    a=float(input('Podaj liczbe wspolczynnika a: '))
    if a == int(a):
        a=int(a)
    b=float(input('Podaj liczbe wspolczynnika b: '))
    if b == int(b):
        b=int(b)
    c=float(input('Podaj liczbe wspolczynnika c: '))
    if c == int(c):
        c=int(c)
    wspolczynniki = [a,b,c]
    return wspolczynniki

# oblicz deltę
def obliczDelte():
    global delta
    a,b,c=czytajWspolczynniki()
    delta = b**2-4*a*c
    return delta

# wyznacz pierwiastki równania - zwraca tablicę pierwiastków
# (jeden lub dwa elementy) lub pustą tablicę, jeśli delta < 0
def obliczPierwiastki():
    global x1, x2, x0, pierwiastki
    obliczDelte()
    if delta>0:
        x1 = (-b-(delta)**(1/2))/(2*a)
        x2 = (-b+(delta)**(1/2))/(2*a)
        if x1 == int(x1):
            x1=int(x1)
        if x2 == int(x2):
            x2=int(x2)
        pierwiastki = [x1,x2]
        return pierwiastki
    elif delta==0:
        x0 = (-b)/(2*a)
        if x0==int(x0):
            x0=int(x0)
        pierwiastki = [x0]
        return pierwiastki
    else:
        pierwiastki=[]
        return pierwiastki

# wyświetl wyznaczone pierwiastki równania kwadratowego
def wyswietlPierwiastki():
    miejscaZerowe=[]
    for i in obliczPierwiastki():
        miejscaZerowe.append(i)
    print(miejscaZerowe)
obliczPierwiastki()