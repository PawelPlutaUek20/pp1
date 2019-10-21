#49
nrDniaTygodnia = 2
print("| PN | WT | SR | CZ | PT | SB | ND |")
for i in range(0,40,7):
    for j in range(1,8):
        if int(i+j-nrDniaTygodnia)<=0:
            print("|    ",end='')
        else:
            if int(i+j-nrDniaTygodnia)<10:
                print("|  {}".format(i+j-nrDniaTygodnia), end=' ')
                if j == 7:
                    print("|", end='')
            elif int(i+j-nrDniaTygodnia)<31:
                print("| {}".format(i+j-nrDniaTygodnia), end=' ')
                if j == 7:
                    print("|", end='')
                elif int(i+j-nrDniaTygodnia)==30:
                    print("|", end='')
            elif int(i+j)<36:
                print("    |", end='')
            elif nrDniaTygodnia == 6:
                print("    |",end='')
    print()
