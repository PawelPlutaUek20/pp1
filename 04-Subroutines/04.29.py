tab=[2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]
tab.sort()
def mediana():
    if len(tab)%2==0:
        print((tab[(len(tab)//2)-1]+tab[(len(tab)//2)])/2)
    else:
        print(tab[(len(tab)//2)])
        
def dominanta(tab):
    return max(tab, key=tab.count)
    
print('Mediana:',end=' ')
mediana()
print('Dominanta:', end=' ')
print(dominanta(tab))