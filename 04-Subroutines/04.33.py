def fib(n):
    a,b = 0,1
    for i in range(n-1):
        a,b = b,a+b
    return a
n=20
fibonacci=[]
while n>0:
    fibonacci.append(int(fib(n)))
    n-=1
print(*fibonacci[::-1], sep=', ')