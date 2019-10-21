#43
a=[]
x=int(input("Podaj pierwsza liczbę: "))
a.append(x)
y=int(input("Podaj druga liczbę: "))
a.append(y)
z=int(input("Podaj trzecia liczbę: "))
a.append(z)
b=sorted(a)
print("Liczby w kolejności rosnącej: {}".format(', '.join(str(a) for a in a)))
