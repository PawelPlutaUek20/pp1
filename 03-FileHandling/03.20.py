a=[]
with open('C:/Users/Paweł/Desktop/pp1/03-FileHandling/numbers.txt', 'r') as file:
    for num in file:
        if int(num)%2==0:
            a.append(num)
with open('C:/Users/Paweł/Desktop/pp1/03-FileHandling/evennumbers.txt', 'w') as evenfile:
    for a in a:
        evenfile.write(a)