#39
a,b = 0,1
print(a, end=', ')
n=0
while n<50:
    a,b = b,(a+b)
    print(a, end=", ")
    n+=1
