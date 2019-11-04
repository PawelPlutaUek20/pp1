def suma(N):
    if N==0:
        return 0
    if N>0:
        return N + suma(N-1)
print(suma(500))
    