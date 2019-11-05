tab=[1,2,3,4,5,6,7,8]
parzysta = filter(lambda x : x%2==0, tab)
print('Liczby parzyste: ', end='')
print(*list(parzysta), sep=', ')