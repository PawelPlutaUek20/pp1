#22
x=[15,8,31,47,2,19]
y=[]
for i in x:
    if i%2!=0:
        y.append(i)
print("srednia arytmetyczna liczb nieparzystych wynosi:", sum(y)/len(y))