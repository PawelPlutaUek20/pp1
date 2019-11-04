def potega(x,n):
    if n==0:
        return 1
    if n>0:
        return x * x**(n-1)
print(potega(5,3))