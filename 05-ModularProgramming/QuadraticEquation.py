# odczytaj współczynniki z klawiatury, zwraca tablicę współczynników
def czytajWspolczynniki():
    a=float(input('Podaj liczbe wspolczynnika a: '))
    if a == int(a):
        a=int(a)
    b=float(input('Podaj liczbe wspolczynnika b: '))
    if b == int(b):
        b=int(b)
    c=float(input('Podaj liczbe wspolczynnika c: '))
    if c == int(c):
        c=int(c)
    return [a,b,c]

# oblicz deltę
def obliczDelte(wspolczynniki: list):
    a = wspolczynniki[0]
    b = wspolczynniki[1]
    c = wspolczynniki[2]
    return b**2-4*a*c

# wyznacz pierwiastki równania - zwraca tablicę pierwiastków
# (jeden lub dwa elementy) lub pustą tablicę, jeśli delta < 0
def obliczPierwiastki(wspolczynniki: list, delta: float):
    a = wspolczynniki[0]
    b = wspolczynniki[1]
    c = wspolczynniki[2]
    
    if delta>0:
        x1 = (-b-(delta)**(1/2))/(2*a)
        x2 = (-b+(delta)**(1/2))/(2*a)
        if x1 == int(x1):
            x1=int(x1)
        if x2 == int(x2):
            x2=int(x2)
        return [x1,x2]
    elif delta==0:
        x0 = (-b)/(2*a)
        if x0==int(x0):
            x0=int(x0)
        return [x0]
    else:
        return []

# wyświetl wyznaczone pierwiastki równania kwadratowego
def wyswietlPierwiastki(wspolczynniki:list,pierwiastki: list):
    a = wspolczynniki[0]
    b = wspolczynniki[1]
    c = wspolczynniki[2]
    print('Równanie kwadratowe postaci:',end=' ')
    if b>0:
        b=f'+{b}'
    elif b==0:
        b=''
    if c>0:
        c=f'+{c}'
    elif c==0:
        c=''   
    if a==1:
        print(f'x²{b}x{c}=0')
    else:
        print(f'{a}x²{b}x{c}=0')
    if len(pierwiastki)==2:
        print(f'Pierwiastki równania: x₁={pierwiastki[0]}, x₂={pierwiastki[1]}')
    elif len(pierwiastki)==1:
        print(f'Pierwiastek równania: x₀={pierwiastki[0]}')
    elif len(pierwiastki)==0:
        print(f'Równanie nie ma pierwiastków')
