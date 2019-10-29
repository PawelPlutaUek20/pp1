import re
a=[]
with open('C:/Users/Paweł/Desktop/pp1/03-FileHandling/land.txt', 'r') as file:
    for lines in file:
        x=re.findall("\d",lines)
    for num in x:
        num = int(num)
        a.append(num)
    print(sum(a))
    