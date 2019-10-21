#48
for i in range(0,7):
    for j in range(1,44,7):
        if i+j<10:
            print(" {}".format(i+j), end=' ')
        else:
            print("{}".format(i+j), end=' ')
    print()
