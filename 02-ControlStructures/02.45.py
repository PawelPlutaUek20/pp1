#45
n = int(input("Podaj liczbe n poczatkowych liczb pierwszych: "))
tab=[2]
x=2
y=0
while len(tab)<n:
    while x%tab[y]!=0 or x==3:
        if y==len(tab)-1 or x==3:
            tab.append(x)
            x+=1
            y=0
        else:
            y+=1
    else:
        x+=1
        y=0
print("Lista pierwszych " +str(n)+ " liczb pierwszych: ", end='')
print( *tab, sep=", ", end="")