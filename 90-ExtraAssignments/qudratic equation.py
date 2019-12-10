a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

delta = b ** 2 - 4 * a * c

if a>0:
    if b>0:
        if c==0:
            print(0, -b/a)
        else:
            if delta>0:
                print((-b+sqrt(delta))/2*a,(-b-sqrt(delta))/2*a)
            if delta == 0:
                print(-b/2a)
            else:
                print("nie ma pierwiastkow")
    if b==0:
        if c==0:
            print(0)
        elif c>0:
            print("nie ma pierwiastkow")
        else:
            print( )
            
        
else:
    print("to nie jest rownanie kwadratowe")