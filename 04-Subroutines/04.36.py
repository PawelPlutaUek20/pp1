tab = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]
def Sum(tab):
    if isinstance(tab, int):
        return tab
    
    sum = 0
    for i in range(len(tab)):
        sum += Sum(tab[i])
    return sum
print(Sum(tab))