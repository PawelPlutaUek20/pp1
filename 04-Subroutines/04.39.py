def zmiesci_sie(n,x,y):
    if n>=x and n<=y:
        return n
x,y=0,100
n=int(input('Podaj liczbe: '))
print('Liczba',zmiesci_sie(n,x,y),'mieści się w zakresie <%d,%d>'%(x,y))