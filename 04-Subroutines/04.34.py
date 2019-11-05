fib_n=[]
def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=20
while n>0:
    fib_n.append(fib(n))
    n-=1
print(*fib_n[::-1], sep=', ')