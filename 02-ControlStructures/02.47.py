#47
x = int(input("Podaj kwote w zl: "))
if x//5>0:    
    print("5 zl - " + str(x//5)+ "szt")
if x%5//2>0:
    print("2 zl - " + str(x%5//2)+ "szt")
if x%5%2//1>0:
    print("1 zl - " + str(x%5%2//1)+ "szt")