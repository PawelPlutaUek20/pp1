#25
x = int(input("Podaj nr rachunku bankowego: "))
print(str(x)[:2] + " " + ' '.join(str(x)[i:i+4] for i in range(2, 26, 4)))