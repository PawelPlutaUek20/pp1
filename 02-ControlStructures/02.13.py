#13
x = float(input("Podaj wartosc wspolrzednej x: "))
y = float(input("Podaj wartosc wspolrzednej y: "))
if x>0 and y>0:
    print("punkt P({},{}) znajduje sie w pierwszej cwiartce ukladu".format(x,y))
elif x<0 and y>0:
    print("punkt P({},{}) znajduje sie w drugiej cwiartce ukladu".format(x,y))
elif  x<0 and y<0:
    print("punkt P({},{}) znajduje sie w trzeciej cwiartce ukladu".format(x,y))
elif x>0 and y<0:
    print("punkt P({},{}) znajduje sie w czwartej cwiartce ukladu".format(x,y))
elif x==0 and y != 0:
    print("punkt P({},{}) znajduje sie na osi OY".format(x,y))
elif y==0 and x != 0:
    print("punkt P({},{}) znajduje sie na osi OX".format(x,y))
else:
    print("punkt P({},{}) znajduje sie na poczatku ukladu wspolrzednych".format(x,y))