#50
x = int(input("Podaj liczbe dziesietna: "))
y = []
while x != 1:
    if x%2==0:
        y.append(0)
        x = x//2
    else:
        y.append(1)
        x = x//2
y.append(1)
print(*y[::-1], sep='',end='(2)')
