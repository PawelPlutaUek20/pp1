#40
import random
n=0
six=[]
five=[]
four=[]
three=[]
two=[]
one=[]
while n<100:
    x = random.randint(1,6)
    if x==1:
        one.append(x)
    elif x==2:
        two.append(x)
    elif x==3:
        three.append(x)
    elif x==4:
        four.append(x)
    elif x==5:
        five.append(x)
    elif x==6:
        six.append(x)
    n+=1
print("Jedynka: "+str(len(one)))
print("Dwójka: "+str(len(two)))
print("Trójka: "+str(len(three)))   
print("Czwórka: "+str(len(four)))
print("Piątka: "+str(len(five)))
print("Szóstka: "+str(len(six)))
