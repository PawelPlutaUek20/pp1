a=[]
list=[]
count=0
with open('C:/Users/Paweł/Desktop/pp1/03-FileHandling/numbersinrows.txt', 'r') as file:
    for lines in file:
        x= lines.rstrip('\n').split(',')
        a.append(x)
    b = sum(a,[])
    for y in b:
        y = int(y)
        list.append(y)
        count+=1
    print(sum(list))
    print(count)