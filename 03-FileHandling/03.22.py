a=[]
i=1
with open('C:/Users/Paweł/Desktop/pp1/03-FileHandling/students.txt', 'r') as file:
    for line in file:
        x= line.rstrip('\n').split(',')
        a.append(x)
    while i<len(a):
        if int(a[i][2])<30:
            print("%-7s %-8s %s" %(a[i][0], a[i][1], a[i][4]))              
            i+=1
        elif int(a[i][2])>30:
            i+=1
