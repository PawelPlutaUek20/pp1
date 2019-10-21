#37
a=int(input("Podaj pierwszą liczbę: "))
b=int(input("Podaj drugą liczbę: : "))
c=int(input("Podaj trzecią liczbę: "))
if a>b:
    if a<c:
        print("Mediana wynosi: "+str(a))
    elif b>c:
        print("Mediana wynosi: "+str(b))
    else:
        print("Mediana wynosi: "+str(c))
else:
    if b<c:
        print("Mediana wynosi: "+str(b))
    elif a>c:
        print("Mediana wynosi: "+str(a))
    else:
        print("Mediana wynosi: "+str(c))
