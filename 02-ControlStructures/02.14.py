#14
x = float(input("Podaj wiek psa w ludzkich latach: "))
if x>0 and x<= 2:
    y=x*10.5
if x>2:
    y=21+(x-2)*4
print("Wiek psa w psich latach to {:.0f} lata".format(y))