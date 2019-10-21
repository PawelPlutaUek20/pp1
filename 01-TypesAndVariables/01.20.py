#20
import math
pi = math.pi
r = float(input("Podaj promien kola: "))
P = pi*r**2
Obw = 2*pi*r
print("Pole koła o promieniu {} wynosi {:.2f}".format(r,P))
print("Obwód koła o promieniu {} wynosi {:.2f}".format(r,Obw))