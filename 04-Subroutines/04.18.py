def silnia(n):
    #0!=1 oraz 1!=1
    if n==0 or n==1:
        return 1
    #n! = n * (n-1)!
    if n > 1:
        return n * silnia(n-1)

print(f'5! = {silnia(5)}')