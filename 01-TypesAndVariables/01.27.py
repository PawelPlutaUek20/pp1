#27
import math
x = int(input("Podaj liczbe naturalna: "))
y = int(input("Podaj druga liczbe naturalna: "))
z = math.gcd(x,y)
print("największy wspólny podzielnik liczb {} i {} jest liczba {}".format(x,y,z))