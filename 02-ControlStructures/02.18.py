#18
for i in range(1,31):
    if i%3==0 and i%5==0:
        i = "BINGO"
    elif i%3==0:
        i = "THREE"
    elif i%5==0:
        i = "FIVE"
    print(i, end = ' ')