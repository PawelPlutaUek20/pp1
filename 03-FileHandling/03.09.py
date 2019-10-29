i=1
with open('C:/Users/Paweł/Desktop/pp1/03-FileHandling/NoEducation.txt','r') as file:
    for line in file:
        if i>2:          
            print(i-2, line, end='')
            i+=1
        else:
            print(line, end='')
            i+=1