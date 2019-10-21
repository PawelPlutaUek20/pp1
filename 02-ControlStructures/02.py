#x = 10
#y = 23
#if x>y:
#    print(x, "jest większe od",y)
#elif x==y:
#    print(x, "jest rowne",y)
#else:
#    print(y, "jest większe od",x)

#x= int(input("Podaj liczbe calkowitą: "))
#if x%2!=0 and x>0:
#    print(x, "jest zarówno dodatnia, jak i nieparzysta.")
#else:
#    print(x, "albo nie jest dodatnia albo jest parzysta")

#Zadanie 14
#wiek_psa=int(input("Podaj wiek psa w ludzkich latach: "))
#if wiek_psa<=2:
#    print("Wiek psa w psich latach to", wiek_psa*10.5, "lata")
#elif wiek_psa>2:
#    print("Wiek psa w psich latach to", 21+(wiek_psa-2)*4, "lata")

#Zadanie 13
#x=5
#y=2
#if x>0 and y>0:
#    print("Punkt P("+str(x)+","+str(y)+") znajduje się w pierwszej ćwiartce układu współrzędnych")
#elif x<0 and y>0:
#    print("Punkt P("+str(x)+","+str(y)+") znajduje się w drugiej ćwiartce układu współrzędnych")
#elif x<0 and y<0:
#    print("Punkt P("+str(x)+","+str(y)+") znajduje się w trzeciej ćwiartce układu współrzędnych")
#elif x>0 and y<0:
#    print("Punkt P("+str(x)+","+str(y)+") znajduje się w czwartej ćwiartce układu współrzędnych")
#elif x==0 and y!=0:
#    print("Punkt P("+str(x)+","+str(y)+") znajduje się na osi OY")
#elif y==0 and x!=0:
#    print("Punkt P("+str(x)+","+str(y)+") znajduje się na osi OX")
#else:
#    print("Punkt P("+str(x)+","+str(y)+") znajduje się on w początku układu współrzędnych")

#Zadanie 15
#x=int(input("Podaj liczbe: "))
#for i in range(1,11):
#    print(x, "x", i, "=", x*i)

#Zadanie 22
#x=[15,8,31,47,2,19]
#y=[]
#for i in x:
#    if i%2!=0:
#        y.append(i)
#print("średnią arytmetyczną wszystkich liczb nieparzystych wynosi:",sum(y)/len(y))