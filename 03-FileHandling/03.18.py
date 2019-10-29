a=[]
with open('C:/Users/Paweł/Desktop/pp1/03-FileHandling/numbers.txt', 'r') as file:
    x=file.read()
    x.split()
    for y in x.split():
        a.append(int(y))
    a.sort()
    for z in a:
        print(str(z)+'\n', end='') 