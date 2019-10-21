#41
n=[]
while 1:
    x = int(input("Podaj liczbe: "))
    if x==0:
        break
    n.append(x)
print("REZULTAT: Liczb={}, Suma={}, Średnia={}".format(len(n),sum(n),sum(n)/len(n)))
