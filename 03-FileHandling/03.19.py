a=[]
with open('C:/Users/Paweł/Desktop/pp1/03-FileHandling/universities.txt', 'r') as file:
    for line in file:
        a.append(line)
    a.sort()       
with open('C:/Users/Paweł/Desktop/pp1/03-FileHandling/universities.txt', 'w') as abcfile:
    for a in a:
        abcfile.write(a)