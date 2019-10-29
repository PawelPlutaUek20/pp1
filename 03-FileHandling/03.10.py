with open('C:/Users/Paweł/Desktop/pp1/03-FileHandling/numbers.txt','r') as file:
    x=file.read()
    x.split()
    nums=[]
    for y in x.split():
        nums.append(int(y))
    print(sum(nums))