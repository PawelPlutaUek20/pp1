#35
print("Podaj wartosci a,b,c funkcji kwadratowej ax²+bx+c: ")
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
Δ=b**2-4*a*c
x1=(-b+(Δ**(1/2)))/(2*a)
x2=(-b-(Δ**(1/2)))/(2*a)
if x1== x2:
    print("Pierwiastek rownania kwadratowego to: "+str(x1))
else:
    print("Pierwisatki rownania kwadratowego to: "+str(x1)+", "+str(x2))
