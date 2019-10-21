#33
x = ["zero", "jeden", "dwa", "trzy", "cztery", "piec", "szesc", "siedem", "osiem", "dziewiec", "dziesiec"]
n = int(input("Podaj liczbe naturanla: "))
l = 0
while l<len(str(n)):
    if l==0:
        print(str(n)+" - ", end='')
    print(x[int(str(n)[l])], end=" ")
    l+=1
